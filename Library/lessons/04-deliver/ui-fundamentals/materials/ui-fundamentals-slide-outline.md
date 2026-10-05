# Slide Deck Outline: UI Fundamentals

> **Source of truth:** `ui-fundamentals-lesson.md`
> All content changes (activities, concepts, examples, timing) must be made there first, then reflected here.
> This file contains only slide-specific concerns: layout types, visual hints, kickers, structure, and speaker notes.

> **How to use this file**
> This outline is ready to hand to your own AI tool or process to generate the slide deck; the build prompt isn't included here.
> Speaker notes are written as short bullets, not prose: they're meant to be glanced at while teaching, not read.

---

## Session metadata

| Field | Value |
|---|---|
| Session title | UI Fundamentals |
| Session subtitle | Judging design decisions you didn't make |
| Instructor | Winnie Nguyen |
| Program | Standalone. Fills the Track 1 Session 6 slot when that programme runs |
| Level | Junior |
| Year | 2026 |
| Previous session | None. Standalone |
| Next session | None. Hands off to any prototyping or critique session |
| Running example | Food delivery, order tracking screen. Same case as the senior track: four stages, actual job at waiting-for-delivery |
| Cover photo | A hand holding a phone showing a delivery tracking screen, seen slightly from behind. The viewer can tell something is being judged, not admired |
| Style reference | `../assets/style-reference-schematic.png` |

---

## Visual language

**This is a lesson about seeing. The deck has to be seen, not read.** A student who can recite "proximity means near equals related" and cannot spot a grouping failure has learned a sentence, not a skill. So almost every principle in this deck is shown as a specimen, and the words on the slide are labels for what the eye is already doing.

### Two registers, and the switch between them means something

**SCHEMATIC.** Abstracted UI: grey bars for text, geometric shapes for controls, no real words, no photography. This is the register for teaching a mechanism. Its whole value is that it removes content as a variable, so nobody can be distracted by whether the copy is good or the photo is nice. Only structure is left, and structure is what the five layers are about. Style reference: `../assets/style-reference-schematic.png`.

**REAL.** Fully rendered screens with real type, real colour, real images. This is the register for the stimulus set, the tracking screen and the reveal. It is used wherever *attractiveness itself* is the subject, because a grey-bar wireframe cannot fool anybody and the whole reveal depends on students having been fooled.

**The rule: schematic teaches the mechanism, real shows what fools you.** Each layer runs schematic first, then real. Never mix the two registers inside one slide.

### Schematic drawing kit

| Element | How to draw it |
|---|---|
| Body text | Grey bars, `--ink-ghost`, ~8px tall, 2px radius. Never real words. Vary length to imply content |
| Heading text | Taller, darker bars, `--ink-muted`. Length shorter than body runs |
| Primary button | Filled rounded rect, `--sienna` |
| Secondary button | Outlined rounded rect, `--ink-muted` hairline |
| Input field | Outlined rounded rect, taller than a button, empty |
| Radio / checkbox | Circle. Filled `--sienna` when selected, hairline `--ink-muted` when not |
| Image or map | Flat rect, `--paper-deeper` fill. No icon inside, no mountain glyph |
| Specimen frame | 1.5px `--ink` hairline, square corners, generous internal padding |
| Annotation | `--sienna` arrows, brackets and measurement rules |
| Measurement labels | `--font-mono`, small, `--sienna` |

### Rules for every specimen slide

1. **The frame separates specimen from slide.** Anything inside a hairline frame is a UI being examined. Anything outside it is the deck talking. Never let slide chrome bleed into a specimen.
2. **One accent, pointing at one thing.** `--sienna` marks the element under discussion and nothing else. If two things are purple, the slide is making two arguments and should be two slides.
3. **No red X, no green tick, no "bad" and "good" labels.** Mark what is under discussion and let the student judge. The moment the slide grades the screen, it has done the work the student was supposed to do.
4. **COMPARE slides change exactly one variable.** Same content, same layout, one decision different. Two screens that differ in five ways teach taste. Two that differ in one teach a principle.
5. **Label comparisons in `--font-mono`, neutrally.** "24px" and "18px", not "wrong" and "right".
6. **Measurement is drawn, not described.** If the slide claims a gap is 24, the 24 is on the slide with a bracket. This is the habit that converts a junior's "I think" into "it's 3.9 and it needs 4.5".

### Asset production note

Less work than it looks. The schematic kit is one Figma component set reused across every diagram. The REAL register is one tracking screen built once in its broken state, plus five corrected variants and two effect versions (blurred, desaturated). The stimulus set is the only genuinely separate build.

---

## Slide structure

