# 25. Complete (2,2) exclusion and the actual third-neighborhood square

**Checked-source cutoff: 22 October 2026, 09:08 UTC.** The entire (2,2) maximal rank-three Gauss profile is now excluded. Six of the original nine profiles are excluded; only (1,1), (1,2), and (2,1) remain possible, without a realization claim. The actual corrected J3 is square-zero on actual 3Q. Neither result evaluates the fourth obstruction or improves SF≥3, square rank≥27, or the general section count of four or five. The original source-recovery, higher-lifting and Weil-class algebraicity objectives remain open.

## 25.1 From 24 pairs to three, with fixed denominators

Write K=E⁻, L=(Q*)⁻, A=E/K and B=Q*/L, and a=deg A, b=deg B. For profile (2,2), K and L are interior rank-three derivative stages; K⁻ and L⁻ are endpoints whose derivative ranks must not be assumed three. Both endpoint kernels are saturated in the constant ambient bundle and have highest splitting degree at most −4.

The second-interior injections K/K⁻→A(−2) and L/L⁻→B(−2) give a≥−2 and b≥−10. The original determinant defect t=−6−a−b is nonnegative and at most six. Every nonzero invariant effective divisor has degree at least twelve, so t=0 and B=A*(−2). This does not initially set the two second-interior defects to zero.

For either interior pair (N,C), with highest degree −d, exact Euler characters give

    χ_G(C(d−2))−χ_G(N(d)) = H⁰(T_N(d)) + H¹(N⁻(d)),

where T_N is the second-interior torsion cokernel. Nonnegative irreducible multiplicities on the right retain the negative H¹ contributions omitted by the earlier H⁰-only bound. Testing every compatible candidate reduces 24 pairs and 1,221 records to seven pairs and 723 records. All survivors have original defect zero. [Second-interior proof][EULER]

The primal endpoint derivative factors through A(−4), regardless of its rank. Strict top-slope decrease implies H⁰(K⁻(4))→H⁰(A) is injective. Hence

    H⁰(A)+χ_G(A(2))−χ_G(K(4))

must be a genuine representation. Four pairs have V multiplicity −1 and are excluded. The three remaining A are O(−8)⊕O(2)⊕O(6), O(−8)⊕O(4)⊕O(6), and O(−8)⊕W O(5), with degrees 0,2,2. Their records total 354. Both second-interior defects are now strictly below twelve and therefore zero. The earlier possible twelve-defect branch was retained until its primal partner was independently excluded. [Endpoint top-slope proof][TOP]

The fixed histories are **35→34→24→7→3→0 pairs** and **2,947→1,880→1,221→723→354→0 records**. The final zero follows from the geometric proof below, not a claim that a new character enumeration alone proves realizability or emptiness. These nested denominators are distinct from the nine-profile universe and must not be added together.

## 25.2 Endpoint rank drop closes the last three pairs

Put N=L⁻. The exact sequence 0→N→L→B(−2)→0 gives rank N=7 and deg N=−48−2b. Thus **a=0 gives deg N=−36**, while **a=2 gives deg N=−32**. Its derivative factors through B(−4).

The endpoint splitting overlists use both exact Euler identities at twists four AND five. The rank-seven excess above degree −4 bounds all possible blocks. For degree −36 the only necessary splittings are

    V O(−4) ⊕ W′ O(−5) ⊕ W O(−7),
    V O(−4) ⊕ W′ O(−5) ⊕ O(−6) ⊕ O(−8).

For either degree −32 case the only retained splitting is

    V O(−4) ⊕ W O(−5) ⊕ W′ O(−5).

The two-twist calculation initially also allows O(−4)⊕V O(−4)⊕W′ O(−5)⊕O(−6). It is removed by H⁰(N(4))→H⁰(B), because H⁰(B)=Sym⁶W=V⊕P4 has no trivial constituent. Twist four alone is not the exhaustive certificate. These are necessary overlists, not actual maps. [Complete endpoint proof][CLOSE]

For a saturated negative rank-r bundle F with derivative rank one, the successive negative kernels give a full backward flag. If d_r is its last line-quotient degree, and δ_i are the invariant effective divisor degrees of its nonzero line derivatives, then

    deg F = r d_r − r(r−1) − Σ_(i=1)^(r−1) i δ_i.

Every δ_i is zero or at least twelve. If its derivative reaches only summands of degree at most c, then d_r≤c. Rank zero is impossible for a negative saturated bundle in a constant bundle. This argument needs no assumption that F spans the whole ambient bundle.

For both degree −32 endpoints, ordinary Hom-degree vanishing leaves only O(2) reachable in B(−4), so the derivative rank is exactly one. The flag formula gives 0≤7d₇−10≤4, forcing all δ_i=0 and the impossible equality 7d₇=10. Both pairs are excluded.

