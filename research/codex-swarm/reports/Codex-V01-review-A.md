> Reviewed metadata record; scope in STATUS.md.

# Independent coverage/metadata review: A01 and A02 concrete contracts

Review scope: output request identity, full owners, signs, scalar edges/derivative coordinates, prefix-mask accounting and admission flags. Current/frame mathematical identities are separately owned by V03. Read producer sources without editing or executing them; ran only own small metadata comparison script Codex-V01-review-A.py against independently reconstructed Codex-V01-requests.json.

Reviewed output hashes:
A01 seed12-e34-demand.json SHA256fc0fc9da978a9c7cbbedb7dc0bec6d4d118f03cd8734849c5434930219d0338c.
A02 seed30_e34_contract.json SHA25621d3282027d9c58f42cc0478da05e4890f466fb5eea63467cc995db713018bcc.
Changing either output invalidates this exact-byte review; read back any amendments.

## Metadata acceptance

A01 matches seed12 cloudrow4 q3localrank6, full owners(12,0,5,8,1),(12,1,1,9,9),(12,2,2,11,13),(12,3,4,15,15). Effective row coefficient2 and E denominator2 occur exactly once; branch signs+,-,+,-. Scalar edges are owners(2,3),(2,3),(1,2),(1,2), derivatives zero-based2,3,3,2 and current coordinates3,2,2,3, kindsL,L,U,U. Four independent outer weight references preserve all concrete prefix masks.

A02 matches seed30 cloudrow7 q4localrank0, owners(30,0,0,0,0),(30,1,1,1,8),(30,2,2,3,12),(30,3,3,7,14),(30,4,4,15,15). Effective coefficient+1 already includes terminal/J2 sign cancellation; each E branch has denominator2. Edges(3,4),(3,4),(2,3),(2,3), same derivative/current pattern as A01. Five owner-ledger weights remain; mask_merger_applied=false and owners_merged=false.

Both concrete tuples are already source-first sorted, sign+1. Legal masks are lowbiti and standard tags highbit3-i, matching independent manifest. Both remain candidate UNKNOWN fixed-mask terms. Neither silently replaces a prefix factor with its mask-summed family or doubles a prefix sum.

All actual_source_admitted/Laurent_admitted/execution_release/arithmetic_cost_certificate/physical_polynomial_evaluation/physical_polynomial_expansion flags are FALSE in both outputs. A01 additionally records selected Lower cannot accept tail tags(9,13,15), and fallback_used=false. Symbolic public AST nodes and source_formula_bound=true outer references are not executable lowering or source admission. Publication must retain that bounded description.

## Actionable coverage ambiguity before enumeration

A02 scalar_leaf.inserted_label_domain encodes legal_mask:[0,15], standard_tag:[0,15], alongside a carrier array that enumerates six values. This is ambiguous: a normal enumeration interprets those arrays as ONLY the two endpoint labels, omitting14 possibilities each. Replace with a tagged inclusive-range object or explicit list(range(16)); if intended as bounds, state that in machine-readable schema. Standard tags of actual insertions additionally need branch/endpoint binding; generic0..15 is only an enclosing universe, not a proof all such insertions occur. This does not imply a currently executed bad scan; the scalar leaf is unlowered and all admission flags remain false.

No full-label enumeration, resource certificate, coefficient value or global mathematical conclusion is accepted by this review. Next: clarify A02 domains and read back final JSON; V03 completes source/current review separately.
