# A transition-only scalar solver for the compensated first lift

## Result and scope

There is an exact alternative first-order lift using only the physical rank-two row transitions, the prescribed gerbe cocycle, and scalar Čech operations. It avoids evaluating the four-block splitting-connection trace. It is defined on the common refinement of the carrier/line and standard product covers.

This is a formula-level alternative, not an executable improvement: it requires a new resource preflight. No polynomial values, partition expansions, jets, residual evaluations, or new second-order source were generated. No arithmetic execution is authorized by this note.

The alternative is first-order gauge equivalent to the pinned lift. Consequently it preserves its entire second-order obstruction class for the fixed ambient two-jet, with induced order-two gauge terms retained. No vanishing or value of that class is established.

All public sources below are pinned to commit `08b73637d4136f91606aad332c46cafd064417f8` in `Akilleez-QA/read-em-and-weep`.

## 1. The exact scalar problem left by rank two

Fix one pair `(a,b)=(1,2)` or `(3,4)`. Use the physical determinant-one row transitions, with

`g_ik = g_jk g_ij`,

`mu_ab(F,G) = (V_a(F)V_b(G)-V_b(F)V_a(G))/2`,

`b_ab,ijk = (15/4) q_a,ij q_b,jk`.

Matrix order is as written. Define

`C_ab,ijk = g_ik^-1 mu_ab(g_jk,g_ij)`,

`K_ab,ij = mu_ab(g_ij^-1,g_ij)`,

`F_ab,ijk = b_ab,ijk - tr(C_ab,ijk)/2`.

For row-End cochains use

`(delta x)_ijk = g_ij^-1 x_jk g_ij - x_ik + x_ij`.

The pinned first-order source proves, using only the two-by-two identity
`[Q,P]=2QP-tr(QP)I` for traceless `P,Q`, that

`delta K_ab = 2 C_ab - tr(C_ab) I`.

Thus, for any scalar cochain `s_ab` satisfying `delta s_ab=F_ab`,

`x_ab = s_ab I - K_ab/2`,

`u_ab = g x_ab`

solves the actual first-order equation

`delta x_ab = b_ab I - C_ab`.

The scalar equation must be solved. Rank two does not permit setting `s_ab=0`: that would require the additional cochain identity `tr(C_ab)=2b_ab`, which neither the first-order rank theorem nor the pinned construction asserts.

### Closure checked directly

Write `A=g_ij`, `B=g_jk`, `D=g_kl`. Multiplying the row-End Čech differential of `C_ab` on the left by `DBA` gives

`mu_ab(D,B) A - mu_ab(D,BA) + mu_ab(DB,A) - D mu_ab(B,A) = 0`.

This is exactly minus the Hochschild cocycle identity for the bidifferential `mu_ab`. Hence `delta C_ab=0`. Taking trace removes the conjugations. Since the `q_a` are scalar Čech cocycles, `delta b_ab=0`, so

`delta F_ab=0`.

No order-two residual or finite-model oracle enters this proof.

## 2. Cover and scalar pole domain

Let `V` be the pinned six-carrier, sixteen-line-mask cover, `U` the sixteen standard product charts on `Y=(P1)^4`, and `B` their common refinement. Write `r:B->U`, `s:B->V`, and `f_ab=s*F_ab`.

Order common vertices by the original source vertex first and standard vertex second. Then `s` preserves the order, with possible repetitions. On increasing common triples its pullback of `F_ab` is exactly the expression obtained from the pulled-back physical transitions and gerbe. Repeated source vertices are adjacent and give zero for both `C_ab` and `b_ab`. This ordering is essential: the nonlinear source is not re-evaluated after an arbitrary permutation. The linear alternating-cover maps involving `r`, `Pi`, `A`, `S`, and `K_cov` do not require `r` to preserve the order.

The pair character identifies scalar cochains with sections of

`L_ab = O(n_1,n_2,n_3,n_4)`,

where `n_a=n_b=-2` and the other `n_i=0`. The covers and every map used below are deck invariant.

A sufficient first-order pole domain is carrier exponent 14 and legal-line exponent 1, per source-vertex occurrence:

- The primitive carrier bound is 2. Therefore `g,g^-1` have carrier bound 4; `g^-1` is the determinant-one adjugate.
- A derivative adds at most 1 to an existing owned carrier pole. Thus `C_ab` has bound at most `4+5+5=14`. The gerbe adds no carrier poles.
- The pinned scalar solution also has carrier bound 14: its connection blocks have bound 7 and its scalar trace uses at most two such blocks. The other terms have smaller bound.
- Endpoint cancellation in the trace leaves only logarithmic line seeds. Each term of `C_ab`, `b_ab`, and the pinned scalar uses coordinates `a,b` once each. Each legal seed has a simple pole with an actual mask owner. Thus legal-line bound 1 suffices.

This repeats the first-order portion of the existing full-matrix pole proof, not a scalar-row or numerator-cancellation argument. Including the pinned scalar in the domain is useful only for the proof of exactness below; the alternative does not evaluate it.

Use the already proved fixed carrier partition at `N=14`. Its parameters are `M=27`, `L0=135`, and, on a chart with `d` carrier-unit summands, multinomial degree `L=d*134+1`, at most 671. Use legal weights `(1,0)` on finite charts and `(t^2,1-t^2)` on infinity charts. These give fixed common-cover weights `rho` and operators

`Pi : C(B,L_ab) -> C(U,L_ab)`,

`H_rho : C^q(B,L_ab) -> C^(q-1)(B,L_ab)`

with the exact identities

`Pi delta = delta Pi`,

`delta H_rho + H_rho delta = 1-r*Pi`.

The weights clear every inserted vertex's owned poles; the unchanged suffix keeps its original legal denominators. Nothing transfers a factor from an absent carrier. These formulas are finite, but their values are not generated here.

Let `A` and `S` be the fixed Alexander–Whitney and signed-staircase maps between standard tensor and ordered Čech complexes, and `K_cov` the checked rectangle-cone homotopy. Their conventions are

`SA=1`,

`delta K_cov+K_cov delta=1-AS`.

For example, `S(c)_[01]x[01]=c_(00,10,11)-c_(00,01,11)`. This fixes the comparison sign independently of the new construction.

## 3. Explicit scalar tensor contraction, including signs

In one factor use the common finite frame of `O(n)`, with `n=0` or `-2`. Let chart states `A,B` have Čech degree zero, and `C` be their overlap in degree one. The differential is

`delta(f_A,f_B)=f_B-f_A`.

In this frame, A-sections have powers `x^e` with `e>=0`; B-sections have powers `e<=n`; C-sections are finite Laurent polynomials after the regular transport.

Define the degree-minus-one homotopy on C-monomials by

`h_n(x^e C) = -x^e A`, if `e>=0`,

`h_n(x^e C) = +x^e B`, if `e<0` and `e<=n`,

`h_n(x^e C) = 0`, otherwise,

and set it to zero on degree zero.

For `n=0`, the only harmonic group is degree zero. Define `p_0(f_A,f_B)` as the coefficient of `x^0` in `f_B`, and `i_0(c)=(c,c)`.

For `n=-2`, the only harmonic group is degree one. Define `p_-2(f_C)=[x^-1]f_C`, and `i_-2(c)=c x^-1 C`.

In each case the monomial check gives

`delta h_n+h_n delta=1-i_n p_n`, `p_n i_n=1`.

For `n=0`, the exponent-zero check is important: `h_0(1 C)=-1 A`, while the degree-zero projection uses the B coefficient. These choices make the displayed identity exact.

On the four-factor tensor product set `J_i=i_i p_i`,

`P=p_1 tensor p_2 tensor p_3 tensor p_4`,

`I=i_1 tensor i_2 tensor i_3 tensor i_4`,

`h = h_1 tensor 1 tensor 1 tensor 1`

`  + J_1 tensor h_2 tensor 1 tensor 1`

`  + J_1 tensor J_2 tensor h_3 tensor 1`

`  + J_1 tensor J_2 tensor J_3 tensor h_4`.

