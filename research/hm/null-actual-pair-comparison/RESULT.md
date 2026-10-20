# Full pair ordinary-HKR comparison by actual square-zero gauges

## Result and exact scope

For the stipulated actual algebraic pair ambient, with the already established coherent signed-permutation action and equivariant square identity N²=p*O(1), the effective invariant root-transported algebroid has ordinary HKR class

    (P, D_P(H/2), −2H²).

This follows from actual algebra-chart and central-arrow gauges on the full action/Čech nerve, followed by an exact scalar-coefficient descent comparison. It does not follow from evaluating a characteristic map on the carrier. More precisely, after a common affine refinement there exists an equivalence, inducing the identity on reduction and on the canonically normalized coefficient ideal, to the explicit downstairs first-order presentation in Section 5. Thus this is more than an equality of characteristic images or a computation of the symbol. No preferred numerical list of gauge cochains is selected: one remaining scalar Čech primitive is specified by an equation and its existence is proved by an isomorphism of cohomology complexes. No physical evaluation is required to establish that existence.

The conclusion compares a full **pair square-zero algebroid**, including its unary and scalar triple data. It is not a comparison with an unspecified frozen representative at higher order. A corrected model specified only by its ordinary first-order HKR class is determined here only up to first-order identity-reduction equivalence. All thirty retained physical values remain unknown; no global mixed carrier is constructed.

## 1. Inputs inspected and conventions

