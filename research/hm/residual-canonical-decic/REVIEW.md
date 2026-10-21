# Independent review: residual canonical decic

Verdict: PASS. Reviewed PROOF.md SHA256: b547aecf0a4551b24083bdeffc61af1cc1d2bfde26e03f0694897cc93b4025d5. This is an independent mathematical review, not formal proof-assistant verification. Work over C. The exact dependency is PR571 at 25afc8bfce079492b6b06bb6f52489f8d481c2aa; the additional non-descent statement uses PR570 at e5e55594ef2b99cefb81c4c02b22cb45e1ff0025 and the cited BHM normalization description.

## Representation and independence

The pair-to-axis interface is justified: the order-five subgroup of each direction stabilizer fixes both members of its cusp pair, and these are exactly its two projective fixed points. After unitary conjugation the faithful projective action is the rotational A5 action. The intrinsic frame calculation is valid: the real three-dimensional action is irreducible, so the self-adjoint invariant frame operator is scalar, with trace six giving 2I. A fixed C5 acts transitively on the other five axes, forcing the common squared inner product to be 1/5.

The decisive Hermitian pairing is the spin-five pairing on Sym^10(C²), not the ordinary fifth symmetric power pairing on R³. Independently, a meridian rotation sends X^5Y^5 to (cX+sY)^5(-sX+cY)^5, with c=cos(θ/2) and s=sin(θ/2). Orthogonality of distinct weight monomials makes the normalized pairing its middle coefficient. Expanding gives exactly (63t^5-70t^3+15t)/8 with t=cos θ. Thus the six-vector Gram matrix is (14/25)I+(11/25)G and is positive definite. This proves actual restricted-section independence without importing ambient quintic independence or evaluating a selected HM instance.

The displayed quadratic coefficients must be read as one half of sin θ, not sin(θ/2); the proof's explicit final notation makes that distinction.

## Pair identifications and singularities

Once independence is proved, the signed permutation description is faithful to the six actual decic generators. The character counts 6, 1, -2 at the identity, order-five elements, and involutions are correct. The incidence count 6·5/15=2 counts the axes stabilized by an involution. Averaging over C5 gives a two-dimensional invariant subspace and trace -2 for its normalizing involution, hence scalar action -I.

At each fixed point the degree-ten fiber character is trivial because the relevant SL2 eigenvalue has tenth power one. Evaluation therefore lies in the invariant subspace, so the two fixed points have identical projective images. The six images are distinct: D5 is maximal in A5, and a fixed projective image would be a one-dimensional character, whereas the signed permutation module and its dual have no invariant line.

The classical Castelnuovo bound applies to this integral nondegenerate curve without a smoothness hypothesis. Degree ten in P5 gives arithmetic genus at most six. Six distinct paired normalization fibers contribute at least six to the total delta invariant. Equality forces precisely six singularities with delta one and exactly two branches each. The completed-local-ring argument identifies each as an ordinary node; it excludes additional singularities, extra branches and other identifications.

## Canonical polarization and non-descent

The nodal curve is Gorenstein. Riemann–Roch, degree ten and six independent sections yield a nonzero section of the degree-zero invertible sheaf omega_Gamma tensor O_Gamma(-1). On an integral projective curve it has no zero divisor and trivializes the sheaf. Hence O_Gamma(1)=omega_Gamma and h0=6, proving completeness of the canonical system.

BHM Proposition 9 and Proposition 10, printed pp.63–64 of the cited volume, explicitly identify pairs of singular pentagon fibers at their common vertices, with two distinct normalization preimages at each resulting surface double point. The exact surface dictionary transfers this to S. The proposed descended elliptic-base morphism would have to take one surface point to two distinct base points, which is impossible. This excludes descent of that particular fibration, including after a base automorphism; it does not exclude every morphism from S to P1 or assert a Stein factorization.

## Boundary

No selected actual-source coefficient, matrix, rank or parameter was evaluated. The argument does not identify the entire primary degeneracy scheme at its boundary, establish the separate fixed-beta geometry, or solve full Q4, prescribed source membership, higher target lifting or algebraicity. The two public external inputs are the classical integral-curve Castelnuovo bound in the cited Di Gennaro reference, §2(v), and the stated BHM normalization gluing. All other new deductions are supplied in the proof.
