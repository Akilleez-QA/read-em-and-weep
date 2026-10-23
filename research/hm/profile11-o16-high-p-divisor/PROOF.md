# The divisor-twelve high-P branch is impossible in four source127 edges

## Statement and boundary

For G3.11.cce6e3ba4eeb, source_index127, with actual quotient

    A_q=O(-8)+O(2)+O(16)

and original defect zero, consider the following four necessary source tuples:

    (0,0,1,1,0,1,0,0): E=(P+D) O(-2)+(V+P) O(-4)+O(-8);
    (0,1,0,0,0,1,0,1): E=(P+D) O(-2)+T O(-3)+O(-8)+O(-10);
    (0,1,0,0,0,0,1,0): E=(P+D) O(-2)+T O(-3)+W O(-9);
    (1,0,1,0,1,1,0,0): E=(P+D) O(-2)+Wp O(-3)+V O(-4)+Wp O(-5)+O(-8).

In every case the canonical P O(-2) subblock maps only to O(16). Its degree-eighteen line system must be basepoint-free. Equivalently, the only possible nonempty common divisor, of degree twelve, is impossible.

This is an exclusion of one formal branch in each of four edges, not an exclusion of any entire source edge or stable label. No compatible-pair decrement follows. The basepoint-free branch remains open in all four cases here. No selected actual HM/source coefficients, parameters, points, derivatives, matrices, ranks, selected models, scans, or large computation are used. The checks below are fixed abstract representation arithmetic and original-catalog reads.

## 1. Immutable input

The original actual bundle, strict-top, source and quotient data are at commit db51525015bb7c5e825833d550d08dedf6f6ea96:

https://github.com/Akilleez-QA/read-em-and-weep/tree/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load

The exact sources are ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md, NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md, one-one-endpoint-necessary-pairs.json, and rank-three-quotient-frontier-144.json. Their immutable paths and Git blob hashes are recorded in the accompanying input manifest. Entry127 and its stable label supply exactly the four tuples displayed above.

For the universal first-polar principle and small representation identities we use PR802, commit e484640a6565c278321bf6557860262c1ac1b7df, Sections3 and5:

https://github.com/Akilleez-QA/read-em-and-weep/blob/e484640a6565c278321bf6557860262c1ac1b7df/research/hm/profile11-o16-constant-span-exclusion/PROOF.md

For an independent numerical contradiction after saturation, the profile-free quadratic Gauss-gap lemma is in PR796, commit d2b43060c83328dd5118aee6b9288fcfa0c873ac, Section8:

https://github.com/Akilleez-QA/read-em-and-weep/blob/d2b43060c83328dd5118aee6b9288fcfa0c873ac/research/hm/profile12-quadratic-block-exclusion/PROOF.md

Work over C with the binary icosahedral group G, its defining two-space W, other two-space Wp, and representations A=Sym2 W, D=Sym4 W, T=Sym5 W, V of dimension3 and P of dimension4. Every nonempty invariant effective divisor on P1 has degree at least12. G is perfect, so invariant effective divisors have invariant defining sections with the standard line-bundle linearization. The actual E is saturated in a constant bundle H O and satisfies H0(E^-(2))=0. The raw derivative of E has the original saturated quotient A_q.

## 2. There is only one possible common-divisor degree

Put F=P O(-2), a saturated direct subbundle of the top quadratic block. Its maps to O(-8) and O(2) vanish, respectively by degree and by P not occurring in Sym4 W=D. Thus its external derivative is represented by

    p:F -> O(16).

Strict-top injects P into H0(O(18)), so this line system has four independent sections. A common divisor Delt of degree d would leave four independent sections of O(18-d), giving d<=15. If nonempty it has d>=12. Its defining section is invariant. Odd degrees have no invariants because the central involution acts with odd sign, and

    Sym14 W=A+V+P+D

has no invariant. Consequently the only possible nonempty degree is d=12.

Assume this case. Dividing by the entire common divisor leaves an onto system

    p0:P O(-2) -> O(4),
    0 -> K0(2) -> P O -> O(6) ->0.              (1)

It is onto because the full common divisor was removed. Since Sym6 W=V+P, its injection on sections has P image and H1(K0(2))=V. The kernel has rank3 and degree-12, and H0(K0(2))=0.

These constraints force the exact kernel

    K0=V O(-4).                                 (2)

