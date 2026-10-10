# Slide Deck Outline — Systematic AI Prototyping: Lesson 0 (Program Introduction)

> **Source of truth:** `lesson-0-program-introduction.md` is the source of truth for content. This file only covers slide-specific concerns, matched to the format of `lesson-1-slide-outline.md`.
> **Short by design.** Lesson 0 is the first slice of Session 1, not its own session. The deck runs straight from cover to a bridge into Lesson 1, with no section dividers and no padding.
> **Speaker notes are bullets, not prose.** They need to be scannable while teaching standing up, per `CLAUDE.md` and the house rule on this. This file follows it; `lesson-1-slide-outline.md` currently doesn't, worth a separate pass if you want that fixed too.

---

## Prompt to use

```
Using the outline in this file, build an HTML slide deck for Systematic AI Prototyping — Lesson 0 (Program Introduction).

Follow the rules in _system/rules/SLIDE_DECK_RULES.md exactly.
File: library/lessons/03-develop/ai-prototype-development/learning/Systematic AI Prototyping - Lesson 0.dc.html
Copy tokens.css and deck-stage.js locally so the deck is self-contained.
Match the visual system already established in Build the Framework First.dc.html and Systematic AI Prototyping - Lesson 1.dc.html: same tokens, same layout types, same restraint.
This deck is short and stays that way: 6 slides, no section dividers, straight through cover to bridge. Don't pad it out to look more substantial than it is.

VISUAL DESIGN DIRECTION — apply globally to every slide:

- Prefer diagrams, flows, and visual metaphors over bullet lists. If content can be shown
  as a shape, flow, or diagram, do that instead of listing text.
- Use inline SVG for all diagrams. Keep them flat, clean, and minimal.
  Use only token colours (--sienna, --ochre, --sage, --ink, --paper) plus the deck's purple/violet accent.
- Avoid centred bullet lists. Use .process or .numbered layouts with visual numbering.
- Slide 3 (Choosing an AI Tool) uses the comparison-table supplementary layout from SLIDE_DECK_RULES.md §9 (mono headers, hairline row borders), not a numbered or process layout.
```

---

## Session metadata

| Field | Value |
|---|---|
| Project name (Claude Design sidebar) | Systematic AI Prototyping — Lesson 0 |
| File name | Systematic AI Prototyping - Lesson 0.dc.html |
| Cover title (on-slide) | One Method, Four Weeks |
| Subtitle | What this arc builds, lesson by lesson, and how AI fits into each one |
| Instructor | Winnie Nguyen — Senior Product Designer at NAB |
| Program | Private Training |
| Year | 2026 |
| Previous session | — (opens Session 1) |
| Next session | Lesson 1: Project Setup & the Pattern-First Method, same session, immediately after |
| Cover visual | Four small nodes on a single line, left to right, each numbered 1–4. The fourth node opens into a tiny "live URL" glyph instead of a plain dot, previewing the arc's shape without giving any lesson away in detail |

*Cover title is a placeholder. Swap it for whatever you'd rather open with; nothing downstream depends on the exact wording.*

---

## Slide structure — 6 slides

> **6 slides, fully specified, no section dividers.** Runs straight: cover → curriculum → objectives → tool choice → materials → bridge into Lesson 1. Nothing here re-teaches content Lesson 1 itself will cover; this deck previews outcomes and clears logistics, then hands off.

---

## 0. Cover

---

### COVER
- Title: One Method,\nFour Weeks
- Subtitle: What this arc builds, lesson by lesson, and how AI fits into each one
- Kicker/date line: 2026 · PRIVATE TRAINING
- Author: Winnie Nguyen — Senior Product Designer at NAB
- 🎨 Visual: Four small nodes on one horizontal line, numbered 1–4, evenly spaced. Node 4 looks slightly different: a small "live URL" glyph instead of a plain dot, hinting at Lesson 4's outcome without explaining it. Keep it restrained and mostly whitespace. This is an orientation cover, not a teaching-moment one.

---

## 1. The four-lesson arc

---

