# Independent review: length-twelve torsion and the actual cubic Wp subsystem

## Verdict

PASS, with no mathematical blocker found, for precisely the conditional statement in BALANCED-TORSION-CUBIC-SUBSYSTEM.md:

- label G3.11.73682b4c817f, source index 72;
- actual source E=P O(-2)+2T O(-3)+O(-10);
- actual quotient A_q=O(-10)+W O(5), original determinant defect zero;
- the restriction p:P O(-2)->W O(5) has generic rank two and is not onto.

The conclusion is the forced actual cubic Wp subsystem and exact top-image torsion length 12. This is not an exclusion, a realization, an assertion about the onto branch, or an assertion about all compatible source types for this label.

Reviewed proof SHA-256:

b1a6b94b0e1a7cce942af8e52d4bcc59317ce9d8c6823610e5d288da0c62429f

The reviewed proof bytes match this hash. Review date: 2026-10-23 UTC.

## Source pins checked

Original source commit: db51525015bb7c5e825833d550d08dedf6f6ea96.
Repository directory: research/hm/order-four-quadratic-load in Akilleez-QA/read-em-and-weep.

The following Git blob IDs were independently recomputed from the immutable input bytes using Git's blob header and SHA-1 convention, and match the proof's pins:

- ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md: b93e0b3589ef71cf2c029fd07a6bdb1da8ba92b3.
- NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md: d7506dae49b4be43230450c4132bd5db91f137ef.
- ONE-ONE-ENDPOINT-DEGREE-WINDOWS-AND-159-NECESSARY-PAIRS.md: dcacf0bcdef8377c1ed7654e5b82659ea409456e.
- one-one-endpoint-necessary-pairs.json: fe0afa410d89340d3082dc814277f89fbb582c19.
- rank-three-quotient-frontier-144.json: 8b5971092f9ef762584912609fd5e9301c4e271d.

The source-index-72 catalog entry has A_q=W O(5)+O(-10), B_q=W O(-7)+O(8), and defect zero. Its ten compatible tuples include (0,2,0,0,0,0,0,1), which the pinned E-catalog formula converts exactly to P O(-2)+2T O(-3)+O(-10). The frontier entry independently matches stable label G3.11.73682b4c817f to index 72 and these quotient data. The review does not replace the other nine compatible tuples by this one.

The first-polar sources read for this review are:

- PR799, commit 2172e4a7abbbe232f9f448bea6fa01dee7927460, research/hm/profile11-quadratic-polar-obstruction/PROOF.md. Input proof SHA-256: 3a55f2c37548c7b05bf0f39f775ab37807c9f852d3601f77271fc0dd052022ed.
- PR802, commit e484640a6565c278321bf6557860262c1ac1b7df, research/hm/profile11-o16-constant-span-exclusion/PROOF.md. Input proof SHA-256: a18a6990f719592d71853692157161a9ca5fe6b7f2a78edacbfa060bb3513459.

The universal first-polar argument is also verified directly below, so the review does not merely rely on a named predecessor lemma.

## 1. Rank-two top image and its complete splitting classification

Write I=im(p). A rank-two image sheaf on the smooth curve is locally free, and W O(5)/I is torsion of length d. Because the component F->O(-10) vanishes by degree, ker(p)=F intersect E^-. The strict-top vanishing H0(E^-(2))=0 therefore injects P=H0(F(2)) into H0(I(2)). The map F(2)=P O->I(2) is a sheaf surjection, so I(2) is globally generated and H1(I(2))=0. Consequently

4 <= h0(I(2)) = 2+deg(I(2)) = 16-d.

The nonzero torsion divisor is invariant. The minimum nonempty invariant divisor degree 12, together with d<=12, gives d=12. Thus deg I=-2 and H0(I(2))=P, not only equality of dimensions.

A globally generated rank-two degree-two equivariant bundle I(2) has ordinary degrees (0,2) or (1,1). In the first case the distinct rank-one slope pieces have trivial coefficient characters, because the binary icosahedral group is perfect. Hence I=O(-2)+O. In the second case center-evenness of I forces the rank-two coefficient at degree -1 to be center-odd, hence W or Wp. These are all possibilities. Their twist-two sections are respectively 1+A, 1+A, and Wp tensor W=P. Only I=Wp O(-1) survives.

The surjection P O->I(2)=Wp O(1) is the complete evaluation map: the induced section map is an isomorphism. Its Euler kernel, after twisting back, is K0=Wp O(-3).

## 2. Exact raw image does not require the external image to be saturated

Set B=beta_F(F), the raw derivative image in (H O/F)(-2). Projection to Q(-2) carries B onto the image of F under beta_E, namely I through the actual injection of A_q into Q(-2). If an element of B projects to zero, it is locally the derivative of a section in K0. The internal derivative of K0 takes values in

(E/F)(-2)=2T O(-5)+O(-12).

Every homomorphism from Wp O(-3) to this target is zero by ordinary degrees. Thus B->I is both surjective and injective as a sheaf map. This conclusion uses no saturation of I in W O(5).

Define the raw first span G as the inverse image of B(2) under H O->H O/F. There is an actual exact sequence

0 -> F -> G -> I(2) -> 0.

In particular G is locally free of rank six and degree -6, even before checking whether its ambient quotient is locally free.

## 3. The invariant torsion argument proves ambient saturation

Let M be the saturation of G in H O. It is equivariant, has rank six, and M/G is equivariant torsion. Its length e is the degree of an invariant effective divisor. Since M is a subbundle of a trivial bundle, every splitting degree of M is nonpositive. Therefore

0 <= e=deg M-deg G=deg M+6 <= 6.

