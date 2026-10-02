---
title: ""
lesson_file: ""             # e.g. customer-understanding-lesson.md — the paired source-of-truth file
level: ""                   # Junior | Senior/Lead | (blank if the track has no split)
slide_count: 0
duration: "90 min"
status: draft                # draft | ready-to-build | matches-built-deck
built_deck: ""               # filename of the .html/.dc.html deck once one exists, else leave blank
last_synced: 2026-00-00      # date lesson.md and this file were last confirmed in sync
---

> **Source of truth:** `[lesson_file]`
> All content changes (activities, phases, timing, concepts) are made there first, then reflected here.
> This file contains only slide-specific concerns: layout types, on-slide text, visual hints, kickers, and speaker notes.
> See `CLAUDE.md` → Lesson file sync rule for what triggers an update on which side.

> **Layout vocabulary is fixed.** Every `###` slide header below must use one of the 15 types
> documented in `_System/Themes/slide-design/RULES.md` (Cover, Section divider, Statement, Numbered,
> Compare, Process, Quote, Milestone, Practice, End, Diagram, Formula, Image, plus the two
> remaining reserved slots). If a slide genuinely needs something none of these cover, add the
> type to `RULES.md` first — do not invent a one-off name here. `SECTION`, `COMPARISON`, and
> `ACTIVITY` are drift, not valid types — use `SECTION DIVIDER`, `COMPARE`, `MILESTONE`.

---

## Session metadata

| Field | Value |
|---|---|
| Program | <!-- ux-class \| private-training --> |
| Track / session | <!-- e.g. Track 3, Session 3 --> |
| Stage | <!-- Discover \| Define \| Develop \| Deliver \| Foundation --> |
| Prior session | <!-- what this hands off from --> |
| Next session | <!-- what this hands off to --> |
| Running example | <!-- e.g. food delivery — see framework files before introducing a new case --> |

---

## Slide structure — [N] slides

<!-- One line per section, mirroring the lesson.md Run-of-Show blocks in the same order. -->

---

## Standard slide entry

<!-- Every slide below follows this field set. Do not drop fields; write "None." rather than omitting one. -->

```
### [LAYOUT TYPE] · [Slide title / short label]
- Kicker: [eyebrow line above the title]
- Title: [on-slide title — line breaks written as \n]
- On-slide: [the actual visible text/labels — short, not prose. "None." if the layout has no body copy field]
- Speaker notes:
  - [one point per line, glanceable — never a prose paragraph]
  - [bold the beat that must not be missed]
  - [facilitation cues — timing, checkpoints — get their own bullet]
- 🎨 Visual hint: [SCHEMATIC / REAL / TYPOGRAPHIC, then the description]
```

Speaker notes are always bullets, 3–6 per slide. More than ~7 means the slide is carrying too much and should probably split. This applies to every slide in every outline, old or new — see `CLAUDE.md` and the mentoring-practice notes on why (read standing up, mid-session).

---

## Slides

<!-- COVER is locked. Copy this block as-is and change ONLY Stage, Title, Subtitle and Right panel photo.
     See CLAUDE.md → Cover slide rule. No badge, tag, session number, level or duration. -->

### COVER
- Year: 2026 · Winnie Nguyen
- Stage: [Foundation | Discover | Define | Develop | Deliver | Leader Level]   <!-- from the lesson folder, no number -->
- Title: [Line one]\n*[Accent line]*
- Subtitle: [One sentence, 12 words or fewer, no em dash]
- Author: Winnie Nguyen
- Credentials:
  - Senior Product Designer at NAB
  - Master of UX & Service Design
  - Product Design Instructor
- Right panel photo: [one line: real photo, subject and mood]
- Speaker notes:
  - [3–6 bullets]
- 🎨 Visual hint: Cover layout, fixed. White left panel with year line, stage label, title (accent on line 2) and subtitle. Right panel is the real photo with dark gradient overlay, name and three credential lines bottom-left.

---

<!-- Slide entries go here, in the standard field format above, one section-divider per lesson phase. -->
