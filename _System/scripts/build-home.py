#!/usr/bin/env python3
"""
build-home.py — Mentoring Hub homepage generator

Run from anywhere:
    python3 _System/scripts/build-home.py          (one build)
    python3 _System/scripts/build-home.py --watch  (keep rebuilding on any change)

Reads
  - Programs  : <WEBSITE>/src/pages/training/programs/*.sessions.js + *.jsx   (live program pages)
  - Lessons   : Library/lessons/**/<topic>-lesson.md                          (+ EXTRA_LESSONS below)
  - Mentees   : <MENTEES>/<name>/plan|sessions|assessments                    (public: card + detail page)
  - Design    : <WEBSITE>/design-system/css + fonts  (copied, so the output is standalone)

Writes (all static, relative links, open index.html straight from disk)
  Homepage/index.html
  Homepage/programs/<program>.html
  Homepage/lessons/<lesson>.html
  Homepage/assets/css|fonts|lesson-assets

Edit the CONFIG block to change paths, lesson↔program mapping or lesson titles.
"""

import html
import json
import time
import os
import re
import shutil
import sys
from pathlib import Path
from urllib.parse import quote, unquote

import markdown

# ─────────────────────────────────────────────────────────────────────────────
# CONFIG
# ─────────────────────────────────────────────────────────────────────────────

ROOT = Path(__file__).resolve().parent.parent.parent  # 03_Mentoring (this file lives in _System/scripts/)
OUT = Path(os.environ.get("HOME_OUT", ROOT / "Homepage"))

GDRIVE = Path("/Users/winnie.nguyen/Library/CloudStorage/GoogleDrive-nguyenphuctuongvan@gmail.com/My Drive")
WEBSITE = Path(os.environ.get("WEBSITE_DIR", GDRIVE / "02_Personal/01_Personal Website"))
MENTEES = Path(os.environ.get("MENTEES_DIR", GDRIVE / "03_Mentoring/Mentees"))
if not MENTEES.exists():
    MENTEES = ROOT / "Mentees"

DESIGN_SYSTEM = WEBSITE / "design-system"
PROGRAMS_SRC = WEBSITE / "src/pages/training/programs"
LESSONS_DIR = Path(os.environ.get("LESSONS_DIR", GDRIVE / "03_Mentoring/Library/lessons"))
if not LESSONS_DIR.exists():
    LESSONS_DIR = ROOT / "Library/lessons"

# Optional: base URL of the live website, so program pages get an "Open live page" link.
SITE_BASE = os.environ.get("SITE_BASE", "").rstrip("/")

# Stage folder -> label (anything not listed is labelled from its folder name)
STAGES = {
    "00-foundation": "Foundation",
    "01-discover": "Discover",
    "02-define": "Define",
    "03-develop": "Develop",
    "04-deliver": "Deliver",
    "leader-level": "Leader level",
}

# Which program sessions a lesson belongs to is written IN THE LESSON, in its front matter:
#     programs: [ui-ux-fundamentals:01, junior-to-mid-level:01]
# Older-style lessons (no front matter) use a header line instead:   **Programs:** ui-ux-fundamentals:05, junior-to-mid-level:05
# This table is only a fallback for folders that have no lesson file yet, so there is nothing to carry the line.
LESSON_PROGRAMS = {
    "systematic-ai-prototyping": [("systematic-ai-prototyping", "01"), ("systematic-ai-prototyping", "02"),
                                  ("systematic-ai-prototyping", "03"), ("systematic-ai-prototyping", "04")],
}

# Programs: display order + a short tag. Anything not listed is appended.
PROGRAM_ORDER = ["ui-ux-fundamentals", "junior-to-mid-level", "mid-to-senior", "systematic-ai-prototyping"]
PROGRAM_TAG = {
    "ui-ux-fundamentals": "Course",
    "junior-to-mid-level": "Roadmap",
    "mid-to-senior": "Roadmap",
    "systematic-ai-prototyping": "Short course",
}

# ─────────────────────────────────────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────────────────────────────────────

esc = html.escape


def slugify(s):
    s = re.sub(r"<[^>]+>", "", s.lower())
    s = re.sub(r"[^\w]+", "-", s, flags=re.UNICODE).strip("-")
    return s or "section"


def parse_front_matter(raw):
    m = re.match(r"^---\n(.*?)\n---\n?", raw, re.S)
    if not m:
        return {}, raw
    meta = {}
    for line in m.group(1).split("\n"):
        kv = re.match(r"^([\w-]+):\s*(.*)$", line)
        if not kv:
            continue
        v = re.sub(r"\s+#.*$", "", kv.group(2).strip())  # trailing yaml comment
        if v.startswith("[") and v.endswith("]"):
            v = [x.strip().strip('"') for x in v[1:-1].split(",") if x.strip()]
        else:
            v = v.strip('"')
        meta[kv.group(1)] = v
    return meta, raw[m.end():]



def parse_inline_header(body):
    """Lessons without front matter open with '# Title', a byline and '**Key:** value' lines, then '---'."""
    m = re.match(r"^(#\s+.*?\n)(.*?)\n---\s*\n", body, re.S)
    if not m:
        return {}, body
    meta = {}
    for key, val in re.findall(r"\*\*([A-Za-z ]+):\*\*\s*([^*\n]+?)(?=\s+·\s+\*\*|\s*$)", m.group(2), re.M):
        meta[key.strip().lower()] = val.strip()
    return meta, m.group(1) + body[m.end():]


def pretty_level(v):
    return {"mixed": "All levels", "all levels": "All levels", "junior": "Junior", "senior-lead": "Senior / Lead",
            "intermediate": "Intermediate", "foundational": "Foundational"}.get(str(v).lower(), str(v).title() if v else "")


def pretty_date(v):
    m = re.match(r"(\d{4})-(\d{2})-(\d{2})", str(v or ""))
    if not m:
        return str(v or "")
    months = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()
    return f"{int(m.group(3))} {months[int(m.group(2)) - 1]} {m.group(1)}"


def chip(text, tone="default", cls=""):
    return f'<span class="chip chip--sm chip--soft chip--{tone} {cls}">{esc(str(text))}</span>'


# ─────────────────────────────────────────────────────────────────────────────
# MARKDOWN  (python-markdown needs GFM-style lists/tables normalised first)
# ─────────────────────────────────────────────────────────────────────────────

LIST_RE = re.compile(r"^(\s*)([-*+]|\d+[.)])\s+(.*)$")


def normalise_markdown(body):
    """GFM -> python-markdown: blank line before lists/tables, 4-space nesting, task boxes."""
    out, in_fence, stack, prev = [], False, [], "blank"
    for line in body.split("\n"):
        if re.match(r"^\s*```", line):
            in_fence = not in_fence
            out.append(line)
            prev = "code"
            continue
        if in_fence:
            out.append(line)
            continue
        if not line.strip():
            out.append(line)
            prev, stack = "blank", []
            continue
        m = LIST_RE.match(line)
        if m:
            indent = len(m.group(1).replace("\t", "    "))
            while stack and stack[-1] > indent:
                stack.pop()
            if not stack or stack[-1] < indent:
                stack.append(indent)
            depth = len(stack) - 1
            text = re.sub(r"^\[ \]\s*", "☐ ", m.group(3))
            text = re.sub(r"^\[[xX]\]\s*", "☑ ", text)
            if prev not in ("list", "blank"):
                out.append("")
            out.append("    " * depth + m.group(2) + " " + text)
            prev = "list"
            continue
        if prev == "list" and line.startswith((" ", "\t")):
            out.append("    " * max(len(stack), 1) + line.strip())  # continuation paragraph in an item
            continue
        is_table = line.lstrip().startswith("|")
        if is_table and prev not in ("table", "blank"):
            out.append("")
        out.append(line)
        prev = "table" if is_table else "text"
    return "\n".join(out)


def render_markdown(body, prefix=""):
    md = markdown.Markdown(
        extensions=["tables", "fenced_code", "toc", "sane_lists", "md_in_html"],
        extension_configs={"toc": {"slugify": lambda v, s: prefix + slugify(v), "toc_depth": "2"}},
    )
    out = md.convert(normalise_markdown(body))
    headings = [{"id": t["id"], "text": html.unescape(re.sub(r"<[^>]+>", "", t["name"]))} for t in md.toc_tokens]
    return out, headings


# ─────────────────────────────────────────────────────────────────────────────
# PROGRAMS
# ─────────────────────────────────────────────────────────────────────────────

CAMEL = {"ui-ux-fundamentals": "UiUxFundamentals", "junior-to-mid-level": "JuniorToMid",
         "mid-to-senior": "MidToSenior", "systematic-ai-prototyping": "SystematicAiPrototyping"}


def load_programs():
    progs = {}
    for f in sorted(PROGRAMS_SRC.glob("*.sessions.js")):
        slug = f.name.replace(".sessions.js", "")
        t = f.read_text(encoding="utf-8")
        try:
            data = json.loads(t[t.index("["): t.rindex("]") + 1])
        except ValueError as e:
            print(f"  ! skipped {f.name}: not plain JSON ({e})")
            continue
        phases, sessions, cur = [], [], None
        for x in data:
            if "phase" in x:
                cur = x["phase"]["en"]
                phases.append(cur)
            else:
                sessions.append({
                    "idx": x["idx"], "title": x["title"]["en"], "summary": x["summary"]["en"],
                    "phase": cur, "tools": [tl if isinstance(tl, str) else tl.get("en", "") for tl in x.get("tools", [])],
                })
        # page title + hero copy live in the shell html and the jsx
        title, desc, stat = slug.replace("-", " ").title(), "", ""
        shell = WEBSITE / "training/programs" / f"{slug}.html"
        if shell.exists():
            m = re.search(r"<title>(.*?)</title>", shell.read_text(encoding="utf-8"))
            if m:
                title = re.sub(r"\s+[—-]\s+Winnie Nguyen$", "", m.group(1))
        jsx = next((p for p in PROGRAMS_SRC.glob("[A-Z]*.jsx") if p.stem == CAMEL.get(slug)), None)
        if jsx:
            j = jsx.read_text(encoding="utf-8")
            m = re.search(r'hero-desc"><span className="lang-en">(.*?)</span>', j, re.S)
            if m:
                desc = re.sub(r"<[^>]+>", "", m.group(1)).replace("&apos;", "'").strip()
            m = re.search(r'hero-stat"><strong>(\d+)</strong><span><span className="lang-en">(.*?)</span>', j)
            if m:
                stat = f"{m.group(1)} {m.group(2)}".replace("Sessions · ", "sessions · ")
        progs[slug] = {"slug": slug, "title": title, "desc": desc, "stat": stat,
                       "phases": phases, "sessions": sessions}
    order = [s for s in PROGRAM_ORDER if s in progs] + [s for s in progs if s not in PROGRAM_ORDER]
    return [progs[s] for s in order]


# ─────────────────────────────────────────────────────────────────────────────
# LESSONS  (one FOLDER = one lesson; the folder's materials/, slides/ and homework feed its page)
# ─────────────────────────────────────────────────────────────────────────────

ASSETS = OUT / "assets"
IMG_EXT = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg"}
# materials/*.md that are NOT lesson plans
NOT_LESSON = re.compile(r"(slide-outline|brainstorm|build-prompt|stub|^readme|^index|^learnings)", re.I)


NON_TOPIC = {"assets", "learning", "materials", "slides"}  # helper folders, never a lesson


def visible(p):
    return not p.name.startswith((".", "_"))


def sync_file(src, dest):
    """Copy only when missing or changed, so big slide decks aren't re-copied on every rebuild."""
    try:
        if dest.exists():
            a, b = src.stat(), dest.stat()
            if a.st_size == b.st_size and abs(a.st_mtime - b.st_mtime) < 2:
                return
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dest)
    except OSError as e:
        print(f"  warn: could not copy {src.name}: {e}")


def fix_deck_links(dest):
    """Copied decks were authored for the Library layout, so their relative links to sibling guides/indexes die
    on the site. Repoint any dead relative link to the matching site page (lesson page, else the lesson library, or home)."""
    for f in dest.rglob("*.html"):
        try:
            txt = f.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue

        def repl(m):
            href = m.group(2)
            if re.match(r"^(https?:|mailto:|tel:|data:|javascript:|#|//|/)", href):
                return m.group(0)
            path = unquote(html.unescape(href.split("#")[0].split("?")[0]))
            if not path or (f.parent / path).exists():
                return m.group(0)
            stem = Path(path).stem
            if Path(path).name.lower() == "index.html":
                target = OUT / "index.html"
            elif (OUT / "lessons" / f"{stem}.html").exists():
                target = OUT / "lessons" / f"{stem}.html"
            else:
                target = OUT / "lessons.html"
            return m.group(1) + os.path.relpath(target, f.parent).replace(os.sep, "/") + m.group(3)

        new = re.sub(r'(<a\b[^>]*?\bhref=")([^"]*)(")', repl, txt)
        if new != txt:
            f.write_text(new, encoding="utf-8")


