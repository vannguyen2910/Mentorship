---
title: "Problem Definition & Strategy: Lesson Brainstorm"
type: brainstorm
program: private-training
level: senior-lead
status: built
date: 2026-08-29
previous-session: "Customer Understanding (Senior/Lead)"
---

# Problem Definition & Strategy: Lesson Brainstorm

Working document that shaped the Define-stage session following Customer Understanding (Senior/Lead) in the private training track. Desk research plus the session shape.

**Built, 2026-08-29.** The lesson pair now exists: `problem-definition-strategy-lesson.md` and `problem-definition-strategy-slide-outline.md` in this folder, plus `library/frameworks/opportunity-solution-tree/framework-opportunity-solution-tree.md`. This file stays as the research and reasoning record; the lesson file is the source of truth for content from here on.

**Scoping decisions locked in (2026-08-29):**
- Format: one combined 90 minute session, problem definition and strategy together.
- Scope of "strategy": project-level design strategy (diagnosis, guiding policy, design principles, actions, non-goals). Roadmap, quarterly bets and team allocation stay out, they belong with `leader-level/estimating-design-effort`.
- Metrics: teach the full business metric to product outcome to output chain, with an explicit proxy and leading-indicator fallback for mentees who have no analytics access.
- Placement: its own topic folder, `02-define/problem-definition-strategy/materials/`. Initially folded into `synthesis-problem-definition-in-ux/` on the Customer Understanding same-folder convention, then moved out on 2026-08-29: that convention pairs two levels of one topic, and these are two different sessions with different methods, outputs and next-session links. The folder name `synthesis-problem-definition-in-ux` does not describe this session either.

**What the mentee walks in holding**, straight out of the last session:
- `jtbd-map.md`: stage map, stakeholder-assumed job, actual job derived from 2 to 3 interviews, and the gap between them
- `insight-synthesis-template.md`: insights written in the three-leg formula (observation, implication, recommended decision, scoped to a stage)
- `stakeholder-readout-template.md`: an implication-first readout, already pitched once
- An updated Assumption Map from Audit & Desk Research

They have evidence and they have insight. What they do not have is a decision about which problem the team is going to spend the next quarter on, or a defensible reason for the ones they are not touching.

---

## 1. The Problem This Lesson Solves

Three failure modes, all specific to the senior-to-lead transition:

1. **Too many valid problems.** Research produces a dozen defensible insights. A junior designer picks the most interesting one. A senior is expected to choose the one with the strongest link to a business outcome, and to be able to say why the other eleven lost.
2. **Problem statement mistaken for strategy.** "Users need a way to X because Y" is a well-formed problem statement and still not a strategy. It names a gap but not an approach, not a set of trade-offs, and not what the team will refuse to do. Stakeholders read it, agree with it, and change nothing.
3. **No line from problem to measurable outcome.** The design gets shipped, the deck says "improved usability," and nobody can tell six months later whether the bet paid. Senior designers get asked this question; junior ones usually do not.

Root cause across all three: the Define stage is usually taught as a synthesis exercise (cluster, label, write a statement) rather than as a decision under uncertainty with an opportunity cost attached. Synthesis produces clarity. Strategy produces commitment, which is a different and less comfortable skill.

---

## 2. Part A: Problem Definition at Senior Level, What the Research Says

### 2a. Reframing before defining (Wedell-Wedellsborg)

The HBR research behind *What's Your Problem?* surveyed 106 C-suite executives; 85% said their organisations were bad at problem diagnosis. The central line is worth teaching verbatim: "The point of reframing is not to find the 'real' problem but, rather, to see if there is a better problem to solve." That reframes reframing itself as an option-generation move, not a truth-finding one, which is the distinction most designers miss.

Seven listed practices: establish legitimacy, bring outsiders into the discussion, get people's definitions in writing, ask what's missing, consider multiple categories, analyse positive exceptions, question the objective. Seven is too many for a 90 minute session. Three of them carry most of the weight for a designer working from research data:
- **Question the objective**: whose goal is this, and what happens if that goal is wrong
- **Analyse positive exceptions**: which users already succeed at this job, and what is different about them (this one maps directly onto a JTBD stage map, since the mentee already has stage-level data)
- **Ask what's missing**: what does the current problem framing leave entirely out of the frame