> **90-minute version, 44 slides.**
> Arc: Open → The Frame → Layers 1 to 4 → The Reveal → Layer 5 → Practice → Close.
> Five teaching layers, each running the same four-beat pattern: the question it answers, the principle (schematic), the worked example (real), the sentence you say to a dev. That repetition is deliberate and should not be varied for interest.
> **The reveal sits at slide 30, not slide 4.** The Aesthetic-Usability Effect only works if students have already been caught by it in the opening. Do not move it earlier.
> **The tracking screen appears in every layer**, each time with all previous layers already corrected. By Layer 5 the students have watched one screen repaired in front of them. That cumulative build is the deck's spine and is also what proves the reading-order claim visually.
> Ten text-only slides out of 44, and half of those carry a small specimen. Every remaining slide shows something.
> **Pacing:** 43 slides across 70 minutes of teaching, so roughly 1.6 minutes each. That is faster than a text deck and it should be. A specimen slide is looked at, not read, and several are questions the room answers in fifteen seconds. The slides that need to breathe are the map problem, the blur test, the Kurosu finding and the closing six-state progression; take time on those and move briskly through the rest.
> Every slide lists on-slide content separately from speaker notes; keep the two from merging back together when building the deck.

---

## 1. Open

---

### COVER
- Year: 2026
- Day label: Standalone
- Title: UI\n*Fundamentals*
- Subtitle: Judging design decisions you didn't make.
- Author: Winnie Nguyen
- Right panel photo: A hand holding a phone at a slight angle, delivery tracking screen visible. Judged, not admired.
- Speaker notes:
  - Do not explain the subtitle yet. It earns itself by minute 50.
  - Say only: today is not about making screens look good.
- 🎨 Visual hint: REAL. Photograph, warm light, slightly overhead. The screen readable enough to identify as a tracking screen, not readable enough to evaluate.

---

### PRACTICE · Which one ships?
- Kicker: Before anything else
- Title: Which one\n*would you ship?*
- On-slide: The stimulus set, 6 to 8 screens of the same product, unlabelled. Instruction: **Pick one. Write the reason in one sentence.**
- Speaker notes:
  - 3 minutes. Silent. No discussion.
  - Do NOT say any of these were AI-generated. That is the whole design of the set.
  - Collect the sentences. Read 2 or 3 aloud, flat, no commentary.
  - Expect "looks cleaner", "more modern", "feels professional".
  - Resist resolving it. The discomfort is the material.
- 🎨 Visual hint: REAL. A grid of 6 to 8 fully rendered screen thumbnails, genuinely attractive, all similar quality. No labels, no numbers that imply ranking, no frames that make one look chosen. They must be hard to choose between.

---

### STATEMENT · The split
- Kicker: What just happened
- Title: Everyone here can *make*\na screen like these.\nNobody can say *why*\none is better.
- On-slide: The same grid, greyed
- Speaker notes:
  - Name it and move on. Do not answer it.
  - The room split. That split is the evidence the session opens on.
  - Leave it sitting there. It gets picked up at minute 50.
- 🎨 Visual hint: REAL, desaturated to near-grey. Three different thumbnails ringed in `--sienna` hairline, showing the room disagreed. The rings are the only colour on the slide.

---

## 2. The Frame

---

### DIAGRAM · Two gulfs
- Kicker: The frame
- Title: Making moved.\n*Judging didn't.*
- On-slide: LEFT **Gulf of Execution** wanting → doing. RIGHT **Gulf of Evaluation** seeing → understanding
- Speaker notes:
  - Norman's two gulfs, turned on the designer instead of the user.
  - Making a screen used to take tool skill, time, craft. That is why juniors couldn't produce senior work.
  - A sentence of prompting now produces a plausible, well-spaced, attractive screen.
  - Nothing in the last few years made it easier to look at three screens and know which is right.
- 🎨 Visual hint: SCHEMATIC. Two identical gap diagrams side by side: a figure glyph on one bank, a screen glyph on the other, the gap drawn as a measured span. LEFT span almost closed, annotated in `--sienna`. RIGHT span at full original width, same annotation style, unchanged. The two spans must be visibly the same drawing so the difference reads as width alone.

---

### STATEMENT · Where the value went
- Kicker: The consequence
- Title: Producing is no longer\nthe thing you're *paid for.*
- On-slide: nothing
- Speaker notes:
  - Say this plainly. Do not soften it.
  - Value sat in making because making was scarce. It isn't.
  - It sits in judging now, because judging is what stayed scarce.
  - Uncomfortable for someone whose title says designer and whose day is spent producing. Let it be uncomfortable.
  - **Judging requires criteria you can name. That's the rest of the session.**
- 🎨 Visual hint: Deliberately blank. The only fully empty slide in the deck, and it should feel like it. No specimen, no diagram, no accent.

---

### STATEMENT · The dev thread
- Kicker: How you'll know it worked
- Title: Every layer today ends\nin a sentence you could\nsay to a *developer.*
- On-slide: Not a rationale. A sentence.
- Speaker notes:
  - The test of understanding a layer is not applying it. It's saying why, to someone who doesn't care about design.
  - Most junior designers lose arguments they were right about.
  - Because the only thing they had available was "it looks better".
  - Flag it now so they listen for the sentence at each layer.
