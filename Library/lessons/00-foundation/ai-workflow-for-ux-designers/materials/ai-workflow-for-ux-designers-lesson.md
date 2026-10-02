---
title: "Set Up Your AI Workflow"
subtitle: "How to think about, choose, and use AI across the design process — not just for prototyping"
type: lesson
program: ux-class
tags: [ai, workflow, mindset, design-thinking, prompting, tools, foundational]
level: foundational
date: 2026-07-20
draft: true
slides: ""
previous-session: "Design Thinking for UX Designer"
next-session: "Customer Understanding"
---

## Overview

In the previous session, students learned the Design Thinking cycle — Empathise, Define, Ideate, Prototype, Test — as the framework for the whole program. This session answers a different question: *how does AI fit into that framework, deliberately, rather than accidentally?*

Most designers are already using AI somehow. 91% of designers used AI in 2026, and the average designer now reaches for 7 different AI tools regularly. But usage isn't the same as a workflow. Most designers picked up AI tool by tool, task by task, with no underlying framework for when to trust it, when to double-check it, or how to prompt it well. This session builds that framework — before students touch AI seriously in Customer Understanding, Synthesis, Design Framework, or the AI Prototype Development sessions later in the program.

**The core distinction this lesson teaches: AI-assisted vs. AI-generated.** AI-generated means AI made the decision. AI-assisted means the designer made the decision and AI did the assembly. Every activity in this session — and every AI-related activity in every session after this one — depends on students understanding that difference and choosing AI-assisted on purpose.

This is also the session where students who have never opened a text editor learn just enough technical vocabulary — Markdown, HTML, local folders — to not feel lost the moment an AI tool mentions a `.md` file or a "browser-viewable prototype." That's not a side note. It's a prerequisite for every AI-heavy session that follows, especially AI Prototype Development.

> **Why this session exists, and where it sits:** Design Thinking gave students the *what* — the 5-stage cycle. This session gives them the *how* — a deliberate, reviewable way of bringing AI into every stage of that cycle. Students carry this mindset and toolkit forward into every subsequent session, particularly the AI Prototype Development session, which assumes this vocabulary and this level of critical engagement with AI output.

---

## Learning Objectives

By the end of this session, students will be able to:

1. **Explain** the benefits and risks of a deliberate AI workflow, using real 2026 industry data, not just intuition
2. **Describe** how the UX Product Designer role shifts when AI is part of the workflow — from maker to strategist/editor
3. **Apply** the CARE prompting framework (Context, Ask, Rules, Examples) to write a structured AI prompt
4. **Distinguish** AI-assisted from AI-generated work, and default to AI-assisted by design
5. **Reuse** saved artifacts — past synthesis, problem statements, prototype patterns — as Context for new prompts, instead of re-describing a project from memory each time
6. **Map** AI's role across each of the 5 Design Thinking stages — where it helps most, where it's riskiest, and what artifact each stage hands forward
7. **Recognise** basic technical vocabulary — Markdown (`.md`), HTML, local folder structure — well enough to work with AI tools without feeling lost
8. **Set up** a personal AI tool stack and a clean local project folder, organised to hold artifacts you'll reuse across the whole design process

---

## Materials Needed

- Access to an AI chat tool (ChatGPT, Gemini, Claude, or any tool students are comfortable with)
- Students' Design Thinking artefacts from the previous session (problem statement draft, or any real project in progress)
- A laptop with a file explorer/Finder open (for the local folder activity)
- Prompt library handout (see below)
- Technical literacy self-check handout (see Pre-Class Preparation)

---

## Pre-Class Preparation

**For students:**

1. **Bring one AI tool you already use** — even informally (ChatGPT for random questions counts). We'll audit it together, not judge it.
2. **Self-check your technical literacy.** Answer honestly — no wrong answers, this just tells us where to spend time in Phase 2:

   | Concept | Can you explain it to a teammate? |
   |---|---|
   | What a `.md` (Markdown) file is | ☐ Yes ☐ Not sure |
   | What HTML is and why a browser needs it | ☐ Yes ☐ Not sure |
   | What a "local folder" is, and why it's different from a Google Drive or Figma file | ☐ Yes ☐ Not sure |

   If you checked "Not sure" on any of these, don't worry — Phase 2 is built for you, and nobody will be quizzed cold.
3. **Optional read:** NN/G's [AI for UX: Getting Started](https://www.nngroup.com/articles/ai-ux-getting-started/) — 5 minutes, sets the tone for today.

**For the instructor:**
- Prepare a live example of a "bad" vague prompt vs. a CARE-structured prompt on the same task, to demo the difference live in Phase 3.
- Have your own local project folder open and ready to screen-share for the Phase 2 folder-setup demo.
- Review the Connection to Curriculum table at the end of this file — this session's Phase 4 stage-mapping activity should reference the same 5-stage vocabulary from `design-thinking-lesson.md` exactly, not a paraphrase.

---

## Session Structure

| Phase | Activity |
|---|---|
| 1 | Mindset reframe — benefits, impact, and why a deliberate workflow beats ad hoc tool use |
| 2 | Technical literacy primer — Markdown, HTML, local folders |
| 3 | The AI workflow toolkit — CARE prompting + AI-assisted vs. AI-generated |
| 4 | Mapping AI across the 5 Design Thinking stages |
| 5 | Build your workflow (hands-on) + share & reflect |

---

### Phase 1 — Mindset Reframe

