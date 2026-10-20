# Rank-three curves: only a possible orbit of twenty-five lines

## Statement and dependencies

Work over C with the five-dimensional Schrödinger representation V of H₅. Write A=H₅/Z(H₅)≅F₅² and let N⊂PGL(V) satisfy A normal in N, N/A≅SL₂(F₅), with the standard faithful conjugation action on A. All invariant cycles below are actual cycles, not just numerical classes.

Use the established N-equivariant linear 20-by-15 matrix b of ../rank-one-middle-curve-exclusion/PROOF.md, with

    rank b_u = 4 + rank Q_u,
    Z_j = { [u]∈P(V) : rank Q_u≤j }.

Assume the additional decic-closure conclusion dim Z₅≤1, with precisely the dependencies recorded in Section 7 of that proof. Let Γ₃ denote the reduced sum of all one-dimensional irreducible components of Z₃.

**Theorem.** Either Γ₃=0, or Γ₃ consists of exactly twenty-five distinct lines forming one N-orbit and also one free A-orbit on the component set. In particular deg Γ₃=25 in the nonzero case. Degree 35 is impossible.

This is a necessary configuration, not an existence assertion. Isolated points of Z₃ and its scheme structure are not classified. The proof does not imply that Z₃ is finite.

The imported geometric exclusions are ../normalizer-small-curve-exclusion/PROOF.md (no nonzero invariant effective cycle of degree ≤20) and its ADDENDUM_DEGREE_30.md, Sections A–D. We provide the new genus extension and all additional reductions below. No actual source map, numerical instance, or application is evaluated.

## 1. The determinantal multiplicity bound gives degree at most 37

Let L₁₀ be the space spanned by all 10-by-10 minors of b. These are homogeneous forms of degree ten, with common base support

    Bs(L₁₀) = {rank b≤9} = Z₅.

Since this support has dimension at most one, three members g₁,g₂,g₃ can be chosen to form a homogeneous regular sequence: choose the first nonzero, the second avoiding its finitely many hypersurface components, and the third avoiding the surface components of their intersection. At each stage none of those components lies in the base support. The intermediate complete intersections are Cohen–Macaulay and unmixed, so this component avoidance gives nonzerodivisors. Their common zero scheme W is a pure curve of degree 10³=1000.

For a reduced integral curve C⊂Z₃ with generic point η, R=O_(P⁴,η) is regular local of dimension three. Let m be its maximal ideal. The rank of b modulo m is s≤7. Splitting off an invertible s-by-s block gives diag(I_s,M), with all entries of M in m. Each 10-minor belongs to m^(10−s)⊂m³. Determinantal ideals are unchanged by invertible row/column operations. Thus g_i∈m³.

Since C is a component of W, q=(g₁,g₂,g₃)R is an m-primary parameter ideal. Its colength is the generic multiplicity of W along C. The regular-sequence and regular-local associated-graded formulas give

    length(R/q^n) = length(R/q) binom(n+2,3),
    length(R/m^(3n)) = binom(3n+2,3).

The containment q^n⊂m^(3n) implies, by comparing leading cubic coefficients, length(R/q)≥27. This argument requires neither smoothness of C nor transverse intersection.

N-equivariance makes Γ₃ an invariant reduced effective cycle. Every component contributes at least 27 times its degree to W, whence

    27 deg Γ₃ ≤1000,
    deg Γ₃ ≤37.                                              (1)

The chosen W need not be N-invariant.

## 2. Heisenberg-invariant reduced curves have degree divisible by five

Let D be any A-invariant reduced projective curve, possibly reducible. Its invariant homogeneous ideal gives H₅-actions on H⁰(D,O_D(n)). The center acts by the scalar character of weight n, up to the immaterial dual sign convention. If 5∤n this character is nontrivial, and the dimension of the representation is divisible by five. Indeed, clock and shift generators cyclically permute five eigenspaces of equal dimension when their commutator has primitive fifth-root scalar.

For sufficiently large n, higher cohomology vanishes, so

    h⁰(D,O_D(n)) = d n + χ(O_D),    d=deg D.

Take consecutive sufficiently large integers n≡1 and n+1≡2 modulo five. Both dimensions are divisible by five; their difference is d. Thus

    5 | deg D.                                               (2)

This applies to Γ₃'s reduced support and separately to any A-stable integral component. From (1), (2), the degree-≤20 exclusion, and the degree-30 exclusion, a nonzero Γ₃ initially has degree 25 or 35. The argument below also directly excludes the degree-30 configuration without needing that imported theorem.

## 3. SL₂(F₅) has no faithful action on a curve of genus at most eight

The degree-30 addendum, Section A, proves the result in genera at most six. Recall also its exclusion of faithful A₅-actions in genera 1, 2, and 3. We treat h=7 and h=8 without claiming an A₅ genus-four exclusion.

Suppose G=SL₂(F₅) acts faithfully on a smooth projective curve Y of genus h∈{7,8}. Its central involution z=−I acts nontrivially. On B=Y/⟨z⟩ the induced A₅-action is faithful: the kernel on the invariant function field is exactly the degree-two deck group. If r=g(B), Riemann–Hurwitz reads

    2h−2 = 2(2r−2)+b,
    b = 2h+2−4r ≥0,

where b is the number of distinct branch points on B. Consequently r≤4. Genera r=1,2,3 are excluded by the imported A₅ result.

