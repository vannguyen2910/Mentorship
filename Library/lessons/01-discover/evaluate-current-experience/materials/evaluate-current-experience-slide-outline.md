---
title: "Evaluate Current Experience"
lesson_file: "evaluate-current-experience-lesson.md"
level: Junior
slide_count: 41
duration: "90 min"
status: draft
built_deck: ""
last_synced: 2026-10-07
---

> **Source of truth:** `evaluate-current-experience-lesson.md`
> All content changes (activities, phases, timing, concepts) are made there first, then reflected here.
> This file contains only slide-specific concerns: layout types, on-slide text, visual hints, kickers, and speaker notes.
> See `CLAUDE.md` → Lesson file sync rule for what triggers an update on which side.

> **Layout vocabulary is fixed.** Every slide header below uses one of the types documented in `_system/rules/SLIDE_DECK_RULES.md`. Activities use `MILESTONE`, assignments use `PRACTICE`, the closing slide uses `END`.

---

## Session metadata

| Field | Value |
|---|---|
| Program | private-training |
| Track / session | Discover, junior |
| Stage | Discover |
| Prior session | Design Thinking for UX Designer |
| Next session | Customer Understanding |
| Running example | Food delivery, ordering and checkout stage. Calibration issues are in the lesson's Appendix D |

---

## Slide structure: 41 slides

> **90-minute slot, fully scripted (82 min plus an 8-minute buffer).** Arc: Frame (opinion vs finding) → Method (by stage) → Principles (ten principles plus accessibility) → Guided practice → Severity → Own product, manual → AI assist (brainstorm, `evaluation.md`, `evaluation.html`, three levels) → Assignment.
> Slides 1 to 34 contain no AI. AI appears from Part 6 (slide 35) onward, by design.

1. Introduction (slides 1 to 2)
2. Opening: Opinion isn't a finding (slides 3 to 5)
3. Part 1: Choose a method by stage (slides 6 to 10)
4. Part 2: The principles (slides 11 to 23: divider, overview, ten principle slides, matching activity)
5. Part 3: Evaluate together (slides 24 to 27)
6. Part 4: Rate severity (slides 28 to 32)
7. Part 5: Your own product (slides 33 to 34)
8. Part 6: AI as an assistant (slides 35 to 39)
9. Assignment + Close (slides 40 to 41)

---

## Visual system

> Applies to every slide. Reuse before you build: the items marked **REUSE** already exist in the former Audit & Desk Research and Customer Understanding decks.

- **Principle slides:** the ten "Heuristic NN / 10" slides are reused from the former Audit & Desk Research deck as is (already inside the built deck `slides/Evaluate Current Experience.dc.html`, slides labelled "Heuristic 01 to 10"): one principle per slide with a bad and a good UI example. They use generic examples. The food-delivery checkout comes in through the speaker-note bridge, the matching activity and the seeded set.
- **One thread:** the food-delivery checkout. The live demo uses a real screenshot (slide 3). Illustration slides use one original, neutral mock checkout so no real brand UI appears in the deck.
- **Pins:** numbered --sienna pins mark issues on any screen. A pin keeps the same number from the moment it appears until it is plotted on the 2x2.
- **Family colours:** the three heuristic families get three fixed tints (see/understand, control/recover, predictable/efficient), used on the overview page, the ten principle slides, the cheat sheet and the evaluation table.
- **Progress rail:** a thin six-segment bar on section dividers and milestones. Segments 1 to 5 are solid, segment 6 (AI) is dashed until the AI part starts.
- **Timer ring:** every MILESTONE shows its minutes inside a ring that sits with the decorative circles. No new colours.
- **REUSE:** Nielsen's 10 two-row grid (Audit), annotated mock UI with circled issues (Audit, "What is a UX audit?"), weak/strong stacked cards (Audit, assumption formula), file-card icon with mono filename (Audit, "Build once"), 2x2 matrix SVG (Customer Understanding, Importance x Evidence). The built Audit deck is a bundled file, so these are referenced by slide name.
- **Accessibility of the deck itself:** severity and family are never shown by colour alone (use number, shape or label). Text contrast at least 4.5:1.

---

## Slides

### COVER
- Year: 2026 · Winnie Nguyen
- Stage: Discover
- Title: Evaluate\n*Current Experience*
- Subtitle: Judge what exists against clear principles, with evidence you can show.
- Author: Winnie Nguyen
- Credentials:
  - Senior Product Designer at NAB
  - Master of UX & Service Design
  - Product Design Instructor
- Right panel photo: Real photo, a designer at a desk reviewing a phone app flow, printed screens and sticky-note annotations in view. Focused, evidence-gathering mood, not a brainstorm.
- Speaker notes:
  - Welcome and frame the session in one sentence: today you learn to judge a design with a method, not with taste
  - Name who it's for: anyone who designed something without guidance, or inherited something someone else designed
  - **Say early: the first stretch of the session uses no AI. AI arrives at the end, once you can check it.**
  - Mention you'll finish with a ranked, evidenced evaluation of your own product
- 🎨 Visual hint: Cover layout, fixed. White left panel with year line, stage label, title (accent on line 2) and subtitle. Right panel is the real photo with dark gradient overlay, name and three credential lines bottom-left.

---

## 1. Introduction

### DIAGRAM · Agenda
- Kicker: What we're building today
- Title: Six moves.\nOne ranked evaluation.
- On-slide:
  1. **Choose** a method for your stage
  2. **Learn** the principles
  3. **Evaluate** together
  4. **Rate** by severity
  5. **Evaluate** your own product
  6. **Use AI** to extend it
- Speaker notes:
  - Walk through the six moves in one pass, ten seconds each
  - Point to move 6: AI is last on purpose
  - **The Success Check: your evaluation is complete, issues are ranked, and each has a screenshot or example**
  - Say the timing: you'll evaluate your own flow with about 14 minutes of hands-on time
