# Seed-4 E12: direct curvature support closes carrier-block order changes

## New result

The explicit curvature-defect contraction from the source-order comparison vanishes on its complete three-owner N14 scalar-input domain. This is a new direct-F support theorem, not reuse of the old adjacent-edge separators.

Together with the reviewed seed-4 naturality and fresh-order support theorems, it proves:

**For every cover order preserving the declared auxiliary-first carrier blocks, the same refined seed-4 E12 functional is zero on every scalar edge input t whose reindexing belongs to the certified complete edge domain and whose curvature delta t belongs to the complete three-owner N14 F domain.**

The theorem permits arbitrary internal orderings of masks and standard tags within each carrier block. It does not identify an actual historical order, identify a historical scalar solution, or compare this refined seed with the different historical scalar-41 detector. It does not prove a full obstruction value or any other seed/component.

All 256 potentially nonzero swap assignments have new A/B support certificates: 512 of 512, zero unresolved. The same integer normal (-1,-1,0,1) works throughout; the smallest strict gap is 30. No physical polynomial was evaluated or expanded.

## 1. Exact source and comparison conventions

The starting comparison is [source-order-curvature-comparison.md at 9a4eda0d2251f0a89a677018188d5f9ea9269c5e](https://github.com/Akilleez-QA/read-em-and-weep/blob/9a4eda0d2251f0a89a677018188d5f9ea9269c5e/research/hm/null-source-integration/order-comparison/source-order-curvature-comparison.md).

Let N be fresh numeric-mask order and O any order with the same auxiliary-first carrier blocks. On the SAME refined seed-4 q=2 construction, L4,N R2=L4,O, with fixed pre-sort staircase (3,11,15), selector -2*[12,6], and target kappa=(-1,-2,-2,-2). No HPL prefix row is introduced or changed. Define C_ON=E_N R1-R2 E_O. The reviewed comparison gives

    L4,O E_O(t) = -L4,N C_ON(t)

provided R1 t lies in the old complete edge support domain. This addendum proves the right side zero if F=delta t lies in the domain below. F is reindexed alternatingly; no nonlinear curvature generator is reevaluated on reordered tuples.

In an N-oriented triangle, reversing its first two vertices and pulling back the orientation gives the LOCAL swap-prescription defect

    C_swap,N = signed E_(swapped prescription) - E_N
             = -1/2 (ell_1,01 partial_0 F_N - ell_0,01 partial_1 F_N).

The builder uses N-sorted owners and computes this C_swap,N. On a swapped pair it is the NEGATIVE of C_ON=E_N R1-R2 E_O after both are expressed in N coordinates. The new support proof kills either sign; they are not asserted to be literally the same multiplier. Here F_N denotes the alternating reindexing of the input curvature, not a fresh nonlinear source value.

Coordinates here are zero-based, so E12 corresponds to (0,1). All source derivatives and coefficient extraction use the global finite frame with the authenticated scalar-character conversions. A sorting sign remains an external factor of +1 or -1; it cannot alter support exclusion.

## 2. Exhaustive reduction, without rescanning the old full domain

The previously proved disjoint partition of all 884736 assignments is retained. For an order change, it refines as follows:

- 622592 assignments containing exceptional carrier 0 or 5: the first carrier stays exceptional; its P[:,6] is literally zero for arbitrary residuals.
- 259072 primary assignments with an inactive outer owner: the weight product is zero, independently of ordering.
- 1024 active assignments with first carrier 2: its selector column is zero.
- 1536 active assignments with first carrier 1 and three distinct carriers: the relative order of the tuple is unchanged by a carrier-block reorder.
- 256 active assignments with first carrier 1, repeated carrier, and zero complementary current difference: the defect is literally zero.
- 256 remaining active assignments: the new direct-F support proof below.

These numbers sum to 884736. Only the last 512 require a repeated-carrier discussion. Outer carrier activity at standard tags 3,11,15 allows original owner carriers respectively {1,2}, {1,2,3}, and {4}. The only repeated-carrier case with a nonzero selector is therefore (1,1,4), attached to those original standard owners. Different masks or standard tags remain different full owners.

The legal activity rule says that a nonzero mask bit requires the corresponding standard infinity bit. Standard bits are decoded high-first, legal bits low-first. Thus the legal masks are

    standard 3:  {0,4,8,12},
    standard 11: {0,1,4,5,8,9,12,13},
    standard 15: {0,...,15}.

There are 4*8*16=512 such assignments. Both carrier-1 owners have legal bit 1 zero. Their physical same-carrier transition is D_b D_a^(-1), because the normalized K_ab=(P_a I_b)^t is identity. Its normalized current is exactly

    ell_d,ab = (bit_d(b)-bit_d(a))
               (x_d^2+1)/(2 x_d(x_d^2-1)) diag(1,-1).

This follows from differentiating the actual moving diagonal frames, rather than setting their values to one. Matching inclusion/projection removes the outer frame conjugation once. Both log-derivative terms are retained in their difference.

Consequently ell_1,01=0. Also ell_0,01=0 unless the standard-11 owner has bit 0 one. The remaining masks are exactly

    (mask_standard3, mask_standard11, mask_standard15)
      in {0,4,8,12} x {1,5,9,13} x {0,...,15}.

There are 256. They have distinct physical labels. Sorting can put either standard-3 or standard-11 owner first; the new lowering keeps the actual sorted owners and the sign of their bit difference.

## 3. Whole-curvature domain, without the scalar solver's boundary factors

For each actual owner v=(carrier,mask,standard), let

    d_v = H_carrier^14 product_i ell_(bit_i(mask),i),
    ell_(0,i)=Y_i, ell_(1,i)=X_i(X_i^2-Y_i^2).

Use the complete homogeneous numerator domain for

    F = P / product_(three actual owners v) d_v,
    F has scalar character (0,0,-2,-2).

The source N14 pole bound justifies this domain for curvature inputs carrying that bound. Membership of t in the scalar edge domain alone does not imply this boundary-free N14 bound on delta t; it is a separate hypothesis of the theorem. Divisors remain attached to their actual occurrences even when two carriers coincide. In the finite chart Y_i=1, the denominator is product H_v^14 times x_i(x_i^2-1) for each bit-one owner. The bit-zero Y factor contributes its homogeneous degree even though its finite expression is 1.

The full numerator degree is

    M_i = (0,0,-2,-2)_i + sum_v (71+2 bit_i(v)).

Therefore every input numerator is supported in 0<=n_i<=M_i. This is a complete global numerator space, not a sample, raw curvature summand, or unverified finite Laurent truncation. It deliberately overbounds the sharper N14 pair-specific degree facts when available.

There is NO standard-boundary factor of degree 5250 here. That large factor was needed for scalar solutions T(F), not the original three-owner F. The direct curvature formula therefore admits a substantially smaller numerator box while retaining all three physical owners.

## 4. Exact new multiplier and derivative accounting

For first carrier 1, the authenticated diagonal part of the seed selector is

    gamma = 2 v1 (v1^2+v2^2 v3)/h1.

It follows from the pinned I[12,1], P[:,6], and denominator entries. The tests check those literal sparse source lists; they do not multiply or expand them. Since C_swap,N=+ell_0,01 partial_1 F_N/2 in this sector, its selected scalar multiplier is

    W = gamma/2 * (bit_0(second)-bit_0(first))
                    * (x_0^2+1)/(2 x_0(x_0^2-1)).

The log denominator is owned by the carrier-1 owner whose bit 0 is one. The h1 denominator in gamma stays owned by the actual first vertex. Even when these happen to be the same owner, the ledger retains both factors correctly.

Write D=product_v d_v in the finite frame and rho=the SAME outer carrier54/legal29 product used in the fresh theorem. Then exactly

    rho W partial_1(P/D)
       = A P + B partial_1 P,
    A = rho W partial_1(D^(-1)),
    B = rho W D^(-1).

This differentiates the whole regular rational F_N (written F in the domain formula). No derivative is passed through an outer partition and no separate unregularized Leibniz term of an inner scalar solver is used.

The lowering computes new owned denominator ledgers for A and B and cancels them against the same exact outer quotient formulas. Its maximal displayed envelope is carrier16, legal3, and no standard-boundary denominator, safely inside outer54/legal29. Some displayed denominators are conservative because a syntactic derivative can retain a zero term before simplification. No bound relies on canceling them by unsupported physical identities.

For A, coefficient demand has target kappa and numerator exponent box 0<=n<=M. For B, express the derivative using the original numerator coefficient P_n: the target is kappa+e_1 and the box has n_1>=1, all other n_i>=0. This is the exact derivative coefficient shift, not a lowered degree box mistaken for an original-exponent box. Multipliers with zero derivative coefficient may be kept safely.

## 5. Complete support certificates and independent replay

`probe_direct_curvature.py` builds these NEW A/B rational AST roots for every remaining full assignment. It uses the public factored quotient and owner-ledger machinery but never calls the old four-term build or imports a saved old separator. Bounded composition sums remain symbolic; their summands are not enumerated.

`direct-curvature-support.json` binds each input mask triple, actual sorted owners, full numerator degree, both newly derived denominator ledgers, multiplier support bounds, projected target, necessary numerator interval, and strict separating gap.

Every certificate uses w=(-1,-1,0,1). If [m_lo,m_hi] encloses the multiplier's support projection and [p_lo,p_hi] is the complete numerator projection, the certified inequality is

    target - m_hi > p_hi.

Thus the demanded coefficient is zero for every polynomial numerator in the entire declared domain. All 512 A/B associations satisfy this strict inequality. The minimum gap is 30. No cancellation between assignments or between A and B is required, so arbitrary choices of which carrier-1 pairs are reversed by O cannot change the conclusion.

`test_direct_curvature.py` independently replays every bound using bounded-simplex VERTEX enumeration, instead of the builder's greedy support optimizer. This enumerates small metadata polytope vertices only, never the physical composition-sum terms. It rebuilds every new root, compares the complete saved record, recomputes derivative-shift inequalities, checks all owner ledgers, and checks the finite activity reduction. Source-selector and dependency-hash controls bind the specific public primitives used.

The dependency hashes identify the public support-certificate files used by this addendum. The earlier source-order note and its eight abstract tests remain unchanged.

## 6. Conclusion and remaining limits

The assembled curvature defect is zero term by term for any carrier-block-preserving order. Combined with the prior fresh complete-domain theorem and seed-4 naturality, this proves the conditional universal zero statement at the start of this note.

The remaining historical identification obligations are now narrower: exhibit the actual historical cover/source witness, its scalar edge-domain and curvature N14-domain membership, and its identification with this SAME refined seed construction if that comparison is intended. No concrete historical enumeration, historical scalar-41 equivalence, full-source primitive Q, or full detector homotopy Xi has been supplied here.

This is null's source-comparison result only. It does not take ownership of other scalar/seed work. No physical polynomial operations, external posting, resource-policy changes, arithmetic execution admission, or global obstruction conclusion occur in this package.

## Reproduction

From this package in its published directory, with an unchanged public `null-support-certificates` dependency, run:

    python -B prepare_certificate.py
    python -B test_direct_curvature.py ../../../null-support-certificates

For optional regeneration of this new certificate only:

    python -B probe_direct_curvature.py ../../../null-support-certificates

Preparation authenticates and restores the distributed certificate. The test command independently verifies it. Optional regeneration rebuilds the NEW 256-tuple certificate and public dependency hashes. None reruns the previous full assignment/support scans.
