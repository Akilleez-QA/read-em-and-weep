# The actual leading first-normal scalar is the canonical source correction

## Result and scope

In the fixed actual harmonic frame of PR692/713/716, write the leading first-normal coherence as

    P=A n,   M=A T+s0 n+B1(A,n),   A=a²h.

Here n has weight eight, T weight four, a is the negative quadratic (a unit over k=C(L)), and h has binary positive degree four. For the canonical actual ladder, the previously unspecified scalar is exactly

    s0 = -a L_can(a,h).                                      (1)

This identifies s0 as a symbolic source operation. It assigns no actual coefficient or source value and performs no actual point, derivative or rank evaluation. It does not prove the fourth-square class vanishes. In particular, the local first-normal factor must NOT be simplified to F=A: the canonical negative source correction survives at precisely the relevant weight.

## Pinned inputs

All three following source definitions are read at commit 8d8b5be4ce62c3055bb53be9e16d29cc63072f04, under research/hm/order-four-quadratic-load/:

1. [ACTUAL-FOURTH-BOCKSTEIN-AS-A-FIFTH-NEIGHBORHOOD-ADJOINT-BOUNDARY.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/8d8b5be4ce62c3055bb53be9e16d29cc63072f04/research/hm/order-four-quadratic-load/ACTUAL-FOURTH-BOCKSTEIN-AS-A-FIFTH-NEIGHBORHOOD-ADJOINT-BOUNDARY.md), fixed input and §2: b=L_can(a,h), with a,h,b sections of O(2), and

       J3=(ah-qb)U_a-q² C_h.

2. [ACTUAL-MULTIPLIED-NILPOTENT-COHERENCE-FIXES-ENDPOINT-SCALE.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/8d8b5be4ce62c3055bb53be9e16d29cc63072f04/research/hm/order-four-quadratic-load/ACTUAL-MULTIPLIED-NILPOTENT-COHERENCE-FIXES-ENDPOINT-SCALE.md), §§3–4: on a negative chart with coordinates (r,t), z=t/r, q_r=q/r², a=r² α(z),

       U_a=α(z-κq_r)U_(r²),    N_r=U_(r²)/r².

   These are exact induced section identities modulo q², including at zeros of the generator. No division by N_r is involved.

3. [ACTUAL-CANONICAL-RAW-CUBIC-HAS-A-NONZERO-LINEAR-LIFTING-CORRECTION.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/8d8b5be4ce62c3055bb53be9e16d29cc63072f04/research/hm/order-four-quadratic-load/ACTUAL-CANONICAL-RAW-CUBIC-HAS-A-NONZERO-LINEAR-LIFTING-CORRECTION.md), §§1–2,6: L_can is the unique sheaf factorization T_raw=β2 L_can, and takes values in the negative quadratic representation A_neg=Sym²W. It is polynomial and linear in the direction a, and linear in h. In invariant representation notation L_can(a,h)=γ S_h(a), with γ nonzero but not assigned here.

