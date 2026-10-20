# Current independent mathematical audit

Review date: 20 October 2026. Verdict: PASS under the written hypotheses. This is a formal mathematical review, not machine-checked verification.

## S161: reduced Serre residue certificates

1. Every top Čech boundary misses a coordinate denominator, whereas every weight-minus-five monomial other than the all-minus-one monomial is such a boundary. The coefficient trace is therefore normalized exactly as stated. The ordered homogeneous volume, simplex orientation, Whitney factorial and barycentric integral have consistent signs and no extra rank-two or factorial factor.
2. Ordinary matrix trace identifies End(H) with its dual. The twists -r and r-5 sum to -5, and degree two pairs with degree two on P^4. The Stacks Project duality statements verify perfectness and the cup/evaluation interpretation.
3. The TW product is formed before integration. Both boundary identities have the correct Leibniz signs, so the pairing depends only on classes. No contraction is silently extended to the dual twists -4 or -3; Whitney extension there needs none.
4. Perfectness proves existence of a detecting dual class but produces no witness. Finite supplied representatives yield finite exact expressions; arbitrary cutoffs or a few zero pairings cannot establish vanishing.
5. Restriction from the dual of Hom(S_r,T_r) onto the dual of its equivariant subspace is surjective. Tensor decomposition and Serre duality therefore give the claimed finite-sum realization of every chosen parameter functional. The operation must be equivariant for equality of different lifts, as explicitly stipulated.
6. The imported four upper and eight lower parameters, the ten/twenty downstairs target dimensions, and the four lower/eight upper retained dimensions remain distinct. The lower slot flip is not replaced by the naive twice-iterated multiplicity flip. Full target image follows only conditionally on nonzero equivariant operation.


## Exact reviewed files

- `DEPENDENCIES.md`: SHA-256 `d76aacf629feb28a0075dd4bfbeae9ad2c7a9ea5946fa576e691f12424391324`.
- `MATHEMATICAL-NOTES.md`: SHA-256 `278892f60cc859e22887aae311d91f18676b20beb1ca116620809f5d7ef4ff91`.
- `PROOF.md`: SHA-256 `7cb9324ac84cc98659d3d8563815f4500d39989b1c0f2ba72fbac1ed6f121860`.
- `PUBLIC-SOURCES.md`: SHA-256 `46e3423d538a2872190a56cd54712fc1217c57fe6cbb24b86d1cf694eed8f58c`.
- `README.md`: SHA-256 `9b2d8097d88744827fc3e6c5671df779c1208348c8a50cbd298e8ac266ad10e7`.

The proof and supplementary mathematical arguments were read in full. Existing dependency files were independently fetched at their immutable commits; contents and Git-blob hashes matched the recorded pins. Newly published predecessors were read back before binding their immutable links. Reference substitutions change no mathematical statement.

The duality and projective-space cohomology sources were checked directly: [Stacks 48.27](https://stacks.math.columbia.edu/tag/0FVU) and [Stacks 30.8](https://stacks.math.columbia.edu/tag/01XS).

No selected HM/source-instance operation, source matrices, product values, ranks, jets, residuals, detectors or actual Massey values were evaluated. No mathematical experiment or large computation was run. No nonvanishing witness, positive-characteristic TW comparison, or source implementation is asserted.
