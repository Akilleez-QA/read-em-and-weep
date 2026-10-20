# Publication scope

This is a preserved theorem manuscript, with the exact hypotheses and held identifications listed in unit 06 INPUTS.md. Abstract geometry and formal conditional implications are distinct from identification with the actual HM module or retained source. Historical words such as “new,” “remaining,” or “previously verified” describe the source manuscript, not a claim about the current research frontier.

# Discriminant localization cannot detect the retained obstruction

Let Y=P⁴ over C, B₀=End₀(HM), D=V(Δ), where Δ is the nonzero degree-six binary-quartic discriminant. Put F₁=W*⊗B₀(-4) and F₂=(W²)*⊗B₀(-3). The constant one-dimensional factors W* and (W²)* are retained intrinsically and omitted in twist computations below. We assume the admitted source comparison to these coherent cohomology groups and a common compatible algebraic Čech complex. This is a structural theorem for every class, not a computation of the actual source.

## 1. Affine exclusion and explicit finite bounds

Write S=C[a,b,c,d,e]. The complement U=Y\D is D₊(Δ)=Spec((S[Δ⁻¹])₀), hence affine. Every positive-degree coherent cohomology class restricts to zero on U. In particular H²(Y,Fᵢ)→H²(U,Fᵢ|U) is the zero map. Constructing a primitive only after removing D, even a globally compatible primitive on U, therefore supplies no vanishing test for the retained class.

The established 11-regularity of B₀ gives H²(B₀(t))=0 for t≥9 and H¹(B₀(t))=0 for t≥10. Thus multiplication by Δ³ maps H²(B₀(-4)) to H²(B₀(14))=0, while multiplication by Δ² maps H²(B₀(-3)) to H²(B₀(9))=0. These are twisted multiplication maps, not multiplication by a global function on projective space.

More concretely, on a finite affine cover of Y with affine intersections, let cᵢ be any regular 2-cocycle of Fᵢ. The natural inclusion Fᵢ→Fᵢ(nD) sends cᵢ to a boundary for (i,n)=(1,3),(2,2). Choose hᵢ∈C¹(Fᵢ(nD)) with δhᵢ=cᵢ. Interpreting Fᵢ(nD) inside the meromorphic sheaf Fᵢ(*D), these are compatible meromorphic primitives with poles of order at most three and two respectively. Equivalently solve δbᵢ=Δⁿcᵢ in the twisted bundle and divide by Δⁿ. No choice or evaluation of the actual source is needed for this existence statement, and it does not supply an explicit source primitive.

These are sufficient universal bounds, not proven minimal bounds. A smaller pole bound may impose a genuine condition: classes admitting a primitive with pole order ≤n are exactly ker[H²(Fᵢ)→H²(Fᵢ(nD))]. The theorem excludes unbounded localization and these universal bounds as discriminators; it does not exclude stronger, source-specific small-pole constructions.

## 2. Exact principal-parts obstruction

Define Pᵢ,n=Fᵢ(nD)/Fᵢ. Here principal parts means polar parts along D, not the sheaf of jets of the diagonal. D is an effective Cartier divisor, including at its singular points, and there is an exact sequence

0→Fᵢ→Fᵢ(nD)→Pᵢ,n→0.

For a bounded-pole primitive h, its polar part q=πh is a closed Čech 1-cochain because δh=c is regular. The connecting map ∂:H¹(Pᵢ,n)→H²(Fᵢ) sends [q] to [c], with the convention ∂[q]=[δh]. The relevant exact sequence is

H¹(Fᵢ(nD))→H¹(Pᵢ,n)→H²(Fᵢ)→H²(Fᵢ(nD)).

Consequently the invariant obstructing replacement of h by a regular primitive is the class of [q] modulo im H¹(Fᵢ(nD)). It is independent of the chosen bounded-pole primitive. At a universal bound this quotient is canonically H²(Fᵢ); it relocates the entire original obstruction and does not eliminate it.

For an explicit proof of the removal criterion, suppose [q] lies in that image. Choose a closed meromorphic 1-cochain z with [πz]=[q]. Then q−πz=δa for a 0-cochain of Pᵢ,n. On the affine cover a lifts to a meromorphic 0-cochain b, by exactness of sections for quasi-coherent sheaves on affine opens. Therefore h−z−δb has zero polar part, is a regular 1-cochain, and its differential remains c. Conversely if r is a regular primitive, h−r is closed and maps to q. This is exact both ways.

At the first universal bound, F₁(3D)=W*⊗B₀(14), so H¹ and H² vanish and

H¹(P₁,3) ≅ H²(F₁).

At the second smaller universal bound, F₂(2D)=(W²)*⊗B₀(9), so only H² is certified to vanish. The correct statement is

H¹(P₂,2)/im H¹(F₂(2D)) ≅ H²(F₂).

