# SC-R independent review — pending staging handoff

**Disposition: NOT ACCEPTED / final producer review not performed.** At
2026-10-16T08:10:58Z, `producer-ready.json` was absent after ten bounded
30-second marker waits (300 seconds total, each reported 30.00 or 30.01 s).
The producer was still adding/changing files. The marker is only a staging
handoff; its eventual presence will not establish correctness or admission.
No producer defect is asserted from its absence.

Only `test_independent.py` and this report were written by SC-R. No GitHub
writes, commits, pushes, detector selection, seed-4 scans, physical source
evaluation, witness computation, polynomial expansion of physical inputs, or
large oracle runs were performed. Null's selector/transport/carrier-defect
work was not duplicated.

## Independent source expectations established before handoff

Sources were read using `git show <commit>:<path>`, rather than trusting the
assignment's paraphrase. Exact SHA-256 authentication used Python
`hashlib.sha256(subprocess.check_output(['git','show',pin+':'+path]))`.
The test file saves all nine pins and their authentication test.

Pin A = `10810ee877fdaf291399198ad60d7dd0c316a42d`.
Pin B = `08b73637d4136f91606aad332c46cafd064417f8`.

| Pin | Source path | SHA-256 |
|---|---|---|
| A | `research/hm/null-proof-foundations/direct-scalar-free-pairing-reduction.md` | `246b7265f4f8936bf5cc2bfd9f0f7505f119d4b3515acdd82822f7d45c0c4d00` |
| A | `research/hm/null-proof-foundations/hm-regular-cover-transport.md` | `98a10d3da934ef5b6dfe1e2cf6af4ac46fcf6347e0e6081a8c0cbd58b2f7f02d` |
| A | `research/hm/null-proof-foundations/transposed-scalar-demand-grammar.md` | `bcc18aff1cd807fae12093d9d2cc6271fb505b9151e28ab524a903114010d87b` |
| A | `research/hm/null-source-integration/combined-pole/PROOF.md` | `03673d6f120cb0b89d6d3887b7ab0bfee6aa33acf2abcc0ddbb116071b159c25` |
| A | `research/hm/null-source-integration/order-comparison/source-order-curvature-comparison.md` | `c8dc3acbda9bcfc80317116ff2ff400e275ecf82a18f5321479c936d3c109451` |
| B | `research/hm/current-scalar-geometric-dependencies/data/source-formulas.js` | `c4f65ff831092d0e56b3e33a0357f44182169fda45943ea780c8c551b4023f94` |
| B | `research/hm/current-scalar-geometric-dependencies/frames-and-poles.md` | `876cad001a8f96bb207ca246873e3efe67afd9a394cc4d2a0796992596b84916` |
| B | `research/hm/current-scalar-residual-attribution/closure-and-characters.md` | `434aa106d0780f6eeef956335cc207a8b436d35db52f515f52bb5d49204292a2` |
| B | `research/hm/current-scalar-proof/map-and-comparison.md` | `777a11e0e82ca5de557d1b756e9ce7535836a0ff4cc34ee6e50712e23f788e72` |

The reduction, sections 2–6, requires all five terms
`M0^0 + Fq kp,ik + Fp kq,ik + Ep(Tq Fq) + Eq(Tp Fp)`.
Here `M0` uses `u0=gk` in **globalCross**, including
`-bp kq,ik - bq kp,ik - bp bq I` after left normalization. A baseline
before gerbe subtraction instead requires `(F-b)k=-ck`; mixing these
conventions is incorrect. The terms individually need not be closed.

The pinned JavaScript and closure note section 2 fix `mu1=1/2` and mixed
`mu2=1/4`, with signs `+,-,-,+`, and products with the jk endpoint on the
left. Form the nonlinear row expression before transposition. The source
normalization is left multiplication by `gik^-1`; transpose reverses products.

Closure note section 3 fixes `J0=j(R^t)` and
`J1=H_0 delta J0`, `J2=-H_-1 delta J1`, `J3=H_-2 delta J2`,
where `H_r(F)=hF+(-1)^r(IP)Fh`. The scalar maps act on `J2`; their closure
uses `delta J2=d_End J3`. The physical-frame conversion is `tau^(r-2)`,
hence `tau^-4` for the scalar. Fixing endpoint frame values does not set
frame derivatives to zero. Physical Q factors must follow the actual source
construction rather than a derivative of an already frozen constant matrix.

