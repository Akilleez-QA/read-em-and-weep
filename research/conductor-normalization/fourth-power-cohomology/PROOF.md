# Publication scope

This is a preserved theorem manuscript, with the exact hypotheses and held identifications listed in unit 04 INPUTS.md. Abstract geometry and formal conditional implications are distinct from identification with the actual HM module or retained source. Historical words such as “new,” “remaining,” or “previously verified” describe the source manuscript, not a claim about the current research frontier.

# Fourth-power ideal cohomology: an excluded shortcut and the exact remaining map

## Result

Let Y=P⁴ over C, B=End₀(HM), and N⊂Y be the reduced triple-root binary-quartic locus. Import the proved geometric identification

    (q_*(I_D⁴ EA))_sign = C := B(-4) I_N,
    I_N=(t₂,t₃), deg(t₂)=2, deg(t₃)=3,

with the actual inclusion into T=B(-4). Then the tempting vanishing H³(B(-9))=0 is false: in fact

    h³(B(-9)) = h¹(B(4)) = 85+h⁰(B(4))+h²(B(4)) ≥ 85.

Thus the proposed all-zero-groups shortcut cannot prove fourth-power vanishing. This does not prove the map H²(C)→H²(T) nonzero: its exact remaining dependence is recorded below.

There is a canonical two-step Koszul boundary

    δ_N : H⁰(N,B(4)|N) → H²(Y,B(-1)).

Under the trace and Serre pairings, the image of fourth-power inclusion is precisely

    im[H²(C)→H²(B(-4))] = (im δ_N)^⊥.

The target has dimension ten by the previously verified HM row. Consequently its image dimension is 10−rank δ_N, without any rank evaluated here. Universal first-ten vanishing for fourth-power representatives holds if and only if δ_N is surjective. All ten classes have fourth-power representatives if and only if δ_N=0. These alternatives are not decided by the present proof.

## 1. Primary cohomology input and its exact scope

W. Decker and F.-O. Schreyer, *Pullbacks of the Horrocks–Mumford bundle*, J. reine angew. Math. 382 (1987), pp.215–220, unnumbered proposition on printed p.218 proves h¹(End(HM)(k))=0 for all k≤−2, with values 24 at k=0 and 5 at k=−1. The saved primary-page image was independently viewed for this proof, and the proposition and normalization c₁(HM)=−1 are legible. Source: https://gdz.sub.uni-goettingen.de/id/PPN243919689_0382?tify=%7B%22pages%22%3A%5B222%5D%2C%22view%22%3A%22info%22%7D .

This proposition gives no positive-twist H¹ or H² vanishing. No such vanishing is imported here. Since End(HM)=O⊕B in characteristic zero and intermediate cohomology of O(k) vanishes on P⁴, the proposition applies to H¹(B(k)). Stability of the rank-two HM bundle gives Hom(HM,HM(k))=0 for k<0, hence H⁰(B(k))=0 in that range. No stability assertion for B itself is needed. The trace pairing gives B≅B∨. Serre duality therefore gives

    H³(B(4)) ≅ H¹(B(-9))∨ = 0,
    H⁴(B(4)) ≅ H⁰(B(-9))∨ = 0,
    H³(B(-9)) ≅ H¹(B(4))∨.

The existing independent source audit derives h²(B(-1))=10 from this same proposition, stability and Riemann–Roch. Duality gives h²(B(-4))=10.

## 2. Riemann–Roch obstruction to the zero-group shortcut

For the normalized rank-two HM bundle, c₁=−H and c₂=4H². Let x₁,x₂ be formal Chern roots and d=x₁−x₂. Then d²=c₁²−4c₂=−15H². The formal roots of B are 0,d,−d, so

    ch(B)=1+exp(d)+exp(-d)=3−15H²+(75/4)H⁴.

Using td₁(P⁴)=5H/2 and td₂(P⁴)=35H²/12 yields

    χ(B(t)) = 3 binom(t+4,4) − (15/2)t² − (75/2)t −25.

At t=4 this is 210−120−150−25=−85. Section 1 eliminates h³ and h⁴ at that twist; hence

    h¹(B(4))=85+h⁰(B(4))+h²(B(4))≥85.

This argument uses a formal Chern-character calculation, not a concrete polynomial, matrix, source or obstruction evaluation.

## 3. Full exact dependence of H²(C)

The imported complete-intersection resolution is

    0 → B(-9) --u→ B(-6)⊕B(-7) --w→ C → 0,
    u(s)=(-t₃s,t₂s),  w(a,b)=t₂a+t₃b.

Put μᵢ=Hᶦ(u). Its long exact sequence gives the unconditional short exact sequence

    0 → coker μ₂ → H²(C) → ker μ₃ → 0.

Equivalently, by duality, put

    αᵢ:Hᶦ(B(1)⊕B(2)) → Hᶦ(B(4)),
    αᵢ(a,b)=-t₃a+t₂b.

Then

    0 → coker α¹ → H²(C)∨ → ker α² → 0.             (1)

