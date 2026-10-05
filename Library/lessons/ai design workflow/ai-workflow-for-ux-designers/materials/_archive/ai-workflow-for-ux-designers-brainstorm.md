---
title: "AI Workflow for UX Product Designers — Lesson Brainstorm"
type: brainstorm
program: ux-class
status: draft
date: 2026-07-20
---

# AI Workflow for UX Product Designers — Lesson Brainstorm

Working document to shape a new lesson: how UX Product Designers set up and use an AI-augmented workflow. Structured around your questions, with curated resources at the end. This is prep material — not yet a `*-lesson.md` / `*-slide-outline.md` pair.

**Where this could sit in the curriculum:** Your existing sequence runs Design Thinking → Customer Understanding → Synthesis/Problem Definition → Design Framework (Atomic Design) → AI Prototype Development. This lesson reads as a *foundational* session — either taught first (before Design Thinking, as "how we'll work all semester") or as a standalone module students revisit once they've felt the pain of doing things manually. AI Prototype Development already teaches AI for one specific activity (prototyping); this lesson would be the umbrella — mindset, tools, and how AI touches *every* stage, not just prototyping.

---

## 1. Benefits of Applying an AI Workflow

- **Speed**: research synthesis that took days (coding interview transcripts, tagging themes) compressed to hours. NN/G: AI is most helpful for the *planning and analysis* phases of research, not for replacing the research itself.
- **Volume without burnout**: quantity-first stages (Ideate's "50+ ideas before you pick one") become easier to sustain — AI removes the friction of generating raw material, leaving humans to curate.
- **Consistency**: a defined AI workflow (prompts, tools, review steps) produces more consistent outputs across a team than ad hoc, tool-by-tool improvisation.
- **Lower floor, not just higher ceiling**: junior designers benefit disproportionately. Studies outside design (GitHub Copilot, customer support agents) consistently show *less experienced* practitioners gain the most from AI assistance — the gap between junior and senior narrows on execution tasks, even as it widens on judgment tasks.
- **Business impact**: McKinsey's 2025 State of AI findings cited a 22% higher feature adoption rate for orgs that integrated AI into product design workflows. Figma's 2026 data: 91% of designers who increased AI use said it helped them create better designs, 89% said they worked faster, 80% said it improved collaboration.
- **Frees time for the parts AI can't do**: synthesis, judgment, taste, stakeholder framing — the argument across almost every source below is that AI's real benefit is reclaiming time from mechanical tasks to spend on strategic ones.

**Caveat worth teaching alongside the benefits:** Figma's 2026 report also found a split — 36% of designers said design got *better* with AI, 35% said *worse*, 29% said no change. The benefit isn't automatic; it depends on how deliberately the workflow is set up. That tension is a good open for the lesson.

---

## 2. Impact on UX Product Designers

- **Role is shifting from maker to strategist/editor.** NN/G frames it directly: "think of yourself as a strategist who leverages AI... your hands still direct the work." The designer's value moves toward framing the problem, setting constraints, and judging output — not producing every pixel or every research summary from scratch.
- **The "AI-UX Generalist" is emerging as the most valuable profile** — designers with strong human-centered thinking, data literacy, and strategic vision who use AI to automate the grunt work, rather than narrow specialists who only execute one part of the pipeline. This connects directly to NN/G's "Return of the UX Generalist" thesis.
- **Half of designers surveyed in 2026 have shipped AI-generated code to production** — the boundary between design and front-end implementation is blurring (directly relevant to your `ai-prototype-development` lesson).
- **Taste and judgment become the scarce skill, not output.** As AI lowers the cost of producing *something*, the ability to tell whether that something is *right* — for these users, this brand, this moment — becomes the differentiator. Several sources (Smashing Magazine, NN/G "Design Taste vs. Technical Skills") converge on this.
- **New failure modes to watch for as an instructor:** designers who let AI's fluent output substitute for their own review ("looks done" ≠ "is done"), and designers who never develop foundational skills because AI always provided the first draft. Both are worth naming explicitly in a mindset section.

---

## 3. Mindset About AI

A few framings worth building the lesson's opening around:

- **"Augment, don't replace."** The dominant framing across every source (Fast Company, NN/G, Smashing Magazine, IDEO): AI takes the tedious and repetitive; the designer keeps authorship, judgment, and ethics. This should probably be the lesson's single headline message.
- **AI as intern, not oracle.** NN/G's "Your AI UX Intern: Meet Ari" is a genuinely useful mental model for students: a talented intern who works fast, never gets tired, but still needs supervision, correction, and shouldn't be trusted unsupervised on anything that matters. This reframes "AI got it wrong" from a failure of the tool into an expected part of the workflow — you review an intern's work, you don't just ship it.
- **AI as "cybernetic teammate," not partner.** TIME's article ("Why Thinking of AI as a 'Partner' Can Be Counterproductive") is a nice counterpoint — the language we use (master / partner / assistant / tool) shapes how much authority we hand over. Worth a short discussion prompt.
- **Critical engagement over blind trust.** NN/G's "7 Deadly AI Sins for UX Professionals" gives a concrete, teachable checklist of anti-patterns (e.g., trusting AI-generated data as real user data, skipping verification, letting AI make design decisions unsupervised).
- **This is a hype cycle, and designers should know that.** NN/G draws a direct parallel to the VR hype cycle — early over-promise, a trough of disillusionment, then durable practical use. Framing AI this way helps students calibrate expectations rather than treating every new tool as either magic or a threat.
- **Ethics and bias awareness.** Your own `design-framework-lesson.md` already makes this point for Atomic Design AI use — training data skews Western/English, so AI-suggested hierarchies or patterns may not match Vietnamese/SEA user mental models. This same caveat applies broadly: AI output default styles, defaults, and assumptions need a critical read, not a trusting one.

---

## 4. Why We Should Use AI in the Workflow

Boil this down to a few honest reasons, not hype:

1. **Because the industry has already normalised it.** 91% of designers now use AI (2026), the average designer uses 7 AI tools regularly (up from 3 the prior year), 72% use generative AI specifically. Not adopting a deliberate workflow doesn't mean avoiding AI — it means using it accidentally and inconsistently.
2. **Because it removes friction from the parts of the job designers already dislike** — transcribing interviews, restating the same component five times, writing the first draft of copy, building throwaway wireframes to test an idea.
3. **Because clients/employers increasingly expect designer + AI fluency as a baseline skill**, not a specialization — similar to how Figma fluency became table stakes a decade ago.
4. **Because the risk of *not* engaging critically is higher than the risk of engaging.** Teams that hand over judgment entirely produce worse work; teams that refuse to engage at all fall behind on speed. The deliberate middle path — a defined workflow with review checkpoints — is the actual skill being taught.

---

## 5. AI Tools Landscape (mapped roughly to what they're good for)

Per your lesson convention, **specific tool names should be generalised in the actual lesson content** ("AI chat tool," "AI coding tool," etc.) — but useful for you to know the current landscape while designing the lesson:

| Category | What it's for | Examples in the wild (2026) |
|---|---|---|
| AI chat / reasoning tools | Research synthesis, ideation partner, strategy, writing | ChatGPT, Claude, Gemini, Perplexity |
| Research-specific AI | Interview transcription, thematic analysis, synthesis docs | Condens.io, various AI-assisted research platforms |
| Inspiration / moodboarding | Visual direction, trend scanning | Lummi AI, InspoAI |
| Color / type systems | Token and palette generation | Khroma |
| Sitemap / IA generation | Structuring flows and content hierarchy | Relume |
| AI-native design/prototype tools | Text-to-UI, multi-screen generation | v0 (Vercel), Lovable, Flowstep, UXPin Merge |
| AI coding tools | Turning designs/specs into working code | Cursor, GitHub Copilot, Windsurf |
| In-tool AI features | Layer renaming, component detection, auto-layout suggestions | Figma AI features |
| Audit / QA | Accessibility and design-system compliance checks | Beacon AI, internal linting tools (IBM Carbon, Shopify Polaris examples) |

**Instructor note:** the "one tool per stage" framing above is a simplification — most experienced designers in 2026 use 2–3 general-purpose AI chat tools for almost everything (research, ideation, writing, review) and reach for specialized tools only for prototyping/code. Teaching students to start with a general tool and go deep, rather than tool-collecting, avoids overwhelming them.

---

## 6. Aligning AI Workflow with Design Thinking / Your Design Process Framework

Your curriculum already has two frameworks this lesson should map onto explicitly, using the exact same vocabulary students already know:

**A. The 5-Stage Design Thinking cycle** (from `design-thinking-lesson.md`): Empathise → Define → Ideate → Prototype → Test.

**B. The 5-Step design-framework process** (from `design-framework-lesson.md`): Find screens → Sketch zones → Map to interaction patterns → Define tokens → Build components.

Rather than inventing new vocabulary, this lesson's job is to answer: **"at each stage/step you already know, what does AI do, and what stays yours?"** That structural choice also makes this lesson feel like a natural bridge between Design Thinking (early in the curriculum) and AI Prototype Development (late in the curriculum) — it's the connective tissue.

A useful teaching frame from the research: AI's usefulness is *not evenly distributed* across the five stages. It's strongest at Empathise (synthesis) and Prototype (generation), weaker and riskier at Define and Test (judgment-heavy, evidence-heavy), and situational at Ideate (great for volume, risky for genuine novelty). Naming this unevenness up front prevents the common mistake of trying to force AI into every stage equally.

---

## 7. Applying AI to Each Activity

Drafted against the Design Thinking cycle, since it's the framework students learn earliest. Each entry: what AI does well, what to watch for, and a rough prompt shape (generalise tool names in the final lesson).

### Empathise
- **AI does well:** turning raw interview transcripts into thematic clusters, sentiment groupings, and pull-quote libraries; drafting interview guides and screener questions; summarizing competitive research.
- **Watch for:** synthetic users / digital twins are *not* a substitute for real user data — NN/G is explicit that AI-simulated behaviour can supplement, not replace, real research. AI does not control your customer's purse strings; they do.
- **Prompt shape:** "Here are my raw interview transcripts: [paste]. My research goal is [X], my working personas are [Y]. Identify recurring themes, contradictions between participants, and 3 quotes that best represent each theme."

### Define
- **AI does well:** drafting problem statement variations from a set of insights; generating JTBD statement options; stress-testing a "How Might We" for scope (too broad/too narrow).
- **Watch for:** this is a judgment-heavy stage — AI can generate candidate problem statements, but choosing *which one is true to the evidence* is not delegable. This is where "7 Deadly AI Sins" (trusting AI's framing over your own evidence) bites hardest.
- **Prompt shape:** "Based on these research insights: [paste], draft 3 alternative problem statements at different levels of scope. For each, tell me what evidence supports it and what evidence is missing."

### Ideate
- **AI does well:** raw volume generation — NN/G's research found teams using AI to augment ideation outperformed both individuals and teams without AI. Great for breaking a creative block or generating a first pass of 20+ directions to react against.
- **Watch for:** AI converges toward generic/statistically common ideas; genuinely novel concepts still come from human insight and constraint-setting. Use AI to widen the field, not to pick the winner.
- **Prompt shape:** "The problem is [X], the user is [Y]. Generate 15 different solution directions ranging from obvious to unconventional. Group them by underlying strategy, not just surface idea."

### Prototype
- **AI does well:** this is AI's strongest stage today — text-to-UI generation, promptframes (AI-enhanced wireframes with realistic-feeling content instead of lorem ipsum), generating realistic mock data/tables/charts for testing. Directly overlaps with your `ai-prototype-development` lesson content (prototype pattern, component inventory, interaction pattern).
- **Watch for:** NN/G's core finding — AI "follows general directions but lacks the sophistication to weigh design tradeoffs." Spacing, grouping, and hierarchy are the first things to break. Output is a starting point, not a result.
- **Prompt shape:** already fully built out in your `ai-prototype-development-lesson.md` — this section could literally cross-reference that lesson rather than duplicate it.

### Test
- **AI does well:** drafting test scripts and task scenarios, generating realistic mock data so prototypes don't fall apart at "real content" (see NN/G's "Leverage AI for Mock Tables and Charts"); helping synthesize findings across multiple test sessions faster.
- **Watch for:** the highest-risk stage for over-trusting AI. Synthetic/AI-simulated user behaviour cannot replace real usability testing with real users — it can fill gaps or predict population-level trends, but not substitute for direct observation of confusion, hesitation, and delight.
- **Prompt shape:** "Here are notes from 5 usability test sessions: [paste]. Identify patterns across sessions — which issues appeared with multiple users vs. only one. Flag anything that contradicts our original problem statement."

---

## 8. Additional Perspectives Worth Considering

A few angles you didn't list but that would strengthen the lesson:

- **AI as a workshop/team teammate, not just a solo tool.** NN/G frames AI as a "cybernetic teammate" in group settings — worth a short section on AI in critiques, brainstorms, and stakeholder workshops, not just 1:1 designer work. Their "4 Tips for Preparing AI-Enhanced Workshops" and "Facilitating AI-Enhanced Workshops" articles are directly usable here.
- **A prompting framework, taught explicitly.** NN/G's CARE framework (Context, Ask, Rules, Examples) is a simple, teachable structure students can reuse across every stage — worth introducing early in the lesson rather than leaving prompting to intuition, echoing how your `ai-prototype-development` lesson already teaches the "five ingredients" prompt structure for build prompts.
- **Career/skills framing, not just task framing.** Beyond "how do I use AI today," students likely want "what skills should I be building so I stay valuable." NN/G's "Redefine Your Design Skills to Prepare for AI" and "The Future-Proof Designer" give a concrete answer (storytelling, data judgment, strategic framing) that could close the lesson on a forward-looking note, similar to how `ai-prototype-development-lesson.md` ends with "the designers who get hired... will be the ones who can define the system clearly enough that AI can build from it."
- **An "AI workflow audit" as a hands-on activity.** Rather than only teaching stages abstractly, have students map their *current* personal workflow (which tools, which stages, ad hoc or deliberate) before introducing the framework — mirrors the diagnostic approach your other lessons use (e.g., the Figma-file checklist in `ai-prototype-development-lesson.md`'s Pre-Class Preparation).
- **Ethics and bias as a standing agenda item, not a footnote.** Given your program serves Vietnamese/SEA designers, and training data skews Western — this deserves more than a caveat. IDEO's downloadable ethics tools (cited below) could become an actual in-class exercise rather than a mentioned resource.
- **Feed forward, don't start fresh.** A new AI conversation defaults to zero context — most designers' instinct is to retype a project summary from memory every time, which is slow and where inconsistency creeps in (this week's description of the research subtly contradicts last week's). The fix: treat the local folder (above) as an artifact library, and default to pasting/attaching a saved artifact as Context rather than re-describing the project. This is sometimes called "context engineering" in 2026 AI practice — see [Sourcegraph's guide](https://sourcegraph.com/blog/context-engineering) and [Karo Zieminski's 2026 Operating Manual](https://karozieminski.substack.com/p/context-engineering-product-builders-guide-2026) — and it's also exactly what the `ai-prototype-development` lesson's "prototype pattern" already does under a different name: a saved artifact fed into every build prompt instead of re-explained per screen. Worth generalizing this as a habit across all five Design Thinking stages, not just Prototype: each stage should hand its output forward as the next stage's Context (Empathise → synthesis doc → Define → problem statement → Ideate → selected directions → Prototype → prototype pattern → Test → test synthesis). Many AI chat tools in 2026 also support persistent project-level context/memory (upload once, referenced automatically in future conversations) — worth a live demo if the class's chosen tool supports it.
- **Distinguish "AI-assisted" from "AI-generated."** Your `ai-prototype-development-lesson.md` already draws this distinction well for prototypes — it's worth generalizing as a core vocabulary term for the whole lesson: the designer stays in control of decisions; AI handles assembly. This one distinction could be the lesson's throughline.

---

## 9. Technical Literacy Primer — Vocabulary Designers May Not Know

Most UX designers have never needed to open a text editor or a terminal — Figma abstracted all of that away. But the moment AI workflows enter the picture (especially AI coding tools and AI-generated prototypes), three concepts show up constantly and nobody stops to explain them. Worth a short "before we start" glossary section in the lesson — probably in Pre-Class Preparation or as the opening 5 minutes, since everything downstream assumes this vocabulary.

### What is a `.md` file (Markdown)? Why do we need it?

**What it is:** Markdown is a plain-text way of writing formatted documents — headings, bold, bullet lists, tables, links — without a word processor. Instead of clicking a "Bold" button, you type `**bold**`. Instead of choosing "Heading 2" from a menu, you type `## Heading`. A `.md` file is just a `.txt` file that follows these typing conventions; any plain text editor can open it, and tools that understand Markdown (GitHub, Notion, AI chat tools, this very course's lesson files) render it as a nicely formatted document.

**Why designers need it:**
- **It's the native language of AI tools.** When you paste a prompt, a component inventory, or a prototype pattern into an AI chat tool, Markdown formatting (headers, tables, bullet lists) is how you give it clean structure — and it's also how the AI formats its replies back to you. Learning to read a `.md` file is learning to read what AI tools produce by default.
- **It's lightweight and versionable.** Unlike a Word doc or Figma file, a `.md` file is just text — it can be copied, pasted, diffed, and tracked by version control (like `git`) without any special software. This is why engineers write documentation, READMEs, and specs in Markdown instead of Google Docs.
- **It's what this course is built on.** Every lesson file in this program (`*-lesson.md`, `*-slide-outline.md`) is Markdown. If a student ever needs to open one directly instead of just reading it, they should recognize `#` = heading, `-` = bullet, `**text**` = bold, `| |` = table — that's the entire vocabulary needed to read 95% of Markdown.
- **Practical takeaway for the lesson:** students don't need to write Markdown by hand — but they should recognize a `.md` file when an AI tool creates one (e.g., "I've saved this as `component-inventory.md`") and know they can open it in any text editor, Notion, or even just paste it back into an AI chat tool.

### What is HTML? Why do we need it?

**What it is:** HTML (HyperText Markup Language) is the language every web page is built from. It's not a programming language — it's a structural one. It uses "tags" to say what each piece of content *is*: `<button>` marks something as a button, `<img>` marks an image, `<h1>` marks a main heading, `<div>` marks a generic container/section. A browser (Chrome, Safari) reads an HTML file and draws it on screen as the page you actually see.

**Why designers need it:**
- **It's what AI-generated prototypes actually are.** As covered in the `ai-prototype-development` lesson, when an AI coding tool "builds a screen," what it's literally producing is an HTML (or React, which compiles down to HTML) file. Understanding that the AI's output is HTML demystifies what's happening — it's not a black box, it's a document made of nested tags, and it's directly readable.
- **Nesting = hierarchy, which designers already understand.** HTML tags nest inside each other the same way Atomic Design components nest (an Organism contains Molecules, which contain Atoms). A `<nav>` tag containing `<button>` tags is structurally the same idea as `o/navigation` containing `a/button` instances. This is a fast way to make HTML feel familiar rather than foreign.
- **It lets designers give precise feedback instead of vague feedback.** "This looks off" is a hard note for AI to act on. "The button is outside the card's `<div>`, that's why it's not padded correctly" is something both a human and an AI tool can act on directly. Teaching just enough HTML vocabulary (tag, attribute, nesting) upgrades the quality of every correction a designer gives during the build-and-review loop.
- **Practical takeaway for the lesson:** students don't need to write HTML from scratch — but they should be able to recognize that a "browser-viewable prototype" means an HTML file opened in a browser (not a Figma link), and be able to skim generated code well enough to spot obviously wrong structure (a button that isn't inside a form, an image tag with no image).

### Local Folder Setup — Why "Where Your Files Live" Matters, at Every Stage

**What it is:** A *local folder* is simply a folder on your own computer's hard drive (as opposed to a Figma file living on Figma's servers, or a Google Doc living in Drive). This is not just a Prototype-stage concept — the moment a student starts pasting research notes or synthesis output into an AI chat tool at Empathise, a clean folder is what lets them find and reuse that work later. It becomes most visible once they open an AI coding tool (Cursor, GitHub Copilot, Windsurf), which doesn't read one file at a time — it opens an entire local folder as a "project" and reads everything inside it as context — but the habit should start on day one, not the day they open a coding tool.

**Why designers need to understand this — and set it up well:**
- **A messy folder produces messy output at every stage**, not just at build time — the same reason a messy Figma file (per the `design-framework` lesson's cleanup step) produces a messy component inventory.
- **One project = one folder — but there's no single correct way to organise inside it.** Worth presenting as options, not a mandate:
  - **By design process stage** — `01-empathise/ 02-define/ 03-ideate/ 04-prototype/ 05-test/`. Mirrors the process; fast to find "what did I do at Define?"
  - **By file type** — `notes/ assets/ prompts/ exports/`. Fast to grab "all my notes" regardless of stage; also the structure AI coding tools expect most naturally once a student reaches Prototype.
  - **By deliverable** — `research/ design-system/ prototype/ presentation/`. Best for team projects where the output matters more than the stage-by-stage history.
  A reasonable progression: students start with the file-type option (simplest) for their first project, then move to the by-stage option once they feel the friction of hunting through mixed content.
- **Cloud-sync folders (Google Drive, Dropbox) can complicate this.** If a student's project folder lives inside a cloud-synced Drive folder, AI coding tools sometimes behave unpredictably (files appearing as placeholders until downloaded, sync conflicts while the AI is writing). Worth a one-line warning: for AI coding tool work, prefer a plain local folder over a cloud-sync folder, and export/copy the finished result to Drive afterward.
- **Practical takeaway for the lesson:** a short "before you start" checklist — create one dedicated folder for this project on day one, pick one of the three organisation options above, and avoid working directly inside a live cloud-sync folder while an AI tool is actively writing files.

---

## Curated Resources

### Research & Reports (data to cite in the lesson)

- **[Figma — State of the Designer 2026](https://www.figma.com/reports/state-of-the-designer-2026/)** and **[Figma's 2026 AI Report](https://www.figma.com/blog/2026-ai-report/)** — survey of 906+ designers; the adoption stats (91% use AI, 72% use genAI, satisfaction/collaboration deltas) come from here. Best single source for "why now" data to open the lesson.
- **[NN/G — Using AI for UX Work: Study Guide](https://www.nngroup.com/articles/ai-work-study-guide/)** *(Oct 2025)* — the single best curated index for this entire lesson. Organized into Integrating AI into Workflows, Career Strategy, Design, Research, Writing, Service Design, Ideation/Workshops, and State of AI — practically a syllabus already. Start lesson planning here.
- **[McKinsey — State of AI 2025]** *(referenced via search; McKinsey's ongoing State of AI series)* — source for the 22% higher feature adoption stat for AI-integrated product design workflows. Worth pulling the primary McKinsey report directly if citing a specific number in slides.
- **[IDEO — 2024 AI Research](https://www.ideo.com)** — businesses using AI saw measurable growth gains concentrated in *growth*, not cost-cutting — useful reframe against the "AI = efficiency/cost savings" assumption.

### Mindset & Framework Articles

- **[NN/G — AI for UX: Getting Started](https://www.nngroup.com/articles/ai-ux-getting-started/)**
- **[NN/G — AI as a UX Assistant](https://www.nngroup.com/articles/ai-roles-ux/)** — the "content editor / research assistant / ideation partner / design assistant" framing is a clean structure to borrow.
- **[NN/G — 7 Deadly AI Sins for UX Professionals](https://www.nngroup.com/articles/7-ai-sins/)** — a ready-made checklist/activity.
- **[NN/G — Your AI UX Intern: Meet Ari](https://www.nngroup.com/articles/ai-intern/)** — the intern metaphor, genuinely useful for framing supervision.
- **[NN/G — Redefine Your Design Skills to Prepare for AI](https://www.nngroup.com/articles/prepare-for-ai/)**
- **[NN/G — The Future-Proof Designer](https://www.nngroup.com/articles/future-proof-designer/)**
- **[NN/G — The Return of the UX Generalist](https://www.nngroup.com/articles/return-ux-generalist/)**
- **[NN/G — Design Taste vs. Technical Skills in the Era of AI](https://www.nngroup.com/articles/taste-vs-technical-skills-ai/)**
- **[NN/G — The VR Hype Cycle: Lessons for the Age of AI](https://www.nngroup.com/articles/vr-hype-cycle-lessons-for-ai/)**
- **[NN/G — CARE: Structure for Crafting AI Prompts](https://www.nngroup.com/articles/careful-prompts/)** — a reusable prompting framework for the whole lesson.
- **[Fast Company — Use AI to augment design, not replace it](https://www.fastcompany.com/91551054/use-ai-to-augment-design-not-replace-it)**
- **[TIME — Why Thinking of AI as a "Partner" Can Be Counterproductive](https://time.com)** *(via IDEO's curated list)* — good discussion-prompt material on language/framing.
- **[Smashing Magazine — Beyond Algorithms: Skills of Designers That AI Can't Replicate](https://www.smashingmagazine.com/2023/04/skills-designers-ai-cant-replicate/)**

### Design Thinking + AI (process alignment)

- **[IDEO U — The Intersection of Design Thinking and AI](https://www.ideou.com/blogs/inspiration/ai-and-design-thinking)**
- **[IDEO U — Top 22 Best AI x Design Thinking Resources](https://www.ideou.com/blogs/inspiration/best-ai-x-design-thinking-resources-books-articles-courses-more)** *(updated Nov 2025)* — itself a curated meta-list; includes IDEO's downloadable **AI ethics card deck** and **Legal & Ethical Framework for Gen AI**, both usable as in-class tools rather than just reading.
- **[Harvard Business Review — Design Thinking in the Age of AI](https://hbr.org)** *(via IDEO's list)* — practical business-process examples.
- **"AI Design Workflow — 6 must-know stages"** *(LinkedIn infographic, Imen Mlika, Digital Designer)* — AI Research Synthesis, Generative Ideation, AI Wireframing, Conversational UX, Adaptive Interfaces, Responsible AI Testing. Good sanity-check against the lesson's own 4-bucket breakdown; stages 4–6 are useful "further exploration" pointers not yet covered in depth.

### Stage-Specific (Research, Ideation, Prototype, Test)

- **[NN/G — Accelerating Research with AI](https://www.nngroup.com/articles/research-with-ai/)**
- **[NN/G — Synthetic Users: If, When, and How to Use AI-Generated "Research"](https://www.nngroup.com/articles/synthetic-users/)**
- **[NN/G — AI as a Creative Teammate](https://www.nngroup.com/articles/ai-creative-teammate/)** — the ideation research finding (AI-augmented teams outperformed both AI-less teams and AI-solo individuals).
- **[NN/G — AI-Assisted Prototyping: Promise and Pitfalls (video)](https://www.nngroup.com/videos/ai-assisted-prototyping/)**
- **[NN/G — Promptframes: Evolving the Wireframe for the Age of AI](https://www.nngroup.com/articles/promptframes/)**
- **[NN/G — Leverage AI for Mock Tables and Charts When Testing Prototypes](https://www.nngroup.com/articles/ai-data-prototype-testing/)**
- **[NN/G — AI Design Tools Are Marginally Better: Status Update (2025)](https://www.nngroup.com/articles/ai-design-tools-update-2/)** — honest, unhyped state-of-the-tools piece; good for calibrating student expectations.

### Books

- **[Human-Centered AI — Ben Shneiderman](https://www.google.com/search?q=Human-Centered+AI+Ben+Shneiderman)** *(book)* — "optimistic realist's guide" to augmenting rather than replacing human capability; probably the most credible single book to assign as pre-reading.
- **[You Look Like a Thing and I Love You — Janelle Shane](https://www.google.com/search?q=You+Look+Like+a+Thing+and+I+Love+You)** *(book)* — accessible, funny demystification of how AI actually works; good for students intimidated by the technical side.
- **The Design of Everyday Things — Don Norman** *(classic, not AI-specific)* — resurfaces in multiple curated AI-for-designers reading lists as the grounding text on affordances and feedback loops that still applies when co-designing with AI output.
- *(Optional, lighter):* **AI for Designers — Md Haseen Akhtar & Janakarajan Ramkumar** — beginner-friendly, direct bridge between AI concepts and design practice; useful as an assigned skim rather than a deep read.

### Video / Podcast

- **[NN/G — Outcome-Oriented Design: The Era of AI Design (video)](https://www.nngroup.com/videos/the-era-of-ai-design/)**
- **[NN/G — Return of the Generalist (video)](https://www.nngroup.com/videos/return-of-the-generalist/)**
- **NN/G Podcast — "AI & UX Research" (feat. Savina Hawkins & Caleb Sponheim)** and **"Design's Role as AI Expands" (feat. Don Norman & Sarah Gibbons)** — both linked from the NN/G study guide above; strong for an audio pre-work assignment.
- **IDEO U — Creative Confidence Podcast**, AI-focused episodes (via IDEO's curated resource list) — interviews with Tom Gruber (co-creator of Siri) and Google DeepMind's creative AI lead; good for a "hear from practitioners outside pure UX" angle.

---

## Suggested Next Step

If you want to move from brainstorm to lesson file: pick which framework to anchor on (Design Thinking's 5 stages is the most natural fit, since students already have that vocabulary from `design-thinking-lesson.md`), and I can draft the `*-lesson.md` / `*-slide-outline.md` pair from this brainstorm, following your existing lesson conventions (Overview, Learning Objectives, Session Structure, Core Content, Activities, AI in Practice, Assessment, Resources).
