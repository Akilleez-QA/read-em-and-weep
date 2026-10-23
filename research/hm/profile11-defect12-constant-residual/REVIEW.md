# Independent audit of the defect-twelve constant residual

Audited frozen files (SHA-256):

    PROOF.md
    0e28eed42faf99a0ebaed4bfcf7e54b20f0e13d642f92f61864e421043e71915

    UNIVERSAL-RESIDUAL-COMPATIBILITY.md
    4fe2d9ae2b6396ff43a3438d31f742451d2461daeb196aca5e6ed534a7f08feb

Neither audited file was modified. This review does not incorporate any subsequent delta-zero endpoint closure, which would require a separate argument and review.

## Verdict

The stated source reductions and saturated residual theorem are valid. I found no substantive mathematical gap in `PROOF.md`, and no required change to its conclusions. In particular, the proof does not accidentally replace the defective external line by a saturated line in the delta-zero branches, and it does not import the profile-(1,2) interior-stage hypothesis.

The surviving E10 residual is a necessary condition, not a full-label exclusion or an actual HM realization. The separate `UNIVERSAL-RESIDUAL-COMPATIBILITY.md` construction is also valid within its explicitly abstract scope.

This audit used only the universal bundle and connection arguments, bounded representation identities, and read-only inspection of the pinned public inputs. It used no selected actual coefficients, parameter values, points, derivative evaluations, matrices, source-instance ranks, experiments, scans, or large computation.

## Checks of the five main risks

### 1. Full-image saturation despite the defective external line

Section 3 is correct. Put N=(E/F)(-2) and M=(H O/F)(-2). Since N is saturated in M and J is saturated in N, J is saturated in M. The needed equality

    Ibar intersect N = J

