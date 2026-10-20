# Independent audit: first-order root-transport gauge

## Verdict

The proposed chart gauge and central arrow correction have the correct signs with the stipulated total Čech–forms product. They give a genuine first-order cochain comparison, not just equality of characteristic evaluations. Descent of the scalar term requires one additional explicit normalization of the original scalar cocycle, or a hypothesis that it already is a horizontal invariant representative. The claim is valid for the full equivariant first-order ambient class stipulated below; it does not follow from its characteristic image alone.

Everything here is formal algebra. No physical execution, import, or experiment is used.

## 1. Cochain convention and direct Morita expansion

Write products of a Čech p-cochain of q-forms and a Čech p'-cochain of q'-forms with the sign (-1)^(q p'). The Čech differential is a derivation with respect to total degree p+q. In particular, if α is a Čech 1-cochain of 1-forms,

    (α²)_ijk = -α_ij ∧ α_jk.

Take the first-order product μ(f,g)=π(df,dg)/2, zero original unary cochain, original triple unit 1+s b, and lifted line arrows q_ij=ℓ_ij, with s²=0. The exact inverse-line Morita transport gives

    v'_ij(f)=π(df,α_ij),                 α=dlog ℓ,
    b'_ijk=b_ijk - μ(ℓ_jk,ℓ_ij)/(ℓ_ijℓ_jk)
           =b_ijk + π(α_ij,α_jk)/2
           =b_ijk - (ιπ α²)_ijk/2.

This confirms the scalar sign independently of the characteristic map. The equations apply to all composable arrows of the full action/Čech groupoid, with the appropriate pullbacks implicit.

## 2. Chart and arrow gauges

Choose local root-square trivializations with conventions giving

    α=α₀+δγ,     α₀=(1/2)p*dlog t,     γ=(1/2)dlog h.

The identity must come from an equivariantly compatible genuine isomorphism N²≅p*O(1), not merely its Chern class.

Define w_i(f)=π(df,γ_i). This is a derivation. The chart identification G_i=Id+s w_i preserves the local first-order product. Under

    F^new_ij=G_i F'_ij G_j^(-1)

its unary term is v'_ij+w_i-w_j, hence Dπ α₀. Its action on a triple unit 1+s b' leaves b' unchanged to this order.

Set

    c=(1/2)ιπ(γ α₀+α₀ γ+γ δγ).

Since γ has total degree one, α₀ has total degree two, and δα₀=0,

    δ(γ α₀+α₀ γ+γ δγ)
      =δγ α₀+α₀ δγ+(δγ)²
      =α²−α₀².

The arrow units 1+s c are central at first order. Their algebroid gauge adds δc to b' and does not change unary arrows. Consequently the final cochain is exactly

    (π, Dπ α₀, b−(1/2)ιπ α₀²).

This result includes the full groupoid, not just ordinary chart intersections. Reversing the direction of chart conjugation or using 1−s c would reverse the needed signs.

## 3. What is still needed to descend b

The displayed gauge leaves the original b in place. Thus an arbitrary original full-groupoid representative b does not become a horizontal invariant cochain merely because its cohomology class is invariant.

A sufficient precise hypothesis is that the original scalar class, in the full equivariant coherent-cochain complex, is

    [b]=−15[(1/2)ιπ α₀²].

Then put b₀=−(15/2)ιπ α₀². Equality of these full classes supplies a scalar 1-cochain β with δβ=b₀−b. The additional central arrow gauge 1+sβ changes the original scalar representative to b₀. This is legitimate before or after the root correction; to first order the central corrections add.

For a finite group in characteristic zero, coherent group cohomology in positive degree is contracted by averaging. In a suitable equivariant acyclic Čech resolution, invariant Čech cochains compute the same cohomology as the full action/Čech total complex. This supplies the invariant representative argument, including elimination of group-degree components; it is not a statement about ramified Hochschild–Kostant–Rosenberg descent. One must include the coefficient character in this averaging.

Knowing only κ(b)=κ(b₀), or a nonequivariant class without the equivariant lift, is not the stated justification. If the full ambient class is already fixed on a smooth upstairs space, one may first choose a standard first-order representative via the upstairs differential Hochschild/Čech comparison. This is a choice of equivalent presentation, not a computation of any fixed physical representative or higher jet.

After this normalization the scalar term is literally

    b_final=−8 ιπ α₀².

## 4. Inertia and strict group arrows

On a root stabilizer the classical line character can be −1. Its dlog is zero; disappearance from α does not mean the character has disappeared from the line. The inverse Morita bimodule retains the inverse line character and removes it from a module whose reduction is N⊗p*E. Neither the chart nor the central gauge alters this order-zero assertion.

With α₀ horizontal and b_final horizontal, their components on pure group arrows and on mixed group/Čech simplices vanish in an invariant presentation. The resulting first-order algebra action is strict in that presentation. This conclusion uses the b-normalization in Section 3. The original weak transported action cannot simply be declared strict before that step.

For a transported locally free module reducing to p*E, stabilizers act trivially on its reduced fiber. With a genuine strict finite-group action, characteristic zero, and the local flat deformation hypotheses, equivariant averaging of a lifted basis and Nakayama give an invariant basis near each stabilizer chart. Its invariant module is locally free over the invariant algebra, and reduction is compatible. This avoids the sign-character counterexample, whose nontrivial residual character violates this hypothesis. It proves no higher-order or mixed statement.

## 5. Actual invariant cochain descent

Use the stipulated canonical coefficient isomorphism jΩ=(1/8)Tr_p(−Ω), and apply the invariant local multiplication and arrows to pullbacks of downstairs functions. For this specific representative, the required identities are identities of regular coefficient-valued maps:

    jΩ(π(d p*f,d p*g)) = P(df,dg),
    jΩ(π(d p*f,α₀)) = D_P((1/2)dlog t)(f),
    jΩ(ιπ α₀²) = (1/4)(dlog t)².

They can be verified on the étale locus and extended as regular maps, once the given coefficient isomorphism and regularity are established. This is a direct computation of the invariant product, unary arrows, and scalar units. It does not assert an unrestricted ramified HKR isomorphism or use normalized trace as a multiplicative inverse to a branch factor.

The descended first-order cochain therefore represents

    (P, D_P(H/2), −2H²).

The scalar is −8 times 1/4. The local product still has the standard factor 1/2 in front of P.

## 6. Scope of acceptance

Accepted: the root-dependent gauge formula, its signs, its full-groupoid applicability given genuine linearization, and first-order invariant descent after the original scalar cocycle has been normalized in the full equivariant complex.

Not established by the two input reports alone: that an unspecified physical ambient actually has this full equivariant class and regular coefficient presentation; that an underlying square identity supplies the missing linearization; any fixed higher coefficient, mixed-order comparison, or preservation of a frozen physical representative.

Sources read: [research/hm/null-root-morita-inertia/root-morita-0719/RESULT.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/711c6bf8c6248f46d73661be8a42ede671a3712b/research/hm/null-root-morita-inertia/root-morita-0719/RESULT.md); [research/hm/null-root-characteristic/root-characteristic-0527/RESULT.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/47bce0703b1a78fb05a99541bab2168f4f2170c5/research/hm/null-root-characteristic/root-characteristic-0527/RESULT.md); [research/hm/null-ramification-guard/ramified-descent-0644/RESULT.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/2c387062518fec4044568fe638760343b87cc25f/research/hm/null-ramification-guard/ramified-descent-0644/RESULT.md). This audit is independent of the comparison report, whose final scalar-normalization argument is reviewed in §7 below.

## 7. Cross-check of the completed comparison

Subsequently read [research/hm/null-actual-pair-comparison/RESULT.md](RESULT.md) in full, together with [research/hm/null-effective-atlas/RESULT.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/d8d4a4a096431ad1506b0b847b72b0aeeeceda7f/research/hm/null-effective-atlas/RESULT.md) and [research/hm/null-invariant-coefficient-ideal/RESULT.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/64b6c62a23db6189186896285c956133608ad3c7/research/hm/null-invariant-coefficient-ideal/RESULT.md). The completed comparison supplies exactly the missing scalar normalization identified above. Its equation δ(se)=ρ(−15β²/8)−sb has the correct sign and normalization. The finite-pushforward/affine-Čech/exact-invariants argument proves the required quasi-isomorphism for the scalar coefficient sheaf; it makes no unjustified claim for the ramified Hochschild complex.

In particular, once existence of the coherent equivariant scalar cocycle is given, its full equivariant class is indeed uniquely determined by its invariant ordinary class. This follows from H^n_G(X,K)=H^n(X,K)^G for finite G in characteristic zero. Thus the comparison report legitimately uses the ordinary source scalar class together with the already supplied full equivariant presentation; no extra group-degree scalar ambiguity remains.

The direct formulas for the descended product, F_ij(f,η)=(f,η+df∧β_ij/2), and A_ijk=(1,−2β²_ijk) all check. Their tensor identities are regular everywhere, without inverting the ramification Jacobian. The invariant-ideal report supplies the needed coefficient identification across branch intersections.

The link to the independently constructed effective atlas is also justified by that report's actual choice-independence theorem. More explicitly, on each inverse-image affine U_i the normalized root-transported presentation is a strict algebra chart. Its regular module, transported back through the constructed Morita equivalence, supplies one of the equivariant rank-one original-ambient modules reducing to N allowed in the effective-atlas construction. The affine comparison theorem therefore compares this choice to its other auxiliary root modules and invariant generators. This is a comparison of actual internal Morita charts, not descent of the inter-ambient root line itself.

Final audit: ACCEPT the first-order comparison under its explicitly stipulated algebraic sheaf, coherent action, equivariant root-square, and source scalar-class premises. The earlier limitations concerning fixed higher representatives and mixed carrier existence remain unchanged. This audit checks the mathematics of the cited local results; it does not independently recertify the pinned physical source data.
