# The c-d-f even algebra and its conditional split alternative

**Craig Ward · 23 October 2026 · Update through PR1015**

[PR1015](https://github.com/Akilleez-QA/read-em-and-weep/blob/e6cdc5c10d2cb1aed27eb76ff44d0b4aa652bdce/research/hm/cdf-even-commutant-split-line/PROOF.md) classifies the full algebra of parameter-independent equivariant endpoint maps commuting with every negative quadratic. Assuming an actual c-d-f occurrence, but **without assuming one-sided B preservation**, this algebra has dimension eight. Imposing the invariant Q leaves either the common scalars or C². The nonscalar alternative forces formal persistence of the original D kernel and generic original rank36. Neither alternative is selected or realized, and no source-dual pair is removed.

## 1. Even and full-linear algebras are not interchangeable

The reconstruction lemma applies to the generated F⊕B source and the joint-injective full target. It forces scalar actions a,b on those source blocks and the same actions on their target blocks. The remaining L target has no degree-two source, so its equivariant target action is unrestricted by the negative quadratics.

Consequently the even algebra has four diagonal coordinates and four arrows: L_V→B_V, L_P→F_P, and two L_P→B_P arrows. Their products vanish, giving a four-dimensional square-zero radical and semisimple quotient C⁴. The full negative-linear-pencil algebra is a proper four-dimensional subalgebra: it requires the two L diagonal scalars to agree and forbids three of the four arrows. Omitting the middle degree genuinely enlarges the algebra.

## 2. Actual generation leaves two algebra possibilities

Actual generation Y=im Q+im q₋ makes the source-action map from the Q-compatible algebra into C² injective. An endpoint map with zero source action kills both generating images and therefore vanishes. A unital subalgebra containing the common scalars is thus C or C².

In the nonscalar case the unique compatible idempotent with source values (0,1) has two target L bits. The possibilities putting L_V on the B side cannot supply the actual two V image constituents. Putting both L constituents on the F side would make the B block onto with kernel A; preserved-block recursion would then kill the known second obstruction on A. Only one footprint remains: L_V is on the F side, and L_P on the B side.

Two graph shears remain allowed by idempotence. Their actual values are not selected, and they are not independently realized parameters: a compatible idempotent, if present, is unique for the actual Q. Its differing L diagonal values prevent extension to the full linear pencil, so it does not contradict the older scalar full-linear Q-commutant theorem.

## 3. What that footprint would force

The F target eigenspace has character V+P+D and dimension12; Q from X_F is onto it with kernel the entire original D. The B target eigenspace has character V+3P+2D and dimension25, with Q kernel A and cokernel P.

For every negative quadratic direction, a right inverse of the onto F block gives the recurrence xₙ₊₁=−sT_a xₙ. It lifts every initial D vector to all formal orders. Together with the imported 33 unit Smith factors and generic second rank three, this forces generic original rank exactly36, kernel dimension five and cokernel dimension one. All later generic original Bocksteins vanish in this conditional alternative. It does not compute extra specialized survivors or prove that the alternative occurs.

## 4. The one-sided branch is scalar even at this level

If one additionally assumes Q(X_B)⊂Y_B, the previously proved actual kernel lies wholly in X_B. The only nonscalar footprint instead places its D kernel inside the disjoint X_F. Hence the nonscalar alternative is impossible under this extra hypothesis, and the Q-compatible even algebra is scalar there.

This does not reduce the [one-sided raw cubic](59-cdf-preserved-b-cubic.md) from three dimensions, determine its value, or establish one-sided preservation. Parameter-dependent endomorphisms remain outside this classification. Four necessary pairs across three labels remain.

The full proof has independent review and 77 checks in both normal and optimized Python. The all-orders claim comes from the arbitrary-order recurrence, not merely the finite symbolic checks. No actual HM coefficient, parameter point or instance rank is evaluated.
