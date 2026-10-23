# The low D row and two exact kernel alternatives in source127 a-b-c-f

## Result and scope

For the original source

    G3.11.cce6e3ba4eeb, source_index127,
    (1,1,1,0,0,1,0,0),
    E=D O(-2)+(Wp+T) O(-3)+V O(-4)+O(-8),
    A_q=O(-8)+O(2)+O(16),
    B_q=O(-18)+O(-4)+O(6), original defect zero,

the canonical F=D O(-2) block must have nonzero external row toward O(2). Exactly the following alternatives remain for its high O(16) row:

1. If the high row is zero, F is the standard U_4^6 inside its actual constant span V+P. Its saturated first span is T O(-1), and the external kernel is S O(-3).
2. If the high row is nonzero, the actual external map F->O(2)+O(16) is onto everywhere. Its exact kernel is one of

       O(-6)+W O(-11),
       O(-6)+O(-10)+O(-12).                    (1)

This is a structural reduction and conditional exclusion, not a whole-source or whole-label exclusion. The surviving internal maps in (1) are not declared zero, and no next Gauss rank is inferred from these abstract splittings. No other source, abstract family or necessary-pair count is changed.

No selected actual HM/source coefficients, parameters, points, derivatives, matrices, instance ranks, models, scans or large computation are used. All representation checks concern fixed abstract characters.

## 1. Exact actual inputs and the high-only kernel dependency

The four original inputs are the actual-presentation note, strict-top theorem and two catalogs at commit db51525015bb7c5e825833d550d08dedf6f6ea96, under research/hm/order-four-quadratic-load in Akilleez-QA/read-em-and-weep. Their exact URLs and Git blob hashes are in audit-inputs/manifest.json. They give saturated full-span E in H O, with

    H=2A+2V+2P+2D, rank E=17, degree E=-54,
    H0(E)=0, H0(E^-(2))=0,
    Q=H O/E,
    E^+/E=O(-6)+O(4)+L, L=O(18) saturated in Q. (2)

The final equality uses the original defect-zero convention. Work over C with binary icosahedral G. Here W is its defining two-space; A=Sym2 W, S=Sym3 W, D=Sym4 W, T=Sym5 W; Wp,V,P are the other irreducibles of dimensions2,3,4. Every nonempty invariant effective divisor has degree at least twelve, and there are no nontrivial line characters.

The sole newer dependency is the public PR905 proof at

    2db172b32dc014c06521a3fcba20261db5bb00fa,
    research/hm/profile11-source127-acff-exclusion/PROOF.md,
    Git blob 3448047b9f67b258955f0fe53c3368b6f7615d9e.

https://github.com/Akilleez-QA/read-em-and-weep/blob/2db172b32dc014c06521a3fcba20261db5bb00fa/research/hm/profile11-source127-acff-exclusion/PROOF.md

Its Sections2 and3 prove the following universal conditional fact: a nonzero high-only D(-2)->O(16) row is basepoint-free, and its kernel is

    O(-6)+Wp O(-5)+O(-10).                     (3)

The proof uses the independent D coefficient sections, the absent D in Sym6 W, H0(K(2))=0, H1(K(2))=A+V+2P and chi_G(K(3))=-W-Wp-T. It does not use the other source's remaining splitting or the presence of a second D block once the high-only row is obtained. The present source has precisely the same actual quotient (2), strict-top input and high-only map when its low row is assumed zero. Thus that exact conditional kernel statement applies; no whole-source conclusion from PR905 is transferred.

We also use its elementary image lemma: if the internal derivative image J is saturated in (E/F)(-2) and the external image L0 is saturated in Q(-2), the complete derivative image I is saturated. Its quotient is an extension of the two locally free quotients. The raw first span M is then saturated, and

    0 -> J -> I -> L0 ->0,
    0 -> F -> M -> I(2) ->0,
    (E intersect M)/F=J(2) inside E/F.         (4)

A quadratic raw first span is a quotient of D W O(-1), so all its splitting degrees are zero or minus one.

## 2. A zero low row has two genuinely surviving internal channels

Assume the low F->O(2) row is zero. Its negative row vanishes by degree. Strict-top forces the high row nonzero, so (3) applies and its external O(16) image is saturated.

Write R=Wp O(-3), and write T_src O(-3) for the original T block. The internal target of (3) is

    R(-2)+T_src O(-5)+V O(-6)+O(-10).

