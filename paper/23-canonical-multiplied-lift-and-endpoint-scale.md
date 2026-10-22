# 23. Canonical multiplied nilpotent lift and fixed endpoint scale

**Checked-source cutoff: 22 October 2026, 08:15 UTC.** This chapter adds the actual first-normal square-zero lift of the multiplied nilpotent, the fixed-boundary consequence of the Cartan–Koszul multiplier, and the published necessary (2,2) quotient list. The general section count remains four or five. The third Bockstein is zero and all four actual fourth coefficients remain unevaluated.

**Supersession:** [Chapter 24](24-multiplied-coherence-and-fifth-neighborhood-boundary.md) now includes the published coherence and exact actual 5Q boundary comparison, and refines the necessary list to 24 pairs/1,221 records. This chapter preserves the 08:15 source frontier; its exclusion of later coherence work is historical.

## 23.1 The actual endpoint and the precise lift

Retain B=End₀(F), the physical equation q=q₀, Q=(q=0), and 2Q=(q²=0) for the actual marked bundle. Let N be its fixed invariant nilpotent, ξ=δ_q(N), and ζ_a=k At_F(D_a), with aξ=qζ_a. Put

    r=a_m/b_m,   κ=−(χ/g_L)r,   r_ξ=k/κ,
    ξ=r_ξ At_F(D0),   D0=diag(−2I_V/5,3I_W/5).

There is an explicit global degree-zero monad cochain U_a of twist four such that

    dU_a=q²(k e_a),   U_a|Q=aN,
    (U_a mod q²)²=0 on F|2Q.

Its induced section is the unique equivariant linear physical-positive family lifting a↦aN. This is an actual-bundle statement on 2Q, not a hypothetical spinor extension. It lifts aN, not N itself, and does not extend the family to 3Q or perform the further division qv_h=ahζ_a. [Canonical lift][LIFT]

## 23.2 Source gauge, both arrows, and boundary sign

Write the monad source as A⊕U, middle as E=U⊗Ω²(2), and right term as (A⊕U)*⊗Δ. Here U=W′ and A is the negative quadratic three-space. The differential convention is

    (dT)_left=T_middle α−αT_source,
    (dT)_right=T_right β−βT_middle.

Fixed duality requires a skew middle component and T_right=−T_source†. For the natural Euler deformation e0_nat, the left-channel coefficients are (−6a_m/5,4b_m/5,−c_m/5). The constant source gauge

    G_source=diag(−I_A/5,−6I_U/5),
    G_middle=0,   G_right=−G_source†

satisfies e0_red=e0_nat+dG on both arrows, with left channels (0,2b_m B,0). The complete Clifford primitive and b_m-divided Cartan–Koszul homotopy satisfy

    (P_red)_middle=−2BMB*/(rχ),
    (P_red)_source=(P_red)_right=0,   dP_red=q e0_red,
    (T_red)_middle=rM_a+M_b,
    dT_red=a e0_red−qκ e_a.

The source blocks of T_red are AA=P_b, UU=Q_b, UA=(c_m/b_m)R and AU=(a_m/c_m)S; its right component is the negative adjoint. In particular the reverse source and natural Hamiltonian pullback action are retained. Define

    P_nat=P_red−qG,   T_nat=T_red−aG.

Then dP_nat=q e0_nat and dT_nat=a e0_nat−qκ e_a. The target-minus-transport convention gives δ_q[P_nat|Q]=[e0_nat]. Indeed, if e0_nat=dS_i locally, the closed lifts P_nat−qS_i have divided transition difference −δ_Cech S, the same sign as the natural deformation cochain.

The invariant physical-positive section line H⁰(B_Q(2))₊=C N and the injective invariant boundary, using stability and the pinned square sequence, identify r_ξP_nat|Q=N without a free rescaling. These are representatives of the fixed classes; previously chosen Čech representatives need not be literally identical.

Consequently

    U_a=r_ξ(aP_nat−qT_nat)=r_ξ(aP_red−qT_red)

