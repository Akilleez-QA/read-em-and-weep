# Supporting regularity theorem

This existing result is included as a prerequisite for the selected pole, detector and socle manuscripts. The older intermediate bounds are preserved as history; SHARPEST-BOUND.md records the stronger proved bounds under its precise hypotheses. No source membership is inferred.

# Exact regularity of normalized HM and improved tracefree bounds

## Result

For the normalized Horrocks–Mumford bundle F on complex P⁴,

    reg(F)=5.

Consequently F∨ is 4-regular and B₀=End₀(F) is 9-regular. In particular

    H¹(B₀(t))=0 for t≥8,
    H²(B₀(t))=0 for t≥7.

Thus H²(B₀(8))=0 is settled affirmatively. The regularity bound for B₀ need not be sharp.

## Primary verification

Source: Wolfram Decker, *Monads and cohomology modules of rank 2 vector bundles*, Compositio Mathematica 76 (1990), 7–17.

https://www.numdam.org/article/CM_1990__76_1-2_7_0.pdf

Printed page 13 (PDF page 8) expressly normalizes c₁F=−1 and identifies H²F(*) as a two-dimensional vector space in degree −2. Printed page 16 (PDF page 11), Remark 2(ii), displays the following minimal graded free resolution, with S=C[z₀,…,z₄]:

    0→2S(-8)→20S(-6)→35S(-5)⊕2S(-3)
      →15S(-4)⊕4S(-3)⊕10S(-2)→15S(-1)→5S→H¹F(*)→0.

Both printed pages were inspected as rendered images, rather than relying on OCR, which omits the displayed equations. The primary PDF is linked above; source page-image verification is historical provenance, not an attachment in this review unit.

## Independent consequences of that resolution

Taking the alternating sum of the Hilbert series of the free modules yields

    Hilb(H¹F(*),z)
      =(5−15z+10z²+2z³+15z⁴−35z⁵+20z⁶−2z⁸)/(1−z)⁵
      =5+10z+10z²+2z³.

The last equality is a polynomial identity (checked by multiplication; a tiny symbolic factorization was also performed). Hence H¹F(t) vanishes for t<0 and t≥4, and h¹F(3)=2. This uses no selected matrix rank, polynomial instance or geometric source evaluation.

## The four regularity conditions

For rank two, c₁F=−1 gives F∨≅F(1). Serre duality therefore gives

    Hⁱ(F(t))∨≅H^(4−i)(F(−t−4)).

The four groups for 5-regularity vanish:

- H¹F(4)=0 by the Hilbert series.
- H²F(3)=0 because the only nonzero H² twist is −2.
- H³F(2)∨=H¹F(−6)=0 by the Hilbert series.
- H⁴F(1)∨=H⁰F(−5)=0.

For the last condition, stability suffices, but no stability theorem is needed: use the normalized monad 5O(−1)→2Ω²(2)→5O and its kernel K. After twisting by −5, H⁰K(−5) injects into H⁰(2Ω²(−3))=0, and H¹(5O(−6))=0. The sequence 0→5O(−6)→K(−5)→F(−5)→0 then implies H⁰F(−5)=0. The exterior Euler sequence injects Ω²(−3) into 10O(−5), verifying its H⁰ vanishing.

Thus F is 5-regular. It is not 4-regular because h¹F(3)=2. Persistence of regularity rules out all smaller regularities, proving reg(F)=5.

## Endomorphisms

Twisting by O(1) lowers the regularity bound by one, so F∨=F(1) is 4-regular. Tensor subadditivity for locally free sheaves on projective space makes F⊗F∨ 9-regular. In characteristic zero the trace splitting

    End(F)=O⊕End₀(F)

makes B₀ 9-regular as a direct summand. Persistence gives Hⁱ(B₀(t))=0 whenever t≥9−i. In particular the claimed separate H¹ and H² thresholds follow.

The tensor subadditivity and persistence references and hypotheses were checked in ../effective-collision-bound/PROOF.md, Section 2; this proof changes only the HM regularity input.

## Consequence for the older coefficient-cohomology criterion

In ../sixth-ideal-pushforward/ALL-POWERS.md set n=k−3. Its adjacent-generator resolution has dᵢ≥n and eᵢ≥n+3. Tensoring by B₀(−4) and dualizing the controlling outer groups reduces them to H²B₀(dᵢ−1) and H¹B₀(eᵢ−1). Therefore all outer groups vanish for n≥8, proving

    H²(B₀(−4)K_(k−3))=0 for every k≥11.

This particular argument does not establish coefficient-cohomology vanishing at k=10: K₇ has a weight-seven minimal generator t₂²t₃, whose outer group involves H²B₀(6). No assertion that this group is nonzero is made. A stronger statement about the image in ambient cohomology can use additional arguments and must be distinguished from vanishing of the coefficient-cohomology group itself.

## Scope

This is a formal cohomological consequence of a published primary resolution. No actual HM matrices were evaluated; no source representative, selected rank instance, obstruction coordinate or jet was computed. No publishing or source-app changes were made.

## Both weighted targets and the common unweighted order ten

The numerical distinction is essential:

- unweighted sign coefficient (r=0): sufficient ideal order k≥10;
- first-weight sign coefficient (r=1): sufficient ideal order k≥11;
- second-weight sign coefficient (r=2): sufficient ideal order k≥12;
- one common UNWEIGHTED regular source representative: sufficient ideal order 10, because the weights supply one and two further orders.

Here is the uniform argument, under exactly the geometry and regular transport hypotheses in prerequisite full-target-collision-criterion, document PROOF.md. (see the unit INPUTS.md) Its coefficient formula is

    (q_*(I^k EA^r))_sign=B₀(r−5)K_(k−3),   r=0,1,2.

Writing n=k−3, the controlling dual groups are

    H²B₀(dᵢ−r),     H¹B₀(eᵢ−r).

If n≥r+7, then dᵢ−r≥7 and eᵢ−r≥10≥8, so both vanish by 9-regularity. This proves

    H²(Y,(q_*(I^k EA^r))_sign)=0 for k≥r+10.

A closed regular unweighted representative R∈I¹⁰E therefore gives

    e_sign(σR)∈Z²(I¹¹EA),
    e_sign(τR)∈Z²(I¹²EA²),

because σ∈IA and τ∈I²A², while projection preserves ideal powers. Both classes vanish in their ideal-power coefficient cohomology. The imported regular class transport, weighted multiplication compatibility, and injective constant inclusions identify these vanishings with vanishing of the two retained weighted traces. The same r=0 argument kills the constant component if the corresponding transport is included.

The assumption may instead be imposed on the H-sign projection R_H of a raw source, exactly as in the imported theorem. Closure, global regularity, ideal membership, the correct coefficient identification and the cohomological comparison [R_H]=j₀([C]) are separate necessary premises. No actual source is claimed to satisfy them. The sufficient common order 10 is not asserted minimal and is not a deformation order.
