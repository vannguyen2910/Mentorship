---
title: "Opportunity Solution Tree"
type: framework            # framework | guide | template | reference
program: private-training   # ux-class | private-training | both
tags: [opportunity-solution-tree, opportunity-mapping, problem-definition, prioritisation, outcome, continuous-discovery, jtbd]
level: senior-lead
date: 2026-08-29
draft: false
download: ""
---

## What This Is

An Opportunity Solution Tree is a map of a decision, not a map of a customer. It hangs everything off one outcome you are trying to move, lists the unmet customer needs that could plausibly move it, and only then lets solutions into the room.

The structure has four layers:

| Layer | What sits here | Where it comes from |
|---|---|---|
| **Outcome** (root) | One product outcome: a customer behaviour you want more or less of | Chosen with the business, not invented by design |
| **Opportunity space** | Customer needs, pains and desires, in the customer's language | Interview evidence, never a brainstorm |
| **Solutions** | Multiple candidate responses per opportunity | Ideation, after the opportunity is chosen |
| **Assumption tests** | The experiment that would tell you a solution is worth building | Written before building, not after |

The layer that does the real work is the second one. Most teams have no opportunity space at all: they have a backlog, which is a solution list with the reasoning deleted. A tree makes the reasoning visible again, so a solution can be argued about on the grounds of the need it serves rather than on whoever asked for it loudest.

**The root is a behaviour, not a business metric.** "Increase revenue" cannot be the root, because nothing below it can be judged against it. "More customers get through waiting-for-delivery without checking the tracking screen to reassure themselves" can, because every candidate opportunity underneath it either plausibly moves that behaviour or does not.

---

## When to Use It

- When you already understand what customers are trying to get done and now have more valid problems than you have capacity to solve.
- When you are about to be asked "why this and not that," which is the question a tree is built to answer.
- At the moment a roadmap, a quarter, or a design direction is being set, not in the middle of executing one.
- **Not** before you have talked to customers. A tree built from internal knowledge is a backlog with new headings.
- **Not** as a company-wide artefact. One tree belongs to one team working on one outcome; a tree that tries to hold everything holds nothing.

---

## How It Works

### Step 1 · Set the root

Take what you already know about the customer's job and restate it as a behaviour you want more of. Test the root against three failure shapes:

| Bad root | Why it fails | Fixed |
|---|---|---|
| "Increase revenue 15%" | A business metric. Nothing below it can be judged against it | "More customers complete checkout in one sitting" |
| "Launch the new status page" | An output. It is a solution wearing a target's clothes | "Fewer customers need to check on their own order" |
| "Improve the customer experience" | Unfalsifiable. No behaviour named, so nothing can fail | "Customers stop re-confirming orders they've already placed" |

One root per tree. Two roots means two trees, or an unresolved argument about priorities that is now hiding inside a diagram.

### Step 2 · Harvest the opportunity space from evidence you already have

Walk your existing research artefacts stage by stage and lift out what is already written. Nothing new is invented at this step. Each gap, each insight, each recurring friction becomes a candidate opportunity.

If nothing can be harvested because there is no research behind you, stop. The tree is not the problem to solve first.

### Step 3 · Rewrite each one in the customer's language

An opportunity is a need, a pain, or a desire, described the way the person experiencing it would describe it. Not a feature, not a capability, not a screen.

**The three-solutions test:** name three genuinely different ways you could address it. If you cannot, what you have written is a solution, not an opportunity, and it needs rewriting one level up.

| Written as | Three solutions? | Verdict |
|---|---|---|
| "Push a proactive alert when the ETA changes" | No. That is the solution | Solution in disguise |
| "I need to know the app will tell me the moment something changes, without going to look" | Yes: a proactive alert, a promise stated up front about when we will contact you, a courier message channel | Opportunity |

### Step 4 · Tag every opportunity with its stage and its evidence count

Two tags, both short, both load-bearing later:
- **Stage:** where in the customer's job this sits. Without it, a recommendation cannot be scoped, and "we should fix the job" is not a recommendation.
- **Evidence count:** how many separate conversations it appeared in. A one-source opportunity is not disqualified, it is labelled, so nobody treats it as settled by accident.

