# Rank-eleven endpoint splitting reduces the (2,1) list to twelve pairs

## Result and limits

Starting with the thirteen necessary pairs in TWO-ONE-PRIMAL-INTERIOR-AND-ENDPOINT-QUOTIENT-CONSTRAINTS.md, existence of the rank-eleven primal endpoint as an equivariant split bundle excludes

    A = O(-10) + 2O(6), B = 2O(-8) + O(8).

Thus twelve necessary pairs remain, accounting for 867 of the previous 877 formal source records. The other source records are retained as an overlist: this calculation does not test a particular endpoint's embedding into each source E.

There are also new constraints on the separate second-primal defect s:

- A = Wprime O(-5) + O(16): only s=0, instead of 0 or12.
- A = Wprime O(-1) + O(6): only s=0, instead of 0 or12.
- A = O(-8) + O(6) + O(16): s=30 is impossible, but s=32 is retained.

All other previously allowed defect degrees remain in the necessary overlist. The positive defects have substantially fewer possible torsion characters and endpoint splittings; the complete finite list is in two-one-rank-eleven-endpoint-splittings.json. Cyclic and semisimple length-two sheaves are both included, not conflated. No profile is excluded, no actual realization is asserted, and no SF or square-rank conclusion changes.

## 1. Exact endpoint identities

Retain the predecessor's notation

    K=E^-, M=K^-, A=E/K, J=K/M,
    0 -> J -> A(-2) -> T -> 0, length T=s.

The proved ranks and degrees give rank M=11 and

    deg M=-48-2a+s, maxdeg M<=-4, a=deg A.

No rank is assigned to the derivative of M. Its factorization through J(-2), combined with maxdeg M^-<=-5, gives only the established injection

    H0(M(4)) -> H0(J(2)) -> H0(A).

For every integer r, additivity in the two bundle sequences and the torsion sequence gives

    chi(M(r)) = chi(E(r))-chi(A(r))-chi(A(r-2))+H0(T(r)).       (1)

Let

    X = chi(A(3))+chi(A(1))-chi(E(3))-H0(T(3)),
    Z = chi(E(4))-chi(A(4))-chi(A(2))+H0(T(4)),
    H = H0(A).

Then the necessary conditions are

    H1(M(3))=X, chi(M(4))=Z, H0(M(4)) <= H.                  (2)

The last inequality means constituentwise containment. The predecessor only required two resulting Euler envelopes to be genuine. Here a single rank-eleven split bundle must realize both characters simultaneously. That is a genuinely stronger requirement.

The fixed actual Euler characters are chi(E(3))=U and

    chi(E(4)) = M3 tensor Sym^3 W - M4 tensor Sym^4 W,
    M4 = 2V+4P+3D.

These identities concern the actual source presentation, not an invented source splitting.

## 2. Complete finite window for M

Write each equivariant block as R O(-4-j), with j>=0. Equivariant splitting is available because ordinary splitting is invariant degree by degree and the finite group is linearly reductive. The central parity condition is

    center(R)=(-1)^j.

A rank-eleven bundle with the stated degree has total weighted excess

    sum j dim(R) = -44-deg M = 4+2a-s = c.

For the thirteen input pairs, 0<=c<=32. Consequently every block has j<=c, hence ordinary degree in [-36,-4]. Every positive-j block contributes

    H1(R O(-4-j)(3)) = R tensor Sym^(j-1) W,
    H1(R O(-4-j)(4)) = R tensor Sym^(j-2) W  (j>=2),

with the second expression zero for j=1. Its twist-four H0 is zero. The j=0 blocks have H1 at both twists zero and H0 at twist four equal to R.

The verifier first enumerates all positive-j blocks with j dim(R)<=c, the required central parity, and H1 at twist three contained in X. It recursively chooses their nonnegative multiplicities so their twist-three characters sum exactly to X, using rank at most eleven. Once these blocks are chosen, their twist-four H1 character is known and the remaining top-block coefficient representation is forced to be

    R_top = Z + H1(M_low(4)).

It must be genuine, center-even, have dimension equal to the unfilled rank, and be contained in H. These tests recover every possible M satisfying (2), and only such M. Indeed every actual M decomposes into the selected positive-j blocks and these forced j=0 blocks; conversely each enumerated object has exactly the stipulated split-bundle numerical and cohomological data. This converse does not assert existence of any bundle maps.

There is no speculative search cutoff: rank, weighted excess, central parity, and finite irreducible list bound the entire enumeration. The dynamic programming returns complete tuples of blocks, not merely a Boolean feasibility result.

## 3. Exhaustive torsion possibilities through degree32

