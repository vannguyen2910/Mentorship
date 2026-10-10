---
description: Build a lesson in two gated stages: content brief first (WF-5), then the paired lesson and slide outline in sync, review, and site rebuild. Never builds without an approved brief
argument-hint: <topic or lesson slug> [stage: foundation|discover|define|develop|deliver|leader-level] [for: <mentee or "class">] [level: junior|senior|mixed]
---

Build a lesson: $ARGUMENTS

This command has two stages with a hard gate between them. Stage A produces a brief and stops. Stage B runs only after the user approves the brief in chat. Never skip the gate, even when the request looks small (Rule WF-5). Chat with the user in Vietnamese.

## Language (decided 2026-10-11)

New lessons are written in **Vietnamese**. Existing lessons written in English stay as they are until the user asks for a rewrite.

- **Vietnamese:** the brief, the lesson body, the slide outline's on-slide text and speaker notes, activity instructions, homework text.
- **English:** file and folder names, slugs, front matter keys and tags (WF-4), section headings and slide titles/kickers (VI_VOICE rule 1), and professional terms kept in English per VI_VOICE rule 4.
- **Skills to use, in this order:**
  1. `vi-voice`: load before drafting anything. It sets voice, term list and phrases to avoid. Where it conflicts with the writing style guide, VI_VOICE.md wins.
  2. `vietnamese-voice-dictionary`: when the user's own words (a brief, a correction, a note) look like speech-to-text errors, resolve them with it before using them. Ask once if a word is ambiguous.
  3. `vietnamese-transcript-cleaner`: when the source material in A1 is a raw transcript or caption file.
  4. `vietnamese-copy-polish`: after drafting, run it over the on-slide text and any text a learner reads: missing diacritics, long sentences, filler, en and em dashes, weak hooks. It is a final check, not a rewrite of the teaching content.

## Stage A: Brief (always first)

### A1. Find what already exists

1. Search `library/lessons/**/materials/` and `library/frameworks/` and `library/guides/` for the topic. If a lesson already exists, this is an update, not a new lesson: say so, list what exists (lesson, outline, deck, `draft` status, last sync date) and propose only the delta.
2. Read the neighbours: the lesson before and after in the programme (`previous-session`, `next-session` front matter, the relevant `programs/*/README.md` or coaching plan), so the handoffs are real.
3. Look in `source/` and `_inbox/` for raw material on the topic (WF-1, WF-6). Do not move anything.
4. If the lesson is for one mentee, read their `mentee.md`, plan and latest recap for context. That context shapes the examples, but it must not appear by name in the lesson (see CLAUDE.md, General lesson conventions). Apply WF-2 if the idea came from a private session: generalise, and record `source: adapted-from-private-session` in front matter.

### A2. Ground the content

Teach what is in the user's own material first. Where the lesson needs a claim, a statistic or a method that is not in their files, find a source (use web search) and record it with author, year and sample size. Do not state a number without a source. Separate what a source found from what the author infers. Where something is Winnie's own teaching method, mark it as such and do not invent supporting research.

### A3. Write the brief

Save to `library/lessons/<stage>/<slug>/materials/<slug>-brief.md` (create the lesson folder only if the user has confirmed the stage and slug; ask once if either is unclear, offering 2 or 3 options with a recommendation, per WF-3). Use exactly:

```markdown
---
title: ""
type: lesson
audience: ux-class | private-training
level: beginner | intermediate | advanced
duration: "90 min"
---

## Purpose
One sentence: what the learner can do after this session that they could not before.

## Structure
1. Block name, minutes: what it covers (one line each)
...
(timings sum to the duration with a stated buffer)

## Learning objectives
3 to 5, each starting with a Bloom verb and observable.

## Key decisions
- Running example and why
- Where AI appears and where it does not (manual before AI)
- What is cut, and what is deferred to another lesson
- Open questions for Winnie
```

Also list, in the brief, the sources found in A2 and anything marked `[to confirm]`.

### A4. Gate

