# Profile (1,2): endpoint and orbit characters leave ten necessary pairs

## Result and attribution

Starting with the 25 necessary quotient pairs in ONE-TWO-FINITE-QUOTIENT-PAIRS-AND-ZERO-DEFECT.md, the additional constraints below leave ten pairs, 38 necessary endpoint/defect records, and 52 inherited compatible pair/E records. They exclude every second-dual defect s=20 branch. These are necessary overlists, not realizations. Profile (1,2) remains open; SF>=3 and square rank>=27 are unchanged.

We credit Mr. Slop's [PR674 proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/2516a879b4b1469da1a29eaefafcfddf4e171a0d/research/hm/primal-quotient-degree-bound/PROOF.md) for the independent profile-independent bound a>=-4, original defect t=0, and its second-dual defect table. We use these results, rather than reproving them. The earlier 25-pair note independently proves original t=0. This note contributes endpoint splitting, orbit-cokernel and endpoint rank-drop constraints, not another proof of that theorem.

Retain

    K=E^-, A=E/K, L=(Q*)^-, B=Q*/L,
    M=L^-, J=L/M, T=coker(J -> B(-2)).

Here M has rank seven, maxdeg M<=-3, B=A*(-2), a=deg A, and

    deg M=-36+2a+s,  s=length T<=14-2a.

PR674 permits s=0,12,20 at a=-4; s=0,12 at a=-2,0; and only s=0 at a=2,4,6. No H0(Q*(1)) vanishing and no rank-three assertion at M or its later kernels is used.

## 1. Endpoint top-degree inequality

If the highest splitting degree of M is -d, the strict-top-slope lemma gives H0(M^-(d))=0. Its derivative factors through J(-2), which injects into B(-4). Consequently

    H0(M(d)) -> H0(J(d-2)) -> H0(B(d-4))

is injective. Thus, in irreducible multiplicities,

    H0(M(d)) <= H0(B(d-4)).                         (1)

This is a section-space injection, not a fiber-rank assertion.

There is also a useful certificate that needs no splitting enumeration. Since maxdeg M<=-3, H0(M(3)) injects into H0(B(-1)). The exact sequences give

    chi(M(t))=chi(Q*(t))-chi(B(t))-chi(B(t-2))+H0(T(t)).  (2)

Combining at t=3 implies the genuine-character constraint

    H0(B(-1))+chi(B(3))+chi(B(1))-chi(Q*(3)) >= 0.   (3)

Indeed its difference from H0(T(3)) is a sum of H1(M(3)) and the cokernel of the section injection. For the old pair A=Wprime O(-1)+O(6), expression (3) equals 2W+Wprime-T6, an immediate contradiction.

## 2. The complete small torsion possibilities

When s=12 or 20, the determinant divisor of J -> B(-2) must be the single reduced projective icosahedral orbit D_s of that size. Orbit sizes are 12,20,30,60; below 24 the only positive sums are 12 and 20. At each point of D_s the cokernel length is one. Hence T is an equivariant line bundle on the reduced finite orbit, extended by zero.

The binary stabilizer of a point of D_12 is cyclic of order 10; that of a point of D_20 is cyclic of order 6. The fiber character of O(1) generates their character groups: on the corresponding eigenline in the standard SL2 two-space, a generator has a primitive eigenvalue of that order. Equivariant line bundles on a transitive finite orbit are precisely its stabilizer characters. Since T is center-even, the complete list is

    s=12: T = O(k)|D_12,  k=0,2,4,6,8;
    s=20: T = O(k)|D_20,  k=0,2,4.

These are possibilities for an equivariant sheaf, not assertions that a quotient B(-2)->T exists. In particular the test is conservative.

The defining equation of either orbit divisor is invariant: its one-dimensional defining space is stable, and the binary icosahedral group has no nontrivial characters. Thus the equivariant divisor sequence gives the exact character

    H0(T(t))=chi(O(k+t))-chi(O(k+t-s)).              (4)

For s=0 this character is zero. No point coordinates or local instances enter (4).

## 3. A proved finite endpoint window

Write the center-even equivariant splitting of M as a sum of irreducible blocks R O(-j), with j>=3 and R of central parity (-1)^j. Its rank is seven and its degree is at least -44. Therefore

    sum (j-3)dim R = -deg M-21 <=23.

