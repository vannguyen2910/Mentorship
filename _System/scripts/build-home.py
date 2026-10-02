#!/usr/bin/env python3
"""
build-home.py — Mentoring Hub homepage generator

Run from anywhere:
    python3 _System/scripts/build-home.py          (one build)
    python3 _System/scripts/build-home.py --watch  (keep rebuilding on any change)

Reads
  - Programs  : <WEBSITE>/src/pages/training/programs/*.sessions.js + *.jsx   (live program pages)
  - Lessons   : Library/lessons/**/<topic>-lesson.md                          (+ EXTRA_LESSONS below)
  - Mentees   : <MENTEES>/<name>/plan|sessions|assessments                    (internal only)
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
        data = json.loads(t[t.index("["): t.rindex("]") + 1])
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


def sync_tree(src, dest):
    """Mirror src into dest (adds, updates and removes files)."""
    want = set()
    if src.exists():
        for f in sorted(src.rglob("*")):
            if f.is_file() and not any(part.startswith((".", "_")) for part in f.relative_to(src).parts):
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
            slide_files = [f for f in sorted(sdir.rglob("*")) if f.is_file() and visible(f)] if sdir.exists() else []
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
        roadmap = re.search(r"^##\s+(Roadmap to .*)$", body, re.M)
        name = meta.get("student") or d.name.replace("-", " ").title()
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
        people.append({
            "name": name, "slug": d.name,
            "level": meta.get("level", ""), "target": meta.get("target_level", ""),
            "program": (roadmap.group(1).replace("Roadmap to ", "") if roadmap else readme_program),
            "planned": int(planned) if str(planned).isdigit() else None,
            "logged": len(sessions), "baseline": bool(assess), "has_plan": bool(plan or plan_pdf),
            "status": "Completed" if closeout else ("In progress" if (sessions or plan or plan_pdf) else "Not started"),
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


def mentee_card(m):
    initials = "".join(w[0] for w in m["name"].split()[:2]).upper()
    tone = {"Completed": "success", "In progress": "primary", "Not started": "default"}[m["status"]]
    if m["planned"]:
        pct = min(100, round(100 * m["logged"] / m["planned"]))
        prog = f'<div class="mentee__bar"><span style="width:{pct}%"></span></div><div class="mentee__count">{m["logged"]} of {m["planned"]} sessions logged</div>'
    elif m["logged"]:
        prog = f'<div class="mentee__count">{m["logged"]} session{"s" if m["logged"] != 1 else ""} logged</div>'
    else:
        prog = '<div class="mentee__count">No sessions logged yet</div>'
    checks = "".join(
        f'<li class="{"is-done" if ok else ""}">{"✓" if ok else "○"} {label}</li>'
        for label, ok in [("Coaching plan", m["has_plan"]), ("Baseline assessment", m["baseline"])]
    )
    links = " · ".join(f'<a href="{u}">{esc(t)}</a>' for t, u in m["links"])
    return f"""<article class="mentee">
  <div class="mentee__head"><div class="mentee__avatar" aria-hidden="true">{esc(initials)}</div>
    <div><h3 class="mentee__name">{esc(m['name'])}</h3><div class="mentee__level">{esc(m['level'])}</div></div>
    {chip(m['status'], tone)}
  </div>
  <p class="mentee__prog">{esc(m['program'] or 'Program not set')}</p>
  {prog}
  <ul class="mentee__checks">{checks}</ul>
  <div class="mentee__links">{links}</div>
</article>"""


def page_header(eyebrow, title, desc, note=""):
    return f"""<div class="page-header"><div class="page-eyebrow">{eyebrow}</div>
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
  {big("private-training.html", "02 · Mentees", "Private Training", "Everyone I coach one to one: their program, progress, coaching plan and baseline assessment. Internal only.", f"{len(mentees)} mentees", "yellow")}
  {big("programs.html", "03 · Programs", "Programs", "The offers people enrol in, such as UI/UX Fundamentals and the roadmaps to Mid and Senior, with every session and its lesson.", f"{len(programs)} programs", "gray")}
</section>
"""
    return page("Training Hub — Winnie Nguyen", body, 0, "Lesson library, private training and programs.")


def build_lessons_index(lessons):
    stages = ["All"] + [s for s in STAGES.values() if any(l["stage"] == s for l in lessons)]
    filters = "".join(
        f'<button type="button" role="tab" class="tabs__tab{" tabs__tab--active" if s == "All" else ""}" data-stage="{s}" aria-selected="{"true" if s == "All" else "false"}">{s}</button>' for s in stages
    )
    body = f"""{page_header("Lesson Library", "Lesson Library", "Click a lesson to read the full plan: timing, activities and facilitator notes.")}
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
    body = f"""{page_header("Programs", "Programs", "Read from the live program pages, so titles and curriculum stay in sync.")}
<section class="section section--tight">
  <div class="cl-grid prog-grid">{''.join(program_card(p, counts['by_program'].get(p['slug'], 0)) for p in programs)}</div>
</section>"""
    return page("Programs — Training Hub", body, 0, "All programs.", active="programs")


