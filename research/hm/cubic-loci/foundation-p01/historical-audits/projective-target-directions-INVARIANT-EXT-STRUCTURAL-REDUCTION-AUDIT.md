# Historical scope-limited review receipt

This review concerns the original source, possibly a larger scope than the excerpt in this unit. It is not a review of normalized publication bytes.

# Independent audit of the invariant-Ext structural reduction

## Verdict and scope

**Pass for the structural reduction and for the stated conditional implication. Not a proof of D or a certification of its numerical row.** The remaining numerical premise (C) has not been verified in a primary source or proved here. Neither its bibliographic attribution nor the secondary statement quoted in the audited document closes that premise.

This audit uses static document reads and abstract geometry/cohomology only. No actual model, source matrix, rank certificate, polynomial instance, point, jet, or residual was evaluated or executed. Hashing authenticates document bytes only. No external write, message to an external service, merge, upstream change, or local Codex task was performed.

## Hash-bound inputs

Audited document:

- `INVARIANT-EXT-STRUCTURAL-REDUCTION.md`
- SHA-256: `b60abd97c363f51888db83062d9c4b04141e80bc459f02a91ffaacfa7360bb44`

Presentation context inspected, without reopening its literal coefficient audit:

- `hm-presentation-independent/PROOF.md`
- SHA-256: `ed549d3b6d19c1fbef269d390a6313269a369d8616a9343991e43585460915b7`

The companion `INVARIANT-FORMAL-SMOOTHNESS.md` (SHA-256 `945e7982a0d10870d896a0ec4004408ce7beb2d7b16664c7a696c506eb296e46`), particularly its opening and §§1–2, was read solely to check the intended deck-linearization convention. Its historical D assertion is not used as numerical evidence.

## 1. Quotient, pullback, and splitting

The symmetric quotient of four copies of P¹ is Sym⁴(P¹) ≅ P⁴. The quotient map is finite and surjective, with generic degree 24: a divisor with four distinct geometric points has 24 orderings. Ramification along coincident-point loci does not alter the generic degree or invalidate flatness.

The flatness claim is valid. The source is smooth and hence Cohen–Macaulay, the target is regular, both have dimension four, and the finite surjective map has zero-dimensional fibers. The local dimension equality required by miracle flatness holds. Thus its finite direct image B is locally free, with rank 24.

The equality σ*O(1) = O(1,1,1,1) follows, for example, by taking the hyperplane of effective divisors containing a fixed point of P¹. Its inverse image is the sum of the four corresponding coordinate divisors. This establishes the required line bundle equality without a coordinate-model calculation.

For every integer n, Künneth gives intermediate-cohomology vanishing for O(n,n,n,n): all factors have only H⁰ for n ≥ 0, all vanish for n = −1, and all have only H¹ for n ≤ −2. Finiteness and projection formula transfer this to B(n). Horrocks' criterion therefore applies to the vector bundle B on P⁴, with all twists and all intermediate degrees 1, 2, 3 covered.

If a summand O(k) of B had k ≥ 1, then B(−1) would have a section. Its vanishing therefore restricts the summands to O(−a), a ≥ 0. The Hilbert series then determines their multiplicities uniquely. The abstract identity

Σ(n+1)⁴zⁿ = (1 + 11z + 11z² + z³)/(1−z)⁵

gives B ≅ O ⊕ O(−1)¹¹ ⊕ O(−2)¹¹ ⊕ O(−3). The multiplicities sum to 24, consistently with the degree. This is only a vector bundle splitting, and the audited text correctly does not infer a splitting of algebras.

## 2. Deck invariants and the action convention

For locally free E, Extʲ(E,E) = Hʲ(End E). With the induced deck action, cancellation of the line factor gives a G-equivariant identification

End(N ⊗ q*σ*H) ≅ q*σ*End H.

The conjugation action on End N ≅ O is trivial; changing a linearization of N by a scalar character does not change this assertion. The quotient equality (q_*O_X)^G = O_Y, projection formula, finite pushforward, and the characteristic-zero Reynolds projector then give

