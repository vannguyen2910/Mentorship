# Series Plan: Decisions and Lesson Skeleton

What we are building and what has been decided. Read this first. Evidence is in `01-research.md`; the method is in `02-method.md`; quality and measurement in `03-quality-and-measurement.md`.

**In this file**
- [Part 1 — Decisions log](#part-1--decisions-log)
- [Part 2 — Series skeleton: lesson names and learning objectives](#part-2--series-skeleton-lesson-names-and-learning-objectives)

---

## Part 1 — Decisions log

Running record of what Winnie and Claude have decided. Update this file whenever a decision changes. Research files in this folder (`01-` onward) inform these decisions but don't overrule them.

### Decided (2026-10-05)

| Decision | Choice | Notes |
|---|---|---|
| Audience | **Mid/senior designers** | Students must already have design foundations. No teaching of basics. |
| Main outcome | **Run a repeatable AI workflow** | A chain where each step's output is the next step's input. Not prompt tips, not tools. |
| Gate list unified | **Done 2026-10-05.** One canonical list: four stage gates, 16 lettered checks (1a to 4d), in `02-method.md` Part 3, §2. Replaces the six-stage gate table, the per-lesson gate wording and the four named gates. Stage map, lesson plan, competitor example (each activity gate names the check it supports) and the hub (gate cards show the checks, status derived) all use it. Discover's gate is now "Question + evidence" because the co-define agreement is check 1a | Review item resolved. Checks are my wording; tune after the pilot |
| Quality gate | **Mix by stage; one canonical list** | Four stage gates, each a short list of lettered checks (1a to 4d). The only gate list is in `02-method.md` Part 3, §2; the stage map, lesson plan, hub and activity flows all use it. Activity gates (A, B, C) each name the stage check they support. |
| Series size | **8–10 lessons** | Foundation + stages (concept and practice) + capstone. |
| Output storage | **One living working file** (sections per step) + `sources/` folder; each activity's shareable output is an HTML page that becomes a page of the Experience Hub | Replaces the earlier one-file-per-output idea. See `02-method.md` Part 1 §3. |
| Final report = **Experience Hub** | **One hub that stores every output of the case and lets the designer cross-reference them** (opportunity ↔ hypothesis ↔ decision ↔ principle ↔ test ↔ metric). Built page by page across the series; finished in the capstone | Defined 2026-10-05. See `03-quality-and-measurement.md` Part 1 ("The Experience Hub") |
| Data safety | **Lesson 1 teaches a data-safety block (10 min of the 90-minute session):** why it matters (confidentiality, NDAs, company policy, Vietnam's 2025 personal data law in force from 1 January 2026), the fact that consumer plans of AI tools may use conversations to improve models unless switched off, a three-kind sort (safe / ask first / never in a public tool) with a six-card exercise, four habits (check policy, classify, remove identifiers locally, contain the folder), plus publishing and ownership notes. Output: `00-context/data-rules.md`. Lesson 1 timings were later rebalanced and then refit to the 90-minute class (12 / 21 / 10 / 25 / 8, plus a 14-minute buffer) | Added 2026-10-05 after the content review. Not legal advice; recheck vendor terms and the law before teaching |
| Account trade-off | A GitHub account is needed **only to publish** a shareable hub. The hub repository must be public (free Pages publishes only from public repositories; a private repository does not make a Pages site private). A student may keep their whole case in a separate private repository as a backup | Updated 2026-10-05: no longer required for everyone. Recheck GitHub's plan rules before teaching |
| Tools students bring | **Every student brings at least one AI tool to class** (decided 2026-10-05): an **AI chat tool from week 1**, and an **AI coding tool by week 6** (the prototype weeks). Recommended examples: **Claude** (chat), **Cursor** and **Codex** (coding). Any equivalent tool is fine if the student's company allows it and it accepts attached files. The lesson text and slides stay generic ("AI chat tool", "AI coding tool"); the named examples live in **one student handout**, `assets/templates/tools-to-bring.md`, which is a scoped exception to the generic-labels convention | Selection order: company-allowed first (see data safety), then it must take an attached file, then data controls, then cost. Not verified: current features, plans, prices and data controls of the named tools; the handout tells students to check, and the instructor confirms the recommended list before the course. A student whose company bans AI tools uses the course case card in class |
| Class format | **One online session a week, 7 to 8 students, 10 sessions.** Each week: up to 15 minutes of prep (a one-page brief), a **90-minute live working session**, up to 60 minutes of homework (about 2.5 to 2.75 hours in total, within the students' 2 to 3 hours). Live = a short teach, then applying the step to the student's own case in breakout rooms of 3 to 4 with coaching | Decided 2026-10-05. Detail in "Class format and timeline" below |
| Timeline | **10 weeks, about 2.3 months** (about 27 student hours). An optional catch-up week would make it 11 weeks, about 2.5 months (still open) | |
| Own case is the default | Students bring their own case and want to apply the teaching and the mentoring to it. The course case card and a stand-in PO are fallbacks | Reverses the earlier "outside-in or shared case by default" |
| Discover in 90 minutes | **Option B:** user-voice synthesis live; competitor analysis as a short live demo (about 20 minutes) with the full analysis as optional homework; interviews: the AI-assisted synthesis is taught on evidence the student already has | Decided 2026-10-05 |
| Hosting and sharing | **The hub is private by default** (decided 2026-10-05): it lives in the student's case folder on their own computer; to show a stakeholder they export pages to PDF or send the folder zipped. **Publishing is optional** and only for a case free to share (a course case, or a cleaned-up version): the student publishes on GitHub Pages in their own public repository, **hosts it and is responsible for it**. Winnie does not host, upload, list or moderate hubs. Guide: `assets/templates/publish-guide.md` (optional homework) | Replaces the earlier "everyone publishes publicly in Lesson 1" plan, which assumed shared cases. Most students bring their own, often confidential, cases. A private live link would need a paid password plan or the company's own hosting; that is not part of the course |
| Hub robustness | **Done 2026-10-05.** `hub-guard.js` records data-file errors; `hub.js` checks `hub-data.js` and each page and shows a setup-problem box instead of a blank page (syntax errors, duplicate or bad IDs, broken links, type or page mismatches, items listed but not written or written but not listed, bad gate or access values); one bad entry no longer stops the rest; a noscript message; README troubleshooting and a safe-editing instruction for AI tools. Example metric corrected to "4 of 5 finish unaided" (five users give counts, not rates) | Tested with good data and four kinds of broken data in a browser. Not yet tested with students. Not done: AI-synced data, and a guard against gaming the warnings by linking one principle to everything |
| Hub template | **Built** (`assets/templates/hub/`): folder of 9 linked pages; `hub-data.js` is the one file with every ID and link; the Overview computes the alignment table and warnings | Untested with students |
| Activity page | Each activity ends with an HTML page that students build themselves from a provided template; it becomes **one page of the hub**, not a standalone report. Competitor analysis is the first example | Example: the hub's Evidence page, `assets/templates/hub/evidence.html` (the earlier standalone template is archived) |
| Measurement scope | **Pre-launch usability metrics are the core** (students rarely have post-launch access); post-launch is background | `03-quality-and-measurement.md` Part 2 |
| Measurement framework | **One framework: Goals → Signals → Metrics**, using HEART's Task success and Happiness pre-launch | Others: ask the PO to track after launch |
| Business metrics | Designers rarely see them (PO owns them). Teach students to **ask actively** and to record assumed metrics as unconfirmed | PO question kit in Part 2 of `03-quality-and-measurement.md` |
| Positioning | **Design is a strategic partner that co-defines the requirement with business and product, not a recipient of the PRD.** Start from the business question; any existing PRD is a draft to improve | Stage map, Lesson 2 (now "Shape the brief with your PO"), and the Define output ("shared problem brief") updated |
| Access risk | **Some students have no access to the PO or business.** The series degrades gracefully: three access levels (full, limited, none) with a written-questions fallback; AI never plays the PO; unconfirmed outcomes are recorded as assumed; agreement status travels with the scope and brief | Lessons 2 and 4 in `00-plan.md` Part 2; mention in Lesson 1 |
| Lesson 1 | **The existing lesson `ai-workflow-for-ux-designers` is Lesson 1**, re-scoped to AI terminology and project folder structure. Series is now numbered 1–10 | **Re-scope applied 2026-10-05** (lesson and slide outline rewritten, in sync; old deck archived; deck not rebuilt). Mapping in `00-plan.md` Part 2 |
| Principles sufficiency | **Nielsen's 10 are enough** for students whose company has no written principles | No need for the Foundation lesson to add product-specific ones |
| UX principles | **Nielsen's 10 heuristics as the baseline**; add the organisation's own UX, business and service principles where they exist | `03-quality-and-measurement.md` Part 1 |
| Hypothesis granularity | No standard; depends on the solution. Rule of thumb in Part 1 of `03-quality-and-measurement.md` | |
| Alignment check | **Lives in the closing block of "Refine and check your design"** (about 30 minutes; the hub builds the matrix, so the manual part is the principle audit), with a light version at every activity's last gate (standard rule 12) | Revised 2026-10-05. The separate critique-loop lesson is removed; challenging before deciding is already a step in every activity flow |
| Prototype lessons | **Two lessons, not one:** "Build your first prototype" (first version on the design system) and "Refine and check your design" (refine, then the alignment check). The series stays at 10 lessons | Decided 2026-10-05: prototyping on a design system takes longer than one lesson |
| Discover widened | **Discover is no longer competitor-centric.** The main activity is a user-voice synthesis (real quotes from reviews, forum posts and short interviews); competitor analysis is the second. Rule: every evidence pack pairs what others do with what users say or do | Decided 2026-10-05, after the content review. New: `examples/user-voice-synthesis/` |
| Stage map | **Define output = problem brief with outcome + success metrics, ranked opportunities, hypotheses, principles** | Diagram updated; alignment check shown at every gate |
| Activity method | **Generic standard for all activities**; competitor analysis is one worked example | `02-method.md` Part 1 and `02-method.md` Part 2 are generic; examples live in `examples/` |
| Diagram style | Flat fills, no bold outlines | activity flows follow this |
| Tool naming | Generic labels only ("AI chat tool", "AI coding tool") | Per CLAUDE.md general lesson conventions. |

### Framing from Winnie (source of the series)
- Market fear: designers who only receive a PRD from the PO and turn it into screens fear AI will take their job. **Response (decided 2026-10-05):** do not wait for the PRD; co-define the requirement with the business and product.
- "AI won't replace people; people who use AI will replace people who don't."
- Goal: leverage existing design skill with AI as an assistant in daily work, with systematic thinking, not a prompt course.
- Every AI idea or solution must pass the UX principles and outputs defined earlier in the workflow.

### Still open
1. Where does the existing lesson `ai-workflow-for-ux-designers` fit in the series? (Not yet re-read against the new outline.)
2. How strict is "no code" for the prototype stage? (Assumed: no code written by the student; AI coding tool does it.)
3. Capstone format: individual project on a real work case, or a shared case study?
4. Vietnam validation: interview 5–8 local designers or hiring managers (see `01-research.md` Part 3).

### Series vocabulary (plain-language rule, 2026-10-05)
Use **one name per idea**, and nothing else, in anything a student reads. Define a term on first use. Do not add new terms without adding them here.

| Say | It means | Do not say |
|---|---|---|
| **case**, **case folder** | The project the student works through, and its folder | case file, project file |
| **working file** | The one Markdown file an activity fills, section by section | living file |
| **context pack** | The `00-context` folder pasted into AI steps first | constraint layer |
| **hub** (Experience Hub on first use) | The connected website that holds every output | final report (only for the finished hub) |
| **output** | A file or page a step produces | artifact, deliverable |
| **gate** and **check** | A gate is a short checklist before moving on; a check is one yes/no question (1a, 3b …) | — |
| **stage map**, **activity flow**, **step card** | The three views: the whole series, one activity, one step | Level 1, Level 2, Level 3 |
| **pattern** (Investigate or Generate) | The starting shape of an activity flow | archetype |
| **alignment check**, **alignment table** | Does each decision trace to a user need and pass the principles | alignment matrix |
| **opportunity** | A user need worth solving, backed by evidence | — |

Plain wording for hub warnings and reviews: a **decision with no user need behind it** (not "orphan"), an **opportunity with no decision** (not "uncovered"), a **decision that pulls against a principle** (not "strain"), **word for word** (not "verbatim"), **access levels** full, limited and no access (not "tiers"), and "**if no, go back to step N**" (not "go-back rule"). The internal key `rel: "strains"` in the hub data file stays as it is; students never see it.

### File index
- `00-plan.md` — this file: decisions and the series skeleton
- `01-research.md` — market research, risks, Vietnam market, teaching notes
- `02-method.md` — activity flow standard, step card template, stage methods and gates
- `03-quality-and-measurement.md` — traceability and alignment check, measuring success
- `examples/` — two worked examples: competitor analysis and user-voice synthesis (step cards; diagrams are in `assets/diagrams/`)
- `assets/starter-files/` — the weekly starter files: a case folder template, the fictional course case (case card, PO case pack, 24 quotes with an answer key, three competitor pages), a prototype starter with a small design system and rules file, and a working checkpoint prototype
- `assets/` — diagrams, templates (competitor page; **Experience Hub** in `templates/hub/`), reference images and `SOURCES.md`
- `_archive/` — the original 11 separate files, kept unchanged

---

## Part 2 — Series skeleton: lesson names and learning objectives

**Created:** 2026-10-05 · **Status:** draft for discussion. Built from decisions in `00-plan.md` Part 1 and the method in Part 1 of `02-method.md`–Part 1 of `03-quality-and-measurement.md`. Nothing here is taught or tested yet.
Lesson folders would be siblings under `ai design workflow/`, each with its own `materials/`, `slides/`, `assets/` (slugs suggested below). Per CLAUDE.md, lesson content stays generic: no tool names, no mentee names.

### Series
**Working title:** AI Design Workflow for Experienced Designers
**Audience:** mid/senior UI/UX/product designers with design foundations (no basics taught).
**Series outcome:** *By the end, the designer can act as a strategic partner: start from the business question, co-define the requirement with product and business, then run a repeatable AI-assisted workflow to a validated, handoff-ready prototype, where every step's output is the next step's input and every output passes a review gate.*
**Prerequisites:** working knowledge of research, UX design and prototyping; an AI chat tool from week 1 and an AI coding tool by week 6 (recommended examples in `assets/templates/tools-to-bring.md`); one case to use across the series. **Default: the student's own case** (see Case model below). Fallback: the course case card.
**Positioning (decided 2026-10-05):** designers do not wait for the PRD to arrive. They start from the business question and shape the brief, so the PRD becomes something they help write, not something they receive. Where a PRD already exists, it is treated as a draft to improve.
**Through-line:** one case from lesson 1 to the capstone. Each lesson adds one section to the same case folder.
**Case model (revised 2026-10-05):** the default case is the **student's own case** (real or realistic), because students come to apply the teaching and the mentoring to their own work. Their hub is **private by default**. Confidential material is anonymised before it goes into an AI tool or into class, and what is shared in class stays in class (a cohort ground rule). **Fallbacks:** the course case card (a fictional meal-kit app) for students whose company bans AI tools or whose case is too sensitive for class; a **stand-in PO** (a peer or the instructor, from a case pack) for the co-define conversation when a student has no access to a real PO. The real PO conversation happens during the week; the live session rehearses it. Case pack template: `assets/templates/po-case-pack-template.md`.

### Class format and timeline (decided 2026-10-05)
**Rhythm.** One online session a week, 7 to 8 students, 10 weeks. Students have about 2 to 3 hours a week in total, so each week is:
| Part | Time | Rule |
|---|---|---|
| Prep before class | up to 15 min (about 20 in week 1, for the tool test) | A one-page brief (the week's terms or steps), never a video |
| **Live working session** | **90 min** | A short teach, then apply the step to your own case in breakout rooms of 3 to 4, with coaching. Never depends on homework having been done |
| Homework | up to 60 min | One deliverable per week (the next hub page), with a minimum version and any extra marked optional |
| **Total** | **about 2.5 to 2.75 hours** | |

**Rules that make it fit**
1. **Starter files every week** (drafted 2026-10-05 in `assets/starter-files/`; its `README.md` maps each week to its files). A student who skipped homework is handed that week's starting folder, so nobody is blocked.
2. **Real data, anonymised, or a fallback.** Students use their own evidence and material, anonymised. If their company bans AI tools or the case is too sensitive, the course case card stands in.
3. **Coaching in small rooms.** With 7 to 8 students, two rooms of 3 to 4; review two hubs live each session.
4. **Confidentiality ground rules** said at the start of week 1: what is shared in class stays in class; share only what you are comfortable showing; anonymise first.
5. **Minimum viable homework.** If time is short, do the required part only; optional parts never block the next session.

**Timeline.** 10 weeks is about 2.3 months and about 27 student hours. An optional catch-up week (not yet decided) would make it 11 weeks, about 2.5 months.

**Week by week** (first split; untested)
| Week | Lesson | Live (90 min) | Homework (up to 60 min) | Starter file |
|---|---|---|---|---|
| 1 | Set up your AI workspace | Demo, terms in action, data safety, build the case folder | Finish the context files (35); share your hub, optional (25) | Case folder template, empty hub |
| 2 | Shape the brief | Rehearse the PO conversation in pairs; AI prepares questions; draft the scope | Hold the real conversation, or send the written questions; record the agreement status (40) | Scope page; case pack if no PO access |
| 3 | Research you can trust | User-voice synthesis on your own anonymised evidence (or a prepared quote set); 20-minute competitor demo | Verify and write opportunities (60); competitor analysis optional | Prepared quote set |
| 4 | Frame the problem | Write the problem brief: opportunities, hypotheses, success metrics, principle checks | Polish the brief page (45) | Brief template |
| 5 | Explore ideas | Three directions, choose one, flows | Flows and content (45) | Directions template |
| 6 | First prototype | Design-system notes, rules file, build the first version | Extend the main flow (60) | Starter prototype project with a rules file |
| 7 | Refine and check | Refine, states, system and accessibility check, alignment check on the top three decisions | Fix the findings (45) | Checkpoint prototype |
| 8 | Test with users | Test plan and script; peer usability tests (students test each other, under the ground rules) | One or two outside tests, optional (45) | Test plan template |
| 9 | Hand off and measure | Handoff pack, measurement plan for the PO | Finish both (45) | Handoff template |
| 10 | Capstone | 7 to 8 presentations of about 8 minutes, plus feedback | None | None |

### Overview
Lesson 1 is the existing lesson `ai-workflow-for-ux-designers` ("Set Up Your AI Workflow"), re-scoped to **AI terminology and how to structure your project folder** (decided 2026-10-05). The context pack moved: the context pack starts in Lesson 1's folder, principle checks are written in Lesson 4 (they are part of the problem brief), and the design system context is added in Lesson 6.

| # | Lesson | Stage | Main output (feeds next) | Gate checks practised (see `02-method.md` Part 3, §2) |
|---|---|---|---|---|
| 1 | Set up your AI workspace | Foundation | Case folder with context pack started; shared vocabulary | (sets up all gates) |
| 2 | Shape the brief with your PO | Discover | Shared scope: business question, outcome and success metrics agreed with the PO, beliefs | 1a |
| 3 | Turn research into insights you can trust | Discover | Evidence pack: what users say (reviews, interviews) plus what others do (competitors) | 1b, 1c |
| 4 | Frame the problem worth solving | Define | Shared problem brief (the requirement), co-signed: outcome, opportunities, hypotheses, principle checks | 2a to 2d |
| 5 | Explore ideas and pick a direction | Develop | Three directions, one chosen; flows and content | 3a |
| 6 | Build your first prototype | Develop | First working prototype on the design system | 3d (design system) |
| 7 | Refine and check your design | Develop | Refined prototype + alignment table + principle audit | 3d, 3b, 3c |
| 8 | Test with real users | Deliver | Findings (task success, time, errors, SUS) | 4a, 4b |
| 9 | Hand off and measure success | Deliver | Handoff pack + measurement plan | 4c, 4d |
| 10 | Capstone: present your case | All | Complete case + portfolio piece | all |

---

### Lesson 1 — Set up your AI workspace
*Existing lesson:* `ai-workflow-for-ux-designers` (keep the folder and slug; the lesson title is now "Set up your AI workspace"). *Re-scoped from* "Set Up Your AI Workflow", then **rebalanced 2026-10-05** (see below).
**Why:** every later lesson assumes students can follow AI terms, know what is safe to give an AI tool, and keep their work in a folder the AI can use. This lesson gives them that once, so no later lesson re-teaches it.
**By the end, students can:**
1. Explain ten core AI terms in their own words: AI chat tool, AI coding tool, context, context window, grounding, hallucination, agent, connector (MCP), reusable instructions (skills, rules files, project memory), and AI-assisted vs AI-generated. (Model, prompt and in-tool AI features are covered in passing.)
2. Recognise Markdown and HTML, and explain why a plain local folder matters.
3. Set up the series **case folder** with the standard layout, a started context pack and an empty hub.
4. Reuse a saved file as context instead of retyping, and ask for a source pointer and an "unknown" answer.
5. Decide what is safe to give an AI tool: sort material into safe, ask first and never in a public tool; anonymise before pasting; write their own data rules.
6. Explain how to share their hub with a stakeholder: private by default (a PDF or zipped folder), published on GitHub only when the case is free to share.
**Key activity:** an instructor demo of one task done twice (vague vs structured instruction on a case card), then build the case folder and run one instruction against a saved file. **Homework (up to 60 minutes):** Assignment 1 (case folder, required, about 35 minutes) and Assignment 2 (share your hub, optional, about 25 minutes: PDF export, or publish if the case is free to share).
**Output:** case folder with `00-context/` started (product and users, accessibility rules, data rules, optional glossary) for the student's own case, and an empty hub (private).

**Rebalance (2026-10-05, for the earlier 120-minute version)** — fixes from the content review (overloaded, no early value):
| Before | After |
|---|---|
| 120 minutes fully used (13 / 38 / 23 / 30 / 16), no slack | **106 minutes of content + 14 minutes buffer** (14 / 30 / 18 / 30 / 14) |
| First value came late (after terms and folders) | **"One task, done twice" demo in the first 14 minutes**: a vague and a structured instruction on a case card, so the terms later explain something students have already seen |
| 14 terms in 5 groups, 15 + 15 minutes | **10 terms**, 12 minutes of terms + 10-minute pair activity; model, prompt and in-tool features in passing |
| Separate stat slides; Markdown to HTML pipeline slide; "public means" slide | Merged or folded into speaker notes; 38 slides become **35** |
| GitHub teach 7 minutes with its own public-link slide | **5 minutes**, two slides; the public/private rules are in the speaker notes of the five-steps slide and in the guide |
| Lesson file ~6,000 words | **~5,100 words** (outline ~5,000) |
**Refit to the 90-minute class (2026-10-05).** The weekly format (see Class format) shrinks the live session from 120 to 90 minutes: terms and folder detail move to a one-page pre-read (the Week 1 brief, inside the lesson file); live phases are 12 / 21 / 10 / 25 / 8 minutes plus a 14-minute buffer; Activity 1 is 5 minutes; the data safety block stays; GitHub publishing becomes optional homework; the lesson file is about 4,550 words and the outline has 30 slides. Terms are taught "in action" against the demo, not read out.
Superseded by the refit above for the 90-minute class: the GitHub teach is now optional homework and the case model is the student's own case by default. Kept: the data safety block (now 10 minutes of the live session), never to be cut.
Still true: this is the heaviest lesson in the series; a pilot should check the clock. Cut order if it overruns: "reuse" block in Phase 3, then the Phase 5 hub description, never data safety.

### Terminology list (ten terms; rebalanced 2026-10-05)
| Group | Terms |
|---|---|
| The tools | AI chat tool, AI coding tool |
| Talking to the AI | context, context window, grounding |
| When it goes wrong | hallucination (why "unknown" is an allowed answer) |
| How some tools act | agent, connector (MCP) |
| Carrying your standards | reusable instructions: skills, rules files, project memory |
| Stance (covered in the mindset phase) | AI-assisted vs AI-generated |
In passing, not on the cards: model, prompt, in-tool AI features, tokens. Markdown, HTML and the local folder are taught as files, in the folder phase. Basis: Figma describes MCP as the interface that lets AI tools read designs, and skills as reusable markdown instructions ([Figma — design systems, AI and MCP](https://www.figma.com/blog/design-systems-ai-mcp/)); other terms are standard usage. Keep each to one plain sentence plus a designer example.

#### The case folder students build (replaces Options A/B/C as the series default)
```
[case-name]/                         one plain local folder per project
├── 00-context/                      the context pack, pasted into AI steps first
│   ├── product-and-users.md
│   ├── principle-checks.md          (written in Lesson 4)
│   ├── design-system-notes.md       (added in Lesson 6)
│   ├── accessibility-rules.md
│   └── data-rules.md
├── 01-discover/                     one living .md file per activity, plus sources/
├── 02-define/                       problem-brief.md
├── 03-develop/                      options.md, alignment.md, prototype/
├── 04-deliver/                      test-plan.md, findings.md, handoff.md
├── hub/                             the Experience Hub: one HTML page per activity, plus index.html (started in Lesson 1 from a template, grown every lesson)
└── case-log.md                      the decision log: one line per decision and why
```
**Why this suits AI work:** numbered stage folders keep order; one file per activity gives each AI step a named input; `00-context` is the first thing pasted into every step; short plain-text files are easy to give the AI selectively; and an AI coding tool can open the whole folder as its project. Keep it a plain local folder while an AI tool is writing files; copy to cloud storage afterwards (as the existing lesson already teaches).
The existing lesson's three options (by stage, by file type, by deliverable) become *alternatives students may know about*; the series uses the stage layout because later lessons point to it.

#### Mapping the existing lesson to the new scope
| Existing part | Keep / trim / replace |
|---|---|
| Overview and objective 4: AI-assisted vs AI-generated | **Keep.** It is the throughline |
| Phase 1 Mindset (data, role shift) | **Trim to ~10 minutes.** The series already opens with the market case; keep the 91% / 7-tool data and the split finding (Figma, 36/35/29). **Add the partner message:** designers who wait for a PRD are the most exposed; the series moves them upstream. Say plainly that access to the PO and business varies, and that the workflow still works when it is limited (see the access risk in Lesson 2). The existing role-shift line ("maker to strategist and editor") is the natural place |
| Phase 2 Technical literacy (Markdown, HTML, local folder, three folder options) | **Keep and extend.** Add the terminology list above; replace the three folder options with the case folder |
| Phase 3 CARE prompting + feed forward / context | **Keep, shorten.** Keep feed-forward and context reuse. Keep CARE as a light frame and map it to the series instruction checklist: Context = sections you give; Ask = the task; Rules = use only the provided material, say "unknown", return only your section; Examples = the format wanted |
| Phase 4 Four buckets mapped to five Design Thinking stages | **Replace.** Use the Double Diamond stage map (`assets/diagrams/ai-design-workflow-double-diamond.svg`) as the preview of the series. Move the bucket examples out; the later lessons cover them |
| Phase 5 Build your workflow | **Keep, change the content:** build the case folder, run one instruction against a saved output |
| Activity 1 (stage-mapping canvas) | **Rework** onto the four-stage map, or drop in favour of the folder build |
| Homework | Review after the above |

#### Issues found in the existing lesson (fixed 2026-10-05)
1. ~~Tool brand names in student-facing text~~ **Fixed.** Generic labels only.
2. ~~Private mentee names in the activity notes~~ **Fixed.** The old private-mentee notes and the second assignment (capturing screens for a Design Thinking-era lesson) were removed.
3. ~~Program framing (ux-class, five Design Thinking stages)~~ **Fixed.** Front matter now `program: ai-design-workflow`; content uses the four-stage series map; no Design Thinking dependency.
4. ~~Unverified figures~~ **Fixed.** The McKinsey figure and the "Meet Ari" framing were dropped. Phase 1 now uses the AI + Design 2026 and Figma figures that were checked in this research.
5. ~~Missing partner framing~~ **Fixed.** Phase 1 now carries the partner stance and the honest note about access.
6. ~~Sync rule~~ **Done.** Lesson and slide outline rewritten together (34 slides). **The deck (HTML) has not been rebuilt.** The previous deck is in `slides/_archive/`, so it no longer shows as a deck link. The root-level copy `AI Workflow Deck.html` in the lesson folder and the old `materials/ai-workflow-for-ux-designers-brainstorm.md` are untouched and describe the earlier version.

---

### Lesson 2 — Shape the brief with your PO
*Slug:* `shape-the-brief`
**Why:** Designers who only receive a PRD are the most exposed. This lesson moves them upstream, to where the requirement is shaped.
**By the end, students can:**
1. Start from the business question (a goal, idea or problem) instead of waiting for a finished PRD, and treat any existing PRD as a draft to improve.
2. Use an AI chat tool to prepare for the conversation: questions for the business, assumptions to test, and what evidence exists or is missing (verified against what they actually know).
3. Ask the PO and the business for the outcome, the success metric and its baseline, and record any metric they could not confirm as "assumed".
4. Bring evidence to the table (even a small piece) to earn a say, and write a shared scope that the PO agrees to.
5. Write down what they already believe so it can be tested later.
**Key activity:** Shape-the-brief flow (Investigate pattern, adapted): you gather what exists → AI prepares questions and assumptions → you verify → you meet the PO and business (a human-only step: the real PO during the week, rehearsed in pairs in class; a stand-in PO from a case pack for students with no access) → AI turns your notes into a draft scope → you verify against the notes → you share back and agree *(to draw)*.
**In class:** rehearse the conversation in pairs, about 10 minutes each way. The PO player answers only from a fact sheet (sanitised facts the student writes about their own stakeholder, or the course case pack) and says "we haven't decided that" for anything else. The real meeting happens during the week; students without access use the written-questions route below.
**Output:** `## Scope`: business question, outcome, metrics (confirmed or assumed), beliefs, and an **agreement status** (agreed / pending / not available).
**Partner moves taught:** ask early, bring a small piece of evidence, write things down and share them back, and treat the draft as shared property.

#### ⚠️ Access risk: some students cannot reach the PO or the business
Some students truly have no access to the PO or the business. **The default case is now the student's own, so the three access levels below apply to everyone.** The stand-in PO (a case pack, played by a peer or the instructor) is the rehearsal and the fallback for students with no access. Teach the levels so students know what to do when the meeting is not available, and make the workflow work in all three:

| Access level | Situation | What the student does | Agreement status |
|---|---|---|---|
| 1 Full access | Can meet the PO and business | Run the meeting step, then share the draft scope back and get agreement | **agreed** |
| 2 Limited access | Can message or reach the PO indirectly (via a lead, PM or account manager) | Send the AI-drafted written questions and an assumptions memo, with a response date. Ask for corrections, not for a full meeting | **pending** until answered |
| 3 No access | Cannot reach the PO or business at all | Build the scope from what exists (the PRD or brief, public company information, product data they can see, colleagues who do talk to the business). Record every outcome and metric as **assumed**. Choose usability measures they control (task success, time, errors, SUS). Flag the scope as unconfirmed in the case log | **not available** |

**Fallback flow step (for limited and no access):** replace "you meet the PO and business" with "you send written questions and an assumptions memo". The AI drafts both from the student's materials; the student edits and sends them. If nobody replies, the student proceeds on labelled assumptions and carries the risk forward.
**Rules for the AI in this lesson:** it prepares questions and drafts notes. It must **not** play the PO and supply business facts or "typical" metrics. Simulated answers are not evidence (see the synthetic-user finding in `01-research.md` Part 2).
**What the student still gains with no access:** a written, assumption-flagged scope that someone can correct later is better than designing from a brief with the assumptions hidden. It also gives them something to show when they do get a seat.
**Teach this honestly in class:** say plainly that access varies, that having no access is a weaker position, and that the workflow is built to degrade gracefully, not to pretend the problem does not exist. *(⚠️ The access levels are my design, not tested; the Vietnam context is described in `01-research.md` Part 3 with low-confidence sources.)*

### Lesson 3 — Turn research into insights you can trust
*Slug:* `research-you-can-trust`
**Why (widened 2026-10-05):** competitor analysis shows what rivals do. It cannot show why users behave as they do, so a Discover built on it alone is the weakest evidence. This lesson pairs two kinds of evidence and keeps the AI honest on both.
**By the end, students can:**
1. Choose evidence types that fit their question from a menu, and always pair **what others do** (competitors, desk research) with **what users say or do** (reviews, forum posts, interviews, tickets, analytics).
2. Run a **user-voice synthesis**: the AI works only from real, anonymised quotes (public reviews and forum posts, plus 3 to 5 short interviews), returns every quote word for word with its ID, and may answer "unclassified" or "unknown".
3. Verify it: trace each top theme to its quotes, confirm they are word for word, read a sample of what the AI left out, count the errors, and decide whether to rerun a step.
4. Weigh themes by severity, context and reach, not by count alone, write opportunity candidates with quote IDs, and state what the sample cannot tell them.
5. Run a competitor analysis as a second activity, and combine both into one evidence pack.
**Key activities:** **User-voice synthesis** is the main in-class activity ✅ (`examples/user-voice-synthesis/`, flow and step cards). **Competitor analysis** is the second ✅ (`examples/competitor-analysis/`): a 20-minute live demo, with the full analysis as optional homework. Interview synthesis, desk research and support tickets are variations of the same flow (swap the source in step 4). *(Assumed split for 90 minutes: user voice about 50, competitor demo about 20, combining the evidence pack and wrap-up about 10, buffer 10. Students use the evidence they already have, anonymised, or a prepared set of quotes. Untested.)*
**Evidence menu (pick by question):**
| Evidence | Tells you | Source type | Watch out for |
|---|---|---|---|
| Competitor analysis | What others do | Public pages | Not why users choose; copying competitors |
| Desk research | What is known | Articles, reports | Invented citations; check each claim against its source |
| Public reviews and forum posts | What users say, at scale | Secondary | Skew to extremes; fake reviews |
| Short interviews (3 to 5) | Why, and past behaviour | Primary | Small sample; polite friends; personal data and consent |
| Support tickets, analytics | Real problems, real behaviour | Internal | Data safety; access; anonymise |
**Data safety applies here:** anonymise before the AI sees any quote (find and replace on your own computer), and keep real-work data private (Lesson 1).
**Output:** `## Evidence` (AI draft and verified) plus `## Themes` / `## Patterns`; the Evidence page in the hub; the evidence pack that feeds the problem brief. Gate checks 1b, 1c (and 2a when the evidence supports an opportunity).

### Lesson 4 — Frame the problem worth solving
*Slug:* `frame-the-problem`
**By the end, students can:**
1. Turn an evidence pack into a ranked list of opportunities (user needs, not features), each linked to its evidence.
2. Turn Nielsen's 10 heuristics (plus any organisation principles) into yes/no principle checks for this product, saved in `00-context/principle-checks.md`.
3. Write testable hypotheses for the solution direction ("we believe X for Y will change Z, and we will know because M") and set the right level for each.
4. Define success using Goals → Signals → Metrics, choosing metrics they can measure before launch.
**Key activity:** Problem brief flow *(to draw)*.
**Output:** the shared problem brief, co-signed by product and business, which becomes the requirement: outcome and success metrics, ranked opportunities, hypotheses, principles to check against.
**Partner move:** walk product and business through the brief and get their agreement before design begins; a PRD, if one is written, is written from this.
**If access is limited or absent (see Lesson 2):** the "agreement" part of the gate cannot be met. Carry the Lesson 2 agreement status into the brief, mark every unconfirmed outcome and metric as **assumed**, and keep the evidence part of the gate fully intact. Students in no access still complete the brief; it is labelled "unconfirmed by business".

### Lesson 5 — Explore ideas and pick a direction
*Slug:* `explore-ideas`
**By the end, students can:**
1. Direct an AI chat tool to generate at least three genuinely different directions from the problem brief and constraints.
2. Select a direction by checking each against the principle checks and the opportunities, and record why the others were set aside.
3. Shape user flows and content with AI drafts they edit and own (no AI-written final copy without review).
**Key activity:** Ideation and flow flow (Generate pattern) *(to draw)*.
**Output:** chosen direction, flow, content model.

### Lesson 6 — Build your first prototype
*Slug:* `build-your-first-prototype`
**Why (split 2026-10-05):** prototyping on a design system takes more than one lesson. This one gets a first working version, built the right way.
**By the end, students can:**
1. Write `00-context/design-system-notes.md` (tokens, components, patterns, do and don't, accessibility rules) in a form an AI coding tool can read, and put the standing rules in a rules file.
2. Set up the prototype project in the case folder: rules file, flow and content model from the previous lesson, and a clear view of what the tool can see and change (agent, connector).
3. Compare a vague instruction with a constrained one on the same screen, and explain the difference. (Detailed specifications, linked design files and stated accessibility requirements improve results; vague instructions give generic layouts.)
4. Build the first version of the main flow, one screen at a time, by checking the files the agent changed, not only its reply, and saving each working state.
5. Judge fidelity, and know the prototype is a reference, not production code.
**Key activity:** Prototype build flow (Generate pattern) *(to draw)*.
**Output:** a first working prototype in `03-develop/prototype/`, design system notes, a rules file, and the first design decisions (D items) in the hub. Gate check 3d (design system used) begins here.
**No design system?** Use a starter system supplied by the instructor or an open design system, with a short note on what was borrowed.

### Lesson 7 — Refine and check your design
*Slug:* `refine-and-check`
**Why:** the first version is never the one you test. This lesson extends it, checks it against the system and accessibility, and closes the Develop stage with the alignment check (the former critique-loop lesson is folded in here).
**By the end, students can:**
1. Extend the prototype to states and edge cases (empty, loading, error, success), responsive behaviour and real content, one change at a time, checking changed files and keeping a saved state each time.
2. Run an AI first-pass check against the design system (tokens, components, spacing) and against the accessibility rules (contrast, labels, focus, tap targets), confirming each finding themselves. An AI check is a first pass, not an audit.
3. Fill the hub with design decisions and let its alignment table show decisions with no user need behind them and opportunities no decision serves.
4. Run the principle audit: the AI argues where each decision breaks a principle (Nielsen's 10 plus any organisation principles); decide for each finding to fix, accept as a recorded trade-off, or cut.
5. Run a light alignment check at the end of any activity.
**Key activities:** Refine loop (Generate pattern) *(to draw)*, then the **Alignment check** flow ✅ drafted in `03-quality-and-measurement.md` Part 1 *(to draw)* as a closing block of about 30 minutes. *(Assumed split for 90 minutes: states and content 30, system and accessibility check 20, alignment check on the top three decisions 25, buffer 15. Untested.)*
**Output:** a refined prototype, the alignment table and principle audit in the hub, the decision log updated. Gate checks 3d, 3b, 3c.

### Lesson 8 — Test with real users
*Slug:* `test-with-real-users`
**By the end, students can:**
1. Use AI to prepare a test plan and script from their hypotheses, and explain why AI-simulated users cannot replace real ones.
2. Run a usability test and measure task success, time on task, errors and SUS against a baseline.
3. Verify AI-assisted analysis of findings against raw recordings or notes, and weigh findings by importance rather than frequency.
**Key activity:** Plan-and-read-the-measurement flow (Investigate pattern), pre-launch scope *(to draw)*. **Live in a 90-minute session:** plan and script the test, then peer usability tests in pairs (students test each other's prototypes under the confidentiality ground rules; sanitise if needed). Outside tests are optional homework.
**Output:** findings, updated decision log, updated prototype.

### Lesson 9 — Hand off and measure success
*Slug:* `hand-off-and-measure`
**By the end, students can:**
1. Produce a handoff pack in which the prototype is the reference and the decision log explains the choices, so a developer can build without asking.
2. Write a measurement plan for after launch (what to track, where, when to review) and hand it to the PO, even if they cannot access the data themselves.
3. Describe their own AI workflow results (time per step, error rate, rework) with counts, not impressions.
**Key activity:** Handoff flow *(to draw)*.
**Output:** handoff pack and measurement plan.

### Lesson 10 — Capstone: present your case
*Slug:* `capstone`
**By the end, students can:**
1. Run the full chain on a real case, each step's output feeding the next, with every gate recorded in the hub.
2. Present the case showing evidence, decisions and trade-offs, so an employer or PO sees the judgement, not just the speed.
3. State which parts of the workflow they would keep, tune, or skip, with reasons from their own measured results.
4. Finish the **Experience Hub**: every output from the case on one connected site, with the cross-links working, so a reader can start from any decision and reach its opportunity, hypothesis, principle, test and metric.
**Output:** the finished Experience Hub (the final report), the complete case folder, and a portfolio piece.

---

### Open items for discussion
1. ~~Length and format~~ **Decided 2026-10-05:** one online 90-minute session a week, 10 weeks, 7 to 8 students, up to 60 minutes of homework (see Class format and timeline). Open: whether to add a catch-up week.
2. ~~Edit the existing lesson now?~~ **Done 2026-10-05.** Remaining: build the new deck from the 35-slide outline. Cleaned up 2026-10-05: the identical duplicate of the old deck was removed (one copy stays in `slides/_archive/`); the old brainstorm file is in `materials/_archive/`; the standalone competitor template is in `learning/_archive/templates/`.
3. ~~Hosting choice~~ **Decided:** students host their own hubs on GitHub Pages (homework after Lesson 1); Winnie does not host. Open: what do you do for students who get stuck on the homework (a help slot at the start of the next lesson), and what is the answer for a student who refuses any account?
3b. **Lesson 1 carries a lot.** If it overruns, move "context reuse" or the CARE mapping to Lesson 2, where students first use it for real.
4. **Overlap with Library Discover lessons:** Lesson 3 should point to them for method and teach only the AI-assisted layer.
5. ~~Case~~ **Decided 2026-10-05:** the student's own case by default; the course case card and the stand-in PO are fallbacks. Open: who writes the case packs for students without PO access, and whether to write a second course case.
6. **Flows still to draw:** (drawn: competitor analysis, user-voice synthesis) shape the brief, problem brief, ideation/flow, prototype build, alignment check, plan-and-read-measurement, handoff.

