# Uniform legal-mask exclusion for one fixed carrier sector

## Result and precise domain

For seed4, terminal row2, staircase(3,11,15), and source-first carriers(1,2,4), every legal-mask tuple gives the zero E12 coefficient functional on its complete numerator domain. The computation is metadata-only: no physical polynomial expansion, evaluation, coefficient extraction, or physical product was used.

Legal masks use low-bit coordinate order; standard tags use high-bit coordinate order. The standard infinity-coordinate sets are respectively {2,3}, {0,2,3}, and {0,1,2,3}. Thus the active legal masks are

- owner0: 0,4,8,12
- owner1: 0,1,4,5,8,9,12,13
- owner2: 0 through15

There are 4×8×16=512 active tuples, with4096 individual A/B functionals. Every one is separately support-excluded. In the complete16³=4096 label domain, the other3584 tuples have an exact literal-zero outer quotient: at least one legal bit lies on a finite-standard coordinate. These labels are classified, not deleted from the numerator complex. All4096 tuples are certified zero; none is unresolved in this fixed sector.

The separate parameterized lowering uses the original Lower class, with only the three legal masks substituted in the build function. It keeps the complete seed/owner/carrier/legal/standard labels in every actual denominator. At the original masks(12,13,15), the complete serialized artifact is byte-identical to the authenticated original. Original files are unchanged.

## Root cause: support obstruction is uniform and monotone

This is not cancellation among legal masks, among currents, or between A and B. Each individual multiplier's allowed exponent envelope is separated from the complete coefficient-demand domain. The same normals work throughout:

- edge(1,2): w=(1,0,1,1)
- edge(0,1): w=(0,-1,0,1)

Let moi denote coordinate i of owner o's legal mask. For all four edge(1,2) A/B multipliers, the exact envelope-separation gap is

    487 - 58(m02+m03) - 57(m10+m12+m13+m20+m22+m23).

Its minimum is29, attained at masks(12,13,13) and(12,13,15). The bit m21 is invisible in this direction.

For the first edge(0,1) term, both A and B have gap

    273 - 57(m03+m13) - 58m23.

For the second term, both have gap

    272 - 57(m03+m13) - 58m23.

The respective minima are101 and100. Each is attained by64 active tuples: exactly those with m03=m13=m23=1. Other bits are invisible to these gaps. Hence setting every allowed legal bit to1 is a worst case, not a lucky choice. Removing an allowed bit can only enlarge the relevant gap or leave it unchanged.

These identities were checked exactly over the complete512-case finite domain, not inferred statistically from a sample. The underlying arithmetic explanation follows.

## Why the coefficients are58 and57

Write t=x_i^-1, q=1-t². The line portion of the actual outer quotient is

    m=0: sum(k=29..57) binom(57,k) t^(2k-29) q^(57-k)
    m=1: sum(k=0..28) binom(57,k) t^(2k) q^(28-k).

For a direction with w_i=1, these factored expressions have upper support bounds−29 and0. Switching m from0 to1 therefore changes the bound by+29. The extra homogeneous pullback x_i^-58 changes it by−58, while the legal clearance L_i^29 with L_i=x_i(x_i²−1) changes it by+87. The net is+58 for an off-edge owner.

For an on-edge owner, its actual inverse denominator contains one L_i, reducing that change by3. The full numerator degree increases by2. Together they decrease the separation gap by55+2=57.

For w_i=−1, the line bounds are85 and56, a change of−29. Homogenization adds58 and legal clearance subtracts29, for net0 off-edge. The only variable negative-direction bit here is m21, and owner2 is off edge(0,1); the two on-edge owners are forced to have coordinate1 legal bit0. Coordinates of weight0 make no change.

### Current-denominator compensation

The preceding explanation retains the actual current denominators; it does not replace them by uniform divisors. Let ell_oi be the legal order in the multiplier's derived denominator ledger, e_o indicate edge membership, and h_i=max(w_i,3w_i). Let N be the upper envelope bound of the first root factor, namely its cleared rational numerator. The independently audited finite-domain invariant is

    N - sum(o,i) (ell_oi - e_o moi) h_i = N0.

In the saved term/A/B order, N0 is(113,83,113,82,67,55,68,56). Carrier and standard orders are mask-independent. Thus all extra common-denominator legal factors in the current numerator are compensated exactly at the envelope level. The residual edge denominator is exactly the one used in the58/57 calculation. The exhaustive independent check of this invariant makes the causal reduction auditable rather than relying on a fitted affine formula.

## Full-domain and derivative conventions

Every vertex's complete homogeneous degree in coordinate i is

    5250 + 14×5 + (1+2moi).

The5250 standard degree remains present on finite standard charts. Each edge degree adds both vertex degrees and the input character(0,0,−2,−2). The terminal target is kappa=(−1,−2,−2,−2). A tests multiplier exponent kappa−a; B tests kappa−a+e_d and requires a_d≥1. B's derivative factor is therefore not silently evaluated at0, and target and numerator exponents are not confused.

Each terminal owner composition is a singleton at(0,0,0,0,2671), with zero bases appearing only to exponent0. With polynomial convention0^0=1, the body and chained binomial coefficient are exactly1. No physical polynomial evaluation is needed to establish this template identity.

## Failure-mode controls

- Reversing mask bit order would give the wrong512 active labels: decoders are independently checked using binary strings.
- Using observed numerator support instead of full homogeneous degrees could manufacture separation: every domain is reconstructed from full section degrees.
- Dropping full owner labels could falsely merge denominators: every ledger is checked against the exact owner tuple.
- Forgetting the B target shift or its a_d≥1 condition changes the gap: both are checked independently.
- Treating0^0 as0 incorrectly discards the terminal outer weight: singleton identities are checked non-vacuously.
- Envelope overlap is never a nonzero certificate. In this domain there is no overlap case left unresolved, but that logic remains explicit.
- The result establishes this fixed carrier/staircase/row sector. It does not predict whether changed carriers, staircase, terminal character, or coefficient target retain these normals or positive gaps.

## Reproduction and artifacts

- lower_legal_mask_sector.py: separate parameterized lowering
- preflight_legal_mask_sector.py and legal-mask-sector-support.json: exhaustive label-domain certificate
- derive_legal_mask_gap_patterns.py and legal-mask-gap-patterns.json: exact closed-gap verification
- test_legal_mask_sector.py: independent polytope-vertex support audit and provenance/domain tests
- legal-mask-sector-test-results.txt: final independent test transcript

 Private resource configuration is omitted; execution release remains false. No execution release or global factorization admission follows.