This is the piece the existing Junior lesson does not teach at all. The Junior pipeline goes observation to insight to HMW to problem statement in one direction, with no step that challenges whether the framing itself is the right one.

### 2b. Problem statements as scoping artefacts (NN/g)

NN/g's definition: "a concise description of the problem that needs to be solved," carrying three components, the background and context, who is affected and how, and the organisational impact if it goes unresolved. That third component is the senior-level addition. Junior problem statements name the user and the barrier. Senior ones also name what it costs the business to leave it alone, which is what makes the statement fundable.

Their named pitfalls: solutioneering during discovery, laundry lists of unrelated problems, and starting without clear problem direction. Note also that NN/g treats a problem statement as something that gets refined throughout discovery and can shift when new evidence arrives, which supports teaching it as a versioned living file rather than a one-time output.

**The upgrade to teach, not the formula.** A senior mentee already knows the Junior formula, `[user] needs a way to [goal] because [barrier]`. Re-teaching it wastes the session. What they have not been taught is the version that survives a funding conversation, which adds three things the Junior formula leaves out:

- **The organisational cost of leaving it alone.** NN/g's third component. Without it a problem statement is true, agreed with, and unfunded.
- **A scope boundary.** Which JTBD stage this sits in, so the statement names a place in the journey rather than the whole product.
- **The evidence base, stated out loud.** How many conversations it rests on. A senior is expected to volunteer this number before being asked.

Teach it as a side-by-side upgrade of a statement they already wrote, roughly 90 seconds inside the diagnosis teaching, not as a new concept with its own block.

**Three artefacts that get confused, worth separating explicitly.** An **opportunity** is a customer need, stated in their terms, sitting in the tree. A **problem statement** is the one opportunity that got chosen, framed, and priced. A **diagnosis** is that same statement doing strategic work at the top of a brief. They are not three exercises, they are one sentence at three stages of promotion. A **How Might We** is the fourth thing and it belongs to the next stage, since its job is to open solution space, not close problem space.

### 2c. Opportunity space over problem list (Teresa Torres)

The Opportunity Solution Tree is the strongest structural fit for what this mentee already has, because it was designed to sit directly on top of interview data. Four levels: a single **outcome** at the root (a product outcome measuring customer behaviour, not a business metric and not feature adoption), an **opportunity space** of customer needs and pain points sourced from interviews, **solutions** (plural per opportunity), and **assumption tests**.

Two points that matter for teaching:
- Opportunities must come from story-based interviews, not internal brainstorming: "When we generate opportunities off the top of our heads, we bring our own biases and half-truths into the picture." The stated minimum before mapping is 3 to 4 interviews. The last session asked for 2 to 3, so this is nearly aligned and worth a note in the lesson.
- **Effort is deliberately excluded** from opportunity assessment. Assessment criteria are opportunity sizing (reach and frequency), market factors, company factors, and customer factors (importance and satisfaction with existing solutions). The rationale: different solutions to the same opportunity vary wildly in complexity, so pricing effort at opportunity level kills viable problems early. This is a genuinely counterintuitive teaching point for designers who default to an impact/effort 2x2.

Common mistakes named: manufacturing opportunities without interviews, confusing an opportunity with a solution, over-indexing on one interview or one support ticket, and building company-wide trees instead of one per product team.

### 2d. Choosing one: prioritisation methods (NN/g's five)

Worth teaching as a menu with selection criteria rather than a single method:
- **Impact/effort matrix**: quadrants of quick wins, big bets, money pits, fill-ins. Fast, democratic, oversimplifies to two variables.
- **Desirability / feasibility / viability scorecard**: 1 to 10 across three criteria, weightable. Adaptable, but scoring is subjective.
- **RICE**: (Reach x Impact x Confidence) / Effort, with impact scored 0.25 to 3 and confidence 25 to 100%. Rigorous, needs metrics the mentee may not have access to.
- **MoSCoW**: must / should / could / will not, with weighted dot voting. Easy, and the Must column overloads without a fixed timebox.
- **Kano**: attractive, performance, indifferent, must-be. Forces user data into the room, useful specifically in politically driven or development-led cultures.

For a senior audience the interesting content is not the arithmetic, it is the meta-question: which method survives your organisation's politics. RICE loses to a loud stakeholder unless the confidence number is defensible. Kano is the one that reintroduces user evidence into a feature-request culture.

