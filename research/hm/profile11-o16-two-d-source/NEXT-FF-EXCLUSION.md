# The two-D source is impossible at source index113

## Statement and boundary

For G3.11.ad509d55173f, with A_q=O(-10)+O(2)+O(16) and original defect zero, the entire source tuple (0,0,0,0,0,2,0,1) is impossible. Its bundle is

    E=(P+2D) O(-2)+2 O(-8)+O(-10).

This is one further source-edge exclusion, not a whole-label exclusion. It is independent of the six-source-edge argument prepared separately. It uses only the original source and quotient data, the P+D polar argument in PR802, and the horizontal preserved-lattice lemma in PR828. No actual coefficients, parameters, points, derivative values, matrices, instance ranks, selected models, scans, or unapproved computation are used.

## Immutable public inputs

The original catalog and actual-bundle inputs are at db51525015bb7c5e825833d550d08dedf6f6ea96, research/hm/order-four-quadratic-load/, specifically ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md, NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md, one-one-endpoint-necessary-pairs.json, and rank-three-quotient-frontier-144.json. The index113 source list consists of all ten tuples a=d=g=0, h=1, b+c+e+f=2; the statement removes only the f=2 tuple.

PR802, commit e484640a6565c278321bf6557860262c1ac1b7df, Sections3 and5, supplies the exact P+D line-system kernels and universal nonzero-internal-image polar contradiction:

https://github.com/Akilleez-QA/read-em-and-weep/blob/e484640a6565c278321bf6557860262c1ac1b7df/research/hm/profile11-o16-constant-span-exclusion/PROOF.md

PR796, commit d2b43060c83328dd5118aee6b9288fcfa0c873ac, Section3, supplies the actual saturated internal/external derivative-image lemma:

https://github.com/Akilleez-QA/read-em-and-weep/blob/d2b43060c83328dd5118aee6b9288fcfa0c873ac/research/hm/profile12-quadratic-block-exclusion/PROOF.md

PR828, commit ae077cbe42d65cde27d65ce88923dc35851b6952, Section1, supplies the preserved coherent-lattice lemma:

https://github.com/Akilleez-QA/read-em-and-weep/blob/ae077cbe42d65cde27d65ce88923dc35851b6952/research/hm/profile11-horizontal-quotient-exclusion/HORIZONTAL-CONSTANT-QUOTIENT-EXCLUSION.md

The proof below restates all interfaces and checks them in this different source. None of PR802's full-label conclusions is imported. Work over C with the binary icosahedral representations W,Wp,A,V,P,S,D,T used in those sources.

## 1. Split off the actual high-line quadratic subsystem

Strict-top injects the top coefficient P+2D into

    H0(O(4)+O(18))=A+V+2P+2D.

The two D source copies map to exactly two D target occurrences, one in each summand. The induced two-dimensional multiplicity map is an isomorphism. Its low-row kernel is one D multiplicity line. Together with P, which has no component to O(2), this defines an actual saturated subbundle

    F=(P+D) O(-2) subset E

mapping only to O(16). Its nine independent sections have no common divisor, because a nonempty invariant divisor would leave at most seven sections of O(18). Thus F->O(16) is onto. The complementary D has a nonzero component to O(2).

The complete exact line-system kernels from PR802 Section3 are

    (V+P) O(-4)+O(-6);
    Wp O(-3)+V O(-4)+Wp O(-5)+O(-6);
    T O(-3)+O(-6)+O(-10).                         (1)

They depend only on the onto P+D system in degree18 and strict-top, all now established.

The actual internal derivative has target

    (E/F)(-2)=D O(-4)+2 O(-10)+O(-12).

There is no component into D O(-4): the equal-degree V/P channels vanish, Wp is absent from D W=S+T, and D is absent from Sym2 W and Sym6 W for the O(-6),O(-10) channels. The only nonzero possibility is therefore the O(-10) in the last kernel mapping by a constant row into 2 O(-10). Every nonzero such row is saturated. Thus the internal image is either0 or O(-10), and the full raw derivative image is saturated by PR796.

The nonzero alternative gives exactly

    F^+=A O+(Wp+T) O(-1),

as in PR802 Section5. That section's contradiction uses only F=(P+D) O(-2), the actual constant A and the three linear channels P->Wp, P->T, D->T. These are precisely the present interfaces; it does not require the internal O(-10) to land in a particular lower source summand. The contradiction therefore excludes this entire nonzero constant-row alternative.

