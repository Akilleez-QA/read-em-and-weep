# Independent review

## Verdict

Accepted as a conditional, source-bound mathematical derivation bridge. No sign, overlap, mask, quotient, repeated-axis or composition-order defect was found in the pinned source. This is not a machine-checked proof, a production execution, a resource-admission result, or evidence that a physical residual vanishes.

The eight reference methods agree with the full source AST. Exactly 53 original class methods, excluding those named `laurent_coefficient`, agree with the inert candidate. The full textual diff adds Laurent-certificate-related methods and classes; it does not alter the original helpers, imports, class decorators, or ordinary derivation definitions. Equality of selected method ASTs alone would not establish that last fact; the complete pinned source/candidate comparison was also inspected. Added certificate functionality remains outside this theorem.

## Mathematical checks

- The sixteen masks form a free basis of the quotient over K by successive monic-quadratic division. A separate field claim about the quotient is unnecessary.
- Construct the derivation first on B=K[Y_0,...,Y_3], with D_i(c)=Y_i partial_i(c) and D_i(Y_j)=delta_ij h_i. The relation ideal is stable because D_i(Y_i²-C_i)=2Y_i h_i-(3x_i²-1)Y_i=0. It therefore descends to the quotient. This explicit lift clarifies the original proof's compressed polynomial-extension sentence.
- Reduction of each overlapping mask bit contributes exactly one C_i; parity is XOR. The multiplication loop implements this for all mask pairs.
- Differentiating a rational numerator/denominator yields (N_i D-N D_i)/D². Localization proves representative independence. Nonzero formal D has nonzero square.
- For an absent bit, V_i toggles the bit and differentiates c. For a present bit, it toggles the bit and yields C_i c'+h_i c. Consequently the second derivatives are respectively C_i c''+h_i c' and C_i c''+3h_i c'+3x_i c.
- Different axes commute because their commutator is a derivation vanishing on all generators and their rational inverses. The finite symbol checks corroborate the two-state rule but do not replace this proof.
- The jet loop applies the listed axes in sequence, hence denotes V_(i_n)...V_(i_1). Repeated axes are preserved and the empty sequence is the identity. Commutation is mathematical, not a claim of equal resource consumption or identical runtime objects.

## Exact accepted premises and residual gaps

1. Standard Python integer, Fraction, tuple, dictionary, iteration and bitwise semantics are trusted. No interpreter or standard-library verification is supplied.
2. The exact pinned definitions are used without monkey-patching, forged objects, hostile iterators, mutated execution internals or incompatible subclasses. Objects satisfy constructor invariants, share one live Execution, and axes are a finite sequence of valid integers.
3. Operations return successfully within their resource limits. The proof says nothing about affordability, admission, termination of arbitrary callers, or physical evaluation feasibility.
4. Rational denominators are nonzero formal polynomials. Specialization to geometric points requires a separate nonvanishing or regular-extension argument.
5. The source inspection and ordinary mathematical reasoning are trusted. Hashes bind bytes; matching AST contracts and finite mutation controls do not mechanically prove semantic correctness.
6. No general multi-term Element inverse, polynomial long-division correctness, Laurent-certificate theorem, primitive identity receipt, owner/chart theorem, transport identity or global residual comparison is discharged.
7. The reported historical commit association is provenance only. No remote checkout or manifest authenticity was independently verified, and the historical manifest is not needed to reproduce these controls.

## Reproduction and control strength

The original checker passed 915 checks both normally and under Python -O. The portable checker passes 918: the original controls plus a pinned reference-contract file and exact eight-reference/53-core cardinality checks. Explicit exceptions enforce every check under optimization.

The negative-pin harness appends an inert comment separately to each of the three pinned inputs in temporary copies, and requires the specific pin rejection in both normal and optimized modes. All six controls pass. This tests byte binding, including changes that preserve AST meaning.

The formal model checks repeated derivatives using an abstract h'_i token. The identification h'_i=3x_i is supplied by the explicit mathematical derivative of h_i=(3x_i²-1)/2, not by evaluating curve polynomials. None of these runs imports production code, executes source AST, constructs production field objects, evaluates physical sources/models/owners/jets, or performs actual polynomial products.
