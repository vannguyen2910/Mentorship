---
description: Prepare the next mentoring session: one-page prep from the last recap, open homework, coaching plan and lesson, plus a gap check for lesson and slides
argument-hint: <mentee> [session number or date]
---

Prepare a session: $ARGUMENTS

Output is a private one-page prep note. This command reads and drafts only. It does not send messages, change the calendar, or build lessons or slides. Read `_system/rules/VI_VOICE.md` before writing any Vietnamese.

**Language and skills:** write the prep note in Vietnamese (decided 2026-10-11): body text in Vietnamese, section headings and professional terms in English, file names and front matter keys in English. Apply the Vietnamese skills in this order:

1. `vietnamese-voice-dictionary`: on the user's own words when they look like speech-to-text errors. Ask once if a word is ambiguous.
2. `vi-voice`: load before drafting, and follow `_system/rules/VI_VOICE.md`.
3. `vietnamese-copy-polish`: on the optional Zalo reminder and the Calendar description (texts others read). On the prep note itself use it as a check only: diacritics, sentence length, filler, dashes. Do not restructure the note.


## 1. Identify the session

Work out the mentee and the session number (default: the next number after the last row in `mentees/<slug>/sessions.md`, or the first planned row if none are logged). If the user gave no date, check Google Calendar (list_events for the next 14 days, search the mentee's name) for the upcoming slot. If the calendar is unavailable or has no match, leave the date as "to confirm". Do not invent a date.

## 2. Read what exists (skip silently what is missing, but list it under Gaps)

- `mentees/<slug>/mentee.md`: programme, sessions, cadence, goal, project, lesson mapping (`lessons:`)
- `mentees/<slug>/plan/`: the coaching plan, for what this session is supposed to move forward
- `mentees/<slug>/sessions.md` and the most recent file in `mentees/<slug>/sessions/`: last recap, its Commitments & Next Steps, and its Next Session Plan seed
- `mentees/<slug>/homework/`: anything submitted since the last session
- `mentees/<slug>/assessment.md`: baseline numbers, for steering focus (do not quote scores in anything the mentee sees)
- the matching lesson in `library/lessons/**/<slug>/materials/<slug>-lesson.md`, and a deck in `mentees/<slug>/slides/` named `Session N - ...` or one under the lesson's `slides/`

## 3. Write the prep note

Save to `mentees/<slug>/sessions/prep-NN-YYYY-MM-DD.md` (private, `draft: true`). Keep it to one page:

1. **Where they are**: 3 to 4 lines. Programme position, what changed since the last session, mood or energy if the recap says.
2. **Open items**: homework due and whether it was submitted, commitments from last time, with status (done, not done, unknown).
3. **Goal of this session**: one sentence, taken from the coaching plan and the lesson, not invented.
4. **Proposed agenda**: timed blocks that add up to the session length in `cadence`. Reuse the lesson's own phases and timings. Add a 10 minute check-in on homework at the start unless the plan says otherwise.
5. **Questions to ask**: 3 to 5, aimed at the blockers and patterns in the last recap.
6. **Things to watch**: from the recap's trainer notes and assessment gaps. Candid wording is fine here, since the note is private.
7. **Gaps**: lesson file missing or still `draft: true`, slides missing, homework not submitted, no recap, no baseline, no date.

## 4. Gap handling (WF-5)

If the lesson or slides are missing or incomplete, do not build them. List exactly what is missing and offer `/build-lesson` (which starts with a content brief for approval). If the mentee's project is the vehicle for the lesson, suggest one concrete way to apply it to their project.

## 5. Report

Show the agenda and gaps in chat, with the path of the prep note. Offer, but do not do without a yes:

- a short Zalo reminder draft in Vietnamese for the mentee (time, what to bring, homework to have ready)
- a Calendar description with the agenda and the lesson or deck link
