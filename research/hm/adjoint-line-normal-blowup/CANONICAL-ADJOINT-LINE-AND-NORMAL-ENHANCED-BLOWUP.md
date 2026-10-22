# The canonical adjoint line and its normal-enhanced resolution

## Result and established input

Let X=2Q=(q²=0), Q the actual integral rank-three quadric, and B=End_0(F). Write s,t for the negative linear coordinates, C=(s=t=0)⊂Q, Ω=Q\C and Ω_X=X\C. The closed subset removed is the same underlying conic; when an ideal is needed below, distinguish the multiplier ideal I=(s,t)⊂O_X from the reduced-center ideal (s,t,q).

Use the actual canonical multiplied family and its coherence theorem at commit 2e20281e6eb850904093af3a6c737f3ee0ed28f2:

- U_a∈H⁰(B_X(4)), U_a|Q=aN, and U_a²=0.
- κ≠0 and aU_b−bU_a=−(κ/2)q{a,b}N, where {a,b}=a_s b_t−a_t b_s.
- On D(s), z=t/s and q_s=q/s² give U_a=A(z−κq_s)U_(s²) for a=s²A(z).

These are credited inputs from ACTUAL-MULTIPLIED-NILPOTENT-COHERENCE-FIXES-ENDPOINT-SCALE.md, not new conclusions here. This note makes the next geometric construction:

1. The section family determines a canonical invertible abstract adjoint-line subsheaf on Ω_X, with nonzero infinitesimal Picard class. It cannot extend as an invertible sheaf over X.
2. Blowing up the multiplier ideal I does not resolve the deformed negative projection.
3. Blowing up J=I²+(q) does resolve it and supplies an invertible extension of the adjoint line on that modification.

No spinor kernel, subbundle of the adjoint, or extension to 3Q is asserted.

## 1. The family defines a genuine abstract line

Define M⊂B_X(4)|Ω_X as the image of A⊗O_Ω_X under a↦U_a. The cited factorization says M is generated on D(s) by U_(s²), and on D(t) by U_(t²). Let

    L=M⊗O_X(-2)|Ω_X.

Its local generators inside B_X(2) are

    n_s=U_(s²)/s²,       n_t=U_(t²)/t².

Each is an injective image of O_Ω_X. Indeed, if f n_s=0, reduction modulo q gives f_0 N=0. Since Q is integral and N is a nonzero section of a locally free sheaf, f_0=0. Thus f=qg locally. The equality qg n_s=0 identifies in the square-zero ideal with g_0 N=0, hence g_0=0 and f=0. This argument remains valid at zeros of N; no nowhere-vanishing assertion is used.

The coherence equation gives

    n_t=(1−2κq/(st))n_s.                            (1)

The factor is a unit because q²=0. Hence L is an invertible O_Ω_X-module and an abstract line subsheaf of B_X(2). It need not be a subbundle: its quotient in the adjoint need not be locally free. Its reduction is the trivial abstract line O_Ω, embedded by N.

This construction uses the full image of A and is consequently independent of a chosen binary basis. Its sections are square-zero adjoints, by the cited pair-product theorem or directly by the local generator squares.

## 2. Its Picard class is nonzero

The square-zero ideal of Ω in Ω_X is O_Q(-2)|Ω. The exact units sequence is

    1→1+O_Ω(-2)→O_Ω_X^*→O_Ω^*→1.

In the frame convention n_t=g_st n_s, equation (1) gives the infinitesimal class

    [L]=−2κ[1/(st)] ∈ H¹(Ω,O_Ω(-2)).               (2)

This class maps injectively into Pic(Ω_X). In fact Hartogs on the normal projective Q gives H⁰(Ω,O_Ω)=C; its units C* lift as constants, so the preceding connecting homomorphism from global units is zero.

To verify that [1/(st)] is nonzero, use the homogeneous coordinate ring

    R=(C[V]/(q))[s,t].

