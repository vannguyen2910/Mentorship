---
title: "UI Fundamentals"
subtitle: "Judging design decisions you didn't make"
type: lesson
program: standalone
tags: [ui-design, visual-hierarchy, typography, colour, spacing, design-tokens, components, design-systems, accessibility, wcag, gestalt, ux-laws, ai-workflow, critique]
level: junior
duration: "90 min"
date: 2026-09-09
draft: true
slides: ""
previous-session: "None. Standalone."
next-session: "None. Standalone. Hands off to any prototyping or critique session."
programs: [ui-ux-fundamentals:06]
---

## Overview

Most UI lessons assume the student is starting from a blank artboard. Almost none of them are.

A working junior designer inherits nearly everything. The screens they are asked to judge were made by someone else, or by a machine. The components they build with were built by their manager. The colours and spacing were decided before they arrived. The one thing they are rarely doing is inventing, and the one thing every course teaches is inventing.

So this session is not about making a screen look good. It is about judging design decisions you did not make, and being able to say the reason out loud to a developer who is about to build it.

The gap this closes is not visual vocabulary. Students can produce screens. What they cannot do is choose between two of them, or explain why the one they chose is right, which means they cannot defend their work, cannot evaluate what an AI tool hands them, and cannot tell whether the component they inherited is well made or badly made. Framed in Norman's terms, generative tools have collapsed the Gulf of Execution almost to nothing. Producing a plausible, attractive screen now costs a sentence. They have done nothing at all for the Gulf of Evaluation. A designer can now generate three competent-looking options and has no criteria to choose between them.

The session teaches one instrument, a five-layer decision stack, and then points it at three different inherited things: screens the student did not make, the student's own screen, and the component their team already uses. Same tool, three surfaces. That repetition is what makes it portable rather than a trick for checking screens.

Two outputs leave the room. A decision sheet, which records what was changed and why, and a documented token set, which is an audit of what the team already uses rather than an invented one. Both are what make this session chainable to a prototyping or critique session later.

---

## Learning Objectives

By the end of this session, students will be able to:

1. **Explain** why an attractive screen is not evidence of a usable one, and name the research finding behind it
2. **Apply** five layers of visual decision-making in reading order: space, hierarchy, type, colour, component
3. **Say out loud**, in a developer's register, the reason behind a spacing, hierarchy, type, colour or component decision
4. **Name** the principle or law behind each layer, and say what it does and does not cover
5. **Identify** two commonly misapplied UX laws and explain why the usual application is wrong
6. **Audit** the design tokens their team already uses, and name what is inconsistent or undefined
7. **Interrogate** an inherited component: what decisions are baked into it, and whether those decisions hold up against the five layers
8. **Raise** a problem with an inherited component as a question rather than an accusation

---

## Success Check

- The student can look at a screen they have never seen and name, in order, which of the five layers is failing first.
- The reason a student gives for a decision would survive being repeated to a developer without the developer asking "says who?"
- The token audit names at least one thing that is inconsistent or undefined in what their team currently uses. An audit that finds nothing has not been done.
- When asked about a component they find confusing, the student states which specific layers do not resolve, rather than saying it feels wrong.

---

## Materials Needed

- **One real screen from the student's own work.** Not a portfolio piece, not a redesign concept. Something currently in production or in a live file, ideally one they have had a conversation about with a developer.
- **Access to their team's design system or component library**, whatever state it is in. A shared Figma file, a Storybook, a folder of screens somebody keeps reusing. If the team has no system at all, that fact is itself the material and the session works fine.
- **One component from that system that the student finds confusing.** They should bring the confusion, not resolve it beforehand.
- **The stimulus set** (instructor): six to eight screens of the same product, mixed AI-generated and real, close enough in visual quality that the choice is not obvious. Prepared in advance. See the facilitation note below.
- **A contrast checking tool.** Any of them. The habit matters more than the tool.
- **The food delivery tracking screen**, prepared at a teachable level of wrongness, used for every worked example on the slides. It is needed in eight versions: the original, five progressively corrected states (one per layer), a heavily blurred version and a desaturated version. Built once as one file with variants, not eight separate screens.
- **The schematic specimen kit**, a small set of reusable abstracted UI parts (grey bars for text, geometric shapes for controls) used for every principle diagram. See the Visual language section of the slide outline for the drawing rules.
- An AI tool, for the critical-thinking beat only. It is used here as something to be checked, not as something to produce with.

