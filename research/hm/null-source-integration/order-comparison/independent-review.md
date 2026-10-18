# Independent review: source-order curvature comparison

## Verdict

Accepted as an exact abstract order-defect calculation and a conditional seed-4 reduction. No sign correction is needed in the six-permutation table, the identity `delta E = -A(F)`, or equations (S), (T), (U), and (V), under their stated hypotheses. This is not a historical-order seed-4 zero certificate or a comparison of actual historical and fresh sources.

The inspected eight-test suite passed independently with `python -B test_order_defect.py` on 2026-10-16. Only abstract exact-rational tests were run. No physical polynomial operation, support scan, source-model execution, or external posting was performed.

Reviewed file hashes:

- `source-order-curvature-comparison.md`: SHA256 `ce91f2663d5272bec5f7ead7449c6cd7b6d389345942aa8482a72abf9a0497a1`
- `test_order_defect.py`: SHA256 `b033421bcd172b3397056f95e5afb98184690a059be4eef80475f715c26a1d10`

## Accepted mathematical claims

1. **All six signs.** For the original oriented triangle, the defect is zero for 012 and 210, `-B_01(F)/2` for 102 and 201, and `+B_12(F)/2` for 021 and 120. The table uses the original orientation of F. Independently reducing to `e(l,r)=(l01*r12-r01*l12)/2`, with `l02=l01+l12`, verifies the table. Testing potential differences `l_ij=h_j-h_i` loses no local cocycle: every additive current on a simplex has this form, entry by entry. The complete bilinear-basis tests therefore certify the formal identities, not merely sampled values.

2. **Differential sign.** The cup Leibniz rule gives `delta(l cup r-r cup l)=-l cup delta r-delta r cup l` when l and r have degree one and delta l is zero. Subtracting the second directional pair yields precisely `delta E_p(t)=-A_p(delta t)`. The full tetrahedral bilinear-basis test agrees. The artificial SL2 example genuinely has a nonzero reordered-prescription defect. The separate tetrahedron example has `delta E=N/2`.

3. **Reindexing is a chain map.** Extending one already defined cochain alternatingly is distinct from evaluating the cup prescription anew on the reordered tuple. The note consistently keeps these operations separate. The owned-denominator numerator complex also reindexes by signed tuple permutation: its denominator product and each owner occurrence are retained, and the multiplication differential conjugates accordingly. No historical nonlinear construction follows from that linear chain isomorphism alone.

4. **Conditional seed-4 naturality (S).** The local authenticated detector composition confirms that the q=2 seed has only the inclusion, with no prefix homotopies. The fresh seed-4 audit confirms the fixed staircase `(3,11,15)`, target `(-1,-2,-2,-2)`, and coefficient/selector `-2*[12,6]`. For an intra-carrier reorder, the actual first owner may change but its carrier does not. With the same bare carrier I/P, `P I=1`, matching physical frames, identical owner weights, and the same underlying alternating residual, the generic frame-cancellation identity proves termwise naturality. Sorting signs cancel through R. The new artificial inclusion test is consistent with this proof; it is a control, not authentication of the physical data.

5. **Conditional reduction (T).** From `C_ON=E_N R_1-R_2 E_O`, applying L4,N and (S) gives the displayed minus sign. The fresh support theorem applies only after the reindexed historical input is shown to belong to its complete certified per-edge numerator domain with the actual character/frame conversions and owner ledger. Under that hypothesis, (T) is correct. Domain membership is an outstanding witness, not a conclusion of the abstract tests.

6. **Full comparison.** Equation (U) follows by linearity without assuming equality of curvatures. Equation (V), a valid admitted primitive Q, closure, and a full detector comparison suffice for equality of full source values. The note correctly does not apply full-detector boundary annihilation to an isolated seed, and does not reopen the finite-domain gap already closed by the later owned-denominator certificate.

## Required precision correction

The last paragraph of section 7 says the tests check “a single component's failure to annihilate a boundary.” The implemented test is evaluation of an arbitrary scalar coboundary at one triangle. It is not the actual seed-4 functional and does not establish that seed 4 fails to annihilate a particular admitted End boundary. Replace that phrase with:

> “a generic triangle-evaluation functional's failure to annihilate a boundary”

Likewise, the test name `test_single_component_does_not_kill_boundaries` may optionally become `test_triangle_evaluation_need_not_kill_boundaries`. Section 4's existing formulation that a seed is “not known to annihilate boundaries” is appropriately limited and should remain. This wording correction does not change any equation or conclusion.

## Outstanding source obligations and scope

- Keep the historical order O as an authenticated-order parameter. Numeric low-bit ordering is established for the fresh construction; the displayed coordinate-1-first list is only a contrasting example. No historical enumeration is supplied or inferred here.
- Retain the distinction between L4,O, the same refined seed construction in O order, and the historical scalar-41 detector. Their equality is not proved.
- A zero conclusion still needs a certificate for the curvature contraction in (T), or a direct historical-order support proof. The diagonal current shortcut is unavailable because the authenticated carrier-1 selector has a diagonal term.
- The original support associations do not automatically cover the cross-edge products obtained by expanding D F. No such coverage is certified by these tests.
- The eight tests do not certify real-source equality, historical numerator-domain membership, source closure, a cross-order primitive Q, a detector homotopy Xi, resource admission, or an obstruction value.

## Source checks

The review read the local copies of the combined seed-4 coverage audit, exact scalar dual-fill contract, authenticated refined detector composition, physical current source binding, generic kernel frame-cancellation audit, fresh-order contract, and owned-denominator finite-domain certificate. These support the structural and domain distinctions used above. This review does not independently attest to the note's historical inert-source SHA256 or to remote Git provenance; those are separate provenance claims.