- 🎨 Visual hint: SCHEMATIC. A route map, not a list: six stops on a horizontal path with a small icon per stop (signpost, ladder, book, magnifier, gauge, laptop). Stops 1 to 5 sit on a solid line; stop 6 (AI) sits past a dashed gap with a lighter tag "extend". Progress rail starts here.

---

## 2. Opening: Opinion Isn't a Finding

### IMAGE · Spot one problem
- Kicker: 60 seconds
- Title: Find one thing that\nslows a hungry customer.
- On-slide: A real checkout screen from a food-delivery app
- Speaker notes:
  - Show the live checkout. Give them 60 seconds, no vocabulary yet
  - Take two answers and write them on the board exactly as said
  - **Notice what you got: reactions, like "cluttered" or "hard to see"**
  - Hold the reveal for the next slide
- 🎨 Visual hint: REAL. Full-bleed screenshot of the live food-delivery checkout. Build 1: clean screen with a 60-second timer ring top-right. Build 2: the two student reactions appear as speech bubbles pointing at the spots they mean, with no pins and no vocabulary yet.
- 📌 **TODO (Winnie):** capture the checkout screenshots before the session, as a backup for the live app.

---

### DIAGRAM · Opinion is not a finding
- Kicker: The shift
- Title: A reaction can't be checked.\nA *finding* can.
- On-slide: "Cluttered" and "hard to see" are real reactions. But no one can verify them, rank them, or act on them. An evaluation turns a reaction into something a team can use.
- Speaker notes:
  - Use their two answers from the last slide as the examples
  - Ask: could a developer act on "it's cluttered"?
  - Define evaluation in plain words: judging what exists against a standard, to find where users will struggle
  - **It is not a redesign. Describing the problem and fixing it are two different jobs.**
- 🎨 Visual hint: SCHEMATIC. REUSE the annotated mock UI from the Audit slide "What is a UX audit?". Left: the mock screen with the two reactions as grey speech bubbles ("cluttered", "hard to see") and a muted "can't check, can't rank" tag. Right: the same screen with numbered --sienna pins and short evidence tags. A thin arrow labelled "reaction → finding" joins the two.

---

### FORMULA · A finding has four parts
- Kicker: The format
- Title: Four parts.\nOne rule.
- On-slide (rows, escalating):
  - What I saw.
  - What I saw. Where.
  - What I saw. Where. Which principle.
  - What I saw. Where. Which principle. **Proof.**
  - No screenshot, no finding.
- Speaker notes:
  - Build the rows one at a time, adding a part each time
  - Define each part with one food-delivery phrase, not a rule
  - **Land on the last line and pause. Everything today depends on it.**
  - Tell them: every finding you log today follows this format
- 🎨 Visual hint: TYPOGRAPHIC with an anchor visual. Four escalating rows on the left as before. On the right, one crop of the mock checkout builds with each row: a pin appears, then a location tag ("Review order"), then a principle tag, then a framed screenshot stamped "PROOF" in --sienna. The last line sits alone below.

---

## 3. Part 1: Choose a Method by Stage

### SECTION DIVIDER · Part 1
- Kicker: Part 1
- Title: Choose a *method.*
- Sub: The stage your project is in decides what you do first.
- Speaker notes:
  - Keep this short: 10 seconds
  - Frame the question: what do I have, and what do I need to know?
- 🎨 Visual hint: SCHEMATIC. Section divider layout, large "1" at 120px. Progress rail with segment 1 filled. A faint ladder illustration (draft, live, inherited) runs behind the title at low opacity.

---

### DIAGRAM · Where is your project?
- Kicker: Part 1 · Stage
- Title: Three stages.\nThree starting points.
- On-slide:
  - **Draft:** screens exist, no users yet → heuristic evaluation, then a walkthrough of one key task
  - **Live, you designed it:** data exists → analytics and feedback to find where, then heuristic evaluation there
  - **Live, you inherited it:** complaints exist → analytics and feedback first, then heuristic evaluation on the flagged flows
- Speaker notes:
  - Ask the mentee to point to their stage as you go
  - Explain the logic: the more data you have, the more you use it to decide where to look
  - **No users? Heuristic evaluation is the cheapest place to start.**
  - Do not explain usability testing here. It comes later in the track
- 🎨 Visual hint: SCHEMATIC. A three-rung ladder, each rung with a small phone illustration that matures: sketchy wireframe (draft), polished screens with a tiny chart badge (live, you designed it), screens with a stack of sticky complaints (live, inherited). Under each rung a method chip. An unplaced --sienna "you are here" pin hovers above the ladder.

---

### NUMBERED · Three methods
- Kicker: Part 1 · Methods
- Title: Three methods.\nThree questions.
- On-slide:
  1. **Analytics, feedback, SUS:** Where are users struggling, and how much?
  2. **Cognitive walkthrough:** Can a first-time user finish this one task?
  3. **Heuristic evaluation:** Does this design break well-known principles?
- Speaker notes:
  - Teach each method as the question it answers, not as a definition
  - SUS in one breath: a 10-statement survey, scored 0 to 100, around 68 is average. It tells you how well, not what's wrong
  - Name each method's limit in one phrase: where, one task, judgment
  - Walkthrough in one sentence: at each step of one task, ask will they try it, notice it, connect it, see it worked. Not practised today
  - **Today we practise the third. The other two tell you where to point it.**
- 🎨 Visual hint: SCHEMATIC. Three cards (3-col override), each with a mini illustration as the dominant element: a funnel chart with a drop-off step (analytics and SUS), a phone with a footprint path across four steps (walkthrough), the Nielsen two-row grid thumbnail (heuristic evaluation). Card 3 carries a --sienna ribbon "today".

---

