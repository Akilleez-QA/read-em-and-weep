# 26. Asymmetric quotients and the coupled Cartan frontier

**Checked-source edition: 22 October 2026, 09:40 UTC.** The section-count theorem remains four or five. This chapter adds the initial 25-pair necessary list for (1,2), its endpoint refinement to ten pairs, a profile-independent primal degree improvement, exact partial-primitive interfaces, and restricted next-division exclusions including the all-four-source Cartan comparison. None excludes (1,2), proves SF≥4, evaluates the fourth obstruction, or completes the original source-recovery, higher-lifting or Weil-class algebraicity objectives. Chapter 25.3 records the earlier bounds; the results here supersede its open original twelve-defect branch, not its historical proof.

## 26.1 Twenty-five necessary quotient pairs, not realizations

Write K=E⁻, A=E/K, L=(Q*)⁻, B=Q*/L and a=deg A, b=deg B. For the hypothetical maximal rank-three profile (1,2), the original transpose injection is an isomorphism:

    A ≅ B*(−2),     t=−6−a−b=0.

The initial theorem gives at most **25 ordered equivariant splitting pairs (A,B)**, and **155 compatible pair/E-type records**, involving 25 of the 28 proven formal E types. These are necessary overlists, not constructed quotient maps or realizations. The pair count and record count are different denominators; neither can be added to the nine-profile universe or to the historical (2,2) inventories. [Finite-pair proof][PAIRS]

The finite windows follow from actual bundle bounds. Every line degree of A lies in [−10,26]; every line degree of B lies in [−28,8]. A center-even rank-three equivariant splitting is three even-degree trivial-coefficient lines, an odd-degree W or W′ block plus an even-degree line, or a single even-degree A_std or V block. No splitting list for Q*, no H⁰(Q*(1)) vanishing, and no rank-three assertion at an endpoint is imported.

The initial necessary Euler tests leave 154 A shapes and 228 B shapes. Actual quotient cohomology gives

    H¹(B(r)) ≤ −χ_G(Q*(r)),       r=−2,−1,0,

reducing the B list to 91. For each proven E type one also imposes H⁰(E(2))≤H⁰(A(2)), H⁰(E(3))≤H⁰(A(3))+H⁰(A(1)), and H¹(A(r))≤H¹(E(r)) for −2≤r≤8. Inequalities mean nonnegative irreducible multiplicities in the difference. Necessary block-Hom and ordinary degree inequalities are imposed without treating nonzero Hom as an injective or surjective map.

Before the added quotient-cohomology inequalities, just five original twelve-defect pairs remain. Each B contains a trivial-coefficient O(−14) or O(−26). Its H¹ contains a trivial representation, whereas

    H¹(Q*) = A_std ⊕ 2V ⊕ 3P4 ⊕ 4D5

has none. The required H¹(Q*)→H¹(B) surjection is impossible. This is an independent five-case saturation certificate for t=0.

The initial 25 pairs, subsequently refined in Section 26.8, are specified by the following complete list of A; in every entry B=A*(−2):

    O(−10)⊕O(−8)⊕O(14)
    O(−10)⊕O(−8)⊕O(16)
    O(−10)⊕O(2)⊕O(4)
    O(−10)⊕O(2)⊕O(6)
    O(−10)⊕2O(4)
    O(−10)⊕O(4)⊕O(6)
    2O(−8)⊕O(14)
    O(−8)⊕O(2)⊕O(4)
    O(−8)⊕O(2)⊕O(6)
    O(−8)⊕O(4)⊕O(6)
    O(−8)⊕O(4)⊕O(8)
    O(−8)⊕2O(6)
    W O(−9)⊕O(14)
    W O(−9)⊕O(16)
    W′ O(−3)⊕O(4)
    W′ O(−3)⊕O(6)
    W′ O(−1)⊕O(2)
    W′ O(−1)⊕O(4)
    W′ O(−1)⊕O(6)
    V O(0)
    O(−10)⊕W O(3)
    O(−8)⊕W O(3)
    O(−8)⊕W′ O(3)
    O(−10)⊕W O(5)
    O(−8)⊕W O(5).

