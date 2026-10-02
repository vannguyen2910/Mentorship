# Mentoring Program — Claude Rules

## Lesson file sync rule

Every lesson in `Library/lessons/` has two paired files:
- `*-lesson.md` — the source of truth for all content (activities, phases, timing, concepts)
- `*-slide-outline.md` — reflects the lesson structure as slide specs (layout types, visual hints, kickers)

**When either file is updated, always check and update the other.**

New `*-slide-outline.md` files start from `_System/templates/_template-slide-outline.md`, not a blank page — it fixes the session metadata table, the standard slide-entry fields, and the speaker-notes-as-bullets rule. Layout types come from the catalogue in `_System/Themes/slide-design/RULES.md` (canonical — other paths to a rules file are pointers to it).

Specifically:

| What changed in lesson.md | What to update in slide-outline.md |
|---|---|
| Phase timing (e.g. "15 min" → "20 min") | MILESTONE slide `Num:` value + arc description + slide structure note |
| Phase added or removed | Add/remove the corresponding slide section; update total slide count in the structure note |
| New checkpoint or transition inserted | Add a STATEMENT or MILESTONE slide at the matching position in the outline |
| Section reordered (e.g. concept extension moved) | Reorder the corresponding slides in the outline |
| Slide count changes for any reason | Update the `## Slide structure` header line (e.g. "17 slides" → "18 slides") |

| What changed in slide-outline.md | What to update in lesson.md |
|---|---|
| Slide timing or Num value changed | Update the matching phase timing in the Session Structure table |
| Slide added or removed | Check if the lesson phase needs a matching structural change |
| Kicker or title copy changed | Check if the lesson phase heading or key message should match |

**Always apply both files in the same response.** Never leave one out of sync with the other.

---

## Testimonial capture rule

Whenever a prompt includes feedback from a student or mentee about Winnie's teaching/mentoring — praise, a reaction, a quote, however casually mentioned — automatically add it to the central quote bank at `Showcase/testimonials.md`, in the same response, without being asked.

Specifically:

| What to do | How |
|---|---|
| Add the entry | Follow the format already defined at the top of `testimonials.md`: name, company/context, programme, date, quote, context line, permission line |
| Set permission status | Default to `Permission to publish externally: not yet confirmed` unless the user explicitly says the student agreed to publish |
| Sync the student's own record | If the student has an existing file (e.g. `Mentees/[name]/README.md` or a session recap), also add the quote there so both stay in sync — same principle as the lesson sync rule above |
| Don't gate on being asked | Capture it proactively; just tell the user afterward that it was added, don't ask permission first |

If `Showcase/testimonials.md` doesn't exist yet, create it using the same structure as the current file (header, permission note, entry-format block, then entries).

---

## Programme kickoff & close-out rule

Every private-training student should get two artifacts from `_System/templates/`: a coaching plan at kickoff (`_template-coaching-plan.md`) and a close-out recap on their final session (`_template-programme-closeout.md`). This makes every future close-out able to show real before/after growth instead of a single snapshot.

Specifically:

| When | Do this |
|---|---|
| Starting a new private-training student | Create their coaching plan from `_template-coaching-plan.md`. Its "Baseline Assessment" section is mandatory — run the self-assessment tool (`Programs/training-hub/student-design-assessment.html`) with the student at or before Session 1 and save the result into their student folder. Without this, there's nothing to compare the close-out reassessment against. |
| Running the final session of a programme | Create the recap from `_template-programme-closeout.md`, not the plain `_template-session.md`. Pull the Session 1 baseline numbers into its "Baseline vs Reassessment" table — don't just report the final score in isolation. |
| A student has no baseline on file (older/in-flight programmes) | Flag this to Winnie explicitly rather than silently using only the final snapshot — the close-out template's comparison table will be incomplete without it. |
| Close-out is reached | Apply the testimonial capture rule above in the same response — close-out sessions are exactly where testimonials tend to surface. |

---

## General lesson conventions

- All specific AI tool names (Claude, Cursor, ChatGPT, Copilot, etc.) should be replaced with generic labels: "AI chat tool", "AI coding tool", "your AI tool". Do not introduce tool names when editing lesson content.
- Lesson and slide-outline content must never reference a specific mentee or student by name — every lesson is built to be taught to any mentee, not just the one it was drafted for. Do not introduce a mentee's name, cohort, or identifying detail when drafting or editing `*-lesson.md` or `*-slide-outline.md`; if an example needs a person, use a role label ("the mentee", "a junior designer") instead. This is separate from the private-session attribution rule in `WORKFLOW_RULES.md`, which governs crediting a mentee when their session is the *source* of a class example — that rule is about consent to reuse, this one is about the lesson content itself staying generic regardless of where an idea came from.
- The `*-slide-outline.md` file contains only slide-specific concerns (layout, visual hints, kickers). Do not add full lesson prose to it.
- The `*-lesson.md` file is the source of truth. If content in the two files conflicts, the lesson file wins.
- For detailed voice/tone rules (tone, English code-switching, punctuation, teleprompter script format, Practice/Bài Tập script structure), see `Programs/online-course/AI Prototype Development/writing-style-guide.md`. Read this before drafting or revising any `*-lesson.md`, `*-slide-outline.md`, or teleprompter script.