### DIAGRAM · Your own design is hardest to see
- Kicker: Part 1 · A warning
- Title: You know *why.*\nA new user doesn't.
- On-slide: If you designed it, you remember every reason behind every choice. A first-time user has none of that. Three habits close the gap: do a task, not a tour; judge against the principles, not your memory; read the screen text out loud.
- Speaker notes:
  - Say this directly to the mentee: finding problems in your own work is the evaluation working, not you failing
  - Walk the three habits with one example each
  - Also address inherited work: judge the screens, don't just repeat the old complaints
  - **Reading text out loud is the fastest way to catch jargon.**
- 🎨 Visual hint: SCHEMATIC. Split view of the same mock screen. Left, "The designer": thought bubbles over every element ("I chose this because...") in muted ink. Right, "A first-time user": the same elements with only question marks and a blank-eyed face icon. The three habits sit as three mono labels along the bottom.

---

### MILESTONE · Place your project
- Kicker: Activity · Part 1
- Num: 3
- Title: Minutes
- Sub: Place your project on the stage ladder. Pick one method to start with. Write one line on why. Share back.
- Speaker notes:
  - Time-box hard: 3 minutes
  - **Challenge one choice: "What would you learn that you don't already know?"**
  - Note how many started with analytics versus heuristic evaluation, and why
- 🎨 Visual hint: TYPOGRAPHIC. Milestone layout on --sienna with the 3-minute timer ring around the 280px numeral. A small ladder icon next to the one-line prompt. Progress rail at the bottom, segment 1.

---

## 4. Part 2: The Principles

### SECTION DIVIDER · Part 2
- Kicker: Part 2
- Title: The *principles.*
- Sub: What you judge against.
- Speaker notes:
  - Hand out the one-page Heuristics Cheat Sheet now
  - **Tell them: keep it beside you for the rest of the session**
- 🎨 Visual hint: SCHEMATIC. Section divider layout, large "2" at 120px. Progress rail with segments 1 to 2 filled. A faint cheat-sheet page outline (three coloured bands) behind the title, hinting at the handout.

---

### DIAGRAM · Ten principles, one page
- Kicker: Part 2 · Nielsen's 10
- Title: Ten principles.\nThree families.
- On-slide:
  - **See and understand:** 1, 2, 6, 8
  - **Control and recover:** 3, 5, 9
  - **Predictable and efficient:** 4, 7, 10
- Speaker notes:
  - Define heuristic in plain words: a rule of thumb that holds across most products
  - Show all ten on one page first. This is the map for the next ten slides
  - Name the three family questions: Can I see what's going on? Can I stay in control? Is it predictable?
  - **Then one slide per principle, about a minute each. Same layout every time.**
  - If you can't name the heuristic while evaluating, find the family first, then narrow down
- 🎨 Visual hint: SCHEMATIC. REUSE the Nielsen two-row, five-column numbered grid from the Audit deck (the single principles page). Recolour the ten cards into the three fixed family tints, with a family bracket label under each group. Each card keeps its number, name and the deck's generic italic "e.g." line, so the overview matches the ten slides that follow. Number plus bracket, so colour is never the only cue.

---
### DIAGRAM · Principle 1: Visibility of system status
- Kicker: Heuristic 01 / 10
- Title: Visibility of system status
- On-slide:
  - **Definition:** The system keeps users informed about what is going on, through timely feedback.
  - **Why it matters:** If a click shows nothing, people click again, leave, or assume it broke. Feedback tells them the system heard them.
  - **Bad:** Upload report: a file row "Report.pdf" with nothing shown during the wait. Caption: "Nothing shows during the wait."
  - **Good:** Same row with a progress bar, "64% · about 12 seconds left", and a Cancel button.
- Speaker notes:
  - Say it in one line: The system keeps users informed about what is going on, through timely feedback.
  - Evaluator's question: Look at every action that takes time. Does the screen say something happened?
  - Checkout bridge: after Place Order, the screen sits on a spinner with no confirmation.
  - Often confused with 9: this is feedback on any action, 9 is about failures
  - **Look for silence: spinners, frozen states, no confirmation**
- 🎨 Visual hint: REUSE as is. Source: former Audit & Desk Research deck, slide "Heuristic 01: Visibility of system status", already in the built deck. Layout: left column with mono label "HEURISTIC 01 / 10", large 01 numeral, title, definition, and a "WHY IT MATTERS" block. Right: two phone panels, BAD (purple dot) and GOOD (yellow dot), with the italic caption under the BAD panel. UI shown: bad is upload report: a file row "Report.pdf" with nothing shown during the wait. Good is same row with a progress bar, "64% · about 12 seconds left", and a Cancel button. Do not restyle.
---
### DIAGRAM · Principle 2: Match between system and the real world
- Kicker: Heuristic 02 / 10
- Title: Match between system and the real world
- On-slide:
  - **Definition:** Speak the users' language, with words and concepts they already know, not internal jargon.
  - **Why it matters:** People do not learn your system's vocabulary. Familiar words and icons cut the learning cost to zero.
  - **Bad:** Account menu: "Deprecate principal entity", "Purge user record", "Terminate session". Caption: "Labels use the team's words, not users' words."
  - **Good:** Account menu: "Close account", "Delete my data", "Sign out".
- Speaker notes:
  - Say it in one line: Speak the users' language, with words and concepts they already know, not internal jargon.
  - Evaluator's question: Read every label aloud to a first-time user. Would they say it this way?
  - Checkout bridge: the fee line says "SF" instead of "Service fee".
  - Often confused with 4: here the word is unfamiliar, in 4 it is inconsistent
  - **Look for abbreviations, system names and codes shown to users**