If r=0, then b=16 or 18. A point stabilizer for a faithful finite action on a smooth curve in characteristic zero is cyclic (its action on the tangent line is faithful). In A₅ cyclic subgroups have orders 1,2,3,5. Every orbit on P¹ therefore has size 60,30,20,12. Neither 16 nor 18 is a sum of such sizes. An invariant branch set of the required size is impossible.

It remains to consider r=4. If h=8, then b=2. On any smooth curve with faithful A₅-action every orbit has size at least 12 by the same cyclic-stabilizer observation. Thus the invariant two-point branch set is impossible.

If h=7, then b=0 and z acts freely on Y. The only involution in G is z: an order-two determinant-one matrix over F₅ is diagonalizable with eigenvalues ±1, leaving only I and −I. Every cyclic subgroup of even order therefore contains z. Since a point stabilizer is cyclic and z is free, every nontrivial point stabilizer has odd order. Its injection into A₅ implies that this order is 3 or 5.

Let q be the genus of Y/G, and let a,c count branch points of inertia orders 3,5. Riemann–Hurwitz for the degree-120 quotient gives

    1/10 = (2h−2)/120 = 2q−2 + 2a/3 + 4c/5.

For q≥2 the right side is at least 2. For q=1 it is either zero or at least 2/3. For q=0, multiplication by 30 gives

    20a+24c = 63,

impossible since the left side is divisible by four. This excludes the last case and proves the genus-at-most-eight obstruction.

## 4. No N-stable integral curve of degree at most 35

An A-stable integral curve C spans P⁴ by irreducibility of the Schrödinger representation. Any projective transformation fixing C pointwise is scalar: C lies in a finite union of projectivized eigenspaces, hence, by integrality, in one eigenspace; nondegeneracy forces that eigenspace to be V. Thus, if C is N-stable, the induced action on its smooth normalization X is faithful.

For d=deg C≤35, Castelnuovo's geometric-genus bound gives

    g(X)≤π(35,4)=176,

since 35−1=3·11+1 and π(35,4)=3·11·10/2+11. This bound applies to integral singular embedded curves by applying the birational linear series on the normalization.

Put Y=X/A. Riemann–Hurwitz for the degree-25 quotient gives

    g(Y)≤floor((g(X)+24)/25)≤8.

The induced N/A-action on Y is faithful: an element of N trivial on k(X)^A is in the Galois deck group A. Section 3 is a contradiction. Therefore no such N-stable integral curve exists.

## 5. Component-orbit classification up to degree 37

Let Γ be a nonzero N-invariant reduced curve cycle of degree at most 37. This includes Γ₃. For any component C, its A-orbit has size 1,5, or 25.

### 5.1. An A-orbit of size 25 forces precisely twenty-five lines

The N-orbit of C is a disjoint union of A-orbits of size 25, by normality. Its size is a multiple of 25. The degree bound forces exactly 25 components, all of degree one. Their reduced orbit sum Δ is N-invariant of degree 25. The remainder Γ−Δ is invariant effective of degree at most 12, so the degree-≤20 exclusion forces Γ−Δ=0. Thus Γ=Δ is one orbit of twenty-five lines, and A acts freely and transitively on its components.

### 5.2. An A-orbit of size five is impossible

The component's A-stabilizer is an axis of F₅². SL₂(F₅) is transitive on the six axes, and A-orbits with different stabilizers are disjoint. Hence its N-orbit has at least 30 components. If their common degree is at least two, the total degree is at least 60. If they are lines, Section C of the degree-30 addendum proves the stronger bound of at least 60 lines: for each axis, its normalizer acts by all affine label transformations on the five eigenlines and is transitive on their ten unordered pairs; the six axes yield disjoint sets of ten projective lines. Either way degree ≤37 is impossible.

### 5.3. All components A-stable is impossible

Every such component is nondegenerate and has positive degree divisible by five, by Section 2; hence degree at least five. There are at most seven components. The N-action on their set factors through G=SL₂(F₅), of order 120. Each orbit size divides 120 and is at most seven, so its possible sizes are 1,2,3,4,5,6. Sizes 2,3,4 cannot occur: G is perfect, so its permutation image is perfect, whereas the corresponding symmetric groups are solvable. Thus each orbit has size 1,5, or 6.

A singleton is an N-stable integral curve whose degree is at most 37 and divisible by five, hence at most 35. Section 4 excludes it.

For an orbit of size m=5 or 6 and common component degree d, we have md≤37, so d≤7. Degree divisibility forces d=5. Section D of the degree-30 addendum excludes either orbit size: the normalization of an A-stable quintic is elliptic, A acts by translations, and the stabilizer N_C acts on A through the cyclic group of elliptic automorphisms modulo translations, of order at most six. Faithfulness of N/A→Aut(A) then gives

    |N_C/A|≤6,
    [N:N_C]≥20.

For clarity, the elliptic claim follows from Castelnuovo g≤1 and the faithful A-action excluding genus zero; it is not a smoothness claim about the original embedded curve. Thus neither orbit of size five nor of size six can occur.

All alternatives except Section 5.1 have been excluded. Applying this classification to Γ₃ proves the theorem.

## Scope of the conclusion

The determinantal bound, Heisenberg degree congruence, and component-orbit restrictions prove a dichotomy: the rank-at-most-three locus has no curve, or its entire reduced curve part is one twenty-five-line orbit. They do not establish that such an orbit exists or lies in this rank locus, and do not remove possible isolated rank-at-most-three points. The separate rank-at-most-two finiteness result implies, if additionally invoked, that each of these hypothetical lines has residual rank exactly three at its generic point.