The twenty-map note was read for the specified I20 and J2 target; SC-R did
not reprove Null's source-independent transport contract. The selected 32
requests mean 20 `Q^2`, ten `v_k Q`, and two `v_k v_l` weighted sums, not 32
isolated positions. Independent labelled-subset counting checks the full
weights, with `Q=x1*x2+x3*x4`, elementary `v_k`, exponent `e=-m-1`, and
index `sum_i(2-m_i)*3^(3-i)`.

The combined-pole proof equations (1)–(5) are a **conditional algebraic
implication** from the actual whole-source clearing equality and polynomial
quotients. They explicitly do not supply the actual-source equality witness
or executable coefficient realization. Full owner occurrences cannot be
merged because their equations have the same value. The order-comparison
note sections 2–6 forbids automatic equality of rebuilt cross-order source
formulas. A symbolic grammar is not an actual coefficient realization.

## Saved independent controls and actual execution

`test_independent.py` SHA-256:
`298852a6f00ff22b36bab084f1402418559f3d86593512118f65ca5b795af9e2`.
It imports no producer implementation. Its eight saved tests cover:

1. Exact authentication of the nine cited source files.
2. The graded End homotopy identity on every matrix unit of an artificial
   five-dimensional split complex, including a wrong-sign negative control.
3. A nonzero frame derivative with identity endpoint frame value.
4. A six-vertex Cech lift with varying local contractions and nonzero J1/J2,
   checking all three recurrence signs. The tiny complex has no degree -3
   entries, so this does not test a nonzero J3 coefficient.
5. A complete source-elimination identity using artificial polynomial SL2
   transitions, both scalar cochains, both Fk corrections, all four Moyal
   terms, all three gerbe terms, and directional derivatives. The baseline
   changes if gerbe subtraction is removed; matrix multiplication does not
   commute, and transpose reverses products.
6. Independent expansion of the bivector square's two mixed orders.
7. Forward Laurent differentiation versus adjoint convolution, including
   the zero coefficient of a naked derivative at exponent -1.
8. Labelled-subset reconstruction of all 32 request weights and I20 labels.

Actual commands/results:

- `python -B -c 'import sympy; print(sympy.__version__)'` failed with
  `ModuleNotFoundError`; the saved controls instead use only the standard
  library and exact `Fraction` arithmetic.
- `python -B research/codex-swarm/scalar-compiler/test_independent.py` ran
  an earlier, four-test **preliminary expectation-building** revision:
  `Ran 4 tests in 0.116s`, `OK`. This revision comprised source elimination,
  Moyal mixed coefficient, derivative convolution, and request weights.
- The final eight-test revision has **not been run**. No final producer
  tests or final acceptance tests were run before the required marker.
- Ten separate marker loops each used `time.monotonic()` with a 30-second
  bound and one-second sleeps, checking only marker existence. All returned
  `{'marker': False, 'wait_seconds': 30.0}` (one `30.01`).
- `sha256sum` recorded the test, request input, and staging inventory below.
  Request input SHA-256 was
  `f256746fbfd0897fd4a5241e13715198004d277fec700b7ba5c4b3ace9bfe5e0`.

## Staging inventory, not reviewed producer hashes

No producer file was substantively reviewed because the handoff never
arrived. These are **observed byte hashes only**, and may already be stale:

| File | SHA-256 |
|---|---|
| `compiler.py` | `51d60f35adbf34ecb3ca6af327c86bbd0db8eed4f010d2fcc9adbf06c6958091` |
| `compiled-template.json` | `a703550f40d84956e180e04dd9a343bbbf7b5a956f2fdfb321410f7fe621fd3b` |
| `run_formal.py` | `f1a2aed056f40894d649801a011f8ae073772b39c878dd17af78f89a00ef1f42` |
| `formal-run-receipt.json` | `9402e504a9d5dd69a7c1ac73789c8f1e5f5ec12e445ea5b3ddae99499aed489d` |
| `test_compiler.py` | `267af3587ae1a02056aec354c535a9c7e0a3f1193680930810784591438cbc3f` |

## Next owner and unresolved checks

Root/SC producer: finish the package and publish `producer-ready.json`.
Root/SC-R follow-up: authenticate the completed snapshot, run the final
eight independent controls, inspect the producer's complete symbolic DAG,
then add API-level adversarial tests in the reserved test file. In particular
test exact source-leaf/pair/mask/frame bindings; owner occurrence and domain
binding; rejection of booleans wherever integers are required; rejection of
forged closure/admission flags; all five Rsharp terms; all twenty rows acting
on J2 with J3 closure; and preservation of all 32 request weights. None of
those producer-facing checks is discharged by this pending report.

Any requested actual-source equality witness, executable coefficient
realization, or physical evaluation belongs to its separately authorized
owner. This review grants no arithmetic release and no obstruction value.
