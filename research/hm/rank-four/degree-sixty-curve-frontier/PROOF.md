# Degree-sixty curve frontier: normalization genus and quadratic deficiency

## Statement

Work over C with the standard projective normalizer N=A⋊SL₂(F₅), where A=F₅², and its Schrödinger action on P⁴. Let C be an N-invariant reduced curve of degree 60 with no line or conic components. Import the established exclusion of N-stable integral curves of degree at most 45, the faithful-normalizer genus lower bound 326, and the exclusion of N-invariant integral quintic surfaces.

Then C is integral. For its normalization ν:X→C and L=ν*O_C(1), necessarily:

- X→Y=X/A is étale, g(Y)=14, and g(X)=326;
- h⁰(X,L)=h⁰(C,O_C(1))=5;
- H⁰(I_C(2))=H⁰(I_C(3))=0;
- h⁰(X,L²)=h⁰(C,O_C(2))=20;
- h¹(I_C(1))=0 and h¹(I_C(2))=5;
- 326≤p_a(C)≤368.

Thus the curve must have a five-dimensional quadratic deficiency. This is a necessary-condition theorem, not an exclusion or an existence theorem. Neither normality nor arithmetic Cohen–Macaulayness is assumed.

## Dependencies

The projective group, component orbit arguments, degree-five divisibility, and small component stabilizer estimates are proved in ../rank-four-degree-fifty-equality/PROOF.md, Sections 1–3. The faithful-action lower bound is in that directory's ADDENDUM.md, Section 1; its underlying quotient-genus obstruction is ../binary-group-genus-thirteen/PROOF.md. The invariant-quintic surface exclusion, including nonnormal surfaces, is ../quintic-surface-classification/PROOF.md, together with the sectional-genus input checked in that directory's ROOT_CHECK.md. The proof also uses the classical characteristic-zero uniform position theorem and Castelnuovo's genus bound.

This argument does not depend on the newer degree-50/55 exclusion or on the irreducibility of Sym²V*. The no-quadrics assertion will follow from the no-cubics assertion.

## 1. Integrality and the complete linear series

An A-orbit of components has size 1, 5, or 25. As each component has degree at least three, size 25 costs at least 75. A size-five orbit has an order-five stabilizer in A; conjugation produces all six stabilizer axes and hence at least thirty components, costing at least 90. Thus every component is A-stable. Such a component spans P⁴ and has degree divisible by five.

The action on components factors through the perfect group SL₂(F₅). A nonsingleton orbit has size at least five. Its common degree is at most twelve and divisible by five, hence five or ten. For such components, the stabilizer argument in the imported degree-fifty proof gives an N-orbit of size at least twenty and total degree at least 100. Therefore every component is N-stable. Each has degree at least fifty by the established ≤45 exclusion and degree divisibility, so the total degree sixty forces a single component.

N acts faithfully on X: a finite projective transformation fixing a nondegenerate integral curve pointwise fixes its span. The imported group-action theorem gives g(X)≥326.

The H₅ action lifts to L. In degree n not divisible by five, its center acts nontrivially on H⁰(X,Lⁿ), so the dimension is a multiple of five. This is the usual clock-and-shift eigenspace argument and also applies to H⁰(C,O_C(n)). There are at least five sections of L from ambient hyperplanes. If h⁰(X,L)≥10, choose ten independent sections containing these five. They are basepoint free, and their map is birational onto a nondegenerate degree-sixty curve in P⁹: projecting to the original five sections recovers ν followed by the embedding of C. Castelnuovo gives

    π(60,9)=8·7·6/2+7·3=189,

since 59=8·7+3. This contradicts g(X)≥326. Therefore h⁰(X,L)=5. The inclusions of ambient sections into H⁰(C,O_C(1)) into H⁰(X,L) imply h⁰(C,O_C(1))=5 and H¹(I_C(1))=0.

## 2. There are no cubic equations

Suppose W=H⁰(I_C(3)) is nonzero. It is N-stable. The greatest common divisor of all its polynomials is well-defined up to scalar and its line is H₅-stable. If its degree were positive, it would be at most three. Every H₅ character kills its central commutator subgroup, but the center acts on degree-e polynomials by a nontrivial scalar for 1≤e≤3. This is impossible. Thus the gcd is one.

Choose f,g∈W coprime. Such a pair exists: after choosing any nonzero f, avoid for g each of the finitely many proper linear subspaces of W consisting of multiples of an irreducible factor of f. Their common zero scheme is a complete-intersection surface of degree nine.

If the base locus B=V(W) had no surface component, choose h∈W avoiding every surface component of V(f,g). Then f,g,h form a regular sequence in the polynomial ring: the first two are a complete intersection, with no embedded associated primes, and the third avoids their minimal primes. The resulting complete-intersection curve has degree 27 and contains C of degree sixty, impossible.

Consequently the union T of the reduced surface components of B is nonempty, N-stable, and has total degree at most nine. Its A-component orbits cannot have size 25. A size-five orbit would, by the six-axis argument, force at least thirty components. Therefore every component S of T is A-stable.

