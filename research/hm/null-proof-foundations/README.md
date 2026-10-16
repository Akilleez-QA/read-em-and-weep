# HM scalar and detector proof foundations

This is a focused reproducible companion to `../null-support-certificates/`.
It publishes proof notes and abstract regression sources behind the scalar
reduction, direct-dual and selector claims. It is not a physical-source
calculation, an arithmetic admission, a value of the actual second-order
obstruction, or a complete proof of its vanishing or nonvanishing.

## Replay

Use Python 3.12 with SymPy 1.14.0 (`requirements.txt`). From this directory run:

    python run_checks.py

The wrapper refuses disabled assertions, runs all 14 test scripts as separate
processes, regenerates both public metadata certificates byte-for-byte, and
checks SHA256SUMS. No network, physical-source module, or physical coefficient
input is needed. The largest serialized certificate is small enough for plain
JSON; no compressed-artifact preparation is required.

The recorded run passes 76 unittest cases, the direct-dual cup-sign controls,
the exact rational finite-domain and jet examples, 1,219,730 formal adjoint
checks, and 150,453 oriented-cover/coefficient-index checks. Test counts are
controls of the stated formulas and examples, not a coverage claim for the
actual geometric obstruction.

## Claims to files

| Claim and status | Proof notes | Executable controls |
| --- | --- | --- |
| Corrected trace-free scalar elimination; all baseline/gerbe, Fk and E(TF) terms retained. Symbolic proof; detector application requires authenticated domain. | `direct-scalar-free-pairing-reduction.md`, `scalar-reduction-root-check.md`, scalar adjoint/domain notes indexed below | `test_m0_baseline_formal.py`, `test_scalar_homotopy_adjoint.py`, `test_scalar_cover_adjoint.py` |
| Full homogeneous owned-denominator complex is finite and H1-exact under stated cover/acyclicity assumptions; bounded primitive proves boundary annihilation at formula level. | `owned-denominator-finite-domain-certificate.md`, `direct-dual-scalar-fill-contract.md` | `test_owned_denominator_complex.py`, `test_direct_dual_cup_signs.py` |
| Finite jet dual construction is valid if chain compatibility, quotient surjectivity and actual detector factorization are supplied. Conditional for the actual detector. | `jet-quotient-direct-dual-certificate.md`, `jet-dual-compression-independent-audit.md` | `test_jet_quotient_dual_certificate.py`, `test_jet_dual_independent.py` |
| Exactly 4038 formal paths reduce to 78 owner-aware survivors; no cross-owner identities or unproved tail mergers. | `source-independent-selector-pruning.md`, `root-selector-pruning-audit.md` | `prune_refined_selector_paths.py`, `test_refined_selector_pruning.py`, `test_refined_selector_pruning_independent.py`, `refined-selector-pruning.json` |
| Metadata generator fixes all 78 seeds and refuses mutation/readiness shortcuts. | Metadata/domain discussion in the proof index | `compile_refined_detector_metadata.py`, `test_refined_detector_metadata.py`, `test_refined_detector_metadata_independent.py`, `refined-detector-metadata.json` |
| Quartic current remainder survives formal tests; second-jet/commutativity shortcuts are insufficient. Abstract identities and counterexamples, not an actual-source nonzero conclusion. | `rsharp-quartic-current-remainder.md`, `m0-second-jet-survivor.md`, `second-jet-no-go-independent-audit.md` | `test_rsharp_quartic_remainder.py`, `test_source_second_jet_degeneracy.py` |
| Seven inference guards prevent invalid implications from a baseline, local value, support or specialization to the complete obstruction. | `obstruction-inference-fmea.md` | `test_obstruction_inference_guards.py` |

See `proof-notes-index.md` for the complete selected note inventory and
chronological qualifications. The scalar-elimination proof itself is written
algebra; the listed baseline and adjoint controls do not constitute a full
machine formalization of that proof.

## Dependency and serialization scope

The two metadata modules are identical copies of the sanitized companion
release's modules so this directory is independently runnable. Their
mathematical seed, map, sign and owner data are unchanged. The public
serialization omits private operational configuration and regenerates the
metadata SHA256 and the pruning certificate's base-certificate binding.
`regeneration-results.json` records the resulting public hashes and comparison
with the original mathematical content. Do not use an original private
serialization's hash to validate these public bytes.

No historical experimental runners, physical source polynomial files or
private operating configuration are required. Original source artifacts and
published witnesses were left unchanged. A path-portability change in the
independent jet test resolves its sibling control by `__file__` rather than
assuming a local directory name. Proof notes may cite pinned public source
formulas for their hypotheses; those sources are not evaluated by this suite.

## Included geometric prerequisite addendum

The full earlier notes `hm-transition-only-first-lift-alternative.md`,
`hm-full-sign-legal-line-bound.md`, and `hm-regular-cover-transport.md` are now
included. They supply the scalar-solver/gauge formulas, original-source legal
pole proof, and explicit signed regular-cover comparison cited by the later
foundations. Their pinned upstream references remain prerequisites for applying
the formulas to the geometric source. This adds written proofs, not a new
physical computation or a claim that every historical audit is bundled. See
`proof-notes-index.md` for the original-source versus refined-source distinction.

## Open obligations

- Actual detector/source binding and all required frame, owner and partition
  identities must remain authenticated when applying the formulas.
- The direct-dual existence theorem does not supply physical coefficient rows,
  an instantiated pivot/factored inverse, or a physical exact-fill residual.
- The jet quotient needs actual detector factorization and the stated exact
  chain/quotient conditions; examples prove neither for the full detector.
- Formal selector pruning leaves source arithmetic, coefficient extraction and
  complete implementation costs unresolved.
- Abstract quartic/second-jet survivors do not prove their actual geometric
  specialization is nonzero. A local nonzero value need not survive in cohomology.
- No complete corrected obstruction evaluation or feasible arithmetic schedule
  is supplied here; execution gates remain closed.