**Open with the data, not the hype.** Show two numbers side by side: 91% of designers used AI in 2026, and 7 tools per designer on average. Then show the split finding from Figma's 2026 report: 36% of designers said design got *better* with AI, 35% said *worse*, 29% said no change. Ask the class: why would the same tools produce such different outcomes for different people?

**Land the answer:** the difference isn't the tool. It's whether the designer has a deliberate workflow — a way of deciding when to use AI, how to prompt it, and how to review its output — or whether they're using AI accidentally, tool by tool, task by task, with no underlying framework.

**Benefits, stated plainly:**
- Research synthesis that took days now takes hours — AI is strongest at *planning and analysis*, not at replacing the research itself.
- Junior designers benefit disproportionately — AI narrows the execution gap between junior and senior, even as it widens the judgment gap. That's worth naming directly for a room with mixed experience levels.
- McKinsey's 2025 State of AI findings: organisations that integrated AI into product design workflows saw 22% higher feature adoption. Figma 2026: 91% of designers who increased AI use said it improved their design quality; 89% said they worked faster.

**The role shift, stated plainly:**
- The designer's job is moving from *maker* to *strategist and editor*. NN/G puts it directly: "your hands still direct the work" — AI is a set of gloves, not a replacement hand.
- The most valuable profile emerging in 2026 is the "AI-UX Generalist": strong human-centred thinking, data literacy, and strategic vision, who uses AI to automate the grunt work rather than specialising narrowly in one execution skill.
- Half of designers surveyed in 2026 have shipped AI-generated code to production. The line between design and implementation is blurring — directly relevant to the AI Prototype Development session later in this program.

**Mindset framings to land here — pick 2–3, don't try to cover all of them:**
- **"Augment, don't replace."** The dominant framing across the industry: AI takes the tedious and repetitive; the designer keeps authorship, judgment, and ethics.
- **AI as intern, not oracle.** NN/G's "Meet Ari" framing: a talented intern who works fast, never tires, but still needs supervision and correction. This reframes "AI got it wrong" as an expected part of the workflow, not a failure.
- **This is a hype cycle — know that going in.** NN/G draws a direct parallel to the VR hype cycle: early over-promise, a trough of disillusionment, then durable practical use. Naming this explicitly helps students calibrate expectations rather than treating every new tool as either magic or a threat.
- **Bias and ethics aren't a footnote.** Training data skews Western/English. For a program serving Vietnamese/SEA designers, this deserves airtime here, not just a caveat — the same point already made in the Design Framework session about AI-suggested component hierarchies.

**Discussion prompt (neighbour exercise):** "Turn to the person next to you: think of one time AI genuinely helped your work, and one time it quietly made your work worse without you noticing right away. What was different about those two moments?" Collect 2–3 answers. Common pattern: the "helped" moments involved a clear ask and a review step; the "worse" moments involved trusting output without checking it.

---

### Phase 2 — Technical Literacy Primer

Most students have never needed to open a text editor — Figma abstracted all of that away. But AI workflows constantly surface three concepts, and nobody usually stops to explain them. Teach this as a fast, plain-language primer — not a coding lesson.

**What is a `.md` file (Markdown)? Why do we need it?**

Markdown is a plain-text way of writing formatted documents — headings, bold, bullet lists, tables, links — without a word processor. Type `**bold**` instead of clicking a Bold button. Type `## Heading` instead of choosing a style from a menu. A `.md` file is just a `.txt` file that follows these typing conventions.

Why designers need it: it's the native language of AI tools. Every prompt you structure with headers and bullets, and every reply an AI tool gives back, is Markdown under the hood. It's also what this entire program's lesson files are built from — recognising `#`, `-`, `**text**`, and `| |` tables is the whole vocabulary needed to read almost any Markdown file. Students don't need to write it by hand — they need to recognise it and know they can open a `.md` file in any text editor or paste it back into an AI chat tool.

**What is HTML? Why do we need it?**

HTML (HyperText Markup Language) is the language every web page is built from. It's structural, not a programming language — tags say what each piece of content *is*: `<button>` marks a button, `<img>` marks an image, `<h1>` marks a heading, `<div>` marks a container. A browser reads an HTML file and draws it on screen.

Why designers need it: an AI-generated prototype (covered in depth in the AI Prototype Development session) *is* an HTML file. Nesting in HTML works the same way nesting works in Atomic Design — a `<nav>` containing `<button>` tags is structurally the same idea as an Organism containing Atom instances. Naming that parallel makes HTML feel familiar rather than foreign. And basic tag vocabulary upgrades feedback quality: "the button is outside the card's container, that's why the padding looks wrong" is something both a human and an AI tool can act on; "this looks off" isn't.

**How Markdown and HTML work together**

These two aren't unrelated trivia — they're two ends of the same pipeline, and designers use it constantly outside of prototyping too. Take synthesis: paste 8 interview transcripts into an AI chat tool and ask it to find themes. What comes back — headings per theme, bullet lists of supporting quotes, bold insight statements — is Markdown. That's your working document: plain text, easy to correct, easy to paste into your next prompt as Context.

Now say that synthesis needs to become something you actually show stakeholders — a research report with a header, a card per theme, maybe a chart of theme frequency. Paste the same Markdown synthesis doc back into an AI tool and ask it to turn it into an HTML report. What comes back is a real webpage: laid out, styled, ready to open in a browser or drop into a deck. Markdown was the working document. HTML is the presentation artifact.