---

### 2e. JTBD map vs opportunity map: the bridge teaching block

Both maps are built from the same interviews, both hang things off a spine, and both live as markdown files in the mentee's project folder. Without an explicit comparison the mentee will treat the second as a reformat of the first, and the opportunity map will come out as the JTBD map with different headings. This block prevents that, and doubles as the instructions for activity 1.

**What each one is.** The JTBD map describes the customer's world as it is: the stages of the job, the job statement at each stage, what the stakeholder assumed, what the customer actually said, and the gap between them. The opportunity map describes the team's decision space: one outcome you are trying to move, and the unmet needs that could plausibly move it. The first is an evidence layer. The second is a decision layer, and it is an argument rather than a record.

| | JTBD map | Opportunity map |
|---|---|---|
| Question it answers | What is the customer actually trying to get done, and where does our understanding diverge from theirs | Given the outcome we want to move, which unmet need do we bet on |
| Organising spine | The customer's own sequence of stages | One product outcome, at the root |
| Unit on the map | A job statement, per stage | An opportunity: a need, pain or desire in the customer's language |
| Built from | Switch-timeline interviews plus the stakeholder check-in | The gaps and insights already written on the JTBD map |
| Whose thing it is | The customer's reality, you are recording it | Your team's choice, you are defending it |
| How often it changes | Rarely. The job is stable even as solutions change | Often. It moves whenever the target outcome or the evidence moves |
| Does it hold solutions | Never | Yes, in the layer beneath opportunities, though not in this session |
| Failure mode | A persona in disguise: demographics and attitudes instead of a job | A feature list in disguise: solutions written as if they were needs |
| One-line test | Could a completely different product satisfy this job? If no, it is not a job, it is your product described | Can you name three different solutions for this? If no, it is not an opportunity, it is a solution |

**Why the second map exists at all.** A JTBD map can tell you a dozen true things and still not tell you what to do on Monday, because it has no target and no ranking. Nothing in it says which stage matters most, because importance is a property of what the business is trying to achieve, not of the customer's journey. The opportunity map introduces the missing ingredient, a single outcome at the root, and everything below it earns its place by plausibly moving that outcome. That is also why the two cannot be merged: the moment you rank stages by business value, you have stopped describing the customer and started arguing for a plan, and the description is worth keeping clean.

**When to reach for which.** The JTBD map is the right tool when you do not yet know what people are trying to accomplish, when the stakeholder view and the customer view might diverge, or when you need to show that you understand the customer before proposing anything. The opportunity map is the right tool when you already have that understanding plus enough interviews, when you have more valid problems than capacity, and when someone is about to ask why this and not that. Two wrong-tool signals worth naming: building an opportunity map with no interviews behind it is Torres's manufacturing mistake, and building yet another JTBD map when the real question is prioritisation is research used to postpone a decision.

**How to convert one into the other**, which is exactly what activity 1 runs:

1. **Set the root.** Take the actual job statement from `jtbd-map.md` and restate it as a customer behaviour you want more of. Not revenue, not adoption, not a feature being used.
2. **Harvest.** Walk the stages. Every gap and every insight already written becomes a candidate opportunity. Nothing new gets invented at this step.
3. **Rewrite in customer language.** A need, pain or desire, never a feature. Apply the three-solutions test to each one and rewrite anything that fails it.
4. **Tag.** Each opportunity carries the stage it came from and the number of interviews it appeared in. This is what makes the map defensible later.
5. **Prune and group.** Drop anything that cannot plausibly move the root outcome, group siblings under a parent where they share a cause, and mark single-source items as unconfirmed.

This comparison is a strong candidate to live in `library/frameworks/opportunity-solution-tree/` rather than only inside the lesson, since the mentee will need it again on the next project.

---

## 3. Part B: Strategy, What the Research Says

### 3a. Rumelt's kernel, the spine of the second half

*Good Strategy / Bad Strategy* gives the cleanest structure for turning a defined problem into a strategy, and it scales down from corporate to a single design initiative without distortion. Three parts:
- **Diagnosis**: "defines or explains the nature of the challenge by identifying certain aspects of the situation as critical." A judgment, not a provable fact. This is exactly what a well-framed problem statement is.
- **Guiding policy**: "an overall approach chosen to cope with or overcome the obstacles identified in the diagnosis." Directional and memorable, not a task list.
- **Coherent actions**: coordinated steps that carry out the policy, which reinforce rather than contradict each other.

