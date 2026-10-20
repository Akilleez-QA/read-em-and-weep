# Pure-square reduction: the weight-zero characteristic map is zero

## New result

For the actual carrier `X=C^4`, `C:y²=x³−x`, `E=f*H⊗N`, the characteristic map vanishes on the entire deck-invariant Hochschild group:

`ev_E : HH²(X)_0 → Ext²(E,E)_0` is zero.

Consequently, changing second-order ambient coefficients while keeping the first-order ambient and module boundary fixed cannot change the pure-square obstruction class. This is stronger than the earlier observation that such changes *might* affect weight zero: for this particular geometric carrier, they do not. It does not prove that the pure-square obstruction itself is zero.

With the imported vanishing of the mixed component, the fixed-boundary diagonal problem and the problem allowing arbitrary second-order ambient changes have the same necessary weight-zero condition:

`o_even := [C_PP+C_QQ] = 0`.

In fact, once mixed vanishing is admitted, this condition is sufficient for existence for the original fixed two-jet, on an acyclic algebraic refinement. Thus adjustable ambient coefficients provide no additional existence cases for this boundary. For the two-parameter total-degree-two lift, the same statement holds separately for `[C_PP]` and `[C_QQ]`.

## 1. Exact calculation of the possible ambient correction space

Let `G=(Z/2)^4` act by `y_i↦−y_i`. The source supplies a nowhere-zero vector field `V_i` of character `χ_i` on each elliptic factor. By Serre duality, `H¹(O_C)` has the same nontrivial character as `dx/y`. Therefore

- `H⁰(Λ²T_X)` has characters `χ_iχ_j`, `i<j`;
- `H²(O_X)` has characters `χ_iχ_j`, `i<j`;
- `H¹(T_X)=⊕_{i,j} C(V_i⊗ε_j)` has character `χ_iχ_j` on the displayed summand, where `ε_j` spans `H¹(O_{C_j})`.

The equivariant HKR decomposition in PR16 therefore gives

`HH²(X)_0 = ⊕_{i=1}^4 C κ_i`, with `κ_i=V_i⊗ε_i`.

There are no bivector or scalar-gerbe directions of weight zero. The only candidates are the four independent complex-structure deformations of the elliptic factors. This calculation concerns the geometric upstairs carrier, not the auxiliary compact pair plane.

## 2. Actual geometric extensions kill all four evaluations

The pinned carrier is not an arbitrary bundle having the same Chern classes. It is expressly

`E=f*H⊗N`, `N=O_X(Σ_i {∞}_i)`,

with `f` the product of the four degree-two x-maps followed by `(P¹)^4→Sym⁴(P¹)=P⁴`.

Deform the ith factor by the smooth family, near `t=0`,

`C_t : y²=x(x−1)(x+1−t)`.

Its four ordered branch points are `0,1,−1+t,∞`, and it retains the section `∞` and involution `y↦−y`. The x-map is a relative degree-two map to the fixed P¹. Keep the other three factors unchanged. On the resulting product family `𝓧_i`, define the relative line bundle `𝓝_i` by the four infinity sections and the relative map `𝓯_i` by multiplication of the four binary linear factors. Then

`𝓔_i = 𝓯_i*H ⊗ 𝓝_i`

is a vector bundle extending exactly the original `E`. This uses no new HM deformation or quantization theorem: pullback and tensor product of a fixed locally free bundle remain locally free. The construction is also compatible with the deck involutions.

The Kodaira–Spencer class of `C_t` is nonzero. Infinitesimally, the ordered branch cross-ratio changes; a PGL₂ vector field fixing `0,1,∞` is zero, so it cannot produce this movement of the fourth branch point. Equivalently this is the local parameter on the moduli of elliptic double covers with ordered branch points. Extra automorphisms at `j=1728` only ramify the coarse j-map; they do not annihilate this marked-family Kodaira–Spencer class. The fixed infinity section makes the degree-two map the complete linear series `|2∞|`, so this is not merely a change of map on a fixed marked elliptic curve. Since `H¹(T_C)` is one-dimensional, its nonzero Kodaira–Spencer class spans that space. The product-family class is consequently a nonzero multiple of `κ_i`.

