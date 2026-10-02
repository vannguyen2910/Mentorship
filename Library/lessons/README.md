# Lessons

Full lesson plans for class sessions and private training, organised into folders by design thinking stage so you can find what fits where.

Each file covers one session: run-of-show, activities, AI in Practice, and assessment.

**Naming:** `lesson-[topic].md`
**Template:** Copy `_System/templates/_template-lesson.md` to get started.

## Standard layout inside each lesson

```
<lesson>/
  materials/   source of truth: <slug>-lesson.md + <slug>-slide-outline.md (+ brainstorm, build prompt)
  slides/      built decks only (html, pdf)
  assets/      images used by the lesson or deck
  _archive/    superseded drafts
```

Mentee homework is not stored here. It lives in `Mentees/<name>/homework/<lesson>/`.

## Folder structure

- `00-foundation/` — cross-cutting lessons, taught early and referenced throughout (not tied to one stage)
- `01-discover/`
- `02-define/`
- `03-develop/`
- `04-deliver/`

Topic folders keep their original names inside their stage folder (e.g. `01-discover/desk-research/`).

`leader-level/` holds `change-management/` and `estimating-design-effort/` — leader/senior-manager track content, a different curriculum tier from the discover/define/develop/deliver flow above, not an omission from it. Neither has a finished lesson.md yet.

`02-define/` holds two separate sessions in two folders: `synthesis-problem-definition-in-ux/` is the UX Class treatment of synthesis mechanics, `problem-definition-strategy/` is the Senior/Lead session that follows Customer Understanding. Same stage, different sessions, so they are not level variants of one topic and do not share a folder.

`problem-understanding/` was a superseded early draft of the Customer Understanding session (same content now built out in `01-discover/customer-understanding/`) — moved to `Library/_to_delete/problem-understanding/` pending permanent deletion.

## Files in this folder

| File | Topic | Program | Level | Status |
|---|---|---|---|---|
| `00-foundation/design-thinking/materials/design-thinking-lesson.md` | Design Thinking for UX Designer | UX Class | — | ✅ Ready |
| `00-foundation/ai-workflow-for-ux-designers/materials/ai-workflow-for-ux-designers-lesson.md` | Set Up Your AI Workflow | UX Class | — | 🚧 Draft |
| `00-foundation/mental-models-in-ux-design/slides/mental-models-in-ux-design.html` | Mental Models in UX Design | UX Class | — | ✅ Ready |
| `01-discover/desk-research/materials/desk-research-lesson.md` | Desk Research | Private Training | Mid | ✅ Ready |
| `01-discover/customer-understanding/materials/customer-understanding-lesson.md` | Customer Understanding | UX Class | Junior | ✅ Ready |
| `01-discover/customer-understanding/materials/customer-understanding-senior-lesson.md` | Customer Understanding | Private Training | Senior / Lead | ✅ Ready |
| `02-define/synthesis-problem-definition-in-ux/slides/synthesis-problem-definition-in-ux.html` | Synthesis & Problem Definition | UX Class | — | ✅ Ready |
| `02-define/problem-definition-strategy/materials/problem-definition-strategy-lesson.md` | Problem Definition & Strategy | Private Training | Senior / Lead | ✅ Ready |
| `03-develop/information-architecture/slides/information-architecture.html` | Information Architecture | UX Mentoring | — | ✅ Ready |
| `03-develop/ui-fundamentals/materials/ui-fundamentals-lesson.md` | UI Fundamentals (Judging design decisions you didn't make) | Standalone | Junior | 🚧 Draft |
| `03-develop/design-framework/materials/design-framework-lesson.md` | Design Once. Use Everywhere. (Atomic Design) | UX Class | Intermediate | 🚧 Draft |
| `03-develop/ai-prototype-development/materials/ai-prototype-development-lesson.md` | AI Prototype Development | UX Class | Intermediate | 🚧 Draft |
| `03-develop/develop-solutions-ideate/materials/develop-solutions-ideate-lesson.md` | Develop Solutions & Ideate | UX Class / Private | — | ✅ Ready |
| `03-develop/interaction-design-user-flows/materials/interaction-design-user-flows-lesson.md` | Interaction Design & User Flows | UX Class / Private | Intermediate | ✅ Ready |
| `04-deliver/solution-validation-user-testing/materials/solution-validation-user-testing-lesson.md` | Solution Validation & User Testing | UX Class | Intermediate | ✅ Ready |

**Reading by level:** for a topic taught at more than one level, the level version lives in the same topic folder, filename-suffixed (e.g. `customer-understanding-lesson.md` for Junior vs `customer-understanding-senior-lesson.md` for Senior/Lead) — same materials folder, so both versions of a topic stay visible side by side.

**Status:** 🚧 Draft means the file's own frontmatter has `draft: true` — content exists but hasn't been finalised for delivery.

## Track build status

`track-senior-lead.md` maps the eight-session Roadmap to Senior/Lead curriculum (defined in `Business/services/service-catalog.md`) against what is actually built, with the gaps and the recommended build order. Three of eight sessions exist at senior level today.

## The Library site

`Library/index.html` (with `Library/library-data.js`) is a browsable site over these same lessons, with a stage filter, search, tags, and cross-references between sessions — open it locally for the fuller picture rather than reading this table.

## Also in the library (status not yet recorded here)

| File | Topic | Stage |
|---|---|---|
| `01-discover/evaluate-current-experience/materials/evaluate-current-experience-lesson.md` | Evaluate Current Experience | Discover |
| `03-develop/interaction-design-user-flows/materials/interaction-design-user-flows-lesson.md` | Interaction Design & User Flows | Develop |
| `03-develop/ai-prototype-development/materials/ai-prototype-development-lesson.md` | AI Prototype Development | Develop |
| `04-deliver/solution-validation-user-testing/materials/solution-validation-user-testing-lesson.md` | Solution Validation & User Testing | Deliver |