---

## Pre-Class Preparation

1. **Bring the screen.** One, real, from work. If they bring three, pick the busiest one, because density is where the layers show.
2. **Bring the confusing component.** Ask them not to work out why it is confusing beforehand. The confusion is the raw material.
3. **Find out whether the team has tokens.** Not what they are, just whether they exist and where. Five minutes of asking, done before the session rather than during it.
4. **Bring one design decision a developer pushed back on.** What was built, what they said, what happened. It gets used twice.

---

## Session Plan

| # | Block | Topic | Duration |
|---|---|---|---|
| 1 | Open | Which one ships? | 5 min |
| 2 | Frame | You can make it. You cannot judge it. | 7 min |
| 3 | Layer 1 | Space and layout | 10 min |
| 4 | Layer 2 | Hierarchy, and two laws you will hear quoted wrongly | 10 min |
| 5 | Layer 3 | Type | 7 min |
| 6 | Layer 4 | Colour | 10 min |
| 7 | Reveal | Why the prettiest one won | 5 min |
| 8 | Layer 5 | Components, and the one you inherited | 12 min |
| 9 | Practice | *Reserved. Winnie to define.* | 16 min |
| 10 | Close | Two outputs, and where they go | 4 min |

86 minutes scripted into a 90 minute slot. Five teaching layers, one reveal, one practice block.

> **Why the layers run in this order.** Reading order, not importance order. Grouping registers before hierarchy, hierarchy before type, type before colour emphasis, and the component is the last thing a person consciously identifies. Teaching in the order a screen is actually read means a student can check their work by looking rather than by remembering a list. It also runs from the most structural decision to the most local, so the expensive mistakes get caught first.

> **Why the reveal sits at minute 49 and not at minute 5.** The Aesthetic-Usability Effect only lands if the student has already been caught by it. They pick the prettiest screen in the opening, spend forty minutes learning four layers, and only then find out what happened to them at the start. Named up front it is a fact they nod at. Named after four layers it is an explanation of their own behaviour, and it recontextualises everything they have just learned. Do not move it earlier.

> **Facilitation note on the stimulus set.** Six to eight screens of the same product, some AI-generated, some real, and the students are not told which is which. This matters: the moment they know a screen came from an AI tool, they start hunting for AI tells instead of applying criteria, and the point of the session is that the source does not change the criteria. Each screen should fail on exactly one layer, and the failures should be spread across the five, so that whichever screen a student defends, some layer later in the session takes it away from them. Building this set is the single largest prep cost and it is reusable indefinitely.

> **Facilitation note on Layer 5.** This is the layer most likely to overrun, and it is the one worth overrunning for. It is also the only layer with a political dimension, because the student is being taught to evaluate their manager's work. Read the guardrail out loud rather than assuming it is obvious.

> **If the student's team has no design system at all.** The session does not break. Layer 5 runs on any public component the student uses regularly instead, and the token audit becomes a derivation: pull the spacing, sizes and colours actually present in their own screen and write down what the implicit system already is. Most teams have an accidental system nobody has written down, and finding it is a more useful exercise than being handed a tidy one.

---

## Core Content

### Open · Which One Ships?

Put the stimulus set up. Ask each student to pick the one they would ship and write the reason in one sentence.

Do not discuss the answers yet. Collect them, read two or three aloud without comment, and move on. The reasons will be some version of "it looks cleaner" or "it feels more modern," and the room will split. That split is the session's opening evidence and it should be left sitting there uncomfortably rather than resolved.

Name what just happened in one line, then leave it: everyone here can make a screen like these. Nobody here can say why one of them is better.

---

### Frame · You Can Make It. You Cannot Judge It.

Two gulfs sit between a person and a system. The Gulf of Execution is the distance between wanting something and doing it. The Gulf of Evaluation is the distance between what the system shows and understanding what it means.

Normally these are talked about as problems the user has. Turn them on the designer instead.

Making a screen used to be the hard part. It took tool skill, time and craft, and the reason a junior could not produce senior work was mostly that they could not physically make it yet. That gulf has closed. Generative tools produce plausible, attractive, competently spaced screens from a sentence. Execution is close to free.

The evaluation gulf has not moved at all. Nothing about the last few years made it easier to look at three screens and know which one is right.

