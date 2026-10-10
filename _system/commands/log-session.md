---
description: Log a mentoring session from a Zoom/Meet transcript (or Notion): sessions.md, public playback, private recap, homework and Zalo drafts, testimonial capture, site rebuild
argument-hint: <mentee> <topic> [date] [transcript path, or paste the transcript after the command]
---

Log a session: $ARGUMENTS

Everything below is a draft until the user approves it. Nothing is sent, posted or published by this command. Read `_system/rules/VI_VOICE.md` before writing any Vietnamese.

**Language and skills:** write private notes and everything the mentee reads in Vietnamese (decided 2026-10-11): body text in Vietnamese, section headings and professional terms in English, file names and front matter keys in English. Apply the Vietnamese skills in this order:

1. `vietnamese-voice-dictionary`: first, on the user's own words in `$ARGUMENTS` and chat when they look like speech-to-text errors. Ask once if a word is ambiguous. Do not run it on the mentee's words in the transcript (the cleaner handles those).
2. `vietnamese-transcript-cleaner`: on any Zoom/Meet transcript or caption file (step 3).
3. `vi-voice`: load before drafting the playback, the recap and the Zalo message, and follow `_system/rules/VI_VOICE.md`.
4. `vietnamese-copy-polish`: last, on the playback and the Zalo message (the two texts the mentee sees): diacritics, sentence length, filler, dashes, a clear next step. On private notes use it as a check only and do not restructure them.


## 1. Identify the session

Work out the mentee, the topic and the date (default today). Ask once if the mentee or topic is unclear. Find the session number from `mentees/<slug>/sessions.md`.

## 2. Get the source material (first match wins)

1. **Transcript file or pasted text** from Zoom or Meet (txt, vtt, srt, docx, or pasted into chat). Copy a file input to `mentees/<slug>/transcripts/session-NN-YYYY-MM-DD.<ext>` (private, never published). If the transcript was pasted, save it there as `.md`.
2. **Notion**: search the page "Coaching Program - <Full Name>" and open the matching session sub-page (notion-search, then notion-fetch).
3. **Neither exists**: ask the user for 3 to 5 bullets and work from those. Do not invent session content.

## 3. Clean and extract (private working notes, from the transcript)

Follow the `vietnamese-transcript-cleaner` conventions (restore diacritics and punctuation, merge broken lines, label speakers). Then pull out:

- topics covered and the mentee's key moments
- decisions made and what the mentee committed to do (action items, with owner and rough due date)
- the mentee's blockers, patterns and strengths shown
- anything Winnie promised during the session (to send, to show later, to explain), listed separately from the mentee's commitments
- anything the mentee said about Winnie's teaching (testimonial candidates). Never invent one; if there is none, say so
- anything reusable for class (WF-2 candidates), described generically with no names

Mark anything you are unsure of as `[to confirm]` rather than guessing.

## 4. Draft the public playback

Write 2 to 3 plain sentences on what was covered and what the mentee did or will do next. Public-safe only: no company names, no third parties, no candid assessment or weaknesses, no scores, nothing from the private recap. Strengths-framed and neutral. Show the draft and wait for the user to approve or edit it.

## 5. Run the log script (after playback approval)

`python3 _system/scripts/mentee.py log <mentee> --topic "<topic>" --date YYYY-MM-DD --playback "<approved text>" --build`

Add `--n N` to edit an existing session, `--status` if not Completed, and `--lesson <slug>` if the output says no lesson matched and the user names one. This creates the private recap from the template under `mentees/<slug>/sessions/`.

## 6. Fill the private recap

Fill the recap the script created from step 3, in Vietnamese per the Language note above: Session Summary, Topics Covered, Key Observations, Student Work Reviewed, Feedback Given, Commitments & Next Steps (homework and owners), My Notes as Trainer, Next Session Plan. Keep `draft: true`. Candid observations belong here, never in the playback. If the recap already exists (re-run or edit), check every quote in it against the transcript and flag any quote that does not appear there, instead of overwriting it.

## 7. Follow-up drafts (append to the recap under `## Follow-up drafts`)

- **Homework**: one clear task, expected output, due date, and the lesson or template it relates to. If the lesson has a homework section, reuse it rather than inventing a new task.
- **Zalo message** to the mentee: short, warm, in Vietnamese per VI_VOICE.md. Thanks, 2 to 3 takeaways, the homework and due date, next session date if known. The user copies and sends it. Never claim it was sent.
- **Next-session seed**: 3 bullets for `/prep` to pick up (open questions, what to check on the homework, what to teach next). Put the same bullets in the recap's Next Session Plan.

## 8. Testimonial capture

If step 3 found feedback about Winnie's teaching, apply the testimonial capture rule in CLAUDE.md in this same response: add it to `showcase/testimonials.md` (permission: not yet confirmed unless the user says otherwise) and to the mentee's own record. Tell the user it was added.

## 9. Report

The build prints a "Mentee health check". Pull out the lines for this mentee and say what is still open (missing playback, slides, dates, baseline). Then report:

- lesson link and slides found (the user should drop a deck named `Session N - ...` into the mentee's `slides/` folder if none)
- the private recap path and the three follow-up drafts, ready to review
- WF-2 candidates, if any, as a short list (do not adapt them without asking)
- what is still waiting on the user: send the Zalo message, set the homework in Notion if used

## 10. Final session only

If this was the programme's final session, follow the close-out rule in CLAUDE.md (close-out template, baseline vs reassessment, testimonial capture) and set `status: "completed"` and `end:` in `mentees/<slug>/mentee.md`, and fill the Post-training column of `mentees/<slug>/assessment.md` from the reassessment (numbers only). If no baseline is on file, flag that explicitly.
