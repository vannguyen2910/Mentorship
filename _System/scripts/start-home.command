#!/bin/bash
# Double-click to work on lessons with a live preview:
#   - rebuilds the Homepage whenever a lesson .md, slide deck or mentee homework file changes
#   - serves it and opens it in your browser; open pages refresh themselves after each rebuild
# Leave this window open; close it (or press Ctrl+C) to stop.
python3 -u "$(dirname "$0")/build-home.py" --serve