The [compact records][PAIRDATA] supply compatible E IDs and dependency hashes. Further necessary tests may shorten this list without contradicting the present result.

## 26.2 Mr. Slop's independent degree bound and the distinct second-dual defect

Mr. Slop's [PR674 proof][DEGREE] proves **a≥−4 for every maximal rank-three profile**, not only (1,2). The argument starts from a≥−8, even parity, and two genuine-character envelopes:

    C2(A)=χ_G(A(2))+V,
    C3(A)=H⁰(A(1))+χ_G(A(3))−(W′+2T).

The second uses H⁰(K(3))→H⁰(A(1)) injective, which follows from strict top-slope decrease without imposing a plateau rank at the endpoint. At a=−8 all six elementary candidates fail C3. At a=−6 the two envelopes leave three necessary types, each containing O(12).

Actual transpose incidence embeds A into Q(−2). But a nonzero invariant form f12 gives an injective multiplication H⁰(Q(−14))^G→H⁰(Q(−2))^G=0. The vanishing on the right follows by equivariant Serre duality from the absence of a trivial summand in H¹(Q*). Consequently O(12) cannot map to Q(−2), excluding a=−6. The multiplier may have zeros: injectivity uses that it is a non-zero-divisor on a vector bundle, not that it is nowhere zero.

For (1,2), combine a≥−4 with b≥−12 to obtain t≤10. An invariant nonempty divisor has degree at least twelve, so t=0. This overlaps the preceding five-case certificate and is **not an additional elimination to count twice**. All 25 listed pairs already satisfy a≥−4. The new finite-pair contribution is the explicit 25-pair/155-record necessary classification; PR674 supplies the stronger profile-independent theorem.

The second dual derivative is different. Put M=L⁻, J=L/M and let s be the determinant length of J→B(−2). Then

    −4≤a≤6,     b=−6−a,
    0≤s≤14−2a,     deg M=−36+2a+s.

PR674's complete initial necessary degree table retains the twenty-point orbit; Section 26.8 subsequently excludes every such branch:

| a | b | possible s | corresponding deg M |
| --- | --- | --- | --- |
| −4 | −2 | 0, 12, 20 | −44, −32, −24 |
| −2 | −4 | 0, 12 | −40, −28 |
| 0 | −6 | 0, 12 | −36, −24 |
| 2 | −8 | 0 | −32 |
| 4 | −10 | 0 | −28 |
| 6 | −12 | 0 | −24 |

Thus original defect zero does not erase the distinct second-dual defect; in particular **s=20 at a=−4 remains possible under PR674's constraints alone**. This is a necessary table, not a realization claim; the endpoint/orbit theorem in Section 26.8 supplies the additional exclusion.

## 26.3 Positive Atiyah differentiation supplies a partial primitive, not the division

The checked positive-interface result retains the natural moving Cartan projector, actual cubic identification f, channel coefficients and determinant frame. For positive selfadjoint trace-free H, h=(1/2)D_Hq, the full actual coefficient tensor is

    B* δ_H C = −c Ĥ p_C(w).

It is a nonzero equivariant tensor D5⊗A→U⊗W=P4 and hence surjects onto that irreducible coefficient space. This does not assert surjectivity or nonvanishing in the final cohomology quotient. Its Cartan compression satisfies

    C_H²=(tr_V(H²)/6)I,
    C_H C_K+C_K C_H=(tr_V(HK)/3)I.

The off-diagonal spin/Cartan component is essential; a compression-only replacement loses it. Natural differentiation includes δ_HΠ=[Ĥ,Π], rather than holding the projector fixed. [Positive interface][ATIYAH]

