#!/usr/bin/env python3
import sys
import json

event = json.loads(sys.stdin.read())
entry = event.get("entry", {})
tags = list(entry.get("tags", []))
source_app = entry.get("source_app", "").lower()

# Add tags based on source application
if "code" in source_app or "cursor" in source_app:
    tags.append("dev")
elif "chrome" in source_app or "firefox" in source_app:
    tags.append("web")
elif "slack" in source_app or "teams" in source_app:
    tags.append("communication")
elif "outlook" in source_app:
    tags.append("email")

entry["tags"] = list(set(tags))
event["entry"] = entry
print(json.dumps(event))
