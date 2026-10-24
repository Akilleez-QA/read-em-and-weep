# Independent whole-proof review of the ordered (1,2) necessary reduction

## Verdict and scope

Conditional PASS for the author's complete 60 -> 41 -> 18 -> 7 -> 3 necessary reduction, including its finite coverage, cohomology, endpoint capacities, retained torsion, and the length-three-specific N=8/N=9 rank-one endpoint gap. The separate new proof in NEW-CUT.md then cuts the two B=O(-8)+W' O(-3)+O(14) tuples, leaving one necessary tuple. No ordered-profile closure or stronger global rank theorem is claimed by this review.

All eight pinned source texts were read and independently authenticated. In particular the entire PR1140 proof, not just its headline, was read before applying its rank-independent cubic kernel alternatives.

## 1. Complete initial domains

The lower and upper endpoint ranks are thirteen and five, with derivative ranks at most three. The actual strict-top argument gives top(K)<=-3, hence a<=-40 after parity. The reversed dual plateau permits no section of Z0(2): a section reaches its constant span within at most two transforms, which would put a constant subbundle in an interior stage. Thus top(Z0)<=-3 and b<=-16 after parity. These bounds do not assert H0(Q*(1))=0.

The rank-four degree identity is 2a+b=-138+2delta1+delta2. It implies a>=-60 and 2delta1+delta2<=42. Each divisor degree is in <12,20,30>. The exact finite domain has forty-nine rows, retaining all positive defects.

For a rank-four quotient B of the fixed source E, its ascending ordinary degrees dominate the four smallest source degrees. To prove this, consider the direct sum of target blocks of degree at most a cutoff: it can be hit only by source blocks of no greater degree, so its rank cannot exceed their rank. This gives the ordered inequality for every cutoff. It is necessary, not sufficient.

Since d=degree B is in [-14,6], its smallest ordinary degree is at least the fixed source minimum and its largest at most d minus the three smallest source degrees. This is a complete finite degree range. The independent checker first enumerates ordered integer degree partitions, then all parity-compatible coefficient representations in each equal-degree group. It does not import the author's block enumeration.

## 2. Cohomology and capacity checks

The quotient E -> B gives H1(E(1)) -> H1(B(1)) surjectively and H1(E(3)) -> H1(B(3)) surjectively. Vanishing H0(K(t)) for t<=2 gives both the Euler inequalities and the source twist-two section injection.

Dualizing the coherent-image injection B -> Q(-2) gives Q* -> B*(-2) with torsion cokernel. Factoring through its locally free image proves H1(Q*) -> H1(B*(-2)) is surjective: both H2 of the kernel and H1 of the torsion cokernel vanish. Equivariant Serre duality therefore gives H0(B)<=M2. This is the valid untwisted Q* statement, not the withdrawn twist-one filter.

The actual next derivative kernel has top at most -4, so H0(K(3)) injects into H0(B(1)). Combining this with chi(K(3))=chi(E(3))-chi(B(3)) gives the top-section Euler inequality. PR1140 supplies the actual coefficient-space injection W'+2T into H0(B(3)); it is not a fiberwise rank-fourteen assertion.

For lower capacity, each successive coherent-image quotient injects into B(-2j). Its ranks form a positive nonincreasing string bounded by three; negativity and saturation exclude an early nonzero horizontal endpoint. Summing determinant bounds is therefore valid, even with unsaturated images. The independent checker maximizes over these rank strings rather than the author's height partitions.

For upper capacity, L3* injects into B*(-4), with no equality assumption. Iterated derivative quotients of Z0 inject into L3*(-2j), hence into B*(-4-2j). Maximizing against the latter larger bundle is a valid majorant. The same actual B is used at both endpoints.

The independent full source-domain counts at the successive eight filters are:

    D: 809,336,180,123,73,70,70,65,47;
    P: 512,236,130,82,47,43,43,38,28;
    V: 398,190,102,64,36,25,25,22,20;
    Z: 398,190,102,64,36,36,36,33,24.