For completeness, a block R O(-j), j>=4, contributes R Sym(j-4) W to H1(K0(2)), whose dimension is3 and sole constituent is V. The bound (j-3) dim R<=3 and center parity leave only V O(-4): at j4 the coefficient must be V; at j5 every odd irreducible is too large after multiplication by W; at j6 the scalar gives A, not V; and j>=7 exceeds the bound. The degree-minus-three blocks contribute no H1, but (2) already accounts for the full rank3, so none occur.

## 3. The internal derivative is zero, without saturating the external line

For the four sources, the targets (E/F)(-2) are, respectively,

    D O(-4)+(V+P) O(-6)+O(-10);
    D O(-4)+T O(-5)+O(-10)+O(-12);
    D O(-4)+T O(-5)+W O(-11);
    D O(-4)+Wp O(-5)+V O(-6)+Wp O(-7)+O(-10).

All maps from K0=V O(-4) to these targets vanish. The same-degree D component is zero because V and D are inequivalent; every other target has strictly lower degree. Thus the actual internal derivative of K0 is zero.

Let I be the full raw image of the derivative of F in (H O/F)(-2). Its external projection has image O(4), embedded with divisor twelve in the original O(16) quotient. The internal kernel image is zero, so, as actual image sheaves,

    I is isomorphic to O(4).

At this stage the external image is not saturated, and we do not apply the saturated internal/external image lemma. In particular no O(16) image is silently substituted for O(4).

Let Mraw be the actual raw first-osculation sheaf, generated by F and its derivatives. It has the exact sequence

    0 -> P O(-2) -> Mraw -> O(6) ->0,            (3)
    rank Mraw=5, degree Mraw=-2.

This sequence is valid before saturation: Mraw is the inverse image of I(2) in H O/F. On a smooth curve these sheaves are locally free, although Mraw need not yet be saturated.

## 4. The invariant saturation budget is too small for a defect

Let M be the saturation of Mraw in H O and let delta be the length of M/Mraw. Then

    deg M=-2+delta.

A subbundle of a constant bundle has nonpositive degree, hence 0<=delta<=2. On the other hand, a nonzero quotient M/Mraw has G-invariant effective determinant divisor of degree delta. Every nonempty invariant effective divisor has degree at least12. Therefore delta=0:

    M=Mraw=F^+ is saturated, and M/F=O(6).       (4)

This is the new saturation step. It retains the genuine degree-twelve external divisor and shows that it cannot be converted into an unspecified osculation defect.

Now the profile-free quadratic Gauss gap already gives a contradiction. A saturated quadratic bundle of rank r with saturated raw Gauss rank one and F^+/F=O(b) must have b=2r or b<=r-1. Here r=4 and b=6, whereas 3<6<8. This contradiction is independent of any maximal-plateau or no-section hypothesis for E^+.

## 5. Direct polar verification of the contradiction

The same conclusion can be seen without invoking the gap lemma. First polars give an onto map

    P W O(-1) -> M,

so M(1) is globally generated. Saturation inside a constant bundle makes all splitting degrees at most0, hence the only degrees are0 and-1. From rank5 and degree-2, the constant coefficient has dimension3 and the linear coefficient dimension2. The exact character identities from (3) are

    chi_G(M)=-P+Sym6 W=V,
    chi_G(M(1))=Sym7 W=Wp+T.

Since V W=T, the actual splitting is

    M=V O+Wp O(-1).                              (5)

The V is the canonical actual constant subspace given by H0(M). Project F and M by this constant V. The target Wp O(-1) is saturated in the projected ambient constant bundle. The projected map

    P O(-2) -> Wp O(-1)

cannot be zero, since otherwise the rank-four F would lie in a rank-three constant space. Its equivariant Hom space is one-dimensional because P=Wp W. Every nonzero such map is the tensor-Wp Euler map, hence onto everywhere.

The derivative of projected F lands in the projected M=Wp O(-1), because the derivative of F lands in M. Local lifting along the onto map therefore shows that the entire Wp O(-1) is preserved by the trivial connection. A horizontal subbundle in characteristic zero is constant, contradicting its degree-2. This independently confirms the contradiction in Section4.

## Remaining branch

The four high-P systems must therefore be basepoint-free. Their degree-eighteen external images and nonzero possible internal channels require separate treatment. This proof neither assumes that those channels vanish nor transfers any full-source exclusion from the divisor-twelve branch. It makes no whole-source or whole-label count change and is not Lean certification.