has dU_a=q²(k e_a). The common source gauge cancels literally. Restricting the actual locally free monad preserves its exactness at the ends, so U_a mod q² induces the asserted trace-free endomorphism.

For uniqueness use

    0 → B_Q(2) —q→ B_(2Q)(4) → B_Q(4) → 0.

Differences of equivariant linear physical-positive section families belong to Hom_G(A,C N)=0. Arbitrary separate closed changes of primitives need not cancel as cochains; when they retain the stated family and restriction, their induced sections agree. Thus canonicity is a section-family assertion, not uniqueness of all cochain representatives. [Proof and conventions][LIFT]

## 23.3 Square-zero requires the full supertrace certificate

Put P=(P_red)_middle and T=(T_red)_middle. With the algebraic Clifford tensor in a compatible determinant frame, the complete channel identities give

    M²=χq I_U,   B*B=0,
    B*M_aB=−aM,   M_bB=3aB/2.

The compression follows from the complete second-channel equation, not an independently chosen proportionality. Hence

    P²=0,   B*TB=−raM,
    tr_E(PT)=2a tr_U(M²)/χ=4aq.

The trace over U is the full two-dimensional trace. The determinant factors cancel as in the fixed Clifford primitive; χ is not set to one. Both endpoint components of U_a are divisible by q. Keeping their contributions, not just the middle trace, yields

    Str(U_a²)=r_ξ²q²[Str(T_red²)−8a²],
    Str(T_red²)=tr_E(T²)−2tr((T_red)_source²).

The alternating monad trace equals the cohomology trace over O_(2Q), because the restricted monad is locally split at its ends. Fixed duality gives tr(U_a)=0, while the displayed identity gives tr(U_a²)=0 modulo q². Rank-two Cayley–Hamilton in characteristic zero therefore gives

    U_a²=(1/2)tr(U_a²)I=0 on F|2Q.

Polarization also gives U_aU_b+U_bU_a=0. Nilpotence on the reduced Q alone would not prove this result. Nor does this calculation assert literal square-zero of every raw monad component, exhibit a global chain null-homotopy for the square, or extend a selected spinor line. [Trace certificate][LIFT]

## 23.4 Fixed-boundary endpoint scale

Keep M(v)²=χq₀(v)I and tr(M(ξ)[M(η),M(ζ)])=g_Lτ(ξ,η,ζ), using the full two-dimensional trace. The completed multiplier gives κ=−(χ/g_L)r and a At_F(D0)=q₀κ At_F(D_a).

For the cone marking n=σσᵗJ0, actual nilpotent N=θn, and conic transition I−(ρ_C/z)n, let [η_ap,n]=2[n/z]. The positive logarithmic displacement is

    P^F=P^m(I+q₀η_+) mod q₀²,   η_+=c_+η_ap.

The fixed boundary is ξ_Q=−[η_+,N]. Thus the bracket displacement is η_b=−η_+, not η_+. Substituting the multiplier in c_+/k=−2ρ_C/(θκ) gives

    c_+/k=2ρ_C g_L/(θχr),
    c_b/k=−2ρ_C g_L/(θχr).

For the separately fixed edge and normal-root markings,

    η_E=C_ap a_m b_m η_ap,   d=K_cup b_m²,
    η_+=η_E/(2d),   ρ_C=C_res r²,

one obtains

    c_+=C_ap r/(2K_cup),
    k=θ C_ap χ/(4C_res K_cup g_L).

No constant has been assigned the value one. The cubic conformal scalar, Serre marking and normal-cup normalization retain their distinct meanings. The formula for ρ_C uses a fixed vertex residue, not an unnormalized raw conic residue. [Exact scale consequence][SCALE]

The covariance checks are substantive:

- Under q₀↦νq₀ with N fixed, χ and κ divide by ν, C_ap↦νC_ap and K_cup↦ν²K_cup. Thus c_+ divides by ν and k by ν². P_nat↦νP_nat, T_nat is unchanged, and r_ξ divides by ν: U_a is unchanged and its q²-boundary has weight ν⁻².
- Under σ↦lσ with determinant fixed, ρ_C, θ and C_res divide by l²; both scale formulas remain unchanged.
- Reexpressing channels by L↦sL and τ↦tτ requires a_m↦a_m/t and b_m↦b_m/s. Then χ↦s²χ, g_L↦(s³/t)g_L and r↦(s/t)r, leaving κ and the displayed boundary ratio unchanged.
- At marked endpoint exchange μ²=−1, r changes sign and ρ_C is unchanged. With N held fixed and ξ defined as its actual endpoint boundary, k is unchanged and c_+ changes sign. Transport of a separately normalized ξ is a different convention.

An independent determinant-frame change must not be confused with changing only a pairing-defined cross operator while retaining its identification with the algebraic M=i_vL.

## 23.5 The published (2,2) necessary quotient list

This separate Gauss refinement concerns a hypothetical maximal rank-three profile (2,2). Write K=E⁻, L=(Q*)⁻, A_q=E/K and B_q=Q*/L for the full derivative quotients. The labels A_q,B_q here avoid confusion with the quadratic direction space A and adjoint bundle B above. No cubic or quadratic subimage is substituted for these quotients.

Negative transpose gives an injective equal-rank map A_q→B_q*(−2) with torsion length

    t=−6−deg A_q−deg B_q.

Strict top-degree decrease in both negative towers gives deg A_q≥−12 and deg B_q≥−24. Its invariant determinant divisor initially allows t∈{0,12,20,24,30}. Exhaustive formal representation and degree constraints reduce this to t=0 or 12. At zero the injection is an isomorphism. At twelve the divisor is the unique reduced orbit of size twelve; local elementary divisors are (1,1,z), so the induced quotient map has fiber rank two there.

The published calculation retains 2,947 necessary records, 35 ordered quotient pairs, 26 of the 28 formal primal types and 35 of the 37 formal dual types. There are 2,688 defect-zero records and 259 defect-twelve records; each quotient side has 28 distinct splitting shapes. The calculation exhausts the possible rank-three representation blocks in proved degree windows and applies necessary character, Hom and ordinary injection inequalities. The proof explains why each filter is necessary; the script is not a realizability test.

This is an overlist, not a construction or exclusion of (2,2). The remaining possible maximal profiles are still (1,1), (1,2), (2,1), (2,2). SF≥3 and square rank≥27 are unchanged. The next section gives the now-published exact-kernel refinement. [Published quotient theorem][GAUSS]; [compact distribution][SUMMARY]

## 23.6 Exact kernels refine the list to 34 pairs

At the next checked pin, full negative-kernel splitting and exact cohomology compatibility reduce the preceding overlist to 1,880 records and 34 ordered quotient pairs, using 25 primal and 33 dual types. There are 1,723 defect-zero records and 157 defect-twelve records. These remain necessary possibilities, not sheaf-extension existence or realized profiles. [Exact-kernel refinement][KERNEL]

For either 0→N_k→F_k→C_k→0, with N_k=K or L, all kernel degrees are at most −3. Thus H¹(N_k(2))=χ(C_k(2))−χ(F_k(2)). Blocks R O(−j), j≥4, contribute R⊗Sym^(j−4)W. Their total dimension is at most thirty, giving j≤33 and a finite exhaustive enumeration. The degree −3 coefficient is forced by χ(N_k(3))+H¹(N_k(3)); it must be genuine, center-odd, and contained in H⁰(C_k(1)). This splitting step alone removes no quotient pair.

For each splitting and source type, exact cohomology then requires all three characters

    X=H⁰(F_k(t))−H⁰(N_k(t)),
    Y=H⁰(C_k(t))−X,
    Z=H¹(F_k(t))−H¹(C_k(t))

to be genuine; Euler exactness identifies H¹(N_k(t))=Y+Z. The tested window −30≤t≤34 is exhaustive for these character conditions: below it all H⁰ vanish and above it all H¹ vanish. These are necessary image conditions, not a construction of the exact sequence.

