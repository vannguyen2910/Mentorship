---
description: Close out a private-training programme: baseline vs reassessment, close-out recap, assessment table, testimonial capture, training log, and follow-up drafts. Drafts for review, sends and publishes nothing
argument-hint: <mentee> [reassessment results: paste numbers or name the file]
---

Close out a programme: $ARGUMENTS

Everything below is a draft until the user approves it. Nothing is sent or published. Chat in Vietnamese; read `_system/rules/VI_VOICE.md` before writing any Vietnamese. Follow the "Programme kickoff & close-out rule" and the testimonial capture rule in CLAUDE.md.

**Language and skills:** write the close-out recap and every draft in Vietnamese (decided 2026-10-11): body text in Vietnamese, section headings and professional terms in English, file names and front matter keys in English. Apply the Vietnamese skills in this order:

1. `vietnamese-voice-dictionary`: on the user's own words when they look like speech-to-text errors, including pasted reassessment notes. Ask once if a word is ambiguous.
2. `vietnamese-transcript-cleaner`: on the final session's transcript if it is raw.
3. `vi-voice`: load before drafting the recap and the follow-up drafts.
4. `vietnamese-copy-polish`: last, on the three follow-up drafts (thank-you, testimonial request, check-in), which the mentee reads. On the recap use it as a check only.


## 1. Confirm this is the final session

Read `mentees/<slug>/mentee.md` (planned `sessions`, `start`, `status`), `sessions.md` and the latest recap. If the logged sessions do not reach the planned count, say so and ask once whether the user wants to close out early. If the final session has not been logged, run the `/log-session` flow first (transcript, playback, recap), then continue here.

## 2. Collect baseline and reassessment

**Baseline** (never skip, never invent). Look in this order:
1. `mentees/<slug>/assessment.md`, Baseline column
2. `mentees/<slug>/assessments/` (a baseline file or the tool's PDF)
3. the coaching plan's "Baseline Assessment" section in `mentees/<slug>/plan/`

**Reassessment:** the user ran the self-assessment tool (`programs/assessment-tool/student-design-assessment.html`) with the mentee. Take the results from what the user pastes, or from a file in `assessments/`. If neither exists, stop and ask for the numbers. Do not estimate them.

If no baseline exists anywhere, flag it explicitly: the comparison table cannot show movement, and the close-out will say "baseline not on file" in those cells. Offer the honest alternative (compare against the coaching plan's stated starting point and the first recap's observations), clearly labelled as qualitative.

Metrics to capture, numbers only: date taken, target level, career readiness %, designer profile, craft %, behaviour %, AI readiness, skills at or above target.

## 3. Gather the growth evidence

Read every recap in `mentees/<slug>/sessions/` and the coaching plan's "How Success Looks Like" table. Build, privately:

- **Observed change:** specific behaviours that differ from Session 1, each with the session it appeared in. Prefer observed behaviour over a rating delta (the close-out template says so).
- **Success markers:** each marker from the plan as met, partly met, or not yet, with one line of evidence. Mark `[to confirm]` where the recaps give no evidence.
- **What did not move:** areas still "Developing", taken from the reassessment, not from your impression.

## 4. Write the close-out recap

Use `_system/learning templates/_template-programme-closeout.md`, not the plain session template. If `mentee.py log` already created a recap file for the final session, fill that file in place instead of creating a second one. Save as `mentees/<slug>/sessions/session-NN-<topic>.md` with `draft: true`. Fill every section: Baseline vs Reassessment (with the Change column), What moved and why (2 to 3 sentences, observed behaviour first), Key Observations, Feedback Given, Commitments & Next Steps (tied to what is still "Developing"), My Notes as Trainer. Candid wording is allowed here because the file is private.

## 5. Update the public-facing source files (numbers only)

- `mentees/<slug>/assessment.md`: fill the Post-training column. Numbers and labels only. No notes, no commentary, because this table is published on the mentee's page. If the Baseline column is blank, leave it blank and say so.
- `mentees/<slug>/mentee.md`: set `status: "completed"` and `end: YYYY-MM-DD`.

Show both edits to the user before saving them.

## 6. Testimonial capture (same response)

If the mentee said anything about Winnie's teaching in this session or in the transcript, add it to `showcase/testimonials.md` in the format at the top of that file (permission: not yet confirmed unless the user says otherwise), and add it to the close-out recap's My Notes as Trainer so both stay in sync. Tell the user it was added.

If no testimonial surfaced, say so in one line. Offer a draft request (step 8) instead of inventing a quote.

## 7. Training log

Append an entry to `mentees/training-log.md` using its entry template: type `private-training`, participants `1`, duration from `start` to `end`, topics from `sessions.md`, one short note. Do not edit `business/profile/pitch-deck-content.md`. Instead print the one stat line that would change (for example the session count) and ask the user whether to apply it.

## 8. Follow-up drafts (Vietnamese, per VI_VOICE.md; the user sends them)

Save under `## Follow-up drafts` in the close-out recap:

- **Thank-you and next steps:** 3 sentences on the growth in the mentee's own terms, the 2 or 3 things to keep practising, and an open door.
- **Testimonial request:** short, non-leading, makes it easy to say no, says what it would be used for and asks for permission separately. Never suggest wording of the testimonial.
- **Check-in:** propose a light follow-up 4 to 6 weeks out, as a suggestion with no date promised.

## 9. Reusable material (WF-2)

List up to 3 ideas from the programme that could become class material, described generically with no names. Do not adapt them without a yes.

## 10. Rebuild and report

Run `python3 _system/scripts/build-home.py` (site rebuild rule), then report:

- baseline vs reassessment table (3 to 5 rows), or the explicit "baseline not on file" flag
- what moved, in two sentences
- files changed, with paths
- items waiting on the user: approve the assessment edits, send the three drafts, confirm testimonial permission, decide on the pitch deck stat
- anything still `[to confirm]`
