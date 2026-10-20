Editorial scope: This is a mathematical source edition. Historical review and check statements describe the original artifact, not a fresh run. Supporting snapshots are dependencies, not additional new results. Later PR145 mixed-class vanishing supersedes historical unknown mixed-class status; it does not resolve the six pure diagonal conditions.

Supporting dependency only: this complete source text is not a fresh result of this packet.

# Complete remaining-target normal form

## Scope

This is a formal synthesis of the supplied public source-adjoint, current-curl, differentiated-partition/domain, endpoint-transfer, common-split-connection and overlap-homotopy packets. No actual source/model/owner/jet values, matrix-polynomial products, experiments were used. The supplied current remote revision is context only, not independently authenticated here. Every geometric/domain statement below is conditional on the packets' actual homogeneous all-chart denotations, normalized contraction, legal owner localizations and ordinary full partition comparison. No cancellation, retained-test value or performance claim follows.

## 1. Conventions and unreduced identity

Work first in the pinned common finite frame, with fixed regular selector L and ambient restrictions δ. Let Δ be the actual row Čech differential, π15 the single full-sign extraction, and S the staircase map. Write J1=Hδj (unsigned), J2=−HδHδj, T=LJ2 and M=ΠT; typed input-degree versions of these words are understood. Π and S commute with the relevant Čech differentials. No input is assumed closed. The original source-adjoint fluxes G_d remain unchanged:

    p F_spec = Σ_d ∂_d G_d + B_p.

For r=(a,b), complementary q, on each increasing triple (i,j,k), put

    L_v=g_ij^−1 V_v g_ij,
    U_v=g_ij^−1 g_jk^−1(V_v g_jk)g_ij,
    Z_a=(s_q,jk L_b−s_q,ij U_b)/2,
    Z_b=(−s_q,jk L_a+s_q,ij U_a)/2,
    Ccur_r=2(s_q,ij+s_q,jk) k_r,ij−2s_q,ij k_r,ik.

Use both pairs (r,q)=((0,1),(2,3)),((2,3),(0,1)). Thus there are exactly four Z_d, covering all eight original signed E branches. Define R*=R_alg+Ccur_P+Ccur_Q. Then the exact starting remainder is

    B_p=π15 S { p M R*
                  −Σ_d[(V_d p) M Z_d
                        +p Π'_d T Z_d+p Π T'_d Z_d] }.       (1)

Primes differentiate coefficients, not the inserted Z_d. Formula (1) follows by the Leibniz rule for the complete kernel pΠT; it does not differentiate s_raw again.

The complete algebraic input has NOT been shortened. With A=g_ij, B=g_jk, G=g_ik=BA and U_r=g k_r,

    R_alg=tf(G^−1 N)+F_Q k_P,ik+F_P k_Q,ik,

where, in original order,

    N=U_P,jk U_Q,ij+U_Q,jk U_P,ij
       +μ_P(U_Q,jk,A)+μ_Q(U_P,jk,A)
       +μ_P(B,U_Q,ij)+μ_Q(B,U_P,ij)+μ2(B,A)
       −b_P U_Q,ik−b_Q U_P,ik−b_P b_Q G.

Both original Fk branches, all seven kinetic terms and all three negative gerbe terms survive. In particular no F is replaced by an s_raw endpoint.

## 2. One boundary map and one exact normal form

For direction d write Γ_d=Γ_End,d, C_d=[δ,Γ_d], and use the overlap decomposition C_d=C0_d+d_End R_d+R_d d_End. Set

    W_d=δR_d+R_dδ,
    Q_d=L H R_d j,
    O0_d=L H C0_d J1+L H δH C0_d j,
    D_d=O0_d+L R_d J1+L H W_d j,
    K_d=Qdot_d T−Π Q_d.

Here Qdot_d is the full differentiated partition prism, not a prefix-only prism. The common-split and overlap identities give

    T'_d=−LΓ_d J2+D_d−δQ_d−Q_dΔ,
    Π'_d=δQdot_d+Qdot_dδ,
    δT=TΔ.

