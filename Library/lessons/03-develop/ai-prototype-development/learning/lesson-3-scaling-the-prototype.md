---
title: "Lesson 3: Scaling the Prototype"
subtitle: "Set the rules before you prompt, feed the AI your user flow, build the journey in one pass — then review it, scale it to a second journey, and stitch the result into one walkable thread"
type: lesson
program: private-training
tags: [prototype, AI, design-system, pattern-first, rules, propagation, stitching, journeys, accessibility]
level: intermediate
date: 2026-09-20
draft: false
slides: "lesson-3-slide-outline.md"
previous-session: "Lesson 2: Build Your Design System"
next-session: "Lesson 4: Present & Publish"
---

> **Cover title: "Scaling the Prototype" — the same as the formal title, deliberately.** Lessons 1 and 2 front a tagline distinct from their title ("Stop Starting From Zero," "From Blueprint to Working Screens"); this lesson does not. An earlier draft used "Build Once, Scale by Rule" as the cover — that is retired, not kept as a subtitle. Don't reintroduce it when the deck is built.
> **Spine reworked (2026-09-20) to match how Winnie actually works.** The first draft taught rule *harvesting*: build one screen slowly, correct it, mine the corrections for rules, then build the rest. That is not the real workflow. In practice, with the design system and templates already built, the next move is to **set the rules first**, then hand the AI a user flow and have it build the whole journey in one prompt. The lesson now teaches that. What survived the rework untouched: the layer ladder, the ten rules, the propagation prompt, multi-journey scoping, and the stitch. What changed: rules moved from output to input, the build moved from screen-at-a-time to journey-at-once, and feeding an existing flow artifact became a first-class path.
> **The second-tool comparison is removed from the programme,** not deferred. It was promised in the coaching plan, cut from Lesson 2, and has no room here. The coaching plan has been updated in five places. If a student asks, say plainly that one method taught properly beats two half-learned — and that the rules file transfers to any tool unchanged.
> **No deck exists yet.** Until one is built, **this file is canonical for prompt wording** — the reverse of the Lesson 2 relationship, where the built deck was the source of truth. When the deck is built, reverse-sync `lesson-3-slide-outline.md` from it the same way Lesson 2's was.

## Overview

Lesson 2 ended with four files and a navigable `design-system.html`, and no screens. That was deliberate. This lesson builds the screens — and it builds them the way a designer with a working system actually builds them, which is not one screen at a time.

**The order is the lesson.** Rules first, before any prompt. Then the flow — fed in, not invented by the AI. Then the build, in one pass, because the system is what constrains the output now. Then the review, which is the longest segment in the session and the one where design judgement actually lives. Then it scales: a second journey costs a fraction of the first, and that is the proof the system works rather than a claim about it. It closes by stitching both journeys into one thread and walking it in sixty seconds.

**What the student leaves with:** two journeys built and reviewed, a rules file that visibly changes what the tool generates and that they've now rewritten in their own words, an `index.html` stitching the journeys, and a triage list sorted by which layer fixes it.

**What this lesson is honest about, in two places.** First, the rules handed over at the start are not the student's yet — they come from someone else's experience, and only the ones they rewrite after their first build will survive contact with a deadline. Second, "update one template and the whole prototype updates" is true of exactly one layer — tokens — and a governed prompt everywhere else. Both are taught as stated limits rather than glossed.

**This lesson runs on top of `03-develop/ai-prototype-development-lesson.md` ("AI Prototype Development")**, same relationship Lessons 1 and 2 have to it — but it deliberately **departs from that lesson's Phase 4 Step 6**, which says to build one screen at a time. See *Why not screen-by-screen any more* below; the departure is reasoned, not accidental, and should be said out loud to a student who has read the source lesson.

## Session Structure

**Organised Why → What → How → Do**, same convention as Lessons 1 and 2.

1. **[WHY]** Recap: you have the system, not the product
2. **[WHAT]** Rules before prompts — why the file comes first
3. **[DO]** Set up the rules file — starter set, then adapt it
4. **[HOW]** Three ways in: feed the flow
5. **[DO]** Build the journey — one prompt
6. **[DO]** Review the journey — three edit modes, then the layer ladder
7. **[DO]** Update the rules, then propagate
8. **[WHAT/DO]** One product, many journeys — scope and build journey two
9. **[DO]** Stitch, then walk the journey
10. **[DO]** Wrap-up & homework

