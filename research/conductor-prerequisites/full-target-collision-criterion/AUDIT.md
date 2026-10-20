> Historical mathematical review retained with the source. This is not a new independent review or a formal verification certificate.

# Independent audit: a common sufficient collision order for the full retained target

## Verdict

**PASS at the stated algebraic-sheaf and imported transport scope.** The proposed coefficient identity, the separate first- and second-weight bounds, and the common sufficient unweighted order 12 are correct. The sharper formulation requiring this order only after the order-eight pairing-character projection is also correct.

The theorem is conditional on an actual regular closed representative with the stated ordinary ideal membership and on the regular source-to-paired coefficient transport. It proves neither of those premises for the physical source. It evaluates no obstruction, selected source, jet, matrix, or pairing, and gives existence rather than a formula for the resulting regular primitives.

The constant-zero hypothesis is not needed to use the trace-corrected weight τ. It is needed to replace τ by σ² unless constant-zero has been separately proved. Under the full common-order premise, the same argument at weight zero proves constant-zero as well, provided the unweighted transfer is included.

This audit read the final PROOF.md, including its H-projection and twist-injectivity qualifications, and independently checked it against the effective regularity proof, the all-power ideal calculation, the trace-corrected-square construction, the weighted-selection theorem and its independent audit, and the coefficient/character calculation in the weighted Koszul proof. The proposed H-projection refinement was also checked separately.

## 1. The coefficient identity and all three bounds

Use the natural ungraded permutation linearization on

    A=q*O_Y(1),  E=q*B0⊗A^(-2),  B0=End₀(F).

The previously audited equality of actual sign subsheaves is

    (q_*I^k)_sign=O_Y(-3)K_(k-3),  k≥3.

Because EA^r=q*B0(r-2), projection formula and the exact finite-group sign projector give

    (q_*(I^k EA^r))_sign=B0(r-5)K_(k-3).

This is valid for each r=0,1,2. The -3 Vandermonde twist is independent of r. No additional permutation sign belongs to A.

Put n=k-3. The adjacent-minimal-monomial resolution of K_n, for n≥1, has generator degrees d_i≥n and syzygy degrees

    e_i=d_i+3(b_(i+1)-b_i)≥n+3.

The stronger syzygy estimate is justified by the strict increase of the integer exponents b_i in the chosen ordering. Tensoring by the locally free B0(r-5) preserves exactness. The relevant segment of the cohomology sequence has outer groups

    ⊕H²(B0(r-5-d_i)),  ⊕H³(B0(r-5-e_i)).

Since ω_Y=O_Y(-5), up to fixed harmless one-dimensional normalization factors, and B0 is trace self-dual, their duals are precisely

    ⊕H²(B0(d_i-r)),  ⊕H¹(B0(e_i-r)).

There is no missing extra -1 in these general formulas. For r=1 they specialize to the d_i-1 and e_i-1 formulas in the effective first-weight proof.

The imported 11-regularity gives H²(B0(t))=0 for t≥9 and H¹(B0(t))=0 for t≥10. Therefore n≥r+9 makes d_i-r≥9 and e_i-r≥12. Both outer groups vanish, proving

    H²(Y,(q_*(I^k EA^r))_sign)=0 for k≥r+12.

In particular:

- r=0: k≥12 kills the unweighted sign coefficient cohomology.
- r=1: k≥13 kills the first weighted sign coefficient cohomology.
- r=2: k≥14 kills the second weighted sign coefficient cohomology.

These are sufficient bounds, with no claim of optimality. The n≥1 prerequisite of the resolution is automatically satisfied at every stated bound. The proof uses vanishing of the entire ideal-power H² group, a stronger assertion than merely zero image in the unrestricted ambient cohomology.

## 2. The weights have the needed ordinary ideal orders

In a descended frame, set x=σ₁-σ₂ and y=σ₁-σ₃. Since the three pairing weights sum to zero,

    σ₁=(x+y)/3,
    σ₂=(y-2x)/3,
    σ₃=(x-2y)/3.

Consequently every σ_i is a global section of IA. The trace identity t₂=2∑σ_i² gives q*t₂∈I²A². Thus

    σ∈IA,
    τ=σ²-q*t₂/6∈I²A².

