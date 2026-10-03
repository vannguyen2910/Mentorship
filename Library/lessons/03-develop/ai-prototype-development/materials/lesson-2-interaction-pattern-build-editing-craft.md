---
title: "AI Prototype Development"
type: lesson
stage: Develop
level: "Intermediate"
duration: ""
date: 2026-09-19
tags: [prototype, AI, design-system, pattern-first, interaction-pattern, tokens]
draft: false
recovered: "rebuilt from the rendered lesson page of 2026-10-02 (not the original file); check formatting"
---

> **Filename note:** this file is still named `lesson-2-interaction-pattern-build-editing-craft.md` from when the lesson carried the build and editing-craft content. That content has moved to Lesson 3 (see the scope note below), so the filename no longer describes the lesson. Renaming it means updating `lesson_file` in the slide outline and the README table — worth doing in one pass, not piecemeal. **Scope note (2026-09-18):** Pre-Flight cleanup, syncing design tokens and generating the component inventory — originally taught in Lesson 1 — moved here to match the delivered Lesson 1 deck, which ends at the conceptual "Design Pattern" overview rather than building it hands-on. **Scope reconciliation (2026-09-19) — this lesson no longer teaches building screens.** The built deck (`Lesson 2 - Build It standalone.html`) ends at "Map the Pattern." The three-file model, the five-ingredient build prompt, the three edit modes, the timed hands-on build and the second-tool comparison have been removed from this file; they are Lesson 3's opening work now. Two additions came the other way: **scoping the build** and **confirming the student's setup** are now explicit steps of their own, before any tool work. Net effect is a shorter, tighter session — see the time budget below, which now comes in around 70 minutes rather than 90. **Two known deck mismatches, recorded not fixed:** the Closing slide still claims "2–3 screens working in the browser, refined with the three edit modes," and the Cover's speaker notes still reference working screens and a Section 4 second-tool comparison. Neither happens in this deck. Replacement wording is proposed at the top of `lesson-2-slide-outline.md`.

## Overview

Lesson 1 named the Design Pattern — tokens, component inventory, template — as three things the student already has in Figma. Naming it isn't the same as having it in a form AI can read. This lesson turns that named concept into real, saved artifacts: synced tokens, a component inventory, coded templates, all consolidated into one page, `design-system.html`. It then adds the second half of a prototype pattern — the **interaction pattern** — and folds that back into the same page, so it stops being a static swatch sheet and becomes navigable.

**What the student leaves with:** `design-system/tokens.css`, `learning/component-inventory.md`, one coded template per pattern type, `learning/interaction-pattern.md`, and a `design-system.html` they can open in a browser and click through. No screens yet — screens are Lesson 3.

**Three ways to get there, same destination.** A student with Figma MCP set up reads the design file directly (Method A). A student without it pastes what they have into their AI coding tool and has it generate the same output (Method B). A student whose team's design system already lives in code points the tool at the repository instead (Method C). None is a lesser fallback. Confirm which applies at the setup step and walk only that path — a given student runs exactly one.

**This lesson runs on top of `03-develop/ai-prototype-development-lesson.md` ("AI Prototype Development"), not alongside it** — same relationship Lesson 1 has to it. The Pre-Flight checklist and the token-sync and component-inventory prompts are that lesson's Phase 4 Steps 1, 3 and 4, run as written. What's new here: the three-method framing, one coded template per pattern type, consolidating everything into one demoable page, and the interaction pattern taught as its own concept rather than a single prompt.

## Session Structure

**Organised Why → What → How → Do**, same convention as Lesson 1.

1. **[WHY]** Recap: the Design Pattern is named, not yet real
2. **[HOW]** Pre-Flight: clean up the design file
3. **[HOW]** Scope the build — 2–3 screens, decided before any tool work
4. **[HOW]** Confirm your setup — MCP, no MCP, or design system in code
5. **[DO]** Sync your design tokens
6. **[DO]** Generate the component inventory
7. **[DO]** Bring the templates into code
8. **[DO]** Consolidate into `design-system.html` — review everything once, together
9. **[WHAT]** The interaction pattern
10. **[DO]** Generate the interaction pattern — prompt, cross-check, update the showroom
11. **[DO]** Wrap-up & homework