**Time budget — the default plan, not an aspirational one:**

| # | Segment | Minutes |
|---|---|---|
| 1 | Recap | 4 |
| 2 | Rules before prompts | 5 |
| 3 | Set up the rules file | 9 |
| 4 | Three ways in — feed the flow | 5 |
| 5 | Build the journey (one prompt) | 13 |
| 6 | Review — modes, then the layer ladder | 15 |
| 7 | Update the rules, then propagate | 9 |
| 8 | Journey two — scope and build | 13 |
| 9 | Stitch and walk | 13 |
| 10 | Wrap-up | 4 |
| **Total** | | **90** |

**Segment 6 is the longest in the session, and that is a direct consequence of segment 5.** One prompt builds a whole journey, so all of its corrections arrive at once instead of trickling in screen by screen. That's the trade this method makes: less time prompting, more time reviewing. Say it to the student before the build so the size of the pile isn't a surprise.

**Cut order if you run long, in this order and no other:** journey two collapses to *scope only, build as homework* (segment 8 → 5 minutes); then the propagation demo in segment 7 becomes a walkthrough rather than a live run; then the stitch index is generated and walked but not tidied. **Never cut segments 3, 5 or 6** — rules, build, review. A session that builds two journeys and reviews neither has taught nothing.

**Where the 1:1 format earns its keep.** Segments 5, 8 and 9 all involve generation the student can start and then talk over. Wall-clock cost is lower than the table implies, as long as you are asking the coaching questions while the tool runs rather than watching it together in silence.

---

## WHY — Recap: You Have the System, Not the Product

**Open with the inventory, not a re-teach.** Ask the student to name what they have, from memory: `design-system/tokens.css`, `learning/component-inventory.md`, one template per pattern type, `learning/interaction-pattern.md`, and `design-system.html`. If they can't name them, that's the more useful diagnostic than anything else in the first five minutes — it means the files are on disk but not in their head, and the rules step next will land flat.

**Key message:** everything built last lesson describes the product. Nothing built last lesson *is* the product. Today the description starts generating the thing — and the first move is not a prompt.

**Check the homework in one question:** does every scoped screen have a template to build from? If the cross-check gap from Lesson 2 is still open, fix it now — a minute here costs a segment later.

---

## WHAT — Rules Before Prompts

**The claim, stated plainly: the rules file is written before the first build prompt, not after it.** This is the move that separates a designer who prototypes with AI occasionally from one who does it systematically, and it is the single most transferable thing in the session.

**Why it has to come first.** An AI coding tool with a design system in front of it and no constraints will still generate something reasonable — and reasonable is the problem. It will invent a component that looks like yours, pick a hex value near your token, add a state nobody designed. None of that reads as an error on screen; it reads as a slightly different product. Constraints applied afterwards mean finding and undoing that, screen by screen. Constraints applied first mean it never happens.

**What the tool predictably gets wrong, which is why a starter set is possible at all.** NN/g's study of AI prototyping in real design contexts found that even well-prompted output "missed subtle but important details related to spacing, grouping, and hierarchy," and that without explicit direction the output "defaults to neutral, minimalistic visual aesthetics" with no visual identity. These failures are boringly consistent across tools and projects. **A consistent failure is a rule waiting to be written** — which is exactly how the starter set in the next segment came to exist.

**Say the governance line here, because the student can finally see its consequence:** if the tool can read your system, it generates on-system; if it can't, it generates something else. That is why Lesson 2 existed. The rules file is the second half of the same idea — the system says what exists, the rules say what the tool is allowed to do with it.

---

## DO — Set Up the Rules File

### Where the rules go

**Into the rules/context file set up in Lesson 1** — the one the AI coding tool reads automatically — not a new file. That file now carries two jobs, so give it two labelled sections so they stay separable:

```
# Project rules & context

## Where things live
- Design tokens: design-system/tokens.css
- Component inventory: learning/component-inventory.md
- Interaction pattern: learning/interaction-pattern.md
- Templates: design-system/template-<type>.html
- Screens: screens/<journey>/<screen>.html
- System checkpoint page: design-system.html

## Rules for building screens
1. ...
```

**Why the split matters:** the pointers go stale when files move; the rules go stale when the system changes. Mixed together, you can't tell which half is lying to you. Stale context files actively degrade output, so this file gets maintained like the artifacts it points at — not written once and forgotten.

