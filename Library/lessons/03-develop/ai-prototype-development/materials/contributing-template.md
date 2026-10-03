# Contributing to <repo name>

One page. Your rules for this project — for you and for your AI tool. Copy it into your project, fill in the blanks, and push it. If something here is wrong, fix it with a pull request.

## The rules
1. **Never work directly on `main`.** It is your live site. One branch per idea.
2. **Pull before you start** each session, especially if you use two laptops or your AI tool pushes for you.
3. **Branch names:** `area/short-description` — e.g. `tokens/update-spacing`, `components/button-states`.
4. **Commit notes** say what changed and why, in one line.
5. **This project is public.** Never add passwords, keys or `.env` files. Git history is permanent.

## Opening a pull request
Every pull request has:
- A short summary of what changed and why
- A screenshot, if the UI changed
- Which tokens or components you touched

## Review and merge
- **Read your own changes** on the pull request as if someone else wrote them, before you merge.
- Merge into `main` — your live site updates.
- Then pull, and start your next branch.
- *If you add collaborators later:* name a reviewer and an owner who merges here.

## If something breaks
Delete the branch. `main` is untouched, so your live site is fine. If two copies changed the same file, stop and decide which version stays — it's a design decision, not a tool error.

## Using an AI tool in this repo
Point it at the rules file and this file first. It must follow the tokens and components already here, must never touch `main`, and must not edit files outside the change you asked for. Read its answer, and review the changes in GitHub Desktop, before agreeing to a push.

Useful prompts (from the Lesson 4 deck):
- Check if GitHub has anything new for this project, and bring it into my folder.
- Run localhost so I can preview my work.
- Create a new branch called area/short-description and switch to it. Don't touch main.
- Show me what I've changed since my last commit, in plain language.
- Open a pull request for this branch. Write a short summary of what changed and why.
- Clone <repo URL> into a new folder and tell me what's in it. *(Set up on another laptop.)*
- Undo my last commit but keep my changes, so I can edit them again.