The harmonic/filtered input is [PR692 at 858f96ba1539afb1293f31239b8761af08e46f60](https://github.com/Akilleez-QA/read-em-and-weep/blob/858f96ba1539afb1293f31239b8761af08e46f60/research/hm/vertex-scalar-filtration/PROOF.md), research/hm/vertex-scalar-filtration/PROOF.md, §§1–2. [PR713 at 5b3943980ecaef78ee7f56fbc015d40955fb24f0](https://github.com/Akilleez-QA/read-em-and-weep/blob/5b3943980ecaef78ee7f56fbc015d40955fb24f0/research/hm/leading-vertex-obstruction/PROOF.md) and [PR716 at 2a602d811b904def02bd56518fb0549e2911ff3e](https://github.com/Akilleez-QA/read-em-and-weep/blob/2a602d811b904def02bd56518fb0549e2911ff3e/research/hm/firstnormal-trace-variation/PROOF.md) identify precisely the above leading P,M and their role in the fourth-square class. [PR729 at c384ae419983a5031af19c37674df020de1aa5da](https://github.com/Akilleez-QA/read-em-and-weep/blob/c384ae419983a5031af19c37674df020de1aa5da/research/hm/firstnormal-scalar-slope/PROOF.md) supplies the scalar-slope theorem cited below.

The letter r is a chart coordinate only, avoiding collision with s0. The symbol α′ below denotes the formal derivative of an arbitrary quadratic in a negative chart, not evaluation of actual source derivatives.

## 1. Exact scalar before taking a leading weight

Expand the exact coherence identity modulo q². Since α is quadratic,

    r² α(z-κq/r²)=a-κq α′(z) mod q².

Consequently

    U_a=(a-κq α′(z))N_r mod q²,
    J3|2Q=F_r N_r,
    F_r=(ah-qb)(a-κq α′(z)) mod q²
       =a²h+q[-ab-κah α′(z)] mod q².               (2)

This is a product of scalar functions multiplying an actual section. The q² C_h term disappears on 2Q, so neither an unknown primitive nor its choice enters (2). The equality is stronger than division in a fraction field: all scalar functions are regular on the negative chart and the source identity already holds as sheaf morphisms.

Use the physical positive representative h in D5, which is the harmonic quadratic in positive ambient coordinates and has binary degree four on Q. Explicitly, positive ambient quadratics split as the harmonic D5 summand plus the invariant line kq. The fixed D5 inclusion has zero kq component: its harmonic normal coefficient is zero. Adding q times a scalar would change that prescribed ambient source and is not an allowed reinterpretation of h here. Negative-coordinate functions a,b,α′ are independent of the positive binary variables and of q. The harmonic coefficient product with any such negative function has no positive harmonic correction: B_j(c,H)=0 for j>0 when c is independent of the positive variables. This agrees with the degree-zero-factor vanishing in [the pinned universal harmonic-product theorem, §1](https://github.com/Akilleez-QA/read-em-and-weep/blob/8d8b5be4ce62c3055bb53be9e16d29cc63072f04/research/hm/order-four-quadratic-load/UNIVERSAL-SECOND-NORMAL-HARMONIC-PRODUCT-AND-OPERATOR-DEFECT.md). Thus (2) is also the harmonic scalar coefficient decomposition relevant to PR716; there is no concealed B1(a,ah) contribution.

Now b=L_can(a,h) belongs to A_neg, not the positive source space. Although it depends linearly on the abstract input h, its VALUE is a negative quadratic: it has binary positive degree zero. Source parameter degree and positive-coordinate degree must not be conflated. Therefore

    (-ab)_0=-ab,   (-κah α′)_0=0.

Taking degree zero of F_r,1 proves (1). The connection correction in (2) starts in degree four and first affects the weight-twelve part of L1, not M=(L1)_8.

## 2. Chart and completion independence at the required weight

On the opposite volume-compatible negative chart w=-r/t the exact coherence supplies its corresponding scalar F_t. The same argument there gives its degree-zero first coefficient -ab in that physical frame. More intrinsically, the coherence theorem gives

    N_t-N_r=-2κ q N/(rt) mod q².

This changes the first-normal matrix coefficient by a scalar multiple of n_full, which starts at weight eight; hence it does not change T4. The compensating change in F1 is a negative rational function times A=a²h, and therefore has positive binary order four. It cannot change s0. The statement is tensorial under the fixed physical trivializations; no determinant or equation-line unit is suppressed.

Likewise the full actual higher filtered terms of N_r cannot alter the displayed leading P,M: n_full starts at eight, T_full at four, and harmonic B1 lowers weight by four. This is the established filtered estimate of PR692, not a replacement of the actual source by a homogeneous model.

## 3. A source-operation description without normalization guessing

Equation (1) can equivalently be written

    s0(a,h)=-a [the unique A_neg-valued factor of T_raw through β2](a,h).

The uniqueness is sheaf-theoretic, including exceptional fibers; it does not involve inverting a selected minor. In the invariant symmetric-endomorphism description from the pinned source theorem,

    s0(a,h)=-γ a S_h(a).                              (3)

The scalar γ is the already fixed actual normalization of L_can. Formula (3) does not set it to one, recover it from representation dimensions, or identify an arbitrary Schur gauge with the canonical one. For another compatible ladder with source correction b′, precisely the same proof yields s0′=-ab′. Transporting b′ to L_can remains required before applying (1) to that ladder.

For fixed nonzero a, the known surjectivity h↦L_can(a,h) implies that h↦s0(a,h), regarded as a negative quartic, has image a A_neg. This is a consequence of the source-operation theorem, not a new instance rank test. In particular the scalar term is not identically absent from the family. No claim that it is nonzero for every h is made.

## 4. Exact separation of the remaining scalar compatibility

Let V=(k[X,Y]/(f3))8 and d=[d2]∈V. PR729 proves dim V=3, d≠0, and, for the immutable local fourth-square class K,

    K(s0+λ)=K(s0)+a λ d.

The comparison also shifts R by λT and keeps n,T,A fixed; these are abstract local solutions, not claimed global completion freedoms. Define K0 by the same local equation with zero scalar coefficient, equivalently by replacing M by M-s0n and R by R-s0T. The same theorem guarantees that this is a valid local q² square solution and that K0 is independent of its R choice. Then the actual source identification gives the exact compatibility equation

    K_actual = K0 - a² L_can(a,h) d.                 (4)

Thus the three-dimensional necessary immutable-class gate separates as follows:

- The image of K0 in V/kd (dimension two) must vanish.
- If it does vanish, there is a unique coefficient τ with K0=τd; the remaining actual scalar compatibility is τ=a²L_can(a,h).

This is not an evaluation or proof of either condition. It does show precisely why tuning an abstract scalar is not an actual solution: the scalar is already fixed by the canonical raw-cubic source operation. It also identifies the two-dimensional test independent of the scalar first-normal coefficient s0 (but not of A=a²h or the source h), and the subsequent normalized scalar equality, with all signs fixed by the actual ladder. Even their fulfillment addresses only this immutable quotient; the full square-ideal class and later Bockstein/algebraicity gates must not be conflated with it.

## Verification and boundary

The companion bounded verifier checks the scalar expansion with free symbols, the exact polynomial Taylor identity modulo q² for an unspecified quadratic, the positive-degree separation, and the slope substitution signs. It neither loads nor evaluates actual HM coefficients or source instances. The central proof is the exact source/coherence comparison (2), not a numerical check. No large computation, selected model, or Gauss/identity-W analysis was performed.
