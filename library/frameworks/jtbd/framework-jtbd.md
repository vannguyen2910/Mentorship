---
title: "Jobs to Be Done (JTBD)"
type: framework            # framework | guide | template | reference
program: both               # ux-class | private-training | both
tags: [jtbd, jobs-to-be-done, motivation, user-interview, switch-interview, research-methodology]
level: intermediate
date: 2026-08-22
draft: false
download: ""
---

## What This Is

Jobs to Be Done starts from one claim: people don't buy products, they hire them to make progress on something in their life. The "job" is that progress: not who the person is, not what they demographically look like, but what they're trying to get done and why they reached for a solution to do it. A 25-year-old and a 55-year-old can be hiring the exact same product for the exact same job; two people who look identical on a persona slide can be hiring completely different jobs.

JTBD explains motivation. It answers the question friction metrics and heuristic evaluation can't: not "where does this break," but "why does the user care enough to be here at all, and what would make them leave for something else." That's what makes it a natural extension of a current-state audit: the audit tells you what's broken, JTBD tells you why it matters to the person experiencing it.

A job statement is only real once it's been tested. Written before any research, it's a hypothesis: a specific, testable guess about motivation, no different in status from an entry on an Assumption Map. It becomes an actual job only after a pattern shows up across more than one real conversation.

---

## When to Use It

- When you already know *what's* broken (from an audit, from friction analysis) but not *why* it matters enough to the user for the fix to be worth prioritising.
- Before designing anything that asks someone to change an existing behaviour: JTBD explains what would actually make someone switch, which is exactly the moment a redesign is betting on.
- To pressure-test a stakeholder's or team's assumed understanding of the customer against what the customer actually says.
- Not as a solo desk exercise. A job statement written without talking to anyone is a candidate hypothesis, not a job; treat it the same way you'd treat an unproven assumption on the map.

---

## How It Works

### Step 1 · Know the three job types

| Type | Covers | Example |
|---|---|---|
| **Functional** | The practical task being accomplished | "Get my order delivered while it's still hot, without having to track it down myself." |
| **Emotional** | How the person wants to feel, or wants to stop feeling, while doing it | "Feel confident my order hasn't been forgotten, instead of refreshing the tracking screen every few minutes." |
| **Social** | How the person wants to be seen by others while doing it | "Be seen by my family as someone who has dinner sorted, not someone anxiously staring at an app at the table." |

Most real jobs carry all three at once. A functional-only reading of a job ("the user wants to place an order") usually misses the reason the friction actually hurts.

### Step 2 · Write it as a hypothesis, using the job statement formula

> *"When [situation], I want to [motivation], so I can [expected outcome]."*

This is deliberately circumstance-first, not persona-first. It starts with the situation the person is in, not who they are; that's what separates a job statement from a persona line.

**Weak (persona dressed as a job):** "As a busy professional, I want a fast checkout."
**Strong (circumstance-first):** "When I'm waiting on a food delivery and the ETA just changed, I want to know exactly what's happening, so I can stop refreshing the tracking screen every few minutes out of anxiety it's not coming."

Until this is tested, label it clearly as a **candidate job hypothesis**, the same discipline the Assumption Map already teaches: write it in testable language, then go find out if it's true.

### Step 3 · Interview for the job, don't ask for it directly

People are bad at self-reporting motivation directly: "why did you do that?" usually gets a rationalised answer, not the real one. JTBD is typically surfaced through a **switch interview**: reconstructing the timeline of the decision, not asking someone to explain their own psychology.

| Stage | What you're listening for | Example prompt |
|---|---|---|
| **First thought** | The moment the problem first became real to them | "When did you first start thinking about this?" |
| **Passive looking** | What they were doing instead, before actively searching | "What were you doing about it before you started looking for something new?" |
| **Active looking** | What triggered them to actually start searching, and what they compared | "What made today the day you actually went looking? What else did you consider?" |
| **Deciding** | The moment of commitment, and what almost stopped them | "What almost made you not go ahead?" |
| **Using / first experience** | Whether the reality matched what they were hoping for | "Now that you're using it, is it doing what you hoped?" |

This technique assumes a real decision or switch happened. It doesn't transfer cleanly onto someone who never switched to anything, which is exactly why it isn't the right tool for a conversation with an internal stakeholder (see Common Mistakes).

### Step 4 · Derive the actual job from the pattern, not from one conversation

One interview gives you one story. The job is the pattern that repeats across several. Treat anything drawn from a single conversation as still provisional: the same "top-left, unproven" status an assumption gets before it's tested. Two to three interviews showing the same circumstance–motivation–outcome shape is what turns a candidate hypothesis into an actual job statement worth designing around.

### Step 5 · Break the job into its own stages, one job statement per stage

A single job statement captures the job's overall motivation. It doesn't capture how that motivation shifts as someone actually moves through doing it: the situation at the start of a process is rarely the situation at the end, even though it's still "the same job." Break the job into its own stages, in your own words (however many the project actually has, not a fixed universal count), and write a job statement for each one.

Most real jobs land somewhere between 3 and 6 stages. Fewer than that is usually too coarse to be useful; more than that starts turning into a full journey map instead of a job breakdown.

**Applied to the food-delivery job from Step 4:**

| Stage | Job statement |
|---|---|
| **1. Browsing** | "When I'm deciding what to eat, I want to see options that match what I'm in the mood for, so I can choose quickly without endless scrolling." |
| **2. Ordering and checkout** | "When I've picked what I want, I want to confirm the order is right before I pay, so I can trust what I'm about to be charged for." |
| **3. Waiting for delivery** | "When my order is out for delivery, I want to know it's still coming, so I can stop fearing it's not." |
| **4. Receiving the order** | "When the order arrives, I want to check it's complete and correct, so I can start eating without a second trip back to the app." |

