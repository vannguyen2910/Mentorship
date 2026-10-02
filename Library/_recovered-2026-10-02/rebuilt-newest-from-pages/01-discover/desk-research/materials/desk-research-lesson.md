---
title: "Desk Research"
subtitle: "Look outward before you decide what the evidence says"
type: lesson
stage: Discover
level: "All levels"
duration: "90 min"
date: 2026-08-11
tags: [desk-research, competitor-analysis, pattern-log, assumption-map, synthesis, stakeholder-presentation]
draft: false
previous-session: "Evaluate Current Experience"
next-session: "Customer Understanding"
recovered: "rebuilt from the rendered lesson page of 2026-10-02 (not the original file); check formatting"
---

## Overview

Every redesign starts with a temptation: skip straight to solutions. This session interrupts it. Before any workflow gets touched, the team needs an evidence-backed picture of the current state, drawn from more than one place, not a list of pet peeves and not a redesign disguised as a critique.

Evaluate Current Experience looked inward: the mentee's own product, judged against heuristics. This session looks outward and sideways. It opens by formalising the raw assumptions carried over from earlier sessions into a prioritised map, because research without a target produces a pile of miscellaneous observations. Once the highest-importance, least-proven assumptions are named, the session runs desk research aimed at them: a competitor scan logged as patterns, then the other sources that already exist (support tickets, analytics, prior research). The mentee's `evaluation.md` from the previous session is the third evidence stream. All three feed back into the assumption map, which gets updated, not rebuilt. From there, the session teaches how to turn scattered findings into a narrative instead of a list, and how to present it to stakeholders with every claim traceable to evidence.

The session runs in three movements, by design. First, everything is taught the traditional way, with no AI: assumptions, desk research, synthesis, presenting. Second, the mentee practises it all by hand on their own project. Only then does AI come in, as one chain: brainstorm, convert the output to reusable `.md` assets, then visualise those files in a one-page `readout.html`, with each step verified, with particular care around invented competitors and sources. A mentee who has done it by hand can tell when AI is wrong.

---

## Who takes this session

- **Mid-level:** Evaluate Current Experience is required first. This session assumes the mentee can already run a heuristic evaluation and has an `evaluation.md`.
- **Senior:** may skip Evaluate Current Experience by passing the senior fast-track check inside that lesson. A senior who skipped it arrives without an `evaluation.md`; in Close the Loop they use whatever current-state evidence they already have (known friction, tickets, a past review).

---

## Learning Objectives

By the end of this session, students will be able to:

1. **Formalise** raw, unstructured assumptions into a prioritised map before any evidence-gathering begins
2. **Conduct** a targeted competitor scan against 2 to 3 comparators, aimed at named assumptions, and log it as patterns, not screenshots
3. **Identify** recurring patterns across sources (competitors, tickets, analytics, prior research, their own evaluation) instead of isolated observations
4. **Update** an assumption map with new evidence, moving items between Confirmed / Unconfirmed / Unknown
5. **Synthesise** findings from several sources into 3 to 4 evidence-grounded insight statements, a narrative, not a list
6. **Present** current-state findings to stakeholders using a headline-first, evidence-backed structure that can withstand pushback
7. **Verify** AI-assisted research (competitor details, sources, claims) and build reusable assets that scale beyond this one project

---

## Success Check

- Every insight traces back to named evidence: a competitor pattern, a ticket theme, a metric, a prior study, or a finding from `evaluation.md`. Nothing is a vague impression.
- The team understands what the evidence says about the assumptions that matter most, and what is still unproven.

---

## Materials Needed

- The mentee's `evaluation.md` from Evaluate Current Experience (the inward-looking evidence). Seniors who skipped it bring any current-state notes they have.
- The mentee's raw assumptions list from earlier sessions, if it exists. If it doesn't, no blocker, Activity 1 writes one quickly from the project.
- Their project's flow or key workflow, named in advance, so the competitor scan has something to compare against.
- Access to 2 to 3 candidate comparators (live products or app downloads), picked in advance if possible.
- The AI foundation folder set up in the Discovery stage, with an AI tool linked
- `Library/frameworks/assumption-map/framework-assumption-map.md`: teach directly from this file for the Assumption Map section
- A pattern log worksheet (the schema as a table, one worked example row) to hand over for the manual scan. AI turns it into `competitor-pattern-log.md` later in the session.
- Shared doc space for the three reusable assets and `readout.html` built during the AI block

