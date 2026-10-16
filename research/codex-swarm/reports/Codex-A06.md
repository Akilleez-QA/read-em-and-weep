> Worker proposal/review record. Acceptance and supersession are tracked in `../STATUS.md`.

Codex-A06 — **arithmetic admission: NOT ADMITTED.** Available reports are I01/V01/V03 proposals; no C/A survivor-size or arithmetic schedule report was available. No physical arithmetic or tests ran. Reviewer: Codex-V06/Codex-I01; review pending.

**Combined ledger contract.** Domain: exact characteristic-zero evaluation of the complete corrected
\[
R^\sharp=M(0)^0+F_qk_p+F_pk_q+E_p(T_qF_q)+E_q(T_pF_p),
\]
with authenticated full owners, frames, cancellations and detector demands. All 78 seeds contribute to ONE detector.

Maintain one global physical ledger across every worker and route. Start with **149 polynomial products encumbered and 294117 bytes held**. Neither allowance resets per worker; the held pool has no authorized release.

For a serialized schedule, let \(L_t\) be live allocation IDs outside the held pool. Each allocation has a certified byte bound \(b(v)\). For operation \(t\), let \(N_t\) be new allocations, \(F_t\) allocations freed after completion, and \(w_t\) additional workspace, including transient arithmetic and serialization buffers. Require:
\[
L_{t+1}=(L_t\cup N_t)\setminus F_t,
\]
\[
B_t=294117+\sum_{v\in L_t\cup N_t}b(v)+w_t,\qquad
B_{\rm peak}=\max_t B_t,
\]
\[
P_t=149+\sum_{j\le t}p_j.
\]
Outputs are charged before input frees. Shared allocations count once only with authenticated allocation identity and lifetime; identical symbolic expressions do not establish sharing. Concurrent operations require their overlapping live sets and workspaces to be combined. Otherwise the certificate must prescribe serial execution.

Here \(p_j\) counts actual polynomial-product invocations, including recomputation. Record coefficient multiplications, additions, exact divisions and reductions separately; streaming coefficients does not justify declaring multiplication cost zero. No release or recomputation refunds cumulative product charges. Admission requires both inequalities against the **existing global caps**, after accounting for any other commitments.

**Required joined C/A records.**

- C: complete demand keys and ownership; each label classified as retained, proved zero, reserved or unresolved. Preserve the seed4 E12 and 704-tuple reservations.
- A: each retained demand bound to exact source bytes, operation DAG, representation, certified survivor/support and coefficient-bit bounds, output size, workspace, dependencies and last uses.
- Join: complete coverage of all five displayed terms, exact sharing identities, operation counts, and one schedule covering every worker’s allocations and transfers.

Missing survivor sizes, source bytes, workspace bounds, global caps or unaccounted commitments means **no admission**. A rigorous representation-specific storage bound is acceptable; guessed occupancy is not. The Laurent envelope, carrier/legal pole bounds, 78 selectors, request-family counts and dependency-node counts are not storage measurements.

**Evidence and failure control.** Pin `08b73637d4136f91606aad332c46cafd064417f8`; source: `research/hm/current-scalar-geometric-dependencies/data/{source-formulas.js,model.json}`. Public comments #6205127744 establish the corrected representative; #6205249609 explicitly separates support envelopes from storage; #6205455951 supplies pruning; #6205660472 leaves arithmetic readiness unresolved; #6206738230 supplies existence without a feasible schedule. Their reported checks were not rerun here.

Original contribution: the combined lifetime/count recurrence and admission contract. Orchestration rosters and prose are dependency evidence, not physical arithmetic certificates. Next step: supply the joined C/A manifest above for V06/I01 review. This contract establishes neither a detector value nor completeness.