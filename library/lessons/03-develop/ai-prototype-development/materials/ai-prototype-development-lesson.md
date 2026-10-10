---
title: "AI Prototype Development"
subtitle: "How to use AI and your design system to prototype smarter — not screen by screen"
type: lesson
stage: Develop
level: "Intermediate"
duration: ""
date: 2026-06-16
tags: [prototype, AI, figma, design-system, pattern-first, system-thinking]
draft: true
previous-session: "Design Once. Use Everywhere. (Atomic Design)"
recovered: "rebuilt from the rendered lesson page of 2026-10-02 (not the original file); check formatting"
programs: [ui-ux-fundamentals:09, junior-to-mid-level:07, mid-to-senior:07]
---

## Overview

In the previous session, students built a design system — tokens, atoms, molecules, organisms, templates, and at least one page. They know *how to build systematically*. This session answers *how to prototype that system* — using AI as a collaborator, not just a generator.

The most common mistake designers make when prototyping is starting with a screen. They open Figma (or a coding tool), pick a screen, and start filling it in. Then they do the next screen. Then they realise screens don't connect. Components diverge. States are missing. AI output is inconsistent because every prompt starts from scratch.

**Template-first flips this.** Before touching any screen, you define two things:

1. What components exist — including all their states (empty, loading, error, filled) — from your design system
2. How users move through the product (interaction pattern)

Once that prototype pattern exists, AI can build from it. Students take their prototype pattern and use an AI coding tool to generate a working, browser-viewable prototype — no screen-by-screen design required.

**Why "pattern"?**

The word "pattern" isn't arbitrary — it comes from software engineering. In object-oriented programming, the *Prototype Design Pattern* is a technique where instead of building new objects from scratch every time, you define one prototype object and clone it. Each clone starts identical, then gets customised for its specific use. The principle: define once, reuse many times, customise at the edges.

That's exactly what this lesson does for prototyping. Your component inventory is the prototype. Every screen AI builds is a clone — assembled from the same defined parts, not invented from scratch. Designers who've worked with engineers will find this familiar. Designers who haven't now have the vocabulary to talk about it.

**What is an AI-assisted prototype?**

An AI-assisted prototype (also called a GenAI prototype) is a working, browser-viewable prototype where the screens are *generated* by AI — not designed one by one in a design tool. Instead of placing every element by hand, the designer defines the rules: what components exist, what states they can have, and how screens connect. The AI coding tool reads those rules and assembles the screens from them.

The output is real code — HTML or React — running in a browser. Not a clickable Figma file. Not a mockup. A prototype that a developer, stakeholder, or user can open on any device, interact with, and share via a link.

What makes it "AI-assisted" (not just "AI-generated") is that the designer stays in control of the decisions. You define the system. You set the constraints. You review every screen and correct what's wrong. The AI handles the assembly. The result is faster than building by hand, and more accurate than asking AI to design from a blank brief — because the brief is already written. It's called your prototype pattern.

A realistic expectation: NN/G research (2025) found that AI prototyping tools "follow general directions but lack the sophistication to weigh design tradeoffs." Output is often good at a distance — assembled, interactive, running in the browser — but misses subtleties: spacing, grouping, visual hierarchy, contrast. It will also default to generic visual styles if you don't give it your tokens and your component system. That's exactly what the first two steps of Phase 4 prevent.

Adobe Design's experiment (2026) found the opposite of what most people expect: working closer to the build process made collaboration *more* intensive, not less. Design judgment, taste, and craft didn't disappear — they became more essential because decisions were made in the moment the experience was actually taking shape.

This lesson focuses on the **coded prototype path**: using an AI coding tool to generate HTML or React from the prototype pattern. The prototype pattern is the instruction manual. AI does the assembly.

This lesson follows one path: **Starting fresh** — generating a prototype pattern from your design principles up, regardless of how much of your design system you've already built. The output is the same either way: a prototype pattern AI can build from.

> **This lesson builds directly on your Atomic Design output.** Students who completed their Figma Template and at least one Page are ready to go. Students who didn't complete it will use a provided starter template — but the lesson will make you want to finish it.

---

## Learning Objectives

By the end of this session, students will be able to:

1. **Explain** why pattern-first prototyping is faster and more consistent than screen-by-screen
2. **Define** a prototype pattern: component inventory (with states) and interaction pattern
3. **Use an AI tool** to analyse their design system and generate a prototype blueprint
4. **Use an AI coding tool** to generate a working prototype from their prototype pattern
5. **Build** at least 1 working screen in the browser with navigation to at least 1 other state

---

## Materials Needed