A concrete global fixed-duality partial primitive G_(a,h) is constructed with middle component aρ²(hD_a−R_h⊗(wD_a)) and the indicated A→U source block. Its closed residual E_(a,h)=dG_(a,h)−ah e_a has exactly two explicit arrow columns. The remaining equation is

    kE_(a,h)+dJ_h=−qV_h,     C_h=kG_(a,h)+J_h.

Literal q-divisibility makes V_h closed because multiplication by q is injective on the locally free chain-Hom terms. The result specifies this equation and partial primitive; it does not supply J_h or V_h. Abstract primitive existence from earlier chapters is not an explicit evaluated primitive.

## 26.4 Higher Cartan lifts are not multiplicative

For an End(P)-valued negative homogeneous symbol S of degree d>0, the regular global skew lift is

    T_d(S)(η)=(1/d)Σ_i i_x[e_i∧E_(∂_iS)(η)].

It kills the full B-channel and has positive Cartan A-column SΠ(A). For quadratic f and S the exact multiplication correction is

    Δ(f,S)=T_4(fS)−fT_2(S)
          =(1/8)j∧i_x E_({f,S}_ω),     j=i_wω.

Every such correction is square-zero, and any two have product zero. Its compressed positive block is zero, but the full operator can be nonzero. Therefore replacing multiplication of a quadratic lift by rebuilding a quartic lift without Δ changes the cochain. These universal identities neither solve the residual equation nor show that source components can be omitted. [Higher-lift proof][HIGHER]

## 26.5 Two restricted Cartan constructions are excluded

The first exclusion concerns the pure right-Clifford-factor family. With J_v=ρ³(M(v)) and F_v=J_v²−χqI, the family S(v,w)=R(w)F_v gives a global skew lift annihilating both full U-source channels. Nevertheless its c-column cannot satisfy the required congruence with only its specified source-AA correction. Quotienting by the negative osculating hyperplane removes that source correction; the complete binary transvectant identity forces the remaining row to vanish, contradicting the nonzero ah term. This holds for every nonzero a and positive trace-free h, not merely for equivariant R. It excludes this sufficient construction, not actual division. [Right-factor exclusion][FACTOR]

The full quadratic Cartan principal-symbol space is larger. Its global factorization on the null conic is

    S(v)=B(v)Ā(v)† mod q,
    B(v)=R Ā(v)+Z M(v).

The missing spin interface is Hom(U,P)=V⊕D5. The actual positive off-diagonal derivative has a nonzero D5 component there. This global quotient-bundle factorization is not a classification of all middle homotopies. Source-A→U corrections contribute in both monad channels, with neighboring bidegrees that must be balanced, including legitimate source-AA terms. [Full principal interface][SPIN]

The second exclusion is stronger but still restricted: **an arbitrary polynomial middle Cartan symbol satisfying SĀ=0 on q=0 cannot solve the principal c-column when only source-AA and source-A→U blocks are retained**. It uses the actual smooth invariant bicubic, its two disjoint reduced twelve-point ramification orbits, and their Lagrangian tangent planes. At least six ramification pairs avoid the zeros of any fixed nonzero a and h. At such a variable pair, both source corrections vanish in the osculating quotient, while the imposed annihilation kills the middle term and leaves a nonzero −2a(w)²h(r²)z(w). This is a uniform geometric argument, not evaluation of a selected source instance. [Ramification exclusion][RAM]

The two no-go statements are nested restrictions, not two obstructions to unrestricted division. A successful explicit construction must retain a nonzero principal U-column balance through additional coupled source/middle terms, or leave the stated Cartan principal comparison. The actual fourth value remains unevaluated.

### All four source blocks still require complementary middle transport

The subsequent strengthening removes the imposed annihilation SĀ=0 and permits all four source blocks. It excludes any proposed middle operator T for which one common symbol S gives all three projected arrow actions

    π(TA)=SĀ,     π(TB)=0,     π(TC)=Sp_C.