You keep Markdown. AI builds HTML when you need something visual. That's the whole loop — raw insight in, formatted report out. It's the same loop the AI Prototype Development session uses later (component inventory → AI → running screens), just applied here to a research report instead of a screen.

**Local folder setup — why "where your files live" matters, at every stage**

A *local folder* is simply a folder on your own computer's hard drive — not a Figma file on Figma's servers, not a Google Doc in Drive. This isn't a Prototype-stage concept. From the moment you start using AI at Empathise — pasting interview notes into an AI chat tool, saving synthesis output — a clean folder is what lets you find and reuse that work later. It matters most visibly once you reach an AI coding tool (which opens a whole local folder as a project and reads everything inside it as context), but the habit should start on day one, not the day you open Cursor.

Why it matters: a messy folder produces messy output at every stage, for the same reason a messy Figma file produces a messy component inventory (a point already taught in the Design Framework session). One project = one folder — never scattered across Desktop, Downloads, and Drive. Cloud-sync folders (Google Drive, Dropbox) can behave unpredictably mid-write once an AI coding tool is actively generating files — prefer a plain local folder while actively building, and copy the finished result to Drive afterward.

**There's no single correct way to organise that folder — pick whichever option fits how you think:**

*Option A — By design process stage* (mirrors the 5-stage cycle):
```
my-project/
  01-empathise/   research notes, interview transcripts, AI synthesis output
  02-define/      problem statements, JTBD notes, HMWs
  03-ideate/      concept sketches, AI-generated idea lists
  04-prototype/   design tokens, component inventory, generated screens
  05-test/        test scripts, session notes, findings
```
Best for solo projects where you want the folder to mirror your process — fast to answer "what did I do at Define?" Numbering the folders (`01-`, `02-`...) keeps them sorted in stage order in Finder/Explorer.

*Option B — By file type:*
```
my-project/
  notes/     research notes, meeting notes, AI chat exports
  assets/    images, icons, exported design files
  prompts/   saved CARE prompts you reuse
  exports/   finished deliverables — prototypes, reports, decks
```
Best for grabbing "all my notes" or "all my exports" regardless of which stage produced them. This is also the structure AI coding tools expect most naturally once you reach Prototype.

*Option C — By deliverable:*
```
my-project/
  research/
  design-system/
  prototype/
  presentation/
```
Best for team projects, or when what matters is the output, not your stage-by-stage history — easier for a teammate or stakeholder to find "the prototype" without knowing how you got there.

Many students start with Option B for their first project or two — it's the simplest — then move to Option A once they feel the friction of hunting through mixed content by stage. There's no wrong choice here; the only real mistake is no structure at all.

**Quick pulse-check before moving on:** ask the room to raise a hand for whichever of the three concepts they'd still hesitate to explain to a teammate. Address the most-raised one for 60 seconds before continuing — don't let this phase run long; the goal is recognition, not mastery.

---

### Phase 3 — The AI Workflow Toolkit

**AI-assisted vs. AI-generated — the throughline for this entire program.**

AI-generated means AI made the decision. AI-assisted means the designer made the decision and AI did the assembly. This single distinction is why the AI Prototype Development session insists students define a "prototype pattern" before touching a build prompt — the pattern is what keeps AI in the assistant role instead of the decision-maker role. Land this now, explicitly, so every later session can reference it instead of re-teaching it.

**A prompting framework, taught explicitly: CARE**

Rather than leaving prompting to intuition, teach NN/G's CARE structure — a simple frame students can reuse in every stage and every future session:

| Letter | Meaning | Example |
|---|---|---|
| **C** — Context | What's the situation? Who's involved? What already exists? | "I'm designing a checkout flow for a Vietnamese food delivery app." |
| **A** — Ask | What specifically do you want? | "Generate 3 alternative empty-cart states." |
| **R** — Rules | Constraints, tone, format, what to avoid | "Keep copy under 8 words. No exclamation marks. Match a calm, trustworthy tone." |
| **E** — Examples | Show, don't just tell | "Here's an example of the tone I mean: [paste]." |

**Live demo:** show a vague prompt ("make this better") next to the same request rebuilt with CARE. Let students see the output difference live, not just hear about it.

**Feed forward: prefer past work over starting fresh**

There's a habit worth building into CARE's "Context" step specifically: **default to reusing an artifact you already have, not re-describing your project from memory.** A new AI conversation defaults to a blank slate — it knows nothing about your project until you tell it. Most students' instinct is to retype a summary of their project every time, from memory, slightly differently each time. That's slow, and it's also where inconsistency creeps in — this week's synthesis subtly contradicts last week's because you described the research differently in the retelling.

The fix: your local folder (Phase 2) isn't just a place to dump files — it's your artifact library. Every stage produces something worth saving: an Empathise-stage synthesis doc, a Define-stage problem statement, a Prototype-stage component inventory. When you sit down for a new AI task, the first question isn't "how do I explain my project," it's "which saved artifact already answers this." Paste or attach that file as your Context, instead of authoring a fresh description.

This is the same principle the AI Prototype Development session teaches under a different name: the "prototype pattern" works precisely because it's a saved artifact fed into every build prompt, rather than re-explained screen by screen. What's new here is naming it as a general habit that applies to *every* stage, not just Prototype — this is sometimes called "context engineering" in 2026 AI practice: treating context as something you deliberately assemble and carry forward, not something you retype under pressure each session. Multi-step AI work compounds this further — each step's output becomes the next step's input, so a sloppy artifact at Empathise degrades everything built on top of it at Define and beyond.

