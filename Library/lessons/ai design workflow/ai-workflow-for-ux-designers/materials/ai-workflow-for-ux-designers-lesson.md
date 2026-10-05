---
title: "Set Up Your AI Workspace"
subtitle: "The shared vocabulary and the folder every later lesson builds on"
type: lesson
program: ai-design-workflow
tags: [ai, terminology, context, folder, data-safety, hub, foundational]
level: foundational
duration: "90 min"
date: 2026-10-05
draft: true
slides: ""
previous-session: ""
next-session: "Shape the Brief with Your PO"
---

## Overview

This is the first lesson of the AI Design Workflow series for mid and senior designers. It does three jobs, so no later lesson has to repeat them.

**1. A shared vocabulary.** When an AI tool talks about a "context window", an "agent" or "MCP", you should know what it means and what to do about it.

**2. A project folder the AI can work with.** Every later lesson adds one file or one page to the same case. In a clear structure, each AI step gets a named input and you can find, check and reuse everything.

**3. A clear rule for what is safe to give an AI tool.** Designers hold other people's material. Before anything is pasted into a tool, you need a way to decide what is safe.

The lesson also sets the stance for the series: **designers are partners who help define the requirement with the business and product, not people who wait for a PRD to arrive.** Later lessons build the habit; this one sets up the words and the tools.

**The core distinction: AI-assisted vs AI-generated.** AI-generated means the AI made the decision. AI-assisted means you decided and the AI did the assembly. AI drafts. You verify. You decide.

**How each week works (the whole series).** One online session a week with 7–8 students. Each week: **up to 15 minutes of preparation** (a little more in week 1, because you set up your tool), **a 90-minute live working session** where you apply the step to your own case with coaching, and **up to 60 minutes of homework**. About 2.5 to 2.75 hours in total. The live session never depends on homework having been done.

> **Where this sits:** it comes before the first step of the workflow. It assumes you already do research, UX design and prototyping, and teaches the AI layer on top.

---

## Learning Objectives

By the end of this session, students will be able to:

1. **Explain** ten core AI terms in their own words: AI chat tool, AI coding tool, context, context window, grounding, hallucination, agent, connector (MCP), reusable instructions (skills, rules files, project memory), and AI-assisted vs AI-generated
2. **Recognise** Markdown and HTML, and explain why a plain local folder matters when an AI tool reads or writes files
3. **Set up** the series case folder for their own case, with the standard layout, a started context pack and an empty hub
4. **Reuse** a saved file as context for an instruction instead of retyping a project description, and ask for a source pointer and an "unknown" answer
5. **Decide** what is safe to give an AI tool by sorting material into three kinds (safe, ask first, never in a public tool), anonymise before pasting, and write their own data rules
6. **Explain** how to share their hub with a stakeholder: private by default (a PDF or zipped folder), and published on GitHub only when the case is free to share

---

## Materials Needed

- **At least one AI chat tool on the student's own laptop** that the student's company allows (or the course case card, below, if none is allowed). Recommended examples are in the tools handout (`tools-to-bring.md`)
- A laptop with a file explorer open
- The Week 1 brief (the one-page pre-read at the end of this file)
- The case card for the demo (Phase 1), ten terminology cards, and six material cards for the sorting exercise
- The series case folder template and the empty hub template folder
- The student publishing guide (`publish-guide.md`), for the optional homework
- One case to use through the series. **Default: the student's own case** (real or realistic). Fallback: the course case card, or a product the student knows from outside

---

## Pre-Class Preparation (about 20 minutes this first week; 10 to 15 minutes in later weeks)

**For students:**

