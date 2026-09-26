#!/usr/bin/env bash
set -euo pipefail
URL="http://localhost:${WAAP_PORT:-8080}"
if curl -fsS --max-time 5 "$URL" >/dev/null; then
  echo "Gate aprobado: WAAP responde en $URL"
else
  echo "Gate no aprobado: WAAP no responde en $URL" >&2
  exit 1
fi
