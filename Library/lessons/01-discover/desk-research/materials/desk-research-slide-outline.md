# Slide Deck Outline: Desk Research

> **Source of truth:** `desk-research-lesson.md`
> All content changes (activities, phases, timing, concepts) must be made there first, then reflected here.
> This file contains only slide-specific concerns: layout types, visual hints, kickers, and structure.
> The Assumption Map content (types, formula, matrix) lives in `library/frameworks/assumption-map/framework-assumption-map.md`. The slides below apply that same framework to this session's evidence sources (competitor scan, other desk research sources, and the mentee's evaluation.md). It isn't a separate version of the framework.

> **How to use this file**
> Paste both this file and `desk-research-lesson.md` into your AI tool with the instruction below to generate a new slide deck.
>
> **Built deck:** `Desk Research Deck.html` in the lesson folder is built from this outline (35 slides, self-contained). The old `Audit & Desk Research Deck.html` is superseded and was replaced.

---

## Prompt to use

```
Using the outline in this file, create an HTML slide deck for Desk Research.

Follow the rules in _system/rules/SLIDE_DECK_RULES.md exactly.
Save the file to library/lessons/01-discover/desk-research/materials/deck.html.

VISUAL DESIGN DIRECTION: apply globally to every slide:
- Prefer diagrams, frameworks, and annotated tables over bullet lists.
- Use inline SVG for all diagrams. Clean, flat shapes using only token colours.
- For the Importance × Evidence matrix, draw a 2×2 grid with quadrant labels. Match the visual language of the Assumption Map matrix in the Customer Understanding deck since it's the same framework.
- For "Patterns, not screenshots," show 4 scattered small icons (from different sources: competitor, ticket, analytics, evaluation.md) converging into 1 labelled pattern icon with a connecting motion line.
- For "Close the Loop," draw the assumption map with 2-3 items visibly moving from Unconfirmed to Confirmed (arrow + before/after state).
- For the insight statement formula, reuse the weak-vs-strong stacked card pattern from the Assumption formula slide.
- For "Headline-first structure," use a stacked pyramid or inverted funnel: headline at top (largest), 3-4 insight blocks in the middle, appendix note faded at the bottom.
- File-card visuals (AI block and recap only) should look like a saved file: a small file-card icon with the filename in mono type, to reinforce these are literal saved assets, not abstract advice.
- Activity / milestone slides feel like full-bleed moments: kicker, time, title, prompt only. All four activities sit together in Part 5, after the teaching.
- AI slides (Part 6) use the standard light layouts. Deck rules do not allow dark section backgrounds.
- Part intro slides use a solid --sienna full-bleed background with part number and name only.
- Every slide should have one dominant visual element.
- Avoid centred bullet lists. Use .numbered or .process layouts with visual numbering instead.
- Four slides need a real image, not just an SVG icon: "What is desk research?", "Patterns, not screenshots," "What to look for," and "Headline-first structure." Each one's visual hint below specifies what to mock or source. Treat these as the slides worth spending extra production time on, everything else stays flat SVG.
```

---

## Session metadata

| Field | Value |
|---|---|
| Session title | Desk Research |
| Session number | Session 3 |
| Instructor | Winnie Nguyen |
| Program | Private Training |
| Year | 2026 |
| Previous session | Evaluate Current Experience |
| Next session | Customer Understanding |
| Cover photo | Designer comparing several products side by side on screen, notes and annotations visible. Diagnostic, evidence-gathering feel, not a whiteboard brainstorm. |

---

## Slide structure

> **90-minute slot, 83 minutes scripted across 35 slides, 7 minutes of intentional buffer.**
> Arc: Mindset → Teach (assumptions, desk research, synthesis, present) → Practise (four activities, by hand) → AI assist (brainstorm → .md → HTML, verified at each step) → Assignment.

---

## 1. Introduction

---