Consequently

    F^+=C0 O, C0=A+V+P, dim C0=10,
    (C0 O)/F=O(18).                               (2)

Here constancy also follows directly from saturated rank10 and degree0. The external high line is saturated, so E+C0 O is saturated, E intersect C0 O=F, and constant projection gives an actual saturated bundle

    Z=(E+C0 O)/C0 O=D O(-2)+2 O(-8)+O(-10)        (3)

in (H/C0) O. The actual derivative quotient of Z is exactly O(2)+O(-10), with saturated raw image. Indeed it is the projection of the original exact derivative quotient by its saturated O(16) summand, as in PR802 Sections6-7.

## 2. The residual quadratic block has a constant seven-dimensional span

Let D0=D O(-2) be the top subbundle of Z. Its component to O(-10) vanishes by degree. Strict-top makes its O(2) component nonzero. It is the complete quartic evaluation system and is onto, with kernel S O(-3). The internal derivative of that kernel into

    (Z/D0)(-2)=2 O(-10)+O(-12)

vanishes by degree. Thus the actual raw image is saturated and

    M=D0^+,
    0 -> D O(-2) -> M -> O(4) ->0.                (4)

First-polar generation gives degrees0 or-1 for M. Equation(4) gives rank6, degree-6, and chi_G(M(1))=T, so M=T O(-1).

The derivative of M kills D0 and hence has rank at most1. It is nonzero, since M is a negative saturated subbundle of a constant bundle. A pure-linear bundle reaches its full constant coefficient span in one forward step. Therefore this span C1 has dimension7 and

    C1 O/M=O(6).                                 (5)

Taking global sections identifies C1=Sym6 W=V+P, although only its dimension and the line quotient in (5) are needed below. All statements concern the actual projected connection.

## 3. Remove the negative endpoint exactly

Put Z'=ker(Z->O(-10)) and K=Z^-. Only the O(-10) source summand in(3) maps to that negative quotient, so its coefficient is a nonzero scalar and

    Z'=D O(-2)+2 O(-8), rank Z'=7, deg Z'=-26.

The top D0 already maps onto the positive O(2). Consequently

    0 -> S O(-3) -> K -> 2 O(-8) ->0.

This extension splits equivariantly because H1(O(5))=0. In particular every degree of K is at least-8, so Hom(K,O(-12))=0.

Derivatives of K lie in Z, and their possible internal component outside Z' is precisely K->(Z/Z')(-2)=O(-12); it vanishes. The external derivative of Z' has full saturated image O(2), supplied by D0. PR796 therefore gives

    G=(Z')^+=Z'+M,
    G/Z'=O(4), rank G=8, deg G=-22.               (6)

These are exact actual sheaves, with no divisor or unspecified saturation correction.

## 4. The preserved sum cannot have its required quotient degree

Set S0=Z'+C1 O. Because derivatives of Z' land in G=Z'+M and M is contained in C1 O, S0 is preserved by the trivial connection. Its horizontal saturation is constant, and the preserved coherent-lattice lemma makes S0 itself constant.

For completeness, the latter statement retains possible torsion: in the constant saturation, the determinant lattice is locally t^m O. Preservation would require the derivative m t^(m-1)dt to belong to t^m O dt. In characteristic zero this forces m=0, so the sum is already saturated and constant.

The quotient C1 O/M has rank1. Since G=Z'+M, the rank of S0 is8 or9. Rank8 is impossible: the saturated rank8 bundle G inside the same constant ambient bundle would then equal the constant S0, contradicting deg G=-22. Hence S0 has rank9, and S0/G is a line bundle of degree22.

But the sum identity yields an onto map

    O(6)=C1 O/M -> S0/G=O(22).

An onto map between line bundles is an isomorphism, impossible for different degrees. This contradiction excludes the entire source stated at the outset.

## Precise unresolved neighboring branch

The analogous source (P+2D) O(-2)+O(-8)+W O(-9) for index127 has the same high-line constant reduction. It is not excluded by the statement above: its O(-8) quotient can be supplied either by the O(-8) scalar component or by the W O(-9) Euler component. When the scalar component is nonzero, the argument proceeds with Z'=D O(-2)+W O(-9), G of degree-24, and the same impossible O(6)->O(24) surjection. When that scalar component is zero, the kernel instead includes O(-8)+O(-10), and an additional O(-10) internal derivative channel survives. That branch is left open and no entire source127 edge is removed here. The same extra channel prevents silently importing this proof for source127's h-f-f tuple.