- 🎨 Visual hint: SCHEMATIC. A small empty speech bubble in `--sienna` outline, sized for one short sentence, pointing at a schematic screen fragment. The bubble stays empty here; it gets filled five times later in the deck. Reuse this exact bubble on every dev sentence slide.

---

### DIAGRAM · The Decision Stack
- Kicker: The instrument
- Title: Five layers,\nin *reading order.*
- On-slide: **01 · Space** what belongs with what · **02 · Hierarchy** what gets read first · **03 · Type** how it stays readable · **04 · Colour** what's the one thing to do · **05 · Component** why does this exist
- Speaker notes:
  - Reading order, not importance order.
  - Grouping registers before hierarchy. Hierarchy before type. Type before colour emphasis. The component is the last thing you consciously identify.
  - So they can check their work by looking, not by remembering a list.
  - Also runs most structural to most local, so the expensive mistakes get caught first.
  - **One instrument. Today it gets pointed at three different things.**
- 🎨 Visual hint: SCHEMATIC. One schematic screen shown exploded into five stacked transparent planes, each plane isolating what that layer governs: plane 1 only the gaps, plane 2 only the size and weight differences, plane 3 only the type runs, plane 4 only the filled shapes, plane 5 only the component outlines. Numbered down the side in `--font-mono`. This is the deck's key image; it returns as a small locator on every layer divider.

---

## 3. Layer 1 · Space and Layout

---

### SECTION DIVIDER · Layer 1
- Kicker: Layer 01
- Title: SPACE AND\nLAYOUT
- On-slide: What belongs with what?
- Speaker notes:
  - Most junior screens fail here.
  - Almost nobody diagnoses it here, because it presents as "the screen feels messy".
- 🎨 Visual hint: SCHEMATIC. The five-plane stack from the previous slide, small, upper right, with plane 1 in `--sienna` and the rest ghosted. Same locator treatment on all five dividers.

---

### COMPARE · Proximity
- Kicker: The principle
- Title: Spacing is the first\n*meaning* on the screen.
- On-slide: Two specimens. Identical elements. Only the gaps differ. Mono labels: **8 / 8 / 8** and **8 / 24 / 8**
- Speaker notes:
  - Ask before explaining: how many groups do you see in each?
  - Left reads as one list of six. Right reads as two groups of three. Same six elements.
  - Proximity is not a preference. It's how vision works before conscious attention arrives.
  - **Spacing gets read before any of the words do.**
- 🎨 Visual hint: SCHEMATIC, side by side in matched frames. Six identical grey bars in each. LEFT evenly spaced. RIGHT with one 24px gap in the middle. The gaps themselves annotated with `--sienna` measurement brackets. Nothing else differs, including bar lengths.

---

### COMPARE · Common region
- Kicker: The principle
- Title: A boundary *beats*\nproximity.
- On-slide: Two specimens. LEFT: two bars close together, two far. RIGHT: the far pair enclosed in one card, the close pair split across a card edge
- Speaker notes:
  - Ask which items belong together in each. The answer flips.
  - Two items far apart inside one card read as more related than two close items either side of a card edge.
  - **The recurring mistake this explains:** reaching for a divider or a border when the real problem was the spacing.
  - Borders are a strong tool. Used to patch a spacing problem, they add a second grouping signal that argues with the first.
  - Most juniors have never heard this one. Expect it to land.
- 🎨 Visual hint: SCHEMATIC. Same bars in both frames, same positions. RIGHT adds one hairline card boundary in `--sienna`. The point is that only the boundary was added and the reading changed completely.

---

### DIAGRAM · The 8pt scale
- Kicker: The rule
- Title: Every gap is a\nmultiple of *eight.*
- On-slide: 8 · 16 · 24 · 32 · 40 · 48
- Speaker notes:
  - That's the whole rule. It is not an aesthetic claim.
  - Its value: it converts a question with infinite answers into one with six.
  - "Is this 24 or 25?" stops being something a person can have an opinion about.
  - Which means it stops being something to argue with a developer about. That's most of the point.
- 🎨 Visual hint: SCHEMATIC. A schematic screen with a `--sienna` measurement rule running down its left edge, every gap bracketed and labelled in mono. One gap deliberately at 25 and labelled 25, sitting visibly off the rule's tick marks. Do not mark it wrong; the tick marks do that.

---

### COMPARE · Worked: the tracking screen
- Kicker: Food delivery
- Title: Nothing removed.\nJust *regrouped.*
- On-slide: The tracking screen, before and after, spacing only
- Speaker notes:
  - First time they see the real screen. It comes back in every layer from here.
  - Status and estimated time belong together. Usually not spaced as though they do.
  - Courier name sits close enough to the order contents to read as part of them.
  - Ask: what did I actually change? Answer should be "the gaps".
  - **Same elements, same count, same copy. Only the gaps.**
- 🎨 Visual hint: REAL, both sides fully rendered. Identical content in both. The changed gaps marked with `--sienna` brackets on the AFTER only. Keep every other property identical between the two, including image crop, so the eye has nowhere else to go.

