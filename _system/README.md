# _System

Everything that runs the workspace rather than the teaching content.

| Folder | Holds |
|---|---|
| `rules/` | Mentoring, workflow, automation and slide-deck rules |
| `templates/` | Blank starter files. Copy, never edit. |
| `rules/SLIDE_DECK_RULES.md` | Canonical slide deck design rules (moved from `Themes/slide-design/RULES.md`). Deck assets (`tokens.css`, `deck-stage.js`) live in each lesson's `slides/` folder |
| `commands/` | Slash commands (`/lead`, `/prep`, `/log-session`, `/nudge`, `/build-lesson`, `/closeout`, `/new-mentee`). `.claude/commands` is a symlink to this folder so Claude Code can read them |
| `scripts/` | `new-lesson.sh`, `sync-lesson.py`, `watch.sh` (run from the repo root) |

## Templates

| Template | Use for |
|---|---|
| `_template-lesson.md` | A new class session or lesson plan |
| `_template-slide-outline.md` | Slide specs paired with a lesson |
| `_template-framework.md` | A reusable UX method, tool, or guide |
| `_template-session.md` | A private training session recap |
| `_template-coaching-plan.md` | Programme kickoff, with baseline assessment |
| `_template-programme-closeout.md` | Final-session recap with baseline vs reassessment |
| `_template-showcase.md` | A student artifact for the Showcase |
| `_template-problem-brief.md` | A problem brief |
| `_template-opportunity-map.md` | An opportunity map |
| `_template-ia-decision-record.md` | An information architecture decision record |

**Workflow:** copy the file, rename it, move it to the right folder, fill it in.
