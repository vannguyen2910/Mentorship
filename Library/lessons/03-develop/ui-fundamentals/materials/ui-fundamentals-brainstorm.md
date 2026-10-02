---
title: "UI Fundamentals: Lesson Brainstorm & Desk Research"
type: brainstorm
program: standalone
level: junior
status: draft
date: 2026-09-09
---

# UI Fundamentals: Lesson Brainstorm & Desk Research

Working document to shape Track 1, Session 6. Prep material, not yet a `*-lesson.md` / `*-slide-outline.md` pair.

**Scoping decisions locked in:**
- One 90-minute session. Not split into 6a/6b, no buffer slot consumed.
- **Standalone library lesson**, level-tagged Junior. Lives in `03-develop/ui-fundamentals/`. It happens to fill the Track 1 Session 6 slot named in the service catalog, but it is not written into that sequence and any programme can pull it.
- Taught evaluation-first: judgment is the skill, visual craft is the evidence behind it.
- Practice runs on whatever screen the student brings from their own work, not on a prescribed prior-session artifact.
- **Tokens: audit what the team already has**, do not invent a new set. Employed juniors usually inherit tokens somebody else defined. Fallback for a student whose team has none: derive a minimal set from their own screen.
- **Audience: mostly employed juniors.** Students have a job, an inherited component library, and real developers and BAs. The dev-conversation thread is used the same week, not rehearsed. See section 1 for the positioning consequence.
- **Stimulus: mixed set.** AI-generated screens and real product screens in the same set, students not told which is which. Makes the point that the source does not change the criteria.
- **System-agnostic.** The five layers are taught as portable principles. No single public design system is anchored on, so the lesson does not assume what the student uses at work.
- **Worked example: food delivery**, continuing the canonical case already running through the senior track rather than introducing a parallel one. See section 3a.

**Where it sits:** Develop stage. Standalone, but it slots naturally between an IA session and any prototyping or critique session, and it fills the Track 1 Session 6 slot when that programme runs.

```
(any screen the student brings)
      |
UI FUNDAMENTALS  ->  ui-decision-sheet.md + documented token set
      |
prototyping session   (tokens as input; the stack as the AI-correction checklist)
      |
critique session      (critiques against the student's own decision sheet)
```

The two outputs are what make it chainable. Nothing upstream is assumed.

---

## 1. The Problem This Lesson Solves

The obvious reading is that junior designers lack visual vocabulary: they do not know type scales, they do not know spacing systems, they pick colours by feel. That reading produces a "visual design basics" lesson, and that lesson already exists in a hundred places on the internet. It is not what is actually failing.

The real failure is **defensible reasoning**. Evidence, from a real mentee message (career changer, 8 months in, now titled UI Designer):

- She can produce screens. Production is not the blocker.
- She is confused by her manager's existing components and does not know when to use them.
- She cannot hold a design conversation with a developer or a BA.
- She studied at training centres, but they assumed design principles were already known and skipped them.

Every one of those is a judgment problem, not a making problem.

**The frame: Gulf of Execution vs Gulf of Evaluation.** Norman's two gulfs describe the distance between intention and action (execution), and between system state and understanding (evaluation). Applied to the designer rather than the end user, generative AI tools have collapsed the Gulf of Execution almost to zero: producing a plausible, attractive screen now costs a sentence of prompting. They have done nothing for the Gulf of Evaluation. A junior can now generate three competent-looking options and has no criteria to choose between them.

That is the sentence the lesson exists to fix: *"em không biết cái nào là đúng."*

So the job moved. It used to be mostly making. It is now mostly judging, and judging requires named criteria you can say out loud.

