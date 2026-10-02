---
title: "Nielsen's 10 Usability Heuristics"
type: reference             # framework | guide | template | reference
program: both                # ux-class | private-training | both
tags: [heuristic-evaluation, usability, design-review, ux-audit]
level: intermediate
date: 2026-08-22
draft: false
download: ""
source: "https://www.nngroup.com/articles/ten-usability-heuristics/"
---

## What This Is

Jakob Nielsen's 10 general principles for interaction design, first published in 1994 and last reviewed by NN/g in January 2024. They're called "heuristics" because they're broad rules of thumb, not prescriptive guidelines — use them to structure a heuristic evaluation or as a quick cross-check during any design review or UX audit. Not original to this vault — kept here for reference, not teaching.

---

## The 10 Heuristics

### 1. Visibility of System Status

The design should always keep users informed about what is going on, through appropriate feedback within a reasonable amount of time.

*Check for:* loading indicators, confirmation after actions, current location/progress markers, real-time validation.

### 2. Match Between the System and the Real World

The design should speak the users' language. Use words, phrases, and concepts familiar to the user, rather than internal jargon. Follow real-world conventions, making information appear in a natural and logical order.

*Check for:* terminology that matches user vocabulary (not internal/system naming), logical field and content ordering, familiar icons and metaphors.

### 3. User Control and Freedom

Users often perform actions by mistake. They need a clearly marked "emergency exit" to leave the unwanted action without having to go through an extended process.

*Check for:* undo/redo, cancel options, back navigation that actually works, no forced multi-step commitment to exit a flow.

### 4. Consistency and Standards

Users should not have to wonder whether different words, situations, or actions mean the same thing. Follow platform and industry conventions.

*Check for:* consistent terminology/icons/patterns within the product (internal consistency) and against platform norms (external consistency).

### 5. Error Prevention

Good error messages are important, but the best designs carefully prevent problems from occurring in the first place. Either eliminate error-prone conditions, or check for them and present users with a confirmation option before they commit to the action.

*Check for:* constraints on invalid input, confirmation before destructive/irreversible actions, disabled states that prevent premature submission.

### 6. Recognition Rather than Recall

Minimize the user's memory load by making elements, actions, and options visible. The user should not have to remember information from one part of the interface to another. Information required to use the design should be visible or easily retrievable when needed.

*Check for:* visible field labels, persistent context (e.g. summaries, breadcrumbs), no reliance on users remembering values from an earlier screen.

### 7. Flexibility and Efficiency of Use

Shortcuts — hidden from novice users — may speed up the interaction for the expert user so that the design can cater to both inexperienced and experienced users. Allow users to tailor frequent actions.

*Check for:* keyboard shortcuts, saved presets/defaults, bulk actions, ability to skip steps for repeat users.

### 8. Aesthetic and Minimalist Design

Interfaces should not contain information that is irrelevant or rarely needed. Every extra unit of information competes with the relevant units of information and diminishes their relative visibility.

*Check for:* visual clutter, competing calls to action, content that doesn't serve the current task.

### 9. Help Users Recognize, Diagnose, and Recover from Errors

Error messages should be expressed in plain language (no error codes), precisely indicate the problem, and constructively suggest a solution.

*Check for:* jargon-free error copy, specificity about what went wrong, a clear next step — not just "something went wrong."

### 10. Help and Documentation

It's best if the system doesn't need any additional explanation. However, it may be necessary to provide documentation to help users understand how to complete their tasks.

*Check for:* contextual help at point of need, searchable/task-focused documentation (not a wall of text users must memorize upfront).

---

## How to Use This in a Review

Run each screen or flow against all 10 — don't stop at the first violation found. Rate severity using the [Severity Rating Scale](./framework-severity-rating-scale.md) so findings can be prioritized rather than listed flat. Pair with the Assumption Map framework when a violation ties back to an untested belief about users.

---

## Further Resources

- **Source:** [10 Usability Heuristics for User Interface Design (NN/g)](https://www.nngroup.com/articles/ten-usability-heuristics/)
- **Pairs with:** [Severity Rating Scale](./framework-severity-rating-scale.md) — use it to score what this checklist surfaces

---

*Source: Jakob Nielsen, NN/g · Compiled August 2026*