The eliminated pair has A_q=W O(−7)⊕O(16), B_q=O(−18)⊕W O(5). Every one of the 28 possible E types has no A3=Sym²W in H¹(E(2)), but H¹(A_q(2))=W⊗Sym³W=A3⊕D5. The quotient E→A_q would force a surjection on H¹ because H²(K(2))=0. Semisimplicity makes this impossible. This independently explains the pair exclusion without any actual map evaluation. [Standalone exclusion][EXCLUDE]

For each of the seven defect-twelve quotient pairs, the equivariant cokernel, if realized, is uniquely O_D(2) or O_D(6), with exponent modulo ten. The C10 stabilizer on the reduced twelve-point orbit has only five center-even line characters. The identity χ_G(O_D(s+t))=χ_G(O(s+t))−χ_G(O(s+t−12)), compared with the exact quotient character at t=0,…,9, selects exactly one of them. The character result already holds for all 259 defect-twelve records in the earlier overlist; the refined 157 inherit it. No further pair is excluded. [Orbit cokernel characters][TORSION]

## 23.7 Source-dependent operator transport and Euler–Koszul channels

Fix the actual first-normal operator, bundle, source and determinant markings, together with the prescribed harmonic symbol/scalar completion through q². Its weight-zero second-normal adjoint transport defect defines a class on the vertex cover in

    J_η(4)=P4 O_L(−4),
    H¹(J_η(4))=P4⊗A=V⊕P4⊕D5.

This is a twelve-dimensional target with no invariant vector, not an automatic vanishing theorem for a source-parametrized family. The coefficient sequence 0→V O_L(−6)→J_η(4)→O_L(2)→0 is nonsplit. Scalar classes in O_L(2) have zero H¹, but their three-dimensional H⁰ and prescribed local coefficients cannot be silently discarded. [Actual transport class][OPERATOR]

With Dq=ρq, write T_P(A)=PAP⁻¹−H(DP)P⁻¹ and A_j=T_Pij(A_i)+q²a_ij modulo q³. If a cycle product is I+q²C, the transported defect sum is H0(D+2ρ)C+[A0,C]. A regular adjoint C starts at chain weight −2, while the cone operator starts at four, so the weight-zero sum vanishes. This proves the cocycle property without constructing a globally glued third-neighborhood bundle. Changes of second-normal transition lifts have no weight-zero effect; changes of operator lifts give a coboundary. Independence holds relative to the fixed symbol/scalar completion, not arbitrary changes of it. The physical coefficient line retains its q-frame weight and the 2ρ term.

Its contribution h2 Dn+[a2,n]−λ2n is invisible to scalar differentiated-square constraints, since tr(nDn)=tr(n[a2,n])=tr(n²)=0. The actual class still requires the conic-selected K4 and complete endpoint η transport. Changing a marked cone representative by ℓN̂ shifts the raw class by ℓ[Z0], rather than zero. Only the restricted lower-centralizer case ℓ=aρ_source is already licensed by the ambient chain to disappear in the final second-symbol quotient. An arbitrary ℓ is not covered.

The source representation Sym³A⊗D5=3A⊕3V⊕3P4⊕4D5 gives ten universal coefficient channels. Let

    F3=Hom_G(D5,P4⊗A⊗Sym³A*),   dim F3=10,
    F4=Hom_G(D5,P4⊗Sym⁴A*),     dim F4=5,
    c(T)=⟨a,T⟩,   s(Q)=grad_a(Q)/4.

For the fixed invariant pairing and compatible volume, Euler and curl give the canonical decomposition

    T=(1/4)grad(c(T))+a cross R,
    R=−curl(T)/4,   div R=0.

Thus F3=s(F4)⊕K is a canonical five-plus-five splitting. The quadratic divergence-free R is unique: curl(a cross R)=a div R−4R. Equivalently the six-dimensional quadratic vector space is divided by its one-dimensional radial subspace; div(aℓ)=4ℓ fixes the representative. [Euler–Koszul splitting][EULER]

