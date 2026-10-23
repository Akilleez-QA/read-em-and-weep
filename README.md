# Proof repair: current status

**Craig Ward · 23 October 2026 · Mathematical checkpoint through PR1046**

**The universal pure-V component-scheme classification is complete, and now transfers to the determinant-embedded original fourth D row. The original proof repair is not.** Four necessary source-dual pairs across three stable labels remain. No actual compatible pure-V source, nonzero gate or coefficient ratio is selected.

[Paper index](paper/README.md) · [Detailed status](paper/01-current-status.md) · [Historical archive](paper/52-root-status-archive-through993.md)

## Complete universal classification

In the pinned quadratic-lift basis R=αR₁+βR₂, every nonzero coefficient pair belongs to exactly one of these five strata. Z denotes the six prescribed length-four order-five ideals (u²,v²) and ten reduced order-three axes, of total length 34.

| Ratio β/α | Complete nonic component scheme | Length |
|---|---|---:|
| −2 | Six Z ideals; m² at ten order-three axes | 54 |
| −1 | Z plus fifteen reduced order-two axes | 49 |
| 0 | Z plus twelve reduced conic points | 46 |
| +2 | m³ at six order-five axes; ten reduced axes | 46 |
| Every other ratio, including infinity [0:1] | Exactly Z | 34 |

This describes the component **ideal sheaf**, equivalently the saturated homogeneous ideal. There are no extra support points, hidden local thicknesses or divisorial components in any nonzero stratum. Equality with Z holds for **every** member outside the four special ratios, not merely a generic member. The two length 46 cases are different schemes, not interchangeable outcomes. [Complete theorem](paper/82-pure-v-complete-nonic-classification.md)

![Complete universal nonic coefficient strata; zero gate separate and actual coefficient unknown](paper/figures/pure-v-coefficient-pencil.svg)

The zero pair is separate: its component ideal is zero and its base scheme is the entire plane, with no finite length. Whether the actual conditional gate is zero remains unknown. The figure locates exact ratios, not mathematical branches between them, fractions of search space or completion percentages.

## What closed the remaining scheme questions

- **Fifteen-axis occurrence and reducedness:** that orbit occurs exactly at β=−α. Whole-orbit remainder and Nakayama certificates give ambient maximal ideals, so this full scheme has length 49. The earlier possible fifteen-axis double points never occur. [Occurrence theorem](paper/79-pure-v-fifteen-axis-scheme.md)
- **No thirty-point orbit:** an exact homogeneous mirror resultant and all exceptional gcds exclude this support for every nonzero coefficient pair, including coefficient infinity. [Whole-pencil exclusion](paper/80-pure-v-no-thirty-orbit.md)
- **Conic thickness resolved:** at β=0, all twelve conic basepoints are reduced in the ambient plane, not just on the conic. Its complete scheme is Z plus that reduced orbit, length 46. [Ambient local ideals](paper/81-pure-v-conic-ambient-scheme.md)

Together with the exact jet cases, these replace the older necessary nine-length list by an exhaustive scheme theorem. This completes the stated universal question, not the actual-source problem.

## Global geometry, source-reported

mr. slop establishes actual restriction sequences 0→Jg→ker Θ→C*O(8)→0 and 0→C→H₉→Jg*O(8)→0. Jg has an actual 28→41 Steiner presentation, rank 13 and degree 28. It is **not** the rank 13, degree 20 residual of the finite splitting. A determinant of degree −8 forces a nonzero intersection with the selected A(4)⊕W(5) subbundle; it does not choose either component map. The sequences are not asserted split. [Full-source report and parity](paper/83-global-ninth-bridge-source-report.md)

## Original-fourth bridge and retained boundaries

The new exact bridge proves equality of projective component ideal sheaves for the nonic F and determinant-embedded original-fourth D row H=FL, including all ten order-three axes where L loses surjectivity. Whole-orbit certificates give m off the C₃ jet line and m² on it. The five-stratum table therefore transfers unchanged. [Exact local comparison](paper/84-pure-v-fourth-ideal-transfer.md)

This is not equality of raw graded ideals, quadratic-lift rank-drop schemes or singular-target fiber maps. Additional specialized A-kernel classes remain outside the comparison. Actual coefficients and source occurrence remain unknown.

## Fixed source frontier

| Source | Stable label | Catalogue pairs (E,Q*) |
|---|---|---|
| Source126 | G3.11.8ae96830fd21 | (10,129), (10,157) |
| Source127 c-d-f | G3.11.cce6e3ba4eeb | (14,148) |
| Source2 | G3.21.d610e381ed75 | (13,21) |

These are **2+1+1 necessary pairs**, not actual realizations. Source126's octic scalar, applicable single-line cubics, c-d-f alternatives, actual compatibility and physical higher lifting/algebraicity remain unresolved. Seven opposite-bundle types are a separate catalogue. [Earlier results and limits](paper/01-current-status.md)

Exact checks support written proofs over pinned premises, not formal certification of the entire repair. Collaborator reports are full-source readings, not independent reproofs. Draft PRs are not merges.
