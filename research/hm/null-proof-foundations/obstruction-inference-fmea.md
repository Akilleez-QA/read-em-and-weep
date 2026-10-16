# HM obstruction inference FMEA and root-cause audit

## Result and scope

No actual obstruction value follows from the current artifacts. The selected eight-root support exclusion is valid for exactly seed4/row2, carrier(1,2,4), legal(12,13,15), standard(3,11,15). The complete detector remains uncomputed. The strongest live failure mode is promoting this bounded zero to a global zero or promoting a local/formal survivor to a nonzero obstruction.

Ranking below is by consequence and live unresolved status, not frequency. No failure probabilities or RPN scores are assigned. A mathematical proof, tested compiler protection, and remaining implementation obligation are distinguished explicitly. New tests are abstract inference witnesses; they do not install an actual semantic admission guard.

## Priority 1: live gaps that could reverse the final conclusion

### 1. Partial detector or source block promoted to complete obstruction (false zero or false nonzero)

Correct chain: Rsharp = M0^0 + Fq kp + Fp kq + Ep(Tq Fq) + Eq(Tp Fp). The complete Phi has all three terminal rows and 78 signed staircase seeds plus all eligible outer owner assignments. The derivative blocks are not optional even though the scalar solutions can be eliminated from the direct pairing formula. All three terms of T* survive: H_rho*, Pi* K_cov* R*, and Pi* S* h* A* R*.

Root cause: confusing a linear reduction with deletion of its correction terms; confusing seed count or one selected full-owner zero with coverage of the entire sum. Failure is silent because a partial expression can itself be closed or evaluate to zero.

Implemented protection: scalar kernel typed branch compilation and actual-admission refusal; canonical seed serialization and exact 78-path audits. Proof protection: `direct-scalar-free-pairing-reduction.md`, equations (2) and (3); `authenticated-refined-detector-composition.md`, equation (1). These do not constitute evaluated all-owner coverage. Live dependency: complete exactly regularized rows/owner sum and complete representative, or a valid global identity replacing them. Current v5 kernel still records 78 regularization/Laurent-lowering obligations.

New regression: an exact rational complex C1 -> C2 -> C3, D1(t)=(t0,t0,0), D2(x)=x0-x1, Phi(x)=x2. It has one-dimensional H2. A zero baseline plus either a B(F)-labelled or E(TF)-labelled closed correction has detector 1; deleting that block gives false zero. A baseline class 1 plus correction -1 gives false nonzero if only the baseline is retained. These are independence countermodels, not HM realizations.

### 2. Local or formal nonzero promoted to actual obstruction (false nonzero)

M0 is generally not closed. Phi can be applied linearly to its individual summands, but class interpretation belongs to the complete closed Rsharp. The second-jet shear example diag(1,-1)/8 disproves a universal transition-local first-jet reduction; it does not prove an actual HM value or detector survival. A support envelope intersecting a demand region is only failure to prove zero. Formal nonzero coefficients may vanish at actual parameter specialization.

Root cause: conflating cochain and cohomology, necessary support conditions and sufficient nonvanishing conditions, or universal jet countermodels and the fixed physical source. Existing protection is principally explicit theorem scope in `second-jet-no-go-independent-audit.md`, `selected-support-separation-independent-audit.md`, and the prefix-pruning counterexample; the coefficient checker also labels formal counterexamples appropriately. Live dependency: actual closed complete representative, exact actual coefficient, and the authenticated complete detector pairing.

New regressions: on a tetrahedron, an edge cochain supported on (1,2) has a coboundary with nonzero values on triangles (0,1,2) and (1,2,3), yet is exact and closed. A separate model has nonclosed M0 and nonclosed correction with closed sum. The two polynomials x^2 and -x^2 have overlapping support but zero sum. Formal t is nonzero in Q[t] and specializes to zero at t=0. None is an actual HM evaluation.

### 3. Owned-domain clipping or unsupported small-jet quotient (false zero)

The exact complex uses every homogeneous monomial 0<=a_i<=n_i+sum deg_i(d_v) and all 1536 common vertices. Solver-observed support is not this full space. D1D0=0 alone does not establish H1=0 after clipping. Nor does D0^t e=0 on a clipped domain prove a complete dual filling.

Existing proof/test protection: `owned-denominator-finite-domain-certificate.md` proves full-domain H1 exactness through the acyclic sheaf Koszul resolution and proves boundary annihilation via a bounded primitive; `test_owned_denominator_complex.py` contains the omitted-column example with e(z)=3 despite all retained gauge tests passing. `check_rectangular_jet_factorization.py` derives full sparse rows and rejects off-stencil monomials; actual metadata admission is closed. Live dependency: complete actual Laurent multipliers, instantiated exact row/filling residual, and schedule. The full-domain theorem is not missing; its small computational realization is.