def sync_tree(src, dest):
    """Mirror src into dest (adds, updates and removes files)."""
    want = set()
    if src.exists():
        for f in sorted(src.rglob("*")):
            if f.is_file() and not any(part.startswith((".", "_")) and not part.startswith("_ds") for part in f.relative_to(src).parts):  # _ds = deck design-system files (tokens, fonts)
                rel = f.relative_to(src)
                want.add(rel)
                sync_file(f, dest / rel)
    if dest.exists():
        for f in sorted(dest.rglob("*"), reverse=True):
            if f.is_file() and f.relative_to(dest) not in want:
                f.unlink()
        for d in sorted((x for x in dest.rglob("*") if x.is_dir()), reverse=True):
            if not any(d.iterdir()):
                d.rmdir()


def stage_label(dirname):
    return STAGES.get(dirname) or re.sub(r"^\d+-", "", dirname).replace("-", " ").title()


def load_variant(f, folder):
    raw = f.read_text(encoding="utf-8")
    meta, body = parse_front_matter(raw)
    if not meta:
        inline, body = parse_inline_header(body)
        if inline:
            meta = {"duration": inline.get("duration", ""), "level": inline.get("audience", "").lower(),
                    "tags": [t.strip() for t in inline.get("methods", "").split("·") if t.strip()], "subtitle": "",
                    "programs": [t.strip() for t in inline.get("programs", "").split(",") if t.strip()]}
            meta["_methods"] = inline.get("methods", "")
    if str(meta.get("type", "lesson")).lower() in ("brainstorm", "reference"):
        return None
    h1 = re.search(r"^#\s+(.*)$", body, re.M)
    title = meta.get("title") or (re.sub(r"^Session \d+\s*[·:-]\s*", "", h1.group(1)).strip() if h1 else folder.replace("-", " ").title())
    if h1 and body.lstrip().startswith(h1.group(0)):  # page header already shows the title
        body = body.lstrip()[len(h1.group(0)):].lstrip("\n")
    desc = meta.get("subtitle", "")
    if not desc and meta.get("_methods"):
        desc = "Methods: " + meta["_methods"]
    if not desc:
        m = re.search(r"##\s*Overview\s*\n+(.+?)(\n\n|$)", body, re.S)
        desc = re.sub(r"[*_`>]", "", (m.group(1) if m else "").strip()).replace("\n", " ")
        desc = desc[:200].rsplit(" ", 1)[0] + "…" if len(desc) > 200 else desc
    tags = meta.get("tags", [])
    tags = [t for t in (tags if isinstance(tags, list) else [tags]) if t.lower() not in ("mixed", "junior", "senior-lead", "senior")]
    return {"path": f, "title": clean_title(title), "subtitle": meta.get("subtitle", ""), "desc": desc, "meta": meta, "body": body,
            "level": pretty_level(meta.get("level", "")), "duration": meta.get("duration", ""),
            "date": pretty_date(meta.get("date", "")), "tags": tags[:6],
            "draft": str(meta.get("draft", "false")).lower() == "true"}


def clean_title(t):
    t = re.sub(r"^(Slide Deck Outline|Learnings)\s*[—:-]\s*", "", t.strip())
    t = re.sub(r"\s*Slide Deck Outline\s*$", "", t)
    return re.sub(r"\b(Ai|Ux|Ui)\b", lambda m: m.group(1).upper(), t).strip()


def person_first_name(folder_name):
    return folder_name.split("-")[0].title()


def load_homework(topic_name):
    items = []
    if not MENTEES.exists():
        return items
    for mentee in sorted(p for p in MENTEES.iterdir() if p.is_dir() and visible(p)):
        hw = mentee / "homework" / topic_name
        if not hw.is_dir():
            continue
        first = person_first_name(mentee.name)
        for f in sorted(hw.rglob("*")):
            if not f.is_file() or any(x.startswith((".", "_")) for x in f.relative_to(hw).parts):
                continue
            stem = re.sub(rf"^{re.escape(mentee.name)}[-_ ]", "", f.stem, flags=re.I)
            stem = re.sub(r"^[A-Z][a-z]+[-_][A-Z][a-z]+[-_]", "", stem) if stem == f.stem else stem
            items.append({"src": f, "mentee": first, "mentee_dir": mentee.name, "rel": f.relative_to(hw),
                          "label": re.sub(r"[-_]+", " ", stem).strip().title() or f.stem,
                          "is_image": f.suffix.lower() in IMG_EXT, "ext": f.suffix.lower().lstrip(".")})
    return items


FALLBACK_USED = []

MENTEE_PUBLISHED = set()


def mentee_href(d, p):
    """Mentees/ is git-ignored (private), so only slides and homework are copied into Homepage/assets/mentees/ and linked from there."""
    rel = p.relative_to(d)
    dest = ASSETS / "mentees" / d.name / rel
    sync_file(p, dest)
    MENTEE_PUBLISHED.add(dest)
    return "../assets/mentees/" + quote(d.name) + "/" + quote(rel.as_posix())


def mentee_md_page(d, f, rel):
    """Markdown file -> a readable page inside the site (a raw .md would download instead of opening)."""
    body = parse_front_matter(f.read_text(encoding="utf-8"))[1]
    html_body, _ = render_markdown(body)
    dest = ASSETS / "mentees" / d.name / "md" / rel.with_suffix(".html")
    depth = 4 + len(rel.parts) - 1   # Homepage/assets/mentees/<slug>/md/<rel>.html
    title = nice_topic(f.stem)
    page_html = page(f"{title} — {d.name.replace('-', ' ').title()}", f'''<div class="tp"><a class="tp-back" href="{"../" * depth}mentees/{d.name}.html#artifacts">← Back to mentee</a>
<article class="tp-body">{html_body}</article></div>''', depth, "", body_cls="tp-white", active="mentees")
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(page_html, encoding="utf-8")
    MENTEE_PUBLISHED.add(dest)
    return "../assets/mentees/" + quote(d.name) + "/md/" + quote(rel.with_suffix(".html").as_posix())


def prune_mentee_assets():
    base = ASSETS / "mentees"
    if base.exists():
        for f in sorted(base.rglob("*"), reverse=True):
            if f.is_file() and f not in MENTEE_PUBLISHED:
                f.unlink()
            elif f.is_dir() and not any(f.iterdir()):
                f.rmdir()


def nice_topic(stem):
    return re.sub(r"[-_]+", " ", stem).strip().title()


def read_sessions_table(path):
    """Mentees/<slug>/sessions.md: `| # | Topic | Date | Status | Lesson | Playback |`, one row per session."""
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")] if line.strip().startswith("|") else []
        if len(cells) >= 4 and cells[0].isdigit():
            cells += [""] * (6 - len(cells))
            rows.append({"n": int(cells[0]), "title": cells[1], "date": pretty_date(cells[2]), "status": cells[3], "lesson": cells[4], "playback": cells[5]})
    return rows


def read_assessment(path):
    """Mentees/<slug>/assessment.md: `| Metric | Baseline | Post-training |` table, or front matter `na: "reason"`."""
    out = {"rows": [], "na": ""}
    if not path.exists():
        return out
    fm, body = parse_front_matter(path.read_text(encoding="utf-8"))
    out["na"] = fm.get("na", "")
    for line in body.splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")] if line.strip().startswith("|") else []
        if len(cells) >= 3 and cells[0].lower() != "metric" and not set(cells[0]) <= set("-: "):
            out["rows"].append((cells[0], cells[1], cells[2]))
    return out


def read_plan_sessions(plan_body):
    """Planned sessions from the coaching plan: `### Session N · Title` (or `:` / `—`), optional `*Phase*` line,
    then `**Learning objectives**` and `**Success check**` bullet lists."""
    out = []
    parts = re.split(r"^###\s+Session\s+(\d+)\s*[·:—-]\s*(.+?)\s*$", plan_body, flags=re.M)
    for i in range(1, len(parts) - 2, 3):
        chunk = re.split(r"^(?:##\s|---\s*$)", parts[i + 2], maxsplit=1, flags=re.M)[0]
        ph = re.search(r"^\*([^*\n]+)\*\s*$", chunk, re.M)

        def bullets(label):
            m = re.search(rf"\*\*{label}[^*]*\*\*\s*\n((?:\s*[-*]\s+.*\n?)+)", chunk, re.I)
            return [re.sub(r"^\s*[-*]\s+", "", l).strip() for l in m.group(1).splitlines() if l.strip()] if m else []
        bring = re.search(r"\b(Bring\b[^.\n]*\.)", chunk)
        out.append({"n": int(parts[i]), "title": parts[i + 1].strip(), "phase": ph.group(1).strip() if ph else "",
                    "objectives": bullets("Learning objectives"), "success": bullets("Success check"), "bring": bring.group(1) if bring else ""})
    return out


