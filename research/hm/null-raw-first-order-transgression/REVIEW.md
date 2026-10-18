# Independent review

## Verdict

No mathematical defect was found in the conditional ordered transgression theorem. The original proof's primitive-frontier wording was stale: C already has a separate structural proof, while primitive A remains supported here only by imported historical exact-computation evidence. The portable proof corrects that wording and imports C rather than claiming to reprove it.

## Inspected reasoning

1. Expanding delta T before applying any trace yields exactly XY-(X+C-B)(Y+D-C). This is a free associative identity, so no cyclic Cech trace is involved.
2. A' is a chain-map-valued form because both split connections commute with the same transported differential. B and the old A need not be chain maps. Products of coefficients of A' remain chain maps; cancellation of paired diagonal blocks is therefore justified only for A'.
3. The degree signs and squared line weights give -5+15-90+50=-30.
4. The edge correction -15r/8 combines with the antisymmetric wedge coefficient to give the ordered triangle term 15 Q_ab/4. Dropping or reversing the correction does not do so.
5. The transported column differences are -P^t and -Q^t. Ordinary coefficient transposition gives tr(Q_b P_a-Q_a P_b)=-2 tr(C). The inverse and transport order were checked explicitly.
6. The earlier common-frame correction was inspected. Multiplying prescribed middle columns by ambient nu gives I diag(nu,nu^-1). Both split and old connection coefficients acquire the same -k dlog(nu) term, which cancels in B. No spurious scalar shift belongs in A^E.
7. The frozen scalar source retains the original B_i B_j order, both endpoint traces, all four internal signs/weights, the factor 1/4, and the edge coefficient -15/8.

## Evidence and limits

The reviewer read the original transgression proof and checker, both immutable source snapshots, the moving-frame bridge, transition bridge, primitive contraction bridge, root-line proof, narrow scalar implementation bridge, earlier common-frame correction, and the later structural-C review. Original checker runs passed under normal Python and -O. The portable checker also passed in both modes from a different working directory.

The formal checks do not verify arbitrary Cech/exterior algebra software, actual primitive entries, arithmetic-engine semantics, legal chart coverage, source-specific determinant normalization, or full physical-frame correspondence on every chart. These remain explicit dependencies, not consequences of a PASS output. The actual B/C results are imported from their separately scoped evidence. Historical A was not replayed or independently attested.

The source snapshots were inspected locally and bound to their supplied immutable pins. This review did not independently re-fetch the repository or authenticate a remote historical execution. The AST contract was extracted from the exact reviewed source and is a source-drift control, not independent semantic execution.

Original files were preserved. No physical source or production module was run, no actual model product was formed, and no external publication occurred.
