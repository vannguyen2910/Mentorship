# 📥 Inbox

This is a **temporary processing zone**. Nothing lives here permanently.

Drop raw files, rough notes, unstructured content, or anything you're not sure where to put.
Claude will process each item, move the source file to the right folder, and create the structured artifact in the correct location.

---

## How to use

1. Drop your file or paste your content here
2. Tell Claude: "Process my inbox" or "Process [filename]"
3. Claude will triage, brief (if a build is needed), and route — then clear the item out

## What happens to each item

| Item type | Source file moved to | Structured artifact created in |
|-----------|---------------------|-------------------------------|
| Raw lesson notes | `source/` | `library/lessons/<stage>/<name>/` |
| Rough slide content | `source/` | Brief, then `library/slides/<name>/` |
| Private session notes | `mentees/<mentee>/sessions/` | n/a |
| Mentee homework or transcript | `mentees/<mentee>/homework/` or `transcripts/` | n/a |
| Framework or guide draft | `source/` | `library/guides/` or `library/frameworks/` |
| Reusable template | `_system/templates/` | n/a |
| Student work for the showcase | `showcase/private/` | n/a |
| Business doc (pricing, CV, social post) | `business/` | n/a |
| Unsure | Ask Claude to triage | Confirmed by you |

## Rules

- **Nothing stays here permanently.** Every item must be processed and moved.
- **Do not save finished work here.** Inbox is for inputs, not outputs.
- **If you're unsure what to do with it** — drop it here and let Claude triage it (Rule WF-4 + Rule WF-6).