def mentee_detail(d, meta, plan_body, session_files, readme, mm=None):
    """What the public detail page shows. Session recaps, transcripts and assessment files stay private: only
    topic / date / status (from the README log or recap titles), slide decks and homework files are published."""
    ov = re.search(r"^##\s+Program(?:me)? Overview\s*\n(.*?)(?=^---\s*$|^##\s)", plan_body, re.M | re.S)
    overview = ov.group(1).strip() if ov else ""

    mm = mm or {}
    rows = []
    sessions_md = d / "sessions.md"
    if sessions_md.exists():   # source of truth; the README / recap / transcript fallbacks below only run without it
        rows = read_sessions_table(sessions_md)
    if not rows and readme.exists():
        for m in re.finditer(r"^\|\s*(\d+)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*$", readme.read_text(encoding="utf-8"), re.M):
            status = re.split(r"\s+[—-]\s+see\b", m.group(4))[0].strip()
            rows.append({"n": int(m.group(1)), "title": m.group(2), "date": "" if m.group(3) in ("", "—", "-") else m.group(3), "status": status})
    if not rows:
        for f in session_files:
            fm, _ = parse_front_matter(f.read_text(encoding="utf-8"))
            n = fm.get("session_number") or (re.search(r"session-(\d+)", f.name) or [None, ""])[1]
            if str(n).isdigit():
                title = re.sub(r"^Session\s*\d+\s*[—:-]\s*", "", fm.get("title", "")) or nice_topic(re.sub(r"^session-\d+-", "", f.stem))
                rows.append({"n": int(n), "title": title, "date": pretty_date(fm.get("date")), "status": "Completed"})
    td = d / "transcripts"
    for f in sorted(td.glob("*")) if td.exists() and not sessions_md.exists() else []:
        t = re.match(r"^(?:Session|Lesson)\s*(\d+)(?:\.\d+)?\s*[-–:_]?\s*(.*?)(?:\s*-\s*Part \d+)?$", f.stem, re.I)
        if t and not any(r["n"] == int(t.group(1)) for r in rows):
            rows.append({"n": int(t.group(1)), "title": t.group(2).strip(" _-"), "date": "", "status": "", "weak": True})   # file names only, never contents
    rows.sort(key=lambda r: r["n"])

    playback = {r["n"]: r["playback"] for r in rows if r.get("playback")}
    pb = d / "playback.md"   # legacy; sessions.md has a Playback column, one line per session: "3: https://link" or "3: short summary"
    if pb.exists():
        for m_ in re.finditer(r"^\W*(\d+)\s*:\s*(\S.*)$", pb.read_text(encoding="utf-8"), re.M):
            playback[int(m_.group(1))] = m_.group(2).strip()

    slides, other = {}, []
    sd = d / "slides"
    for f in sorted(sd.rglob("*")) if sd.exists() else []:
        if not f.is_file() or any(x.startswith((".", "_")) for x in f.relative_to(sd).parts):
            continue
        item = {"label": re.sub(r"\.dc$", "", f.stem), "ext": f.suffix.lower().lstrip("."), "url": mentee_href(d, f)}
        num = re.match(r"^(?:(?:Session|Sesion|Day|Lesson)\s*)?(\d+)(?:\.\d+)?(?:\s+(\d+))?\s*(?:[-–·:.]\s*)(.*)$", f.stem, re.I)
        if not num:
            other.append(item)
            continue
        item["topic"] = re.sub(r"\s*[—-]\s*Winnie Nguyen$", "", num.group(3)).strip()
        for n in range(int(num.group(1)), int(num.group(2) or num.group(1)) + 1):   # "Day 1 2-" covers days 1 and 2
            slides.setdefault(n, []).append(item)

    homework = {}
    hd = d / "homework"
    for f in sorted(hd.rglob("*")) if hd.exists() else []:
        rel = f.relative_to(hd)
        if not f.is_file() or any(x.startswith((".", "_")) for x in rel.parts):
            continue
        topic = nice_topic(rel.parts[0]) if len(rel.parts) > 1 else "General"
        stem = re.sub(rf"^{re.escape(d.name)}[-_ ]", "", f.stem, flags=re.I)
        homework.setdefault(topic, []).append({
            "label": nice_topic(re.sub(r"^[A-Z][a-z]+[-_][A-Z][a-z]+[-_]", "", stem)) or f.stem,
            "is_image": f.suffix.lower() in IMG_EXT, "ext": f.suffix.lower().lstrip("."), "url": mentee_href(d, f)})

    # Loose files: anything dropped in the mentee folder or in a folder the site doesn't already use shows up as a link.
    # Skipped: README / mentee / sessions / assessment files, the private folders, and names starting with "." or "_".
    # artifacts/ HTML pages embed inline; Markdown files are rendered to a readable page; everything else links to the file.
    artifacts, groups = {}, {}
    SKIP_FILES = {"readme.md", "mentee.md", "sessions.md", "assessment.md", "playback.md", "profile.md"}
    RESERVED = {"assessments", "homework", "plan", "sessions", "slides", "transcripts"}
    for f in sorted(d.rglob("*")):
        rel = f.relative_to(d)
        if not f.is_file() or any(x.startswith((".", "_")) for x in rel.parts) or rel.parts[0].lower() in RESERVED:
            continue
        if len(rel.parts) == 1 and f.name.lower() in SKIP_FILES:
            continue
        in_art = rel.parts[0] == "artifacts"
        sub = rel.parts[1:] if in_art else rel.parts
        group = nice_topic(sub[0]) if len(sub) > 1 else ("Artifacts" if in_art else "Files")
        ext = f.suffix.lower().lstrip(".")
        if ext == "md":
            url = mentee_md_page(d, f, rel)
        else:
            url = mentee_href(d, f)
        groups.setdefault(group, []).append({"label": f.name, "ext": ext, "url": url, "embed": in_art and ext in ("html", "htm")})
    for g, files in groups.items():
        # a folder with an HTML page shows the page(s); its css/js/images ride along unlisted
        artifacts[g] = [x for x in files if x["embed"]] + [x for x in files if not x["embed"] and not any(y["embed"] for y in files)]

    prof = dict(mm)   # mentee.md first
    if not mm and (d / "profile.md").exists():   # facts copied from the private Notion hub: role, dates, cadence, goal
        prof, _ = parse_front_matter((d / "profile.md").read_text(encoding="utf-8"))
    lesson_map = {int(n): slug.strip() for n, slug in re.findall(r"(\d+)\s*=\s*([\w-]+)", str(prof.get("lessons", "")))}
    lesson_map.update({r["n"]: r["lesson"] for r in rows if r.get("lesson")})
    when = " – ".join(x for x in [pretty_date(prof.get("start")), pretty_date(prof.get("end"))] if x)

    plan_dir = d / "plan"
    plan_files = sorted(plan_dir.glob("*.pdf"))[-1:] or sorted(plan_dir.glob("*.md"))[:1] if plan_dir.exists() else []
    return {"overview": overview, "cadence": prof.get("cadence") or meta.get("cadence", ""), "role": prof.get("role", ""), "when": when, "start": pretty_date(prof.get("start")), "end": pretty_date(prof.get("end")), "goal": prof.get("goal", ""), "project": prof.get("project") or meta.get("project_vehicle", ""),
            "sessions_log": rows, "playback": playback, "lesson_map": lesson_map, "slides": slides, "slides_other": other, "homework": homework,
            "plan_url": "", "roadmap": read_plan_sessions(plan_body), "artifacts": artifacts, "assessment": read_assessment(d / "assessment.md"), "prog_slug": prof.get("programme_page", "")}   # coaching plans stay private (draft: true in the template); not published



def resolve_programs(slug, variants):
    """(program slug, session idx) pairs, read from each lesson file's own `programs:` line."""
    out = []
    for v in variants:
        raw = v["meta"].get("programs", [])
        for item in (raw if isinstance(raw, list) else [raw]):
            item = str(item).strip().strip("\"'")
            if ":" in item:
                prog, idx = item.rsplit(":", 1)
                pair = (prog.strip(), idx.strip().zfill(2))
                if pair not in out:
                    out.append(pair)
    if not out and slug in LESSON_PROGRAMS:
        out = list(LESSON_PROGRAMS[slug])
        FALLBACK_USED.append(slug)
    return out


def load_lessons():
    lessons = []
    for stage_dir in sorted(p for p in LESSONS_DIR.iterdir() if p.is_dir() and visible(p)):
        for topic in sorted(p for p in stage_dir.iterdir() if p.is_dir() and visible(p) and p.name.lower() not in NON_TOPIC):
            slug = topic.name
            mats = topic / "materials"
            files = [f for f in sorted(mats.glob("*.md")) if not NOT_LESSON.search(f.stem)] if mats.exists() else []
            primary = next((f for f in files if f.stem == f"{slug}-lesson"), None)
            if primary:
                files = [primary] + [f for f in files if f != primary]
            variants = [v for v in (load_variant(f, slug) for f in files) if v]
            # variant tab labels: the level when titles repeat, else the title
            titles = [v["title"] for v in variants]
            for v in variants:
                v["label"] = v["title"] if len(set(titles)) == len(titles) else (v["level"] or v["path"].stem)
            outline = next(iter(sorted(mats.glob("*slide-outline.md"))), None) if mats.exists() else None
            title = variants[0]["title"] if variants else None
            if not title and outline:
                m = re.search(r"^#\s+(?:Slide Deck Outline\s*[—-]\s*)?(.*)$", outline.read_text(encoding="utf-8"), re.M)
                title = m.group(1).strip() if m else None
            title = clean_title(title or slug.replace("-", " ").title())

            sdir = topic / "slides"
            slide_files = [f for f in sorted(sdir.rglob("*")) if f.is_file() and visible(f) and "_archive" not in f.relative_to(sdir).parts] if sdir.exists() else []
            htmls = [f for f in slide_files if f.suffix.lower() == ".html" and f.parent == sdir]
            if len(htmls) > 1:
                htmls = [f for f in htmls if f.name.lower() != "index.html"] or htmls
            pdfs = [f for f in slide_files if f.suffix.lower() == ".pdf"]
            links = []
            for v in variants:
                u = str(v["meta"].get("slides", "")).strip()
                if re.match(r"^https?://", u) and u not in [l["url"] for l in links]:
                    links.append({"url": u, "label": v["label"] if len(variants) > 1 else "Open slides"})
            homework = load_homework(slug)
            first = variants[0] if variants else {}
            lessons.append({
                "slug": slug, "folder": topic, "stage": stage_label(stage_dir.name), "stage_dir": stage_dir.name,
                "title": title, "subtitle": first.get("subtitle", ""), "desc": first.get("desc", ""),
                "variants": variants, "decks": htmls, "pdfs": pdfs, "links": links, "homework": homework,
                "draft": bool(first.get("draft")), "programs": resolve_programs(slug, variants),
                "has_page": bool(variants or htmls or pdfs or links or homework),
            })
    return lessons


def copy_lesson_image(variant, folder_slug, href):
    """Resolve an image href from a lesson, copy it next to the site, return the site-relative path."""
    href = unquote(html.unescape(href))
    if re.match(r"^(https?:|data:)", href):
        return href
    src = (variant["path"].parent / href).resolve()
    if not src.exists():
        topic = variant["path"].parents[1]
        norm = lambda n: re.sub(r"[-_\s]+", " ", n).strip().lower()  # tolerate hyphen / underscore / space differences
        want, exact = norm(Path(href).name), Path(href).name
        found = [Path(r) / f for r, _, fs in os.walk(topic, followlinks=True) for f in fs]
        hits = [f for f in found if f.name == exact] or [f for f in found if norm(f.name) == want]
        src = hits[0] if hits else None
    if not src or not src.exists():
        return None
    name = re.sub(r"\s+", "-", src.name)
    sync_file(src, ASSETS / "lesson-assets" / folder_slug / name)
    return f"../assets/lesson-assets/{quote(folder_slug)}/{quote(name)}"


def render_lesson_body(variant, folder_slug, idx, by_stem):
    body_html, headings = render_markdown(variant["body"], prefix=f"v{idx}-")

    def fig(m):
        tag = m.group(0)
        src = re.search(r'src="([^"]*)"', tag)
        alt = re.search(r'alt="([^"]*)"', tag)
        src, alt = (src.group(1) if src else ""), (alt.group(1) if alt else "")
        new = copy_lesson_image(variant, folder_slug, src)
        if not new:
            return f'<span class="tp-fig__cap">[image not found: {alt or esc(src)}]</span>'
        cap = f'<span class="tp-fig__cap">{alt}</span>' if alt else ""
        return f'<a class="tp-fig" href="{new}" target="_blank" rel="noopener"><img src="{new}" alt="{alt}" loading="lazy">{cap}</a>'

    body_html = re.sub(r"<img\b[^>]*>", fig, body_html)

    def link(m):
        href = html.unescape(m.group(1))
        stem = re.sub(r"-(lesson|slide-outline)$", "", Path(href.split("#")[0]).stem)
        target = by_stem.get(stem)
        if href.endswith(".md") or ".md#" in href:
            if target:
                return f'<a href="{target}.html"'
            return f'<a class="tp-dead" title="Source file link: {esc(href)}"'
        if re.match(r"^https?:", href):
            return f'<a href="{m.group(1)}" target="_blank" rel="noopener"'
        return m.group(0)

    body_html = re.sub(r'<a href="([^"]+)"', link, body_html)
    return body_html, headings


def prepare_lesson_assets(lessons):
    """Copy slides + homework next to the site; prune folders of lessons that no longer exist."""
    live = {l["slug"] for l in lessons}
    for sub in ("lessons", "homework", "lesson-assets"):
        base = ASSETS / sub
        if base.exists():
            for d in base.iterdir():
                if d.is_dir() and d.name not in live:
                    shutil.rmtree(d, ignore_errors=True)
    for l in lessons:
        if l["decks"] or l["pdfs"]:
            sync_tree(l["folder"] / "slides", ASSETS / "lessons" / l["slug"] / "slides")
            if (l["folder"] / "assets").exists():
                sync_tree(l["folder"] / "assets", ASSETS / "lessons" / l["slug"] / "assets")
            fix_deck_links(ASSETS / "lessons" / l["slug"] / "slides")
        else:
            shutil.rmtree(ASSETS / "lessons" / l["slug"], ignore_errors=True)
        want = set()
        for h in l["homework"]:
            dest = ASSETS / "homework" / l["slug"] / h["mentee_dir"] / h["rel"]
            sync_file(h["src"], dest)
            h["url"] = f"../assets/homework/{quote(l['slug'])}/{quote(h['mentee_dir'])}/{quote(h['rel'].as_posix())}"
            want.add(dest)
        hdir = ASSETS / "homework" / l["slug"]
        if hdir.exists():
            for f in hdir.rglob("*"):
                if f.is_file() and f not in want:
                    f.unlink()


# ─────────────────────────────────────────────────────────────────────────────
# MENTEES  (internal only)
# ─────────────────────────────────────────────────────────────────────────────

