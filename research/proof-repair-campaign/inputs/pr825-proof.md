# A degree-ten constant osculating block stops at the forward endpoint

## Result and scope

For either zero-original-defect maximal profile-(1,1) label

    G3.11.dc58cc54f352: A_q=O(-10)+O(-8)+O(26),
    G3.11.4b6dad66f329: A_q=W O(-9)+O(26),

assume the top degree-twenty-eight section system has common divisor of degree20. The published divisor reduction forces the matching source E6 or E13 and the actual constant osculating block

    F=U_8^10, F^+=U_9^10, C=Sym10 W, F^{++}=C O.

Then the exact sheaf intersections are necessarily

    E^+ intersect C O = F^+,
    E intersect C O = F.                              (1)

In particular C O is not contained in E^+. The image of E^-=K in (H/C) O has, at the generic point, the same subspace as the image of the T O(-3) summand of E/F. No assertion of global projection saturation is made in this surviving alternative.

This is a new necessary endpoint condition, not a full exclusion of either label or of the degree20-divisor stratum. The source2 branch is not under consideration. All maps below come from the original constant connection and actual quotient/intersection maps. No selected actual HM/source coefficients, parameters, points, derivative values, matrices, source-instance ranks, selected models, scans, or large computation are used.

## 1. Immutable inputs

The repository is Akilleez-QA/read-em-and-weep. The original source, quotient and plateau conventions are pinned at

    db51525015bb7c5e825833d550d08dedf6f6ea96,
    research/hm/order-four-quadratic-load/.

The exact files used are ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md, NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md, ONE-ONE-ENDPOINT-DEGREE-WINDOWS-AND-159-NECESSARY-PAIRS.md, one-one-endpoint-necessary-pairs.json, and rank-three-quotient-frontier-144.json. The labels have source indices112 and115 respectively.

The degree20-divisor reduction is PR813, commit

    3f99ecf539a3a3da61743df0dff409e54270c865,
    research/hm/profile11-o26-divisor-reduction/PROOF.md.

Every path is at https://github.com/Akilleez-QA/read-em-and-weep/blob/COMMIT/PATH with the displayed immutable COMMIT and PATH.

Work over C with binary icosahedral group G and standard notation W,Wp,A,V,P,S,D,T. Thus Sym5 W=T, Sym6 W=V+P, Sym7 W=Wp+T, Sym8 W=P+D, and Sym10 W=A+V+D. All irreducibles are self-dual. The actual E has H0(E(1))=0, is saturated in H O, and has Gauss quotient A_q. Original defect zero gives the saturated exact quotient

    E^+/E=A_q(2)=O(28)+L(2),                           (2)

where L=O(-8)+O(-10) for E6 and L=W O(-9) for E13. In both cases

    E/F=T O(-3)+L.                                    (3)

Maximal backward index one requires rank beta_(E^-)<3.

The common divisor of degree20 is a reduced invariant orbit, with equation f20 unique up to nonzero scalar. The actual map F->A_q has image f20 O(6) in O(26). Hence the map F^+->E^+/E has image f20 O(8) in O(28), and kernel F. PR813 also gives the actual constant C and the displayed complete osculating identities. Apolarity gives

    (C O)/F=W O(9), (C O)/F^+=O(10).                  (4)

## 2. There are only two endpoint intersections

Since F^+ is saturated in the constant bundle and is contained in E^+, the saturated intersection E^+ intersect C O has rank10 or11. In rank10 it equals F^+ as a sheaf. In rank11 it equals C O. Indeed both sheaves are saturated in C O, and equal generic rank implies equality.

Assume for contradiction the second alternative:

    C O subset E^+.

The map C O->E^+/E has no component in the negative bundle L(2), so its image is a subsheaf of O(28). It contains the image f20 O(8) of F^+. Its zero divisor therefore divides the reduced degree20 orbit. Invariance leaves only image O(28) or f20 O(8).

If its image were f20 O(8), its kernel N=E intersect C O would have rank10 and degree-8. But any subbundle of E has every splitting degree at most-2, since H0(E(1))=0. A rank10 subbundle must then have degree at most-20, a contradiction. Consequently

    0 -> N -> C O -> O(28) -> 0,
    rank N=10, deg N=-28,
    0 -> F -> N -> O(-10) -> 0.                        (5)

The last sequence follows by quotienting by F in (4).

## 3. The constant projection gives a genuine negative residual subbundle

The derivative of N lies in C O, since C is constant. Its image in Q(-2) therefore lies in (C O/N)(-2)=O(26), which is exactly the positive part of A_q. Thus the actual map N->A_q has zero component in L. On the other hand, the map E/F=T O(-3)+L->L is zero on T O(-3) by degree, and an isomorphism on L by surjectivity of E->A_q. For L=O(-8)+O(-10), its two cross channels vanish by degree and the absence of an invariant quadratic; for L=W O(-9), Schur's lemma applies.

It follows that the O(-10) in (5) embeds entirely in T O(-3). This is a saturated subbundle there: N/F is saturated in E/F because N is the sheaf intersection with a constant subbundle, and its quotient E/N is torsion-free. Put

    Z0=T O(-3)/O(-10).

This is a bundle of rank5 and degree-8. Since it is a quotient of T O(-3), the bundle Z0(3) is globally generated. Every splitting degree of Z0 is therefore at least-3. No finer splitting or coefficient calculation is required.

The actual image of C O/N in Q is exactly the positive O(28) summand of E^+/E. It is saturated in Q: E^+/E is saturated because E^+ is a subbundle of H O, and O(28) is a direct summand of the quotient (2). Consequently E+C O is saturated in H O. Its quotient by the constant C O gives an actual saturated subbundle

    R=(E+C O)/C O = E/N

of (H/C) O. Quotienting (3) by the O(-10) subbundle, which lies entirely in its T factor, gives the abstract direct sum

    R=Z0+L.                                          (6)

Here both summands are actual subbundles of R, and R itself is actually embedded and saturated in the constant quotient. We have not inferred projection saturation merely from local freeness.

## 4. The top residual must be horizontal

Constant projection commutes with the original connection. Therefore the derivative of R lies in E^+/C O. Its quotient by R is

    (E^+/C O)/R = E^+/(E+C O) = L(2),                 (7)

because C O/N is exactly the positive O(28) part of (2). Thus the derivative of the top residual Z0 into the ambient quotient factors through the map

    Z0 -> L(2) tensor Omega1 = L.

It vanishes by ordinary degrees: every summand of Z0 has degree at least-3, while every summand of L has degree at most-8. Hence the derivative of Z0 lies in R. Its remaining internal derivative is the O-linear map

    Z0 -> (R/Z0)(-2)=L(-2),

which vanishes by the same degree comparison. The actual subbundle Z0 of the constant ambient quotient is therefore horizontal.

In characteristic zero a horizontal subbundle of a constant bundle is constant: its Grassmannian classifying map has zero derivative, hence is constant. Its degree is consequently zero. But deg Z0=-8. This contradiction excludes C O subset E^+.

## 5. Recover the stated exact intersections

Section2 leaves E^+ intersect C O=F^+. Intersecting with E and using the kernel statement following (4) gives E intersect C O=F. Since p:F->A_q has nonzero generic image in its positive line, the generic projection of E^- to E/F is the kernel of E/F->L. Equation (3) identifies it with T O(-3).

This proves (1) and the asserted generic projected-kernel description. It does not establish saturation of that surviving projection, constant separation of C, or a contradiction in the remaining alternative.