### COVER
- Year: 2026
- Day label: Session 3
- Title: Desk\n*Research*
- Subtitle: Look outward before you decide what the evidence says
- Author: Winnie Nguyen
- Right panel photo: Designer comparing several products side by side on screen, notes and annotations visible. Diagnostic, focused, not a brainstorm mood.

---

### DIAGRAM: Agenda
- Kicker: What we're doing today
- Title: Learn it.\nDo it. Then AI.
- 3 agenda items:
  1. **Teach:** Assumptions, desk research, synthesis, presenting
  2. **Practise:** Four short activities on your own project, by hand
  3. **AI assist:** Brainstorm, convert to .md, visualise in HTML
- 🎨 Visual hint: 3 numbered cards in a horizontal flow with arrows between them. Card 3 in a darker tone with a mono "AI" tag to signal the shift. Small caption: "Homework: your stakeholder pitch."

---

## 2. Opening: Mindset

---

### STATEMENT: Understand before you redesign
- Kicker: Before we start
- Title: You can't fix\na system you\nhaven't *mapped.*
- Lead: A design decision made without a grounded picture of the current state is just a guess, and guesses compound. If nobody checked the assumptions behind a redesign, it isn't really a redesign. It's the same unverified beliefs, just wearing a nicer interface.
- 🎨 Visual hint: Full-bleed --paper-deeper background. Large muted outline of a floor plan or system diagram with a magnifying glass icon over one section in --sienna. Simple, diagnostic feel.

---

## 3. Part 1: Target What You're Testing

---

### SECTION DIVIDER: Part intro
- Kicker: Part 1
- Title: TARGET WHAT\nYOU'RE TESTING
- 🎨 Visual hint: Light --paper-deeper background (per deck rules). Big sienna part number. "Part 1" small muted text bottom-left. Title in large bold display type, one line of sub copy. No other content.

---

### NUMBERED: What is an assumption?
- Kicker: Recap
- Title: Four types.\nOne formula.
- Lead: Assumptions are everything believed without evidence. The full teaching lives in the Assumption Map framework doc. This is just the recap, applied to today's context.
- 4 types in a row: User · Problem · Solution · Business (name plus a one-line description each, no examples. This is the condensed recap, not the full teaching)
- 🎨 Visual hint: 4 cards in a horizontal row, same visual style as the Customer Understanding deck's assumption-types slide, signalling this is the same framework reused. Small mono label bottom-right of the slide: "Full framework → framework-assumption-map.md"

---

### STATEMENT: The assumption formula
- Kicker: Write it right
- Title: Write assumptions\nyou can *actually test.*
- Formula callout: *"We believe [WHO] will [WHAT] because [WHY]. We'll know we're right when [SIGNAL]."*
- Weak vs strong example (reuse the checkout example or swap for an enterprise-tool example)
- 🎨 Visual hint: Same weak/strong stacked card pattern as the Customer Understanding deck. WEAK: muted, cross icon. STRONG: --sienna border, checkmark icon, [WHO][WHAT][WHY][SIGNAL] labelled inline.

---

### DIAGRAM: The Importance × Evidence Matrix
- Kicker: Prioritise
- Title: Test the ones that\ncould break everything.
- Lead: Plot your assumptions on two axes: how important, and how proven. The top-left quadrant (high importance, low evidence) is where today's desk research gets pointed. Skip this step and research turns into a pile of miscellaneous observations. Aim it here instead and it produces something specific and defensible.
- Quadrant labels: TEST FIRST (top-left) · PROCEED (top-right) · MONITOR (bottom-left) · FILE (bottom-right)
- 🎨 Visual hint: Same 2×2 matrix SVG as the Customer Understanding deck. Top-left quadrant in --sienna tint with "START HERE" arrow. Add a small callout box bottom-right: "This is what today's desk research tests."

---

## 4. Part 2: Desk Research

---

### SECTION DIVIDER: Part intro
- Kicker: Part 2
- Title: DESK RESEARCH
- 🎨 Visual hint: Light --paper-deeper background (per deck rules). Big sienna part number. "Part 2" small muted text bottom-left. Title in large bold display type, one line of sub copy. No other content.