Tensor maps use the Koszul sign: the term applying `h_j` has sign `(-1)^(sum of the preceding Čech degrees)`. The four identities telescope to

`delta h+h delta=1-IP`.

For `L_ab`, the harmonic tensor has degree 2 only: C-state with exponent -1 in factors `a,b`, and the diagonal constant degree-zero class in the other factors. In particular `H^1(Y,L_ab)=0`.

## 4. Why the sole scalar obstruction projection is zero

Set

`c_ab=Pi f_ab`, `t_ab=S c_ab`.

They are closed. The only candidate scalar obstruction is `P t_ab`.

Its zero value is a theorem about the already authenticated first-order equation, not an evaluation of a new source. The pinned source proves algebraically that its prescribed scalar `s_old,ab` obeys

`delta s_old,ab = F_ab`

for precisely the gerbe representative `b_ab=(15/4)q_a cup q_b`, including its `-15 q_a,ij q_b,ij/8` representative correction. By the domain check in section 2, the comparison maps apply to that identity. Therefore

`P t_ab = P S Pi s*(delta s_old,ab)`

`        = P delta(S Pi s*s_old,ab) = 0`.

No entry of `s_old,ab` must be constructed or evaluated to use this exact identity. The rank-12 theorem gives the compatible cohomological statement that the compensated bivector evaluates to zero; the pinned source identity additionally authenticates the concrete row convention and the actual gerbe representative needed here.

This does not use a geometric oracle for any order-two class. It proves only the vanishing of this scalar first-order projection.

## 5. A completely specified new first lift

On the common refinement define

`s_new,ab = H_rho f_ab + r*(K_cov c_ab + A h t_ab)`.

Then

`delta s_new,ab`

`= (f_ab-r*c_ab) + r*(c_ab-A t_ab) + r*A(t_ab-I P t_ab)`

`= f_ab`.

Every sign is positive in this formula. The last equality uses the proved `P t_ab=0`. Pull back the physical transitions and set

`u_new,ab = g (s_new,ab I-K_ab(g)/2)`.

This is a valid first lift of the prescribed gerbe/bivector problem. The original physical frame derivatives remain in `g` and `K`; no frame ratio is replaced by a constant during differentiation.

The expression is finite and uses only rank-two matrix differentiation/multiplication, scalar cover maps, Laurent coefficient splitting, and the given gerbe cochain. The four-block trace is used as an existing exactness proof, not as an input to be evaluated.

## 6. Equality of obstruction classes and the required gauge terms

Both scalar solutions have pure character `chi_ab`. Their difference

`d_ab=s_new,ab-s*s_old,ab`

is a closed scalar 1-cochain. The scalar cohomology calculation in section 3 gives `H^1(O_X)_chi_ab=0`; hence `d_ab=delta f0_ab`. Thus the two first lifts are gauge equivalent already within the scalar part. This is stronger than merely applying the Ext^1 weight bound.

For clarity, the full induced second-order gauge correction cannot be discarded. If `H_i=1+hbar z_i` and the original transitions are `g+hbar u+hbar^2 v`, then the pinned row convention gives

`G'_ij=F_ij(H_j^-1) star G_ij star H_i`.

The ambient source has no order-one overlap automorphism. Expanding the gauge law algebraically through order two gives

`u'_ij=u_ij-z_j g_ij+g_ij z_i`,

`v'_ij=v_ij+z_j^2 g_ij-z_j u_ij+u_ij z_i-z_j g_ij z_i`

`                    -mu_1(z_j,g_ij)+mu_1(g_ij,z_i)`.

The inverse here is the star inverse through this order. Choosing `z_i=-(f0_12,i+f0_34,i)` gives the new first lift. Retaining the displayed induced second-order term makes the module defects transform covariantly. If one computes the residual using only the new first lift and sets its second-order transition coefficient to zero, the two normalized residuals differ by an ordinary End Čech boundary, namely the negative differential of the normalized induced coefficient. Hence the full-sign obstruction class is unchanged.

This is an algebraic comparison identity, not the construction or evaluation of a new second-order residual.

## 7. What survives, and what requires a new proof/preflight

