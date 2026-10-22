# Independent review: Gram spectral geometry

Verdict: PASS, conditional on the pinned structural input. This is independent mathematical review, not proof-assistant formal verification and not independent reevaluation of the actual HM map.

Reviewed PROOF.md with SHA-256 33a0e355ee9beaec7d87576217ee88129a207242bd4830fbb3b5f17e9768c3d3. This is the final proof version after the status sentence was updated to record this review.

The reviewer read the immutable Gram-composite source at commit 15adb8e5ea61f07e87df6a0044b7375e580fe7f3. It supplies the required self-adjointness, characteristic identity, and reduced twelve-point determinant divisor. The proof makes no additional actual-instance assumption.

## Checks

1. The cyclic algebra O plus O(-4) plus O(-8) is globally well defined by d in H0(O(12)). Simple zeros imply both local smoothness and irreducibility over the base function field. Riemann--Hurwitz gives genus ten and distinguishes this cover from the genus-four support. The relative dualizing twist O(8) and canonical twist O(6) are correct.
2. E becomes a rank-one module over the generic cubic field. Base torsion-freeness implies spectral torsion-freeness by the norm/adjugate argument. One may clear denominators when using it for arbitrary local spectral sections. Smoothness then makes the module a line bundle B, including at ramification points. Its degree is twelve by Euler characteristic.
3. The perfect symmetric pairing is spectral-algebra-linear precisely because M is self-adjoint. Finite duality gives B squared equal to the relative dualizing line, with no inverse or missing base twist. Thus B(-4) is two-torsion. Nontriviality follows from the incompatible pushforward splitting, or global-section counts six versus three. The theta characteristic B(-1) has square omega_S and no sections by projection formula. Its even parity is therefore correct.
4. The full centralizer is End over the spectral algebra of B, hence pi_*O_S. This proves the sheaf statement at the totally ramified fibers, not just a generic rational identity. The twisted coefficient degrees m, m-4, m-8 and both dimension formulas are correct. All commuting sections are self-adjoint, so the skew-adjoint intersection vanishes in characteristic zero. The resulting zero infinitesimal orthogonal stabilizer does not exclude discrete stabilizers.

## Novelty and boundaries

Relative to the two cited inputs, the genus-ten spectral module, nontrivial two-torsion, ineffective theta characteristic, complete centralizer, and orthogonal infinitesimal-stabilizer exclusion are new derived consequences. The spectral construction is a general method applied to the newly pinned actual Gram map; no claim of novelty for that general method is warranted. No exhaustive comparison against every repository file was undertaken.

The separation from the genus-four cubic support is essential and is maintained. The deck action on the cover is not asserted to lift to B or its theta characteristic. The proof neither assumes the remaining correction commutes with M nor proves a value or nonvanishing statement for the normal cohomology class, the third Bockstein, or the open algebraicity goal.

No selected coefficients, points, actual matrices, actual ranks, or large computation were evaluated. No external state was changed.
