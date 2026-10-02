---
title: "Evaluate Current Experience"
subtitle: "Judge what exists against clear principles, with evidence you can show"
type: lesson
program: private-training
tags: [evaluation, heuristic-evaluation, cognitive-walkthrough, severity-rating, wcag, usability, current-state, ai-workflow]
level: junior, mid
duration: "90 min"
date: 2026-10-01
draft: true
slides: ""
previous-session: "Design Thinking for UX Designer"
next-session: "Customer Understanding"
---

## Overview

Most junior designers have never been shown how to judge a design properly. They ship a flow, or inherit one, and the only tool they have is taste: "this feels off", "I'd change the colour". Taste is a fine starting point and a weak argument. It can't be checked, it can't be ranked, and nobody else on the team can act on it.

This session gives a junior designer the foundation to evaluate an experience that already exists, whether they designed it themselves without guidance or inherited it from someone else. The first 64 minutes are manual and principle-led: pick the right method for the stage the project is in, judge a food-delivery checkout against Nielsen's 10 usability heuristics, attach evidence to every issue, and rate each issue by severity so the biggest problems rise to the top. Only then does AI enter, as an assistant for 12 minutes: to brainstorm issues the mentee missed, to structure their findings into their own `evaluation.md` file, and to preview the `evaluation.html` page they will generate as homework. An accessibility check against WCAG 2.1 AA is a take-home pass, not taught live.

The order is deliberate. A mentee who learns the principles first can tell when AI is wrong. A mentee who starts with AI learns to accept whatever it says.

This lesson sits between Design Thinking and Customer Understanding. It builds on the screen flow the mentee captured in Design Thinking, and it hands off a ranked list of what is wrong and where. Customer Understanding then picks up the question an evaluation can't answer: why. Mid-level mentees must take this session before Desk Research; seniors can skip it by passing the senior fast-track below. Desk Research then uses the mentee's `evaluation.md` as one of its evidence sources.

---

## Learning Objectives

By the end of this session, students will be able to:

1. **Choose** the right evaluation method for the stage their project is in
2. **Apply** usability heuristics to a live product, with evidence for every issue
3. **Rate** issues by severity so the biggest problems rise to the top
4. **Use** AI to brainstorm, structure, and visualise their findings, while keeping every judgment their own

---

## Success Check

- A heuristic evaluation of your current product is complete
- Issues are ranked by severity, and each one has a screenshot or example

**In-session checkpoint:** one flow of your own product evaluated, with 3 to 5 findings, each rated 0 to 4 and each with a screenshot. The full Success Check above is met when the assignment is submitted.

---

## Plain-Language Glossary

Say each of these once, in plain words, before using it. Keep this list on screen or in the handout.

| Term | Plain meaning |
|---|---|
| Evaluation | Judging something that already exists against a standard, to find where users will struggle. It is not a redesign. |
| Heuristic | A rule of thumb. A principle that holds across most products, not a rule for one screen. |
| Finding | One issue, written with what you saw, where, which principle it breaks, and proof. |
| Severity | How bad an issue is, so the worst gets fixed first. |
| Evidence | A screenshot or example anyone can look at and see the same thing you saw. |
| Walkthrough | Stepping through one task as a first-time user would, asking four questions at every step. |

---

## Materials Needed

- A live food-delivery app on the mentor's phone or screen, used only for the opening. Live apps change without warning, so keep one screenshot of its checkout as a backup.
- The seeded checkout set (Appendix F): 5 screens of a neutral mock food-delivery checkout with planted issues and an answer key. The guided practice runs on this, so every mentee faces the same findings.
- `Library/frameworks/framework-nielsen-usability-heuristics.md`: teach the 10 heuristics from this file. The lesson below groups and simplifies it for juniors, it doesn't replace it.
- `Library/frameworks/framework-severity-rating-scale.md`: teach the 0 to 4 scale and its factors from this file.
- The ten heuristic slides reused from the former Audit & Desk Research deck: `assets/heuristic-principle-slides.html`
- The Heuristics Cheat Sheet (Appendix A): one page, handed out before Part 2
- The Evaluation Worksheet (Appendix B): the manual template the mentee fills in during Part 5
- The three pre-written calibration issues (Appendix D) for the severity activity, and the six symptom cards (Appendix E) for the matching activity
- For the AI block: an AI chat tool for the brainstorm and `evaluation.md` steps, and an AI tool that can create files (an AI coding tool, or a chat tool with file creation) for the `evaluation.html` homework step. The AI foundation folder from earlier sessions is the working folder.