## Priority 2: protected transformations whose invariants must survive further lowering

### 4. Wrong-owner merger or old four-tail descent (primarily false zero; either sign possible)

A common vertex is (carrier, legal mask, standard tag), not merely a carrier. Distinct tagged vertices remain distinct even when their physical source label repeats. Equal divisor factors retain multiplicity. Matching endpoint frame owners are required for Iphysical Rphysical^t Pphysical = I Rnormalized^t P. Prefix carrier equality may prune only after common-frame conversion; it does not prune repeated tail carriers.

Root cause: quotienting labels before proving descent, reassigning a sorted owner's tag, or merging scalar-solver dummy indices with outer owners. Implemented tests: complete owner checks, asymmetric legal/standard bit-order controls, wrong endpoint/owner negatives in frame cancellation, and repeated-tail allowance in independent pruning tests. Mathematical negative witness: carrier1's nonzero selector on a repeated-carrier tagged triple can occur for a closed exact cochain, so closedness alone cannot justify pointwise pruning. Live dependency: preserving this ledger through all remaining Laurent grouping. No new carrier-only descent has been proved.

### 5. Omitted frame, denominator or zero-order derivative terms (false zero or false nonzero)

For C(alpha partial_i+beta)(cP/D), the exact multipliers are A=C[alpha(c_i/D-cD_i/D^2)+beta c/D] and B=C alpha c/D. The derivative does not hit external C. In moving matrix frames, T_ab,d=partial_d K_ab+Q_b,d K_ab-K_ab Q_a,d; canceling nu in a matching contraction does not delete the Q terms. Complementary finite-frame c=alpha=1,beta=0 is an authenticated special case, not a universal rule.

Implemented protection: arbitrary-function quotient/product-rule tests, nonconstant conversion controls, all-current AST Q-term checks, and wrong-orientation/double-normalization negatives. Live dependency: exactly-once frame and derivative treatment in every remaining actual Laurent lowering. The independent suites rerun below pass.

### 6. Incorrect support/stencil arithmetic (false zero)

For complete edge numerator x^a, the row is A_(kappa-a)+sum_i a_i B_i,(kappa-a+e_i). B has no contribution at a_i=0. Standard homogeneous degree remains 5250 even if its finite-chart expression is 1. Current support exclusion uses mixed directions, not only coordinate boxes; every target shift and the nonzero derivative subdomain are material.

Implemented protection: independent polytope-vertex optimization versus production greedy allocation; exact full homogeneous box checks; cancellation-conservative support envelopes; derivative-shift checks; malformed inverse/template rejection. The selected gaps are 29 on edge(1,2), and 100 or 101 on edge(0,1). These tests protect the one authenticated tuple, not every owner assignment. Live dependency: coverage and regularity proofs for the remaining tuples.

## Root-cause structure and release criteria

The recurring root cause is a domain or quantifier substitution: selected -> complete; local -> cohomological; formal -> physical; envelope -> support; same carrier -> same owner; full space -> clipped space. Numeric exactness does not repair such substitutions.

Before claiming a global zero, require explicit coverage of the complete Rsharp pairing, every retained owner assignment and terminal row, with justified zeros or exact cancellation. Before claiming nonzero, require an exact actual coefficient of the complete authenticated pairing, not a support possibility or a generic jet value. Preserve closure/comparison hypotheses, ownership multiplicities and frame derivatives. A detector value of zero alone also needs the relevant detecting/completeness theorem before being promoted to class vanishing; this audit does not supply a new theorem of detector faithfulness.

Test arithmetic is confined to abstract rational models and metadata audits. Counts of proof-tool operations are not physical execution costs.

## Reproduction

`test_obstruction_inference_guards.py` contains seven unittest methods across two guard families. With the companion tests available on the Python import path:

    python -B -m unittest -v test_obstruction_inference_guards

The source audit records this combined regression:

    python -B -m unittest -v test_actual_scalar_differential_kernel test_generic_kernel_frame_cancellation test_refined_selector_pruning_independent test_selected_support_separation_independent test_selected_coefficient_support test_obstruction_inference_guards

Reported result: 39 methods passed. The finite-owned-domain and jet checker protections above were source/audit reviewed here; they were not included in that 39-method rerun. New tests are deliberately independent of physical source construction and should not be represented as actual detector authentication.

## Dependency scope

Companion references are identified by basename. A referenced file not supplied with this collection is an external prerequisite, not an embedded proof or a verified relative link. The reading order and unresolved conditions are listed in `proof-notes-index.md`. Reported test results describe the source audit; this proof copy does not by itself constitute a new test run.
