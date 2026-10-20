# Excluding small normalizer-invariant curve cycles

## Statement and hypotheses

Work over an algebraically closed field k of characteristic zero. Let V be the five-dimensional Schrödinger representation of the Heisenberg group H₅, and let

N ⊂ PGL(V),    H = H₅/Z(H₅) ≅ (F₅)²,

with H normal in N, N/H ≅ SL₂(F₅), and conjugation on H the standard two-dimensional action. Assume, as in the projective Heisenberg normalizer, that N acts faithfully on P(V). The argument needs this exact sequence and conjugation action; a chosen splitting is unnecessary.

**Theorem.** There is no nonzero N-invariant effective one-dimensional cycle in P(V) ≅ P⁴ of degree at most 20. In particular, degrees 10 and 20 are impossible.

Here an effective cycle is a finite sum Z = Σ mᵢ[Cᵢ], with distinct reduced integral curves Cᵢ and positive integer multiplicities mᵢ. Invariance means invariance of the cycle itself, not merely of its Chow class.

## 1. Component orbits

Let C be a component of an invariant effective cycle Z with deg Z ≤ 20. Its H-orbit has size 1, 5, or 25.

An orbit of size 25 is impossible: its 25 distinct curves already contribute at least 25 to the degree, even if each is a line and each multiplicity is one.

Suppose the orbit has size 5. Its stabilizer H_C is then a subgroup of order 5, hence a line in H ≅ F₅². For every n ∈ N,

H_(nC) = n H_C n⁻¹.

SL₂(F₅) acts transitively on the six lines in F₅². Thus the N-orbit of C contains components with each of the six possible H-stabilizers. Each associated H-orbit has five components, and these six H-orbits are disjoint: because H is abelian, the H-stabilizer is constant on any H-orbit. Consequently the N-orbit contains at least 6·5 = 30 distinct components. This again contradicts deg Z ≤ 20.

Therefore every component C is H-stable.

## 2. Every component spans P⁴ and has degree at least five

The linear span of an H-stable integral curve is H₅-stable in V. Irreducibility of the Schrödinger representation forces this nonzero span to be V. Thus C is nondegenerate in P⁴.

The restriction to C of any subgroup of PGL(V) preserving C is faithful. Indeed, if a projective transformation fixes C pointwise, choose a linear representative A. Every point of C is an eigenline of A, so C is contained in the finite union of the projectivized eigenspaces of A. Integrality forces C to lie in one of them; since C spans P(V), that eigenspace is all V. Thus A is scalar. The same faithfulness holds on the normalization, since an automorphism trivial on the normalization is trivial on C.

A nondegenerate integral curve in P⁴ has degree at least 4. For example, the pullback of O_C(1) to its normalization has degree d and at least five independent sections, while a degree-d line bundle on a smooth curve has at most d+1 independent sections.

Degree 4 is impossible here. Castelnuovo's bound gives genus zero for the normalization of a nondegenerate degree-4 curve in P⁴. The faithful H-action would therefore embed C₅ × C₅ in PGL₂(k). Such an embedding cannot exist: the centralizer of an order-5 element in PGL₂(k) is a one-dimensional torus, whose finite subgroups are cyclic. Since H is abelian, it would lie in this centralizer and be cyclic, a contradiction.

Hence every Cᵢ has degree at least 5, so Z has at most four distinct components.

## 3. Each component is N-stable

Since H fixes every component, the permutation action of N on the component set factors through SL₂(F₅). This group is perfect, whereas every subgroup of S₄ is solvable. A perfect solvable group is trivial. Thus the permutation action is trivial, and every component is N-stable.

For completeness, perfection of SL₂(F₅) follows directly from elementary matrices. Put D = diag(2,3), and let u(t) be the upper unipotent elementary matrix. Then

[D,u(t)] = u(3t).

As t varies, these commutators include all upper unipotents. The analogous calculation includes all lower unipotents. Upper and lower elementary matrices generate SL₂(F₅), proving perfection.

## 4. Low-genus obstruction for SL₂(F₅)

**Lemma.** SL₂(F₅) has no faithful action on a smooth projective curve of genus at most 3.

We first record two elementary facts about A₅.

(a) A₅ has no faithful action on a genus-one curve. Choose an origin on that curve E. The quotient of Aut(E) by its translation subgroup is a finite cyclic group (of order 2, 4, or 6 in characteristic zero). Since A₅ is perfect, any A₅-action has image contained in the translations. The translation group is abelian, so the action is trivial.

