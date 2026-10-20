# Addendum: exclusion of degree 30

This addendum leaves PROOF.md unchanged and uses precisely its hypotheses: algebraically closed characteristic-zero field, the projective Schrödinger action on P⁴, H ≅ F₅² normal in N, and N/H ≅ SL₂(F₅) acting on H in the faithful standard representation. Invariance always means invariance of an actual effective curve cycle, not just of its class.

**Theorem.** No N-invariant effective curve cycle has degree 30.

Together with PROOF.md, this excludes degrees 10, 20, and 30. Thus if an independently established construction gives an invariant effective cycle of degree c₃ = 10n with integer n and 0 ≤ c₃ ≤ 30, necessarily n = 0 and the cycle is zero. No conclusion about any remaining zero-dimensional singularities follows from this cycle argument alone.

## A. SL₂(F₅) has no faithful curve action in genus at most six

### A.1. A₅ has no faithful action in genus three

The genus-one and genus-two exclusions are proved in §4 of PROOF.md. Suppose A₅ acts faithfully on a smooth curve of genus three. The quotient map has degree 60. In characteristic zero, point stabilizers are cyclic, so its ramification indices are among 2, 3, 5. If the quotient has genus r, Riemann–Hurwitz says

1/15 = 2r − 2 + a/2 + 2b/3 + 4c/5,

where a, b, c are the numbers of branch points of indices 2, 3, 5.

If r ≥ 2, the right side is at least 2. If r = 1, the positive right side is at least 1/2. Both are impossible. For r = 0, multiplication by 30 gives

15a + 20b + 24c = 62.

Reduction modulo 5 forces c ≡ 3 mod 5, hence c ≥ 3, but then 24c ≥ 72 > 62. This is impossible as well.

Thus A₅ has no faithful curve action in any of genera 1, 2, 3.

### A.2. Central quotient reduces to one hyperelliptic possibility

Suppose G = SL₂(F₅) acts faithfully on a smooth curve Y of genus h ≤ 6. Let z = −I and B = Y/⟨z⟩, with genus r. As in PROOF.md, the induced A₅-action on B is faithful, and

2h − 2 = 2(2r − 2) + b,

where b is the number of branch points. In particular r ≤ floor((h+1)/2) ≤ 3. Section A.1 and the previous proof force r = 0. Consequently Y → B is hyperelliptic and its branch set has

b = 2h + 2 ≤ 14

points. This set is nonempty and A₅-invariant. Every point stabilizer in a faithful A₅-action on P¹ is cyclic of order 1, 2, 3, or 5. Thus every orbit has size 60, 30, 20, or 12. The only nonempty invariant set of at most 14 points has exactly 12 points and is one orbit. Hence h = 5 and each branch point has stabilizer of order 5.

### A.3. The twelve-point branch case cannot have the required lift

Choose an involution a in A₅. Its two fixed points on P¹ are outside the branch set, because branch-point stabilizers have odd order 5. Choose a coordinate x with these fixed points at 0 and ∞. Then a acts as x ↦ −x.

Because ∞ is not branched, the genus-five cover admits an equation

y² = f(x),

where f is a squarefree degree-12 polynomial. Its roots form six pairs {α,−α}, with α ≠ 0; after rescaling f, it is an even polynomial. Therefore a has the two lifts

(x,y) ↦ (−x,y),    (x,y) ↦ (−x,−y).

Both lifts have order 2. These are all lifts, because any two lifts of the same base automorphism differ by the hyperelliptic deck involution.

In contrast, every preimage of a in SL₂(F₅) has order 4. Indeed, −I is the unique element of order 2 in SL₂(F₅): an order-two determinant-one matrix in characteristic 5 is diagonalizable with eigenvalues ±1, and determinant one leaves only I or −I. A preimage of a has square in {I,−I}; it is not central and cannot have order 2, so its square is −I. A faithful action would map this element to an automorphism of order 4 lifting a, which we have just shown impossible.

This proves the genus-at-most-six obstruction. It uses no choice of a complex two-dimensional representation of SL₂(F₅) and no binary invariant-form classification.

## B. No N-stable integral curve of degree at most 30

An H-stable integral curve spans P⁴ by irreducibility of V, and the induced N-action on its normalization is faithful whenever the curve is N-stable; see §2 of PROOF.md.

For a nondegenerate integral curve of degree d ≤ 30, Castelnuovo's bound yields normalization genus g ≤ 126: at d = 30,

29 = 3·9 + 2,    π(30,4) = 3·9·8/2 + 9·2 = 126.

For the quotient by H, Riemann–Hurwitz gives genus h satisfying

h ≤ (g+24)/25 ≤ 150/25 = 6.