At the same variable ramification pair, the full U-column balance forces λSĀ=0. Choose an input with p_C(w,z) in im Ā but not in the negative tangent plane. The full c-column balance then requires λSp_C(w,z)=2a(w)²h(v)z(w)≠0, a contradiction. Every source-block image is killed by λ; no source block is silently omitted. This excludes canonical Cartan-only lifts satisfying the displayed common-action hypothesis, not arbitrary middle operators. [Complementary-middle proof][MIDDLE]

For the unrescaled actual primitive, retain Z_a=k e_a and define comparison errors

    E_A=π(TA)−SĀ,     E_B=π(TB),     E_C=π(TC)−Sp_C.

Whenever the marked inputs satisfy p_C(w,z)=Ā(v,u), the exact necessary interface value is

    λ(E_C(z)−E_A(u)−(b_m/a_m)E_B(u))
        =2k a(w)²h(v)z(w).

The symbol S cancels and all channel ratios and the fixed Atiyah scalar remain. This nonzero required combination is not a computation of its individual blocks or of the fourth obstruction. At least one of the three common-action equalities must fail. A spin-VV→Cartan-VV block is one possible mechanism; mixed-form→Cartan-VV transport is another, and both may coexist. Thus the theorem does not require mixing different exterior-form sectors. The full middle operator and actual divided class remain unconstructed.

## 26.6 Separate geometry: the normal-enhanced blowup

Mr. Slop's [PR673][BLOWUP] gives a separate consequence of the already established multiplied-lift coherence. On X=2Q away from C=(s=t=0), the image family defines an invertible abstract adjoint-line subsheaf L⊂B_X(2). Its generators satisfy

    n_t=(1−2κq/(st))n_s,
    [L]=−2κ[1/(st)] ≠ 0 in H¹(Q∖C,O(−2)).

The Picard class and H¹(Q,O_Q(−2))=0 obstruct an invertible extension over X. Blowing up the multiplier ideal I=(s,t) does not resolve the deformed negative projection z′=t/s−κq/s²; it is not the blowup of the reduced-center ideal (s,t,q).

The normal-enhanced ideal J=I²+(q) does resolve both projections. On its s²-chart, z=t/s and η=q/s² are regular with η²=0; the deformed coordinate is z−κη. The line extends as (p′_Y)*O(2)⊗p_Y*O(−2), together with an injective abstract adjoint-line embedding and square-zero generators. The quotient need not be locally free: this is not a line subbundle, a spinor kernel, a 3Q extension, or a next-division solution. This geometric result does not alter any profile or record count.

## 26.7 Evidence, related work and remaining objectives

The new finite counts concern exact abstract character arithmetic and necessary bundle constraints. The Cartan checks are complete free-coefficient identities; the geometric arguments above supply the passage from identities to conclusions. None is a proof-assistant certificate or an actual-instance rank scan. The [related-work comparison](related-work-horrocks-mumford.md) distinguishes established methods and HM geometry from the particular marked statements, and makes no certified novelty or priority claim.

Six of nine maximal rank-three profiles remain excluded, with (1,1), (1,2), (2,1) still possible. SF≥3, square rank≥27, the four-or-five section theorem, and the finite Smith exponent range 4–31 (or permanent cokernel) are unchanged. Evaluating the actual divided class and fourth gate, deciding four versus five, and the original repair objectives remain open.

## 26.8 Endpoint and orbit constraints refine the asymmetric overlist

The subsequent endpoint theorem uses PR674's profile-independent degree bound and second-dual table, together with the 25-pair list in Section 26.1. It leaves **ten necessary quotient pairs, 38 endpoint/defect records, and 52 inherited pair/E-type records**. It excludes every second-dual s=20 branch. Thus Section 26.2 correctly retains s=20 within PR674's initial table; the further constraints here exclude it, rather than silently deleting a legitimate earlier possibility. [Endpoint proof][ENDPOINT]

