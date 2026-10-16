# SC-R2 final independent implementation review

Current disposition: the two findings below were subsequently repaired and all31 tests pass; see [root follow-up](review-fix-followup.md). This report preserves the pre-fix snapshot.

Disposition: **final implementation acceptance withheld: two reproducible API integer-validation defects require producer fixes.** The reviewed symbolic construction otherwise passes the independent checks described below. This review supplies no physical-source acceptance or arithmetic release.

Only `test_independent.py` and this report were written. No producer edits, commits, posts, artifact regeneration, waiting, physical evaluation, or large oracle were performed. Root owns publication and producer-fix routing.

## Findings for producer

1. **Boolean standard tags accepted**, `compiler.py:284–286`, `bind_outer_assignment`. With tags `[False,8,12,14,15]` and owners `[[0,j,1,0,int(t)] for j,t in enumerate(tags)]`, the API returns an assignment instead of rejecting it. Owner fields themselves have strict integer checks, but the separate standard tags do not; `False == 0` passes the binding. Require strict integer tags before equality/range checks. Saved regression: `test_boolean_standard_tag_must_be_rejected`.
2. **Boolean selector coordinates accepted**, `compiler.py:80–84`, `row_bottom_coefficients`. With a zero 15×5×5 coefficient array, term `{'block':[2,0],'entry':[False,0],'coefficient':1}` returns `{(False,0,0):1}` instead of rejecting it. Comparisons/indexing allow booleans to alias integer coordinates, undermining malformed-row diagnostics. Require strict integer entry coordinates in both supported blocks. Saved regression: `test_boolean_bottom_selector_must_be_rejected`.

Both failures reproduce normally and under `-O`. They do not demonstrate an incorrect value in the canonical emitted artifact or bypass of `validate_template`; they prevent acceptance of the requested strict API integer boundary. Producer must fix; reviewer did not patch producer code. A repaired implementation needs a new authenticated handoff and rerun.

## Authenticated snapshot and source comparison

Before editing, all twelve handoff file records matched both byte lengths and SHA-256, including the two reserved reviewer files. After testing, all ten unchanged producer records still matched. The reviewer outputs intentionally supersede their handoff hashes.

Read staging expectations and all eight existing independent controls first, then the current README, operator contract, complete compiler and producer tests. Authenticated the nine earlier source pins and the added transport proof at `43193bc8badf3f29a1363132135d956cc12d46ad`, blob `fc8befcc863efd073d4a66dc6eec12c722504447`, SHA-256 `e0fac7c2a2564dd1521a6055238e175fcf83e11e1b4bf9302eacad13ed040db3`. Read that proof directly with `git show` and compared sections 2–7 to actual code; read the pinned source JavaScript directly as well. This review is not just producer-regeneration agreement.

The actual artifact contains 4,270 nodes and twenty source triples. Every node was traversed for backward integer references, positive matrix dimensions, product compatibility, and applicable frame/leaf metadata. The API polynomial control independently evaluates all five source branches on artificial noncommuting SL2 polynomials. It checks `u0=gk`, seven kinetic terms, the three negative gerbe terms, left normalization, trace-free baseline, complementary Fk terms, and all four signed terms of each E correction. Reversing matrix products changes the artificial result; deleting gerbe subtraction changes the baseline. These assignments are deliberately artificial, including solver assignments; they assert no actual source identity.

The physical-jet nodes retain differentiated moving frames and sorted commuting directions. Q leaves retain their edge and coordinate bindings. Derivatives of T retain a whole combined-solver node, complementary direction, false clearing witness, both signed prisms and both standard branches. Inner14/legal1 and outer54/legal29 remain distinct. The outer standard5251 field is a target-unit allowance.

An independent free associative algebra expands the emitted J0–J3 circuits, treating each transposed complete residual as an atom. Every resulting word, rational coefficient, block and contraction owner matches independently written alternating-face and graded-homotopy recurrences. This tests the actual symbolic J3 stencil, including signs and deleted-prefix owners; it does not establish nonzero actual physical J3 or actual closure. The eight original math controls and producer abstract split-complex closure checks also pass.

All twenty emitted constant rows were decoded independently from the authenticated polynomial gamma model and compared with their actual entry circuits on J2 blocks `(2,0)` and `(3,1)`. Gamma's constant coefficients enter; no extra polynomial v factor or historical special-scalar minus is introduced. The minus in the family operator is already in J2. The thirty-row producer chain check reports 1,500 coefficient checks. This matches the pinned all-row operator `-lambda S Pi H_-1 delta H_0 delta j(Rsharp)`.

The actual compiled coefficient trees preserve every selected request: 32 weighted sums, 127 listed contributions, 121 distinct map/exponent demands, and 24 correctly signed staircases each. Original independent labelled-subset enumeration verifies the complete Q²/v_k Q/v_k v_l weights, residue exponents and terminal indices. No 78-selector substitution or carrier merger appears.

Adversarial artifact mutations reject missing actual source branches, missing actual gerbe terms, absent J3, reversed non-palindromic products, wrong rational signs, changed frame flags, lost Q/g owners, wrong partition charges, forged closure instantiation, and every false physical/admission flag. Assignment tests preserve full occurrences, reject merged occurrence IDs, and distinguish common-vertex repetition from repeated carriers.

## Executed final suite and immutable tested hashes

Command per mode: `python -B [-O] -m unittest discover -s research/codex-swarm/scalar-compiler -p 'test_*.py' -v`. Each subprocess had **512 MiB address-space, 59 s CPU and 60 s wall limits**; bytecode writing was disabled. Final normal run: **30 tests in 1.987 s, 28 passed, 2 failed**, wall 2.150528 s. Final optimized run: **30 tests in 1.967 s, 28 passed, 2 failed**, wall 2.134179 s. Each mode includes 12 producer tests, eight original independent math controls, and ten new independent API tests. Both child exit codes were 1. An earlier draft run had an additional reviewer mutation-test failure caused by reversing a palindromic product; choosing an actually changed ordered product corrected that test before these final runs.

| Tested file | SHA-256 |
|---|---|
| compiler.py | `42dc34d123c5aa69834f003034a66ca13b6a031b84504eefd12c20d30aa4b9f2` |
| test_compiler.py | `7281fc6127ed2fd8c2e571fea06d8dde91b4a817044f32d9c27b110274a8e8fc` |
| test_independent.py | `040b047195aa4ab34077ca011cebf352866943e92717749ae73621656602ce3f` |
| compiled-template.json | `30fa190054411ea8180015be2ad3dbba65bd209abef7ddd78973a6fae024c565` |
| producer-ready.json | `4d70f5df16569cb379ebfd99e89c339522bd9c10e475183c204a7258779de5b6` |

## Acceptance boundary

The supported scope is an executable **symbolic matrix/cochain operator and authenticated finite demand stencil**, subject to the two API repairs. Cover/solver/coefficient nodes remain declarative adapters rather than executable physical coefficient realizations. Authentication and abstract closure do not discharge the theorem's source/domain hypotheses.

All seven actual physical gates remain explicitly **false**: physical matrix-leaf lowering, actual F clearing witness, all-row transport-domain witness, outer-fiber coefficient realization, historical-order identification, physical evaluation, and execution release. Whole-source clearing equality, original physical frames/deck removal/tau^-4, target-intersection regular extension, partitions and coefficient convolution still require actual witnesses and realization. No physical polynomial expansion, source coefficient computation, occupied-support estimate, 96^5 fiber enumeration, or obstruction value was obtained. The obstruction remains undecided.
