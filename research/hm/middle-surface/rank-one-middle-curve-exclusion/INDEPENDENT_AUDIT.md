# Independent audit: residual-rank-one middle curves

## Verdict

PASS for the structural argument described below, conditional on the explicitly imported full-normalizer/bundle hypotheses and the established bound dim{rank Q≤3}≤1. It proves that the closed residual-rank-one locus D1 is finite (possibly empty). It does not assert that D1 is empty or reduced.

Audited independently against:

- /research/hm/middle-surface/low-metric-rank-middle-exclusion/PROOF.md, Sections 1–2 (definition of Q and exclusion of residual rank zero);
- /research/hm/rank-four/quintic-surface-classification/RANK_AT_MOST_THREE_COROLLARY.md, hypotheses and Section 1 (the rank-at-most-three locus has dimension at most one under the full imported hypotheses);
- /research/hm/rank-four/normalizer-small-curve-exclusion/PROOF.md (no nonzero N-invariant effective curve cycle of degree at most twenty).

## 1. Global matrix, twist, and rank

The middle contraction is the bundle morphism

    b: U⊗Sym²V → J⊗O,   u⊗(ab) ↦ f(a,u,b),

where U=O(-1), dim Sym²V=15, and dim J=20. Thus in constant bases it is a 20-by-15 matrix of homogeneous linear forms. Its 8-by-8 minors are homogeneous degree-eight forms (some may vanish identically).

At [u], the subspace u·V⊂Sym²V has dimension five. Its image under b is the repeated-input image, of dimension four: u² maps to f(u,u,u)=0, and modulo Cu the map v↦f(u,u,v) is injective. After quotienting by this subspace in the source and its image in the target, the resulting map is precisely the established residual map Q: U⊗Sym²(V/Cu)→J/I. Elementary rank additivity therefore gives

    rank b_u = 4 + rank Q_u.

Consequently the common zero support of all degree-eight minors is exactly Z3={rank Q≤3}. No matrix evaluation is needed. The rank-fourteen quotient presentation G is not needed for this elementary identity; it enters the imported proof of the dimension bound.

## 2. Existence and purity of a degree-512 complete intersection

Let L⊂S8, S=C[x0,…,x4], be the linear span of the minors. Its projective base support has dimension at most one. Hence its homogeneous ideal has height at least three. This includes an empty base support.

Choose F1,F2,F3∈L successively. At the first step choose F1≠0. If i<3 forms have already been chosen as a regular sequence, S/(F1,…,Fi) is Cohen–Macaulay and its associated primes are its minimal primes, all of height i. No such prime can contain L: for i≤2 it would supply a projective component of the base support of dimension at least two (or all P4 for i=0). Each forbidden containment defines a proper linear subspace of L; finitely many cannot exhaust L over C. Choose the next form outside their union.

Thus three general forms can be chosen to form a homogeneous regular sequence. Their quotient is Cohen–Macaulay, with all minimal primes of height three and no embedded primes. Its projectivization T is a pure one-dimensional complete intersection of degree 8³=512. In particular every integral curve contained in the base support is an irreducible component of T. This proves the required proper intersection rather than assuming a generic-transversality statement along the base locus.

## 3. Generic-point order of vanishing

Let C be any irreducible curve component of D1. At its generic point η, the ambient ring R=O_(P4,η) is regular local of dimension three, with maximal ideal m and residue field C(C). Residual rank zero is excluded, so b modulo m has rank exactly five. An invertible 5-by-5 block and local invertible row/column operations put b into a unit identity block of size five plus a complementary matrix whose entries all belong to m.

Determinantal ideals are unchanged by these operations. Every 8-by-8 minor of the resulting block matrix uses at least three entries from the complementary block; hence I8(b)R⊂m³. Equivalently, the elementary identity after splitting a unit rank-five block is I8(b)=I3(complement). Therefore every chosen Fi belongs to m³.

Because T is a pure curve and C is a component, q=(F1,F2,F3)R is m-primary. Its generators form a system of parameters in the regular, hence Cohen–Macaulay, local ring R. Therefore

    length_R(R/q) = e(q,R).

For every n, q^n⊂m^(3n), and thus

    length(R/q^n) ≥ length(R/m^(3n)).

Comparing the degree-three leading terms of the Hilbert–Samuel polynomials gives e(q,R)≥27e(m,R)=27. This establishes generic multiplicity at least 27 with no smoothness assumption on C and no assumption on leading forms of Fi.

## 4. Degree budget and invariance

The fundamental cycle of T has coefficient length(O_(T,η)) at each integral curve component C. By the preceding calculation, its coefficient is at least 27 at each component of D1. All other components have positive coefficients. Consequently, writing Ctot for the reduced union of all curve components of D1,

    27 deg(Ctot) ≤ deg T = 512,
    deg(Ctot) ≤ floor(512/27) = 18.

