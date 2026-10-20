# Exact base Čech source at the cusp

20 October 2026. Formal mathematical record; no obstruction coordinates were evaluated.

## 1. Conventions and inputs

Fix one ordered factor pair p=(r,s), with π_p=V_r∧V_s. Cover indices are Greek and factor indices Roman. On a triangle (α,β,γ), write

    A=h_{αβ}, B=h_{βγ}, H=h_{αγ}=BA,
    g_e=τ_e h_e, τ_e²=l_e, τ_{βγ}τ_{αβ}=τ_{αγ}.

The last identity uses actual compatible root frames, possibly after étale refinement; it is not a choice of independent square roots on edges. Let L=O(1,1,1,1). The scalar l_e is its transition. Work in one common rational base coordinate system x_i, so y_i²=F_i=F(x_i). Every displayed derivative acts on the entire following matrix, in the indicated edge frame.

Put

    ∇_{i,e}=∂_{x_i}+(1/2)∂_{x_i}log(l_e),
    D_{i,e}=F_i∇_{i,e}+F'_i/2,
    L_{i,e}=F_i∇_{i,e}²+(F'_i/2)∇_{i,e}.

These are scalar differential operators acting entrywise, not End-connection commutators. In particular ∇² includes the derivative of its scalar connection coefficient. Define ∇_{rs,e}=∇_{r,e}∇_{s,e}; these commute on each edge because the scalar connection is an exact logarithmic differential.

Let the stipulated normalized first lift be

    x_{p,e}=g_e^{-1}u_{p,e}=y_r y_s X_e,
    U_e=h_e X_e, so u_{p,e}=τ_e y_r y_s U_e.

X is a fixed regular base Čech cochain with the pair twist O(-2 in r,-2 in s); it is not a globally defined untwisted matrix of functions. Its representatives below use the same local odd generators y_r,y_s. Write U_A=AX_{αβ}, U_B=BX_{βγ}, U_H=HX_{αγ}.

For the short PR16 cocycle, write

    q_{i,e}=y_i Q_{i,e},
    b_{p,αβγ}=y_r y_s β_{αβγ},
    β_{αβγ}=λ Q_{r,αβ}Q_{s,βγ}, λ=15/4.

On the oriented standard 0-to-infinity overlap, Q_i=1/x_i. Pullbacks/refinements and reversed edges retain their actual Čech signs. The notation Q denotes coefficient extraction in the odd finite-flat summand, not division by y at its zeros.

The base first-order equation is exactly

    X_{αβ}+A^{-1}X_{βγ}A-X_{αγ}
      = β I -(1/2)H^{-1}[(∇_{r,βγ}B)(∇_{s,αβ}A)
                         -(∇_{s,βγ}B)(∇_{r,αβ}A)].              (1)

Use the twisted Čech interpretation of this equality if different odd generators are used on different charts. The accepted fixed-class cancellation supplies a regular X solving (1). It does not specify its coefficients.

## 2. Complete normalized pure source

Define scalar operators acting on the scalar triangle coefficient β by

    d_i β=F_i ∂_{x_i}β+(F'_i/2)β.

Then the complete base representative C_p of g_{αγ}^{-1}R_{pp,αβγ} is

    C_p=H^{-1}(N_1+N_2+N_3+N_4+N_5+N_6+N_7+N_8),          (2)

where the order of all matrix factors is part of the formula:

    N_1=F_r F_s U_B U_A,

    N_2=(1/2)[F_s(D_{r,βγ}U_B)(∇_{s,αβ}A)
               -F_r(D_{s,βγ}U_B)(∇_{r,αβ}A)],

    N_3=(1/2)[F_r(∇_{r,βγ}B)(D_{s,αβ}U_A)
               -F_s(∇_{s,βγ}B)(D_{r,αβ}U_A)],

    N_4=(1/8)[(L_{r,βγ}B)(L_{s,αβ}A)
               +(L_{s,βγ}B)(L_{r,αβ}A)
               -2F_rF_s(∇_{rs,βγ}B)(∇_{rs,αβ}A)],

    N_5=λ[a_{r,α}F_s Q_{s,αβ}(∇_{s,βγ}B)
             +F_r Q_{r,αβ}a_{s,β}(∇_{r,βγ}B)]A,

    N_6=-F_rF_s β U_H,

    N_7=-(1/2)F_rF_s β² H,

    N_8=-(1/2)[F_s(d_r β)(∇_{s,αγ}H)
                 -F_r(d_s β)(∇_{r,αγ}H)].

These are, respectively, the eight terms u u, μ_p(u,g), μ_p(g,u), μ_pp(g,g), T_p(g)g, -bu, -b²g/2, and -μ_p(b,g). In particular N_5 and N_8 have not been combined into a claimed boundary or discarded. The pair μ_pp is mD_p²/8; no extra cross-pair factor belongs here.

### General ordered β-coefficients in the gerbe

To avoid confusion with the scalar β in (2), denote the constant source coefficients β_{rs},β_{sr} by c_{rs},c_{sr} in this paragraph. If

    b_p=c_{rs} q_r∪q_s+c_{sr} q_s∪q_r,

replace β everywhere by

    β=c_{rs}Q_{r,αβ}Q_{s,βγ}+c_{sr}Q_{s,αβ}Q_{r,βγ},

and replace N_5 by

    [F_s(c_{rs}a_{r,α}Q_{s,αβ}-c_{sr}Q_{s,αβ}a_{r,β})∇_{s,βγ}B
     +F_r(c_{rs}Q_{r,αβ}a_{s,β}-c_{sr}a_{s,α}Q_{r,αβ})∇_{r,βγ}B]A.

This follows directly from s_k=Σc_{ij}(δ_{ki}a_i∪q_j-δ_{kj}q_i∪a_j) and T_p=s_rV_s-s_sV_r. The short representative used in the main formula is c_{rs}=λ,c_{sr}=0. Changing this representative without its actual Čech equivalence is not licensed by the formula.

## 3. Derivation and endpoint checks

The identities needed for direct substitution are

    V_i(τ_e h_e)=τ_e y_i∇_{i,e}h_e,
    V_i²(τ_e h_e)=τ_e L_{i,e}h_e,
    V_rV_s(τ_e h_e)=τ_e y_r y_s∇_{rs,e}h_e,
    V_r(τ_e y_r y_s U_e)=τ_e y_s D_{r,e}U_e,
    V_s(τ_e y_r y_s U_e)=τ_e y_r D_{s,e}U_e.

The same odd derivative identities without τ apply to b=y_r y_s β, with d_i in place of D_{i,e}. Each term contains τ_{αγ} after multiplication, which cancels only after the derivatives have been performed. Freezing τ before differentiating loses all logarithmic connection terms.

Alexander–Whitney endpoints are essential:

    (a_r∪q_s)_{αβ}=a_{r,α}q_{s,αβ},
    (q_r∪a_s)_{αβ}=q_{r,αβ}a_{s,β}.

Thus the two a-values in N_5 are at different endpoints. Likewise b uses Q_{r,αβ}Q_{s,βγ}, whereas T uses Q on αβ and differentiates B on βγ. Finally N_8 differentiates H on αγ, not A or B separately. All four distinctions survive normalization.

## 4. Exact cusp specialization, without physical evaluation

Set F(x)=x³. The cusp data are

    F_i=x_i³, F'_i/2=(3/2)x_i²,
    D^c_{i,e}=x_i³∇_{i,e}+(3/2)x_i²,
    L^c_{i,e}=x_i³∇_{i,e}²+(3/2)x_i²∇_{i,e},
    d_i^c β=x_i³∂_{x_i}β+(3/2)x_i²β,
    a_{i,0}=-x_i/2, a_{i,∞}=0, Q_i=1/x_i on the standard overlap.

Let ε_{i,α} be 1 if the refinement chart α maps to the factor-i zero chart and 0 if it maps to the infinity chart. Then a_{i,α}=-(1/2)ε_{i,α}x_i. Formula (2) specializes exactly by replacing F,D,L,d by these expressions. For explicitness the cusp numerator is

    N_1^c=x_r³x_s³ U_B U_A,
    N_2^c=(1/2)[x_s³(D^c_{r,βγ}U_B)(∇_{s,αβ}A)
                  -x_r³(D^c_{s,βγ}U_B)(∇_{r,αβ}A)],
    N_3^c=(1/2)[x_r³(∇_{r,βγ}B)(D^c_{s,αβ}U_A)
                  -x_s³(∇_{s,βγ}B)(D^c_{r,αβ}U_A)],
    N_4^c=(1/8)[(L^c_{r,βγ}B)(L^c_{s,αβ}A)
                  +(L^c_{s,βγ}B)(L^c_{r,αβ}A)
                  -2x_r³x_s³(∇_{rs,βγ}B)(∇_{rs,αβ}A)],
    N_5^c=-(λ/2)[ε_{r,α}x_r x_s³ Q_{s,αβ}(∇_{s,βγ}B)
                    +ε_{s,β}x_s x_r³ Q_{r,αβ}(∇_{r,βγ}B)]A,
    N_6^c=-x_r³x_s³ β U_H,
    N_7^c=-(1/2)x_r³x_s³ β² H,
    N_8^c=-(1/2)[x_s³(d_r^c β)(∇_{s,αγ}H)
                   -x_r³(d_s^c β)(∇_{r,αγ}H)].              (3)

On an edge where both standard Q-values are 1/x, N_5^c becomes

    -(λ/2)[ε_{r,α}x_r x_s²∇_{s,βγ}B
              +ε_{s,β}x_s x_r²∇_{r,βγ}B]A.

That last simplification is only for such an edge; it must not replace the actual Q cochains globally. In particular a∞=0 does not make all of T vanish.

Define

    C_p^c=H^{-1}Σ_{j=1}^8 N_j^c,
    C^c=C_{12}^c+C_{34}^c,
    v=[C^c] ∈ H²((P¹)^4,ρ*End H).                         (4)

This v is exactly the cusp value Q(1,0,0) identified in the boundary report, not a value obtained by evaluating any actual matrix entry here.

## 5. Regularity, closure, and no asserted primitive

Equations (2)–(3) are rational-coordinate expressions for regular invariant Čech cochains. Poles in x at infinity are coordinate artifacts: use the local generator z=y/x² and t=1/x there, and V(t)=-z, V(z)=-1/2 at the cusp. Transform the odd generators, l, h, and X together. No inversion of y, F, or F' is required anywhere in the derivation.

More intrinsically, on an affine refinement with actual root frames, all eight original PR16 operations are regular. After normalization the root factors cancel, and each term has trivial deck character. Finite-flat pushforward identifies its invariant coefficients with regular sections of ρ*End H on the corresponding base intersection. The square-frame formula descends through the étale refinement: within a fixed base chart the extra root transitions are ±1 and their derivatives vanish. This proves regularity without pretending that 1/x or a finite-chart connection expression is regular on every chart.

The full descent equations together with (1) imply δC_p^c=0. The individual N_j are not claimed cocycles. Any argument extracting their separate cohomology classes would require further proof. A second-order base primitive Y would have to satisfy δY=-C^c. The present symbolic expansion does not produce such Y or a cancellation theorem.

The cusp does not itself remove the cohomology problem. The element y/x on the normalization is not regular at the cusp in C[x,y]/(y²-x³). Replacing the cusp by its normalization and treating this element as a global regular primitive changes the sheaf and can erase the genuine genus-one contribution. No such replacement is used here.

## 6. Six-value computation contract, not an evaluation

Use the already-audited compact target and covariance, rather than re-proving polynomiality. The class v lies in the A² rotation eigenspace of the six ρ₂ copies: two dimensions in the canonical twist -1 projection and four in the twist -2 projection. Fix a certified chain comparison and six cohomology coordinate functionals ℓ₁,…,ℓ₆ on precisely this subspace. The six required values are

    ν_j=ℓ_j([C_{12}^c+C_{34}^c]), j=1,…,6.

A valid implementation would have to supply:

1. Actual h,l and their classical cocycle/frame identities on one acyclic base cover, with all rational expressions restricted to their genuine domains.
2. Regular pair-twisted X for both pairs and exact verification of (1).
3. All eight terms of (3), in the declared row order, and exact closure of their sum.
4. A chain comparison into the accepted compact target, retaining any required refinement corrections. If using PR16's column contractions, transpose the completed row residual, not intermediate nonlinear factors.
5. Six cohomology coordinates modulo boundaries, not raw cochain entries, in the single rotation eigenspace. Verify the two/four canonical splitting.

One nonzero ν_j detects the remaining diagonal obstruction. All six zero establish v=0, hence v+Rv=0 under the accepted cusp-to-original identification and the injectivity of v↦v+Rv. Constructing the actual second-order module still requires back-substitution and verification of its transition equation. No ν_j, matrix product, or primitive was computed here.

## Sources read

- [branch-boundary-extension.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/c9412e435d6349ea5c9395711aa794e3dd003641/research/hm/null-branch-polynomial-extension/branch-boundary-extension.md), [branch-boundary-audit.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/c9412e435d6349ea5c9395711aa794e3dd003641/research/hm/null-branch-polynomial-extension/branch-boundary-audit.md), [branch-covariance-next.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/c9412e435d6349ea5c9395711aa794e3dd003641/research/hm/null-branch-polynomial-extension/branch-covariance-next.md), [pure-square-next.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/b8903f211ef47802a9f701d9e74d3f67377022f2/research/hm/null-pure-square-reduction/pure-square-next.md), [pure-ambient-audit.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/b8903f211ef47802a9f701d9e74d3f67377022f2/research/hm/null-pure-square-reduction/pure-ambient-audit.md), and the scalar-pairing convention check.
- Direct read-only fetch of PR16, commit c8aec970fd65a105f39f4e8aeb8a17f0f0053f89, blob a58834ab61e18a5dedd8a7bf20bec7121bfa9165, especially §§1–7:
  https://github.com/Akilleez-QA/read-em-and-weep/blob/c8aec970fd65a105f39f4e8aeb8a17f0f0053f89/research/hm/second-order-algebroid.md

The exact base source and cusp substitution above are formal deductions, not claims that PR16 already stated them.
