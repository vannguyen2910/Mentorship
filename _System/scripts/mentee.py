#!/usr/bin/env python3
"""
mentee.py — set up mentees and log sessions, so the site (build-home.py) needs no hand-editing.

  python3 _System/scripts/mentee.py new "Full Name" [--role R] [--level L] [--target T] [--program P]
                                     [--sessions N] [--start YYYY-MM-DD] [--cadence C] [--goal G] [--project X]
  python3 _System/scripts/mentee.py log <mentee> --topic "Topic" [--n N] [--date YYYY-MM-DD] [--status Completed]
                                     [--lesson slug] [--playback "text or https://link"] [--build]
  python3 _System/scripts/mentee.py check       (rebuild and print the mentee health check: missing baseline, lesson, slides, playback...)
  python3 _System/scripts/mentee.py migrate     (one-off: write mentee.md + sessions.md for mentees that lack them)

Each mentee folder keeps two public-facing source files; everything else on their page is derived:
  mentee.md    front matter: name, role, level, target, program, sessions, start, end, cadence, goal, project, status
  sessions.md  table: | # | Topic | Date | Status | Lesson | Playback |
Private files (recaps in sessions/, transcripts/, assessments/) are never published.
"""

import argparse
import datetime as dt
import importlib.util
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
MENTEES = ROOT / "Mentees"
TEMPLATES = ROOT / "_System" / "learning templates"
SUBDIRS = ["artifacts", "assessments", "homework", "plan", "sessions", "slides", "transcripts"]
HEADER = "| # | Topic | Date | Status | Lesson | Playback |\n|---|---|---|---|---|---|\n"


