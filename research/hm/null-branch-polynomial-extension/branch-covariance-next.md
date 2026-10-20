# Branch covariance of the pure obstruction: fixed target, unresolved polynomiality

> Historical status: this is the initial denominator objection, not the final conclusion. The subsequent [extension proof](branch-boundary-extension.md) and [audit](branch-boundary-audit.md) close it under the stated premises. Its diagnosis is retained to document why smooth-locus homogeneity alone was insufficient.

19 October 2026. Formal mathematical record; no obstruction coordinates were evaluated.

## Verdict

There is a canonical parameter-independent deck-invariant target. There is also a concrete quadratic calculation for the raw bidifferential terms when their arguments are branch-independent base cochains. Neither fact establishes that the **complete pure obstruction class** is a homogeneous quadratic polynomial in the branch quartic.

The exact missing statement is a universal polynomial source comparison, including the actual root-line module, first-order lift, scalar primitives, and unary overlap corrections. The existing mixed comparison and uniqueness statements are only first-order/mixed statements. They do not supply this universal pure comparison. Thus the proposed quadratic representation-theoretic reduction is presently unproved, not disproved. A homogeneous regular class on the smooth branch locus can have discriminant denominators and violate the proposed restriction on torus weights.

## 1. The invariant target really is fixed

Let B=(P1)^4, let m:B→P4 multiply the four binary linear factors, and let p_F:X_F=C_F^4→B be the product double cover. Set f_F=m p_F and E_F=f_F*H⊗N_F, with the actual infinity-root line whenever infinity is a simple branch point. Let G=(Z/2)^4 be the independent deck group. Define

    M=m*End(H),      W=H²(B,M).

There is a canonical equality End(E_F)=p_F*M: the root line cancels in the endomorphism sheaf, not merely in its Chern character. The deck linearization induced by this description is canonical. Finite pushforward and the projection formula give

    H²(X_F,End(E_F))^G
      =H²(B,(p_{F,*}(p_F^*M))^G)
      =H²(B,M⊗(p_{F,*}O_XF)^G)
      =H²(B,M)=W.

Here p_{F,*} denotes finite pushforward and p_F^* denotes pullback. Taking invariants is exact in characteristic zero and (p_{F,*}O_XF)^G=O_B. These are canonical sheaf identifications, so there is no choice of periods, cohomology basis, or Gauss–Manin trivialization. The same argument applies to End₀ and to a family over the smooth parameter locus.

Consequently changing elliptic moduli does NOT itself prevent a fixed target. In a universal family the invariant relative cohomology is W⊗O_S. Singular covers still have the invariant-function identity, but extending the actual module and its quantization to them is a separate issue.

The diagonal binary D5 action on B and the audited HM action induce an actual action on M and W. Scalar ambiguities of an HM lift cancel in End(H). This is the correct ambient representation in which a branch-covariant pure class would live. It is not automatically either of the two retained mixed target spaces.

## 2. What is genuinely quadratic before solving or comparing anything

On a finite chart write C_F:y²=F(x) and

    V=y∂x+(F'/2)∂y,       L_F=F∂x²+(F'/2)∂x.

For a base function a, V²a=L_Fa. For a pair put D=V1⊗V2−V2⊗V1. On base functions a,b,

    mD²(a,b)=(L1 a)(L2 b)+(L2 a)(L1 b)
                 −2F(x1)F(x2)(∂1∂2a)(∂1∂2b).

This is homogeneous of degree two in the coefficients of F, with all coordinate differentiation included. It establishes the degree assertion for the raw μ_pp=mD²/8 on branch-independent base arguments.