Hʲ(X,End E)^G ≅ Hʲ(Y,σ*End H).

Exactness of the Reynolds projector also justifies commuting invariants with cohomology; no freeness of the branched deck action is required.

Applying the splitting of B gives exactly the four-term additive decomposition and multiplicities stated in §2 of the audited document. It does not identify Yoneda products, preserve multiplication through the noncanonical splitting, or determine any operation on the historical complex.

**Minor clarification recommended:** explicitly say in that section that the invariants use the induced deck action on End E, or fix the G-linearization of N and E as the companion formal-smoothness document already does. Without an action convention the superscript G is not intrinsically specified by an ordinary bundle alone. With the convention in the companion document, there is no mathematical gap here.

## 3. Stability and duality prerequisites

For the normalized rank-two HM bundle, the monad implies H⁰(H) = 0: H⁰(Ω²(2)) = 0 and H¹(O(−1)) = 0 give the required vanishing through its two short exact sequences. A destabilizing saturated rank-one subsheaf has double dual O(d) with d ≥ 0. Its inclusion extends across codimension at least two to a nonzero map O(d) → H because H is locally free. Multiplication by a nonzero section of O(d) would then yield a nonzero section of H, a contradiction. This fills in the standard extension step implicit in the audited stability argument.

Stability in characteristic zero gives simplicity and, by slope comparison, Hom(H,H(t)) = 0 for t < 0. Therefore h⁰(End H) = 1 and negative-twist h⁰ vanishes. The trace pairing on endomorphisms is perfect, so End H is self-dual. Serre duality on P⁴ yields exactly the displayed twist −t−5.

For t = 0, −1, −2, −3, the dual twists are −5, −4, −3, −2. Consequently h⁴ vanishes unconditionally from stability, and h³ vanishes if the corresponding four h¹ values in (C) vanish. There is no sign or dimension shift error.

## 4. Riemann–Roch and the conditional numbers

Writing the formal Chern roots as x₁,x₂ gives (x₁−x₂)² = c₁²−4c₂ = −15h². Hence

ch(End H) = 2 + exp(x₁−x₂) + exp(x₂−x₁) = 4−15h²+(75/4)h⁴.

Using td₁(P⁴) = 5h/2 and td₂(P⁴) = 35h²/12, the correction to 4χ(O(t)) is

−15(t²/2 + 5t/2 + 35/12) + 75/4.

This proves the audited formula

χ(End H(t)) = 4 binom(t+4,4) − (15/2)t² − (75/2)t −25.

The binomial is its polynomial extension for arbitrary integer t. The four listed Euler characteristics −21, 5, 20, 20 and the resulting conditional rows (1,24,2,0,0), (0,5,10,0,0), (0,0,20,0,0), (0,0,20,0,0) are all consistent. Their weighted sum is (1,79,352,0,0). These are formal consequences of the expressly unverified premise (C), not independently established dimensions.

## 5. Exact remaining gap and dependency boundary

There is one substantive open dependency: the classical negative-twist h¹ information asserted in (C). No primary verification of that theorem was attempted or achieved in this audit. In particular the cited secondary paper is not being certified as a source of the entire required table.

The required input can be narrowed according to the goal:

- For D alone, meaning the invariant Ext¹ dimension 79, it suffices to establish h¹(End H) = 24, h¹(End H(−1)) = 5, and h¹(End H(−2)) = h¹(End H(−3)) = 0. The twists −4 and −5 are not needed for that degree-one conclusion.
- For all four complete cohomology rows and the invariant row through degree four, the additional h¹ vanishings at −4 and −5 suffice. Vanishing at every t ≤ −2 is stronger than needed.

The independent presentation proof P identifies the literal presentation with the classical bundle and closes a different dependency. The earlier A result is likewise separate. Neither P nor A supplies the missing classical h¹ values. Thus the correct final state is: structural reduction proved; P available independently; numerical completion of D remains conditional on the stated classical input.