**Check the wiring before anything else.** If the student's tool isn't actually reading this file, everything after this segment is theatre. A perfect rules file in a file nobody reads is the most expensive kind of nothing.

### The starter set — ten rules

1. **Only components from the inventory.** If a screen needs one that isn't in `component-inventory.md`, stop and add it to the inventory first — then build.
2. **No raw values.** Every colour, type and spacing value comes from `tokens.css`. If a needed value doesn't exist there, flag it; don't invent one.
3. **Screens inherit the template, they don't fork it.** Anything shared across screens of a type belongs in `template-[type].html`.
4. **Every build carries flow context** — what precedes each screen, what follows, what carries over.
5. **Real content, never lorem ipsum.** Placeholder text hides hierarchy problems until the day someone else reads the screen.
6. **One layer per edit, and name the layer in the prompt.**
7. **Attach only the files the step needs.** Extra context doesn't improve the answer; it widens what the tool might modify.
8. **Flag, don't invent.** Every generation ends with a list of what it had to invent or couldn't do.
9. **Save before a structural edit**, so a bad edit is recoverable. This becomes literal in Lesson 4.
10. **WCAG 2.1 AA on every generated screen** — colour contrast, visible focus states, minimum target size — and flag anything that can't be verified.

**Rules 1 and 2 are the whole answer to "don't use anything outside the design system."** Rule 2's second clause matters as much as the first: *flag what doesn't exist* is what stops a missing token becoming an invented hex code that looks fine and is wrong.

**Rule 10 is the one nothing in this arc has caught until now.** AI-built screens routinely ship invisible focus states and near-miss contrast, and by Lesson 4 the prototype is at a public URL. Say it to a senior designer straight: enforcing it at generation costs nothing per screen, auditing it afterwards costs a session. It's a rule, not a review — there is no audit in this lesson.

### The honest part: these rules aren't the student's yet

**Say this out loud rather than hoping it goes unnoticed.** The ten rules above came from someone else's scar tissue — a mentor's practice and published research — not from anything the student has watched go wrong on their own product. That's a legitimate way to start; it's most of what a masterclass is for. But it has a predictable consequence worth naming in advance:

- **They'll believe about three of them today.** Probably 1, 2 and 8 — the ones whose failure mode they can already picture.
- **The rest earn belief in segment 6**, when the review turns up the exact thing a rule was written to prevent.
- **The ones that stick are the ones they rewrite in their own words** after that review. That's segment 7, and it's why the rules file is revisited rather than written once.
- **A rules file that hasn't changed since week one isn't being used.** Say that as the test they apply on their own projects.

**Facilitator note:** don't oversell the starter set to compensate. A student who is told these are proven and then watches one fail will discount all ten. Framing them as a well-founded starting point that they will edit is both true and more durable.

---

## HOW — Three Ways In: Feed the Flow

**The AI needs to know the journey before it can build it, and there are three places that knowledge can come from.** Same structure as Lesson 2's three methods: confirm which applies to this student, then walk only that path. A given student runs exactly one.

- **Method A — a flow artifact they already have.** A Figma flow, a FigJam board, a journey map, a written user flow from research. Feed it: paste it, screenshot it, or read the file live if MCP is connected. **This is the most common case for a senior designer and the fastest path** — the thinking is already done, it just hasn't been handed over.
- **Method B — nothing written down.** Describe the journey in the prompt: the screens in order, what the user does on each, what moves them to the next. Slower to type, identical output.
- **Method C — `learning/interaction-pattern.md` from Lesson 2.** Already in the project, already in the tool's reach. The tightest path when the student built it properly last lesson.

**What a flow artifact says and doesn't say.** Method A's input usually covers which screens exist and what connects them, and says nothing about what components each screen needs — that's what `component-inventory.md` supplies. Worth naming, because a student feeding a rich-looking flow can assume it's the whole brief and skip the inventory in the prompt. The flow is the thread; the inventory is the parts.

**Whichever method, the flow gets saved into the project** rather than living only in the prompt. If it isn't already `interaction-pattern.md`, it becomes it, or sits beside it. This is the *artifacts over prompts* habit — nothing that will be needed twice gets retyped.

**Facilitator note:** if Method A's artifact is messy or half-finished, feed it anyway rather than tidying it first. The gaps show up as flagged items in the build output, which is a faster and more honest audit of the flow than reading it again.

---

## DO — Build the Journey

**One prompt, one journey. Not one screen at a time.**

