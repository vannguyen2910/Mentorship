# 03_Mentoring

Folders follow the teach workflow: plan, build, teach, follow up, show.

| Folder | Stage | What lives here |
|---|---|---|
| `_inbox/` | Capture | Raw drops, triaged then cleared |
| `source/` | Capture | Raw inputs and archive (gitignored). Icon packs in `_asset-packs/` |
| `library/` | Plan + build | Lessons by stage, frameworks, guides, slides |
| `programs/` | Teach | Online course, Training Hub site, assessment tool |
| `mentees/` | Follow up (private) | One folder per mentee: plan, sessions, slides, transcripts, assessments, homework. Also `training-log.md` |
| `showcase/` | Show | `public/`, `private/`, `testimonials.md` |
| `business/` | Run | Services and pricing, lead tracker, CV and bios, social content |
| `_system/` | Support | Rules, templates, slide design system, scripts |
| `docs/` | Publish | Generated website (served by GitHub Pages). Never edit by hand: `python3 _system/scripts/build-home.py` rewrites it |

Private by `.gitignore`: `source/`, `mentees/`, `business/`, `showcase/private/`, `showcase/testimonials.md`, `programs/assessment-tool/`.