The second expression denotes the pullback of the paired trace-corrected weight. There is no discrepancy between m*t₂ on X and q*t₂ on Z.

These are ordinary ideal-sheaf statements at all points of Z. In particular the complete-intersection weight ideal remains the relevant ideal at a quadruple collision, even though its generators have quadratic order in the small diagonal's transverse coordinates. Small-diagonal order and ordinary powers of I are different measurements.

For a regular closed I^12E-valued cochain R, multiplication yields closed cochains σR and τR with respective ideal orders 13 and 14. The reduced union of all four triple diagonals is S4-stable; hence I, its ordinary powers, and the corresponding tensor coefficient sheaves are stable. The genuine cochain action and the sign projector therefore preserve these ideal memberships. It is unnecessary, and false, to treat σ or τ as S4-invariant.

The result is

    e_sign(σR)∈Z²(I^13EA),
    e_sign(τR)∈Z²(I^14EA²).

Both cochains are boundaries by Section 1. On a quotient-adapted affine cover, the same conclusion holds within their sign ideal-power complexes: finite inverse images and their intersections are affine, and the coherent coefficient sheaves are Čech-acyclic on these opens. No claim that arbitrary generator coefficients in an ideal factorization are themselves closed is needed.

## 3. Precisely which pairing subgroup is used

Let

    H0=⟨(12),(34)⟩,
    H=⟨(12),(34),(13)(24)⟩.

H0 has order four and fixes the two ordered quadratic blocks. H has order eight and stabilizes the unordered pairing 12|34. Its quotient by H0 exchanges the two blocks.

In the ungraded E convention, the paired block-even class has character

    χ=sign|H.

Thus each inner pair swap is negative and exchanging the two blocks is positive. In the natural canonical-form convention, the corresponding paired class is H-invariant. The ordered root top-form permutation sign accounts for the change between the conventions. This is distinct from the all-four-odd deck character on a product of root double covers.

The relevant pairing projector is

    e_H=(1/8)∑_(h∈H)sign(h)h,

not the ordinary invariant average. The weights σ and τ are H-invariant sections: their chosen pairing is fixed, each is even under block exchange, and the trace correction is pulled back from Y.

The unweighted sheaf-vanishing theorem does not require the input cochain to have an H character. That character becomes relevant when identifying its class with the particular paired even target. No S4 representation on the fixed paired deformation ambient is required or asserted.

## 4. Audit of the sharper H-projection criterion

For every H-invariant weight w, multiplication M_w commutes with e_H. Also

    e_sign e_H=e_sign.

Indeed e_sign h=sign(h)e_sign, so every summand in the composite contributes the same e_sign. Consequently the exact regular cochain identity is

    e_sign(w e_HR)=e_sign(wR),  w=1,σ,τ.

It follows that the common sufficient order may be required only of

    R_H=e_HR∈C²(I^12E),  δR_H=0,

rather than of the original R. The target comparison needed is [R_H]=j₀([C]). If [R]=j₀([C]) is already known and the paired image has character χ, then this equality follows automatically. More generally one may stipulate the comparison only after e_H; no assertion about discarded H-character components is then needed.

Because I is S4-stable, applying e_H to an I^12-valued representative never loses its ideal order. This implication does not go in the opposite direction, so the projected formulation genuinely weakens the input requirement. When the input is already H-character-valued, the two formulations coincide.

A different operation must not be confused with this safe normalization: subtracting a previously known unweighted sign boundary does not preserve I^12 membership unless that boundary has the required membership too. The proof should apply to the representative or projected representative for which the ordinary ideal order is actually established.

## 5. Exact transport requirements

The paired-target conclusion requires more than a representation-theoretic selection rule. It needs regular coefficient-level maps whose cohomology gives the inclusions j_r, with the following properties:

1. The paired even finite-duality coefficient is embedded into the actual upstairs E coefficient with the stated H-character and ramification/canonical-line convention.
2. This construction is compatible with the descended line twists O_Y(r), r=0,1,2, and with multiplication by the pulled-back paired sections σ and τ.
3. The full upstairs sign projector corresponds to the paired constant projector. For a paired class D of twist r,

       e_sign j_r(D)=j_r(i_const,r(Tr_m^ωD)),

   where i_const,r(η) is the functional f↦η Tr_F(f)/6.
