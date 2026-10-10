# Information Architecture

**Type:** Lesson
**Duration:** 120–135 minutes
**Audience:** Intermediate
**Methods:** Card Sorting · Sitemaps · Tree Testing · User Flows · Process Map · AI Workflow for Flows
**Programs:** ui-ux-fundamentals:04, junior-to-mid-level:05

---

## Key Concepts

### What is Information Architecture?
IA is the discipline of deciding how content is organised, labelled, and connected so that users can find what they need without thinking too hard. It determines what lives where, what things are called, and how navigation is structured. Most designers inherit an IA from whoever designed before them — and rarely question it.

---

### Inherited IA vs Evidence-Based IA

The most important distinction in this lesson. Most product structures were built by product owners, engineers, or business stakeholders who organised things the way the *business* thinks — by feature, team, or product line. Users don't organise information that way.

| | Inherited IA | Evidence-Based IA |
|---|---|---|
| **Source** | POs, stakeholders, briefs, legacy systems | User research, card sorting, tree testing |
| **Organising logic** | Business structure, feature ownership, system architecture | Users' mental models, language, and task sequences |
| **What it solves** | Internal alignment, delivery scope | User findability, navigation confidence |
| **Risk** | "It makes sense to us" bias | Requires time and method discipline |

A navigation that mirrors the org chart is almost always inherited IA. A navigation built from card sorting and tested with tree testing is evidence-based.

---

### Card Sorting

**What it is**
A method for learning how users mentally group and label content. Users are given cards representing content items and asked to arrange them into groups that feel natural to them.

**When to use it**
- Before building or redesigning navigation — when you don't yet know how content should be grouped
- When users complain they can't find things, but you're not sure which categories or labels are wrong
- When you've inherited a navigation structure and want to know if it matches how users actually think

**Why to use it**
Most navigation structures reflect internal business logic, not user logic. Card sorting reveals the gap. It gives you evidence to defend structural decisions to stakeholders — not just intuition.

**How to use it**
Two formats depending on your question:

- **Open card sort** — users create their own categories and name them. Use this when you don't yet have a navigation structure. Best for discovery. Reveals the user's mental model directly.
- **Closed card sort** — users sort cards into categories you've already defined. Use this to validate an existing structure. Reveals whether your labels match users' expectations.

Run with 15–20 participants for reliable patterns. For a quick in-session test, even 3–5 people surfaces structural assumptions worth questioning. Look for clustering agreement, not perfect consensus — divergence is data too.

Tools: FigJam, Miro (physical sticky notes), Optimal Workshop, or Maze for async runs.

---

### Sitemaps

**What it is**
A structural diagram showing the hierarchy and relationship between all pages or screens in a product. A sitemap is not a wireframe — it shows *what exists and how it connects*, not what anything looks like.

**When to use it**
- At the start of a redesign, to document the current structure before changing anything
- After card sorting, to redesign the structure based on user evidence
- When onboarding onto a new product — to build a shared understanding of the current state

**Why to use it**
Without a sitemap, structural problems stay invisible. You can't redesign what you haven't made explicit. A sitemap also makes it possible to have an honest conversation with stakeholders about whether the current structure serves users — or the business.

**How to use it**
Draw two versions when doing IA work:

- **Inherited sitemap** — drawn from the current live product. Documents reality as it is. Start here. Take screenshots, map every screen, and draw the hierarchy.
- **Evidence-based sitemap** — rebuilt from card sorting results and JTBD insights. Organises content around user tasks, not business categories. This is the goal.

Every box in the sitemap should be nameable and have a clear parent. If you can't define what belongs in a section without referring to the team that built it — that's an IA problem.

---


### User Flows

**What it is**
A diagram of the steps one user takes to complete one specific task — from entry point to final outcome. A user flow is not a wireframe. It maps the *screens, actions, and decisions* along a task path, from the user's point of view.

**Goal**
Design and check the path of a task before drawing any screen. Find friction (steps the user should not have to take) and missing states (error, empty, loading, success) while they are still cheap to fix.

**Scope**
- **In:** one user, one task, one entry point. Only what the user sees, does, and decides.
- **Out:** what the system does behind the scenes, other actors (admin, support team, payment provider), and internal handoffs. Those belong to the Process Map (next section).

**Why user flows matter in the design process**
Most design problems live in the flow, not in individual screens. A screen can look polished and still sit in the wrong place in a broken flow.

