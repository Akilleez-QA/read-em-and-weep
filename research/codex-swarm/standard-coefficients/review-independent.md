STD-R independent review of STD01 — 2026-10-16

NARROW ACCEPTANCE: the reviewed package implements an executable, bounded synthetic coefficient program for R(K_cov Pi + A h S Pi) with its harmonic remainder retained. No blocking defect was found in that scope. This is not acceptance of an actual HM primitive, an obstruction value, physical execution, or an external capability. Only test_independent.py and this review are reviewer-owned changes.

Read: standard-coefficients/producer-ready.json, standard.py, proof.md, test_standard.py, README.md, contract.json, source-pins.json, run_controls.py; and the insertion handoff, interfaces.py, polynomial_coefficients.py, inserted_program.py and program-contract.json. The immutable proof references in source-pins.json were treated as external dependencies, not re-proved or certified here. The shared interface digest agrees with STD01's interface pin.

The concrete AW implementation uses high-bit standard coordinates and canonical cut vertices, with orientation supplied after normalization. Reversing a simplex changes the sign of its canonical AW cells; it does not change the cut convention. Staircases carry permutation signs. The producer checks S A = 1 on 81 tensor cells; independently fixed examples check coordinates and signs. Independent chain-boundary calculations check the cone recurrence in degrees 3, 4 and 5, including nonzero minima and non-monotone bit rectangles. Every tested cone vertex remains inside its source rectangle. These finite controls support, rather than replace, the inductive proof of boundary k + k boundary = 1-G.

The tensor h was checked against an independently written forward tensor differential and independently constructed IP, on regular basis cells at nine selected exponent vectors for each of the two pair twists and the trivial twist. The vectors include -3, -2, -1, 0 and positive thresholds. The checks distinguish the B constant projection for O(0) from the C exponent -1 projection for O(-2), and include prefix and Koszul signs. This exercises delta h + h delta = 1-IP without constructing the expected answer from h_requests.

Pi was independently compared with sparse multiplication of a two-term rational numerator and three two-term Laurent quotient factors. Coincident exponent sums, negative shifts, polynomial degree clipping, odd auxiliary-first source ordering, reversed target orientation, cache reuse, seed and slot occurrence preservation are covered. This artificial algebra verifies the supplied-oracle convolution formula; it does not establish rho/C = Qhat, source numerator identity, completeness of a physical fiber, or a partition identity for actual data. Repeated physical source labels vanish only in the alternating F pullback; the producer control for this distinction was rerun.

Full R was tested with identical physical labels but distinct complete output occurrences and standard tags: the edge can be nonzero. Reversal negates it, equal standard tags vanish, and merging occurrence IDs is refused. Binding to the insertion adapter preserves the full owners. A separate artificial integration control verifies that WholeNumerator supplies C_a C_b Z once around the standard B endpoint; the endpoint itself supplies no such padding. The Pi support enclosure control requests no source coefficients and allows overestimation. No physical owner enumeration is implied.

Complementary scalar derivatives use (e_d+1) times the shifted coefficient. Independent tests check a nonzero positive derivative, a negative-to-negative exponent shift reaching h before its predicates, the zero-factor short circuit, and refusal of a derivative along the scalar pair. The F34 tensor structure is accepted only structurally. This review does not infer a source-first alternating F12/F34 equality or permit sorting a raw inverse-image triple before nonlinear evaluation.

The accepted identity is delta B + B delta = 1-A I p S on the standard complex, and its R/Pi restriction when the oracle premises hold. The API spells the projection P in its metadata. An independent nonclosed fixture has nonzero B delta and checks the complete identity on selected triangles. Independent closed harmonic generators for both pair twists are constructed directly from cut bits, have p S F = 1, and satisfy delta B = 0 with nonzero F. Therefore arbitrary closed F need not satisfy delta B = F. For the actual source, closure alone is insufficient: harmonic vanishing or a separate authenticated first-order primitive witness remains OPEN. No actual source primitive is accepted.

Whole-standard extension is an input obligation. Direct complete synthetic Laurent fixtures are checked at finite-only and infinity-only target coordinates. Oracle witnesses refuse common-local-only scope, changed targets, reordered owners, changed seed ownership, missing coefficient identity/domain and a Boolean substitute. Malformed fiber occurrences, duplicate common labels and duplicate quotient exponents also refuse before source coefficient evaluation. Synthetic modes are rechecked after cache population. Physical evidence is refused. These are interface checks over trusted synthetic objects, not an authentication boundary against a malicious Python callback. A correctly shaped synthetic witness does not prove its claimed extension theorem or completeness of an omitted polynomial.

