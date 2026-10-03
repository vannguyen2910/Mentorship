---
title: "Systematic AI Prototyping — Lesson 4: Publish It"
subtitle: "From a prototype on one laptop to a live URL you can safely keep changing"
type: lesson
program: private-training
tags: [prototype, AI, git, github, publishing, branching]
level: intermediate
date: 2026-09-19
draft: true
slides: "../slides/AI Prototyping - Lesson 4.html"
previous-session: "Lesson 3: Scaling the Prototype"
next-session: "Lesson 5: Beyond the Pattern (optional bonus)"
---

> **Updated 2026-10-03 (third pass) to match the built deck.** `AI Prototyping - Lesson 4.html` is presentation reality; this file and `lesson-4-slide-outline.md` were re-synced from it. The deck moved from a team-collaboration section to a **solo "Try Ideas Safely" section on the mentee's own repo**, added a localhost-preview step and a Homework slide. The filename `lesson-3-4-stub.md` is stale (it holds Lesson 4 only) — renaming it to `lesson-4-publish-it.md` means updating the README table and the outline's `lesson_file` in the same pass, recorded here and deliberately not done piecemeal.
> **Cover title: "Publish It."** A single-message statement, like Lessons 1 and 2. Subtitle: "Git and GitHub Desktop for non-technical designers."
> **Scope change from the original plan.** The presentation coaching moved here from Lesson 3 is **not in the deck**, nor are the solo practice rep, the SHOW teach-back or the simulate-a-mistake-and-recover beat. Replaced by: a localhost preview before every commit, a branch-and-self-review section, and Homework. See "Open decisions".
> **The second-tool comparison is removed from the programme** (2026-09-19), not deferred to here. Don't reintroduce it as a closing extra.
> **Speaker notes in the deck are Vietnamese**, each with a Figma-based analogy for the concept. Slide copy is English.

---

# Lesson 4: Publish It — Git & GitHub for Non-Technical Designers

**Learning Objectives**
- Understand the local-vs-published mental model: the local folder is the draft, GitHub is the published version, push is the publish button
- Use ten core words correctly — repo, clone, commit, push, pull, branch, main, pull request, merge, clash
- Set up GitHub Desktop and connect it to the same project folder organised in Lesson 1, then make a first publish
- Publish the stitched prototype to a live, self-updating URL with GitHub Pages — independent of any design-tool account
- Preview work with localhost before every commit, so only clicked-through work goes live
- Understand why every push to main changes the live site, and use a branch, a self-reviewed pull request and a merge to try ideas safely
- Write a one-page `CONTRIBUTING.md` rulebook that both the mentee and their AI tool follow
- Ask an AI tool to do the same Git work in plain language — first push, publish, pull, branch, review, undo