Likewise, if a first-order odd cochain has the particular form u=y1 y2 U with U branch-independent, then u u is quadratic after y_i²=F(x_i). For example

    V1(y1 y2 U)=y2(F(x1)∂1U+F'(x1)U/2),

so μ_p(u,g) and μ_p(g,u) are quadratic when g is branch-independent and descended from the base. The same calculation applies to −μ_p(b,g) if b=y1 y2 B with branch-independent B. Factors such as x1−x2 do not change this degree accounting.

The square identity

    ((x1−x2)y1y2)²=Disc(q) Res(q,F)

has this same quadratic degree, because the resultant is degree two in the coefficients of F. It is evidence for the local degree accounting, not a replacement for the other terms.

These calculations do NOT show that the actual root-twisted transition matrices, normalized first lift, scalar cochains, and overlap operators admit these branch-independent forms on a common polynomial model. They deliberately state that additional hypothesis rather than bury it.

## 3. The full source that must be controlled

For either pure direction p, the source is

    R_pp = u_p,jk u_p,ij
         + μ_p(u_p,jk,g_ij)+μ_p(g_jk,u_p,ij)
         + μ_pp(g_jk,g_ij)+T_p,ij(g_jk)g_ij
         − b_p,ijk u_p,ik − (b_p,ijk²/2)g_ik
         − μ_p(b_p,ijk,g_ik),
    C_pp=g_ik^−1 R_pp.

It is the class of this entire expression in W that is at issue. The local formula in §2 covers only terms whose arguments have the specified branch-independent presentation. It does not prove a statement about T_p(g)g or remove root-frame derivatives from g. Nor does it prove that primitives used to obtain u_p or b_p are polynomial in the parameter.

The supplied compact pure lift is branch-independent and unique up to gauge in its first-order square-zero model. That helps identify the boundary. To establish the claimed polynomial pure class, one still needs a comparison into the actual root-twisted source **through the pure square**, or a polynomial replacement ambient with an identified first-order boundary to which the ambient-independence theorem applies.

Uniqueness does not supply a polynomial comparison: a unique solution on an open parameter locus can involve inverses of parameter polynomials. A fixed cohomology dimension also does not rule out those denominators. Conversely, denominators in one chosen primitive would not disprove polynomiality of the class, because they may cancel modulo boundaries. The necessary statement concerns the class, not a particular gauge.

The proved invariant characteristic-map vanishing eliminates changes of the second ambient jet after fixing and identifying the first-order structure and module boundary. It does not identify a branch-dependent first-order comparison, construct a universal second jet, or prove its polynomial extension. It can be used to finish a polynomiality proof only after such a replacement has actually been constructed.

## 4. Reversal and the actual two-torsion root discrepancy

Restrict to

    F=XY(A X²+BXY+C Y²),
    S={A C (B²−4AC)≠0}⊂A³.

The origin and infinity are distinct branch sections. On each smooth curve,

    div(x)=2P0−2P∞,
    L=O(P0−P∞),       L²≅O.

The line L is nontrivial: on an elliptic curve O(P−Q) is trivial only for P=Q. Binary reversal exchanges the two sections. Therefore it carries the chosen root N∞ to N0, and their quotient on the fourfold is the external product of these nontrivial two-torsion lines. It does not preserve N∞ literally.

This causes no ambiguity in W, because End(E⊗L)=End(E) canonically. But equality of target spaces is not an equivalence of the two module deformation problems. A source-level comparison is required.

There is a credible way to supply it for differential algebroids: a torsion line is trivialized by a finite étale μ2-torsor; in compatible étale frames its transitions are constants ±1. Differential products and overlap operators preserve constants, so twisting by those transitions preserves the complete module equation, including noncentral terms. Étale descent would then lift the torsion twist and act identically on End-obstructions. This argument is valid **if** the prescribed differential algebroid and comparison are extended functorially to this étale cover. It must be supplied for the actual source; it is not implied by the observation that End forgets N. It also does not by itself solve extension across the singular branch divisor.

In particular, do not claim a genuine reflection action on the original fixed-root source simply by cancelling N in End. The family action, root-twist equivalence, and all first-order identifications must be bound together.

## 5. Why homogeneity and smooth-family covariance are insufficient

Scaling F by λ is intertwined with y↦c y for c²=λ. Under this identification the pair bivector scales by λ, and its pure quadratic terms scale by λ². For a coherently identified first-order ambient and boundary, functoriality and the invariant ambient-independence theorem therefore support a degree-two scaling law for the obstruction. Without that identification this remains a conditional assertion, not a proof from V alone.

Even granting this law, regularity on S and full D5 covariance do not imply polynomiality on A³. For instance the scalar function B⁴/(AC) is regular on S, homogeneous of degree two, and D5-invariant, but is not a quadratic polynomial. More decisively, use the torus convention in which A,C have weights +1,−1 modulo five and reversal swaps A,C. The covariant

    Φ(A,B,C)=(A³/C, C³/A)

is regular on S and homogeneous of degree two. It is equivariant for the two-dimensional D5 representation with torus weights +4,−4 and reversal swapping the coordinates. At the original F0=(1,0,−1),

    Φ(F0)=(−1,−1),

which is reflection-even and nonzero. These are torus weights ±1 modulo five, outside 0,±2. This is a counterexample to deriving the proposed weight bound from homogeneity, smooth-family regularity, and equivariance alone. It is NOT a claim that the actual obstruction equals Φ.

## 6. Exact conditional theorem and next gate

A sufficient theorem would be the following.

There exists a class-valued polynomial map Q:U→W, U=span{X³Y,X²Y²,XY³}, homogeneous of degree two, whose restriction to S is the image of the complete actual pure source under the canonical invariant identification of §1. The map is D5-equivariant for the audited binary/HM actions, with the actual root-twist and parameter identifications included.

Equivalently, one needs a D5-equivariant linear map Sym²(U)→W representing the actual source. If this theorem holds, F0 lies in the ±1 torus-weight subspace, so Q(F0) lies in the sum of the weight 0,±2 subspaces of W. Since R F0=−F0 and Q is even, R Q(F0)=Q(F0). Hence

    Q(F0) ∈ (W_0 ⊕ W_2 ⊕ W_−2) ∩ ker(R−1).

This is a valid conditional target restriction. It is not a vanishing result: W has not been shown to have zero intersection with this subspace. The pure source targets W, not automatically the previously annihilated retained mixed targets.

One route to proving the missing theorem is to construct the entire source and an identified first-order boundary over the polynomial parameter ring C[A,B,C], before inverting A C (B²−4AC), with coefficients of total branch degree two after invariant normalization. A fixed acyclic base cover and the canonical cohomology identification then put its class in W⊗C[A,B,C]_2. Alternatively, prove that the smooth-family class has no poles along every component of the excluded divisor; degree-two homogeneity would then force polynomiality. Merely proving it away from that divisor is not enough.

The infinity section ceases to be the same smooth Cartier branch section at A=0, and the origin does so at C=0. Thus extending the original N∞ construction across the entire affine parameter space is a real geometric task, not automatic from the formula y²=F. A root-stack/Morita replacement might provide it, but requires the exact pure source comparison now missing.

## Evidence used

Read: [pure-square-next.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/b8903f211ef47802a9f701d9e74d3f67377022f2/research/hm/null-pure-square-reduction/pure-square-next.md), [pure-ambient-audit.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/b8903f211ef47802a9f701d9e74d3f67377022f2/research/hm/null-pure-square-reduction/pure-ambient-audit.md), [second-order-implication-audit.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/b8903f211ef47802a9f701d9e74d3f67377022f2/research/hm/null-pure-square-reduction/second-order-implication-audit.md), [retained-equivariance-next.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/43194f29b0f1b01dac1ef1cc92742359da5e6e34/research/hm/null-dihedral-mixed-vanishing/PROOF.md), [dihedral-ambient-audit.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/43194f29b0f1b01dac1ef1cc92742359da5e6e34/research/hm/null-dihedral-mixed-vanishing/AMBIENT-AUDIT.md), and the relevant character-audit statement. These provide the complete PR16 numerator, canonical fixed-carrier description, first-order compact uniqueness, mixed source comparison, and actual D5 action. No inspected report supplies the universal pure-square polynomial comparison above.

Conclusion: the target trivialization is proved; the raw degree calculation and root discrepancy are explicit; the proposed quadratic covariance theorem and its weight reduction remain conditional. This is an evidenced blocker to the suggested deduction, not evidence that pure-square polynomiality or vanishing is false.
