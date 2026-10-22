# 21. Complete (3,1) exclusion and the second-normal residue

This chapter records published results through **22 October 2026, 07:09 UTC**. It supersedes the open (3,1) frontier in Chapters 17–20 and sharpens the normal comparison without evaluating the fourth Bockstein. The generic section count remains **four or five**; the finite last Smith exponent remains **4–31**, or the cokernel is permanent. Generic **SF ≥ 3** and positive-square rank **≥ 27** are unchanged.

The results concern several different maps. The nonzero scalar obstruction of a fixed midpoint pair, the rank of a lower square-secant map, and the actual fourth filtered obstruction are not interchangeable.

## 21.1 The entire extremal (3,1) Gauss profile is excluded

Chapter 20 left ten necessary rank-one first quotients after excluding the rank-two and rank-three dual-image branches. The next exclusion removes all three e=11 cases and four e=9 cases. The last three e=9 candidates have

    A0 = B ⊕ O(−8),
    B = 2O(4), O(4) ⊕ O(6), or W O(5).

The final exclusion rules out all three. Together these results close the **entire maximal (k,l)=(3,1) profile**, not just its rank-two branch. The remaining possible maximal profiles are

    (1,1), (1,2), (1,3), (2,1), (2,2).

These are possibilities still requiring exclusion or realization, not constructed geometries. No new (1,3) reduction is included at this cutoff.

The last proof uses the actual saturated Gauss flag K=E⁻, K2=E⁻⁻, F0=E⁻⁻⁻, of ranks 14, 11 and 8, with deg E=−54. The first actual image is forced to have no torsion defect: A1=B(−2)⊕O(−10). Two-twist character identities, cohomology budgets and exhaustive equivariant splitting exclude the first two B cases. For B=W O(5), the next actual image is W O(1)⊕O(−12). Complete evaluation kernels and the remaining Hom supports then force a nonzero all-negative saturated subbundle with zero Gauss derivative, contradicting characteristic-zero constancy of its Grassmannian map.

Only the three known interior steps are assumed to have rank three. Subsequent ranks are derived. The proof keeps actual images distinct from their saturations, includes the empty negative tail in its finite splitting check, and never regards a bundle splitting or graph removal as a horizontal decomposition. These distinctions are essential to the closure. The remaining profiles prevent any inference that SF ≥ 4.