---

### STATEMENT · Dev sentence 01
- Kicker: Say this
- Title: *"Those two are in the same\ngroup, so the gap is 8. The next\ngroup starts at 24. It's the scale,\nnot my preference."*
- On-slide: the corrected specimen, small, beside the quote
- Speaker notes:
  - Have someone read it out loud. It feels strange the first time, which is the point.
  - Note what it does: removes the designer's taste from the sentence entirely.
- 🎨 Visual hint: The empty speech bubble from the frame section, now filled with this sentence, pointing at a small SCHEMATIC fragment showing the two gaps. Same bubble, same position, on all five dev sentence slides so they read as a series.

---

## 4. Layer 2 · Hierarchy

---

### SECTION DIVIDER · Layer 2
- Kicker: Layer 02
- Title: HIERARCHY
- On-slide: What gets read first?
- Speaker notes:
  - Not "make the important thing bigger".
- 🎨 Visual hint: Five-plane locator, plane 2 in `--sienna`.

---

### DIAGRAM · Four levers
- Kicker: The principle
- Title: Size is only the\n*most obvious* one.
- On-slide: **01 · Size** · **02 · Weight** · **03 · Colour** · **04 · Space**
- Speaker notes:
  - Same-size screen can have perfect hierarchy if the other three work.
  - Five type sizes can have none.
  - Von Restorff: the item that differs is the one noticed. So emphasis is a fixed budget.
  - **Three primary buttons is zero primary buttons.**
- 🎨 Visual hint: SCHEMATIC. Four small specimens in a row, identical content in each, each one establishing the same hierarchy using only one lever. Fourth specimen uses space alone and should be the most surprising. Bottom of slide: a fifth specimen using all four at once on three different elements, visibly failing.

---

### COMPARE · Two firsts
- Kicker: The failure mode
- Title: Which one is\n*primary?*
- On-slide: LEFT: one filled button, one outlined. RIGHT: two filled buttons. Ask the room.
- Speaker notes:
  - Ask it as a real question. Wait for the room to answer the right-hand one.
  - The failure is not too many sizes. It's two elements both trying to be first.
  - **If a student can't say which element gets read first on their own screen, it doesn't have hierarchy. It has variety.**
  - Point forward: they will find this on their own screen in the practice block.
- 🎨 Visual hint: SCHEMATIC. Matched specimens. LEFT has exactly one `--sienna` filled element. RIGHT has two. No labels, no marks. The slide asks the question and refuses to answer it.

---

### IMAGE · The blur test
- Kicker: A tool you can keep
- Title: Blur it. The content goes.\nThe *hierarchy stays.*
- On-slide: The tracking screen, heavily blurred
- Speaker notes:
  - Purely a demonstration. Show it, let them look, then show the unblurred version.
  - Blur removes content and leaves structure. What you can still see is what a user sees in the first half second.
  - **If nothing dominates when it's blurred, nothing dominates.**
  - Tell them to use this on their own screens. It costs nothing and it works forever.
  - Have them squint at the room's own screens if there's time.
- 🎨 Visual hint: REAL. The tracking screen at a heavy gaussian blur, full bleed or near it. No annotation at all on this slide. The next click reveals the sharp version at the same size and position for direct comparison.

---

### COMPARE · Worked: the map problem
- Kicker: Food delivery
- Title: The prettiest element\nis the *least useful* one.
- On-slide: The tracking screen. Beside it, the actual job: *"let me stop fearing it's not coming."*
- Speaker notes:
  - This is the whole session in one screen. Sit on it.
  - The map is almost always largest and most colourful. It's also the least useful thing here.
  - The job is fear reduction. What answers it: the status, and the promise that the app will tell you when something changes.
  - What doesn't: a motorbike moving on a map, which mostly gives you something to stare at while you keep worrying.
  - **Why the junior version leads with the map:** attractiveness was the only criterion they had.
  - The evidence says lead with reassurance. Evidence, not taste.
- 🎨 Visual hint: REAL, both sides, spacing already corrected from Layer 1 so the cumulative build is visible. BEFORE: map dominant. AFTER: status and the notification promise dominant, map reduced to a supporting band. The actual-job quote sits outside both frames in `--sienna`, with a thin line to the element that answers it in the AFTER.

---

### TWO-COLUMN · Two laws you'll hear quoted wrongly
- Kicker: Scope check
- Title: A rule has a *scope.*\nCheck it before you\ninvoke it.
- On-slide: LEFT **Hick's Law** "reaction time among simple, unfamiliar, equally likely options" / *Not* a scan of a labelled, grouped menu. RIGHT **Miller's 7±2** "immediate memory span, mostly about chunking" / *Not* a limit on nav items. Recognition, not recall.
- Speaker notes:
  - 3 minutes. They will hear both used as arguments and need to know when the argument is invalid.
  - Hick's: standard misuse is "nav must have fewer than five items". A categorised list of 20 routinely beats an ungrouped 8.
  - Grouping and labelling beat item-count reduction.
  - Miller's: those items are on screen being read, not held in mind. Different task entirely.
  - **Not trivia.** A designer who quotes a law that doesn't apply loses the argument and some credibility with it.