---

### DIAGRAM: What is desk research?
- Kicker: Define the method
- Title: Look outward.\nUse what already exists.
- Lead: Desk research is reviewing what already exists before generating new research: competitor products, tickets, analytics, prior studies. It's fast, cheap, and narrowly aimed. Evaluate Current Experience looked inward at your own product; this looks outward and across the organisation. It describes what's happening and what others do. Solutions come later.
- 🎨 Visual hint: **Real image needed.** LEFT panel, "Inward" (muted, labelled "Evaluate Current Experience, done"): the annotated mock UI from the evaluation session, shrunk. RIGHT panel, "Outward" (dominant): three genericised competitor screen crops side by side with small source icons beneath them (ticket, chart, document) feeding the same row, with 2 patterns circled in --sienna. The contrast is inside versus outside, not audit versus critique.
- 📌 **TODO (Winnie):** source or mock this image before building the deck.

---

### NUMBERED: Picking comparators
- Kicker: Who to scan
- Title: Two or three.\nMixed on purpose.
- Lead: 2 to 3 comparators is enough for one pass: at least one direct competitor (same category) and ideally one indirect (different category, same user job). More dilutes focus without adding signal. A comparator earns its place only if it speaks to a top-left assumption.
- 3 items: Direct (same product category) · Indirect (same job, different category) · Earns its place (speaks to a named assumption)
- 🎨 Visual hint: Three cards in a row. Direct in --sage-tint, indirect in --sienna-tint, "earns its place" card with a small matrix icon with the top-left quadrant filled. Light, this is a quick teach.

---