**Positioning flag, unresolved.** The service catalog describes Track 1 students as career transitioners, 0 to 2 years, "mostly pre-income." The students who actually turn up are employed juniors with a manager, a component library and a squad. That gap is not this lesson's problem to fix, but it does mean two of this session's strongest beats (Layer 5's component interrogation, and the dev sentence at every layer) assume employment that the catalog copy does not promise. Either the catalog description gets updated to match who enrols, or this session sits closer to Track 2 than its numbering suggests. Worth resolving before the catalog goes in front of a prospective student, same class of discrepancy as the two already logged in `track-senior-lead.md`.

---

## 2. The Anchor: the Aesthetic-Usability Effect

If the lesson has one load-bearing research finding, this is it, because it is the scientific name for the exact trap the students are in.

**Kurosu & Kashimura (1995), Hitachi Design Center.** 252 participants rated 26 variations of an ATM interface. The correlation between rated aesthetic appeal and *perceived* ease of use was stronger than the correlation between aesthetic appeal and *actual* ease of use. Tractinsky replicated it in Israel (1997) expecting a cultural difference and found the effect even stronger.

Two consequences, and the second is the one nobody teaches juniors:

1. **For users:** attractive design buys tolerance. People forgive small friction in something that looks good. This is real and it is a competitive advantage. It has a ceiling, though: severe usability problems break through the goodwill regardless of how the thing looks.
2. **For designers and researchers:** attractive design *hides problems from you*. In usability testing, participants struggle through a task and then praise the visuals, and the real defect never gets named.

Point 2 is why a junior cannot pick between three AI-generated screens. All three are attractive. Attractiveness is exactly the signal that stops being diagnostic once everything is attractive. AI raised the aesthetic floor for everyone, which means aesthetics no longer discriminate, which means judgment has to come from somewhere else.

**Teaching move:** run the judgment activity *before* naming this effect, let the students pick the prettiest option, then name what just happened to them. Self-demonstration beats explanation.

---

## 3. The Decision Stack

Five layers, taught in decision order rather than as five topics. Each layer runs the same loop: see it broken, name the rule, say the sentence you would say to a developer, fix it live. Five repetitions of one pattern is what makes it hold in 50 minutes.

| # | Layer | The question it answers | Grounding |
|---|---|---|---|
| 1 | Space & Layout | What belongs with what? | Gestalt: proximity, common region. 8pt spacing scale |
| 2 | Hierarchy | What gets read first? | Von Restorff. F-pattern scanning. Serial position |
| 3 | Type | How does the reading order stay readable? | Type scale, line height, measure. Legibility research |
| 4 | Colour | What is the one thing to do here? | Von Restorff. Semantic roles. WCAG 2.1 AA as a hard gate |
| 5 | Components | Why does this thing exist and when do I not use it? | Jakob's Law. Tesler's Law. Error prevention |

**Why this order.** It runs from the decisions that are cheapest to change and most structural, down to the ones that are most local. It also matches the order in which a screen is *read*: grouping registers before hierarchy, hierarchy before type, type before colour emphasis, and the component is the last thing you consciously identify. Teaching in reading order means students can check their work by looking, not by remembering a list.

**Layer 1 is where the most damage gets undone.** Most junior screens fail at grouping, not at prettiness. Gestalt proximity says elements near each other are perceived as related, and common region says a shared boundary (a card, a panel) beats proximity when the two compete. Juniors reach for borders and dividers when the actual fix is space. The 8pt scale gives them a decision rule instead of a feeling: every gap is a multiple of 8, so "is this 24 or 25?" stops being a question.

**Layer 5 is the heaviest and answers the mentee's question directly.** "Why does my manager's component exist?" is the real curriculum here. A component encodes decisions somebody already made and defended: states, spacing, minimum sizes, accessibility behaviour. Using it is not a constraint on creativity, it is inherited reasoning. The skill is knowing what is baked in, and knowing the narrow conditions under which you would justify making a new one.

This layer stops short of Atomic Design vocabulary, which `03-develop/design-framework/` owns.

**The hard case: what if the inherited component is simply bad?** Often it is. A confused junior cannot tell which of two things is true: the component is well-reasoned and she has not learned to read it, or the component is genuinely sloppy and her confusion is accurate information. That is the Gulf of Evaluation again, one level up: she cannot judge the screen, and she cannot judge the system that produced the screen.

The resolution is neither "trust the system" nor "critique the system." It is to **run the same five layers on the component itself**. If its decisions resolve against the stack, the gap is hers and it is a learning problem. If two of them do not resolve, the gap is the component's, and she now has specific language instead of a vague feeling.

Three reasons this is the right teaching move:
1. It applies one instrument to a third surface (screens she did not make, her own screen, the component she inherited), which demonstrates the stack is portable rather than a screen-checking trick.
2. It converts "I'm confused" into a question a senior will respect: *"I ran our button against these five checks and the spacing and the disabled state don't resolve. Can you walk me through the reasoning?"* That is how a junior earns credibility rather than spending it.
3. It costs almost no additional teaching time, because the instrument is already built by the time Layer 5 runs.

**Guardrail, and it must be said out loud in the session:** ask, do not indict. A junior who arrives on Monday announcing the design system is broken has made her position worse regardless of whether she is right.

---

## 3a. The Worked Example: Food Delivery, Tracking Screen

Track 1 continues the canonical food delivery case rather than introducing a parallel one. Same product across tracks, different altitude: the senior track reasons about *why* the waiting-for-delivery stage matters, Track 1 designs the screen that stage happens on.

The natural surface is **the order tracking screen**, and it is a genuinely good teaching surface rather than a convenient one:

- It is stage 3 of the canonical four stages, and stage 3 is the marked focus area of the whole running case.
- The canonical actual job is *"let me stop fearing it's not coming."* That gives Layer 2 a real answer to "what should be read first?" which is not a matter of taste: whatever reassures. Most junior versions of this screen lead with the map, which is the most attractive element and the least reassuring one. That is the Aesthetic-Usability Effect visible in a single screen.
- It has genuine grouping problems for Layer 1 (status, ETA, courier, order contents, actions all competing) and genuine component and state problems for Layer 5.
- Because the job is already documented from interviews, a design decision on this screen can be defended with evidence rather than preference, which is the entire point of the session.

Canonical details are fixed and must not be varied. They live in the senior track's files and in project memory: four stages, the stage 3 job in both long and short form, the stakeholder-assumed job, the 2-of-3 evidence shape and the deliberately unpromoted third interview. Read the current state of those files before drafting, since they are edited directly between sessions.

---

## 4. Laws Shortlist

The nine-rule infographic maps cleanly onto established laws. Mapping it out is worth doing because it converts a list of tips into a body of knowledge with citations, which is exactly the "defensible" part of the lesson.

| Infographic rule | Law / principle | Source |
|---|---|---|
| 1. Use Familiar Patterns | **Jakob's Law** | Nielsen, 2000 |
| 2. Reduce the Choices | **Hick's Law** (Hick-Hyman) | Hick 1952, Hyman 1953 |
| 3. Design for Scanning | **F-pattern scanning**; Law of Prägnanz | NN/g eyetracking 2006, 2017; Gestalt 1920s |
| 4. Show the Options | **Recognition over recall** (Heuristic 6); Miller's chunking | Nielsen 1994; Miller 1956 |
| 5. Show Progress | **Goal-Gradient Effect**; Zeigarnik Effect | Hull 1932; Kivetz, Urminsky & Zheng 2006; Zeigarnik 1927 |
| 6. Set Smart Defaults | **Default Effect / status quo bias** | Samuelson & Zeckhauser 1988; Johnson & Goldstein 2003 |
| 7. Prevent Accidental Loss | **Error prevention** (Heuristic 5); poka-yoke; loss aversion | Nielsen 1994; Shingo; Kahneman & Tversky 1979 |
| 8. Use Contrast | **Von Restorff (isolation) Effect**; Fitts's Law | von Restorff 1933; Fitts 1954 |
| 9. End with Clarity | **Peak-End Rule** | Kahneman, Fredrickson, Schreiber & Redelmeier 1993 |

**Worth adding, in priority order:**

1. **Aesthetic-Usability Effect** (Kurosu & Kashimura 1995). Non-negotiable. It is the lesson's thesis. See section 2.
2. **Tesler's Law / Conservation of Complexity** (Larry Tesler). Complexity cannot be removed, only moved: either the user absorbs it or the system does. This is the single best law for the "talking to dev and BA" thread, because it reframes a design argument from taste ("I think it should be simpler") into an allocation question ("who absorbs this complexity, and is that the right party?"). Developers respond to that framing.
3. **Gestalt: proximity, similarity, common region** (Wertheimer, Koffka, Köhler, 1920s). The mechanism under Layer 1. Common region is the one juniors have never heard of and immediately use.
4. **Fitts's Law** (Fitts 1954). Target size and distance. Connects directly to the WCAG AA touch target minimum, so it does double duty as an accessibility rule with a reason attached.
5. **Doherty Threshold** (IBM 1982, ~400ms). Perceived performance, loading and skeleton states. Optional; overlaps with Session 8's states coverage.

**Recommended teaching load: 8 named laws, not 14.** One anchor per layer plus the thesis:

- Thesis: Aesthetic-Usability Effect
- Layer 1: Gestalt proximity + common region
- Layer 2: Von Restorff + F-pattern
- Layer 3: (no named law; type is craft, and pretending otherwise is padding)
- Layer 4: Von Restorff again, applied to colour + WCAG AA
- Layer 5: Jakob's Law, Tesler's Law, error prevention

The rest belong to Session 8 (Interaction Design & Critique), which already owns states, flows and the critique format. Progress indicators, defaults, success states and confirmation dialogs are behavioural and state decisions, and four of the nine infographic rules land there rather than here. That boundary should be explicit in both lesson files so the two sessions do not duplicate.

---

## 5. Teach Against the Misapplications

A short beat here does more for credibility than another law does, and it is the difference between a designer who quotes laws and one who understands them. Two candidates, both extremely common in Vietnamese design communities and both cited constantly by juniors:

**Hick's Law is over-applied.** It describes reaction time for a choice among a set of simple, equally probable, unfamiliar options. It does not describe a person scanning a well-categorised menu or a familiar list, where the user is not evaluating every item serially. Using it to argue "our navigation must have fewer than 5 items" is the standard misuse. The honest version: grouping and labelling beat raw item-count reduction, and a categorised list of 20 outperforms an ungrouped list of 8.

**Miller's Law is misapplied almost universally.** Miller (1956) measured immediate memory span for items a person had to *hold in memory*, and the paper itself was partly about chunking, not a design constraint. It says nothing about how many links a navigation bar may have, because the items on screen are being *read*, not memorised. A menu is recognition, not recall. Teaching this correction is a fast credibility win and it directly serves the "talk to dev and BA" goal, because it teaches students to check whether a rule actually applies before invoking it.

---

## 6. Activities and Assignment

**Winnie is defining these.** Not specified here.

What the research does constrain, and what any activity design needs to satisfy:

- **Time budget.** The five layers need roughly 50 minutes if each is taught see-it-broken / name-the-rule / say-the-dev-sentence / fix-it-live. That leaves about 30 minutes for hook, activity and close in a 90-minute slot.
- **Required output 1: a documented token set.** Not an invented one. The student audits the spacing scale, type scale and colour roles their team already uses, writes them down, and notes what is inconsistent or undefined. A student whose team has none derives a minimal set from their own screen instead. Any downstream prototyping session needs this as input.
- **Required output 2: a written record of *why*.** A revised screen alone is not enough, because any critique session downstream has to critique the reasoning, not the pixels.
- **Sequencing note from section 2.** If any activity involves judging screens, the Aesthetic-Usability Effect should be named *after* students have picked, not before. Self-demonstration is the only way that finding lands.
- **Register.** Any share-back is stronger delivered as if to a developer rather than to a design mentor. Students find the register shift harder than the content, which is diagnostic in itself.

---

## 7. Boundaries With Adjacent Lessons

| Adjacent | Owns | This lesson must not |
|---|---|---|
| `03-develop/design-framework` (Atomic Design) | Atoms/molecules/organisms vocabulary, library architecture | Teach the atomic taxonomy. Layer 5 stops at component anatomy and reuse logic |
| S7 AI Prototype Development | Build loop, correcting AI output, tokens in practice | Teach prototyping mechanics. It hands over the tokens and the checklist only |
| S8 Interaction Design & Critique | All UI states, task vs user flows, critique format | Teach state design or run a full critique. Progress, defaults and success states belong there |
| `Library/guides/how-to-give-design-critique` | Critique protocol | Redefine a critique format |
| `Library/frameworks/framework-nielsen-usability-heuristics.md` | The 10 heuristics | Restate all ten. Pull heuristics 5 and 6 only |

---

## 8. Resources

**Already in the Knowledge Sharing bank (usable as-is):**

| Resource | Layer |
|---|---|
| Intro to the 8-Point Grid System | 1 |
| Airbnb: Building a Visual Language | 3, 4 |
| UI Design in Practice: Colors (UXMISFIT) | 4 |
| Colorable (contrast tool) | 4 |
| Progressive Disclosure (NN/g) | 2 |
| Mobbin pattern library | 5 |
| 5 Practical Solutions for Responsive Data Tables | 5 |
| Tabs on Mobile (MS Teams) | 5 |
| Nielsen's 10 Heuristics for UI | 5 |
| Dark Patterns | Ethics beat |
| Atomic Design (EN and VI) | Handover only |

**Gaps the bank does not cover, sourced here:**

- Aesthetic-Usability Effect: https://www.nngroup.com/articles/aesthetic-usability-effect/
- Laws of UX (reference set for the shortlist): https://lawsofux.com/
- Hick's Law original framing and limits: https://en.wikipedia.org/wiki/Hick%27s_law
- Miller's 7±2 as a design myth: https://uxmyths.com/post/931925744/myth-23-choices-should-always-be-limited-to-seven
- Navigation does not need 7±2 (Stéphanie Walter): https://stephaniewalter.design/blog/your-menu-doesnt-need-millers-7-plus-minus-2-rule/
- Goal-gradient (Kivetz, Urminsky & Zheng 2006): https://journals.sagepub.com/doi/abs/10.1509/jmkr.43.1.39

**Still to source before the build:**

- Gestalt common region, a clean visual explainer suitable for beginners
- Type scale: a defensible ratio-based method rather than "pick these sizes"
- F-pattern / layer-cake scanning: the NN/g eyetracking source
- Legacy material to mine: `Source/my-teaching/ui-ux-class/ui-ux-class-oct-2019/Day 2 - Color Theory.pdf` and `Day 4 to 6 - Design Components.key`; `Source/my-teaching/internal-uiux-class/week-2/` has a typescale reference image and moodboard set

---

## 9. Open Questions

1. **The title.** "UI Fundamentals" is the service catalog's name, but the lesson as scoped is not really about fundamentals. Every surface it touches is something the student *inherited and must evaluate*: screens they did not make, a component somebody else built, tokens somebody else defined. The honest subject is judging design decisions you did not make. Worth deciding whether the file keeps the catalog name for findability or takes a name that matches what it teaches.
2. **Stimulus set.** Mixed AI-generated and real product screens, close in attractiveness, differing on one layer each. Must be built before first delivery. Reusable, and the single largest prep cost in the session.
3. **The food delivery tracking screen** has to be built for the slides at a teachable level of wrongness. See section 3a.
4. **Language.** Vietnamese or English delivery. Law names stay in English; explanations follow the code-switching conventions in the writing style guide.
5. **Slide count.** Existing outlines in the library run 17 to 33 slides. Target not yet set.
