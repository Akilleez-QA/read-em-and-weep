# Independent source-bound review of the closed-K obstruction

## Verdict

**Accepted.** In the actual pinned source, the common-frame one-form

    F = A_1 − 19 dlog(v1)

for the rational carrier pair (0,1) is nonzero. Its coefficient in the v1 direction is

    F(∂/∂v1) = −20/v1 + O(v1^−2).

Consequently the contraction scalar K of the compact first-order representative is not a Čech one-cocycle: on actual repeated-last-carrier triples its differential Λ=δK has a nonzero target-pair contraction. These same triples have Ω identically zero. The proposed removal of K/4 by first declaring K closed and then applying the scalar H1 argument is therefore unavailable.

The source/common-frame dependency left pending in the original note is resolved below. The coefficient 19 is obtained directly from the transported ambient split determinants. The counterargument does not require the global determinant-ratio gluing premise, any source point, any source polynomial evaluation, or a second-jet computation.

This does not contradict the later full-S4-sign boundary theorem. That theorem supplies a boundary for a projection of the **complete** raw remainder by a different cubic transgression, with the ambient contributions retained. It does not assert δK=0 or use the rejected closed-K shortcut.

There is one precise convention correction to the later S4 proof's normalization explanation: the actual common-ambient induced connection difference is −Lᵗ. A displayed additional scalar dlog(νj/νi) comes from comparing untransported prescribed-frame arrays and is not the same common-frame object. Its cubic trace and tracefree part are nevertheless the same, so this wording correction does not change the S4 primitive or its coefficient. Section 8 explains the distinction.

## 1. Frozen inputs and permitted checks

The six reviewed notes/checker were fetched at PR79 commit
`b4f62461e03491ceb0dccd910fd457c267a5b924`, under
`research/hm/null-source-integration/complete-raw-remainder/`:

- `source_pair_trace_obstruction.md`
- `source_diagonal_connections.md`
- `finite_mask_affine_pairing.md`
- `finite_weighted_trace_reduction.md`
- `curvature_descent_followup.md`
- `check_pair_trace_structure.py`

The reviewed bytes match the public blobs exactly; `source-pins.json` records their repository-relative paths, commits, Git blobs and SHA-256 digests. The source model and generator were authenticated independently against their canonical public copies at commit `10810ee877fdaf291399198ad60d7dd0c316a42d`:

- [Model](https://github.com/Akilleez-QA/read-em-and-weep/blob/10810ee877fdaf291399198ad60d7dd0c316a42d/research/hm/null-operator-compiler/hm-pinned-model.json), Git blob `fcd48a9a22d40d55ce7a08b8aefcb4eaa2fdf761`, SHA-256 `635bb12d9986e0dcada161d4173c773c4f134b9225354a3bc74267840ca19926`.
- [Generator excerpts](https://github.com/Akilleez-QA/read-em-and-weep/blob/10810ee877fdaf291399198ad60d7dd0c316a42d/research/hm/null-operator-compiler/hm-pinned-source-formulas.js), Git blob `3dfed53a28b53b3c912a097971d89fc547330a5f`.
- [First-order source](https://github.com/Akilleez-QA/read-em-and-weep/blob/08b73637d4136f91606aad332c46cafd064417f8/research/hm/current-scalar-residual-attribution/first-order-source.md), especially sections 1, 3 and 4.
- [Physical-frame theorem](https://github.com/Akilleez-QA/read-em-and-weep/blob/08b73637d4136f91606aad332c46cafd064417f8/research/hm/current-scalar-geometric-dependencies/frames-and-poles.md), especially sections 1, 2 and 4.

I read the supplied structural checker before running it, normally and with optimization. It passes in both modes. The independent `check_metadata_independent.py` also passes in both modes and produces identical receipts. It checks byte provenance, unique nonzero sparse records, exact support intersections, exponent shifts, denominator records, degrees and leading coefficient records. It does not construct/evaluate a source transition or polynomial, take source derivatives, choose a point, or run Ω. No source evaluator or production launcher was imported.

The mathematical contraction identities, determinant-one transition identity and inverse-splitting identities are the already certified source premises, read from the source description; this review does not rerun their physical polynomial checkers. The formal deductions below are separate from the metadata checks.

## 2. Whole-ambient transport fixes the cohomology normalization

Use superscript `pres` for matrices in a vertex's own prescribed ambient line frame, and use a single finite reference frame for every ambient block in subsequent products. Write ν_i for the source line-frame ratio and ℓ_i=dlog ν_i. The four ambient weights, ranks and supertrace signs are

    k = (−1,1,3,5),   n = (5,15,10,2),   ε = (−,+,−,+).

The source explicitly gives D_i^pres=ν_i^−2 D_ref. Transport of coefficient vectors in weight k to the common ambient reference is multiplication by ν_i^k. Since the differential raises k by two,

    D_common = ν_i^(k+2) D_i^pres ν_i^−k = D_ref.

Thus every transported split connection really is compatible with the same common differential. If U_i^pres is a split basis, its actual common-frame split basis is

    S_i^(k) = ν_i^k U_i,pres^(k).

In the middle weight-one block, the prescribed cohomology columns are

    f_i^pres = I_c^ref diag(1,ν_i^−2).

Their common-ambient images, with the dual projection transported reciprocally, are

    I_i = ν_i f_i^pres = I_c^ref C_i,
    P_i = C_i^−1 P_c^ref,
    C_i = diag(ν_i,ν_i^−1).

They agree exactly with the pinned generator's determinant-normalized transition formula:

    G_ij = P_i I_j = C_i^−1 K_ij C_j = g_ijᵗ,
    K_ij = P_c(i)^ref I_c(j)^ref.

The common split coefficient is Ω_i=−dS_i S_i^−1. Because the columns I_i are columns of S_i, they are parallel:

    dI_i + Ω_i I_i = 0.

The common pivot coefficient is a_i=−p_i/2, where p_i=dlog v_pivot(i). Indeed its prescribed coefficient is ℓ_i−p_i/2, and transport subtracts ℓ_i. Put

    A_i=Ω_i−k a_i,    b_i=P_i A_i I_i,
    Γ_i=P_i dI_i,    η_ij=−2(a_j−a_i)=p_j−p_i.

Since k=1 on the cohomology-containing block,

    b_i=−Γ_i−a_i I.

This is the full connection identity, not merely its tracefree part. In particular, Γ is being differentiated in the common ambient reference; it is not obtained by subtracting two coefficients left in different prescribed frames. Likewise T_i=[D,A_i]=dD+2a_iD uses D_ref and the common a_i. No line-frame derivative has been suppressed.

The split connection is zero on cohomology in its own parallel frame I_i. Hence the split-connection difference Z_ij=Ω_j−Ω_i induces

    z_ij=P_i Z_ij I_i=−dG_ij G_ij^−1=−L_ijᵗ.

The determinant-one source identity gives tr z_ij=0. The usual chain-map trace identity applies to products of the Z coefficients because [D,Z]=0; it is not asserted for individual A_i or Ω_i coefficients.

## 3. Independent derivation of the exact δK formula

Use the scalar contraction K in the curvature note, not the rational transition matrix K_ij of section 2. To distinguish them temporarily, write the scalar as 𝒦:

    𝒦_ij = str(A_i ∧ Z_ij) − tr(b_i ∧ z_ij).

Let

    Q_ij = P_i A_j I_i − G_ij b_j G_ij^−1.

Since A_j−A_i=Z_ij+kη_ij/2, its cohomology projection gives

    G_ij b_j G_ij^−1−b_i = z_ij+η_ij I/2−Q_ij.

Substituting b_i=−Γ_i−a_iI and η/2=a_i−a_j cancels the scalar pivot differences, yielding

    Q_ij = G_ij Γ_j G_ij^−1−dG_ij G_ij^−1−Γ_i.

This verifies the curvature note's Q with the actual common-frame source normalization. It is also the defect obtained from the source contraction identity, since inserting I_jP_j=1−Dh_j−h_jD gives the two displayed h/T terms in that note.

On an ordered triple, transport the second-edge quantities to frame i. Because Z and z are Čech one-cocycles,

    δ str(A_i∧Z_ij)
      = str(Z_ij∧Z_jk)+(η_ij/2)∧str(kZ_jk),

    δ tr(b_i∧z_ij)
      = tr(z_ij∧z_jk)−tr(Q_ij∧z_jk).

The central term in the second line is zero by tr z_jk=0. The first supertrace is the cohomology trace because both factors are chain maps. Subtraction gives exactly

    Λ_ijk=δ𝒦_ijk
      = tr(tf(Q_ij)∧z_jk)+(η_ij/2)∧str(kZ_jk).

The plus sign and factor 1/2 are thus checked independently. This is an equality of cochains, not only cohomology classes. Its being a coboundary does not make it the zero cochain.

## 4. The source coefficient 19, without determinant gluing

The generator's prescribed interior split-column powers are

    U0: (ν^−2 repeated 5 times, 1, ν^−2, ν² repeated 8 times),
    U1: (1 repeated 8 times, ν² repeated 2 times).

Both prescribed determinant exponents are 4. The extreme prescribed split bases are identities. Including the whole-ambient factor ν^k in rank n changes the four exponents to

    e = (−5, 4+15, 4+30, 10) = (−5,19,34,10).

Since the common split coefficient is −dS S^−1, the ν coefficient of str(kΩ) is

    −Σ_r ε_r k_r e_r = −(−5+19−102+50)=38.

Now take j and k on the same carrier, with different legal masks. Their rational carrier split matrices are identical, so their determinant logarithmic derivatives cancel in Ω_k−Ω_j. This gives directly

    str(kZ_jk)=38(ℓ_k−ℓ_j).

No formula for the individual rational carrier determinants, no gluing of det(U0)/det(U1), and no global-unit argument is needed here. For i on carrier 0 and j on carrier 1, η_ij=dlog v1. Therefore the scalar contribution to Λ is precisely

    19 dlog(v1) ∧ (ℓ_k−ℓ_j).

This establishes the exact coefficient needed for the counterargument. More generally, assuming the previously admitted individual pivot determinant formulas, their −2 pivot exponents give −4p_i and recover the full 38δℓ−4δp identity. That stronger individual-determinant assertion is not a premise of this review's nonclosedness proof.

## 5. Reference connections, affine masks and the leading term

Sparse P-row/I-column intersections exhaust every possible contribution to Γ_c^ref=P_c^ref dI_c^ref. For primary carrier c the intersections are rows c and c+5, with no off-diagonal intersections. The selected I entries are 1 and v_c, paired with P entries 1 and v_c^−1, where v0=1. For auxiliary carrier 5 the rows are 5 and 14 and the entries are 1 and −v4/v1², with reciprocal P entries. Thus all six identities hold:

    Γ_c^ref=diag(0,σ_c),
    σ_c=dlog s_c,
    (s_0,...,s_5)=(1,v1,v2,v3,v4,−v4/v1²).

In particular the auxiliary σ is not the logarithmic derivative of its pivot. After C_i transport,

    Γ_i=diag(ℓ_i,σ_c−ℓ_i).

These are flat diagonal local connections, but their projection descent defects need not vanish. Directly differentiating C_i and canceling every resulting term in Q gives

    Q_ij=C_i^−1 Q_ij^ref C_i,
    Q_ij^ref=K_ij Γ_j^ref K_ij^−1−dK_ij K_ij^−1−Γ_i^ref.

For the second edge, with z_jk^ref=−dK_jk K_jk^−1, its transported expression is

    G_ij z_jk G_ij^−1
      =C_i^−1[K_ij z_jk^ref K_ij^−1
        +ℓ_j K_ij h K_ij^−1−ℓ_k K_ik h K_ik^−1]C_i,
    h=diag(1,−1).

This checks mask independence of Q, all signs in the affine-mask formula, and absence of a first-mask dependence in the trace pairing. When j and k have the same carrier, K_jk=I and η_jk=0. Define

    A_j=tr(tf(Q_ij^ref) K_ij h K_ij^−1),
    u_ij=p_j−p_i.

Sections 3–4 then give the exact repeated-carrier formula

    Λ_ijk=(A_j−19u_ij)∧(ℓ_j−ℓ_k).

For the pair (0,1), put t=v1 and work over F0=Q(v2,v3,v4). The authenticated sparse records give

    Γ_0^ref=0,   Γ_1^ref=diag(0,dt/t),
    d0=t v2 v3 v4−1,   d1=−t^5+t v2 v3 v4.

Cyclicity, with tr h=0, therefore gives

    A_1=−dt/t−tr(K^−1 dK h),   K=P_0^ref I_1^ref.

The complete row/degree table is

    K00: (row1,1), (row4,−2), (row7,−1)
    K01: (row4,0), (row7,−1)
    K10: (row1,0), (row4,−4), (row5,−2), (row7,−2)
    K11: (row4,−2), (row5,−2), (row7,−2).

No multiplication or evaluation of a source polynomial is needed for this table: each order is the sum of two numerator degrees minus the two denominator degrees. The unique degree-zero contributions in K01 and K10 have the exact leading coefficient records giving

    K01=v2 v4/v3+O(t^−1),
    K10=−v3/(v2 v4)+O(t^−1).

For example the two factors in K01's row4 contribution have leading terms −t/v3 and −v2v4/t; K10's row1 has first factor −v3/(v2v4) and second factor exactly 1. Meanwhile K00=O(t) and K11=O(t^−2). Hence

    det K=K00K11−K01K10=1+O(t^−1).

This alone establishes invertibility over F0(t) and suffices; the already certified exact determinant-one identity is unnecessary for this particular valuation step. If M=K^−1∂_tK, then

    M00=(K11∂_tK00−K01∂_tK10)/det K=O(t^−2).

Here ∂_tK00=O(1), and a bounded rational function such as K10 has derivative O(t^−2). Also tr M=∂_t log(det K)=O(t^−2). Thus tr(Mh)=2M00−tr M=O(t^−2), and finally

    (A_1−19dt/t)(∂_t)=−20/t+O(t^−2)≠0.

All orders are in the formal Laurent field F0((1/t)). This is an algebraic nonidentity proof, not a value at an infinity chart or at any numerical point. Lower-order cancellations cannot alter the displayed coefficient −20.

## 6. Pullback, legal masks and Ω=0

The elementary-symmetric field inclusion

    Q(v1,v2,v3,v4) → Q(x0,x1,x2,x3)

is finite separable in characteristic zero. Its Jacobian determinant is the nonzero Vandermonde, so the induced map on rational one-forms is injective. The subsequent elliptic function-field extension is also finite separable. Consequently the nonzero F=A_1−19dlog v1 remains nonzero on the actual product of curves.

Removing the finitely many carrier and legal-frame zero/pole divisors leaves a dense common finite open. On that open all masks are simultaneously legal and

    ℓ_m=Σ_a m_a r_a dx_a,
    r_a=(x_a²+1)/(2x_a(x_a²−1))≠0

as rational functions. If F has a nonzero dx_b component, take the other coordinate a in the target pair containing b, and use j=(carrier1,mask0), k=(carrier1,mask 2^a), with i on carrier0. Then

    Λ_ijk=−F∧r_a dx_a

has a nonzero contraction in that target pair. Its physical multiplier y_c y_d is nonzero in the function field, so it cannot erase the nonidentity. The two carrier1 vertices are distinct even though their carrier labels coincide.

There is a useful strengthening: F is pulled back from the elementary-symmetric variables, so the one-form is invariant under permutation of the four x coordinates. Those permutations act transitively on the four differential components. If any component were identically zero, invariance would force all four to be zero. Therefore every dx component is nonzero. Each of the four single-bit last masks detects a nonzero contraction in its containing target pair. In the source's zero-based bit convention, the fixed triple

    ((carrier0,mask0),(carrier1,mask0),(carrier1,mask1))

already has Λ_(0,1)≠0 as a rational function. This fixes a legal symbolic family, not a point or a numerical value.

For each such family, the second-edge rational carrier core is P_1^ref I_1^ref=I. Thus its physical row transition is a diagonal ratio of frames differing in just one coordinate. It depends only on that coordinate and its elliptic y coordinate. Every cross slot in Ω differentiates two distinct coordinates, so every relevant second derivative of this second edge is identically zero. Therefore every transported J cross slot is zero and Ω=0 identically. The first edge may depend on all coordinates; that does not affect this conclusion.

## 7. What is refuted, and what remains compatible

Nonzero Λ on a dense open disproves the global cochain identity δK=0, without needing an extension argument at infinity. It therefore refutes the specific implication chain

    K is closed → scalar H1 vanishing supplies K=δf
                → BI removes E_p(K_q)+E_q(K_p) by that primitive.

It does not establish that the last E combination is nontrivial in cohomology, that it cannot cancel other remainder terms, or that it cannot be a boundary for another reason. In particular Λ itself is exact by definition. Nonzero cochains and zero cohomology classes are fully compatible.

The later full-S4-sign result concerns

    Alt(R_raw)=δP,
    P_ij=−ι_(V0∧V1∧V2∧V3)[(Z_i+Z_j)∧L_ij]/72,
    Z_i=str(B_i³).

It retains the four ambient B blocks in Z_i and cancels the complete alternating scalar and quartic-current terms together. It does not delete K individually. Therefore the accepted closed-K counterargument and the full-sign boundary theorem coexist. Neither settles the remaining unprojected obstruction, its other symmetry sectors, Rsharp, or an executable detector/cutoff bound.

## 8. Precise normalization clarification for the later cubic proof

The local-array identity

    P_fi f_j=(ν_i/ν_j)G_ij

is algebraically true if f_i=I_i^ref diag(1,ν_i^−2) and the ambient arrays are compared without transport. However, f_i and f_j are written in different prescribed ambient line frames. To compare actual cohomology sections inside i's ambient frame, the middle weight-one ambient transition contributes ν_j/ν_i:

    P_fi (ν_j/ν_i) f_j = G_ij.

Equivalently, placing each frame in the common ambient reference gives e_i=ν_i f_i and the same G_ij. These e_i are actual split-parallel columns there. The geometric induced connection difference is consequently

    A^E_common=−dG_ij G_ij^−1=−L_ijᵗ.

The formula

    −d[(ν_i/ν_j)G_ij][(ν_i/ν_j)G_ij]^−1
      =−dG_ijG_ij^−1+dlog(ν_j/ν_i)I

instead belongs to the untransported array comparison. It must not be substituted for A^E_common in the full Γ, Q or δK identities. This is exactly the scalar ambiguity that section 2 avoids, and it is why the common determinant exponents must include all four ambient blocks.

For the later cubic proof, this distinction changes no invariant cubic trace. For any matrix-valued one-form X and scalar one-form α,

    tr((X+αI)³)=tr(X³)+α∧tr(X²)=tr(X³),

because tr(X²)=0. Its tracefree part also stays the same. Using the correct actual A^E_common directly gives the same identity tr((A^E_common)³)=tr(L³), with the usual exterior transpose sign. Thus the cubic proof's normalization explanation can and should be corrected while preserving its resulting boundary identity and primitive. The closed-K formulas reviewed here require no correction.

## Reproduction and evidence limits

The directory contains this proof/review, the pinned repository-input manifest, an independent metadata checker, and matching normal/optimized receipts. The supplied structural checker was also read and passed in both modes. The two metadata implementations agree. Their PASS results authenticate exactly the sparse facts used in section 5 and provenance; they do not stand in for the mathematical frame, trace or pullback arguments.

No source polynomial or numerical point was evaluated. No source transition matrix or source jet was constructed computationally. No Ω computation was repeated.