- Students' Figma files from the Atomic Design session (Templates + at least one Page)
- Starter Figma template (provided for students without completed work)
- Access to an AI chat tool (any tool you're comfortable with, for the framework-generation step)
- One AI coding tool for the build, picked from the comparison below
- Prompt library handout (see below)

### Choosing an AI Tool

                                                     | Tool | Type | Design-system support | Strengths | Weaknesses | Use when |
|---|---|---|---|---|---|
| Cursor / Claude Code / Windsurf | AI coding tool | Highest — connects via Figma MCP, reads variables, tokens, components, and variants directly | Most detail on the design system via MCP | Requires manual MCP setup; no visual design UI | Already comfortable in a code editor, need the tightest adherence to the design system |
| Claude Design | AI design tool | Highest — builds the design system from the design file itself during onboarding, then reuses it for every later prototype | No MCP setup needed; generates a visual prototype quickly from text or an image; edits directly via comments | Not as deep as a code editor for complex logic | Want the design system to self-sync with no config; need a fast prototype or deck |
| Bolt / Replit | AI coding tool | High — reads Figma metadata directly, including real tokens and components | Ships with frontend, backend, and database; high fidelity | Can be more complex than a simple MVP needs | Full-stack app that still needs high fidelity to the original design |
| Figma Make | AI design tool | Medium — connects directly to Figma but doesn't yet expose tokens clearly | High visual fidelity, easiest to use since it lives inside Figma | Tokens not clearly exposed; less flexible outside Figma | Design already exists in Figma, just need to add interactivity |
| Lovable | AI coding tool | Low — relies on a written brand description, doesn't extract tokens directly | Generates a complete app from a written description | Can drift from the original design | MVP or small production app, no interest in touching code |

*Snapshot as of September 2026 — the market moves fast, so choose by category and support level, not by clinging to a specific tool name.*

**Sync note (2026-09-14), deliberate exception:** this table names specific tools, per Winnie's direct request — an intentional exception to the "no specific AI tool names" convention in `CLAUDE.md`, scoped to this table only. Matches the same exception already applied to `programs/online-course/AI Prototype Development/Section 1 - Giới Thiệu/learning/section 1-slide-outline.md`.

---

## Pre-Class Preparation

**For students:**

Before class, check your Figma file against this list. How far you get tells you which entry point you are:

                              | Level | What to check | Ready? |
|---|---|---|
| Atoms & Molecules | Key components have variants (at minimum: default + one other state) | ☐ |
| Organisms | At least 2 Organisms assembled from your molecules (e.g. nav bar, form, card list) | ☐ |
| Templates | At least 1 Template frame exists per screen in your concept (skeleton layout, no real content) | ☐ |
| Pages | At least 1 Page exists — a Template filled with real text, real images, realistic data | ☐ |

- Bring what you have — your Figma file and (if you have one) your codebase. If your system is partial or you haven't started, download the starter template from the class Notion page.
- Regardless of how much you've completed, today's process is the same: build your prototype pattern from design principles, then build.
- Make sure you have access to an AI chat tool — use whichever you're most comfortable with
- **Connect your MCP before class.** Set up the connection between your design tool and your AI coding tool (e.g. Figma MCP → Cursor, or similar). This must be working before Phase 4 — troubleshooting it mid-session costs too much time. If you're unsure how, follow the setup guide on the class Notion page.

**For the instructor:**

- Prepare a live demo using your own Figma template (a simple 3-screen flow works well: onboarding → home → detail)
- Have a pre-built coded prototype ready as a "reveal" for the coded path demo
- Load the prompt library into your AI tool before class so you can demo without typing

---

## Session Structure

                             | Phase | Activity |
|---|---|
| 0 | AI foundations recap (conditional — skip if already covered) |
| 1 | Mindset reframe — why pattern-first beats screen-by-screen |
| 2 | Generate the prototype pattern — from design principles to a document AI can build from |
| 4 | Hands-on build — clean up design file, then AI coded prototype |
| 5 | Share & reflect |

---

### Phase 0 — AI Foundations Recap

> **Run this phase only if students haven't already covered "Set Up Your AI Workflow" (or equivalent foundations) — check this during Pre-Class Preparation. Don't assume tool fluency just because a student is a confident designer: Phase 1's mindset reframe assumes this vocabulary already exists, so skipping this phase for a student who needs it makes Phase 1 land softer than it should.**

Adapted from `ai-workflow-for-ux-designers` ("Set Up Your AI Workflow"), slides 5–20 — the mindset and working-vocabulary content this lesson leans on. Skips slides 1–4 (course intro, adoption stats) and everything past 20 (the four-bucket AI-in-practice framework, assignments) as out of scope here.

**Part A — Mindset (slides 5–9).** Trim or skip this part for a student who's already comfortable with AI tools generally and just needs the tactical vocabulary in Part B — it's onboarding, not required review.

**From maker to strategist and editor** (slide 5) AI is a set of gloves, not a new hand. The work shifts from making everything by hand to directing and editing what AI produces — the designer stays the strategist. Land this first: it frames everything after it as a shift in role, not a loss of control.

**Mindset 1 — AI takes the tedious work, you keep the judgment** (slide 6) AI handles what's repetitive. Authorship, taste, and ethics stay with the designer.

**Mindset 2 — treat AI like a talented intern, not an oracle** (slide 7) Fast, tireless, occasionally brilliant — and it still needs supervision. Every output gets reviewed, not trusted blind.

**Mindset 3 — we've been here before** (slide 8) Remember VR? Hype peak, then a dip, then durable use. Today's rough AI output isn't a verdict on the method — it's the normal dip before the tool becomes genuinely useful.

**Plain-language version** (for explaining this further down the chain, or to someone new to it): first bike ride, you wobble and fall. That doesn't mean bikes are broken, it means you're still learning. AI tools are at that wobbly stage right now. They'll get steadier.

**Optional activity** (slide 9): ask the student to name one time AI helped and one time it quietly hurt their work. Worth running if the student has enough AI-tool history to draw on; skip it for someone brand new to these tools with nothing yet to reflect on.

**Part B — Working Vocabulary (slides 10–20).** Always run this part — Phase 1 assumes this vocabulary already exists.

**Markdown, briefly** (slide 11) Plain text with typing rules — what AI tools read and write by default. Not abstract: the prototype pattern students write in Phase 2 (component inventory, interaction pattern) is a markdown document. That's why it's `.md` and not a Word doc — AI parses it cleanly and cheaply.

**What a prototype actually is** (slide 12) An AI-generated prototype is just an HTML file — a structure a browser renders, not a Figma export. Say this plainly before students reach Phase 4's build, so the output format isn't a surprise.

**How markdown and HTML work together** (slide 13) Raw insight goes in as markdown — brainstorms, documentation. AI turns it into something that runs in the browser as HTML — the prototype itself, a synthesis report, a map. One is what you write; the other is what gets shown.

**Folder organisation, briefly** (slide 14) "No wrong choice. Only mistake: no structure." One project, one folder, organised from day one — not the day the AI coding tool opens. This lesson's own Phase 4 runs its own MCP-connected workflow and doesn't need re-teaching this, but private-training adaptations of this lesson (see `systematic-ai-prototyping-lesson.md`) build directly on it.

**AI-generated vs. AI-assisted** (slide 16) "AI decides" vs. "you decide, AI assembles faster than you could alone." This is the same distinction drawn in this lesson's own Overview under "What is an AI-assisted prototype?" — landing it here first, before Phase 1, means it isn't explained twice.

**CARE — the shape of a good prompt** (slide 17) Context (the situation — who's asking, what project, what stage), Ask (one clear task, not five vague ones), Rules (constraints, tone, format), Examples (show, don't tell). Several prompts later in this lesson already follow this shape; naming the structure explicitly helps students who want to write their own variations rather than just running the provided ones.

**The context habit — reuse, don't retype** (slide 18) "Reuse what you already have, don't retype it" — Starting Fresh vs. Feed Forward. A new chat starts at zero; a folder doesn't. This is the same principle behind this lesson's prototype pattern: define once, save it, point the AI tool at the file instead of re-explaining the system in every prompt.

**Vague vs. CARE-structured — see the difference** (slide 19) If time allows, run this live: prompt an AI tool with something vague ("make this better") next to a CARE-structured version of the same request, on the same task, and compare the output side by side. Fine to defer this demo to Phase 4 instead, once students are writing their own build prompts — the payoff is bigger there, and it avoids running the same demo twice.

**What each tool is for** (slide 20) A one-line map distinguishing an AI coding tool (Cursor, GitHub Copilot, Claude Code) from an AI chat tool (ChatGPT, Claude, Gemini) and from in-tool AI features (Figma AI, Notion AI). Students new to the coding-tool category need this before Phase 4, not during it.

**Facilitator note:** treat this as real onboarding for students who need it, not a formality — check comfort with the chosen AI coding tool's basic interface (where to type, where output appears, how to accept/reject a change) before moving into Phase 1. This phase is not yet reflected in the live slide deck (`ai-prototype-development-slide-outline.md` / the Claude Design deck) — until those are updated, deliver it verbally or from this file directly.

---

### Phase 1 — Mindset Reframe

**The problem with screen-by-screen prototyping**

Open with a demonstration, not a slide. Take a simple 3-screen flow (e.g. Login → Dashboard → Detail). Show what happens when you prototype it screen by screen:

- Each screen is a separate design decision
- Components drift (the button on screen 1 is slightly different from screen 3)
- When the design changes, every screen needs updating
- When you hand it to an AI tool, each prompt starts from zero
- Each retry or redo reprocesses everything that came before it, which quietly burns far more tokens, and money, than expected

This isn't just a quality problem, it's a cost problem too. Agentic AI tasks can consume up to 1,000x more tokens than a simple chat reply, and because conversation history resends with every message, a short prompt can balloon past 15,000 tokens by message twenty. Developers have reported losing $47 in a single afternoon, or $350 in a day, almost entirely from retry and regeneration loops, the same "starts from zero" pattern this phase is about to fix.

Then show the pattern-first alternative:

- Start with the component inventory (what exists)
- Map the interactions (how screens connect)
- Define states (what can change on a component)
- Now every screen is just an *arrangement* of things that already exist

**Key message:** Your design system is not the output of Atomic Design. It is the *input* to your prototype. The Template you built is a blueprint. AI just builds from blueprints.

NN/G research confirms this directly: "longer prompts with clear, detailed design requirements consistently yield better results" with AI coding tools. The prototype pattern *is* that detailed context. Without it, AI fills gaps with assumptions — generic layouts, default styles, misread patterns. With it, AI builds from a complete brief rather than guessing.

**Discussion prompt (neighbour exercise):** "Turn to the person next to you: if AI could read your entire design file right now and build a prototype, what would it need to know that isn't visible in your designs? Then share one answer with the class."

Collect 2–3 answers quickly. Common ones: what clicks lead where, what empty/loading/error states look like, what the user is trying to do. These map directly to the two layers of a prototype pattern:

- "What clicks lead where" → **interaction pattern**
- "What components exist and what looks they can have" → **component inventory (with states)**

**In Phase 2, you will build this document.** Everything students just named in the discussion is what they're about to make explicit — for themselves, and for their AI tool.

---

### Phase 2 — Generate the Framework

> **Structure:** Class demo → Students run their own prompts → Regroup and share outputs

**Class demo**

Before students touch their own files, run Starting fresh live using your own Figma template. Show the complete sequence: system qualities → token decisions → component inventory → product context → prototype pattern. Students don't need to follow along yet — they're watching the rhythm of the prompts and seeing what the output looks like. Point out the moment product context enters and what changes.

---

**Students run their own prompts**

Students choose their entry point and run the prompts below. Students with large inventories will want to keep going — tell them the goal is a working prototype pattern, not an exhaustive one. They can complete it in homework.

**What a prototype pattern is**

Regardless of entry point, every student produces the same output by the end of this phase: a **prototype pattern** — a structured description of their design system that AI can build from. It has two layers:

1. **Component inventory** — all components with their variants and states included (default, hover, loading, empty, error, success)
2. **Interaction pattern** — how screens connect and under what conditions

States are part of the component inventory — not a separate layer. When you list a component, you list all the looks it can have right there alongside it.

**Interaction pattern types**

Every screen in a prototype is doing one of a small number of things. Knowing the type helps you map the correct components and transitions:

                                             | Type | What it does | Example screens |
|---|---|---|
| **Read** | User views content — no state change | Dashboard, detail page, profile, feed |
| **Edit** | User modifies existing content | Settings, edit profile, update item |
| **Add** | User creates something new | New post, add to cart, create account |
| **Confirm** | User reviews and approves an action | Order summary, delete confirmation, submit form |
| **Navigate** | User moves between sections | Tab bar, menu, back/forward |
| **Search / Filter** | User queries or narrows a list | Search results, filter panel, sort |
| **Onboard** | User is guided through first-time setup | Welcome screen, tutorial steps, permissions |

Most prototypes use 3–4 of these. When you map your interaction pattern, label each screen with its type — it tells AI exactly what kind of flow to build, what components it needs, and what transitions are required.

---

#### Starting fresh

The risk when starting fresh is jumping straight to product context — "I'm building a food delivery app" — and generating UI that looks right but doesn't have a principled system underneath it. Instead, start with how the system should *feel*, then let product context come second.

**Step 1 — Define system qualities, not product**

Students describe the qualities they want the system to have — without naming the product:

> "I want to design a system that is [calm / energetic], [minimal / rich], [serious / playful], with [fast / deliberate] interactions. Generate design principles and token decisions — colour scale, type scale, spacing rhythm — from these qualities. Don't assume any specific product."

Your AI tool returns a principled token structure tied to the qualities, not to a product category.

**Step 2 — Generate the Atomic component inventory**

From those principles, your AI tool generates a component list that any product built on this system would need:

> "Based on these design principles, what Atomic components does this system need? List atoms, molecules, and organisms with their required states. Keep it product-agnostic — just what the system requires."

**Step 3 — Apply product context**

Only now do students bring in their specific concept:

> "My product is [X] for [Y users]. I have this prototype pattern: [paste]. Which components map to my 3–4 screens? What needs adapting? What's missing?"

**Step 4 — Interaction pattern**

> "My prototype has these screens: [list]. The user's goal is [goal]. Map the interactions — what does each screen link to, and under what conditions?"

States are already captured in Step 2 as part of the component inventory. Students don't need a separate state map prompt.

**Instructor note:** Walk through Steps 1–2 live before students start. Show them how the AI tool generates a system that could apply to multiple products — then in Step 3, watch it narrow to their specific concept. This is the AI-as-collaborator moment: students see that the system predates the product.

---

**Regroup**

Ask 2–3 students to share their prototype pattern on screen briefly. You're not reviewing quality — you're normalising what the output looks like. "Does yours roughly look like this? Good. If not, don't worry — we'll use Phase 3 to fill the gaps."

**Convergence point:** by the end of Phase 2, every student has a prototype pattern with a component inventory (states included) and an interaction pattern.

---

### Phase 4 — Hands-On Build

> **Prerequisite:** MCP connection between design tool and AI coding tool must be set up before this phase. See Pre-Class Preparation.

**Step 1 — Clean up your design file**

Before AI reads anything, remove what shouldn't be there. Unused components, duplicate variants, orphaned test layers, one-off experiments that never got deleted — AI can't tell "this is part of my system" from "I forgot to delete this." It will include all of it in the component inventory, and the prototype ends up bloated with things nobody meant to ship.

Checklist:

- Delete or archive components you're not using in this prototype
- Merge duplicate variants of the same component (two slightly different buttons with different names)
- Remove hidden/test layers and old exploration frames
- Confirm naming is consistent — the same component shouldn't have two different names in different places

Prompt to use (if the file is large enough that eyeballing it isn't practical): "Here is my Figma component list: [paste]. Which of these look like duplicates, unused variants, or one-off experiments rather than real system components?"

This step is easy to skip because it feels like tidying, not real work. It isn't optional — it's the difference between an accurate component inventory in Step 4 and a bloated one built on messy design work.

**Step 2 — Scope the build** Pick 2–3 screens from your interaction pattern. Don't try to build everything. The goal is to prove the pattern works — not to finish the prototype.

**Step 3 — Sync your design tokens**

> "Read my design file via MCP. Extract the design tokens — colour values, typography styles, and spacing. Generate a CSS variables file from these tokens so every screen uses the exact values from my design system."

This runs once. All screens built after this step use your actual design colours and type, not AI defaults. NN/G found that without explicit token guidance, AI tools default to generic visual styles — often resembling common component libraries with neutral colour palettes and minimalist styling that looks interchangeable across products. Token sync is what makes the output look like *your* product, not a template.

**Step 4 — Generate the component inventory**

> "Read my design file. Generate a component inventory: list every component with its name, purpose, and all its states (default, hover, loading, error, etc.). Flag anything that looks incomplete or inconsistent."

Students review the output. Correct names or states that are wrong. This becomes the source of truth for the build. If Step 1 was actually done, this list should be short and clean — a long, messy inventory here is a sign to go back and finish cleanup first.

**Step 5 — Generate the interaction pattern**

> "Based on the component inventory, map the interaction pattern for my prototype: which screens exist, what connects them, and what triggers each transition. Use the component inventory as your reference."

**Step 6 — Build one screen at a time**

"One screen at a time" isn't the screen-by-screen anti-pattern from Phase 1. There, each screen was designed from scratch with no shared reference — that's what caused the drift. Here, every screen is built against the same component inventory and interaction pattern from Steps 4–5, so context doesn't reset between screens. Building sequentially — instead of one giant prompt for everything — is what makes the review loop possible: catch and correct an issue on screen 1 before it repeats on screens 2 and 3.

Write build prompts using five ingredients: goal (what this screen does), layout (how things are arranged), content (what information is real, not placeholder), audience (who's using it), and flow context (what screen this follows, what it leads to, and what carries over — cart contents, form data, login state). Losing flow context is the most common way a sequentially-built prototype ends up feeling like disconnected screens instead of one product.

> "Build the [Screen name] screen. Goal: [what the user is trying to do here]. Layout: [how things should be arranged — e.g. 'metrics in a top row, detail chart below']. Content: [real field names and sample data, not lorem ipsum]. Audience: [who's using it]. Flow context: this screen follows [previous screen] and leads to [next screen]; carry over [state/data that persists]. Use the full component inventory and interaction pattern above — not just this screen's portion. Match component names exactly. Output [React/HTML]."

If you have a reference screenshot — a similar screen, a competitor layout, visual inspiration — attach it before you prompt. "Make it feel like this" works far better with an image than a description.

**Refine each screen** — after building, compare it to your design file and correct using whichever mode fits the size of the fix:

                         | Mode | Use for | Example |
|---|---|---|
| Chat | Broad or structural changes, anything needing explanation | "Rearrange this screen so the primary action is in the top row." |
| Targeted feedback | One specific element — name exactly what's wrong and where | "The button padding here is too tight." "Use the primary token colour on this card." |
| Direct adjustment | Quick spacing/alignment nudges you can just drag into place | (no prompt needed, if your tool supports direct manipulation) |

Rule of thumb: chat for structure, targeted feedback for component-level fixes, direct manipulation for anything you can drag. Mixing all three based on the fix is faster than describing everything in chat.

**Exploring a different direction:** if a screen isn't working, don't overwrite it blindly — say so explicitly: "Save what we have and try a completely different layout for this screen." Most AI design tools preserve the current version so you can compare rather than lose it.

> "This is what you built: [describe]. Here is what should be different: [list corrections]. Update the output."

**Minimum output:** 1 screen running in browser with navigation to at least 1 other state

**What to expect from AI output (set this expectation before students start):** First screens will be technically assembled but rough — spacing may be off, groupings may not match the design, hierarchy may feel flat. This is normal and documented. NN/G research found that even with detailed prompts, AI output "missed subtle but important details related to spacing, grouping, and hierarchy." The review step is exactly where designer judgment enters. Tell students: the first output isn't the result — it's the starting point.

**Instructor support during hands-on:**

- Circulate and check students are correcting after each screen — not just generating and moving on
- Key coaching question: "Does this match your design? What would you correct before building the next screen?"
- If students feel discouraged by imperfect output: "This is normal — NN/G found AI gets close but misses nuance. Your eye is what makes it right. That's not a bug — that's the job."
- If students skip the review: "The review is where you get AI accuracy. Generation without review is just guessing."
- If MCP connection fails: students fall back to pasting the prototype pattern as markdown text into the AI tool — they still run steps 4–6, just without live file reading
- Circulate during Step 1 specifically and check students are actually deleting/archiving components, not just skimming the file — this is the step most likely to get skipped or rushed, and it's the one that determines whether Step 4's inventory is usable

### Phase 5 — Share & Reflect

Ask 2–3 students to share their screen:

- What did you build?
- What did the AI do that surprised you?
- What would have taken longer without the prototype pattern?

**Closing thought for the instructor to land:**

> Screen-by-screen prototyping scales to 3 screens. Template-first prototyping scales to 300. The designers who get hired in the next 5 years won't be the ones who can design faster — they'll be the ones who can *define the system clearly enough that AI can build from it*. That's what you practised today.

---

## Concept Extension — Stitching Prototypes

> **Run this as a separate standalone session for intermediate cohorts.** Do not try to fit it into the same session as the pattern-first lesson — it will crowd out the hands-on build time that freshers need most. A dedicated session file should be created for this content.
>
>
>
> It can be briefly mentioned during Phase 1 as a third reason why pattern-first matters — one sentence is enough ("Later, you'll see how this same prototype pattern lets you stitch multiple team prototypes into a single journey"). Full teaching belongs in its own session.
>
>
>
> For students who finish Phase 4 early, you may share the Nathan Curtis article link as optional reading.
>
>
>
> This concept can be introduced during Phase 1 as a third reason why pattern-first matters, taught as a standalone extension for students who finish Phase 4 early, or expanded into its own session for advanced cohorts.

### What is a Stitched Prototype?

> "A stitch prototype is a collection of prototypes from multiple products, woven together to interactively demo a threaded, complete digital journey." — Nathan Curtis, EightShapes

A stitched prototype is not a single Figma file with all your screens. It is a navigable experience assembled from multiple design artefacts — Figma frames, screenshots, coded screens, even lo-fi sketches — connected at the seams so a user (or stakeholder) can walk the complete journey end-to-end.

The individual parts may have been built by different teams, in different tools, at different fidelity levels. Stitching doesn't require them to be consistent. It requires them to be connected.

---

### Why Stitch?

**1. Products span multiple flows and personas — your prototype usually doesn't.** A student's 3–4 screens might cover a customer journey. But what about the banker who processes the same application? The broker who submitted it? Stitching lets you prototype across personas without duplicating the design system.

**2. Stakeholders see fragments. Stitching shows them the whole.** Individual team demos are expert demos. "Here's our screen, here's what it does." A stitched prototype is a user demo. "Here's what the customer experiences, from the moment they start to the moment they're done." Those are completely different conversations — and the second one is the one that aligns stakeholders and surfaces the real gaps.

**3. Transitions are where the real design problems hide.** Screen 2 and Screen 3 look fine in isolation. But what happens between them? Who triggers the transition? What data carries over? What does the user see while they wait? Stitching forces you to design the seams, not just the screens.

---

### How to Stitch

**Step 1 — Define the journey thread** Before touching any file, write one sentence: *"The user's goal across all screens is [goal]."* This is the thread. Every screen in the stitch must serve this thread. If it doesn't, it doesn't belong — or the thread needs to be longer.

**Step 2 — Gather artefacts, don't rebuild them** Collect what exists: Figma frames, exported PNGs, coded screens, even annotated wireframes. A stitch prototype is not a redesign. Gather, don't rebuild. If a screen is missing, note it as a gap — don't fill it now.

**Step 3 — Build an index** Create a homepage for your stitch — a single page that lists every screen in the journey with its current status (complete, in progress, missing). This is the bird's-eye view. Stakeholders can drop in from any point. Designers can see where the gaps are.

**Step 4 — Add the seams** Connect each screen to the next with navigation links. This is the actual stitching. Seams don't need to be perfect — a clickable button that leads to the next screen is enough. Don't get lost perfecting transitions; get the path walkable.

**Step 5 — Demo the journey, not the screens** Present the stitch as a user would experience it — start to finish, in character. Don't narrate the design decisions. Narrate the user's goal. "She opens the app wanting dinner sorted without thinking about it. She does this. She sees this. She gets here." One minute. Then stop and invite discussion.

> **Resist fixing seams.** A stitch prototype reveals inconsistency — it is not an audit tool. If you see a button that's slightly wrong or spacing that's off, note it and move on. Turning a stitch session into a design review kills the collaboration that makes stitching work. — Nathan Curtis

---

### How AI Fits

Stitching is where AI becomes genuinely powerful — not at the component level, but at the journey level.

**AI chat tool — identify missing seams**

> "Here is my interaction pattern: [paste]. Here are the screens I've built: [list]. What transitions are undesigned? What does the user see between Screen 2 and Screen 3 that hasn't been prototyped?"

**AI chat tool — generate the index page**

> "Here are my prototype screens: [list each with a one-sentence description and status: complete/in progress/missing]. Generate a simple HTML index page that lists them with their status, links to each, and shows the overall journey flow."

**AI coding tool — build the HTML stitch shell** For coded prototypes, an AI coding tool can build the navigation shell that connects Figma exports or coded screens into a single navigable experience:

> "I have these screens as separate HTML files: [list]. Build a navigation wrapper that stitches them into a single prototype — a homepage index, back/forward navigation, and a progress indicator showing where the user is in the journey."

---

### Real-World Example

> *Use this with students if relevant — you don't need to show the screens.*

At NAB, five design squads were building separate pieces of a mortgage platform — income verification, document management, credit assessment, settlement, and more. Each squad had its own Figma file, its own prototype, its own demo. No one was showing the banker's complete journey from application to approval.

A stitched E2E prototype was built across all five squads — one shared canvas, navigable end-to-end. The impact: 90% E2E journey coverage, 4 personas aligned, 2–3× more explicit design decisions. The key was not rebuilding anyone's work — just connecting it. The seams were visible. That was fine. The journey was now visible too. That was everything.

---

### The Stitch Mindset

Three things to teach students before they stitch:

1.  **It's a throwaway artefact.** A stitched prototype exists to communicate the journey while the product is being built. The day the product ships, the stitch is retired. Don't treat it like a deliverable — treat it like a communication tool with an expiry date.
2.  **The goal is the journey, not the screens.** Individual screens will be imperfect. Inconsistencies will be visible. That's the point — stitching surfaces what polished individual demos hide.
3.  **One minute hooks the room.** A complete end-to-end demo should take no more than 60 seconds. Walk the user goal, not the design decisions. If you can't tell the story in a minute, the journey isn't clear enough yet.

---

### Resources

- **Nathan Curtis — [Stitching Prototypes](https://medium.com/eightshapes-llc/stitching-a-journey-together-in-a-prototype-d3b86d26ebb)** *(EightShapes, 2015)* — the original article, saved in your Notion Knowledge Sharing library. The Marriott International case study is the clearest illustration of the concept. Assign as pre-reading if you teach this as a standalone session.
- **EightShapes reference** — [eightshapes.com/articles/stitching-a-journey-together-in-a-prototype](https://eightshapes.com/articles/stitching-a-journey-together-in-a-prototype/)

---

## Homework

**Template-first prototype completion**

Extend your prototype from today:

- Add at least 2 more screens to your interaction pattern
- Ensure every component in the new screens comes from your existing design system (no new components without updating the inventory)
- Document one thing AI got wrong and how you corrected it

Submit: a live/repo link or code repository link + a 3-sentence reflection on the AI collaboration experience

---

## Prompt Library Reference

### Starting fresh

                         | Goal | Prompt |
|---|---|
| Define system qualities | "I want a system that is [calm/energetic], [minimal/rich], [serious/playful]. Generate design principles and style decisions — colour palette, typography, spacing. No product name yet." |
| Generate component inventory | "Based on these design principles: [paste]. What UI components does this system need? List small pieces like buttons and inputs, medium pieces like forms and cards, and bigger sections like nav bars. Include all the states each component needs. Keep it general — not tied to any specific product yet." |
| Apply product context | "My product is [X] for [Y users]. I have this prototype pattern: [paste]. Which components fit my screens? What needs changing? What's missing?" |
| Interaction pattern | "My prototype has these screens: [list]. The user's goal is [goal]. Show me how each screen connects to the others — what does a tap or action lead to? What happens if something goes wrong?" |

### Build Phase

                         | Goal | Prompt |
|---|---|
| Start coded prototype | "Build a prototype from this prototype pattern: [paste]. Use [React/HTML]. Match these naming conventions: [list]." |
| Review AI output | "Does this [code/design] match my interaction pattern? What's missing or inconsistent?" |
| Unstick mid-build | "I'm building [screen]. Available components: [list]. How do I assemble this screen without creating anything new?" |
| Correct AI mistakes | "This output has these problems: [list]. Here is the correct behaviour: [describe]. Fix only these issues." |

---

## Instructor Notes

**Handling mixed completion from Atomic Design:** Students who didn't complete the Template from the previous session may feel behind. Frame it positively: "This lesson will show you exactly why the Template matters. Use the starter file today, and you'll want to go back and finish your own."

**The most common failure mode:** Students treat Phase 4 as "free design time" and start inventing new things. The prototype pattern is a constraint, not a suggestion. If a student needs a component that isn't in their inventory, that's a signal — either they missed it in Phase 2, or their concept has shifted. Either way, it's a design decision to make consciously, not accidentally.

**On AI outputs that are wrong:** When an AI tool generates something incorrect, that's curriculum. Stop the class, show it, and ask: "What did we not tell the AI clearly enough?" This reinforces that AI quality depends on how well you define the prototype pattern — which is exactly the skill this lesson builds.

**Pacing notes:**

- Starting fresh students often run long in Phase 2 if they have large component inventories. Cap the prompting and tell them to finish the prototype pattern in homework.
- Phase 4 always feels too short. Reassure students: the goal is to prove the prototype pattern works, not to finish the prototype.

---

## Recommended Resources

These are resources I'd genuinely point students to — not a complete list, but the ones that make the biggest difference for this specific lesson.

---

### Mindset & Framework Thinking

**[Atomic Design by Brad Frost](https://atomicdesign.bradfrost.com/)** *(free online)* Still the clearest articulation of why systems beat screens. Students coming from the previous session will have seen this — point them to Chapter 4 specifically, which covers moving from design system to deliverable. This is the conceptual bridge into today's lesson.

**[The Component Gallery](https://component.gallery/)** *(free)* A curated reference of how real design systems name and structure their components. Useful in Phase 2 when students are auditing their component inventory — if they're unsure what to call something or whether they're missing a component type, this is a faster reference than googling.

---

### Figma Prototype Path

**[Figma Variables documentation](https://help.figma.com/hc/en-us/articles/15339657135383)** *(official docs)* The authoritative source on Variables — the most important Figma feature for pattern-first prototyping. The section on "modes" is what makes design tokens from the Atomic Design session actually work inside a prototype. Worth reading before class, not during.

**[Smart Animate guide — DesignCourse on YouTube](https://www.youtube.com/watch?v=6Id4INKEwb8)** The clearest practical walkthrough of Smart Animate I've found. Under 15 minutes. Recommend this to Path A students who haven't used it before — watch it the night before the session, not during.

---

### Coded Prototype Path

**[shadcn/ui](https://ui.shadcn.com/)** *(free, open source)* The best real-world example of a design system that directly becomes code components. When students ask "what does a coded design system actually look like?", show them this. Recommend this as a reference for what students are building toward — not a template to copy.

**[v0 by Vercel](https://v0.dev/)** *(free tier available)* A browser-based AI tool for generating UI components from descriptions. More constrained than a full AI coding environment — you describe a component, it generates it, you copy it — but that constraint is useful for students just starting out with AI-generated code. A good stepping stone before moving to a full AI coding tool.

**Your AI coding tool's documentation** Whatever tool students choose — Cursor, GitHub Copilot, Windsurf, or others — point them to the section on context and codebase indexing. The reason pattern-first works so well with AI coding tools is that they can read your whole project, but only if it's structured clearly. The prototype pattern from Phase 2 is what makes the AI's suggestions accurate rather than generic.

---

### AI Collaboration

**Your AI tool's prompting guide** Every major AI tool publishes guidance on how to get better results from prompts. The prompt library in this lesson is a starting point, not the ceiling. Encourage students to read the guide for whichever tool they use — specifically the sections on specifying output format and giving the AI a role to play. Both techniques are directly applicable to the prompts in Phase 2.

**[AI-assisted design-to-code workflows — Lenny's Newsletter](https://www.lennysnewsletter.com/)** *(search "AI design prototype")* Lenny's newsletter has published practitioner walkthroughs of AI-assisted design-to-code workflows across multiple tools. The quality varies, but the best ones are honest about what breaks and why — which is more useful for students than polished demos that make everything look easy.

---

### What I'd Actually Assign

If I had to pick one resource per path:

- **Everyone:** Brad Frost Chapter 4 — before class
- **Figma prototype students:** Figma Variables docs — skim before class, reference during
- **Coded prototype students:** shadcn/ui homepage — just look at it, understand what a coded design system produces, then come to class ready to build toward that

Everything else is optional depth. Students who finish the hands-on early can explore v0 or their AI tool's prompting guide. Students who struggle should focus on the prototype pattern, not the tools.

---

## Connection to Curriculum

                             | Session | Role in this lesson |
|---|---|
| Problem Understanding | Defines the user goal that drives the interaction pattern |
| Synthesis & Problem Definition | Defines what success looks like — used to evaluate prototype completeness |
| Design System (Atomic Design) | Produces the component inventory and Template that this lesson builds from |
| **This session** | Translates the design system into a working prototype using AI |
| Next session | TBD |
