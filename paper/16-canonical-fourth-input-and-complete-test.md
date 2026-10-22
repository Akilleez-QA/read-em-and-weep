# 16. The canonical fourth input and a complete four-channel test

## 16.1 A nonzero raw cubic with zero final third quotient

The [canonical raw-cubic theorem][RAW] identifies the actual fixed-probe tensor before the second-symbol quotient:

    T(a,h)=Ψ(a,h,[aζₐ]) ∈ P4,
    T=β₂ L_can,       L_can:D5 O(−3) → A O(−2).

This factorization is unique as a sheaf map, including across the six exceptional axes. The factor is **nonzero**, although the final third Bockstein is zero. In a uniform C5 eigenframe, the full cochain for a=t², h=Y⁴ pairs nontrivially with the actual raw P4 dual line. The resulting residue is −4Akλ/(B²c²ν), with every factor nonzero; A,B in that formula are scalar tensor-line symbols, not the representation and adjoint bundle. The residue uses the whole cochain and the actual raw quotient, not the annihilator of the second image. It is therefore compatible with Chapter 15's zero final quotient.

Intrinsically, identify D5 with the trace-free self-adjoint endomorphisms S_h of the invariant three-space A. Then

    L_can(a,h)=γ S_h(a),       γ≠0.

For every a≠0 this is onto A. Indeed a covector annihilating all S_h(a) would give sym(a⊗ℓ) proportional to the rank-three metric; its rank is at most two, so the proportionality and then ℓ vanish. Consequently im Tₐ=im β₂,ₐ in every direction: raw rank three away from the axes and rank two at each axis.

This is the canonical cyclic/Atiyah probe normalization. An arbitrary Schur reduction has a transported correction L, whose coefficient need not equal that of L_can. No invariant numerical scalar is assigned. In a compatible reduction the fourth representative remains B₄|D5−B₃|A L_can; neither its correction composite nor its final quotient is proved nonzero.

## 16.2 The correction kernel is a secant bundle

Fix the actual equivariant identification J:D5→Sym⁴W. The [kernel theorem][KER] gives L_can(a,h)=γ(a,Jh)₂. Its rank-two kernel bundle 𝒦 on X=P(A) fits into

    0 → 𝒦 → D5 O_X → A O_X(1) → 0.

For a=ℓm with distinct apolar roots, its fiber is J⁻¹ span(ℓ⁴,m⁴); at a=ℓ² it is J⁻¹(ℓ³W). It is the dual of the tautological degree-four evaluation bundle on the universal length-two divisor. Thus c₁(𝒦)=−3H, c₂(𝒦)=6H², and on the square conic's parametrization ν, ν*𝒦=W O(−3).

With F=I_Σ(10), the exact equivariant restriction sequence has dimensions

    0 → Hom_G(A,H⁰(I_Σ(9))) → Hom_G(D5,H⁰(F))
      → Hom_G(𝒦,F) → 0,
    dimensions: 1 → 4 → 3.

The kernel consists precisely of families factoring through L_can. Restricting the compatible fourth representative to 𝒦 removes its explicit third-source correction, but only tests three channels. Even zero on all of 𝒦 would leave the one-dimensional factoring possibility; no actual restricted value is evaluated.

## 16.3 What the lower vector shadow actually retains

The [actual lower comparison][LOW] distinguishes the full lower class from its effective shadow. Set C=H¹(B_Q(2))₊, with Serre-involution decomposition C=C₋⊕C₊ of dimensions 21+9. The cyclic image J₀=D5·ξ_Q is the actual five-dimensional D5 summand of C₊=P4⊕D5. Its injectivity follows from the commuting Serre tangent and polynomial-restriction diagrams, not merely from its permitted character.