- 🎨 Visual hint: SCHEMATIC, one small specimen per column proving the counter-case. LEFT: an ungrouped list of 8 bars beside a grouped, labelled list of 20, the 20 visibly easier to parse. RIGHT: a nav bar of 9 items that is obviously fine to read. The specimens carry the argument; the text only names it.

---

### STATEMENT · Dev sentence 02
- Kicker: Say this
- Title: *"The status is the primary.\nIf it can't be the biggest element,\nit has to be the highest contrast\none. It can't be neither."*
- On-slide: the corrected specimen, small, beside the quote
- Speaker notes:
  - Note the structure: it names a constraint, not a preference.
  - "It can't be neither" is the part that ends the conversation.
- 🎨 Visual hint: Series bubble, filled. Small SCHEMATIC fragment showing one dominant element among four.

---

## 5. Layer 3 · Type

---

### SECTION DIVIDER · Layer 3
- Kicker: Layer 03
- Title: TYPE
- On-slide: How does the reading order stay readable?
- Speaker notes:
  - Shortest layer. 7 minutes.
  - **Say out loud that this layer has no named law behind it.**
  - Not every design decision has a psychology paper underneath it. Some of it is craft with conventions.
  - Pretending otherwise teaches them to reach for a citation they don't have, which will embarrass them in front of an engineer.
- 🎨 Visual hint: Five-plane locator, plane 3 in `--sienna`.

---

### COMPARE · Three and two
- Kicker: The rule
- Title: Three sizes and two weights\nbeat *nine of each.*
- On-slide: LEFT: seven sizes, several 2px apart, labelled in mono. RIGHT: three sizes and two weights, same content
- Speaker notes:
  - Junior screens typically carry 6 or 7 sizes, most differing by 2px, communicating nothing.
  - **A difference the eye can't reliably detect isn't a hierarchy signal. It's noise with maintenance cost.**
  - Point at the 2px pairs and ask which is bigger. Nobody will be sure. That is the demonstration.
  - Decide the ratio between steps, then everything takes a value from the scale. Same logic as the 8pt grid: remove opinion from the decision.
  - Line height belongs to the size, not the block. It lives in the scale.
  - Measure affects whether a paragraph gets read more than the typeface does. Juniors adjust the typeface.
- 🎨 Visual hint: This one uses real type rather than bars, since the subject is type. Matched frames, identical copy in both. Every size labelled in mono beside it. LEFT deliberately includes 15/16/17px so the indistinguishable pairs are visible as numbers but not as sizes. RIGHT shows the three-step scale with its line heights bracketed in `--sienna`.

---

### DIAGRAM · The diagnostic
- Kicker: When it goes wrong
- Title: Needing a fourth size means\nthe problem *isn't the type.*
- On-slide: It's Layer 2, unresolved.
- Speaker notes:
  - This is the diagnostic that makes the layer worth teaching.
  - They're trying to fix a hierarchy problem with a type solution.
  - Send them back up the stack rather than down it.
- 🎨 Visual hint: SCHEMATIC. The five-plane stack with a `--sienna` arrow travelling from plane 3 back up to plane 2. Beside it, one specimen shown twice: once "fixed" by adding a fourth type size and still unclear, once fixed by changing the spacing and clear at three sizes.

---

### STATEMENT · Dev sentence 03
- Kicker: Say this
- Title: *"Three sizes, two weights, all\non the scale. If I need a fourth,\nsomething upstream is wrong\nand I should fix that instead."*
- On-slide: the type scale, small, beside the quote
- Speaker notes:
  - The second half is what makes it credible. It admits a failure condition.
- 🎨 Visual hint: Series bubble, filled. Small specimen of the three-step scale.

---

## 6. Layer 4 · Colour

---

### SECTION DIVIDER · Layer 4
- Kicker: Layer 04
- Title: COLOUR
- On-slide: What is the one thing to do here?
- Speaker notes:
  - Note the question. Not "what palette", not "what mood".
- 🎨 Visual hint: Five-plane locator, plane 4 in `--sienna`.

---

### DIAGRAM · Roles, not palettes
- Kicker: The principle
- Title: A colour isn't a colour.\nIt's a *job.*
- On-slide: Brand · Neutral · Success · Warning · Error, each with its surface and text values
- Speaker notes:
  - Junior version of this layer: pick a palette that looks nice.
  - Working version: assign meaning, then never use a meaning-carrying colour for anything else.
  - **The moment error red is also the primary button, the screen has lost the ability to say error.**
  - Von Restorff again, which is why this layer is short. Colour is the strongest emphasis lever, so the easiest to spend badly.
  - If the primary action isn't the only saturated element, it isn't the primary action.