So the value moved. It used to sit in making, because making was scarce. It now sits in judging, because judging is what is left scarce. This is uncomfortable framing for someone whose job title says designer and whose day is spent producing, and it should be said plainly rather than softened: producing is no longer the thing you are paid for.

Judging requires criteria you can name. That is what the rest of the session is.

**The dev thread.** Every layer today ends with a sentence you could say to a developer. Not a design rationale, a sentence. The test of whether a student understands a layer is not whether they can apply it, it is whether they can say why in a register that a person who does not care about design will accept. Most junior designers lose arguments they were right about because they only had "it looks better" available.

---

### Layer 1 · Space and Layout

**The question this layer answers:** what belongs with what?

Most junior screens fail here, and almost nobody diagnoses it here, because a grouping failure presents as a vague feeling that the screen is messy.

**Proximity.** Elements placed near each other are perceived as related, whether or not they are. This is not a preference, it is how vision works before conscious attention arrives. Which means spacing is not decoration, it is the first piece of meaning on the screen, and it gets read before any of the words do.

**Common region.** A shared boundary beats proximity when the two compete. Two items far apart inside the same card read as more related than two items close together on either side of a card edge. This is the one juniors have almost never heard of, and it explains a specific recurring mistake: reaching for a divider line or a border when the actual problem was that the spacing was wrong. Borders are a strong tool. Reached for to fix a spacing problem, they add a second grouping signal that argues with the first one.

**The 8pt scale.** Every gap is a multiple of 8. That is the whole rule. Its value is not aesthetic, it is that it converts a question with infinite answers into a question with a small number of answers. "Is this 24 or 25?" stops being a question a person can have an opinion about, which means it stops being a thing to argue with a developer about, which is most of the point.

**Worked example.** On the tracking screen, the order status and the estimated time belong together and are usually not spaced as though they do, while the courier's name sits close enough to the order contents to read as part of them. Fix the grouping and the screen stops feeling busy without a single element being removed.

> **The sentence you say to a dev:** "Those two are in the same group, so the gap is 8. The next group starts at 24. It's the scale, not my preference."

---

### Layer 2 · Hierarchy

**The question this layer answers:** what gets read first?

Hierarchy is not "make the important thing bigger." There are four levers, and size is only the most obvious one: size, weight, colour and space. A screen where everything is the same size can still have perfect hierarchy if the other three are doing work, and a screen with five type sizes can have none.

The failure to watch for is a screen where two elements are both trying to be primary. Not too many sizes: two firsts. There can only be one thing that gets read first, and if a student cannot say which element that is on their own screen, the screen does not have hierarchy, it has variety.

**Von Restorff, the isolation effect.** The item that differs from its neighbours is the one that gets remembered and noticed. Practical consequence, and it is the one juniors resist: emphasis is a fixed budget. Every additional emphasised element on a screen makes every other emphasised element weaker. Three primary buttons is zero primary buttons.

**F-pattern scanning.** People do not read screens, they scan them, and on text-dense layouts the scan tends toward an F or a layer-cake shape driven by headings. What matters for a junior is the implication rather than the shape: the first two words of a heading do more work than the rest of the heading, and content placed below a heading nobody reads is content that does not exist.

**Worked example, and this is the one that matters.** On the tracking screen, the map is almost always the largest, most colourful element. It is also, according to the actual job, the least useful thing on the screen. The job is *"let me stop fearing it's not coming."* What answers that fear is the status and the promise that the app will tell them when something changes. What does not answer it is a map of a motorbike moving, which mostly gives someone something to stare at while continuing to worry.

So the junior version leads with the map because the map is the most attractive element, and attractiveness is what they had available as a criterion. The evidence says lead with reassurance. This is the whole session in one screen, and it is worth sitting on for a minute.

#### Two laws you will hear quoted wrongly

Worth three minutes, because students will hear both of these used as arguments and need to know when the argument is invalid.

**Hick's Law** describes reaction time when choosing among simple, unfamiliar, roughly equally likely options. It does not describe someone scanning a well-labelled, well-grouped menu, because that person is not evaluating every item in turn. Using it to argue that navigation must have fewer than five items is the standard misuse. A categorised list of twenty routinely beats an ungrouped list of eight. Grouping and labelling beat item-count reduction.

