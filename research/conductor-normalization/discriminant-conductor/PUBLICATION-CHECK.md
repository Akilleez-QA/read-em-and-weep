# Independent publication review: unit 02

Verdict: PASS for the pure binary-quartic normalization, conductor, and covariant theorems at the exact proof revisions below. This does not certify the separately published HM-module or polar applications, any actual-instance computation, or future edits.

Reviewed on 2026-10-20: both staged PROOF files; both split historical audits; README, INPUTS, HISTORY, COVERAGE and SOURCE-HASHES; the PR description; and the ten-entry tree-elements payload. Re-reviewed the regular-pair addition and audit split after the initial review. The payload file containing this review must be synchronized after it is copied into the publication tree.

## Exact reviewed proof revisions

- `research/conductor-normalization/discriminant-normalization-conductor/PROOF.md`
  SHA-256: `c4512e49823fd3f21a85202568bdfd6f1292d03aefb7183610945a9264b45264`
- `research/conductor-normalization/explicit-conductor-covariant/PROOF.md`
  SHA-256: `d9a2bc898582a4118c4d83748f650ef4800b3720cbba62199e32dd0586f03986`

Reviewed split audit hashes:

- Discriminant audit: `5036abd3d560630d61ea1947333fe29ee2d784a40d388fd18408ac3773446f66`
- Covariant audit: `22132b9c087b38c567bd359b7a3302b107071f4dbfdd65201784f9314cec93aa`

All ten tree-elements content entries matched their staged files, and all four SOURCE-HASHES public checksums matched, before replacing the provisional review with this final verdict. Regenerate the tree-elements content entry for the review after copying it into the payload.

## Mathematical checks

1. Proper quasi-finite birational normalization and the generic cusp/node local models give the stated conductor orders.
2. Finite duality identifies an actual invertible conductor ideal, rather than only its numerical class or reflexive hull. This rules out an extra codimension-two ideal factor at quadruple roots.
3. Full-section-module Cohen–Macaulayness, Hilbert series, regularity, and minimality yield the normalization resolution. The row-deletion quotient retains its degree-six kernel.
4. Hilbert–Burch, generic reducedness, and absence of embedded primes identify the reduced conductor union everywhere, including the affine cone vertex.
5. The equivariant pullbacks of the five quartic generators have the exact conductor factor, with a base-point-free residual degree-four system.
6. The conductor square includes the tangency at the quadruple locus, and the descent criterion does not discard its nonreduced scheme structure or assume global-section surjectivity.
7. The explicit coefficients, primary-factorization signs, four syzygies, and completeness of the Hilbert–Burch matrix are correct. Independence over constants is used together with the already proved free resolution, not as a substitute for it.
8. The added regular-pair clarification closes the self-containment issue: the nondegenerate quadratic I is irreducible, the invariant cubic J is not divisible by it, and the degree-six complete intersection contains the degree-six irreducible triple-root surface. Unmixedness and the degree formula exclude extra components and nilpotents, so N=V(I,J).

## Scope checks

The explicit audit's module application is separated to unit09, and the discriminant audit's polar-layer application to unit06. Their endpoint, source-transport, and HM-cohomology premises are not required for the pure geometric claims approved here. The earlier malformed prerequisite locator and nonmathematical metadata labels have been removed. No absolute workspace paths were found in the unit's mathematical payload.

The original mathematical audits remain history; this review supplies the independent check of the staged proof revisions. No selected quartic, HM map, actual source, numerical rank, or obstruction value was evaluated. The PR description's pure-core claim is justified.
