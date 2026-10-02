# AI Prototype Development — Learning Folder Index

Two layers live here: the standalone method lesson, and the private-training arc built on top of it.

## Source lesson (standalone — also used by Online Course sections 2-6)

| File | What it is | Status |
|---|---|---|
| `ai-prototype-development-lesson.md` | "Build the Pattern First" — canonical method: AI foundations, mindset reframe, component inventory, interaction pattern, build/edit prompts, stitching | Complete |
| `ai-prototype-development-slide-outline.md` | Paired slide outline for the above | Complete |

## Private-training arc (4 lessons, 1:1, weekly)

| File | What it is | Status |
|---|---|---|
| `lesson-0-program-introduction.md` | Orientation — delivered before/at the start of Session 1, not a session itself | Drafted |
| `lesson-1-project-setup-pattern-first-method.md` + `lesson-1-slide-outline.md` | Lesson 1: project folder setup, naming the Design Pattern (tokens, component inventory, template) | Drafted |
| `lesson-2-interaction-pattern-build-editing-craft.md` + `lesson-2-slide-outline.md` | Lesson 2 “Build Your Design System”: Pre-Flight cleanup, scope, setup check, token sync, component inventory, templates into code, consolidation into `design-system.html`, interaction pattern | **Built** — outline reverse-synced from the live deck |
| `lesson-3-scaling-the-prototype.md` + `lesson-3-slide-outline.md` | Lesson 3 “Scaling the Prototype” (cover fronts the lesson title, not a tagline): set the rules before prompting, three ways to feed the AI a user flow, build the whole journey in one prompt, review it with the three edit modes plus the layer ladder, rewrite the rules from that review, propagate a system change, scope and build a second journey, stitch and walk it note-and-move-on | **Drafted** — lesson file is canonical until a deck is built |
| `lesson-3-4-stub.md` | Objectives-only stub for **Lesson 4 only** — Lesson 3 split out on 2026-09-19. Filename now stale | Stub |

**Note (2026-09-18):** Pre-Flight cleanup, token sync, and component-inventory generation moved from Lesson 1 to Lesson 2 to match the actual delivered Lesson 1 deck — see the scope-reconciliation notes in both lesson files.

**Note (2026-09-19):** Lesson 2 is now built. Its outline was reverse-synced from `standalone program/Lesson 2 - Build It standalone.html`, which ends at the interaction pattern — so building screens, the three edit modes and the second-tool comparison have been removed from Lesson 2 and belong to Lesson 3. Lesson 2's filename is now stale (it still says `interaction-pattern-build-editing-craft`); rename it together with `lesson_file` in the outline and this table. One more open knock-on: Lesson 1's "Design It in Figma" produces a single template, while Lesson 2 now expects one per pattern type.

**Note (2026-09-19, later):** Lesson 3 is drafted and split out of the stub into its own pair, same pattern as Lessons 1 and 2. Lesson 2's known deck mismatches are now **fixed in the built deck** (Closing checklist, Cover speaker notes and subtitle, plus a third — a “five build ingredients coming up” clause that now points at Lesson 3); its outline records what was wrong rather than deleting it. Lesson 2's `next-session` and the title in this table now read “Lesson 3: Scaling the Prototype.” The second-tool comparison has been removed from the programme and Huy's coaching plan updated in five places.

**Note (2026-09-20):** Lesson 3 retitled to “Scaling the Prototype” and its lesson file renamed to `lesson-3-scaling-the-prototype.md` in the same pass; the six cross-references were updated with it. Its slide outline also went from 20 to 30 slides by splitting slides that carried two ideas — see the note at the top of that file for what to re-merge if it ever needs to come back down. The cover slide now fronts “Scaling the Prototype” rather than a separate tagline — a deliberate break from Lessons 1 and 2, recorded in both Lesson 3 files and in the Lesson 4 stub’s cover-title guidance.

**Note (2026-09-20, later):** Lesson 3's spine was reworked to match how Winnie actually works. The earlier version taught rule *harvesting* — build one screen slowly, mine its corrections for rules, then build the rest. The real workflow is the reverse: **set the rules first, feed the AI an existing user flow, and build the whole journey in one prompt.** Both Lesson 3 files were rewritten around that; Sections 3 and 4 of the outline (journeys, stitching) are unchanged. Three consequences worth knowing: the lesson now **deliberately departs from the source lesson's “one screen at a time”** (Phase 4 Step 6) and says so in the body; the review segment grew to 15 minutes and is the longest in the session, because one prompt produces one large pile of corrections; and a new slide (9, “These rules aren’t yours yet”) states openly that the starter rules are handed over rather than earned, with slide 16 as the place the student rewrites them. If a deck ever gets built from an older copy of the outline, the tell is a Section 1 called “The Expensive First Screen.” **Separately, Lesson 3's speaker notes changed from connected sentences to short scannable bullets**, at Winnie's request, for reading at a glance while teaching — bold marks what to say aloud, the rest is a cue. Lessons 1 and 2 still use connected sentences, so the three outlines now diverge on this; convert them the same way or accept the split deliberately.

**Open, recorded not fixed:** two stale filenames — `lesson-2-interaction-pattern-build-editing-craft.md` and `lesson-3-4-stub.md` (now Lesson 4 only). Each rename touches this table plus a `lesson_file` or frontmatter reference; do them in one pass. Lesson 1's “Design It in Figma” still produces a single template where Lesson 2 expects one per pattern type.

**Next:** build Lesson 3's deck from `lesson-3-slide-outline.md`, then reverse-sync that outline from the built deck the way Lesson 2's was. Then draft Lesson 4 into its own pair — note it now opens with the presentation coaching moved out of Lesson 3, which makes it the tightest session in the arc.

---

*Index — not lesson content. See `CLAUDE.md` at the project root for the lesson/slide-outline sync rule these pairs follow.*
