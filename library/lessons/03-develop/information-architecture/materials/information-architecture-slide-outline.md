# Session 4 · Information Architecture

**Winnie Nguyen**

---

## Session 3 Recap

**Last session: Synthesis & Problem Definition**

What you learned:
- How to turn raw interview notes into themes using Affinity Mapping
- How to write Insight Statements: Observation + Implication
- How to frame design opportunities with How Might We
- How to write a Problem Statement grounded in user research

Your assignment was to:
- Run affinity mapping on all interview notes
- Write 3 insight statements using the formula
- Share your problem statement with one stakeholder and note their response

> Today we take that problem statement and ask: how does the product need to be *organised* to solve it?

---

## What We're Building Today

Turn your problem statement into a structural design decision.

1. **Inherited vs Evidence-Based IA** — understand what you're actually working with
2. **Card Sorting** — how to learn what users expect before you build
3. **Sitemaps** — make the current structure visible so you can change it
4. **User Flows** — map what a user actually does, step by step, before touching a screen
5. **Process Map** — zoom out to see who does what behind the screen, and where work waits
6. **AI Workflow** — use AI to build and check flows and maps without letting it invent the product

---

## Mindset Shift

> **A polished screen in the wrong flow is still a broken design.**

| Before | After |
|--------|-------|
| "I'll figure out the structure as I wireframe." | "I map the structure first. Wireframes come after the flow is clear." |

---

## Part 1 — What is Information Architecture?

IA is how content is organised, labelled, and connected so users can find what they need — without thinking too hard.

It decides:
- What lives where
- What things are called
- How navigation is structured

> Most designers inherit an IA from whoever came before — and never question it.

---

## Inherited vs Evidence-Based IA

| | Inherited IA | Evidence-Based IA |
|---|---|---|
| **Source** | POs, stakeholders, legacy systems | User research, card sorting |
| **Organising logic** | Business structure, team ownership | Users' mental models and task sequences |
| **Risk** | "It makes sense to us" bias | Requires method discipline |

**The signal:** If your navigation mirrors the org chart — it's inherited.

---

## Part 2 — Card Sorting

**What it is**
Users arrange content cards into groups that feel natural to them. You observe the result.

**When to use it**
- Before building navigation — when you don't know how to group content
- When users complain they can't find things
- When you've inherited a structure and want to test it

**Why it matters**
It gives you evidence to defend structural decisions — not just intuition.

---

## Two Types of Card Sort

**Open card sort**
- Users create their own categories and name them
- Use when: you have no existing structure
- Reveals: the user's mental model directly

**Closed card sort**
- Users sort cards into categories you've already defined
- Use when: you want to validate an existing structure
- Reveals: whether your labels match user expectations

> 3–5 people surfaces structural assumptions worth questioning. You don't need 20.


---

## Part 3 — Sitemaps

**What it is**
A structural diagram of every page or screen in a product — showing hierarchy and connection. Not a wireframe. No layouts, no UI.

**When to use it**
- At the start of any redesign — before changing anything
- After card sorting — to rebuild structure from evidence
- When onboarding to a new product

**Why it matters**
You can't redesign what you haven't made visible. A sitemap makes structural problems undeniable.

---

## Two Sitemaps to Draw

**Inherited sitemap**
- Drawn from the current live product
- Documents reality as it is right now
- Start here — take screenshots, map every screen, draw the hierarchy

**Evidence-based sitemap**
- Rebuilt from card sorting results and your JTBD Map
- Organises content around user tasks, not business categories
- This is the goal

> Every box should be nameable without referring to which team built it. If you can't — that's an IA problem.


---

## Part 4 — User Flows

**What it is**
A diagram of the steps one user takes to complete one specific task — from entry point to final outcome.

Not a wireframe. A map of the screens, actions, and decisions along a task path, from the user's point of view.

**Goal**
Design and check the path of a task before drawing any screen. Find friction and missing states while they are cheap to fix.

---

## User Flow · Scope

| In | Out |
|---|---|
| One user, one task, one entry point | Other actors (admin, support, payment provider) |
| Screens, actions, decisions | What the system does behind the scenes |
| What the user sees | Internal handoffs → *Process Map* |

> Most design problems live in the flow — not in individual screens.

Without a user flow:
- You design screens without knowing what comes before or after
- Error states and edge cases are discovered in development — not design
- Stakeholders debate screen details without agreeing on task structure

---

## How to Draw a User Flow

