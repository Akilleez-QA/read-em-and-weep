#!/usr/bin/env bash
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
: "${VERMILION_ROOT:?Set to an existing built pinned Vermilion checkout}"
cd "$VERMILION_ROOT"
[[ "$(git rev-parse HEAD)" == 1a56a4f38cbb126b7d73b04207e9c6fda9f179bf ]] || { echo "Wrong Vermilion revision" >&2; exit 2; }
source scripts/lean_env.sh
[[ "$(lean --version)" == "Lean (version 4.33.0,"* ]] || { echo "Wrong Lean version" >&2; exit 2; }
export LEAN_PATH="$HERE/bridge-deps:$HERE/proofs:${LEAN_PATH:-}"
for m in ResidueBridge residue/Evidence residue/residue_term residue/missing_face_zero SelectorLaurentBridge; do
  lean --plugin="$vrml_cvc5_plugin" "$HERE/bridge-deps/$m.lean" -R "$HERE/bridge-deps" -o "$HERE/bridge-deps/$m.olean"
done
lean --plugin="$vrml_cvc5_plugin" "$HERE/proofs/bounded.lean" -o "$HERE/proofs/bounded.olean"
lean --plugin="$vrml_cvc5_plugin" "$HERE/BoundedBridge.lean"
lean --plugin="$vrml_cvc5_plugin" "$HERE/Axioms.lean"
