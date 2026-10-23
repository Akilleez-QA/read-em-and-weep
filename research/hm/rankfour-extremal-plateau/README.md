# Rank-four maximal (3,3) plateau exclusion

Conditional on the original actual equivariant bundle geometry, this packet
excludes the maximal rank-four Gauss profile (3,3), and only that profile.
It does not establish a global rank-five bound or original proof repair.

Read PROOF.md for the geometric argument and exact premise limits.
INPUTS.json authenticates three complete pinned originals in inputs/.
CANDIDATES.json contains the twenty newly derived abstract rank-four
quotient shapes, not an enumeration of selected actual HM data.

Reproduce from any working directory:

    python3 verify.py > normal.json
    python3 -O verify.py > optimized.json
    cmp normal.json RESULT.json
    cmp optimized.json RESULT.json

The final certificate has 768 explicit checks. The proof, not the
arithmetic alone, establishes the sheaf, saturation and persistence steps.
COORDINATION.json records the read-only PR1 checkpoint used to avoid
duplicating the collaborator's separate profile11 work. No external
repository state was changed while producing this packet.
