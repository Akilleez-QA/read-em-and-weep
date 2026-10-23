# Endpoint-safe degree windows for the shortest rank-three Gauss profile

## Result and scope

For the remaining maximal profile (k,l)=(1,1), put K=E^-, L=(Q*)^-, A=E/K, B=Q*/L, a=deg A and b=deg B. Both A and B have rank three. Then

    -4 <= a <= 24,    -30 <= b <= -2,
    t = length coker(A -> B*(-2)) belongs to {0,12,20,24}.

All degrees a,b are even. The finite necessary quotient classification specified in Section 5 has **159 pairs**, distributed as 80,61,5,13 at t=0,12,20,24, respectively. Its complete machine-readable output is `one-one-endpoint-necessary-pairs.json`. It is an overlist, not a realization theorem. Neither the profile nor its positive-defect branches are excluded. No SF>=4 or smoothing conclusion is asserted.

The degree theorem needs only the original rank-three derivative, not the assertion that either endpoint has rank-three derivative. In particular it must not be confused with the stronger dual-interior bound available in profile (1,2).

## 1. Actual sources and endpoint distinction

Read `ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md` for the actual two presentations, 28 primal types and plateau definitions, and `NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md` for strict top-slope decrease. The original transpose injection is the one used in `ONE-TWO-ASYMMETRIC-QUOTIENT-DEGREE-AND-DEFECT-BOUNDS.md`, Sections 1-2; its Section 3 dual-interior argument is NOT used here.