- 🎨 Visual hint: REUSE as is. Source: former Audit & Desk Research deck, slide "Heuristic 02: Match between system and the real world", already in the built deck. Layout: left column with mono label "HEURISTIC 02 / 10", large 02 numeral, title, definition, and a "WHY IT MATTERS" block. Right: two phone panels, BAD (purple dot) and GOOD (yellow dot), with the italic caption under the BAD panel. UI shown: bad is account menu: "Deprecate principal entity", "Purge user record", "Terminate session". Good is account menu: "Close account", "Delete my data", "Sign out". Do not restyle.
---
### DIAGRAM · Principle 3: User control and freedom
- Kicker: Heuristic 03 / 10
- Title: User control and freedom
- On-slide:
  - **Definition:** Users make mistakes and need a clearly marked emergency exit to leave the unwanted state.
  - **Why it matters:** People explore. When they can undo, go back, or cancel, they try more and fear less.
  - **Bad:** Dialog "Delete 12 photos? This cannot be changed." with a single OK button. Caption: "Only one path forward."
  - **Good:** Photos grid (8 items left) and a dark bar "12 photos deleted" with an Undo action.
- Speaker notes:
  - Say it in one line: Users make mistakes and need a clearly marked emergency exit to leave the unwanted state.
  - Evaluator's question: Try to back out of every step. Can users cancel, undo, or return?
  - Checkout bridge: pressing Back from payment empties the cart.
  - Often confused with 5: 3 is recovering after, 5 is preventing before
  - **Look for lost work, no cancel, and Back that destroys progress**
- 🎨 Visual hint: REUSE as is. Source: former Audit & Desk Research deck, slide "Heuristic 03: User control and freedom", already in the built deck. Layout: left column with mono label "HEURISTIC 03 / 10", large 03 numeral, title, definition, and a "WHY IT MATTERS" block. Right: two phone panels, BAD (purple dot) and GOOD (yellow dot), with the italic caption under the BAD panel. UI shown: bad is dialog "Delete 12 photos? This cannot be changed." with a single OK button. Good is photos grid (8 items left) and a dark bar "12 photos deleted" with an Undo action. Do not restyle.
---
### DIAGRAM · Principle 4: Consistency and standards
- Kicker: Heuristic 04 / 10
- Title: Consistency and standards
- On-slide:
  - **Definition:** Same words, same actions, same patterns, inside the product and across platform conventions.
  - **Why it matters:** Every inconsistency forces a re-learn. Consistency makes screens predictable at a glance.
  - **Bad:** Projects, Tasks and Members lists where each create action looks different: "+ New", "Add", "Invite". Caption: "Create actions use a different style on every screen."
  - **Good:** The same three lists, each with the same "+ New" action in the same place.
- Speaker notes:
  - Say it in one line: Same words, same actions, same patterns, inside the product and across platform conventions.
  - Evaluator's question: Pick one action and trace it across screens. Is it named and styled the same way?
  - Checkout bridge: "Checkout" on one screen, "Pay now" on the next, for the same step.
  - Often confused with 2: 4 is about sameness, 2 is about familiarity
  - **Look across screens, not within one. Place two screens side by side**
- 🎨 Visual hint: REUSE as is. Source: former Audit & Desk Research deck, slide "Heuristic 04: Consistency and standards", already in the built deck. Layout: left column with mono label "HEURISTIC 04 / 10", large 04 numeral, title, definition, and a "WHY IT MATTERS" block. Right: two phone panels, BAD (purple dot) and GOOD (yellow dot), with the italic caption under the BAD panel. UI shown: bad is projects, Tasks and Members lists where each create action looks different: "+ New", "Add", "Invite". Good is the same three lists, each with the same "+ New" action in the same place. Do not restyle.
---
### DIAGRAM · Principle 5: Error prevention
- Kicker: Heuristic 05 / 10
- Title: Error prevention
- On-slide:
  - **Definition:** Eliminate error-prone conditions, or check for them and confirm before the action is committed.
  - **Why it matters:** Good error messages are second best. Stopping the mistake saves the user and support team the cleanup.
  - **Bad:** Booking form: check-in 31/02/2026, check-out 01/01/2020, a Book button. Caption: "Impossible dates go through."
  - **Good:** A March 2026 calendar where past days are greyed out and cannot be picked.
- Speaker notes:
  - Say it in one line: Eliminate error-prone conditions, or check for them and confirm before the action is committed.
  - Evaluator's question: Find inputs with strict rules. Does the interface stop bad input, or only complain afterwards?
  - Checkout bridge: the tip field accepts 5000 when the user meant 5.00.
  - Often confused with 9: 5 stops the error, 9 helps after it happens
  - **Look at inputs and irreversible buttons first**
- 🎨 Visual hint: REUSE as is. Source: former Audit & Desk Research deck, slide "Heuristic 05: Error prevention", already in the built deck. Layout: left column with mono label "HEURISTIC 05 / 10", large 05 numeral, title, definition, and a "WHY IT MATTERS" block. Right: two phone panels, BAD (purple dot) and GOOD (yellow dot), with the italic caption under the BAD panel. UI shown: bad is booking form: check-in 31/02/2026, check-out 01/01/2020, a Book button. Good is a March 2026 calendar where past days are greyed out and cannot be picked. Do not restyle.
---
### DIAGRAM · Principle 6: Recognition rather than recall
- Kicker: Heuristic 06 / 10
- Title: Recognition rather than recall
- On-slide:
  - **Definition:** Make options visible. Users should not have to remember information from one part to another.
  - **Why it matters:** Memory is limited. Showing options turns a recall task into an easier recognition task.
  - **Bad:** Orders screen with a field "Type the exact order ID". Caption: "Users must remember the exact ID."
  - **Good:** Orders screen with search plus a Recent list: #48213 Blue backpack, #48177 Desk lamp, #48090 Notebook set.
- Speaker notes:
  - Say it in one line: Make options visible. Users should not have to remember information from one part to another.
  - Evaluator's question: Look for blank fields and codes. What must users remember that the screen could show?
  - Checkout bridge: the promo code entered earlier is missing from the order summary.
  - Often confused with 8: 6 is missing information, 8 is too much
  - **Look for information that appeared once and then vanished**