**Prompt to use:**
> "Build the [journey name] journey as a working prototype. The flow: [paste the flow artifact, or describe it — the screens in order, what the user does on each, what moves them to the next].
> Use `design-system/tokens.css`, `learning/component-inventory.md` and `design-system/template-[type].html` as they are — read them, don't restate them. Follow the project rules.
> Output one HTML file per screen at `screens/[journey]/`, linked to each other in flow order.
> End with a list of anything you had to invent, and anything in the flow you couldn't build from the system."

**Three clauses are load-bearing.** *Read them, don't restate them* is artifacts-over-prompts made literal — if the student starts pasting the inventory into the prompt, the router file isn't wired and that's the real fix. *Follow the project rules* is the entire previous segment collapsing into four words, and it only works if the wiring check passed. *End with a list of anything you had to invent* makes the build report its own gaps, which front-loads the review.

**If they have a reference screenshot** — a similar product, a competitor layout, visual inspiration — attach it. NN/g is unambiguous that a visual reference produces more consistent and accurate output than description alone.

### Why not screen-by-screen any more

**The source lesson says to build one screen at a time, and this lesson doesn't. Say that difference out loud** — a student who has read it will notice, and the reasoning is worth more than the rule.

That advice existed because, at the time, **nothing constrained the output except the sequence itself.** Building one screen and correcting it before the next was the only available review loop; a single giant prompt meant a single giant pile of drift with no shared reference to check it against.

That condition no longer holds. Tokens, the component inventory, the templates and now the rules file all constrain every screen equally, whether they're generated one at a time or together. **The constraint moved from the sequence into the system.** Two things follow:

- **Flow context stops being something you remember to type.** It was the most commonly dropped of the five build ingredients precisely because it had to be restated per screen. Build the journey at once and the AI sees the whole thread by construction.
- **The seams get designed rather than discovered.** Screens built in one pass share navigation and carried-over state because they were generated against the same flow, instead of being reconciled afterwards.

**The honest cost, stated before the build rather than after:** one prompt produces one large pile of corrections. That's why the next segment is the longest in the session. This method trades prompting time for reviewing time — it does not remove the reviewing.

---

## DO — Review the Journey

**This is the longest segment in the lesson and the one where design judgement actually lives.** Fifteen minutes, and it will feel like more, because everything arrives at once.

**Start with the build's own list.** It was asked to report what it invented and what it couldn't build from the system. Read that first — it's the fastest route to real gaps, and anything on it is a correction before the visual pass even starts.

**Then walk the screens in flow order, not file order.** The journey is the unit now, so review it as one: does the thread hold, does each screen lead where the flow says, does carried-over state actually carry.

### Question one — how big is the fix?

| Mode | Use for | Example |
|---|---|---|
| Chat | Broad or structural changes, anything needing explanation | "Rearrange this screen so the primary action is in the top row." |
| Targeted feedback | One specific element — name exactly what's wrong and where | "The button padding here is too tight." |
| Direct adjustment | Quick spacing or alignment nudges you can drag | (no prompt needed, if the tool supports it) |

Rule of thumb: chat for structure, targeted feedback for component-level fixes, direct manipulation for anything draggable. If a screen isn't working at all, say "save what we have and try a completely different layout" rather than overwriting blindly — most tools preserve the current version so you can compare instead of losing it.

### Question two — where does the fix belong?

| Symptom | Fix at | File |
|---|---|---|
| The heading copy on this one screen is wrong | instance | `screens/[journey]/[screen].html` |
| Every screen of this type is missing a back affordance | template | `design-system/template-[type].html` |
| The blue is wrong, everywhere | token | `design-system/tokens.css` |
| A state got built that isn't in the system | inventory | `learning/component-inventory.md` |
| The screen has nowhere to go | flow | `learning/interaction-pattern.md` |

**The rule: fix at the highest layer the symptom is true at.**

**The test question, asked out loud on every correction:** *"is this wrong on more than one screen?"* With a whole journey in front of them the student can now answer that by looking rather than predicting — which is the one genuine advantage a journey-at-once build has over a screen-at-a-time one at review time. Use it.

**Two ways to get it wrong, and only one of them is obvious.**

- **Fix too low** and you fix the same thing on every screen, with the versions drifting apart a little more each time. This is screen-by-screen prototyping wearing a different hat.
- **Push too high** and the system carries something only one screen ever needed. A component inventory quietly fills up with one-offs this way.

Not the highest layer available — the highest layer the symptom is actually true at.

