---
title: "AI Prototype Development"
type: lesson
stage: Develop
level: "Intermediate"
duration: ""
date: 2026-09-13
tags: [prototype, AI, design-system, pattern-first, folder-structure]
draft: true
recovered: "rebuilt from the rendered lesson page of 2026-10-02 (not the original file); check formatting"
---

## Overview

Most designers who try AI prototyping start the same way: open a screen, describe it, generate it, move to the next screen. It works for the first one or two screens, then falls apart — components drift, states go missing, every new prompt starts from zero because nothing was defined ahead of time.

This lesson flips that. Before touching a single screen, the student sets up a project folder built to last, then learns to name what already exists in their design system — tokens, component inventory, template — as a **Design Pattern** the AI coding tool will eventually build from. This lesson stops at naming it well and getting the folder ready. Turning the Design Pattern into the two markdown layers AI actually reads — the **component inventory** and the **interaction pattern** — is hands-on work that starts next lesson, along with Pre-Flight cleanup and syncing design tokens.

**Scope reconciliation (2026-09-18):** this lesson used to also cover Pre-Flight cleanup, token sync, and component-inventory generation. Those moved to `lesson-2-interaction-pattern-build-editing-craft.md` to match the actual delivered deck (see `lesson-1-slide-outline.md`, which was reverse-synced from the built deck and flagged this gap) — the live session ends at the conceptual Design Pattern overview, not a hands-on build. If teaching from this file, don't build the component inventory or sync tokens today; that's next lesson's opening work.

**Known gap, not yet reconciled:** the built deck also carries three content pieces this file doesn't yet have in prose — a "Design It in Figma" 3-step process for the template ingredient, a 7-type "common template pattern types" lookup table, and a "Which Screens Are Right" scoping slide with three named traps. Flagged here rather than silently trusted, same convention as the slide outline's own mismatch notes — reconcile when next revising this file in full.

**This lesson runs on top of `03-develop/ai-prototype-development-lesson.md` ("AI Prototype Development"), not alongside it.** The AI foundations recap and the mindset reframe below are that lesson's Phase 0 and Phase 1, run as written — the method doesn't change for private-training delivery, only the pacing and the audience (1:1, not a cohort). What's actually new here — and written out in full — is the project folder setup and where the "artifacts over prompts" habit starts. See that lesson's Overview for the full pattern-first rationale if it's useful background before teaching this.

## Session Structure

**Organised Why → What → How → Do** — motivation before mechanics, mechanics before hands-on practice. Each segment below is tagged with which stage it serves.

1. **[WHY]** Mindset reframe: why screen-by-screen breaks
2. **[WHAT]** AI foundations recap
3. **[WHAT]** Your Design Pattern — naming tokens, component inventory, and template
4. **[HOW]** Organise the project folder
5. **[HOW]** Class activity (10 min): set up your project folder
6. **[DO]** Wrap-up & homework

---

## WHY — Mindset Reframe: Why Screen-by-Screen Breaks

**Run Phase 1 — Mindset Reframe from `03-develop/ai-prototype-development-lesson.md` exactly as written:** the 3-screen screen-by-screen demo (e.g. Login → Dashboard → Detail), the pattern-first alternative it lands on right after (component inventory → interaction pattern → states → screens as arrangement — now its own four slides in `lesson-1-slide-outline.md`, one per step, immediately after the drift demo), the key message that the design system is the *input* to the prototype rather than the finished output of earlier work, and the discussion prompt mapping what's missing to the two prototype-pattern layers ("what clicks lead where" → interaction pattern, Lesson 2; "what components exist and what they can look like" → component inventory, this lesson). None of it needs adapting for private-training delivery — the concept and the demo don't change with format.

**Two more problems now named explicitly, before the fix — sourced from the online course's Section 2 (`programs/online-course/AI Prototype Development/Section 2 - Thay Đổi Tư Duy Phát Triển AI Prototype/section 2-lesson.md`), not from Phase 1 of the source lesson.** Phase 1's demo only dramatises component drift. Section 2 names two more problems with the old way that Phase 1 doesn't: AI keeps no memory between prompts (every request starts from zero), and states get forgotten until a developer or the user finds the gap after launch. Both now have their own slide in `lesson-1-slide-outline.md`, right after the drift demo and before the pattern-first fix — naming all three before showing the fix makes the fix land harder.

**Why this comes first:** motivation before mechanics. The student needs to feel the drift problem before being asked to spend twenty minutes on folder structure — otherwise the folder work reads as busywork instead of the fix.