For the actual second symbol β2_a, the unique quadratic source family ℓ2(a,h)=a cross S_h(a) gives a nonzero factoring family B_fac=β2_a(ℓ2). Nonvanishing uses sheaf-injectivity of the actual second symbol, not merely two nonzero factors. The final universal map F3→F4/(C B_fac) has

    ker(c modulo C B_fac)=K⊕C grad(B_fac)/4,
    dimension 5+1=6.

The five Koszul directions have zero raw contraction; the sixth has nonzero contraction and vanishes only after the actual second-symbol quotient. No canonical complement to C B_fac in F4 is asserted. Neither the actual class coefficients nor the comparison with the actual next division has been computed. These channel descriptions do not evaluate a fourth obstruction.

## 23.8 Evidence and the open boundary

The lift and scale proofs were read in full, independently audited, and their two proof texts and two verifiers matched exact published readbacks before integration. Their companion checks pass with free coefficients. They check source-gauge signs, natural/reduced algebra, trace constants, rank-two Cayley–Hamilton and equation/frame covariance; they use no actual-instance coefficient assignment or matrix-rank experiment. These are supplementary checks, not proof-assistant certificates.

The canonical actual 2Q lift and endpoint-scale ratios do not perform qv_h=ahζ_a, assemble the remaining higher-weight endpoint comparison, or evaluate the fourth Bockstein. They do not contradict the obstruction to the specified midpoint nilpotent extension. General sections remain four or five, the finite last Smith exponent is 4–31 or the cokernel is permanent, and the original source-recovery, lifting and Weil-class algebraicity goals remain open. The operator and Euler–Koszul results below are included; later lift-coherence drafts are not incorporated.

The exact-kernel, standalone exclusion, orbit-character, operator-class and Euler–Koszul proofs were read and independently audited before integration; their verifiers passed and eleven immutable published readbacks matched exactly. The kernel audit also checked a wider twist range. These checks retain the necessary-only and uncomputed-actual-class boundaries.

## Immutable source ledger and reproduction

All paths below are in research/hm/order-four-quadratic-load in PR543. Run companion scripts there with their published imported helpers.

- At `3333cce744b3bd8e4472969f599588fec3e20d52`: [canonical actual multiplied lift][LIFT] and [lift verifier][LIFTV]; [fixed-boundary endpoint scale][SCALE] and [scale verifier][SCALEV].
- At `fa239126cdfe19839a54e89a3d2911e5be476fcb`: [(2,2) quotient proof][GAUSS], [quotient verifier][GAUSSV], and [compact checked summary][SUMMARY]. The full generated record file is reproducible; no map realization is inferred.