def load_mentees():
    people = []
    if not MENTEES.exists():
        return people
    for d in sorted(p for p in MENTEES.iterdir() if p.is_dir()):
        plan = next(iter(sorted((d / "plan").glob("*.md"))), None) if (d / "plan").exists() else None
        plan_pdf = next(iter(sorted((d / "plan").glob("*.pdf"))), None) if (d / "plan").exists() else None
        meta, body = ({}, "")
        if plan:
            meta, body = parse_front_matter(plan.read_text(encoding="utf-8"))
        mm = parse_front_matter((d / "mentee.md").read_text(encoding="utf-8"))[0] if (d / "mentee.md").exists() else {}
        roadmap = re.search(r"^##\s+(Roadmap to .*)$", body, re.M)
        name = mm.get("name") or meta.get("student") or d.name.replace("-", " ").title()
        if " " not in name and d.name.count("-"):
            name = d.name.replace("-", " ").title()
        sess_dir = d / "sessions"
        sessions = sorted(sess_dir.glob("session-*.md")) if sess_dir.exists() else []
        closeout = any("close-out" in s.name or "closeout" in s.name for s in sessions)
        readme = d / "README.md"
        readme_program = ""
        planned = meta.get("sessions", "")
        if readme.exists():
            rt = readme.read_text(encoding="utf-8")
            if re.search(r"Completed\s+\d", rt) and "Programme" in rt:
                closeout = True
            m = re.search(r"\*\*Program:\*\*\s*(\d+)-session", rt)
            if m and not planned:
                planned = m.group(1)
            m = re.search(r"\*\*Program:\*\*\s*([^\n]+?)(?:\s+—|$)", rt, re.M)
            readme_program = m.group(1).strip() if m else ""
            log_rows = re.findall(r"^\|\s*\d+\s*\|", rt, re.M)
            if log_rows and len(log_rows) > len(sessions):
                sessions = [None] * len(log_rows)
        assess = sorted((d / "assessments").glob("*")) if (d / "assessments").exists() else []
        links = []
        for label, p in [("Coaching plan", plan_pdf or plan), ("Baseline", assess[0] if assess else None)]:
            if p:
                links.append((label, quote(os.path.relpath(p, OUT).replace(os.sep, "/"))))
        detail = mentee_detail(d, meta, body, sorted(sess_dir.glob("session-*.md")) if sess_dir.exists() else [], readme, mm)
        if (d / "sessions.md").exists():
            sessions = [r for r in detail["sessions_log"] if r["status"].lower().startswith("completed")]
            planned = mm.get("sessions") or planned
        status = {"completed": "Completed", "in-progress": "In progress", "not-started": "Not started"}.get(str(mm.get("status", "")).lower())
        people.append({
            **detail,
            "name": name, "slug": d.name,
            "level": mm.get("level") or meta.get("level", ""), "target": mm.get("target") or meta.get("target_level", ""),
            "program": mm.get("program") or (roadmap.group(1).replace("Roadmap to ", "") if roadmap else readme_program),
            "planned": int(planned) if str(planned).isdigit() else None,
            "logged": len(sessions), "baseline": bool(assess) or any(b for k, b, _ in detail["assessment"]["rows"] if k == "Career readiness"), "has_plan": bool(plan or plan_pdf),
            "status": status or ("Completed" if closeout else ("In progress" if (sessions or plan or plan_pdf) else "Not started")),
            "links": links,
        })
    return people


# ─────────────────────────────────────────────────────────────────────────────
# HTML
# ─────────────────────────────────────────────────────────────────────────────

def reload_js(pre):
    """Reload the open page when a rebuild finishes (only when served over http; a no-op from file://)."""
    return ("<script>(function(){if(location.protocol.indexOf('http')!==0)return;var u='%sassets/build-stamp.txt',last=null;"
            "function c(){fetch(u,{cache:'no-store'}).then(function(r){return r.ok?r.text():null}).then(function(t){"
            "if(t===null)return;if(last!==null&&t!==last)location.reload();last=t}).catch(function(){})}"
            "c();setInterval(c,1500)})();</script>") % pre


def page(title, body, depth=0, desc="", extra_head="", body_cls="", active=""):
    pre = "../" * depth
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<meta name="robots" content="noindex"/>
<meta name="description" content="{esc(desc)}"/>
<title>{esc(title)}</title>
<link rel="stylesheet" href="{pre}assets/css/tokens.css"/>
<link rel="stylesheet" href="{pre}assets/css/components.css"/>
<link rel="stylesheet" href="{pre}assets/css/site.css"/>
<link rel="stylesheet" href="{pre}assets/css/card-list.css"/>
<link rel="stylesheet" href="{pre}assets/css/text-page.css"/>
<link rel="stylesheet" href="{pre}assets/css/home.css"/>
{extra_head}
</head>
<body class="{body_cls}">
{nav(depth, active)}
{body}
{footer()}
{reload_js(pre)}
</body>
</html>
"""


def nav(depth, active=""):
    pre = "../" * depth
    def link(key, href, label):
        return f'<a href="{pre}{href}" data-text="{label}"{" class=active" if active == key else ""}>{label}</a>'
    return f"""<nav>
  <a class="nav-logo" href="{pre}index.html"><img src="{pre}assets/images/logo-nav.svg" alt="Winnie Nguyen — Training Hub"/></a>
  <div class="nav-links">
    {link("lessons", "lessons.html", "Lesson Library")}
    {link("mentees", "private-training.html", "Private Training")}
    {link("programs", "programs.html", "Programs")}
  </div>
</nav>"""


def footer():
    # Mirrors design-system/components/layout/SiteFooter.jsx and data/site.js
    return """<footer>
  <div class="footer-inner">
    <p>© 2026 Winnie Nguyen · Senior Product Designer</p>
    <div class="footer-links">
      <a href="mailto:nguyenphuctuongvan@gmail.com">Email</a>
      <a href="https://www.linkedin.com/in/winnienguyen2910" target="_blank" rel="noopener">LinkedIn</a>
    </div>
  </div>
</footer>"""


def program_card(p, lesson_count):
    sessions = len(p["sessions"])
    stat = p["stat"] or f"{sessions} sessions"
    return f"""<a class="cl-mini prog-mini" href="programs/{p['slug']}.html">
  <div class="cl-mini__top">{chip(PROGRAM_TAG.get(p['slug'], 'Program'), 'default')}<span>{esc(stat)}</span></div>
  <h3 class="cl-mini__title">{esc(p['title'])}</h3>
  <p class="cl-mini__desc">{esc(p['desc'])}</p>
  <span class="cl-mini__cta">{lesson_count} of {sessions} sessions have a lesson page →</span>
</a>"""


def lesson_card(l):
    tags = " ".join(t for v in l["variants"] for t in v["tags"])
    levels = " ".join(v["level"] for v in l["variants"])
    hay = esc(" ".join([l["title"], l["subtitle"], l["desc"], tags, l["stage"], levels]).lower())
    soon = not l["variants"]
    top = chip(l["stage"], "default") + (chip("Coming soon", "warning") if soon else "")
    desc = l["desc"] or ("Lesson plan coming soon." if soon else "")
    inner = f"""<div class="cl-mini__top">{top}</div>
  <h3 class="cl-mini__title">{esc(l['title'])}</h3>
  <p class="cl-mini__desc">{esc(desc)}</p>"""
    attrs = f'data-stage="{l["stage"]}" data-hay="{hay}"'
    if l["has_page"]:
        return f'<a class="cl-mini lesson-card" href="lessons/{l["slug"]}.html" {attrs}>\n  {inner}\n</a>'
    return f'<div class="cl-mini lesson-card lesson-card--soon" {attrs}>\n  {inner}\n</div>'


def md_progress(logged, planned):
    """Material 3 linear progress indicator. Fallback: the design system has no progress component."""
    if not planned:
        return f'<div class="mentee-count">{logged} session{"s" if logged != 1 else ""} logged</div>'
    pct = min(100, round(100 * logged / planned))
    return (f'<div class="md-progress" role="progressbar" aria-valuemin="0" aria-valuemax="{planned}" aria-valuenow="{logged}" '
            f'aria-label="Sessions logged"><span style="width:{pct}%"></span></div>'
            f'<div class="mentee-count">{logged} of {planned} sessions logged</div>')


STATUS_ORDER = {"In progress": 0, "Not started": 1, "Completed": 2}   # list order on the Private Training page
STATUS_TONE = {"Completed": "success", "In progress": "primary", "Not started": "default"}


def mentee_card(m):
    """Card-list template: compact card (cl-mini). Every card carries the same fields: status, name, programme."""
    prog = m["program"] or "Private training"
    hay = esc(" ".join([m["name"], prog, m["status"]]).lower())
    return f"""<a class="cl-mini mentee-card" href="mentees/{m['slug']}.html" data-status="{m['status']}" data-hay="{hay}">
  <div class="mentee-card__head"><h3 class="cl-mini__title">{esc(m['name'])}</h3>{chip(m['status'], STATUS_TONE[m['status']])}</div>
  <p class="cl-mini__desc">{esc(prog)}</p>
  <dl class="mentee-card__dates"><div><dt>Enrolled</dt><dd>{esc(m['start']) or '–'}</dd></div><div><dt>End date</dt><dd>{esc(m['end']) or '–'}</dd></div></dl>
</a>"""


def page_header(eyebrow, title, desc, note=""):
    eyebrow_html = f'<div class="page-eyebrow">{eyebrow}</div>' if eyebrow else ""
    return f"""<div class="page-header">{eyebrow_html}
  <h1 class="page-title">{title}</h1><p class="page-desc">{desc}</p>{note}</div>"""


def build_index(programs, lessons, mentees, counts):
    def big(href, kicker, title, desc, stat, tone):
        return f"""<a class="hub-card hub-card--{tone}" href="{href}">
  <h2 class="hub-card__title">{title}</h2>
  <p class="hub-card__desc">{desc}</p>
  <div class="hub-card__foot"><strong>{stat}</strong><span class="hub-card__cta">Open →</span></div>
</a>"""
    body = f"""
<header class="hero hero--solo">
  <div>
    <div class="hero__eyebrow">Training hub</div>
    <h1 class="hero__title">Everything I teach, <em>in one place</em>.</h1>
    <p class="hero__lead">The lessons I teach from, the people I coach one to one, and the programs that tie them together.</p>
  </div>
</header>
<section class="section hub-grid">
  {big("lessons.html", "01 · Lessons", "Lesson Library", "Full lesson plans with timing, activities and facilitator notes. Filter by design-thinking stage or search by topic.", f"{len(lessons)} lessons", "purple")}
  {big("private-training.html", "02 · Mentees", "Private Training", "Everyone I coach one to one: their program, progress, session topics, slides and homework.", f"{len(mentees)} mentees", "yellow")}
  {big("programs.html", "03 · Programs", "Programs", "The offers people enrol in, such as UI/UX Fundamentals and the roadmaps to Mid and Senior, with every session and its lesson.", f"{len(programs)} programs", "gray")}
</section>
"""
    return page("Training Hub — Winnie Nguyen", body, 0, "Lesson library, private training and programs.")


def build_lessons_index(lessons):
    stages = ["All"] + [s for s in STAGES.values() if any(l["stage"] == s for l in lessons)]
    filters = "".join(
        f'<button type="button" role="tab" class="tabs__tab{" tabs__tab--active" if s == "All" else ""}" data-stage="{s}" aria-selected="{"true" if s == "All" else "false"}">{s}</button>' for s in stages
    )
    body = f"""{page_header("", "Lesson Library", "Click a lesson to read the full plan: timing, activities and facilitator notes.")}
<section class="section section--tight">
  <div class="cl-controls">
    <div class="input-field cl-search"><input id="q" type="search" placeholder=" "/><label for="q">Search lessons, topics, levels</label></div>
  </div>
  <div class="tabs tabs--pill cl-tabs"><div class="tabs__list" role="tablist" aria-label="Filter by stage">{filters}</div></div>
  <div class="cl-grid lesson-grid" id="lesson-grid">{''.join(lesson_card(l) for l in lessons)}</div>
  <p class="cl-empty" id="empty" hidden>Nothing found. Try a different word.</p>
</section>
<script>
(function () {{
  var cards = [].slice.call(document.querySelectorAll('.lesson-card'));
  var q = document.getElementById('q'), empty = document.getElementById('empty');
  var btns = [].slice.call(document.querySelectorAll('.tabs__tab')), stage = 'All';
  function apply() {{
    var words = q.value.toLowerCase().split(/\\s+/).filter(Boolean), shown = 0;
    cards.forEach(function (c) {{
      var ok = (stage === 'All' || c.dataset.stage === stage) && words.every(function (w) {{ return c.dataset.hay.indexOf(w) > -1; }});
      c.hidden = !ok; if (ok) shown++;
    }});
    empty.hidden = shown > 0;
  }}
  btns.forEach(function (b) {{ b.addEventListener('click', function () {{
    stage = b.dataset.stage; btns.forEach(function (x) {{ x.setAttribute('aria-selected', x === b ? 'true' : 'false'); x.classList.toggle('tabs__tab--active', x === b); }}); apply();
  }}); }});
  q.addEventListener('input', apply);
}})();
</script>
"""
    return page("Lesson Library — Training Hub", body, 0, "All lesson plans.", active="lessons")


def build_programs_index(programs, counts):
    body = f"""{page_header("", "Programs", "Read from the live program pages, so titles and curriculum stay in sync.")}