**One-on-one adjustment:** the source lesson frames the discussion prompt as a neighbour exercise for a cohort. In a 1:1 session, just ask it directly and talk it through together — there's no room to turn to.

---

## WHAT — AI Foundations Recap

**This lives in `03-develop/ai-prototype-development-lesson.md` as Phase 0** — run it exactly as written there, in its two parts: Part A (mindset — maker-to-strategist, treating AI like an intern, the VR hype-cycle expectation-setting) and Part B (working vocabulary — markdown, HTML, AI-generated vs. AI-assisted, CARE, the context habit, tool types). Source material is `ai-workflow-for-ux-designers` ("Set Up Your AI Workflow"), slides 5–20 — Phase 0 already documents which of those slides it draws on and why, so this file doesn't need to repeat that.

**Now reflected as slides, not just a pointer.** `lesson-1-slide-outline.md` carries dedicated slides for the maker-to-strategist reframe, all three Part A mindsets, the markdown/HTML/folder vocabulary, and CARE — condensed for a 1:1 session, not a 1:1 copy of all 14 source items. Left as verbal-only or folded into an existing slide, on purpose: "What a prototype actually is" (already its own WHAT slide), AI-generated vs. AI-assisted (already implied in that slide's own visual), folder organisation (covered properly in the HOW section below, no need twice), the vague-vs-CARE live demo (deferred to Lesson 2's build, per Phase 0's own suggestion, so it isn't run twice), and the AI-coding-tool-vs-chat-tool map (the student's already using one specific tool by this point — no taxonomy needed).

**Check comfort level before trimming — don't default to the coaching plan's assumption.** Part A is flagged as trimmable for students already comfortable with AI tools generally, but confirm that directly with the student first. If they're newer to this than expected, treat Part A as real onboarding, not a skip.

**Why this comes second:** now that the student wants the fix, define the vocabulary before showing them the mechanics — "component inventory," "AI-assisted," "context file" all need a shared definition before the folder setup puts them into practice.

**Run it, don't skip it — check first, don't assume:** a student may be newer to their AI coding tool than a "comes in already using it" read of the coaching plan suggests, so this isn't a formality — check their comfort with the chosen tool's basic interface (where to type, where output appears, how to accept/reject a change) before moving into the folder setup below.

---

## WHAT — Your Design Pattern

**Name the three ingredients, don't re-teach them.** Tokens, component inventory, and template are concepts the student already knows — this lesson deliberately doesn't teach design-system fundamentals (see Instructor Notes below). What's new here is naming how the three combine, for the rest of this arc: **Design Pattern** — tokens (colour, type, spacing values) + component inventory (every component, every state) + template (the skeleton layout screens are built from). All three should already exist in the student's Figma file; nothing here gets built from scratch.

**Distinguish it from "prototype pattern" immediately — the names are close on purpose, but the concepts aren't the same.** Design Pattern lives in Figma — it's what the student already has. Prototype pattern (component inventory + interaction pattern, built later this lesson and next) lives in the project folder as markdown — it's what gets built *from* the Design Pattern, for AI to read. Say the distinction out loud if the student looks confused: "Design Pattern lives in Figma. Prototype pattern lives in your project folder."

**Why this comes here:** right before the folder setup and the token-sync/component-inventory work below — this is what those steps read from. Naming it first means "sync your tokens" and "generate the component inventory" aren't abstract instructions, they're operations on something just named.

---

## WHAT — Choosing an AI Tool

**If the student hasn't already picked a tool from Lesson 0's comparison, do it now — before the folder setup below.** The choice determines how the design-token sync step later in this lesson actually works, so it can't be deferred past this point.

                                                     | Tool | Type | Design-system support | Strengths | Weaknesses | Use when |
|---|---|---|---|---|---|
| Cursor / Claude Code / Windsurf | AI coding tool | Highest — connects via Figma MCP, reads variables, tokens, components, and variants directly | Most detail on the design system via MCP | Requires manual MCP setup; no visual design UI | Already comfortable in a code editor, need the tightest adherence to the design system |
| Claude Design | AI design tool | Highest — builds the design system from the design file itself during onboarding, then reuses it for every later prototype | No MCP setup needed; generates a visual prototype quickly from text or an image; edits directly via comments | Not as deep as a code editor for complex logic | Want the design system to self-sync with no config; need a fast prototype or deck |
| Bolt / Replit | AI coding tool | High — reads Figma metadata directly, including real tokens and components | Ships with frontend, backend, and database; high fidelity | Can be more complex than a simple MVP needs | Full-stack app that still needs high fidelity to the original design |
| Figma Make | AI design tool | Medium — connects directly to Figma but doesn't yet expose tokens clearly | High visual fidelity, easiest to use since it lives inside Figma | Tokens not clearly exposed; less flexible outside Figma | Design already exists in Figma, just need to add interactivity |
| Lovable | AI coding tool | Low — relies on a written brand description, doesn't extract tokens directly | Generates a complete app from a written description | Can drift from the original design | MVP or small production app, no interest in touching code |

*Snapshot as of September 2026 — the market moves fast, so choose by category and support level, not by clinging to a specific tool name.*

**Why this comes here:** right before the project folder gets built and the rules/context file gets written for a specific tool — the choice has to be locked before that step, not during it.

**Sync note (2026-09-14), deliberate exception:** this table names specific tools, per Winnie's direct request — an intentional exception to the "no specific AI tool names" convention in `CLAUDE.md`, scoped to this table only. Matches the same exception already applied to `programs/online-course/AI Prototype Development/Section 1 - Giới Thiệu/learning/section 1-slide-outline.md`.

**What MCP actually is — one line, deliver verbally.** The table above says the top row "connects via Figma MCP" without ever defining it — give the student one sentence before moving on: MCP (Model Context Protocol) is an open standard that lets an AI coding tool read a tool like Figma directly, the same way a USB-C port works with any device rather than needing a different cable for each one. Full setup steps aren't needed yet — they live in `lesson-2-interaction-pattern-build-editing-craft.md`'s Prompt & Reference Library, for when the student actually connects it next lesson.

**Known gap, not yet reconciled:** like the other prose gaps already flagged in the Overview above, this MCP one-liner isn't in the built deck yet either — deliver it verbally from this file until the deck catches up.

---

## HOW — Organise the Project Folder

**"No wrong choice. Only mistake: no structure."** (`ai-workflow-for-ux-designers`, slide 14). Open with the end in mind: this folder is what the student will work in for the entire 4-lesson arc, and it's the same folder that gets published to GitHub in Lesson 4. Structure it right now and there's no rework later.

**The structure to set up:**

```
project-name/
├── README.md              — one paragraph: what this is, how to run it (human-facing)
├── AGENTS.md               — a short router, not the full spec
│                             (recognised by Claude Code, Cursor, Copilot CLI,
│                             Codex CLI, and Gemini CLI — the closest thing
│                             to a cross-tool standard right now)
├── CLAUDE.md, .cursorrules, etc.   — only if a student's specific tool insists
│                                      on its own filename; one line each,
│                                      "Rules live in AGENTS.md, read that first"
├── learning/                — everything the router points to, read on demand
│   ├── prd.md               — what's being built and why
│   ├── flowchart.md         — how screens connect
│   ├── preferences.md       — visual/voice/decision rules for this project
│   ├── component-inventory.md    (built this lesson)
│   └── interaction-pattern.md    (built next lesson)
├── design-system/         — exported tokens + reference screenshots from Figma
├── screens/                — the actual built screens, once they exist
└── assets/                 — images, icons, fonts

```

**Why AGENTS.md matters, and why it's a router, not a file cabinet, this is the crux of the whole arc:** most designers trying AI prototyping re-explain their system in every single prompt. That's slow, inconsistent, and doesn't scale. The fix isn't just "write it down once", it's writing it down in a shape that doesn't get reloaded in full on every prompt, and naming it something most tools already recognise without a second copy. Keep AGENTS.md itself short and stable, project overview, core conventions, and pointers to the files below it, so it's cheap to load every time. The actual detail lives in `learning/`, and the AI coding tool only pulls in the specific file a task needs, `prd.md` when scoping a new screen, `preferences.md` when a visual call is ambiguous, `component-inventory.md` and `interaction-pattern.md` when building. Point the router at `learning/component-inventory.md` and `learning/interaction-pattern.md`, and every future prompt can be short, because the system context is already loaded, on demand rather than all at once.

**Facilitator watch-fors:**

- Don't let the student skip AGENTS.md "because the folder is small right now." The point is to build the habit before it matters, not after the project has grown past the point where retrofitting it is easy.
- Watch for the file becoming a dumping ground, if the student starts pasting the whole PRD or long visual explanations straight into the router file, redirect that content into `learning/` and leave a one-line pointer behind instead. A bloated router file is a token-cost problem in its own right, it reloads in full on every single prompt whether or not that prompt needs it.
- If the student's tool insists on its own filename instead of reading AGENTS.md directly (a Claude Code student wanting `CLAUDE.md`, a Cursor student wanting `.cursorrules`), don't let them duplicate content into it. One line is enough: "Rules live in AGENTS.md, read that first." Two files with the same information drift apart the moment one gets updated and the other doesn't.
- One rule file is enough for the project sizes in this lesson. If a student's project later grows into genuinely distinct areas with different conventions (a design-system-heavy marketing site plus a data-heavy dashboard, say), nested `AGENTS.md` files per area are a real pattern, root file for global rules, a subdirectory file only where that area's rules actually differ, loaded on demand the same way `learning/` already is. Not needed for a typical single-flow prototype, worth knowing exists for when one outgrows a single file.

**Minimum result:** the folder above exists, with `README.md` and `AGENTS.md` both written (even briefly), `learning/` created (empty is fine — `component-inventory.md` gets real content next lesson), and the design system already exported into `design-system/`.

---

## HOW — Class Activity: Set Up Your Project Folder (10 min)

**Build it live, don't just show it.** After the diagram and the AGENTS.md explanation above, hand the folder structure over to the student to build for real, on their own machine, while you watch — not a follow-along demo, actual hands-on time.

**What happens in the 10 minutes:**

- Student creates the folder structure from above — README, `AGENTS.md`, `learning/`, `design-system/`, `screens/`, `assets/`
- Student exports their design system (tokens + reference screenshots) into `design-system/`
- Student writes a first pass at the rules/context file — even a few lines is enough to start

**Facilitator role during the 10 minutes:** most of this takes minutes and doesn't need supervision — check email, let the student work. The one thing worth stopping to check personally is the rules/context file, since that's this session's one must-get-right item (see the watch-fors above). If the student finishes early, let them get a head start skimming the Design Pattern material above rather than sit idle — Pre-Flight, token sync, and the component inventory are next lesson's work, not today's.

---

## DO — Wrap-up & Homework

**Land the key idea:** the system isn't the output of design work anymore — starting today, it's the input to everything that gets built from here.

**Homework before next lesson — checklist:**

- ☐ Bring the Figma file with tokens, components, and a template already in it — Pre-Flight cleanup runs at the top of next lesson, so it doesn't need to be spotless yet
- ☐ Scope the case study: pick 2–3 screens from the anchor project to prototype first — enough to prove the pattern works, not the whole product
- ☐ Confirm the project folder from today (`README.md`, `AGENTS.md`, `learning/`, `design-system/`, `screens/`, `assets/`) is set up and the design system is exported into `design-system/`

---

## Instructor Notes

- **This lesson is organised Why → What → How → Do** — mindset reframe and the pattern-first alternative (Why) → foundations recap and the Design Pattern concept (What) → folder setup (How) → wrap-up (Do). Apply the same ordering to later lessons.
- **This lesson points to `03-develop/ai-prototype-development-lesson.md` for method content instead of restating it.** The AI-foundations recap (Phase 0) and the mindset reframe (Phase 1) live there. This file only carries what's genuinely new to private-training delivery: folder organisation, the artifacts-over-prompts habit (the rules/context file and where it starts pointing to saved artifacts next lesson), and 1:1 pacing/adaptation notes. Rewriting method content here instead of pointing to it creates two sources of truth that will drift the moment the method changes.
- **Pre-Flight cleanup, token sync, and component-inventory generation are not in this lesson** — see the scope-reconciliation note in the Overview above. They open `lesson-2-interaction-pattern-build-editing-craft.md` instead.
- The rules/context file set up in this lesson is the single idea the whole arc hangs on — artifacts over prompts, this arc's application of the Feed Forward habit from Phase 0. It has nothing to point to yet by the end of this lesson besides itself and the exported design system — that's expected; `component-inventory.md` and `interaction-pattern.md` don't exist until next lesson. If a student walks away from this lesson without the folder and router file set up, next lesson starts from behind.
- Keep tool references generic in delivery ("your AI coding tool," "a second AI coding tool") so this lesson is reusable across students regardless of which tools they use — note the specific tools for a given cohort separately, outside this file.
- This lesson deliberately doesn't teach design-system fundamentals (tokens, atomic design, states) — it assumes that fluency already exists. If a student is shaky on those concepts, that's a different, earlier lesson. The "Design Pattern" slide doesn't re-teach these concepts — it names how three things the student already knows combine into the term this arc uses, and draws the line between that and "prototype pattern" (the artifact built from it).

---

*Created by Winnie Nguyen · Private Training · Last updated September 2026*