**Editing the design system means editing the file, not regenerating from Figma.** A student who finds a missing state will instinctively go back to Figma. Stop them: add it to `component-inventory.md`, then regenerate `design-system.html` from the corrected files. Figma is upstream of Lesson 2, not upstream of every correction — and the arc's artifacts only stay authoritative if corrections land in them.

**Coaching question to ask before they look at anything:** *"what do you think it got wrong?"* Getting the student predicting is what turns review from inspection into judgement, and it's the habit that outlives the mentor.

---

## DO — Update the Rules, Then Propagate

### Rewrite the rules in their own words

**Go back to the rules file with the review still fresh.** Two passes, both short:

- **Which rule caught something?** Those are now believed rather than accepted. Nothing to change — but say which ones they were, because naming them is what converts them.
- **What got corrected that no rule covers?** That's a new rule, written in the student's words, at the top of the list. A correction they'd make again on the next journey is a rule by definition.

**Also worth pruning:** a starter rule that produced nothing on this build isn't necessarily wrong, but a rules file nobody can justify line by line stops being read. If the student can't say why a rule is there, mark it rather than deleting it, and revisit after journey two.

**This is where a handed-over rules file becomes theirs**, which is the whole answer to the honesty problem raised in segment 3. It's five minutes and it's the most important five minutes in the session for what happens after the programme ends.

### The propagation truth

The student will ask the obvious question: if I change a template, does every screen update?

**Be honest, in three parts:**

- **Tokens — genuinely automatic.** Change `tokens.css` and every screen changes, because every screen links it. One file, one edit, whole prototype. This is the retroactive payoff of Lesson 2's token sync.
- **Templates and components — not automatic.** A template change is a *prompt you run*, governed by rule 3. Nothing propagates by itself.
- **Which is fine, as long as nobody pretends otherwise.** "The prototype updates automatically" is doing a lot of work in most demos of this. Yours updates reliably, which is the more useful property.

**The propagation prompt:**
> "I've changed `[file]`. Every screen in `screens/` was built from it. Update each screen to match that change — only that change, nothing else. List every file you touched and what changed in each. If a screen has diverged from the template in other ways, report it — don't fix it."

**Three clauses, three jobs.** *Only that change* is the scope guardrail — an agent given a wide brief edits widely, and unasked-for edits are how a working prototype quietly breaks. *List every file you touched* makes the blast radius visible instead of trusting it. *Report, don't fix* keeps unrelated drift as information rather than a second uncontrolled edit.

**Run it live on whatever template-layer correction came out of the review.** There will almost always be one, and running it now rather than describing it is what makes the layer ladder feel usable rather than theoretical.

**The grown-up version of this, worth one minute:** the GOV.UK Prototype Kit. Pages `extend` a shared layout; change the layout once and every page that extends it updates. That's designers, at government scale, running exactly this model with propagation built in instead of prompted. It tells a senior designer this isn't a workaround — it's the lightweight version of an established method, and nothing learned here gets thrown away if the prototype outgrows plain HTML.

---

## WHAT / DO — One Product, Many Journeys

**A product is not one journey, and a prototype of one journey is a demo of a fragment.** The student has just built a thread. Someone else touches the same object, with a different goal, and nothing built so far says anything about them.

**Teach the scoping question, not an example.** This arc stays generic on purpose and the student's own product is the right vehicle. Ask:

> **"Who else touches this object, and what are they trying to do with it?"**

Three answers that usually land, offered as prompts if the student stalls — not as a menu to pick from:

- **A second persona on the same object.** The customer submits; someone reviews, approves, or processes. This is the one that makes stitching genuinely worth doing, because it's the journey no single squad ever demos.
- **A second goal for the same persona.** Same user, different intent — the thing they do the other 90% of the time.
- **The unhappy path.** Error, empty, rejected, interrupted. Ties straight back to the states in the component inventory, most of which have never been built.

**Scope it the same way as journey one:** one user goal, two or three screens. The goal is to prove the system carries across journeys, not to finish the product.

**Then name the real test, before building:** journey two should cost a fraction of journey one — less prompting, and visibly less correcting, because the rules file has just been rewritten from journey one's review. **If it doesn't feel dramatically cheaper, the rules file isn't doing its job**, and that's the finding, not a failure. Diagnose it rather than pushing through: rules too vague to be checkable, sitting in a file the tool doesn't read, or corrections that should have become rules in segment 7 and didn't.