Show the brief in chat and stop. Do not create the lesson, the outline or a deck. The user replies "looks good" or edits inline and says "build it". Anything less than a clear yes is not approval.

## Stage B: Build (only after approval)

### B1. Scaffold

Create `library/lessons/<stage>/<slug>/{materials,slides,assets,_archive}` if missing. Start from `_system/learning templates/_template-lesson.md` and `_system/learning templates/_template-slide-outline.md`, not a blank page. Front matter: `draft: true`, tags only from the WF-4 vocabulary (2 to 5, one audience, one level), `program`, `level`, `duration`, `previous-session`, `next-session`.

### B2. Write the lesson (`<slug>-lesson.md`, source of truth)

Follow the structure the existing lessons use (Overview, Learning Objectives, Success Check, Materials Needed, Pre-Class Preparation, Session Plan, Core Content, Activities, AI in Practice, Assessment, Further Resources). Rules that always apply:

- **Vietnamese paper style:** objective, third person, no "bạn" or "mình" in the lesson file (speaker notes in the outline use "mình"), no imperatives, a Limitations note, numbered references [n] for every figure (VI_VOICE.md). Sources can stay in their original language; the claim is written in Vietnamese.
- **No spoken filler and no translated-sounding phrases:** check the "Bỏ khỏi văn bản chính thức" and "Cụm dịch từ tiếng Anh cần tránh" tables in VI_VOICE.md before saving.
- **No tool names:** write "AI chat tool", "AI coding tool", "your AI tool". Never introduce Claude, ChatGPT, Cursor, Copilot or similar.
- **No mentee or student names**, no cohort or identifying detail.
- **Manual before AI:** the learner does the thinking before AI helps. AI assists, the learner decides.
- **AI in Practice** section is mandatory (LP-4): a try-this prompt, a critical-thinking prompt, a prompt tip, an ethics note.
- Timings sum to the stated duration, with the buffer written down.
- Anything uncertain stays marked `[to confirm]`; do not smooth it over.

### B3. Write the slide outline (`<slug>-slide-outline.md`) in the same response

Apply the sync rule in CLAUDE.md: both files are written together and never left out of sync. Use the layout catalogue in `_system/rules/SLIDE_DECK_RULES.md`. Never invent a layout type. Every slide has the standard fields (Kicker, Title, On-slide, Speaker notes as 3 to 6 bullets, Visual hint). The COVER slide follows the locked block in the template. Update the slide count in the `## Slide structure` line and the MILESTONE `Num:` values to match the lesson's phase timings.

### B4. Review before reporting

Run the `review-mentoring` skill's checks on the pair, or apply its checklist inline: objectives match activities, timings sum, handoffs from and to neighbouring lessons are consistent, outline matches lesson, QA-2 checklist (MENTORING_RULES.md). Then run the language pass from the Language section: `vietnamese-copy-polish` on on-slide text, and the VI_VOICE.md tables on the lesson body. Fix what is wrong, and list what you could not fix.
When Winnie corrects a Vietnamese line, add the before and after to `VI_VOICE.md` so the fix applies next time (that rule is in CLAUDE.md).

### B5. Deck

A deck is a separate step. Do not generate deck HTML in this command. State exactly what is needed: the outline path, the slide count, and the nearest existing deck folder to copy support files from (`slides/deck-stage.js` and `slides/tokens.css` live in each lesson's own `slides/` folder; there is no shared theme folder). The built deck, once it exists, goes directly in `slides/` as an `.html` file (not `_archive/`, not nested), per CLAUDE.md.

### B6. Rebuild and report

Run `python3 _system/scripts/build-home.py` (site rebuild rule in CLAUDE.md) and report the lesson card or page line for this lesson. Then report:

- files created or changed, with paths
- the sync check result (lesson vs outline: slide count, timings)
- open `[to confirm]` items and review findings
- what waits on the user: approve to mark `draft: false`, build the deck, add `programs:` line if the programme page needs it, assign it to the mentee's `lessons:` mapping in `mentee.md` when relevant