Every individual block satisfies j<=26. This proves an exhaustive finite window, not an experimental cutoff. All nine binary-icosahedral irreducibles are allowed subject to rank and parity. For degrees -44,-40,-36,-32,-28,-24, respectively, the numbers of all rank-seven splittings in this window are

    721, 443, 248, 120, 53, 19.

The verifier enumerates these integer partitions, applies (1), and tests (2) against the entire list (4). It checks twists 0 through 26. In fact two consecutive twists determine all Euler characters: tensor the standard equivariant Euler sequence to obtain chi(F(t+1))=W chi(F(t))-chi(F(t-1)), also for torsion sheaves. The additional twists provide redundant checks across the whole splitting window.

These tests leave fourteen old pair IDs:

    0,2,4,5,6,7,8,9,12,14,20,21,23,24.

Every s=20 case is already excluded at this stage. There are 53 endpoint records here. The compact JSON records every stage count, including empty defect branches.

## 4. Further backward rank-one obstruction

The derivative of M lands in B(-4). For each M block R O(e) and target block S O(f), an equivariant component can be nonzero only if f>=e and R occurs in S tensor Sym^(f-e) W. This is a universal Hom-character test, not an actual map or rank evaluation.

If the sum of all reachable target blocks has ordinary rank zero, M would be horizontal, impossible for a negative saturated subbundle. If that sum has rank one, it is a trivial-coefficient line O(c). The derivative of M has rank exactly one. The backward rank-one lemma from TWO-TWO-ENDPOINT-RANK-DROP-EXCLUDES-LAST-THREE-PAIRS.md applies without requiring M to span the ambient constant space. Repeated negative kernels give a full equivariant rank-one flag inside M: subsequent derivatives have rank at most one, and rank zero on a positive-rank negative saturated bundle is impossible.

If the last quotient has degree h, and the internal adjacent line gaps are delta_i, then

    deg M=7h-42-sum_(i=1)^6 i*delta_i,
    h<=c,  h even,  delta_i>=0.

Each delta_i and the final map gap c-h are degrees of invariant effective divisors. They belong to the semigroup generated by 12,20,30 (the other orbit size 60 is redundant). The flag lines are center-even, so h is even. The finite check is exhaustive because

    ceil((deg M+42)/7) <= h <= c <=4,
    sum i*delta_i <= 7c-42-deg M.

All gap values are enumerated only up to that proved budget. If no such h and gaps exist, the endpoint is impossible. This removes fifteen more endpoint records and all records for old pair IDs 5,9,23,24. No rank-two or rank-three endpoint assertion is added.

## 5. Remaining necessary overlist

In every row B=A*(-2). Counts give distinct necessary M splitting types by defect; the JSON includes each one explicitly and the possible stabilizer parameters k.

| Old ID | A | s=0 count | s=12 count |
|---|---|---:|---:|
|0|O(-10)+O(-8)+O(14)|6|2|
|2|O(-10)+O(2)+O(4)|1|1|
|4|O(-10)+2O(4)|0|1|
|6|2O(-8)+O(14)|2|2|
|7|O(-8)+O(2)+O(4)|2|2|
|8|O(-8)+O(2)+O(6)|1|0|
|12|W O(-9)+O(14)|6|2|
|14|Wprime O(-3)+O(4)|2|3|
|20|O(-10)+W O(3)|1|0|
|21|O(-8)+W O(3)|2|2|

There are 23 zero-defect and 15 twelve-defect endpoint records. Of particular note, old pair4 now requires second-dual defect twelve, whereas pairs8 and20 require second-dual defect zero. Original defect remains zero throughout. The 52 pair/E records merely inherit earlier compatibility and have not passed any actual extension or map-realization test.

## Reproduction and limits

Run `python3 verify_one_two_endpoint_orbit_constraints.py`. It reads the earlier JSON and the frozen abstract character verifiers, and writes only the new file one-two-endpoint-orbit-constraints.json. Earlier files are not overwritten. It runs in under a second in the task environment, uses exact characters in Q(sqrt(5)), and records dependency hashes.

No selected HM/source coefficients or points, instance matrices, actual-map rank evaluations, scans, local-model spikes, or consumed experiments occur. The geometric arguments establish necessity; finite character arithmetic alone is not a realizability proof or a global rank-three exclusion.