**Two things journey two will surface, both normal:**

- **A screen type with no template.** Back to the template step for one quick addition. Cheaper now than at the stitch.
- **A second thread in the interaction pattern.** `interaction-pattern.md` gets a second journey section. Same file, not a second file — one map of the product.

**File organisation:** `screens/journey-[name]/`. One folder per journey keeps the propagation prompt's blast radius legible and makes the stitch index trivial to generate.

---

## DO — Stitch, Then Walk the Journey

**This is the source lesson's "Concept Extension — Stitching Prototypes," run as written.** Five steps, and the method is a pointer, not a rewrite.

1. **Define the journey thread.** One sentence: *"the user's goal across all of these screens is [goal]."* With two journeys there may be two threads meeting at one object — say where they meet, because that's the seam that matters most.
2. **Gather, don't rebuild.** Everything needed already exists. If something is missing, note it as a gap; don't fill it now.
3. **Build the index.** One page listing every screen in both journeys with its status.
4. **Add the seams.** Navigation between screens. A clickable thing that goes to the next screen is enough — don't perfect transitions, get the path walkable.
5. **Walk it, in character, in sixty seconds.**

**Index prompt:**
> "Here are my prototype screens: [list each with a one-sentence description and status — complete, in progress, missing]. Generate `index.html`: list them grouped by journey with their status, link to each, and show the journey flow. Use `tokens.css` and follow the project rules."

**Seams prompt:**
> "I have these screens as separate HTML files: [list]. Add a navigation wrapper that stitches them into one prototype — links from each screen to the next in its journey, a way back to the index, and an indicator of where the user is. Put the shared chrome in the template, not in each screen."

That last clause is rule 3 doing its job at the exact moment it's most tempting to break it.

### The walk, and the critique

**The critique happens during the walk, and takes the note-and-move-on form.** Walk the journey start to finish, in character, narrating the user's goal rather than the design decisions. Log every flaw. Fix nothing.

**Nathan Curtis's rule, which is the whole reason this works:** a stitched prototype reveals inconsistency; it is not an audit tool. Turning a stitch session into a design review kills the collaboration that makes stitching valuable.

**Capture format — one line per issue, three columns:**

| Where | What | Layer |
|---|---|---|

**The third column is where the layer ladder pays off twice.** The triage list comes out of the walk already sorted, so the fixing pass is fast and the highest-leverage fixes are obvious.

**If it takes longer than a minute to walk, the thread isn't clear enough yet.** That's a finding about the journey, not about the prototype's polish.

### The stitch mindset — three things to land before the demo

1. **It's a throwaway artefact.** It exists to communicate the journey while the product gets built, and it retires the day the product ships. Treating it as a deliverable is what makes people polish it instead of using it.
2. **The goal is the journey, not the screens.** Inconsistencies will be visible. That's what stitching is for — a polished individual demo hides exactly what a stakeholder needs to see.
3. **One minute hooks the room.** Walk the user's goal, not the design decisions, then stop and invite discussion. If the story takes longer, the thread isn't clear — and the fix is in the thread sentence, not the screens.

**Facilitator note:** the strongest pull in this segment is toward fixing one small thing "while we're here." Don't. The walk is ten minutes; a fixing detour is twenty and the walk never finishes. Say up front that nothing gets fixed and hold it.

---

## DO — Wrap-up & Homework

**Land the key idea:** the screens are not the deliverable of this lesson. The rules file is — specifically, the version they rewrote in segment 7. Screens are what it produces, and it will produce them again on the next project, for a different product, without a mentor in the room.

**Recap what today produced:** two journeys built and reviewed, a rules file that has changed since it was handed over, a stitched `index.html`, and a triage list sorted by layer.

**Homework before Lesson 4 — checklist:**

- [ ] Work the triage list, highest layer first — token fixes before template fixes before instance fixes
- [ ] Finish journey two if it was scoped but not built
- [ ] Walk the stitched journey once, alone, and time it. Over sixty seconds means the thread needs tightening, not the screens
- [ ] Add any rule the homework earns — the rules file keeps growing after the session
- [ ] Draft three sentences on how you'd introduce this prototype to someone who's never seen it. Raw material, not a script
- [ ] Have a GitHub account and GitHub Desktop installed before the session — install friction shouldn't eat session time

**Name what's next explicitly:** Lesson 4 opens with presenting the work — the methodology and decisions, not the pixels — then publishes the prototype to a live, self-updating URL that doesn't depend on any design tool account.