Keep M=L⁻, J=L/M and T=coker(J→B(−2)). The rank-seven endpoint M has highest splitting degree at most −3, and its derivative factors through J(−2)⊂B(−4). If its top degree is −d, strict top-slope decrease gives the section injection

    H⁰(M(d)) → H⁰(B(d−4)).

No endpoint derivative rank is assumed. The exact Euler identity is

    χ_G(M(t))=χ_G(Q*(t))−χ_G(B(t))−χ_G(B(t−2))+H⁰(T(t)).

For s=12 or 20, the determinant divisor is the single reduced invariant orbit of that size. Its binary stabilizer is cyclic of order ten or six respectively. Center-even equivariant line sheaves on it are exhausted by T=O(k)|D_s, with k=0,2,4,6,8 for s=12 and k=0,2,4 for s=20. The invariant divisor sequence supplies

    H⁰(T(t))=χ_G(O(k+t))−χ_G(O(k+t−s)).

These are conservative possibilities for a torsion sheaf, not constructed quotients. Since deg M≥−44, every splitting block R O(−j) lies in the proved finite window 3≤j≤26: its excess contributes (j−3)dim R to a total at most 23. The complete top-degree and Euler tests leave fourteen old pair IDs and 53 endpoint records, already excluding all s=20 cases. The tested twists 0 through 26 are redundant checks, not an empirical cutoff; the equivariant Euler recurrence determines the characters from two consecutive twists.

A further backward rank-one test uses only universal Hom characters. A rank-zero reachable target would make the negative saturated endpoint horizontal and is impossible. If the total reachable target is a single line O(c), the derivative has rank exactly one. Its backward flag has

    deg M=7h−42−Σ_(i=1)^6 iδ_i,     h≤c,     h even.

The internal gaps δ_i and final gap c−h lie in the invariant-divisor semigroup generated by 12,20,30. The degree budget makes this a finite necessary test. It excludes fifteen endpoint records and all records for four further pairs, leaving ten. No analogous endpoint rank-two or rank-three premise is imposed.

The final list uses the zero-based IDs of the frozen 25-pair JSON. In every row B=A*(−2); the columns count distinct necessary M splitting types by second-dual defect, not actual maps.

| Old ID | A | s=0 | s=12 |
| --- | --- | ---: | ---: |
| 0 | O(−10)⊕O(−8)⊕O(14) | 6 | 2 |
| 2 | O(−10)⊕O(2)⊕O(4) | 1 | 1 |
| 4 | O(−10)⊕2O(4) | 0 | 1 |
| 6 | 2O(−8)⊕O(14) | 2 | 2 |
| 7 | O(−8)⊕O(2)⊕O(4) | 2 | 2 |
| 8 | O(−8)⊕O(2)⊕O(6) | 1 | 0 |
| 12 | W O(−9)⊕O(14) | 6 | 2 |
| 14 | W′ O(−3)⊕O(4) | 2 | 3 |
| 20 | O(−10)⊕W O(3) | 1 | 0 |
| 21 | O(−8)⊕W O(3) | 2 | 2 |

The endpoint totals are **23 with s=0 and 15 with s=12**, hence 38. Original defect t remains zero in every case. Old pair 4 requires second-dual defect twelve; old pairs 8 and 20 require second-dual defect zero. The 52 inherited pair/E records are a separate denominator and have not passed actual extension or map-realization tests.

The fixed necessary-pair history is **25→14→10**, while endpoint records go **53→38** after the first endpoint/orbit stage. These counts must not be combined with the nine maximal profiles, the earlier (2,2) universes, or with one another. The (1,2) profile remains open, and SF≥3, square rank≥27, four-or-five sections and all original-repair boundaries remain unchanged. The [endpoint record file][ENDPOINTDATA] records the exhaustive finite windows, surviving types and dependency hashes; the [verifier][ENDPOINTV] supplements the geometric necessity arguments.

## Immutable source ledger and reproduction