**Suggested time budget — treat as the default plan, not an aspirational one:**

                                                                           | # | Segment | Minutes |
|---|---|---|
| 1 | Recap | 3 |
| 2 | Pre-Flight | 8 |
| 3 | Scope the build | 3 |
| 4 | Confirm setup | 2 |
| 5 | Sync tokens (generate only) | 5 |
| 6 | Component inventory (generate only) | 5 |
| 7 | Templates into code (generate only) | 6 |
| 8 | Consolidate + review everything, once | 10 |
| 9 | Interaction pattern (concept) | 6 |
| 10 | Interaction pattern (prompt + cross-check + update showroom) | 12 |
| 11 | Wrap-up | 5 |
| — | Buffer | 5 |
| **Total** |  | **~70** |

**This session now runs about 70 minutes, not 90 — an open decision, not an oversight.** Removing the build freed roughly twenty minutes. Three reasonable uses, in rough order of preference: spend it on the consolidation review, which is where every deferred correction lands and where a rushed pass costs the most later; let the session genuinely end early, which a 1:1 can do and a cohort can't; or pull the first screen build forward from Lesson 3, which re-fattens this lesson and thins the next. Decide deliberately rather than letting the time drift into whichever segment overruns first. **Recommendation as of 2026-09-19: spend it on the consolidation review, and do not pull the first screen forward.** Lesson 3 is built around screen one being the screen whose corrections generate the rules file; moving it here separates the build from the harvest by a week and the harvest is what makes Lesson 3 work.

**Review moved, not added.** Segments 5–7 look short because they are: no correction happens at any of them. The single combined pass in segment 8 replaces three separate reviews (a CSS file, a markdown table, a mental check against Figma) with one look at a rendered page.

---

## WHY — Recap: The Design Pattern Is Named, Not Yet Real

**Open with a callback, not a re-teach.** Lesson 1 already taught the Design Pattern (tokens, component inventory, template, in Figma) and how it differs from the prototype pattern (in the project folder, in markdown, for AI to read). Don't restate either. Ask the student to say the difference back in one sentence, and move on.

**Key message:** naming a system and having AI build from it are two different milestones. Today closes that gap.

**One-on-one adjustment:** ask whether the student's Figma file changed since Lesson 1. Pre-Flight catches drift either way, so this isn't an inspection — it's a natural opener.

---

## HOW — Pre-Flight: Clean Up the Design File

**This is Phase 4 Step 1 in `03-develop/ai-prototype-development-lesson.md`, run exactly as written.** Before AI reads anything, remove what shouldn't be there. AI can't tell "this is part of my system" from "I forgot to delete this" — it includes all of it in the component inventory, and everything after is built on top of the mess instead of the system.

**Checklist:**

- Delete or archive components not used in this prototype
- Merge duplicate variants of the same component
- Remove hidden/test layers and old exploration frames
- Confirm naming is consistent across the file

**Prompt to use**, if the file's too large to eyeball:

> "Here is my Figma component list: [paste]. Which of these look like duplicates, unused variants, or one-off experiments rather than real system components?"

**Facilitator note:** feels like tidying, isn't optional — it's the difference between a short, clean inventory in the next step and a bloated one built on messy design work. The deck's before/after shows exactly what this catches: `Button`, `Button v2`, `btn_old` collapsing to one `Button`.

---

## HOW — Scope the Build

**Screen scoping was taught in Lesson 1** ("Which Screens Are Right": one user goal, 2–3 screens, and the three traps), and the student scoped their screens as Lesson 1 homework. This is a decision, not a lesson — keep it to a minute or two.

**Two things to settle:**

- Pick 2–3 screens from the interaction pattern named last lesson.
- The goal is to prove the pattern works, not to finish the prototype.

**Why it sits here rather than later:** the number and type of screens picked here is what makes the template step concrete — it tells you how many templates you need and which pattern types they have to cover. Scope after the templates are built and you find out too late.

