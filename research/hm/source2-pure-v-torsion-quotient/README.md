# Pure-V torsion quotient

New pure-V source2 quotient constraints, without assuming Q compatibility:

- The endpoint quotient is the actual torsion evaluation pencil on D12,
  with dimensions(12,12,5), not just an abstract character triple.
- The full quotient has dimensions(36,48,33). Its first pencil has rank36
  off D12 and35 on D12, with common kernel zero.
- Its maximal-minor degeneracy scheme is exactly the REDUCED divisor D12.
- Every nonzero second arrow is onto.
- The universal first cokernel has length12 torsion and torsion-free part
  Sym^8(W)O(1) plus A O(5), of rank12 and degree24.

The residual two-pencil extension need not be split by these arguments.
No Q-stable decomposition, obstruction equivalence, actual compatible line,
source exclusion or complete repair is claimed.

PROOF.md supplies the geometry. INPUTS.json pins three exact published
originals, copied into inputs/. Run Python3 with SymPy:

    python verify.py
    python -O verify.py

Both runs pass192 checks of authenticated inputs and bounded synthetic
universal algebra. No selected actual coefficient or point is evaluated.