The bad-strategy half is arguably the better teaching material, because it names what designers actually produce: goals mistaken for strategy ("increase sales 20%" is a goal with no diagnosis attached), fluff, failure to face the challenge, and jumping straight to actions, which Rumelt calls wishful thinking. A design equivalent to show side by side: "redesign the onboarding flow" is an action with no diagnosis and no policy behind it.

Mapping this onto what the mentee already holds is tidy: the JTBD gap becomes the diagnosis, design principles become the guiding policy, and the roadmap of design moves plus explicit non-goals becomes the coherent action set.

### 3b. Design principles as the guiding policy (NN/g)

NN/g frames design principles as decision-making support, and that is the framing to teach: a principle earns its place only if it can settle an argument between two reasonable options. Three to five is the commonly cited working number. The test to give mentees: if the inverse of your principle is obviously stupid, the principle is fluff. "Be user friendly" fails. "Favour recovery over prevention: let people act, then make undo cheap" passes, because a team could reasonably choose the opposite.

### 3c. Design strategy as translation to business terms

The recurring theme across the practitioner sources: design strategy is the bridge from business objective to design initiative, and it has to be stated in business terms rather than aesthetic ones. Named components across sources: business alignment, research findings, competitive position, three to five design principles, an initiative roadmap, resourcing, success metrics, and a governance or decision-rights model. Worked example of the translation: a business goal of "increase self-service adoption by 30%" becomes a design initiative to "redesign the help centre with better search and contextual guidance."

For a 90 minute lesson, resourcing and governance are out of scope. They belong with `leader-level/estimating-design-effort`, which is a natural companion session.

### 3d. Outcome vs output, and the metric

The root of an Opportunity Solution Tree is a product outcome, defined as a measure of customer behaviour or sentiment, deliberately not a business metric and not feature adoption. That distinction is the whole content of this block. A useful three-level chain to teach, since most mentees can only influence the middle one directly:
- Business metric (revenue, cost to serve) which design influences indirectly
- Product outcome (a behaviour changed) which design owns
- Output (screens shipped) which is not evidence of anything on its own

Realistic constraint worth flagging: many mentees have no analytics access. The lesson needs a fallback for defining a proxy or leading indicator that is observable without a dashboard, otherwise this block becomes theory.

---

## 4. On the Existing "Synthesis & Problem Definition" Lesson

Short answer: related, but this should not be a senior re-run of it. It should start where that one stops.

The existing `02-define/synthesis-problem-definition-in-ux` is a UX Class session for an intermediate audience, built as a four-step pipeline (affinity mapping, insight statements, How Might We, problem statement) run as a facilitated workshop on a recipe app practice dataset. Its subject is **synthesis mechanics**: how to get from sticky notes to one clear statement, with the designer acting as workshop facilitator.

Three reasons to keep them distinct rather than build a senior variant of it:

1. **The senior mentee has already done the synthesis.** Their insights are written, in a three-leg formula that already goes further than the Junior lesson's observation-plus-implication definition, since it also names a recommended decision. Re-teaching affinity mapping to someone who arrives holding a JTBD map and finished insight statements would waste the session.
2. **The pipeline stops one step short of the actual senior job.** It ends at a single problem statement, assumed to be the right one. It contains no reframing step, no opportunity comparison, no prioritisation, and no strategy layer. The senior failure mode is not writing a bad problem statement, it is committing to the wrong problem confidently.
3. **The unit of work is different.** The Junior lesson's output is an artefact from a workshop. The senior lesson's output is a bet with an opportunity cost, defended to people who can overrule it.

What should carry over: the ladder-of-abstraction framing, the insight formula (already extended in Customer Understanding), and the workshop-facilitation mindset, which stays relevant since a senior runs the room. HMW is the one piece worth keeping in shortened form, as the bridge from a chosen opportunity into solution space, but as a five minute recap rather than a taught step with its own activity.

**Decided:** two separate topic folders in `02-define/`. The Customer Understanding same-folder convention was tried first and reversed, because it pairs two *levels of one topic* and these are two *different sessions*: different methods, different outputs, different next session, and a folder name that only describes one of them. The Junior files were renamed at the same time to the library's standard `topic-lesson.md` / `topic-slide-outline.md` shape.