4. The maps on these constant summands are injective in H². A split regular coefficient inclusion supplies this in every twist; alternatively it must be included as a separate premise.
5. The regular source comparison is made in the full unweighted cohomology, either [R]=j₀([C]) or, in the sharper formulation, [R_H]=j₀([C]).

The draft correctly stipulates the needed injectivity and source comparison. One important logical distinction is worth retaining: an injective map on H² at twist zero does not, by itself, imply injectivity after twisting. Twisting the underlying split coefficient inclusion is valid; formally twisting only an isolated vector-space inclusion is not.

Under these properties,

    [e_sign(σR_H)]=j₁(i_const,1(Tr_m^ω(σ[C]))),
    [e_sign(τR_H)]=j₂(i_const,2(Tr_m^ω(τ[C]))).

Vanishing of the left sides therefore implies vanishing of both weighted traces. The second equality uses the same regular coefficient-module compatibility as the first, with O_Y(2). It is not a new étale-fiber calculation.

The divisor six normalizes the split constant inclusion because Tr_F(1)=6. It does not divide the weighted duality trace itself. Finite duality gives Tr_m^ω(wλ)=λ(w), including on ramified fibers; there is no inversion of a possibly degenerate algebra-trace pairing.

Cohomological source comparison suffices. If, for example, R_H-j₀(C)=δQ with Q regular, then weighting and sign projection change the weighted representative by δe_sign(wQ). This correction must be included when transporting any actual primitive back to the canonical source. The proof does not require Q to have the high ideal order, because the ideal-order vanishing is first established for R_H and only then passed through the cohomological comparison.

If starting on a product C⁴ of root double covers, the all-four-odd finite pushforward and its permutation/frame transport must first identify the relevant coefficient with E on Z. A raw expression on one affine root chart does not establish this global premise. Nor may one silently replace the pulled-back ideal of D by the reduced ideal of its inverse image at ramification points. Any transfer of the proposed ordinary ideal order must be checked for the actual sheaf and ideal used by the theorem.

## 6. Constant-zero and the retained/full distinction

The established trace-corrected coefficient decomposition gives the two retained coordinates

    C10=Tr_m^ω(σ[C]),
    C20=Tr_m^ω(τ[C]),

with intrinsic weight normalization factors W* and (W*)². Their joint vanishing is equivalent to zero of the retained thirty-dimensional class, without any assumption about the constant coordinate.

For a general even class,

    Tr_m^ω(τ[C])
      =Tr_m^ω(σ²[C])-(t₂/6)Tr_m^ω([C]).

Thus replacing τ by σ² is justified if the constant coordinate is zero in cohomology. It does not imply that an arbitrary constant representative vanishes pointwise. The trace-corrected weight avoids this extra assumption entirely.

There is also a valid stronger conditional conclusion. Under the same I^12 premise on R_H, the r=0 case gives [e_sign R_H]=0. By the unweighted sign/constant comparison, Tr_m^ω([C])=0. Therefore the common-order hypothesis and all three transfer comparisons kill the full even class, including its constant component. This conclusion must stay conditional on the representative-membership premise; it is not a second independent proof for the actual physical source without that premise.

If the membership premise is established only for a representative of the retained projection, the argument proves zero of that retained projection. It makes no new statement about a different unprojected class's constant component. The draft's formulation with the full paired class C avoids this ambiguity.

## 7. Scope limits and final finding

The audited criterion requires actual ordinary sheaf membership of a globally regular closed representative on a cohomology-computing cover. It is not implied by set-theoretic vanishing, generic-branch order, a formal small-diagonal order, deformation order, or high order of an already weighted sign remainder alone.

The H-projected common-order formulation is sound and useful. At the admitted coefficient and transport scope it supplies a universal sufficient test for both retained targets, with conditional vanishing of the constant target as well. No necessary condition, minimal collision order, physical membership, evaluated obstruction, or explicit source primitive has been obtained.

 No physical-source value is evaluated.