1. **Name the task** — be specific. Not "checkout." "Book and confirm a slot as a returning user."
2. **Define entry and end points** — draw Start and End pills before anything else
3. **Map the happy path first** — the ideal sequence when everything works
4. **Add error and edge case branches** — slot taken, not logged in, empty state — every branch needs a destination
5. **Add notes where friction shows up**
6. **Review for completeness** — every diamond needs two labelled outgoing arrows. No orphaned shapes.

---

## The 5 Shapes That Carry All the Meaning

| Shape | What it represents | Example |
|---|---|---|
| **Pill** | Start and end points | "User opens the app", "Booking confirmed" |
| **Rectangle** | A screen or user action | Views slot list, taps "Pay" |
| **Diamond** | Decision point | "Slot still available?" / "Payment succeeded?" |
| **Arrow** | Flow direction | Label branches: Yes / No, Success / Error |
| **Note** | Context that doesn't fit a shape | "Friction: 3 taps to reach this" |

> Consistent shapes make your flow readable to anyone on the team — no explanation needed. A sixth shape usually means a system step. That's Process Map territory.

---

## When to Use a User Flow

- Before wireframing — settle the structure of a task before designing any screen
- Reviewing an existing product — document what users actually have to do
- Identifying friction — where users drop off or get lost
- Handing screens to engineering — shows *when* and *under what conditions* each screen appears

---

## Example · Book and Confirm a Slot (User Flow)

Start → views slot list → selects slot → ◇ Slot available? → reviews → pays → ◇ Payment OK? → "Booking confirmed" → End

> Note on the last step: *"Confirmation says 'pending', not 'confirmed'."*

The flow shows what the user sees. It can't explain *why* it says "pending." → next section.

---

## What a Good Flow Reveals

- Decision points where users do work the system could handle automatically
- Flows longer than necessary because content is in the wrong IA location
- Missing states: empty, error, loading, success

> If a core task takes more than 7 steps — the IA is likely the problem, not the screen design.

---

## JTBD → Flow

Use your JTBD Map to evaluate every step.

**Ask for each step:** Does this help the user move toward their job — or is it friction the system created for its own reasons?

| JTBD Insight | Flow Implication |
|---|---|
| Users need to confirm quickly before losing a slot | No upsell screens in the critical path |
| Users feel anxious about irreversible actions | Add a review step before final commit |
| Users want to look competent when sharing work | Surface "share" at task-completion, not buried in settings |

---

## Activity 1 · 20 min

> Pick one real project. Choose the core task a user needs to complete. Walk through it yourself — screen by screen — and map every step using the 5 shapes.

Start with the happy path. Then add one error branch and one note.

---

## Part 5 — Process Map

**What it is**
A diagram of how work moves between actors — the user, the system, the internal team, and third parties — to deliver one outcome.

A user flow follows one person's path. A process map shows the whole operation behind it, including what the user never sees.

**Goal**
Make handoffs, dependencies, and bottlenecks visible. Find steps that exist because of how the organisation or system is built — not because the user needs them.

---

## Process Map · Scope

| In | Out |
|---|---|
| Multiple actors | Screen layout and detail |
| Front-stage and back-stage | A single user's feelings and decisions |
| End to end, trigger to outcome | |

> Zoom out from the User Flow of the same task.

---

## How to Build a Process Map

1. **Start from the user flow** — its steps become the front-stage layer
2. **List the actors** — user, system, internal team, third parties. One swimlane each.
3. **Place every step in the lane of whoever owns it** — including steps the user never sees
4. **Mark the handoffs** — every arrow crossing a lane. Label what is passed.
5. **Look for waiting, repeating, orphaned steps**
6. **Compare with the user flow** — which steps does the user only *feel* as a delay?

---

## The Shapes and Tools

| Shape / tool | What it represents | Example |
|---|---|---|
| **Swimlane** | One actor per lane | User · System · Ops team · Payment provider |
| **Rectangle** | An action by that actor | Ops team reviews the booking |
| **Diamond** | Decision point | "Above auto-approval limit?" |
| **Parallelogram** | Automatic system step | Locks slot, sends email, validates card |
| **Handoff arrow** | Work crossing lanes | System → Ops team: "approval needed" |

```
┌──────────────────────────────────────────────┐
│  USER      │  Selects slot → Pays → "pending" │
├──────────────────────────────────────────────┤
│  SYSTEM    │  ▱ Locks slot → ▱ Requests pay   │
├──────────────────────────────────────────────┤
│  OPS TEAM  │       ◇ Needs approval? → Review │
├──────────────────────────────────────────────┤
│  3RD PARTY │       Gateway → Returns result   │
└──────────────────────────────────────────────┘
```

---

## When to Use a Process Map

