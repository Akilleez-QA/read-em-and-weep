#!/usr/bin/env bash
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
: "${DEPENDENCY_ROOT:?Set to existing pinned Mathlib (4.19) or Vermilion (4.33) checkout}"
cd "$DEPENDENCY_ROOT"
[[ "$(git rev-parse HEAD)" == "1a56a4f38cbb126b7d73b04207e9c6fda9f179bf" ]] || { echo "Wrong dependency revision" >&2; exit 2; }
[[ "$(lake env lean --version)" == "Lean (version 4.33.0,"* ]] || { echo "Wrong Lean version" >&2; exit 2; }
export LEAN_PATH="$HERE${LEAN_PATH:+:$LEAN_PATH}"
lake env lean "$HERE/ResidueBridge.lean" --root="$HERE" -o "$HERE/ResidueBridge.olean"
lake env lean "$HERE/AccumulationBound.lean" --root="$HERE" -o "$HERE/AccumulationBound.olean"
lake env lean "$HERE/audit/AuditChecks.lean" --root="$HERE" -o "$HERE/audit/AuditChecks.olean"