[Seven-case exclusion](https://github.com/Akilleez-QA/read-em-and-weep/blob/b0e71c4430049509a7a90168aaa1ebe7ab3146cc/research/hm/order-four-quadratic-load/EXTREMAL-31-RANK-ONE-DEGREE-ELEVEN-EXCLUSION.md); [last three cases and whole-profile closure](https://github.com/Akilleez-QA/read-em-and-weep/blob/93f99e65a95583d8bf083ae5b0169ed9a5411f6c/research/hm/order-four-quadratic-load/EXTREMAL-31-LAST-RANK-ONE-EXCLUSION.md).

## 21.2 The ambient multiplier is a monad ratio, not an evaluated number

Fix the channel maps, equation, Hamiltonian volume and determinant/Serre markings. For nonzero formal monad coefficients (a_m,b_m,c_m), the actual relation

    a At_F(D0) = q0 κ_F At_F(D_a)

has

    κ_F = C_mult a_m/b_m,    C_mult ≠ 0.

The constant C_mult is **unevaluated** in these fixed markings. Rechoosing a channel basis to make it one is not its evaluation. Full two-block covariance, including the determinant factor in Hamiltonian transport, proves the ratio law. The apolar/edge comparison and the actual two-root displacement separately give

    η_E = C_ap a_m b_m η_ap,
    d = K_cup b_m²,
    η_+ = η_E/(2d),
    c_eta+ = C_ap/(2K_cup) · a_m/b_m.

All constants displayed as nonzero remain unassigned; the positive-transition displacement and its bracket-normalized negative must not be conflated.

The missing multiplier determination is reduced to a global degree-two homotopy of the determinant-valued monad:

    d_M T_a = a δ_D0 M − q0 C_mult(a_m/b_m) δ_Da M.

Both monad arrows and their fixed-duality trace-free relation must be respected. Every term of the twist-two chain-Hom complex has vanishing higher cohomology, so this is a genuinely global polynomial homotopy problem, not a reduction hiding an extra Čech obstruction. This chapter neither constructs T_a nor determines C_mult.

[Monad-ratio theorem and global homotopy reduction](https://github.com/Akilleez-QA/read-em-and-weep/blob/28c2e5ff0e7454942220d0edec9a710b5f90f2f5/research/hm/order-four-quadratic-load/ACTUAL-AMBIENT-ATIYAH-MULTIPLIER-IS-THE-MONAD-RATIO.md).

## 21.3 Marked endpoint exchange constrains, but does not evaluate, the fourth gate

For the two actual ambient endpoints F and F′ related by multiplication of the negative coordinates by μ with μ²=−1, use the same physical equation, fixed cone nilpotent N, boundary normalization ξ_F=δ_(q0,F)(N), and pencil q0−ta. Then

    β4_F′(a,h) = −β4_F(a,h)

in the **same actual second-symbol cokernel**, including its rank-drop fibers. The actual second-symbol tensors and raw cubic D5 tensors agree. Their unique canonical third source correction agrees as a coefficient family as well; its contribution is retained in the corrected chain.

The extra cyclic-source sign, not simply the fourth power of a, produces the minus sign. This is an exchange of two distinct actual endpoints. It neither forces either value to vanish nor defines a fourth operation on a first-normal affine line through the midpoint. The midpoint extension needed for such a claim is not supplied. All fourth coefficients remain unevaluated.

[Marked endpoint exchange](https://github.com/Akilleez-QA/read-em-and-weep/blob/28c2e5ff0e7454942220d0edec9a710b5f90f2f5/research/hm/order-four-quadratic-load/FOURTH-BOCKSTEIN-HAS-ODD-MARKED-ENDPOINT-EXCHANGE.md).

## 21.4 A nonzero local old-connection term is not the full error

For the fixed multiplied corrected midpoint source a=t², h=X²Y², the lowest actual first-normal connection K0 is computed in both complete regular charts. Its old-connection contribution

    C_K = ([K0,T4] + B1(K0,n) − B1(n,K0))_11

is an explicit nonzero quartic in the regular chart. Complete affine harmonic transport, the q-symbol correction, determinant scalar, and filtered bounds justify this lowest-coefficient identification. The result concerns K0, not the full K.

This is **one local summand** of the next harmonic error. It is not an independently glued global class, the complete R2, or a fourth value. The fixed gamma/q-symbol terms, finite conic transport, higher coefficients and failed endpoint nilpotent gluing remain in the full calculation and may cancel this contribution. Earlier degree-twelve statements concerned a different regular scalar-lift commutator correction; they do not say that every old-K contribution has degree twelve.

[Actual lowest connection and local summand](https://github.com/Akilleez-QA/read-em-and-weep/blob/28c2e5ff0e7454942220d0edec9a710b5f90f2f5/research/hm/order-four-quadratic-load/ACTUAL-LOWEST-NORMAL-CONNECTION-HAS-AN-EXPLICIT-NEXT-ERROR-TERM.md).

## 21.5 The genuine midpoint pair has a canonical nonzero residue

Start with the fixed, genuine first-normal midpoint bundle and its twisted nilpotent, not an arbitrary local matrix. In the marked harmonic frame,

    Ncorr = L(n) + q L(T),
    Ncorr² = q² L(χ) I modulo q³,
    χ I = T² + B1(n,T) + B1(T,n) + B2(n,n).

Both ordered mixed products are required. The lowest scalar coefficient has cover degree eight and is nonzero modulo (f,g_x)². A regular second correction changes it by tr(nS), in precisely that square ideal; it cannot kill the class across the vertex common-zero locus. Off that locus the ideal is the unit ideal, so no obstruction there is claimed. Changing the specified first-normal nilpotent is outside the assertion.

Arbitrary local matrix and transition lifts to the third neighborhood suffice to define the scalar residue: half-trace and conjugation show that the coefficients agree modulo the image of tr(n·), namely I_Z². Thus they glue canonically in O_(2Z) without asserting a global second-normal midpoint extension. The genuine midpoint pair is crucial; the corresponding endpoint first-normal nilpotent does not glue.

The conic transverse slice and its equivariant balance force the conic component to vanish. The vertex constant is also zero. Consequently the global class lies in the invariant nilpotent line. With the independently marked apolar generator n_ap and physical equation q0=νq, its exact normalization is

    χ̄_physical = −Bλ/(4ν²) · n_ap ≠ 0.

The sign is checked against the original apolar representative, and a regular ideal-membership identity compares the entire two scalar representatives, not just one coefficient. This is a canonical obstruction for the **fixed midpoint nilpotent pair**. It is not an obstruction for every arbitrary local nilpotent, a value of the fourth gate, or an evaluation of the ambient multiplier C_mult.

[Actual residue and global gluing](https://github.com/Akilleez-QA/read-em-and-weep/blob/eaf7bb8b1bf01b1e350e22c7b4c39c0692f52b63/research/hm/order-four-quadratic-load/ACTUAL-HARMONIC-NILPOTENT-HAS-A-NONZERO-SECOND-NORMAL-RESIDUE.md); [exact apolar normalization](https://github.com/Akilleez-QA/read-em-and-weep/blob/eaf7bb8b1bf01b1e350e22c7b4c39c0692f52b63/research/hm/order-four-quadratic-load/ACTUAL-NILPOTENCE-RESIDUE-HAS-AN-EXACT-APOLAR-NORMALIZATION.md).

## 21.6 Lowest tangent acyclicity is associated-graded only

For the actual marked vertex filtration, let E4 be the associated-graded weighted-degree-four coefficient bundle of B_Q(4). Its exact trace sequence is

    0 → W′ O_L(−1) → E4 → Sym¹²(W′) O_L → 0.

The tangent-modulo-conjugation coefficient is gr4 M(2)=W′ O_L(−1). Both H⁰ and H¹ vanish before taking invariants. Therefore H⁰(E4)≅Sym¹²(W′) and H¹(E4)=0. A compatible global scalar datum has a unique global matrix lift at this weight; there is no independent global tangent choice.

The proof retains the triangular marked transition and physical twist. For a weight-four trace-free matrix R, tr(nR)=0 forces R=τ(0,ℓ), with ℓ linear; no regular conjugator exists at the required negative weight. The square-ideal Hilbert series ends at degree eleven, so the degree-twelve trace map is onto.

The full actual R2 has **affine**, inhomogeneous transition corrections. It need not be tangent, nor a section of E4 before compatible subtraction. The exact differentiated-square constraint remains

    tr(nR2) + tr(TR1) + tr B1(n,R1)
      = H0 Dχ + 2(H0ρ−Λ0)χ.

R1 has not been set to zero, and the nonzero χ cannot be removed by inventing a square-zero second-normal lift. Vanishing of the degree-twelve square-ideal quotient does not mean the actual scalar polynomial is zero. Higher weight-eight terms and the endpoint/conic corrections remain. **The full affine R2 comparison and the fourth value are still unresolved at this cutoff.**

[Associated-graded trace sequence and strict boundary](https://github.com/Akilleez-QA/read-em-and-weep/blob/a648e97659121a924dcbb4586b9ecaadc2dd9e35/research/hm/order-four-quadratic-load/ACTUAL-LOWEST-NEXT-ERROR-TANGENT-COEFFICIENT-IS-ACYCLIC.md).

## 21.7 Mr. Slop: the actual square-secant map and its sextic factor

Mr. Slop's **PR667**, using the pinned two-channel interface and actual two-input datum, proves a fixed-map statement. On the square conic X=P(W), the actual restricted map K_(u²)→P has rank two except at exactly twelve **reduced C5 square points**, where it has rank one. This is not the different universal family-detection map Q→Hom(K_a,P), nor the rank of the full D→P map.

After twisting by O_X(−4), the map factors as

    W O_X(−7) → W′ O_X(−1) → P O_X.

The saturated image is W′ O_X(−1), and the locally free quotient is W′ O_X(1). The first arrow is the unique nonzero equivariant binary sextic matrix up to scalar. Its determinant has the twelve simple C5 zeros. Untwisted, the factorization is W O_X(−3)→W′ O_X(3)→P O_X(4).

The local elementary divisors (1,t) describe this restriction's image saturation at those points. They are **not the ambient pencil's last Smith exponent**. The sextic factorization determines the restricted actual map projectively, not its numerical normal scale or the fourth obstruction. The lower endpoint P here must not be identified with the third-Bockstein P merely from their representation names.

[PR667: exact square-conic rank and sextic factorization](https://github.com/Akilleez-QA/read-em-and-weep/blob/7d53ea234b99b75e89a29c4caba7ec564e134410/research/hm/actual-square-rank-drop/PROOF.md)

## 21.8 Mr. Slop: fixed-channel zero schemes have length at most eighteen

Mr. Slop's **PR666** sharpens the earlier twenty-one bound to **eighteen**. For a nonzero universal channel, the nonempty finite fixed-channel zero scheme has only the necessary lengths

    6, 10, 15, 16, 18.

Only length eighteen can be nonreduced: if it occurs, it consists of the six first infinitesimal neighborhoods of the C5 axes. The other cases are reduced permitted axis-orbit unions. These lengths are necessary possibilities, not assertions that all occur.

The extremal length-twenty-one residual would force a unique invariant linear syzygy; canonical polarization proves that the ambient invariant multiplication has zero kernel. Dihedral stabilizer irreducibility then excludes local length two at C3 and C5 axes, removing lengths twelve and twenty. If the C2 channel occurs, it is distinct from both other axis channels and has exactly fifteen reduced points. Whether C2 occurs and whether the C3 and C5 channels coincide remain open. No reducedness of the **total** rank-drop scheme is inferred.

This universal fixed-channel zero-scheme result does not determine the actual fixed-map square rank in Section 21.7. Their loci and purposes are different: the former is supported on nonsquare axes; the latter concerns twelve points on the square conic.

[PR666: fixed-channel zero-scheme exclusion](https://github.com/Akilleez-QA/read-em-and-weep/blob/0fc85f297a62c7be473a8da9ad992bb84706f8f2/research/hm/maximal-channel-zero-exclusion/PROOF.md)

## 21.9 Reproduction and the remaining gates

Run the companion Python verifiers from the source directory with its pinned dependencies:

- [verify_monad_ratio_edge_apolar_root_comparison.py](https://github.com/Akilleez-QA/read-em-and-weep/blob/28c2e5ff0e7454942220d0edec9a710b5f90f2f5/research/hm/order-four-quadratic-load/verify_monad_ratio_edge_apolar_root_comparison.py)
- [verify_actual_lowest_normal_connection_term.py](https://github.com/Akilleez-QA/read-em-and-weep/blob/28c2e5ff0e7454942220d0edec9a710b5f90f2f5/research/hm/order-four-quadratic-load/verify_actual_lowest_normal_connection_term.py)
- [verify_fourth_marked_endpoint_exchange.py](https://github.com/Akilleez-QA/read-em-and-weep/blob/28c2e5ff0e7454942220d0edec9a710b5f90f2f5/research/hm/order-four-quadratic-load/verify_fourth_marked_endpoint_exchange.py)
- [verify_extremal_31_rank_one_degree_eleven_exclusion.py](https://github.com/Akilleez-QA/read-em-and-weep/blob/b0e71c4430049509a7a90168aaa1ebe7ab3146cc/research/hm/order-four-quadratic-load/verify_extremal_31_rank_one_degree_eleven_exclusion.py)
- [verify_extremal_31_last_rank_one_exclusion.py](https://github.com/Akilleez-QA/read-em-and-weep/blob/93f99e65a95583d8bf083ae5b0169ed9a5411f6c/research/hm/order-four-quadratic-load/verify_extremal_31_last_rank_one_exclusion.py)
- [verify_actual_nilpotent_second_normal_residue.py](https://github.com/Akilleez-QA/read-em-and-weep/blob/eaf7bb8b1bf01b1e350e22c7b4c39c0692f52b63/research/hm/order-four-quadratic-load/verify_actual_nilpotent_second_normal_residue.py)
- [verify_actual_nilpotent_apolar_residue_normalization.py](https://github.com/Akilleez-QA/read-em-and-weep/blob/eaf7bb8b1bf01b1e350e22c7b4c39c0692f52b63/research/hm/order-four-quadratic-load/verify_actual_nilpotent_apolar_residue_normalization.py)
- [verify_lowest_next_error_tangent_acyclicity.py](https://github.com/Akilleez-QA/read-em-and-weep/blob/a648e97659121a924dcbb4586b9ecaadc2dd9e35/research/hm/order-four-quadratic-load/verify_lowest_next_error_tangent_acyclicity.py)

Each verifier link is pinned to the same immutable commit as its companion proof above. The latest included PR543 source snapshot is a648e97659121a924dcbb4586b9ecaadc2dd9e35, tree a2431fad1490bd0212994e6d06d2fef1b0e3bcfa. Universal identities and finite character/splitting checks supplement the authored geometric proofs; they are not proof-assistant certificates or selected-instance experiments. PR666/667 are separately attributed mathematical arguments, not extra PR543 verifier results.

The next exact tasks are the marked global monad homotopy if an absolute C_mult is needed; the complete affine R2 transport and actual division; and evaluation of the corrected fourth class B4|D5−B3|A L in the actual quotient. The four allowed fourth channels and their complete detection criteria remain structural tests, not evaluated coefficients. Further Gauss progress must address the five surviving profiles without upgrading necessary splitting candidates to realizations. Original source recovery, higher lifting and Weil-class algebraicity remain separate open objectives. Later unpublished affine-transport or (1,3) work is deliberately excluded.
