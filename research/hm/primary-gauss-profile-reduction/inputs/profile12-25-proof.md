# Profile (1,2): 25 necessary quotient pairs and zero original defect

## Result

For the hypothetical maximal rank-three profile (1,2), retain

    K=E^-, A=E/K, L=(Q*)^-, B=Q*/L.

The original negative-transpose injection A -> B*(-2) must be an isomorphism. There are at most 25 ordered equivariant splitting pairs (A,B), listed below by A with B=A*(-2). These pairs have 155 compatible pair/E-type records involving 25 of the 28 proven formal E types.

This is a necessary overlist, not a realizability statement or an exclusion of (1,2). It does not change SF>=3 or square rank>=27. No endpoint derivative rank, no splitting list for Q*, and no vanishing H0(Q*(1)) are assumed. All earlier files remain unchanged.

## 1. Finite and exhaustive windows

The degree/defect note proves a=deg A in [-8,6], b=deg B in [-12,2], both even, and original torsion length t=-6-a-b in {0,12}. Its strict-slope argument gives maxdeg K<=-3, maxdeg K^-<=-4, maxdeg L<=-2, and maxdeg (L^-)<=-3; only the dual second derivative is asserted to have rank three.

Because E(10) is globally generated, every line degree of its quotient A is at least -10. Since A has rank three and a<=6, every degree is at most 6+10+10=26. Conversely B injects into E*(-2), whose largest line degree is at most 8; thus every degree of B is at most 8. Since b>=-12 and B has rank three, every degree is at least -12-8-8=-28. Repeated degrees are counted with ordinary multiplicity.

An equivariant splitting of a center-even rank-three bundle has exactly one of these forms:

- Three trivial-coefficient lines, each of even degree.
- One W or Wprime block of odd degree and one trivial-coefficient line of even degree.
- One A_std or V block of even degree.

This follows from the complete irreducible dimensions 1,2,2,3,3,4,4,5,6 and central parity, not from a proposed Q* splitting. The verifier enumerates only these rank-three characters inside the proved windows.

## 2. Necessary character tests

Write X>=Y for nonnegative irreducible multiplicities in X-Y. The initial tests are

    chi(A(3))+H0(A(1)) >= U = Wprime+2T6,
    chi(A(2)) >= -V,
    chi(B)+chi(B(2)) >= chi(Q*(2)) = -1-2A_std-V-D5.

Their exact-sequence proofs are in the degree/defect note. They leave 154 A shapes and 228 B shapes before using the additional quotient-cohomology information.

Here is the additional information, which is valid without a Q* splitting list. The actual presentation and H0(Q*)=0 give

    H1(Q*)=M2=A_std+2V+3P4+4D5.

More generally H0(Q*(r))=0 for r<=0. The actual presentation gives chi(Q*(r)) exactly, so H1(Q*(r))=-chi(Q*(r)) in this range. Since Q* -> B is a bundle quotient on P1, the cohomology sequence is surjective on H1 at every twist. Therefore

    H1(B(r)) <= -chi(Q*(r))   for r=-2,-1,0.       (1)

Only these three twists are tested; no claim that they imply all other cohomology constraints is needed. They reduce the B list to 91 shapes.

For each of the 28 proven E types, exact quotient cohomology also gives

    H0(E(2)) <= H0(A(2)),
    H0(E(3)) <= H0(A(3))+H0(A(1)),
    H1(A(r)) <= H1(E(r))   for -2<=r<=8.           (2)

For the first inequality use H0(K(2))=0. For the second, H0(K(3)) injects into H0(A(1)), since the kernel K^- has no sections at twist three. The exact sequence makes H0(E(3)) a sum of H0(K(3)) and a subrepresentation of H0(A(3)). The third is simply the H1-surjection for E -> A. All representations are semisimple in characteristic zero.

