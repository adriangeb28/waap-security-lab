import json
import random
from pathlib import Path

OUT = Path(__file__).resolve().parents[2] / "logs" / "traffic_normal.jsonl"
OUT.parent.mkdir(parents=True, exist_ok=True)

paths = ["/", "/rest/products/search", "/api/Products/1", "/#/search?q=apple"]
methods = ["GET", "GET", "GET", "POST"]

with OUT.open("w", encoding="utf-8") as f:
    for _ in range(500):
        item = {
            "method": random.choice(methods),
            "url": random.choice(paths),
            "body": "",
            "params": {"q": random.choice(["apple", "phone", "book", ""])}
        }
        f.write(json.dumps(item) + "\n")

print(f"Tráfico sintético generado en {OUT}. Para el informe final, sustituirlo por tráfico observado en el laboratorio.")