Historical context: [PR1 comment 6269399364](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6269399364), including its effective affine atlas conclusion and remaining full-ambient comparison. Mathematical dependencies: [research/hm/null-root-morita-inertia/root-morita-0719](https://github.com/Akilleez-QA/read-em-and-weep/blob/711c6bf8c6248f46d73661be8a42ede671a3712b/research/hm/null-root-morita-inertia/root-morita-0719/RESULT.md), [research/hm/null-root-characteristic/root-characteristic-0527](https://github.com/Akilleez-QA/read-em-and-weep/blob/47bce0703b1a78fb05a99541bab2168f4f2170c5/research/hm/null-root-characteristic/root-characteristic-0527/RESULT.md), [research/hm/null-invariant-coefficient-ideal](https://github.com/Akilleez-QA/read-em-and-weep/blob/64b6c62a23db6189186896285c956133608ad3c7/research/hm/null-invariant-coefficient-ideal/RESULT.md), and [research/hm/null-effective-atlas](https://github.com/Akilleez-QA/read-em-and-weep/blob/d8d4a4a096431ad1506b0b847b72b0aeeeceda7f/research/hm/null-effective-atlas/RESULT.md); also the [research/hm/null-pair-swap-coherence](https://github.com/Akilleez-QA/read-em-and-weep/blob/0050df8fa957b9f7f5e1b21137c63bffc646a1eb/research/hm/null-pair-swap-coherence/RESULT.md), [research/hm/null-actual-source-factorization/classical-root](https://github.com/Akilleez-QA/read-em-and-weep/blob/c9bb53d934ad86e50d8519a35d663f9a96fa481d/research/hm/null-actual-source-factorization/classical-root/RESULT.md), [research/hm/null-actual-source-factorization/physical-factorization](https://github.com/Akilleez-QA/read-em-and-weep/blob/c9bb53d934ad86e50d8519a35d663f9a96fa481d/research/hm/null-actual-source-factorization/physical-factorization/RESULT.md) and effective-atlas independent review.

The pinned source [second-order-algebroid.md, commit c8aec970fd65a105f39f4e8aeb8a17f0f0053f89](https://github.com/Akilleez-QA/read-em-and-weep/blob/c8aec970fd65a105f39f4e8aeb8a17f0f0053f89/research/hm/second-order-algebroid.md#L13-L185) fixes the product normalization, total Čech–forms convention, scalar class Π, line calibration and row transition orientation. The source's actual algebraic sheaf/derivative interpretation remains an input; this report does not recertify it by execution.

Let X=C², Y=P², G=W₂, p:X→Y, deg p=8. Let s²=0, with s carrying the determinant character χ, and let Ω(π)=1. Use the antisymmetrized genuinely equivariant representative, equivalent by the previously proved central gauge to the ordered source. Its product is m+sπ/2, unary maps are identity (apart from geometric action on group arrows), and units are 1+s b with [b]=−15Π. The full equivariant scalar cocycle, not only its underlying ordinary Čech class, is used below.

For forms with Čech/groupoid degrees r,r′ and form degrees q,q′, use

    u·v = (−1)^(q r′) u cup-wedge v.

The differential δ is the ordinary simplicial/groupoid coboundary, with face pullbacks included. It is a derivation for this product with the total sign (−1)^(r+q). Thus a one-form Čech one-cocycle has total degree two; a one-form zero-cochain has total degree one. All formulas can be read on the simplicial nerve of the equivariant cover, avoiding any convention ambiguity in a separately totalized group/Čech bicomplex.

Write C(u)=(1/2)ι_π u on two-form-valued cochains and define D_π η by

    (D_π η)(f)=π(df,η).

This is the unary convention furnished by the actual root-conjugation formula. With the source's total-form signs it agrees with the D convention in the corrected characteristic expression. Multiplying its outputs by s gives invariant coefficient-valued maps. No Todd factor is used.

## 2. Compute the actual root-transported cochains

Choose genuine root frames n_a on a G-stable refinement and write n_b=ℓ_ab n_a, including the appropriate geometric pullbacks on group arrows. Set α_ab=dlog ℓ_ab. This is a cocycle on the full groupoid: δα=0. Use the zero-order units ℓ_ab themselves as lifts q_ab in the local product. They are star-invertible: π(dℓ,dℓ⁻¹)=0, so their classical inverses are also their star inverses at this order.

The exact root Morita formulas give

    F^N_ab=Ad_star(ℓ_ab⁻¹) F_ab,
    A^N_abc=ℓ_ab⁻¹ star F_ab(ℓ_bc)⁻¹ star A_abc star ℓ_ac.

Expanding once, and interpreting the result relative to each arrow's geometric map, gives

    μ^N=π/2,
    v^N_ab(f)=π(df,α_ab),
    b^N_abc=b_abc−μ(ℓ_bc,ℓ_ab)/ℓ_ac
             =b_abc−C(α²)_abc.                         (1)

Indeed α²_abc=−α_ab∧α_bc, while μ(ℓ_bc,ℓ_ab)/ℓ_ac=−π(α_ab,α_bc)/2. These fix the scalar sign directly. Any s-linear choices in the q lifts add only the already known scalar coboundary. Equation (1) is a computation of ambient cochains and actual triple units, not a module obstruction calculation.

The original coherent group action can first be made genuine using its known ordered-to-antisymmetrized gauge. The same formulas on all arrows retain the group/group and group/Čech units. Discarding those components would not justify what follows.

## 3. Use the genuine squared-line isomorphism, not only c₁

Choose an affine cover V_i of Y with frames e_i of O(1), with e_j=t_ij e_i and β_ij=dlog t_ij. Refine its inverse-image cover by root-frame opens. The **equivariant line isomorphism** N²≅p*O(1) gives regular invertible functions h_a such that

    n_a²=h_a p*e_i.

Consequently, on all arrows,

    ℓ_ab²=(h_b/h_a)p*t_ij,
    α=α₀+δγ,
    α₀=(1/2)p*β,       γ_a=(1/2)dlog h_a.             (2)

Geometric pullbacks are implicit in the quotient h_b/h_a on a group arrow. The cover labels i can be held fixed under G. Therefore α₀ is zero on pure group arrows. This is precisely where the genuine equivariant square identity is stronger than the rational equality c₁(N)=p*H/2.

Every γ_a is regular, because h_a is a unit on its root-frame open. No logarithm, local analytic branch, or division by a ramification equation is taken: dlog h means h⁻¹dh. Nontrivial order-two inertia is allowed; its constant sign has zero logarithmic derivative. We neither construct O(1/2) on Y nor claim N itself descends.

Now apply the local algebra isomorphisms

    T_a=Id+s D_π γ_a.

Their inverses are Id−s D_πγ_a. The coefficient D_πγ_a is an ordinary derivation, so T_a preserves m+sπ/2 exactly modulo s², without requiring any Poisson-vector-field condition. With F_new=T_a F^N_ab T_b⁻¹, its unary coefficient is

    D_πα + D_πγ_a−D_πγ_b = D_πα₀.                    (3)

A chart map acts trivially on 1+s b^N at this order. To correct the scalar coefficient, put

    K=γ α₀+α₀ γ+γ δγ,       c=C(K).

The product/differential convention in Section 1 gives the literal identity

    δK=(δγ)α₀+α₀δγ+(δγ)²=α²−α₀².                 (4)

There is no commutation of Alexander–Whitney products in (4). Apply the central arrow gauge u_ab=1+s c_ab, with the convention A_new=u_ab F_ab(u_bc) A_old u_ac⁻¹. Since s²=0 this changes b^N by +δc and leaves unary maps unchanged. Equations (1) and (4) therefore give the exact presentation

    μ=π/2,        v=D_πα₀,        b_new=b−C(α₀²).      (5)

All these maps and units are regular algebraic sheaf data, valid also at branch intersections. The full groupoid differential in (4) handles the transported coherence, rather than imposing strictness by fiat.

## 4. Scalar descent and the precisely specified remaining primitive

There is one scalar representative choice to remove. Let β² denote the total Čech–forms representative of H², and set

    B_Y=−15 β²/8 ∈ Čech²(V,ω_Y).

Define the injection of coefficient sheaves in differential-form notation by

    ρ(η)=s f, where fΩ=p*η.                           (6)

Pullback of top forms is injective and regular. The invariant-ideal proof establishes, across every ramification stratum,

    ω_Y ≅ (p_*(sO_X))^G,

with inverse normalized trace (1/8)Tr after multiplication by Ω. It follows that (6) induces a quasi-isomorphism from a downstairs affine Čech complex to the equivariant upstairs refinement complex **for this coefficient sheaf**. Here is the precise justification: p is finite, so inverse images of the V_i and their intersections are affine; quasi-coherent higher cohomology on them vanishes; finite-group invariants are exact in characteristic zero. Refinement and group resolutions therefore compute the same derived sections, namely those of (p_*(sO_X))^G=ω_Y. This includes all positive group-coherence degrees. It is not a claim of naturality of the whole Hochschild complex under a ramified map.

The source specifies [b]=−15Π, Π=C(c₁(N)²). Equation (2), an identity from the actual square isomorphism, gives

    [s b]=[ρ(B_Y)]

in that equivariant scalar complex. To see the normalization directly, C(α₀²)Ω=(1/2)α₀²=p*(β²/8). Thus the class in question is exactly −15/8, not −15 or −15 times eight. The full equivariant class is fixed by its invariant ordinary class because positive group cohomology vanishes; no hidden finite-group additive cocycle remains.

Consequently there exists an ordinary scalar degree-one cochain e in the common equivariant affine refinement with

    δ(s e)=ρ(B_Y)−s b.                               (7)

Equation (7) is the only unevaluated choice in this construction. It is a proved solvable additive Čech equation, not an additional obstruction or an assumption about the carrier. One may obtain a primitive in any chosen affine group/Čech resolution; different solutions give equivalent gauges. Applying the central gauge 1+s e to (5) yields

    μ=π/2,
    v=D_π(p*β/2),
    s b_final=ρ(B_Y−β²/8)=ρ(−2β²).                  (8)

A demand for explicit physical coefficient functions for e would be a stronger, presently unperformed deliverable. The proof of the full first-order equivalence does not require selecting or evaluating them.

## 5. Ramified descent of the complete normal form

On each V_i the downstairs algebra has underlying additive sheaf O⊕ω and product

    (f,η) star (g,θ)=(fg, fθ+gη+(1/2)df∧dg).

The complete overlap and triple data furnished by (8) are

    F_ij(f,η)=(f, η+df∧β_ij/2),
    A_ijk=(1, −2(β²)_ijk).                           (9)

There is no extra action on the ideal because all its correction terms would be quadratic in the square-zero ideal. The derivation rule proves F_ij is an algebra isomorphism. δβ=0 proves the overlap composition identity. A is central and δβ²=0 proves the actual unit pentagon. Thus (9) is an explicit effective corrected pair representative, not a collection of desired characteristic values.

To verify that (8) descends to (9), use the identities of regular forms

    π(d p*f,d p*g)Ω=p*(df∧dg),
    π(d p*f,p*β/2)Ω=p*(df∧β/2),
    C((p*β/2)²)Ω=p*(β²/8).

Each equality holds as a tensor identity everywhere on X. In particular the unary and scalar comparisons do not invert dp and do not divide by its determinant. The coefficient identification (6) handles its vanishing at the branch divisor. This rules out an unexamined Jacobian/ramification correction in these actual cochains.

After the full gauges, pure group-arrow unary corrections vanish because α₀ is pulled back from Y, and the scalar cochain is the inflated base cocycle by (7). The remaining group maps are the genuine geometric/parameter action with trivial extra group-composition units. The actual invariant pushforward therefore has exactly (9). There is no residual root stabilizer character in its internal algebra; the original character remains in the inter-ambient Morita bimodule, where it belongs.

The already established effective-atlas construction is independent, up to its specified identity-reduction comparisons, of choices of auxiliary root modules and invariant generators. Concretely, on U_i=p⁻¹(V_i), take the regular module of the normalized chart; transport it back through the above gauges and the root Morita equivalence. This is an admissible equivariant local root lift of N for that construction. Its end-algebra atlas gives the present normal form, and the prior choice-independence theorem compares it with any other admissible choice. Hence the effective-atlas output is equivalent to the normal form just computed. This uses its effectiveness theorem; it does not substitute pointwise inertia cancellation for that theorem.

## 6. Ordinary HKR and limits of the conclusion

All three components of (9) are already multiderivation/scalar cocycles: the alternating local product is P/2, the unary cocycle is D_P(β/2), and the scalar cocycle is −2β². Ordinary HKR therefore reads off

    [P], [D_P(H/2)], [−2H²].

No evaluation on any rank-two bundle, trace-faithfulness claim, derived-category characteristic-map injectivity, or Todd-modified coordinates enters this deduction. For context, first-order twisted-presheaf deformation coordinates are treated by [Dinh Van–Liu–Lowen, Non-commutative deformations and quasi-coherent modules](https://arxiv.org/abs/1411.0331); here the actual equivalence has been supplied directly by the square-zero formulas, so no general classification theorem is needed to infer its existence.

The narrow comparison is now complete under the stipulated sheaf premises: a full actual pair presentation is equivalent to a representative of the corrected ordinary-HKR direction. Literal equality with a separately fixed presentation is not claimed, and the gauge primitive (7) has not been physically evaluated. If a separately prescribed corrected pair is specified as any differential square-zero representative of these same three ordinary-HKR coordinates, the usual total-cochain equivalence gives an additional first-order comparison after common refinement. Its chosen cochains would still have to be recorded to match a frozen physical representative.

For the already stipulated factorized two-pair algebra, one can tensor these pair equivalences using the established algebraic differential external product. Their products automatically retain st cross terms. This supplies an equivalence to the **external product of (9)**. It does not identify an independently prescribed mixed deformation that may contain an additional mixed class, nor align any specified frozen module two-jet. Existence of a global mixed carrier and the thirty retained values remain open.

No model imports, physical matrix products, parameter searches, physical source/jet evaluations, or experiments were performed.

Independent review: AUDIT.md in this directory records a passing sign, full-groupoid scalar-normalization, ramified-descent, and effective-atlas cross-check. Its initial scalar-normalization caveat is explicitly discharged by Section 4 here and the final review addendum.
