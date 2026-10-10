---
title: "Lesson 3: Scaling the Prototype"
lesson_file: "lesson-3-scaling-the-prototype.md"
level: "intermediate"
slide_count: 30
duration: "90 min"
status: drafted
built_deck: ""
last_synced: 2026-09-20
---

> **Source of truth, for now: the lesson file.** No deck exists yet, so `lesson-3-scaling-the-prototype.md` is canonical for prompt wording, timing and instructor notes, and this outline is the spec the deck gets built from. **Once the deck is built, reverse-sync this file from it**, exactly as Lesson 2's outline does.
> **Speaker notes are short scannable bullets — changed from the connected-sentence convention on 2026-09-20, at Winnie's request, for reading at a glance while teaching.** Lessons 1 and 2 still use connected sentences, so the three decks now diverge on this. When Lesson 3's deck is built, carry the bullets into it. **Bold marks the thing to actually say out loud**; the rest is the facilitator's own cue, not a script.
> **Cover title is the lesson title, not a tagline — a deliberate departure from Lessons 1 and 2.** Lesson 3's cover says "Scaling the Prototype," the same as its title. "Build Once, Scale by Rule" is retired, not demoted to a subtitle.
> **Spine reworked (2026-09-20) to match how Winnie actually works.** The previous outline taught rule *harvesting* — build one screen slowly, mine its corrections for rules, then build the rest. The real workflow is the reverse: **set the rules first**, feed the AI an existing user flow, build the whole journey in one prompt. Sections 1 and 2 were rewritten around that; Sections 3 and 4 are unchanged. If a deck gets built from an older copy of this file, the tell is a Section 1 called "The Expensive First Screen" — that outline is superseded.
> **Every prompt on screen is short and plain — no CARE breakdown anywhere in this deck.** Same decision as Lesson 2.
> **Two slides exist to tell the truth rather than teach a step — 9 and 17.** Slide 9 says the starter rules aren't the student's yet; slide 17 says only tokens propagate automatically. Neither is padding; neither gets cut for time.

---

## Session metadata

| Field | Value |
|---|---|
| Program | SYSTEMATIC AI PROTOTYPING |
| Track / session | Lesson 3 |
| Stage | Develop |
| Prior session | Lesson 2: Build Your Design System |
| Next session | Lesson 4: Present & Publish |
| Running example | The student's own anchor project — their own flow, their own second journey |
| Cover visual | Full-bleed photo panel right, instructor avatar + name + title bottom-left of the text panel |

---

## Slide structure — 30 slides

> Cover and an agenda slide, then four sections each opening on a full-bleed divider: **Section 1 "Rules Before Prompts"** (7), **Section 2 "One Prompt, One Journey"** (9), **Section 3 "One Product, Many Journeys"** (3), **Section 4 "Stitch the Journey"** (4). Closes on the Closing slide.
> **Section 2 carries 42 of the 90 minutes across 9 slides.** Section 1 moves briskly — 7 slides in 18 minutes. Section 2 stops dead on slides 12 and 14.
> **The order is the argument.** Rules → flow → build → review. If the build prompt ever moves earlier, the lesson stops working: the one-prompt build is only safe because the rules exist.
> **Slides 13–15 carry the one genuinely new idea** — the layer ladder and its test question. Slide 14 gets the most visual weight in the deck.
> **Slide 12's notes carry the departure from the source lesson** — "one screen at a time" is not taught here. That belongs in the notes, not on screen.
> **Section 3 teaches a question, not an example.** The three places to look stay in the notes deliberately — on screen they become a menu.

---

## 0. Cover & Agenda

---

### COVER · Cover
- Category line: SYSTEMATIC AI PROTOTYPING
- Kicker: LESSON 3
- Title: Scaling the\nPrototype (second line accented)
- Subtitle: Set the rules before you prompt, hand the AI your user flow, build the journey in one pass — then review it, scale it, and stitch it.
- Author: Winnie Nguyen — UX Product Design Instructor
- Speaker notes:
  - Name today's output first: 2 journeys built + reviewed, a rules file that changes the output, 1 stitched thread walkable in 60s
  - **"The screens aren't the deliverable today. The rules file is."**
  - Specifically: the version he rewrites after the first review
  - Say it now, repeat it at the close