The characteristic evaluation of a Kodaira–Spencer class is precisely the obstruction to extending `E` over that first-order deformation, equivalently contraction of its Atiyah class. The explicit extension `𝓔_i` proves `ev_E(κ_i)=0`. Linearity proves the asserted vanishing on all `HH²(X)_0`.

This argument proves vanishing of the full End-valued characteristic class, not merely its trace. Determinant triviality alone would not have sufficed.

## 3. Consequence for the complete PR16 numerator

Retain the actual pure source, with no dropped noncentral terms:

`R_pp = u_p,jk u_p,ij + μ_p(u_p,jk,g_ij) + μ_p(g_jk,u_p,ij)`

`        + μ_pp(g_jk,g_ij) + T_p,ij(g_jk)g_ij`

`        − b_p,ijk u_p,ik − (b_p,ijk²/2)g_ik − μ_p(b_p,ijk,g_ik)`.

Set `C_pp=g_ik⁻¹R_pp`. For two ambient two-jets agreeing to first order, PR16 §8 identifies the change of the second-order module obstruction with `ev_E([η])`, where `η` is their total Hochschild two-cocycle difference. Since the characteristic map is deck-equivariant,

`pr_0 ev_E([η]) = ev_E(pr_0[η]) = 0`.

This holds even when the new ambient correction is not equivariant: it can introduce pair-character components, but it cannot cancel a nonzero invariant obstruction. In a deck-equivariant two-parameter problem apply this independently to the `s²` and `t²` coefficients. Their allowed weight-zero ambient differences have zero characteristic image.

Thus there is an exact source-specific exclusion of a proposed shortcut: neither a new scalar gerbe coefficient, a new bivector, nor a diagonal Kodaira–Spencer coefficient can repair a nonzero `o_even`. The first two have no invariant HH² component; the last four have zero evaluation by the actual family above. A literal representative may change by a Čech boundary, so this does not assert equality of raw numerators.

## 4. Scope and next target

The first-order module boundary remains fixed. Allowing arbitrary non-equivariant Ext¹ changes is a different problem: their quadratic and cross terms may alter the invariant obstruction and are not eliminated here. For the stipulated pair-character boundary, the imported pair-character Ext¹ vanishing already supplies uniqueness up to gauge.

The formal branch-cross-ratio family is a proof device for the characteristic map, not an allowed replacement of the original quantization. It does not identify an odd-ideal square with a branch sextic, make the full pure ambient D5-invariant, or prove the invariant obstruction vanishes. Those are separate possible routes. The reduced remaining task is to annihilate or detect the canonical invariant quadratic class itself, with both `T_p(g)g` and `−μ_p(b_p,g)` retained; changing only the second ambient jet cannot evade it.

## Pinned sources read

1. PR16 full source, especially §§1, 5, 8–9, commit `c8aec970fd65a105f39f4e8aeb8a17f0f0053f89`, blob `a58834ab61e18a5dedd8a7bf20bec7121bfa9165`:
https://github.com/Akilleez-QA/read-em-and-weep/blob/c8aec970fd65a105f39f4e8aeb8a17f0f0053f89/research/hm/second-order-algebroid.md

2. Actual carrier `E=f*H⊗N`, degree-two x-maps and infinity divisor, commit `3bdc6cb28ecd75cfefb3cb0d85f42d5bcde8cc7f`, blob `fc0b0c7cf512d93c7a4ea976f986b7332b926f51`:
https://github.com/Akilleez-QA/read-em-and-weep/blob/3bdc6cb28ecd75cfefb3cb0d85f42d5bcde8cc7f/research/hm-carrier-and-atlas.md

The zero characteristic-map result above is a new formal deduction from these actual geometric data, not a claim already made in either source. The supplied mixed-vanishing and source-comparison premises remain imported.

