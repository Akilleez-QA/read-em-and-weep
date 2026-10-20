# Independent audit: normalized line-complex quantization

20 October 2026. Formal result and existing review record; actual HM/source values are not evaluated here.

## Verdict and essential distinction

The line bundles in the normalized resolved complex

    L = [5N⁻¹ → 15N → 10N³ → 2N⁵],   N=O(1,1,1,1),

admit compatible commuting additive-action lifts and therefore a global twist quantization of their morphism category. This alone does **not** quantize the differential or its degree-zero cohomology bundle. In the canonical compensated-symmetry sector the strict global first-order differential correction is actually zero. A strict solution consequently requires literal vanishing of its first curvature matrix, not merely vanishing of that matrix's hypercohomology class.

The full derived endomorphism model has additional total-degree-one contributions from H⁴ of negative Hom bundles. Those are not optional terms that can be discarded in an argument using Ext groups. In the relevant χ12, (a,b)=(-,+) sector, the H⁴(End⁻³) input has dimension 60 before differentials. This is compatible with zero Ext¹ in that sector: source cochains and surviving cohomology classes are different notions.

## 1. Actual model and additive lifts

The pinned ext-model.md source gives the four-term complex on P⁴ with degrees -1,0,1,2 and terms 5O(-1),15O,10O(1),2O(2). Pullback along x_i=t_i², followed by the root twist N, yields the displayed powers. The normalized-model identification and vector field are independently recorded in ../null-cusp-normalization/cusp-normalization-next.md.

On a finite coordinate chart define, on Nⁿ,

    D_i^(n) = (t_i²/2)∂_(t_i) − (n t_i/2).

For a change to u_i=1/t_i, write a coefficient as f=t_iⁿ g(u_i). Direct differentiation gives

    D_i^(n)(t_iⁿ g)=−(t_iⁿ/2)∂_(u_i)g.

Thus the apparent zero-order pole is precisely what makes the operator global on the line bundle. It has symbol V_i=(t_i²/2)∂_(t_i), and is the infinitesimal lift of the standard unipotent action on P¹ and its integral tensor powers. Distinct factor lifts commute. The compatibility required for tensor products is

    D_i^(n+m)(fg)=D_i^(n)(f)g+fD_i^(m)(g).

In particular an element a of Hom(Nⁿ,Nᵐ)=N^(m−n) carries D_i^(m−n), not D_i^(0). Equivalently,

    D_i^(m)(a s)−a D_i^(n)(s)=D_i^(m−n)(a)s.

This formula is necessary for any proposed quantized Hom composition.

## 2. Exact twist and signs

Fix the normalization of the actual scalar Moyal product. For illustration write its exponent as sP+tQ, with

    P=(D₁⊗D₂−D₂⊗D₁)/2,
    Q=(D₃⊗D₄−D₄⊗D₃)/2.

If the scalar source uses another coefficient, replace both displayed halves consistently; none of the parity conclusions depends on that normalization. For composable b:Nⁿ→Nᵐ and a:Nᵐ→Nˡ, define

    a ⋆ b = composition ∘ exp(sP+tQ)(a⊗b),

using D^(l−m) on the first Hom factor and D^(m−n) on the second. Output is in Hom(Nⁿ,Nˡ)[[s,t]]. The operator is global. Tensor-product compatibility and commuting D's imply associativity by the ordinary abelian-twist identity. There is no additional Koszul sign from D, since these operators are even. Matrix order remains a after b.

This constructs an associative graded category, not yet a DG category with the old differential d. Set C_P(a,b)=composition(P(a⊗b)), and C_PP=composition(P²(a⊗b))/2. If d_s=d+s a+s² b, square-zero means

    [d,a] = −C_P(d,d),
    [d,b] = −(a²+C_P(d,a)+C_P(a,d)+C_PP(d,d)).

Here a,b have internal degree one and [d,a]=da+ad. Associativity gives [d,C_P(d,d)]=0 with the degree-two commutator dC−Cd. It does not give C_P(d,d)=0. Before a square-zero differential has been supplied, the commutator with d in the twisted category is generally curved rather than a differential.

The same convention extends to the two-parameter equations; the mixed second-order twist coefficient is composition(PQ(a⊗b)), since P and Q commute. Importing the formulas into a reversed row-composition convention requires consistently reversing composition, not silently mixing conventions.

## 3. Strict compensated-symmetry bottleneck

Factor permutations act trivially on the fixed HM multiplicity spaces and canonically on the pulled-back line bundles. The classical d is invariant. A degree-one strict correction is a global section of

    End(L)¹=N²⊗C²⁴⁵.

Deck χ12 sections of N² have the monomial basis

    t₁t₂ t₃^e₃ t₄^e₄,   e₃,e₄∈{0,2}.

Every one is even under a=(12). Thus

    H⁰(End(L)¹)_(χ12,a=-)=0.

Likewise the χ34, b=(34)-odd strict sector vanishes. The active vector-field wedge is odd under its internal swap, and has the indicated pair deck character. Therefore the first-order curvature C_P(d,d) is χ12 and a-odd, while a symmetry-compatible strict a must be zero. A strict equivariant lift exists to first order if and only if

    C_P(d,d)=0 as a global matrix section.

This is stronger than its class being zero in Ext². It is also not bypassed by starting with a nonequivariant strict first-order correction: the equation is linear with equivariant source, so projection to the desired sector would give a solution there. Since that sector is zero, existence of any strict solution forces the same literal zero. This last statement fixes the same classical complex and quantized line terms; changing the resolution or introducing descent/higher components is not a strict solution in that sense.

There is no formal proof here that this curvature is zero or nonzero for the actual HM maps. No permitted identity has been replaced with a source evaluation.

## 4. Full derived corrections and the missing H⁴ row