- 🎨 Visual: Full-bleed photo right panel, text panel left with avatar, name and title bottom-left.

---

### AGENDA · The Order Is the Lesson
- Kicker: Ninety minutes
- Title: Rules. Flow.\nBuild. Review.
- On-slide, numbered: 1 Set the rules — before any prompt · 2 Feed the flow you already have · 3 Build the journey in one pass · 4 Review it — the longest part · 5 Do it again, cheaper, on a second journey
- On-slide line: Most of today is steps 1 and 4. The build is the short bit.
- Speaker notes:
  - Map, not content — walk the five fast
  - **"The prompting is the short part. Rules and review are where the time goes."**
  - Inverts what he expects — correct it now, not at minute 40
  - The trade: 1 prompt = less typing, one big pile of corrections instead of five small ones
  - Running late? Step 5 → scope-only + homework. Never cut 1, 3 or 4
- 🎨 Visual: Five numbered bars of visibly uneven width, the first and fourth much wider than the rest.

---

## 1. Rules Before Prompts

---

### SECTION DIVIDER · Section 1: Rules Before Prompts
- Kicker: Section 1
- Ghost numeral: 1
- Title: Rules Before Prompts
- On-slide: The constraints go in first. Everything after is cheaper because of it.
- Speaker notes:
  - Transition beat — say the name, let it sit
  - **"The difference between using AI occasionally and doing this systematically is whether the rules existed before the first prompt."**
  - No new concepts yet
- 🎨 Visual: Full-bleed dark, giant low-opacity ghost numeral "1," yellow mono "Section 1" tag.

---

### STATEMENT · The System, Not the Product
- Kicker: Recap, not re-teach
- Title: Four files.\nZero screens.
- On-slide: tokens.css · component-inventory.md · template-<type>.html · interaction-pattern.md → design-system.html
- On-slide line: Everything you built describes the product. Nothing you built is the product.
- Speaker notes:
  - Ask him to name the four files from memory — **before** the list appears
  - Can't name them → re-anchor now, or the rules step lands flat
  - Homework check, one question: **"does every scoped screen have a template?"**
  - Gap still open → fix it here. A minute now, a segment later
- 🎨 Visual: Four muted file chips feeding one accented page chip, arrow between.

---

### STATEMENT · Reasonable Is the Problem
- Kicker: Why rules come first
- Title: It won't make\nan error.\nIt'll make a\ndifferent product.
- On-slide: A component that looks like yours. A hex value near your token. A state nobody designed. None of it reads as wrong on screen.
- On-slide line: Constraints applied afterwards mean finding and undoing all of it, screen by screen.
- Speaker notes:
  - The argument the whole section rests on — don't rush
  - Unconstrained AI + a design system still makes something **reasonable** — that's the problem
  - **"A slightly-off button isn't a bug report. It's a slightly different product."**
  - By the time you notice, it's on every screen
  - Governance line: **"If the tool can read your system it generates on-system. If it can't, it generates something else."**
  - System = what exists. Rules = what the tool may do with it
- 🎨 Visual: Two near-identical component rows side by side, differences marked subtly — same shape, wrong values.

---

### STATEMENT · What It Will Get Wrong
- Kicker: Predictable enough to write down in advance
- Title: Assembled.\nRough.\nGeneric.
- On-slide three findings: Misses spacing, grouping and hierarchy — even with a detailed prompt · Defaults to neutral, minimalist visuals with no identity, unless told otherwise · Follows directions well; weighs design tradeoffs badly
- On-slide line: Boringly consistent across tools and projects. A consistent failure is a rule waiting to be written.
- Speaker notes:
  - Sits before the rules, not after — it's what makes a starter set possible
  - Source: NN/g, AI prototyping in real design contexts
  - **"These aren't your tool's quirks. They repeat — which is why someone can hand you rules before you've made the mistake."**
  - If he's already seen it → name it as confirmation, not warning