The induced N/H = SL₂(F₅)-action on this quotient is faithful by the function-field deck-kernel argument in §5 of PROOF.md. Section A gives a contradiction.

## C. A line with H-orbit of size five has N-orbit of size at least sixty

Let L ⊂ P⁴ be a line whose H-stabilizer A has order 5. In the Schrödinger representation, any lift of a generator of A has five distinct one-dimensional eigenspaces. Indeed, a complementary Heisenberg element cyclically permutes these eigenspaces by the nondegenerate commutator pairing. A projective line stable under A is therefore the span of a pair of these eigenlines.

Label the five eigenlines by F₅. The complementary part H/A acts by all translations of the labels. The subgroup of SL₂(F₅) stabilizing the axis A induces every nonzero scalar on A. Its lifts to N consequently act on the eigenline labels by affine transformations whose linear parts range over all F₅×. Scalar factors in conjugating a chosen lift of A merely change the additive part of this affine permutation.

Thus the stabilizer in N of the axis A acts transitively on all ten unordered pairs of distinct eigenline labels. The N-orbit of L contains all ten resulting coordinate lines. SL₂(F₅) is transitive on the six possible axes A. The ten lines associated to distinct axes are disjoint as sets of components: a line stable under two distinct axes would be H-stable, contradicting irreducibility of V. Hence the full N-orbit contains at least 6·10 = 60 lines.

This is a statement about invariant linear subspaces of the abstract Schrödinger representation; no numerical instance or problem-specific matrix is used.

## D. Small N-orbits of H-stable curves cannot occur

Every H-stable integral curve has degree at least five by PROOF.md.

Suppose C is H-stable and has degree at most six. Castelnuovo gives normalization genus g ≤ 2. In the faithful H-action on its normalization, point stabilizers are cyclic and hence have order 1 or 5. Write q for the genus of the quotient and t for the number of branch points. Riemann–Hurwitz becomes

2g − 2 = 25(2q − 2) + 20t.

Therefore 2g − 2 is divisible by 5. Among g = 0,1,2, this forces g = 1.

Let E denote this elliptic normalization, and let N_C be the stabilizer of C in N. After choosing an origin, Aut(E) modulo translations is cyclic of order at most six. H acts by translations: its image in that cyclic quotient is trivial because H is a 5-group. (In fact H is the full translation subgroup E[5].)

Conjugation on H by any automorphism of E depends only on its class modulo translations. Hence the image of N_C in Aut(H) has order at most six. But the prescribed conjugation action N/H → Aut(H) is faithful, so the restriction N_C/H → Aut(H) is faithful too. Thus

|N_C/H| ≤ 6,    [N:N_C] = 120/|N_C/H| ≥ 20.

In particular, an H-stable curve of degree at most six cannot have an N-orbit of size five or six (indeed, cannot have an N-orbit of size below twenty). This treats quintics and possible sextics uniformly, without requiring a line-bundle degree-divisibility argument.

## E. All degree-thirty component configurations

Let Z be an N-invariant effective curve cycle of degree 30. Multiplicities are positive integers and constant along N-orbits.

### E.1. An H-orbit of size 25

If a component C has H-orbit of size 25, its N-orbit has size divisible by 25. The degree bound forces this N-orbit to have exactly 25 components, all lines, each with multiplicity one. Their orbit sum is an N-invariant effective cycle of degree 25. Subtracting it from Z leaves an N-invariant effective cycle of degree 5. This contradicts PROOF.md.

### E.2. An H-orbit of size 5

If C has H-orbit of size five, the six-axis argument of §1 of PROOF.md gives at least 30 distinct components in its N-orbit. The total degree 30 therefore forces exactly 30 lines, all with multiplicity one. But Section C proves that the orbit of such a line has at least 60 components, a contradiction.

### E.3. Every component is H-stable

The remaining possibility is that all components are H-stable. Each has degree at least five, so there are at most six distinct components. The N-action on components factors through the perfect group SL₂(F₅). Any orbit of size at most four is a singleton, since its permutation image is a perfect subgroup of a solvable symmetric group. A singleton component is N-stable and is excluded by Section B.

Thus any component orbit must have size five or six. If its size is m, and its component degree is d and multiplicity is μ, then

m μ d ≤ 30.

Since m ≥ 5 and d ≥ 5, one has μ = 1 and d ≤ 6. Section D excludes an orbit of either size for such a component. This is the final contradiction.

The theorem follows. All possibilities for reducible support and positive cycle multiplicities have been covered. The degree-25 orbit possibility was not assumed impossible; only its unavoidable degree-five remainder in a degree-thirty cycle was excluded.