For degree −36, the first splitting likewise has rank one; any rank-one branch of the second splitting gives 0≤7d₇−6≤8 and the impossible equality 7d₇=6. Only the second splitting with derivative rank two could remain. Its reachable target is C=O(2)⊕O(−8). If P=N⁻ and the determinant torsion has length t, then rank P=5 and deg P=−30+t. Strict top-slope decrease gives deg P≤−25, hence t≤5. Invariance forces t=0. Thus the sole rank-two branch has **rank-five kernel of degree −30**, not degree −36.

Exact Euler identities at twists five and six leave P=(1⊕P4)O(−6) or P=W′ O(−5)⊕O(−6)⊕W′ O(−7). Its derivative factors through C(−2)=O⊕O(−10), with the latter summand unreachable by degree. Its rank is one. The flag formula gives 0≤5d₅+10≤10, so all internal gaps vanish and d₅=−2. The final nonzero map O(−2)→O would have an invariant effective divisor of degree two, impossible. This closes the last branch and the entire (2,2) profile.

The conclusion is six excluded profiles out of nine, not elimination of rank three itself. The remaining (1,1), (1,2), and (2,1) profiles remain necessary possibilities. Neither SF≥4 nor a better square-rank bound follows.

## 25.3 Bounded information on the remaining asymmetric profile

For (1,2), keep K,A,L,B and put M=L⁻, J=L/M. The proved bounds are

    −8≤a≤6,     −12≤b≤2,     t=−6−a−b∈{0,12}.

If t=12, only (a,b)=(−8,−10) or (−6,−12) remains. The second dual injection is saturated: J=B(−2), and M has rank seven and degree −28 or −24 respectively. Neither degree pair is excluded or asserted realized. [Asymmetric proof][ASYM]

Here Q* and L are interior rank-three stages, but K and M are endpoints. In particular the (2,2) vanishing H⁰(Q*(1))=0 is not imported. The primal degree improvement uses the actual Euler characters and top-slope section injection; the boundary a=−10 would force A=2O(−10)⊕O(10), whose required H¹(K(2)) has negative V and P4 multiplicities. The dual bounds use only the interior injection and degree parity. Original twelve-defect torsion and second dual torsion remain distinct. This is bounded necessary information, not a complete classification of (1,2) or (2,1).

## 25.4 The existing actual J3 is square-zero

Retain Chapter 24's actual global primitive and section

    J3=(ah−qb)U_a−q²C_h ∈ H⁰(B_(3Q)(8)),
    dC_h=ahZ_a−qV_h.

For every nonzero negative quadratic a and nonzero source h in D5, **J3²=0 on actual 3Q**, for every indicated actual global primitive C_h. Zero-source cases may use zero primitives. This is a property of the existing section of the restricted actual ambient bundle; it neither computes C_h nor constructs an extension of the midpoint bundle to 3Q. [Actual square-zero proof][SQUARE]

Trace-free Cayley–Hamilton first writes J3²=q²χ I with χ∈H⁰(O_Q(12))₊. Set f₀=a²h. The regular Serre pair gives the exact trace ideal im tr(N−)=I_Z²(6); a local q² correction changes χ by f₀ tr(NK). Thus the relevant obstruction is modulo f₀I_Z², not the reduced ideal or reduced support.

On negative vertex charts, actual coherence factors the 2Q section through a local square-zero first-normal lift. The regular (3,5) pair forces its first-normal correction to start in weighted degree four; its scalar square starts in degree eight. Multiplication by h, of cover degree four, lands in I_Z² because the actual square-ideal quotient has no degree at least twelve. Completion and descent preserve the full actual containment, without identifying a homogeneous truncation with C_h.

Near the conic retain the invertible determinant factor: N=uσσᵗJ, σ=(s,t). If U_a=aN+qT_a, exact coherence and regularity give

    T_a=τ((κu/2)D_aσ+av),
    T_a²=a²(κu+σ∧v)² I,

where τ(v)=σvᵗJ+vσᵗJ. The unit u and physical κ are not normalized away. The scalar square coefficient of (ah−qb)U_a is a⁴h²(κu+σ∧v)²; the b cross term vanishes. After division by f₀ it lies in I_Z², since a∈(s,t)². This includes the locus a=0 and asserts no globally flat kernel line.

The local quotients glue because Q is integral and f₀ is nonzero. Finally H⁰(I_Z²(6))₊=0 kills χ/f₀. This proves the global square-zero statement, not vanishing of the fourth boundary, explicit construction of its primitive, or completion of the original repair.

## 25.5 Evidence and whole-project interpretation