**Two ways this shows up in practice:**
- **Reference a saved file directly.** "Context: here's my Empathise-stage synthesis doc: [paste from `01-empathise/synthesis.md`]." Faster and more accurate than reconstructing it from memory, and it's exactly why Phase 2's folder habit matters beyond just tidiness.
- **Use your AI tool's persistent project/memory feature, if it has one.** Many AI chat tools now let you set up a project once — upload your synthesis docs, personas, and problem statement — so every new conversation inside that project already has the context, instead of you re-attaching files each time. Worth demoing live if your AI tool supports it.

**Rule of thumb to give students:** if the context you're about to type already exists somewhere in your folder, stop typing and go find the file. Retyping from memory is where drift enters your workflow — same failure mode as the "component drift" problem taught in the Design Framework session, just at the level of ideas instead of UI components.

**A quick vocabulary check on what AI tools are actually for**, without naming specific brand names in the takeaway (per program convention — refer to "AI chat tool" / "AI coding tool" in all student-facing material):

- **AI chat tools** — research synthesis, ideation, writing, strategy conversations
- **AI coding tools** — turning a defined pattern into working code (covered fully in AI Prototype Development)
- **In-tool AI features** — layer renaming, component detection, auto-suggestions inside the design tool itself

**Instructor note:** resist tool-collecting. Most experienced designers in 2026 lean on 2–3 general-purpose AI chat tools for almost everything, and reach for a specialised tool only when the task demands it (prototyping/code). Teach depth with one tool before breadth across many.

---

### Phase 4 — Where AI Fits in Your Design Process

Reframe this away from "AI, in general" and toward what a product/UX/UI designer actually spends their week doing. Almost every real AI use case a designer has falls into one of four buckets: **synthesising research, setting up the process map, prototyping, and everything else** — critique prep, stakeholder comms, QA, accessibility, competitive analysis. This section walks through each bucket with real design artifacts and examples, then ties them back to the 5-stage vocabulary from Design Thinking so nothing here feels like a new framework — just a closer look at four things you already do.

**Key teaching point:** AI's usefulness is not evenly distributed across these buckets. It's strongest at Synthesis and Prototyping — both are fundamentally pattern-matching and generation tasks. It's weakest at the judgment calls inside Process Mapping and the "Other" bucket — deciding which insight is real, which flow is right, what's actually on-brand. Naming this unevenness up front stops students from trying to force AI equally into everything.

**Second teaching point — this is where "feed forward" from Phase 3 becomes concrete:** each bucket below produces an artifact worth saving into your local folder. That artifact isn't just a record of what you did — it's the Context you paste into your next prompt, instead of re-describing your project from memory. The chain of artifacts *is* the workflow: synthesis doc → process map → prototype pattern → test synthesis.

---

#### 1. Synthesising Research (maps to Empathise, sometimes Test)

Every designer produces piles of raw research and not enough time to make sense of it: interview transcripts, survey exports, support tickets, usability session notes, competitor screenshots. AI's best use here isn't replacing the research — it's compressing the distance between raw notes and a synthesis artifact you can actually design from.

- **Interview → themes.** Paste transcripts, get thematic clusters with supporting quotes — a faster first pass at what you'd otherwise do by hand with sticky notes in an affinity map.
- **Empathy Map drafting.** Turn interview notes into a first-draft Say / Think / Do / Feel map — the same Synthesis Activity from Design Thinking, just faster to get to a v1 you then correct.
- **Assumption audit.** Paste your team's stated assumptions, ask AI to sort them into Known / Unknown and flag which have zero supporting evidence.
- **Competitive teardown.** Paste screenshots or descriptions of 3 competitor flows, ask for a structured comparison table (pattern used, strength, weakness) instead of building it cell by cell.

Prompt (CARE): *Context* — "Here are my raw interview transcripts from 8 sessions on [topic]: [paste]." *Ask* — "Draft an Empathy Map (Say/Think/Do/Feel) and identify 4–6 recurring themes with 2 supporting quotes each." *Rules* — "Separate observation from inference. Flag anything based on a single participant." *Examples* — "Match this format: [paste your research repo template]."

Stays yours: which themes are actually load-bearing for the decision ahead, and whether a quote is being used out of context. AI-simulated "synthetic users" can supplement, never replace, real research — AI doesn't control your customer's purse strings; they do.

Artifact to save: the synthesis doc — Empathy Map + theme list + Assumption Map. This becomes your Context for the process map next.

---

#### 2. Setting Up Your Process Map (maps to Define → Ideate — the "Organise for users" step)

This is the bucket that gets skipped most often under time pressure, and it's where AI genuinely closes a gap: turning synthesised research into the maps and flows that make a problem visible — journey maps, sitemaps, task flows, service blueprints.

- **Current-state journey map.** From your synthesis doc, draft a first-pass journey — stage → user action → thought/feeling → pain point. Same Define-stage output you already know, faster to a correctable v1.
- **Evidence-based sitemap.** From research + competitive audit, draft an information architecture that traces back to evidence instead of guesswork.
- **Task flow drafting.** Describe the feature in a sentence, get a first-pass task flow (entry point → steps → decision points → exit) to correct against your own judgment of the real flow.
- **Service blueprint.** For anything with a "backstage" (support, fulfilment, onboarding with a human in the loop), draft frontstage/backstage swimlanes from a raw process description.
- **HMW generation.** Convert insight statements into How Might We questions, scored for scope — not too broad, not already a solution. Same Define-stage activity, sped up.