---

## Prompt & Reference Library

**This file is canonical for prompt wording until a deck is built.** When the deck exists, reverse-sync the outline from it and treat the deck as the presentation reality, same as Lesson 2.

**Build a journey — one prompt:**
> "Build the [journey name] journey as a working prototype. The flow: [paste the flow artifact, or describe it — the screens in order, what the user does on each, what moves them to the next].
> Use `design-system/tokens.css`, `learning/component-inventory.md` and `design-system/template-[type].html` as they are — read them, don't restate them. Follow the project rules.
> Output one HTML file per screen at `screens/[journey]/`, linked to each other in flow order.
> End with a list of anything you had to invent, and anything in the flow you couldn't build from the system."

**Build a single screen — for a gap found later:**
> "Build the [screen name] screen into the [journey] journey. Goal: [what the user is doing]. It follows [screen] and leads to [screen], carrying over [state]. Follow the project rules."

**Correct a screen:**
> "This is what you built: [describe]. Here is what should be different: [list corrections]. Change only those things. Update the output."

**Explore a different direction without losing what exists:**
> "Save what we have and try a completely different layout for this screen."

**Propagate a system-layer change:**
> "I've changed `[file]`. Every screen in `screens/` was built from it. Update each screen to match that change — only that change, nothing else. List every file you touched and what changed in each. If a screen has diverged from the template in other ways, report it — don't fix it."

**Find the undesigned seams (chat tool, before stitching):**
> "Here is my interaction pattern: [paste]. Here are the screens I've built: [list]. What transitions are undesigned? What does the user see between [screen] and [screen] that hasn't been prototyped?"

**Generate the index:**
> "Here are my prototype screens: [list each with a one-sentence description and status — complete, in progress, missing]. Generate `index.html`: list them grouped by journey with their status, link to each, and show the journey flow. Use `tokens.css` and follow the project rules."

**Add the seams:**
> "I have these screens as separate HTML files: [list]. Add a navigation wrapper that stitches them into one prototype — links from each screen to the next in its journey, a way back to the index, and an indicator of where the user is. Put the shared chrome in the template, not in each screen."

---

## Reference: The Rules File Template

Give this to the student as a starting shape, not a finished file. After segment 7 it should no longer look exactly like this — that's the point.

```markdown
# Project rules & context

## Where things live
- Design tokens: design-system/tokens.css
- Component inventory: learning/component-inventory.md
- Interaction pattern: learning/interaction-pattern.md
- Templates: design-system/template-<type>.html
- Screens: screens/<journey>/<screen>.html
- System checkpoint page: design-system.html

## Rules for building screens
1. Only use components listed in component-inventory.md. If a screen needs
   one that isn't there, add it to the inventory first, then build.
2. Never use a raw colour, type or spacing value. Use the tokens in
   tokens.css. If a needed value doesn't exist, flag it — don't invent one.
3. Screens inherit from their template. Anything shared across screens of a
   type goes in template-<type>.html, not in each screen.
4. Every build carries flow context: what precedes each screen, what
   follows it, and what carries over.
5. Real content, never lorem ipsum.
6. One layer per edit — instance, template, token, inventory or flow — and
   name the layer in the prompt.
7. Only read the files the task needs.
8. Every generation ends with a list of anything invented or unresolved.
9. Save before any structural edit.
10. Every generated screen meets WCAG 2.1 AA — colour contrast, visible
    focus states, minimum target size. Flag anything you can't verify.
```

---

## Instructor Notes