---

## Pre-Class Preparation

**Prerequisite:** Mid-level mentees complete Evaluate Current Experience first. Seniors may skip it via the senior fast-track in that lesson.

Ask the mentee to do the following before the session:

1. **Bring `evaluation.md`** from Evaluate Current Experience, or whatever current-state notes exist.
2. **Bring the raw assumptions list** from earlier sessions if it exists. It's a bonus, not a blocker.
3. **Pick one key workflow** (e.g. document upload, theme customisation, checkout) to use as the subject of the competitor scan.
4. **Shortlist 2 to 3 comparators** to scan: at least one direct competitor, ideally one indirect product that serves the same user job. Make sure you can open them live.
5. **Check your AI tool works** and can create files. The AI block builds `.md` and `.html` files.

---

## Session Plan

                                                                                                     | Act | Block | Topic | Duration |
|---|---|---|---|
| 1 · Teach | Opening | Understand before you redesign | 4 min |
| 1 · Teach | Teaching | The Assumption Map: types, formula, matrix (from the framework doc) | 7 min |
| 1 · Teach | Teaching | Desk research: what it is, comparators, what to look for, patterns not screenshots | 8 min |
| 1 · Teach | Teaching | The other sources: tickets, analytics, prior research | 4 min |
| 1 · Teach | Teaching | Close the loop + the list-vs-narrative trap + insight formula | 6 min |
| 1 · Teach | Teaching | Present with confidence: headline-first, evidence, pushback | 5 min |
| 2 · Practise | Activity | Structure your raw assumptions; flag top-left test-first targets | 8 min |
| 2 · Practise | Activity | Competitor scan on your workflow, logged in the pattern worksheet | 12 min |
| 2 · Practise | Activity | Close the loop: update the Assumption Map | 5 min |
| 2 · Practise | Activity | Synthesise 2 insight statements | 6 min |
| 3 · AI assist | 1 · Brainstorm | AI suggests comparators and angles; keep only what you verify | 3 min |
| 3 · AI assist | 2 · Convert to .md | Turn verified leads and your manual work into the three `.md` assets | 5 min |
| 3 · AI assist | 3 · Visualise in HTML | Generate a one-page `readout.html` from those `.md` files only | 4 min |
| 3 · AI assist | Verify | Check each step for invented competitors, sources, claims | 2 min |
| 4 · Close | Assignment | Assignment briefed + wrap-up | 4 min |

**Scripted total: 83 min, inside a 90-minute slot.** The remaining 7 minutes are intentional buffer. Expect the Assumption Map teaching and the competitor scan to run long. That's what the buffer is for.

> **Story logic:** Teach everything first, the traditional way, so the whole method is on the table. Then practise it by hand on the mentee's own project, in the same order it was taught. Then bring in AI, where it can only speed up something the mentee already understands and can check. The stakeholder pitch is homework; it opens the next session.

---

## Core Content

### Opening: Understand Before You Redesign

You can't fix a system you haven't mapped. Every design decision made without a grounded picture of the current state is a guess, and guesses compound. A redesign built on assumptions nobody checked is a rewrite of the same unverified beliefs in a nicer interface.

The goal of this session isn't to produce a list of everything wrong or everything competitors do well. It's to produce a small number of evidence-backed insights the whole team can act on and defend, starting from what the team already (unknowingly) assumed.

Quick recap of where the evidence stands: Evaluate Current Experience produced findings from the inside. Today adds the outside. Neither is enough alone.

> **Delivery note:** Teach Parts 1 to 4 straight through with no activities in between. The activities come together after Part 4, then the AI block. Ask one quick check question per part instead of an activity.

---

### Part 1: Target What You're Testing

#### What is an assumption?

An assumption is anything believed about users, the problem, the solution, or the business that hasn't yet been proven with evidence. Every brief, every backlog, every "obviously users want X" carries them. If earlier sessions surfaced a raw list, the first job is to turn it into something that can direct the work. If not, write a quick list from the project in Activity 1.

**Full framework teaching (the four assumption types, the WHO/WHAT/WHY/SIGNAL formula, the Importance × Evidence matrix, common mistakes) lives in `Library/frameworks/assumption-map/framework-assumption-map.md`. Teach directly from that file.** What follows is the condensed version plus this session's application.

                         | Type | Covers |