External capabilities still OPEN: actual cleared numerator/source identity and source closure; complete Qhat streams, complete finite owner fibers and the partition-quotient identity; actual owned C_a/C_b inputs and clearings; whole-coefficient extension to the entire standard target, bound to complete owned clearings and domain; actual harmonic-vanishing/first-order primitive witness; physical homogeneous-frame and derivative identification; the correctly ordered freshly evaluated complementary source; physical execution admission and budget. Synthetic mode labels, finite caps, dependency pins and test success issue none of these capabilities.

Validation from standard-coefficients (direct filenames avoid the shared sys.path test-module collision):

| Command | Result |
| --- | --- |
| python -B test_independent.py -v | 11/11 PASS |
| python -B -O test_independent.py -v | 11/11 PASS |
| python -B test_standard.py -v | 12/12 PASS |
| python -B -O test_standard.py -v | 12/12 PASS |

All independent checks use unittest assertions that remain active under -O. The first independent run exposed an incorrect reviewer expectation about reversed AW cuts; only that expectation was corrected. A combined module-name unittest invocation resolved the insertion reviewer's identically named module after standard.py changed sys.path; those results are excluded from the STD-R counts above. Direct file executions explicitly reported STD-R's IndependentControls class. The producer run_controls.py parent was not run, since it rewrites producer receipt/log files.

No actual HM polynomials or actual owner fibers were evaluated; no physical coefficient scans, budget releases, commits or posts were performed. No producer files were edited.

Hash integrity: before reviewer writes, all 17 files named by the two producer manifests matched their declared SHA-256 hashes. Both handoffs were additionally hashed, for 19 captured files. All 19 hashes were rechecked after testing and before this review was written, with no changes; all 17 manifest entries still matched. This checks byte integrity of the reviewed handoffs, not their mathematical authority. The equal before/after hashes follow (paths relative to research/codex-swarm):

| Producer file | SHA-256 before = after |
| --- | --- |
| inserted-coefficients/README.md | `73a0e378388cae87f576b02a7ead5dbfb0e7d2c8fa4c1d118b45ec59baeeba43` |
| inserted-coefficients/inserted_program.py | `aac77cef25974ed0d3fcdfded48ee037ff86ec7e88215c841b6e59c5f32dd4bf` |
| inserted-coefficients/interfaces.py | `9ba74c9e328c38083c4f8d49a04818d8a67216aa0a0b477563523ed4728f72fa` |
| inserted-coefficients/polynomial_coefficients.py | `c826bc5379910222bb962288581a9e5fec64d3b956c03cefdfc4566567cf19ee` |
| inserted-coefficients/producer-ready.json | `dc594bb51adcf7dffe0ab51a4fd6d2d330af4e937afab39ab0c7d787a8f75e19` |
| inserted-coefficients/program-contract.json | `d245f0291f1e05d7354b8e9e26fc0469ce2a7aa6e85c0510285a66061daa8808` |
| inserted-coefficients/source_program.py | `1f6241ddc12c41ea2f8476cef53bc0b148562c2ade56c0c4f8aede68de8ced1c` |
| inserted-coefficients/test_inserted.py | `4207c21a53be11da2e0744838311d36ce2ec3b50f39c1ffe2002ed5cbe7c187a` |
| standard-coefficients/README.md | `cc2a5ba9b70049017374caabb10f3a0b16e55c8d6bbba66283b4dbbc2403f7d3` |
| standard-coefficients/contract.json | `0508543ef38646e18b956e115c39d2ae84489ceaf0bbd40122c084ca49e4f013` |
| standard-coefficients/controls-normal.log | `b022ebefa9e9ea5c5d49f4742925e6e6c4b77150507ac5571c63ca4a1ff94898` |
| standard-coefficients/controls-optimized.log | `d5005710a936d968c0bed6bc8825cffbc4a305382c694149d452ee4763bf7c92` |
| standard-coefficients/controls-receipt.json | `b97ee8914851124f624d188310f53182fe71a0ce772e902b366e93415a3d5008` |
| standard-coefficients/producer-ready.json | `087f208b95b3118255362cf1f28482bddff81d61daada2c1fa20095dc1f952c6` |
| standard-coefficients/proof.md | `6e12f4541e15fe7c1ee7d67669d76b950a246aceb8f6cd9e5a18e5eb8b226b89` |
| standard-coefficients/run_controls.py | `7e828c438c960607cfe15ba914828552630a4b8d1ff10690637411075bc0d9bd` |
| standard-coefficients/source-pins.json | `fc6b0d964dd6e6f0fe3bb7b794e5484ecf0c10c0efc417b250676d2976c9f08e` |
| standard-coefficients/standard.py | `bd9c9a77d2e366a92e265406727bd26ba05c4b15680df384d16f6b1c074ad2fd` |
| standard-coefficients/test_standard.py | `7c9ea5edc7b85a8377b377a1f580604ee01ad050a1d4721597575dd4f42b897e` |
