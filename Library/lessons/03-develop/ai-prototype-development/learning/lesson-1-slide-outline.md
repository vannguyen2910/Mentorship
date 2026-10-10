# Lesson 1: Stop Starting From Zero

> **Source of truth:** this file now documents the actual, final built deck (`AI Prototyping - Lesson 1.html`, in `library/lessons/03-develop/ai-prototype-development/standalone program/`). It was reverse-synced from the live deck on 2026-09-15, so wording, order, and structure here should match what's on screen exactly.
> `lesson-1-project-setup-pattern-first-method.md` remains the source of truth for teaching content, timing, and instructor notes. If the two ever disagree going forward, treat the live deck as the presentation reality and flag the lesson file for reconciliation rather than silently trusting either one.
> **Reconciled 2026-09-18:** the "Build It" gap this note used to flag (lesson file still taught Pre-Flight/token-sync/component-inventory as Lesson 1 content, deck had already moved them out) is now fixed — `lesson-1-project-setup-pattern-first-method.md` was updated to match this deck, and that content now opens `lesson-2-interaction-pattern-build-editing-craft.md` instead. The two smaller mismatches noted below (file path/name, and the CARE "Action" vs "Ask" wording) are now resolved — see the note below dated 2026-09-19.
> **Speaker notes below are written as a teaching narrative, not scannable reference bullets** — connected sentences a facilitator can read or paraphrase aloud in order, explaining the *why* behind each beat, not just naming it. This is a deliberate departure from the standard "3–6 bullets" speaker-note convention for this file specifically, at Winnie's request, to make live 1:1 delivery smoother. The bolded sentence inside each note is the one beat not to skip if the rest gets compressed.
> **Both mismatches from the original sync are now resolved (checked 2026-09-19):** (1) the "Prompt to use" section below points at the deck's actual current location, `library/lessons/03-develop/ai-prototype-development/standalone program/AI Prototyping - Lesson 1.html` — confirmed against the file on disk. (2) On slide 1.8 (CARE), the built deck's on-slide title is simply "CARE." — there is no spelled-out "Context → Action → Rules → Examples" line in it, and the speaker notes already say "Ask," matching this outline and the CARE framework everywhere else in the project. Nothing further to fix here.
> **Structural change from the previous version of this outline:** the old Why → What → How → Do shape (pattern-first "4 steps," a standalone AI-tool comparison table, and a "Build It" phase of Pre-Flight / sync tokens / generate component inventory) is gone from this deck. The live deck runs Cover → **Section 1: AI Foundation** → **Section 2: Project Setup** → **Section 3: The Problem** → **Section 4: The Solution: Your Design Pattern**. The Closing slide's own notes confirm "Build It" has been split into a separate Lesson 2 draft.

---

## Prompt to use

```
Using the outline in this file, update the HTML slide deck for Systematic AI Prototyping — Lesson 1 (Stop Starting From Zero).

Follow the rules in _system/rules/SLIDE_DECK_RULES.md exactly.
File: library/lessons/03-develop/ai-prototype-development/standalone program/AI Prototyping - Lesson 1.html

VISUAL DESIGN DIRECTION — apply globally to every slide:

- Prefer diagrams, flows, and visual metaphors over bullet lists. If content can be shown
  as a shape, flow, or diagram — do that instead of listing text.
- Use inline SVG for all diagrams. Keep them flat, clean, and minimal —
  use only token colours plus the deck's purple/violet accent and yellow/sage support colours.
- Section-divider slides are full-bleed dark (--ink background, --paper text), with a giant
  low-opacity ghost numeral and a yellow mono "Section N" eyebrow tag.
- Milestone/activity slides should feel like a full-bleed pause moment — purple background,
  a large timer numeral, minimal supporting content.
- Real, shipped examples (Winnie's own prototypes, MUI's site) are used as actual screenshots,
  not illustrative mockups, wherever the slide is making a "this is real" point.
- Avoid centred bullet lists. Use numbered-circle or comparison layouts with visual structure.
```

---

## Session metadata

| Field | Value |
|---|---|
| Project name | Systematic AI Prototyping — Lesson 1 |
| File name (as built) | AI Prototyping - Lesson 1.html |
| Cover title (on-slide) | Stop Starting From Zero |
| Subtitle | Set up your project folder, and build the first thing AI actually reads from. |
| Instructor | Winnie Nguyen — UX Product Design Instructor |
| Program | Private Training |
| Year | 2026 |
| Previous session | Lesson 0: Program Introduction |
| Next session | Lesson 2: Interaction Pattern, Build & Editing Craft (opens with Build It — cleanup, token sync, component inventory — then adds the interaction pattern, the build, and edit-mode practice; see `lesson-2-slide-outline.md`) |
| Cover visual | Right panel: solid purple background, large soft decorative circle top-right, full-bleed photo of organised file folders (representing project setup), instructor avatar + name + title bottom-left of the text panel. |