Without a user flow:
- You design screens before knowing what should come before or after them
- Edge cases (error states, empty states, permission gates) get discovered in development — not design
- Stakeholders debate screen-level details without ever agreeing on the task structure

**How to use it**

1. **Name the task** — be specific. Not "checkout" but "book and confirm a slot as a returning user."
2. **Define the entry point and end point** — draw the Start and End pills before anything else. Where does the task begin: direct link, navigation tap, search result, notification?
3. **Map the happy path first** — the ideal sequence when everything works.
4. **Add branches for errors and edge cases** — the slot is taken, the user is not logged in, the content has not loaded. Each branch needs a destination — never leave a line unresolved.
5. **Add notes where friction shows up** — a step that feels long, a screen the user did not expect, a place where users hesitate.
6. **Review for completeness** — every diamond has at least two labelled outgoing arrows. Every path ends somewhere. No orphaned shapes.

**The 5 shapes that carry all the meaning**

A user flow is built from five shapes. Using them consistently makes the flow readable to anyone on the team without explanation.

| Shape | What it represents | Example |
|---|---|---|
| **Pill / rounded rectangle** | Start and end points | "User opens the app", "Booking confirmed" |
| **Rectangle** | A screen or a user action | Views the slot list, taps "Pay", fills a field |
| **Diamond** | Decision point | "Is the slot still available?", "Did payment succeed?" |
| **Arrow** | Direction of the flow | Label every branch: Yes / No, Success / Error |
| **Note** | Context that does not fit a shape | "Error message shown here", "Friction: 3 taps to reach this" |

If a step needs a sixth shape, it is probably a system step or a handoff — that is Process Map territory.

**When to use it**
- Before wireframing — to settle the structure of a task before designing any screen
- When reviewing an existing product — to document what a user currently has to do
- When identifying friction — where users drop off, get confused, or take the wrong path
- When handing a screen-level design to engineering — it shows *when* and *under what conditions* each screen appears

**What a well-drawn flow reveals**
- Decision points that ask users to do work the system could do automatically
- Flows that are longer than necessary because content is in the wrong place in the IA
- Missing states: what happens at empty state, error state, loading state?

**How JTBD shapes user flows**
Jobs-to-Be-Done gives you the lens for evaluating a flow. For each step, ask: does this step help the user progress toward their job — or is it friction the system is adding for its own reasons?

If the functional job is "confirm my booking before I lose the slot," every step that delays confirmation is a structural problem. JTBD makes those problems visible — and defensible to stakeholders.

| JTBD Insight | Flow Implication |
|---|---|
| Users' primary job is confirming quickly before the slot expires | Reduce steps between intent and confirmation — no upsell screens in the critical path |
| Users feel anxious about irreversible decisions | Add a review step before final commit; make "go back" always visible |
| Users want to look competent when sharing work | Surface "share" at task-completion moments, not buried in settings |

**Running example — "Book and confirm a slot" (user flow)**
Start → views slot list → selects a slot → ◇ Slot still available? (No → sees alternatives → back to slot list) → reviews details → taps "Pay" → ◇ Payment successful? (No → error message → retry) → sees "Booking confirmed" → End. Note on the last step: *"Confirmation says 'pending', not 'confirmed'."*

The flow shows what the user sees. It cannot explain *why* the confirmation says "pending." That question moves to the next section.

---

### Process Map

**What it is**
A diagram of how work moves between the different actors — the user, the system, the internal team, and third parties — to deliver one outcome. Where a user flow follows one person's path, a process map shows the whole operation behind it, including what the user never sees.

**Goal**
Make handoffs, dependencies, and bottlenecks visible. Find the steps that exist because of how the organisation or system is built, not because the user needs them. Give design, engineering, and operations one shared picture of how the task really runs.

**Scope**
- **In:** multiple actors, front-stage (what the user sees) and back-stage (what happens behind it), end to end from trigger to outcome.
- **Out:** screen-level detail and layout. A process map says *who does what and in which order*, not what the screen looks like.
- Think of it as zooming out from the User Flow of the same task.

**How to use it**

1. **Start from the user flow** — take the task you already mapped. Its steps become the front-stage layer.
2. **List the actors** — user, system, internal team (support, ops, admin), third parties (payment provider, email service). Each actor gets one horizontal swimlane.
3. **Place every step in the lane of whoever is responsible for it** — including the steps the user never sees.
4. **Mark the handoffs** — every arrow that crosses from one lane to another is a handoff. Label what is passed (data, approval, notification).
5. **Look for waiting, repeating, and orphaned steps** — a step with no owner, a manual check, or a loop between lanes is where delays and errors hide.
6. **Compare against the user flow** — which steps does the user see, and which do they only feel as a delay or an error message?