Prompt: *"Here is my research synthesis: [paste]. Draft a current-state journey map with 5–7 stages. For each stage: user action, thought/feeling, pain point, and which research insight supports it. Flag any stage where you're guessing rather than working from the research."*

Stays yours: the sequencing and priority calls, and deciding what's genuinely a distinct stage versus a micro-step AI padded the map with to look thorough. Validate the map against real users before treating it as ground truth — a journey map is a hypothesis document until it's been checked.

Artifact to save: the journey map / sitemap / task flow, plus your chosen problem statement. This becomes your Context heading into Prototype.

---

#### 3. Prototyping (maps to Prototype)

This program has a full dedicated session on this — AI Prototype Development — so treat what's here as a preview, not the full teaching. The heavyweight version (component inventory + interaction pattern → AI generates working screens) lives there. The everyday, lighter-weight uses show up constantly before that session even starts:

- Generating the component states you forgot to design (empty, loading, error, success) from a description of the default state.
- Drafting realistic placeholder content (real-sounding names, prices, dates) instead of lorem ipsum, so a prototype survives a stakeholder actually reading it.
- Building a rough clickable flow fast enough to test navigation with 5 users before investing in high-fidelity Figma.
- Generating 3 layout variations of a screen to react against, rather than starting from a blank frame.

Prompt: *"I have this component inventory: [paste or describe]. Generate the missing states for [component] — I only have 'default,' I need hover, loading, error, and empty."*

Stays yours: spacing, grouping, and hierarchy judgment. AI "follows general directions but lacks the sophistication to weigh design tradeoffs" — treat the first output as a starting point, not a result.

Artifact to save: the prototype pattern and the running prototype. This becomes your Context at Test.

---

#### 4. Other Designer Activities (cross-cutting — doesn't map to one stage)

The work that doesn't fit neatly into a single Design Thinking stage but eats real time every week:

- **Critique prep** — "Here's my screen: [describe/paste]. Playing devil's advocate, what would a tough design critique flag about hierarchy, accessibility, and consistency with our design system?" Arrive at critique with your own blind spots already found.
- **Stakeholder communication** — turn a messy set of design decisions and trade-offs into a clear one-pager or slide narrative. The translation work between "what I decided" and "why a non-designer should care."
- **Usability test synthesis** — turn raw session notes into a findings doc with severity ratings. The same Test-stage activity from Design Thinking, faster.
- **Design QA** — check a set of screens against your design tokens/component library for consistency before handoff. Catch the hardcoded colour or off-brand spacing before a developer does.
- **Accessibility first pass** — "Check this component list against WCAG AA — flag likely contrast, tap-target, and labelling issues." A first pass before a real accessibility audit, not a replacement for one.
- **UX writing** — drafting and refining button labels, error messages, empty states, and tooltips in the product's voice, then editing hard — AI copy defaults to generic SaaS tone unless corrected.

Stays yours: every one of these is a first draft, not a final artifact. The pattern from every bucket repeats here — AI produces a fast, reviewable draft; you decide what's true, what's on-brand, and what ships.

---

**Quick reference — how the four buckets map onto the 5 stages you already know:**

| Bucket | Design Thinking stage(s) | AI does well | Stays yours |
|---|---|---|---|
| Synthesising Research | Empathise (some Test) | Clustering, theme-finding | Which theme is load-bearing |
| Process Mapping | Define → Ideate | Drafting a first-pass map | Sequencing, priority calls |
| Prototyping | Prototype | Assembling from a pattern | Spacing, grouping, hierarchy |
| Other Activities | Cross-cutting | Fast first drafts | What's true, what's on-brand |

**Convergence point:** by the end of Phase 4, every student can name, for their own real project, one AI use case in each of the four buckets — and can point to where the resulting artifact will live in their local folder. If a bucket comes up blank, that's useful information, not a failure — not every project touches all four in a given week.

---

### Phase 5 — Build Your Workflow (Hands-On) + Share & Reflect

**Step 1 — Set up your local folder (5 min)**
Using the Phase 2 vocabulary, create one dedicated project folder on your own machine for this program's work. Pick one of the three organisation options from Phase 2 (by stage, by file type, or by deliverable) and build out the subfolders now. This becomes the folder you use across every stage from here forward — not just the one AI coding tools open later.

**Step 2 — Pick your primary AI chat tool (2 min)**
From the tool you brought in Pre-Class Preparation, or a new one — pick one you'll use as your default for the rest of the program. Depth beats breadth.

**Step 3 — Write one CARE prompt for your real project (8 min)**
Using your Phase 4 stage-mapping, pick the stage you're currently working on in your real project. If you already have a saved artifact from an earlier stage (even a rough one), use it as your Context — don't retype a project summary from memory. Write a full CARE-structured prompt for one task in that stage. Run it. Read the output critically — does it hold up, or does it need correction? Save the result into your local folder before you move on, so it's ready to feed forward next time.

**Step 4 — Share & reflect (5 min)**
Ask 2–3 students to share:
- Which stage did you pick, and what did AI actually give you?
- Where did you have to correct or push back on the output?
- What's one thing you'll do differently now that you have a CARE structure, versus how you prompted before today?

**Closing thought for the instructor to land:**