If e were positive, invariance would require e>=12. Therefore e=0 and G=M=F^+.

This is a valid use of the invariant-divisor bound on the full ambient saturation defect. It does not confuse that defect with the distinct length-twelve defect of I inside W O(5).

For a quadratic inclusion with coefficient map P tensor Sym^2 W->H, at an arbitrary tautological line l the first polar image is the image of P tensor lW. Euler's identity includes the value itself in that image, and the remaining direction is the derivative. Thus the raw first span is the image of P tensor W O(-1). Since the raw span has now been proved saturated, this map surjects onto F^+. It follows that F^+(1) is globally generated while F^+ is a subbundle of a trivial bundle. Its degrees lie in {-1,0}; rank six and degree -6 force six copies of O(-1).

Twisting the exact raw sequence by one gives chi_G(F^+(1))=Wp tensor Sym^2 W=T. Hence F^+=T O(-1).

## 4. The linear coefficient-kernel lemma is exact, including its twist

Let M=U O(-1) be any saturated linear subbundle of a constant space, let C be its full coefficient span, and let a:U tensor W->C be its coefficient map. Write K=ker(a), and L=O(-1), the tautological line bundle.

At a line l, saturation of M means its value map U tensor l->C is injective. Thus K intersects U tensor l trivially. Projection through the equivariant Euler sequence

0 -> L -> W O -> L^* -> 0

injects K O into U L^*. Its image is the kernel of the induced map U L^*->(C O)/M. This induced map, twisted by L^2, is the derivative map M=U L->((C O)/M)(-2), up to the irrelevant nonzero scalar from a coordinate convention. Therefore

M^-=K O(-2).

Equivalently, the value and first derivative of a linear bundle span all of C at each line, so this induced derivative is onto its quotient; no generic-fiber argument or hidden torsion replacement is involved. This also verifies that M^+=C O.

Apply the lemma to M=F^+=T O(-1). The derivative of F lands in M, so F is contained in M^-. Because both are pure degree-minus-two bundles, this inclusion gives an actual coefficient injection P->K.

The character T tensor W=V+P+D is multiplicity-free. Also dim C cannot equal six: otherwise a saturated rank-six M contained in C O would equal C O, contradicting deg M=-6. Thus dim C>=7, and dim K<=5. Once P of dimension four is present, neither remaining constituent V nor D can fit. Hence K=P, C=V+D, and M^-=F exactly as embedded sheaves.

## 5. Complete classification of the actual constant quotient

The actual quotient Q_C=(C O)/M is locally free, globally generated, rank two, and degree six. Since H0(M)=H1(M)=0, the map C->H0(Q_C) is an isomorphism. Its presentation is therefore the complete evaluation sequence.

A degree-zero direct summand in Q_C would give a nonzero constant functional on C annihilating all of M's coefficients, contrary to the definition of C. Thus no such summand exists.

The proof's exclusion of a degree-one summand is valid: under a splitting of the complete evaluation quotient, the evaluation kernel and its derivative split inside the corresponding direct decomposition of H0(Q_C). An O(1) summand contributes an O(-1) summand to M with zero backward kernel. Therefore the derivative span of M^- cannot recover that summand, contrary to (M^-)^+=F^+=M. This is a statement in a genuine constant direct-sum decomposition, not an arbitrarily split nonconstant ambient connection.

There is also an independent shorter equivariant check here. In rank two and degree six, a degree-one summand would force the other degree to be five. The distinct rank-one slope pieces each have a one-dimensional coefficient character, necessarily trivial; their odd degrees would then make them center-odd, whereas Q_C is center-even. Thus (1,5) is impossible already by central parity.

With both degrees at least two, the exhaustive ordinary splittings are (2,4) and (3,3). The first has trivial coefficient lines. The second has a rank-two center-odd coefficient, necessarily W or Wp. The complete equivariant possibilities are exactly

O(2)+O(4), W O(3), Wp O(3).

Twisting the actual evaluation sequence by -1 yields

H0(Q_C(-1)) = H1(M(-1)) = T.

The three candidate section characters are W+S, W+S, and T. Thus Q_C=Wp O(3), with no omitted compatible splitting.

## 6. Actual cubic identification and determinant

The complete evaluation sequence for Q_C=Wp O(3) canonically identifies, up to equivariant bundle isomorphism, its constant source with Wp tensor Sym^3 W and its kernel with Wp tensor Sym^2 W O(-1). The actual embedded backward kernel established above is F, so the resulting flag is

C=Wp tensor Sym^3 W=V+D,
M=Wp tensor Sym^2 W O(-1)=T O(-1),
F=Wp tensor W O(-2)=P O(-2),
F^-=Wp O(-3).

The character identities used in this identification follow from the pinned products Wp tensor W=P, P tensor W=Wp+T, and T tensor W=V+P+D: Wp tensor Sym^2 W=T and Wp tensor Sym^3 W=V+D.

The original top map factors through F/F^-=Wp O(-1), identified with I. Its embedding into W O(5) has determinant in Hom(O(-2),O(10))=H0(O(12)); the determinant characters are trivial. On a smooth curve, the determinant vanishing multiplicities of a generically invertible square bundle map equal the local torsion lengths of its cokernel. Therefore its divisor is exactly the original top-image torsion divisor of degree 12.

## Review boundary

Only universal bundle exactness, equivariant splitting and representation identities, invariant divisor degrees, direct reading of the fixed source-index-72 metadata, and byte hashing were used. No actual HM/source coefficients, selected parameters or points, evaluated derivative values, instance matrices or ranks, models, scans, or large computation were selected or performed. This is a written mathematical review, not proof-assistant certification.