**The shapes and tools**

| Shape / tool | What it represents | Example |
|---|---|---|
| **Swimlane** | One actor per horizontal lane | User · System · Ops team · Payment provider |
| **Rectangle** | An action by the actor in that lane | Ops team reviews the booking |
| **Diamond** | Decision point | "Booking above the auto-approval limit?" |
| **Parallelogram** | Automatic system step (input / output) | Locks the slot, sends confirmation email, validates the card |
| **Handoff arrow** | Work crossing from one lane to another | System → Ops team: "approval needed" |

```
┌──────────────────────────────────────────────────────────────┐
│  USER      │  Selects slot → Taps "Pay"        … sees "pending"│
├──────────────────────────────────────────────────────────────┤
│  SYSTEM    │  ▱ Locks slot → ▱ Requests payment → ▱ Sends email│
├──────────────────────────────────────────────────────────────┤
│  OPS TEAM  │            ◇ Needs approval? → Reviews manually  │
├──────────────────────────────────────────────────────────────┤
│  3RD PARTY │            Gateway processes → Returns result    │
└──────────────────────────────────────────────────────────────┘
```

**When to use it**
- The task involves more than one actor — checkout with a payment provider, onboarding where the system sends emails, admin features where a second user type acts on something the first one started
- The user flow looks fine but users still hit delays, errors, or confusion that screens cannot explain
- Before handing work to engineering — to show the back-stage logic behind each screen
- When aligning design, engineering, and operations on who owns which step

**What a well-drawn process map reveals**
- Handoffs with no clear owner or no visible status for the user
- Manual steps hiding behind an automated-looking screen
- Waiting time the user experiences but the interface never explains
- Steps that exist only because of how teams or systems are organised

**Running example — "Book and confirm a slot" (process map)**
Same task, four lanes. The system locks the slot and requests payment (parallelogram). The payment provider returns the result. Then the system hands the booking to the Ops team for manual approval — a handoff the user never sees. Approval can take hours. Meanwhile the user's screen says "pending."

What the user flow could not show: the "pending" is not a screen problem. It is a manual handoff. The structural fix is in the process (auto-approve below a limit, show approval status), not in the layout.

**User Flow vs Process Map**

| | User Flow | Process Map |
|---|---|---|
| **Perspective** | One user | The whole organisation |
| **Question it answers** | "What does the user go through?" | "Who does what, and where does work wait?" |
| **Actors** | The user | User, system, internal team, third parties |
| **Visibility** | Front-stage only | Front-stage and back-stage |
| **Shapes** | Pill, Rectangle, Diamond, Arrow, Note | + Swimlane, Parallelogram, Handoff arrow |
| **Best for** | Designing and checking a task path | Finding bottlenecks and aligning teams |
| **Order** | Draw first | Draw second, zoomed out from the flow |

---

### AI Workflow for User Flows and Process Maps

**What it is**
A repeatable way to use AI to build, check, and sharpen a user flow or process map — without letting AI invent the product. It is a workflow, not a prompt: eight steps, alternating between you and AI, with three checkpoints.

**Goal**
Use AI for what it does well (structuring notes, spotting gaps, widening options, writing diagram code) and keep for yourself what it cannot do (knowing what the product really does, deciding what to change).

**Scope**
- **In:** current-state maps of one task, as far as you and your sources know. A structural fix proposed from the map.
- **Out:** inventing a flow from a one-line description; knowing the system's real constraints; knowing why users behave as they do. Those need the product, the team, and real users.

**Why not just one prompt?**
Ask AI to "draw the user flow for booking a slot" and it returns a clean, plausible diagram in seconds. It is also made up. Nothing in it is tied to your product, and a polished diagram is the hardest kind to doubt. The fix is not a better prompt. It is a process where AI only works from facts you collected, and where every AI output goes through you before the next step.

