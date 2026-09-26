#!/usr/bin/env set -euo pipefail
curl -fsS http://localhost:${WAAP_PORT:-8080}/health >/dev/null
echo "WAAP policy deployment gate: READI"