|---|---|
| User | Who they are, what they care about, how they behave |
| Problem | The nature and severity of the problem |
| Solution | Whether the proposed fix addresses the problem |
| Business | Market viability, pricing, regulatory factors |

Formula: *"We believe [WHO] will [WHAT] because [WHY]. We'll know we're right when [SIGNAL]."*

Matrix: plot each assumption on **Importance** (vertical) × **Evidence** (horizontal). The top-left quadrant (high importance, low evidence) is where today's research gets pointed.

#### Why this comes before the research, not after

Open-ended research produces an open-ended list: every competitor, every feature, no priority. An evaluation or scan aimed at 3 to 5 named, high-stakes, unproven assumptions produces findings that confirm, break, or complicate a belief the team can act on. Naming the targets first is what makes the work grounded instead of exhaustive.

---

### Part 2: Desk Research

#### What is desk research?

Desk research is reviewing what already exists before generating new primary research. Competitor products, market reports, existing analytics, support ticket themes, prior research documents: it's fast and cheap, and its job here is narrow: test specific, named assumptions, not gather general inspiration. Where Evaluate Current Experience looked inward at your own product, desk research looks outward and across the organisation. It describes what is happening and what others do. It does not prescribe a fix; solutions come later.

#### Picking comparators

2 to 3 comparators is enough for one pass: a mix of direct competitors (same product category) and indirect ones (different category, same user job). More dilutes focus without adding signal. A comparator earns its place only if it speaks to a top-left assumption.

#### What to look for

Not visual inspiration. The question is: how do others solve the same job, and where do they deliberately diverge? Look at how they handle the key moments in your workflow (entry, first decision, error, completion). A pattern only goes in the log if it speaks to a named assumption.

#### Patterns, not screenshots

The most common desk research mistake is collecting screenshots and calling it research. If three of three comparators show file requirements before upload, that's not three screenshots, it's one pattern with a count, and it's a far stronger, more defensible finding. The same holds across sources: a ticket theme, a drop-off in analytics, and a heuristic finding in `evaluation.md` pointing at the same step is one pattern with three independent sources. Group raw observations into 4 to 6 recurring patterns before moving on. In the scan, each observation is a row with a fixed schema: competitor / workflow / pattern observed / which assumption it relates to / why it matters.

#### The other sources (quick pointer)

Competitor scanning is one source. Three more usually exist already and are cheaper than new research:

- **Support tickets and feedback:** look for themes and counts, not single complaints. Ask which assumption each theme speaks to.
- **Analytics:** where users drop off or loop. Numbers show where; they rarely show why, so tag them as "where" evidence.
- **Prior research:** earlier studies, survey results, interview notes. Check the date and the audience before trusting it.

For each source, note what it can and cannot prove. Everything gets tagged to an assumption, same as the scan. Full practice is in the assignment.

---

### Part 3: Synthesis

#### Close the Loop

Return to the assumption map from Part 1. For each assumption targeted today, gather the evidence from all available sources: the competitor pattern log, any ticket, analytics, or prior-research notes the mentee has, and the findings in `evaluation.md` (tag each to an assumption where one applies). Then:

- Move it to **Confirmed** if the evidence supports it, noting the sources. Two independent sources beats one.
- Keep it **Unconfirmed**, with an updated confidence note, if evidence was partial or mixed.
- Add new entries to **Unknown** if the research surfaced a belief nobody had named yet.

(Practised after the teaching, in the Close the Loop activity.) This is the step most teams skip, and it's the difference between research that produces a document and research that changes what the team believes. The assignment includes a second, fuller close once the remaining sources are gathered.

#### From List to Narrative

##### The list-vs-narrative trap

A findings log, even a well-organised one, reads as a list until it's synthesised. Stakeholders don't act on lists; they act on stories that connect a specific problem to a consequence they care about. Synthesis turns "here's what we found" into "here's what this means and why it matters."

##### The insight statement formula

For each cluster of related findings, write:

> *"We noticed [PATTERN, with evidence] across [N sources/instances]. This confirms/breaks our assumption that [ASSUMPTION]. It matters because [BUSINESS OR USER IMPACT]."*

**Weak:** "Competitors do upload differently." **Strong:** "All three comparators show accepted file formats before the upload step, and our own tickets show 'upload failed' as the top complaint theme. This breaks our assumption that users know what a valid file is. It matters because upload sits upstream of every other task; if users can't get past it, nothing downstream gets used."

Aim for 3 to 4 insight statements total. More dilutes the narrative back into a list.

