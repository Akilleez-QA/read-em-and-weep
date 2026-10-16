# Independent audit: selected full-owner E12 lowering

## Verdict

The selected carrier124 full-owner lowering is consistent with the authenticated source formulas and matching external pinned contraction certificate. All four audit corrections are satisfied in the snapshot below. This verifies one structurally active candidate tuple, not polynomial nonvanishing, all full-owner labels, a detector value, or arithmetic execution admission.

## Public snapshot (resource metadata redacted; mathematical content preserved)

- Compiler SHA256: `8c3bb290df33a2d17da477cd30a36cc581aeddc4cdb3e276fdfbf35973ced89d`
- JSON SHA256: `d07117856027c371cc3dd7c3dca21fc95fd34c32d8b84dbb6fa9693f416f506f`
- Tests SHA256: `1e3288ff01d3aa9ad5e87fcd49f9ebfe88b937d485aeaea899c2c28f531a12f2`
- Historical identity-report Git blob: `e55dae1fccef9b66bd5735b04fc09bd5590180fc`
- Historical checker Git blob: `25816d9ba8699ffaf20c562d9dd8403f049ae383`

All 15 tests were independently rerun successfully with `python -B -m unittest -v test_selected_kernel_denominator_lowering`. The historical physical-polynomial checker was inspected as text, not executed. No physical source polynomial, partition, current, coefficient, or residual was evaluated or expanded. New numerical tests use only abstract toy inputs.

## Source, current, and selector

The actual owners are seed4 occurrences0,1,2 with carriers1,2,4, legal masks12,13,15 and standard tags3,11,15. They are source-first with positive sorting sign. Legal masks use low-bit coordinate order and standard tags use high-bit coordinate order. Both Q terms are retained in each normalized tangent, with the actual rational logarithmic derivative.

The four edge/current/derivative choices and signs match E12. The complete pinned selector is -2 times entry[12,6] of I transpose(tf(R)) P; the terminal coefficient and E factor1/2 each occur once. Explicit trace-free projection removes the need to assert individual current tracelessness. Projection commutes scalar multiplication, differentiation, conjugation and Cech frame transport, so it is valid for the projected E contribution. This observation does not independently reprove the other M0 formulas.

The physical diagonal frames cancel in the complete selector contraction once. Neither a moving frame nor its Q derivative has been silently replaced by the identity.

## Reverse transition

The source certificate's canonical model SHA256 equals `b6b532c4bab5787397a4cddde34210c12fae71853b30cb73ecbe8a9c2b4826b2`, independently recomputed from the current pinned model. Read-only inspection of the matching historical checker shows all six charts are checked for:

- I_b P_b = Id - gamma H0_b - H1_b delta
- P_a I_a = Id
- delta I_a = 0
- P_a gamma = 0

Consequently P_a I_b P_b I_a = Id by inserting the first identity and using the latter three. Swapping a,b gives the other product order. Transposition proves inverse(C_ab)=C_ba for C_ab=(P_a I_b)^t. This uses the full contraction identities, not PI alone or determinant-one. Authentication now explicitly relies on the externally pinned exact certificate; it is not a new physical-polynomial computation.

## Factored polynomial and Laurent semantics

Every pinned I/P numerator is completely represented by rational constants, elementary-symmetric substitution, addition, multiplication and nonnegative integral powers. Rational denominator arithmetic aligns actual full-owner factors before cancellation. Quotient-rule differentiation is exact. Its unsimplified zero-derivative contributions can overestimate denominator orders but cannot invalidate clearance.

The local v_j formula equals tau times the finite v_j after substitution t_i=1/x_i. The bounded-composition domain is n_i>=0, sum n_i=L, n_j>=535 and n_i<=534 for i<j. Its chained binomial coefficient is the multinomial coefficient. The c_i powers are n_i and the v_i powers are n_i-535*[i=j], all nonnegative on that domain. The Cbar and legal-line binomial ranges likewise have nonnegative exponents. Complete homogeneous polynomials are represented by their exact finite recursive sums, without physical expansion.

Each cancellation uses only the identical full owner. For an infinity coordinate, the clearing factors contribute x_i^[-270-29*d], d=1 or3, and the retained standard denominator contributes x_i^-Z. The quotient is already pulled back by t_i=1/x_i. These are precisely one scalar pullback, with no additional section twist. The ordinary negative DAG powers have coordinate bases only.

The derived conservative representation orders across all eight A/B outputs are carrier20, legal3 and standard5251. These are not claims of minimal pole orders. Carrier123's final weight vanishes on standard15: c0 through c3 are zero while its chosen n3 is at least535. The carrier124 alternative is described only as structurally active; nonzero-node identity is not misrepresented as a polynomial nonvanishing proof.

## Corrections and tests

1. Denominator union keys are sorted. Saved JSON regenerates byte-for-byte under hash seeds1 and51.
2. Scope now says structurally active candidate rather than nonzero weight.
3. Tests now include abstract bounded-composition partition/body semantics at thresholds1..3 and dimensions1..3, exact rational quotient derivative controls, and scalar-identity trace-free annihilation.
4. Inverse rewriting now binds the historical certificate/checker by Git blob, SHA256, canonical model hash and the four required identity counts.

Existing mask, signs, owners, maxima, coordinate-only inverses, metadata mutation, excess/wrong-factor refusal and gates tests also pass.

## Remaining scope

The global78 regularization families remain unresolved. Extending the single tuple to other full-owner tuples and other sectors, and constructing a static arithmetic schedule and peak-byte certificate, remain separate work. Private resource configuration is omitted; execution release remains false. No execution release, public post, detector value or physical source evaluation follows from this audit.