Define the coupled test/selector operator

    A_d(p)=(V_d p)LJ2−p LΓ_d J2.

Substitution into (1) gives the SINGLE normal form

    B_p = π15 S {p ΠT R*
                   −Σ_d Π A_d(p) Z_d
                   −p Σ_d Π D_d Z_d
                   −p Σ_d K_d ΔZ_d}
          −π15 δ_tensor [p S Σ_d K_d Z_d].                 (2)

The boundary and defect have the SAME map K_d and the SAME minus sign. Degree-indexed Π, T, Qdot and Q are implicit: K applied to a degree-two input lands in degree three; K applied to ΔZ uses its degree-three-input version and lands in degree four.

Direct sign check: the outer family is −pδ(Qdot T Z)−p Qdot T ΔZ. The negative inner derivative contributes +pΠδ(QZ)+pΠQΔZ, besides +pΠLΓJ2Z−pΠDZ. Since Πδ=δΠ and p is a compatible section, the two boundary contributions combine to −δ[p(Qdot T−ΠQ)Z]; the two defect contributions combine to −p(Qdot T−ΠQ)ΔZ. This proves (2) without dropping a projection or assuming ΔZ=0.

Do NOT also subtract the older differentiated-HPL U boundary. Formula (2) replaces that ordinary-derivative decomposition wholesale. Keeping its old boundary while replacing its remaining terms by the common-split expression would count the inner removal twice.

## 3. Scalar-free substitution in the entire combined defect

Let θ_v,ij=g_ij^−1 V_v g_ij and

    C_(v,q),ijkl=θ_v,ij F_q,jkl
                  +F_q,ijk g_ik^−1 θ_v,kl g_ik.

The actual first-order identity δs_raw,q=F_q and Δθ_v=0 give

    ΔZ_0=−C_(1,Q)/2,  ΔZ_1=+C_(0,Q)/2,
    ΔZ_2=−C_(3,P)/2,  ΔZ_3=+C_(2,P)/2.

Consequently the fourth family inside (2) is exactly

    (p/2)[K_0 C_(1,Q)−K_1 C_(0,Q)
           +K_2 C_(3,P)−K_3 C_(2,P)].                     (3)

This substitution applies to BOTH Qdot T and −ΠQ in K. The plus between the two cups in C is forced by the degree-one cup Leibniz sign. The final current is transported by g_ik, not g_ij. Only this defect family loses s_raw; the boundary, current-curl, coupled selector and D_d inputs retain it. Closure of C is not vanishing.

## 4. New conditional domain theorem: coupled test/selector term

Individual Γ coefficients in a fixed finite reference need not have owned infinity poles. An edge-difference estimate does not prove their local bound. Instead use the actual normalized local frame and the literal identity

    Γ_k=B_raw,k+kβ Id,  β=α−Vν/ν.

On a finite factor (bit m∈{0,1}), β=−m y/(2x); its possible x pole belongs to the bit-one legal factor x(x²−1). At infinity set t=1/x, z=t²y and use the SAME transported old connection. The normalized line ratios satisfy

    ν_B²=t                 (m=0),
    ν_B²=1−t²              (m=1),
    α_B=m zt/(1−t²).

Thus with the full invariant V (equal to −z∂t on functions of t),

    ρ_B=Vν_B/ν_B=−z/(2t)   (m=0),
    ρ_B=zt/(1−t²)          (m=1),
    β_B=(1−m)z/(2t).

The infinity t pole is therefore owned by the bit-zero legal factor Y; β_B vanishes for bit one. This proves β has local owned 0/1, not merely that edge differences do. The imported local raw-block derivation gives B_raw 5/1, so Γ_k has owned 5/1 in the correctly normalized local chart. The induced Γ_End action has the same 5/1 bound: its two products are added, not multiplied. The extremal resolution blocks can equivalently be checked directly from Γ_−1=ρ Id and Γ_2=−5ρ Id. This argument requires the actual normalized ν_B and transported α_B, not arbitrary frame labels or resetting the old connection to zero.