---

### Part 4: Present with Confidence

#### Headline-first structure

Stakeholders are busy. Lead with the headline, the single most important insight, not the methodology. A workable structure: one-line summary of what was researched and why, then 3 to 4 insights each with evidence and business impact, then a recommended next step. Push the full pattern log and screenshots into an appendix.

#### Grounding every claim in evidence

Every insight should trace to something specific: a competitor pattern, a ticket count, a metric, a prior study, a finding with a screenshot. If an insight can't point to a specific piece of evidence, it isn't ready to present.

#### Handling pushback

"That's just your opinion" is the most common pushback. The answer is never to argue harder; point at the evidence attached to the insight: the pattern, the count, the sources, the assumption it broke. Confidence comes from preparation, not tone.

---

## Activities

All four run after the teaching, in the order it was taught. Manual only: no AI until the AI block.

### Activity: Structure Your Assumptions

**Type:** In-class · Assumption Map template (FigJam or Notion) **Time:** 8 min **Format:** Solo

1. **(3 min)** Open your raw assumptions list from earlier sessions. If you don't have one, write 8 quickly from your project, covering all four types: user, problem, solution, business.
2. **(3 min)** Select or rewrite 5 to 8 using the formula *"We believe [WHO] will [WHAT] because [WHY]. We'll know we're right when [SIGNAL]."* Make each specific, not generic.
3. **(1 min)** Plot each on the Importance × Evidence matrix.
4. **(1 min)** Share back: which assumption landed top-left, and why is it the one worth testing first?

---

### Activity: Competitor Scan

**Type:** In-class · Live comparator products + pattern log worksheet **Time:** 12 min **Format:** Solo, using your own project

1. **(2 min)** Name the workflow and the top-left assumption it relates to. Confirm your 2 to 3 comparators (at least one direct, one indirect if you have one).
2. **(6 min)** Walk the same workflow in each comparator. At each key moment (entry, first decision, error, completion), add a row: competitor, workflow, pattern observed, related assumption, why it matters. Take one screenshot per pattern.
3. **(2 min)** Group your rows into 2 to 3 recurring patterns, with a count (e.g. "3 of 3 show formats before upload").
4. **(2 min)** Share back: which pattern speaks most directly to your top-left assumption, and where do your comparators diverge?

---

### Activity: Close the Loop

**Type:** In-class · Assumption Map **Time:** 5 min **Format:** Solo

1. **(3 min)** Using your pattern worksheet and your `evaluation.md` findings (tag each to an assumption), mark each targeted assumption Confirmed (with sources), keep it Unconfirmed with an updated confidence note, or add it to Unknown if something new surfaced. Re-plot anything that moved.
2. **(2 min)** Share back: which assumption moved the furthest, and how many independent sources moved it? You'll do a second, fuller pass once tickets, analytics, and prior research come in.

---

### Activity: Synthesise Your Insights

**Type:** In-class · Insight statement formula (on paper or in a doc) **Time:** 6 min **Format:** Solo

1. **(1 min)** Review your pattern worksheet, `evaluation.md` findings, and updated Assumption Map side by side.
2. **(4 min)** Write 2 insight statements using the formula: pattern with evidence, assumption confirmed or broken, why it matters.
3. **(1 min)** Share back your strongest insight and the evidence behind it.

---

## AI in Practice: Brainstorm, Convert to .md, Visualise in HTML

Everything above was done by hand. Now AI speeds up work the mentee already understands and can check. The flow is one chain, the same as Evaluate Current Experience: **brainstorm → convert the output to `.md` → use HTML to visualise that content.** Each step feeds the next, and each step's output is checked before it moves on.

### Step 1. Brainstorm (3 min)

Paste your top-left assumption and workflow into your AI tool and ask for: comparators you may have missed (direct and indirect), and other angles on the same assumption (what tickets or analytics would show). The output is raw leads, not facts. Open each product yourself and keep only what you can verify. Mark each lead "AI-suggested, verified" or "AI-suggested, not verified", and drop anything unverified before step 2.

### Step 2. Convert the output to `.md` (5 min)

Give AI your verified brainstorm leads plus your manual work (worksheet rows, `evaluation.md` findings, your two insight statements) and ask it to convert them into saved files. Paste the existing material first, and ask it to *structure* it, not invent new content.

