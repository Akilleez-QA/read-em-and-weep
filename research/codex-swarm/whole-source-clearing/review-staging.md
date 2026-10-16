# CLR-R independent review — pending producer handoff

**Disposition: NOT ACCEPTED / final review not performed.** On 2026-10-16,
`producer-ready.json` did not appear during ten bounded waits, each at most
30 seconds and cumulatively less than 300 seconds. The marker would establish
staging readiness only, not correctness or admission. No final producer tests
or independent tests were run before this handoff. Root owns rescheduling the
final review after the producer finishes. Do not treat the saved tests as a
passing certificate.

Only `test_independent.py` and this report were written by CLR-R. No producer
file, GitHub state, commit, push, detector selection, or seed-4 scan was changed.

## Independent expectations from pinned sources

All source reads below used `git show
10810ee877fdaf291399198ad60d7dd0c316a42d:<path>`, before preparing the controls.
The transition-only note defines `F=b-tr(g_ca*mu(g_bc,g_ab))/2`, with
`mu=(derivative-product difference)/2`. Thus its whole normalized finite
expression has coefficient **-1/4**, and includes the actual gerbe
`(15/4)q_ab,0*q_bc,1`.

The executable excerpt specifies `K_ab=(P_a I_b)^t` and physical
`g_ab=D_b K_ab D_a^-1`, where `D=diag(nu,nu^-1)`. Differentiating before
cancelling endpoint frames gives
`T_ab,i=partial_i K_ab+Gamma_b,i K_ab-K_ab Gamma_a,i` with
`Gamma=diag(m*rf,-m*rf)` and
`rf=(x_i^2+1)/(2*x_i*(x_i^2-1))`.
The pinned contraction identities, including `P I=1`, `delta I=0`,
`P gamma=0`, and `E=1-gamma H0-H1 delta`, are the existing algebraic basis
for replacing the inverse by `K_ca`. CLR-R did not rerun that physical
identity checker; its receipt is an imported premise, not a new calculation.

The literal denominator metadata gives primary `dp=di=-H` in `v0=1` and
auxiliary `dp=di=-v1*a`, `a=v1*v3*v4`. Hence every stored I/P entry has
polynomial clearing `H²*(entry)=-H*(stored numerator)` on primary carriers,
and `a²*(entry)=-v3*v4*(stored numerator)` on the auxiliary carrier. This
finite identity alone supplies no homogeneous or infinity assertion.

An independent owner ledger is `K_ca:(2,0,2)`,
`T_bc:(0,3,3)`, `T_ab:(3,3,0)`, giving **(5,6,5)**.
Each derivative direction is used once in the product. Binary masks allow
`(m_b-m_a)/x = m_b(1-m_a)(x²-1)/ell_b
-m_a(1-m_b)(x²-1)/ell_a`, with mask-0 ell=1 and mask-1
ell=`x*(x²-1)`. These are owner-local factors; coincident equations at
different occurrences do not authorize borrowing. At most one legal factor
per pair direction and occurrence is needed in this displayed formula.

Source-first repeated **source** labels `(carrier,mask)` make an adjacent
transition identity and the adjacent gerbe q zero. General common cochains
only vanish on repeated common labels including standard tags. A final
source adapter must implement this distinction, rather than use a generic
common-cochain predicate for F or merely declare it in text.

The combined-pole proof is explicitly conditional on homogeneous source
clearing. Its required complete numerator is
`N=C_a*C_b*Z*B + Z*sum(Q_u*P_uab)
-C_a*Z*sum(Q_u*Q_v*P_uvb)`, followed by differentiation of the **combined**
numerator. `B=R(K_cov Pi+A h S Pi)F` must remain complete. A finite whole-F
polynomial identity does not establish homogeneous coordinate bounds
217/210, infinity-frame poles, or the actual executable B coefficient
program. The order-comparison pin forbids automatic cross-order equality.
Null retains ownership of selector commutation, the 20-row transport
contract, and the carrier-block defect; none was duplicated here.

## Staged snapshot and remaining review

The producer file initially read was `clearing.py`. A later hash inventory
recorded SHA256 `bda3c36e14e729d16c777923e6b38d6ca61f3e29e620e670dafd8f9f1d1e86e6`.
Concurrent changes mean that hash does not certify the earlier textual
inspection. At the final directory check, `test_clearing.py` had also arrived,
SHA256 `ca54ca6cb20a1b9e87df9e33bc8d8af2cc3111a850b1db82ac1b4ad92dcd001e`;
it was neither reviewed nor run. The marker remained absent.
This is an **unstaged preliminary snapshot**, not a finalized reviewed
package. The initially displayed DAG includes the gerbe and both derivative products;
its catalog contains the six expected denominator cases. Its flags retain
the homogeneous and coefficient gaps. No conclusive mathematical defect is
asserted from this inspection. Absence of a handoff and completed proof/test
artifacts prevents acceptance; source binding, all entries, final owner
maps, repeat predicates, complete-B treatment, and generated receipts must
be checked again against final hashes.