### STATEMENT: What to look for
- Kicker: Not inspiration
- Title: Not what looks good.\n*How they solve the job.*
- Lead: The question is how competitors solve the same problem, and where they deliberately diverge from it. This isn't about visual inspiration. A pattern only earns a place in the log if it speaks to one of today's targeted assumptions. Look at the key moments: entry, first decision, error, completion.
- 🎨 Visual hint: **Real image needed.** RIGHT panel: a small genericised competitor screenshot crop with the relevant pattern circled in --sienna (e.g. a competitor's upload flow showing file format requirements upfront, before the user hits an error), labelled "this." Genericise or blur any identifiable branding. LEFT panel keeps a muted mood-board icon, crossed out, labelled "not this," to hold the contrast.
- 📌 **TODO (Winnie):** source or mock this image before building the deck.

---

### DIAGRAM: Patterns, not screenshots
- Kicker: The real skill
- Title: Four screenshots, or\none *pattern?*
- Lead: The most common desk research mistake is collecting screenshots and calling it research. Three of three comparators showing file requirements before upload is one pattern with a count. And when a competitor pattern, a ticket theme, and a finding in your evaluation.md all point at the same step, that's one pattern with three independent sources, a much stronger and more defensible finding.
- 🎨 Visual hint: **Real image needed.** 4 small realistic UI crops on the left, each from a different source (two competitor screens, a ticket excerpt card, an analytics drop-off chart crop), all showing the same underlying issue, e.g. no format guidance before upload. Motion lines converge into 1 larger crop on the right labelled "Pattern: no format guidance before upload, 4 sources" in --sienna. The crops must read as genuine UI and data, not icon placeholders.
- 📌 **TODO (Winnie):** source or mock this image before building the deck.

---

### NUMBERED: The other sources
- Kicker: 4 minutes
- Title: Three more sources\nalready exist.
- Lead: Competitors are one source. Tickets, analytics, and prior research usually exist already and are cheaper than new research. For each one, note what it can and cannot prove, and tag it to an assumption. Full practice is the assignment.
- 3 columns: Support tickets (themes and counts, not single complaints) · Analytics (shows where users drop off, rarely why) · Prior research (check the date and the audience)
- 🎨 Visual hint: Three cards with a "what it can prove / what it can't" two-line split on each, using --sage-tint and --sienna-tint. Keep light.

---

## 5. Part 3: Synthesis

---

### SECTION DIVIDER: Part intro
- Kicker: Part 3
- Title: SYNTHESIS
- 🎨 Visual hint: Light --paper-deeper background (per deck rules). Big sienna part number. "Part 3" small muted text bottom-left. Title in large bold display type, one line of sub copy. No other content.

---

### DIAGRAM: Update the Assumption Map
- Kicker: Close the loop
- Title: What did the evidence\nactually *prove?*
- Lead: Return to your map. Using your pattern log and the findings in your evaluation.md (each tagged to an assumption), move every targeted assumption to Confirmed (with its sources), keep it Unconfirmed with an updated note, or add new Unknowns if something surfaced that nobody had named. Two independent sources beat one. This is the step most teams skip, and it's what turns research into a change in what the team believes.
- 🎨 Visual hint: The same Importance × Evidence matrix, now showing 2–3 items with a visible arrow moving from the top-left "Test First" quadrant toward the top-right "Proceed" quadrant, labelled "Confirmed" in --sage. One item shown moving sideways with a question-mark badge, labelled "still Unconfirmed." Small footnote on the slide: "Second pass after tickets, analytics, and prior research, see assignment."

---

### STATEMENT: The list-vs-narrative trap
- Kicker: Why this matters
- Title: Stakeholders don't\nact on lists.
- Lead: Even a well-organised findings log reads like a pile of complaints until it's synthesised. Synthesis is the job of turning "here's what we found" into "here's what this means and why it matters."
- 🎨 Visual hint: Two panels. LEFT: a dense, flat bulleted list, greyed out, labelled "Findings log." RIGHT: a single bold highlighted card with a headline-style sentence, labelled "Insight." Visual weight should make the right side clearly more compelling.

---

### DIAGRAM: The insight statement formula
- Kicker: Write it right
- Title: Pattern → assumption\n→ *impact.*
- Formula callout: *"We noticed [PATTERN, with evidence] across [N instances]. This confirms/breaks our assumption that [ASSUMPTION]. It matters because [IMPACT]."*
- Weak vs strong example (competitors do upload differently → formats-before-upload example from the lesson)
- 🎨 Visual hint: Same weak/strong stacked card pattern as the Part 1 assumption-formula slide. The visual consistency signals it's the same rigour, applied to a new step.

---

## 6. Part 4: Present with Confidence

---

### SECTION DIVIDER: Part intro
- Kicker: Part 4
- Title: PRESENT WITH\nCONFIDENCE
- 🎨 Visual hint: Light --paper-deeper background (per deck rules). Big sienna part number. "Part 4" small muted text bottom-left. Title in large bold display type, one line of sub copy. No other content.

---

### DIAGRAM: Headline-first structure
- Kicker: Structure
- Title: Lead with the\nheadline. Not the method.
- Lead: One-line summary → 3–4 insights with evidence and impact → recommended next step. Push the full findings log into an appendix; the core readout stays tight.
- 🎨 Visual hint: **Real image needed.** LEFT: the stacked inverted-pyramid shape as before (Headline on top, 3-4 insight blocks in the middle, faded appendix at the bottom). RIGHT: a small thumbnail of an actual mocked one-page stakeholder readout, framed like a document or slide preview, showing a real headline sentence, 3 to 4 insight blocks with small evidence tags, and a faded appendix section, so the abstract pyramid has a concrete artifact sitting next to it.
- 📌 **TODO (Winnie):** source or mock this image before building the deck.

---

### DIAGRAM: Sample readout: patterns across sources
- Kicker: What good looks like
- Title: One headline.\nThree sources behind it.
- Lead: A worked example. Headline: "Users can't tell what a valid file is before they upload." Evidence beneath it: a pattern from 3 of 3 comparators, the top ticket theme, the drop-off step in analytics, and one finding from evaluation.md with its screenshot. Impact and next step follow. Each claim points at a named source.
- 🎨 Visual hint: A one-page mocked readout framed like a document: headline on top, four small evidence tags (Competitors 3/3, Tickets, Analytics, Evaluation), impact line, next step, faded appendix. Replaces the old audit-report sample; same layout, retargeted to patterns across sources.

---

### STATEMENT: Handling pushback
- Kicker: Defend it
- Title: "That's just\nyour opinion."
- Lead: The answer is never to argue harder. Point at the evidence already attached to the insight: the pattern, the count, the sources, the assumption it broke. Confidence comes from preparation, not tone. You'll practise this in your homework pitch.
- 🎨 Visual hint: A speech bubble with the pushback line on the left, muted. On the right, a card stack of four evidence tags (pattern, count, sources, assumption) in --sienna that the line is answered with. One dominant visual.

---

## 7. Part 5: Practise

---

### SECTION DIVIDER: Part intro
- Kicker: Part 5
- Title: PRACTISE
- 🎨 Visual hint: Light --paper-deeper background (per deck rules). Big sienna part number. "Part 5" small muted text bottom-left. Title in large bold display type, one line of sub copy. No other content.

---

### MILESTONE: Structure Your Assumptions
- Kicker: Activity
- Num: 8
- Title: Minutes
- Sub: Open your raw list from earlier sessions, or write 8 fast. Rewrite 5 to 8 with the WHO/WHAT/WHY/SIGNAL formula, specific not generic. Plot each on the matrix. Share back: which one landed top-left?

---

### MILESTONE: Competitor Scan
- Kicker: Activity
- Num: 12
- Title: Minutes
- Sub: Name your workflow and top-left assumption. Walk it in 2 to 3 comparators. Add a row per pattern: competitor, workflow, pattern, related assumption, why it matters. Group into 2 to 3 patterns with a count. Share back which speaks most to your assumption. No AI yet.

---

### MILESTONE: Close the Loop
- Kicker: Activity
- Num: 5
- Title: Minutes
- Sub: Using your pattern worksheet and evaluation.md findings, mark each targeted assumption Confirmed (with sources), Unconfirmed, or newly Unknown. Re-plot what moved. Share back: which moved furthest, and how many independent sources moved it?

---

### MILESTONE: Synthesise Your Insights
- Kicker: Activity
- Num: 6
- Title: Minutes
- Sub: Review your worksheet, evaluation.md and updated map together. Write 2 insight statements using the formula. Share back your strongest one and the evidence behind it.

---

## 8. Part 6: AI Assist

---

### SECTION DIVIDER: Part intro
- Kicker: Part 6
- Title: AI ASSIST
- 🎨 Visual hint: Light --paper-deeper background (per deck rules). Big sienna part number. "Part 6" small muted text bottom-left. Title in large bold display type, one line of sub copy. No other content.

---

### PROCESS: The AI chain
- Kicker: 14 minutes
- Title: Brainstorm. Convert.\nVisualise.
- Steps: 1. Brainstorm: AI suggests leads · 2. Convert: verified output becomes .md files · 3. Visualise: the .md files become one HTML page
- 🎨 Visual hint: Standard light layout, mono "AI" tag. Three-stage horizontal flow with arrows: a chat bubble icon, then a file-card icon with ".md", then a browser-frame icon with ".html". A small "verify" checkpoint badge sits between each stage. This is the map for the next three slides; one dominant visual, minimal text.

---

### PROCESS: Step 1, Brainstorm
- Kicker: 3 minutes
- Title: Leads, not facts.
- Steps: 1. Paste your top-left assumption and workflow · 2. Ask for missed comparators (direct and indirect) and other angles · 3. Open every product yourself · 4. Keep only what you can verify
- 🎨 Visual hint: Standard light layout. The chain visual from the previous slide in miniature at the top with stage 1 highlighted. Below, a short list of AI leads, each with a verified tick or a struck-through "not found" tag. Dominant visual: the leads list with ticks and strikes.

---

### PROCESS: Step 2, Convert to .md
- Kicker: 5 minutes
- Title: Your work,\nsaved as files.
- Steps: 1. Give AI your verified leads plus your manual work · 2. Ask it to structure, not invent · 3. Save `competitor-pattern-log.md`, `insight-synthesis-template.md`, `stakeholder-readout-template.md`
- Prompt tip: Paste the existing file first and ask AI to extend it, not regenerate it.
- 🎨 Visual hint: Dark background, chain miniature with stage 2 highlighted. Left: the worksheet table and verified leads as input. Arrow. Right: three file-cards stacked, filenames in mono, with the pattern log schema (five columns) visible on the top card. Reuse the file-card pattern.

---

### PROCESS: Step 3, Visualise in HTML
- Kicker: 4 minutes
- Title: Same content,\nas one page.
- Steps: 1. Point AI at your .md files · 2. Ask for a one-page readout.html using only what is in them · 3. If something is wrong, fix the .md and regenerate · 4. Compare it with what you would have written by hand
- 🎨 Visual hint: Dark background, chain miniature with stage 3 highlighted. A browser-frame preview of a one-page readout (headline, insight cards with evidence tags, pattern counts, impact, next step) with small arrows pointing from three .md file-cards on the left into the page. Caption: ".md is the source of truth."

---

### STATEMENT: Verify at every step
- Kicker: 2 minutes
- Title: AI invents.\nYou check.
- Lead: AI can name competitors that don't exist, describe features a product doesn't have, and cite statistics it made up. Nothing goes into a .md file or readout.html until you've opened the product or the source yourself. Check the readout line by line: does each claim point at a named source in your .md files?
- 🎨 Visual hint: Standard light layout. A readout card with three lines, one struck through in --sienna with a "not found" tag, to show a fabricated claim being caught. One dominant visual.

---

## 9. Recap + Assignment + Close

---

### NUMBERED: The three files you built
- Kicker: Build Your Research Toolkit
- Title: Three files.\nEvery future project.
- Lead: Each is a saved asset that compounds. Point AI at the existing file and ask it to extend, never regenerate. Your evaluation.md from last session is the fourth file, an input today.
- 3 items: `competitor-pattern-log.md` · `insight-synthesis-template.md` · `stakeholder-readout-template.md`
- 🎨 Visual hint: 3 file-card icons in a row, file-card style from the AI build slide, all with a check-mark badge. A small faded fourth card on the left labelled `evaluation.md` with "from last session".

---

### PRACTICE: Assignment: Full Desk Research Pass
- Kicker: Assignment
- Title: Take It to\nFull Scale
- Steps:
  - Finish the competitor scan: 2 to 3 comparators, every pattern logged with a screenshot
  - Gather at least two other sources: tickets, analytics, prior research, logged as patterns with counts
  - Update your Assumption Map fully, citing sources
  - Write 3 to 4 insight statements, each grounded in evidence
  - Finish readout.html and rehearse a 60-second pitch. You deliver it next session, and I push back once.
- AI prompt: *"Here's my pattern log and source notes: [paste both]. Using my insight synthesis template, draft 4 candidate insight statements. Flag any that rest on a single source or something I haven't verified myself."*
- Deliverable: Updated pattern log, source notes, updated Assumption Map, readout.html. Share before next session.
- 🎨 Visual hint: Numbered steps list on left. AI prompt in dark code-block card below. --sienna accent on "Deliverable" label.

---

### END: Closing
- Kicker: One thing to carry forward
- Title: "You can't fix\na system you\nhaven't *mapped.*\nAnd you can't\n*sell* a fix\nnobody believes\nis real."
- Lead: Assumptions tell you where to look. Desk research tells you what's out there. Synthesis turns it into a story. AI speeds you up only after you can do it by hand.
- Sign: Winnie Nguyen