---

## Pre-Class Preparation

Ask the mentee to do the following before the session:

1. **Pick one key flow in your own product** (a flow you designed, or one you inherited). Choose a flow with 4 to 8 steps, such as sign-up, search to result, or checkout. Not the whole product. If you captured a screen flow in Design Thinking, use that one, so the same flow carries into Customer Understanding.
2. **Capture it as screenshots**, one per step, in order. Name them `01-...png`, `02-...png`. Resize to about 1200 px wide so the later HTML file stays small.
3. **Check confidentiality.** If the product is internal or customer-facing at work, blur or replace any real customer data and check your company's rules on what can go into an AI tool. If in doubt, evaluate a personal or portfolio project instead.
4. **Confirm the AI foundation folder and an AI tool are set up** from earlier sessions. This lesson assumes they are.

---

## Session Plan

| Act | Block | Topic | Duration |
|---|---|---|---|
| 1 · Frame | Opening | Spot one problem, then learn why opinion isn't a finding | 4 min |
| 2 · Method | Teaching + Activity | Choose a method by project stage | 7 min |
| 3 · Principles | Teaching + Activity | Nielsen's 10: overview page, one slide per principle, matching activity | 17 min |
| 4 · Practice | Guided activity | Evaluate the seeded checkout together | 12 min |
| 5 · Severity | Teaching + Activity | Rate issues 0 to 4, then plot them | 10 min |
| 6 · Own product | Activity (manual) | Evaluate and rate your own flow, no AI | 14 min |
| 7 · AI assist | Teaching + Build | Brainstorm → `evaluation.md` → see `evaluation.html` | 12 min |
| 8 · Close | Wrap | Checkpoint, homework, bridge to Customer Understanding | 4 min |

**Scripted total: 80 min, with a 10-minute buffer inside the 90-minute slot.** The first 64 minutes (blocks 1 to 6) use no AI at all. AI is 12 minutes, by design. Expect block 3 and block 6 to run long; the buffer is for them.

**If time runs short, cut in this order:**

1. Skip the optional knowledge check after Part 4
2. In Part 4, the mentor plots the 2x2 instead of the mentee
3. The `evaluation.html` demo in Part 6 moves entirely to homework

Do not cut the manual evaluation in block 6. It is the point of the session.