One must not silently discard H¹(B₀(9)); the established regularity does not cover it. Taking the common bound n=3 gives F₂(3D)=(W²)*⊗B₀(15), so both outer groups vanish and

H¹(P₂,3) ≅ H²(F₂).

Naturality identifies the map H¹(P₂,2)→H¹(P₂,3) with the second connecting map followed by the inverse of this isomorphism. It is therefore surjective, with kernel exactly im H¹(F₂(2D)). Passing from the two-pole principal parts to common three-pole principal parts removes precisely the closed-meromorphic-cochain ambiguity; it does not discard any actual obstruction information.

More generally all transition maps H¹(Pᵢ,n)→H¹(Pᵢ,m) for m≥n≥3 are isomorphisms, since both connecting maps identify them with the identity on H²(Fᵢ). Thus allowing still larger poles stabilizes the obstruction rather than erasing it from principal-parts cohomology.

Using the previously established dimensions ten and twenty, the two common triple-pole polar-part groups have dimensions ten and twenty. All thirty retained conditions therefore survive exactly as a principal-parts cohomology class. The group dimensions are inherited premises, not new rank evaluations.

## 3. A finite, precise next dependency

The useful next step for any actual meromorphic construction is to form its closed polar 1-cochains on a compatible cover and prove the classes above vanish (or prove one nonzero). At common bound three, the requirement is exactly [q₁]=[q₂]=0 in H¹(P₁,3)⊕H¹(P₂,3). At bounds three and two, the second class need only lie in im H¹(F₂(2D)). Merely checking that poles occur only on D, that the order is bounded as above, or that the differential is regular does not discharge this requirement.

There is also a finite layer-by-layer formulation. Write Pᵢ,0=0. For k≥1,

0→Pᵢ,k−1→Pᵢ,k→Fᵢ(kD)|D→0.

The highest polar symbol of h is a closed 1-cochain in Fᵢ(kD)|D. After allowing subtraction of a closed k-pole 1-cochain, h can be reduced to a (k−1)-pole primitive precisely when its symbol class lies in the image of H¹(Fᵢ(kD))→H¹(Fᵢ(kD)|D). This follows from 0→Fᵢ((k−1)D)→Fᵢ(kD)→Fᵢ(kD)|D→0 by the same cochain lift argument. For a specified h without closed-cochain adjustment, a zero symbol cohomology class suffices to remove that layer by a coboundary. Local cancellations or a vanishing top layer do not by themselves remove all lower layers. Singularities of D do not change these exact sheaf statements.

## 4. Why regular Frobenius reconstruction does not bypass this test

The source's latest reconstruction uses the regular coefficient pairing ε:A→L², with dual basis (τ+I,σ,1), and gives mutually inverse O_Y-linear chain maps E and R between the even duality coefficient complex and its three coordinate complexes. Tensoring these maps by O(nD) preserves their inverse identities and commutes with inclusions from pole order n−1 to n. Therefore E and R induce inverse maps on polar-part sheaves and their cohomology as well. They preserve the common pole filtration in both directions.

After the certified constant component has a compatible regular primitive p₀, reconstruction of bounded-pole p₁,p₂ introduces no poles beyond the common bound. But the reconstructed primitive is regular exactly when its coordinate cochains are regular. Likewise its polar-part obstruction vanishes exactly when both retained coordinate obstructions vanish. There can be no hidden cancellation between the two independent coordinate classes that evades pole removal: applying E recovers each coordinate.

Regular reconstruction solves assembly after compatible regular primitives exist. Localization solves existence of meromorphic primitives for every possible class. The missing mathematical content between them is exactly the polar-part class above. Preserve all source comparison corrections: if R_raw−j(c)=δq_source, first subtract e(wq_source) from an upstairs weighted primitive and apply the admitted coefficient projection/chain identification. Regular corrections alter no polar parts, but this assertion applies only once their regularity and common-complex compatibility are established. For the original mixed defect D_mix=D_model+δh_corr, a resulting regular model primitive H_model produces x=−h_corr−H_model, as in the latest handoff.

## Sources and scope

- Latest reconstruction: https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6279132359
- Local regularity proof: ../effective-collision-bound/PROOF.md, especially §5.
- Local regular reconstruction audit: prerequisite regular-reconstruction-update, document AUDIT.md. (see the unit INPUTS.md)
- Coordinate identification: prerequisite weighted-trace-filtration-audit, document TRACE-CORRECTED-SQUARE.md. (see the unit INPUTS.md)
- Standard affine opens in Proj: https://stacks.math.columbia.edu/tag/01M3, §27.8.
- Affine higher-cohomology vanishing and affine-cover Čech comparison: https://stacks.math.columbia.edu/tag/01X8, §30.2.

Only structural sheaf arguments were used. No actual mixed-source, selected rank, polynomial-instance, jet or obstruction evaluation, or large computation occurred. All thirty actual values remain undecided.