- 🎨 Visual hint: REUSE as is. Source: former Audit & Desk Research deck, slide "Heuristic 06: Recognition rather than recall", already in the built deck. Layout: left column with mono label "HEURISTIC 06 / 10", large 06 numeral, title, definition, and a "WHY IT MATTERS" block. Right: two phone panels, BAD (purple dot) and GOOD (yellow dot), with the italic caption under the BAD panel. UI shown: bad is orders screen with a field "Type the exact order ID". Good is orders screen with search plus a Recent list: #48213 Blue backpack, #48177 Desk lamp, #48090 Notebook set. Do not restyle.
---
### DIAGRAM · Principle 7: Flexibility and efficiency of use
- Kicker: Heuristic 07 / 10
- Title: Flexibility and efficiency of use
- On-slide:
  - **Definition:** Shortcuts, hidden from novices, speed up the work of experts. The product serves both.
  - **Why it matters:** Frequent users repeat tasks hundreds of times. Small accelerators compound into hours saved.
  - **Bad:** Invoices list where each row needs its own menu to Approve. Approving 3 invoices takes 3 menus. Caption: "Approve each one: open the menu, choose Approve, repeat."
  - **Good:** Same list with checkboxes and a bar "3 selected" with Approve and Reject for all.
- Speaker notes:
  - Say it in one line: Shortcuts, hidden from novices, speed up the work of experts. The product serves both.
  - Evaluator's question: Watch an expert use the flow. Where are they slowed down by steps built for beginners?
  - Checkout bridge: no way to reorder a past meal or reuse a saved address.
  - Juniors often miss this one because it only shows on the second use
  - **Look for repeated tasks with no shortcut**
- 🎨 Visual hint: REUSE as is. Source: former Audit & Desk Research deck, slide "Heuristic 07: Flexibility and efficiency of use", already in the built deck. Layout: left column with mono label "HEURISTIC 07 / 10", large 07 numeral, title, definition, and a "WHY IT MATTERS" block. Right: two phone panels, BAD (purple dot) and GOOD (yellow dot), with the italic caption under the BAD panel. UI shown: bad is invoices list where each row needs its own menu to Approve. Approving 3 invoices takes 3 menus. Good is same list with checkboxes and a bar "3 selected" with Approve and Reject for all. Do not restyle.
---
### DIAGRAM · Principle 8: Aesthetic and minimalist design
- Kicker: Heuristic 08 / 10
- Title: Aesthetic and minimalist design
- On-slide:
  - **Definition:** Interfaces should not contain information that is irrelevant or rarely needed.
  - **Why it matters:** Every extra item competes with the one that matters. Less noise makes the key action easier to find.
  - **Bad:** Checkout crowded with warranty, gift wrap, newsletter, loyalty, coupon and referral extras around a small Pay button. Caption: "Extras compete with the Pay button."
  - **Good:** Checkout with item, subtotal, shipping, total, an "Add promo code" link and a clear "Pay $48.00".
- Speaker notes:
  - Say it in one line: Interfaces should not contain information that is irrelevant or rarely needed.
  - Evaluator's question: Count the choices on a screen. Which ones does a typical user need?
  - Checkout bridge: upsell banners push the order total below the fold.
  - This is not about pretty. It is about what competes with the task
  - **Look for what pushes the main action out of view**
- 🎨 Visual hint: REUSE as is. Source: former Audit & Desk Research deck, slide "Heuristic 08: Aesthetic and minimalist design", already in the built deck. Layout: left column with mono label "HEURISTIC 08 / 10", large 08 numeral, title, definition, and a "WHY IT MATTERS" block. Right: two phone panels, BAD (purple dot) and GOOD (yellow dot), with the italic caption under the BAD panel. UI shown: bad is checkout crowded with warranty, gift wrap, newsletter, loyalty, coupon and referral extras around a small Pay button. Good is checkout with item, subtotal, shipping, total, an "Add promo code" link and a clear "Pay $48.00". Do not restyle.
---
### DIAGRAM · Principle 9: Help users recognize, diagnose, and recover from errors
- Kicker: Heuristic 09 / 10
- Title: Help users recognize, diagnose, and recover from errors
- On-slide:
  - **Definition:** Error messages in plain language, name the problem precisely, and suggest a solution.
  - **Why it matters:** An unclear error leaves users stuck. A clear one gets them back on track without contacting support.
  - **Bad:** Create account form with a banner "Error: validation failed (E102)" and a field message "Invalid input". Caption: "It names neither the problem nor the fix."
  - **Good:** Password field message "Your password is too short. Use at least 8 characters." with a live checklist.
- Speaker notes:
  - Say it in one line: Error messages in plain language, name the problem precisely, and suggest a solution.
  - Evaluator's question: Trigger every error you can. Does each say what went wrong and how to fix it?
  - Checkout bridge: "Payment failed. Error 4012." and nothing else.
  - Only applies once something has failed. Before that, it is 5 or 1
  - **Look for codes, vague messages, and no next step**
- 🎨 Visual hint: REUSE as is. Source: former Audit & Desk Research deck, slide "Heuristic 09: Help users recognize, diagnose, and recover from errors", already in the built deck. Layout: left column with mono label "HEURISTIC 09 / 10", large 09 numeral, title, definition, and a "WHY IT MATTERS" block. Right: two phone panels, BAD (purple dot) and GOOD (yellow dot), with the italic caption under the BAD panel. UI shown: bad is create account form with a banner "Error: validation failed (E102)" and a field message "Invalid input". Good is password field message "Your password is too short. Use at least 8 characters." with a live checklist. Do not restyle.
---
### DIAGRAM · Principle 10: Help and documentation
- Kicker: Heuristic 10 / 10
- Title: Help and documentation
- On-slide:
  - **Definition:** Best if no explanation is needed. When it is, help is easy to search, task-focused, and short.
  - **Why it matters:** Some tasks need guidance. Help that appears where the question arises beats a manual users must hunt for.
  - **Bad:** "Need help?" opening a file: user-guide-v3-final.pdf (412 pages). Caption: "Help is far from the task."
  - **Good:** A search box where "refund" returns short task results: Request a refund, Refund status, Refund policy.