The ambient divided class v_h restricts canonically to C/J₀. The midpoint operator class lies in C₋; its affine variation to the actual endpoint lies in C₊, modulo J₀. The vector cochain R/ν gives their common image in H¹(P4 O_L(−4)), the effective twelve-space. The exact comparison is

    0 → (P4⊕D5)₋ ⊕ (P4)₊ → C/J₀ → H¹(P4 O_L(−4)) → 0,
    dimensions: 13 → 25 → 12.

The missing negative nine-space is polynomial. The missing positive P4 **contains the actual normal variation modulo J₀**; this does not prove that variation is nonzero or fills P4. Neither missing component is evaluated. Thus R is not a representative of the full C or C/J₀ class and cannot simply be fed into the next ambient q₀ division.

Keeping the entire homogeneous normal matrix does not fix this loss. The [full-matrix comparison][MAT] identifies its coefficient bundle with J₋=P4 O_L(−4) before taking cohomology. The trace map is an isomorphism there, and Gram subtraction loses no additional information. The two different quotient sequences are

    0 → H⁰(E₋) [12] → H⁰(M₋) [24] → H¹(J₋) [12] → 0,
    0 → A [3] → H⁰(M₋) [24] → C₋ [21] → 0.

Their difference is H⁰(E₋)/A=Sym⁸W′=P4⊕D5. Every nonzero such coefficient lift has a nonzero conic octic restriction, so it is not a genuine global G(2) coboundary. The absolute polynomial component or a proof of its irrelevance is needed for a route using the full lower lift; a normalized dual route may bypass it. No unpublished recovery of this component is included.

## 16.4 The corrected fourth source cannot be trace-free

In the convention q₀−ta, put

    x(a,h)=[v_h(a)−b(a,h)ζₐ] ∈ C/J₀,
    q₀v_h=ahζₐ,       [av_h]=β₂,ₐ(b(a,h)).

Here b is the canonical nonzero linear correction. The [trace theorem][TR] constructs the symmetric map

    𝒯:Sym²₀A → C/J₀,       𝒯(a⊙c)=[aζ_c],

where the expression means the symmetric product followed by its trace-free quotient. Commutativity makes it symmetric modulo J₀, the invariant ambient component vanishes, and the nonzero second symbol proves 𝒯 is nonzero and therefore injective on D5.

The uncorrected [v_h] has zero invariant parameter trace. With b(a,h)=γS_h(a), contraction gives instead

    Tr_A x(−,h)=−γ𝒯(S_h) ≠ 0 for h≠0.

This is a forced injective D5 family in the actual next input. The earlier trace-free normal form applies to the preceding uncorrected family, not this corrected source. It neither evaluates the next division q₀w_h=a(v_h−bζₐ) nor excludes cancellation in the fourth quotient.

## 16.5 Square detection and its required source correction

The two fourth square channels lie in Hom_G(D5,Sym²⁰W). If E₁₂ is the C5 orbit on the square parameter line, the [detection filtration][SQ] is

    0 → Δ₁₂ Sym⁸W → Sym²⁰W → H⁰(O_(E₁₂)(20)) → 0.

A C5-square fiber detects exactly one of the two channels. Its kernel is the D5 copy in Δ₁₂ Sym⁸W. Thus one zero fiber on this orbit alone cannot kill the full square restriction. If its detected coefficient is zero, a further full-fiber zero away from E₁₂ kills the remaining square channel, since its degree-eight factor is basepoint-free.

At a=t² the only fourth-detectable input character is h=X²Y², not the cubic test's X⁴. The [actual correction theorem][IN] proves L_can(t²,X²Y²) is a nonzero multiple of t². In the displayed eigenframes its ratio to L_can(t²,Y⁴)=ℓst is B/(6A), with ℓ≠0. The correction term B₃(t²)|A(t²) has exactly the target character of the fourth square quotient, so weights do not permit its deletion. This proves a nonzero required source correction, not a nonzero correction composite or fourth value.

## 16.6 One ideal-sheaf jet and one C5-square fiber are a complete test