> **Story logic:** The session moves from *why* (an opinion isn't a finding) to *how to choose* (method by stage) to *what to judge against* (principles) to *how to judge* (evidence plus severity) to *doing it yourself* (manual) to *doing it faster and sharing it* (AI). By the end, the mentee has a ranked, evidenced evaluation of their own product, and an `evaluation.md` they can reuse on every future project.

---

## Senior Fast-Track (skip check)

Seniors may skip this session if they can already do what it teaches. Run this check before booking the session. It is not part of the 90-minute plan or the slide deck, and takes about 15 minutes.

1. **Rate (8 min):** Give the mentee the three calibration issues from Appendix D (C1 to C3) without the suggested ratings. They rate each 0 to 4 and give a one-line reason.
2. **Write (7 min):** They pick a flow in their own product and write one finding in the four-part format (what I saw, where, which principle, proof), with a screenshot.

**Pass:** all three ratings are within one point of the mentor's suggested rating, the reasoning names frequency and impact, and the finding has all four parts with real proof. A pass means the mentee skips this session and goes straight to Desk Research. They bring any current-state notes in place of `evaluation.md`.

**Not yet:** run the full session, or only Parts 2 to 4 (principles, guided practice, severity) if the gap is narrow. Say which gap showed up (ratings without reasoning, findings without proof, principles misnamed) so the mentee knows what to practise.

---

## Core Content

### Opening: Opinion Isn't a Finding

**Spot it (1 min).** Show the food-delivery checkout screen. Ask: *"Find one thing that would slow a hungry customer down. Tell me what it is."* Take two answers.

Then name what just happened. Both answers were a start, and both were probably opinions: "it's cluttered", "the button is hard to see". Those are real reactions, but they can't be checked, can't be ranked, and a teammate can't act on them.

**The shift (3 min).** An evaluation turns a reaction into something usable. It has four parts:

1. **What I saw**: an observation anyone could confirm
2. **Where**: the exact screen and step
3. **Which principle it breaks**: the standard you're judging against
4. **Proof**: a screenshot or example

> **No screenshot, no finding.** This is the one rule the whole session rests on.

Evaluation is also not redesign. Describing the problem and proposing the fix are two different jobs. Today's job is only the first.

---

### Part 1: Choose a Method by Stage

#### The question to ask first

Before judging anything, ask: *what do I have, and what do I need to know?* The method follows from the stage your project is in.

**Where is your project?**

| Stage | What you have | Good starting method |
|---|---|---|
| Draft | Screens exist, nothing shipped, no users yet | Heuristic evaluation, then a walkthrough of the one key task |
| Live, you designed it | A shipped flow and some data | Analytics and feedback to find where, then heuristic evaluation on those spots |
| Live, you inherited it | Someone else's product, often with a backlog of complaints | Analytics and feedback first (fast), then heuristic evaluation on the flagged flows |

#### Three methods, one line each

| Method | The question it answers | Needs | Limit |
|---|---|---|---|
| Analytics, feedback review, SUS | *Where* are users struggling, and how much? | Existing data, support tickets, reviews, or a short survey | Tells you where and how much, not why |
| Cognitive walkthrough | Can a first-time user finish *this one task*, step by step? | One task and the screens | Slow. One task at a time |
| Heuristic evaluation | Does this design break well-known principles? | Screens and the principle list. No users needed | It is judgment. It finds many problems but not all of them |

**SUS (System Usability Scale)** in one breath: a 10-statement survey answered on a 5-point agree scale. The result is a score from 0 to 100, and around 68 is the commonly cited average. It tells you *how well* the product is doing overall, not *what* is wrong.

**The cognitive walkthrough** gets one sentence live, because it isn't practised in this session. The four questions go on the Cheat Sheet. At every step of one task, it asks:

1. Will the user try to do the right thing at this step?
2. Will they notice the right action is available?
3. Will they connect that action with what they're trying to do?
4. After they act, will they see that it worked?

A "no" to any of the four is a finding.

**Usability testing with real users** is the next step up when you need to see behaviour, not judge a design. It is taught later in the track. Evaluation tells you where to point it.

#### Your own design is the hardest one to see

If you designed it, you know why every choice was made, so you can't see it as a first-time user would. Three habits help:

- Do a task, not a tour. Walk it as someone who has never seen it, with a goal ("reorder my usual meal").
- Judge against the principle list, not your memory of why you chose it.
- Read the on-screen text out loud. Jargon and vague labels become obvious.

A finding in your own work isn't a failure. It's the evaluation doing its job.

---

### Part 2: The Principles

Teach from `framework-nielsen-usability-heuristics.md`. Show all ten on **one overview page first**, grouped into three families so a junior has a map. Then take **each principle on its own slide**, about a minute each: the plain meaning, one broken food-delivery example, and one check-for line. The ten slides are reused as is from the Audit & Desk Research deck (Heuristic 01 to 10, saved in `assets/heuristic-principle-slides.html`): each has a definition, a Why it matters line, and a bad and good UI example. Teach the slide's own example first, then use the food-delivery line in the tables below as the bridge to the checkout. Budget 1 minute for the overview, 12 for the ten slides, 3 for the matching activity (Appendix E), and 1 to hand out the Cheat Sheet. Don't ask a discussion question on every slide: each slide's speaker notes mark the ones that earn one.

#### Family 1: Can I see and understand what's going on?

| Heuristic | In plain words | What it looks like broken (food delivery) |
|---|---|---|
| 1 Visibility of system status | The product tells me what's happening | After tapping Place Order, the screen sits on a spinner. Did my payment work? |
| 2 Match with the real world | It speaks my language | A line labelled "SF" instead of "Service fee" |
| 6 Recognition over recall | I don't have to remember things | The promo code I entered earlier isn't shown on the order summary |
| 8 Aesthetic and minimalist design | Only what matters is on screen | Upsell banners push the order total below the fold |

#### Family 2: Can I stay in control and recover?

| Heuristic | In plain words | What it looks like broken (food delivery) |
|---|---|---|
| 3 User control and freedom | I can undo or back out | Pressing Back from payment empties my cart |
| 5 Error prevention | It stops me making the mistake | The tip field accepts 5000 when I meant 5.00 |
| 9 Recognise, diagnose, recover from errors | Errors tell me what to do next | "Payment failed. Error 4012." and nothing else |

#### Family 3: Is it predictable and efficient?

| Heuristic | In plain words | What it looks like broken (food delivery) |
|---|---|---|
| 4 Consistency and standards | Same thing, same look, same word | "Checkout" on one screen, "Pay now" on another, for the same step |
| 7 Flexibility and efficiency | Fast for people who've done it before | No way to reorder a past meal or save an address |
| 10 Help and documentation | Help is there when I need it | No explanation of what the "service fee" covers |

**Tip for juniors:** when you spot a problem and can't name the heuristic, find the family first ("this is about not knowing what's happening") and then narrow to the heuristic. If a problem fits two heuristics, pick the closest one and note the second. Don't stall.

#### Take-home: the accessibility check (WCAG 2.1 AA)

Not taught live. Hand it out with the Cheat Sheet. After class, the mentee runs one extra pass on the same screens, with four fast checks:

| Check | What to look for | Reference |
|---|---|---|
| Text contrast | Body text at least 4.5:1 against its background. Large text and UI component borders at least 3:1 | WCAG 1.4.3, 1.4.11 (AA) |
| Colour alone | Is anything communicated by colour only (a red field with no message)? | WCAG 1.4.1 (A) |
| Labels | Does every input have a visible label, not just placeholder text? | WCAG 3.3.2 (A) |
| Touch targets | Tap targets about 44 x 44 pt. Note: WCAG 2.1 doesn't require this at AA, it is a recommended practice | Best practice (2.5.5 is AAA) |

Log accessibility issues in the same worksheet, using the check name in the Heuristic column.

---

### Part 3: Guided Practice (Checkout Together)

#### What a good finding looks like

| Weak | Strong |
|---|---|
| "The checkout is confusing." | At Review order, the service fee is labelled "SF" with no explanation. A user can't tell what they're paying for before they commit. Breaks *Match with the real world*. Screenshot attached. |

> The strong example is a format demonstration, not a claim about any real app. The mentee's findings come from what they actually see on the seeded checkout set.

**Three tests for a finding.** Before logging an issue, check it against these:

1. **Is it something you saw, not felt?** "The button is grey" is a sighting. "It looks ugly" isn't.
2. **Does it affect what the user can do or understand?** If not, it's a preference.
3. **Is it a problem, not a fix?** "Make the button blue" is a solution. Write the problem it would solve.

#### How the guided practice runs

1. **Mentor models one finding end to end** on the seeded checkout set (Appendix F), using the service fee finding. Think aloud: what I saw, where, which family, which heuristic, then capture the screenshot and circle the spot. About 3 minutes.
2. **Mentee finds two more**, using the same four-part format and the Cheat Sheet. About 6 minutes.
3. **Share back.** Compare with the answer key. Did anyone choose a different heuristic for the same issue? That's fine, and a good discussion. About 3 minutes.

The seeded set has nine planted issues and the mentee only needs two. Accept an unplanted issue too, if it passes the three tests.

---

### Part 4: Rate Severity

Teach from `framework-severity-rating-scale.md`.

#### Why rate at all

A list of 25 findings is a list of complaints. A ranked list is a plan. Severity is how you decide what the team looks at first.

#### The scale

| Score | Label | Meaning |
|---|---|---|
| 0 | Not a problem | Not a usability issue. Don't log it |
| 1 | Cosmetic | Fix if there's spare time |
| 2 | Minor | Low priority |
| 3 | Major | Important, high priority |
| 4 | Catastrophe | Must fix before release |

#### Three plain questions

Don't guess a number. Ask:

1. **How often?** Does everyone hit it, or only some people on some days?
2. **How bad when it happens?** Can the user recover, or are they stuck, charged twice, or losing data?
3. **Does it keep happening?** Is it confusing once, then learned, or does it cost the user every time?

If a fourth thing is on your mind, ask whether it damages trust in the product. Data loss and double charges do. The framework doc calls this market impact.

#### From answers to a number: the 2x2

Plot each issue on two axes: **frequency** (rare to often) and **impact** (small to big).

| | Rare | Often |
|---|---|---|
| **Big impact** | Usually 2 or 3 | Usually 3 or 4 |
| **Small impact** | Usually 0 or 1 | Usually 2 |

Then use the third question to nudge: if it **keeps costing the user every time**, round up. If it **wears off after the first time**, round down. The top-right of the plot is where you start your report.

> Two evaluators rarely give the same number. The goal is to land within one point of each other, and to be able to explain why.

#### Calibrate

Use the three issues in Appendix D. Mentee rates all three silently, then compare with the mentor's suggested ratings. The discussion is the point, not matching the number.

---

### Part 5: Evaluate Your Own Product (Manual)

No AI in this block. The mentee uses the Cheat Sheet, the Worksheet, and their screenshots.

**Setup (2 min).** Confirm the flow and screenshots. Confirm which entry point applies: *I designed this* (use the three habits from Part 1) or *I inherited this* (note any known complaints, but judge the screens, don't repeat the complaints).

**Evaluate and rate (10 min).** For each step of the flow:

1. Look at the screen as a first-time user doing the task.
2. Check each family: seeing and understanding, control and recovery, predictable and efficient.
3. Log every issue in the Worksheet with the four-part format and a screenshot file name.
4. Rate each with frequency, impact, and a severity from 0 to 4.

**Target: 3 to 5 findings.** Quality over count. The accessibility check is a take-home.

**Share back (2 min).** Mentee names their highest-severity issue and the evidence for it.

**Facilitator watch-fors:**

- A list of ten cosmetic points and nothing about the task. Redirect to the task
- Everything rated 4. Ask: "If everything is a catastrophe, what's first?"
- Solutions written instead of problems. Ask: "What is the problem that fix would solve?"
- Findings with no screenshot. They don't count yet
- Defending the design instead of logging the issue ("I did it that way because..."). Acknowledge it, then log it

---

### Part 6: AI as an Assistant

By now the mentee has done the work manually. AI is introduced to extend it, not replace it.

#### The rule: AI assists, you decide

AI can look at a screenshot and miss the thing you saw, or invent something that isn't there. It has no idea who your users are. The mentee's manual pass is what lets them tell the difference. Say this out loud at the start of the block.

#### Step 1: Brainstorm (4 min)

The mentee gives AI their screenshots and the Cheat Sheet and asks it to brainstorm issues they may have missed, one family at a time. AI does not rate severity and does not suggest fixes at this stage.

For every AI suggestion, the mentee asks three questions:

1. **Can I see it on the screen?** (Point to the exact element.)
2. **Does it really break that principle?**
3. **Would a real user hit it?**

Yes to all three: add it to the Worksheet with a screenshot and rate it yourself. Otherwise discard it. Expect to discard some.

#### Step 2: Build your own `evaluation.md` (6 min)

The mentee asks AI to turn their finished Worksheet into a single `evaluation.md` using the schema in Appendix C. AI structures. It does not add findings and does not change the mentee's severity scores.

Save the file in the AI foundation folder. It is a reusable asset: next project, the mentee starts from the same schema.

**Check the output:** the number of findings matches the Worksheet, every finding has an evidence file name, and no score has changed.

#### Step 3: See `evaluation.html` (2 min, then homework)

In class, the mentor shows the prompt and a finished `evaluation.html` built from a sample `evaluation.md`. The mentee generates their own as homework, asking an AI tool that can create files to read `evaluation.md` and generate one HTML page: a summary, a table ranked from highest severity to lowest with the screenshot embedded in each row, and the 2x2 plot with each issue as a numbered point.

- **Embed the screenshots in the HTML** so it is one portable file. Resized images keep it small.
- **`evaluation.md` is the source of truth.** To change a score, edit the `.md` and regenerate the `.html`. Never edit the `.html` by hand.
- **The page must pass its own checks.** Ask for text contrast of at least 4.5:1 and for severity to be shown by number or shape as well as colour.

**Check the output:** spot-check three rows against the `.md`, and check the position of three points on the plot.

---

### Close (4 min)

1. Read the in-session checkpoint aloud and check it against the mentee's work: one flow, 3 to 5 findings, each rated and each with a screenshot. Say that the full Success Check is met with the assignment.
2. Brief the homework.
3. Name where evaluation stops: it tells you *what* is wrong and *where*. It can't tell you *why* users struggle. Ask: *"Pick your top finding. What do you believe about your user that makes it a problem, and how do you know?"* Take one answer.
4. Bridge: *"Next session, Customer Understanding, starts from there. Your `evaluation.md` shows where friction is likely. Talking to real users tells you why, and which of your beliefs are wrong."*

> **Facilitator note:** Mid-level mentees take Desk Research between this session and Customer Understanding. For them, the bridge is the same, with the findings in `evaluation.md` becoming evidence in Desk Research.

---

## Activities

### Activity: Place Your Project and Pick a Method
**Type:** In-class · discussion
**Time:** 3 min (inside Part 1)
**Format:** Solo, then share

1. **(1 min)** Place your project on the stage table: draft, live and you designed it, or live and you inherited it.
2. **(1 min)** Pick one method to start with and write one line on why.
3. **(1 min)** Share back. Mentor challenges one choice: "What would you learn that you don't already know?"

---

### Activity: Match the Symptom
**Type:** In-class · Appendix E
**Time:** 3 min (end of Part 2)
**Format:** Solo, then reveal

1. **(2 min)** Read each of the six symptom cards. Name the principle number and its family.
2. **(1 min)** Reveal. If a symptom fits two principles, accept either when the mentee can say why. Ask which two were hardest to place.

---

### Activity: Evaluate the Checkout Together
**Type:** In-class · seeded checkout set (Appendix F) + Cheat Sheet
**Time:** 12 min
**Format:** Mentor models, then solo, then share

1. **(3 min)** Mentor models one finding end to end.
2. **(6 min)** Mentee finds two more findings in the four-part format, each with a screenshot.
3. **(3 min)** Compare and discuss.

---

### Activity: Calibrate Severity
**Type:** In-class · Appendix D
**Time:** 5 min (inside Part 4)
**Format:** Solo, then pair

1. **(2 min)** Rate the three issues silently using the 2x2 and the three questions.
2. **(3 min)** Compare with the mentor. Where you differ by more than one point, explain your reasoning.

---

### Activity: Evaluate Your Own Product
**Type:** In-class · Worksheet (Appendix B) · no AI
**Time:** 14 min
**Format:** Solo, with coaching

See Part 5.

---

### Activity: Build Your Evaluation With AI
**Type:** In-class · AI chat tool, plus a demo of an AI tool that creates files
**Time:** 12 min
**Format:** Solo, with coaching

See Part 6.

---

## AI in Practice: Brainstorm, Build, Visualise

This session's AI use is deliberately late and deliberately limited. The mentee does the judging. AI helps them see more, structure what they found, and show it.

### 🤖 The three prompts

**Brainstorm:**

> *"I'm evaluating the [flow name] of [product]. Attached are screenshots of each step, in order. Below are usability principles in three groups, each with a 'check for' line. Review one group at a time. For each possible problem, tell me which step, point to the exact element or quote the exact text, and name the principle. Do not rate severity. Do not suggest redesigns. If you can't tell from the screenshot, say 'not sure'."*
> [paste the Cheat Sheet]

**Build `evaluation.md`:**

> *"Here is my completed findings worksheet: [paste]. Turn it into one markdown file named evaluation.md using exactly this structure: [paste the schema from Appendix C]. Do not add findings. Do not change any severity score. If a field is missing, write MISSING instead of guessing."*

**Generate `evaluation.html` (homework):**

> *"Read evaluation.md. Generate one self-contained HTML file named evaluation.html with: (1) a summary header, (2) a table sorted by severity, highest first, with each row showing the id, title, heuristic, severity, and the screenshot, (3) a 2x2 plot with frequency on the horizontal axis and impact on the vertical axis, each issue shown as a numbered point. Embed the screenshots in the file. Use only data from evaluation.md. Text contrast at least 4.5:1, and show severity with a number or shape as well as colour."*

### 🧠 Critical thinking

- Where did AI point to something that wasn't on the screen? What gave it away?
- What did you catch in your manual pass that AI missed? What did AI catch that you missed?
- Rating severity needs to know your users and your business. What did AI not know?

### ✍️ Prompt engineering tip

Tell AI what *not* to do. "Do not rate severity" and "do not change any score" keep the judgment with you and make the output easier to check. Constraints are as useful as instructions.

### ⚖️ Ethics consideration

Screenshots of real products can contain customer data or confidential designs. Before uploading anything to an AI tool, blur personal data and check your company's rules. And an AI-written explanation of an issue is not evidence. Only the screenshot is.

---

## Assessment

### Quick knowledge check

Optional. Run verbally in the buffer after Part 4, or set as a take-home self-check:

1. Your analytics show a big drop-off at one step and you have no budget for user testing. Which method do you start with, and then which?
2. What makes something a finding rather than an opinion?
3. Two issues both happen often. One is a confusing label, the other charges the customer twice. Which goes first, and why?

---

## Assignments

### Assignment: Finish and Share Your Evaluation
**Due:** Before next session
**Time estimate:** 2 to 2.5 hours
**Type:** Analysis · Your real project

1. Complete the evaluation of your first flow. In class you logged 3 to 5 findings, so cover every remaining step.
2. Evaluate **a second flow** of the same product, using the same manual-first order: Worksheet first, then AI to brainstorm.
3. Run the four accessibility checks from the Cheat Sheet on both flows and log what you find in the Worksheet.
4. Make sure every finding has a screenshot or example and a severity from 0 to 4.
5. Generate your final `evaluation.md` covering both flows, then use the HTML prompt to generate `evaluation.html`.
6. Write one line at the top of `evaluation.md`: which method you started with and why.
7. At the bottom of `evaluation.md`, add a section called "Open questions about users". For your top three findings, write one line each: *what do I believe about the user here that I haven't checked?* You'll use these in Customer Understanding.
8. Optional stretch: ask a peer to rate your top three issues without seeing your scores, then compare. Where you differ by more than one point, write down why.

**Deliverable:** `evaluation.md` and `evaluation.html`, covering two flows, at least 6 findings in total, ranked by severity, each with evidence, plus three open questions about users. Save to your homework folder before the next session.

> **AI in Practice:** *"Here is my evaluation.md: [paste]. Check it against my screenshots. Which findings are vague, missing evidence, or written as solutions instead of problems? Don't edit anything, just list them."*

---

## Practice Dataset

Mentees who can't bring their own product can evaluate the full seeded checkout set (Appendix F) end to end with the same Worksheet.

---

## Appendix A: Heuristics Cheat Sheet (one page)

**Family 1: Can I see and understand what's going on?**

- 1 Visibility of system status: after any action, show what happened
- 2 Match with the real world: use the user's words
- 6 Recognition over recall: show it, don't make me remember it
- 8 Aesthetic and minimalist design: if it doesn't help the task, remove it

**Family 2: Can I stay in control and recover?**

- 3 User control and freedom: undo, cancel, go back safely
- 5 Error prevention: stop the mistake before it happens
- 9 Recognise, diagnose, recover from errors: say what went wrong and what to do next

**Family 3: Is it predictable and efficient?**

- 4 Consistency and standards: same thing, same look, same word
- 7 Flexibility and efficiency: shortcuts for repeat users
- 10 Help and documentation: help at the point of need

**Take-home accessibility check (WCAG 2.1 AA):** contrast 4.5:1 text and 3:1 UI parts · not colour alone · visible labels · tap targets about 44 pt (best practice)

**Walkthrough (each step of one task):** will they try it, notice it, connect it, see it worked?

**Finding format:** What I saw · Where · Which principle · Proof

**Severity:** 0 not a problem · 1 cosmetic · 2 minor · 3 major · 4 catastrophe

---

## Appendix B: Evaluation Worksheet (manual)

| # | Where (screen / step) | What I saw | Heuristic or WCAG check | Evidence (file name) | Frequency (rare / sometimes / often) | Impact (small / medium / big) | Severity (0 to 4) |
|---|---|---|---|---|---|---|---|
| 1 | | | | | | | |
| 2 | | | | | | | |
| 3 | | | | | | | |
| 4 | | | | | | | |
| 5 | | | | | | | |
| 6 | | | | | | | |

---

## Appendix C: `evaluation.md` Schema

```
# Evaluation: [product], [flow]

- Date:
- Evaluator:
- Method: [which method you started with, and why, in one line]
- Scope: [flow name, number of steps]

## Findings (ranked by severity, highest first)

### F1: [short title]
- Where:
- What I saw:
- Heuristic or WCAG check:
- Evidence: [screenshot file name]
- Frequency:
- Impact:
- Severity: [0 to 4]

### F2: [short title]
...
```

A suggested fix is deliberately not part of the schema. Evaluation describes the problem. Fixes come later.

---

## Appendix D: Calibration Issues (food delivery, illustrative)

These are teaching examples, not claims about any real app. C1 and C2 also appear in the seeded checkout set (Appendix F), so the mentee has already seen those screens.

| # | Issue | Mentor's suggested rating and reasoning |
|---|---|---|
| C1 | After tapping Place Order, the screen stays on checkout with a spinner for 8 to 10 seconds and no confirmation. Some users tap again and place a double order. (Visibility of system status, Error prevention) | **4.** Everyone who orders hits the wait, the impact is a double charge, and trust is at stake. Many would argue 3. The reasoning matters more than the number. |
| C2 | The service fee line is labelled "SF" with no explanation. (Match with the real world, Help and documentation) | **2.** Every order sees it and it keeps happening, but impact is small: confusion, not a blocked task. Raise to 3 if you argue it harms trust. |
| C3 | The promo code field uses a slightly different grey from the other fields on the same screen. (Consistency and standards) | **1.** Rarely noticed, no effect on completing the task. |

---

## Appendix E: Match the Symptom (six cards)

Read each card. The mentee names the principle and its family. If a symptom fits two, accept either with a reason.

| # | Symptom (food delivery) | Principle | Family |
|---|---|---|---|
| 1 | The order status says "Preparing" for 40 minutes and never changes | 1 Visibility of system status | See and understand |
| 2 | A confirmation dialog asks "Proceed with disposition?" | 2 Match with the real world | See and understand |
| 3 | I removed an item from my cart by accident and there is no undo | 3 User control and freedom | Control and recover |
| 4 | Stars on the rating screen, thumbs on the review screen, for the same rating | 4 Consistency and standards | Predictable and efficient |
| 5 | The delivery address field accepts a 3-digit postcode | 5 Error prevention | Control and recover |
| 6 | "Something went wrong." and a Close button | 9 Recognise, diagnose, recover from errors | Control and recover |

---

## Appendix F: Seeded Checkout Set

Five screens of a neutral mock food-delivery checkout (no real brand), exported at about 1200 px wide: Cart, Review order, Payment, Placing order, Payment failed. Nine issues are planted, so every mentee faces the same findings. The mentor models P1. The mentee finds two others.

| ID | Screen | Planted issue | Principle(s) | Suggested severity |
|---|---|---|---|---|
| P1 | Review order | The fee line is labelled "SF" with no explanation | 2 Match, 10 Help | 2 |
| P2 | Review order | The promo code applied earlier is missing from the summary | 6 Recognition over recall | 2 |
| P3 | Review order | Three banners push the order total below the fold | 8 Minimalist design | 2 |
| P4 | Payment | The tip field accepts 5000 | 5 Error prevention | 3 |
| P5 | Payment | Back from this screen empties the cart | 3 User control and freedom | 3 |
| P6 | Payment | The button says "Pay now"; the cart screen said "Checkout" for the same step | 4 Consistency and standards | 1 |
| P7 | Placing order | A spinner and no confirmation, with the button still tappable | 1 Visibility, 5 Error prevention | 4 |
| P8 | Payment failed | "Payment failed. Error 4012." with no next step | 9 Recover from errors | 3 |
| P9 | Cart | The past-orders list has no Reorder button | 7 Flexibility and efficiency | 2 |

**To build:** draw the five screens as an original mock, one issue per spot, and export as PNG. Calibration issues C1 (P7) and C2 (P1) in Appendix D reuse these screens.

---

## Further Resources

- **Nielsen's 10 Usability Heuristics (internal):** `Library/frameworks/framework-nielsen-usability-heuristics.md`
- **Severity Rating Scale (internal):** `Library/frameworks/framework-severity-rating-scale.md`
- **NN/g, 10 Usability Heuristics for User Interface Design:** https://www.nngroup.com/articles/ten-usability-heuristics/
- **NN/g, How to Rate the Severity of Usability Problems:** https://www.nngroup.com/articles/how-to-rate-the-severity-of-usability-problems/
- **W3C, WCAG 2.1 Quick Reference:** https://www.w3.org/WAI/WCAG21/quickref/

---

*Created by Winnie Nguyen · Private Training · Last updated October 2026*
