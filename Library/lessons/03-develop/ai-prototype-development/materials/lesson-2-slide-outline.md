---
title: "Lesson 2: Build Your Design System"
lesson_file: "lesson-2-interaction-pattern-build-editing-craft.md"
level: "intermediate"
slide_count: 15
duration: "70 min"
status: built
last_deck_fix: 2026-09-19
built_deck: "standalone program/Lesson 2 - Build It standalone.html"
last_synced: 2026-09-19
---

> **Source of truth:** this file documents the actual, final built deck (`Lesson 2 - Build It standalone.html`). It was reverse-synced from the live deck on 2026-09-19, so wording, order and structure here should match what is on screen exactly. Same relationship Lesson 1's outline has to its deck.
> `lesson-2-interaction-pattern-build-editing-craft.md` remains the source of truth for teaching content, timing and instructor notes. If the two disagree going forward, treat the live deck as the presentation reality and flag the lesson file for reconciliation rather than silently trusting either one.
> **Scope reconciliation (2026-09-19):** the built deck ends at "Map the Pattern." The earlier outline's Section 3 (Build & Edit — the three-file model, the five-ingredient build prompt, the three edit modes, the 30-minute hands-on build) and Section 4 (second-tool comparison) are not in it, and that content has been removed from the lesson file. The deck's screen labels record this: numbering runs 2.3 then jumps to 5 for the Closing. Building screens is now Lesson 3's opening work, not Lesson 2's closing work.
> **Deck mismatches — FIXED in the built deck on 2026-09-19.** Both slides below now carry the replacement wording; the record of what was wrong and why is kept here rather than deleted. The Cover subtitle was corrected in the same pass (it also promised screens), and the Closing's third checklist item was reworded from "Next: stitch these screens…" to "Next: build your screens from these files, then stitch them into one journey," since it referred to screens this deck never builds.
> **Originally recorded as:**
> 1. **Closing (5)** — the checklist reads "2–3 screens working in the browser, refined with the three edit modes." No screens are built in this deck and edit modes are never taught. Suggested replacement: "Templates, component inventory and interaction pattern built, reviewed and saved" and "`design-system.html` navigable — clicking a screen card opens its flow."
> 2. **Cover (0), speaker notes** — still say "working screens built from all three" and "if short on time later, the second-tool comparison in Section 4 is the first thing to cut." Neither exists. The honest cut order for this deck is Pre-Flight's before/after walkthrough first, then the interaction-pattern concept slide.
> **Speaker notes below are written as the deck itself carries them** — connected sentences a facilitator can read or paraphrase aloud, not scannable reference bullets. This matches Lesson 1's outline convention, set at Winnie's request for smoother 1:1 delivery.

---

## Session metadata

| Field | Value |
|---|---|
| Program | SYSTEMATIC AI PROTOTYPING |
| Track / session | Lesson 2 |
| Stage | Develop |
| Prior session | Lesson 1: Stop Starting From Zero |
| Next session | Lesson 3: Scaling the Prototype |
| Running example | The student's own anchor project — not a fixed demo product |
| Cover visual | Full-bleed photo panel right, instructor avatar + name + title bottom-left of the text panel |

---

## Slide structure — 15 slides

> Cover, then two numbered sections, each opening on its own full-bleed divider: **Section 1 "From Named to Real"** (1.1–1.8, 8 slides — recap, Pre-Flight, scope, setup, tokens, component inventory, templates, consolidation), **Section 2 "The Interaction Pattern"** (2.1–2.3, 3 slides). Closes on the Closing slide, labelled 5 in the deck.
> **Section 1 front-loads two decisions the old outline handled verbally.** "Scope the Build" (1.3) and "Confirm Your Setup" (1.4) are now their own slides, placed before any tool work, so the 2–3 screens and the MCP question are settled once rather than re-asked at each step. Screen scoping was taught in Lesson 1 — 1.3 is a decision slide, not a re-teach.
> **Every prompt on screen is short and plain — there is no CARE breakdown anywhere in this deck.** By Lesson 2 the CARE shape has been taught and used; the slides carry the runnable prompt, and the lesson file's Prompt Library carries the expanded CARE versions for students who want more scaffolding. Don't reintroduce four-part prompt cards here.
> **Review is deferred three times and happens once, at 1.8.** Tokens, the component inventory and the templates are all generated without correction, then checked together against the rendered `design-system.html`. Every file in this deck is `design-system.html` — not `design-system/index.html`.
> **The template step produces one template per pattern type, not one overall.** Slide 1.7's output shows READ and EDIT side by side, because a Read screen and an Edit screen do not share a skeleton. Knock-on not yet resolved: Lesson 1's "Design It in Figma" still has the student design a single template, and should produce one per type.
> **Section 2 runs three beats on its final slide.** Prompt, cross-check, then update the showroom — `design-system.html` is regenerated once at 2.3 to fold in `interaction-pattern.md`, so clicking a screen card opens that screen's flow. This supersedes the earlier "one-off checkpoint" decision: the page is built at 1.8 and updated once at 2.3, then left alone.

