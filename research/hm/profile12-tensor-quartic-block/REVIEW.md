# Independent review: tensor-quartic constant subsystem

## Verdict and exact object reviewed

**PASS, with the saturation boundaries stated in the proof retained.** No mathematical correction is required to the reviewed version. The theorem proves an actual fifteen-dimensional constant subsystem, the two specified sheaf intersections, and the stated locally free residual image sheaf. It does not prove that the residual image is saturated in the constant quotient.

The exact reviewed file is `PROOF.md`, with SHA256

    863bb17be118558b5c6199d0b3b73a7257cdd1f6871cdd903be2a19128574c98

The review did not modify that file. The conclusion is conditional on the actual formal profile-(1,2) hypotheses in the theorem, not a realization assertion for either source type.

The review independently checked:

- the pinned public inputs and the relevant source/label correspondence;
- the complete small rank-eight syzygy support and rank-three quotient list;
- saturation of the initial derivative image, rather than just local freeness of its source or image;
- the full constant-span argument and identification with the complete quartic evaluation sequence;
- the exact sheaf-kernel arguments for both intersections;
- the nonsplit Euler extension and the actual residual bundle type.

No actual HM/source coefficients, source-instance points, parameter choices, derivatives, matrices, or source-instance ranks were selected or evaluated. The only computation was small exact universal character arithmetic and the two complete support checks displayed below. No source-instance scan, large computation, or previously exhausted section-envelope scan was run.

## 1. Public input verification

The following files were read through the connected GitHub read interface at commit `db51525015bb7c5e825833d550d08dedf6f6ea96`:

1. [Actual equivariant splitting and Gauss persistence](https://github.com/Akilleez-QA/read-em-and-weep/blob/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load/ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md).
2. [Negative Gauss kernels strictly lower the top slope](https://github.com/Akilleez-QA/read-em-and-weep/blob/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load/NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md).
3. [Profile-(1,2) quotient pairs and zero defect](https://github.com/Akilleez-QA/read-em-and-weep/blob/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load/ONE-TWO-FINITE-QUOTIENT-PAIRS-AND-ZERO-DEFECT.md).
4. [The quotient-pair certificate](https://github.com/Akilleez-QA/read-em-and-weep/blob/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load/one-two-finite-quotient-pairs.json).
5. [The stable-label certificate](https://github.com/Akilleez-QA/read-em-and-weep/blob/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load/rank-three-quotient-frontier-144.json).

The [PR796 proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/d2b43060c83328dd5118aee6b9288fcfa0c873ac/research/hm/profile12-quadratic-block-exclusion/PROOF.md) was also read at the exact stated commit. The fetched text has SHA256

    622763aac375db7e17bc7cab472f1afda0477b0f769371a3b3ef845cd5c9e3b1

as claimed.

The certificates identify old pair 0 with `G3.12.37914c53373c`, A_q=O(-10)+O(-8)+O(14), and source IDs {0,3,6}. They identify old pair 12 with `G3.12.eed6acb13f3e`, A_q=W O(-9)+O(14), and source IDs {0,3,6,10,12,13}. Both original defects are zero. The relevant E-catalog tuples are

    entry 6:  (0,1,0,0,0,1,0,1),
    entry 13: (0,1,0,0,0,0,1,0),

which yield exactly the E6 and E13 splittings in the reviewed proof. PR796 supplies the stated removal of the other entries. Thus there are two surviving source types across three compatible label/source records: entry 6 for either label and entry 13 for the second label.

The inputs actually needed locally are the saturated actual inclusion E in H O, H0(E(1))=0, H0(E^-(2))=0, the genuine zero-defect quotient A_q=B_q^*(-2), and the interior identity (E^+)^-=E. In particular H0(E^+)=0 follows by taking the derivative of a constant section and using H0(E)=0. This review is not a new audit of every historical frontier computation or of realization of the catalog.

## 2. Independent character audit and the top-block kernel

The character arithmetic was recomputed exactly over Q(sqrt(5)), with the nine irreducible characters checked orthonormal. Symmetric powers were obtained from the universal recurrence

    Sym^0 W=1,  Sym^1 W=W,
    Sym^(n+1) W=W Sym^n W-Sym^(n-1) W.

Relevant results are

    Sym^6 W=V+P,             Sym^7 W=Wp+T,
    Sym^8 W=P+D,             Sym^16 W=V+P+2D,
    Sym^17 W=Wp+S+2T,
    V W=T,                   V A=P+D,
    V D=A+V+P+D,             Wp W=P,
    Wp A=T,                  Wp S=V+D,
    P W=Wp+T,                D W=S+T,
    T W=V+P+D,               W S=A+D.

The restriction F=(P+D) O(-2) -> A_q has no component in the two negative directions. Its nine degree-sixteen sections are independent because the quotient kernel is E^- and H0(E^-(2))=0. Its common divisor is invariant. A nonempty projective A5 orbit has size at least twelve: a point stabilizer is cyclic, and a cyclic subgroup of A5 has order at most five. A common divisor of degree at least twelve leaves at most five independent sections of O(16). Therefore the nine-section system is basepoint free and p:F->O(14) is a bundle surjection.

Consequently K0 has rank 8, degree -32, every ordinary degree at most -3, and

    H1(K0(2))=V+D,
    chi_G(K0(3))=(P+D)W-Sym^17 W=0.

For an irreducible R O(-j), j>=4, its contribution R Sym^(j-4)W must fit within V+D. The complete dimension bound is (j-3)dim R<=8. Central parity must match j. The only supported contributors are:

| Block | H1 at twist 2 | H1 at twist 3 |
|---|---|---|
| V O(-4) | V | 0 |
| D O(-4) | D | 0 |
| Wp O(-7) | V+D | T |
| O(-8) | D | S |

For completeness, the eliminated degrees are not being hidden behind a search: j=5 permits only W or Wp, giving 1+A or P; j=6 permits only the trivial coefficient, giving A; j=7 additionally permits W, giving A+D; j=9 and j=11 have no odd coefficient small enough; j=10 gives V+P; j>=12 exceeds the bound. At j=4 the budget permits only V,D, and at j=8 only the trivial coefficient fits.

The V+D budget can therefore be filled only by V(-4)+D(-4), V(-4)+O(-8), or Wp(-7). Degree -3 blocks contribute H0, but no H1, at twist 3. The zero Euler character uniquely forces their coefficient representations to be 0,S,T, respectively. This gives exactly

    (V+D) O(-4),
    S O(-3)+V O(-4)+O(-8),
    T O(-3)+Wp O(-7).

All have rank 8 and degree -32. The syzygy list in the proof is complete.

## 3. Initial derivative saturation is genuinely proved

The map kappa:K0->(E/F)(-2) is well defined using the original constant connection. Its Leibniz correction is in F. Ordinary degree comparison kills every component for the first kernel type. For the second, the only additional possibility is O(-8)->T O(-5), whose equivariant Hom vanishes because Sym^3 W=S contains no T.

For the third type the only possible component is Wp O(-7)->T O(-5). Its equivariant Hom is one dimensional because Wp tensor A=T. A nonzero representative is, for every line l in W, the inclusion

    Wp tensor l^2 -> Wp tensor Sym^2 W.

It has rank two at every point. Hence its image J is saturated in the actual internal target, not merely locally free. The zero case is also saturated.

Here is an explicit check of the saturation step for the full image I. Put

    A_internal=(E/F)(-2),
    B_ambient=(H O/F)(-2),
    L=O(14) subset Q(-2).

The image of I in Q(-2) is exactly L, and I intersect A_internal=J. Thus

    0 -> J -> I -> L -> 0,
    0 -> A_internal/J -> B_ambient/I -> Q(-2)/L -> 0.

The last sequence has locally free end terms: the first by the preceding explicit map, the second by the zero-defect original quotient and its direct O(14) summand. Its middle term is therefore locally free. This proves the required saturation of I. No general inference from “locally free image” to “saturated image” is being used.

If J=0, the exact forward sequence yields rank(F^+)=10 and deg(F^+)=-2, hence chi(F^+)=8>0, contradicting H0(E^+)=0. Therefore the third kernel type occurs with J=Wp O(-7). The resulting forward transform has rank 12, degree -12, and no H0. Every splitting degree is at most -1, so all twelve degrees equal -1. Finally

    chi_G(I(3))=Sym^17 W-Wp Sym^2 W=Wp+S+T

gives F^+=(Wp+S+T) O(-1). The twists and degree calculations are correct.

## 4. Complete rank-three quotient classification

The exact, unsaturated-up-to-torsion quotient X=F^+/F has rank 3, degree 6, and degrees at least -1, since X(1) is globally generated. Cohomology gives

    H0(X)=P+D,    chi_G(X(-1))=T.

There are exactly eleven equivariant splitting types satisfying just rank, degree, central parity, and the lower degree bound:

- the three trivial-line patterns (0,0,6), (0,2,4), (2,2,2);
- R O(d)+O(6-2d), for R=W or Wp and d=-1,1,3;
- A O(2) and V O(2).

All eleven were checked. Exactly four have H0=P+D, with the following further Euler characters:

| Type | chi at twist -1 |
|---|---|
| V O(2) | T |
| Wp O(1)+O(4) | Wp+S |
| W O(-1)+O(8) | Wp+T-W |
| Wp O(-1)+O(8) | T |

Thus only the first and last remain. In the last type, the O(8)->O(16) component of the exact quotient sequence vanishes: Sym^8 W=P+D has no invariant. Exactness would then inject O(8) into Wp O(-5), impossible. Hence X=V O(2), and the genuine exact sequence is

    0 -> Wp O(-5) -> V O(2) -> O(16) -> 0.

This excludes the spurious alternative using the actual quotient map, not just an Euler-character comparison.

## 5. Full constant span and the tensor-quartic identification

For a pure degree -1 subbundle of a constant bundle, choose an affine trivialization of O(-1). Every inclusion column is a linear polynomial v+z w. Its value and first derivative span v,w at every point of that chart. Repeating on the other chart or using saturation shows that the first forward transform of F^+ is exactly its full constant span C0 O. No source-instance values are needed.

Since F^+ is saturated in H O, the quotient C=(C0 O)/F^+ is a vector bundle. It is globally generated. A global section of C* would be a constant functional annihilating F^+, hence annihilating its entire constant span; it must vanish. Thus every splitting degree of C is positive. Its degree is 12.

The derivative of F^+ kills F and factors through X=V O(2); its saturated image is C(-2). Therefore 1<=rank C<=3. Rank one would require V in Sym^8 W, which is false. At rank two, an irreducible two-dimensional coefficient would have degree 6, contradicting central parity. The possible line pairs are (2,10),(4,8),(6,6). Among their components, a map V O(2)->O(c-2) is possible only when c=10, since the only relevant occurrence of V is in Sym^6 W. Consequently rank two cannot have generic derivative rank two.

It follows that rank C=3. The induced map V O(2)->C(-2) is generically full rank with source and target both of degree 6. Its determinant has degree zero and is nonzero, so the map is an everywhere isomorphism. Thus C=V O(4).

The cohomology vanishings of F^+=O(-1)^12 identify C0 with H0(V O(4)), and identify the quotient map with the complete evaluation map. Hence

    C0=V tensor Sym^4 W=A+V+P+D,
    F^+=V tensor U_3^4.

The backward kernel in this complete quartic subsystem is V tensor U_2^4. It contains F because the derivative of F lies in F^+. Both have rank 9 and degree -18. Their inclusion is therefore an equality; equivalently, saturation precludes a nonzero torsion discrepancy. This proves the actual subsystem, not just its representation character.

## 6. Exact intersections, without fiberwise overclaiming

Let G0=E intersect F^+. The projection of F^+/F into E^+/E is the exact O(16) quotient just obtained, because the original derivative image is saturated. Therefore

    G0/F=Wp O(-5),    F^+/G0=O(16).

The derivative of F^+ modulo F^+ gives an isomorphism

    F^+/F -> ((C0 O)/F^+)(-2).

Composing with the natural map to (H O/E^+)(-2), its kernel on F^+ is exactly E intersect F^+=G0, by (E^+)^-=E. Taking the corresponding quotient by F therefore identifies the kernel on the right with Wp O(-5). By the definition of an intersection as a sheaf kernel, this proves

    Nplus/F^+=Wp O(-3),    (C0 O)/Nplus=O(18).

The last identity also proves Nplus saturated in C0 O, of rank 14 and degree -18.

The derivative of Nplus inside the actual constant subsystem has target O(16). Its restriction to F^+ is already the onto map F^+->O(16). Hence it is onto. The natural map O(18)->H O/E^+ is a sheaf injection, and that is sufficient to identify its derivative kernel with E intersect C0 O. Tensoring a sheaf injection by the line bundle O(-2) preserves injectivity. No fiberwise injectivity of that map is required. Thus

    0 -> N -> Nplus -> O(16) -> 0,
    N=(Nplus)^-,    rank N=13,    deg N=-34.

Both successive quotients of C0 O by N are vector bundles, so N is saturated in C0 O. In particular the asserted saturation of these two intersection sheaves is valid. It does **not** imply that their fibers are the full fiberwise intersections with E or E^+: base change of the intersection kernel can fail where the relevant projected image is not saturated. The reviewed proof correctly keeps these two statements separate.

## 7. Euler extension and residual image

The map N->Nplus/F^+ is onto locally: lift a local quotient section to Nplus and subtract a section of F^+ with its prescribed derivative in O(16). Its kernel is G0. Dividing by F gives the actual extension

    0 -> Wp O(-5) -> N/F -> Wp O(-3) -> 0.

Its equivariant Ext group is

    (End(Wp) tensor H1(O(-2)))^G=C.

Here H1(O(-2)) is the trivial representation for the standard SL2 linearization, and Schur's lemma gives the one-dimensional invariant endomorphisms. If the extension split, its Wp O(-3) summand would map to E/F with zero component in T O(-3), by inequivalence of Wp and T, and zero components in every lower-degree summand, by degrees. That contradicts the sheaf inclusion N/F->E/F. Thus the extension is nonzero and is the Euler sequence tensored with Wp:

    N/F=(Wp tensor W) O(-4)=P O(-4).

The extension by F splits equivariantly as a bundle because H1(O(2))=0, with finite-group averaging if needed. Therefore

    N=(P+D) O(-2)+P O(-4).

This does not give a splitting of the ambient constant connection.

The inclusion P O(-4)->E/F has only its T O(-3) component. Its equivariant Hom is one dimensional, since P occurs once in T tensor W=V+P+D. It is nonzero, and the standard representative is Wp tensored with the complete quadratic evaluation kernel

    0 -> W O(-4) -> Sym^2 W O(-3) -> O(-1) -> 0.

This map is fiberwise injective with locally free quotient. It follows that the quotient inside E is exactly

    Z=Wp O(-1)+O(-8)+O(-10)  for E6,
    Z=Wp O(-1)+W O(-9)       for E13.

Both types have rank 4 and degree -20, agreeing with rank(E)-rank(N)=4 and deg(E)-deg(N)=-20.

Finally, the projection E->(H/C0) O has sheaf kernel N by definition. Therefore the induced morphism Z->(H/C0) O is a sheaf injection and identifies Z with the actual image. It has generic fiber rank four. Nothing in this argument forces its cokernel to be locally free.

## 8. Required qualifications and fixes

No correction to the reviewed hash is required. The following restrictions are essential parts of the valid conclusion:

1. Saturation of Z in (H/C0) O remains open. Local freeness of Z, including the explicit splitting just proved, does not settle it.
2. Saturation of O(18)->H O/E^+ remains open. A sheaf injection can lose rank on fibers.
3. The two intersection formulas are exact sheaf statements. They do not identify the full pointwise intersections at all points.
4. Neither a horizontal splitting of the residual extension nor a constant direct-sum splitting E=N direct-sum Z is proved.
5. Neither surviving profile-(1,2) label is excluded. The separate source2 case is untouched.

Within those expressly stated boundaries, every step needed for the tensor-quartic subsystem, intersection degrees/types, and rank-four degree-minus-twenty residual image is justified.
