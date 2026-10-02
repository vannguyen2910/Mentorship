// ═══════════════════════════════════════════════════════════════
//  WINNIE NGUYEN — KNOWLEDGE LIBRARY DATA
//  This is your source of truth. Edit this file to manage
//  your library. The HTML site reads from here automatically.
//
//  HOW TO ADD A MATERIAL:
//  1. Copy an existing entry (from { to the closing },)
//  2. Paste it at the top of the array (after the first [)
//  3. Update all the fields
//  4. Save this file and refresh the site
//
//  FIELD REFERENCE:
//  id            → unique number (increment from the last one)
//  type          → "lesson" | "framework" | "slides" | "guide"
//  program       → "ux-class" | "private" | "both"
//  title         → display title of the material
//  description   → 1–2 sentence summary shown on the card
//  audience      → "Beginner" | "Intermediate" | "Advanced"
//  duration      → e.g. "90 min" or "Reference" or "Full deck"
//  tags          → array of short topic tags, e.g. ["Research", "Synthesis"]
//  objectives    → array of learning outcomes (keep to 2–4)
//  prerequisites → array of suggested prior knowledge (can be empty [])
//  date          → display date, e.g. "Apr 2026"
//  file          → relative path to the .md file, e.g. "lessons/my-lesson.md"
//                  leave as "" if no file yet
//
//  crossRef      → array of intentional links to other materials
//                  each item: { id: <number>, rel: "<relationship>" }
//                  rel options:
//                    "requires"  → students should complete this first
//                    "uses"      → this lesson/guide uses this framework/tool
//                    "extends"   → goes deeper on the same topic
//                    "companion" → pair these together in the same session
//                  leave as [] if no cross-references
//
//  stage         → which design thinking stage this LESSON belongs to.
//                  Leave unset for frameworks/slides/guides.
//                  "Discover" | "Define" | "Develop" | "Deliver" | "Foundation"
//                  "Foundation" = cross-cutting, spans multiple stages
//                  (design thinking overview, AI workflow, mental models)
// ═══════════════════════════════════════════════════════════════

