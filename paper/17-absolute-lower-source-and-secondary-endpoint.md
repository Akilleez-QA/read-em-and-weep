# 17. Absolute lower sources and the remaining secondary endpoint

> **Current-status note (22 October 2026, 07:09 UTC):** The historical Gauss frontier below is superseded by [Chapter 21](21-gauss-closure-and-second-normal-residue.md): the entire (3,1) profile is excluded. Its five remaining possible profiles are not realizations, and SF ≥ 3 / square rank ≥ 27 remain unchanged. Chapter 21 also records the exact midpoint residue, associated-graded tangent acyclicity and the still-open affine R2/fourth comparison. Earlier proof bodies are preserved.

**Historical frontier.** This chapter retains its earlier source scope. [Chapter 19](19-actual-endpoint-values-and-last-gauss-quotient.md) supersedes its open-endpoint and Gauss status with actual endpoint values, the complete (6,2) exclusion and eleven remaining necessary K splittings in (8,2). The fourth obstruction remains open.

The corrected C5-square lower source is now proved nonzero, already on the reduced genus-four cubic. This is not a nonzero fourth Bockstein. The absolute midpoint and Atiyah representatives recover information lost in the effective vector quotient; the endpoint variation remains an unevaluated secondary P4 residue. The distinction between these three statements is essential throughout this chapter.

## 17.1 The absolute midpoint and Atiyah sections

Use the fixed canonical normalization, with a=t² and h=X²Y² for the fourth-detectable C5-square input. The [absolute midpoint calculation][MID] constructs the full midpoint class in

    H⁰(M₈(−2))/A = Cminus,

rather than only its effective twelve-dimensional image. In the symbolic divisor frame, its double-cubic coordinate is r_mid/(νg²) in O_(2D)(−2,10). Here ν is the physical equation factor: the calculation divides by the cover equation, so this factor cannot be suppressed. The numerator is given explicitly in the cited source. Both complete regular charts, their finite quintic-source changes modulo f², the full tangent equation and the unique Hessian gluing primitive establish that it is the actual global class. Local normal conjugation changes the error by a commutator and does not change this quotient. No splitting of the lost polynomial nine-space is chosen.

The separate [absolute Atiyah comparison][ATI] identifies the full t(a)=aζₐ class by

    r_t/g² on 2D,
    r_t=k a[Dₐ(fg)−2a_z fg]=2k a ∂z(a f g),
    Dₐ=2a∂z+(a_z/2)Euler_positive.

The determinant-line term −2a_z is required. Unlike r_mid, this Atiyah derivative has no normal-division factor ν. Its finite covariance under g↦g+pf is an identity modulo f², not merely agreement on the reduced curve. At the detecting square, the already-fixed canonical correction is b=γa with γ≠0. Thus the entire corrected midpoint projection is

    (r_mid/ν−γr_t)/g².

This recovers the absolute negative-involution class, including every polynomial-nine direction. It does not yet calculate the endpoint Cplus/J=P4 component or the next ambient division.

## 17.2 The reduced cubic canonically realizes the lower negative class

The [reduced-cubic theorem][RED] starts with the actual double-cubic sequence and nilpotent splitting

    0 → N₈ → M₈ → π_*O_D(−2,12) → 0,
    N₈=O_L(4) ⊕ W′O_L(1).

After twisting by O_L(−2), the W′O_L(−1) cohomology vanishes and H¹(O_L(2))=0. The scalar class of N is precisely the remaining A=H⁰(O_L(2)). Consequently

    0 → A → H⁰(M₈(−2)) → H⁰(D,O_D(−2,10)) → 0,
    Cminus ≅ H⁰(D,O_D(−2,10)).

This is canonical and equivariant. The genus is four and the line has degree 24, so h⁰=21 and h¹=0, agreeing with Cminus=V⊕2P4⊕2D5. An absolute class vanishes in Cminus exactly when its restriction to D vanishes; the three scalar directions exhaust the global nilpotent layer in this twist.

On D the Atiyah section becomes 2k a²f_z/g. The relative derivative f_z/g lies in O_D(−2,6), so the line after multiplication by a² is O_D(−2,10), as required. This realization eliminates an ambiguity in representing the lower class. It does not remove the later division problem.

## 17.3 The corrected square source is nonzero