The root integration checked the complete sources, independent audits, passing companion verifiers and exact immutable published readbacks before this edition. The supplementary checks concern universal regular-pair identities, abstract characters and bounded degree arithmetic; they are not selected actual-instance rank experiments or proof-assistant certificates.

The [progress map](progress-map.md) and [scoped inventory](data/INVENTORY.md) preserve stable local denominators and the original project's open bridges. Completed early Rao and odd lanes are distinguished from excluded cases. Overlapping scopes, nested Gauss lists and editorial objectives are not summed into a global family count or subjective percentage. Fourth-value evaluation, the four-versus-five decision, original source recovery, higher lifting and Weil-class algebraicity remain open.

## Immutable source ledger and reproduction

All sources below are in PR543 under research/hm/order-four-quadratic-load. Run each verifier with its pinned imported helpers and frozen input records.

- 914f839bc525a1edf52d9734e9844950647419e0: [second-interior proof][EULER] and [verifier][EULERV]; [endpoint top-slope proof][TOP] and [verifier][TOPV]. These produce the seven-pair/723-record and three-pair/354-record summaries; --full regenerates separately named survivor files.
- bcb820f06b0d3df35c96f928360f1e973e552c65: [asymmetric bounds][ASYM] and [verifier][ASYMV].
- 2bd41cac562738b3c526f529d51c56f8b6010632: [actual J3 square-zero proof][SQUARE] and [verifier][SQUAREV]. This is the final unit-retaining proof.
- c8975a41912b28938bc5b912e6637698a9652195: [complete (2,2) closure][CLOSE], [verifier][CLOSEV], and [compact summary][CLOSES]. The verifier checks both endpoint Euler twists and reads the frozen 354-record input without modifying it.

[EULER]: https://github.com/Akilleez-QA/read-em-and-weep/blob/914f839bc525a1edf52d9734e9844950647419e0/research/hm/order-four-quadratic-load/TWO-TWO-SECOND-INTERIOR-EULER-EXCLUDES-SEVENTEEN-PAIRS.md

[EULERV]: https://github.com/Akilleez-QA/read-em-and-weep/blob/914f839bc525a1edf52d9734e9844950647419e0/research/hm/order-four-quadratic-load/verify_two_two_second_interior_euler.py

[TOP]: https://github.com/Akilleez-QA/read-em-and-weep/blob/914f839bc525a1edf52d9734e9844950647419e0/research/hm/order-four-quadratic-load/TWO-TWO-ENDPOINT-TOP-SLOPE-LEAVES-THREE-PAIRS.md

[TOPV]: https://github.com/Akilleez-QA/read-em-and-weep/blob/914f839bc525a1edf52d9734e9844950647419e0/research/hm/order-four-quadratic-load/verify_two_two_endpoint_top_slope.py

[ASYM]: https://github.com/Akilleez-QA/read-em-and-weep/blob/bcb820f06b0d3df35c96f928360f1e973e552c65/research/hm/order-four-quadratic-load/ONE-TWO-ASYMMETRIC-QUOTIENT-DEGREE-AND-DEFECT-BOUNDS.md

[ASYMV]: https://github.com/Akilleez-QA/read-em-and-weep/blob/bcb820f06b0d3df35c96f928360f1e973e552c65/research/hm/order-four-quadratic-load/verify_one_two_asymmetric_degree_bounds.py

[SQUARE]: https://github.com/Akilleez-QA/read-em-and-weep/blob/2bd41cac562738b3c526f529d51c56f8b6010632/research/hm/order-four-quadratic-load/ACTUAL-CORRECTED-THIRD-NEIGHBORHOOD-LIFT-IS-SQUARE-ZERO.md

[SQUAREV]: https://github.com/Akilleez-QA/read-em-and-weep/blob/2bd41cac562738b3c526f529d51c56f8b6010632/research/hm/order-four-quadratic-load/verify_actual_corrected_third_neighborhood_square_zero.py

[CLOSE]: https://github.com/Akilleez-QA/read-em-and-weep/blob/c8975a41912b28938bc5b912e6637698a9652195/research/hm/order-four-quadratic-load/TWO-TWO-ENDPOINT-RANK-DROP-EXCLUDES-LAST-THREE-PAIRS.md

[CLOSEV]: https://github.com/Akilleez-QA/read-em-and-weep/blob/c8975a41912b28938bc5b912e6637698a9652195/research/hm/order-four-quadratic-load/verify_two_two_endpoint_rank_drop_exclusion.py

[CLOSES]: https://github.com/Akilleez-QA/read-em-and-weep/blob/c8975a41912b28938bc5b912e6637698a9652195/research/hm/order-four-quadratic-load/two-two-endpoint-rank-drop-summary.json
