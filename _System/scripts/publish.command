#!/bin/bash
# Double-click to publish the site: builds, shows the mentee health check and what changed, then commits and pushes
# ONLY after you confirm. Run with --dry-run to stop before committing.
#
# Publishes only: docs/ (the generated site) and _system/scripts/ (the generator). Anything else you have
# changed (library/, programs/, ...) is listed but left alone. mentees/ is git-ignored and never published;
# slides and homework are copied into docs/assets/mentees/ by the build.

set -u
cd "$(dirname "$0")/../.." || exit 1
DRY=0; [ "${1:-}" = "--dry-run" ] && DRY=1
PATHS=(docs _system/scripts)
LIMIT_MB=50

echo "== 1/4  Build =="
python3 -u _system/scripts/build-home.py || { echo "Build failed. Nothing was committed."; read -rp "Press Enter to close"; exit 1; }

echo; echo "== 2/4  What would be published =="
git add -N "${PATHS[@]}" 2>/dev/null
CHANGED=$(git -c core.quotepath=false status --porcelain -z -- "${PATHS[@]}" | tr '\0' '\n' | sed 's/^...//' | grep -v '^$')
if [ -z "$CHANGED" ]; then echo "Nothing to publish: the site is already up to date."; [ $DRY = 0 ] && read -rp "Press Enter to close"; exit 0; fi
git diff --stat -- "${PATHS[@]}" | tail -1
echo "$CHANGED" | awk -F/ '{print "  " $1 "/" $2 "/" $3}' | sort | uniq -c | sort -rn | head -12

# safety: private material must never go out
BAD=$( { echo "$CHANGED" | grep -E '^mentees/'; echo "$CHANGED" | grep -Ei '(^|/)(transcripts|assessments)/|session-[0-9]+-.*\.md$|\.srt$|coaching plan'; } || true)
if [ -n "$BAD" ]; then echo; echo "STOP: private-looking files are in the change set:"; echo "$BAD" | head; read -rp "Press Enter to close"; exit 1; fi
BIG=$(echo "$CHANGED" | while IFS= read -r f; do [ -f "$f" ] && [ "$(du -m "$f" | cut -f1)" -ge $LIMIT_MB ] && echo "$f"; done)
if [ -n "$BIG" ]; then echo; echo "STOP: files of ${LIMIT_MB} MB or more (GitHub rejects 100 MB, warns at 50 MB):"; echo "$BIG"; read -rp "Press Enter to close"; exit 1; fi

NEWFILES=$(echo "$CHANGED" | grep '^docs/assets/mentees/' | sed 's#^docs/assets/mentees/##')
if [ -n "$NEWFILES" ]; then echo; echo "Mentee files going public (slides, homework, loose files). Check none are private:"; echo "$NEWFILES" | sed 's/^/    /' | head -40; fi

OTHER=$(git status --porcelain | grep -v -E "^.. (docs|_system/scripts)/" | wc -l | tr -d ' ')
[ "$OTHER" != "0" ] && echo "  (not included: $OTHER other changed paths outside docs/ and _system/scripts/)"

if [ $DRY = 1 ]; then echo; echo "Dry run: stopping before commit."; exit 0; fi

echo; echo "== 3/4  Commit =="
read -rp "Commit message [Update mentorship site $(date +%Y-%m-%d)]: " MSG
MSG=${MSG:-"Update mentorship site $(date +%Y-%m-%d)"}
read -rp "Commit and push to $(git remote get-url origin) ($(git branch --show-current))? [y/N] " OK
[ "$OK" = "y" ] || [ "$OK" = "Y" ] || { echo "Cancelled. Nothing was committed."; git reset -q -- "${PATHS[@]}"; read -rp "Press Enter to close"; exit 0; }

git add -- "${PATHS[@]}" && git commit -m "$MSG" || { read -rp "Commit failed. Press Enter to close"; exit 1; }

echo; echo "== 4/4  Push =="
git push origin "$(git branch --show-current)" && {
  USER_REPO=$(git remote get-url origin | sed -E 's#.*github.com[:/]([^/]+)/([^/.]+)(\.git)?#\1 \2#')
  set -- $USER_REPO
  echo; echo "Pushed. GitHub Pages usually updates in a minute or two:"; echo "  https://$1.github.io/$2/"
}
read -rp "Press Enter to close"