**The principles behind the workflow**
1. **Facts first, AI second.** You walk the product and collect notes. AI works only from those notes.
2. **The table is the source of truth; the diagram is a view of it.** AI writes a step table first. You verify it. Only then does AI turn it into diagram code.
3. **Unknown is a valid answer.** Every row is marked stated, inferred, or unknown. A gap shown is better than a gap filled with a guess.
4. **Every claim points to evidence.** Each step cites a note ID. Each AI observation cites a row.
5. **Alternate you and AI.** No two AI steps in a row. Each AI output is reviewed by you before it is used.
6. **Keep the AI draft.** Your corrections go in a separate copy. The gap between them is your measure of how far to trust AI on this kind of task.
7. **Widen before you choose.** AI proposes at least three genuinely different ways to fix the worst step, and argues against its own conclusion. You decide.

**The workflow**

| # | Step | Who | What happens | Output |
|---|---|---|---|---|
| 1 | Frame | You | Task, entry and end, the job (from JTBD), constraints, method (User Flow / Process Map), and what you believe the flow is today | `Frame` |
| 2 | Capture the facts | You | Walk the product and take notes (one per step, with a failure state). For a Process Map, add back-stage facts from the team, each tagged with its source | Notes with IDs |
| 3 | Structure | AI | Turns the notes into a step table: shape, label, next step, evidence, status (stated / inferred / unknown). Lists gaps. No suggestions yet | `Table (AI draft)` |
| 4 | Verify · **Checkpoint A** | You | Walk the product again against the table. Fix a copy, never the AI draft. Resolve or keep visible every "inferred" and "unknown" | `Table (verified)` |
| 5 | Analyse | AI | User Flow: friction vs the job, three different ways to restructure the worst step, then argues against itself. Process Map: lanes, handoffs, waits, and questions for the team | `Analysis` |
| 6 | Decide the fix · **Checkpoint B** | You | Choose one structural change; say why the step exists today and what you would test. Check "removable" steps with whoever owns them | `Fix + decision` |
| 7 | Diagram code | AI | Converts the verified table to diagram code (Mermaid). Same steps, no additions | `Diagram code` |
| 8 | Draw and state limits · **Checkpoint C** | You | Render it, compare to the table, mark constraint-driven steps in red, write what the map cannot tell you | `Final diagram + limits` |

**The three checkpoints**
- **A (after step 4)** — Could someone else follow this table and reach the same screens? Is every "inferred" row confirmed or removed? If no → walk the product again.
- **B (after step 6)** — Were at least three different options considered? Does the fix trace to the job and to evidence in the table? If no → ask for alternatives again, and resolve unknowns with the team.
- **C (after step 8)** — Does the diagram contain exactly the verified steps? Is every unknown visible? If no → fix the code or the table.

**Two branches, one spine**

| | User Flow branch | Process Map branch |
|---|---|---|
| **Facts you collect** | Your own walkthrough notes | Walkthrough notes + back-stage facts with a source for each |
| **What AI adds at step 5** | Friction analysis and restructuring options | Lanes, handoffs, waits, and a list of questions to ask the team |
| **Order** | First | Second, reusing the verified table |

If the task has one actor, run the User Flow branch only. If friction cannot be explained by the screens, add the Process Map branch.

**The shape of the key instructions**
Every AI step in the workflow carries the same few lines. Use them as a checklist when you write your own:
- Use **only** the notes / table below
- Cite the **ID** for every claim
- Mark guesses as **inferred**; say **unknown** instead of filling a gap
- **Do not add, remove, or rename** steps
- Argue against your own conclusion: *what is the strongest reason this step exists, and what would change your mind?*
- Return **only your section**, in the stated format

**Starter instruction for step 3 (Structure)**
> *"Using only the notes below, build a step table for this task. Columns: ID, Shape (pill, rectangle, diamond, note), Label, Next (for a diamond, one row per branch with a label), Evidence (note IDs), Status (stated / inferred / unknown). Every step must cite at least one note. If you do not know what happens, write 'unknown' — do not fill the gap. Then list: diamonds with fewer than two branches, paths that never reach an end, and states with no coverage in the notes (empty, error, loading, success). No suggestions yet."*

**Watch out for**
- AI does not know your system's real constraints. It may suggest removing a step that is technically required. Check with whoever owns it.
- A clean diagram with no "unknown" rows is a warning sign. Real notes always leave gaps.
- Mermaid output looks authoritative. Always count nodes against the table.

**What this cannot tell you:** why users drop off, how long steps really take, or whether the fix works. That needs real users.