Invariant determinant divisors up to degree32 are supported on the unique special orbits D12, D20, D30, of sizes12,20,30. Their binary stabilizers are C10, C6, C4. Since the torsion is center-even, reduced-orbit line possibilities are

    O(k)|D12, k=0,2,4,6,8;
    O(k)|D20, k=0,2,4;
    O(k)|D30, k=0,2.

At s=24 the divisor is 2D12. At each point the DVR module has length two, and is either cyclic R/m^2 or semisimple (R/m)^2. Averaging a generator lift against its stabilizer character produces an eigen-generator in the cyclic case; Nakayama then identifies the full module. Transport over the orbit yields precisely

    O(k)|2D12, k=0,2,4,6,8,
    O(k)|D12 + O(l)|D12, 0<=k<=l<=8, k,l even.

The second list includes repeated and distinct characters. There is no additional infinitesimal linearization parameter: the eigen-generator argument identifies the action on the whole cyclic module.

At s=32 the divisor is D12+D20, with length one at each point. Disjoint support gives the fifteen possibilities

    O(k)|D12 + O(l)|D20, k=0,2,4,6,8 and l=0,2,4.

The zero-defect sheaf is zero. These are exhaustive isomorphism-class possibilities for T, independently of the parallel (1,1) local-torsion calculation.

The defining divisor sections are invariant, because their stable lines carry one-dimensional characters and the binary icosahedral group is perfect. Therefore the exact Euler signatures are

    H0(O(k+r)|D_d)=chi(O(k+r))-chi(O(k+r-d)),

using d=24 for a cyclic doubled-orbit sheaf and adding the two signatures in a semisimple or disjoint-support case. The cyclic filtration has conormal shift -12 modulo10. In particular cyclic k has the same Euler signatures as semisimple {k,k-2 modulo10}; they remain different sheaf types in the output.

This argument verifies the needed length-two classification directly. It does not assume simple support at s=24 or32 and does not depend on the parallel torsion classification.

## 4. Two transparent exclusion certificates

### The pair A=O(-10)+2O(6)

Here s=0 already follows from the predecessor's degree bound, and exact character arithmetic gives

    H1(M(3))=2S,
    chi(M(4))=-2 A_std + 2V+2P-D.

The only positive-j blocks whose twist-three H1 is contained in 2S are S O(-5) and O(-8), each contributing S. Their twist-four H1 characters are respectively zero and A_std. Hence any sum of these blocks has zero D multiplicity in H1(M(4)). The identity

    H0(M(4)) = chi(M(4))+H1(M(4))

would have D multiplicity -1, impossible. Thus the entire pair is excluded even before the endpoint section injection is used. The finite check of these two eligible blocks requires only j dim(R)<=8.

### The s=30 branch of A=O(-8)+O(6)+O(16)

For either possible D30 line, H1(M(3))=Wprime. Its only eligible positive-j block is Wprime O(-5), with zero H1 at twist four. For line parameter k=0 the required chi(M(4)) is

    -A_std+V+P+D,

and for k=2 it is

    -one+2V+P.

Neither is genuine, so no M exists. This excludes s=30 without imposing a derivative rank.

By contrast s=32 survives: it forces

    T = O(4)|D12 + O(2)|D20,
    M = (V+2P) O(-4).

The endpoint has rank11 and degree-44 as required. This is a necessary formal endpoint and torsion alternative, not a realized quotient or derivative.

## 5. Remaining defect list and reproduction

Using zero-based pair indices in the input JSON, the retained lists are

    0: excluded
    1: 0
    2: 0,12,20,24
    3: 0
    4: 0
    5: 0,12,20,24
    6: 0
    7: 0
    8: 0,12
    9: 0,12,20,24,32
    10: 0,12,20,24
    11: 0
    12: 0.

Indices3/4 and6/7 distinguish the original defect-zero and defect-twelve pairs with the same A. This second-primal analysis depends only on A and the fixed E Euler characters; it does not identify the original torsion with T.

Run:

    python3 verify_two_one_rank_eleven_endpoint_splittings.py

The verifier reads the pinned predecessor summary without rerunning its writer and uses the existing exact character ring. It writes only the new endpoint output. It checks ranks, degrees, central parity, exact twist-three and twist-four characters, the endpoint injection inequality, and redundantly verifies (1) from twists -2 through8 for every retained endpoint. Two consecutive Euler characters suffice for the full sequence, by the equivariant Euler relation chi(F(r+1))=W chi(F(r))-chi(F(r-1)); the redundant interval is not an exhaustiveness assumption.

All calculations use universal characters and bounded integers. There are no selected actual coefficients or points, actual-instance matrices or rank evaluations, scans of the actual map, model spikes, or consumed experiments. No earlier file is edited. Necessary endpoint existence is not global quotient realization, let alone realization by the actual Gauss derivative.