- Speaker notes:
  - Say it in one line: Best if no explanation is needed. When it is, help is easy to search, task-focused, and short.
  - Evaluator's question: Search for help like a user. Is the answer found fast, and is it about the task?
  - Checkout bridge: nothing explains what the service fee covers.
  - Usually the lowest severity in a flow. Rate it honestly
  - **Look for unexplained terms and help that sits far from the task**
- 🎨 Visual hint: REUSE as is. Source: former Audit & Desk Research deck, slide "Heuristic 10: Help and documentation", already in the built deck. Layout: left column with mono label "HEURISTIC 10 / 10", large 10 numeral, title, definition, and a "WHY IT MATTERS" block. Right: two phone panels, BAD (purple dot) and GOOD (yellow dot), with the italic caption under the BAD panel. UI shown: bad is "Need help?" opening a file: user-guide-v3-final.pdf (412 pages). Good is a search box where "refund" returns short task results: Request a refund, Refund status, Refund policy. Do not restyle.
---
### MILESTONE · Match the symptom
- Kicker: Activity · Part 2
- Num: 3
- Title: Minutes
- Sub: Six food-delivery symptoms. Name the principle and its family for each. If it fits two, say why.
- Speaker notes:
  - Read the six cards one at a time, or show them all and let the mentee work through them
  - **Reveal after two minutes. Ask which two were hardest to place.**
  - Expect confusion between 2 and 4, and between 5 and 9. Name that difference out loud
  - Accept either principle when the mentee can give a reason
- 🎨 Visual hint: TYPOGRAPHIC. Milestone layout on --sienna with the 3-minute timer ring. Six small symptom cards in two rows of three, each with a blank answer slot. Progress rail, segment 2.

---

### SECTION DIVIDER · Part 3
- Kicker: Part 3
- Title: Evaluate\n*together.*
- Sub: One finding modelled. Two found by you.
- Speaker notes:
  - Switch to the seeded checkout set, not the live app
  - **Mentor models first, then the mentee goes**
- 🎨 Visual hint: SCHEMATIC. Section divider layout, large "3" at 120px. Progress rail with segments 1 to 3 filled. A faint crop of the checkout with one pin glowing, previewing what comes next.

---

### COMPARE · Weak vs strong finding
- Kicker: Part 3 · The standard
- Title: "Confusing"\nor a *finding?*
- On-slide:
  - **Weak:** "The checkout is confusing."
  - **Strong:** At Review order, the service fee is labelled "SF" with no explanation, so a user can't tell what they're paying for before they commit. Breaks Match with the real world. Screenshot attached.
- Speaker notes:
  - Read both aloud and ask the mentee what's missing from the weak one
  - Point out the four parts in the strong one
  - **This example shows the format. It is not a claim about any real app.**
- 🎨 Visual hint: SCHEMATIC. REUSE the weak/strong stacked-card pattern from the Audit assumption formula slide. WEAK: muted card, cross icon, the one-line complaint. STRONG: --sienna border, tick icon, four labels (Saw, Where, Principle, Proof) highlighted inline, and a small framed screenshot crop with a pin as the fourth part.

---

### NUMBERED · Three tests for a finding
- Kicker: Part 3 · Check before you log
- Title: Three tests.\nBefore you log it.
- On-slide:
  1. **Saw, not felt:** "The button is grey", not "it's ugly"
  2. **Affects the user:** can they do or understand less?
  3. **Problem, not fix:** write the problem, not "make it blue"
- Speaker notes:
  - Run one quick example for each test
  - Use test 3 to restate: evaluation describes, fixes come later
  - **Failing a test doesn't mean delete it. It means rewrite it.**
- 🎨 Visual hint: SCHEMATIC. A funnel running left to right. Sticky notes labelled "cluttered", "ugly" and "make it blue" drop in; each test is a gate (Saw, Affects user, Problem) that bounces some notes back with a "rewrite" arrow. One note exits as a clean finding card with a pin.

---

### MILESTONE · Evaluate the checkout
- Kicker: Activity · Part 3
- Num: 12
- Title: Minutes
- Sub: Watch one finding modelled on the seeded checkout. Then find two more in the four-part format, each with a screenshot. Compare with the answer key.
- Speaker notes:
  - Split: 3 minutes mentor models, 6 minutes mentee, 3 minutes discuss
  - Use the seeded checkout set, not the live app, so every mentee faces the same findings
  - Model out loud: what I saw, where, which family, which heuristic, then circle the screenshot
  - **If two people pick different heuristics for the same issue, that's a good discussion, not a mistake**
  - Watch for opinions slipping in. Use the three tests
- 🎨 Visual hint: TYPOGRAPHIC. Milestone layout on --sienna with the 12-minute timer ring. Beneath the numeral, three small chips in a row: "3 model", "6 you", "3 discuss". Progress rail, segment 3.

---

## 6. Part 4: Rate Severity

### SECTION DIVIDER · Part 4
- Kicker: Part 4
- Title: Rate by\n*severity.*
- Sub: A list is complaints. A ranked list is a plan.
- Speaker notes:
  - Say the subtitle aloud
  - **Frame why: a team can only fix so much. Severity says what first.**
- 🎨 Visual hint: SCHEMATIC. Section divider layout, large "4" at 120px. Progress rail with segments 1 to 4 filled. A faint long list on the left collapsing into a short ranked list on the right, previewing "a list is complaints, a ranked list is a plan".