- 🎨 Visual: Three stacked finding cards, muted, with a single accented line beneath.

---

### CODE · Where the Rules Live
- Kicker: Into the file you already made
- Title: Two sections,\none file.
- On-slide code: `# Project rules & context` / `## Where things live` — tokens, inventory, interaction pattern, templates, screens, checkpoint page / `## Rules for building screens` — the constraints
- On-slide line: Pointers go stale when files move. Rules go stale when the system changes. Keep them separable.
- Speaker notes:
  - Goes in the **Lesson 1 rules/context file** — not a new file
  - Two jobs now, so label both halves or you can't tell which is stale
  - Stale context files actively degrade output — maintain it like the artifacts
  - ⚠️ **Check the wiring before moving on** — is the tool actually reading it?
  - Not wired → the next 40 minutes are theatre
- 🎨 Visual: Single file card split into two labelled bands, monospace, the second band taller.

---

### NUMBERED · Rules 1–5: The System Rules
- Kicker: What the prototype is allowed to be made of
- Title: Five rules\nabout the system.
- On-slide list: 1 Only components from the inventory — if it's missing, add it there first, then build · 2 No raw values, ever — tokens only, and flag what doesn't exist · 3 Screens inherit the template, they don't fork it · 4 Every build carries flow context · 5 Real content, never lorem ipsum
- Speaker notes:
  - Don't read all five — land 1, 2, 3
  - **1 + 2 = the whole answer to "don't use anything outside the design system"**
  - Rule 2's second clause: **flag what doesn't exist** — stops a missing token becoming an invented hex that looks fine
  - Rule 3 makes propagation possible later; without it every screen is its own template
  - Rule 5: lorem ipsum hides hierarchy problems until the demo
  - Rule 4 is last lesson's habit, written down — don't labour it
- 🎨 Visual: Five numbered rules, numbers in accent, rules 1 and 2 subtly emphasised.

---

### NUMBERED · Rules 6–10: The Working Rules
- Kicker: How you and the tool behave
- Title: Five rules\nabout working.
- On-slide list: 6 One layer per edit, named in the prompt · 7 Attach only the files the step needs · 8 Flag, don't invent — every generation ends with what it couldn't do · 9 Save before a structural edit · 10 WCAG 2.1 AA on every screen — contrast, visible focus, target size
- Speaker notes:
  - Land 7 and 10, let the slide carry the rest
  - **7 is counterintuitive: more context doesn't help, it widens what the tool might modify.** Needs 3 files? 30 makes it worse
  - **10 is new to this arc.** AI screens routinely ship invisible focus + near-miss contrast
  - Next lesson it's at a public URL
  - **"Enforcing it at generation costs nothing. Auditing it afterwards costs a session."**
  - It's a rule, not a review — no audit today
  - 9 becomes literal next lesson, when "save" stops meaning Cmd-S
- 🎨 Visual: Five numbered rules, numbers in accent, rules 7 and 10 subtly emphasised.

---

### STATEMENT · These Rules Aren't Yours Yet
- Kicker: The honest bit
- Title: You'll believe\nthree of these\ntoday.
- On-slide: These came from someone else's scar tissue — a mentor's practice and published research. Not from anything you've watched go wrong on your product.
- On-slide, what happens next: The rest earn belief in the review · The ones that stick are the ones you rewrite in your own words · A rules file that hasn't changed since week one isn't being used
- Speaker notes:
  - Say it out loud — he's already thinking it
  - Both true at once: handing over rules is what a masterclass is for **and** a rule you didn't earn is one you drop under pressure
  - He'll believe ~3 today — usually 1, 2, 8 (failures he can picture)
  - Rest earn belief in ~20 min, at the review
  - ⚠️ **Don't oversell to compensate** — one rule visibly failing discredits all ten
  - Frame: well-founded starting point he *will* edit. The edit is slide 16, not a vague promise
