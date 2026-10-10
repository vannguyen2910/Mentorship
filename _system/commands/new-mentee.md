---
description: Set up a new private-training mentee (folder, mentee.md, sessions.md, coaching plan) so they appear on the site
argument-hint: <full name> [role, programme, sessions, start date, cadence, goal]
---

Set up a new mentee: $ARGUMENTS

1. From the arguments, work out: full name (required), role, level, target level, programme name, number of sessions, start date, cadence, goal, project vehicle, and which programme page they follow (one of: ui-ux-fundamentals, junior-to-mid-level, mid-to-senior, systematic-ai-prototyping). Ask the user once, in one message, for anything essential that is missing (name and programme at minimum). Do not invent values.
2. Run:
   `python3 _system/scripts/mentee.py new "<Full Name>" --role ... --level ... --target ... --program ... --sessions N --programme-page <slug> --start YYYY-MM-DD --cadence ... --goal ... --project ... --build`
   (omit flags you have no value for).
3. Tell the user what was created, then remind them of the mandatory step from CLAUDE.md: run the self-assessment tool (`programs/assessment-tool/student-design-assessment.html`) with the mentee at or before session 1 and save the PDF in `mentees/<slug>/assessments/` and copy the headline numbers (readiness %, profile, craft/behaviour %, AI readiness, target level, date) into the Baseline column of `mentees/<slug>/assessment.md`.
4. Offer to help fill in the coaching plan in `plan/`. Never put the mentee's name in `*-lesson.md` or `*-slide-outline.md` files.
