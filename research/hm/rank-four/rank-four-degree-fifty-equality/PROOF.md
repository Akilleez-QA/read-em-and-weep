# Conditional classification of the degree-fifty equality case

## Statement and dependencies

Work over C with the projective Schrödinger normalizer N, its normal subgroup A≅(Z/5)², and G=N/A≅SL₂(F₅) acting faithfully and standardly on A. Let Γ⊂P⁴ be a nonzero N-invariant reduced curve of total degree 50, with no line or conic components.

Then Γ is integral. If X is its smooth normalization and Y=X/A, then

- X→Y is étale of degree 25;
- g(Y) is 14 or 15;
- g(X) is respectively 326 or 351.

This is a necessary-condition theorem, not an existence assertion or an exclusion of degree 50.

The representation-theoretic dependencies are: every A-stable integral curve spans P⁴, every A-stable integral curve has degree divisible by five, and the standard G-action is transitive on the six order-five subgroups of A. These are established in ../rank-three-curve-constraints/PROOF.md and ../normalizer-small-curve-exclusion/PROOF.md. We also import the faithfully acting G genus-at-most-thirteen obstruction proved in ../binary-group-genus-thirteen/PROOF.md. The remaining tools are Castelnuovo's bound, Riemann–Hurwitz, and elementary finite-group and elliptic-curve facts.

For Γ=Γ₄, N-invariance and the no-line/no-conic hypotheses are imported from ../rank-four-line-component-exclusion/PROOF.md and ../rank-four-canonical-conic-exclusion/PROOF.md, with their dependencies. The newer cubic/quartic exclusion is not needed here.

## 1. All components are A-stable

The A-orbit of an integral component has size 1, 5, or 25. All component degrees are at least three. An orbit of size 25 would already contribute at least 75 to the degree.

For an orbit of size five, the A-stabilizer of the component is an order-five subgroup. It is constant on this A-orbit because A is abelian. Conjugation by N produces all six such subgroups, and A-orbits with different stabilizers are disjoint. Thus the N-orbit contains at least 30 components and contributes degree at least 90. This too is impossible.

Every component is therefore A-stable. Each spans P⁴, has degree divisible by five, and admits a faithful action of its N-stabilizer on its normalization. For the last assertion, a projective transformation fixing an integral nondegenerate curve pointwise must be scalar: the curve lies in the union of its projectivized eigenspaces, hence by integrality in one, and its span is all of P⁴.

## 2. Small-degree A-stable components have large N-orbits

Let C be A-stable of degree at most ten, let X_C be its normalization, and write K=N_C. Castelnuovo gives

    g(X_C) ≤ π(10,4) = 9.

Point stabilizers in a faithful finite action on a smooth complex curve are cyclic, since they act faithfully on the tangent line. For the A-action, each nontrivial inertia group therefore has order five. If q=g(X_C/A) and t counts branch points on the quotient, Riemann–Hurwitz gives

    g(X_C) = 25q − 24 + 10t.

The bound 0≤g(X_C)≤9 forces precisely two possibilities:

    (g(X_C),q,t) = (1,1,0) or (6,0,3).

Indeed q≥2 is impossible; q=1 forces t=0; and q=0 forces t=3.

In the genus-one case, A acts by translations, since its image in the origin-fixing elliptic automorphism group (cyclic of order 2, 4, or 6) is trivial. Conjugation on A by K factors through this elliptic automorphism quotient. The prescribed action K/A→Aut(A) is faithful, so |K/A|≤6.

In the genus-six case, the induced K/A-action on X_C/A≅P¹ is faithful. To justify this carefully, any element of K acting trivially on the invariant function field C(X_C)^A is a deck transformation of the degree-25 Galois extension C(X_C)/C(X_C)^A, hence lies in A. This proves that the kernel is exactly A. The induced group preserves the three branch points. Its permutation action on these points is faithful, because an automorphism of P¹ fixing three distinct points is the identity. Thus K/A embeds in S₃ and again |K/A|≤6.

In both cases,

    [N:K] = 120/|K/A| ≥20.

Consequently the N-orbit of such a component has degree at least 20·5=100.

