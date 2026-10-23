# Independent review: complete sextic-channel classification

Verdict: PASS for the complete stated universal theorem, including the exact degree-one ambient strata and their abstract realization models. This is independent written-proof review with exact supporting controls, not proof-assistant verification or a new actual HM case exclusion.

## Frozen bindings

- PROOF.md SHA256: cb771135ef4cdb9a8f290d31c702c97f6b57c5d385bbc343040e3ac189fc00c6.
- verify.py SHA256: ff9511990c490a9a099eeba75974e0e4727d810eb8da5381ddb3d9d91c4fdf33.
- RESULT.json SHA256: d8e389f5a1b55ecfa10e59ddb7df49f78cf78e074395c4ef81723da850497173.

The entire proof, implementation, reproduction instructions and four full immutable sources were read. PR1147, PR1150 and PR1148 proofs and the public character source were freshly retrieved from their original immutable URLs. Every retained original matches by exact byte count, SHA256 and Git blob SHA1, as reproduced from INPUTS.json and originals/. These are public mathematical sources; no actual HM coefficients or instance computations enter the review.

## Mathematical verification

1. Semisimplicity and multiplicity one really leave exactly V, P and V+P as nonzero invariant sextic subspaces. The full-system evaluation kernel is l Sym5 on every fiber under determinant/apolar identification; multiplication realizes T O(-1) as that saturated kernel. Together with the two pinned exact sequences, twisting gives every listed kernel, cokernel and minimal multiplier threshold. The free resolutions are induced in every degree and respect multiplication, rather than being inferred from Hilbert numerators. The quotient lengths 27,24,21 are correct.
2. Pulling the actual annihilation back along the dual injection of the possibly partial coefficient quotient gives the full universal apolar factor Sym6 O(-d). This factorization does not assume completeness. Ordinary degree vanishing removes the high source, while multiplicity-one representation theory identifies exactly the two possible scalar channels. Their nonzero support need not equal the full source U. The inactive block is retained as a direct summand of the actual kernel B.
3. H0(S)=0 is precisely that the union of actual F fibers spans H as a constant vector space. Applying the constant surjection to R* makes the span of the projected fibers all of R*. Those fibers are l^d J, so the equality R*=J Sym^d is justified, not merely a containment or a dimension prediction. Consequently the exceptional d=1, V-only coefficient image is exactly T of dimension six, with W' kernel in Sym7. A full eight-dimensional alternative is correctly excluded in this stratum.
4. The kernel B is saturated in H O because it is a bundle summand of saturated F. Its quotient in the constant projection kernel is torsion-free, hence locally free on P1. If B is nonzero, equality of its rank with that constant kernel would make it constant, contradicting negativity. This proves the strict integer improvement. The same argument applies to inactive same-degree blocks, not only to the higher-degree source.
5. For d=1 the high block is absent, and spanning makes H a quotient of U tensor W. The exact ambient possibilities follow from the coefficient modules T, W'+T and W'+2T and the actual quotient R*. With full source and V-only support, the inactive P has a coefficient quotient of W'+T whose dimension is at least its fiber rank four; only dimensions six or eight can occur. This forces H=2T or W'+2T. P-only support forces a nonzero inactive V coefficient image, which is the whole irreducible T, hence H=W'+2T. Both-active support requires a quotient W'+T, allowing only W'+T or W'+2T. These give exactly the displayed codimensions 5/7,7,1/7.
6. The realization claims satisfy the actual line-annihilation condition, not just a source-embedding rank test. In the full coefficient model, the chosen support multiplication quotient has dual polynomial line obtained from the complete Veronese line. Pairing that line with the tautological source inclusion equals pairing l^7 with l times the active sextic, which vanishes by apolarity. For single active V the line is a nonzero projection to T; an invariant base divisor of degree at most seven is impossible by the orbit-twelve bound, so its inclusion is saturated. The same argument applies to the other coefficient projections.
7. The twelve-dimensional V-only model uses multiplication on V into T and directional contraction on P into a separate T. The contraction on all sextics has rank six and its one-dimensional kernel is a pure sixth power for every nonzero direction. P contains no such power: distinct self-dual irreducibles V and P are orthogonal for the invariant apolar form, and a pure power in P would imply a common zero of the basepoint-free V net. Thus the P restriction is fiberwise injective of rank four; it spans T by irreducibility. Projection onto the first T has precisely active V, and its saturated partial degree-seven line annihilates the whole direct sum. This verifies the c=5 model, including the apolar condition.
8. Full multiplication into Sym7 supplies the c=1 both-active model; the tautological fourteen-dimensional model supplies all c=7 alternatives with the selected support quotient. Each inclusion is saturated and spans its ambient. Their center is odd. The final parity warning is correct: a center-even ambient forces n even, so none of these degree-one n=7 strata is silently asserted for a center-even HM ambient.

## Reproduction and independent evidence

The supplied checker reproduces all 10,131 recorded controls, including 5,740 monomial apolar pairings, identically with ordinary Python and Python -O. Both outputs match the retained RESULT.json byte for byte.

The separate independent_check.py in this review directory uses exact class-character inner products instead of the production McKay-product recurrence, exhausts support and degree-one representation quotient choices, verifies the three Hilbert numerators, and proves 2,100 full formal apolar polynomial identities by binomial coefficients over rational numbers. It also checks the six explicit full-evaluation syzygies and two universal directional-contraction chart minors, with the exact pure-power kernel identity. No parameter or actual source is sampled. It authenticates all four freshly retrieved originals. Its 4,475 checks reproduce identically normally and under -O, matching this directory's distinct RESULT.json.

Run, from this directory:

    python independent_check.py
    python -O independent_check.py

The checker uses only its local INPUTS.json and originals/ and is relocatable. Run the production verify.py in the theorem packet separately; do not overwrite its RESULT.json with the independent output.

## Scope

No correction is required. The classification exhausts the three nonzero equivariant sextic subsystems, their nonzero scalar supports, their coefficient-span cases and the claimed degree-one abstract ambient realizations. It does not prove any new actual osculating-containment hypothesis, exhaust HM Gauss profiles, close profile11, or repair the original theorem. The finite tests support the written universal proof and do not replace it.