---

## 5. Continuity from Customer Understanding: the Input / Output Chain

The rule this session is built on: **no activity starts from a blank page.** Every activity takes its input either from the previous session's deliverable or from the activity immediately before it, and every output writes into one of two files rather than a fresh worksheet. If an activity can be run without opening something the mentee already has, it is the wrong activity.

The spine across the whole private training track:

`assumption-map.md` (Audit & Desk Research) to `jtbd-map.md` (Customer Understanding) to `opportunity-map.md` (this session, activities 1 to 3) to `problem-brief.md` (this session, activities 4 to 6) to the stakeholder pitch.

The single most important join: **the JTBD gap becomes the diagnosis.** Customer Understanding ends by comparing what the stakeholder assumed the customer's job was against what the interviews showed it actually is, scoped to a stage. In Rumelt's kernel a diagnosis is precisely that, a judgment naming which aspect of the situation is critical. So the mentee is not writing a new problem in this session, they are promoting a finding they already hold into the top of a strategy.

### The six activities, chained

| # | Activity | Input, and where it comes from | Technique or framework | Output |
|---|---|---|---|---|
| 1 | Map your opportunity space | The gaps in `jtbd-map.md` plus the insights in `insight-synthesis-template.md`, one opportunity per gap. The root outcome is the actual job statement restated as a customer behaviour, so they arrive with the root already written. | Opportunity Solution Tree (Torres), run through the five conversion steps in section 2e | `opportunity-map.md` parts 1 and 2: outcome at the root, opportunity space beneath it, each opportunity tagged with the JTBD stage it came from and the number of interviews it appeared in |
| 2 | Reframe the top branch | The highest-value branch from activity 1 | Reframing (Wedell-Wedellsborg), three practices only: question the objective, analyse positive exceptions (run directly against the JTBD stage map, which customers already clear this stage and what is different about them), ask what is missing | `opportunity-map.md` part 3: two alternative framings of that opportunity, one kept, one line on why the other lost |
| 3 | Score, commit, and state it | The kept framing from activity 2, held against the rest of the opportunity space from activity 1 | Torres's opportunity assessment first (sizing, market factors, company factors, customer factors, effort deliberately excluded), then translated into whichever of the NN/g five the mentee's organisation actually speaks, usually impact/effort or a DVF scorecard. Closes by writing the senior-grade problem statement: user, goal, barrier, organisational cost, JTBD stage, evidence base | `opportunity-map.md` part 4: the chosen problem written as one statement, the runner-up, and the written reason the runner-up lost |
| 4 | Write the problem brief | The problem statement written at the end of activity 3, which becomes the diagnosis verbatim rather than being rewritten | Rumelt's kernel. Design principles as the guiding policy, each run through the fluff test (state the credible opposite, or cut it) | `problem-brief.md` parts 1 to 4: diagnosis, guiding policy (3 principles), coherent actions, explicit non-goals |
| 5 | Name the measure | The brief from activity 4, specifically the behaviour named in the diagnosis | Business metric to product outcome to output chain, with a proxy or leading indicator fallback where there is no analytics access | `problem-brief.md` part 5: success measure, plus how it will be observed |
| 6 | Defend the bet | The finished brief | Headline-first, implication-first pitch structure carried over from Audit & Desk Research, plus a pushback drill on the one question that is new this session | HTML one-pager rendered from `problem-brief.md`, per the track convention that content lives in markdown and visualisation lives in HTML |

### Notes on the chain

**The problem statement is the hinge, not a separate step.** It is written at the tail of activity 3 and carried into activity 4 as the diagnosis, unchanged. That is the promotion chain the mentee should be able to point at afterwards: opportunity, then chosen and framed problem statement, then diagnosis. One sentence, three stages, no rewriting between them. Writing it inside activity 3 also fixes the tightest block in the session, since activity 4 no longer has to produce a diagnosis from a concept, it places a sentence it already has.

**How Might We is deliberately not here.** It opens solution space, which is the job of `03-develop/develop-solutions-ideate`. Mentioning it in the close as the next stage's first move is enough; giving it time in this session would blur the line the whole lesson is trying to hold, which is that problem space closes before solution space opens.