In the uniform symbolic frame of [the proof][RED],

    f=A X²Y+B Y³z+Ac X³z²−Bc XY²z³,
    g=−λ(BXY⁴z⁻³+A X³Y²z⁻⁴)/(2Ac),   a=z².

Here A,B,c,λ,k are nonzero scalar parameters, not assigned actual coefficient values. Put θ=νγ and F=λkY⁶/(Ac⁴z⁷). Polynomial division by f in X gives

    rem(r_mid,f)=−FP/6,       rem(r_t,f)=2FQ.

The X²z⁰ coefficients in P,Q are A²,−A²; the X²z¹⁰ coefficients are 2B²c⁴,B²c⁴. Therefore P+12θQ could vanish only if simultaneously θ=1/12 and θ=−1/6. This contradiction holds for every constant θ. The cited proof gives the full remainders and verifies them symbolically.

Since D is integral, this proves the corrected Cminus class nonzero. Its complementary endpoint P4 cannot cancel a nonzero class in a distinct direct summand. Hence the actual corrected lower source [v_h−bζₐ] in C/J is nonzero. The result is uniform over the C5 orbit, not a selected-instance computation.

Actual third vanishing nevertheless says that multiplication by a kills this source in P4 before the next division. One must still solve the actual ambient equation

    q₀w_h=a(v_h−bζₐ)

and then compute a w_h modulo the second image. Nonzero lower source therefore does not imply nonzero fourth value.

## 17.4 Trace null-homotopy leaves a secondary endpoint P4

The [normal-variation theorem][TRACE] uses the actual trace sequence

    0 → G(−4) → B_Q(−2) → I_Z² → 0,
    q(E)=tr(NE).

Its invariant square shadow has two components, not one:

    q(η)=δ(αe_v+βn₈),       α≠0.