- At `10df28e8c87f5c9d156e394f235f6b00e34144d0`: [kernel proof][KERNEL] and [verifier](https://github.com/Akilleez-QA/read-em-and-weep/blob/10df28e8c87f5c9d156e394f235f6b00e34144d0/research/hm/order-four-quadratic-load/verify_two_two_exact_kernel_splittings.py); [exclude proof][EXCLUDE] and [verifier](https://github.com/Akilleez-QA/read-em-and-weep/blob/10df28e8c87f5c9d156e394f235f6b00e34144d0/research/hm/order-four-quadratic-load/verify_two_two_seven_w_quotient_exclusion.py); [torsion proof][TORSION] and [verifier](https://github.com/Akilleez-QA/read-em-and-weep/blob/10df28e8c87f5c9d156e394f235f6b00e34144d0/research/hm/order-four-quadratic-load/verify_two_two_twelve_orbit_torsion_characters.py); [operator proof][OPERATOR] and [verifier](https://github.com/Akilleez-QA/read-em-and-weep/blob/10df28e8c87f5c9d156e394f235f6b00e34144d0/research/hm/order-four-quadratic-load/verify_second_normal_operator_transport_class.py); [euler proof][EULER] and [verifier](https://github.com/Akilleez-QA/read-em-and-weep/blob/10df28e8c87f5c9d156e394f235f6b00e34144d0/research/hm/order-four-quadratic-load/verify_transport_channel_euler_koszul_splitting.py); [compact 34-pair summary](https://github.com/Akilleez-QA/read-em-and-weep/blob/10df28e8c87f5c9d156e394f235f6b00e34144d0/research/hm/order-four-quadratic-load/two-two-exact-kernel-summary.json).

[LIFT]: https://github.com/Akilleez-QA/read-em-and-weep/blob/3333cce744b3bd8e4472969f599588fec3e20d52/research/hm/order-four-quadratic-load/ACTUAL-MULTIPLIED-NILPOTENT-HAS-A-CANONICAL-SQUARE-ZERO-LIFT.md
[LIFTV]: https://github.com/Akilleez-QA/read-em-and-weep/blob/3333cce744b3bd8e4472969f599588fec3e20d52/research/hm/order-four-quadratic-load/verify_actual_multiplied_nilpotent_square_zero_lift.py
[SCALE]: https://github.com/Akilleez-QA/read-em-and-weep/blob/3333cce744b3bd8e4472969f599588fec3e20d52/research/hm/order-four-quadratic-load/ACTUAL-ENDPOINT-SCALE-FROM-THE-CARTAN-KOSZUL-MULTIPLIER.md
[SCALEV]: https://github.com/Akilleez-QA/read-em-and-weep/blob/3333cce744b3bd8e4472969f599588fec3e20d52/research/hm/order-four-quadratic-load/verify_actual_endpoint_scale_from_cartan_multiplier.py
[GAUSS]: https://github.com/Akilleez-QA/read-em-and-weep/blob/fa239126cdfe19839a54e89a3d2911e5be476fcb/research/hm/order-four-quadratic-load/TWO-TWO-SYMMETRIC-QUOTIENT-DEFECT-IS-ZERO-OR-TWELVE.md
[GAUSSV]: https://github.com/Akilleez-QA/read-em-and-weep/blob/fa239126cdfe19839a54e89a3d2911e5be476fcb/research/hm/order-four-quadratic-load/verify_two_two_symmetric_quotient_constraints.py
[SUMMARY]: https://github.com/Akilleez-QA/read-em-and-weep/blob/fa239126cdfe19839a54e89a3d2911e5be476fcb/research/hm/order-four-quadratic-load/two-two-symmetric-quotient-summary.json

[KERNEL]: https://github.com/Akilleez-QA/read-em-and-weep/blob/10df28e8c87f5c9d156e394f235f6b00e34144d0/research/hm/order-four-quadratic-load/TWO-TWO-EXACT-NEGATIVE-KERNEL-SPLITTING-REFINEMENT.md
[EXCLUDE]: https://github.com/Akilleez-QA/read-em-and-weep/blob/10df28e8c87f5c9d156e394f235f6b00e34144d0/research/hm/order-four-quadratic-load/TWO-TWO-SEVEN-W-QUOTIENT-IS-EXCLUDED-BY-EXACT-COHOMOLOGY.md
[TORSION]: https://github.com/Akilleez-QA/read-em-and-weep/blob/10df28e8c87f5c9d156e394f235f6b00e34144d0/research/hm/order-four-quadratic-load/TWO-TWO-TWELVE-ORBIT-COKERNEL-HAS-WEIGHT-TWO-OR-SIX.md
[OPERATOR]: https://github.com/Akilleez-QA/read-em-and-weep/blob/10df28e8c87f5c9d156e394f235f6b00e34144d0/research/hm/order-four-quadratic-load/ACTUAL-SECOND-NORMAL-OPERATOR-TRANSPORT-HAS-A-SOURCE-PARAMETRIZED-CLASS.md
[EULER]: https://github.com/Akilleez-QA/read-em-and-weep/blob/10df28e8c87f5c9d156e394f235f6b00e34144d0/research/hm/order-four-quadratic-load/ACTUAL-TRANSPORT-CHANNEL-KERNEL-HAS-AN-EULER-KOSZUL-SPLITTING.md