We use the independently checked, all-profile theorem a>=-4 from [Mr. Slop's PR674 proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/2516a879b4b1469da1a29eaefafcfddf4e171a0d/research/hm/primal-quotient-degree-bound/PROOF.md). That theorem is an explicit input, not reproved by the present verifier.

The actual bundles are center-even and have presentations

    0 -> E -> M3 O(-1) -> M4 O -> 0,
    0 -> Q* -> M3* O(-1) -> M2* O -> 0,

where M2=A_std+2V+3P+4D, M3=3W'+3S+6T and M4=2V+4P+3D. Their ranks are 17,13 and both degrees are -54. All E degrees lie in [-10,-2]. Q* has no constant subbundle, so all its degrees are <=-1. We do NOT assume H0(Q*(1))=0.

Strict top-slope decrease gives

    maxdeg K<=-3, maxdeg K^-<=-4,
    maxdeg L<=-2, maxdeg L^-<=-3.

These statements hold independently of the ranks of the endpoint derivatives. Their derivatives land in A(-2) and B(-2), respectively. Consequently

    H0(K(3)) -> H0(A(1)),
    H0(L(2)) -> H0(B)

are injective. The second assertion is the essential endpoint-safe substitute for a rank-three interior quotient injection.

## 2. A finite lower slope bound for Q*

Equivariant splitting writes Q* as a sum of R O(-j), j>=1, with central parity (-1)^j. Its exact H1 is M2. Each irreducible block with j>=2 therefore has

    R Sym^(j-2) W <= M2

in the representation ring. Dimension gives (j-1)dim R<=41 and hence j<=42. Checking those nine irreducibles and that bounded interval gives exactly 38 admissible blocks; the greatest j is 30. The verifier prints the complete list. Degree -1 blocks have no H1 and do not affect the lower bound. Thus every degree of Q* is >=-30 and Q*(30) is globally generated.

Since B is a quotient, B(30) is globally generated and every degree of B is >=-30. Negative transpose, in both directions, gives

    A -> B*(-2) -> Q(-2),
    B -> A*(-2) -> E*(-2).

These are injective maps of locally free sheaves; no saturation of their images is asserted. The largest degree of E*(-2) is at most 8. Any line summand of B of degree greater than 8 would have zero map into E*(-2), contradicting injectivity. Therefore every B degree lies in [-30,8].

## 3. Excluding b=-34 and b=-32

Rank L=10, deg L=-54-b and maxdeg L<=-2 imply b>=-34. Center-even determinant parity makes b even. The original transpose determinant and a>=-4 give b<=-2.

Riemann--Roch and the endpoint injection give

    -24-b = chi(L(2)) <= h0(L(2)) <= h0(B).

At b=-34 or -32, at most one ordinary degree of B is nonnegative: two such degrees and the lower bound -30 on the third would give b>=-30. Every nonnegative degree is at most 8, so h0(B)<=9. This excludes b=-34, which would require h0(B)>=10.

At b=-32, the sole nonnegative degree must be >=7. Its coefficient representation has rank one, hence is trivial, so its degree is even and therefore exactly 8. The other two degrees sum to -40. A center-odd two-dimensional block would have degree -20, which has the wrong parity; thus they are trivial even lines. Their six possibilities are

    (-30,-10,8), (-28,-12,8), (-26,-14,8),
    (-24,-16,8), (-22,-18,8), (-20,-20,8).

Since H0(L(1))=0, the representation

    D1(B)=chi(B(1))-chi(Q*(1))=H1(L(1))

must be genuine. Its W' multiplicity for these six triples is, in order,

    -2, -1, -1, -1, -1, -2.

Each is impossible. This proves b>=-30, without a rank assertion about L's derivative.

## 4. Degree and determinant windows

From a>=-4, b>=-30 and a+b<=-6, we obtain a<=24 and b<=-2. Thus t=-6-a-b lies between 0 and 28. Its effective divisor is invariant under projective A5, whose orbit sizes are 12,20,30,60. The only sums of orbit lengths at most 28 are 0,12,20,24. In particular degree 24 means twice the twelve-point orbit; it must not be discarded merely because there is no orbit of size 24.

## 5. Reproducible finite necessary quotient list

A center-even rank-three equivariant bundle is exactly one of:

- three trivial even-degree lines;
- R O(e)+O(f), R=W or W', e odd, f even;
- R O(e), R=A_std or V, e even.

This exhausts rank-three splittings, since the other irreducibles have dimension at least four. The verifier enumerates these forms only within the proved degree windows: A has ordinary degrees >=-10 and total a in [-4,24], while B has degrees in [-30,8] and total b in [-30,-2]. No actual coefficients or chosen maps are enumerated.

It retains the following necessary conditions, all inequalities meaning nonnegative irreducible multiplicities:

1. The primal endpoint envelopes chi(A(2))+V and H0(A(1))+chi(A(3))-(W'+2T) are genuine, and H1(A(1))<=W'+3T because A is a quotient of E.
2. The dual endpoint envelopes D1(B) and D2(B)=H0(B)+chi(B(2))-chi(Q*(2)) are genuine. Indeed D2 is the character of coker[H0(L(2))->H0(B)] plus H1(L(2)). Also H1(B)<=M2 since B is a quotient of Q*.
3. t=-6-a-b belongs to {0,12,20,24}. Sorted ordinary degrees of A are componentwise <= those of B*(-2), a necessary condition for an injective equal-rank map on P1. Each irreducible summand on each side has a nonzero equivariant Hom into the opposite dual-twisted bundle. This is only a necessary Hom test, not a matrix-rank test. When t=0 the exact equivariant splittings must agree: A=B*(-2).
4. Incidence and Serre duality give H0(A)<=M2, H0(B)<=M4, H0(B(-1))<=W'+3T.
5. There must be at least one of the actual 28 E types for which, for every integer u from -10 through 10,

       H1(A(u)) <= H1(E(u)),
       H0(B(u)) <= H1(E(-u)).

The first follows from E->A and the second from B->E*(-2). Serre duality dualizes representations, but all irreducibles here are self-dual. The finite twist range is a declared necessary filter, not a claim that cohomology outside it has been completely characterized. The JSON records every compatible primal type for each surviving pair.

These exact tests leave 159 pairs and 25 degree triples. Grouping triples by defect gives:

    t=0:  a=-4,-2,0,2,4,6,8,10,12,14,16,18,22,24; b=-6-a.
    t=12: a=-4,-2,0,2,4,6,10,12; b=-18-a.
    t=20: (a,b)=(-2,-24),(2,-28).
    t=24: (a,b)=(-2,-28).

Thus the additional necessary constraints exclude a=20 and b=-26, among other combinations, but do not shrink the extreme degree interval or eliminate a positive-defect branch.

## Verification and limitations

Run `python3 verify_one_one_endpoint_degree_windows.py`. It imports only the existing abstract character ring and the frozen 28-type verifier, checks all bounded lists and certificates, asserts the final counts, and writes the complete JSON. No frozen predecessor is edited. The saturation, quotient, endpoint and determinant arguments are mathematical inputs supplied above; the arithmetic alone does not prove those facts.

All computations use universal binary-icosahedral characters and bounded hypothetical integers. No actual HM/source coefficient, selected point, actual matrix, rank test, model spike or experiment is evaluated. The rank-three profile remains open.