def build_mentees_page(mentees):
    note = '<p class="home-section__note" style="margin-top:var(--space-4)">Internal view. Do not publish this page: it names the people I coach.</p>'
    body = f"""{page_header("Private Training", "Private Training", "Everyone I coach one to one.", note)}
<section class="section section--tight">
  <div class="mentee-grid">{''.join(mentee_card(m) for m in mentees)}</div>
</section>"""
    return page("Private Training — Training Hub", body, 0, "Mentees.", active="mentees")


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
  var showTab = group('[data-tab-btn]', '[data-tab-panel]', 'data-tab-id', function (id) { history.replaceState(null, '', id === 'lesson' ? location.pathname : '#' + id); });
  var showVar = group('[data-var-btn]', '[data-var-panel]', 'data-var-id');
  var h = (location.hash || '').replace('#', '');
  showTab(['slides', 'homework'].indexOf(h) > -1 && document.querySelector('[data-tab-id="' + h + '"]') ? h : 'lesson');
  if (document.querySelector('[data-var-btn]')) showVar('0');
  var decks = [].slice.call(document.querySelectorAll('[data-deck-btn]'));
  decks.forEach(function (b) { b.addEventListener('click', function () {
    var f = document.getElementById('deck-frame'); f.src = b.dataset.src; document.getElementById('deck-open').href = b.dataset.src;
    decks.forEach(function (x) { x.classList.toggle('tabs__tab--active', x === b); x.setAttribute('aria-selected', x === b); });
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


def slides_panel(l):
    empty = '<div class="tp-slides tp-slides--empty"><strong>No slides yet</strong><span>Add a deck (.html) or .pdf to this lesson\'s <code>slides/</code> folder, or a <code>slides:</code> link in the lesson front matter.</span></div>'
    base = f"../assets/lessons/{quote(l['slug'])}/slides/"
    parts = []
    if l["decks"]:
        srcs = [base + quote(d.relative_to(l["folder"] / "slides").as_posix()) for d in l["decks"]]
        picker = ""
        if len(l["decks"]) > 1:
            picker = '<div class="tabs tabs--pill deck-picker"><div class="tabs__list" role="tablist" aria-label="Choose a deck">' + "".join(
                f'<button type="button" role="tab" class="tabs__tab{" tabs__tab--active" if i == 0 else ""}" data-deck-btn data-src="{src}">{esc(re.sub(chr(46) + "dc$", "", d.stem))}</button>'
                for i, (d, src) in enumerate(zip(l["decks"], srcs))) + "</div></div>"
        parts.append(f"""{picker}<div class="tp-slides"><iframe id="deck-frame" src="{srcs[0]}" title="Lesson slides" allowfullscreen loading="lazy"></iframe></div>
<p class="tp-slides__link"><a id="deck-open" href="{srcs[0]}" target="_blank" rel="noopener">Open slides full screen ↗</a></p>""")
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
        info = f'<div class="tp-hw__info"><strong>{esc(h["label"])}</strong><span>by {esc(h["mentee"])}</span></div>'
        if h["is_image"]:
            cards.append(f'<a class="tp-hw__card" href="{h["url"]}" target="_blank" rel="noopener"><div class="tp-hw__thumb"><img src="{h["url"]}" alt="{esc(h["label"])}" loading="lazy"></div>{info}</a>')
        else:
            ext = FILE_ICON.get(h["ext"], h["ext"].upper()[:4] or "FILE")
            cards.append(f'<a class="tp-hw__card" href="{h["url"]}" target="_blank" rel="noopener"><div class="tp-hw__thumb"><span class="file-card__ext">{esc(ext)}</span></div>{info}</a>')
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


def build():
    FALLBACK_USED.clear()
    for needed in (DESIGN_SYSTEM, PROGRAMS_SRC, LESSONS_DIR):
        if not needed.exists():
            sys.exit(f"Missing folder: {needed}")
    for d in ("lessons", "programs"):  # regenerate from scratch so removed lessons don't linger
        shutil.rmtree(OUT / d, ignore_errors=True)
        (OUT / d).mkdir(parents=True, exist_ok=True)
    shutil.rmtree(ASSETS / "lesson-assets", ignore_errors=True)
    copy_design_system()

    programs = load_programs()
    lessons = load_lessons()
    mentees = load_mentees()

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
    for p in programs:
        (OUT / "programs" / f"{p['slug']}.html").write_text(build_program_page(p, by_slug), encoding="utf-8")
    for l in lessons:
        if l["has_page"]:
            (OUT / "lessons" / f"{l['slug']}.html").write_text(build_lesson_page(l, lessons, programs, by_stem), encoding="utf-8")

    (ASSETS / "build-stamp.txt").write_text(str(time.time_ns()), encoding="utf-8")  # written last: open pages reload on it
    pages = sum(1 for l in lessons if l["has_page"])
    soon = [l["title"] for l in lessons if not l["variants"]]
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