---

### DIAGRAM · The severity scale
- Kicker: Part 4 · 0 to 4
- Title: Five levels.\nOne ranking.
- On-slide:
  - **0** Not a problem
  - **1** Cosmetic
  - **2** Minor
  - **3** Major
  - **4** Catastrophe
- Speaker notes:
  - Teach from the severity framework doc
  - Note that 0 usually isn't logged at all
  - **Define 4 plainly: must fix before release**
  - Give one food-delivery example for 4: a double charge
- 🎨 Visual hint: SCHEMATIC. Five escalating badges in a horizontal row, each a different shape (dot, small square, triangle, diamond, octagon) with its number, label and a one-line food-delivery consequence beneath (tiny grey mismatch, unexplained fee, cart lost, double charge). Colour ramp is secondary to shape and number.

---

### PROCESS · Three questions to a number
- Kicker: Part 4 · How to score
- Title: Don't guess.\nAsk three.
- On-slide:
  - **01 · How often?** Everyone, or some people sometimes
  - **02 · How bad?** Can they recover, or are they stuck
  - **03 · Does it keep happening?** Once, or every time
- Speaker notes:
  - Add the optional fourth consideration verbally: does it damage trust?
  - Link to the earlier example: double charge scores high on all three
  - **Persistence is the nudge: keeps costing the user, round up. Wears off, round down.**
- 🎨 Visual hint: SCHEMATIC. Three dial gauges in a process track (How often, How bad, Does it keep happening). Run the double-charge example live: all three needles swing to the right as the speaker talks. A small "trust" badge sits beside the third as the optional fourth consideration.

---

### DIAGRAM · The 2x2 plot
- Kicker: Part 4 · Rank
- Title: Biggest problems\nrise to the top-right.
- On-slide:
  - Horizontal axis: frequency (rare → often)
  - Vertical axis: impact (small → big)
  - Top-right: usually 3 or 4
  - Bottom-left: usually 0 or 1
- Speaker notes:
  - Draw the 2x2 live and plot the three calibration issues
  - **The top-right is where your report starts**
  - Say: two evaluators rarely give the same number. Aim for within one point, and be able to explain why
  - If time is short, the mentor plots them rather than the mentee
- 🎨 Visual hint: SCHEMATIC. REUSE the 2x2 matrix SVG from the Customer Understanding deck. Relabel the axes Frequency (horizontal) and Impact (vertical), and flip the highlight to top-right with the "START HERE" arrow. Three numbered points (the calibration issues) drop in one at a time with a short title tag each. Quadrant labels carry the score ranges.

---

### MILESTONE · Calibrate severity
- Kicker: Activity · Part 4
- Num: 5
- Title: Minutes
- Sub: Rate three food-delivery issues silently. Compare with the mentor. Where you differ by more than one point, explain why.
- Speaker notes:
  - Use the calibration issues from the lesson appendix
  - **The reasoning is the point, not matching the mentor's number**
  - The quick knowledge check is optional: use the buffer, or set it as a take-home self-check
- 🎨 Visual hint: TYPOGRAPHIC. Milestone layout on --sienna with the 5-minute timer ring. Beside the prompt, three small cards labelled C1, C2, C3 with a blank score slot each. Progress rail, segment 4.

---

## 7. Part 5: Your Own Product

### SECTION DIVIDER · Part 5
- Kicker: Part 5
- Title: Your own\n*product.*
- Sub: No AI yet.
- Speaker notes:
  - Confirm everyone has their screenshots ready
  - **Say it plainly: no AI in this block. You do it by hand first.**
- 🎨 Visual hint: SCHEMATIC. Section divider layout, large "5" at 120px. Progress rail with segments 1 to 5 filled. A partly filled worksheet row in the background with a "no AI yet" stamp.

---

### MILESTONE · Evaluate your own flow
- Kicker: Activity · Part 5 · Manual
- Num: 14
- Title: Minutes
- Sub: One flow, your screenshots, the Cheat Sheet and the Worksheet. Find 3 to 5 issues, each with a screenshot, a frequency, an impact, and a severity from 0 to 4.
- Speaker notes:
  - Setup is 2 minutes, evaluating and rating is 10, share back is 2
  - The accessibility check is a take-home, so don't run it now
  - Remind them of the three habits for judging their own design
  - **Watch for: ten cosmetic points, everything rated 4, solutions instead of problems, no screenshots**
  - Coach, don't answer: "Which family does this fall in?"
  - Ask for the highest-severity issue at the share-back
- 🎨 Visual hint: TYPOGRAPHIC. Milestone layout on --sienna with the 14-minute timer ring, the largest moment of the deck. A thin strip of five screen thumbnails under the numeral, one pin on the third, suggesting the learner's own flow. Progress rail, segment 5.

---

## 8. Part 6: AI as an Assistant

### SECTION DIVIDER · Part 6
- Kicker: Part 6
- Title: AI as an\n*assistant.*
- Sub: Now that you can check it.
- Speaker notes:
  - Explain why this comes last: you can only check AI when you know the principles
  - **The rule: AI assists, you decide.**
- 🎨 Visual hint: SCHEMATIC. Section divider layout, large "6" at 120px. Progress rail with the sixth segment switching from dashed to solid. Behind the title, two lanes: a solid "your lane" and a dashed "AI lane" merging at the right.

---

### DIAGRAM · AI assists, you decide
- Kicker: Part 6 · The rule
- Title: AI can miss it.\nAI can *invent* it.
- On-slide: AI doesn't know your users, and it can describe a problem that isn't on the screen. Your manual pass is what lets you tell the difference. Every AI suggestion needs three answers: Can I see it? Does it break that principle? Would a real user hit it?
- Speaker notes:
  - Name the three checks aloud
  - Say what AI will not do today: rate severity, change your scores, suggest redesigns
  - **Expect to discard some suggestions. That means the check is working.**
  - Mention confidentiality: blur real customer data before uploading screenshots