The component-idempotent coefficient α is fixed by the actual Serre marking. At the source stage recorded here β was not evaluated; [Chapter 18.1](18-actual-cone-lift-and-nilpotent-trace.md#181-the-actual-nilpotent-trace-coefficient-is-nonzero) now proves β≠0 by actual restriction to 2C. The full block torus does not provide a global marking that permits setting β=0.

For the actual first-normal variation b₁ and the corrected scalar inverse u, the operator diagram is

    L(E)=HDE+[Aconn,E]+HρE,
    T(f)=HDf+uf,       qL=Tq,       Λ=Hρ−u.

The normal-equation term Hρ must be retained. The ordinary square of the actual degree-three/degree-five regular pair has no positive-cover layer of degree at least twelve. Since T raises degree by four, T(n₈)=0. Also T(e_v)=u e_v; the global u vanishes on the double conic, so u e_v=u|_(2Z). The actual global section αu is therefore a null-homotopy:

    q(b₁)=δ(αu|_(2Z))=0.

This proves existence of a unique lift to the injective H¹(G) image Cplus=P4⊕D5. It does not calculate that lift. Concretely, for compatible scalar lifts t_i of αe_v+βn₈, choose adjoint lifts K_i with

    q(K_i)=T(t_i)−αu,
    L(η)_ij−(δK)_ij=τ(γ_ij).

The Serre residue of γ, after removing global quadratic components, lies in V⊗A=P4⊕D5. Quotienting by the actual cyclic image J=Q(D5) leaves exactly

    [r_var] ∈ (V⊗A)/Q(D5)=P4.

This endpoint value is unevaluated. In particular, killing βn₈ in the scalar quotient does not license deleting it from the compatible adjoint lifts or this secondary construction. The trace map has a nine-dimensional kernel; its zero value alone cannot select the remaining class.

## 17.5 Secant restriction and parameter trace reconstruct the lower family

The [family reconstruction theorem][FAMILY] concerns Cbar=C/J=Cminus⊕P4 of dimension 25, with the canonical secant sequence

    0 → K → D5 O_X → A O_X(1) → 0,       X=P(A).

Restriction and parameter trace give an isomorphism

    Hom_G(D5,H⁰(Cbar O_X(2)))
      → Hom_G(K,Cbar O_X(2)) ⊕ Hom_G(D5,Cbar),
    dimensions 13 → 11+2.

The vanishing of H¹(X,O_X(1)) gives surjective restriction. Its kernel is Hom_G(A⊗A,Cbar), of dimension two, because A⊗A=1⊕A⊕D5. Each kernel family is R(a,L_can(a,h)). If L_can(a,h)=γS_h a, contraction of the two parameter slots sends this family to γT(S_h), an isomorphism on that two-dimensional kernel. This is parameter trace, not adjoint trace in Section 17.4.

For the endpoint summand alone, restriction is already an isomorphism of dimensions 2→2: there is no P4 in A⊗A, and no map D5→P4. Thus secant restriction removes the canonical correction but does not remove either endpoint channel. The corrected and uncorrected families have the same K-restriction but different traces. These are reconstruction statements for whole families, not evaluations of the actual family.

## 17.6 Two distinct complete tests for the fourth family

[Chapter 16.6](16-canonical-fourth-input-and-complete-test.md#166-one-ideal-sheaf-jet-and-one-c5-square-fiber-are-a-complete-test) gives the axis ideal-sheaf-jet plus C5-square test, with dimensions 3+1. Mr. Slop's [PR659][SECANT] supplies a different complete test: the three-dimensional secant-restricted fourth family plus the one character-allowed scalar at a C5 square, again 3+1.

The secant restriction kernel T is a factoring line M∘L_can. Its coefficient series is an A in degree eighteen on the square conic. It has no common zero: an invariant common divisor of degree at most eighteen would have to be the twelve-point orbit, whose removal would force an impossible A in Sym⁶W=V⊕P4. Thus every nonzero member of T is a nonzero full D5-family fiber at every square.

The different line N left by square restriction plus all six axis ideal-sheaf fibers vanishes on the entire square conic. Hence T∩N=0, and secant restriction detects N. At a C5 square only the stabilizer-fixed source character contributes, giving the single supplementary scalar. Neither test has been performed on the actual fourth family. Neither tests the extra specialized A-kernel line. Their identical dimensions do not identify their data.

## 17.7 From five Gauss quotient shapes to four and 73 necessary pairs

This is a separate Gauss branch, not a computation of the endpoint P4. For the hypothetical (3,1) rank-three plateau with rank-two dual cubic image, the [five-quotient theorem][FIVE] leaves

    A₀=E/K=O(n−2)⊕W′O(1−e),
    (n,e)=(4,2),(6,2),(8,2),(6,4),(8,4).

The image is saturated. These are necessary shapes, not existence assertions. The [section-envelope refinement][ENVELOPE] tests all 28 necessary primal types against each shape. At twist two, the inclusions and derivative yield, in irreducible-multiplicity order,

    S=H⁰(K(2)) ≤ H⁰(E(2)),    S ≤ H⁰(A₀),
    H⁰(E(2))−S ≤ H⁰(A₀(2)).

The cubic test also retains the derivative upper envelope, Euler positivity, the quotient lower envelope and S⊗W≤H⁰(K(3)). The last inclusion follows from the canonical degree-minus-two evaluation subbundle, not an assumed injectivity of arbitrary section multiplication. The input H⁰(E(1))=0 is global, not inferred from forward length one.

The five twist-two survivor counts are 9,22,23,16,22, totaling 92. The cubic envelopes reduce them to 4,21,21,10,21, totaling 77 of the original 140 pairs. These are necessary overlists, not existence assertions.

The subsequent [smallest-quotient exclusion][SMALL] eliminates the entire (n,e)=(4,2) shape A₀=O(2)⊕W′O(−1), including all four surviving pairs. The section and Euler bounds force exactly two possible splittings:

    K=W′O(−3)⊕(V⊕P4⊕D5)O(−4),
    K=(W′⊕S4)O(−3)⊕(V⊕P4)O(−4)⊕O(−8).

Here S4=Sym³W. The actual derivative K→A₀(−2)=O⊕W′O(−3) is an isomorphism on the W′O(−3) block. Eliminating other components into that target by a triangular source automorphism leaves the unique nonzero polynomial evaluation D5 O(−4)→O or S4 O(−3)→O. Their exact evaluation kernels force, respectively,

    K₂=(V⊕P4)O(−4)⊕S4 O(−5),
    K₂=(A⊕V⊕P4)O(−4)⊕O(−8).

In both cases the first derivative is sheaf-surjective and K/K₂=O⊕W′O(−3). The next derivative must have rank three but maps to O(−2)⊕W′O(−5). Its component into W′O(−5) is zero by degree and Hom_G(S4,W′)=Hom_G(W′,S4)=0. It therefore has rank at most one, a contradiction. This computes the actual derivative kernel; it does not assume a horizontal splitting or lift through a proposed extension.

At this historical stage the progression was 140→77→73 necessary quotient/type pairs, with counts 21,21,10,21 in the order (6,2),(8,2),(6,4),(8,4). [Chapter 18.10](18-actual-cone-lift-and-nilpotent-trace.md#1810-two-gauss-quotient-shapes-and-the-unchanged-frontier) subsequently excludes the whole (6,4) and (8,4) shapes, extending the progression to 140→77→73→63→42. Only (6,2) and (8,2) remain in the rank-two branch at the current cutoff. The entire (3,1) profile and the rank-one dual-image branch remain unresolved. Generic SF≥3 and positive-square rank≥27 are unchanged.

## 17.8 Evidence and unchanged frontier

The absolute comparisons and nonproportionality proof establish a genuine lower-source result. Their universal verifiers check symbolic identities, covariance, characters and degree arithmetic with parameters unassigned. The geometric actual-map comparisons remain dependencies, not consequences of a numerical rank experiment or a proof-assistant certificate.

All four actual fourth coefficients remain unknown. The endpoint P4 secondary residue remains unknown. Generic sections remain four or five; the last generic finite Smith exponent remains 4≤e≤31, or the cokernel is permanent. Original source recovery, lifting and Weil-class algebraicity remain open.

## Pinned source references

[MID]: https://github.com/Akilleez-QA/read-em-and-weep/blob/a90d2ddd38f9ed8c28fcd8ca965f2479a12c9bf2/research/hm/order-four-quadratic-load/ACTUAL-MIDPOINT-ABSOLUTE-SECTION-FOR-THE-FOURTH-SQUARE-INPUT.md
[ATI]: https://github.com/Akilleez-QA/read-em-and-weep/blob/a90d2ddd38f9ed8c28fcd8ca965f2479a12c9bf2/research/hm/order-four-quadratic-load/ACTUAL-ATIYAH-CLASS-HAS-AN-ABSOLUTE-DOUBLE-CUBIC-REPRESENTATIVE.md
[RED]: https://github.com/Akilleez-QA/read-em-and-weep/blob/a90d2ddd38f9ed8c28fcd8ca965f2479a12c9bf2/research/hm/order-four-quadratic-load/ACTUAL-CORRECTED-FOURTH-SQUARE-SOURCE-IS-NONZERO-ON-THE-CUBIC.md
[TRACE]: https://github.com/Akilleez-QA/read-em-and-weep/blob/c9c54d50c94fc17cad7a14fce93b31bb22b9ea5f/research/hm/order-four-quadratic-load/ACTUAL-NORMAL-VARIATION-TRACE-HAS-A-GLOBAL-NULL-HOMOTOPY.md
[FAMILY]: https://github.com/Akilleez-QA/read-em-and-weep/blob/c9c54d50c94fc17cad7a14fce93b31bb22b9ea5f/research/hm/order-four-quadratic-load/LOWER-FAMILY-IS-DETERMINED-BY-SECANT-RESTRICTION-AND-TRACE.md
[FIVE]: https://github.com/Akilleez-QA/read-em-and-weep/blob/a90d2ddd38f9ed8c28fcd8ca965f2479a12c9bf2/research/hm/order-four-quadratic-load/EXTREMAL-31-RANK-TWO-DUAL-IMAGE-FIVE-QUOTIENTS.md
[ENVELOPE]: https://github.com/Akilleez-QA/read-em-and-weep/blob/c9c54d50c94fc17cad7a14fce93b31bb22b9ea5f/research/hm/order-four-quadratic-load/EXTREMAL-31-FIVE-QUOTIENT-SECTION-ENVELOPES.md
[SECANT]: https://github.com/Akilleez-QA/read-em-and-weep/blob/f4f2a5d4e3351da91796b9e7af78707150eac878/research/hm/invisible-channel-geometry/SEPARATING-THE-TWO-INVISIBLE-QUARTIC-LINES.md
[SMALL]: https://github.com/Akilleez-QA/read-em-and-weep/blob/0a95ace992688a278ef211d981e2fdef1bd5f1ad/research/hm/order-four-quadratic-load/EXTREMAL-31-SMALL-QUOTIENT-EXCLUSION.md