**Where it could break.** Two activities are at risk of drifting into generic exercises. Activity 2's reframing becomes a creativity game unless it is anchored to the stage map, so the positive-exceptions practice is the one to lead with, since it cannot be done without stage-level data. Activity 5's metric becomes theory unless it is tied to the specific behaviour named in the diagnosis, so it is written into the brief rather than discussed in the abstract.

**Evidence gate.** Torres puts the minimum at 3 to 4 interviews before mapping an opportunity space. Customer Understanding asks for 2 to 3. A mentee arriving with two is one interview short, so `opportunity-map.md` is labelled provisional and the assignment carries one more interview, rather than the map being treated as settled.

**Contrast to state out loud in block 1.** Customer Understanding also ended with a stakeholder pitch, so without naming the difference this one reads as a repeat. Last session pitched a finding, and the hard question was "how do you know". This session pitches a commitment with an opportunity cost, and the hard question is "why not the other one". Same audience, same template, different burden of proof.

**1:1 adaptation.** The source material for most of these techniques assumes a team workshop: silent clustering, dot voting, group scoring. Private training has one mentee, so group mechanics are replaced by forced ranking, a written scorecard, and the mentor playing the sceptical stakeholder. Worth stating in the lesson, since a mentee who later runs these as team workshops needs to know which parts were compressed for the 1:1 format.

**Possible new framework doc.** `library/frameworks/opportunity-solution-tree/framework-opportunity-solution-tree.md`, following the pattern already set by `assumption-map` and `jtbd`, so the tree is taught from a standalone reusable file rather than embedded in this one lesson. Decide before the build.

---

## 6. Session Shape (90 min slot, 85 min scripted)

Reworked from the first twelve-block draft, which alternated teaching and activity five times. A senior learner loses more to that switching than a junior does, and the twelve-block version also hid the two files the session exists to produce. This version runs three teaching runs and three build blocks, with each build block completing a file.

| # | Block | Content | Duration |
|---|---|---|---|
| 1 | Open | From a defensible problem to the right problem. Names the two files this session produces, and the question the pitch will face at the end | 3 min |
| 2 | Teach A | JTBD map vs opportunity map (what, why, when, how, per section 2e), then opportunity space and reframing: outcome at the root, effort excluded, and the three reframing practices as operations on the tree | 15 min |
| 3 | Build 1 | Opportunity map: run the five conversion steps against `jtbd-map.md`, then reframe the top branch two ways and keep one. Completes `opportunity-map.md` parts 1 to 3. Activities 1 and 2 | 14 min |
| 4 | Teach B | Choosing: opportunity assessment criteria, translating them into the prioritisation language the organisation already speaks, and the senior problem-statement upgrade | 5 min |
| 5 | Build 2 | Score, commit, state it. Completes `opportunity-map.md` part 4 and the problem statement. Activity 3 | 9 min |
| 6 | Teach C | The strategy argument in one run: Rumelt's kernel, bad strategy in a design deck, principles as decision rules with the fluff test, outcome versus output with the proxy fallback | 9 min |
| 7 | Build 3 | The problem brief end to end: place the statement as the diagnosis, three principles, coherent actions, non-goals, measure. Completes `problem-brief.md`. Activities 4 and 5 | 16 min |
| 8 | Defend | Pitch the bet, take the pushback drill on "why not the other one", then coaching feedback on the answer. Activity 6 | 11 min |
| 9 | Close | Assignment, and How Might We named as the next stage's first move | 3 min |

The six chained activities from section 5 all survive, grouped rather than cut. What the rework fixed: the weak four-minute teaching block feeding a scattered scoring activity is gone, since the choosing teaching now carries the problem-statement upgrade that was wrongly parked in the strategy block; the strategy teaching is one continuous argument, diagnosis to policy to action to how you would know, rather than being interrupted by a separate metrics block; and the defence gets eleven minutes, enough for the pitch, the pushback and the coaching conversation, which is where the senior skill actually gets built.

**Facilitation note to write into the lesson:** a sixteen-minute build block goes quiet in a 1:1. Each build block needs a checkpoint at roughly the halfway mark where the mentee says out loud what they have so far, so the mentor catches a wrong turn before the block ends rather than after.