The genus-six case is essential: a faithful (Z/5)²-action of genus six does exist, for example on the Fermat quintic. It would be incorrect to infer elliptic normalization from genus at most nine alone.

## 3. Integrality

The action of N on the components factors through the perfect group G. Any orbit of size at most four is a singleton, since its permutation image would be a perfect subgroup of a solvable symmetric group.

If there were a nonsingleton component orbit of size m, then m≥5. Its common degree d is divisible by five and md≤50, so d is five or ten. Section 2 rules this out. Thus every component is N-stable.

An N-stable integral component of degree at most 45 is excluded by ../binary-group-genus-thirteen/PROOF.md, Section 4: its normalization has genus at most 301, its A-quotient has genus at most thirteen, and the induced G-action on that quotient is faithful, a contradiction. Since every component degree is a positive multiple of five and the total is 50, there can only be one component, of degree 50.

## 4. The quotient genus and the genus-sixteen obstruction

For the normalization X of Γ, Castelnuovo gives

    49 = 3·16 + 1,
    g(X) ≤ π(50,4) = 3·16·15/2 + 16 = 376.

The quotient Y=X/A satisfies

    g(Y) ≤ floor((376+24)/25) = 16.

The induced G-action on Y is faithful by the invariant-function-field argument in Section 2. The imported genus obstruction yields g(Y)≥14.

We exclude genus sixteen directly. In G the nonidentity element orders are 2,3,4,5,6,10, and the unique involution is the central element z=−I. For a faithful G-action on a genus-sixteen curve, Riemann–Hurwitz for its G-quotient, of genus r, reads

    1/4 = 2r−2 + Σ(1−1/e_i).

The right side forces r=0 and either three or four branch points: for r=1 a positive ramification contribution is at least 1/2; r≥2 is impossible; and five branch points give at least 1/2 when r=0. The complete unordered signature list is

    (3,4,6), (4,4,4), (2,2,2,4).

For completeness, a three-entry signature requires reciprocals summing to 3/4. For smallest entry two, checking the other entry in {2,3,4,5,6,10} gives no allowed third entry (the only positive candidate reciprocals for sorted entries give third entries 20,12,20/3). For smallest entry three, the second entry three gives third entry twelve, four gives six, and five gives 60/13; larger second entries cannot work with sorting. For smallest entry four, equality requires all entries four. A larger smallest entry makes the sum too small. For four entries, the all-two tuple has reciprocal sum two, and decreasing that sum by 1/4 requires precisely one replacement of two by four: replacing one two by three decreases by 1/6, two such replacements already decrease by 1/3, and replacing by five or more decreases by more than 1/4.

Branch cycles have these exact orders, product one, and generate G. For (2,2,2,4), the first three cycles equal z, so the fourth must equal z, contrary to its order four.

For (3,4,6), projection to G/⟨z⟩≅A₅ gives a generating triple of orders (3,2,3), with product one. The two three-cycles cannot generate A₅ if their product has order two: if their supports meet in one letter their product is a five-cycle; otherwise they are supported on at most four letters and fix a common letter. This is a contradiction.

For (4,4,4), projection gives three involutions with product one. The first two have involutory product and therefore commute, so the generated group has order at most four, not 60. This too is impossible. Hence g(Y)∈{14,15}.

## 5. The A-cover is étale

Let n be the number of branch points of X→Y. Every nontrivial inertia group has order five, so

    g(X) = 25g(Y) −24 +10n.

For g(Y)=14 the genus bound gives n≤5; for g(Y)=15 it gives n≤2.

The branch set on Y is G-invariant, since A is normal in N. Every point stabilizer in the faithful G-action on Y is cyclic. Its order is therefore at most ten, by the element-order list for G, so every G-orbit on Y has at least 120/10=12 points. A nonempty invariant branch set would have at least twelve points, contradicting either bound. Thus n=0 and the asserted genera follow.

## Scope

This argument concerns the reduced curve support and its normalization. It does not establish smoothness of the embedded curve, control its scheme multiplicity or isolated points, construct an étale cover with the required projective realization, or exclude the two surviving normalization genera. No source tensor, source coefficient, selected source input, or problem-specific operation matrix was evaluated.
