# A faithful linear vertex formula for the fifth adjoint boundary

## Statement and pinned dependencies

Work with the actual quadric cone Q, vertex L=P(W), positive binary space U, and the fixed physical-even marking. Write B=End_0(F), q for the ambient cone equation of twist two and cover weight four, and J for the ideal of L in Q. Fix the classified source and fourth lift K=a_source J4 in B_(4Q)(12). Its restriction is a_source^4 h N. No actual coefficient or source value is evaluated below.

The dependencies are:

- PR770, b242300110c33627eb77ee5ab36cc81fffa359e4: the exact stack-square trace map tau=tr(N−) induces H1(B_Q(4))_+ ≅ H1(Qsq)_+, where Qsq=pi_*(I_Z^2(6)), and the exact second-symbol image V_a must still be quotiented.
- PR773, 53209eb6d4e45883ce0f31dd6d9b1c191bd6c4a3: conic normalization and the vertex square filtration, including its degree-eight relation P4 O_L(-2).
- PR774, eec909bef4a7e6998737773d5eadd0ad562e79d9: regular physical matrix filtration, with entry degrees d,d−2,d+2 at matrix weight d.
- PR775, af2fc052d3da2c4abc315dca268ed65b62f5cde5: the global total-weight bound K≥12, physical-even weights in 4Z, and the fixed homogeneous harmonic convention.
- PR777, 490337fee9e8f06fa8bf3e893ab646a37f996bf2: regular local normalization N=n8+terms of weight at least16, and the corresponding elimination of B0 below.
- PR778, e527b939f9a8f5cf8967f32048a23a9d830d77c9: exact homogeneous triangular reference transitions T0 and their first ambient correction qZ0.
- PR779, 89e02759fde0924a787a8f145d814aceaab93c40: the actual class of that correction is nonzero. It cannot be discarded by an asserted global normalization.

All subscripts + below mean the invariant direct image under the finite quotient by physical inversion, or equivalently the positive summand of a physical-involution-stable Čech complex. In characteristic zero this operation is exact and its cohomology equals the positive eigenspace of the original cohomology. These are sheaves on the quotient, not O_Q-submodules closed under multiplication by odd functions. Every filtered sequence below is first an equivariant sequence and is then passed through this exact operation.

Immutable proof links for the pinned dependencies:

- [PR770 proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/b242300110c33627eb77ee5ab36cc81fffa359e4/research/hm/faithful-fifth-norm/PROOF.md).
- [PR773 proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/53209eb6d4e45883ce0f31dd6d9b1c191bd6c4a3/research/hm/fifth-norm-finite-jet/PROOF.md).
- [PR774 proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/eec909bef4a7e6998737773d5eadd0ad562e79d9/research/hm/matrix-jet-filtration/PROOF.md).
- [PR775 proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/af2fc052d3da2c4abc315dca268ed65b62f5cde5/research/hm/first-subleading-norm-formula/PROOF.md).
- [PR777 proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/490337fee9e8f06fa8bf3e893ab646a37f996bf2/research/hm/global-subleading-residue/PROOF.md).
- [PR778 proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/e527b939f9a8f5cf8967f32048a23a9d830d77c9/research/hm/normal-transition-channel/PROOF.md).
- [PR779 proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/89e02759fde0924a787a8f145d814aceaab93c40/research/hm/normal-extension-comparison/PROOF.md).

We prove that the weight-zero part of the fifth gluing discrepancy detects its entire physical-even cohomology class. Its explicit formula involves only B2,B3 and A1,A2,A3 in the normalized notation below. Neither B1 nor A0 occurs in this linear formula. Only harmonic product operators of order at most two are required. The statement is about the actual boundary map, not a generic dimension count or evaluation of its value.

## 1. The leading trace comparison is an isomorphism

All weight-zero trace-free coefficients have form X0=[[x,0],[z2,-x]]. They form the actual triangularly glued bundle J0. At physical twist four, the earlier exact identification is J0(4)=P4 O_L(-2). The physical-even filtration of B_Q(4) has no negative weights. Its leading quotient is J0(4), so restriction and leading-coefficient extraction define a sheaf morphism to the pushforward of J0(4) from L. This is a quotient of filtered sheaves, not an arbitrary harmonic projection of a global matrix.

Put A_L=ker(O_Q(6)→R_L), where R_L is the vertex part of the ordinary STACK-square quotient. The established square filtration gives, in the physical-even sector,

    0 → (J^6 O_Q(6))_+ → (A_L)_+ → P4 O_L(-2) → 0.       (1)

Indeed the first even relation is in J-order four, binary-cover degree eight, and the even quotient is killed at order six. The map in (1) takes this leading relation; no splitting of the actual square thickening is presumed.

The ambient even quotient O_Q(6)/J^6 O_Q(6) has split coefficient bundles

    O_L(6),  Sym4 U ⊗ O_L(4),  Sym8 U ⊗ O_L(2).

Its H1 is zero, and its global sections lift by the corresponding ambient homogeneous polynomial pieces. Since H1(O_Q(6))=H2(O_Q(6))=0, the restriction exact sequence gives both

    H1(J^6 O_Q(6))_+=H2(J^6 O_Q(6))_+=0.                (2)