---

## 0. Cover

---

### COVER · Cover
- Category line: SYSTEMATIC AI PROTOTYPING
- Kicker: LESSON 2
- Title: Build\nDesign System (second line accented)
- Subtitle: Sync your tokens, build the component inventory and interaction pattern, then consolidate them into one navigable page.
- Author: Winnie Nguyen — UX Product Design Instructor
- Speaker notes: Name what today produces before touching anything: two saved artifacts (token file, component inventory), a third new one (interaction pattern), and working screens built from all three. Everything today builds toward those files being real, not just named. **Confirm the student's setup right now — MCP, no MCP, or design system already in code — it decides which method they run in Section 1.** If short on time later, the second-tool comparison in Section 4 is the first thing to cut, not anything before it.
- ✅ Fixed 2026-09-19: notes and subtitle both corrected in the built deck. Notes now read "…and a navigable design-system.html built from all three… No screens get built in this deck — screens are Lesson 3," and the cut order is Pre-Flight's before/after walkthrough, then the interaction-pattern concept slide. Subtitle now ends "…then consolidate them into one navigable page."
- 🎨 Visual: Full-bleed photo right panel, text panel left with avatar, name and title bottom-left.

---

## 1. From Named to Real

---

### SECTION DIVIDER · Section 1: From Named to Real
- Kicker: Section 1
- Ghost numeral: 1
- Title: From Named to Real
- On-slide: Pre-Flight, scope the build, sync your tokens, build the component inventory.
- Speaker notes: Pure transition beat — say the section name, let it sit for a second. The one line worth saying out loud: **last lesson named the Design Pattern, this section is where it stops being aspirational.** No new concepts yet — this is execution of something already understood.
- 🎨 Visual: Full-bleed dark, giant low-opacity ghost numeral "1," yellow mono "Section 1" tag.

---

### STATEMENT · Named, Not Built
- Kicker: Recap, not re-teach
- Title: Named,\nNot Built.
- On-slide: Naming a system and having AI build from it are two different milestones. Today closes the gap.
- On-slide diagram: 🏷 Named — lives in Figma → (labelled "Today") → ✓ Built — lives in the project folder
- Speaker notes: Callback, don't re-explain — Design Pattern vs prototype pattern was taught last lesson. Ask the student to say the difference back in one sentence: **Design Pattern lives in Figma, prototype pattern lives in the project folder for AI to read. Today builds the second one.** Ask directly whether their Figma file changed since last lesson — Pre-Flight next catches drift either way.
- 🎨 Visual: Two connected cards, left muted with a label icon, right accented with a checkmark, arrow between them labelled "Today."

---

### NUMBERED · Pre-Flight Checklist
- Kicker: Before AI reads anything
- Title: Clean up your\ndesign file\nfirst.
- On-slide checklist:
  - Delete or archive components not used in this prototype
  - Merge duplicate variants of the same component
  - Remove hidden/test layers and old exploration frames
  - Confirm naming is consistent across the file
- On-slide prompt card (for large files): "Here is my Figma component list: [paste]. Which of these look like **duplicates**, **unused variants**, or **one-off experiments** rather than real system components?"
- On-slide before/after: Before — Button, Button v2, btn_old, Card, Card (test copy), Input, Input_exploration → After — Button, Card, Input
- Speaker notes: AI can't tell "this is part of my system" from "I forgot to delete this" — it includes all of it in the inventory. **This feels like tidying, not real work — say plainly that it isn't optional.** It's the difference between a short, clean inventory next and a bloated one built on messy design work.
- 🎨 Visual: Bulleted checklist left, dark mono prompt card beneath, before/after component-name comparison right with an arrow between the two columns.

---

### STATEMENT · Scope the Build
- Kicker: Before any tool work
- Title: Scope the build.\nDon't build everything.
- On-slide:
  - Pick 2–3 screens from your interaction pattern.
  - The goal is to prove the pattern works, not to finish the prototype.
