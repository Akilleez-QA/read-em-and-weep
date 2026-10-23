# Independent review: zero-arrow reduction for a regular compatible radical line

Reviewed 2026-10-23 UTC separately from the author's self-check. Earlier
published source2 reduction and quotient-normal-form packets were not changed.

## Exact reviewed files

- PROOF.md SHA-256: `3cc300e831db7caf1d69af0411f65bdf912826623bfe18c13ba21e3412d695cd`
- verify.py SHA-256: `567b96e6db230131ea3636123f7f57714981dae2cf50c3d3ce6296f8f3baa74b`
- INPUTS.json SHA-256: `bba5d9624f0fe2d6849d374eafd21874778b904f235d09df7934216ed3b4733f`

Verdict: PASS for the stated conditional theorem. Neither compatible-line
existence nor its direction or restriction rank is established here.

## Independent mathematical checks

Read the entire proof and checker. The exact PR795 first-arrow properties,
PR794 strata, and the previously independently checked PR950 and PR953
reductions give the stated interface.

1. The regular quotient is N0 + N8 + (V+D)[2]. Its first arrows on N0
   and N8 are injective for every nonzero pencil variable. Therefore its
   common first-arrow kernel is exactly the intrinsic isolated V+D space,
   not just a chosen eight-dimensional summand. Every negative quadratic
   kills it by factoring through the first arrows.

2. Equivariance and ker(barQ)=A+D force injectivity on V. The single D
   in Z maps either injectively or to zero; distinct irreducible supports
   prevent cancellation between its image and the V image. Thus the only
   ranks are8 and3. In rank3 the killed D is the actual D in ker(barQ),
   not an arbitrary isomorphic copy.

3. The active quotient is well-defined because the image of Z under the
   whole deformed pencil is the constant space Y=barQ(Z). The displayed
   block matrix correctly retains an arbitrary C(t) off-diagonal block.
   Its triangular domain change has polynomial inverse, preserves the
   t-adic filtration, and contracts only the constant invertible F block.
   When rank3, the additional D[0] is retained as a separate zero-differential
   complex. Dropping that summand would be incorrect; the text does not do so.
   These chain operations prove filtered homotopy equivalence, not merely
   agreement of dimensions or unfiltered cohomology.

4. Independently recomputed sizes and invariant cohomology. Rank8 leaves
   24->20, kernel A+D, cokernel P, rank16. Rank3 leaves an active24->25,
   kernel A, cokernel P, rank21, plus the permanent five-dimensional kernel.
   The long exact sequence of Z->Y (which is onto) gives the asserted
   kernel quotient and unchanged cokernel without requiring Q-stable
   summands in the negative-pencil normal form.

5. In rank3 the reduced32->28 family has a constant five-dimensional
   kernel and hence rank at most27. Restoring PR950's formally invertible
   nine-block gives original rank at most36 over C((t)). The proof then
   correctly invokes polynomial37-by-37 minors to extend that bound to
   every scalar t, including values at which the first cancelled block
   might become singular. It does NOT misuse formal invertibility as
   pointwise invertibility at all scalar values.

6. Checked the final multivariable extension: C[[z1,z2,z3]] is an integral
   domain, the original image block has invertible constant term, and the
   same fixed D remains in the quotient kernel for all three formal
   directions simultaneously. Rank over its fraction field is at most36.
   The injection of the polynomial ring into the power-series ring forces
   all maximal minors to be identically zero polynomials. Thus the result
   holds on the whole affine family Q+Sym²W, not just a formal neighborhood.

7. The resulting nonsurjectivity concerns only each q0+t a family in the
   specified negative quadratic space under the stated regular compatible
   line and rank3 hypotheses. No assertion covers all quadrics, excludes
   source2, or excludes the pure V or exceptional mixed compatible-line
   alternatives. Rank8 is necessary for surjectivity in those families,
   not sufficient. The four-pair frontier is unaffected.

## Executed evidence

Independently ran `python verify.py` and `python -O verify.py`:244 checks
pass, with byte-identical JSON. All five input SHA-256 and Git blob
checks pass. The checker performs bounded synthetic character and block
elimination tests only. The final30 additional checks verify coefficientwise cancellation for three
formal variables. Its finite scalar samples are supporting regression
tests; the universal formal cancellation and all-scalar conclusion follow
from the written algebraic proof and polynomial-minor argument, not sampling.

This review is supporting verification of the new deduction, not itself
new progress or proof-assistant certification. No actual-source coefficient,
point, slope, matrix or rank was evaluated, and no external run was started.