Thus (1) induces an isomorphism on H1. The conic and vertex supports are disjoint, and the physical-even conic quotient O_C(6) lifts by degree-twelve cover polynomials vanishing on R_L. The conic normalization from PR773 therefore identifies H1(Qsq)_+ with H1(A_L)_+. This explicitly accounts for the entire cone; it is not a merely formal-neighborhood assertion.

In a regular normalized frame write

    n8=u [[f3 g5,-f3^2],[g5^2,-f3 g5]],

where u is a base unit and (f3,g5) is a regular binary cubic/quintic pair on every fiber. Leading trace sends

    X0 ↦ u(2 f3 g5 x − f3^2 z2).                       (3)

The degree-eight even square relation is exactly the span of f3 g5 and f3^2 Sym2 U, with its actual nonsplit transition law. Formula (3) maps onto it. It is injective: 2g5 x=f3 z2 implies x=0 by relative regularity, and then z2=0. Equivalently this can be checked over the function field and extended by the already established fiberwise regularity; it is an isomorphism on every fiber of the relation bundles. The determinant and coefficient twists are those of tau:B_Q(4)→O_Q(6), so (3) is a bundle isomorphism J0(4)→P4 O_L(-2), not an identification of two spaces merely having rank four.

For any even section of B_Q(4), its weight-zero coefficient is the only term that can contribute to the cover-degree-eight coefficient of its trace with N. Higher matrix weights have strictly larger trace weight, while N starts in weight eight. Thus the maps just constructed form a commuting square on H1: leading extraction followed by (3) equals tau_* followed by conic normalization and (1). The latter three maps are isomorphisms, by PR770 and (2). Hence

    E:H1(B_Q(4))_+ → H1(L,J0(4))                      (4)

is an isomorphism. This proves faithfulness with the correct global, conic and stack-square interfaces.

## 2. Exact normalized overlap formula

Choose regular normalized physical frames on negative-coordinate affine charts, and their ambient lifts. Fix one overlap and express everything in chart i, including homogeneous coordinate substitution, the twist-twelve scalar transition, and the transformation of the local equation q. The displayed formulas below are in that common trivialization; in particular powers of q are transformed before coefficients are compared. This convention prevents loss of the normal-line twist: division by q^4 changes twist twelve to twist four.

Modulo scalar transition factors, which do not affect adjoint transport, PR778 gives

    T_ij=T0_ij(1+q Z_ij+terms of matrix weight at least8),
    T0=[[alpha,0],[c,delta]],  Z=[[t,0],[ell,-t]].       (5)

Here alpha,delta are base units; c and ell are ordinary transverse-linear forms (binary degree two). T0 has an exact multiplicative ambient lift, not a guessed harmonic lift of a general transition. Z is weight zero with normal-ideal twist minus two. Its twisted Čech class is the actual nonzero κ of PR779.

PR775 §1 proves globally, in the regular adapted physical frames, that K has total matrix weight at least twelve. Together with physical-even weights in 4Z, its first possible weights are twelve and sixteen. Use the fixed homogeneous harmonic lifting H from cone coefficients to ambient polynomials of PR775. Consequently the only pieces of K relevant at total weight sixteen are

    K12=Σ_(r=0)^3 q^r H(A_r),
    K16=Σ_(s=1)^3 q^s H(B_s).                         (6)

The matrix weights are wt(A_r)=12−4r and wt(B_s)=16−4s. PR777 kills B0 by regular local normalization, not by a global frame. Local q^4 corrections allow B4=0. They change a boundary representative only by a coboundary. All coefficients in (6) are those AFTER these changes, not the old untransformed coefficients.

Adopt the Čech boundary convention c_ij=(K_i−T_ij K_j T_ij^-1)/q^4. If an opposite convention is used, all displayed cocycles change sign together. Since K glues on 4Q and the first nonscalar transition correction qZ raises matrix weight by four, K_i12−Ad(T0)K_j12 is already divisible by q^4. Its quotient would have matrix weight minus four, which is impossible for a regular physical-even matrix; hence this total-weight-twelve discrepancy vanishes identically in the ambient reference. Weight considerations and (5) give the boundary's weight-zero part exactly as

    C_ij=[q^4](K_i16−Ad(T0)K_j16−q Ad(T0)[Z,K_j12]).   (7)

The coefficients here are polynomial harmonic coefficients, not restriction to q=0 before division. Higher transitions have weight at least eight; multiplied by K12 they have weight at least twenty, and after division by q^4 retain positive weight. Higher pieces of K likewise do not enter. The expression (7) is therefore the actual leading boundary cocycle in J0(4), and (4) makes its class faithful.

## 3. A universal harmonic degree bound

For a scalar cone coefficient v and an ambient transverse polynomial p, define

    D_r(p,v)=[q^r](p H(v)),

with the resulting harmonic coefficient understood as a cone coefficient. This notation includes nonharmonic p such as c^2. If p has ordinary transverse degree m, then D_r(p,v)=0 for r>m.

