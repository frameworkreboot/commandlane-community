#!/usr/bin/env python3
import sys
import json
from datetime import datetime
from pathlib import Path

event = json.loads(sys.stdin.read())
entry = event.get("entry", {})

log_file = Path.home() / ".cmdlane" / "capture.log"
with open(log_file, "a") as f:
    timestamp = datetime.now().isoformat()
    entry_type = entry.get("entry_type", "unknown")
    body = entry.get("body", "")[:50]
    f.write(f"{timestamp} | {entry_type} | {body}\n")

# Pass through unchanged
print(json.dumps(event))