> Every session from here forward will ask you to use AI for something — research synthesis, problem framing, prototyping. None of those sessions will re-teach what "AI-assisted" means, or how to write a good prompt, or what a `.md` file is. That's what today was for. The tool will keep changing. This workflow — define clearly, prompt deliberately, review critically — doesn't.

---

## Activities

Full instructions for the two in-class activities. Use the Session Structure table for timing and facilitation context — these are the facilitator-ready versions of Phase 4's convergence point and Phase 5's hands-on build.

---

### 🗺️ Activity 1 — Stage Mapping + Artifact Canvas
**Type:** In-class · Worksheet or FigJam
**Time:** 15 min
**Format:** Solo (own real project, or the shared practice project if a student doesn't have one yet)

**What it is:**
Students work through the 5-stage vocabulary from the Design Thinking session and, for each stage, name what AI will help with, what stays their responsibility, and which artifact that stage produces to feed forward into the next. The output is a completed canvas students keep and refer back to for the rest of the program.

**Setup (before class):**
- Prepare a 5-column canvas — physical handout, FigJam board, or shared doc — with columns: Empathise · Define · Ideate · Prototype · Test
- Each column has 3 rows to fill: "AI helps with," "Stays mine," "Artifact to save"
- Have the Phase 4 stage-by-stage breakdown (Core Content) visible or handed out as reference — students are applying it, not deriving it from scratch

**Instructions for students:**

1. **(10 min)** For each of the 5 stages, fill in your canvas: what will AI help you with here, what stays your responsibility, and what artifact will this stage produce that you'll carry into the next one.
2. **(5 min) — Share.** 2–3 students read out one stage from their canvas. Winnie listens for: is the "stays mine" column genuinely a judgment call, or did they just restate the "AI helps with" column in different words?

**Facilitator watch-fors:**
- Students who leave "Artifact to save" blank or vague ("notes") — push for a specific, nameable file: "what would you actually call this file?"
- Students who can't distinguish "AI helps with" from "stays mine" at Define or Test — these are the judgment-heavy stages; if they're stuck, ask "what would you have to personally verify before you'd trust this?"
- Students without a current real project should use the shared practice project rather than skip the activity — the canvas habit matters more than the specific content

**For private mentees (Anh / Vy):**
This canvas becomes their working reference for the rest of the program — every future session's AI activity should trace back to a row on this canvas. Keep it alongside their project files, not just in the shared class board.

---

### 🔧 Activity 2 — Build Your Workflow
**Type:** In-class · Hands-on, own laptop
**Time:** 15 min
**Format:** Solo

**What it is:**
Students set up the actual infrastructure this session has been building toward: a local folder, a primary AI tool, and one real CARE-structured prompt run against their own project — using their Activity 1 canvas as the map for what to prompt and which artifact to reuse as Context.

**Setup (before class):**
- Students should have their laptop with a file explorer/Finder open and access to an AI chat tool
- Have your own local project folder open and ready to screen-share as a live example

**Instructions for students:**

1. **(5 min) — Set up your local folder.** Create one dedicated project folder on your machine. Pick one of the three organisation options from Phase 2 (by stage, by file type, or by deliverable) and build out the subfolders now. This is the folder you'll use across every stage from here forward.
2. **(2 min) — Pick your primary AI chat tool.** From what you brought in Pre-Class Preparation, or a new one — pick one default for the rest of the program. Depth beats breadth.
3. **(8 min) — Write and run one CARE prompt.** Using your Activity 1 canvas, pick the stage you're currently working on. If you already have a saved artifact from an earlier stage (even a rough one), use it as your Context — don't retype a project summary from memory. Write a full CARE-structured prompt, run it, and read the output critically. Save the result into your folder before moving on.

**Facilitator watch-fors:**
- Circulate during Step 1 and check students are actually building subfolders, not just creating one empty folder and moving on
- Key coaching question during Step 3: "What would you correct before you'd actually use this output?" — if a student runs their prompt and moves on without answering that, stop them
- If a student has no prior artifact to feed forward, that's fine — have them note what artifact *this* prompt will produce, so next session they have something to reuse

**For private mentees (Anh / Vy):**
Use their actual current project. The folder and prompt library they start here should become the one they use for the rest of the program — not a throwaway practice exercise.

---

## AI in Practice

### 🤖 Try this prompt

> *"I'm a UX designer working on [describe your project in 1–2 sentences]. I'm currently at the [Empathise/Define/Ideate/Prototype/Test] stage. Using the CARE framework, help me write a well-structured prompt for [the specific task]. Then critique your own prompt: what's still ambiguous, and what should I add?"*

### 🧠 Critical thinking prompt

After running the prompt above, discuss as a class:
- Did the AI's self-critique catch something you missed?
- Where did the AI's suggested prompt still leave room for AI to make a decision that should have stayed yours?
- If you ran this same prompt with less context, how much worse would the output likely be?

### ✍️ Prompt engineering tip

Specificity in the Context section does more work than any other part of CARE. "A checkout flow" gets a generic answer. "A checkout flow for a Vietnamese food delivery app, used mostly on Android, for time-pressed parents ordering dinner after work" gets an answer shaped to the actual problem.

### ⚖️ Ethics consideration

AI tools reflect the design patterns of their training data, which skews heavily Western/English-language. When using AI for research synthesis, ideation, or prototyping for a Vietnamese or Southeast Asian product, stay critical about whether AI's suggestions actually match your users' mental models — not just whether the output looks polished.

---

## Assessment

### Quick knowledge check

Run verbally or in a shared doc at the close of Phase 3 (2–3 min):

1. What's the difference between "AI-assisted" and "AI-generated"? Give an example of each from your own recent AI use.
2. Name the four parts of the CARE prompting framework.
3. At which Design Thinking stage is AI riskiest to over-trust, and why?
4. A colleague says: "I don't need a workflow, I just ask AI for what I need." What's the gap in that thinking?
5. A colleague opens a new AI chat and retypes a summary of their project from memory every time. What would you tell them to do differently, and why?

---

## Homework

### Assignment 1 — Set Up Your AI Workflow
**Due:** Before next session
**Time estimate:** 20 min
**Type:** Setup

If you completed Activity 2 in class, this assignment is mostly about finishing and documenting it properly — not starting from zero.

- Local project folder created, organised using one of the three options from Phase 2 (by stage, by file type, or by deliverable)
- Primary AI chat tool chosen as your default for the rest of the program
- A personal prompt library file started, containing at least 3 CARE-structured prompts (Context, Ask, Rules, Examples) you expect to reuse across upcoming sessions

Submit: a screenshot or link to your folder structure + your prompt library file, shared in the class channel (group) or with Winnie directly (private mentees)

**What Winnie is looking for:**
- Is the folder actually organised — clear subfolders, not just one empty folder created and left?
- Do the saved prompts include all four CARE parts, or just a one-line Ask dressed up as a prompt?
- Does the chosen organisation option make sense for how this student actually works?

---

### Assignment 2 — Capture & Organise Your Current Screens
**Due:** Before next session
**Time estimate:** 30 min
**Type:** Capture · Organisation

This is what Customer Understanding needs from you on day one — the friction analysis activity in that session runs directly on the screen flows you capture here. Put them straight into the folder you set up in Assignment 1, not somewhere you'll have to hunt for later.

- For each main experience in your project, capture the current screen flow as it exists today
- Identify the key experiences to map (e.g. Onboarding, Core Task, Checkout, Settings)
- Screenshot each screen in the flow — aim for a high-level overview, not every micro-state
- Save the screenshots into your local folder from Assignment 1, and label each one with its state
- Optional: paste the flow into your AI chat tool and ask it to draft a one-line description per screen — a fast way to check your labelling is clear before Customer Understanding, using the CARE structure from today
- We will use these flows in the next session to set up friction metrics for each step

Submit: your organised screen flow (folder link or exported images), shared in the class channel (group) or with Winnie directly (private mentees)

**What Winnie is looking for:**
- Are the screens actually inside the Assignment 1 folder, not scattered across Desktop or a random export — this is the folder habit from today, applied for real
- Is each screen labelled with its state, not just a bare filename
- Coverage of the flow at a high level — this doesn't need to be exhaustive, it needs to be usable in next session's friction analysis

---

## Prompt Library Reference

| Goal | Prompt |
|---|---|
| Structure any request (CARE) | "Context: [situation]. Ask: [specific request]. Rules: [constraints/format]. Examples: [reference]." |
| **Synthesising Research** — interview themes | "Here are my raw interview transcripts: [paste]. My research goal is [X]. Draft an Empathy Map and identify recurring themes, contradictions, and 3 quotes per theme." |
| **Synthesising Research** — assumption audit | "Here are our team's stated assumptions: [paste]. Sort into Known vs. Unknown and flag which have zero supporting evidence." |
| **Process Mapping** — journey map | "Here is my research synthesis: [paste]. Draft a current-state journey map with 5–7 stages — action, thought/feeling, pain point, supporting insight per stage. Flag any stage where you're guessing." |
| **Process Mapping** — HMW generation | "Here are my insight statements: [paste]. Draft 5 How Might We questions at different levels of scope. Flag any that are already a solution in disguise." |
| **Prototyping** — missing states | "I have this component inventory: [paste or describe]. Generate the missing states for [component] — I only have 'default,' I need hover, loading, error, and empty." |
| **Other Activities** — critique prep | "Here's my screen: [describe/paste]. Playing devil's advocate, what would a tough design critique flag about hierarchy, accessibility, and consistency with our design system?" |
| **Other Activities** — usability test synthesis | "Here are notes from [N] usability sessions: [paste]. What patterns appeared across multiple users vs. just one? Rate severity. What contradicts our problem statement?" |
| Audit your own prompt | "Critique this prompt I'm about to use: [paste]. What's ambiguous? What decision am I accidentally handing to you that should stay mine?" |
| Feed forward instead of starting fresh | "Context: here's my [previous stage] artifact: [paste saved file]. Don't ask me to re-describe the project — everything you need is in that file. Ask: [your task for this stage]." |

---

## Instructor Notes

**Handling mixed AI fluency in the room:**
Some students already live in AI tools daily; others have barely used them. The Phase 2 technical literacy self-check exists to surface this early without embarrassing anyone — frame it as "this tells me where to spend time," not a test. Pair confident and less-confident students for Phase 5's hands-on step.

**The most common failure mode:**
Students treat AI output as finished rather than as a first draft to review. Watch for this specifically during Phase 5, Step 3 — if a student runs their prompt and moves on without reading critically, stop and ask: "What would you correct before you'd actually use this?" That question is the whole point of the AI-assisted mindset.

**On the technical literacy primer running long:**
Phase 2 is designed to be fast — recognition, not mastery. If discussion pulls it long, cut it short and point students to Further Resources; this content resurfaces naturally (and in more depth) once they're actually building with an AI coding tool in the AI Prototype Development session.

**This session sets vocabulary every later session assumes:**
"AI-assisted vs. AI-generated," "CARE," and the three technical literacy terms should not be re-taught later — they should be referenced. If a later session's students seem to have lost this vocabulary, that's a signal to recap for 2 minutes, not to skip past confusion.

---

## Further Resources

These are resources worth pointing students to — not a complete list, but the ones that make the biggest difference for this specific lesson.

### Mindset & Data
- **[Figma — State of the Designer 2026](https://www.figma.com/reports/state-of-the-designer-2026/)** and **[Figma's 2026 AI Report](https://www.figma.com/blog/2026-ai-report/)** — the adoption and satisfaction statistics used to open Phase 1.
- **[NN/G — Using AI for UX Work: Study Guide](https://www.nngroup.com/articles/ai-work-study-guide/)** *(Oct 2025)* — the single best index for going deeper on every part of this lesson.
- **[NN/G — Your AI UX Intern: Meet Ari](https://www.nngroup.com/articles/ai-intern/)** — the intern metaphor used in Phase 1.
- **[NN/G — 7 Deadly AI Sins for UX Professionals](https://www.nngroup.com/articles/7-ai-sins/)** — a ready-made checklist for the "what stays yours" framing throughout Phase 4.
- **[NN/G — The VR Hype Cycle: Lessons for the Age of AI](https://www.nngroup.com/articles/vr-hype-cycle-lessons-for-ai/)**

### Prompting & Context Reuse
- **[NN/G — CARE: Structure for Crafting AI Prompts](https://www.nngroup.com/articles/careful-prompts/)** — the framework taught in Phase 3, in full.
- **[Sourcegraph — Context Engineering: A Practical Guide for AI Agents](https://sourcegraph.com/blog/context-engineering)** — the source for the "feed forward" framing in Phase 3: each step's output becomes the next step's context, and context quality issues cascade if you're sloppy about it. Written for engineers, but the principle transfers directly.
- **[Karo Zieminski — Context Engineering for Product Builders: The 2026 Operating Manual](https://karozieminski.substack.com/p/context-engineering-product-builders-guide-2026)** — a more product/builder-oriented take on the same idea, including the practice of maintaining a reusable library of past artifacts and prompts rather than starting fresh each time.
- **Your AI chat tool's project/memory feature, if it has one** — by 2026, most major AI chat tools offer some form of persistent, project-scoped context (upload once, referenced automatically in every new conversation within that project). Worth a 5-minute setup demo in class if your tool supports it — check its documentation, since this changes fast and features vary by tool.

### Design Thinking + AI
- **[IDEO U — The Intersection of Design Thinking and AI](https://www.ideou.com/blogs/inspiration/ai-and-design-thinking)**
- **[IDEO U — Top 22 Best AI x Design Thinking Resources](https://www.ideou.com/blogs/inspiration/best-ai-x-design-thinking-resources-books-articles-courses-more)** — includes IDEO's downloadable AI ethics card deck, usable as a follow-up in-class exercise.
- **"AI Design Workflow — 6 must-know stages"** *(LinkedIn infographic, Imen Mlika, Digital Designer)* — a visual 6-stage breakdown: AI Research Synthesis, Generative Ideation, AI Wireframing, Conversational UX, Adaptive Interfaces, Responsible AI Testing. Stages 1–3 map directly onto this lesson's Synthesising Research, Process Map, and Prototyping buckets; stages 4–6 (Conversational UX, Adaptive Interfaces, Responsible AI Testing) point past this lesson toward more advanced, product-specific AI applications — useful as an "if you want to go deeper" pointer for students, especially ahead of Test-stage and AI Prototype Development sessions.

### Stage-Specific Depth
- **[NN/G — Accelerating Research with AI](https://www.nngroup.com/articles/research-with-ai/)** (Empathise)
- **[NN/G — Synthetic Users: If, When, and How to Use AI-Generated "Research"](https://www.nngroup.com/articles/synthetic-users/)** (Empathise/Test)
- **[NN/G — AI as a Creative Teammate](https://www.nngroup.com/articles/ai-creative-teammate/)** (Ideate)
- **[NN/G — Promptframes: Evolving the Wireframe for the Age of AI](https://www.nngroup.com/articles/promptframes/)** (Prototype)

### What I'd Actually Assign
If time only allows one: **NN/G's AI Work Study Guide**, skimmed before class. It's a syllabus in disguise, and every other resource here is one click from it.

---

## Connection to Curriculum

| Session | Role in this lesson |
|---|---|
| Design Thinking | Supplies the 5-stage vocabulary this lesson maps AI onto directly |
| **This session** | Builds the mindset, prompting framework, and technical literacy every later AI-related activity assumes |
| Customer Understanding | First real application of the Empathise-stage AI prompts taught here; also depends directly on Assignment 2's captured screen flows for its friction analysis activity |
| Synthesis & Problem Definition | First real application of the Define-stage AI prompts taught here |
| Design Framework (Atomic Design) | Reinforces AI-assisted vs. AI-generated at the component-system level |
| AI Prototype Development | Assumes this session's vocabulary in full — "AI-assisted," CARE, local folder setup, and basic HTML literacy are all prerequisites, not re-taught there |