The O(-6) kernel term maps nowhere. The Wp(-5) term maps only to the entire original R(-2), by a scalar. The scalar O(-10) term can map to T_src O(-5) and to the scalar O(-10), each in a one-dimensional Hom space. Both channels must be retained.

A nonzero T-valued degree-five scalar row has no common zero, because its invariant common divisor would have degree at most five. A nonzero equal-degree scalar row is an isomorphism. Thus every nonzero full image J0 of O(-10) is a saturated line isomorphic to O(-10), whether its T component, its scalar component, or both are nonzero. The complete internal images are

    J=0, Wp(-5), J0, Wp(-5)+J0.                (5)

They are saturated. The first two cases give first-span degrees8 and2 and are impossible in a constant bundle. The remaining cases yield, respectively,

    M=(A+P) O, or M=A O+T_lin O(-1).            (6)

For the first case, rank M=7, degree M=0 and chi(M)=A+P. In the second, rank M=9, degree M=-6, chi(M)=A and chi(M(1))=W+S+T. Since A W=W+S, the linear coefficient is T. The degree-zero summand is an actual canonical constant space, not an assumed horizontal splitting.

Let N=E intersect M, and let S0=J0(2) be the actual O(-8) line in T_src O(-3)+O(-8). By (4),

    N/F=S0 in the constant case,
    N/F=R+S0 in the linear case.               (7)

These are actual images in the original direct sum E/F.

## 3. Legitimate high capture and elimination of the scalar component

In the constant case, M maps onto L, so constant projection gives a saturated actual E/N in (H/M) O, with derivative image O(2)+O(-8).

In the linear case the canonical constant A has zero maps to the two lower rows of (2), since A is absent from Sym4 W=D. Its high map is nonzero or A would be contained in E. The map A O->L is onto: three independent degree-eighteen coefficients bound its common divisor by sixteen; the only possible invariant degree is twelve, since Sym14 and Sym16 have no invariant; a degree-twelve factor would require A in Sym6 W=V+P, absent. Thus constant projection by A gives saturated actual E'=E/(E intersect A) in (H/A) O with derivative image O(2)+O(-8).

Since A captures M's entire image L, M lies in E+A as a coherent sheaf. Consequently

    0 -> T_lin O(-1) -> E' -> E/N ->0           (8)

is an exact sequence of actual bundles, with T_lin(-1) saturated in the ambient constant bundle.

If S0 has a nonzero scalar component, it is a graph over the original O(-8). Then (7) gives

    E/N=R+T_src(-3)+V(-4) in the constant case,
    E/N=T_src(-3)+V(-4) in the linear case.

Neither the displayed bundles nor T_lin(-1) has a map to O(-8), by degree. Applying Hom(-,O(-8)) to (8) gives the same vanishing for E' without assuming the extension splits. This contradicts the required negative derivative quotient in both cases. Therefore the scalar component is zero and S0 maps nontrivially only to T_src(-3).

## 4. The T-only component is also impossible

The nonzero scalar degree-five row is the complete quintic Euler inclusion, with exact sequence

    0 -> O(-8) -> T_src O(-3) -> D O(-2) ->0.  (9)

It is obtained by dualizing complete degree-five evaluation and twisting by -3. Thus the original scalar O(-8) survives separately, and (7) gives

    E/N=D(-2)+R+V(-4)+O(-8) in the constant case,
    E/N=D(-2)+V(-4)+O(-8) in the linear case.   (10)

In the constant case, R has zero external derivative: its high row has been removed; Wp is absent from Sym5 W=T; and the negative row is too low. Its derivative toward the other summands, twisted by -2, also vanishes by degree. Thus a saturated negative R is preserved by the trivial connection, impossible: its generic constant subspace would extend as the entire constant saturated bundle.

In the linear case the projection of F=D(-2) into T_lin(-1) is nonzero, because rank F=5>rank A=3. The unique such map is the universal multiplication-by-the-formal-line injection D(-2)->T(-1). Differentiation of F stays in M, so the derivative kernel of the linear bundle contains this D(-2).

For a linear inclusion T(-1), that derivative kernel is the coefficient kernel of T W->C_T, twisted by -2. Since T W=V+P+D, its constant span C_T is a quotient of V+P. Its dimension is at least seven, since a saturated negative rank-six bundle cannot span only six constants. Hence C_T=V+P.