The affine opens D_+(s),D_+(t) cover Ω. Their Čech group for O(-2) is the degree −2 part of

    R_(st)/(R_s+R_t).

The Laurent monomial s^(-1)t^(-1) cannot be a sum of an element with nonnegative t-exponent and an element with nonnegative s-exponent. Laurent monomials are independent over C[V]/(q). Thus its class is nonzero. Since κ≠0, L is nontrivial.

## 3. No invertible extension over X

Suppose an invertible sheaf Lbar on X restricts to L. Its restriction to Q is trivial on Ω. Normality of Q and codimension(C,Q)=2 imply that an isomorphism with O_Ω extends uniquely between the two rank-one reflexive sheaves on Q; hence Lbar|Q≅O_Q.

But H¹(Q,O_Q(-2))=0. For example, use

    0→O_P4(-4)→O_P4(-2)→O_Q(-2)→0

and the intermediate cohomology vanishing of projective space. The global square-zero units sequence therefore makes Pic(X)→Pic(Q) injective. It follows that Lbar≅O_X, contradicting the nontriviality of L on Ω_X.

Consequently the globally defined coherent image sheaf

    im(A⊗O_X(-2)→B_X(2))

restricts to L but cannot be invertible everywhere over C. This is an obstruction for the adjoint line itself, stronger than merely observing that the local scalar-divided adjoints do not agree. It is not a statement about the kernel of a nilpotent endomorphism.

## 4. The two negative projections

Let p:Ω_X→P¹ be the original negative projection and p':Ω_X→P¹ the deformed one from the coherence theorem. On D(s), their affine coordinates are

    z=t/s,       z'=z−κq_s.

Using the unoriented opposite coordinate w=s/t, their coordinates on D(t) are

    w=s/t,       w'=w+κq_t.

The opposite correction has a plus sign. Since q_t=q_s/z²,

    (z−κq_s)(w+κq_t)=1