For -3≤r≤3,

    End(L)^r=N^(2r)⊗C^(m_r),
    m₀=354, m_(±1)=245, m_(±2)=80, m_(±3)=10.

On (P¹)^4, these bundles have only H⁰ for r≥0 and only H⁴ for r≤−1. Consequently the hypercohomology E₁ page contains both rows. In total degree one it contains H⁰(End¹) and H⁴(End⁻³). A totalized Čech correction may have components

    (Čech degree, internal degree)=(0,1),(1,0),(2,-1),(3,-2),(4,-3).

The last component is not representable by a global adjacent-map correction.

For the χ12 part of H⁴(N⁻⁶), use the standard Laurent representatives t_i^e_i with -5≤e_i≤-1. The odd exponent space in each active factor has dimension 3; the even exponent space in each complementary factor has dimension 2. Hence the χ12 dimension is 3²·2²=36, and after multiplicity it is 360.

Permutation of two H¹ factors includes the Čech/Künneth minus sign. Thus a=- corresponds to the symmetric square of the active three-dimensional odd space (dimension 6), while b=+ corresponds to the exterior square of the complementary two-dimensional even space (dimension 1). Therefore

    dim H⁴(End⁻³)_(χ12,a=-,b=+) = 10·6·1 = 60.

This is a dimension of an input space, not an Ext¹ dimension or a verified rank statement. The symmetric χ34 sector has the same dimension.

With E₁^{r,p}=H^p(End^r), the potentially relevant higher differential is

    d₅: E₅^(-3,4) → E₅^(2,0).

It can remove a global degree-two curvature class after that class has survived the earlier differentials. An actual first-order correction in a full Čech model may supply the corresponding staircase. Neither this possibility nor the dimension 60 proves that a particular curvature is killed; actual differentials and the stipulated deformation still matter. Conversely, vanishing Ext¹ in this sector does not imply no first-order solution to an inhomogeneous equation: it describes uniqueness modulo gauge after existence.

## 5. Relation to ../null-normalized-boundary-comparison/normalized-boundary-comparison.md

The comparison theorem concerns genuine first-order bundle/module lifts over the same normalized Moyal algebra and in the specified compensated-symmetry sector. Once such a lift is constructed, the theorem identifies its first-order gauge class with the transported stipulated lift, subject to its imported premises. A collection of quantized line terms without a square-zero deformed differential is not such a lift. A bare assertion that the curvature is cohomologically exact is also not an explicit second-order construction.

A strict differential successful to second order would be a sufficient route, provided its cohomology is the required locally free deformation and all comparison hypotheses are checked. It is not a necessary representation of every valid deformation; the full Čech/derived model may require non-strict descent data.

## Sources and limits

Reviewed: ../null-normalized-boundary-comparison/normalized-boundary-comparison.md; ../null-cusp-normalization/cusp-normalization-next.md; https://github.com/Akilleez-QA/read-em-and-weep/blob/add03476d9055aa00e1e00778eea6332cf8e01cc/research/hm/ext-model.md. Source lineage is inherited from those reports; no fresh remote authentication is claimed.

The boundary-comparison report imports characteristic-zero HM rank facts and stipulated first-order existence. This audit does not recalculate those facts. The independent deductions here are the line-lift gluing identity, precise twist-composition convention, strict-sector zero, and full-model input-space calculation. No obstruction coordinate, second-order primitive, or final vanishing theorem is produced.

## 6. Consistency check of the completed construction

I subsequently read normalized-monad-lifting.md in full. Its actual formula (4) for Q(F) is the correct quantized morphism, not the generally invalid unchanged multiplication map. For its right-module convention, Q(F)(z⋆a)=Q(F)(z)⋆a follows by writing both sides as the same three-factor abelian twist; Q(F)Q(G)=Q(F⋆G) follows by the same calculation. These are consistent with the Hom exponent difference in §1 above.

The strict first- and second-order equations have the correct signs and coefficients for the declared composition order. The full equations use the total graded product and have the same signs after totalization. To remove any convention ambiguity, one may define the cup/composition product on bidegrees (p,r) and (q,s) with factor (-1)^(r q). Then its graded commutator with the global degree-one d acts on bidegree (p,r) as (-1)^p times the internal commutator; hence D=δ+[d,-] is precisely the usual total differential. This clarification is incorporated in the result.

The full criterion's necessity and sufficiency are correctly restricted to the perfect-complex deformation model. Its use of nilpotent local splitting and compatible twisted-complex descent is appropriate: locally contractible pairs can be canceled, leaving a locally free lift of E in degree zero. The converse permits transition and higher-homotopy corrections and does not silently restrict to a strict global differential. The first-order d₅ image criterion is correct in the identified symmetry sector: C¹ there is zero, and the only cross-row differential that can hit the lower-row degree-two class is d₅ from upper-row internal degree -3.

Final audit disposition: accepted as a formal construction criterion and structural obstruction analysis, with the explicit imported existence/comparison premises retained. It does not establish a solved second-order lift or the vanishing of the remaining six conditions. The report's separation of those conclusions is accurate.

## 7. Diagonal scope correction verified

The scope correction identified an important scope distinction in the initial §5 wording. I read the corrected §5, including equation (16), and verified it: on s=t=h the second-order equation is

    D b_diag = −(R_PP+R_PQ+R_QQ).

When the imported mixed obstruction class vanishes, this is equivalent to [R_PP+R_QQ]=0, not to separate vanishing of the two pure classes. The latter is required by a full two-parameter lift and is generally stronger. Only the diagonal sum is identified, under the stated imported comparison and detection hypotheses, with the accepted six-condition problem. The construction now states that distinction explicitly and correctly. My acceptance of the full equations is acceptance of the full two-parameter criterion, not a claim that it is necessary for diagonal lifting.