- On-slide diagram: five screen thumbnails — two tagged "Pick these," three tagged "Not yet"
- Speaker notes: Pick 2–3 screens from the interaction pattern named last lesson. **Don't try to build everything — the goal is to prove the pattern works, not to finish the prototype.** This is a quick, concrete decision before any tool work starts.
- 📝 Note: screen scoping itself was taught in Lesson 1 ("Which Screens Are Right"). This slide is the decision, not the teaching — keep it to a minute.
- 🎨 Visual: Two bullets left, a row of five wireframe screen thumbnails right, the first two highlighted and tagged, the rest muted.

---

### COMPARE · Confirm Your Setup
- Kicker: Before any tool work
- Title: Is MCP\nconnected?
- On-slide, two cards:
  - ⚡ Yes — connected · Read the design file live for every step ahead
  - ⌨ System's in code · Point at the repo instead of Figma
- Speaker notes: Before any tool work: does this student have Figma MCP connected? **That answer decides which method they run for every step ahead — sync, inventory, and everything after.** Confirm it now, once, rather than re-asking at each step. A given student only ever runs one path.
- 📝 Note: the third path — no MCP, paste the values in — is in the lesson file and in these notes but is not a card on this slide. If a student is on that path, say so aloud here; the slide won't say it for you.
- 🎨 Visual: Two-column compare, one icon per card (bolt / code brackets), title posed as a question.

---

### PROCESS · Sync Your Design Tokens
- Kicker: Runs once, matters for every screen after
- Title: Sync your design tokens\nas your design system.
- On-slide prompt card: "Read my design file [Link]. Extract the design tokens: **colour values**, **typography styles**, and **spacing**. Generate a CSS variables file from these tokens so every screen uses the exact values from my design system."
- On-slide tip: Have the file open and selected in the Figma desktop app first, copy the link of the section or the whole file.
- On-slide output, "What you get": the generated `:root { ... }` block — colour, font and space variables named by purpose
- Speaker notes: Confirm which method fits this student — MCP connected, no MCP (paste), or design system already in code — only walk the one path that applies, don't demo all three; the prompt shown is the MCP version, adapt the Ask/Rules lines for the other two. Runs once, pays off for every screen built after it — without it, AI defaults to generic colours and type. **Don't check values yet — that's consolidation's job.** Save into `design-system/`, wire it into the router file the same way it already points at `learning/`.
- 🎨 Visual: Dark mono prompt card left with a small tip line beneath, rendered CSS output right in mono type.

---

### PROCESS · Generate the Component Inventory
- Kicker: Demo → run → check later
- Title: Generate the\ncomponent inventory.
- On-slide prompt card: "Read my design file [Link]. Generate a component inventory: list every component with its **name**, **purpose**, and all its **states** (default, hover, loading, error, etc.)."
- On-slide output: a real component gallery — Button, 4 variants × 3 colours × 3 states; Contained button (Primary / Secondary / Error) across Enabled / Hover / Disabled; Outlined button below
- Speaker notes: Demo, then the student runs it on their own system, then move straight to the template — don't correct yet. **Deferred, not skipped: everything gets checked together at consolidation.** Method B (paste) needs the heaviest check later; Method C (codebase) the lightest. Say which applies now. Saved file is the router's second pointer.
- 🎨 Visual: Dark mono prompt card left, rendered component-gallery grid right showing real variants and states rather than a markdown table.

---

### PROCESS · Bring the Template Into Code
- Kicker: Demo → run → check later
- Title: Bring the Template\nInto Code.
- On-slide inputs converging: `tokens.css` + `component-inventory.md` + Figma template designs → 🧩 `design-system/template.html` — structure only, placeholder content
- On-slide prompt card: "Here's my template frame: **[paste or screenshot]**. Using **tokens.css** and **component-inventory.md**, output is html. Match the layout exactly."
- On-slide output, "What you get": two wireframe templates side by side — READ (content blocks, single Edit action) and EDIT (labelled fields, Cancel / Save)
- Speaker notes: Demo → student runs it → straight to consolidation. Don't correct yet. **They designed this template in Figma back in Lesson 1 — this step translates it into code, it doesn't redesign it.** Callback to Lesson 1's "Design It in Figma," which promised the template was the one ingredient nothing would regenerate for them. One prompt, not three — the two files are fixed inputs now; the only thing that varies is how they hand over the frame, and that's one bracket. **Nothing in the output can exist that isn't already in tokens.css or component-inventory.md — anything that doesn't match gets flagged, not invented.** Third piece saved as `design-system/template.html` — consolidation renders all three next.
- 📝 Note: the output shows two templates, one per pattern type, while the prompt and the file label are singular. A Read screen and an Edit screen don't share a skeleton, so one per type is the normal case — worth making the prompt say "a skeleton for each" on the next deck pass.
- 🎨 Visual: Three input chips converging into one file icon top-left, dark mono prompt card beneath, two labelled wireframe templates right.