### Step 5 · Prune and group

Drop anything that cannot plausibly move the root outcome, however true it is. A true finding that does not serve this outcome belongs in your research file, not on this tree. Group siblings under a parent where they share a cause, so the tree reads as a small number of real choices rather than a flat list of twenty items.

### Step 6 · Assess, and leave effort out of it

Compare opportunities on four factors:

| Factor | The question |
|---|---|
| **Opportunity sizing** | How many customers hit this, and how often |
| **Customer factors** | How important is it to them, and how satisfied are they with what exists today |
| **Company factors** | Does addressing it fit what this company is actually trying to be |
| **Market factors** | Does it change our position against alternatives |

**Effort is deliberately excluded at this layer.** Different solutions to the same opportunity vary enormously in cost, so pricing effort before you have explored solutions kills valuable problems on the strength of the first expensive idea anyone happened to imagine. Effort enters one layer down, when comparing solutions to the opportunity you have already chosen.

Most organisations do not speak this language, they speak impact and effort. Translate rather than fight: the four factors above produce your impact judgment, defensibly, and effort gets attached later at the solution layer. Score the opportunity in the language above, present it in the language the room uses.

---

## Opportunity Map vs. JTBD Map

Both are built from the same interviews. Both hang items off a spine. The difference is what they are for, and a mentee who misses it produces the JTBD map again with different headings.

| | JTBD map | Opportunity map |
|---|---|---|
| Question it answers | What is the customer actually trying to get done, and where does our understanding diverge from theirs | Given the outcome we want to move, which unmet need do we bet on |
| Organising spine | The customer's own sequence of stages | One product outcome, at the root |
| Unit on the map | A job statement, per stage | An opportunity: a need, pain or desire in the customer's language |
| Built from | Switch-timeline interviews plus the stakeholder check-in | The gaps and insights already written on the JTBD map |
| Whose thing it is | The customer's reality. You are recording it | Your team's choice. You are defending it |
| How often it changes | Rarely. The job is stable even as solutions change | Often. It moves whenever the target outcome or the evidence moves |
| Does it hold solutions | Not as its structure, though a JTBD map usually carries one opportunity sticky per pain point. Those are solutions attached to pains, not a ranked decision space | Yes, one layer below opportunities, and only once the opportunity is chosen |
| Failure mode | A persona in disguise: demographics and attitudes instead of a job | A feature list in disguise: solutions written as if they were needs |
| One-line test | Could a completely different product satisfy this job? If no, it is not a job, it is your product described | Can you name three different solutions for this? If no, it is not an opportunity, it is a solution |

**Why the second map has to exist.** A JTBD map can tell you a dozen true things and still not tell you what to do on Monday, because it has no target and no ranking. Nothing inside it can say which stage matters most, since importance is a property of what the business is trying to achieve, not of the customer's journey. The opportunity map adds the missing ingredient, one outcome at the root, and everything below earns its place by plausibly moving it.

**Why they should not be merged.** The moment you rank stages by business value, you have stopped describing the customer and started arguing for a plan. Both are legitimate; keeping them in separate files is what lets you change the plan next quarter without quietly rewriting your account of the customer to match.

**Two wrong-tool signals:**
- Building an opportunity map with no interviews behind it. The needs will be manufactured, and they will happen to match what the team already wanted to build.
- Building another JTBD map when the real question is prioritisation. That is research used to postpone a decision.

---

## Example

Carrying forward the food-delivery job from `Library/frameworks/jtbd/framework-jtbd.md`, where the actual job derived from interviews was *"let me stop fearing it's not coming,"* sitting at the waiting-for-delivery stage.

**Root outcome:** More customers get through waiting-for-delivery without checking the tracking screen to reassure themselves.

**Opportunity space, harvested from the stage map:**