Mr. Slop's [PR658][MS] proves that full square restriction plus the six actual axis fibers has a one-dimensional kernel. After dividing by the discriminant, this is the D5 in the nine-dimensional triple-axis octic series P4⊕D5. The cubic septic argument therefore cannot be repeated at fourth order. PR658 also proves that full square restriction plus one first ideal-sheaf jet detects the entire fourth D5 family.

The [sharpened test][JET] replaces that full square restriction with a **single C5-square fiber**. Let p be any semisimple axis, q either C5-fixed square associated with any axis, N=Stab(p), and K=Stab(q). For the four-dimensional space 𝒬₄=Hom_G(D5,H⁰(I_Σ(10))),

    (J_p,E_q): 𝒬₄ → Hom_N(D5,(I_Σ/m_p²I_Σ)(10)|p)
                       ⊕ Hom_K(D5,O(10)|q)

is an isomorphism, with target dimensions **3+1**. The notation |p denotes the supported stalk quotient, not a further tensor with the residue field. This tests the entire D5 family, not one source vector. It is an ideal-sheaf jet: ordinary values and ordinary first derivatives of the defining decics are not the test.

The proof uses m_p²I_Σ,p=m_p⁴ and the quadruple-axis decic series. If c_i is the normalized conic through the other five axes, its six basis sections are F_i=∏_(j≠i)c_j. Residual sequences give dimension six and representation 1⊕D5, so ker J_p is one-dimensional. At either C5 square attached to axis i, F_i is nonzero and every other F_j is zero. Evaluation therefore detects the sum-zero D5 subspace and is nonzero on ker J_p. Finally the jet module is ρ₁⊕2ρ₂ under the dihedral normalizer, while D5|N=1⊕ρ₁⊕ρ₂, giving dimension three; the C5 target has dimension one.

There is no conflict with Section 16.5: a C5 fiber alone detects only one of two square coefficients, whereas the three-dimensional jet supplies the complementary information in this combined four-dimensional test. Neither actual datum has been evaluated. The fourth value on the additional specialized A-kernel line is outside this D5 test.

## 16.7 A normalized dual certificate away from the axes

The [dual certificate][DUAL] offers a separate exact interface on the rank-three second-symbol open set. Write q:V→U for the actual 41→37 ambient map of rank 33, and λₐ for its degree-six cofactor covector annihilating the second image. First define ηₐ(qv)=λₐ(av). Extend ηₐ to φₐ on U, imposing

    φₐ(a b ζₐ)=0 for every b∈A.

Those three vectors are independent modulo qV. The extension is unique modulo λₐ. The second dual division is ρₐ(qv)=φₐ(av), and the fourth scalar is exactly

    λₐ(aw_h)=ρₐ(ahζₐ).

The normalization encodes the nonzero third correction instead of discarding it. Changing φₐ by a multiple of λₐ changes this expression by the already-zero third value. Its degree-ten polynomial extension exists, but at Σ the cofactor vanishes: ordinary evaluation there does not test the ideal-sheaf fiber or the extra A-kernel line. The actual functional value remains unevaluated.

## 16.8 Unchanged theorem and evidence boundary

All four actual fourth coefficients remain unevaluated at the 22 October 2026, 04:51 UTC cutoff. The generic total section count stays four or five; the last generic finite Smith exponent stays 4≤e≤31, or the cokernel is permanent. Nonzero raw cubic, required correction, forced parameter trace and complete detection criteria are distinct from a nonzero fourth Bockstein. Original source recovery, lifting and Weil-class algebraicity remain open.

The separate [extremal Gauss result][GAUSS] restricts a hypothetical (3,1) rank-three plateau: its dual cubic image has rank one or two, never three; rank one forces O(9) or O(11). It does not exclude that entire profile. Generic SF≥3 and positive-square rank≥27 remain unchanged.

The cited proofs give actual-map comparisons and geometric arguments. Their companion verifiers check universal identities, characters, degrees and finite arithmetic, not selected actual coefficient matrices or proof-assistant certificates.