---

## Slide structure — 36 slides

> **Cover, then four numbered sections, each opening on its own full-bleed divider slide: Section 1 "AI Foundation" (1.1–1.9, 9 slides), Section 2 "Project Setup" (2.1–2.3, 3 slides), Section 3 "The Problem" (3.1–3.4, 4 slides), Section 4 "The Solution: Your Design Pattern" (4.1–4.14, 14 slides, including its own internal sub-divider "Putting the Ingredients to Work" before 4.11–4.12).**
> Section 1 covers the maker-to-strategist reframe, all three mindsets, markdown/folder vocabulary, a real-HTML-files proof slide, CARE, and the "feed forward" habit. Section 2 is folder setup end to end, closing on a 10-minute hands-on build. Section 3 names four problems (drift, AI's no memory, forgotten states, and the token cost of re-prompting from zero). Section 4 walks the three Design Pattern ingredients, then a sub-divider into two recap "Step 1 of 2 / Step 2 of 2" slides, a screen-scoping slide with three named traps, and the closing.
> The old "Choosing an AI tool" comparison-table slide and the four "pattern-first, step N of 4" slides are no longer in the built deck.

---

## 0. Cover

---

### COVER
- Kicker: LESSON 1 (mono, with a horizontal rule)
- On-slide category line: Systematic AI Prototyping
- Title: Stop Starting\nFrom Zero (second line, "From Zero," in purple)
- Subtitle: Set up your project folder, and build the first thing AI actually reads from.
- Author: Winnie Nguyen — UX Product Design Instructor (with avatar)
- Speaker notes: Open by naming what this lesson actually produces, not a finished prototype, but the first artifact AI will read from later: the component inventory, and the folder structure it lives in. **Everything today builds toward that folder being ready, so set that expectation up front, or the folder work in Section 2 reads as busywork instead of the point.**
- 🎨 Visual: See cover visual in metadata table above.

---

## 1. AI Foundation

---

### SECTION DIVIDER · Section 1: AI Foundation
- Kicker: Section 1
- Title: AI Foundation
- On-slide: The vocabulary this lesson needs.
- Speaker notes: Pure transition beat. Say the section name, let it sit for a second, then move into the vocabulary. **Nothing to teach here yet, just the signal that you're shifting from "why this matters" into "the words you'll need."**
- 🎨 Visual: Full-bleed dark background, giant low-opacity ghost numeral "1" top-left, "Section 1" tag in yellow mono.

---

### STATEMENT · From Maker to Strategist
- Kicker: AI FOUNDATION
- Title: From Maker to Strategist
- On-slide/Lead: AI is a set of gloves, not a new hand. The work shifts from making everything by hand to directing and editing what AI produces — the designer stays the strategist, not the maker.
- Speaker notes: Open Section 1 with this reframe before any of the three mindsets, because it's the frame everything else sits inside. AI doesn't replace the designer's hands, it takes over the tedious parts of using them, think of it like a set of gloves rather than a new pair of hands: you're still deciding what gets made, you're just not drawing every pixel yourself anymore. **If time is short and the rest of this section gets trimmed, this one line is worth keeping on its own, because without it the three mindsets that follow can read as "AI is taking over" instead of "your role just moved up a level."**
- 🎨 Visual: Two role cards connected by an arrow — left "Maker" (pencil icon, neutral grey), right "Strategist / Editor" (target icon, purple).

---

### STATEMENT · AI Takes the Tedious Work
- Kicker: Mindset 1 of 3
- Title: AI Takes the Tedious Work
- On-slide/Lead: Authorship, taste, and ethics stay with the designer. AI handles what's repetitive, not what matters.
- Speaker notes: This one's quick, and it's not new information, more a permission slip than a lesson. **Say it plainly: the tedious, repetitive parts of the work go to AI, the judgment calls stay with you.** Before running this and the next two mindsets in full, gauge the student's comfort level, if they're already fluent with AI tools generally, this can be a fast nod rather than a full stop, and you can move straight into vocabulary.
- 🎨 Visual: Two cards side by side — "Repetitive work → AI" (gear icon), "Judgment → you" (checkmark icon, purple).

---

### STATEMENT · Treat AI Like an Intern
- Kicker: Mindset 2 of 3
- Title: Treat AI Like an Intern
- On-slide/Lead: Fast, tireless, occasionally brilliant, and it still needs supervision. Every output gets reviewed, not trusted blind.
- Speaker notes: Land this one matter-of-factly. AI is a talented intern, not an oracle, fast, tireless, occasionally brilliant, but it still needs someone checking its work before it ships. **This is the mindset that makes the review habit feel natural rather than like extra friction, and that habit runs through everything built for the rest of this lesson, so it's worth making concrete here rather than assuming it lands on its own.** (Delivery note: "oracle" translates as *tiên tri* if a gloss is needed.)
- 🎨 Visual: Single centred card — desk icon with a checkmark badge, labelled "Talented intern — reviewed before it ships."

---

### STATEMENT · We've Been Here Before
- Kicker: Mindset 3 of 3
- Title: We've Been Here Before
- On-slide/Lead: Hype peak, then a dip, then durable use. Rough AI output today isn't a verdict on the method. It's the normal dip before the tool gets genuinely useful.
- Speaker notes: Open with a toy story. A new toy comes out, everyone loses their mind over it, plays with it nonstop, then it sits in a drawer for a while, that's not the toy failing, that's just what happens with new things. That's exactly what happened with VR headsets: everyone said this changes everything, people tried it, it felt clunky, gave them a headache, so it got put away for a bit. But it didn't disappear, people kept quietly improving it, and now it's genuinely useful, training pilots, training doctors, real work. **AI prototyping tools are on that same story right now, the first few tries might look messy, that's not proof the tool doesn't work, that's just the middle of the story before it gets good.** If the student is very new to this, make it even simpler: remind them of their first bike ride, they wobbled, they fell, that didn't mean bikes were bad, it meant they were still learning, AI is wobbling right now too, it's going to get steadier. If there's time and they've used AI tools enough to have a story of their own, ask for one time it helped and one time it quietly got in the way.
- 🎨 Visual: Hype-cycle curve (SVG) labelled Hype Peak / You Are Here / Durable Use, beside a full-bleed photo of a person wearing a VR headset (credit: Minh Pham / Unsplash).

---

### STATEMENT · Markdown
- Kicker: Vocabulary, not theory
- Title: Markdown
- On-slide/Lead: What AI tools read and write by default. It's why the component inventory built later this lesson is a `.md` file, not a Word doc.
- Speaker notes: Keep this light, it's a vocabulary plant, not a lesson on markdown syntax. **The one thing worth landing: this word comes up constantly for the rest of the lesson, so naming it once now means you're not stopping to explain it later while the student is mid-build and trying to focus on something else.** Point at the real example on screen, your own Urban Farming user flow, and note it's a plain text file, exactly why AI tools can read and write it so easily.
- 🎨 Visual: Real screenshot — a markdown example from Winnie's own Urban Farming user flow, captioned "Winnie Nguyen — Urban Farming."

---

### STATEMENT · One Project, One Folder
- Kicker: Vocabulary, not theory
- Title: One Project, One Folder
- On-slide/Lead: Organised from day one, not the day the AI coding tool opens.
- Speaker notes: Same spirit as the markdown slide, plant the word, don't build the whole idea yet. Just say: everything lives in one folder, organised from day one, not the day you open your AI coding tool for the first time. **The full folder structure gets its own slide coming up in the Project Setup section, so there's no need to preview it here beyond the name.**
- 🎨 Visual: Simple folder-shape icon (SVG, purple tint fill, purple stroke).

---

### COMPARE · A Real HTML File
- Kicker: Before you open the tool
- Title: A Real HTML File
- On-slide/Lead: An AI-generated prototype is real code, a structure a browser renders, not an export. You decide the direction; AI assembles it faster than you could by hand.
- Speaker notes: **This needs to land before the folder work, not after, because if the student's first build surprises them later with "wait, this is just a webpage, not a Figma link," that surprise costs more mid-build than it does right now.** Point at the comparison on screen: a .fig export isn't what gets built here, a real HTML file running in an actual browser window is. Worth naming in passing too, the files written today, the component inventory, the rules file, are all markdown, which loops right back to the vocabulary just covered, it's exactly what AI tools read and write best.
- 🎨 Visual: Side-by-side compare, separated by a ≠ symbol — left "Not this" (dashed box, .fig export icon, faded), right "THIS — HTML IN BROWSER WINDOW" (mock browser chrome with traffic-light dots over placeholder content blocks).

---

### IMAGE · Real HTML in the Browser
- Kicker: Real examples
- Title: None. (kicker + two captioned screenshots only)
- Speaker notes: This is proof, not explanation, so let the screenshots do the talking. **Both examples on screen are real browser windows from actual projects, not mockups built to look like browsers.** If you can, open the file:// URL bar live and point at it directly, seeing the address bar say "this is a file on my computer, not a Figma link" lands harder than being told it.
- 🎨 Visual: Two real screenshots side by side — "Urban Farming prototype in a browser" (captioned "Winnie Nguyen — Urban Farming") and "Personal website prototype in a browser" (captioned "Winnie Nguyen — Personal Website").

---

### FORMULA · CARE
- Kicker: One shape, every prompt
- Title: CARE
  - *(Flag: the built HTML's on-slide breakdown still reads "Context → Action → Rules → Examples" in one place — see the mismatch note at the top of this file, framework everywhere else uses "Ask.")*
- On-slide rows:
  - C — Context — Who's asking, what project, what stage
  - A — Ask — One clear task, not five vague ones
  - R — Rules — Constraints, tone, format
  - E — Examples — Show, don't tell, this locks it down
- On-slide, right panel: a real CARE-structured prompt example — "I'm redesigning the checkout flow for a mobile banking app. Generate a component inventory for the payment confirmation screen, every component, name, and state. Use only components already in my design system; flag anything missing rather than inventing new ones. For example: 'Button — primary action — default, hover, loading, error.'"
- Speaker notes: This is the shape behind every prompt used for the rest of this lesson, so build it up piece by piece rather than reading it as a finished list. Context sets who's asking and what stage they're at. Ask is one clear task, not five vague ones bundled together. Rules are the constraints, tone, format. **And Examples is the piece that actually locks the output down, showing beats telling every time.** Walk through the real example prompt on the right side of the slide and point out each CARE piece inside it, so the framework isn't abstract the moment it's introduced.
- 🎨 Visual: Left column, four stacked CARE rows with escalating colour weight (ink → yellow → purple tint → solid purple). Right column, dark card with the real example prompt in mono type.

---

### COMPARE · Feed It Forward
- Kicker: The habit that makes everything else work
- Title: Feed It Forward
- On-slide/Lead: A new chat starts at zero, your folder doesn't. Save what AI needs once, point the tool at it, and every prompt after that gets to be short.
- Speaker notes: This is the idea the whole lesson has been building toward without saying it outright. **Today's component inventory becomes tomorrow's input, not tomorrow's retyped paragraph.** A new chat always starts at zero, that's just how these tools work, but your folder doesn't have to. Point at the two columns on screen, retyping the same paragraph over and over on the left, one file feeding three prompts on the right, that contrast is the whole habit in one picture.
- 🎨 Visual: Two-column compare — left "Starting fresh" (three repeated grey blocks, captioned "— same paragraph, retyped each time —"), right "Feed forward" (file icon, arrow, three small chat-bubble targets).

---

## 2. Project Setup

---

### SECTION DIVIDER · Section 2: Project Setup
- Kicker: Section 2
- Title: Project Setup
- On-slide: Organise the project, then build it for real.
- Speaker notes: Another pure transition. Say the section name, then move straight into the folder work. **The framing line worth saying out loud: organise the project first, then build it for real, in that order.**
- 🎨 Visual: Same divider treatment, ghost numeral "2."

---

### DIAGRAM · One Folder, Four Lessons
- Kicker: Before anything else
- Title: One Folder, Four Lessons
- On-slide, folder tree (mono):
  - project-name/
  - ├─ README.md
  - ├─ AGENTS.md ← get this exactly right *(highlighted purple/bold)*
  - ├─ learning/
  -   ├─ prd.md
  -   ├─ flowchart.md
  -   ├─ preferences.md
  -   ├─ component-inventory.md
  -   └─ interaction-pattern.md — next lesson *(muted)*
  - ├─ design-system/
  - ├─ screens/
  - └─ assets/
- Speaker notes: Open with the end in mind, this is the folder for the whole engagement, all four lessons, not just a one-off setup task for today. Walk down the tree on screen and let most of it move quickly, README, design-system, screens, assets are all fairly self-explanatory. **Slow down on AGENTS.md specifically, that's the one thing worth getting exactly right today, everything else in this tree can be tidied up later at no real cost, but a sloppy router file compounds every prompt that reads from it afterward.** One distinction worth a sentence, AGENTS.md stays short on purpose, it's a router, not a file cabinet, the detail underneath it lives in `learning/` and only gets pulled in when a prompt actually needs it.
- 🎨 Visual: Literal monospace folder-tree text block (not an SVG diagram), AGENTS.md line called out in purple with an inline "← get this exactly right" note.

---

### COMPARE · This Is AGENTS.md
- Kicker: That same habit, applied to your folder
- Title: This Is AGENTS.md
- On-slide/Lead: This file is where that feed-forward habit lives. Keep it short, point it at the learning/ folder, prd, flowchart, preferences, component inventory, interaction pattern, and every future prompt gets to be short too. Naming note: AGENTS.md is the closest thing to a cross-tool standard, if a student's tool insists on its own name, CLAUDE.md, .cursorrules, that file becomes one line, "rules live in AGENTS.md, read that first," not a second copy.
- Speaker notes: This slide is the direct payoff of the "feed forward" habit from Section 1, now made concrete and specific to the student's own folder. Call it what it is, artifacts over prompts. **If nothing else survives from today's session, this file, wired up correctly, is the one thing that has to.** Point at the comparison, retyping the same explanation into every prompt on the left, versus one router file that reads the right learning/ document automatically on the right, that's the entire argument in one image. The word "automatically" is doing the work here, not "everything at once", AGENTS.md stays small precisely so it can afford to load on every prompt. On naming, call out that AGENTS.md is the file most tools recognize today, Claude Code, Cursor, Copilot CLI, Codex CLI, Gemini CLI, so it's the safer default when you don't know which tool a student will land on.
- 🎨 Visual: Two-column compare — left "Retyped every prompt" (three grey bars), right "Read automatically" (file icon, arrow, three small circles).

---

### MILESTONE · Set Up Your Folder
- Kicker: Hands-on — 10 minutes
- On-slide: 10:00 (large timer numeral)
- Title: Set Up Your Folder
- On-slide/Lead: README, AGENTS.md, learning/ (prd, flowchart, preferences), design-system/, screens/, assets/. Export the design system into it. First pass at AGENTS.md counts, even a few lines.
- Speaker notes: Hand this off as real build time, not a demo you're narrating, watch the student build it rather than building it for them. Most of this folder work takes minutes and doesn't need close supervision. **The one piece worth stopping to personally check is AGENTS.md, since that's the single must-get-right item from this whole session.** Keep an eye on scope too, prd.md, flowchart.md, and preferences.md only need a first pass today, a few lines each is fine, the router file is the one thing that has to be right, not exhaustive. If they finish early, don't let them sit idle, let them get a head start skimming the Problem section that's coming up next.
- 🎨 Visual: Full-bleed purple background, large "10:00" numeral, soft decorative circle top-right.

---

## 3. The Problem

---

### SECTION DIVIDER · Section 3: The Problem
- Kicker: Section 3
- Title: The Problem
- On-slide: Why screen-by-screen breaks.
- Speaker notes: Transition beat. Say the section name, and note out loud that folder setup and the hands-on build are done. **Now it's time to name the problem before showing the fix in Section 4.**
- 🎨 Visual: Same divider treatment, ghost numeral "3."

---

### DIAGRAM · Everything Drifts
- Kicker: The most common mistake — problem 1 of 4
- Title: Everything Drifts
- On-slide/Lead: Home, then detail, then settings. By screen three the button has drifted and the spacing has moved. Hand that to AI and every prompt starts from zero, because nothing connects the screens.
- Speaker notes: Run this as a live demo, not a slide read-through, pull up a real 3-screen flow, ideally the student's own, and show the drift happening in real time as you move through it. **Once they've seen it, ask directly: if AI could read your whole design file right now, what would it need to know that isn't visible in the file itself?** That question is what the rest of Section 4 answers, so let it sit for a moment rather than rushing past it.
- 🎨 Visual: Three phone-frame outlines drifting apart — Screen 1 (baseline), Screen 2 ("Different radius" callout), Screen 3 ("Spacing changed" and "Not in system" callouts).

---

### STATEMENT · AI Forgets Everything
- Kicker: Problem 2 of 4
- Title: AI Forgets Everything
- On-slide/Lead: Each request starts from zero, nothing carries over from the last one. Like asking someone to redraw the same cat, over and over, except they never remember what you told them last time. No document to read from means every prompt is a new starting point, and the result drifts a little each time.
- Speaker notes: This is the quieter problem sitting underneath the one the student just saw. They feel problem 1, the drift, because it's visible on screen, but this slide is why it happens. **Land it as a direct callback: that drift you just watched happen? This is the actual mechanism behind it.** Every prompt starts from zero, nothing carries over, it's like asking someone to redraw the same cat over and over except they never remember what you told them last time, so the result drifts a little more with every attempt.
- 🎨 Visual: Three dashed prompt cards (Prompt #1 / #2 / #3), each a differently-worded description of the same button, captioned "— nothing connects them —."

---

### STATEMENT · Forgotten States
- Kicker: Problem 3 of 4
- Title: Forgotten States
- On-slide/Lead: A login screen gets designed for success, wrong password, loading, no connection all get skipped. Usually a developer or the user finds the gap, after the product ships.
- Speaker notes: This is the problem the component inventory, coming up in the next section, directly solves, states get captured up front instead of discovered after the fact. A login screen usually gets designed carefully for success, and then wrong password, loading, no connection all quietly get skipped, it's almost always a developer or a real user who finds that gap, and by then the product has already shipped. **Good moment to check in directly: has this happened to you? The answer is almost always yes, and that recognition is what makes the fix in Section 4 land.**
- 🎨 Visual: Four login-screen cards — Success (fully designed, purple border), Wrong password / Loading / No connection (each greyed out with a "?", fading opacity left to right).

---

### STATEMENT · Every Redo Costs Tokens
- Kicker: Problem 4 of 4
- Title: Every Redo Costs Tokens
- On-slide/Lead: Each re-prompt reprocesses everything that came before it. Redoing a drifted screen from scratch doesn't just cost time, it costs real money, and it adds up fast.
- Speaker notes: Tie it straight back to the first three problems, drift and forgetting aren't only quality issues, they're the reason the student ends up re-prompting so often in the first place. Every message in a session gets resent along with the next one, so a short first prompt can balloon past 15,000 tokens by message twenty just from accumulated history. **Use a concrete number to land it: developers have reported burning $47 in a single afternoon, or $350 in a day, on "routine" AI-assisted coding, almost entirely from retry and regeneration loops.** Frame the fix as a preview rather than solving it here, a stable reference, which is exactly what Section 4 builds, means the AI stops re-deriving the same context every time, and that's what actually controls the bill.
- 🎨 Visual: Escalating token/cost meter beside three or four stacked prompt cards, each labelled with a rising token count or dollar figure, echoing the dashed prompt-card visual on "AI Forgets Everything."

---

## 4. The Solution: Your Design Pattern

---

### SECTION DIVIDER · Section 4: The Solution
- Kicker: Section 4
- Title: The Solution: *Your Design Pattern*
- On-slide: Tokens, component inventory, template, and how they resolve the four problems.
- Speaker notes: Transition beat. Say the section name and preview what's coming: **tokens, component inventory, template, and how they resolve all four problems just named.**
- 🎨 Visual: Same divider treatment, ghost numeral "4."

---

### COMPARE · One Pattern, Four Fixes
- Kicker: Why a Design Pattern
- Title: One Pattern, Four Fixes
- On-slide/Lead: Everything Drifts → Template gives every screen the same layout to build from. AI Forgets Everything → the pattern is a written document, not memory, so AI reads the same context fresh every time. Forgotten States → Component Inventory names every state up front, so nothing gets skipped. Every Redo Costs Tokens → less re-deriving context means fewer retries, which is what actually controls the bill.
- Speaker notes: Treat this as the payoff slide, every problem named in Section 3 gets its fix said out loud here instead of left implied. Point out that "AI forgets" and "token cost" share one root cause, no persistent context, so the same fix, a written pattern, solves both at once rather than needing two separate answers. Walk the four rows left to right, problem then fix, so the connection lands visually as well as verbally. **The beat not to skip: this is the one slide that proves the whole lesson's thesis, a Design Pattern isn't extra work, it's what removes the rework.**
- 🎨 Visual: Four rows, problem icon and label on the left, arrow, ingredient/fix label on the right, echoing the two-column compare treatment on "Every Screen Reinvents Its Layout."

---

### STATEMENT · Three Ingredients, Already Yours
- Kicker: Your Design Pattern — three ingredients
- Title: Three Ingredients, Already Yours
- On-slide/Lead: Tokens, component inventory, template, all three should already exist in your Figma file. Today's work reads them, it doesn't invent them.
- Speaker notes: First, clear up a naming trap before it causes confusion later, Design Pattern and prototype pattern are two different things that sound almost identical. Design Pattern lives in Figma, it's tokens, component inventory, and template, all three of which should already exist in the student's file. Prototype pattern is what gets built from it, in markdown, for AI to read, that's this lesson's actual output. **If the student looks confused later, come back to this line: Design Pattern lives in Figma, prototype pattern lives in your project folder.** The mapping slide right before this one is the direct answer to the four problems just named in Section 3, worth a quick callback here.
- 🎨 Visual: Three ingredient cards in a row — colour dots (Tokens), a component chip (Component inventory), a skeleton-layout mini-icon (Template).

---

### STATEMENT · Tokens
- Kicker: Ingredient 1 of 3
- Title: Tokens
- On-slide/Lead: The exact values your design system uses. This is what gets synced into the build later this lesson, so AI uses your product's actual look, not a generic default.
- Speaker notes: Keep this one short and moving, it's a name-check, not a tokens lesson, this arc assumes that fluency already exists. **The one thing worth landing: these are the exact values, colour, type, spacing, that get synced into the build later, so AI ends up using the student's actual product look instead of a generic default.**
- 🎨 Visual: Three columns — colour swatches (four blocks), a type scale (three sizes of "Aa"), a spacing scale (five growing squares).

---

### STATEMENT · Component Inventory
- Kicker: Ingredient 2 of 3
- Title: Component Inventory
- On-slide/Lead: The full catalogue, already named as the fix to screen-by-screen drift. Today's artifact; built later this lesson.
- Speaker notes: This term is coming back around for the second time, it was named earlier as the direct fix to screen-by-screen drift, and now it's showing up again as one of the three Design Pattern ingredients. **Both framings are true at once, it's part of what the student already has, informally, in their head and their Figma file, and it's also the artifact they're about to formalise into an actual document today.**
- 🎨 Visual: Three component cards — Button (filled/hover/loading variants + state tags), Card (thumbnail + text lines + state tags), Input field (default/focused/error states + tags).

---

### STATEMENT · Template
- Kicker: Ingredient 3 of 3 — what is it
- Title: Template
- On-slide/Lead: The frame your screens sit inside, structure without real content yet. Same layout, three purposes: adding, editing, reading.
- Speaker notes: Keep this concrete rather than abstract. **A template is a layout, not a finished screen, structure without real content in it yet.** The Add / Edit / Read example on screen makes that distinction tangible immediately, same skeleton, three different purposes depending on what the screen needs to do.
- 🎨 Visual: Three skeleton-screen mockups — Add (empty fields), Edit (pre-filled fields), Read (content block, no inputs).

---

### COMPARE · Every Screen Reinvents Its Layout
- Kicker: WHY WE NEED DESIGN TEMPLATE
- Title: Every Screen Reinvents Its Layout
- On-slide/Lead: This is the same drift from problem 1, but at the layout level, not just the component level. A shared template is what keeps spacing, hierarchy, and structure identical across every screen AI builds.
- Speaker notes: This is the direct link back to problem 1, the drift the student saw at the start of Section 3. **Without a shared template, every single screen re-derives its own layout logic from scratch, and small inconsistencies creep in exactly the way they did in that opening demo.** Point at the comparison, three mismatched bars where every screen guesses its own layout, versus three identical bars where the structure is locked in before any screen gets built.
- 🎨 Visual: Two-column compare — left "No shared template" (three mismatched-width grey bars, "— every screen, a fresh layout guess —"), right "One shared template" (three identical purple-tint bars, "— identical structure, every time —").

---

### NUMBERED · Design It in Figma
- Kicker: Ingredient 3 of 3 — how we build it
- Title: Design It in Figma
- On-slide/Lead: Every other ingredient can be synced or generated by AI later this lesson. The template is the one exception, it has to already exist in Figma before you start prompting.
- On-slide steps:
  - 1. Pick the screen purpose: does it add, edit, or read data?
  - 2. Lay out structure only, real components, placeholder content.
  - 3. Save it in your Figma file, this is what step 2 of "Putting the ingredients to work" points to.
- Speaker notes: Keep this practical and grounded, the template comes from Figma, not from AI, and it has to exist before any prompting starts. Walk the three numbered steps in order: pick the screen's purpose (add, edit, or read), lay out structure only with real components and placeholder content, then save it in the Figma file. **This is the one ingredient nothing later in this lesson regenerates for the student, worth being clear that this step doesn't get automated away.**
- 🎨 Visual: Three numbered circles (purple fill), each paired with its instruction line, stacked vertically.

---

### STATEMENT · Common template pattern types
- Kicker: A lookup catalogue, not a checklist
- Title: Common template pattern types.
- On-slide, 7-card grid: Read (view content, change nothing) · Edit (modify content that already exists) · Add (create something entirely new) · Confirm (review and approve an action) · Navigate (move between sections) · Search / Filter (find or narrow a list) · Onboard (guide a first-time user), plus a closing note card: "Most prototypes need only 3-4. One screen can carry more than one pattern."
- Speaker notes: Frame this as a lookup catalogue, not something to memorise, the actual goal is recognising which pattern a screen belongs to on sight, not reciting the list. Most prototypes only need three or four of these seven. **Worth naming explicitly: a single screen can carry more than one pattern at once, a checkout screen is both Edit and Confirm at the same time, that's exactly why it's called a pattern and not a screen type.**
- 🎨 Visual: 3-column grid of 7 labelled cards, plus one wide dashed note card spanning 2 columns at the end.

---

### IMAGE · Template, Seen in MUI
- Kicker: A real example
- Title: Template, Seen in MUI
- On-slide: two real screenshots (MUI React templates overview page; MUI Checkout and Sign-in templates), sourced to mui.com/material-ui/getting-started/templates
- Speaker notes: This grounds everything just covered in a real, shipped design system, not a teaching concept invented for this lesson. **MUI names its templates the exact same way, Checkout, Sign-in, each one a full screen sequence built around one familiar job.** Seeing a production design system use this same language tends to land more convincingly than another slide of theory would.
- 🎨 Visual: Two real product screenshots side by side, source link credited underneath.

---

### SECTION DIVIDER · Sub-section: Putting the Ingredients to Work
- Kicker: Your Design Pattern, in practice
- Title: Putting the ingredients *to work.*
- Speaker notes: Short divider closing out the ingredients and opening the two-step recap that follows. **From naming what the pieces are to actually putting them into practice** — let this one breathe for just a beat before moving on.
- 🎨 Visual: Dark full-bleed sub-divider, same family as the main section breaks but without a large ghost numeral.

---

### PROCESS · Set Up Your Design System
- Kicker: Step 1 of 2
- Title: Set Up Your Design System
- On-slide/Lead: Sync your tokens, then catalogue every component and its states. This is what you'll build hands-on next, in Build It.
- On-slide: two real screenshots, captioned "Tokens" and "Component inventory"
- Speaker notes: This recaps ingredients 1 and 2, tokens and component inventory, as the first concrete step, and it's literally what gets built hands-on next, in Build It. **Point at the two real screenshots on screen, this is what these documents actually look like once they exist, not an abstract description of them.**
- 🎨 Visual: Two real documentation screenshots side by side, each with a caption underneath.

---

### PROCESS · Design Your Main Screens
- Kicker: Step 2 of 2
- Title: Design Your Main Screens
- On-slide: one real screenshot, "Main concept screens forming the template"
- Speaker notes: This recaps ingredient 3, the template, as the second and final setup step, designing the actual main screens in Figma that everything else gets arranged into later. **The screenshot on screen is a real example of what that looks like finished, worth pointing at directly rather than describing it.**
- 🎨 Visual: One full-width real screenshot of the main concept screens.

---

### STATEMENT · Which Screens Are Right
- Kicker: Before you build anything
- Title: Which Screens Are Right
- On-slide/Lead: One user goal. 2–3 screens that show it. Cut anything that doesn't move the user closer to that goal.
- On-slide traps (✕):
  - Multiple user goals — screens from different goals won't connect naturally
  - Too many screens — scope creep kills the prototype
  - Starting with the hardest screen — start with the core flow instead
- Speaker notes: This is new territory this lesson hasn't covered yet, how to pick which screens to actually build, as opposed to how to build them consistently once chosen. Keep the rule simple: one user goal, two to three screens that show it, cut anything that doesn't move the user closer to that goal. **Close on the three traps as the memorable takeaway: multiple user goals that won't connect naturally, too many screens inviting scope creep, and starting with the hardest screen instead of the core flow, those three are worth landing clearly since they're the mistakes a student is most likely to actually make.**
- 🎨 Visual: Three-row list, each row an ✕ icon, trap name, and one-line consequence, hairline dividers between rows.

---

### END · Closing (Lesson 1)
- Kicker: Before next time
- Title (quote): "The system isn't the output anymore. It's *the input to everything you build.*"
- On-slide checklist:
  - ✓ Your Design Pattern: tokens, component inventory, template
  - ✓ Your project folder and AGENTS.md are set up
  - ✓ Next: Build It (cleanup, token sync, component inventory), then the interaction pattern and your first working screens
- Sign: — Winnie Nguyen
- Speaker notes: Let the pull quote breathe before moving into the checklist, the system isn't the output anymore, it's the input to everything built from here forward. Walk the three checklist items as a recap of exactly what happened today: the Design Pattern, the folder and AGENTS.md, and what's coming next. **Worth naming explicitly: Build It, the cleanup, token sync, and component-inventory generation, is now its own separate Lesson 2 draft, not something being squeezed into today, so the student knows that's coming rather than wondering if it got skipped.**
- 🎨 Visual: Italic pull-quote title on a slightly deeper paper background, checkbox-style checklist below, signature line at the bottom.

---

*Outline reverse-synced from the built deck by Claude · Private Training · Last updated September 2026*