- PR543 at c0b88ea01fa4e0ca57d8e289b236aece9258670b: [finite-pair proof][PAIRS], [record file][PAIRDATA], and [verifier][PAIRV]; [right-factor proof][FACTOR] and [verifier][FACTORV]; [ramification proof][RAM] and [verifier][RAMV].
- PR543 at b2c4239ab1f72b94c2630fb16dcb3665d7d47fdb, the checked positive-Atiyah/higher-Cartan package: [positive interface][ATIYAH] and [verifier][ATIYAHV]; [higher-lift proof][HIGHER] and [verifier][HIGHERV].
- PR543 at 857cd414252618a53a79ddce72982c6d91341db9: [endpoint/orbit proof][ENDPOINT], [verifier][ENDPOINTV], and [records][ENDPOINTDATA]; [full spin interface][SPIN] and [verifier][SPINV]; [all-four-source complementary-middle proof][MIDDLE] and [verifier][MIDDLEV].
- Mr. Slop, PR674 at 2516a879b4b1469da1a29eaefafcfddf4e171a0d: [complete primal-bound proof][DEGREE] and [exact-character verifier][DEGREEV]. Its overlapping t=0 conclusion is credited separately, not counted again.
- Mr. Slop, PR673 at c7e43fc22249bce7cd2abad0551c5173ed831404: [complete geometric proof][BLOWUP] and [chart-identity verifier][BLOWUPV].

Run each linked Python verifier with the pinned dependencies named in its source. The finite-pair verifier produces the initial 25-pair/155-record JSON; the endpoint verifier refines it to ten pairs, 38 endpoint records and 52 inherited pair/E records; it does not construct any actual quotient. The other scripts supplement the authored geometric and operator proofs, not replace them.

[PAIRS]: https://github.com/Akilleez-QA/read-em-and-weep/blob/c0b88ea01fa4e0ca57d8e289b236aece9258670b/research/hm/order-four-quadratic-load/ONE-TWO-FINITE-QUOTIENT-PAIRS-AND-ZERO-DEFECT.md

[PAIRDATA]: https://github.com/Akilleez-QA/read-em-and-weep/blob/c0b88ea01fa4e0ca57d8e289b236aece9258670b/research/hm/order-four-quadratic-load/one-two-finite-quotient-pairs.json

[PAIRV]: https://github.com/Akilleez-QA/read-em-and-weep/blob/c0b88ea01fa4e0ca57d8e289b236aece9258670b/research/hm/order-four-quadratic-load/verify_one_two_finite_quotient_pairs.py

[FACTOR]: https://github.com/Akilleez-QA/read-em-and-weep/blob/c0b88ea01fa4e0ca57d8e289b236aece9258670b/research/hm/order-four-quadratic-load/CLIFFORD-FACTORED-CARTAN-LIFTS-CANNOT-SOLVE-THE-PURE-C-COLUMN.md

[FACTORV]: https://github.com/Akilleez-QA/read-em-and-weep/blob/c0b88ea01fa4e0ca57d8e289b236aece9258670b/research/hm/order-four-quadratic-load/verify_clifford_factored_cartan_principal_obstruction.py

[SPIN]: https://github.com/Akilleez-QA/read-em-and-weep/blob/857cd414252618a53a79ddce72982c6d91341db9/research/hm/order-four-quadratic-load/CARTAN-PRINCIPAL-SYMBOLS-REQUIRE-THE-FULL-SPIN-INTERFACE.md

[SPINV]: https://github.com/Akilleez-QA/read-em-and-weep/blob/857cd414252618a53a79ddce72982c6d91341db9/research/hm/order-four-quadratic-load/verify_cartan_principal_symbols_with_coupled_sources.py

[RAM]: https://github.com/Akilleez-QA/read-em-and-weep/blob/c0b88ea01fa4e0ca57d8e289b236aece9258670b/research/hm/order-four-quadratic-load/ACTUAL-RAMIFICATION-FORCES-A-NONTRIVIAL-PRINCIPAL-U-SOURCE-CORRECTION.md