- **This lesson is organised Why → What → How → Do**, same convention as Lessons 1 and 2.
- **The order is the lesson — rules, flow, build, review.** If a student wants to skip straight to the build prompt, that's the moment to hold the line: the rules file is what makes the one-prompt build safe, and without it this method is just a bigger version of the thing Lesson 1 warned about.
- **Segments 3, 5 and 6 are the spine.** If the session runs late, journey two becomes scope-only and the build becomes homework. Never trade away rules, build or review to protect a later segment.
- **This lesson deliberately departs from the source lesson's "one screen at a time."** The reasoning is in *Why not screen-by-screen any more* — say it out loud to a student who has read the source lesson, because the departure is the interesting part, not an inconsistency to hide.
- **Be honest about the starter rules twice.** Once in segment 3, when they're handed over, and once in segment 7, when the student rewrites them. Overselling them in segment 3 is the failure mode: one visibly wrong rule discredits all ten.
- **Don't oversell propagation either.** Tokens are automatic, everything else is a governed prompt. A senior designer will find out within a week if you claimed otherwise.
- **Rule 10 is enforced at generation, not audited in session.** Don't turn the review or the stitch walk into an accessibility audit — there isn't time and it isn't the point.
- **Hold the line on note-and-move-on.** The pull to fix one small thing during the walk is strong and it eats the segment.
- **Three flow methods, one per student.** Confirm at segment 4, then walk only that path. Don't demo all three — that's reference material, not a teaching sequence.
- **The second tool is removed from the programme.** Huy's coaching plan has been updated in five places. If he raises it, say plainly: one method taught properly beats two half-learned, and the rules file transfers to any tool unchanged.
- **Lesson 4 now opens with fifteen minutes of presenting**, moved here from the original Lesson 3 stub. That puts Lesson 4 under real pressure — the git guide's solo practice rep is the first thing to trim there, not the recovery-from-a-mistake beat.
- **Open knock-on, recorded not fixed:** `lesson-2-interaction-pattern-build-editing-craft.md` still carries a filename describing content that now lives here.
- Keep tool references generic in delivery ("your AI coding tool") so this lesson is reusable across students regardless of which tools they use.

---

## Connection to Curriculum

A private-training adaptation layer on top of `03-develop/ai-prototype-development-lesson.md` ("AI Prototype Development") — Phase 4 Steps 2 and 5 and the whole "Concept Extension — Stitching Prototypes," re-paced for 1:1 delivery and picking up exactly where Lesson 2 ends.

**A deliberate departure from the source lesson:** Phase 4 Step 6's "build one screen at a time" is not taught here. With tokens, a component inventory, templates and a rules file all in place, the constraint that used to come from sequencing now comes from the system, so the journey builds in one pass. The reasoning is spelled out in the lesson body rather than left implicit.

**Genuinely new here, not in the source lesson:** the rules file as a precondition rather than an output, and the honesty about where a student's first rules come from; the three flow-input methods; the journey-at-once build prompt; the layer ladder for edits and the rule to fix at the highest layer the symptom is true at; the propagation prompt and the honest account of what does and doesn't update automatically; multi-journey scoping as the proof the system scales; WCAG 2.1 AA enforced at generation as rule 10; and the note-and-move-on critique folded into the stitch walk rather than run as a separate pass.

**Moved to Lesson 4:** coaching how to present the work, which the original stub placed here.

---

## Secondary Research Notes

Sources behind the claims made in this lesson, for a facilitator who gets challenged on them.

- **NN/g, "AI Prototyping in Real Design Contexts"** — output is assembled but misses spacing, grouping and hierarchy; defaults to generic, identity-free aesthetics without explicit direction; detailed prompts and visual references measurably improve results. Grounds segment 2's argument for rules-first and the reference-screenshot tip. https://www.nngroup.com/articles/ai-prototyping/
- **GOV.UK Prototype Kit — layouts** — pages `extend` a shared layout; change it once and every page using it updates. The established precedent behind rule 3 and the propagation segment. https://prototype-kit.service.gov.uk/docs/how-to-use-layouts
- **Enterprise design system governance in the AI era** — governance shifts from approving components before they're built to detecting and correcting after; machine-readable documentation is what makes tools generate on-system; components reference semantic tokens, never raw values. Grounds rules 1, 2 and 8, and the governance line in segment 2. https://f1studioz.com/blog/blog-enterprise-design-system-governance-ai/
- **Guardrails for AI coding agents** — scoped context beats broad context; extra files widen the surface area of what gets modified. Grounds rules 6 and 7 and the propagation prompt's "only that change" clause. https://www.syncfusion.com/blogs/post/ai-guardrails-coding-agents
- **DESIGN.md / AGENTS.md / RULES.md** — separating visual rules from code-behaviour rules, and the warning that stale context files actively degrade output. Grounds the two-section structure of the rules file. https://designmd.app/blog/design-md-agents-md-rules-md/
- **Nathan Curtis, "Stitching a Journey Together in a Prototype"** (EightShapes) — the stitch definition, the seams argument, and the resist-fixing rule that shapes the walk. https://medium.com/eightshapes-llc/stitching-a-journey-together-in-a-prototype-d3b86d26ebb

---

*Created by Winnie Nguyen · Private Training · Last updated September 2026*
