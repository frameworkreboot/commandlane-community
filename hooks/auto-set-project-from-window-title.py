#!/usr/bin/env python3
import sys
import json
import re

event = json.loads(sys.stdin.read())
entry = event.get("entry", {})
title = entry.get("source_title", "")

# Extract project from VS Code title
# Format: "file.py - ProjectName - Visual Studio Code"
match = re.search(r" - ([^-]+) - (Visual Studio Code|Cursor)", title)
if match:
    project = match.group(1).strip().lower().replace(" ", "-")
    tags = list(entry.get("tags", []))
    tags.append(f"project:{project}")
    entry["tags"] = list(set(tags))
    event["entry"] = entry

print(json.dumps(event))