**Miller's Law** is misapplied almost universally. Miller measured immediate memory span, how many items a person can hold in mind, and the paper was substantially about chunking rather than about limits. It says nothing about how many links a navigation bar can have, because those items are on screen being read, not being memorised. Recognition, not recall.

The point of teaching this is not trivia. It is that a rule has a scope, and the skill is checking whether the rule applies before invoking it. A designer who quotes a law that does not apply loses the argument and some credibility with it.

> **The sentence you say to a dev:** "The status is the primary. If it can't be the biggest element, it has to be the highest contrast one. It can't be neither."

---

### Layer 3 · Type

**The question this layer answers:** how does the reading order stay readable?

Layer 3 has no named law behind it, and saying so is worth doing rather than glossing over. Not every design decision has a psychology paper underneath it. Some of it is craft with conventions, and pretending otherwise teaches students to reach for a citation they do not have, which is a habit that will embarrass them in front of an engineer.

**Three sizes and two weights beat nine of each.** A junior screen typically has six or seven type sizes, most of which differ by two pixels and therefore communicate nothing at all. A difference the eye cannot reliably detect is not a hierarchy signal, it is noise with extra maintenance cost.

**A scale, not a set of fonts.** The decision is the ratio between steps, and then everything on the screen takes a value from that scale. Same logic as the 8pt grid: the aim is to remove opinion from the decision.

**Line height and measure.** Line height belongs to the size, not to the block, so it should live in the scale rather than be adjusted per instance. Measure, the characters per line, has more effect on whether a paragraph gets read than the typeface choice does, and juniors adjust the typeface.

**The diagnostic.** If a student needs a fourth size to make something stand out, the problem is almost never in the type. It is that Layer 2 has not been resolved and they are trying to fix a hierarchy problem with a type solution.

> **The sentence you say to a dev:** "Three sizes, two weights, and every one of them is on the scale. If I need a fourth size, something upstream is wrong and I should fix that instead."

---

### Layer 4 · Colour

**The question this layer answers:** what is the one thing to do here?

**Roles, not palettes.** A colour on a screen is not a colour, it is a job: brand, neutral, success, warning, error, and the surface and text values that carry them. The junior version of this layer is picking a palette that looks nice. The working version is assigning meaning, and then never using a meaning-carrying colour for anything else. The moment error red is also the primary button, the screen has lost the ability to say error.

**Von Restorff again, which is why this layer is short.** Colour is the strongest emphasis lever, which makes it the easiest to spend badly. If the primary action is not the only saturated element on the screen, it is not the primary action.

**Contrast, taught as one rule and a tool.** WCAG 2.1 AA: 4.5:1 for body text, 3:1 for large text and for the non-text parts that carry meaning. Check it, do not estimate it. This layer teaches one rule and the habit of running the tool, not accessibility as a topic. That deserves its own session and does not fit in ten minutes.

The reason it is a hard gate rather than a guideline is worth one sentence: it is the only decision on this screen that has a correct answer, and a junior arguing from a measured number rather than a preference is in a different conversation entirely.

**Worked example.** The tracking screen's status text is frequently mid-grey on white, which fails, and nobody notices because it fails by a small margin and the screen looks calm. Calm and unreadable are easy to confuse.

> **The sentence you say to a dev:** "Red is our error role. If we use it for the primary button we lose the ability to show an error on this screen."

---

### Reveal · Why the Prettiest One Won

Go back to the opening. Ask the room which screen they picked and why, then read out one of the original sentences.

**Kurosu and Kashimura, Hitachi Design Center, 1995.** 252 participants rated 26 variations of an ATM interface on both aesthetic appeal and ease of use. The correlation between rated appeal and *perceived* ease of use was stronger than the correlation between appeal and *actual* ease of use. Tractinsky replicated it in Israel expecting culture to weaken the effect and found it stronger.

People believe attractive things work better. So do designers. So did everyone in this room forty-five minutes ago.

Two consequences, and the second one is the one that is rarely taught.

**For users, this is real and useful.** Attractive design buys tolerance. People forgive small friction in something that looks good, and that is a genuine competitive advantage. It has a ceiling: serious usability problems break through the goodwill regardless of how good the thing looks.

**For designers, it is a trap.** Attractiveness hides problems from the person evaluating. In a usability test, participants struggle through a task and then praise the visuals, and the real defect never gets named.

