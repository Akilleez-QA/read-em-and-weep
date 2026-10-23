# Proof repair: current status

**Craig Ward · 23 October 2026 · Mathematical checkpoint through PR1079**

**Endpoint nine now forces maximal generic row rank 37 for the actual positive 41→37 component. This is not full adjoint invertibility or a complete proof repair.** Four necessary source-dual pairs across three stable labels remain. No actual compatible pure-V source or endpoint branch is selected; endpoint nine now forces the nonzero conic gate.

[Paper index](paper/README.md) · [Detailed status](paper/01-current-status.md) · [Historical archive](paper/52-root-status-archive-through993.md)

## Complete universal component-scheme classification

In the pinned quadratic-lift basis R=αR₁+βR₂, every nonzero coefficient pair belongs to exactly one of these five strata. Z denotes the six prescribed length-four order-five ideals (u²,v²) and ten reduced order-three axes, of total length 34.

| Ratio β/α | Complete nonic component scheme | Length |
|---|---|---:|
| −2 | Six Z ideals; m² at ten order-three axes | 54 |
| −1 | Z plus fifteen reduced order-two axes | 49 |
| 0 | Z plus twelve reduced conic points | 46 |
| +2 | m³ at six order-five axes; ten reduced axes | 46 |
| Every other ratio, including infinity [0:1] | Exactly Z | 34 |

This universal ideal-sheaf table is not a list of available outcomes within each endpoint branch. Every other ratio gives exactly Z; the two length-46 schemes are distinct. [Complete theorem](paper/82-pure-v-complete-nonic-classification.md)

![Complete universal nonic coefficient strata; zero gate separate and actual coefficient unknown](paper/figures/pure-v-coefficient-pencil.svg)

The zero pair is separate: its component ideal is zero and its base scheme is the entire plane, with no finite length. Zero is now excluded in endpoint nine; its status in endpoint sixteen remains unselected. The figure locates exact ratios, not mathematical branches between them, fractions of search space or completion percentages.

## Endpoint nine now forces a nonzero conic gate

The generated endpoint is still **9 or 16**, neither selected. Endpoint nine now forces **R=γR₁ with γ≠0**: exactly the conic coefficient stratum β=0. Its component scheme is Z plus twelve reduced ambient conic points, length 46. Zero and the other four universal nonzero strata are excluded in that branch. Conic membership does not conversely force nine. [Nonvanishing theorem](paper/105-nonzero-small-transfer.md)

Q(NC2)∩NC4 is I4 in endpoint nine and **zero in every endpoint-sixteen branch**. No Q-preservation or matching-character identification with NR4 follows.

## Exact positive Smith profile

In endpoint nine, outside the **28 support points** of the length-46 scheme, the actual positive component has Smith form with **33 unit pivots, three t² pivots and one t⁴ pivot**, plus four zero columns. Thus its formal kernel is free of rank four, its cokernel has length ten, and its maximal-minor ideal is (t¹⁰). The profile also holds for the symbolic generic direction. [Exact theorem](paper/106-positive-component-smith-profile.md)

No profile is asserted at those 28 points. Row rank 37 holds generically in t, not at t=0 or every nonzero t. Not every maximal minor must be nonzero or have order ten. The other parity component and full adjoint problem remain outside this theorem.

## Two actual negative modules, with distinct hypotheses

Endpoint nine gives the actual negative module R·im h of length **32**, supported in degrees 2–4, with socle NC4 and annihilator (W)³. In **residual-large only** (zero N0 projection, nonzero N8 projection), it instead has length **45**, supported in degrees 2–5, socle I4 in degree four plus the marked residual T in degree five, and annihilator (W)⁴. Both have exact minimal equivariant resolutions. [Small module](paper/103-actual-terminal-negative-module.md) · [Residual-large module](paper/107-actual-residual-large-module.md)

Neither is the full Rao module or asserted positive-stable. The length-45 conclusion does not cover the endpoint-sixteen branch with nonzero N0 projection. Neither branch is selected. Attributed opposite-pencil and canonical-string results remain separate. [Source reports](paper/README.md)

The table describes projective component ideal sheaves for both the nonic and determinant-embedded original-fourth D row, not raw graded ideals, quadratic-lift degeneracy or additional specialized A-kernel classes. [Exact transfer](paper/84-pure-v-fourth-ideal-transfer.md)

## Fixed source frontier

| Source | Stable label | Catalogue pairs (E,Q*) |
|---|---|---|
| Source126 | G3.11.8ae96830fd21 | (10,129), (10,157) |
| Source127 c-d-f | G3.11.cce6e3ba4eeb | (14,148) |
| Source2 | G3.21.d610e381ed75 | (13,21) |

These are **2+1+1 necessary pairs**, not actual realizations. Source126's octic scalar, applicable single-line cubics, c-d-f alternatives, actual compatibility and physical higher lifting/algebraicity remain unresolved. Seven opposite-bundle types are a separate catalogue. [Earlier results and limits](paper/01-current-status.md)

Exact checks support written proofs over pinned premises, not formal certification of the entire repair. Collaborator reports are full-source readings, not independent reproofs. Draft PRs are not merges.