<section class="section section--tight">
  <div class="cl-grid prog-grid">{''.join(program_card(p, counts['by_program'].get(p['slug'], 0)) for p in programs)}</div>
</section>"""
    return page("Programs — Training Hub", body, 0, "All programs.", active="programs")


def build_mentees_page(mentees):
    statuses = ["All"] + [x for x in ("In progress", "Completed", "Not started") if any(m["status"] == x for m in mentees)]
    filters = "".join(
        f'<button type="button" role="tab" class="tabs__tab{" tabs__tab--active" if x == "All" else ""}" data-stage="{x}" aria-selected="{"true" if x == "All" else "false"}">{x}</button>' for x in statuses)
    body = f"""{page_header("", "Private Training", "Everyone I coach one to one. Open a card for their programme, sessions and homework.")}
<section class="section section--tight">
  <div class="cl-controls">
    <div class="input-field cl-search"><input id="q" type="search" placeholder=" "/><label for="q">Search by name or programme</label></div>
  </div>
  <div class="tabs tabs--pill cl-tabs"><div class="tabs__list" role="tablist" aria-label="Filter by status">{filters}</div></div>
  <div class="cl-grid" id="mentee-grid">{''.join(mentee_card(m) for m in sorted(mentees, key=lambda m: (STATUS_ORDER[m["status"]], m["name"].lower())))}</div>
  <p class="cl-empty" id="empty" hidden>Nobody found. Try a different word.</p>
