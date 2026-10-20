#!/usr/bin/env bash
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
: "${DEPENDENCY_ROOT:?Set to existing pinned Mathlib (4.19) or Vermilion (4.33) checkout}"
cd "$DEPENDENCY_ROOT"
[[ "$(git rev-parse HEAD)" == "c44e0c8ee63ca166450922a373c7409c5d26b00b" ]] || { echo "Wrong dependency revision" >&2; exit 2; }
[[ "$(lake env lean --version)" == "Lean (version 4.19.0,"* ]] || { echo "Wrong Lean version" >&2; exit 2; }
export LEAN_PATH="$HERE${LEAN_PATH:+:$LEAN_PATH}"
lake env lean "$HERE/KoszulDimension.lean" --root="$HERE" -o "$HERE/KoszulDimension.olean"
lake env lean "$HERE/KoszulSlots.lean" --root="$HERE" -o "$HERE/KoszulSlots.olean"
lake env lean "$HERE/KoszulCombined.lean" --root="$HERE" -o "$HERE/KoszulCombined.olean"
lake env lean "$HERE/Audit.lean" --root="$HERE" -o "$HERE/Audit.olean"
lake env lean "$HERE/AuditCombined.lean" --root="$HERE" -o "$HERE/AuditCombined.olean"
lake env lean "$HERE/Propagation.lean" --root="$HERE" -o "$HERE/Propagation.olean"
lake env lean "$HERE/AuditPropagation.lean" --root="$HERE" -o "$HERE/AuditPropagation.olean"
lake env lean "$HERE/ResidueBridge.lean" --root="$HERE" -o "$HERE/ResidueBridge.olean"
lake env lean "$HERE/TraceDetection.lean" --root="$HERE" -o "$HERE/TraceDetection.olean"
lake env lean "$HERE/AuditTraceDetection.lean" --root="$HERE" -o "$HERE/AuditTraceDetection.olean"