---

### STATEMENT · Consolidate — design-system.html
- Kicker: The payoff — open it in a browser
- Title: One Page,\nAll Three.
- On-slide prompt card: "Build **design-system.html** from tokens.css, component-inventory.md, and template.html. This page is my checkpoint — where I check my design system against Figma before I build any screens. Use Storybook's layout as a reference only, not the tool. One plain HTML file, no build step. Tokens: every value as a labelled swatch showing the token name and the value. Components: one block per component — its name, then every state side by side, each labelled. Show hover and focus as static examples. Template: the empty structure, generic content. Link to tokens.css. Everything on the page uses those tokens, not browser defaults. End with a list of anything you couldn't render."
- On-slide diagram: 🎨 tokens.css + 📄 component-inventory.md + 🧩 template.html → 🖥 design-system.html
- Speaker notes: First "open it in a browser" moment — everything after is judged against this page, not Figma. **The deferred review happens here, once: check tokens, every component state, and template structure against Figma.** One visual pass beats three separate reads. Method B: watch for invented or missing states. Method C: watch for anything not yet shipped. **Real test: components must visibly use the synced tokens, not browser defaults — that's a correction if they don't.** This is the showroom — screens next section are the real rooms built from it.
- 📝 Note: this is the longest prompt in the deck and the only one worth reading aloud in full. The "End with a list of anything you couldn't render" clause is what makes the deferred review safe — read that list first, before looking at the page.
- 🎨 Visual: Long dark mono prompt card left, three file icons converging into one browser-window icon right.

---

## 2. The Interaction Pattern

---

### SECTION DIVIDER · Section 2: The Interaction Pattern
- Kicker: Section 2
- Ghost numeral: 2
- Title: The Interaction Pattern
- On-slide: You just built the showroom. It shows every piece of furniture — not the doors between rooms.
- Speaker notes: Transition beat — bridge from the page still open on their screen, don't gear-change into theory cold. **Point at `design-system.html`: everything on it is a thing. Nothing on it moves.** Callback to last lesson's drift gap, if it lands.
- 🎨 Visual: Same divider treatment, ghost numeral "2."

---

### STATEMENT · What the Inventory Can't Tell You
- Kicker: The gap nothing so far fills
- Title: What the Inventory\nCan't Tell You.
- On-slide, two stacked cards:
  - ✓ Your component inventory says what exists — Button, Card, Nav, every state.
  - ? Nothing you've built says what happens when the button is pressed.
- On-slide closing line: Build screens without it and AI makes beautiful screens where nothing goes anywhere.
- Speaker notes: Define it by the gap, not by a definition — they've just spent 35 minutes on things that exist. A component inventory says what exists. **An interaction pattern says how it connects: which screens exist, what triggers a move from one to the next, what carries over.** Name the failure concretely — a button that looks right and does nothing is the most common first-prototype result. Flow context is one of the five build ingredients in Lesson 3 — it has nowhere to come from without this file. This is the second of the two prototype-pattern layers, and the thing still missing at the end of Lesson 1.
- ✅ Fixed 2026-09-19: the clause now reads "one of the five build ingredients in Lesson 3," which is where they are taught.
- 🎨 Visual: Two stacked cards, upper muted with a checkmark, lower accented with a question mark, one closing line beneath in sienna.

---

### DIAGRAM · Four Layers, One System
- Kicker: Where this sits in what you've built
- Title: Four Layers,\nOne System.
- On-slide rows (interaction pattern listed first and highlighted, the three built layers beneath):
  - `interaction-pattern.md` — the floor plan · How many rooms, which doors?
  - `tokens.css` — the paint · What does it look like?
  - `component-inventory.md` — the furniture · What exists?
  - `template.html` — one room's shape · How is a room laid out?
