# -*- coding: utf-8 -*-
"""追加来源记录到 _sources_raw.jsonl（每行一个 JSON 对象）。用法：
python tools/appendsrc.py <<'EOF'
{"id":"B001", ...}
{"id":"B002", ...}
EOF
"""
import sys, json, pathlib

raw = sys.stdin.read()
path = pathlib.Path("_sources_raw.jsonl")
added = 0
with path.open("a", encoding="utf-8") as f:
    for line in raw.splitlines():
        line = line.strip()
        if not line:
            continue
        obj = json.loads(line)
        f.write(json.dumps(obj, ensure_ascii=False) + "\n")
        added += 1
print(f"appended {added}")