def load_build():
    spec = importlib.util.spec_from_file_location("build_home", Path(__file__).with_name("build-home.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def slugify(name):
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def find_mentee(q):
    q = slugify(q)
    hits = [d for d in MENTEES.iterdir() if d.is_dir() and not d.name.startswith((".", "_")) and (d.name == q or q in d.name)]
    if len(hits) != 1:
        sys.exit(f"Mentee '{q}': {'no match' if not hits else 'ambiguous: ' + ', '.join(h.name for h in hits)}")
    return hits[0]


def q(v):
    return '"' + str(v).replace('"', "'") + '"'


def write_front(path, fields):
    lines = ["---"] + [f"{k}: {q(v) if isinstance(v, str) else v}" for k, v in fields.items() if v not in ("", None)] + ["---", ""]
    path.write_text("\n".join(lines), encoding="utf-8")


def read_rows(path):
    rows = []
    if path.exists():
        for line in path.read_text(encoding="utf-8").splitlines():
            cells = [c.strip() for c in line.strip().strip("|").split("|")] if line.strip().startswith("|") else []
            if len(cells) >= 4 and cells[0].isdigit():
                cells += [""] * (6 - len(cells))
                rows.append(cells[:6])
    return sorted(rows, key=lambda r: int(r[0]))


def write_rows(path, rows):
    cells = lambda r: "| " + " | ".join(c.replace("|", "/") for c in r) + " |"
    path.write_text("# Sessions\n\nPublic session log (topic, date, status, lesson, playback). Edit here or run `mentee.py log`.\n\n"
                    + HEADER + "\n".join(cells(r) for r in rows) + "\n", encoding="utf-8")


def best_lesson(topic):
    """Library lesson whose title shares >= 75% of the shorter title's words with the topic."""
    b = load_build()
    toks = lambda t: {w for w in re.sub(r"[^a-z0-9]+", " ", t.lower().replace("&", " and ")).split() if w not in {"and", "for", "the", "a", "of", "to", "in", "with", "your"}}
    best, score = None, 0.0
    for l in b.load_lessons():
        if not l["has_page"]:
            continue
        a, c = toks(topic), toks(l["title"])
        if a and c and len(a & c) / min(len(a), len(c)) > score:
            best, score = l["slug"], len(a & c) / min(len(a), len(c))
    return best if score >= 0.75 else ""


# ── new ──────────────────────────────────────────────────────────────────────

def cmd_new(a):
    slug = slugify(a.name)
    d = MENTEES / slug
    if (d / "mentee.md").exists():
        sys.exit(f"{d} already has a mentee.md")
    for sub in SUBDIRS:
        (d / sub).mkdir(parents=True, exist_ok=True)
    write_front(d / "mentee.md", {"name": a.name, "role": a.role, "level": a.level, "target": a.target, "program": a.program,
                                  "sessions": a.sessions, "programme_page": a.programme_page, "start": a.start, "cadence": a.cadence, "goal": a.goal, "project": a.project})
    write_rows(d / "sessions.md", [])
    metrics = ["Date taken", "Target level", "Career readiness", "Designer profile", "Craft maturity", "Behaviour maturity", "AI readiness"]
    (d / "assessment.md").write_text("# Assessment\n\nSelf-assessment run at the start and end of the programme (fill Baseline at session 1, Post-training at close-out).\n\n"
                                     "| Metric | Baseline | Post-training |\n|---|---|---|\n" + "\n".join(f"| {m} |  |  |" for m in metrics) + "\n", encoding="utf-8")
    plan = d / "plan" / f"Coaching Plan - {a.name}.md"
    if not plan.exists():
        t = (TEMPLATES / "_template-coaching-plan.md").read_text(encoding="utf-8")
        t = t.replace('student: ""', f'student: "{a.name}"', 1).replace("sessions: 8 ", f"sessions: {a.sessions} ", 1)
        t = re.sub(r'level: ""', f'level: "{a.level}"', t, 1)
        t = re.sub(r'target_level: ""', f'target_level: "{a.target}"', t, 1)
        t = re.sub(r'cadence: ""', f'cadence: "{a.cadence}"', t, 1)
        t = re.sub(r'project_vehicle: ""', f'project_vehicle: "{a.project}"', t, 1)
        plan.write_text(t, encoding="utf-8")
    print(f"Created Mentees/{slug}/  (mentee.md, sessions.md, assessment.md, plan/{plan.name}, empty folders for the rest)")
    print("Still to do (per CLAUDE.md): run the self-assessment tool with them and save the baseline in assessments/.")
    if a.build:
        subprocess.run([sys.executable, str(Path(__file__).with_name("build-home.py"))], check=True)


# ── log ──────────────────────────────────────────────────────────────────────

def cmd_log(a):
    d = find_mentee(a.mentee)
    sess = d / "sessions.md"
    rows = read_rows(sess)
    n = a.n or (max((int(r[0]) for r in rows), default=0) + 1)
    old = next((r for r in rows if int(r[0]) == n), None)
    topic = a.topic or (old[1] if old else "")
    if not topic:
        sys.exit("--topic is required for a new session")
    lesson = a.lesson or (old[4] if old else "") or best_lesson(topic)
    row = [str(n), topic, a.date or (old[2] if old else dt.date.today().isoformat()), a.status or (old[3] if old else "Completed"),
           lesson, a.playback if a.playback is not None else (old[5] if old else "")]
    rows = [r for r in rows if int(r[0]) != n] + [row]
    write_rows(sess, sorted(rows, key=lambda r: int(r[0])))

    # private recap from the template (never published)
    if not list((d / "sessions").glob(f"session-{n:02d}-*.md")):
        t = (TEMPLATES / "_template-session.md").read_text(encoding="utf-8")
        first = d.name.split("-")[0].title()
        t = t.replace('title: ""', f'title: "Session {n} — {topic}"', 1).replace('student: ""', f'student: "{first}"', 1)
        t = t.replace("session_number: 1", f"session_number: {n}", 1).replace("date: 2026-00-00", f"date: {row[2]}", 1)
        (d / "sessions").mkdir(exist_ok=True)
        rec = d / "sessions" / f"session-{n:02d}-{slugify(topic)[:40]}.md"
        rec.write_text(t, encoding="utf-8")
        print(f"Created private recap {rec.relative_to(ROOT)}")

    slides = [f.name for f in (d / "slides").glob("*") if re.match(rf"^(?:Session|Sesion|Day|Lesson)?\s*{n}\b", f.stem, re.I)] if (d / "slides").exists() else []
    print(f"{d.name} · session {n}: {topic} · {row[2]} · {row[3]}")
    print(f"  lesson:   {lesson or 'none matched (pass --lesson <slug>)'}")
    hint = f'none yet (drop a deck named "Session {n} - ..." into slides/)'
    print(f"  slides:   {', '.join(slides) if slides else hint}")
    print(f"  playback: {row[5] or 'not set (pass --playback)'}")
    if a.build:
        subprocess.run([sys.executable, str(Path(__file__).with_name("build-home.py"))], check=True)


# ── migrate ──────────────────────────────────────────────────────────────────

def cmd_migrate(_):
    b = load_build()
    for m in b.load_mentees():
        d = MENTEES / m["slug"]
        if not (d / "mentee.md").exists():
            prof = {}
            if (d / "profile.md").exists():
                prof = b.parse_front_matter((d / "profile.md").read_text(encoding="utf-8"))[0]
            write_front(d / "mentee.md", {
                "name": m["name"], "role": prof.get("role", ""), "level": m["level"], "target": m["target"], "program": m["program"],
                "sessions": m["planned"], "start": prof.get("start", ""), "end": prof.get("end", ""), "cadence": m["cadence"],
                "goal": prof.get("goal", ""), "project": m["project"],
                "status": {"Completed": "completed", "In progress": "in-progress"}.get(m["status"], "not-started")})
            print(f"wrote {m['slug']}/mentee.md")
        if not (d / "sessions.md").exists():
            lessons = {}
            if (d / "profile.md").exists():
                lessons = {int(n): sl for n, sl in re.findall(r"(\d+)\s*=\s*([\w-]+)", str(b.parse_front_matter((d / "profile.md").read_text(encoding="utf-8"))[0].get("lessons", "")))}
            rows = [[str(r["n"]), r["title"], r["date"], r["status"] or "Completed", lessons.get(r["n"], ""), m["playback"].get(r["n"], "")]
                    for r in b.mentee_rows(m)]
            write_rows(d / "sessions.md", rows)
            print(f"wrote {m['slug']}/sessions.md ({len(rows)} sessions)")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    n = sub.add_parser("new")
    n.add_argument("name")
    for k, default in [("role", ""), ("level", ""), ("target", ""), ("program", ""), ("start", dt.date.today().isoformat()), ("cadence", ""), ("goal", ""), ("project", "")]:
        n.add_argument(f"--{k}", default=default)
    n.add_argument("--sessions", type=int, default=8)
    n.add_argument("--programme-page", dest="programme_page", default="", help="slug of the Homepage/programs page, e.g. junior-to-mid-level")
    n.add_argument("--build", action="store_true")
    g = sub.add_parser("log")
    g.add_argument("mentee")
    g.add_argument("--topic")
    g.add_argument("--n", type=int)
    g.add_argument("--date")
    g.add_argument("--status")
    g.add_argument("--lesson")
    g.add_argument("--playback")
    g.add_argument("--build", action="store_true")
    sub.add_parser("check")
    sub.add_parser("migrate")
    a = ap.parse_args()
    {"new": cmd_new, "log": cmd_log, "migrate": cmd_migrate,
     "check": lambda _: subprocess.run([sys.executable, str(Path(__file__).with_name("build-home.py"))], check=True)}[a.cmd](a)


if __name__ == "__main__":
    main()