- On-slide reminder strip, the seven screen types from Lesson 1: Read · Edit · Add · Confirm · Navigate · Search / Filter · Onboard
- Speaker notes: Extends the paint/furniture/room language already used, doesn't introduce a new metaphor. **A floor plan is what reveals whether one room shape is enough — that's why the template cross-check happens after this file exists, not before.** Strip is a reminder, not a re-teach — they saw these in Lesson 1 as a lookup catalogue. One breath each. **The one new use: every screen in the pattern gets labelled with its type. That label tells AI which components the screen needs and which transitions it requires.** One screen can carry two — checkout is Edit and Confirm at once. Full definitions live in the source lesson's Phase 2 table if they want a refresher after the session.
- 🎨 Visual: Four labelled rows, the interaction-pattern row visually heaviest and placed first; a light single-line strip of seven screen-type tags along the bottom.

---

### PROCESS · Map the Pattern
- Kicker: One prompt, then one check
- Title: Map the\nPattern.
- On-slide, three beats: 1 Prompt → 2 Cross-check → 3 Update showroom
- On-slide, under the cross-check beat: **Shape** — does every screen fit the template's shape? · **Flow** — does the template carry what the flow needs (back, nav, progress)?
- On-slide prompt card: "Based on the component inventory, map the interaction pattern for the screens I'm about to build: which **screens** exist, what **connects** them, and what **triggers** each transition. Describe it like a gallery of cards, where **clicking one card opens its own detail screen** with its own interactions. Use the component inventory as your reference. Once this checks out against the template, update **design-system.html** to include this file — make each screen card on it clickable so it opens that screen's own flow."
- On-slide output: Gallery (tagged Navigate) → tap a card → Template detail (tagged Read — its own interactions live here)
- Speaker notes: Short prompt — the file's already loaded, no need to restate what's in it. Save to the router alongside the inventory — its second pointer. Every build prompt after this stays short, because both layers now exist as files. **Expect the question "I have a template now — why isn't it in the prompt?" Answer: feeding it in anchors the AI to the shape it just read, and the interaction pattern is the thing meant to reveal whether one shape is enough. Don't hand the AI the answer you're asking it to check.** Cross-check is the beat people skip, and it asks two things, not one. Shape: a mismatched screen means a second template now. Flow: a template built before the flow existed usually has no back, nav, or progress element — every screen will be missing the same thing. Most 2–3 screen prototypes share one shape — if this one doesn't, repeat "Bring the Template Into Code" once more before moving on. A missing flow element is cheaper: edit `template.html` directly, don't regenerate it. Label each screen with its type as they read the output — that's the recall from the last slide doing its job. **Third beat: once the cross-check passes, `design-system.html` gets regenerated to fold in `interaction-pattern.md` — it stops being a static swatch page and becomes a navigable home page, so clicking a screen card in it opens that screen's own flow.** This only happens once, here, because `interaction-pattern.md` didn't exist yet at the first consolidation.
- 📝 Note: at this point in the lesson the screens don't exist yet, so a card opens the template's shape for that screen type, not a built screen. If Lesson 3 later points the cards at the real screen files, this page becomes the prototype's front door — worth deciding when Lesson 3 is drafted.
- 🎨 Visual: Three numbered beats across the top with the two cross-check questions beneath beat 2, long dark mono prompt card left, gallery-to-detail flow right.

---

## 5. Closing

---

### END · Closing
- Kicker: Before next time
- Title (quote): "The prototype pattern isn't a document in a folder. It's *what every screen reads from instead of a retyped prompt.*"
- On-slide checklist:
  - ✓ Tokens synced, component inventory and interaction pattern built and saved
  - ✓ design-system.html navigable — clicking a screen card opens its flow
  - ✓ Next: build your screens from these files, then stitch them into one journey
- Sign: — Winnie Nguyen
- Speaker notes: Let the pull quote breathe before the checklist — the prototype pattern's job is to be read from, not just stored. Walk the three checklist items as a recap of exactly what happened today. **Worth naming explicitly: no screens were built today, and that is on purpose — Lesson 3 builds them from these files and nothing today gets redone.** Confirm the homework checklist from the lesson file before closing.
- ✅ Fixed 2026-09-19: checklist items 2 and 3 replaced in the built deck, and the speaker notes reworded to stop implying screens were built.
- 🎨 Visual: Italic pull-quote title on a deeper paper background, checkbox checklist beneath, signature line at the bottom.

---

*Reverse-synced from the built deck · Private Training · Last updated September 2026*
