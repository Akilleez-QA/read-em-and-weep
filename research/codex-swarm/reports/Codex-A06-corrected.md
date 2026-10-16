> Worker proposal/review record. Acceptance and supersession are tracked in `../STATUS.md`.

**Codex-A06 correction — supersedes the prior A06 accounting. Admission remains FALSE.**

The prior offsets \(149+\sum p_j\) and \(294117+\text{live bytes}\) were unsupported. A held allowance establishes neither products consumed nor bytes currently live. The reported 149-product/294117-byte limits remain held; this correction grants no execution release.

**Certificate schema.** One global ledger, covering every worker and route:

- `scope`: ledger ID, revision, resource definitions, source pin, authorized caps \(C_P,C_B\), hold/release status.
- `spent`: actual cumulative product count \(S_P\), with unique operation IDs and receipts. Never decreases.
- `reservations`: unique reservation ID, owner, remaining product allowance, byte commitment, validity interval, backing authorization. Reservations are commitments, not measurements.
- `allocations`: globally unique allocation ID, owner, byte bound and evidence, actual size when known, creation/free events, aliases and transfers. Ownership transfer does not end a lifetime.
- `schedule`: dependencies and ordered allocation, operation, output, serialization and free events; concurrent intervals; workspace bounds.
- `coverage`: reconciled actual other-worker live allocations and outstanding commitments; reviewer and unresolved fields. Unknown is distinct from zero.

Every byte account must use the same declared metric. Retained-output bytes and RAM require separate ledgers if both are constrained.

**Exact admission rule.** Let \(R_P\) be outstanding reserved products outside candidate \(K\), and \(Q_P(K)\) its certified remaining product bound. Require
\[
S_P+R_P+Q_P(K)\le C_P.
\]
If \(K\) uses an existing reservation, replace that reservation by its candidate bound; do not count both. Each executed product increments \(S_P\) and consumes its reservation atomically. Failure and recomputation do not refund spent products.

At event \(e\), let \(L_e\) be the union of actual live allocation IDs across **all** workers. New outputs enter before any dependent input is freed:
\[
L_{e+1}=(L_e\cup N_e)\setminus F_e.
\]
The schedule must bound
\[
B_e=\sum_{v\in L_e\cup N_e}b(v)+W_e+U_e\le C_B.
\]
Here \(W_e\) covers concurrent workspace not already represented by allocation IDs; \(U_e\) covers outstanding byte commitments not already backed by those live/workspace charges. Commitments require explicit backing and release events to prevent omission or double counting. Shared storage counts once only with authenticated allocation identity; copies count separately. Check every allowed overlap, or enforce the certified serialization.

Admission requires complete reconciled global state, checked bounds **and** execution authorization. Any unknown leaves admission FALSE.

**Tiny fictional example; no source arithmetic.** Cap 10 products; actual spent 3; another job reserves 2. Candidates requiring 2 and 4 cannot both enter: \(3+2+2+4=11\). Worker boundaries never reset the ledger.

For a 20-byte cap, other live storage is 4 bytes. Worker A holds input 3 and creates output 5; concurrent worker B holds 6; workspace is 2. Peak is \(4+3+5+6+2=20\), counting each allocation ID once. Freeing A’s input first would incorrectly report 17. One additional unbacked byte commitment would reject this overlap.

**Evidence and dependency.** Pin `08b73637d4136f91606aad332c46cafd064417f8`, `research/hm/current-scalar-geometric-dependencies/data/source-formulas.js`; comments #6205127744, #6205249609 and #6205660472 distinguish the corrected source, finite support bounds and unresolved arithmetic readiness. PR79 is metadata only per current task input; certified survivor sizes remain missing.

Original contribution: corrected accounting contract, not a detector or completeness result. Proposed reviewers: V06/I01; review pending. Next step: supply reconciled global receipts, allocation lifetimes and certified size/workspace bounds. No physical-source evaluation, arithmetic oracle or tests ran.