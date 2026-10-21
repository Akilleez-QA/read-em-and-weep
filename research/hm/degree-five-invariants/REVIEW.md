# Independent review: degree-five invariant defect

Verdict: PASS, including Section 6's seven-dimensional invariant product domain. This is an independent mathematical audit of the stated deductions from the pinned primary-geometry inputs, not formal verification or a fresh proof of every upstream theorem. Reviewed 2026-10-21 UTC. No selected HM/source coefficients, evaluation matrices, numerical rank tests, large computations, or public writes were used.

## Sources independently checked

The following immutable files were fetched through the repository connector and read:

- 7bf725bcd857a2deb975f9ecb80fca32e7833ae0, research/hm/order-four-quadratic-load/PRIMARY-INJECTION-AND-FAILURE.md: Section 1 identifies actual natural multiplication with the nonzero N-equivariant exterior-plus-sl(W) map, in the A0=V3 convention.
- e0f15a5c6a49d2101dae450dae4d26171a259331, research/hm/unique-line-surface/PROOF.md: the unique reduced integral line-bearing component is preserved by the full normalizer.
- 6c2dbd48edea0577acf063a60e1edbbbe92ced5c, research/hm/global-primary-equality/PROOF.md: actual degeneracy-scheme equality, normalization, and the thirty reduced transverse branch-difference fibers.
- 7547a6a0d84d29478a0bad2d30bda271c37c269e, research/hm/quadratic-conductor-generation/PROOF.md: Sections 2–3 prove actual quadratic differences generate every node fiber and have dimension five; Section 4 proves im(rho_n)=P_(n-2) im(rho_2), not merely abstract sheaf generation.
- a1c77f791158cc0976df80220c958a50c2217ee3, research/hm/eigenline-postulation/PROOF.md: Sections 6–7 establish the actual-primary range 25<=r_5<=29 using separate quadratic generation and the pinned nonzero degree-five defect.

Also read the local source proofs for eigenline interpolation and primary postulation. Their role is explicitly retained as geometric input: the universal point-configuration calculation alone does not prove the upper bound on r_5.

The original Horrocks–Mumford paper was independently opened at https://www.dam.brown.edu/people/mumford/alg_geom/papers/1973a--Rk2BdleP%5E4-NC.pdf . Printed page 65 proves the normalizer quotient N/H5=SL2(F5); printed page 66 explicitly states transitivity on the twenty-four nontrivial H5/Z characters. Its preceding representation classification supplies the unique five-dimensional irreducible for each nontrivial central character.

## Actual linearization audit

The proof does not substitute invariance of the thirty-point support for equivariance of the actual conductor. The ambient linear N-action restricts to O_S(1) because the actual closed subscheme S is invariant. Each automorphism of the integral S lifts uniquely to its normalization; uniqueness supplies the group law, not a merely projective action. The pullback line bundle, algebra inclusion O_S into nu_*O_X, and quotient T therefore have compatible genuine N-linearizations. The projection formula makes the twisted normalization sequence equivariant.

The scalar center fixes S and X pointwise, acts trivially on their structure sheaves and the untwisted conductor, and has fifth power one on the ambient polarization. Consequently degree-five cohomology carries an N/Z action. With H^1(X,5H)=0, its actual cokernel is H^1(S,O_S(5)). There is no hidden choice of a modular or Weil linearization.

## Representation and target audit

For any such module the twenty-four nontrivial G-character multiplicities are equal, since conjugation by N acts transitively on them. Its dimension therefore equals its invariant dimension plus a nonnegative multiple of twenty-four. A defect of dimension one through five must be G-trivial. This says nothing about triviality under SL2(F5).

Each direction L has an orbit of five eigenlines, with stabilizer exactly L; independent directions cannot share an eigenline by their nontrivial scalar commutator. At a node the length-one conductor is the quotient of the two residue fields by the diagonal. An odd-order stabilizer cannot exchange the branches and fixes each complex residue field, hence fixes this quotient. Every Heisenberg element has order dividing five, so its O(5)-fiber action at a fixed eigenline is trivial too. Each orbit module is therefore genuinely Ind_L^G(1), rather than an unspecified character twist.

Summing the six orbit modules gives six trivial characters and one copy of each of the twenty-four nontrivial characters. Exactness of invariants then proves every nontrivial target channel is hit and gives r_5=24+a, defect=6-a, with 1<=a<=5. The caution about normalizer branch signs and fiber scalars is essential and is correctly preserved.

## Seven-dimensional source audit

Set Q_2=im(rho_2). The pinned multiplication-generation identity gives the actual image of P_3 tensor Q_2 in T(5), so passing to invariants loses no image. As H5-modules, Q_2 is the five-dimensional irreducible with central character epsilon^2, and P_3 is seven copies of its dual, with character epsilon^3. Their tensor product descends to G and is seven regular representations: the character of End(Q_2) is 25 at identity and zero at every nonidentity G element. Thus the invariant source has dimension seven, intrinsically, without choosing an N-equivariant splitting into seven copies.

The resulting map 7 -> 6 has rank a, cokernel the entire degree-five defect, and kernel dimension 7-a=1+defect. This is valid for the actual image module, and does not confuse the conductor image with the full nonambient normalization quotient.

## Limits and conclusion

No correction is needed. The proof establishes a genuine reduction of the remaining rank question, not its solution. It does not identify the six-dimensional invariant target with the unsigned permutation representation or with 1+5; it does not determine a, construct a rank-test matrix, or settle the separate residual/full-adjoint/source/algebraicity questions. Determining the normalizer stabilizer character or the actual invariant multiplication remains additional work.