follows from I intersect N=J and saturation: both intersections have the same generic rank, while a section of their quotient would be torsion in N/J. Therefore Ibar/J injects into Q(-2); its image is a line subsheaf of L containing L(-D12). The resulting divisor D' satisfies 0<=D'<=D12, and

    length(Ibar/I) = 12 - degree(D').

The equivariant defect divisor has degree at most twelve. The minimum projective orbit size is twelve, so its length is exactly zero or twelve. This argument permits I to be saturated when its projection to Q(-2) is not saturated. The distinction between the original defect and delta is preserved.

### 2. Negative-to-positive off-diagonal terms

Section 2 does not require these components to vanish. The original injection has block form

    (negative,positive) -> (a negative, c negative + f12 positive),

where a is an automorphism. The positive-to-negative component vanishes by degrees. The negative diagonal blocks are nonzero constants, with the unequal-line off-diagonal ruled out by the absence of an invariant binary quadratic; for W O(-9), Schur's lemma applies. Generic invertibility of the full map forces a to be invertible.

Passing to the quotient by the saturated positive line kills c, leaving precisely a. Thus the later Gauss-quotient argument is unaffected by these terms.

### 3. Saturation of the residual after delta twelve

For delta=12, D'=0. If F^+=C O, its image in Q is exactly L(2)=O(28), not merely a generically equal line sheaf. This line is saturated in Q. Hence E+C O is saturated in H O and

    Z=E/(E intersect C O) -> (H/C) O

is a saturated inclusion. This is a valid quotient argument; no constancy of an unproved fiberwise intersection is being assumed.

For rank F=14 and J=0, the kernel of C O -> O(28) is precisely F, so the claimed rank-three residual types and degree -26 follow. For rank F=9 and J=Wp O(-7), the actual intersection quotient is Wp O(-5), and its standard saturated inclusion into T O(-3) has quotient P O(-2). The stated residual types in Section 5 follow.

### 4. Actual Gauss quotient of the residual

Projection by the genuine constant space C commutes with the original connection. Its induced normal target is Q/O(28). The original derivative, followed by this quotient and twist, is the surjection E -> A_neg followed by the saturated negative inclusion. It kills E intersect C O because derivatives of sections valued in the constant space C remain valued in C. Therefore it descends to the actual derivative of Z, still surjectively onto A_neg and with saturated image. This establishes Z/Z^-=A_neg; it is not an assertion about a connection placed on an abstract complement.

The strict-top exclusions in Section 5 consequently apply to saturated negative bundles. The rank-three residual in either of the first two labels would have a degree -8 kernel line while maxdeg Z=-8. In the rank-six constant branch, the whole P O(-2) top block would be killed. Both contradict the strict-top theorem.

### 5. First-polar exclusion of E0 in the third label

For the third label, the kernel is O(-10), and its internal derivative lands in 2 O(-10). It cannot vanish identically: otherwise this saturated negative line would be horizontal in the actual constant quotient. A nonzero map here is a constant pair with no zero divisor, so its first forward transform is saturated, has rank two, and has degree -18.

The degree-ten first-polar map W O(-9) has exactly the value-plus-first-derivative image. It therefore surjects onto that transform and is an isomorphism, by equal rank and degree. This supplies the actual tangent subbundle W O(-9), rather than assuming one.

In E0, each component W O(-9) -> O(-8) belongs to the same one-dimensional equivariant Hom space, and the component to O(-10) is zero. Every such map has generic rank at most one, contradicting the rank-two inclusion. In E10, the projection to W O(-9) is a nonzero scalar. Removing its graph component by an equivariant bundle automorphism is legitimate and does not assert a horizontal splitting. The O(-10) kernel has zero component in O(-8), since Sym2 W has no invariant, and is the standard tautological subline of W O(-9).

## Imported arguments and degrees

- The three source-index lists, labels, original defects, and quotient types were checked against the JSON files at db51525015bb7c5e825833d550d08dedf6f6ea96. The E1 and E11 top blocks are indeed 2P+D, so their multiplicity exclusions are correctly included.
- The displayed source types follow from the pinned eight-row catalog. Their ranks and degrees are consistent. The extra top blocks of dimension thirteen have already been excluded before the remaining dimensions 14,12,10,9 are listed.
- PR796's profile-free quadratic gap uses only the actual quadratic inclusion and its saturated transforms. It is applicable at an endpoint.
- For E18 with nonzero J, the raw degree is -10. Hence delta=0; the exact saturated sequence used in PR799 is recovered. PR799 Sections 4-5 thereafter use no original zero-defect hypothesis, so the transfer is sound.
- For E6/E13, nonzero J has degree -14 and rank two, giving raw degree -12 and rank twelve. In the delta-zero branch, the first-polar generation argument forces every splitting degree of F^+ to be -1. This replaces, rather than silently imports, the interior-stage section vanishing in PR797.
- PR797 Sections 4-5 use only this pure-linear actual inclusion and the exact quotient sequence. Their proof of X=V O(2), constant span dimension fifteen, and tensor-quartic identification therefore transfers unchanged. The endpoint intersection statements in its later sections are not needed.
- The constant-character calculation in Section 7 has the correct degree: Sym28 W=A+V+2P+3D, so subtracting P+2D gives C=A+V+P+D.

The three inspected local dependency files exactly match the public Git blobs at the pinned commits:

    PR796: 46a0de762000f21182f6d3168f3ecfd63adaf75f
    PR797: f397008bad1724ba3e81bdf84b5071fbc516f015
    PR799: a62a56f6b8f97e02b3eab6fe3a47ec3bedb6c6b1

## Audit of the universal residual supplement

The Wronskian arguments are sufficient, including at all exceptional orbits.

For the six-dimensional A+V subsystem of degree ten, the Wronskian degree is 30. If second jets fail, a2>=3 in the increasing vanishing sequence, so each of indices 2 through 5 contributes at least one to the weight. An invariant orbit then contributes at least 12 times 4=48, impossible. Thus second jets have full rank everywhere.

For the four-dimensional P subsystem of degree eight, the Wronskian degree is 20. First-jet failure forces weight at least three, hence total invariant contribution at least 36, again impossible. The systems are basepoint-free because an invariant common divisor would have degree at least twelve, exceeding their degrees.

Consequently the first polar of f is an everywhere rank-two saturated embedding, detected already by its A+V projection. The g line is everywhere independent through its P projection, so their direct sum is saturated. In the derivative quotient, the direction from the second jet of f is nonzero modulo its first jets in A+V, and the direction from the first jet of g is independent modulo g in P. These separated projections prove an everywhere rank-two derivative with kernel exactly f. No favorable member of the family is selected.

The multiplicity-free ambient character and the stated nonzero channels give its full constant span. This is a genuine family of abstract embedded residuals, not an extension to the original E or a realization of the full label.

## Optional exposition improvements; no substantive repair required

1. In Section 3, explicitly insert the equality Ibar intersect N=J and the one-sentence saturation argument above. This makes the zero-kernel assertion for Ibar/J transparent.
2. In Section 5, explicitly state that E intersect C O is killed by the projected derivative, because C is constant. This displays why the surjection onto A_neg descends to Z.
3. In the supplement, identify its Hbar with the actual quotient representation, rather than leaving that connection implicit. The pinned presentations give

       H=M3 tensor W-M2-M4=2(A+V+P+D).

   Since C=A+V+P+D, the actual H/C has exactly the proposed Hbar character. This strengthens the explanation of what residual constraints the abstract construction matches, without claiming actual-source realizability.

No full-label exclusion, higher-order actual-source compatibility, or algebraicity conclusion follows from this audit or from the supplement.