The saved stdlib-only `test_independent.py`, SHA256
`080a0e584a22aafc499d272ebbef1b2a68bb3765378c32778bcce0216e52e1e1`,
contains six controls: pin/source-scope authentication, metadata validity
for all 360 primitive entries, six denominator identities, all four binary
mask cases, the owned order ledger, and a nonphysical exact SL2 first-jet
control comparing the entire DAG to the physical-frame gerbe-minus-trace
formula. It evaluates no actual source polynomial. Its setup refuses to run
without the marker. The test code itself remains **unexecuted** and may
require correction when run; no success count is claimed.

Next owner: producer completes/stages the package and marker; root requests
CLR-R final review and runs, from repository root:

```sh
PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s research/codex-swarm/whole-source-clearing -p test_independent.py -v
```

Then inspect all final proof/code/receipt hashes, investigate any failures,
and update this report with actual commands/results and a scoped verdict.
Do not promote any arithmetic, Laurent, geometric-pole, historical-order,
or obstruction-value gate from the current review.

## Actual commands and outcomes

- `git show --stat --oneline 10810ee877fdaf291399198ad60d7dd0c316a42d`:
  confirmed the combined-pole commit. `git show PIN:<path>` read the source
  texts listed below; no physical code was executed.
- Metadata-only Python `json.loads(git show ...)` inspected chart denominator
  lists and compared compiler/support models: JSON content equality **True**;
  both model files have SHA256 `635bb1...19926` below.
- The same exploratory command attempted `import sympy` and exited 1 with
  `ModuleNotFoundError`. No package was installed; the saved independent
  controls use only the standard library.
- Ten Python marker polls used `Path.exists()` and bounded sleeps. Reported
  durations: 30.00, 30.01, 29.93, 29.93, 29.94, 29.93, 29.93, 29.94,
  29.93, 29.93 seconds: total **299.47 seconds**, marker absent each time.
- Metadata-only SHA256 inventories used `hashlib.sha256` over pinned bytes
  and current package files; no generated output file was written.
- No final test command was executed. There are no passing test results.

## Exact source pins (SHA256)

All paths below are at commit `10810ee877fdaf291399198ad60d7dd0c316a42d`.

| Path under `research/hm/` | SHA256 |
|---|---|
| `null-operator-compiler/hm-pinned-model.json` | `635bb12d9986e0dcada161d4173c773c4f134b9225354a3bc74267840ca19926` |
| `null-operator-compiler/hm-pinned-source-formulas.js` | `c4f65ff831092d0e56b3e33a0357f44182169fda45943ea780c8c551b4023f94` |
| `null-operator-compiler/outer-pinned-frames-and-poles.md` | `876cad001a8f96bb207ca246873e3efe67afd9a394cc4d2a0796992596b84916` |
| `null-proof-foundations/hm-transition-only-first-lift-alternative.md` | `a3b9564bd9ef3bbf497538037f73bdd90d998e302205eff342d8c6f52364e1c4` |
| `null-proof-foundations/refined-tracefree-pole-domain.md` | `209d8c8a35edabadabd57d4608c4b49a508700cc00e983d50045b7a722de5ab2` |
| `null-source-integration/combined-pole/PROOF.md` | `03673d6f120cb0b89d6d3887b7ab0bfee6aa33acf2abcc0ddbb116071b159c25` |
| `null-source-integration/order-comparison/source-order-curvature-comparison.md` | `c8dc3acbda9bcfc80317116ff2ff400e275ecf82a18f5321479c936d3c109451` |
| `null-support-certificates/pinned-homogeneous-identities.json` | `55e78bbc838a971b64531379788192acf8877c04f2d797fb13b4f4a68e47b018` |
| `null-support-certificates/pinned-verify-homogeneous-identities.py.txt` (read as inert text only) | `ad6fdb925262b9661bd51c0f65fe1a48d8f4ab1927bbf14b23786a4f0e1503bf` |
| `null-support-certificates/README.md` | `4ad6e152cefd70fda1af83fc531967913ee3122cf208d5eabc0aaf7c6994485a` |
| `null-support-certificates/hm-pinned-model.json` | `635bb12d9986e0dcada161d4173c773c4f134b9225354a3bc74267840ca19926` |
