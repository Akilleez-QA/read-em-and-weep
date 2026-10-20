# Coordinate singular intersections after the seven-dimensional frame bound

Import the exact coordinate-plane kernel and tangent description from ../../cubic-loci/cubic-component-multiplicities/coordinate-component-multiplicities/PROOF.md, and the independent-frame dimension bound dim Z_ind≤7 proved here. Fix any of the three coordinate components C_i≅V², of dimension ten. For a fixed pair b in C_i, write L_i(b):V→J for the trilinear operation in the missing slot, and let D_{i,≥r} denote its kernel-dimension-at-least-r locus, considered set-theoretically for the following dimensions.

Then:

- dim(Sing(Z)∩C_i)=dim D_{i,≥1}=6. Thus this singular intersection has codimension four in C_i.
- dim D_{i,≥2}=dim D_{i,≥3}=5.
- D_{i,≥4}=D_{i,≥5} is the union of the two zero-input axes, of dimension five.
- On the independent-pair locus, the exact kernel-dimension-r stratum has dimension at most 7−r, for 1≤r≤3. Larger kernels cannot occur there.

For the proof, an independent fixed pair has kernel disjoint from its two-plane by the two-plane zero classification. Every nonzero vector in its r-dimensional kernel therefore gives an independent zero triple. On each locally closed constant-rank stratum this is a punctured rank-r vector bundle. Its dimension is the base dimension plus r and is at most seven. This proves the independent-pair bound.

A nonzero proportional fixed pair has a one-dimensional kernel, namely its common line. Such pairs form a six-dimensional locus: four parameters for the projective line and two nonzero scalar parameters. If either fixed input is zero, trilinearity gives the entire five-dimensional kernel, and these two axes have dimension five. These cases exhaust the pair space. Their upper bounds and the displayed six- and five-dimensional subloci prove all exact dimensions above. The imported Jacobian calculation identifies the singular intersection with D_{i,≥1} set-theoretically.

Every irreducible component other than the three coordinate components has dimension at most seven. Indeed a component contained in the dependent zero locus is contained in a coordinate plane or in the rank-one cone D, by the two-plane classification. Any other component meets the independent open and has dimension at most seven. In particular there are no eight- or nine-dimensional components of the full zero scheme.

These are support and dimension statements. They do not determine the singular intersection scheme, its multiplicities, the number of lower-dimensional components, or whether any independent component attains dimension seven. No actual operation map was evaluated.

## Independent audit

PASS. The punctured-kernel bundle dimension formula applies on exact-rank locally closed strata; no bundle across rank jumps is assumed. The proportional and zero-axis strata supply the asserted lower bounds, while all independent-pair strata satisfy the new upper bounds. The imported tangent calculation and dependent-zero classification justify the singular and full-component consequences. No corrections remain.
