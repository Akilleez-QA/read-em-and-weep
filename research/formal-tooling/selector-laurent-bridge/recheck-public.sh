#!/usr/bin/env bash
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
: "${DEPENDENCY_ROOT:?Set to existing pinned Mathlib (4.19) or Vermilion (4.33) checkout}"
cd "$DEPENDENCY_ROOT"
[[ "$(git rev-parse HEAD)" == "1a56a4f38cbb126b7d73b04207e9c6fda9f179bf" ]] || { echo "Wrong dependency revision" >&2; exit 2; }
[[ "$(lake env lean --version)" == "Lean (version 4.33.0,"* ]] || { echo "Wrong Lean version" >&2; exit 2; }
export LEAN_PATH="$HERE${LEAN_PATH:+:$LEAN_PATH}"
lake env lean "$HERE/ResidueBridge.lean" --root="$HERE" -o "$HERE/ResidueBridge.olean"
lake env lean "$HERE/residue/Evidence.lean" --root="$HERE" -o "$HERE/residue/Evidence.olean"
lake env lean "$HERE/residue/residue_term.lean" --root="$HERE" -o "$HERE/residue/residue_term.olean"
lake env lean "$HERE/residue/missing_face_zero.lean" --root="$HERE" -o "$HERE/residue/missing_face_zero.olean"
lake env lean "$HERE/SelectorLaurentBridge.lean" --root="$HERE" -o "$HERE/SelectorLaurentBridge.olean"