For completeness, multiplication of a harmonic homogeneous polynomial by one transverse linear form has harmonic decomposition only in orders zero and one: subtracting its harmonic top component leaves q times a harmonic polynomial of degree one less than the original harmonic input. This follows directly from the Laplacian identity for a linear multiplier and a harmonic input, with the nonzero usual homogeneous-degree denominators in characteristic zero. Iterate this identity over a product of m linear forms, and use linearity to treat every degree-m polynomial p. Each multiplication adds at most one q, proving the bound. This is a universal polynomial identity, not a selected-instance derivative evaluation.

For X=[[x,y],[z,-x]], direct matrix multiplication yields

    Ad(T0)X:
      diagonal = x−c y/delta,
      upper    = alpha y/delta,
      lower    = delta z/alpha+2c x/alpha−c^2 y/(alpha delta).   (8)

Also Ad(T0)[Z,X] has

    diagonal = −(ell+2ct/delta)y,
    upper    = 2alpha t y/delta,
    lower    = 2delta ell x/alpha−2delta t z/alpha
               −2c ell y/alpha−2c^2 t y/(alpha delta).         (9)

Every multiplier in (8) and (9) has transverse degree at most two. In (7), B1 would require harmonic order three, so it contributes zero; A0 would also require order three after the prefactor q, so it contributes zero. The remaining orders are respectively two and one for B2,B3, and two, one and zero for A1,A2,A3. This remains true when T0 mixes harmonic coefficients: it is precisely that mixing which D1 and D2 retain.

## 4. Ordered formula with no hidden matrix operations

Write A_r=[[x_r,y_r],[z_r,-x_r]] and B_s=[[b_s,e_s],[g_s,-b_s]] in chart j and transport all scalar and equation factors into chart i as specified above. Introduce matrices M2,M1 and N2,N1,N0, all with upper entry zero and lower-right entry the negative of the diagonal, by

    diag M2=0,
    low  M2=−D2(c^2,e_2)/(alpha delta);

    diag M1=−D1(c,e_3)/delta,
    low  M1=2D1(c,b_3)/alpha−D1(c^2,e_3)/(alpha delta);

    diag N2=0,
    low  N2=−2D2(c ell,y_1)/alpha
             −2t D2(c^2,y_1)/(alpha delta);

    diag N1=−D1(ell+2ct/delta,y_2),
    low  N1=2delta D1(ell,x_2)/alpha
             −2D1(c ell,y_2)/alpha
             −2t D1(c^2,y_2)/(alpha delta);

    diag N0=0,
    low  N0=2delta(ell x_3−t z_3)/alpha.              (10)

Here A3 has weight zero, so y3=0, x3 is a base coefficient and z3 is transverse-linear. Thus no harmonic correction is needed in N0. Since the local K_i16 in (6) has no q^4 coefficient, the promised formula is

    C_ij=−M2−M1−N2−N1−N0.                           (11)

Formula (11) is linear in the source-section jets A and B, with the actual transition jets fixed. The base functions alpha,delta are transition entries and have no relation to the source polynomial a_source. Every term has matrix weight zero and physical twist four after equation-line transport. In particular its diagonal has binary degree zero and its lower entry binary degree two. The formula is on ordered overlaps; reversal uses the J0(4) transport, not entrywise negation in unrelated frames.

## 5. Meaning, limitations, and the next exact test

The class [C] is E(delta5 K). Hence a fixed K extends to 5Q exactly when [C]=0. For the classified completion ambiguity, the actual criterion is

    beta4_a(h)=0  iff  [C] belongs to E(V_a),
    V_a=im(beta2_a).                                 (12)

No rank assumption or saturation of that exact image is allowed. A scalar norm reference is unnecessary for the direct formula (11); it was needed only by the quadratic norm construction. The full source data remain in A,B and V_a, so this does not remove the source divisors by generic division.

The disappearance of B1 and A0 is a coefficient-level exclusion from the faithful LINEAR cocycle. It is not an assertion that these jets vanish. In particular B1 can still occur pointwise in the quadratic norm expression of PR775. Once a legitimate global fifth-boundary class is formed, its value is determined by the remaining data through (11); changing only B1 in a compatible family cannot change that class. This is the rigorous cohomological redundancy statement. One must not claim that an arbitrarily isolated B1 summand of the norm formula is itself a cocycle, or that each such summand separately vanishes pointwise. Any stronger term-by-term removability claim would need that extra compatibility proof.

The nonzero κ is retained through N2,N1,N0. Its nonvanishing does not imply that their pairing with this section is nonzero, and neither (11) nor (12) evaluates beta4. The next useful step is to understand the class of this explicit cocycle modulo E(V_a), by structural means within the established scope.

The source comparison is targeted: PR773 gives a scalar finite-jet reduction, PR775 its quadratic formula, PR778 its ambient transition channel, and PR779 its nonzero class. None of those assertions supplies the direct linear formula, its faithful leading extraction, or the order-three exclusion proved here. The work uses universal triangular matrix identities, polynomial harmonic decomposition, regular-pair geometry and line-bundle cohomology only. It is authored mathematics, not formal proof-assistant verification; no actual coefficients, points, ranks, derivatives, source instances, scans or large computations were evaluated.