1. **Bring your AI tool.** Read the tools handout (`tools-to-bring.md`, about 5 minutes) and do its 5-minute test, so your tool is working before class. You need a chat tool now and a coding tool by week 6.
2. **Read the Week 1 brief** (one page, at the end of this file). It holds the ten terms and the folder layout, so class time is for using them.
3. **Choose your case.** Your own project, product or feature. Your hub stays **private by default**; you publish only if the case is free to share. Decide what you can show in class: anonymise names, figures and unreleased details first. If your company bans AI tools or the case is too sensitive for class, use the course case card for the in-class steps.
4. **Find out your company's rules on AI tools,** if you work somewhere: is there a written policy, and which tools are approved? If you do not know, ask.

**For the instructor:**
- Prepare the case card and the two demo instructions (Phase 1), and run both once beforehand.
- Have your own case folder open to screen-share, with the `hub/` folder opened in a browser.
- Print or share the ten terminology cards and the six material cards.
- Set the cohort ground rules (Phase 1).
- Prepare two breakout rooms of 3 to 4 students for the activities, and plan where you will coach.

---

## Session Structure

| Phase | Activity | Time |
|---|---|---|
| 1 | The partner mindset, and one task done twice | 12 min |
| 2 | Terms in action, Activity 1, data safety | 21 min |
| 3 | Files and folders an AI tool can work with | 10 min |
| 4 | Build your case folder (Activity 2) | 25 min |
| 5 | What comes next, the hub, sharing, close | 8 min |
| | **Content total** | **76 min** |
| | Buffer for questions, setup trouble and a short break | 14 min |

Total: 90 minutes live. Preparation up to 15 minutes before; homework up to 60 minutes after. *(If the session runs short, shorten Phase 5 and the Activity 1 sharing; do not cut the data safety block.)*

---

### Phase 1 — The Partner Mindset, and One Task Done Twice (12 min)

**Ground rules for the cohort (1 min).** This is a room of working designers with real cases. What is shared in class stays in class. Share only what you are comfortable showing, and anonymise first. Nobody has to show confidential material; the course case card is always available.

**Open with a pair question (2 min).** Each person names one time AI genuinely helped their work, and one time it quietly made the work worse without them noticing at first. The usual pattern: the helpful moments had a clear ask and a review step; the bad ones trusted the output.

**The numbers and the stance (3 min).** About 9 in 10 designers now use AI at least weekly, using seven tools on average (Designer Fund and Foundation Capital, AI + Design 2026). But in Figma's State of the Designer 2026, 36% said design got better with AI, 35% said worse, 29% saw no change. The difference is the way of working. And a designer who waits for a PRD and turns it into screens is the one most exposed, because that step is the one AI compresses. A designer who helps define the requirement with the business is doing the work AI cannot: choosing which problem is worth solving and agreeing what success means. Some of you can be in the room where requirements are shaped, some can only message the PO, some have no access. The series works in all three cases, and the next lesson teaches how.

**One task, done twice (6 min).** The instructor demo that earns the rest of the lesson. Use the case card and show two instructions on the same task.

*Case card (fictional):* "A meal-kit subscription app. Many new customers pause after their first box. The team wants to improve onboarding. The app has a delivery date picker, a menu screen and a payment step. The team suspects price is the reason people leave. No research has been done yet."

*Instruction 1, vague:* "How can I improve onboarding for my meal-kit app?"

*Instruction 2, structured (attach the case card):* "Use only the case card. List the five most important things you would need to know that are NOT in it, and say why each matters. Do not guess or fill gaps from general knowledge. If something is unclear, say 'unknown'. Return only the list."

Show both outputs. The vague one usually gives confident, generic advice and may state things about the product as fact. The structured one usually asks for what only research or the business can answer. Ask: which would you trust, and why? Do not explain yet; the next phase names what they just saw.

---

### Phase 2 — Terms in Action, and Data Safety (21 min)

**Terms in action (6 min).** The definitions are in the Week 1 brief. Do not read them out. Link each to the demo: the case card was the **context**; "use only the case card" was **grounding**; the confident advice from the vague instruction was a **hallucination** risk; "unknown" is why the structured answer helped. Then two quick points that students rarely read: the **context window** (give only the sections a step needs, because long and messy material blurs) and the **agent** (an AI coding tool takes several steps itself, so check the files it changed, not only its reply). **An AI that is allowed to say "unknown" invents less than one that feels obliged to fill every gap.**

