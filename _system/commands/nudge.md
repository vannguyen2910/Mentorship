---
description: Weekly follow-up scan: mentees who are overdue, homework not submitted, unlogged sessions, upcoming sessions without prep, and leads awaiting a reply. Drafts the nudges, sends nothing
argument-hint: [all | mentees | leads | <mentee>]
---

Run the follow-up scan: $ARGUMENTS (default: all)

This command reads files and drafts text. It never sends a message, changes a calendar event, edits the lead tracker, or writes outside the files named in step 4. Today's date comes from the system, never from memory.

**Vietnamese skills:** load `vi-voice` and follow `_system/rules/VI_VOICE.md` before drafting any Vietnamese. Run `vietnamese-copy-polish` over every nudge and follow-up draft before saving it (diacritics, sentence length, filler, dashes, one clear next step). Run `vietnamese-voice-dictionary` only on the user's own words when they look like speech-to-text errors; never on a lead's or mentee's words.

## 1. Mentee scan (skip if the argument is `leads`)

For each folder in `mentees/` whose `mentee.md` has `status: "in-progress"` (or just the one named), read `mentee.md`, `sessions.md`, the latest file in `sessions/`, and the contents of `homework/`.

Raise a flag when:

| Flag | Rule |
|---|---|
| **Overdue session** | Days since the last dated row in `sessions.md` exceed the cadence interval (weekly 7, every 2 weeks 14, otherwise ask) plus 3 days of grace, and no future session is on the calendar |
| **Unlogged sessions** | `sessions.md` has no rows or rows with no date, but the mentee has a start date earlier than today. Say which sessions look unlogged. Do not guess what happened |
| **Homework not in** | The latest recap's Commitments & Next Steps lists a task and nothing in `homework/` is newer than that recap |
| **Next session with no prep** | A session with this mentee is on Google Calendar within the next 48 hours and there is no `prep-NN-*.md` for that number |
| **Near the end** | Fewer than 2 sessions remain, and no baseline or close-out plan is on file |
| **No recap after a session** | A transcript exists in `transcripts/` with no matching `session-NN-*.md` recap |

If Google Calendar is not connected, say so once and skip the two calendar-based checks. Do not guess dates.

## 2. Lead scan (skip if the argument is `mentees`)

Find the newest `uxlevelup-lead-tracker*.xlsx` under `business/services/`. State its file name and date in the report, because a backup file is stale by definition. Read the `Pipeline` sheet only. Raise a flag for rows where `Stage` is not Closed, Enrolled or Lost and any of these hold:

- `Follow-up due` is today or earlier
- `Days since` is 5 or more and `Last contacted` is empty
- `Flag` is not empty

Never write to the spreadsheet. The user updates it.

## 3. Draft the nudges

One draft per flag, in Vietnamese unless the contact wrote in English, in Winnie's voice (VI_VOICE.md):

- **Mentee nudge:** warm, short, no guilt. Name the specific thing (one task, one date), make the next step easy, and offer a way out if they are stuck ("nếu đang kẹt ở bước nào, nhắn mình"). Never mention scores or the baseline.
- **Lead follow-up:** acknowledge what they asked about, give one clear next step, no pressure. Use the "Suggested track" and "Enquired about" columns. Do not quote a price in a follow-up: tuition is worked out after the discovery call (see `/lead`). Same voice and proof rules as `/lead`.
- **Prep trigger:** for a session within 48 hours with no prep, do not draft a message. Tell the user to run `/prep <mentee>`.

Mark anything you are unsure of as `[to confirm]`.

## 4. Write the output

- Per mentee with flags: append a `## Nudge YYYY-MM-DD` section to `mentees/<slug>/sessions/nudge-log.md` (create it if missing, `draft: true`, private).
- Leads: write `business/lead-followups-YYYY-MM-DD.md` with one block per lead (who, stage, why flagged, draft reply).
- Do not create any other folder or file.

## 5. Report

Lead with a count, then a table sorted by urgency: who, flag, what to do, where the draft is. Then:

- what could not be checked (calendar, tracker age, missing dates)
- what is waiting on the user: send the Zalo messages, update the tracker, run `/prep` or `/log-session` where flagged

If nothing is flagged, say so in one line. Do not pad the report.