- 🎨 Visual hint: Five role chips in a row, each showing its surface and text pairing with the ratio printed on it. Beneath: one schematic screen where the error colour is also the primary button, and an error message on the same screen that has visibly nowhere to go. Do not label it as an error; let the collision be seen.

---

### IMAGE · The desaturate test
- Kicker: A second tool you can keep
- Title: Take the colour out.\nIs the hierarchy *still there?*
- On-slide: The tracking screen in greyscale
- Speaker notes:
  - Pairs with the blur test. Blur asks whether structure survives without content. Greyscale asks whether hierarchy survives without colour.
  - **If the primary action disappears in greyscale, colour was doing all the work and the screen fails for anyone who can't rely on it.**
  - This is also the cheapest accessibility check they will ever run, and it costs one toggle.
  - Show the colour version after, same size and position.
- 🎨 Visual hint: REAL. Tracking screen fully desaturated, full bleed or near it, no annotation. Next click restores colour at identical size and position. Two versions worth preparing: one where hierarchy survives, one where it collapses.

---

### COMPARE · One rule and a tool
- Kicker: Contrast
- Title: 4.5:1 for body.\n3:1 for large text and\nanything that *carries meaning.*
- On-slide: Two text samples with their measured ratios printed large. WCAG 2.1 AA. Check it, don't estimate it.
- Speaker notes:
  - One rule and the habit of running the tool. Accessibility as a topic deserves its own session and doesn't fit in 10 minutes.
  - **Why a hard gate rather than a guideline:** it's the only decision on this screen with a correct answer.
  - A junior arguing from a measured number instead of a preference is in a completely different conversation.
  - Worked example: the tracking screen's status text is frequently mid-grey on white. Fails by a small margin, and nobody notices because the screen looks calm.
  - **Calm and unreadable are easy to confuse.** Say this line.
- 🎨 Visual hint: Two real text samples side by side, deliberately similar. Make the failing one look pleasant. Ratios printed beneath each in large mono, `--sienna` on the failing number only. No X, no tick. The number is the verdict.

---

### STATEMENT · Dev sentence 04
- Kicker: Say this
- Title: *"Red is our error role. If we use\nit for the primary button we lose\nthe ability to show an error\non this screen."*
- On-slide: the role chips, small, beside the quote
- Speaker notes:
  - Names a capability being lost, not a rule being broken. Harder to argue with.
- 🎨 Visual hint: Series bubble, filled. Small specimen of the five role chips.

---

## 7. The Reveal

---

### IMAGE · Back to the start
- Kicker: Minute 49
- Title: So why did you pick\n*that one?*
- On-slide: The original stimulus set, back at full size
- Speaker notes:
  - Ask who picked what. Read out one of their original one-sentence reasons.
  - Do not answer yet. Let them try first, with four layers of vocabulary they didn't have at minute 3.
  - Expect better answers now. That improvement is worth naming out loud before the reveal.
- 🎨 Visual hint: REAL, full saturation, larger than the opening grid. Their original handwritten-style reasons overlaid on three of them, small, in `--ink-muted`.

---

### DIAGRAM · Kurosu and Kashimura, 1995
- Kicker: The finding
- Title: People believe attractive\nthings *work better.*
- On-slide: 252 participants · 26 ATM interface variations · appeal correlated more strongly with **perceived** ease of use than with **actual** ease of use
- Speaker notes:
  - Hitachi Design Center, 1995. Tractinsky replicated it in Israel expecting culture to weaken it. Found it stronger.
  - **So do designers. So did everyone in this room forty-five minutes ago.**
  - For users this is real and useful: attractive design buys tolerance, and that's a genuine advantage. It has a ceiling. Serious problems break through regardless.
  - For designers it's a trap: attractiveness hides problems from the person evaluating.
  - In a usability test, participants struggle through a task then praise the visuals, and the real defect never gets named.
- 🎨 Visual hint: Two scatter plots on shared axes, drawn plainly. "Appeal vs perceived usability" steep and tight, `--sienna`. "Appeal vs actual usability" shallow and scattered, `--ink-muted`. No chart junk, no gridlines beyond the axes.

---

### DIAGRAM · The floor rose
- Kicker: Why this matters now
- Title: Attractiveness only works\nas a signal while\nattractiveness is *scarce.*
- On-slide: It isn't any more.
- Speaker notes:
  - Generative tools raised the aesthetic floor for everybody. Nearly everything looks fine now.
  - So looking fine stopped discriminating between options.
  - **A designer whose only evaluation tool was taste has quietly lost their only evaluation tool.**
  - Now reveal the set: some were generated, some were real. Nobody was told, deliberately.
  - The moment you know a screen came from an AI tool you start hunting for tells instead of applying criteria.
  - **The source never mattered. The criteria are the same either way.**
- 🎨 Visual hint: A distribution curve of "visual quality" shown twice: a wide, low old curve in `--ink-muted`, and a compressed curve piled against the ceiling in `--sienna`. Beneath, the stimulus thumbnails re-shown with their sources finally labelled in mono, deliberately interleaved so no pattern is visible.