- 🎨 Visual: Ten rule chips, three accented and seven muted, with a forward arrow labelled to the later rewrite slide.

---

## 2. One Prompt, One Journey

---

### SECTION DIVIDER · Section 2: One Prompt, One Journey
- Kicker: Section 2
- Ghost numeral: 2
- Title: One Prompt,\nOne Journey
- On-slide: Feed the flow. Build it all at once. Then spend the time where it matters.
- Speaker notes:
  - Transition beat
  - **"This is where the rules file starts paying for itself."**
  - 42 of the 90 minutes are in this section — say it, so the pace change doesn't feel like drift
- 🎨 Visual: Full-bleed dark, ghost numeral "2," yellow mono "Section 2" tag.

---

### METHOD · Three Ways In
- Kicker: The AI needs the journey before it can build it
- Title: Feed the flow\nyou already have.
- On-slide three methods: **A — You have a flow artifact.** Figma flow, FigJam, journey map, written flow. Paste, screenshot, or read it live. · **B — Nothing written down.** Describe it: screens in order, what the user does, what moves them on. · **C — interaction-pattern.md.** Already in the project from Lesson 2.
- On-slide line: The flow is the thread. The component inventory is the parts.
- Speaker notes:
  - Confirm which one applies → walk **only** that path. Same as last lesson's three methods
  - **A is the common case for a senior designer, and the fastest** — thinking's done, just not handed over
  - Say the closing line deliberately: a flow says which screens + what connects them, **not** what components each needs
  - Risk: rich-looking flow → he drops the inventory from the prompt
  - Whichever method: **save the flow into the project**, don't leave it in the prompt
  - Messy flow? Feed it anyway — gaps come back as flagged items, faster than re-reading it
- 🎨 Visual: Three input chips converging on one file chip, A accented, B and C muted.

---

### PROMPT · Build the Journey
- Kicker: One prompt, not five
- Title: Build the\nwhole journey.
- On-slide prompt: "Build the [journey] journey as a working prototype. The flow: [paste the flow, or describe it].
  Use tokens.css, component-inventory.md and template-[type].html as they are — read them, don't restate them. Follow the project rules.
  Output one HTML file per screen at screens/[journey]/, linked to each other in flow order.
  End with a list of anything you had to invent, and anything in the flow you couldn't build from the system."
- On-slide callout: Got a reference screenshot? Attach it before you prompt.
- Speaker notes:
  - Three load-bearing clauses:
    - **"Read them, don't restate them"** — if he pastes the inventory in, the router file isn't wired
    - **"Follow the project rules"** — the whole last section in four words
    - **"End with a list of anything you had to invent"** — front-loads the review
  - **If he asks why not one screen at a time** (source lesson says to):
    - That advice existed when nothing constrained output except the sequence
    - Tokens + inventory + templates + rules now constrain every screen equally
    - **"The constraint moved from the sequence into the system."**
    - Flow context stops being something you retype — AI sees the whole thread
    - Seams get designed, not reconciled afterwards
  - ⚠️ Say the cost **before** the build: one prompt = one large pile of corrections. That's why the next three slides are the longest part of the day
- 🎨 Visual: One prompt card feeding a row of linked screen files.

---