- More than one actor — checkout with a payment provider, onboarding with system emails, admin features
- The user flow looks fine but users still hit delays or confusion that screens can't explain
- Before handing work to engineering — shows the back-stage logic behind each screen
- Aligning design, engineering, and operations on who owns which step

---

## Example · Book and Confirm a Slot (Process Map)

Same task, four lanes. The system locks the slot and requests payment. The provider returns the result. Then the system hands the booking to the Ops team for **manual approval** — a handoff the user never sees.

> "Pending" is not a screen problem. It's a manual handoff. The fix is in the process — auto-approve below a limit, show approval status — not in the layout.

---

## User Flow vs Process Map

| | User Flow | Process Map |
|---|---|---|
| **Perspective** | One user | The whole organisation |
| **Question** | What does the user go through? | Who does what, and where does work wait? |
| **Visibility** | Front-stage only | Front-stage and back-stage |
| **Shapes** | Pill, Rectangle, Diamond, Arrow, Note | + Swimlane, Parallelogram, Handoff arrow |
| **Order** | Draw first | Draw second, zoomed out |

---

## Activity 2 · 15 min

> Take the same task and the same flow. Zoom out. List the actors, give each a swimlane, and add the back-stage steps.

Mark every handoff. Circle every place the user waits.

---

## Part 6 — AI Workflow for Flows and Maps

> 9 slides. The centrepiece is slide 3: the whole workflow on one slide, built from `programs/ai-design-workflow/assets/diagrams/user-flow-process-map-activity-flow.html` (16:9, 1920×1080, plain HTML, no SVG). Every other slide in this part drills into one piece of it. Source of truth: `information-architecture-lesson.md`, "AI Workflow for User Flows and Process Maps".

### SECTION DIVIDER · AI Workflow for Flows and Maps
- Kicker: Part 6
- Title: Use AI without\nlosing the map
- On-slide: None.
- Speaker notes:
  - You can now draw a user flow and a process map by hand
  - **Now: how to use AI on them without letting it invent the product**
  - This is a workflow, not a prompt
- 🎨 Visual hint: TYPOGRAPHIC. Same divider style as Parts 1-5.

### STATEMENT · Why not one prompt?
- Kicker: The problem
- Title: A polished diagram is\nthe hardest kind to doubt
- On-slide: "Draw the user flow for booking a slot." → a clean, plausible diagram in seconds. It is also made up.
- Speaker notes:
  - Show the one-line prompt, then the confident diagram it returns
  - Ask: how would you know which steps are real?
  - **Nothing in it is tied to your product**
  - The fix is not a better prompt. It is a process
- 🎨 Visual hint: TYPOGRAPHIC. Large statement; small prompt box underneath.

### DIAGRAM · The whole workflow on one slide
- Kicker: The workflow
- Title: From raw notes to a map you can trust
- On-slide: The activity flow: YOU lane and AI lane, 8 steps, working-file chips, checkpoints A, B, C, and the two-branch band (A User Flow first, B Process Map second).
- Speaker notes:
  - Read the lanes first: purple is you, black is AI. They alternate, never two AI steps in a row
  - Walk steps 1-4: you collect facts, AI structures, you verify. **Nothing is drawn yet**
  - Walk steps 5-8: AI analyses, you decide, AI writes diagram code, you draw and state limits
  - Point at the three circles: each is a stop where you can go back
  - Point at the chips: one working file, each step fills one section
  - Do not explain every box; the next slides drill in
- 🎨 Visual hint: SCHEMATIC. Embed the HTML flow full-bleed; no extra chrome.

### NUMBERED · 7 principles
- Kicker: The principles
- Title: Seven rules behind\nevery step
- On-slide:
  1. Facts first, AI second
  2. The table is the source of truth
  3. Unknown is a valid answer
  4. Every claim points to evidence
  5. Alternate you and AI
  6. Keep the AI draft
  7. Widen before you choose
- Speaker notes:
  - Group them: 1-3 are about what AI may use, 4-5 about review, 6-7 about judgment
  - **Rule 2 is the one to remember: the diagram is only a view of the table**
  - Rule 6: the gap between the AI draft and your fix is how far to trust AI on this kind of task
  - Rule 7: three genuinely different options, not one idea in three wordings
- 🎨 Visual hint: TYPOGRAPHIC. Seven numbered rows, rule 2 highlighted.

### COMPARE · One spine, two branches
- Kicker: User Flow and Process Map
- Title: Same workflow,\ntwo branches
- On-slide:

  | | User Flow | Process Map |
  |---|---|---|
  | Facts you collect | Your walkthrough notes | + back-stage facts, each with a source |
  | AI at step 5 | Friction + restructuring options | Lanes, handoffs, waits, questions for the team |
  | Order | First | Second, reuses the verified table |
