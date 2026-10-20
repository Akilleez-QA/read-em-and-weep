# Historical scope-limited review receipt

This review concerns the original source, possibly a larger scope than the excerpt in this unit. It is not a review of normalized publication bytes.

# Independent formal audit

Audited final proof: [PROOF.md](../MONOMIAL.md). SHA-256 independently verified by the reviewer: `1b96861d7404cf6e4e2c3de3ca8c13496b5f01a70b73e0d8f6f1291e86ba8042`. The audit binds to those exact final proof bytes, including Sections 7–8.

An independent reviewer examined the unrestricted support argument, the affine necessity, the complete permutation-chain signs, the monomial/diagonal reduction, and the final projective-coherence and finite-quotient consequences. It reported that these arguments pass under the stated characteristic-zero hypotheses. No source/model/rank/polynomial-instance/point/jet/residual execution or evaluation was used.

## Checks reported

For j=π(i), transporting the ordered pair of forms (D_j^+,D_j^−) by P_π gives respectively

- a=1: (D_i^+,D_i^−)
- a=2: (D_i^−,−D_i^+)
- a=3: (−D_i^−,D_i^+)
- a=4: (−D_i^+,−D_i^−)

with every right-hand form evaluated at P_πv. The proposed K(a) therefore proves Aδ=δ(P_πv)M on all U,V,Z columns. Paired evaluation proves the final chain equation.

The audit independently confirmed: Z forces the monomial shape of N; zero/nonzero entries propagate along the U cycle; surviving top pairs force preservation of the mate involution (c,l)↦(2c−l,3c−2l); its first component implies constant successive differences, hence affine π. Factoring off the verified affine chain reduces to the audited diagonal classification.

## Convention caveats incorporated

P_πP_σ=P_{σ∘π}, so the matrix labeling is opposite to ordinary function composition. The proof explicitly records this and gives the actual matrix-conjugation action on (α,β). It distinguishes 500 geometric elements from rational-point counts over nonclosed fields and makes no full nondiagonal-stabilizer claim.

## Audit of projective coherence and the free quotient

The reviewer separately audited final Sections 7–8. Pullback order is correct: g*φ_h composed with φ_g targets (h∘g)*H. One-dimensional Hom removes the composition scalar after projectivization, without asserting a split linearization. Matrix representatives differing by scalar define the same base automorphism; intrinsic Hom and uniqueness remove that ambiguity. Over nonclosed fields uniqueness gives Galois-compatible geometric projective maps and therefore descent.

For fixed finite-dimensional W⊂H⁰(T,L), linear independence makes every geometric stabilizer trivial. Since the full acting group scheme is finite étale, the action is scheme-theoretically free. An invariant open in P(W^5) is quasi-projective, its finite quotient exists as a scheme, and its quotient morphism is a finite étale torsor of degree 500. Over nonclosed fields this degree refers to the full finite étale group scheme, not only rational group elements. The generation locus is used conditionally as an invariant open; no unproved openness claim is imposed on arbitrary T.

The proof incorporates these precision clarifications. No substantive mathematical gap was reported.