The subsequent [absolute-source chapter](17-absolute-lower-source-and-secondary-endpoint.md) proves nonzero corrected lower source on the reduced cubic, identifies the remaining secondary endpoint P4, and records the complementary secant-plus-square test. It does not evaluate the fourth gate.

## Pinned source references

[RAW]: https://github.com/Akilleez-QA/read-em-and-weep/blob/4e16e69c776bd85506341b5bb785f0d8a396bd3e/research/hm/order-four-quadratic-load/ACTUAL-CANONICAL-RAW-CUBIC-HAS-A-NONZERO-LINEAR-LIFTING-CORRECTION.md
[KER]: https://github.com/Akilleez-QA/read-em-and-weep/blob/4e16e69c776bd85506341b5bb785f0d8a396bd3e/research/hm/order-four-quadratic-load/CANONICAL-LIFTING-KERNEL-IS-A-SECANT-BUNDLE-AND-LEAVES-THREE-QUARTIC-CHANNELS.md
[SQ]: https://github.com/Akilleez-QA/read-em-and-weep/blob/4e16e69c776bd85506341b5bb785f0d8a396bd3e/research/hm/order-four-quadratic-load/FOURTH-SQUARE-CHANNELS-HAVE-A-C5-DETECTION-FILTRATION.md
[IN]: https://github.com/Akilleez-QA/read-em-and-weep/blob/4e16e69c776bd85506341b5bb785f0d8a396bd3e/research/hm/order-four-quadratic-load/ACTUAL-FOURTH-SQUARE-INPUT-REQUIRES-A-NONZERO-THIRD-SOURCE-CORRECTION.md
[DUAL]: https://github.com/Akilleez-QA/read-em-and-weep/blob/4e16e69c776bd85506341b5bb785f0d8a396bd3e/research/hm/order-four-quadratic-load/FOURTH-BOCKSTEIN-DUAL-CERTIFICATE-WITH-NORMALIZED-SECOND-IMAGE.md
[LOW]: https://github.com/Akilleez-QA/read-em-and-weep/blob/c85c756d333281eccefdb77c4899db4f923d768e/research/hm/order-four-quadratic-load/ACTUAL-VECTOR-SHADOW-LOSES-THIRTEEN-LOWER-LIFT-DIRECTIONS.md
[TR]: https://github.com/Akilleez-QA/read-em-and-weep/blob/c85c756d333281eccefdb77c4899db4f923d768e/research/hm/order-four-quadratic-load/ACTUAL-FOURTH-CORRECTED-SOURCE-HAS-A-NONZERO-PARAMETER-TRACE.md
[MAT]: https://github.com/Akilleez-QA/read-em-and-weep/blob/c85c756d333281eccefdb77c4899db4f923d768e/research/hm/order-four-quadratic-load/FULL-HOMOGENEOUS-NORMAL-MATRIX-STILL-LOSES-THE-POLYNOMIAL-NINE-SPACE.md
[GAUSS]: https://github.com/Akilleez-QA/read-em-and-weep/blob/c85c756d333281eccefdb77c4899db4f923d768e/research/hm/order-four-quadratic-load/EXTREMAL-31-DUAL-CUBIC-IMAGE-HAS-RANK-AT-MOST-TWO.md
[JET]: https://github.com/Akilleez-QA/read-em-and-weep/blob/c85c756d333281eccefdb77c4899db4f923d768e/research/hm/order-four-quadratic-load/FOURTH-GATE-ONE-AXIS-JET-AND-ONE-SQUARE-FIBER.md
[MS]: https://github.com/Akilleez-QA/read-em-and-weep/blob/95004606fb8b2ec51ecd97e2fde0d6d0ff328407/research/hm/fourth-gate-geometric-constraints/FOURTH-GATE-SIX-AXIS-INVISIBLE-CHANNEL.md