Same job, four stages, four genuinely different situations and motivations. And the friction identified earlier ("let me stop fearing it's not coming") sits specifically at stage 3, not spread evenly across the whole thing. That's the payoff: a single job statement says the job matters; a stage-by-stage breakdown says exactly where, in language specific to this project.

**A note on lineage:** the job statement and switch-interview technique (Steps 1–4) come from Clayton Christensen and Bob Moesta's line of JTBD work: circumstance and motivation. This stage-by-stage step is adapted from Tony Ulwick's Outcome-Driven Innovation, which maps any job onto a fixed universal sequence of eight steps (Define, Locate, Prepare, Confirm, Execute, Monitor, Modify, Conclude), the same eight regardless of product. This version trades that fixed vocabulary for one that flexes per project: a small platform feature and an enterprise workflow tool don't always break down the same way. Want the original fixed eight-step version instead: it's in Ulwick's "What Customers Want."

### JTBD vs. Persona

| | Persona | JTBD |
|---|---|---|
| Answers | Who is this person? | Why did they hire this? |
| Built from | Demographics, attitudes, archetypes | Circumstance, motivation, desired outcome |
| Stable across | Products | Only this specific job; the same person has different jobs in different circumstances |
| Risk if used alone | Designs for a type of person, not a real moment of need | N/A |

---

## Example

**Candidate hypothesis (pre-interview):** "When I've placed a food order and the estimated time keeps shifting, I want a single clear signal that it's still on its way, so I can stop refreshing the tracking screen just to reassure myself."

**After 3 interviews:** All three participants described the same trigger: not the ETA itself, but a moment where the tracking screen went quiet for a few minutes and they started to wonder if something had gone wrong. None of them described actively distrusting the delivery app; all three described distrusting whether the app would actually tell them if something changed.

**Actual job (derived from the pattern):** "When my order is out for delivery and the tracking screen goes quiet, I want to know the app will tell me the moment something changes, so I never have to keep checking just to feel confident it's still coming."

**What changed:** the functional read ("show delivery status") and the real job ("let me stop fearing it's not coming") point to different design responses: one is a status indicator, the other is closer to a proactive alert the system pushes to you the moment the ETA changes, not one you have to go check for yourself.

---

## Common Mistakes

1. **Treating a pre-interview job statement as finished.** It's a hypothesis until a pattern from real interviews confirms it; write it that way, and say so out loud when presenting it.
2. **Writing a persona and calling it a job.** If the statement is about who someone is rather than the circumstance they're in, it's not a job statement yet.
3. **Running the switch-interview timeline on someone who didn't switch.** It's built to reconstruct a customer's own decision journey. Pointed at an internal stakeholder, it doesn't produce anything meaningful: a stakeholder's assumed job is an opinion to capture with the Assumption Map, not something to "interview" for using this technique.
4. **Calling it a job after one conversation.** A single interview is a story. The job is what repeats.
5. **Letting the stage-level job statements drift into unrelated jobs.** Each stage should read like a chapter of the same story; the situation changes, but they're still serving one overall job. If the stages read like completely different jobs, either the breakdown is too granular or the overall job statement wasn't well-formed to begin with.

---

## AI in Practice

### 🤖 Try this with AI

> *"Read my audit findings and current Assumption Map already saved in this project folder. Cross-check them against each other, then draft 3 candidate job statements using this format: 'When [situation], I want to [motivation], so I can [expected outcome].' Cover at least one functional, one emotional, and one social angle. Point to which existing file supports each candidate, and flag which one has the least evidence behind it. Label all three as hypotheses to be tested, not confirmed jobs."*

If your AI tool is already linked to your project folder, there's no need to re-explain the project from scratch every time. The value here is cross-checking what you've already written down against itself: not generating something new in isolation. The judgment on whether a candidate statement is genuinely circumstance-first (not a persona in disguise) is still yours; AI defaults toward demographic language unless explicitly told not to.

### 🧠 Critical thinking prompt

- Did AI's draft describe a situation, or did it quietly describe a type of person? Rewrite anything that leads with "as a [role/type]" instead of "when [situation]."
- After real interviews: which candidate hypothesis actually held up, and which one turned out to be your own assumption wearing JTBD language?

### ✍️ Prompt engineering tip

After each interview, save your notes into the project folder and ask AI: *"Cross-check my latest interview notes against my candidate-job-hypothesis.md file. Does this interview support, contradict, or complicate it? Quote the specific line that makes you say so."* Do this after every interview, not just at the end; it's faster to catch a hypothesis that's drifting after interview 1 than to discover it after interview 3.

### ⚖️ Ethics consideration

A job statement that sounds specific and well-formatted is not the same as a job statement that's actually been confirmed. AI is fluent at producing confident-sounding hypotheses; the confidence in the writing has nothing to do with whether it's true yet.

---

## Further Resources

- **Clayton Christensen, "Competing Against Luck":** The foundational book on Jobs to Be Done theory.
- **Bob Moesta, The Rewired Group:** Origin of the switch-interview method used in Step 3.
- **Tony Ulwick / Strategyn, "What Customers Want" and Outcome-Driven Innovation:** The original fixed eight-step Job Map that Step 5's flexible stage breakdown is adapted from: a distinct, process-focused lineage of JTBD from Christensen and Moesta's motivation-focused one.
- **Jobs-to-Be-Done:** https://jobs-to-be-done.com/ (background reading, already referenced from the Customer Understanding and Desk Research lessons).
- **Alan Klement, "When Coffee and Kale Compete":** Accessible introduction to job statements and the functional/emotional/social split.

---

*Created by Winnie Nguyen · Last updated August 2026*