For completeness, 5 divides deg S. For sufficiently large n, its Hilbert polynomial P_S(n)=χ(O_S(n)) equals h⁰(O_S(n)). For n≡1,2,3 modulo five these dimensions are multiples of five. Taking the second difference at three consecutive such integers gives deg S divisible by five. Thus T has exactly one component, of degree five. Its uniqueness makes it N-stable. Its span is an A-invariant projective subspace, hence all of P⁴ by irreducibility of the Schrödinger module. This contradicts the imported invariant integral quintic-surface exclusion.

We conclude W=0. Any nonzero quadric in I_C would yield nonzero cubics by multiplication, so H⁰(I_C(2))=0 as well.

## 3. The initial uniform-position bound

Let Z=C∩H be a general hyperplane section. It consists of sixty distinct points in P³ and is in uniform position. Write h_Z(n) for the rank of degree-n polynomial evaluation on Z. The hyperplane restriction sequences give h_Z(1)=4 and h_Z(2)=10: for the second equality use I_C(1)=I_C(2)=0 and H¹(I_C(1))=0.

The standard uniform-position growth inequality is

    h_Z(a+b)≥min(60,h_Z(a)+h_Z(b)−1).

Using h_Z(1)=4 and h_Z(2)=10 gives successive lower bounds, starting at degree one,

    4,10,13,19,22,28,31,37,40,46,49,55,58,60.

The general hyperplane-section genus inequality, valid also for non-ACM integral curves, is

    p_a(C)≤Σ_(n≥1)(60−h_Z(n)).

The displayed sequence yields p_a(C)≤368, and g(X)≤p_a(C).

Put q=g(Y), where Y=X/A. The induced SL₂(F₅) action is faithful, by the deck-group argument for the invariant function field. Hence q≥14. If t is the number of A-branch points on Y, cyclic inertia has order five and Riemann–Hurwitz gives

    g(X)=25q−24+10t.

The upper bound 368 gives q≤15. For q=14 it gives t≤4, and for q=15 it gives t≤1. The branch set is SL₂(F₅)-invariant. Point stabilizers for its faithful action on the smooth curve Y are cyclic, and have order at most ten; consequently each orbit has at least twelve points. Thus t=0. The only possibilities are (q,g(X))=(14,326) or (15,351).

## 4. The genus-351 possibility is excluded

The fifteen ambient quadrics inject into H⁰(C,O_C(2)) and H⁰(X,L²). If h⁰(X,L²)≥20, choose twenty independent sections including these fifteen. The system is basepoint free and birational, since it contains the second Veronese of the original embedding. Its image has degree 120 in P¹⁹. Castelnuovo gives

    π(120,19)=18·6·5/2+6·11=336,

since 119=18·6+11. Therefore for g(X)=351, h⁰(X,L²)<20. It is a multiple of five and at least fifteen, so it equals fifteen. The intermediate space H⁰(C,O_C(2)) also has dimension fifteen, whence H¹(I_C(2))=0.

Because I_C(2)=I_C(3)=0, the hyperplane ideal restriction sequence now gives I_(Z,H)(3)=0. Thus h_Z(3)=20. Uniform-position growth improves the preceding sequence to

    4,10,20,23,29,39,42,48,58,60,

and the genus upper bound becomes

    p_a(C)≤56+50+40+37+31+21+18+12+2=267.

This contradicts g(X)=351. The same argument also rules out H¹(I_C(2))=0 when g(X)=326.

## 5. The surviving quadratic deficiency

We now have g(X)=326. If h⁰(X,L²)≥25, choose twenty-five independent sections including the fifteen ambient quadrics. The birational degree-120 image in P²⁴ satisfies

    π(120,24)=23·5·4/2+5·4=250,

since 119=23·5+4, again impossible. Thus h⁰(X,L²)≤20. By the center character it is either fifteen or twenty; fifteen is excluded by Section 4's genus-267 argument. Hence h⁰(X,L²)=20.

The H₅-module H⁰(C,O_C(2)) has dimension fifteen or twenty, because it lies between the fifteen ambient quadrics and H⁰(X,L²). Dimension fifteen would again imply H¹(I_C(2))=0 and the same contradiction. It therefore has dimension twenty, and the ambient restriction sequence yields

    h¹(I_C(2))=20−15=5.

This nonzero Rao space proves that C is not arithmetically Cohen–Macaulay. Equality of the two degree-two section spaces does not prove C is normal or smooth. The normalization defect is only bounded here by

    0≤p_a(C)−g(X)≤42.

An optional further bound, useful for subsequent analysis, is h⁰(X,L³)≤40: forty-five sections containing the thirty-five ambient cubics would give a birational degree-180 image in P⁴⁴ and π(180,44)=43·4·3/2+4·7=286. Thus h⁰(C,O_C(3)) is 35 or 40 and h¹(I_C(3)) is zero or five. No multiplication-map conclusion is asserted here.

## Scope

No source tensor, coefficient, selected input, or problem-specific operation matrix was evaluated. Only proof documents and established abstract representation/geometric facts were used.  This proof leaves the genus-326, degree-sixty, quadratic-deficiency-five case open.
