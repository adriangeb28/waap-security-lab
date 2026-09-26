import json
import math
from collections import Counter
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "logs" / "traffic_normal.jsonl"
OUT = ROOT / "logs" / "features_normal.csv"

def entropy(text: str) -> float:
    if not text:
        return 0.0
    counts = Counter(text)
    n = len(text)
    return -sum((c / n) * math.log2(c / n) for c in counts.values())

rows = []
with SRC.open(encoding="utf-8") as f:
    for line in f:
        item = json.loads(line)
        url = item.get("url", "")
        body = item.get("body", "")
        params = item.get("params", {})
        text = url + body
        rows.append({
            "url_len": len(url),
            "body_len": len(body),
            "entropy": entropy(text),
            "param_count": len(params),
            "special_count": sum(text.count(ch) for ch in "'\";()<>%$"),
            "requests_window": 1,
        })

pd.DataFrame(rows).to_csv(OUT, index=False)
print(f"Features escritas en {OUT}")