| Opportunity (customer language) | Stage | Evidence |
|---|---|---|
| "I need to know nothing has gone wrong" | Waiting for delivery | 3 of 3 interviews |
| "I need to know what's actually happening without hunting for it" | Waiting for delivery | 3 of 3 |
| "I need to know what happens next, and roughly when" | Waiting for delivery | 2 of 3 |
| "I need to be sure my order is right before I pay" | Ordering and checkout | 1 of 3, unconfirmed |
| "I need to reach a person when the app cannot tell me anything" | Waiting for delivery | 1 of 3, unconfirmed |

The last two are real and stay on the map, labelled. They are not pruned for being single-source, and they are not treated as settled either. The final one matters more than its count suggests, because it is also the source of a useful reframe: the one participant who stopped refreshing wanted a person on the line, which suggests the settling thing might be a channel rather than a better countdown. Enough to generate a reframe, not enough to justify a bet.

**What it is not:** "Add a progress tracker," "Send push notifications," "Redesign the tracking screen." All three are solutions, and all three belong one layer down, attached to whichever opportunity wins.

---

## Common Mistakes

- **Manufacturing opportunities.** Skipping interviews and generating needs from internal knowledge. The tree will faithfully reproduce the team's existing biases in customer-sounding language.
- **Solutions dressed as opportunities.** Anything that fails the three-solutions test. This is the most common failure and the easiest to catch.
- **A business metric at the root.** Everything below becomes unjudgeable, and the tree turns into decoration.
- **Over-indexing on a single source.** One interview or one loud support ticket driving a branch, without the evidence count visible next to it.
- **Pricing effort too early.** Killing a valuable problem because the first solution anyone imagined was expensive.
- **Perfecting the map instead of using it.** The tree exists to support a decision this week. A beautiful tree that has not chosen anything has done no work.
- **One tree for the whole company.** It becomes unmaintainable, and no one team can act on it.

---

## AI in Practice

### 🤖 Try this with AI

With your AI tool already linked to your project folder, point it at your JTBD map and your interview notes: *"Convert every gap, pain point and opportunity sticky on my JTBD map into candidate opportunities written in customer language. For each one, tag the stage it came from and count how many separate interviews support it. Flag anything that fails the three-solutions test as a solution in disguise, including the opportunity stickies I wrote myself."*

The judgment about what stays on the tree is still yours. AI is fluent at producing plausible needs, including ones that appear in none of your interviews.

### 🧠 Critical thinking prompt

- For each opportunity on your tree, can you point at the line in an interview note that put it there? Anything you cannot trace came from you, not from a customer.
- Does your root outcome name a behaviour, or does it name a result you want the business to have? If a stakeholder could hit it without any customer doing anything differently, it is the wrong root.

### ✍️ Prompt engineering tip

Ask for the failure mode, not the output: *"Read my opportunity map and tell me which items are solutions wearing opportunity language, which are supported by only one interview, and which could not plausibly move the root outcome even if fully solved."* A critique prompt against a file you wrote is more useful than a generation prompt against an empty one.

### ⚖️ Ethics consideration

An opportunity map is an argument for spending other people's time and money. Presenting a single-source opportunity without its evidence count, or a manufactured one alongside evidenced ones, is not a formatting choice. Keep the counts visible in the version you show stakeholders, not just in your working file.

---

## Further Resources

- **Teresa Torres, "Continuous Discovery Habits":** The origin of the Opportunity Solution Tree and the assessment factors used in Step 6.
- **Teresa Torres, Product Talk, "Opportunity Solution Trees":** https://www.producttalk.org/opportunity-solution-trees/
- **Jobs to Be Done framework (internal):** `Library/frameworks/jtbd/framework-jtbd.md`, the map this one is built from.
- **Assumption Map framework (internal):** `Library/frameworks/assumption-map/framework-assumption-map.md`, the discipline for handling anything not yet evidenced.
- **NN/g, "5 Prioritization Methods in UX Roadmapping":** https://www.nngroup.com/articles/prioritization-methods/, for translating an assessment into the language your organisation already uses.

---

*Created by Winnie Nguyen · Last updated August 2026*