> Full step cards and instructions: `programs/ai-design-workflow/examples/user-flow-process-map/step-cards.md`
>
> One-slide view of the whole workflow (HTML): `programs/ai-design-workflow/assets/diagrams/user-flow-process-map-activity-flow.html`

---

## Tools & Materials

- One of your own projects (bring a working product or prototype to the session)
- FigJam or Miro — for drawing the user flow and the process map
- Screenshots of the relevant screens in the flow
- JTBD Map from Session 2 (used to choose which task to map)

---

## Practice Activity 1 — Map the Current User Flow · 20 min

Pick one real project you're working on. Choose one core task — the most important thing a user needs to do in this product. Map the flow exactly as it exists today: not how it should work, but how it actually works right now.

**Steps:**

1. **Choose your task** — pick one core user job from your JTBD Map. Make it specific: not "browse products" but "find and save a product for later." This is the scope of your flow.

2. **Define your entry point and end point** — draw a Start pill and an End pill before anything else.

3. **Walk through the flow step by step** — open your product (or prototype) and complete the task yourself, narrating every step aloud. Write each step on a sticky note as you go. Include every tap, every screen load, every decision.

4. **Assign shapes to each step:**
   - Rectangles for screens and user actions
   - Diamonds for decision points (login check, empty state, error condition)
   - Arrows with labels on every branch

5. **Add the error paths** — for each diamond, follow both the Yes and No branches. Where does the user go if something fails? If you don't know — that's a gap in the design.

6. **Add notes** — mark where the flow felt long, surprising, or unclear.

7. **Count the decision points** — how many times does a user have to make a choice before completing the task? Note which exist because of IA decisions (content is in the wrong place) vs interaction design decisions (the flow is poorly sequenced).

**Debrief prompts:**
- Which steps surprised you — ones you didn't realise existed until you walked through it?
- Which decision points could the system resolve automatically, removing a step entirely?
- Where does the flow break down if the user takes a wrong turn?

---

## Practice Activity 2 — Add the Back-stage Layer · 15 min

Take the same task and the same flow. Zoom out.

**Steps:**

1. **List the actors** — who or what takes part in this task besides the user? System, internal team, third party.
2. **Create one swimlane per actor** and move your user flow steps into the User lane.
3. **Add the back-stage steps** — for each user step, ask: what happens behind the scenes? Who or what does it? Place it in that actor's lane (parallelogram for automatic system steps).
4. **Mark every handoff** — each arrow that crosses a lane. Label what is passed.
5. **Circle the waits** — where does the user wait while someone or something else works?

**Debrief prompts:**
- Which back-stage step has the biggest effect on what the user experiences?
- Which handoff has no clear owner or no visible status for the user?
- Which problem from Activity 1 turned out to be a process problem, not a screen problem?

---

## Assignment (before next session)

**Build the current-state map and identify one structural fix.** Choose the method that fits your project.

1. **Choose your method:**
   - **User Flow** — if your task is mostly in the user's hands (one actor, screen-level friction)
   - **Process Map** — if your task depends on the system, a team, or a third party (multiple actors, handoffs, waiting)
   - Either way, state in one sentence why you chose it.
2. **Complete the map** for your chosen task in FigJam or Miro, using the correct shapes. For a Process Map, annotate every step with **U** (user), **S** (system), **T** (internal team), or **3P** (third party).
3. **Highlight in red** every step that exists because of an IA, system, or organisational constraint — not because it serves the user.
4. **Pick the single highest-friction step** and write a short rationale: why does this step exist, what would need to change structurally to remove it, and what would you test to validate the change?

**🤖 AI in Practice — use the workflow:**
Run steps 1-4 of the AI workflow on your task (frame, capture facts, AI builds the table, you verify it). Bring the AI draft table, your verified table, and the number of rows AI got wrong, invented, or missed. If you have time, continue to step 5 and choose your fix with it.

---

## Related Notion Resources

- [Design Activities by DT Stage — Reference](https://www.notion.so/3248a6b135db810385bdf06991f4f87a) — Card sorting and tree testing in context of the full DT cycle
- [Session 1 Playback — Design Thinking in Practice](https://www.notion.so/3318a6b135db81a2a1ebf83b4ec081a5) — "Organise for users — Evidence-based sitemap, Task flows"
- [Progress Tracker](https://www.notion.so/3238a6b135db816db041d2cfbc58fa8c) — Evidence-based sitemap is the S4 artifact

---

*Lesson: Information Architecture · Part of the 8-session UX Mentoring Program*