Now the part that connects to the whole session. Attractiveness only works as a signal when attractiveness is scarce. Generative tools raised the aesthetic floor for everybody, so nearly everything now looks fine, so looking fine stopped discriminating between options. A designer whose only evaluation tool was taste has, in the last few years, quietly lost their only evaluation tool.

That is why the stimulus set was mixed and why nobody was told which screens were generated. The source never mattered. The criteria are the same either way.

---

### Layer 5 · Components, and the One You Inherited

**The question this layer answers:** why does this thing exist, and when should I not use it?

This is the heaviest layer and the one closest to the student's daily frustration.

**Jakob's Law.** People spend most of their time on other products, so they prefer yours to work like the ones they already know. Familiarity is not a lack of ambition. A novel component costs the user learning time, and that cost has to be paid for by a benefit the designer can name.

**A component is inherited reasoning.** Every component encodes decisions somebody already made and, ideally, defended: which states exist, minimum sizes, spacing, focus behaviour, what happens at the smallest breakpoint. Using it is not a constraint on creativity, it is the reuse of thinking. A student who understands this stops experiencing the design system as a cage.

**States are the part juniors skip.** Default, hover, focus, active, disabled, loading, error, empty. A component defined only in its default state is a picture, not a component, and the missing states become a developer's improvisation, which means the designer stopped making the decisions partway through.

**Tesler's Law, the conservation of complexity.** Complexity in a system cannot be removed, only relocated. Either the user absorbs it or the system does. This is the most useful law in the session for the developer and BA conversation, because it converts a taste argument into an allocation question. "I think this should be simpler" invites disagreement. "This complexity has to live somewhere, and right now it lives with the user; can it live with us instead?" invites a decision. Engineers respond to the second framing because it is the framing they already use.

#### The hard case: what if the component is actually bad?

Often it is. A confused student cannot tell which of two things is true: the component is well-reasoned and they have not learned to read it, or the component is genuinely sloppy and their confusion is accurate information.

That is the Gulf of Evaluation again, one level up. They cannot judge the screen, and they cannot judge the system that made the screen.

The answer is neither "trust the system" nor "critique the system." **Run the same five layers on the component itself.** Space: is the internal spacing on the scale? Hierarchy: is there one clear primary? Type: is it drawing from the same scale as everything else? Colour: do the roles hold, does it pass contrast in every state? Component: are all the states defined, and can anyone say what it is for?

If the decisions resolve, the gap is the student's and it is a learning problem, which is good news. If two of them do not resolve, the gap is the component's, and the student now has specific language instead of a vague feeling.

This is the third surface the same instrument has been pointed at today, and that is the point: it works on things you did not make, on things you did make, and on the system that made both.

> **The guardrail, and say it out loud.** Ask, do not indict. The output of this is a question, not a verdict: *"I ran our button against these five checks and the internal spacing and the disabled state don't resolve for me. Can you walk me through the reasoning?"* That question makes a junior look careful. The same observation delivered as "our design system is broken" makes them look like a problem, and it will be remembered longer than whether they were right. A junior who is right and unemployable has not won anything.

> **The sentence you say to a dev:** "Our button already handles disabled and loading. If I make a new one, we maintain two of them forever."

---

### Close · Two Outputs, and Where They Go

**The decision sheet.** One row per decision: what changed, which layer, which rule or law, and the sentence you would say to a developer. This is what makes the work defensible later, and it is the thing a critique session can actually critique. A revised screen shows what you did. The sheet shows why, and only the why can be argued with productively.

**The token audit.** Not an invented set. What does the team already use for spacing, type and colour roles, written down, with the gaps and inconsistencies named. Most teams have an accidental system that nobody has documented, and the person who documents it becomes useful in a way that is disproportionate to the effort.

Both outputs feed forward. Tokens are the input to any prototyping work, where they are what stops a generative tool inventing its own system on every screen. The decision sheet is the input to any critique, where the question stops being "do you like it?" and becomes "does the stated reason hold?"

**The one thing to carry out of the room.** You will spend most of your career judging work you did not make. The five layers are not a checklist for making screens. They are how you form an opinion you can defend in a meeting, and being able to do that at all is rarer than it should be.

---

## Activities