window.LIBRARY_DATA = [

  {
    id: 1,
    type: "lesson",
    program: "both",
    title: "Synthesis & Problem Definition in UX",
    description: "How to move from raw research findings to actionable insights using Affinity Mapping and How Might We statements. Includes a practice dataset and AI integration exercises.",
    audience: "Intermediate",
    duration: "90–120 min",
    tags: ["Research", "Synthesis", "HMW"],
    objectives: [
      "Apply affinity mapping to organise raw research findings into themes",
      "Write effective How Might We statements that reframe problems as opportunities",
      "Distinguish between a data point, an insight, and a problem statement",
    ],
    prerequisites: ["Basic familiarity with user interviews or observation"],
    date: "Apr 2026",
    file: "lessons/02-define/synthesis-problem-definition-in-ux/materials/synthesis-problem-definition-in-ux-lesson.md",
    page: "lessons/02-define/synthesis-problem-definition-in-ux/slides/synthesis-problem-definition-in-ux.html",
    crossRef: [{ id: 6, rel: "requires" }, { id: 3, rel: "uses" }, { id: 8, rel: "companion" }]
  },

  {
    id: 2,
    type: "lesson",
    program: "ux-class",
    title: "Mental Models in UX Design",
    description: "Understanding how users build mental maps of systems — and how to design interfaces that align with those expectations rather than fight them.",
    audience: "Beginner",
    duration: "60–75 min",
    tags: ["UX Research", "Cognition"],
    objectives: [
      "Explain what a mental model is and why it matters in UX",
      "Identify mismatches between a product's design model and user expectations",
      "Apply mental model thinking to a critique of an existing interface",
    ],
    prerequisites: [],
    date: "Mar 2025",
    file: "",
    page: "lessons/00-foundation/mental-models-in-ux-design/slides/mental-models-in-ux-design.html",
    crossRef: [{ id: 4, rel: "companion" }, { id: 7, rel: "extends" }]
  },

  {
    id: 3,
    type: "framework",
    program: "both",
    title: "Journey Mapping Workshop Guide",
    description: "A step-by-step facilitation guide for running a 2-hour journey mapping session with cross-functional teams. Includes warmup activities, facilitation cues, and debrief prompts.",
    audience: "Intermediate",
    duration: "2 hr workshop",
    tags: ["Research", "Workshop", "Facilitation"],
    objectives: [
      "Facilitate a structured journey mapping session with a mixed team",
      "Guide participants from raw touchpoints to emotional insight",
      "Extract actionable opportunities from the completed map",
    ],
    prerequisites: ["Some prior exposure to user research"],
    date: "Jan 2025",
    file: "",
    page: "frameworks/journey-mapping-workshop-guide/journey-mapping-workshop-guide.html",
    crossRef: [{ id: 6, rel: "requires" }, { id: 1, rel: "companion" }]
  },

  {
    id: 4,
    type: "framework",
    program: "ux-class",
    title: "UX Design Principles Reference",
    description: "A one-page cheat sheet of 12 core UX design principles — from Fitts's Law to progressive disclosure. Designed to be printed and used as a daily reference.",
    audience: "Beginner",
    duration: "Reference",
    tags: ["Foundations", "Principles"],
    objectives: [
      "Recall and apply 12 foundational UX design principles",
      "Use the reference sheet to evaluate design decisions in critiques",
    ],
    prerequisites: [],
    date: "Oct 2024",
    file: "",
    page: "frameworks/ux-design-principles-reference/ux-design-principles-reference.html",
    crossRef: [{ id: 2, rel: "companion" }, { id: 7, rel: "companion" }]
  },

  {
    id: 5,
    type: "slides",
    program: "ux-class",
    title: "Product Thinking Foundations",
    description: "Core concepts for thinking like a product designer — balancing user needs, business goals, and technical constraints. Full class deck with speaker notes.",
    audience: "Intermediate",
    duration: "Full class deck",
    tags: ["Product", "Strategy"],
    objectives: [
      "Explain the product design triangle: user, business, technology",
      "Apply product thinking to evaluate feature proposals",
      "Practise reframing design problems as business opportunities",
    ],
    prerequisites: ["Intro to UX Design"],
    date: "Nov 2024",
    file: "",
    page: "slides/product-thinking-foundations/product-thinking-foundations.html",
    crossRef: [{ id: 2, rel: "requires" }, { id: 7, rel: "companion" }]
  },

  {
    id: 6,
    type: "slides",
    program: "ux-class",
    title: "Intro to UX Research Methods",
    description: "An overview of the most common UX research methods — when to use each, what they're good for, and how to choose the right method for your question.",
    audience: "Beginner",
    duration: "45 min",
    tags: ["Research", "Methods"],
    objectives: [
      "Identify 6+ common UX research methods and their use cases",
      "Choose the right method given a research question and constraints",
      "Distinguish between generative and evaluative research",
    ],
    prerequisites: [],
    date: "Sep 2024",
    file: "",
    page: "slides/intro-to-ux-research-methods/intro-to-ux-research-methods.html",
    crossRef: [{ id: 8, rel: "companion" }, { id: 1, rel: "extends" }]
  },

  {
    id: 7,
    type: "guide",
    program: "both",
    title: "How to Give Design Critique",
    description: "A structured approach to critiquing design work — focusing on intent, not taste. Covers the ABCD method and common mistakes that make critique feel personal.",
    audience: "Intermediate",
    duration: "Reference",
    tags: ["Coaching", "Critique", "Culture"],
    objectives: [
      "Give specific, useful feedback grounded in design intent",
      "Avoid the most common critique pitfalls (taste, solutions, vagueness)",
      "Use the ABCD framework to structure any design feedback",
    ],
    prerequisites: [],
    date: "Sep 2024",
    file: "",
    page: "guides/how-to-give-design-critique/how-to-give-design-critique.html",
    crossRef: [{ id: 4, rel: "companion" }, { id: 2, rel: "extends" }]
  },

  {
    id: 8,
    type: "guide",
    program: "private",
    title: "Interviewing Users Effectively",
    description: "Techniques and scripts for running user interviews that uncover real behaviour, not just stated preferences. Includes a question bank and common pitfalls.",
    audience: "Beginner",
    duration: "Reference",
    tags: ["UX Research", "Methods", "Interviews"],
    objectives: [
      "Write open-ended questions that reveal real user behaviour",
      "Avoid leading questions and confirmation bias in interviews",
      "Synthesise interview notes into key observations on the same day",
    ],
    prerequisites: [],
    date: "Aug 2024",
    file: "",
    page: "guides/interviewing-users-effectively/interviewing-users-effectively.html",
    crossRef: [{ id: 6, rel: "companion" }, { id: 1, rel: "extends" }]
  },

  {
    id: 9,
    type: "lesson",
    program: "both",
    title: "Information Architecture",
    description: "How to organise content around users — not the org chart. Covers inherited vs evidence-based IA, card sorting, sitemaps, and drawing a current-state user flow before touching a wireframe.",
    audience: "Intermediate",
    duration: "90–120 min",
    tags: ["IA", "Navigation", "Card Sorting", "Sitemaps", "User Flows", "JTBD"],
    objectives: [
      "Distinguish between inherited IA and evidence-based IA — and audit an existing product structure",
      "Apply card sorting to reveal how users mentally group content",
      "Draw a current-state sitemap and identify where structure reflects business logic rather than user logic",
      "Map a current-state user flow using correct shapes and swimlanes before wireframing",
    ],
    prerequisites: ["JTBD Map from Session 2", "Validated Problem Statement from Session 3", "Screenshots of your current product screens"],
    date: "Apr 2026",
    file: "",
    page: "lessons/03-develop/information-architecture/slides/information-architecture.html",
    crossRef: [{ id: 18, rel: "extends" }]
  },

  {
    id: 10,
    type: "lesson",
    program: "private",
    title: "Desk Research",
    description: "Turn raw assumptions into a prioritised map, then run a competitor scan and tap existing sources to build an evidence-backed picture before touching a redesign.",
    audience: "Intermediate",
    duration: "90 min",
    tags: ["Desk Research", "Competitor Analysis", "Assumption Map", "Stakeholder Presentation"],
    objectives: [
      "Formalise raw assumptions into a prioritised map before evidence-gathering begins",
      "Log a competitor scan as patterns, not screenshots, aimed at named assumptions",
      "Gather tickets, analytics and prior research as evidence for named assumptions",
      "Synthesise findings into evidence-grounded insight statements and present them to stakeholders",
    ],
    prerequisites: ["Evaluate Current Experience (evaluation.md); seniors may skip via fast-track", "Raw assumptions list from prior session"],
    date: "Aug 2026",
    file: "lessons/01-discover/desk-research/materials/desk-research-lesson.md",
    crossRef: [{ id: 12, rel: "companion" }]
  },

  {
    id: 11,
    type: "lesson",
    program: "ux-class",
    title: "Customer Understanding",
    description: "The mindset shift from 'I know my users' to structured evidence: friction metrics, assumption mapping, research questions, and real user interviews.",
    audience: "Beginner",
    duration: "90 min",
    tags: ["Customer Understanding", "Friction Metrics", "Assumptions", "Research Questions", "User Interviews"],
    objectives: [
      "Identify friction in an existing experience using cognitive, interaction, and emotional friction types",
      "Categorise team assumptions by type and rank them on an importance-vs-evidence matrix",
      "Convert an assumption into a research question and a set of interview questions",
      "Apply user interview fundamentals — open questions, following the story, listening more than speaking",
    ],
    prerequisites: [],
    date: "Jun 2026",
    file: "lessons/01-discover/customer-understanding/materials/customer-understanding-lesson.md",
    crossRef: [{ id: 13, rel: "requires" }]
  },

  {
    id: 12,
    type: "lesson",
    program: "private",
    title: "Customer Understanding (Senior / Lead)",
    description: "Jobs to Be Done for senior practitioners: a stakeholder check-in surfaces the business's assumed customer job, a JTBD-informed interview tests it, and the gap becomes an actionable, pitch-ready insight.",
    audience: "Advanced",
    duration: "90 min",
    tags: ["JTBD", "Jobs to Be Done", "Stakeholder Interview", "User Interview", "Actionable Insight"],
    objectives: [
      "Apply the JTBD framework to build a stage-by-stage map of candidate job hypotheses",
      "Run a stakeholder check-in that surfaces the business's assumed customer job",
      "Conduct a JTBD-informed customer interview across multiple conversations to see a pattern",
      "Write and pitch an actionable insight — observation, implication, and a named decision",
    ],
    prerequisites: ["Desk Research (Assumption Map, insight statements)"],
    date: "Aug 2026",
    file: "lessons/01-discover/customer-understanding/materials/customer-understanding-senior-lesson.md",
    crossRef: [{ id: 10, rel: "requires" }]
  },

  {
    id: 13,
    type: "lesson",
    program: "ux-class",
    title: "Design Thinking for UX Designer",
    description: "The program's entry-point session: why process problems (not skill problems) derail design work, and the 5-stage Empathise/Define/Ideate/Prototype/Test cycle as a flexible tool, not a checklist.",
    audience: "Beginner",
    duration: "90 min",
    tags: ["Design Thinking", "Empathise", "Define", "Ideate", "Prototype", "Test", "UX Process"],
    objectives: [
      "Explain what Design Thinking is and why it exists, in stakeholder-ready language",
      "Identify the 5 stages of the cycle and what question each stage answers",
      "Recognise where a current design process typically breaks down",
      "Draft a project-specific process map naming activities and outputs per stage",
    ],
    prerequisites: [],
    date: "Jun 2026",
    file: "lessons/00-foundation/design-thinking/materials/design-thinking-lesson.md",
    crossRef: [{ id: 11, rel: "companion" }, { id: 14, rel: "companion" }]
  },

  {
    id: 14,
    type: "lesson",
    program: "ux-class",
    title: "Set Up Your AI Workflow",
    description: "How AI fits deliberately into the Design Thinking cycle — AI-assisted vs AI-generated, the CARE prompting framework, and a personal tool stack — before students touch AI seriously in later sessions.",
    audience: "Beginner",
    duration: "90 min",
    tags: ["AI", "Workflow", "Prompting", "Design Thinking", "Draft"],
    objectives: [
      "Distinguish AI-assisted from AI-generated work, and default to AI-assisted by design",
      "Apply the CARE prompting framework (Context, Ask, Rules, Examples)",
      "Map AI's role across each of the 5 Design Thinking stages",
      "Set up a personal AI tool stack and a clean local project folder",
    ],
    prerequisites: ["Design Thinking for UX Designer"],
    date: "Jul 2026",
    file: "lessons/00-foundation/ai-workflow-for-ux-designers/materials/ai-workflow-for-ux-designers-lesson.md",
    crossRef: [{ id: 13, rel: "requires" }]
  },

  {
    id: 15,
    type: "lesson",
    program: "ux-class",
    title: "Design Once. Use Everywhere.",
    description: "Atomic Design as the methodology for translating a validated concept into a buildable design framework — tokens, atoms, molecules, organisms, through to a completed Template and Page.",
    audience: "Intermediate",
    duration: "45 min",
    tags: ["Design System", "Atomic Design", "Components", "System Thinking", "Draft"],
    objectives: [
      "Apply the 5-step process — find screens, sketch zones, map patterns, define tokens, build components",
      "Distinguish the reading direction (top-down) from the build direction (bottom-up)",
      "Translate design principles from validated user feedback into token decisions",
      "Build a completed Template and at least one Page from a validated concept",
    ],
    prerequisites: ["A validated concept from user/stakeholder feedback"],
    date: "May 2026",
    file: "lessons/03-develop/design-framework/materials/design-framework-lesson.md",
    crossRef: [{ id: 16, rel: "requires" }]
  },

  {
    id: 21,
    type: "lesson",
    program: "standalone",
    title: "UI Fundamentals",
    description: "Judging design decisions you didn't make. Five layers of visual decision-making, taught evaluation-first: AI collapsed the Gulf of Execution but not the Gulf of Evaluation, so juniors can produce screens they cannot choose between. Same instrument pointed at three inherited surfaces: screens they didn't make, their own screen, and the component their team already uses.",
    audience: "Junior",
    duration: "90 min",
    tags: ["UI Design", "Visual Hierarchy", "Typography", "Colour", "Design Tokens", "Components", "Accessibility", "UX Laws", "Draft"],
    objectives: [
      "Explain why an attractive screen is not evidence of a usable one, and name the research behind it",
      "Apply five layers in reading order: space, hierarchy, type, colour, component",
      "Say the reason behind a UI decision out loud, in a developer's register",
      "Identify two commonly misapplied UX laws and explain why the usual application is wrong",
      "Audit the design tokens their team already uses, and name what is inconsistent or undefined",
      "Interrogate an inherited component and raise a problem with it as a question rather than an accusation",
    ],
    prerequisites: ["One real screen from their own work", "Access to their team's components, in whatever state"],
    date: "September 2026",
    file: "lessons/03-develop/ui-fundamentals/materials/ui-fundamentals-lesson.md",
    crossRef: [{ id: 15, rel: "related" }]
  },

  {
    id: 16,
    type: "lesson",
    program: "ux-class",
    title: "Build the Pattern First",
    description: "Prototyping with AI as a collaborator, not a generator: define the component inventory and interaction pattern first, then have an AI coding tool assemble a working, browser-viewable prototype from it.",
    audience: "Intermediate",
    duration: "90 min",
    tags: ["Prototype", "AI", "Design System", "Pattern-First", "System Thinking", "Draft"],
    objectives: [
      "Explain why template-first prototyping avoids the inconsistency of screen-by-screen AI prompting",
      "Define a component inventory (including states) and an interaction pattern before prompting",
      "Direct an AI coding tool to generate a working prototype from that pattern",
      "Review and correct AI-assembled screens against the defined system",
    ],
    prerequisites: ["Design Once. Use Everywhere. (Atomic Design)"],
    date: "Jun 2026",
    file: "lessons/03-develop/ai-prototype-development/materials/ai-prototype-development-lesson.md",
    crossRef: [{ id: 15, rel: "requires" }, { id: 19, rel: "companion" }]
  },

  {
    id: 17,
    type: "lesson",
    program: "both",
    title: "Develop Solutions & Ideate",
    description: "Diverge before you converge: Opportunity Tree Mapping, Crazy 8s, concept sketching, concept validation, and an effort-impact matrix to prioritise which ideas are worth developing further.",
    audience: "Intermediate",
    duration: "60–90 min",
    tags: ["Ideation", "Opportunity Tree", "Crazy 8s", "Concept Sketching", "Concept Validation", "Prioritisation"],
    objectives: [
      "Apply the diverge-before-converge mindset to avoid converging too early",
      "Use Opportunity Tree Mapping to move from problem statement to opportunities to solutions",
      "Run Crazy 8s and concept sketching to generate and visualise multiple directions",
      "Validate a concept's logic (legibility, rationale, traceability) and prioritise using an effort-impact matrix",
    ],
    prerequisites: ["A defined problem statement or research insight"],
    date: "Jun 2026",
    file: "lessons/03-develop/develop-solutions-ideate/materials/develop-solutions-ideate-lesson.md",
    crossRef: []
  },

  {
    id: 18,
    type: "lesson",
    program: "both",
    title: "Interaction Design & User Flows",
    description: "Goes deeper than IA's structural foundation: task flows vs user flows, designing for states as a method, and B2B-specific interaction patterns for navigation, forms, and data tables.",
    audience: "Intermediate",
    duration: "90–120 min",
    tags: ["Task Flows", "User Flows", "State Design", "B2B Interaction Patterns", "Handoff Annotation"],
    objectives: [
      "Distinguish a task flow from a user flow and choose the right artefact",
      "Design for states as a deliberate decision, not a pre-handoff checklist item",
      "Apply B2B-specific interaction patterns for navigation, forms, and data tables",
      "Review every flow against the JTBD Map to confirm it serves the user's job",
    ],
    prerequisites: ["Information Architecture (user flow shape language, happy path, swimlanes)"],
    date: "May 2026",
    file: "lessons/03-develop/interaction-design-user-flows/materials/interaction-design-user-flows-lesson.md",
    crossRef: [{ id: 9, rel: "requires" }]
  },

  {
    id: 19,
    type: "lesson",
    program: "ux-class",
    title: "Solution Validation & User Testing",
    description: "Closes the design thinking loop: a prototype is a hypothesis, not a deliverable. Method selection, test planning, moderated facilitation with think-aloud, and synthesis using the Feedback Capture Grid.",
    audience: "Intermediate",
    duration: "90 min",
    tags: ["User Testing", "Solution Validation", "Usability", "Moderated", "Unmoderated", "Synthesis"],
    objectives: [
      "Reframe a prototype as a testable hypothesis with a specific question to answer",
      "Choose the right testing method based on fidelity level and question type",
      "Facilitate a moderated usability session using the think-aloud protocol",
      "Synthesise findings into prioritised recommendations using the Feedback Capture Grid",
    ],
    prerequisites: ["Build the Pattern First (AI Prototype Development)"],
    date: "Jun 2026",
    file: "lessons/04-deliver/solution-validation-user-testing/materials/solution-validation-user-testing-lesson.md",
    crossRef: [{ id: 16, rel: "requires" }]
  },

  {
    id: 20,
    type: "lesson",
    program: "private",
    title: "Problem Definition & Strategy (Senior / Lead)",
    description: "Turns a research finding into a decision: build an opportunity map from the JTBD map, reframe the strongest branch, choose one problem with the rejection written down, then write a project-level design strategy with principles, non-goals and a measure.",
    audience: "Advanced",
    duration: "90 min",
    tags: ["Problem Definition", "Problem Statement", "Opportunity Mapping", "Reframing", "Design Strategy", "Prioritisation", "Design Principles"],
    objectives: [
      "Distinguish a JTBD map from an opportunity map, and explain why a description cannot rank itself",
      "Convert JTBD gaps into an opportunity space rooted in a single product outcome",
      "Choose one problem on evidence-based criteria and state in writing why the runner-up lost",
      "Write a problem statement in its senior form: cost, stage and evidence base included",
      "Build a design strategy using diagnosis, guiding policy and coherent action, with explicit non-goals",
      "Defend the bet against the question a commitment invites: why not the other one",
    ],
    prerequisites: ["Customer Understanding (Senior / Lead): JTBD map, insight statements"],
    date: "Aug 2026",
    file: "lessons/02-define/problem-definition-strategy/materials/problem-definition-strategy-lesson.md",
    crossRef: [{ id: 12, rel: "requires" }, { id: 1, rel: "companion" }]
  },

  {
    id: 21,
    type: "guide",
    program: "private",
    title: "Publish Your Work — Git & GitHub for Non-Technical Designers",
    description: "A hands-on, 1:1 walkthrough that takes a working AI prototype from a local folder to a real, live URL — GitHub Desktop as the tool-agnostic backbone, with an AI-tool prompt shortcut for the same workflow.",
    audience: "Beginner",
    duration: "90–100 min",
    tags: ["Git & GitHub", "Publishing", "AI Coding Tools", "Hands-on"],
    objectives: [
      "Explain the core mental model: local folder as draft, GitHub as published, push as the publish button",
      "Commit and push a project to GitHub using GitHub Desktop, then verify it went live",
      "Turn on GitHub Pages and confirm a working public URL",
      "Prompt an AI coding tool to run the same publish workflow end-to-end",
      "Recover from a bad commit — discard an uncommitted change or amend a bad one — using GitHub Desktop",
    ],
    prerequisites: ["Build the Pattern First (AI Prototype Development)"],
    date: "Sep 2026",
    file: "guides/publish-your-work-git-github-for-non-technical-designers/learning/index.md",
    page: "guides/publish-your-work-git-github-for-non-technical-designers/publish-your-work-git-github-for-non-technical-designers.html",
    crossRef: [{ id: 16, rel: "extends" }]
  }

];
