# Proof repair: current status

**Craig Ward · 23 October 2026 · Mathematical checkpoint through PR1107**

**The original positive 41→37 component now has a proved finite sequential rank criterion through order24. Its actual gate values remain unknown.** The first nonzero class gives generic rank37; allzero gives rank36. This is not full-adjoint invertibility or a complete repair. Endpoint nine is excluded; endpoint sixteen has two unselected mechanisms. Four necessary source-dual pairs across three labels remain.

[Paper index](paper/README.md) · [Detailed status](paper/01-current-status.md) · [Historical archive](paper/52-root-status-archive-through993.md)

## Complete universal component-scheme classification

For R=αR₁+βR₂, every nonzero pair belongs to exactly one stratum. Z denotes the six prescribed length-four order-five ideals (u²,v²) and ten reduced order-three axes, of total length 34.

| Ratio β/α | Complete nonic component scheme | Length |
|---|---|---:|
| −2 | Six Z ideals; m² at ten order-three axes | 54 |
| −1 | Z plus fifteen reduced order-two axes | 49 |
| 0 | Z plus twelve reduced conic points | 46 |
| +2 | m³ at six order-five axes; ten reduced axes | 46 |
| Every other ratio, including infinity [0:1] | Exactly Z | 34 |

Universal strata need not remain available within each mechanism. The length-46 schemes are distinct. [Complete theorem](paper/82-pure-v-complete-nonic-classification.md)

![Complete universal nonic coefficient strata; endpoint nine excluded and endpoint sixteen coefficient unknown](paper/figures/pure-v-coefficient-pencil.svg)

The zero pair has whole-plane base scheme, with no finite length. Residual-large permits only zero or the conic line; nonzero-N0 still has an unselected two-dimensional coefficient space. No completion percentage follows.

## Finite sequential criterion and remaining actual data

[PR1107](paper/126-finite-sequential-obstruction.md) constructs canonical global gates **s3,…,s23**, reached only when preceding classes vanish. They correspond to original orders **4–24**, not independent parameters. The first nonzero s_n gives last Smith exponent n+1 and generic Laurent rank37. If all vanish, any later pivot would force maximal-minor order≥31, contradicting degree≤30; rank is exactly36, with kernel dimension five.

The global recursion updates two consecutive corrections and retains the κ remainder. Its first equivariant κ gauge occurs at original order9. No actual gate is evaluated. The result concerns this rectangular positive component, not the full adjoint, and does not assert a square-conic base-change recursion.

[The canonical terminal sextet T_Q](paper/125-canonical-q-terminal.md) is the actual image Q3(NC3)=WQ2(V_C). In residual-large ℓ|T_Q is an isomorphism, complementing C_term. If τ=0, its first-block projection forces the specific Q2 channel onto (N0,4)_V. This supplies an actual target for further comparison, not a fifth value or source selection.

**Residual-large:** R=αR1. α≠0 iff maximal-minor ideal (t¹⁰), with 33 unit pivots, three t² and one t⁴, outside the known 28-point support. If α=0, the unselected two-dimensional fifth class gives exponent5 iff nonzero. A later finite exponent is ≤24 generically and ≤21 on squares; absence is possible. [Smith and fifth details](paper/121-residual-positive-smith-criterion.md)

**Nonzero-N0:** R=A(R1−4R2)+B(3R1+2R2). For actual row ℓ=(ℓ0,τ) and terminal graph g, zero requires ℓ0+τg=0. Thus τ=0 forces nonzero R; otherwise its zero graph is uniquely −τ⁻¹ℓ0. Neither row nor graph is selected. [Exact channels and corrected factorization](paper/120-corrected-factorization-and-zero-graph.md)

## Two surviving actual negative modules

Both generated modules start with dimensions **9,14,16** in degrees 2–4 and vanish from degree six:

- **Nonzero N0 projection:** degree five has dimension **12**, type 2T; total length **51**. Its terminal subspace may be a graph into NR5. [Separated-terminal theorem](paper/108-separated-terminal-module.md)
- **Zero N0 projection, nonzero N8 projection:** degree five is the marked residual T, dimension **6**; total length **45**. [Residual-large theorem](paper/107-actual-residual-large-module.md)

Both have socle I4 plus their terminal piece, exact resolutions and annihilator (W)⁴. Neither is the full Rao module or asserted positive-stable; neither mechanism is selected.

## Excluded-branch history

Earlier endpoint-nine length-32, nonzero-conic and positive Smith/maximal-row-rank implications have an **excluded antecedent**. They do not solve the surviving positive component. [Dated theorem](paper/106-positive-component-smith-profile.md)

The table covers nonic and determinant-fourth D projective ideal sheaves, not raw ideals, lift degeneracy or extra specialized A-kernel classes. [Exact transfer](paper/84-pure-v-fourth-ideal-transfer.md)

[Opposite-pencil source reports](paper/122-opposite-nonzero-core-source-report.md) now give intrinsic criteria for all seven necessary rows across the old zero/nonzero gate. No row or gate is selected; these are not im h endpoint spaces.

## Fixed source frontier

| Source | Stable label | Catalogue pairs (E,Q*) |
|---|---|---|
| Source126 | G3.11.8ae96830fd21 | (10,129), (10,157) |
| Source127 c-d-f | G3.11.cce6e3ba4eeb | (14,148) |
| Source2 | G3.21.d610e381ed75 | (13,21) |

These are **2+1+1 necessary pairs**, not actual realizations. Source126's octic scalar, applicable single-line cubics, c-d-f alternatives, actual compatibility and physical higher lifting/algebraicity remain unresolved. Seven opposite-bundle types are a separate catalogue. [Earlier results and limits](paper/01-current-status.md)

Checks support written proofs, not formal certification of the repair. Collaborator reports are source readings, not independent reproofs. Draft PRs are not merges.