By (7), the original R lies in M. Its map to constant A is zero, because A Sym3 W=W+S+T has no Wp. Its projection is still an actual injected R in T_lin(-1). Its constant span is a quotient of Wp Sym3 W=V+D and a subrepresentation of V+P, so it is exactly V. The saturated first span of this rank-two family in the constant three-space V is all V.

On the other hand, its external derivative in E' is zero, and (8),(10) show its derivative toward the quotient is a map

    Wp(-3) -> D(-4)+V(-6)+O(-10),

which is zero by degree. All its derivatives therefore stay in the saturated T_lin(-1). Its saturated first span V O would lie there, contradicting H0(T_lin(-1))=0. This excludes the last zero-low-row alternative and proves that F->O(2) is nonzero.

## 5. Zero high row: an actual standard osculating block

Assume now that the high F row is zero. The complete external derivative is the nonzero D(-2)->O(2) row. It is the full degree-four evaluation, hence onto, with kernel S O(-3).

Its internal targets have degrees at most minus five, so the internal derivative image is zero. Formula (4) makes the raw first span saturated. It has rank6, degree-6 and is generated after twist one, hence

    F^+=T O(-1).

The inclusion F->F^+ is the unique nonzero D(-2)->T(-1) Euler inclusion. Its derivative lies in F^+, so the linear coefficient kernel contains D in T W=V+P+D. The same rank argument as Section4 makes the actual constant span exactly V+P=Sym6 W. The coefficient projection T W->V+P is unique up to nonzero scalar on each irreducible summand, and these scalars are absorbed by a constant equivariant automorphism of V+P. Thus the actual inclusions are the standard universal ones

    F=U_4^6=D O(-2),
    F^+=U_5^6=T O(-1),
    C_F=Sym6 W O=(V+P) O.

This is a structural identification, not a selected actual source model.

## 6. Two nonzero rows: surjectivity and exact rank-three classification

Suppose the high F row is also nonzero. The low row is onto with kernel S(-3). The high row restricts nontrivially to this kernel: otherwise it would factor through O(2) by an invariant degree-fourteen scalar form, and that invariant space is zero.

The restricted high row is an S-valued degree-nineteen covariant. Its four independent coefficient sections bound a common divisor by sixteen. Among positive invariant degrees in this range only twelve is possible; removing it would require S in Sym7 W=Wp+T, absent. Thus S(-3)->O(16) is onto, and consequently

    F -> O(2)+O(16) is onto everywhere.         (11)

Its kernel K has

    rank K=3, degree K=-28, H0(K(2))=0,
    H1(K(2))=A+V+2P+D,
    chi_G(K(3))=-W-Wp-2T.                     (12)

These follow from Sym18 W=A+V+2P+D and Sym19 W=W+Wp+S+2T. All degrees of K are at most minus three. Since there are no nontrivial line characters, a rank-three equivariant splitting has only three possible coefficient patterns: one irreducible three-space; three scalar lines; or a W/Wp two-space and one scalar line. A single irreducible three-space would make its degree divisible by three, contrary to -28.

For three scalar lines, all degrees are even. O(-4) is excluded by its trivial H1(K(2)) constituent, so the degrees are at least six. Their sum is28. The complete possibilities, up to order, are

    (6,6,16), (6,8,14), (6,10,12),
    (8,8,12), (8,10,10).

The first is excluded by the trivial constituent in Sym12 W. The other nonmatching cases respectively give H1 characters 2A+V+2D, P+3D, and 2V+2P+D. Only (6,10,12) has the required character A+V+2P+D, and it also has the required twist-three character in (12).

For a two-space U O(-j) and scalar O(-k), j is odd and k even, with j>=3, k>=6 and 2j+k=28. The only pairs are

    (j,k)=(3,22),(5,18),(7,14),(9,10),(11,6).

At (3,22), H1 at twist two matches, but chi at twist three is U-Wp-S-2T, not the target in (12) for either U=W,Wp. At (5,18), the W choice introduces a trivial constituent; the Wp choice matches H1 but gives chi=-W-2Wp-S-T. At (7,14), neither choice matches H1. At (9,10), only Wp matches H1, but gives chi=-S-2T. At (11,6), Wp introduces a trivial constituent, while W matches both characters. Hence precisely the two kernels in (1) survive.

## Contribution and remaining boundary

The entire zero-low-D branch is excluded. The two surviving alternatives identify exact actual quotients and finite kernel types, while retaining their further internal maps. No argument here asserts that those internal images vanish or that osculating gains add through a nonconstant extension. Whole a-b-c-f realizability and the full-profile test remain open.
