# Source-bound null-support certificates

This focused, reproducible research release contains finite-label support proofs and an independent abstract second-jet criterion. It does **not** establish global O2, a complete obstruction value, global factorization, or permission to evaluate the physical source.

## Results and exact scope

The joint theorem in `combined-seed4-e12-coverage-audit.md` certifies **the complete seed-4 E12 directional component is zero**, over all 884736 carrier/legal assignments and six sorted-standard permutations, under the declared **fresh-consistent source ordering**. The joint test binds all 2048 support-certified tuples and 16384 A/B roots to the actual public lowerings. This closes only that component: seed-4 M0/E34, other source components, and the other 77 seeds remain outside this theorem. No historical-order value comparison or global O2 conclusion follows.


- `permuted-standard-support-audit.md`: seed 4, terminal row 2, pre-sort staircase (3,11,15), source-sorted tags (11,3,15). All **704** active tuples in carrier sectors (1,1,4) and (1,2,4) have eight separated A/B multipliers, **5632** separators total. The source-sorting sign is retained. This is not a coordinate-symmetry assumption.
- `legal-mask-sector-support.md` and `legal-mask-gap-patterns.json`: the fixed (1,2,4) carrier sector with tags (3,11,15), all **512** active masks and the exact closed gap formulas. Inactive labels remain accounted for in the full domain.
- `selected-full-owner-kernel-lowering.md`: the actual full-owner, selector-preserving factored lowering used by these certificates. Bounded multinomial sums remain symbolic; support bounds are cancellation-blind envelopes. Separation proves zero; overlap would be unresolved, never nonzero.
- `primary-carrier-support-audit.md`: the prior primary-carrier partition and its additional finite-label scans.
- `exceptional-carrier-support-audit.md` and `exceptional-carrier-independent-audit.md`: exceptional-first contraction-zero evidence, including the independent selector-column proof across all six standard permutations. The candidate partition JSON separately records the (3,11,15) slice. The full exceptional assignment count is 622592; its proof is independent of the primary support scans.
- `source-second-jet-degeneracy-certificate.md`: the abstract criterion Omega=0 iff J-transpose S H is symmetric, covariant second-jet formulas, sufficient conditions and counterexamples. Its **nine tests** use artificial matrices and no HM source data. No distinct-carrier global source identity is claimed.

## Reproduce

Python 3.12 was used. The finite-label support code uses only the standard library. The independent abstract second-jet tests additionally require SymPy (`requirements.txt`).

Run from this directory:

```sh
python prepare_certificates.py
python -m unittest test_source_second_jet_degeneracy test_selected_kernel_denominator_lowering test_selected_support_separation_independent test_legal_mask_sector test_permuted_standard_sector test_primary_carrier_sector test_exceptional_carrier_sector test_exceptional_carrier_independent test_combined_seed4_e12_closure -v
```

The three large generated certificate JSON files are distributed as deterministic gzip archives. `prepare_certificates.py` verifies both compressed and decompressed SHA256 hashes and restores the exact tested bytes using only the standard library. It does not run any mathematical checker. Generated JSON paths are explicitly gitignored.

For a fresh computational regeneration, run `python regenerate_public_certificates.py` after preparation. The regeneration script rebuilds the selected lowering and all support scans, and checks expected public hashes. These are metadata/finite-label computations. They do not expand or evaluate physical source polynomials, enumerate the large composition-summand domains, or release arithmetic execution. `verification-results.txt` records the release replay.

`seed-fingerprint.json` preserves the separately published 78-seed catalog unchanged. Its `origin_kernel_sha256` identifies its historical audited input, not this release's sanitized lowering JSON.

## Public source provenance and release identity

The historical public source remains pinned to commit [`08b73637d4136f91606aad332c46cafd064417f8`](https://github.com/Akilleez-QA/read-em-and-weep/tree/08b73637d4136f91606aad332c46cafd064417f8/research/hm/current-scalar-geometric-dependencies). Original public [source identity](https://github.com/Akilleez-QA/read-em-and-weep/blob/08b73637d4136f91606aad332c46cafd064417f8/research/hm/current-scalar-geometric-dependencies/source-identity.md) and [frames and poles](https://github.com/Akilleez-QA/read-em-and-weep/blob/08b73637d4136f91606aad332c46cafd064417f8/research/hm/current-scalar-geometric-dependencies/frames-and-poles.md) are authenticated by Git blob identifiers in `outer_partition_source_binding.py`.

The model and existing homogeneous-identity receipt are included unchanged. The historical checker is included only as inert `pinned-verify-homogeneous-identities.py.txt` provenance bytes; no release command executes it. Its original byte hash and Git blob identity remain unchanged.

This is a **new public serialization**, not a claim that redacted files have their historical hashes. Private resource configuration and machine-local references were removed from public copies. Hash-bound local proof references and selected-lowering expectations were updated; scans were regenerated. Mathematical formulas, DAG arithmetic, selectors, owner order, degree rules and separation inequalities were preserved. `release-manifest.json` identifies public files and unchanged public witnesses; `mathematical-equivalence.json` records comparison of regenerated mathematical content against the source artifacts. Original source artifacts were not modified.

Execution/factorization acceptance remains false throughout. Resource admission is outside this release.