For the specified representation change, with ℓ_d=V_d logτ,

    p_B=τ²p_A,  J2_B=τ^−2J2_A,
    Γ_End,d,B|r=−2=Γ_End,d,A+2ℓ_d Id.

Therefore

    (V_d p_B)LJ2_B=(V_d p_A)LJ2_A+2p_Aℓ_d LJ2_A,
    p_B LΓ_BJ2_B=p_A LΓ_AJ2_A+2p_Aℓ_d LJ2_A.

The anomalies cancel EXACTLY in A_d(p). With invariant Z_d, A_d(p)Z_d agrees before deck extraction. Full-sign extraction then gives the canonical-bundle coefficient transition τ^−2. Neither separated summand is independently asserted to have this covariance.

The local coefficient of the authenticated dual test is polynomial on each standard representation chart, so V_d p_local is regular. Using j4/2, H6/3, Z19/7 gives J2Z35/15. The two coupled summands have bounds 35/15 and (5/1)+(35/15)=40/16. Thus their SUM has the owned per-occurrence envelope 40/16. This is a conditional all-chart domain conclusion for the combined term, established by the local Γ calculation and anomaly cancellation, not inferred from edge Γ bounds. Ordinary full weights54/29 dominate it, and regular finite-flat character extraction after invariant clearing gives a regular canonical-valued compared term. There is no resulting vanishing assertion.

## 5. Boundary domain and exact survivors

The two pieces of KZ have separate imported domain theorems:

* Qdot T Z: endpoint c=TZ has35/15, differentiated own weight53/28 and every other own weight54/29; the full prism supplies all five source occurrences their weights. The missing-axis eigensheaf and differentiated-weight character restore the full-sign F=O(−4,−4,−4,−4).
* ΠQZ: Q kernel21/9 and endpoint19/7 give40/16; its representation covariance is internal-degree−2, and every source occurrence receives its ordinary54/29 weight. The overlap packet proves this in F.

Their sum/difference is therefore a genuine degree-three F-valued cochain after S and extraction. Multiplication by the actual global dual test p∈H⁰(O(2,2,2,2)) gives a canonical-valued boundary. Its Serre trace vanishes conditionally. It is not being identified with a rational-coordinate divergence.

The surviving KΔZ term is also in the admitted domain: the Qdot T part inherits it from δ(TZ)=TΔZ and the differentiated-prism theorem; ΠQΔZ uses the overlap packet's conservative48/20 bound. The scalar-free form (3) inherits this domain by equality. No independent pole estimate is asserted for separately expanded F-current factors.

The D families retain the existing bounds: C0 insertion families with Z48/22, LRJ1Z40/16, LHWjZ40/16. Their ordinary full comparisons are covered by54/29. The coupled test/selector domain is the additional conditional conclusion of §4. The full baseline and Ccur families remain as their exact original source-derived expressions; no termwise Laurentness, new independent baseline regularity claim or cross-family cancellation is inferred here.

All prefix, edge and tail owners remain attached, including distinct owners with coincident physical divisors and repeated target tags. No absent owner supplies a clearing factor. The mathematical alternating extension does not license running a frozen repeated-key implementation. Normality, actual homogeneous denotation and regular character projection remain premises, not consequences of arithmetic pole ledgers.

After conditionally killing the ONE boundary under Serre trace, the complete unknown target is the trace/residue of the four families inside (2), equivalently with (3): full baseline plus actual current-curl; coupled test/selector; both cohomology-current insertion families and both overlap-homotopy corrections; and the combined scalar-free nonclosed defect. This is an exact remaining-target formula, not a value or a certificate of cancellation. The rational-divergence equivalence still requires the original geometric/same-source/finite-Laurent/trace hypotheses.

If L or ambient restrictions vary, the displayed specialization is insufficient: retain +L'J2 in T', and use C_eff=[δ,Γ]−δ' with its literal insertion corrections. The present boundary combination and domain conclusions assume the pinned fixed-L, fixed-δ representation framework; they do not claim arbitrary owner-gauge invariance.