1. **`competitor-pattern-log.md`**: your worksheet rows plus the verified leads, in the fixed schema (competitor / workflow / pattern / related assumption / why it matters). Append-only from now on. AI's job each time is "add to this log," not "generate a new comparison."
2. **`insight-synthesis-template.md`**: the pattern, assumption, impact formula with your two insights as worked examples.
3. **`stakeholder-readout-template.md`**: headline, 3 to 4 insight slots with evidence and impact fields, recommended next step.

You also bring a fourth file, `evaluation.md`, built in Evaluate Current Experience. It is an input here, not something you build today.

### Step 3. Visualise in HTML (4 min)

Ask AI to read those `.md` files and generate a one-page `readout.html`: headline, your insights with evidence tags, the patterns with counts, impact, next step. The HTML may only use content that is in the `.md` files; no new facts and no invented numbers. If something looks wrong in the page, fix it in the `.md` and regenerate, so the `.md` stays the source of truth. Embed any screenshots so the file is self-contained. The mentee compares the page with what they would have written by hand and notes what AI got right and what it padded. They finish or rework it as part of the assignment.

### Verify (2 min, after each step)

AI is fast at suggesting comparators and describing what they do, and unreliable at it. It can name products that don't exist, describe features a product doesn't have, or cite studies and statistics it invented. The rule: nothing enters the `.md` files or `readout.html` unless you have opened the product or the source yourself. Check the readout line by line: does each claim point at a named source in your `.md` files?

### Critical thinking

- Where did AI save real time, and where did it produce something generic or wrong that needed your project context to fix?
- Clustering findings into patterns, and deciding which assumption an insight confirms or breaks, is judgment, not something to hand to AI. Where did you catch yourself wanting to skip that step?

### Prompt engineering tip

When asking AI to help with any asset, paste the existing file first and ask it to *extend* or *append to* what's there, not generate a fresh version. This is what makes the asset compounding rather than disposable.

### Ethics consideration

A confidently worded AI summary is not evidence. Every insight presented to a stakeholder must trace back to something you actually observed or read: a pattern you logged, a ticket count, a metric, a study you opened.

---

## Assessment

### Quick knowledge check

Run verbally after the practise block, before the AI block (2 to 3 min):

1. What's the difference between a pattern and a screenshot?
2. Why does a saved, append-only log beat re-prompting AI from memory every time?
3. A stakeholder says, "this is just your opinion." What's your response?

---

## Assignments

### Assignment: Full Desk Research Pass

**Due:** Before next session **Time estimate:** 2 to 3 hours **Type:** Analysis · Your real project

Take today's practice pass to full scale on your actual project.

1. Finish the competitor scan: 2 to 3 comparators in total (a mix of direct and indirect), every pattern logged in `competitor-pattern-log.md` with a screenshot and a related assumption.
2. Gather at least two of the other sources: support ticket themes, analytics, prior research. Log each as patterns with counts, tagged to assumptions, noting what each can and cannot prove.
3. Update your Assumption Map fully: every targeted assumption moved to Confirmed, Unconfirmed (with updated confidence), or newly added to Unknown, citing sources.
4. Write 3 to 4 insight statements using your Insight Synthesis Template, each grounded in at least two pieces of evidence where possible.
5. Finish `readout.html` and a 60-second spoken version of your pitch: headline, top insight with evidence and impact, recommended next step. You will deliver it at the start of the next session, and I will push back once. Practise pointing at your evidence, not arguing harder.

**Deliverable:** Updated `competitor-pattern-log.md`, source notes, updated Assumption Map, and `readout.html`. Share before the next session.

> **AI in Practice:** *"Here's my pattern log and my source notes: [paste both]. Using my insight synthesis template, draft 4 candidate insight statements. Flag any that rest on a single source or on something I haven't verified myself."*

---

## Further Resources

- **Assumption Map framework (internal):** `Library/frameworks/assumption-map/framework-assumption-map.md`: full teaching content: types, formula, matrix, common mistakes
- **UXPin, Desk Research in UX:** https://www.uxpin.com/studio/blog/desk-research/: methods and step-by-step guide
- **UXPin, Competitive Analysis for UX:** https://www.uxpin.com/studio/blog/competitive-analysis-for-ux/: comparator selection and evaluation criteria
- **Miro, How to Present UX Research Findings:** https://miro.com/research-and-design/ux-research-presentation-examples/: structuring a stakeholder-ready readout

---

*Created by Winnie Nguyen · Private Training · Last updated October 2026*
