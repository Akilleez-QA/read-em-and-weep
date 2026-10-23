Publication copy of the completed review; original-byte SHA256: `86a6aebc34fae4e84a910124f6c5b1a1c6c9628e71c8a63d462662b8ac412aed`. Paths are artifact-relative. Historical status refers to the review stage described below.

# SC-00 independent static audit and initializer review

Verdict: PASS for the static extraction and for proceeding to a separately bounded universal namespace smoke. Symbolic behavior, initialized sparse-attribute equivalence, full import integration, and all campaign shards remain UNVERIFIED. No candidate payload Python module, historical job, actual instance, source map, or symbolic initializer was executed in this review.

Base payload is the PR810 checkout at `ad780e4a14cf7ac9c9f33140c05803b4c156fde8`, in `research/hm/q-middle-candidate-interface`. Read README-HANDOFF, STATIC-DEPENDENCIES, all three nested prefix sources, the full Clifford and complete-symbol helpers, SourceMap initialization, the sparse orthogonal/q-middle adapters, the frozen verifier tripwire, and the cache schema. The parent previously verified all 80 payload digests; the independent static test replay here also verified all 80 against the new initializer pins and the handoff manifest.

## Final reviewed bytes

In `research/hm/q-middle-explicit-init/`:

- `initializer.py`: `14d57d45128498daee5c6adc9eeda343c2d909ac41713fb5ed09acde3341085a`.
- `test_initializer.py`: `bc15b2dba963eaf442a5a3a23d06e9f00535e5f587808dba5fb36c95e7dcdb4a`.
- `README.md`: `1b0962329c493d38c5cf23e2d8390f7df5893f708ec7086e7f18409177423435`.
- `receipt.json`: `235fdaa6f2501e3a08ca81967e811b73fcf829e472ef93a41695d1abf2cd8eae`.

Ran `python3 -B research/hm/q-middle-explicit-init/test_initializer.py` from the adapter checkout: six tests passed in 0.158 seconds, exit zero. These are static/import-guard/provenance tests. They do not import SymPy or frozen payload modules and do not certify runtime equivalence. The receipt correctly records the earlier smoke failure at RLIMIT_AS setup before symbolic import; this review does not promote it to execution PASS.

## Frozen initialization boundary and hazards

The three source-text cut sentinels occur exactly once and their prefixes parse as Python:

- derive_c_only140_unfiltered_principal_quotient.py: line 28, before `rq_symbols,rh_symbols,Theta=ns['build_symbols']`.
- verify_w_action_mixed_interface_one_ninth.py: line 41 assignment, split begins on preceding newline.
- verify_full_six_space_vertex_correction.py: line 82, before `R6=s.Matrix`.

The historical constructor nevertheless executes the full Clifford helper, including its universal assertions, and the full complete-W helper into a separate namespace. That second helper performs a five-coefficient symbolic quartic-recovery solve before returning its definitions. It does not call build_symbols at this boundary. Later historical top-level code constructs operator families, runs solves, and writes pickles; it is outside the safe cut and must not be imported or run as an entrypoint.

The candidate conservatively copies all mathematical prefix statements and helper definitions into explicit functions. Its own module import is inert apart from ordinary pathlib/hashlib/json work. It has no exec/eval/compile, no historical imports, no family-builder invocation, and no source feasibility solve. README explicitly discloses the retained fixed five-entry `s.solve`; saying that this candidate performs no symbolic solve at all would be false. It also correctly distinguishes frozen global name lookup from new lexical closures. The reviewed assignments preserve final bindings used by A/B, Clifford, Cartan, W-action, and complete-symbol functions; returned-namespace mutation is intentionally unsupported.

The implementation is not the smallest possible cut. A later independent simplification could retain only symbols/exterior helpers; Clifford/Cartan/spin tensors; q=(xy+z²)/theta and its polar r; H3, rh and abase; Pstd/B6/fmat/finv with FA=-9 FB FC/FD; and the sparse constructor's literal outputs. The complete-W helper is used by this initialization only for J3 in the pairing check, while DP, NP, H0 and many retained helpers are unused by the sparse constructor. Keeping these for exact extraction is acceptable at this stage and avoids an unreviewed simplification. Any pruning needs a distinct comparison.

## Exact initialization and API contract

The copied sparse constructor is AST-identical after the documented `self` to `instance` and sparse API renames, plus the instance tripwire. Required API names are:

`NAMES`, `col`, `columns`, `eye`, `getY`, `lapD`, `matadd`, `matfun`, `matpoly`, `projectD`, `putp`, `scale`, `sparse_laurent`, `vadd`, `var`, `vcontract`.

The receipt lists these 16 names. The explicit constructor also uses SymPy separately. Future integration must authenticate the API implementations and their dependency closure; providing an object with matching attribute names is insufficient.

Preserve these equivalence invariants:

1. Internal variable order `(x,y,z,u,w,ha,hb,hc,hd,hf,h,k,l,FB,FC,FD,theta,S,T)` and public first 17 variables. Only FB/FC/FD/theta are denominator units in this sparse ring; coordinate inverses are forbidden. SymPy symbol assumptions and the distinction between internal `S,T` and complete-helper `bs,bt` must survive the reference rename.
2. Pstd's binomial cubic normalization, FA=-9 FB FC/FD, B6 and its pairing diag(-J3/2,-J/3), determinant-adjoint conventions, exterior signs and coordinate/form ordering. Do not replace the full six-space by its Cartan block.
3. All initialized sparse matrices, inverse matrices, As/Bs/Cs, Cp3/Cp4, pC, AAinv, ellmat, cv, YL, q, j, and all three projected affine targets. Compare exact sparse dictionaries and free symbolic function behavior, not only shapes or a few identities.
4. The q-middle constructor deliberately calls OrthogonalSourceMap.__init__ directly, bypassing QOrthogonalSourceMap.__init__. Preserve this choice: calling super through the raw8 constructor would build an unwanted family. Keep the downstream q-middle constructor statements, reference symbol renames, qm_E/qm_RB/qm_ZC/qm_ZQ/qm_RC_Q, and external-direction independence checks.
5. Keep the frozen verifier's class-level SourceMap.source_map tripwire and the new instance tripwire. Instance assignment alone does not prevent an explicit class-method call. No supported legacy middle map may receive new qB input.

The normal frozen sparse API imports Laurent/CachedLex/Fischer definition modules; their heavy jobs are guarded. The dense q-middle reference, however, reaches universal_source_balance_helpers, which still full-execs the Clifford helper and performs quartic recovery at import. This constructor extraction does not make that entire future import graph inert. A wrapper must separately review or replace that bounded initialization and accurately state its scope.

## Complete 26-sector contract

The exact canonical JSON schema hash (sort_keys=True, separators=(',',':')) is `022cd694ede026a7e93b1d3b797c8289d34d34626bc9db065da382373be3bfe6`. The original schema file SHA256 is `eac1a7ab8321e228f42573eee0b1d176803e65630775116ffc414e0f00f764b2`. Only error_schemas is an adapter input; inherited row-count/column/rank metadata is not a newly verified result.

Ten structural-zero sectors must remain present: principal_spin (2x2), cartan_error (2x2), low_polar (4x3), Ylow (6x3), and spinor_form K0_Berror_Uj/Uerror_Uj/Berror_Uj for j=0,1.

The other sixteen are LC (4x3), and for each j=0,1,2: Lharm_Cj (6x1), high_spin_Cj (2x1), sigma_harmonic_Cj (1x1), high_full_remainder_Cj (spinor_form), low_literal_Cj (spinor_form). Empty entries do not authorize dropping a label, kind, or shape. No isolated C5 filter or harmonic-only external restriction may be introduced.

Subsequent SC-03 comparison must retain all five U0/U1/C0/C1/C2 columns, both source endpoints, qN and its companion, every physical-scale monomial, full high/low remainders, exterior defects, all ten skew-pair d-squared defects, and all six external quadratic monomials including trace. Preserve the qB arbitrary symmetric-positive-linear 12x12 input domain (234 coefficients) and positive-coordinate derivative product rules.

## Next safe gate

A namespace-only worker may construct build_namespace and check the disclosed fixed identities under parent-enforced CPU/wall/RSS limits, recording the lack of RLIMIT_AS support honestly. It must not use the existing `--smoke` path unchanged on this host, because that path rejects the address-space limit before import. This review performed no alternate runtime attempt.

After namespace smoke, a distinct bounded integration comparison must check initialized attributes and function semantics against the independently authenticated frozen reference, exact schema equality, API closure, q-middle constructor preservation, and both legacy tripwires. No shard scheduling follows from static tests or namespace-only identities alone. Retain inherited empty and partial logs byte-for-byte, and place every new receipt in a separate versioned run location.