on the overlap, using q²=0. The frames of O_P¹(2) change by z² or (z')². Equation (1) therefore identifies

    L ≅ (p')*O_P¹(2) ⊗ p*O_P¹(-2).                (3)

This fixes the direction of the ratio, rather than identifying L only up to its dual.

## 5. The ordinary multiplier blowup is insufficient

Consider Bl_I(X), where I=(s,t). This is the blowup of the multiplier ideal, not the blowup of the reduced center with ideal (s,t,q).

Near any point of the smooth conic C, q is a regular ambient parameter. In local étale or completed coordinates, the s-chart of this blowup has ring

    C[r,s,z,q]/(q²),       t=sz.

Here r is a local coordinate along C. The element s is a non-zero-divisor, and q is not divisible by s². The proposed coordinate of p' on the complement of the exceptional divisor is

    z−κq/s².

If p' extended to this chart, its reduction would equal the ordinary negative projection z, by equality on a dense open of the integral reduced chart. Its image therefore lies in the affine z-coordinate target chart. A regular extension g would satisfy

    s²(g−z)=−κq.

Reducing modulo s contradicts q≠0 in the chart ring/(s). Thus p' does not extend across any point of this exceptional chart. The ordinary multiplier blowup resolves p but not p'.

## 6. A normal-enhanced blowup resolves both projections

Set

    J=I²+I_(Q/X)=(s²,st,t²,q)⊂O_X,
    π:Y=Bl_J(X)→X.

This ideal is intrinsic: q denotes the image of O_X(-2) under the fixed quadratic equation, and rescaling that equation by a unit does not alter J. Away from C, J=O_X, so π is an isomorphism over Ω_X.

The Rees generator qT is nilpotent, since (qT)²=0, and contributes no Proj chart. The st-chart is covered by the s²- and t²-charts because (stT)²=(s²T)(t²T). Hence those two charts cover Y.

On the s²-chart the affine chart ring of the Rees construction embeds in the localization at the regular element s. Its regular coordinates include

    z=t/s,       η=q/s²,
    t=sz,        q=s²η,       η²=0.

In the same étale or completed local coordinates near C, its chart ring is C[r,s,z,η]/(η²), with the corresponding localization or completion understood. This follows directly by substituting into the Rees subalgebra; there is no discarded nilpotent chart or selected point computation. The analogous t²-chart has w=s/t and η_t=q/t². On their overlap,

    w=1/z,       η_t=η/z².

Thus p and p' extend to Y with respective chart coordinates

    p: z and w,
    p': z−κη and w+κη_t.

The reciprocal identity from Section 4 is regular on this overlap. The reduced space Y_red is Bl_(s,t)(Q), since blowing up I² and I gives the same reduced blowup, and the local charts above retain the stated square-zero normal direction.

Define

    Ltilde=(p'_Y)*O_P¹(2)⊗(p_Y)*O_P¹(-2).

This is an invertible extension of L to Y. Unlike an extension to X, it is possible because the normal direction has been modified: q/s², rather than q alone, is regular in the exceptional chart. The following final step extends the abstract adjoint-line embedding as well; it does not produce a subbundle or a spinor kernel.

## 7. The abstract adjoint-line embedding also extends

Locally choose a trace-free lift Ñ of N to X. Since U_(s²) reduces to s²N, write

    U_(s²)=s²Ñ+q X_s.

Here X_s is a section on Q, and any local lift can be used in the displayed expression. On the s²-chart of Y, define

    ntilde_s=π*Ñ+η π*X_s.

This is regular and satisfies s²ntilde_s=π*U_(s²). It is independent of the auxiliary lifts: changing X_s by qY contributes ηqY=s²η²Y=0; changing Ñ by qZ changes X_s by −s²Z and cancels exactly. Equivalently uniqueness follows by the regularity of s. The analogous construction applies on the t²-chart.

Their unit transition is

    ntilde_t=(1−2κη/z)ntilde_s.

It follows either from the coherence identity or by uniqueness from the dense complement of the exceptional divisor. It is the transition of Ltilde from Section 6. Thus these generators define a homomorphism Ltilde→π*B_X(2).

The reduction of each generator is the nonzero pulled-back section N on the integral Y_red. The square-zero ideal of Y_red is locally invertible over Y_red, as the chart η²=0 shows. The same two-step annihilator argument as in Section 1 therefore proves injectivity. Moreover s⁴ntilde_s²=π*(U_(s²)²)=0, and s is a non-zero-divisor, so ntilde_s²=0; likewise on the opposite chart.

Consequently the canonical adjoint line extends on Y as an invertible abstract subsheaf with square-zero generators. Its embedding can still vanish on fibers, and its quotient need not be locally free. No rank-one kernel of F, flat spinor sheaf, or line subbundle is inferred.

## Contribution and limits

The construction turns the multiplied-lift coherence into an intrinsic nontrivial adjoint line on the punctured double quadric, proves why that line cannot extend over the original endpoint, and gives an explicit proper modification on which its projective geometry does extend. It distinguishes the insufficient multiplier blowup from the required normal-enhanced ideal. It does not carry out the next cohomological division, extend to 3Q, or evaluate any fourth obstruction. All local coordinates are universal charts; no selected actual source instance or numerical rank computation is used.

## Immutable source and verification

The sole new coherence input is the complete actual theorem at:
https://github.com/Akilleez-QA/read-em-and-weep/blob/2e20281e6eb850904093af3a6c737f3ee0ed28f2/research/hm/order-four-quadratic-load/ACTUAL-MULTIPLIED-NILPOTENT-COHERENCE-FIXES-ENDPOINT-SCALE.md

Run `python verify_adjoint_line_resolution.py`. Its bounded symbolic checks verify the reciprocal chart identity, line transition and inverse, normal-enhanced Rees-generator identities, and the ordinary-blowup divisibility obstruction. The Picard, Hartogs, local-ring and injectivity arguments are geometric proofs above, not claims delegated to the finite verifier. No actual-source coefficients or rank tests occur.