### TABLE · How Big Is the Fix?
- Kicker: Review, question one of two
- Title: Chat, point,\nor drag.
- On-slide table: Chat → broad or structural changes, anything needing explanation · Targeted feedback → one specific element, named exactly and located · Direct adjustment → spacing and alignment you can drag
- On-slide line: Start with the build's own list of what it invented. Then walk the screens in flow order, not file order.
- Speaker notes:
  - Point at the on-slide line first — the sequencing is what makes 15 min enough
  - **1. Read the build's own "what I invented" list** — fastest route to real gaps
  - **2. Walk screens in flow order, not file order** — the journey is the unit now
    - Does the thread hold? Does each screen lead where the flow says? Does carried-over state carry?
  - The three modes: from the source lesson, unchanged — he mostly does this by instinct
  - Screen not working at all → **"save what we have and try a completely different layout"** (don't overwrite blindly)
  - Bridge: **"That's how big. It doesn't tell you where."**
- 🎨 Visual: Three-row table, each row with a size indicator from large to small.

---

### DIAGRAM · Fix at the Right Layer
- Kicker: Review, question two — the one that decides whether this scales
- Title: Where does\nthe fix belong?
- On-slide ladder (widest to narrowest): tokens.css — every screen, every journey · component-inventory.md — every use of that component · template-<type>.html — every screen of that type · screen.html — this screen only
- On-slide rule: Fix at the highest layer the symptom is true at.
- Speaker notes:
  - ⭐ Most important slide in the deck — give it room
  - Walk the ladder **bottom up**, then state the rule
  - Anchor each rung to something on his actual screen right now:
    - Wrong heading copy here → instance
    - Every screen of this type missing a back link → template
    - Blue wrong everywhere → token
    - A state built that isn't in the system → inventory
  - Fifth rung, not on the ladder: **screen with nowhere to go → flow, fix in interaction-pattern.md**
  - ⚠️ Missing state → add to component-inventory.md, **not** regenerate from Figma. He will instinctively go back to Figma
  - Anything fixed above instance has to be pushed down — that's slide 18
- 🎨 Visual: Four stacked bars, descending width, top three accented as "system," bottom one muted as "instance." Downward arrow on the left.

---

### STATEMENT · Two Ways to Get It Wrong
- Kicker: The test question
- Title: "Is this wrong\non more than\none screen?"
- On-slide, two failure modes: **Fix too low** — you fix it again on every screen, and the versions drift apart a little more each time · **Push too high** — the system carries something only one screen ever needed
- On-slide line: Not the highest layer available. The highest layer it's actually true at.
- Speaker notes:
  - Drill the question — this is what he uses without you in the room
  - **Point out his advantage right now: a whole journey is built, so he can answer by looking, not predicting**
  - That's the one thing journey-at-once gives you at review time — use it deliberately
  - **Fix too low** = the expected failure. Screen-by-screen prototyping through the back door
  - **Push too high** = nobody warns you. How an inventory fills with one-offs
  - Same question corrects both — memorise the question, not the table
- 🎨 Visual: Two opposing arrows against the ladder silhouette, one too short, one overshooting.

---

### STATEMENT · Now Rewrite Them
- Kicker: The rules become yours
- Title: Which rule\ncaught something?
- On-slide, two passes: **What worked** — name the rules that caught something. Those are believed now, not accepted. · **What no rule covered** — that's a new rule, in your words, at the top of the list.
- On-slide line: A correction you'd make again on the next journey is a rule by definition.
- Speaker notes:
  - 5 minutes — the most important 5 for what happens after the programme
  - **Call back to slide 9 explicitly**: the handed-over set stops being someone else's the moment he rewrites part of it
  - **Make him name which rules caught something** — don't name them for him
  - Pruning: a rule that caught nothing isn't necessarily wrong — **mark it, don't delete it**, revisit after journey two
  - Close with the test he applies alone: **"A rules file that hasn't changed since week one isn't being used."**
- 🎨 Visual: The ten rule chips from slide 9, now with several accented and one new chip in a different treatment at the top.

---

### STATEMENT · What Actually Propagates
- Kicker: The honest version
- Title: One layer\nupdates itself.\nThe rest is\na prompt.
- On-slide three-part: tokens.css → **automatic.** Every screen links it. One edit, whole prototype. · templates and components → **prompted.** Nothing moves until you run it. · "it updates automatically" → doing a lot of work in most demos of this.
- Speaker notes:
  - He'll ask whether a template change updates every screen — answer before he asks
  - Credibility slide as much as a content one
  - **Tokens: genuinely automatic.** One file, one edit, whole prototype — land it as the payoff of last lesson's token sync
  - Everything else: a prompt, governed by rule 3
  - **"Most demos of this are quietly vague about which layer they mean."**
  - **"Yours updates reliably. That's more useful than automatically."**
- 🎨 Visual: Three stacked bands — one marked automatic and accented, one marked prompted and muted, one a quiet caveat line in sienna.

---

### PROMPT · The Propagation Prompt
- Kicker: Pushing a system change down to built screens
- Title: Only that\nchange.\nNothing else.
- On-slide prompt: "I've changed [file]. Every screen in screens/ was built from it. Update each screen to match that change — only that change, nothing else. List every file you touched and what changed in each. If a screen has diverged from the template in other ways, report it — don't fix it."
- On-slide, three clauses labelled: only that change → scope · list what you touched → visibility · report, don't fix → control
- Speaker notes:
  - ⭐ **Run it live** on whatever template-layer fix came out of the review — there'll be one
  - Running it beats describing it: makes the layer ladder usable, not theoretical
  - Three clauses, three failures they prevent:
    - **"Only that change"** — wide brief = wide edits. How a working prototype breaks between two screens you weren't watching
    - **"List every file you touched"** — blast radius visible instead of trusted
    - **"Report, don't fix"** — drift stays information, not a second uncontrolled edit
- 🎨 Visual: Prompt card with the three clauses pulled out as labelled tags beneath.

---

### REFERENCE · The Grown-Up Version
- Kicker: You're not inventing this
- Title: Change the\nlayout once.\nEvery page\nupdates.
- On-slide: The GOV.UK Prototype Kit — pages extend a shared layout; change the layout and every page using it updates. Designers, at government scale, running this model with propagation built in.
- On-slide line: Ours is prompted instead of built in. Same idea, no build step.
- Speaker notes:
  - One minute. Here for credibility, not technique
  - Answers the fair question: is this a workaround that falls apart at scale?
  - **Government service teams have prototyped this way for years** — shared layout, pages extend it, one change reaches every page
  - Plus separate route files per version of a journey
  - Same model as ours, minus the build step, prompt where they have inheritance
  - Frame as direction of travel: **"Nothing you learn today gets thrown away if this outgrows plain HTML."**
- 🎨 Visual: One layout block feeding multiple page blocks, with the changed element highlighted in all of them.

---

## 3. One Product, Many Journeys

---

### SECTION DIVIDER · Section 3: One Product, Many Journeys
- Kicker: Section 3
- Ghost numeral: 3
- Title: One Product,\nMany Journeys
- On-slide: A prototype of one journey is a demo of a fragment.
- Speaker notes:
  - Transition beat
  - **"You've built a thread, not a product."**
  - Someone else touches the same thing, for a different reason — nothing built so far says anything about them
- 🎨 Visual: Full-bleed dark, ghost numeral "3," yellow mono "Section 3" tag.

---

### QUESTION · Who Else Touches This?
- Kicker: Scope journey two
- Title: Who else\ntouches this object,\nand what are they\ntrying to do with it?
- On-slide: Same system. Different thread. One user goal, two or three screens.
- Speaker notes:
  - Put the question up. **Let him answer before you offer anything** — the silence is doing work
  - Only if he genuinely stalls, offer as prompts (not a list):
    - **Second persona on the same object** — customer submits, someone reviews/approves. Best case for stitching: the journey no squad ever demos
    - **Second goal, same persona** — what he does the other 90% of the time
    - **The unhappy path** — error, empty, rejected. Ties back to inventory states never built
  - ⚠️ Keep these **off the screen** — on a slide they become a menu, and picking isn't scoping
  - Then scope like journey one: one goal, 2–3 screens
- 🎨 Visual: One central object with several actor paths converging on it, only one path currently drawn solid.

---

### STATEMENT · One Folder Per Journey
- Kicker: Before you build
- Title: screens/\njourney-name/
- On-slide, two housekeeping moves: **Screens** — one folder per journey, so the propagation prompt's blast radius stays legible and the stitch index is trivial to generate · **Interaction pattern** — a second thread in the same file, not a second file. One map of the product.
- On-slide watch-for: A screen type with no template? One quick addition now — not a surprise at the stitch.
- Speaker notes:
  - 90 seconds of housekeeping — looks like admin, saves a mess
  - Folder split → "every screen in screens/journey-two/" means something precise in a propagation prompt
  - **Interaction pattern stays ONE file** — tempting to split per journey, but the next section is about where threads meet, and a split map can't show you
  - Same instinct as separate route files + one shared design system: separate the threads, share the system
  - Watch-for is normal: new screen type = one more template. 5 min here, broken stitch later
- 🎨 Visual: Folder tree with two journey folders under screens/, and a single interaction-pattern file beside them feeding both.

---

### STATEMENT · It Should Be Cheap
- Kicker: The real test
- Title: If it isn't\nmuch cheaper,\nthe rules aren't\nworking.
- On-slide: Less prompting, and visibly less correcting — because the rules file was just rewritten from journey one's review. That's a finding, not a failure.
- Speaker notes:
  - ⭐ Name the test **before** he builds — a prediction, not a rationalisation afterwards
  - **This is where the lesson stops being a claim and becomes evidence**
  - Sharper than it looks: the rules file changed 20 minutes ago. Not cheaper → the rewrite didn't take
  - Diagnose, don't push through. Three usual causes:
    - Rules too vague to be checkable
    - Sitting in a file the tool doesn't read
    - Corrections that should've become rules and didn't
  - Running behind? **This is the cut point** — journey two becomes scope-only + homework. The question and the test matter, not the screens
- 🎨 Visual: Two journey bars side by side, the second visibly shorter, with a shared system layer beneath both.

---

## 4. Stitch the Journey

---

### SECTION DIVIDER · Section 4: Stitch the Journey
- Kicker: Section 4
- Ghost numeral: 4
- Title: Stitch the Journey
- On-slide: Thread, gather, index, seams, walk.
- Speaker notes:
  - Transition beat
  - **"Individual screens are an expert demo. A stitched journey is a user demo."**
  - Completely different conversations — the second one aligns stakeholders and surfaces real gaps
- 🎨 Visual: Full-bleed dark, ghost numeral "4," yellow mono "Section 4" tag.

---

### STATEMENT · Thread, Then Gather
- Kicker: Before you build anything
- Title: One sentence.\nThen collect.
- On-slide, two steps: **1 Define the thread** — "the user's goal across all of these screens is ___." Every screen serves it, or it doesn't belong. · **2 Gather, don't rebuild** — a stitch is not a redesign. A missing screen is a gap you note, not a task you start.
- On-slide line: Two journeys means two threads meeting at one object. Say where they meet.
- Speaker notes:
  - **Make him say the thread sentence out loud, in one sentence, before anything gets built**
  - It's the filter that keeps a stitch from sprawling — a bad one is why stitches sprawl
  - **Two journeys = two threads meeting at one object. That meeting point is the most interesting seam in the prototype**
  - It's the handoff — one person's job becoming another's. What a single-squad demo never shows
  - ⚠️ The urge to rebuild a "nearly right" screen is the fastest way to lose this segment. Note it as a gap, move on
- 🎨 Visual: Two converging threads meeting at a single highlighted node, loose screens gathered along each.

---

### PROMPT · Index, Then Seams
- Kicker: The actual stitching
- Title: A front door,\nthen the doors\nbetween rooms.
- On-slide index prompt: "Here are my prototype screens: [list with status]. Generate index.html: grouped by journey, with status, links to each, and the journey flow. Use tokens.css and follow the project rules."
- On-slide seams prompt: "I have these screens as separate HTML files: [list]. Add a navigation wrapper that stitches them into one prototype — links from each screen to the next in its journey, a way back to the index, and an indicator of where the user is. Put the shared chrome in the template, not in each screen."
- Speaker notes:
  - **Read the seams prompt's last clause aloud: "put the shared chrome in the template, not in each screen"**
  - That's rule 3 at the exact moment it's most tempting to break — nav is shared by definition
  - Chrome into each screen = hand-forking every file in the prototype
  - Index: **status matters as much as links** (complete / in progress / missing). The gap view is half of what makes it useful to a stakeholder
  - **"Don't perfect transitions. Get the path walkable."** A clickable thing that goes to the next screen is enough
  - Segment ends when you can walk it, not when it's smooth
- 🎨 Visual: Index page block above, screen blocks below with seam arrows between them and back-links to the index.

---

### STATEMENT · Walk It. Note It. Don't Fix It.
- Kicker: The walk is the critique
- Title: Walk it.\nNote it.\nDon't fix it.
- On-slide: Walk the journey in character, narrating the user's goal — not the design decisions. Log every flaw. Fix nothing.
- On-slide capture table: Where | What | Layer
- On-slide quote: "A stitch prototype reveals inconsistency — it is not an audit tool." — Nathan Curtis
- Speaker notes:
  - ⚠️ **Say up front that nothing gets fixed in this segment. Then hold it.** 10 min of walking becomes 20 of fixing and the walk never finishes
  - Curtis's reasoning, not just the rule: a design review kills the collaboration that makes stitching work
  - **Third column is where the layer ladder pays off twice** — the triage list comes out already sorted
  - 6 instance notes + 1 token note → he knows what to do first, without you
  - Walk over a minute? **That's a finding about the thread, not about polish**
- 🎨 Visual: Three-column capture table with a few example rows, one row's Layer cell accented.

---

### NUMBERED · The Stitch Mindset
- Kicker: Three things to believe before you demo it
- Title: It's meant to\nbe thrown away.
- On-slide list: 1 **It's a throwaway artefact** — it exists to communicate the journey while the product gets built, and it retires the day the product ships · 2 **The goal is the journey, not the screens** — inconsistencies will be visible, and that's what stitching is for · 3 **One minute hooks the room** — walk the user's goal, not the design decisions, then stop and invite discussion
- Speaker notes:
  - 90 seconds, worth it even at the end of a long session — changes how he treats the artefact
  - **"Treating a stitch like a deliverable is what makes people polish it instead of using it."**
  - Communication tool with an expiry date → permission to leave the seams visible
  - 2 makes 1 bearable: a polished demo hides exactly what a stakeholder needs to see. **The roughness is the feature**
  - 3 is a hard constraint, not a guideline. Over a minute → fix the thread sentence, not the screens
  - Homework: walk it alone and time it
- 🎨 Visual: Three numbered cards, the first with a subtle expiry or fade treatment.

---

## 5. Closing

---

### CLOSING · What You've Got
- Kicker: Lesson 3
- Title: The screens aren't\nthe deliverable.\nThe rules file is.
- On-slide checklist: Two journeys built and reviewed · A rules file that has changed since it was handed to you · index.html stitching both journeys · A triage list, already sorted by layer
- On-slide next line: Next: present it, then publish it to a real URL.
- Speaker notes:
  - **Point at checklist item 2** — the rewritten rules file is the one that matters
  - **"That's what produces screens on your next project, for a different product, without me in the room."** That's the capability he came for
  - Homework, quickly:
    - Work the triage list **highest layer first**
    - Finish journey two if only scoped
    - Walk it alone and time it — over 60s = tighten the thread, not the screens
    - Add any rule the homework earns
    - Draft 3 sentences introducing the prototype to someone new (raw material for next lesson, not a script)
  - ⚠️ **Confirm GitHub account + GitHub Desktop installed before next session** — install friction shouldn't eat session time
- 🎨 Visual: Four-item checklist with purple check marks, the second item subtly emphasised, author signature bottom right.

---

*Slide outline · Winnie Nguyen · Private Training · Last updated September 2026*
