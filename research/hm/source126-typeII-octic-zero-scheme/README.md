# Canonical octic target section: exact exceptional scheme

The unique invariant target section σ∈H0(E(4)) has a finite zero scheme of length34:

- Six order-five axes, each with completed ideal (u²,v²), length4.
- Ten order-three axes, each reduced, length1.
- No zeros on the discriminant conic of squares.

Its saturated ideal has minimal resolution

    0→3O(−8)⊕O(−11)→5O(−7)→I_Z→0.

The target-factor zero scheme is contained in the zero scheme of the canonical octic generator. Additional source-covector zeros and the actual octic scalar are not computed.

Run `python verify.py` and `python -O verify.py`; each performs92 exact checks. PR995 and PR982 are copied and hash-authenticated. Their immutable public Git blobs were freshly matched during preparation. Checks cover plane and binary character distinctions, the universal conic jet map, A5 subgroup normalizers, the unique orbit-length decomposition, C5 local ideals, and the minimal-resolution Hilbert series.

This is new geometry of σ, not a rebranding of older six-axis schemes for other maps. No actual HM instance evaluation, source exclusion, or full repair is claimed.