---

## 8. Layer 5 · Components

---

### SECTION DIVIDER · Layer 5
- Kicker: Layer 05
- Title: COMPONENTS
- On-slide: Why does this thing exist, and when should I not use it?
- Speaker notes:
  - Heaviest layer, 12 minutes, and the one closest to their daily frustration.
  - Most likely to overrun. Worth overrunning for.
  - Only layer with a political dimension: they're being taught to evaluate their manager's work.
- 🎨 Visual hint: Five-plane locator, plane 5 in `--sienna`.

---

### COMPARE · Jakob's Law
- Kicker: Familiarity
- Title: Familiarity isn't a lack\nof *ambition.*
- On-slide: LEFT a conventional control. RIGHT a novel one doing the same job
- Speaker notes:
  - People spend most of their time on other products and prefer yours to work like the ones they know.
  - A novel component costs the user learning time, and that cost needs a benefit you can name.
  - Ask what the right-hand one buys. Usually nothing the designer can articulate.
  - Not an argument against invention. An argument for being able to justify it.
- 🎨 Visual hint: SCHEMATIC, matched frames, same task in each. LEFT a standard control drawn from the kit. RIGHT the same function as an invented control. Neither marked. Let the room work out which one they'd rather hand to a user.

---

### DIAGRAM · A component is inherited reasoning
- Kicker: What's baked in
- Title: Somebody else's thinking,\nalready *defended.*
- On-slide: Default · hover · focus · active · disabled · loading · error · empty
- Speaker notes:
  - **Using the system isn't a constraint on creativity. It's reuse of thinking.**
  - A student who gets this stops experiencing the design system as a cage. That shift is worth the whole layer.
  - States are what juniors skip.
  - **A component defined only in its default state is a picture, not a component.**
  - The missing states become a developer's improvisation, which means the designer stopped making the decisions partway through.
  - Ask how many of the eight exist in their own team's button. Expect three.
- 🎨 Visual hint: SCHEMATIC. One button exploded into its eight states in a grid, each labelled in mono. Default drawn solid. The other seven drawn in `--sienna` hairline outline only, so what's usually missing is literally an outline waiting to be filled.

---

### DIAGRAM · Tesler's Law
- Kicker: The best law for this conversation
- Title: Complexity can't be removed.\nOnly *moved.*
- On-slide: Either the user absorbs it, or the system does.
- Speaker notes:
  - The single most useful law in this session for talking to devs and BAs.
  - It converts a taste argument into an allocation question.
  - "I think this should be simpler" invites disagreement.
  - "This complexity has to live somewhere, and right now it lives with the user. Can it live with us instead?" invites a decision.
  - **Engineers respond to the second framing because it's the framing they already use.**
- 🎨 Visual hint: SCHEMATIC. A single mass on a beam between two labelled ends, "user" and "system". Shown twice: mass at the user end, mass at the system end. Identical mass in both, `--sienna`. The beam tilts; the mass never shrinks.

---

### DIAGRAM · The hard case
- Kicker: What if it's actually bad?
- Title: Your confusion is data.\nIt just doesn't say *whose\nfault* it is.
- On-slide: TWO POSSIBILITIES: **The component is well-reasoned** and you haven't learned to read it · **The component is sloppy** and your confusion is accurate. ONE TEST: run the five layers on the component itself.
- Speaker notes:
  - Often it IS bad. Say so honestly rather than pretending systems are always right.
  - This is the Gulf of Evaluation again, one level up. They can't judge the screen, and they can't judge the system that made it.
  - Answer is neither "trust the system" nor "critique the system".
  - Space: internal spacing on the scale? Hierarchy: one clear primary? Type: same scale as everything else? Colour: roles hold, contrast passes in every state? Component: all states defined?
  - Resolves → the gap is theirs, it's a learning problem, good news.
  - Doesn't resolve → the gap is the component's, and they now have specific language instead of a vague feeling.
  - **Third surface today. Screens they didn't make, their own screen, and now the system that made both. Same instrument.**
- 🎨 Visual hint: SCHEMATIC. The five-plane stack rotated ninety degrees and aimed at a single component instead of a screen, so the instrument is visibly being reused. Two of the five planes flagged in `--sienna` with mono labels reading "doesn't resolve". The other three plain.

---

### STATEMENT · The guardrail
- Kicker: Say this out loud
- Title: Ask.\n*Don't indict.*
- On-slide: > *"I ran our button against these five checks and the internal spacing and the disabled state don't resolve for me. Can you walk me through the reasoning?"*
- Speaker notes:
  - Do not assume this is obvious. Read it out.
  - That question makes a junior look careful.
  - The same observation delivered as "our design system is broken" makes them look like a problem.
  - And that will be remembered longer than whether they were right.
  - **A junior who is right and unemployable hasn't won anything.**