- Speaker notes:
  - One actor: run the User Flow branch only
  - Friction the screens can't explain: add the Process Map
  - **For Process Map, AI lists questions for the team. It never guesses an owner**
  - Back-stage facts need a source tag, even if the source is "nobody knows"
- 🎨 Visual hint: SCHEMATIC. Two columns, shared spine shown as a bar above.

### NUMBERED · Three checkpoints
- Kicker: The checkpoints
- Title: Three places to\nstop and check
- On-slide:
  - **A (after 4):** Could someone else follow this table to the same screens? Every "inferred" row confirmed or removed? If no → walk the product again.
  - **B (after 6):** Three different options considered? Fix traces to the job and evidence? If no → ask for alternatives; resolve unknowns.
  - **C (after 8):** Diagram has exactly the verified steps? Every unknown visible? If no → fix the code or the table.
- Speaker notes:
  - Each is a yes/no question you can answer
  - Each says where to go back to
  - **A is the one most people skip, and it is the one that stops invention**
  - B also covers checking "removable" steps with whoever owns the system
- 🎨 Visual hint: SCHEMATIC. Three cards with the A, B, C circles from the flow slide.

### NUMBERED · Anatomy of an AI step
- Kicker: Writing the instruction
- Title: Every AI step carries\nthe same six lines
- On-slide:
  1. Use **only** the notes / table below
  2. Cite the **ID** for every claim
  3. Mark guesses **inferred**; say **unknown**
  4. **Do not add, remove, or rename** steps
  5. Argue against your own conclusion
  6. Return **only your section**

  Starter for step 3: *"Using only the notes below, build a step table. Columns: ID, Shape, Label, Next, Evidence, Status (stated / inferred / unknown). If you don't know, write 'unknown'. Then list diamonds with fewer than two branches, paths with no end, and states with no coverage. No suggestions yet."*
- Speaker notes:
  - These six lines are a checklist for writing your own instructions
  - Show the step 3 starter and point at "unknown"
  - **A table with no unknown rows is a warning sign: real notes always leave gaps**
  - Keep the prompt on the slide short; full text is in the lesson
- 🎨 Visual hint: TYPOGRAPHIC. Six lines left, prompt block right.

### STATEMENT · Watch out for
- Kicker: Limits
- Title: AI doesn't know your system.\nYou do.
- On-slide: AI may remove a step that is technically required → check with whoever owns it. Mermaid looks authoritative → count nodes against the table. **This map can't tell you why users drop off, how long steps take, or whether the fix works.**
- Speaker notes:
  - Three warnings, one sentence each
  - **Close on the limit: this is a current-state map, not evidence about users**
  - Ask: how many rows did AI get wrong, invent, or miss? That number is your homework reflection
- 🎨 Visual hint: TYPOGRAPHIC. Statement with three short lines beneath.

### PRACTICE · Bring this home
- Kicker: Homework
- Title: Steps 1-4 on your\nown task
- On-slide: Frame → Capture facts → AI builds the table → you verify. Bring the AI draft table, your verified table, and the count of rows AI got wrong, invented, or missed.
- Speaker notes:
  - No extra class time: this is homework with a demo
  - Choose User Flow or Process Map, same rule as the assignment
  - Step 2 takes longest. Don't skip it
  - Full step cards are in the AI design workflow examples folder
- 🎨 Visual hint: TYPOGRAPHIC. Four short chips for steps 1-4, matching the flow slide colours.

---

## Your Assignment — Before Next Session

Choose the method that fits your project:
- **User Flow** — task mostly in the user's hands (one actor, screen-level friction)
- **Process Map** — task depends on the system, a team, or a third party (handoffs, waiting)

1. State in one sentence why you chose it
2. Complete the current-state map in FigJam or Miro with the correct shapes. For a Process Map, annotate each step: **U** (user), **S** (system), **T** (team), or **3P** (third party)
3. Highlight in red every step that exists because of a system, IA, or organisational constraint — not because it serves the user
4. Pick the single highest-friction step. Write one paragraph: why does it exist, what would need to change to remove it, and what would you test to validate that change?
5. **AI workflow:** run steps 1-4 on your task. Bring the AI draft table, your verified table, and how many rows AI got wrong, invented, or missed

---

*"Organise for users — not for the org chart."*

---

## Thank You

**Winnie Nguyen**

📧 nguyenphuctuongvan@gmail.com