- 🎨 Visual hint: SCHEMATIC. A three-gate checkpoint. AI suggestion cards travel left to right through gates labelled "Can I see it?", "Does it break the principle?", "Would a real user hit it?". Some cards pass, some drop into a discard bin marked "expected". The cards that pass land in the learner's worksheet on the right.

---

### PROCESS · Brainstorm, build, visualise
- Kicker: Part 6 · Three steps
- Title: Three steps.\nYour own files.
- On-slide:
  - **01 · Brainstorm (4 min):** AI suggests missed issues. You verify each one
  - **02 · Build `evaluation.md` (6 min):** AI structures your worksheet. You keep your scores
  - **03 · See `evaluation.html` (2 min):** mentor demos it. You generate yours as homework
- Speaker notes:
  - Walk the three steps with the prompts from the lesson
  - **`evaluation.md` is the source of truth. Edit it, regenerate the .html, never edit the .html.**
  - Checks for each: finding count matches, no score changed, three rows spot-checked
  - Ask for the HTML to pass its own checks: contrast and severity shown by number or shape as well as colour
  - Step 3 is a demo only. Mentees generate their own as homework
- 🎨 Visual hint: SCHEMATIC. Three steps. Step 1: the gate visual in miniature. Step 2: REUSE the Audit "Build once" file-card with `evaluation.md` in mono and a small block of the schema visible. Step 3: a second file-card `evaluation.html` with a thumbnail of the rendered page (ranked table plus the 2x2). A one-way arrow from .md to .html labelled "regenerate".

---

### MILESTONE · Build your evaluation
- Kicker: Activity · Part 6
- Num: 12
- Title: Minutes
- Sub: Brainstorm with AI and verify each suggestion. Turn your worksheet into `evaluation.md`. See a finished `evaluation.html`, then build yours as homework.
- Speaker notes:
  - Keep the prompts on screen
  - Circulate: look for changed scores or findings that appeared from nowhere
  - **If an AI-generated fact isn't on the screenshot, it comes out**
  - Save `evaluation.md` in the AI foundation folder so it carries over
- 🎨 Visual hint: TYPOGRAPHIC. Milestone layout on --sienna with the 12-minute timer ring split into three arcs (4, 6, 2). Beside it, the two file-card icons `evaluation.md` and `evaluation.html`. Progress rail complete.

---

### DIAGRAM · Three levels of AI evaluation
- Kicker: Part 6 · Beyond today
- Title: You did level 1.\nTwo more *exist.*
- On-slide:
  1. **You capture, AI compares:** screenshots and principles in, possible issues out
  2. **Paste a URL, a tool audits:** it scores each principle and attaches evidence
  3. **An agent walks the flow:** it clicks through, captures each step, then evaluates
  - Every level: you verify, you rate, you decide
- Speaker notes:
  - 2 minutes, talk only. Do not demo levels 2 and 3
  - Name where each breaks: level 2 sees public pages only, level 3 follows the path you give it
  - **Research: AI found about a fifth of what experts found, and added false positives. It was weakest on issues that need interaction.**
  - Tie back to the seeded set: "Back empties the cart" needs interaction, so a still screenshot can't show it
  - Keep your principles as a markdown file: the same file feeds all three levels
  - Level 2 is an optional stretch in the assignment. Level 3 is for later
- 🎨 Visual hint: SCHEMATIC. Three stairs rising left to right, one per level, each with a small icon (screenshot stack, URL bar, browser with a footprint path). Level 1 stair is solid and tagged "today". Levels 2 and 3 are dashed. A constant "you verify" bar runs beneath all three stairs. Progress rail complete.

---

## 9. Assignment + Close

### PRACTICE · Assignment: Finish and share
- Kicker: Assignment
- Title: Two Flows.\nOne Ranked List.
- On-slide:
  - Finish your first flow
  - Evaluate a second flow, manual first, then AI
  - Run the four accessibility checks on both flows
  - Every finding: screenshot and severity
  - Generate `evaluation.md` for both flows, then `evaluation.html`
  - One line at the top: which method you started with, and why
  - Add "Open questions about users": for your top three findings, what do I believe that I haven't checked?
  - Optional: ask a peer to rate your top three blind
  - Optional: run one public page through an AI audit tool and compare with your worksheet
- Speaker notes:
  - Deliverable: `evaluation.md` and `evaluation.html`, at least 6 findings, ranked, plus three open questions about users
  - Time estimate: 2 to 2.5 hours
  - Save to your homework folder before the next session
  - Optional level 2: run one public page through an AI heuristic-evaluation tool and compare three lists: both found, only you, only the tool
  - **Do the second flow by hand before you open AI**
- 🎨 Visual hint: SCHEMATIC. Numbered steps on the left. Right: two stacked file-cards showing the deliverables (`evaluation.md`, `evaluation.html`) and a small "2 flows, 6 findings" counter. The AI prompt sits in a dark code-block card below. --sienna accent on "Deliverable".

---

### END · Closing
- Kicker: Carry this forward
- Title: A reaction is a start.\nProof is *the finding.*
- Sign: Winnie Nguyen
- Speaker notes:
  - Read the in-session checkpoint aloud: one flow, 3 to 5 findings, each rated and with a screenshot
  - The full Success Check is met with the assignment
  - Name where evaluation stops: it shows what and where, not why. Ask for one belief about the user behind their top finding
  - Bridge: Customer Understanding picks up the why, by talking to real users
  - **Bring your `evaluation.md` and your three open questions to the next session**
- 🎨 Visual hint: TYPOGRAPHIC. End layout on --paper-deeper. Title in large italic. A final pin-and-frame motif: the checkout silhouette from the opening, now fully annotated and faded behind the title, closing the loop from reaction to finding.