**Activity 1 (5 min)** follows; see Activities.

**What you put in: data safety (10 min).** Everything so far was about what comes out. This is about what goes in. This is practical guidance, not legal advice; your company's policy and local law decide.

**Why it matters.** PRDs, unreleased designs, user research with names in it, client files and financial figures are often confidential or under an NDA. Many companies restrict which AI tools staff may use. In Vietnam, personal data is governed by the Law on Personal Data Protection (Law 91/2025/QH15, in force since 1 January 2026), guided by Decree 356/2025/ND-CP (law-firm summaries, for example [KPMG Vietnam](https://kpmg.com/vn/en/home/insights/2025/06/vietnam-new-personal-data-protection-law.html); check the current text or ask your company). Names, emails, phone numbers and recordings of users are personal data.

**What happens to what you paste depends on the tool and the plan.** Reports from 2026 say that on consumer plans of the main AI chat tools, conversations may be used to improve the models unless you turn that off, while business and enterprise plans usually do not train on your data by default ([summary of tool policies, 2026](https://theaicareerlab.com/blog/does-ai-train-on-your-data)). Settings change, so read the data controls of the tool you use. **Do not assume it is private.**

**Sort what you paste into three kinds:**

| Kind | Examples | Rule |
|---|---|---|
| **Safe**: public facts, your own thinking, fictional cases | A competitor's public pricing page, your notes on a public app, the course case card | Fine in any tool you are comfortable with |
| **Ask first**: internal but not sensitive | Internal process notes, non-public research summaries without names | Only in a tool your company has approved |
| **Never in a public tool**: personal data, unreleased plans, finances, NDA material | Interview transcripts with names, customer lists, an unreleased spec, screenshots of a live admin dashboard | Do not paste. Anonymise first, use an approved tool, or leave it out |

**Four habits before you paste:** (1) check the policy; if there is none, ask, and when in doubt do not paste; (2) sort the material; (3) remove identifiers first, with find and replace on your own computer, not by asking the AI, because that already sends the data (anonymising is not foolproof); (4) keep confidential files out of the tool's folder, because an AI coding tool or agent reads the whole project folder. Also: whether AI output can be used in client work, and who owns it, depends on your company and country; say where AI was used in the case log.

**Sorting exercise (pairs, 3 min).** Six cards: (1) a competitor's public pricing page, (2) an interview transcript with participant names, (3) your notes on a public app you use, (4) an unreleased feature spec, (5) a customer email list, (6) a screenshot of your company's admin dashboard. Expected: 1 and 3 safe; 2, 4, 5 and 6 never in a public tool (2 can become safe after anonymising; 6 depends on what is visible). Discuss any disagreement.

**Output:** a first version of `00-context/data-rules.md`, three lines in the student's own words: what I may paste, what I will not paste, which tool I use for what.

---

### Phase 3 — Files and Folders an AI Tool Can Work With (10 min)

The detail is in the Week 1 brief; use class time on what students get wrong.

**Markdown and HTML (3 min).** Markdown (`.md`) is the working document, plain text with simple marks, what AI tools read and write best. HTML is the presentation, what a browser draws; an AI-built prototype is an HTML file, and so is the hub. You keep the Markdown; the AI builds the page when a stakeholder needs to read it.

**The case folder, kept local (4 min).** Show the layout. A plain local folder, not a cloud document: an AI coding tool opens the whole folder as its project and reads everything in it, and cloud-sync folders can misbehave mid-write. A messy folder gives messy output.

```
[case-name]/
├── 00-context/          the context pack: pasted into AI steps first
│   ├── product-and-users.md
│   ├── principle-checks.md          (written in a later lesson)
│   ├── design-system-notes.md       (added in a later lesson)
│   ├── accessibility-rules.md
│   ├── data-rules.md
│   └── glossary.md                  (optional)
├── 01-discover/         one working file per activity, plus a sources/ folder
├── 02-define/           problem-brief.md
├── 03-develop/          options, alignment check, prototype/
├── 04-deliver/          test plan, findings, handoff
├── hub/                 the Experience Hub: one HTML page per activity
└── case-log.md          one line per decision, and why
```

**One working file per activity (3 min).** Each activity fills one Markdown file, section by section. Two rules keep it safe: (1) **the AI returns only its own section,** and you paste it in, so it cannot silently rewrite settled work; (2) **keep the AI's draft and your checked version as separate sections,** because the gap is your error rate. And one habit: **before you retype your project from memory, find the saved file and attach it.**

---

### Phase 4 — Build Your Case Folder (25 min)

This is Activity 2. Students work in breakout rooms of 3 to 4 while the instructor circulates and coaches.

---

### Phase 5 — What Comes Next, the Hub, and Sharing (8 min)

**The series in one picture (2 min).** Show the stage map: Discover, Define, Develop, Deliver. Each stage's output is the next stage's input. A gate decides whether the work moves on, and at each stage there is something to agree with the PO and the business. We start from a business question, not a received brief.

**The Experience Hub (2 min).** Every output goes into one hub, a small website of linked pages on your own computer, and the finished hub is the final report of the series. Show the empty hub in a browser. Each lesson adds a page. At the end, a reader can start from any design decision and reach the need, hypothesis, principle and test behind it.

**Sharing it (2 min).** **The hub is private by default:** it lives in your case folder and nobody can see it unless you send it. To show a stakeholder, export the Overview and key pages to PDF, or send the hub folder zipped. Only if your case is free to share (a course case, or a cleaned-up version of your work) can you publish it as a live link on GitHub: the optional homework and the publishing guide cover it. **If you publish, you host it and you are responsible for it.** Free GitHub Pages needs a public repository, which is why real work stays private.

**Close (2 min).** Ask two or three students: which term will you now explain differently? Then the closing thought:

> The tools will keep changing. The way of working does not: give the AI a clear input, make it show where each claim comes from, check it, and decide yourself.

---

## Activities

### 🗣️ Activity 1 — Explain It to a Teammate
**Type:** In-class · Pairs
**Time:** 5 min
**Format:** Pairs, terminology cards

**What it is:**
Students turn three terms into their own words, with an example from their own case. The output is the optional `glossary.md` of their context pack.

**Instructions for students:**
1. **(4 min)** Take three cards each. Explain each term to your partner in one sentence, with an example from your own case. Your partner asks one question: "What would you do differently because of that?"
2. **(1 min)** Write the agreed sentences in `glossary.md`.

**Facilitator watch-fors:**
- Definitions copied word for word. Push for their own example.
- Mixing up "context" and "context window": "which is what you give it, and which is its limit?"
- Terms they say they know but cannot use in a sentence about their own work.

**Output:** a draft `glossary.md` (optional, finished as homework if useful).

---

### 🔧 Activity 2 — Build Your Case Folder
**Type:** In-class · Hands-on, own laptop
**Time:** 25 min
**Format:** Solo, in breakout rooms of 3 to 4

**What it is:**
Students set up the infrastructure the whole series runs on, for their own case, and test it with one instruction like the one in the demo.

**Setup (before class):**
- The case folder template and the empty hub template folder available to every student.
- An AI tool the student's company allows. If none, the course case card stands in for the case in step 4.
- The instructor's own case folder ready to share.

**Instructions for students:**

1. **(4 min) Create the case folder.** One folder for your case with the layout from Phase 3. Build the subfolders. Name it after your case, lowercase with hyphens.
2. **(8 min) Start the context pack.** In `00-context/`, write a first version of `product-and-users.md` (what the product is, who uses it, their main job; half a page, anonymised) and `accessibility-rules.md` (the requirements you must meet; a few lines). Bring in `data-rules.md` from the data safety exercise.
3. **(3 min) Add the hub.** Copy the empty hub template folder into `hub/`. Open its `index.html` in a browser. You should see the Overview page with example data. Do not edit it yet.
4. **(10 min) Run one instruction against a saved file.** Attach `product-and-users.md` to your AI chat tool and use:

   > *"Here is the context for my design case. Use only this file. List the five most important things you would need to know about this product and its users that are NOT in the file, and say why each matters. Do not guess or fill gaps from general knowledge. If something is unclear, say 'unknown'. Return only the list."*

   Read the answer critically. Which questions are useful, which generic, which would you have found yourself? Save the useful ones in `00-context/open-questions.md`.

**Facilitator watch-fors:**
- Real subfolders, not one empty folder.
- Students who retype a project summary from memory instead of attaching the file.
- Coaching question in step 4: "What would you correct before you'd use this answer?"
- Anything confidential in the file: stop and anonymise first.
- A blank hub: usually the pages were moved without the CSS and scripts beside them. A box at the top of the page now names most setup mistakes.

---

## AI in Practice

### 🤖 Try this instruction

> *"I'm a UX designer working on [your case in one or two sentences]. Here is my context file: [attach product-and-users.md]. Using only this file, write the instruction I should use to ask you to [the specific task]. Then critique your own instruction: what is still ambiguous, what could you answer by guessing, and what should I add so you can say 'unknown' instead?"*

### ⚖️ Ethics consideration

AI tools reflect the patterns in their training data, which skews Western and English-language. For Vietnamese or Southeast Asian users, ask whether the suggestions match your users' mental models, not only whether the output looks polished. And remember the other direction: what you give the tool can be kept, so apply your data rules every time.

---

## Assessment

### Quick knowledge check

Run verbally at the end of Phase 3 (2 min):

1. What is the difference between AI-assisted and AI-generated?
2. What is a context window, and what should you do when your material is long?
3. Why should you allow an AI to answer "unknown"?
4. What does an agent do that a chat reply does not, and what should you check afterwards?
5. Name two things you would not paste into a public AI tool, and what you would do before pasting an interview transcript.
6. Why is your hub private by default, and when can you publish it?

---

## Homework (up to 60 minutes)

### Assignment 1 — Your Case Folder (required, about 35 min)
**Due:** Before the next lesson

If you finished Activity 2, most of this is finishing and tidying.

- Case folder complete with the standard layout
- `product-and-users.md` finished (one page): the product, the users, their main job, what success might look like, and what you do not know
- `accessibility-rules.md` and `data-rules.md` (three lines) finished
- The empty hub copied into `hub/`
- `glossary.md` (optional)

Submit: the folder tree (a screenshot) and `product-and-users.md` to the instructor for feedback. Anonymise anything confidential first.

**What the instructor is looking for:** a real structure; a `product-and-users.md` specific enough that a stranger could picture the users; data rules in the student's own words.

### Assignment 2 — Share Your Hub (optional, about 25 min)
**Due:** Before the next lesson, if you have time

Choose one:
- **(a) Private.** Export the hub's Overview page to PDF, and open the zipped hub folder on another device. This is how you would send it to a stakeholder.
- **(b) Public, if the case is free to share.** Follow the publishing guide (`publish-guide.md`): create a free GitHub account, create a public repository, upload the contents of `hub/`, turn on GitHub Pages, and open the link in a private browser window. You host it and you are responsible for it.

If you have no time, skip it. The next live session does not depend on it.

---

## Further Resources

- **[Designer Fund and Foundation Capital, AI + Design 2026](https://designerfund.com/blog/ai-in-design-2026)**: the adoption and role-blurring figures.
- **[Figma, State of the Designer 2026](https://www.figma.com/reports/state-of-the-designer-2026/)**: the split between "better" and "worse".
- **[Figma, Design systems, AI and MCP](https://www.figma.com/blog/design-systems-ai-mcp/)**: connectors and reusable instruction files for design work.
- **[NN/g, CARE: Structure for Crafting AI Prompts](https://www.nngroup.com/articles/careful-prompts/)**: a prompting frame; the structured demo instruction follows it.
- **[NN/g, Using AI for UX Work: Study Guide](https://www.nngroup.com/articles/ai-work-study-guide/)**: the best index for going further.

---

## Connection to Curriculum

| Lesson | Role |
|---|---|
| **This lesson** | The shared vocabulary, the data rules, the case folder, the empty hub, and the AI-assisted stance |
| Shape the Brief with Your PO | First use of the case folder; start from the business question and agree the scope |
| Turn Research into Insights You Can Trust | One working file per activity and the "unknown" rule, first on real user quotes and then on competitors |
| Frame the Problem Worth Solving | Writes the principle checks into `00-context` and fills the brief page of the hub |
| Explore Ideas and Pick a Direction, Build Your First Prototype, Refine and Check Your Design | Add the design system notes to `00-context` and the prototype to the hub; "Refine and check your design" closes with the alignment check, which uses the hub's links and warnings |
| Test with Real Users, Hand Off and Measure Success | Fill the findings and handoff pages |
| Capstone | Finishes the hub as the final report |

---

## Week 1 brief (the one-page pre-read, about 10 minutes)

**Ten terms.** Each: what it is, and what you do about it.

| Term | What it is | What you do about it |
|---|---|---|
| **AI chat tool** | You write, it replies. Good for synthesis, ideation, writing | Go deep with one tool before trying many |
| **AI coding tool** | Reads and writes files in your project folder; builds working prototypes | Give it your flow and design system |
| **Context** | Everything it can see now: your instruction, pasted text, attached files, earlier messages | Put the right material in; it knows nothing else about your project |
| **Context window** | The limit on how much it can hold at once; long, messy material blurs | Give only the sections a step needs |
| **Grounding** | Tying the answer to material you supply, not its general knowledge | "Use only the material below. Where does each claim come from?" |
| **Hallucination** | A confident answer that is invented: a competitor that does not exist, a quote nobody said | Ask for a source for each claim, and allow it to answer "unknown" |
| **Agent** | A tool that takes several steps itself: reads files, edits, runs things, reports back | Check the files it changed, not only its reply |
| **Connector (MCP)** | A standard way to let an AI tool read another app, such as your design file | Know what it can see and change before you connect it |
| **Reusable instructions** (skills, rules files, project memory) | A saved instruction, standing project rules, or saved project context | Say it once and reuse it |
| **AI-assisted vs AI-generated** | AI-generated: the AI decided. AI-assisted: you decided, it assembled | AI drafts. You verify. You decide |

In passing: a **model** is the engine behind a tool, a **prompt** is what you give it, and **in-tool AI features** are AI inside your design tool.

**Files in three lines.** Markdown (`.md`) is plain text with simple marks (`## Heading`, `**bold**`, `-` lists, `|` tables); AI tools read and write it best. HTML is what a browser draws; prototypes and the hub are HTML. A plain local folder is a folder on your own computer, not a cloud document; keep your case there while an AI tool writes files.

**The case folder** is the layout in Phase 3: a `00-context` folder first, one folder per stage, a `hub/` folder, and a `case-log.md`.

**Reuse, don't retype.** A new AI conversation knows nothing about your project. Before you describe it from memory, attach the saved file. A good instruction names the material to use, asks for one task, says "use only this, give a source for each claim, answer 'unknown' if it does not say, return only your section", and shows the format you want back.

**Before class:** choose your case (your own, anonymised), and find out your company's rules on AI tools.

---

*Created by Winnie Nguyen · AI Design Workflow · Last updated October 2026*
