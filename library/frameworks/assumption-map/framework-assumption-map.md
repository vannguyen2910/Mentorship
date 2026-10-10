---
title: "Assumption Map"
type: framework            # framework | guide | template | reference
program: both               # ux-class | private-training | both
tags: [assumptions, research-planning, prioritisation, evidence, stakeholder-management]
level: intermediate
date: 2026-08-11
draft: false
download: ""
---

## What This Is

An Assumption Map is a prioritisation tool that surfaces everything a team believes without evidence — about users, the problem, the solution, or the business — and sorts those beliefs by how much they matter and how much proof exists for them. It doesn't replace research. It tells you which research to run first, and it gives you a place to record what any research method (an interview, a heuristic audit, a desk research pass, an analytics pull) actually proved or disproved. The output is a short, ranked list of the assumptions most likely to break the project if they're wrong — which is exactly what any evidence-gathering activity should be pointed at.

---

## When to Use It

- At the start of a project or a new phase, before any evidence-gathering begins — it decides what to go look for, not what you found.
- When a team is stuck or disagreeing about direction and everyone is arguing from a different unstated belief.
- When a stakeholder changes the brief and old assumptions may no longer hold.
- When a prototype test, an audit, or an interview produces an unexpected result — that's new evidence, and the map needs updating.
- After any major evidence pass (research synthesis, desk research round, current-state audit) — this is where confirmed/unconfirmed status actually changes.
- Avoid treating it as a one-time worksheet: it's a living document that should be revisited every time new evidence arrives, not rebuilt from scratch each project.

---

## How It Works

### Step 1 — Name every assumption, in a testable format

Sort each belief into one of four types:

| Type | What it covers | Example | Risk if wrong |
|---|---|---|---|
| **User** | Who users are, what they care about, how they behave | "Users check this feature at least once a week." | The product is optimised for a usage pattern that doesn't exist. |
| **Problem** | The nature, severity, and prevalence of the problem | "Users struggle because there are too many options." | The solution doesn't reduce friction because friction wasn't coming from the options. |
| **Solution** | Whether the proposed fix actually addresses the problem | "A comparison table will help users choose faster." | The fix adds cognitive load instead of reducing it. |
| **Business** | Market viability, pricing, regulatory factors | "Users will pay for this if bundled with the existing plan." | The business model doesn't hold, regardless of UX quality. |

Write each one in this formula so it becomes a hypothesis, not an opinion:

> *"We believe [WHO] will [WHAT] because [WHY]. We'll know we're right when [SIGNAL]."*

**Weak:** "We think users want a faster checkout."
**Strong:** "We believe returning customers will use one-click checkout in over 40% of sessions because reducing checkout steps was the top complaint in last quarter's NPS. We'll know we're right when post-launch checkout completion exceeds 80%."

### Step 2 — Plot on the Importance × Evidence matrix

Two axes:

- **Importance (vertical):** How critical is this assumption to the project's success? If it's wrong, does everything fall apart?
- **Evidence (horizontal):** How much proof do we currently have that it's true — from any source?

| Quadrant | Meaning | Action |
|---|---|---|
| High importance · Low evidence (top-left) | Matters most, known least | **Test first** — this is where the next audit, interview, or desk research pass should point |
| High importance · High evidence (top-right) | Validated | **Proceed** — revisit only if scope changes significantly |
| Low importance · Low evidence (bottom-left) | Unproven but low-stakes | **Monitor** — not worth testing yet |
| Low importance · High evidence (bottom-right) | Known, low-risk | **File** — move on |

### Step 3 — Target your evidence-gathering at the top-left quadrant

Don't run an open-ended audit, interview round, or competitor scan. Pick the top 3–5 assumptions in the top-left quadrant and design the evidence-gathering activity specifically to test them. This is what keeps an audit "specific and grounded" instead of a generic list of complaints — every finding should trace back to an assumption it confirms, breaks, or complicates.

### Step 4 — Update the map, every time

After any evidence pass, revisit each tested assumption:

- Move it to **Confirmed** if the evidence supports it — note the source.
- Keep it **Unconfirmed** but update the confidence note if evidence is partial or mixed.
- Add new entries to **Unknown** if the evidence surfaced a belief nobody had named yet.

This is the step most teams skip. The map's value comes from being current, not from being built once.

---

## Example

**Scenario:** A designer auditing an internal enterprise tool's document upload flow.

**Applied:**

| Step | Input | Output |
|------|-------|--------|
| 1. Name it | Raw belief from the team: "Users get confused by the upload flow" | Formatted: "We believe first-time users will abandon document upload because the file format requirements aren't shown until after a failed attempt. We'll know we're right when re-upload rate exceeds 30%." |
| 2. Plot it | Team rates this high importance (blocks a core task), currently no direct evidence | Top-left quadrant — test first |
| 3. Target evidence | Heuristic audit run specifically on the upload flow, checking error prevention and visibility of system status | Audit finds format requirements only appear after the error state on 3 of 4 upload points |
| 4. Update the map | Audit evidence gathered | Moved to Confirmed — source: heuristic audit, dated; feeds directly into the redesign brief |

---

## Common Mistakes

1. **Building the map once and never returning to it.** An Assumption Map that isn't updated after every research, audit, or desk research pass is just a snapshot of day-one opinions — not a decision-making tool.
2. **Writing assumptions as vague opinions instead of testable claims.** "We think users find this confusing" can't be confirmed or broken. The WHO/WHAT/WHY/SIGNAL formula forces specificity.
3. **Running evidence-gathering activities without checking the map first.** An audit or interview round that isn't aimed at the top-left quadrant produces a list of miscellaneous findings instead of answers to the questions that actually matter.

---

## AI in Practice

### 🤖 Try this with AI

> *"I'm working on [project]. Here's my raw list of assumptions: [paste]. Sort them into the four types — user, problem, solution, business — and rewrite each one using this formula: 'We believe [WHO] will [WHAT] because [WHY]. We'll know we're right when [SIGNAL].'"*

Use AI to accelerate the formatting pass. Do the importance/evidence rating and quadrant placement yourself — that judgment call is what makes the map useful, and it depends on context the AI doesn't have.

### 🧠 Critical thinking prompt

- Which assumptions did AI format in a way that sounds confident but is actually still a guess dressed as a hypothesis?
- Where did AI miss a business or regulatory assumption that only someone inside the project would know to name?

### ✍️ Prompt engineering tip

Keep this as a living file (`assumption-map.md`) in your project folder rather than a one-time chat output. After every evidence pass, paste in what you found and ask AI to draft the updated status for each affected row — then confirm or correct the placement yourself before saving.

### ⚖️ Ethics consideration

Don't let AI's confident tone substitute for actual evidence. A well-formatted assumption is still just an assumption until something outside the chat window confirms it.

---

## Further Resources

- **Assumption Mapping (Strategyzer):** https://www.strategyzer.com/ — Original framework for testing business and product assumptions
- **Jobs-to-Be-Done:** https://jobs-to-be-done.com/ — Background reading on separating functional, emotional, and social assumptions about users

---

*Created by Winnie Nguyen · Last updated August 2026*