(b) A₅ has no faithful action on a genus-two curve. Such a curve has its canonical hyperelliptic double cover to P¹, branched at six distinct points. Its hyperelliptic involution is central in its automorphism group, so an A₅-action descends to P¹. The kernel is contained in the order-two deck group and intersects the embedded A₅ trivially. Thus A₅ acts faithfully on P¹ and preserves the six-point branch set. But every orbit of a faithful A₅-action on P¹ has at least 12 points. To see this, a finite subgroup fixing a point of a smooth curve in characteristic zero is cyclic, by its faithful action on the tangent line. The largest cyclic subgroup of A₅ has order 5, so orbit-stabilizer gives orbit size at least 60/5 = 12. This is a contradiction.

Now suppose G = SL₂(F₅) acts faithfully on a smooth curve Y of genus h ≤ 3. Its central involution z is nontrivial. Let B = Y/⟨z⟩, of genus r. The induced action of G/⟨z⟩ ≅ A₅ on B is faithful: the kernel of the action on the invariant function field k(Y)^⟨z⟩ is precisely the degree-two deck group ⟨z⟩.

Riemann–Hurwitz for Y → B gives

2h − 2 = 2(2r − 2) + b,

where b is the number of branch points, equivalently the number of fixed points of z. Thus r ≤ (h+1)/2 ≤ 2. By (a) and (b), r cannot be 1 or 2. Therefore r = 0, and

b = 2h + 2 ∈ {2,4,6,8}.

This is a nonempty A₅-invariant branch set on P¹ with fewer than 12 points, impossible by the orbit bound. This proves the lemma. Notice that unramified cases have not been omitted: they necessarily have r > 0 and were excluded by (a) or (b).

## 5. Castelnuovo and the H-quotient

Choose any component C of Z. It is N-stable, nondegenerate, and of degree d ≤ 20. Let X be its smooth normalization and g its genus. Castelnuovo's bound in P⁴ is

d − 1 = 3m + ε,    0 ≤ ε ≤ 2,

g ≤ 3m(m−1)/2 + mε.

The bound is nondecreasing with d. At d = 20, one has 19 = 3·6 + 1 and hence

g ≤ 3·6·5/2 + 6 = 51.

This is the geometric-genus bound for the birational linear series on the normalization, so no smoothness assumption on the original embedded C is required. A research source stating this form for simple base-point-free linear series is Korchmáros–Torres, *On the genus of a maximal curve*, §2.1, Lemma 2.1 and equation (2.1):
https://www.ime.unicamp.br/sites/default/files/pesquisa/relatorios/rp-2000-20.pdf#page=4

The N-action lifts faithfully to X by §2. Put Y = X/H, and let h be the genus of Y. Riemann–Hurwitz for the degree-25 map X → Y yields

2g − 2 = 25(2h − 2) + R,    R ≥ 0,

so

h ≤ (g+24)/25 ≤ 75/25 = 3.

Normality of H makes Y an N/H-curve. Moreover, the induced N/H-action is faithful: since H acts faithfully on X, the finite extension k(X)/k(X)^H is Galois with group exactly H. An element of N acting trivially on Y is an automorphism over k(X)^H and therefore lies in H. Hence SL₂(F₅) acts faithfully on Y.

This contradicts §4 and completes the theorem.

## Consequence for the stated numerical reduction

Suppose an independently established construction provides an N-invariant effective curve cycle of degree c₃ = 10n, with n an integer and 0 ≤ c₃ ≤ 30. Then n ∈ {0,1,2,3}, and the theorem excludes n = 1 and n = 2. The remaining numerical alternatives are n = 0 and n = 3.

This conclusion is conditional on actual effectivity and cycle invariance of that construction. A numerical class c₃ alone, or invariance only of its Chow class, does not supply those hypotheses. The argument does not exclude degree 30.

## Optional slight strengthening

The same proof actually excludes every positive degree at most 24. In §§1–3, degree <25 still eliminates the size-25 H-orbit, the size-5 H-orbit still produces ≥30 components, and degree ≤24 still gives at most four H-stable components. At d = 24, Castelnuovo gives 23 = 3·7+2 and g ≤ 63+14 = 77, so h ≤ floor((77+24)/25) = 4. The lemma in §4 also holds for h = 4: Riemann–Hurwitz gives integer r ≤ 2, and in the remaining r = 0 case the branch count is 10 <12. Thus the proof yields the stronger lower bound deg Z ≥25 for every nonzero N-invariant effective curve cycle. No assertion about existence in degree 25 is made.