---

## HOW — Confirm Your Setup

**One question, asked once, before any tool work: is Figma MCP connected?** The answer decides which method the student runs for every generation step ahead — token sync, component inventory, templates. Confirming it now means the rest of the session walks one path instead of re-asking at each step.

- **MCP connected** — read the design file live for every step ahead.
- **Design system already in code** — point at the repository instead of Figma.
- **No MCP** — paste the values and component list in directly. *This third path is in the notes but is not a card on the deck's slide; if a student is on it, say so aloud, because the slide won't.*

**Facilitator note:** if Method A stalls mid-session, don't troubleshoot the connection live — drop straight to the paste-based path for whichever step failed. Same saved file, same output, no time lost debugging.

---

## DO — Sync Your Design Tokens

**Runs once, matters for every screen after.** Without it, AI defaults to generic visual styles — colours and type that could belong to any product. This is what makes everything built later look like the student's actual product rather than a template.

**Prompt to use** (this is the deck's wording, the MCP version — adapt the first line for the other two methods):

> "Read my design file [Link]. Extract the design tokens: colour values, typography styles, and spacing. Generate a CSS variables file from these tokens so every screen uses the exact values from my design system."

**Practical tip worth saying out loud:** have the file open and selected in the Figma desktop app first, then copy the link of the section or the whole file. A link to a file that isn't open is the most common reason this step returns nothing useful.

**What comes back** is a `:root` block of CSS variables named by purpose — `--color-action-primary`, `--space-card-gap` — not by raw value. If they come back named `--color-blue`, that's a correction, but not now.

**Save the result** as `design-system/tokens.css` and wire it into the router file the same way it already points at `learning/`. **Don't check the values yet** — that happens once, at consolidation.

---

## DO — Generate the Component Inventory

**Structure: brief demo → student runs it on their own system → move straight to the templates.** Correction happens once, for everything together, at consolidation.

**Prompt to use** (the deck's wording):

> "Read my design file [Link]. Generate a component inventory: list every component with its name, purpose, and all its states (default, hover, loading, error, etc.)."

**What "good" looks like:** every component, every state, nothing invented. The deck shows the output as a rendered gallery rather than a markdown table — Button across four variants, three colours and three states — which is a more honest picture of what a useful inventory contains than a table of names.

**Watch-fors, deferred not skipped.** Method B needs the heaviest check later: without live file access, AI is likelier to guess at a state that doesn't exist or miss one that does. Method C usually needs the lightest — states are visible in the component code — but it can miss anything designed in Figma that hasn't shipped. Say which caveat applies to this student now, out loud, so it isn't forgotten a few minutes from now.

**Save the output** to `learning/component-inventory.md`. This is the file the rest of this lesson and Lessons 3–4 build from. Nothing written here gets retyped into a prompt again.

---

## DO — Bring the Templates Into Code

**One template per pattern type, not one overall.** A Read screen and an Edit screen don't share a skeleton — Read has content to look at, Edit has fields to fill. Lesson 1 tells the student most prototypes use three or four pattern types, so needing more than one template is the normal case, not the exception. The scoping step above already told you which types are in play.

**Structure: one prompt, not three.** Token sync and the component inventory each needed three parallel methods because the whole task was getting untouched design data out of Figma. By this step that data already exists as saved artifacts, so this prompt leads with them as fixed inputs. The only thing that still varies is how the template frame gets handed over — pasted, screenshotted, or described — and that's one bracket, not a separate prompt per method.

**Prompt to use** (the deck's wording):

> "Here's my template frame: [paste or screenshot]. Using tokens.css and component-inventory.md, output is html. Match the layout exactly."

**Say the expanded version aloud even though the slide is terse:** use only the tokens and components already in those two files; if a value or element doesn't match anything already built, flag it rather than inventing a new one. The fuller CARE version is in the Prompt Library below for a student who wants it written out.

**The template was already designed in Figma, in Lesson 1** ("Design It in Figma", which promised it was the one ingredient nothing would regenerate for them). This step translates it into code — it doesn't redesign it and it doesn't replace the Figma step. Say that explicitly, or a student will open Figma and start over.

**Open knock-on:** Lesson 1 has the student design a single template in Figma. If Lesson 2 wants one per pattern type, Lesson 1's Figma step should produce one per type too. Not a Lesson 2 fix — flagged here so it isn't a surprise.

**Save each as `design-system/template-<type>.html`.** Don't review yet — move straight to consolidation.

---

## DO — Consolidate Into design-system.html

**This is the payoff of the last three steps, and the first "open it in a browser" moment of the lesson.** Tokens, component inventory and templates were generated separately; now they become one real page, and the review deferred three times finally happens, once, together.

**Prompt to use** (the deck's wording — the longest prompt in the deck, and the one worth reading aloud in full):

> "Build `design-system.html` from tokens.css, component-inventory.md, and template.html. This page is my checkpoint — where I check my design system against Figma before I build any screens. Storybook as a layout preference only — not the tool. One plain HTML file, no build step. Tokens: every value as a labelled swatch showing the token name and the value. Components: one block per component — its name, then every state side by side, each labelled. Show hover and focus as static examples. Template: the empty structure, generic content. Link to tokens.css. Everything on the page uses those tokens, not browser defaults. End with a list of anything you couldn't render."

**Two phrases do most of the work.** Naming the page a *checkpoint* tells the AI what it's for, so it resolves layout questions itself instead of guessing. *Storybook as a layout preference* buys the whole component-gallery convention — name, then variants in a labelled grid — in four words. The "not the tool" clause is not optional: Storybook is a real tool with a config folder and a build step, and without that clause the AI may scaffold one, contradicting the no-build-step model taught in Lesson 1.

**Teaching line for the Storybook mention:** this is the designer's version of the page engineers already keep in Storybook — and the same kind of page as MUI's component docs, which the student saw in Lesson 1 ("Template, Seen in MUI"). Said that way it's a callback and shared vocabulary, not a new concept.

**Why "end with a list of anything you couldn't render."** Tokens and the component inventory were both told to flag rather than invent, but their review was deferred to this moment — so the whole design otherwise rests on the student spotting problems by eye. This line makes the page report its own gaps: a component in the inventory with no markup, a token referenced but never defined, a state listed with no distinct styling. It's also the first time in the arc the AI is asked to account for its own output rather than just produce it — worth naming as a habit, not just a rule in this prompt.

**Review everything here, once — starting with the page's own "couldn't render" list.** Read that list first: it's the fastest route to the real gaps, and anything on it is a correction before the visual pass even starts. Then open the page in the browser together and check it against Figma — token colours match, every component state that should exist is rendered, the templates' structure matches the design.

**Real test:** components must visibly use the synced tokens, not browser defaults. A component that renders but ignores the tokens hasn't implemented them — that's a correction.

**Facilitator note on the deferred caveats:** if the student ran Method B, look harder here for an invented or missing state — this is exactly where it shows up. If Method C, check specifically for anything designed but not yet shipped.

**Save the corrected result.** This page, and the `tokens.css` it links to, are what every screen built in Lesson 3 gets compared against, not Figma directly.

---

## WHAT — The Interaction Pattern

**This is Phase 2 in `03-develop/ai-prototype-development-lesson.md`** — the second of the two prototype-pattern layers, and the thing still missing at the end of Lesson 1. A component inventory says what exists. An **interaction pattern** says how it connects: which screens exist, what triggers a move from one to the next, and what carries over between them.

**Define it by the gap, not by a definition.** The student has just spent roughly 35 minutes on artifacts that describe things that exist. The fastest way in is the absence: the inventory says a Button exists in four states, and nothing built so far says what happens when it's pressed. Named concretely — AI builds beautiful screens where nothing goes anywhere — this lands faster than any definition of the term.

**How it connects to what's already built — teach it as the floor plan.** The deck runs on a house metaphor (tokens are the paint, components are the furniture, a screen is a room, `design-system.html` is the showroom). The interaction pattern extends it rather than introducing anything new:

                              | Artifact | In the house | Answers |
|---|---|---|
| `interaction-pattern.md` | **the floor plan** | **how many rooms, which doors?** |
| `tokens.css` | the paint | what does it look like? |
| `component-inventory.md` | the furniture | what exists? |
| `template.html` | one room's shape | how is a room laid out? |

The metaphor does real work here, it isn't decoration: a floor plan is exactly what reveals whether one room shape is enough. That's why the template cross-check has to happen *after* this file exists rather than before — an ordering that otherwise reads as arbitrary.

**Remind the seven screen types, don't re-teach them — but do put them on screen.** They were shown in Lesson 1 explicitly as a lookup catalogue, something not to memorise; here they change job and become load-bearing, since each screen in the pattern gets labelled with its type and that label is what tells AI which components and transitions the screen needs. Content that changes job a week later needs more than verbal recall, so the slide carries a light strip of the seven names — Read, Edit, Add, Confirm, Navigate, Search / Filter, Onboard. Say each in one breath and move on; the definitions stay off the slide. One screen can carry two — checkout is Edit and Confirm at once. Full definitions live in the source lesson's Phase 2 table.

---

## DO — Generate the Interaction Pattern

**Three beats, in order: prompt, cross-check, update the showroom.** The middle one is the beat people skip, and it's the one that costs rework if skipped.

**Prompt to use** (the deck's wording):

> "Based on the component inventory, map the interaction pattern for the screens I'm about to build: which screens exist, what connects them, and what triggers each transition. Describe it like a gallery of cards, where clicking one card opens its own detail screen with its own interactions. Use the component inventory as your reference. Once this checks out against the template, update `design-system.html` to include this file — make each screen card on it clickable so it opens that screen's own flow."

**Save the result** to `learning/interaction-pattern.md`, alongside the component inventory, and point the router file at it too. From here on every build prompt can be short, because both layers of the prototype pattern exist as files.

**Why the template is deliberately not an input to this prompt.** The prompt reads the component inventory only, even though the templates now exist — and a sharp student will ask why. Feeding a template in anchors the AI to the shape it just read: it proposes screens that fit that shape and reports back that one shape is enough. But the interaction pattern is the thing meant to *reveal* whether one shape is enough, so pre-loading the answer defeats the check. Worth saying as a prompting habit rather than a rule about this lesson: don't hand the AI the answer you're asking it to check. Map the pattern blind, then cross-check.

**Cross-check against the templates — two questions, not one.**

**1. Shape.** If a scoped screen's type doesn't fit any template built — a list view when only a detail template exists — that's another quick template now, not a surprise later. Repeat "Bring the Templates Into Code" once more before moving on.

**2. Flow.** Does the template carry the shared elements the flow actually needs — a back affordance, persistent navigation, a progress indicator in a multi-step sequence? The templates were built before the interaction pattern existed, so they were designed without knowing there was a flow at all. Because every screen inherits from them, every screen will be missing the same element. This is the cheaper problem to fix and the more expensive one to miss: it surfaces in Lesson 3, when the student tries to move between screens and there's nothing to click. Fix it by editing the template file directly — a one-minute addition, not a regeneration.

**3. Update the showroom.** Once the cross-check passes, `design-system.html` gets regenerated to fold in `interaction-pattern.md`. It stops being a static swatch page and becomes navigable: each screen appears as a card tagged with its pattern type, and clicking a card opens that screen's own flow. This happens once, here, because `interaction-pattern.md` didn't exist at the first consolidation.

**One thing to be honest about with the student:** the screens don't exist yet, so clicking a card opens the *template's shape* for that screen type, not a built screen. That's still useful — it's the first time they see their whole prototype laid out — but don't let them think they've built it. **Resolved (2026-09-19, when Lesson 3 was drafted):** the cards stay pointed at template shapes. Lesson 3 builds a separate `index.html` as the stitched journey's entry point, so `design-system.html` stays what it is — the system checkpoint — rather than becoming a second, competing front door.

---

## DO — Wrap-up & Homework

**Land the key idea:** the prototype pattern isn't a document that sits in a folder — it's the thing every screen built from here forward reads from instead of a retyped prompt.

**Recap what today actually produced,** which is four files and one page, not screens: `tokens.css`, `component-inventory.md`, one template per pattern type, `interaction-pattern.md`, and a navigable `design-system.html`.

**Homework before next lesson — checklist:**

- ☐ Finish correcting the component inventory if anything on the "couldn't render" list is still outstanding
- ☐ Confirm every scoped screen has a template to build from — add one if the cross-check found a gap
- ☐ Open `design-system.html` once more away from the session and click through every screen card
- ☐ Bring the 2–3 scoped screens to Lesson 3 ready to build

**Name what's next explicitly:** Lesson 3 builds the screens from these files and stitches them into one demoable journey. Nothing built today gets thrown away or redone.

---

## Prompt & Reference Library

**The deck's wording is canonical** — the prompts below are exactly what's on the slides and what the student should run. The CARE templates that follow each one are the expanded form, for a student who wants more scaffolding than the short prompt gives. If the deck's wording changes, re-derive the CARE version from it rather than letting the two drift.

**Pre-Flight cleanup:**

> "Here is my Figma component list: [paste]. Which of these look like duplicates, unused variants, or one-off experiments rather than real system components?"

**Token sync — deck wording:**

> "Read my design file [Link]. Extract the design tokens: colour values, typography styles, and spacing. Generate a CSS variables file from these tokens so every screen uses the exact values from my design system."

*Expanded (CARE), Method A — MCP:*

> **Context:** I'm building [project name] and I've already got my design tokens set up in Figma, in [file or page name]. **Ask:** Read my design file via MCP. Extract the design tokens — colour values, typography styles, and spacing. **Rules:** Generate a CSS variables file from these tokens, named by purpose (e.g. `--color-action-primary`, not `--color-blue`). Every screen built from here on should use these exact values, never a default or an arbitrary one. Save the file as `design-system/tokens.css`. **Examples:** For example: `--color-action-primary: #6B3FEE; --spacing-card-gap: 24px;`

*Expanded (CARE), Method B — no MCP:*

> **Context:** I'm building [project name]. I don't have Figma MCP connected, so I'm giving you the token values directly. **Ask:** Here are the design tokens from my Figma file: [paste colour values, type styles, spacing scale]. Generate a CSS variables file from these. **Rules:** Name tokens by purpose, not by raw value. Every screen built later should use these exact values, not a default. Save the file as `design-system/tokens.css`. **Examples:** For example: `--color-action-primary: #6B3FEE; --spacing-card-gap: 24px;`

*Expanded (CARE), Method C — design system in code:*

> **Context:** I'm building [project name]. My team's design system already lives in code, at [repo or file path], not primarily in Figma. **Ask:** Here is my design system's codebase: [open the repo, or paste the theme/token config file]. Extract the design tokens — colour values, typography styles, and spacing — into a CSS variables file I can reuse. **Rules:** Use the codebase as the source of truth. If Figma and the codebase disagree on a value, flag it — don't guess which one is current. Save the file as `design-system/tokens.css`. **Examples:** For example: `--color-action-primary: #6B3FEE; --spacing-card-gap: 24px;`

**Component inventory — deck wording:**

> "Read my design file [Link]. Generate a component inventory: list every component with its name, purpose, and all its states (default, hover, loading, error, etc.)."

*Expanded (CARE), Method A — MCP:*

> **Context:** I'm building [project name], a [what kind of product] for [who it's for]. My Figma file's components live in [where in the file]. **Ask:** Read my design file via MCP. Generate a component inventory: list every component with its name, purpose, and every state it has. **Rules:** Only include components and states that actually exist in the file — flag anything incomplete instead of inventing it. Group by component. Output as a markdown table. Save it as `learning/component-inventory.md`. **Examples:** For example: `| Button | Primary action | default, hover, loading, disabled |`

*Expanded (CARE), Method B — no MCP:*

> **Context:** I'm building [project name]. I don't have Figma MCP connected, so I'm giving you the component list directly. **Ask:** Here is my component list: [paste names, variants, and any states you already know]. Generate a component inventory from this. **Rules:** Every component needs its purpose and every state — flag anywhere you'd expect a state that isn't listed, rather than inventing one. Output as a markdown table. Save it as `learning/component-inventory.md`. **Examples:** For example: `| Button | Primary action | default, hover, loading, disabled |`

*Expanded (CARE), Method C — design system in code:*

> **Context:** I'm building [project name]. My design system already lives in code, at [repo or file path]. **Ask:** Here is my design system's codebase: [open the repo]. Generate a component inventory from the actual components. **Rules:** Read states from the component code itself — props, variants, conditional styles — not from comments or docs alone. Output as a markdown table. Save it as `learning/component-inventory.md`. Cross-check against Figma in case something's been designed but hasn't shipped. **Examples:** For example: `| Button | Primary action | default, hover, loading, disabled |`

**Templates into code — deck wording:**

> "Here's my template frame: [paste or screenshot]. Using tokens.css and component-inventory.md, output is html. Match the layout exactly."

*Expanded (CARE), one template per pattern type:*

> **Context:** I'm building [project name]. I've already got `design-system/tokens.css` and `learning/component-inventory.md` — here they are: [paste or attach both files]. I'm building a [type] screen and a [type] screen. Here are my template frames, structure without real content: [paste the frames, screenshots, or describe them]. **Ask:** Generate a skeleton for each in HTML and CSS — structure only, placeholder content, one file per template. Use only the tokens and components already in the two files above. **Rules:** Match each layout exactly — spacing, grouping, and hierarchy as designed. Use the synced tokens for any colour, type, or spacing value; use the exact component names from the inventory. If something doesn't match anything already built, flag it — don't invent it. Save as `design-system/template-<type>.html`. **Examples:** For example, a Read template with a sticky header using the `Nav` component and a scrollable content area of placeholder `Card` components; an Edit template with labelled `Input` fields and a Cancel / Save row.

**Consolidate into design-system.html — deck wording:**

> "Build `design-system.html` from tokens.css, component-inventory.md, and template.html. This page is my checkpoint — where I check my design system against Figma before I build any screens. Storybook as a layout preference only — not the tool. One plain HTML file, no build step. Tokens: every value as a labelled swatch showing the token name and the value. Components: one block per component — its name, then every state side by side, each labelled. Show hover and focus as static examples. Template: the empty structure, generic content. Link to tokens.css. Everything on the page uses those tokens, not browser defaults. End with a list of anything you couldn't render."

**Interaction pattern — deck wording:**

> "Based on the component inventory, map the interaction pattern for the screens I'm about to build: which screens exist, what connects them, and what triggers each transition. Describe it like a gallery of cards, where clicking one card opens its own detail screen with its own interactions. Use the component inventory as your reference. Once this checks out against the template, update `design-system.html` to include this file — make each screen card on it clickable so it opens that screen's own flow."

---

## Reference: MCP, Code Connect & Token Naming

**This section is reference depth, not live-session content** — the lesson itself only needs the one-question setup check and Method C's prompts above. Pull from here only if a student wants MCP working live, asks what Code Connect is, or wants the reasoning behind a token-naming correction. Snapshot as of September 2026 — setup steps for any specific tool move fast, confirm current steps rather than assuming these hold indefinitely.

**What MCP is.** Model Context Protocol is an open standard (from Anthropic) that lets an AI tool connect to external tools and data sources through one consistent interface, instead of a custom integration per tool. The common analogy: a USB-C port for AI — one standard connector instead of a different cable for every device. Figma's MCP server is what exposes a design file's components, tokens and layout data to an AI coding tool as structured data, rather than the AI having to guess from a description.

**Setting up Figma's MCP server.** Two versions exist:

- **Remote (cloud-hosted)** — Figma's recommended default, simpler to set up. For Claude Code specifically, install Figma's plugin (`claude plugin install figma@claude-plugins-official`), which bundles MCP settings and skills together.
- **Desktop (local)** — more powerful, runs on the student's machine. Enable it inside the Figma desktop app: open a design file → toggle to Dev Mode → in the Inspect panel, find the MCP section → turn on "Enable desktop MCP server."

**Why Method C exists, and what Code Connect is.** Even with MCP fully working, an AI coding tool reading a Figma file has no way to know a real, already-coded component library exists unless it's told — by default it will still generate fresh code that only resembles the design. Figma's own answer is **Code Connect**: it maps each Figma component to its real production code counterpart, so Dev Mode (and MCP) can return the actual code snippet from the codebase instead of an autogenerated guess. Code Connect setup is its own configuration step most students won't have done — which is exactly why Method C skips Figma and points the AI coding tool straight at the repository instead. Same goal, simpler path for a single lesson.

**Token naming.** Tokens named by purpose (`--color-action-primary`) survive a rebrand; tokens named by value (`--color-blue`) become lies the first time the blue changes. If the sync returns value-named tokens, that's a correction at consolidation, not a style preference.

---

## Instructor Notes

- **This lesson is organised Why → What → How → Do**, same convention as Lesson 1 — recap (Why), Pre-Flight/scope/setup and the interaction-pattern concept (How/What), everything hands-on (Do).
- **The session now runs around 70 minutes against a 90-minute slot.** That's a deliberate consequence of moving the build to Lesson 3, not a gap to fill by accident. See the note under Session Structure for the three reasonable uses of the spare time; pick one before the session, not during it.
- **Two deck mismatches are known and unfixed** — the Closing checklist and the Cover's speaker notes both still promise screens and a second-tool comparison this deck doesn't deliver. Proposed replacement wording is at the top of `lesson-2-slide-outline.md`. Until they're fixed, don't read those two slides' notes aloud verbatim.
- **Every prompt on the slides is short and plain — there is no CARE breakdown in this deck, deliberately.** By Lesson 2 the CARE shape has been taught and used; the slides carry the runnable prompt. The expanded CARE versions in the Prompt Library are for a student who asks for more scaffolding, not the default teaching form.
- **Three methods, one per student.** Confirm at the setup step, then walk only that path. Don't demo all three live — that's reference material, not a teaching sequence.
- **Method B needs closer review than Method A; Method C usually needs the least.** Without live file access, Method B is likelier to invent a state that doesn't exist or miss one that does. Method C reads real component code, so states are usually accurate, but it can miss anything designed in Figma that hasn't shipped.
- **Don't cut Pre-Flight or token sync if running long.** Everything after depends on both being done properly. The first thing to trim is the Pre-Flight before/after walkthrough, then the interaction-pattern concept slide; final polish of the component inventory pushes to homework before either.
- **The router file from Lesson 1 keeps paying off.** By the end of this lesson it should point to four things: `component-inventory.md`, `interaction-pattern.md`, `design-system/tokens.css`, and `design-system.html`. If any aren't wired in, Lesson 3 gets harder than it needs to be.
- **Open knock-on for Lesson 1:** its "Design It in Figma" slide has the student design a single template. This lesson expects one per pattern type. Reconcile in one pass when Lesson 1 is next touched.
- Keep tool references generic in delivery ("your AI coding tool") so this lesson is reusable across students regardless of which tools they use.

---

## Connection to Curriculum

This lesson is a private-training adaptation layer on top of `03-develop/ai-prototype-development-lesson.md` ("AI Prototype Development") — Phase 4 Steps 1, 3 and 4, and Phase 2, re-paced for 1:1 delivery and picking up exactly where Lesson 1 ends. The genuinely new content, not covered in the source lesson as written: the three-method framing (MCP / no-MCP / design-system-in-code), explicit scope and setup steps before any tool work, one coded template per pattern type, consolidating everything into a single demoable `design-system.html`, the interaction pattern taught as its own concept rather than a single prompt, and folding that pattern back into the same page so it becomes navigable.

Phase 4 Steps 5 and 6 — the five-ingredient build prompt and the three edit modes — are **not** covered here. They open Lesson 3.

---

*Created by Winnie Nguyen · Private Training · Last updated September 2026*
