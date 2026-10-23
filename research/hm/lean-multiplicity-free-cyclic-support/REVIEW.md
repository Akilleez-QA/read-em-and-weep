# Independent review: multiplicity-free cyclic support

**PASS.** The final source proves the exact coordinate-support criterion over an arbitrary, possibly noncommutative ring for a dependent product of three pairwise nonisomorphic simple modules. Root's bounded final compilation and separate importing axiom check succeeded. This independent reviewer inspected the theorem statements, proofs, source delta, receipt inputs, artifact hashes and axiom output; no compiler was rerun.

Final source SHA256: `0ade8cbc9c112b3f16cfc32a64adb8913ec8ab705264500c9a2d087bc9fa6ae0`.
Check.lean SHA256: `97053157777ce3d6b467df2b4eae34a95925eb298a40f9b873313994a5a78dcd`.
Pinned mathlib: `d13f23b723b8a846827a245b89c10fc7d3f11612`; Lean 4.34.1.

## Mathematical review

All four declarations retain `Ring R`, modules indexed by `Fin 3`, simplicity of every module and explicit pairwise nonisomorphism. They are:

1. `multiplicityFree_hom_eq_zero`: off-diagonal maps vanish by the simple-module bijective-or-zero theorem; a bijection would give a forbidden isomorphism.
2. `multiplicityFree_endomorphism_coordinate`: finite coordinate expansion and the first theorem show that every endomorphism acts coordinatewise. The j→i component has the correct orientation.
3. `mem_cyclicSpan_iff_coordinate_support`: x lies in the R-span of v exactly when every zero coordinate of v forces that coordinate of x to vanish. Finite-product semisimplicity supplies a genuine complementary projection onto the cyclic span. Its diagonal component fixes v_i; when v_i≠0, the difference from the identity has a nonzero kernel in a simple module and must be zero. When v_i=0 the support condition instead gives x_i=0. Thus the projection fixes x, proving membership.
4. `cyclicSpan_eq_top_iff`: v generates the whole product exactly when all three coordinates are nonzero. Necessity uses a nonzero element of each simple module; sufficiency follows from the exact support criterion.

Coordinate preservation is derived, not assumed. There is no hypothesis that v already generates, that an observation is injective, or that the desired support formula holds. Neither commutativity of R nor scalar Schur's lemma is used. The zero vector and all partial-support cases are included. Pairwise nonisomorphism is essential: repeated simple modules permit diagonal submodules and invalidate the conclusion.

This supplies the abstract algebra behind the multiplicity-free cyclic-support step in PR891 at `eb83daa45fe4686a9f55da604fb2cc8c28d47fb0`, proof SHA256 `98fa36fff78c35f5dc071bbc52aa5e44e045c5f3a8252672a63e1015d027eed9`. It does not formalize the actual group-module decomposition, scalar orbit-span/group-algebra-span bridge, full tensor-family equivariance propagation, Hom dimensions 3/3/4 or 8/8/11, generic projective-open existence or admissible parameter selection. Physical globality, corrected-source membership, cohomology authentication and independent reference normalization remain separate certificates. No actual HM instance was evaluated, and no whole-source exclusion or main repair is claimed.

## Final delta and retained failure

The first proposed source, SHA256 `f33b83d0d2958262f498efe23e015de8efea2da2e77ecc3d9c8719c993ad8940`, failed compilation. Root preserved that exact source and receipt. Its raw receipt SHA256 is `4141976ad4c78613a30fca0e0010fa95f74b9837c5bc817cb8c5f98ba7bf096e`; diagnostic stdout SHA256 is `6d9c75bade4740689b3b0682251e69b39759ce38b662aac6df58256968583287`.

The independently inspected final diff adds `False.elim` to use a contradiction, supplies M explicitly to `sum_single_apply`, adds the endomorphism type to two d−id expressions, and changes `haveI` to `have` following the linter. All theorem statements and assumptions are unchanged. No proof obligation was removed or replaced by an axiom. The original writer's UNCOMPILED scope note and original review remain historical records; the successful evidence below supersedes that execution status.

## Verification evidence

`VERIFICATION.json` records the full bounded evidence; `AXIOMS.txt` preserves the final importing output. The raw receipts inspected here are:

| Run | Raw receipt SHA256 | Result |
|---|---|---|
| Final compile-0002 | `8c3170dc59eb3e6bbc3a82e5562d7a77b546b48dc6c7f31fd950e0b8156adec2` | Success, exit 0, empty stdout/stderr; no warnings |
| Importing axioms-0001 | `9494715464f8126f49cb2249373e8afe1eee67c1ae03064efed4ad272bcb7b10` | Success, exit 0, four requested theorem closures, empty stderr |

All four closures contain only `propext`, `Classical.choice` and `Quot.sound`. Importing stdout SHA256 is `5104647528d71d5daa3ca78b0163c677c3d6b43514eaec17133244fe63529bda`. Current source, Check and both imported artifacts match the recorded inputs: `.olean` SHA256 `8a91427ad24ff7df34744a5a76d49e45ab2719616acec407716d3e94b0798d7c`; `.olean.private` SHA256 `6c3581a4f971134e96ef292fe2505028e14028e37ac82139daf20ceafb52c4b7`.

The final compile used 1.422303 CPU seconds, 1.62530275 wall seconds and 1,024,065,536 bytes sampled group peak RSS. The importing check used 1.351266 CPU seconds, 3.540018708 wall seconds and 996,360,192 bytes sampled group peak RSS. Both receipts report unchanged input hashes, complete cleanup and no signals. Both used the existing 60-second per-process CPU, 75-second wall and 1.5-GiB sampled group-RSS limits. Darwin hard address-space enforcement was unavailable and is not claimed; sampled RSS has no guaranteed overshoot bound between samples.

There are four new checked theorems, no earlier OAI imports and no new axioms, `sorry`, unsafe code or computational oracle. This is independent statement/source/evidence review of one Lean toolchain's runs. It is not a Comparator result or a second independent kernel verification.