**Proposed living assets:**
- `opportunity-map.md`: the tree, rooted in one outcome, sourced from `jtbd-map.md`. Third living file in the track, after the Assumption Map and the JTBD map.
- `problem-brief.md`: the one-pager. Diagnosis, guiding policy (the principles), coherent actions, non-goals, success measure, and the runner-up problem with the reason it lost. This is the session's real deliverable and the artefact the mentee will reuse on every project afterwards.
- Rendered HTML one-pager of the brief for the actual stakeholder presentation, consistent with the track convention that content lives in markdown and visualisation lives in HTML.

**Assignment sketch:** take the problem brief to a real stakeholder, get it either agreed or challenged, and revise it. The measurable success check is whether a stakeholder can restate the diagnosis in their own words a week later, and whether at least one non-goal survived contact with the room.

---

## 7. AI in Practice Angles

Consistent with the track convention that the mentee's AI tool is already linked to their project folder and cross-checks saved files rather than generating from scratch:
- Cross-check the opportunity tree against the interview notes: which opportunities are supported by more than one interview, and which came from a single quote
- Stress-test the framing: ask for three alternative framings of the chosen problem, then reject the ones that are restatements rather than genuine reframes
- Run the fluff test on the design principles: for each, state the credible opposite. If it cannot be stated, the principle is not a decision rule
- Devil's advocate on the pitch: generate the three hardest stakeholder objections to the chosen bet, given the saved evidence

---

## 8. Open Questions Before the Build

Four of the six original questions are now answered and recorded in the scoping block at the top, and the activity chain is settled in section 5. What remains:

1. **Worked example:** use the mentee's own project throughout, as Customer Understanding does, or carry an abstracted enterprise example through the teaching blocks and switch to their project for the activities? Current assumption is their own project throughout, since every activity in this session operates on files they already hold (`jtbd-map.md`, insight statements). The counter-argument is that the bad-strategy teaching in block 8 lands harder with a neutral example nobody is defensive about.
2. **Class version:** whether a UX Class variant gets produced later alongside the senior one in this same folder. Not needed for this build, but it affects how much of the teaching content is written to be reusable at a lower level.

---

## 9. Resources

**Problem framing and reframing**
- Thomas Wedell-Wedellsborg, "Are You Solving the Right Problems?", HBR, January 2017: https://hbr.org/2017/01/are-you-solving-the-right-problems
- Thomas Wedell-Wedellsborg, *What's Your Problem?*: book-length treatment of the same seven practices
- Lillian Xiao, "A guide to problem framing", UX Planet: https://uxplanet.org/a-guide-to-problem-framing-ae58713364ec

**Problem statements**
- NN/g, "Problem Statements in UX Discovery": https://www.nngroup.com/articles/problem-statements/

**Opportunity space**
- Teresa Torres, "Opportunity Solution Trees", Product Talk: https://www.producttalk.org/opportunity-solution-trees/
- Teresa Torres, *Continuous Discovery Habits*
- LogRocket, "Opportunity solution trees: definition, examples, and how-to": https://blog.logrocket.com/product-management/opportunity-solution-trees-definition-examples-how-to/

**Prioritisation**
- NN/g, "5 Prioritization Methods in UX Roadmapping": https://www.nngroup.com/articles/prioritization-methods/

**Strategy**
- Richard Rumelt, *Good Strategy / Bad Strategy*
- Fred Perrotta, "The Kernel of Strategy": https://www.fredperrotta.com/kernel-of-strategy/
- UXPin, "Design Strategy: A Practical Framework for UX Leaders": https://www.uxpin.com/studio/blog/design-strategy/
- Simple Thread, "The Strategic Side of Design": https://www.simplethread.com/strategic-side-of-design/

**Design principles**
- NN/g, "Design Principles to Support Better Decision Making": https://www.nngroup.com/articles/design-principles/
- principles.design, real-world design principle library: https://principles.design/

**Internal cross-references**
- `library/lessons/01-discover/customer-understanding/materials/customer-understanding-senior-lesson.md`: the session this follows
- `library/frameworks/jtbd/framework-jtbd.md`: source of `jtbd-map.md`
- `library/frameworks/assumption-map/framework-assumption-map.md`
- `library/lessons/02-define/synthesis-problem-definition-in-ux/`: the Junior/class treatment, see section 4
- `library/lessons/leader-level/estimating-design-effort/`: companion session if scope extends to allocation

---

*Prep document · Winnie Nguyen · Private Training · August 2026*
