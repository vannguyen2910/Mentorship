---
title: "Track 3 · Roadmap to Senior/Lead: Build Status"
type: reference
program: private-training
level: senior-lead
date: 2026-08-29
draft: false
---

# Track 3 · Roadmap to Senior/Lead: Build Status

The curriculum for this track is defined in `business/services/service-catalog.md`. This file maps that definition against what actually exists in the library, so the gap is visible without opening eight folders.

**Positioning (from the catalog):** from strong executor to strategic partner. Mid-level designers, 3 to 6+ years, capable in craft but stalling at promotion because research leadership, strategic communication or influence are not there yet. Eight sessions, 90 minutes each, biweekly over three months, anchored to the student's own live project throughout.

---

## The eight sessions, and what exists

| # | Session | Lesson file | Slide outline | Status |
|---|---|---|---|---|
| 1 | Mastery Design Process | none | none | ❌ Not built. No file exists anywhere in the library; Desk Research now follows Evaluate Current Experience (seniors may skip it via the fast-track) |
| 2 | Desk Research | `01-discover/desk-research/materials/` | ✅ | ✅ Ready. Level `mixed` |
| 3 | Understand Customer | `01-discover/customer-understanding/materials/customer-understanding-senior-lesson.md` | ✅ | ✅ Ready. Senior/Lead |
| 4 | Problem Definition & Strategy | `02-define/problem-definition-strategy/materials/` | ✅ | ✅ Ready. Senior/Lead. Built Aug 2026 |
| 5 | System Architecture & IA | `03-develop/information-architecture/learning/` exists at class level only | class version only | ⚠️ No senior version. The class lesson does not cover defending IA decisions with evidence, which is the senior half of the catalog description |
| 6 | Design | `03-develop/design-system/materials/` exists at class level only | class version only | ⚠️ No senior version. Atomic Design at intermediate level, not evidence-based design decisions |
| 7 | AI Prototyping | `programs/online-course/AI Prototype Development` plus `00-foundation/ai-workflow-for-ux-designers/` | ✅ | ✅ Reuses existing material by design, per the catalog |
| 8 | Validation & Iteration | `04-deliver/solution-validation-user-testing/learning/` exists at class level only | class version only | ⚠️ No senior version. Missing the prioritisation and measurement half the catalog names |

**Summary:** three of eight sessions are built at senior level (2, 3, 4), one reuses existing material as intended (7), one has never been built at all (1), and three run on class-level lessons that do not cover the senior content the catalog promises (5, 6, 8).

---

## The spine that is built

Sessions 2 to 4 now run as one continuous chain with no blank pages between them:

`assumption-map.md` → `jtbd-map.md` → `opportunity-map.md` → `problem-brief.md`

Each session extends the previous session's file rather than starting a new artefact, and each hands a named input to the next. That chain is the strongest thing about the built portion of this track, and it is the thing sessions 5, 6 and 8 would need to continue if they get senior versions. Session 8's catalog description already anticipates it: "measuring against Session 4's success criteria" is a direct reference to the measure written into `problem-brief.md`.

---

## Two discrepancies to resolve

**1 · Session 4 and the target-state vision.** The catalog describes session 4 as "synthesis into a testable problem statement + target-state vision." The lesson as built delivers the problem statement, a guiding policy, coherent actions, non-goals and a success measure. That is a strategy, and arguably a stronger artefact than a vision, but it is not a target-state vision and the two are not the same thing: a vision describes the future state, a strategy describes the approach for getting there. Either the catalog line gets updated to match what the session teaches, or a vision component gets added and something else comes out to make room. The lesson is currently at 85 minutes in a 90 minute slot.

**2 · Materials status in the catalog.** Track 3 is described as "fully proven and now generalized into a reusable template." Given that four of the eight sessions have no senior-level lesson, that line is ahead of the library. Worth correcting before it goes in front of a prospective student, since it is the sentence that sets their expectation of what they are buying.

---

## What to build next, in order

1. **Session 1, Mastery Design Process.** It is the only session with nothing at all, it is the first thing a student meets, and it is where the process charter and the initial assumptions map come from, which sessions 2 and 3 both depend on. Everything downstream currently starts from an artefact nobody has been taught to make.
2. **Session 5, System Architecture & IA at senior level.** It is the session immediately after the newest one, so the chain breaks there next. The senior content is defending IA decisions against evidence, which pairs naturally with the problem brief.
3. **Session 8, Validation & Iteration at senior level.** It closes the loop back to the success measure written in session 4, and without it the measure never gets evaluated, which is the exact failure the session warns about.
4. **Session 6, Design at senior level.** The class Atomic Design lesson carries more of the load here than the other two class lessons do, so this is the least urgent of the three.

`leader-level/` holds two further sessions, `change-management` and `estimating-design-effort`, which sit outside this eight-session arc as a separate tier. Neither has a finished lesson; `estimating-design-effort` has a completed desk research document and locked scoping, so it is the closest to ready of anything in the library.

---

*Build status · Winnie Nguyen · Last updated August 2026*