Retained exactly:

- The actual compensated gerbe representative, row/column convention, determinant-one transitions, and physical line-frame derivatives.
- Pure pair characters of the two first lifts, and therefore the identification of the full-sign second-order class.
- Linearity of the scalar solving operator in `F_ab`; the cover maps are fixed independently of the cochain.
- Regularity on the explicit common refinement. Carrier and line poles have actual owners.
- The local primitive identities for `I,P,H`, and any pointwise sparse selector identity for a tail with specified carriers.

Not inherited as an executable contract:

- The source is now on common vertices `(standard chart, carrier, line mask)`. It is not a three-carrier-local function with the old four-tail circuit unless descent and compatibility are separately proved.
- The current four-tail/global carrier-weight factorization and 781 owner-feature count cannot be reused automatically. The new scalar includes weighted sums over inserted source vertices and standard tensor primitives.
- The original source's simple group-multilinear mask feature representation is not established for this new refined source. Deck character alone does not prove that representation.
- Legal-line exponent 1 and carrier exponent 14 above certify this first-order scalar solver's domain. They do not establish the existing full-sign J0–J3 bound for the new second-order source. Complementary differentiation of the new partition-dependent scalar must be accounted for, including derivatives of the weights and exact chart restrictions.
- No product count, finite demand set, coefficient-width bound, peak-byte schedule, or end-to-end cost improvement follows from rank two or from the single scalar harmonic coefficient.

Before execution, a fresh static contract must price the rank-two F circuit, the scalar regularization and Laurent splitting, any derivative-compatible representation of the resulting scalar, and the downstream comparison. It must certify compliance with the applicable execution limits, or stop and report its certified prospective bounds. Nothing in this note authorizes an expansion or a residual/jet/sample calculation.

## Sources

1. [Pinned first-order source, sections 1–4](https://github.com/Akilleez-QA/read-em-and-weep/blob/08b73637d4136f91606aad332c46cafd064417f8/research/hm/current-scalar-residual-attribution/first-order-source.md), blob `5f4e56252cd9a8a6eb218aceb911c95a1c330ebc`: determinant-one transitions, scalar equation, representative correction, and exact rank-two identity.
2. [Pinned executable source excerpts](https://github.com/Akilleez-QA/read-em-and-weep/blob/08b73637d4136f91606aad332c46cafd064417f8/research/hm/current-scalar-geometric-dependencies/data/source-formulas.js), blob `3dfed53a28b53b3c912a097971d89fc547330a5f`: physical first-lift and gerbe conventions.
3. [Closure and characters, sections 2 and 5](https://github.com/Akilleez-QA/read-em-and-weep/blob/08b73637d4136f91606aad332c46cafd064417f8/research/hm/current-scalar-residual-attribution/closure-and-characters.md), blob `946f96670ecb8152eaae16195329f9eb1243b7ae`: pure pair characters, ambient identification, and gauge covariance.
4. [Pinned tensor contraction](https://github.com/Akilleez-QA/read-em-and-weep/blob/08b73637d4136f91606aad332c46cafd064417f8/research/hm/current-scalar-proof/finite-model/full-sign-boundary-oracle.js), blob `8f534fd7a074e333fa031a6d8c51b864faf76d42`, `unprunedTransfer/fullH`: the same A/B/C signs. This note uses only the scalar one-factor contraction identity, not the oracle's residual or boundary computations.
5. [Pinned ambient second jet, sections 2–3](https://github.com/Akilleez-QA/read-em-and-weep/blob/08b73637d4136f91606aad332c46cafd064417f8/research/hm/current-scalar-residual-attribution/ambient-second-jet.md), blob `e07d4373a7c22f7cf4502260d80dbd559d942850`: `F_ij=1+hbar^2 T_ij` and the row-left module defect.
6. Companion proof notes `hm-regular-cover-transport.md`, `hm-regular-cover-transport-audit.md`, `hm-full-sign-legal-line-bound.md`, and `hm-first-order-rank12-proof.md`: fixed cover formulas and their checked signs, the owned-pole argument, and first-order cohomology scope.
