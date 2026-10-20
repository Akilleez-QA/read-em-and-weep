# Independent audit: the rank-four curve has total degree at least 100

## Verdict

The proposed strengthened bound is valid, conditional on the explicitly imported curve exclusions and the order-five lift/linearization theorem in `../smooth-normalizer-polarization-divisibility/PROOF.md`. The order-24 and order-20 subgroup argument has no gap. In fact, its divisor argument extends directly to disconnected normalization and gives a shorter proof. Neither route evaluates a source tensor or rank instance.

## 1. Imported facts and reduction

Let N=A semidirect G, A=F_5^2, G=SL_2(F_5), and |N|=3000. Let Gamma be the nonempty reduced curve support in question. Import:

1. N-invariance, degree at most 125, and exclusion of line/conic components from the established rank-four proofs.
2. Exclusion of degree-three/four components from `../rank-four-degree-three-four-exclusion/PROOF.md`. Thus every component has degree at least five.
3. Any A-stable integral component spans P^4 and has degree divisible by five, from `../rank-three-curve-constraints/PROOF.md`, Sections 2 and 4.
4. There is no N-invariant reduced nonempty curve of degree at most 55 without line or conic components, from `../rank-four-degree-sixty-lower-bound/PROOF.md`, Section 5.
5. O(5) is canonically N-linearized; every order-five element acts trivially on its fibre at any fixed projective point; the only possible nonidentity element orders in N are 2,3,4,5,6,10. These are established in `../smooth-normalizer-polarization-divisibility/PROOF.md`, Sections 1–3.

Suppose deg Gamma<100. An A-orbit of 25 components contributes at least 125. An A-orbit of five components has an order-five stabilizer in A. Its N-translates include all six possible stabilizers, since G acts transitively on the six axes. The corresponding A-orbits are disjoint, giving at least 30 components and degree at least 150. Both cases are impossible. Consequently every component is A-stable and spans P^4.

The same reduction works for any total degree strictly less than 125.

## 2. Disconnected-normalization divisibility lemma

**Lemma.** If D is an N-invariant reduced projective curve, every integral component of which spans P^4, then 50 divides deg D.

Let X be the disjoint union of the smooth normalizations of the integral components of D. The N-action lifts to X, and M=nu^*O_D(5) is N-linearized. Its total degree is 5 deg D.

For each N-orbit of connected components of X, choose a representative X_C and let K=N_C. The K-action on X_C is faithful. Indeed, if a projective transformation fixes the integral curve C pointwise, C is contained in one projectivized eigenspace of a linear representative; its full span forces that representative to be scalar. Thus the transformation is the identity in N.

Galois descent/Hilbert theorem 90 for the faithful finite action of K on k(X_C) gives a nonzero K-invariant rational section of M restricted to X_C. Transport this section to all translates of X_C using the N-linearization. It is independent of the chosen transporter precisely because the original section is K-invariant. Doing this separately for every component orbit gives an N-invariant rational section sigma on X, nonzero on every component. There is no gluing condition across intersections of components, since X is their disjoint normalization.

A stabilizer N_p of a point p of X preserves its connected component. Its action there is faithful by the preceding full-span argument. Its derivative at p is injective: a finite-order automorphism of a smooth complex curve with derivative one at a fixed point is the identity. Thus N_p is cyclic, of order e in {1,2,3,4,5,6,10}.

Let m_p be the coefficient of p in div(sigma). If 5 divides e, restrict to the order-five subgroup. It acts trivially on M_p by imported fact 5 and faithfully on the tangent line. Comparing the leading Laurent term of the invariant section in a local parameter gives 5|m_p. Negative coefficients present no problem.

The coefficient is constant on each N-orbit of points. That orbit has size 3000/e. Its contribution to the total degree of div(sigma) is therefore:

- e=1: 3000m;
- e=2: 1500m;
- e=3: 1000m;
- e=4: 750m;
- e=5: 600m with 5|m;
- e=6: 500m;
- e=10: 300m with 5|m.

Every contribution is divisible by 250. The divisor has finite support on the finite disjoint union X, so 250 divides deg M=5 deg D. This proves the lemma.

Applying the lemma after Section 1 gives 50|deg Gamma. A positive total below 100 must therefore equal 50, excluded by imported fact 4. Hence Gamma is empty or has degree at least 100.

In fact, the original upper bound yields the sharper discrete statement:

    Gamma is empty, or deg Gamma is 100 or 125.

Indeed, any total strictly less than 125 has only A-stable components, so the lemma forces a multiple of 50. This does not exclude 125: a free A-orbit of 25 quintic components costs exactly 125 and need not have full-span components.

## 3. Audit of the originally proposed subgroup proof

This gives an alternative proof without using disconnected normalization.

Under deg Gamma<100 all components are A-stable. Let C have degree d and N-orbit size m. Its stabilizer K contains A and is exactly the full inverse image of H=K/A in G: the inclusion in that inverse image is immediate, and both groups have order 25|H|. Therefore in the fixed splitting K=A semidirect H. No conjugacy classification of complements is needed.

A singleton orbit gives an N-invariant integral curve. By the integral divisibility theorem its degree is divisible by 50. Under the degree budget the only possibility is d=50, excluded by the integral degree-at-most-55 theorem.

For nonsingleton orbits, perfectness of G rules out m=2,3,4, because a perfect subgroup of a solvable S_m is trivial. Thus m>=5. If d=5 or 10, `../rank-four-degree-fifty-equality/PROOF.md`, Section 2, gives m>=20, so md>=100. Otherwise 5|d gives d>=15, and md<100 forces m=5 or 6 (and in fact d=15). These correspond to |H|=24 or 20.

For |H|=24, |K|=600. An element of order ten would project to an element of order ten in H: any such cyclic subgroup has trivial intersection with the exponent-five translation group unless the projected order is two; but projection order two has (s-I) invertible and is translation-conjugate to s, hence itself has order two. More directly, the element-order calculation in the imported theorem shows that quotient order identity or five gives order at most five, while any quotient without eigenvalue one has exactly that quotient order. Since 10 does not divide 24, order ten cannot occur. Thus stabilizer orders lie in {1,2,3,4,5,6}. The K-invariant rational section of M_C gives orbit contributions divisible by the gcd of

    600, 300, 200, 150, 600, 100,

which is 50. The entry for inertia five uses coefficient divisibility by five. Hence 50|deg M_C=5d, or 10|d. This excludes d=15. Equivalently, d>=20 forces md>=100.

For |H|=20, |K|=500. Lagrange's theorem together with the N element-order list restricts stabilizers to {1,2,4,5,10}. The effective orbit contributions are multiples of

    500, 250, 125, 500, 250,

whose gcd is 125. Thus 125|5d, or 25|d. This excludes d=15 and gives the stronger md>=150 for any orbit of size six.

Both stabilizer actions are faithful because C spans P^4. Their order-five fibre triviality is inherited by restriction of the same N-linearization, so no new representation-theoretic input is required.

## 4. Boundaries

This audit establishes a reduced-support degree restriction, conditional on the imported established theorems. It neither proves the rank-four curve exists nor excludes degree 100 or 125, and it does not determine scheme multiplicity or isolated points. All work used local proof files and finite-group/curve arguments. No actual source-instance evaluation is claimed.