Here α¹ is dual to μ₃ and α² is dual to μ₂; all vector spaces are finite-dimensional, so dualization is exact. If one separately proves H²(B(1))=H²(B(2))=0, equation (1) simplifies to

    H²(C)∨ ≅ coker[H¹(B(1)⊕B(2)) --α¹→ H¹(B(4))].

This is conditional; the positive H² vanishings have not been verified in the primary source inspected here. Even with these vanishings, the cokernel and the inclusion into the ten-space do not vanish automatically. A nonzero H³(B(-9)) alone also does not imply a nonzero H²(C), since μ₃ may be injective.

## 4. The actual image through dual restriction

The exact restriction sequence

    0 → C → T=B(-4) → T|N → 0

gives

    im[H²(C)→H²(T)] = ker r,
    r:H²(Y,T)→H²(N,T|N).

The surface N is a local complete intersection of degrees 2 and 3, hence is Cohen–Macaulay and Gorenstein, even though it is singular. Adjunction gives ω_N≅O_N(2+3−5)=O_N. Serre duality on this projective Gorenstein surface and the self-duality of B identify

    H²(N,B(-4)|N)∨ = H⁰(N,B(4)|N),
    H²(Y,B(-4))∨ = H²(Y,B(-1)).

The transpose of r is the codimension-two Gysin map δ_N. It is concretely the composition of the two connecting homomorphisms from

    0 → B(-1) → B(2)⊕B(1) → K=B(4)I_N → 0,
    0 → K → B(4) → B(4)|N → 0.

The first maps are (-t₃,t₂) and (t₂,t₃). Thus δ_N sends a section on N first to H¹(K), then to H²(B(-1)). The identification follows from dualizing the two-term locally free resolution of I_N, or equivalently the compatibility of Serre duality with the Koszul fundamental class. A simultaneous sign/ordering choice changes δ_N at most by a nonzero scalar and never changes its image.

Finite-dimensional linear algebra now gives ker r=(im δ_N)^⊥, proving the result. In particular, merely showing that the component multiplication maps on H² vanish would not show this two-step boundary vanishes or is surjective: this is a secondary Koszul map.

A useful completely explicit dependence, with no vanishings assumed, is

    im δ_N = ∂₁(ker[H¹(K)→H¹(B(4))]),

where ∂₁:H¹(K)→H²(B(-1)) is the first sequence's boundary. This specifies exactly which extension information is required beyond numerical cohomology tables.

More explicitly, let L=B(2)⊕B(1) and define

    V=ker[H²(B(-1))→H²(L)],
    Q=coker[H¹(L)→H¹(B(4))].

Every x∈V lifts to some y∈H¹(K). Mapping y into H¹(B(4)) and reducing modulo the image of H¹(L) defines a well-defined linear map σ:V→Q. Different lifts differ by an image from H¹(L), so the quotient removes the ambiguity. Then

    im δ_N=ker σ ⊂ V ⊂ H²(B(-1)).

Indeed σ(x)=0 exactly when a lift y can be adjusted by an H¹(L) image so that its image in H¹(B(4)) vanishes, precisely the condition to come from H⁰(B(4)|N). This is an exact secondary-map criterion retaining all positive H² terms. If H²(B(1))=H²(B(2))=0 were separately verified, V would be the full ten-space, and the dual of the fourth-power image would identify with im σ. Neither σ nor those vanishings is evaluated here.

## 5. What a source-specific criterion would and would not say

On a quotient-adapted affine Čech cover, a regular closed sign two-cochain in I_D⁴EA defines a class in H²(C). Its ambient first-ten class therefore lies in (im δ_N)^⊥. Fourth-power membership alone forces its ambient vanishing exactly when this entire image is zero. Without that map-level theorem, membership is only a restriction on the possible class, whose strength remains undetermined.

Conversely, an ambient class lies in the stated image if and only if it has some closed fourth-power representative on such a cover. This does not assert that an already chosen physical representative has fourth-power membership. Vanishing of an ambient class also does not imply that a fixed representative lies in I_D⁴. The geometric work separately proves that I_D⁵ has the same sign pushforward as I_D⁴, so all these conclusions apply unchanged to the fifth power if that additional input is used.

No actual physical source has been shown to belong to I_D⁴ or I_D⁵ here. No physical source, obstruction value, pairing, matrix rank, polynomial instance, or jet is evaluated; no external writes or large computations are performed.

## Local dependencies and audit provenance

- ../fourth-ideal-pushforward/PROOF.md: ordinary-colon computation, reduced CI image N, and actual sign-pushforward inclusion.
- prerequisite projective-target-directions, document HM-PRIMARY-SOURCE-VERIFICATION.md (see the unit INPUTS.md) and its saved scan: primary negative-H¹ proposition.
- prerequisite projective-target-directions, document INVARIANT-EXT-COMPLETE-D-AUDIT.md (see the unit INPUTS.md): independent stability, RR and h²(B(-1))=10 verification.
- AUDIT.md: independent audit of this bounded cohomological deduction.

The primary scan establishes the stated negative-twist inputs. Searches for further primary positive-twist data did not supply a verified table; this file deliberately leaves those groups and all multiplication/connecting maps unevaluated.