</section>
<script>
(function () {{
  var cards = [].slice.call(document.querySelectorAll('.mentee-card'));
  var q = document.getElementById('q'), empty = document.getElementById('empty');
  var btns = [].slice.call(document.querySelectorAll('.tabs__tab')), status = 'All';
  function apply() {{
    var words = q.value.toLowerCase().split(/\\s+/).filter(Boolean), shown = 0;
    cards.forEach(function (c) {{
      var ok = (status === 'All' || c.dataset.status === status) && words.every(function (w) {{ return c.dataset.hay.indexOf(w) > -1; }});
      c.hidden = !ok; if (ok) shown++;
    }});
    empty.hidden = shown > 0;
  }}
  btns.forEach(function (b) {{ b.addEventListener('click', function () {{
    status = b.dataset.stage; btns.forEach(function (x) {{ x.setAttribute('aria-selected', x === b ? 'true' : 'false'); x.classList.toggle('tabs__tab--active', x === b); }}); apply();
  }}); }});
  q.addEventListener('input', apply);
}})();
</script>"""
    return page("Private Training — Training Hub", body, 0, "Mentees.", active="mentees")


def mentee_overview_panel(m):
    goal = f'<h2>Programme goal</h2><blockquote>{esc(m["goal"])}</blockquote>' if m["goal"] else ""
    ov = f'<h2>Programme overview</h2>{render_markdown(m["overview"])[0]}' if m["overview"] else ""
    plan = f'<p><a class="btn btn--md btn--outlined btn--primary" href="{m["plan_url"]}" target="_blank" rel="noopener">Open coaching plan ↗</a></p>' if m["plan_url"] else ""
    if not (goal or ov or plan):
        return '<div class="tp-slides tp-slides--empty"><strong>Overview coming soon</strong><span>Add a coaching plan to this mentee\'s <code>plan/</code> folder.</span></div>'
    return f'<article class="tp-body">{goal}{ov}{plan}</article>'


def mentee_file_card(f):
    """Design-system Card (interactive) + Chip for one slide deck."""
    ext = FILE_ICON.get(f["ext"], f["ext"].upper()[:4] or "FILE")
    return f'<a class="card card--z1 card--interactive mentee-file" href="{f["url"]}" target="_blank" rel="noopener">{chip(ext, "primary")}<strong>{esc(f["label"])}</strong></a>'


STOP = {"and", "for", "the", "a", "of", "to", "in", "with", "your"}


def toks(t):
    return {w[:-1] if len(w) > 3 and w.endswith("s") else w for w in re.sub(r"[^a-z0-9]+", " ", t.lower().replace("&", " and ")).split() if w not in STOP}   # plural-insensitive


def lesson_for(r, m, lessons, min_score=0.75):
    """The library lesson a session belongs to: explicit `lessons:` override in profile.md, else the best title match
    (at least 75% of the shorter title's words shared, either direction). Returns None when nothing fits."""
    by_slug = {l["slug"]: l for l in lessons if l["has_page"]}
    if r["n"] in m["lesson_map"]:
        return by_slug.get(m["lesson_map"][r["n"]])
    best, best_score = None, 0.0
    for t in [r["title"]] + [d["topic"] for d in r["decks"] if d.get("topic")]:
        a = toks(t)
        for l in by_slug.values():
            b = toks(l["title"])
            if a and b and (min_score >= 0.75 or len(a & b) >= 2):   # looser matches need 2+ shared words
                score = len(a & b) / min(len(a), len(b))
                if score > best_score:
                    best, best_score = l, score
    return best if best_score >= min_score else None


def lesson_link(l):
    return f'<a class="btn btn--sm btn--text btn--primary" href="../lessons/{l["slug"]}.html">Lesson plan →</a>' if l else ""


def mentee_rows(m):
    rows = list(m["sessions_log"])
    known = {r["n"] for r in rows}
    rows += [{"n": n, "title": "", "date": "", "status": ""} for n in sorted(m["slides"]) if n not in known]
    rows.sort(key=lambda r: r["n"])
    for r in rows:
        decks = m["slides"].get(r["n"], [])
        slide_title = next((d["topic"] for d in decks if d.get("topic")), "")
        r["title"] = (slide_title if r.get("weak") else r["title"]) or r["title"] or slide_title or f"Session {r['n']}"
        r["decks"] = decks
    return rows


def mentee_sessions_panel(m, lessons):
    """Sessions tab: what happened in each session (playback), not the slide files."""
    rows = mentee_rows(m)
    if not rows:
        return '<div class="tp-slides tp-slides--empty"><strong>No sessions yet</strong><span>Sessions appear here as they are logged.</span></div>'
    out = []
    for r in rows:
        tone = "success" if r["status"].lower().startswith("completed") else "default"
        meta = ([chip(r["status"], tone)] if r["status"] else []) + ([f'<span class="sess__date">{esc(r["date"])}</span>'] if r["date"] else [])
        pb = m["playback"].get(r["n"], "")
        if pb.startswith("http"):
            play = f'<a class="btn btn--sm btn--soft btn--primary" href="{esc(pb)}" target="_blank" rel="noopener">Session playback ↗</a>'
        elif pb:
            play = f'<p class="sess__sum">{esc(pb)}</p>'
        else:
            play = '<span class="sess__none">Playback coming soon</span>'
        meta.append(lesson_link(lesson_for(r, m, lessons)))
        out.append(f"""<div class="sess"><div class="sess__idx">{r['n']}</div>
  <div><h4 class="sess__title">{esc(r['title'])}</h4>
  <div class="sess__meta">{"".join(x for x in meta if x)}</div>{play}</div></div>""")
    return f'<div class="sess-list">{"".join(out)}</div>'


def mentee_roadmap_panel(m, lessons):
    """Roadmap tab (prep view): every session in the coaching plan, what's done, what's next, and what the library covers."""
    plan = m["roadmap"]
    if not plan:
        return '<div class="tp-slides tp-slides--empty"><strong>No roadmap yet</strong><span>Add a coaching plan with <code>### Session N · Title</code> headings to this mentee\'s <code>plan/</code> folder.</span></div>'
    done = {r["n"] for r in m["sessions_log"] if r["status"].lower().startswith("completed")}
    log = {r["n"]: r for r in m["sessions_log"]}
    nxt = next((p for p in plan if p["n"] not in done), None)
    rows, card = [], ""
    has_phase = any(p["phase"] for p in plan)
    for p in plan:
        lesson = lesson_for({"n": p["n"], "title": p["title"], "decks": []}, m, lessons, 0.6)
        has_deck = bool(lesson and (lesson["decks"] or lesson["pdfs"] or lesson["links"]))
        has_hw = bool(lesson and lesson["homework"])
        if p["n"] in done:
            tone, label = "default", "Done"
        elif not lesson:
            tone, label = "error", "Gap: no lesson"
        elif has_deck:
            tone, label = "success", "Ready"
        else:
            tone, label = "warning", "Partial: no deck"
        lcell = f'<a href="../lessons/{lesson["slug"]}.html">{esc(lesson["title"])}</a>' if lesson else '<span class="sess__none">None in library</span>'
        dcell = f'<a href="../lessons/{lesson["slug"]}.html#slides">Deck</a>' if has_deck else "–"
        hcell = f'<a href="../lessons/{lesson["slug"]}.html#homework">Homework</a>' if has_hw else "–"
        is_next = nxt is p
        date = log.get(p["n"], {}).get("date", "")
        cls = ' class="is-next"' if is_next else (' class="is-done"' if p["n"] in done else "")
        phase_td = "<td>" + esc(p["phase"]) + "</td>" if has_phase else ""
        next_chip = " " + chip("Next up", "primary") if is_next else ""
        rows.append(f'<tr{cls}><th scope="row">{p["n"]}</th>{phase_td}<td><strong>{esc(p["title"])}</strong>{next_chip}</td>'
                    f'<td>{chip(label, tone)}</td><td class="md-nowrap">{esc(date) or "–"}</td><td>{lcell}</td><td>{dcell}</td></tr>')
        if is_next:
            li = lambda xs: "<ul>" + "".join(f"<li>{esc(x)}</li>" for x in xs) + "</ul>"
            prep = "".join(f"<li>{x}</li>" for x in [
                f"Lesson: {lcell}" if lesson else "Lesson: <strong>not in the library yet, needs building</strong>",
                (f"Slides: {dcell}" if has_deck else "Slides: <strong>missing</strong>") if lesson else "",
                f"Homework: {hcell}" if has_hw else "",
                esc(p["bring"])] if x)
            obj = "<h3>Learning objectives</h3>" + li(p["objectives"]) if p["objectives"] else ""
            suc = "<h3>Success check</h3>" + li(p["success"]) if p["success"] else ""
            card = (f'<article class="tp-body"><h2>Next up: Session {p["n"]} · {esc(p["title"])}</h2>'
                    f'<p>{chip(label, tone)} {esc(p["phase"])}</p><h3>Prep checklist</h3><ul>{prep}</ul>{obj}{suc}</article>')
    if not nxt:
        card = '<article class="tp-body"><h2>Programme roadmap complete</h2><p>Every planned session is logged as completed.</p></article>'
    phase_th = "<th>Phase</th>" if has_phase else ""
    table = (f'<article class="tp-body"><h2>All planned sessions</h2><table class="md-table"><thead><tr><th>#</th>{phase_th}<th>Planned topic</th>'
             f'<th>Status</th><th>Date</th><th>Library lesson</th><th>Deck</th></tr></thead><tbody>{"".join(rows)}</tbody></table></article>')
    return card + table


def mentee_slides_panel(m, lessons):
    """Slides tab: the decks used, grouped by session; falls back to the matching library lesson's deck."""
    out = []
    for r in mentee_rows(m):
        lesson = lesson_for(r, m, lessons)
        files = "".join(mentee_file_card(f) for f in r["decks"])
        if not files and lesson and (lesson["decks"] or lesson["pdfs"]):
            files = f'<a class="card card--z1 card--interactive mentee-file" href="../lessons/{lesson["slug"]}.html#slides">{chip("Lesson deck", "primary")}<strong>{esc(lesson["title"])}</strong></a>'
        if not files:
            continue
        out.append(f"""<div class="sess"><div class="sess__idx">{r['n']}</div>
  <div><h4 class="sess__title">{esc(r['title'])}</h4><div class="sess__meta">{lesson_link(lesson)}</div><div class="sess__files">{files}</div></div></div>""")
    if m["slides_other"]:
        out.append(f'<h3 class="tp-hw__group" style="margin-top:var(--space-10)">Other slides</h3><div class="sess__files">{"".join(mentee_file_card(f) for f in m["slides_other"])}</div>')
    if not out:
        return '<div class="tp-slides tp-slides--empty"><strong>No slides yet</strong><span>Add decks to this mentee\'s <code>slides/</code> folder.</span></div>'
    return f'<div class="sess-list">{"".join(out)}</div>'


def mentee_assessment_panel(m):
    """Baseline vs post-training self-assessment (numbers only; notes and recaps stay private)."""
    a = m["assessment"]
    if a["na"]:
        return f'<div class="tp-slides tp-slides--empty"><strong>No assessment for this programme</strong><span>{esc(a["na"])}</span></div>'
    if not a["rows"] or not any(b or p for _, b, p in a["rows"]):
        return '<div class="tp-slides tp-slides--empty"><strong>No assessment yet</strong><span>The baseline is taken at or before session 1; the reassessment at close-out.</span></div>'
    def change(b, p):
        mb, mp = re.fullmatch(r"(\d+)%", b), re.fullmatch(r"(\d+)%", p)
        return f"{int(mp.group(1)) - int(mb.group(1)):+d} pts" if mb and mp else ""
    pending = '<span class="sess__none">Pending</span>'
    rows = "".join(f"<tr><th scope=\"row\">{esc(k)}</th><td>{esc(b) if b else pending}</td><td>{esc(p) if p else pending}</td><td>{change(b, p)}</td></tr>" for k, b, p in a["rows"])
    return f'''<article class="tp-body"><h2>Baseline vs post-training</h2>
<table class="assess-table"><thead><tr><th>Metric</th><th>Baseline</th><th>Post-training</th><th>Change</th></tr></thead><tbody>{rows}</tbody></table>
<p class="sess__none">Self-assessment against the target level, taken at the start and again at the end of the programme.</p></article>'''


def mentee_artifacts_panel(m):
    """Files tab: HTML prototypes from artifacts/ embed inline; every other file is a plain hyperlink."""
    out = []
    for group, files in m["artifacts"].items():
        embeds = [f for f in files if f["embed"]]
        links = [f for f in files if not f["embed"]]
        html_ = f'<h3 class="tp-hw__group">{esc(group)}</h3>'
        for f in embeds:
            html_ += (f'''<div class="art-embed"><div class="art-embed__bar"><strong>{esc(f["label"])}</strong>
<a class="tp-meta__link" href="{f["url"]}" target="_blank" rel="noopener">Open full screen ↗</a></div>
<iframe src="{f["url"]}" title="{esc(f["label"])}" loading="lazy" allowfullscreen></iframe></div>''')
        if links:
            html_ += '<ul class="file-links">' + "".join(
                f'<li>{chip((f["ext"] or "file").upper()[:4], "primary")}<a href="{f["url"]}" target="_blank" rel="noopener">{esc(f["label"])}</a></li>' for f in links) + "</ul>"
        out.append(html_)
    return f'<div class="tp-hw">{"".join(out)}</div>'


def mentee_homework_panel(m):
    if not m["homework"]:
        return '<div class="tp-slides tp-slides--empty"><strong>No homework yet</strong><span>Work from between sessions shows up here.</span></div>'
    groups = []
    for topic, files in m["homework"].items():
        cards = []
        for h in files:
            if h["is_image"]:
                cards.append(f'<a class="tp-hw__card" href="{h["url"]}" target="_blank" rel="noopener"><div class="tp-hw__thumb"><img src="{h["url"]}" alt="{esc(h["label"])}" loading="lazy"></div><div class="tp-hw__info"><strong>{esc(h["label"])}</strong></div></a>')
            else:
                cards.append(f'<a class="tp-hw__card" href="{h["url"]}" target="_blank" rel="noopener"><div class="tp-hw__thumb"><span class="file-card__ext">{esc(FILE_ICON.get(h["ext"], h["ext"].upper()[:4]))}</span></div><div class="tp-hw__info"><strong>{esc(h["label"])}</strong></div></a>')
        groups.append(f'<h3 class="tp-hw__group">{esc(topic)}</h3><div class="tp-hw__grid">{"".join(cards)}</div>')
    return f'<div class="tp-hw">{"".join(groups)}</div>'


def build_mentee_page(m, lessons, programs=()):
    initials = "".join(w[0] for w in m["name"].split()[:2]).upper()
    n_sess = len(m["sessions_log"]) or len(m["slides"])
    n_hw = sum(len(v) for v in m["homework"].values())
    details = [("Status", m["status"]), ("Role" if m["role"] and not m["level"] else "Level", m["role"] or m["level"]), ("Target", m["target"]),
               ("Dates", m["when"]), ("Cadence", m["cadence"]), ("Project focus", m["project"])]
    details = [(k, v) for k, v in details if v]
    prog_page = next((p for p in programs if p["slug"] == m["prog_slug"]), None)
    cells_extra = f'<div><dt>Programme</dt><dd><a class="tp-meta__link" href="../programs/{prog_page["slug"]}.html">{esc(prog_page["title"])} →</a></dd></div>' if prog_page else ""
    cols = " ".join(["minmax(0, 1fr)"] * (len(details) - 1 + bool(cells_extra)) + ["minmax(0, 1.8fr)"])
    cells = cells_extra + "".join(f"<div><dt>{k}</dt><dd>{esc(v)}</dd></div>" for k, v in details)
    info = f'<div class="tp-info"><dl class="tp-meta" style="--tp-cols: {cols}">{cells}</dl>{md_progress(m["logged"], m["planned"])}</div>'
    n_slides = sum(len(v) for v in m["slides"].values()) + len(m["slides_other"])
    tabs = [("overview", "Overview"), ("roadmap", "Roadmap"), ("assessment", "Assessment"), ("sessions", f"Sessions ({n_sess})" if n_sess else "Sessions"),
            ("slides", f"Slides ({n_slides})" if n_slides else "Slides"),
            ("homework", f"Homework ({n_hw})" if n_hw else "Homework")]
    n_art = sum(len(v) for v in m["artifacts"].values())
    if n_art:   # the tab only exists when the folder has artifacts
        tabs.append(("artifacts", f"Files ({n_art})"))
    panels = {"overview": mentee_overview_panel(m), "roadmap": mentee_roadmap_panel(m, lessons), "assessment": mentee_assessment_panel(m), "sessions": mentee_sessions_panel(m, lessons), "slides": mentee_slides_panel(m, lessons), "homework": mentee_homework_panel(m), "artifacts": mentee_artifacts_panel(m) if n_art else ""}
    btns = "".join(f'<button type="button" role="tab" class="tabs__tab" data-tab-btn data-tab-id="{k}" aria-selected="false">{esc(lab)}</button>' for k, lab in tabs)
    panel_html = "".join(f'<section class="tp-panel" data-tab-panel data-tab-id="{k}" role="tabpanel" hidden>{panels[k]}</section>' for k, _ in tabs)
    body = f"""<div class="tp">
  <a class="tp-back" href="../private-training.html">← All mentees</a>
  <header class="tp-head">
    <div class="mentee-hero"><div class="avatar avatar--xl avatar--purple"><div class="avatar__inner">{esc(initials)}</div></div>
    <div><h1 class="page-title">{esc(m['name'])}</h1>
    <p class="page-desc">{esc(m['program'] or 'Program not set')}</p></div></div>
    {info}
  </header>
  <div class="tabs tabs--pill tp-tabs"><div class="tabs__list" role="tablist">{btns}</div></div>
  {panel_html}
</div>
{TAB_JS}"""
    return page(f"{m['name']} — Private Training", body, 1, m["program"], body_cls="tp-white", active="mentees")


def build_program_page(p, lessons_by_slug):
    rows, cur = [], None
    for s in p["sessions"]:
        if s["phase"] != cur:
            cur = s["phase"]
            if cur:
                rows.append(f'<h3 class="sess-phase">{esc(cur)}</h3>')
        linked = [l for l in lessons_by_slug.values() if (p["slug"], s["idx"]) in l["programs"]]
        links = "".join(
            (f'<a class="sess__lesson" href="../lessons/{l["slug"]}.html">{esc(l["title"])} →</a>' if l["has_page"]
             else f'<span class="sess__none">{esc(l["title"])} (coming soon)</span>') for l in linked
        ) or '<span class="sess__none">No lesson page yet</span>'
        rows.append(f"""<div class="sess"><div class="sess__idx">{esc(s['idx'])}</div>
  <div><h4 class="sess__title">{esc(s['title'])}</h4><p class="sess__sum">{esc(s['summary'])}</p>
  <div class="sess__links">{links}</div></div></div>""")
    live = f'<a class="btn btn--md btn--outlined btn--primary" href="{SITE_BASE}/training/programs/{p["slug"]}.html" target="_blank" rel="noopener">Open live page ↗</a>' if SITE_BASE else ""
    body = f"""<div class="tp">
  <a class="tp-back" href="../programs.html">← All programs</a>
  <header class="tp-head">
    <div class="page-eyebrow">{esc(PROGRAM_TAG.get(p['slug'], 'Program'))}</div>
    <h1 class="page-title">{esc(p['title'])}</h1>
    <p class="page-desc">{esc(p['desc'])}</p>
    <p class="prog-stat">{esc(p['stat'])}{(' · ' + str(len(p['sessions'])) + ' sessions listed') if p['stat'] else ''}</p>
    <div class="hero__actions">{live}</div>
  </header>
  <div class="sess-list">{''.join(rows)}</div>
</div>"""
    return page(f"{p['title']} — Training Hub", body, 1, p["desc"], active="programs")


FILE_ICON = {"pdf": "PDF", "md": "MD", "html": "HTML", "fig": "FIG", "pptx": "PPT", "docx": "DOC", "key": "KEY"}

TAB_JS = """<script>
(function () {
  function group(btnSel, panelSel, attr, onShow) {
    var btns = [].slice.call(document.querySelectorAll(btnSel)), panels = [].slice.call(document.querySelectorAll(panelSel));
    function show(id) {
      btns.forEach(function (b) { var on = b.getAttribute(attr) === id; b.setAttribute('aria-selected', on); b.classList.toggle('tabs__tab--active', on && b.classList.contains('tabs__tab')); });
      panels.forEach(function (p) { p.hidden = p.getAttribute(attr) !== id; });
      if (onShow) onShow(id);
    }
    btns.forEach(function (b) { b.addEventListener('click', function () { show(b.getAttribute(attr)); }); });
    return show;
  }
  var firstTab = (document.querySelector('[data-tab-btn]') || {getAttribute: function () {}}).getAttribute('data-tab-id');
  var showTab = group('[data-tab-btn]', '[data-tab-panel]', 'data-tab-id', function (id) { history.replaceState(null, '', id === firstTab ? location.pathname : '#' + id); });
  var showVar = group('[data-var-btn]', '[data-var-panel]', 'data-var-id');
  var h = (location.hash || '').replace('#', '');
  showTab(h && document.querySelector('[data-tab-btn][data-tab-id="' + h + '"]') ? h : firstTab);
  if (document.querySelector('[data-var-btn]')) showVar('0');
  var decks = [].slice.call(document.querySelectorAll('[data-deck-btn]'));
  decks.forEach(function (b) { b.addEventListener('click', function () {
    var f = document.getElementById('deck-frame'); f.src = b.dataset.src; document.getElementById('deck-open').href = b.dataset.src;
    decks.forEach(function (x) { x.classList.toggle('deck-item--active', x === b); x.setAttribute('aria-pressed', x === b); });
  }); });
})();
</script>"""


def variant_meta(l, v, idx):
    """Draft banner + details box for one lesson version; sits above the tabs, switches with the version picker."""
    details = [("Stage", l["stage"]), ("Level", v["level"]), ("Duration", v["duration"]), ("Date", v["date"]),
               ("Source file", v["path"].name)]
    details = [(k, x) for k, x in details if x]
    cols = f"repeat({len(details) - 1}, minmax(0, 1fr)) minmax(0, 1.8fr)"
    cells = "".join(
        f"<div><dt>{k}</dt><dd>{'<code>' + esc(x) + '</code>' if k == 'Source file' else esc(x)}</dd></div>" for k, x in details
    )
    tags = ""
    if v["tags"]:
        tags = '<div class="tp-meta__tags"><dt>Topics</dt><dd>' + "".join(f"<span>{esc(t)}</span>" for t in v["tags"]) + "</dd></div>"
    draft = '<div class="draft-banner">Draft: content exists but is not finalised for delivery.</div>' if v["draft"] else ""
    hidden = "" if idx == 0 else " hidden"
    return f'<div class="tp-info" data-var-panel data-var-id="{idx}"{hidden}>{draft}<dl class="tp-meta" style="--tp-cols: {cols}">{cells}{tags}</dl></div>'


def variant_panel(l, v, idx, by_stem):
    body_html, headings = render_lesson_body(v, l["slug"], idx, by_stem)
    toc = "".join(f'<a href="#{h["id"]}">{esc(h["text"])}</a>' for h in headings)
    hidden = "" if idx == 0 else " hidden"
    return f"""<div data-var-panel data-var-id="{idx}"{hidden}>
  <div class="tp-layout">
    <aside class="tp-toc" aria-label="On this page"><p class="tp-toc__label">On this page</p>{toc}</aside>
    <article class="tp-body">{body_html}</article>
  </div>
</div>"""


def deck_label(path):
    """Card title for a deck: its <title> unless that is a tool default, else the humanised file name."""
    try:
        m = re.search(r"<title>(.*?)</title>", path.read_text(encoding="utf-8", errors="ignore")[:4000], re.S | re.I)
    except OSError:
        m = None
    t = html.unescape(m.group(1)).strip() if m else ""
    if not t or re.match(r"^(bundled page|untitled|index|document)$", t, re.I):
        t = re.sub(r"\.dc$", "", path.stem).replace("_", " ")
        if " " not in t:
            t = t.replace("-", " ").capitalize()
    return t


def slides_panel(l):
    empty = '<div class="tp-slides tp-slides--empty"><strong>No slides yet</strong><span>Add a deck (.html) or .pdf to this lesson\'s <code>slides/</code> folder, or a <code>slides:</code> link in the lesson front matter.</span></div>'
    base = f"../assets/lessons/{quote(l['slug'])}/slides/"
    parts = []
    if l["decks"]:
        srcs = [base + quote(d.relative_to(l["folder"] / "slides").as_posix()) for d in l["decks"]]
        viewer = f"""<div class="tp-slides"><iframe id="deck-frame" src="{srcs[0]}" title="Lesson slides" allowfullscreen loading="lazy"></iframe></div>
<p class="tp-slides__link"><a id="deck-open" href="{srcs[0]}" target="_blank" rel="noopener">Open slides full screen ↗</a></p>"""
        if len(l["decks"]) > 1:
            items = "".join(
                f'<li><button type="button" class="deck-item{" deck-item--active" if i == 0 else ""}" data-deck-btn data-src="{src}" aria-pressed="{"true" if i == 0 else "false"}">'
                f'<span class="deck-item__title">{esc(deck_label(d))}</span></button></li>'
                for i, (d, src) in enumerate(zip(l["decks"], srcs)))
            parts.append(f'<div class="deck-layout"><div class="deck-side" role="group" aria-label="Slide decks"><p class="deck-side__label">Decks ({len(l["decks"])})</p><ul>{items}</ul></div><div class="deck-main">{viewer}</div></div>')
        else:
            parts.append(viewer)
    if l["pdfs"] or l["links"]:
        cards = "".join(
            f'<a class="file-card" href="{base + quote(f.relative_to(l["folder"] / "slides").as_posix())}" target="_blank" rel="noopener"><span class="file-card__ext">PDF</span><strong>{esc(f.stem)}</strong><span>Open PDF ↗</span></a>'
            for f in l["pdfs"]) + "".join(
            f'<a class="file-card" href="{esc(x["url"])}" target="_blank" rel="noopener"><span class="file-card__ext">LINK</span><strong>{esc(x["label"])}</strong><span>{esc(re.sub(r"^https?://", "", x["url"])[:46])} ↗</span></a>'
            for x in l["links"])
        parts.append(f'<h3 class="tp-hw__group" style="margin-top:var(--space-10)">Other formats</h3><div class="file-grid">{cards}</div>')
    return "".join(parts) or empty


def homework_panel(l):
    if not l["homework"]:
        return '<div class="tp-slides tp-slides--empty"><strong>No mentee homework yet</strong><span>Drop files in <code>Mentees/&lt;name&gt;/homework/%s/</code> and they show up here.</span></div>' % esc(l["slug"])
    cards = []
    for h in l["homework"]:
        # sibling links (not nested): the file opens from the thumbnail, the name opens that mentee's Homework tab
        info = (f'<div class="tp-hw__info"><strong>{esc(h["label"])}</strong>'
                f'<span>by <a class="tp-meta__link" href="../mentees/{esc(h["mentee_dir"])}.html#homework">{esc(h["mentee"])}</a></span></div>')
        if h["is_image"]:
            thumb = f'<img src="{h["url"]}" alt="{esc(h["label"])}" loading="lazy">'
        else:
            thumb = f'<span class="file-card__ext">{esc(FILE_ICON.get(h["ext"], h["ext"].upper()[:4] or "FILE"))}</span>'
        cards.append(f'<div class="tp-hw__card tp-hw__card--link"><a class="tp-hw__thumb" href="{h["url"]}" target="_blank" rel="noopener">{thumb}</a>{info}</div>')
    return f'<div class="tp-hw"><div class="tp-hw__grid">{"".join(cards)}</div></div>'


def build_lesson_page(l, lessons, programs, by_stem):
    prog_by_slug = {p["slug"]: p for p in programs}
    used = "".join(
        f'<a class="used__chip" href="../programs/{ps}.html">{esc(prog_by_slug[ps]["title"])} · session {esc(idx)}</a>'
        for ps, idx in l["programs"] if ps in prog_by_slug
    )
    used_html = f'<div class="used"><span>Taught in</span>{used}</div>' if used else ""

    # lesson tab: one panel per lesson file, with a switcher when a folder holds several
    if l["variants"]:
        switch = ""
        if len(l["variants"]) > 1:
            switch = '<div class="tabs tabs--pill var-switch"><div class="tabs__list" role="tablist" aria-label="Lesson version">' + "".join(
                f'<button type="button" role="tab" class="tabs__tab" data-var-btn data-var-id="{i}" aria-selected="false">{esc(v["label"])}</button>' for i, v in enumerate(l["variants"])
            ) + "</div></div>"
        lesson_html = switch + "".join(variant_panel(l, v, i, by_stem) for i, v in enumerate(l["variants"]))
    else:
        lesson_html = '<div class="tp-slides tp-slides--empty"><strong>Lesson plan coming soon</strong><span>Add <code>%s-lesson.md</code> to this folder\'s <code>materials/</code>.</span></div>' % esc(l["slug"])

    meta_html = "".join(variant_meta(l, v, i) for i, v in enumerate(l["variants"]))
    n_slides = len(l["decks"]) + len(l["pdfs"]) + len(l["links"])
    tabs = [("lesson", "Lesson"), ("slides", f"Slides ({n_slides})" if n_slides else "Slides"),
            ("homework", f"Homework ({len(l['homework'])})" if l["homework"] else "Homework")]
    tab_btns = "".join(
        f'<button type="button" role="tab" class="tabs__tab" data-tab-btn data-tab-id="{k}" aria-selected="false">{esc(lab)}</button>' for k, lab in tabs)
    panels = {"lesson": lesson_html, "slides": slides_panel(l), "homework": homework_panel(l)}
    panel_html = "".join(f'<section class="tp-panel" data-tab-panel data-tab-id="{k}" role="tabpanel" hidden>{panels[k]}</section>' for k, _ in tabs)

    first = l["variants"][0] if l["variants"] else {"meta": {}}
    related = []
    for key, label in (("previous-session", "Previous lesson"), ("next-session", "Next lesson")):
        t = first["meta"].get(key)
        if t:
            tgt = next((x for x in lessons if x["title"].lower() == str(t).lower() and x["slug"] != l["slug"] and x["has_page"]), None)
            related.append((label, t, tgt))

    def rel_card(lab, t, tgt):
        tag = "a" if tgt else "div"
        href = ' href="%s.html"' % tgt["slug"] if tgt else ""
        return f'<{tag} class="tp-related__card"{href}><span>{lab}</span><strong>{esc(t)}</strong></{tag}>'

    rel_html = ""
    if related:
        rel_html = f'<section class="tp-related"><h2>Related lessons</h2><div class="tp-related__grid">{"".join(rel_card(*r) for r in related)}</div></section>'

    body = f"""<div class="tp">
  <a class="tp-back" href="../lessons.html">← All lessons</a>
  <header class="tp-head">
    <h1 class="page-title">{esc(l['title'])}</h1>
    {f'<p class="page-desc">{esc(l["subtitle"])}</p>' if l['subtitle'] else ''}
    {used_html}
    {meta_html}
  </header>
  <div class="tabs tabs--pill tp-tabs"><div class="tabs__list" role="tablist">{tab_btns}</div></div>
  {panel_html}
  {rel_html}
</div>
{TAB_JS}"""
    return page(f"{l['title']} — Training Hub", body, 1, l["subtitle"] or l["desc"], body_cls="tp-white", active="lessons")


# ─────────────────────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────────────────────

def copy_design_system():
    css_out = OUT / "assets/css"
    css_out.mkdir(parents=True, exist_ok=True)
    for src in ["css/tokens.css", "css/components.css", "css/site.css",
                "templates/card-list/card-list.css", "templates/text/text-page.css"]:
        text = (DESIGN_SYSTEM / src).read_text(encoding="utf-8")
        if not text.startswith("@charset"):
            text = '@charset "UTF-8";\n' + text  # served without a charset header; avoids "Â·" / garbled arrows
        (css_out / Path(src).name).write_text(text, encoding="utf-8")
    shutil.copy2(Path(__file__).resolve().parent / "home.css", css_out / "home.css")  # hand-written page styles live next to this script
    img_out = OUT / "assets/images"
    img_out.mkdir(parents=True, exist_ok=True)
    shutil.copy2(WEBSITE / "public/portfolio/images/logo-nav.svg", img_out / "logo-nav.svg")
    # Older slide decks link to ../../../../_System/Themes/{tokens,components}.css, a folder that no longer exists
    # in the Library. Serve the design-system versions at that path so those decks still render.
    legacy = OUT / "_System/Themes"
    legacy.mkdir(parents=True, exist_ok=True)
    for name in ("tokens.css", "components.css"):
        shutil.copy2(DESIGN_SYSTEM / "css" / name, legacy / name)
    (OUT / "_System/fonts").mkdir(parents=True, exist_ok=True)
    fonts_out = OUT / "assets/fonts"
    fonts_out.mkdir(parents=True, exist_ok=True)
    for f in ["PublicSans-VariableFont_wght.ttf", "PublicSans-Italic-VariableFont_wght.ttf", "Syne-VariableFont_wght.ttf"]:
        shutil.copy2(DESIGN_SYSTEM / "fonts" / f, fonts_out / f)
        shutil.copy2(DESIGN_SYSTEM / "fonts" / f, OUT / "_System/fonts" / f)


def mentee_health(mentees, lessons):
    """Things worth fixing before publishing, per mentee. Returns [(mentee name, [message, ...])]."""
    out = []
    for m in mentees:
        d = MENTEES / m["slug"]
        w = []
        if not (d / "mentee.md").exists():
            w.append("no mentee.md (run `mentee.py migrate` or `new`)")
        if not (d / "sessions.md").exists():
            w.append("no sessions.md: sessions are guessed from README / recaps / file names")
        if not m["has_plan"]:
            w.append("no coaching plan in plan/")
        if not m["baseline"] and m["status"] != "Not started" and not m["assessment"]["na"]:
            w.append("no baseline assessment (fill the Baseline column in assessment.md; needed for the close-out comparison)")
        if m["status"] == "Completed" and m["planned"] and m["logged"] < m["planned"]:
            w.append(f"marked Completed but only {m['logged']} of {m['planned']} sessions are logged as Completed")
        if m["status"] == "Completed" and not m["when"].count("–"):
            w.append("marked Completed but mentee.md has no end date")
        if not m["prog_slug"]:
            w.append("not linked to a programme page (set programme_page in mentee.md)")
        if m["status"] == "Completed" and not (m["assessment"]["na"] or any(p for k, _, p in m["assessment"]["rows"] if k == "Career readiness")):
            w.append("marked Completed but no post-training assessment in assessment.md")
        if not m["program"]:
            w.append("no programme name (card shows 'Private training')")
        if not m["goal"]:
            w.append("no goal in mentee.md")
        no_lesson, no_slides, no_play, no_date, orphan = [], [], [], [], []
        known = {r["n"] for r in m["sessions_log"]}
        for r in mentee_rows(m):
            lesson = lesson_for(r, m, lessons)
            if r["n"] not in known:
                orphan.append(r["n"])
            if not lesson:
                no_lesson.append(r["n"])
            if not r["decks"] and not (lesson and (lesson["decks"] or lesson["pdfs"])):
                no_slides.append(r["n"])
            if not m["playback"].get(r["n"]):
                no_play.append(r["n"])
            if not r["date"]:
                no_date.append(r["n"])
        fmt = lambda xs: ", ".join(map(str, xs))
        if orphan:
            w.append(f"slides exist for session(s) {fmt(orphan)} but they are not in sessions.md")
        if no_lesson:
            w.append(f"no matching lesson for session(s) {fmt(no_lesson)} (set the Lesson column)")
        if no_slides:
            w.append(f"no slides for session(s) {fmt(no_slides)}")
        if no_play:
            w.append(f"no playback for session(s) {fmt(no_play)}")
        if no_date:
            w.append(f"no date for session(s) {fmt(no_date)}")
        if m["slides_other"]:
            w.append("slide files not tied to a session: " + ", ".join(f["label"] for f in m["slides_other"]))
        out.append((m["name"], w))
    return out


def print_health(report):
    total = sum(len(w) for _, w in report)
    print(f"\nMentee health check: {total} thing{'s' if total != 1 else ''} to look at" if total else "\nMentee health check: all clear")
    for name, w in report:
        if w:
            print(f"  {name}")
            for x in w:
                print(f"    - {x}")
    return total


def lesson_terms(lessons):
    """{slug: set of words} from each lesson's title, subtitle, tags and section headings, plus the document frequency of
    each word across lessons (rare words identify a lesson; common ones like 'design' don't)."""
    import math
    terms = {}
    for l in lessons:
        if not l["has_page"]:
            continue
        text = [l["title"], l["subtitle"]]
        for v in l["variants"]:
            text += [v["title"], v["subtitle"]] + list(v["tags"]) + list(v["meta"].get("keywords") or []) + re.findall(r"^#{2,3}\s+(.+)$", v["body"], re.M)
        terms[l["slug"]] = {w for t in text for w in toks(str(t)) if len(w) > 2}
    df = {}
    for ws in terms.values():
        for w in ws:
            df[w] = df.get(w, 0) + 1
    n = max(len(terms), 1)
    return terms, {w: math.log(n / c) for w, c in df.items()}


def homework_by_content(f, lessons, owner="", cache={}):
    """Lesson front matter can add `keywords: [double diamond, ...]` for terms the lesson text doesn't contain.
    Best lesson by distinctive shared words between the file (its name, and its text if .md/.txt) and the lesson
    content. Needs a clear winner: enough weight, and well ahead of the runner-up."""
    key = id(lessons)
    if key not in cache:
        cache.clear()
        cache[key] = lesson_terms(lessons)
    terms, idf = cache[key]
    words = toks(re.sub(rf"^{re.escape(owner)}[-_ ]", "", f.stem, flags=re.I)) - toks(owner.replace("-", " "))
    if f.suffix.lower() in (".md", ".txt"):
        words |= toks(f.read_text(encoding="utf-8", errors="ignore")[:20000])
    scores = sorted(((sum(idf[w] for w in words & ws), slug) for slug, ws in terms.items()), reverse=True)
    if scores and scores[0][0] >= 2.0 and (len(scores) < 2 or scores[0][0] >= 1.3 * scores[1][0]):
        return next(l for l in lessons if l["slug"] == scores[0][1])
    return None


def homework_lesson_for(f, m, lessons):
    """Which lesson a loose homework file belongs to, and why. (1) the file name names the lesson, (2) its name or text matches lesson content (tags, headings), else (3) the
    mentee's latest dated session on or before the file's modified date, else (4) their last completed session."""
    pages = [l for l in lessons if l["has_page"]]
    name = re.sub(r"[^a-z0-9]+", " ", f.stem.lower())
    ft = toks(f.stem)
    best, best_n = None, 0
    for l in pages:
        slug_hit = len(l["slug"]) > 3 and l["slug"].replace("-", " ") in name
        n = 99 if slug_hit else len(ft & toks(l["title"]))
        if n > best_n and (slug_hit or n >= 2):
            best, best_n = l, n
    if best:
        return best, "file name matches the lesson"
    hit = homework_by_content(f, lessons, m["slug"])
    if hit:
        return hit, "file name / text matches the lesson content"
    from datetime import datetime
    when = datetime.fromtimestamp(f.stat().st_mtime)
    dated, done = [], []
    for r in mentee_rows(m):
        l = lesson_for(r, m, lessons)
        if not l:
            continue
        if r["status"].lower().startswith("completed"):
            done.append(l)
        try:
            dated.append((datetime.strptime(r["date"], "%d %b %Y"), l))
        except ValueError:
            pass
    before = [x for x in dated if x[0].date() <= when.date()]
    if before:
        return max(before, key=lambda x: x[0])[1], "latest session on or before the file date"
    if done:
        return done[-1], "last completed session"
    return None, ""


def sort_loose_homework(mentees, lessons):
    """Files dropped straight into Mentees/<name>/homework/ are moved into homework/<lesson-slug>/ so the lesson page
    picks them up. Returns the number moved. Files that can't be matched stay put (shown under 'General')."""
    moved = 0
    for m in mentees:
        hw = MENTEES / m["slug"] / "homework"
        if not hw.is_dir():
            continue
        for f in sorted(x for x in hw.iterdir() if x.is_file() and visible(x)):
            lesson, why = homework_lesson_for(f, m, lessons)
            if not lesson:
                print(f"  homework: no lesson found for {m['slug']}/{f.name}; left in place (add a lesson name to the file name)")
                continue
            dest_dir = hw / lesson["slug"]
            dest_dir.mkdir(exist_ok=True)
            dest = dest_dir / f.name
            if dest.exists():
                dest = dest_dir / f"{f.stem}-{int(f.stat().st_mtime)}{f.suffix}"
            shutil.move(str(f), str(dest))
            moved += 1
            print(f"  homework: {m['slug']}/{f.name} -> {lesson['slug']}/ ({why})")
    return moved


def build():
    FALLBACK_USED.clear()
    for needed in (DESIGN_SYSTEM, PROGRAMS_SRC, LESSONS_DIR):
        if not needed.exists():
            sys.exit(f"Missing folder: {needed}")
    started = time.time()
    for d in ("lessons", "programs", "mentees"):   # pages are overwritten in place; stale ones are pruned at the end, so open pages never 404 mid-build
        (OUT / d).mkdir(parents=True, exist_ok=True)
    shutil.rmtree(ASSETS / "lesson-assets", ignore_errors=True)
    copy_design_system()

    programs = load_programs()
    lessons = load_lessons()
    MENTEE_PUBLISHED.clear()
    mentees = load_mentees()
    if sort_loose_homework(mentees, lessons):   # loose homework files were filed into lesson folders: reload
        lessons = load_lessons()
        MENTEE_PUBLISHED.clear()
        mentees = load_mentees()
    prune_mentee_assets()

    stage_rank = {s: i for i, s in enumerate(STAGES.values())}
    lessons.sort(key=lambda l: (stage_rank.get(l["stage"], 99), l["title"].lower(), l["slug"]))
    by_slug = {l["slug"]: l for l in lessons}
    by_stem = {}
    for l in lessons:
        by_stem[l["slug"]] = l["slug"]
        for v in l["variants"]:
            by_stem[re.sub(r"-lesson$", "", v["path"].stem)] = l["slug"]

    prepare_lesson_assets(lessons)

    by_program = {}
    for p in programs:
        sess_with = {s["idx"] for s in p["sessions"] if any((p["slug"], s["idx"]) in l["programs"] and l["has_page"] for l in lessons)}
        by_program[p["slug"]] = len(sess_with)
    counts = {"sessions": sum(len(p["sessions"]) for p in programs), "by_program": by_program}

    (OUT / "index.html").write_text(build_index(programs, lessons, mentees, counts), encoding="utf-8")
    (OUT / "lessons.html").write_text(build_lessons_index(lessons), encoding="utf-8")
    (OUT / "programs.html").write_text(build_programs_index(programs, counts), encoding="utf-8")
    (OUT / "private-training.html").write_text(build_mentees_page(mentees), encoding="utf-8")
    for m in mentees:
        (OUT / "mentees" / f"{m['slug']}.html").write_text(build_mentee_page(m, lessons, programs), encoding="utf-8")
    for p in programs:
        (OUT / "programs" / f"{p['slug']}.html").write_text(build_program_page(p, by_slug), encoding="utf-8")
    for l in lessons:
        if l["has_page"]:
            (OUT / "lessons" / f"{l['slug']}.html").write_text(build_lesson_page(l, lessons, programs, by_stem), encoding="utf-8")

    for d in ("lessons", "programs", "mentees"):   # drop pages for lessons / programmes / mentees that no longer exist
        for old in (OUT / d).glob("*.html"):
            if old.stat().st_mtime < started:
                old.unlink()
    (ASSETS / "build-stamp.txt").write_text(str(time.time_ns()), encoding="utf-8")  # written last: open pages reload on it
    pages = sum(1 for l in lessons if l["has_page"])
    soon = [l["title"] for l in lessons if not l["variants"]]
    health_total = print_health(mentee_health(mentees, lessons)) if "--quiet" not in sys.argv else 0
    print(f"Built {len(programs)} programs, {len(lessons)} lesson cards ({pages} pages), {len(mentees)} mentees")
    for l in lessons:
        extras = []
        if len(l["variants"]) > 1:
            extras.append(f"{len(l['variants'])} versions")
        if l["decks"] or l["pdfs"] or l["links"]:
            extras.append(f"{len(l['decks'])} deck, {len(l['pdfs'])} pdf, {len(l['links'])} link")
        if l["homework"]:
            extras.append(f"{len(l['homework'])} homework")
        print(f"  {l['stage']:<12} {l['slug']:<36}{'  [coming soon]' if not l['variants'] else ''}  {'; '.join(extras)}")
    if FALLBACK_USED:
        print(f"  note: program links for {', '.join(FALLBACK_USED)} come from the fallback table (no lesson file to hold a `programs:` line yet)")
    unmapped = [l["slug"] for l in lessons if l["variants"] and not l["programs"]]
    if unmapped:
        print(f"  note: no `programs:` line in: {', '.join(unmapped)}")
    return lessons


def signature():
    """Cheap fingerprint of everything the site is built from."""
    sig = []
    roots = [LESSONS_DIR, MENTEES, PROGRAMS_SRC]
    for root in roots:
        if not root.exists():
            continue
        for dirpath, dirnames, filenames in os.walk(root):
            dirnames[:] = [d for d in dirnames if not d.startswith((".", "_")) and d not in ("transcripts", "node_modules")]
            for fn in filenames:
                if fn.startswith("."):
                    continue
                fp = os.path.join(dirpath, fn)
                try:
                    st = os.stat(fp)
                except OSError:
                    continue
                sig.append((fp, st.st_mtime_ns, st.st_size))
    return hash(tuple(sorted(sig)))


def watch(poll=2.0):
    import time
    print(f"Watching {LESSONS_DIR}\n         {MENTEES} (homework)\n  -> rebuilding {OUT.name}/ on any change. Ctrl+C to stop.\n")
    last = signature()  # the caller has just built; only react to changes after this
    while True:
        try:
            cur = signature()
            if cur != last:
                time.sleep(1.0)  # let a save/sync finish
                if signature() != cur:
                    continue
                print(time.strftime("[%H:%M:%S]"), "change detected, rebuilding…")
                try:
                    build()
                except SystemExit as e:
                    print("  build skipped:", e)
                except Exception as e:  # keep watching after a bad file
                    print("  build failed:", repr(e))
                last = cur
                print()
            time.sleep(poll)
        except KeyboardInterrupt:
            print("\nStopped.")
            return


def serve_and_watch(port):
    """Serve the site, open it in the browser, and rebuild + auto-refresh on every change."""
    import functools
    import http.server
    import threading
    import urllib.request
    import webbrowser

    class Quiet(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *args):
            pass

    try:
        rel = OUT.relative_to(ROOT).as_posix()   # serve the whole 03_Mentoring folder so ../Mentees/... links work
        serve_dir, base = ROOT, f"http://localhost:{port}/{rel}/"
    except ValueError:
        serve_dir, base = OUT, f"http://localhost:{port}/"
    try:
        srv = http.server.ThreadingHTTPServer(("", port), functools.partial(Quiet, directory=str(serve_dir)))
        threading.Thread(target=srv.serve_forever, daemon=True).start()
        print(f"Serving {serve_dir} on port {port}")
    except OSError:
        try:
            urllib.request.urlopen(base + "index.html", timeout=2)
            print(f"Port {port} is already serving the Homepage - reusing it")
        except Exception:
            sys.exit(f"Port {port} is busy with something else. Try:  --serve --port 8811")
    print(f"Open: {base}index.html   (pages refresh themselves after each rebuild)\n")
    webbrowser.open(base + "index.html")
    watch()


def main():
    args = sys.argv[1:]
    port = int(args[args.index("--port") + 1]) if "--port" in args else 8800
    if "--serve" in args:
        build()
        serve_and_watch(port)
    elif "--watch" in args:
        build()
        watch()
    else:
        build()


if __name__ == "__main__":
    main()
