---
title: "Severity Rating Scale for Usability Problems"
type: reference             # framework | guide | template | reference
program: both                # ux-class | private-training | both
tags: [severity-rating, usability, design-review, ux-audit, prioritization]
level: intermediate
date: 2026-08-22
draft: false
download: ""
source: "https://www.nngroup.com/articles/how-to-rate-the-severity-of-usability-problems/"
---

## What This Is

Jakob Nielsen's method for scoring how bad a usability problem is, so a list of findings can be prioritized instead of just listed. It's a companion to [Nielsen's 10 Usability Heuristics](./framework-nielsen-usability-heuristics.md), but it isn't specific to heuristic evaluation — use it to rate any usability problem, however you found it: heuristic review, usability testing, analytics, support tickets.

---

## The Scale

| Score | Label | Meaning |
|---|---|---|
| 0 | Not a problem | Don't agree this is a usability issue at all |
| 1 | Cosmetic | Fix only if there's spare time on the project |
| 2 | Minor | Low priority |
| 3 | Major | Important — high priority |
| 4 | Catastrophe | Must fix before release |

In practice, findings scored 0 usually don't get logged as findings at all — the scale starts doing work at 1.

---

## The Four Factors Behind the Number

A severity score isn't a gut call — it's four factors combined into one:

1. **Frequency** — Is this common or rare? Something every user hits every session outweighs an edge case.
2. **Impact** — When it happens, how hard is it for the user to recover or work around it?
3. **Persistence** — Is it a one-time confusion (annoying once, then learned) or does it keep costing the user every time?
4. **Market impact** — Even if it's technically easy to work around, does it damage trust, adoption, or perception of quality?

You don't score each factor separately and average them — you weigh them together and land on one number. The point of a single score is to make prioritization fast, not to produce a precise measurement.

---

## How to Use This in a Review

For every finding from a heuristic evaluation (or any other audit method), ask: how often does this happen, how bad is it when it does, does it wear off or keep biting, and does it move the needle on how the product is perceived. Land on 1–4. Then sort your findings by score before you write up the report — the catastrophe- and major-rated issues go first, regardless of which heuristic they came from or the order you found them in.

**Worked example:** A delete-document button fires immediately with no confirmation (Error Prevention violation).

- Frequency: happens every time someone misclicks — plausible weekly for high-volume users
- Impact: no undo, so the document is genuinely gone — high
- Persistence: not a learning curve issue, it can bite an experienced user just as easily
- Market impact: data loss is the kind of bug that gets escalated and erodes trust fast

→ Score: **4 — Catastrophe**

---

## Further Resources

- **Source:** [How to Rate the Severity of Usability Problems (NN/g)](https://www.nngroup.com/articles/how-to-rate-the-severity-of-usability-problems/)
- **Pairs with:** [Nielsen's 10 Usability Heuristics](./framework-nielsen-usability-heuristics.md) — use this scale to score what that checklist surfaces

---

*Source: Jakob Nielsen, NN/g · Compiled August 2026*