[RAMV]: https://github.com/Akilleez-QA/read-em-and-weep/blob/c0b88ea01fa4e0ca57d8e289b236aece9258670b/research/hm/order-four-quadratic-load/verify_actual_ramification_forces_principal_u_correction.py

[ATIYAH]: https://github.com/Akilleez-QA/read-em-and-weep/blob/b2c4239ab1f72b94c2630fb16dcb3665d7d47fdb/research/hm/order-four-quadratic-load/ACTUAL-POSITIVE-ATIYAH-DERIVATIVE-HAS-A-SURJECTIVE-P4-TENSOR.md

[ATIYAHV]: https://github.com/Akilleez-QA/read-em-and-weep/blob/b2c4239ab1f72b94c2630fb16dcb3665d7d47fdb/research/hm/order-four-quadratic-load/verify_positive_atiyah_cartan_offdiagonal_interface.py

[HIGHER]: https://github.com/Akilleez-QA/read-em-and-weep/blob/b2c4239ab1f72b94c2630fb16dcb3665d7d47fdb/research/hm/order-four-quadratic-load/UNIVERSAL-HIGHER-CARTAN-LIFTS-HAVE-A-SQUARE-ZERO-PRODUCT-ANOMALY.md

[HIGHERV]: https://github.com/Akilleez-QA/read-em-and-weep/blob/b2c4239ab1f72b94c2630fb16dcb3665d7d47fdb/research/hm/order-four-quadratic-load/verify_higher_cartan_lift_and_product_anomaly.py

[DEGREE]: https://github.com/Akilleez-QA/read-em-and-weep/blob/2516a879b4b1469da1a29eaefafcfddf4e171a0d/research/hm/primal-quotient-degree-bound/PROOF.md

[DEGREEV]: https://github.com/Akilleez-QA/read-em-and-weep/blob/2516a879b4b1469da1a29eaefafcfddf4e171a0d/research/hm/primal-quotient-degree-bound/verify.py

[BLOWUP]: https://github.com/Akilleez-QA/read-em-and-weep/blob/c7e43fc22249bce7cd2abad0551c5173ed831404/research/hm/adjoint-line-normal-blowup/CANONICAL-ADJOINT-LINE-AND-NORMAL-ENHANCED-BLOWUP.md

[BLOWUPV]: https://github.com/Akilleez-QA/read-em-and-weep/blob/c7e43fc22249bce7cd2abad0551c5173ed831404/research/hm/adjoint-line-normal-blowup/verify_adjoint_line_resolution.py

[ENDPOINT]: https://github.com/Akilleez-QA/read-em-and-weep/blob/857cd414252618a53a79ddce72982c6d91341db9/research/hm/order-four-quadratic-load/ONE-TWO-ENDPOINT-ORBIT-CONSTRAINTS.md

[ENDPOINTV]: https://github.com/Akilleez-QA/read-em-and-weep/blob/857cd414252618a53a79ddce72982c6d91341db9/research/hm/order-four-quadratic-load/verify_one_two_endpoint_orbit_constraints.py

[ENDPOINTDATA]: https://github.com/Akilleez-QA/read-em-and-weep/blob/857cd414252618a53a79ddce72982c6d91341db9/research/hm/order-four-quadratic-load/one-two-endpoint-orbit-constraints.json

[MIDDLE]: https://github.com/Akilleez-QA/read-em-and-weep/blob/857cd414252618a53a79ddce72982c6d91341db9/research/hm/order-four-quadratic-load/ACTUAL-NEXT-DIVISION-REQUIRES-COMPLEMENTARY-MIDDLE-TRANSPORT.md

[MIDDLEV]: https://github.com/Akilleez-QA/read-em-and-weep/blob/857cd414252618a53a79ddce72982c6d91341db9/research/hm/order-four-quadratic-load/verify_actual_next_division_complementary_middle.py
