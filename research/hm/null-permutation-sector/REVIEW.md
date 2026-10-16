# Independent review: alternating the genuine ordered-nerve source

## Verdict

The rational representation calculation and the full alternating cancellation of the bilinear second-jet symbol are correct. The unsorted ordered-nerve construction is mathematically valid for the pinned physical source: the published formulas supply its required extension and strict permutation covariance. It is not a proof that the remaining two-dimensional class vanishes, and it does not construct a source-faithful coefficient implementation.

The refinement in `LINEAR_JETS.md` is also correct: the same-array full alternation kills the displayed linear-Hessian expression Q2. An independent computation confirms that its quartic remainder need not vanish: the stated invented current data give normalized alternation `-h/12`.

One definition needs precision. To restrict **exactly** to the five-term fresh raw representative, define the ordered-nerve cochain by

    R_bar = M_bar(s_raw)^0 + delta W_bar,
    W_bar = s_raw,q k_p + s_raw,p k_q.

Here M is the complete normalized mixed module residual. Defining R_bar merely as M_bar^0 produces the same class but differs from the five-term representative by delta W. This clarification has been incorporated into the companion construction.

## 1. Immutable inputs inspected

All references below were read as text. No physical polynomial, coefficient, source jet, residual, fiber or numerical source specialization was evaluated.

At commit `f968b53943ba2312f09fbc3e8f9d462e86bcaa34`:

- [Perfect-Complex-D8-F3.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/f968b53943ba2312f09fbc3e8f9d462e86bcaa34/research/hm/d8-small-certificates/p4/Perfect-Complex-D8-F3.md), especially sections 1–4. Git blob `3a8c3633e83466b29ea2e5739c6b486f856b91b2`.

At commit `08b73637d4136f91606aad332c46cafd064417f8`:

- [first-order-source.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/08b73637d4136f91606aad332c46cafd064417f8/research/hm/current-scalar-residual-attribution/first-order-source.md), especially sections 2–4. Git blob `5f4e56252cd9a8a6eb218aceb911c95a1c330ebc`.
- [ambient-second-jet.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/08b73637d4136f91606aad332c46cafd064417f8/research/hm/current-scalar-residual-attribution/ambient-second-jet.md), sections 1–3. Git blob `e07d4373a7c22f7cf4502260d80dbd559d942850`.
- [closure-and-characters.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/08b73637d4136f91606aad332c46cafd064417f8/research/hm/current-scalar-residual-attribution/closure-and-characters.md), especially sections 1–2 and 5. Git blob `946f96670ecb8152eaae16195329f9eb1243b7ae`.

At commit `e93cf712f9da4926a8450cc870ed45a7bfc379ab`:

- [RS full-source application](https://github.com/Akilleez-QA/read-em-and-weep/blob/e93cf712f9da4926a8450cc870ed45a7bfc379ab/research/codex-swarm/full-source-application/PROOF.md), especially sections 2–5. Git blob `69821c62a44485d64325e77c21bdab3553bf0d17`.
- [BI source-boundary analysis](https://github.com/Akilleez-QA/read-em-and-weep/blob/e93cf712f9da4926a8450cc870ed45a7bfc379ab/research/codex-swarm/source-boundary-analysis/PROOF.md), especially sections 1–5. Git blob `d3663b1fc97ff206d3937b0fe746e0817377af24`.

The review accepts the pinned contraction, determinant-one, small-rank and source-domain premises at their published scope; it does not independently rerun their physical certificates.

## 2. Why the ordered extension exists

Use the actual cover indexed by a carrier and a legal mask. Before sorting, attach the physical transition, connection difference, q-cochain and scalar transgression to every supplied ordered tuple. Repeated labels are allowed.

The relevant identities are identities on this full nerve:

1. Physical transitions satisfy `g_jk g_ij=g_ik`, with no ordering condition.
2. On a common rational chart, each q has the mask-difference rule `q_a,ij=(m_j,a-m_i,a)q_a`, so `delta q=0` on all triples, including repeated labels. This does not claim a regular vertex primitive for the nontrivial scalar Cech class. The ordinary Alexander–Whitney differential and product identities hold on the full ordered nerve.
3. The unsymmetrized transgression of first-order-source sections 2–3 uses only connection differences, `delta A=0`, the differential/product rule, the split-connection trace identity and rank-two matrix identities. Thus its conclusion `delta s_raw=b-tr(C)/2` holds on every supplied ordered triple. The edge correction `-15 q_a,ij q_b,ij/8` must remain.
4. The ambient formulas `b=lambda(q_a cup q_b+q_c cup q_d)` and T satisfy both coherence identities by these same AW identities. Their proof in ambient-second-jet section 2 does not require sorted or distinct vertices.
5. The associative module-defect identity in RS section 2 is an identity on an arbitrary quadruple. Once the first-order defect is zero, it proves `delta M_bar=0`. Trace-free projection commutes with the row-End differential, and adding `delta W_bar` retains closure.

This is stronger than extending a table by guessed antisymmetry. For example, the raw scalar's q_a q_b correction is symmetric under edge reversal, so the raw all-tuples values generally are **not** the alternating extension of their increasing-edge restriction. That discrepancy is permitted and must not be erased before the argument.

Restriction from full ordered cochains to strictly increasing tuples is a chain map: every face of an increasing tuple is increasing. Both augmented sheaf Cech complexes resolve the same sheaf, and restriction extends the identity in augmentation degree. Equivalently one can use the usual full-nerve/increasing-cover comparison. The actual common intersections are affine, as documented in BI section 4, so the global Cech complexes compute the required sheaf cohomology. Thus the restriction induces the canonical cohomology identification.

The repeated-tuple issue is therefore a matter of defining the correct intermediate complex, not an unproved order-change identity for historical source values.

## 3. Strict physical permutation covariance

Let sigma permute the four factors, and permute every legal mask by the same sigma. Carrier labels remain fixed. Write a vertex as `(c,m)` and let

    nu_(c,m) = product_a (y_a/x_a)^(m_a).

The product-line linearization is ordinary, without a Koszul sign. Simultaneously relabeling factors and masks leaves this product unchanged after pullback. The carrier primitives `I_c,P_c,H_c` and the complex maps are rational expressions in the elementary-symmetric coefficient coordinates, which are also unchanged. The physical transition formula in first-order-source section 4 is

    g_ij = transpose(diag(nu_i^-1,nu_i)
                     (P_i I_j) diag(nu_j,nu_j^-1)).

It follows directly, before differentiation, that the transformed transition equals the original transition on the same tuple positions after geometric pullback. The same argument applies to U/Q split matrices; their column scalings are powers of nu. The old connection is a sum of the same one-factor connection forms, selected by the mask, and therefore has the corresponding covariance. Its infinity expression is obtained by transport, not by resetting it to zero.

The invariant fields obey the factor-permutation relabeling rule. Consequently the pulled-back currents and normalized Hessians are the original arrays with derivative labels permuted, in the same first-vertex row frame. No cover-vertex reordering occurs. The common removed deck factor `product_a y_a` is also permutation-invariant. The canonical-bundle sign belongs in Serre duality, not as an extra sign in this local product-frame transformation.

This proves the covariance needed for Omega and Q2, using the concrete physical source formulas. It does **not** claim that the complete raw scalar is an eigen-cochain under reversal of a bivector pair. Its unsymmetrized cup representative and edge correction must be transformed in full.

## 4. Closure, class identification and rank

The full nerve has the genuine S4 chain action, so

    e_sign = (1/24) sum_sigma sign(sigma) rho(sigma)

commutes with delta over Q. The cochain `e_sign R_bar` is closed. Restricting it to increasing tuples represents the geometric sign projection of the same global class.

The accepted-class identification is explicit, not an additional numerical hypothesis:

- RS gives `R(s)=M(s)^0+delta(s_q k_p+s_p k_q)`.
- BI fixes precisely the pinned raw transgression on fresh increasing tuples.
- BI proves `s_N14-s_raw=delta f` because each relevant scalar pair-character sheaf has H1=0, and derives `R_N14-R_raw=delta(B_p(f_q)+B_q(f_p))`.
- The full-sign scalar H2 vanishes, so passing from M to M^0 does not change the obstruction class.

No explicit f or cutoff-bounded comparison primitive is needed for this **global** identification. Conversely, this proof does not grant a finite-cutoff compiler permission to apply its maps to an unbounded primitive.

Using the four pinned H2 ranks, the S4 character of the full deck-sign H2 space is `(352,48,-8,-8,-12)`. Its decomposition is

    20 trivial + 60 V + 30 U + 30(V tensor sign) + 2 sign,

where `U=(2,2)`. For the pair stabilizer D8, epsilon=sign restricted to D8 occurs in U and sign, once each, and in none of the other irreducibles. Hence its epsilon sector is 32-dimensional. Restricting e_sign to that sector is an idempotent with rank 2 and kernel dimension 30. The kernel is not itself an S4 subrepresentation.

The perfect-complex rank paper alone expressly does not identify the actual obstruction's D8 character. The assertion that the **actual** class lies in this 32-dimensional sector retains the separate geometric naturality/choice-identification premise of the sector theorem. The rank calculation is correct under that premise. Even without D8 membership, the full S4 sign projection has rank 2 on the ambient 352-dimensional space; what would be unavailable is the claimed complementary 30-dimensional target for that class.

## 5. Omega and Q2 cancel; Q4 need not

For fixed physical edge transitions, mixed derivatives commute, so `H_ab=H_ba` and `J_ab=J_ba`. The Omega expression is alternating within each bivector pair and symmetric under pair exchange. Consequently its signed sum over 24 permutations is eight times

    Omega_(01,23)-Omega_(02,13)+Omega_(03,12),

and the six possible commutator terms cancel in pairs. This is an exact identity of arbitrary symmetric matrix-valued Hessian arrays. The check on all 324 single-slot sl2 basis pairs is exhaustive for this bilinear bracket expression; scalar parts do not affect brackets. It does not certify a source/cover binding, which is instead supplied by sections 2–3 above.

For Q2, equation (13) of the raw-remainder decomposition suffices. Every term containing H_cd is invariant under exchanging c,d, and every term containing J_ab is invariant under exchanging a,b. These are odd permutations of the four tensor slots. Pairing each permutation with that slot transposition shows that the full alternation of every such tensor term is zero. The signed complementary contraction is a linear combination of slot relabelings and therefore also has zero alternation.

Thus, at the mathematical ordered-source level,

    e_sign R_bar = Alt(Q4 + E_p(s_raw,q) + E_q(s_raw,p)).

The Alt on the right means the genuine full action on the complete physical formulas, not an unsupported sign rule for the scalar arguments.

For the independent quartic control, take `L=(h,e,f,0)` and `U=(0,0,0,h)` in sl2. The 24 signed Q4 values consist of 16 copies of `-h/8` and 8 zeros. Their normalized sum is `-h/12`. These first currents are compatible with determinant-one formal germs `A=exp(x0 h+x1 e+x2 f)` and `B=exp(x3 h)`. This proves only that Q4's alternating tensor is not universally zero. The actual raw scalar E terms can still participate in cancellation, and a nonzero pointwise cochain need not give a nonzero cohomology class.

## 6. Reproducible checks and remaining boundary

`check_review.py` uses only Python's standard library, exact rational matrices and formal tensor labels. It independently checks:

1. All 324 invented single-slot sl2 Hessian pairs under the full 24-term signed Omega sum, plus pair reversal and pair exchange.
2. The formal Q2 alternating identity by exact collection of tensor-monomial coefficients.
3. The quartic negative control, including the histogram of its 24 signed values.

Run `python check_review.py` or `python -O check_review.py`. Neither imports the production source or performs source arithmetic.

What remains is the actual value or a global primitive for the two-dimensional projected remainder, together with any source-faithful executable realization and its own regularity/resource certification. The other 30 target dimensions remain separate. No runtime, owner-count or pole-ledger reduction follows from this review.
