---
title: "Prioritisation Methods: A Reference"
type: reference            # framework | guide | template | reference
program: both               # ux-class | private-training | both
tags: [prioritisation, roadmapping, rice, moscow, kano, impact-effort, decision-making, stakeholder-alignment]
level: intermediate
date: 2026-08-29
draft: false
download: ""
---

## What This Is

A one-page reference to the five prioritisation methods you are likely to meet, so you can pick one deliberately instead of defaulting to whichever your last team used.

**The thing worth understanding before any of the mechanics:** these methods do not find the right answer. They make a judgment visible and arguable. A method's real job is to move a decision from "the loudest person wanted it" to "here is the reasoning, tell me which part you disagree with." A team that scores carefully and then overrides the score is not doing it wrong, as long as the override is said out loud. A team that scores carefully and hides the override is.

So the useful question when choosing is not "which is most accurate," it is **which one survives your organisation's politics**.

---

## When to Use It

- Before a roadmap conversation, a quarter, or a design direction where more than one option is genuinely live.
- When you need to explain a decision to someone who was not in the room while it was made.
- Not for choosing between problems on an opportunity map. That has its own assessment, which deliberately excludes effort. See `Library/frameworks/opportunity-solution-tree/framework-opportunity-solution-tree.md`.
- Not as a substitute for a decision. If the score comes out even, that is information about your options, not a reason to add another column.

---

## The Five, at a Glance

| Method | Best when | Falls over when |
|---|---|---|
| **Impact / Effort** | You need fast visual alignment in a room | Two variables cannot hold the trade-off you are actually making |
| **Desirability / Feasibility / Viability** | Criteria need to be tailored to your context | Scoring is subjective and nobody agrees who scores |
| **RICE** | You have real numbers and many items | You do not have the numbers, and the arithmetic hides that |
| **MoSCoW** | There is a fixed timebox | There is no timebox, and everything becomes a Must |
| **Kano** | The culture is feature-request driven | You have no user data to feed it |

---

## How Each One Works

### 1 · Impact / Effort Matrix

Plot each item on two axes: user value against implementation complexity. Four quadrants fall out: quick wins, big bets, money pits, fill-ins.

**Running it:** dot voting on impact, then on effort, then place the items together.

**Honest assessment:** this is the most common method because it is the fastest, and it is the one most likely to flatten a real trade-off into two dimensions that do not capture it. It is a good alignment tool and a weak analysis tool. Use it to show a decision, not to make one.

### 2 · Desirability, Feasibility, Viability

Score each item 1 to 10 on three criteria and rank by total.

| Criterion | The question |
|---|---|
| Desirability | Do users want it, and is the value distinct |
| Feasibility | Can this team build it with what it has |
| Viability | Does it make sense for the business to sustain |

**Running it:** items as rows, criteria as columns, score, total, sort. Weight the columns if one genuinely matters more, and say what the weights are.

**Honest assessment:** the most adaptable of the five, and the most vulnerable to whoever holds the pen. Have two people score independently before comparing; the disagreements are the useful output, not the average.

### 3 · RICE

**(Reach × Impact × Confidence) ÷ Effort**

| Term | How it is scored |
|---|---|
| Reach | Number of users affected in a set period |
| Impact | 0.25 minimal, 0.5 low, 1 medium, 2 high, 3 massive |
| Confidence | 25% to 100%, how much you trust your own numbers |
| Effort | Person-months |

**Honest assessment:** the confidence multiplier is the part that earns its keep, because it forces you to say out loud how much of the estimate is invented. The risk is that arithmetic reads as objectivity: a precise number built from four guesses is still four guesses. If you cannot source Reach from anything real, use a different method rather than a made-up figure.

### 4 · MoSCoW

Sort into Must have, Should have, Could have, Will not have, with weighted voting inside a fixed timebox.

**Honest assessment:** fast and easy to explain to non-designers, which is why it survives in stakeholder rooms. It has one failure mode and it is fatal: without a fixed timebox, everything becomes a Must and the exercise has sorted nothing. Set the box first. The Will Not Have column is the one that does the work, and it is the one people skip.

### 5 · Kano

Plot items on functionality against satisfaction, and sort into four types.

| Type | Behaviour |
|---|---|
| **Must-be** | Expected. Absent, it causes disproportionate dissatisfaction. Present, nobody notices |
| **Performance** | Satisfaction rises in proportion to investment |
| **Attractive** | Disproportionate delight when done well, and no penalty when absent |
| **Indifferent** | Users do not care at whatever level you build it |

Order: Performance, then Must-be, then Attractive, then Indifferent.

**Honest assessment:** the only one of the five that cannot be run without user data, which is exactly why it is the useful method in a room that has been prioritising on opinion. Its weakness is that classification needs a real survey to be honest, and a team classifying from memory has produced their own opinions in a nicer format.

---

## Choosing One

| If the room is... | Use | Because |
|---|---|---|
| Short on time and needs to align, not analyse | Impact / Effort | It is visual and everyone can participate |
| Arguing across disciplines with different criteria | DVF | The three lenses give each discipline a column to own |
| Numbers-driven, with analytics available | RICE | Confidence makes the uncertainty explicit |
| Working to a hard deadline | MoSCoW | The timebox does the prioritising, the method just records it |
| Driven by feature requests and opinion | Kano | It is the one that forces user evidence back into the conversation |

**Translating between them.** You will often do the rigorous thinking in one language and present in another, and that is not a compromise. Do the assessment properly, then show the result in whatever vocabulary the room already uses. What must not change between the two is the ranking; if it does, you have not translated, you have re-scored to fit the audience.

---

## Common Mistakes

- **Choosing the method after seeing the options.** If you pick the method that produces the answer you already wanted, the exercise is decoration.
- **Estimating effort on a problem rather than a solution.** Effort belongs to a specific solution. Pricing a problem kills valuable ones on the strength of the first expensive idea anyone imagined.
- **Precision without sources.** A RICE score of 43.7 built from four guesses is a guess with a decimal point.
- **No Will Not Have.** Every method above has a way to say no. Skipping it is what turns prioritisation into a wish list with an order.
- **Scoring alone.** The disagreements between two independent scorers are the most valuable output of any of these methods, and averaging deletes them.

---

## AI in Practice

### 🤖 Try this with AI

Point your tool at your scored list, already in your project folder: *"Here is my scored shortlist and the criteria I used. Which scores are doing the most work in the final ranking, and which ones could change by one point without changing the outcome?"* The scores that do not matter are worth knowing about before you defend them.

### 🧠 Critical thinking prompt

- Would this ranking change if a different person in the team had scored it? If yes, name the criterion they would score differently and go ask them.
- Did you choose the method before or after you knew which option you preferred?

### ⚖️ Ethics consideration

A prioritisation output looks objective and is not. Presenting a score without its assumptions, or without the confidence you actually have in the inputs, invites a room to treat a judgment as arithmetic. Say which numbers were sourced and which were estimated, in the same breath as the total.

---

## Further Resources

- **NN/g, "5 Prioritization Methods in UX Roadmapping":** https://www.nngroup.com/articles/prioritization-methods/
- **Opportunity Solution Tree framework (internal):** `Library/frameworks/opportunity-solution-tree/framework-opportunity-solution-tree.md`, for choosing between problems rather than solutions, and why effort is excluded there
- **Noriaki Kano, the Kano model:** the original two-dimensional quality theory behind method 5

---

*Created by Winnie Nguyen · Last updated August 2026*