- 🎨 Visual hint: Two speech bubbles using the deck's series bubble shape. The question in `--sienna`, open and generously sized. The accusation in `--ink-ghost`, smaller and tighter. Same words are not used in both; the contrast is in the framing, not the volume.

---

### STATEMENT · Dev sentence 05
- Kicker: Say this
- Title: *"Our button already handles\ndisabled and loading. If I make\na new one, we maintain two\nof them forever."*
- On-slide: all five sentences, stacked small beneath
- Speaker notes:
  - Ends on cost, which is the language the person on the other side is already thinking in.
  - Point back at all five: **none of them contain the word "looks".**
- 🎨 Visual hint: The fifth series bubble, filled. Beneath it the four earlier bubbles shown small and complete, so the set reads as a finished collection. This is the payoff for repeating the same bubble all session.

---

## 9. Practice

---

### MILESTONE · Practice
- Kicker: Practice
- Num: 16 min
- Title: Run the stack\non *your* screen
- Prompt: *Reserved. Winnie to define.*
- On-slide: nothing else
- Speaker notes:
  - **Activity not yet defined.** Time is held; the constraints below are what the session structure requires of whatever fills it.
  - Must produce the **decision sheet**, or something recording reasons rather than only changes. Downstream critique has nothing to work with otherwise.
  - Must produce the **token audit**: what the team already uses for spacing, type and colour roles, with gaps and inconsistencies named.
  - Runs on **their own screen**, not food delivery. Food delivery is the teaching surface; their work is the practice surface.
  - Share-back is stronger in a developer's register than a design-mentor register. They find the register shift harder than the content, which makes it diagnostic.
  - If the team has no system: derive the implicit one from their own screen instead. Most teams have an accidental system nobody wrote down.
  - **In a 1:1 this goes quiet.** Set a checkpoint around minute 8 where they read out one row.
  - Remind them of the blur and desaturate tests. Both apply to their own screen in seconds.
- 🎨 Visual hint: Full-bleed milestone treatment. Large "16 min", title, prompt. No diagram.

---

## 10. Close

---

### DIAGRAM · The screen, all five layers
- Kicker: What we did to it
- Title: One screen.\n*Five decisions.*
- On-slide: The tracking screen in six states, left to right: original, then after each layer
- Speaker notes:
  - The payoff for carrying one screen all session. Let them look before saying anything.
  - Ask which single step made the biggest difference. Answers vary and all of them are interesting.
  - **Note that fixing the spacing first made the hierarchy problem visible.** That's why the layers run in reading order, and they just watched it happen rather than being told.
  - Nothing was added. No new element, no new copy, no new image.
- 🎨 Visual hint: REAL. Six thumbnails of the same screen in a row, each labelled in mono with the layer just applied. The progression must be legible at a glance from the back of a room. This is the deck's closing image and worth building carefully.

---

### TWO-COLUMN · Two outputs
- Kicker: What leaves the room
- Title: One shows what you did.\nThe other shows *why.*
- On-slide: LEFT **Decision sheet** what changed · which layer · which rule · the sentence you'd say to a dev. RIGHT **Token audit** what your team already uses · what's inconsistent · what's undefined
- Speaker notes:
  - The revised screen is not the output. Anyone can show a revised screen.
  - Only the why can be argued with productively.
  - The audit is not an invented set. Most teams have an accidental system nobody documented.
  - **The person who documents it becomes useful out of all proportion to the effort.** Say this to a junior; it's a concrete career move they can make on Monday.
  - Where they go: tokens are the input to any prototyping work, and they're what stops a generative tool inventing its own system on every screen.
  - The decision sheet is the input to any critique. Question stops being "do you like it?" and becomes "does the stated reason hold?"
- 🎨 Visual hint: Two document specimens side by side, drawn in the schematic kit as filled-in sheets rather than blank ones. Arrows from each pointing right to a labelled destination.

---

### STATEMENT · The one thing
- Kicker: Carry this out
- Title: You'll spend most of your\ncareer judging work\n*you didn't make.*
- On-slide: The five layers are not a checklist for making screens. They're how you form an opinion you can defend.
- Speaker notes:
  - Land the subtitle from the cover. It has earned itself by now.
  - Every surface today was inherited: screens they didn't make, their own screen once it existed, the component someone else built, the tokens someone else defined.
  - Not one thing in this session was invented from blank. That's the actual condition of the job.
  - **And being able to defend an opinion at all is rarer than it should be.**
- 🎨 Visual hint: SCHEMATIC. The three surfaces from the session as three small specimens (a grid of screens, one screen, one component), all three feeding into the five-plane instrument in `--sienna`. The instrument is the constant; the surfaces change.

---

### END
- Title: UI Fundamentals
- Subtitle: Judging design decisions you didn't make.
- On-slide: Winnie Nguyen · 2026
- Speaker notes:
  - None.
- 🎨 Visual hint: Same visual language as the cover, quieter. The tracking screen now shown in its corrected state, small.