Other rank-two or rank-three base curves are harmless: they consume some of the remaining degree. Distinct curves may intersect at closed points, but they have distinct generic primes, so these intersections do not affect the local length or cycle calculation. No hypothesis that D1 is isolated inside Z3 is used.

D1 is closed, projective, and N-stable; therefore the reduced sum of its one-dimensional components is an N-invariant effective cycle. If nonempty, its degree is between one and eighteen, contradicting the imported exclusion for degrees at most twenty. D1 has no curve component. Since D1⊂Z3 and dim Z3≤1, it follows that D1 has dimension at most zero and hence is finite.

## Scope and non-circularity

The key new degree upper bound uses the rank-at-most-three dimension theorem, not merely the earlier bound dim D1≤1. The normalizer small-cycle theorem is used only after the effective, actually invariant reduced cycle has been constructed. Invariance of a Chow class alone would not suffice, but is not what is used here. The stronger optional degree-24 or degree-30 exclusions are unnecessary.


## 5. Line-by-line review of the main proof

After the initial independent derivation, the completed PROOF.md (Sections 1–6) was read and checked. Verdict: PASS. Its version is slightly stronger than the preliminary derivation above: it permits generic matrix rank s≤5, so all minors have order at least 8-s≥3. Thus it proves finiteness of the whole rank-at-most-one support without invoking the separate rank-zero exclusion. The exact formulas length(R/q^n)=length(R/q)·binom(n+2,3) and length(R/m^a)=binom(a+2,3) are correct for a parameter regular sequence and a three-dimensional regular local ring, respectively. Their limiting quotient is 27.

## 6. Conditional extension to residual rank at most two

The same argument proves the following stronger conditional result: if the imported geometry establishes dim Z5≤1, where Z5={rank Q≤5}, then Z2={rank Q≤2} is finite.

Indeed take the span of the 10-by-10 minors of b. Its base support is {rank b≤9}=Z5. Three members form a pure degree-1000 complete-intersection curve by precisely the regular-sequence argument above. At the generic point of any curve in Z2, rank b≤6. Splitting its actual rank s≤6 gives every 10-minor order at least 10-s≥4, hence generic colength at least 4³=64. The reduced union of Z2 curves consequently has degree at most floor(1000/64)=15. It is N-invariant and is excluded by the degree-at-most-twenty theorem.

This extension is algebraically sound; its additional input is dim Z5≤1. It must not be deduced from dim Z3≤1 alone. The same proof is independent of rank-zero exclusion, residual rank constancy at closed points, and separation of curves in the base locus.

### Completed Section 7 review

The appended Section 7 of PROOF.md has now been read in full. PASS. It explicitly declares dim Z5≤1 as premise (8), cites the genus-eleven closure and independent audit, and correctly warns that the original surface reduction and other genus exclusions remain necessary. In particular it does not claim the genus-eleven argument by itself establishes (8).

Its integrated fiber calculation is correct with the listed imported bounds: ranks one, two, three–five, and at least six contribute affine dimensions at most six, five, six, and six, respectively. Residual rank zero is explicitly excluded by the separate imported theorem. Thus the bound six for all independent-zero components follows under the additional premise (8). This audit does not independently re-audit the decic surface reduction or the genus-six/genus-sixteen exclusions.

## 7. Exact integrated dependency and global conclusion

The precise integration artifact is /research/hm/middle-surface/independent-dimension-six/PROOF.md. Its Sections 1–4 were independently reviewed. Section 1 supplies dim Z5≤1 from the already audited decic surface reduction and all three exclusions of sectional genera 6, 11, and 16. The reduction's stated hypotheses and conclusions were cross-checked directly in /research/hm/middle-surface/decic-middle-surface-constraints/PROOF.md. Thus the additional premise in Section 6 above is now supplied by this explicit chain, under the original global hypotheses.

Section 2 then applies the checked degree-1000/multiplicity-64 argument to the reduced union of ALL curve components of Z2, which is the invariant union. Section 3 correctly combines the rank-stratum fiber dimensions to give independent-zero affine dimension at most six. Section 4 correctly deduces that the rank-one scaling diagonal (three nonzero vectors spanning one common one-dimensional vector subspace) is the unique seven-dimensional irreducible component in the all-three-inputs-nonzero zero locus. It is closed there and irreducible of dimension seven; the independent locus and its closure have dimension at most six, so no independent component can contain or enlarge it.

Verdict: PASS for the integration, relative to its explicitly audited component results. Two minor wording clarifications were sent to the author: use the union of all Z2 curve components when asserting invariance, and describe the diagonal as a common one-dimensional subspace of V, equivalently the same point of P(V), rather than a common projective line. These clarify the intended objects and do not require any change to the argument. No new source evaluation is made.