### PROCESS · Four lessons, each building on the last
- Kicker: What Session 1 kicks off
- Title: Four lessons. *Each one builds on the last.*
- On-slide: 4-step horizontal track, one step per lesson, each step showing its number and a short, scannable label:
  1. Change the mindset
  2. Build the prototype
  3. Stitch the journey
  4. Publish with GitHub
- Speaker notes:
  - One lesson per week. Nothing here is a disconnected exercise
  - Each step's artifact is literally what the next week's lesson opens with
  - If the student wants the "why" first, point at Lesson 4's outcome: a real, live URL, not just a mockup
  - Keep this slide moving. It's a map, not the destination
- 🎨 Visual: `.process` layout, `repeat(4,1fr)` track, matching the folder-tree/process visual language already used in `Build the Framework First.dc.html`.

---

## 2. What you'll be able to do

---

### NUMBERED · Learning objectives
- Kicker: By the end of this arc
- Title: What you'll be able to do
- On-slide: 6 numbered objectives, verbs bolded:
  1. **Organise** a prototype project folder that scales
  2. **Explain** why pattern-first beats screen-by-screen
  3. **Generate** a component inventory and interaction pattern from your design system
  4. **Build** a working, browser-viewable prototype from those files
  5. **Stitch** multiple screens into one demoable journey
  6. **Publish** the finished prototype to a live URL
- Speaker notes:
  - Read fast. This is a preview, not a lesson, so don't teach any of these yet
  - Worth returning to at Lesson 3 or 4 as a "look how far you've come" checkpoint
  - If a student looks worried by item 6 (Git/GitHub), reassure them: Lesson 4 has its own guide, nothing to prep now beyond having an account
- 🎨 Visual: `.numbered` layout, six items, visual numbering rather than bullet dots.

---

## 3. Choosing an AI tool

---

### DIAGRAM · Choosing an AI tool
- Kicker: Pick your tool today
- Title: One tool, for the whole arc.
- On-slide: comparison table, 6 columns (Tool / Type / Design-system support / Strengths / Weaknesses / Use when), 5 rows, sorted by design-system support from highest to lowest. Same table as `lesson-0-program-introduction.md`'s "Choosing an AI Tool" section.
- Speaker notes:
  - Sorted by design-system support, highest to lowest. Read it by group, not row by row
  - This slide names specific tools on purpose. It's a dated, deliberate exception to the usual "no tool names" rule (see sync note in the lesson file)
  - Decide today, not later. Lesson 1's folder setup and token sync both depend on the choice
  - Snapshot as of September 2026. Say so out loud if the student's read up on something newer
- 🎨 Visual: Comparison-table supplementary layout (`_system/rules/SLIDE_DECK_RULES.md` §9): mono headers, hairline row borders. Matches the same slide already specified in `lesson-1-slide-outline.md`.

---

## 4. What to bring

---

### PRACTICE · Materials checklist
- Kicker: Before we start building
- Title: Have this ready.
- On-slide: checklist:
  - Your own design system (Figma file, tokens + components)
  - One AI tool chosen from the comparison above
  - A second AI tool for the Lesson 2 comparison (optional)
  - A GitHub account and GitHub Desktop, needed by Lesson 4, not today
- Speaker notes:
  - Confirm the design system exists and is reasonably clean before moving on. At minimum, key components need a default state plus one other
  - GitHub items are a Lesson 4 dependency, not a today one. Don't let it stall this session
  - Flag any gap now, in front of the student, rather than discovering it mid-arc
- 🎨 Visual: `.practice` layout, checklist styling, not a diagram.

---

## 5. Straight into Lesson 1

---

### STATEMENT · Bridge into Lesson 1
- Kicker: Orientation's done
- Title: Let's set up your project folder.
- Lead: No break here. Lesson 1 runs right now, in the same sitting.
- Speaker notes:
  - This is a hand-off, not a close. Don't treat it like the end of a session
  - Move straight into Lesson 1's cover
- 🎨 Visual: Plain text slide, no diagram. Keep it restrained, matching the "STATEMENT" slides elsewhere in this deck family. No `END` layout here, since the session isn't ending.

---

*Created by Winnie Nguyen · Private Training · Last updated September 2026*