## Addendum A: first-boundary independence under an additional ordinary smoothness premise

This is conditional on the separately established premise: every `z∈Ext¹(E,E)` admits an ordinary commutative second-order module deformation (for example, a smooth family whose Kodaira–Spencer map surjects onto all Ext¹). A family of dimension 87 alone is not enough without this tangent-surjectivity statement. It is not needed for the ambient-independence result above.

Write `u=u_P+u_Q` and change it to `u+w`, where `z_ij=g_ij⁻¹w_ij` is an End-valued Čech one-cocycle. Direct subtraction in the complete PR16 numerator, without assuming u is closed, gives

`ΔR = w_jk u_ij + u_jk w_ij + w_jk w_ij`

`     + μ₁(w_jk,g_ij) + μ₁(g_jk,w_ij) − b_ijk w_ik`.

All `T(g)g`, `μ₂(g,g)`, `b²g/2`, and `μ₁(b,g)` terms cancel in this difference because the ambient and classical g are unchanged. The linear terms have the character of w plus P or Q. Modulo an ordinary first-order gauge, choose representatives for z in the nonzero Ext¹ characters; by the imported pair-character Ext¹ vanishing none has character P or Q. Hence no linear term contributes to weight zero. This uses actual character-homogeneous cochains and does not mistake u for a cocycle.

The only remaining invariant variation is the invariant projection of `g_ik⁻¹ w_jk w_ij`, the ordinary quadratic obstruction of z. The additional ordinary smoothness premise makes that entire cohomology class zero. Therefore the pure invariant class is also independent of arbitrary first-order module choices under this premise. Exact pieces discarded in choosing z representatives correspond to reduction-preserving gauges and do not change the obstruction class. No stronger first-boundary independence is claimed without the premise.

## Addendum B: independent check of the proposed branch-square formula

On the finite pair chart let `e₁=x₁+x₂`, `e₂=x₁x₂` and `a_odd=(x₁−x₂)y₁y₂`. Direct symbolic multiplication using the defining curve gives

`a_odd² = (e₁²−4e₂)e₂[(e₂+1)²−e₁²]`.

Indeed `(x₁³−x₁)(x₂³−x₂)=e₂[(e₂+1)²−e₁²]`. Also the pair Poisson bracket gives `{e₁,e₂}=a_odd`, so this is the actual coefficient appearing in the first-order product of symmetric base functions, not a guessed section. With `q=aX²+bXY+cY²`, the homogenization is

`Δ(q)=(b²−4ac)ac[(a+c)²−b²]`.

The factor `ac[(a+c)²−b²]` is, up to the fixed resultant convention, `Res(q,XY(X²−Y²))`, because it is the product of q evaluated at the four branch points. The discriminant supplies the remaining factor. This proves the branch-sextic identity with its stated convention.

Crucial descent qualification: `a_odd` has pair-deck character χ12 but is anti-invariant under interchanging the two elliptic factors. It is therefore not a function on the ordinary symmetric quotient. Its use as the canonical odd coefficient requires the sign-twisted, canonical-form, or parameter-compensated pair presentation. The pullback identity `de₁∧de₂=(x₁−x₂)dx₁∧dx₂` records precisely this sign. For an action assigning the quantization parameter the opposite swap sign, `h a_odd` is invariant and `(h a_odd)²=h²Δ`.

Under the displayed D5 torus action `(a,b,c)↦(ζ⁴a,b,ζ⁻⁴c)`, both `b²−4ac` and `ac` are invariant. The three pieces of the bracket are `a²` of weight ζ³, `2ac−b²` of weight one, and `c²` of weight ζ². Their products with `(b²−4ac)ac` are nonzero polynomials, so the fixed Δ is not invariant. Reversal exchanges the two nontrivial pieces. Thus the multiplication of this sign-twisted coefficient into the even pure-square piece depends on the fixed branch data and does not inherit the mixed square-zero D5 symmetry. This does not by itself show that the full pure obstruction is multiplication by Δ: differentiated terms and source comparisons still have to be included.