**What the student brings:** the stitched prototype with its triage list worked through, and a GitHub account with GitHub Desktop already installed (Lesson 3 homework — install friction shouldn't eat session time). No sandbox repo or invitation is needed any more — Section 5 runs on the mentee's own repo.

---

## Session Structure

Organised Why → What → How → Do, same convention as Lessons 1–3. Total about **90 minutes of content** under a "100 minutes" framing; the remainder is transitions and Q&A.

| # | Section | Min | Slides | Phase |
|---|---|---|---|---|
| 1 | The Local-vs-Published Mental Model | 10 | 3 | **Why / What** — local = draft, GitHub = published; ten words defined our way |
| 2 | Setup & Connect | 10 | 2 | **How** — confirm the prework, connect GitHub Desktop to the real project |
| 3 | First Publish | 20 | 4 | **Do** — preview with localhost, commit, publish repository, push origin |
| 4 | Make It Live | 15 | 3 | **Do** — GitHub Pages: settings, branch, folder, live URL |
| 5 | Try Ideas Safely | 25 | 5 | **Do** — every push goes live; branch, commit, publish branch, pull request, merge; the rulebook |
| 6 | The AI-Tool Shortcut | 10 | 4 | **How** — the same Git habits asked for in plain language |
| — | Opening, Homework, Closing | — | 4 | Cover, agenda, homework, closing checklist and exit ticket |

### 1. The Local-vs-Published Mental Model (10 min)

- Open with a real project's before and after — a plain folder, then a GitHub page with history and a live link — before explaining anything.
- **Local folder = draft. GitHub = published.** Anchor to Figma: a work-in-progress file is the draft; a prototype link sent to a client is the published version.
- A design tool's own share link depends on that account staying active; a GitHub Pages URL doesn't expire with a trial. Checkpoint: the mentee says "draft vs. published" back in their own words.
- **The ten-word glossary slide is the reference for the whole lesson** — return to it whenever a word first appears, especially Branch, Main and Pull request in Section 5.

| Word | Plain meaning | Figma analogy |
|---|---|---|
| Repo | The project's home on GitHub, with all its files and history | A project's Figma file |
| Clone | Download a copy of a project from GitHub to your laptop | Duplicate a team file into Drafts |
| Commit | A saved snapshot with a short note on what changed | Save to version history, with a clear name |
| Push | Send your commits up to GitHub | Publish your changes to the team |
| Pull | Bring the latest changes from GitHub down to your laptop | Update from a new component-library version |
| Branch | Your own copy to try changes in without touching the original | Duplicate a screen to test an idea |
| Main | The official version, and your live site; never edit it directly | The file you hand off to the client |
| Pull request | Ask for a review of your branch before it joins main; alone, you review it yourself (GitLab: Merge Request) | Re-read a screen before handoff |
| Merge | Add your approved changes into main | Move the approved version into the main file |
| Clash | Two copies changed the same thing; you choose which version stays | Two edits to the same button, different colours |

A clear commit note is the same discipline as a clear layer name — vague either one costs more later.

### 2. Setup & Connect (10 min)

- Confirm the prework in 30 seconds; the account and Desktop install were Lesson 3 homework.
- Connect GitHub Desktop to the project. **Say the Add-vs-Create distinction out loud:** the habit reaches for "Create New", which spins up a second, empty repo next to the real one — like creating a blank Figma file when the project file already exists.
- The Changes tab will list every file as new — there's no history yet. Expected, not an error.
- **Checkpoint:** Desktop open, signed in, showing the mentee's own project folder.

### 3. First Publish (20 min)

- **Local preview before publish, always.** Ask the AI tool "Run localhost so I can preview my work" — a private preview that opens only on your own computer. Run it before **every** commit, because what is committed and pushed goes on the real internet. Checkpoint: the preview is open in the browser and works.
- Step 2: open GitHub Desktop and check the right repo is selected; write a message and commit. Flag the first-commit quirk before it's asked — weeks-old finished files still read as new.
- A good commit note is specific ("Change the login button to orange"); a bad one is "fixed stuff".
- Publish repository does two things at once: creates the repo on GitHub and sends the first push. **Publish is the first time; push origin is every time after.**
- **Checkpoint:** the repo exists on GitHub and the Changes tab in Desktop is empty.

### 4. Make It Live (15 min)

- This is the payoff moment of the lesson — don't rush it.
- Repo Settings → Pages; the branch defaults to **None** until chosen, which is expected, not broken. Choose the branch and folder that hold the stitched `index.html`, then Save.
- The first deploy takes a minute or two — use the wait to preview what's next.
- **Name "self-updating" explicitly.** It is the actual objective of the lesson and easy to let pass as a footnote: push again, same URL, new content.
- **Checkpoint:** a working URL is open in the browser, showing the real prototype, not a file listing.

### 5. Try Ideas Safely (25 min)

Until now every change went straight to the live site. This section teaches the solo designer's safety net, **on the mentee's own project — no sandbox repo needed.**

1. **Frame it.** Every push to main changes the live site immediately — like editing a prototype while the client is watching. A branch is a draft page: if the idea fails, delete the branch and main is untouched. Push is "stand up, send it up"; Pull is "sit down at another machine, bring it down" — and Pull matters more with two laptops or when an AI tool pushes for you. Say aloud: **the repo is public, never push passwords or keys.**
2. **Branch before you change anything.** GitHub Desktop: Current Branch → New Branch, named for the idea (`try/new-nav`). Make the change, preview it with localhost, commit with a note on what and why, then Publish branch. **Never work directly on main.** Checkpoint: the new branch is published and visible in GitHub Desktop.
3. **Run the safe loop** on a tiny real change: **Pull → Branch → Commit → Push the branch → Pull request → Merge, then pull.**
   - *Why a pull request when you are alone:* it is the moment to read your own changes as if someone else wrote them — like reviewing a screen before handoff. AI tools can edit many files at once, so this step catches errors.
   - Merging updates the live site automatically — the payoff of the loop.
   - **Checkpoint:** the pull request is open on GitHub, was read through, and is merged.
4. **Your rules ship with the repo.** The rulebook is one page, lives in the repo as `CONTRIBUTING.md`, and is read by the mentee and their AI tool alike. **This is the rules-file idea again** — written down, not remembered. Show the template on screen rather than reading the slide aloud. Closing question: *if something breaks, what do you do?* → Delete the branch; main is untouched. Template: `contributing-template.md`.

### 6. The AI-Tool Shortcut (10 min)

Ten minutes, not a re-teach. The mentee has worked AI-tool-first since Lesson 1 — this is the same habit pointed at a new outcome: describe what you want instead of remembering button names. GitHub Desktop stays the backbone under either path.

- **First push, once per project** (right after creating the empty repo on GitHub): give the folder, the repo URL, the commit message and the branch so nothing is left to guess.
- **Everyday publish:** one plain sentence. Demo the GitHub login popup on the facilitator's own machine first so it isn't a surprise later.
- **Six more things to ask for** (two to try live, four for reference) — two to try live, four for reference. Always read the tool's answer before agreeing, especially for anything that edits or removes a commit.
- Keep tool references generic ("your AI coding tool") — this lesson works whichever tool the mentee uses.

### Homework (before the close)

Assigned just before the close so the mentee leaves with something concrete. Each task ends in a "Done when":

1. **Start a new repo** — a project not yet on GitHub: preview with localhost, create the repo, commit, publish it for the first time **on your own**, then turn on Pages. *Done when: the project has its own live URL.* (This is where the "unaided commit" promised on the closing slide actually happens.)
2. **Write your project's rules** — copy the `CONTRIBUTING.md` template, fill in branch names and commit-note style, save it in the project and push it. *Done when: the file is on GitHub.*
3. **Practice the loop solo** — new branch, one tiny change, publish the branch, open a pull request on your own repo, review it yourself, merge. *Done when: the pull request is merged.*

The mentee sends the result link or a screenshot before the next session for feedback.

### Closing

Checklist: project connected to a real GitHub repo · at least two commits pushed, one unaided · a live, self-updating URL · a pull request merged into your own repo. **Exit ticket: publish one more thing on your own this week.** This is the last session in the arc; name that plainly, then point to Lesson 5 as the optional bonus.

---

## Prompt & Reference Library

Prompts shown on slides, kept short and plain — no CARE breakdown, same decision as Lessons 2 and 3.

**Preview before every commit**
> Run localhost so I can preview my work.

**First push (once per project)**
> Push the [Project Name] folder to my new GitHub repo: https://github.com/<username>/<repo>.git — Init git if needed, commit everything as "Initial commit", and push to main.

**Everyday publish**
> Commit these changes with a short message describing what changed, and push them to GitHub.

**Six more things to ask for** (two to try live, four for reference)

| Goal | Prompt |
|---|---|
| Get the latest | Check if GitHub has anything new for this project, and bring it into my folder. |
| Start a new branch | Create a new branch called tokens/update-spacing and switch to it. Don't touch main. |
| See what changed | Show me what I've changed since my last commit, in plain language. |
| Open a pull request | Open a pull request for this branch. Write a short summary of what changed and why. |
| Set up on another laptop | Clone https://github.com/<username>/<repo>.git into a new folder and tell me what's in it. |
| Go back one step | Undo my last commit but keep my changes, so I can edit them again. |

Lesson 3's prompts live in `lesson-3-scaling-the-prototype.md`; Lesson 2's in `lesson-2-interaction-pattern-build-editing-craft.md`. The rulebook template is `contributing-template.md`.

---

## Instructor Notes

- **Every lesson follows Why → What → How → Do.** Lesson 4's Why is "a design-tool link isn't a real publish"; the What is the local-vs-published model and the ten words; the How is GitHub Desktop and the AI-tool shortcut; the Do is the first publish, the live URL and the team loop.
- **This lesson points to the existing guide for method content instead of restating it** — `Library/guides/publish-your-work-git-github-for-non-technical-designers`. Rewriting its steps here creates two sources of truth. The guide has no coverage of branches or pull requests, so Section 5 is genuinely new content.
- **Hold the line on scope.** The safe loop teaches one clean path for a solo designer. Team collaboration and merge conflicts are no longer taught here — each gets at most a sentence.
- **The rules/context file from Lessons 1 and 3 is the thread the whole arc hangs on** — artifacts over prompts, this arc's application of the Feed Forward habit from `ai-workflow-for-ux-designers`. The `CONTRIBUTING.md` slide makes the point for the mentee's own rulebook, and Homework 2 has them write it. The deck does not currently say that the mentee's own rules file ships in the repo they just published — worth saying aloud in the close.
- **Main is the live site, and the repo is public.** Anything pushed is visible to everyone and goes live on merge. No keys, tokens or `.env` files, ever.

---

## Open decisions

Places where the deck dropped something the earlier plan promised. Decide before the next delivery.

1. **Simulate a mistake and recover.** Originally "the part students actually need". The deck keeps only the "Go back one step" prompt and the "delete the branch" line. Restore a dedicated beat, or accept that?
2. **Presentation coaching.** Moved here from Lesson 3 and not in the deck. Drop it from the programme, or place it in Lesson 5?
3. **Team collaboration.** Clone, shared repos and teammate review are no longer taught. Confirm whether Lesson 5 should pick them up.
4. **Add vs. Create on the Setup slide.** Slide step 2 reads "Create a new Repo" while the notes warn against Create New. Fix the slide copy.
5. **Agenda minutes.** The slide totals 90 minutes under a "One hundred minutes" title.

---

## Connection to Curriculum

A private-training adaptation layer on top of `Library/guides/publish-your-work-git-github-for-non-technical-designers`, pointed to directly rather than restated, re-paced for 1:1 delivery. The branch-and-self-review section, the localhost preview and the AI-tool shortcut are the genuinely new content in this arc.

---

*Created by Winnie Nguyen · Private Training · Last updated October 2026*