We also test the following weak, necessary Hom conditions: every block of A receives a nonzero equivariant map from E; every block of B maps nontrivially into E*(-2); and every block of A and B maps nontrivially under the two negative-transpose directions. For blocks R O(e), S O(f), a possible map requires f>=e and R to occur in S tensor Sym^(f-e) W. These tests never assert injectivity or surjectivity from nonzero Hom. The ordinary sorted degree inequality for A -> B*(-2) is also necessary. If t=0, its determinant is nowhere zero, so the exact equivariant splitting types must match.

## 3. A small certificate excluding defect twelve

Before using the additional inequalities (1)-(2), the initial Euler tests, quotient/injection Hom tests, and H0(E(2)) injection leave exactly five possible defect-twelve pairs:

    A=O(-10)+O(-8)+O(12):
      B=O(-26)+O(6)+O(8),
      B=O(-14)+O(-6)+O(8),
      B=O(-14)+Wprime O(1).

    A=W O(-9)+O(12):
      B=O(-14)+Wprime O(1),
      B=O(-26)+W O(7).

Each B contains O(-14) or O(-26), with trivial coefficient. Their H1 contributions are respectively Sym^12 W and Sym^24 W. Each contains a trivial representation, as checked by exact character arithmetic. But H1(Q*)=M2 has no trivial representation. Thus H1(Q*) cannot surject onto H1(B). All five are impossible. This proves t=0; it uses only the r=0 instance of (1).

## 4. The remaining necessary pairs

In every line B=A*(-2). The 25 possible A types are:

    O(-10)+O(-8)+O(14)
    O(-10)+O(-8)+O(16)
    O(-10)+O(2)+O(4)
    O(-10)+O(2)+O(6)
    O(-10)+2O(4)
    O(-10)+O(4)+O(6)
    2O(-8)+O(14)
    O(-8)+O(2)+O(4)
    O(-8)+O(2)+O(6)
    O(-8)+O(4)+O(6)
    O(-8)+O(4)+O(8)
    O(-8)+2O(6)
    W O(-9)+O(14)
    W O(-9)+O(16)
    Wprime O(-3)+O(4)
    Wprime O(-3)+O(6)
    Wprime O(-1)+O(2)
    Wprime O(-1)+O(4)
    Wprime O(-1)+O(6)
    V O(0)
    O(-10)+W O(3)
    O(-8)+W O(3)
    O(-8)+Wprime O(3)
    O(-10)+W O(5)
    O(-8)+W O(5)

The compact JSON contains the compatible E IDs, their eight-parameter catalog from the proven splitting note, the five excluded twelve-defect pairs, and dependency hashes. The necessary list can be reduced further without contradicting this theorem.

## Coordination and independent saturation input

Concurrently, Mr. Slop's [PR674](https://github.com/Akilleez-QA/read-em-and-weep/blob/2516a879b4b1469da1a29eaefafcfddf4e171a0d/research/hm/primal-quotient-degree-bound/PROOF.md) establishes the stronger profile-independent primal bound a>=-4 and, in profile (1,2), the same original-defect-zero conclusion by invariant multiplication. That result is credited separately. The new contribution here is the explicit finite 25-pair / 155-record necessary classification; its five-case saturation certificate is an independent alternative, not a further elimination to add to PR674. All 25 listed pairs already satisfy a>=-4. Neither argument removes the distinct second-dual defect, including its possible length twenty at a=-4.

## Reproduction and scope

Run python3 verify_one_two_finite_quotient_pairs.py. It imports only the frozen abstract character verifier and proven E-type verifier. It performs bounded operations on universal representation characters and integers, in under a second on the task environment. It writes one-two-finite-quotient-pairs.json. It asserts all displayed counts and the trivial-character obstruction for every preliminary defect-twelve pair.

No actual coefficients, points, instance matrices, rank evaluations, actual-map scans, or large computations are used. In particular this result must not be described as generic rank-three exclusion, a new lower bound SF>=4, or a positive-square rank improvement.
