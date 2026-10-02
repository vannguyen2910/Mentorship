---
title: "Lesson 0: Program Introduction"
subtitle: "Systematic AI Prototyping — opening orientation, delivered inside Session 1"
type: lesson
program: private-training
tags: [prototype, AI, orientation, curriculum]
level: intermediate
date: 2026-09-13
draft: true
slides: "lesson-0-slide-outline.md"
previous-session: ""
next-session: "Lesson 1: Project Setup & the Pattern-First Method"
---

> **Not a separate session — this is the first part of Session 1.** Session 1 runs Lesson 0 and Lesson 1 back to back, in one sitting, the same day: this orientation opens it, then Lesson 1's content runs immediately after. It isn't a fifth session added on top of the 4 the coaching plan commits to — it's the first slice of Session 1's time, before the folder-setup work begins. Keep it brief: the point is shared clarity before that work starts, not a session of its own.

## Overview

This is a 4-lesson arc that takes a designer from prototyping screen-by-screen — in whatever tool is in front of them — to running a systematic, pattern-first method for AI-assisted prototyping. Define the system once (component inventory + interaction pattern), save it as reference files an AI coding tool reads directly, then let AI build and scale from it.

**This lesson assumes an existing design system.** The student should arrive with their own component library (tokens + components in Figma or similar) already built — this arc is about *prototyping from* a system, not building one. If a student doesn't have one yet, hand them a starter system before Lesson 1; don't spend lesson time building one from scratch.

**Not portfolio-specific.** The method applies to any real prototype — a portfolio case study, client work, or a product idea. Frame the anchor project around whatever the student is actually there to build.

---

## Curriculum Summary

The four lessons build on each other and are delivered in order, one per week — each one builds directly on the artifact the last one produced, nothing is a disconnected exercise.

| Lesson | Focus | You'll walk away with |
|---|---|---|
| 1 | Project Setup & the Pattern-First Method | A scalable project folder — including the persistent context file — and your Design Pattern (tokens, component inventory, template) named and ready to build from |
| 2 | Interaction Pattern, Build & Editing Craft | A synced token file, a corrected component inventory, an interaction pattern, and working screens — built from saved artifacts instead of retyped prompts |
| 3 | Stitching the Journey & Presenting the Work | One demoable, navigable journey, plus a draft outline for presenting it |
| 4 | Publish — Git & GitHub for Non-Technical Designers | The prototype live at a real, self-updating URL |

---

## Learning Objectives

By the end of this arc, students will be able to:

1. **Organise** a prototype project folder that scales, including a persistent context file an AI coding tool reads automatically
2. **Explain** why pattern-first prototyping is faster and more consistent than screen-by-screen, and why artifacts (not repeated prompting) should carry that consistency
3. **Generate** a component inventory and interaction pattern from an existing design system, saved as reusable reference files
4. **Build** a working, browser-viewable prototype from those files using an AI coding tool
5. **Stitch** multiple screens into one demoable journey and present the process behind it
6. **Publish** the finished prototype to a live URL via Git/GitHub, independent of any design tool account

---

## Materials Needed

- Student's own design system (Figma file with tokens + components) — bring to Lesson 1
- One AI tool for prototyping, picked from the comparison below (primary tool for the whole arc)
- A second AI tool, for the Lesson 2 comparison (optional but recommended)
- A GitHub account and GitHub Desktop, installed *before* Lesson 4 — don't let install friction eat lesson time
- The prompt reference in each lesson file's own Prompt & Reference section

### Choosing an AI Tool

| Tool | Type | Design-system support | Strengths | Weaknesses | Use when |
|---|---|---|---|---|---|
| Cursor / Claude Code / Windsurf | AI coding tool | Highest — connects via Figma MCP, reads variables, tokens, components, and variants directly | Most detail on the design system via MCP | Requires manual MCP setup; no visual design UI | Already comfortable in a code editor, need the tightest adherence to the design system |
| Claude Design | AI design tool | Highest — builds the design system from the design file itself during onboarding, then reuses it for every later prototype | No MCP setup needed; generates a visual prototype quickly from text or an image; edits directly via comments | Not as deep as a code editor for complex logic | Want the design system to self-sync with no config; need a fast prototype or deck |
| Bolt / Replit | AI coding tool | High — reads Figma metadata directly, including real tokens and components | Ships with frontend, backend, and database; high fidelity | Can be more complex than a simple MVP needs | Full-stack app that still needs high fidelity to the original design |
| Figma Make | AI design tool | Medium — connects directly to Figma but doesn't yet expose tokens clearly | High visual fidelity, easiest to use since it lives inside Figma | Tokens not clearly exposed; less flexible outside Figma | Design already exists in Figma, just need to add interactivity |
| Lovable | AI coding tool | Low — relies on a written brand description, doesn't extract tokens directly | Generates a complete app from a written description | Can drift from the original design | MVP or small production app, no interest in touching code |

*Snapshot as of September 2026 — the market moves fast, so choose by category and support level, not by clinging to a specific tool name.*

**Sync note (2026-09-14), deliberate exception:** this table names specific tools, per Winnie's direct request — an intentional exception to the "no specific AI tool names" convention in `CLAUDE.md`, scoped to this table only. Matches the same exception already applied to `Online Course/AI Prototype Development/Section 1 - Giới Thiệu/learning/section 1-slide-outline.md`.

---

*Created by Winnie Nguyen · Private Training · Last updated September 2026*
