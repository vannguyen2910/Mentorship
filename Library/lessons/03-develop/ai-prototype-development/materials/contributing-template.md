# Contributing to <repo name>

One page. Read it before your first change. If something here is wrong or missing, open a pull request to fix this file.

## The rules
1. **Never work directly on `main`.** One branch per change.
2. **Check for new work before you start** each session (Pull).
3. **Branch names:** `area/short-description` — e.g. `tokens/update-spacing`, `components/button-states`.
4. **Commit notes** say what changed and why, in one line.
5. **This project is public.** Never add passwords, keys or `.env` files. Git history is permanent.

## Opening a pull request
Every pull request has:
- A short summary of what changed and why
- A screenshot, if the UI changed
- Which tokens or components you touched

## Review and merge
- **Reviewer:** <name> — one teammate looks it over and approves
- **Owner / merger:** <name> — merges once approved
- After the merge, everyone pulls.

## If two people changed the same file
Stop and ask who owns it. Don't pick a side just to make the warning go away — it's a design decision, not a tool error.

## Using an AI tool in this repo
Point it at the rules file and this file first. It must follow the tokens and components already here, must never touch `main`, and must not edit files outside the change you asked for. Read its answer, and review the changes in GitHub Desktop, before agreeing to a push.

Useful prompts (the same six as the Lesson 4 deck):
- Check if my teammates added anything new, and bring it into my project.
- Create a new branch called area/short-description and switch to it. Don't touch main.
- Show me what I've changed since my last commit, in plain language.
- Open a pull request for this branch. Write a short summary of what changed and why.
- Clone <repo URL> into a new folder and tell me what's in it.
- Undo my last commit but keep my changes, so I can edit them again.