The endpoint and degree matching leaves exactly 35,14,5,6 triples respectively. The resulting defects are delta1=0 and delta2 in {0,12}, with seven positive-defect triples. All source labels are retained, not chosen afresh for different tests.

## 3. Iterated sections and the upper Euler identity

Strict-top iteration gives top(Kj)<=top(E)-j. Choosing J=max(0,t+top(E)+1) makes H0(KJ(t)) zero, so telescoping the exact quotient sequences gives the finite section envelope. Only its necessity is used. The tested twists 2 through 32 need not be claimed exhaustive: a rejection at any tested twist is already valid. Forty-one triples remain.

After delta1=0, the exact second derivative sequence gives [L3]=[B(4)]+[T2(2)]. Duality reverses the torsion contribution, and equivariant Serre duality produces precisely

    chi Z0(t)=chi Q*(t)+chi B(-t)+chi B(2-t)+chi T2(-t).

Thus neither the torsion shift nor its sign has been dropped. At length twelve the support is the unique reduced twelve-point orbit, the cokernel has one-dimensional fibers there, and the binary stabilizer has order ten. Center-even fiber characters are exactly the five even residues. O(r) restricted to this orbit represents them, with r=0,2,4,6,8; its character is the difference of the two line-bundle Euler characters twelve degrees apart. Genuine length twelve, periodicity ten, and all five distinct characters are checked independently.

The endpoint rank-five, degree-b, top-at-most-minus-three domain has lowest degree at least b+12. Hence it is completely finite. The independent ordinary-first recursion covers every coefficient splitting. Testing the necessary Euler identities at twists zero and one yields precisely eighteen full endpoint tuples, not merely matching counts. They include the positive-defect tuple.

## 4. Horizontal and rank-one endpoint obstructions

The endpoint derivative lands in L3*(-2), which injects into B*(-6). If a direct summand has no Hom to that latter bundle and no internal Hom to (Z0/summand)(-2), it is genuinely horizontal. Its saturation in the constant ambient follows from the successive locally free quotients, so its negative degree is impossible. Eleven tuples are rejected, leaving seven.

Four have all endpoint derivative rows confined to the scalar O(2) target. Their derivative rank is exactly one, since rank zero would make Z0 negative horizontal. Let U be the actual minimal constant span. It is G-invariant and has no proper constant subspace containing the endpoint, by definition. The endpoint has no constant subbundle, so the complete unit-step saturated flag theorem applies inside U.

For the present plateau of length three, the first two forward transforms lie in interior reversed stages without constants. A rank-five rank-one endpoint cannot reach U in those two steps; therefore dim U>=8. Its degree minus twenty-two and the complete flag bound give dim U<=9. Both values must be tested; importing only the length-four N>=9 case would be invalid.

The exact weighted flag identity at N=8 has target 56, with attainable sums up to it exactly {0,36}. At N=9 its target is 18, with only {0}. The complete invariant-divisor semigroup is used in both calculations. Positive controls at permissible degrees verify that the test does not reject every flag. These four tuples are excluded.

## 5. Independent computation and new contribution

The checker independent.py has no production imports. It derives representation tensors from exact nine-class character inner products over Q(sqrt5), builds all ordinary degree partitions independently, uses decreasing rank strings for capacities, reconstructs every endpoint tuple, and proves the additional near-top multiplicity cut in NEW-CUT.md. All eighteen endpoint tuples and statuses agree exactly with the author's baseline output.

There are 3347 explicit checks. Normal, python -O, and different-working-directory outputs are byte-identical. Eight executable mutations are rejected under -O, covering the degree domain, positive torsion retention, upper twist, torsion length, cubic kernel alternative, kernel tail domain, capacity differential, and missing stabilizer character. The tests contain no selected actual geometric instance calculations.

The imported actual geometry and source necessity theorems remain explicit premises. Finite arithmetic verification is not a proof-assistant certification of them. The one residual tuple is still a necessary possibility, not a realized example. Upstream, main, and public discussions were not modified.

Only the complete 60 -> 1 necessary reduction is approved here. No further lower-kernel reduction, realization, or ordered-profile closure follows.