> **Reserved. Winnie is defining the in-class activities.**
>
> 16 minutes are held in the session plan for a practice block. What the session structure requires of whatever fills that slot:
>
> - **It must produce the decision sheet**, or something that records reasons rather than only changes. Any downstream critique has nothing to work with otherwise.
> - **It must produce the token audit**, or the handoff to any prototyping session breaks.
> - **It runs on the student's own screen**, not on the food delivery example. Food delivery is the teaching surface; their work is the practice surface.
> - **Any share-back is stronger in a developer's register** than in a design-mentor register. Students find the register shift harder than the content, which makes it diagnostic.
> - **If any part of it involves judging screens**, the Aesthetic-Usability reveal stays after the judging, never before.

---

## AI in Practice

### 🤖 Try this with AI

> *"Here is a screen from a product I work on. Assess it against five things, in this order: spacing and grouping, visual hierarchy, type scale, colour roles and contrast, and component consistency. For each one, tell me what decision was made, whether it holds up, and what you would say to a developer to justify it."*

### 🧠 Critical thinking

Take one claim the tool made about contrast and check it with a contrast tool. It will frequently assert that a pair passes AA when it does not, and it will assert it in exactly the same confident register it uses for everything else.

This is the point, and it generalises past contrast. An AI tool produces rationale, and rationale is not reasoning. It is text shaped like reasoning, generated after the fact, with no measurement behind it unless a measurement happened. Anything checkable should be checked. Anything not checkable should be held more loosely than the tool's tone invites.

Which returns to the frame the session opened with: the tool closed the execution gap and did nothing for the evaluation gap. Its confidence is not evidence, and treating it as evidence is the same mistake as treating attractiveness as evidence.

### ✍️ Prompt engineering tip

Ask for the assessment in a fixed order and a fixed structure. An open request produces a list of impressions weighted toward whatever is most visually obvious, which is the same bias the session is trying to correct.

---

## Assignments

> **Reserved. Winnie is defining the assignment.**
>
> What the session structure requires: whichever outputs are not completed in the practice block need to be completed here, since both are inputs to downstream work.

---

## Close · Where This Goes Next

Standalone lesson, so nothing is assumed before it and nothing is promised after it. Two natural continuations:

- **Toward prototyping.** The token audit is the input. The five layers become the correction checklist for anything a generative tool produces, which is the difference between prompting until something looks right and knowing when it is.
- **Toward critique.** The decision sheet is the input. A critique against stated reasons is a different exercise from a critique against taste, and considerably more useful to both people in the room.

Adjacent material already in the library: `Library/guides/how-to-give-design-critique` for the critique protocol, `Library/frameworks/framework-nielsen-usability-heuristics.md` for the full set of heuristics this session pulls two from, and `03-develop/design-system` for Atomic Design, which owns the component taxonomy this session deliberately stops short of.

---

## Further Resources

**The anchor finding**
- The Aesthetic-Usability Effect, NN/g: https://www.nngroup.com/articles/aesthetic-usability-effect/

**Layers 1 to 4**
- Intro to the 8-Point Grid System: https://builttoadapt.io/intro-to-the-8-point-grid-system-d2573cde8632
- Building a Visual Language, Airbnb: https://airbnb.design/building-a-visual-language/
- UI Design in Practice: Colors: https://uxmisfit.com/2019/05/21/ui-design-in-practice-colors/
- Colorable, contrast checking: https://colorable.jxnblk.com/
- Progressive Disclosure, NN/g: https://www.nngroup.com/articles/progressive-disclosure/

**Layer 5**
- Mobbin, mobile pattern reference: https://mobbin.design/patterns
- Nielsen's 10 heuristics applied to UI: https://aelaschool.com/en/interactiondesign/10-usability-heuristics-ui-design/
- Responsive data tables, a worked component problem: https://medium.com/appnroll-publication/5-practical-solutions-to-make-responsive-data-tables-ff031c48b122

**The laws, and their limits**
- Laws of UX, reference set: https://lawsofux.com/
- Hick's Law, original framing: https://en.wikipedia.org/wiki/Hick%27s_law
- The 7±2 myth: https://uxmyths.com/post/931925744/myth-23-choices-should-always-be-limited-to-seven
- Your navigation menu doesn't need Miller's rule: https://stephaniewalter.design/blog/your-menu-doesnt-need-millers-7-plus-minus-2-rule/
