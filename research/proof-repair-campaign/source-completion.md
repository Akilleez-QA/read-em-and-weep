# Universal source-completion campaign

## Status and scope

Planning snapshot: candidate development artifacts through 2026-10-22 19:28 UTC, reviewed 2026-10-23. This module proposes a **new, separately identified universal symbolic spike**, not a restart of any prior run. No experiment, verifier, source solve, or actual-instance test was executed to prepare this plan; only file inspection and SHA256 calculation were performed. No external writes were made.

Suggested run identity: `source-completion-qmiddle55-v1-20261023`; the coordinator must choose a fresh immutable run directory before launch. The campaign is universal-symbolic only: no chosen actual Hilbert–Mumford coefficients, specialized geometric points or marking units, selected actual-instance matrices, or instance/rank tests. No paid resources, purchases, new service subscriptions, or paid cloud expansion. All concurrency is bounded by already available free/local resources. This module is not itself a record that launch occurred.

The outcome sought is one of: (a) an exact full-cochain universal completion within a precisely identified enlarged family, (b) an independently replayable exact contradiction for that family, or (c) a documented unresolved structural gap with preserved checkpoints. None alone is an unrestricted proof repair or fourth-Bockstein evaluation.

## Evidence inventory: verified versus unfinished

File basenames identify candidate research artifacts, intended for a separately reviewed repository import under `research/hm/order-four-quadratic-load/`. Only the explicitly pinned public commits below are public prerequisites. All unpinned development results, logs, hashes and mathematical claims are **local-only candidates awaiting reproduction and provenance review/publication**; they are not public established premises. “Verified” below means candidate artifact evidence was found, not that this planning pass reran it or that it is published.

### Pinned foundations and candidate development evidence

1. `MINIMAL-SUPPORTED-W-COEFFICIENT-BASES.md` and `AUDIT-MINIMAL-SUPPORTED-COEFFICIENT-FACTORIZATION.md`: supported coefficient basis has 54+10 identity-W and 162+33 traceless-W directions, totaling 259. The independent audit checks source/target factorizations, all-scale constants, determinant-balanced GL2 covariance, and physical B6 transport. This is coefficient-space independence before exterior action, not independent operators or unrestricted completeness.
2. `COMPLETE-TRACELESS-W-OPERATORS-HAVE-EXACTLY-TWENTY-FOUR-PRESENTATION-RELATIONS.md`: PR755 presentation gives 259−33=226 arbitrary-input supported operators; traceless part 195−24=171, identity part 64−9=55. It is not an operator count on closed/source inputs or a feasibility test.
3. `ACTUAL-SUPPORTED-SOURCE-PROBLEM-HAS-A-FIXED-TRACE-AND-216-HARMONIC-COEFFICIENTS.md` plus `audit_trace_fixed_source_full_blocks.log`: full supported family has exact affine reduction to 216 harmonic coordinates and a fixed trace primitive. Both arrows, source endpoints, external parameter projection and physical q0 are included. Harmonic 216/28/188 and trace 43/5/38 are coefficient/kernel/operator counts, not a solution. The reduction is NOT automatically valid for raw140.
4. `ALL140-FULL-U-AND-LOW-C-COMPLETION-WITNESS.md`: historical universal raw140 family passes full U and low-c equations, retaining 77 redundant coordinate labels; its subsequent first literal physical-q scalar gate has a 70-label affine family. These are intermediate source witnesses, not full high-mixed division. `COMPLETE140-FORCED-C-INTERFACE-INDEPENDENT-AUDIT.md` checks correct physical signs and scales. Later bounded exclusions prevent treating this historical partial progress as an unexplored complete route.
5. `ALL140-COEFFICIENTS-CROSS-THE-BALANCED-PHYSICAL-BOUNDARY-EXACTLY.md`, `verify_balanced_physical_140_boundary.py`, and `verify_full259_raw140_physical_boundary.py` preserve B6 conjugation, the identity-W trace correction, the mixed up/low factors, and the actual determinant adjoint. Do not conjugate their already physical cached matrices a second time.
6. `COMPLETE-SUPPORTED259-SOURCE-FAMILY-IS-EXCLUDED-BY-THE-HARMONIC-CERTIFICATE.md`: no regular division of the raw target F=kAt a p e_D in the complete supported259 family plus allowed negative-quartic Euler completion and full regular source ends. It follows from the full trace reduction and the supported216 94-row certificate. It does not exclude arbitrary middles or decide the canonical fourth source.
7. `UNIVERSAL-SUPPORTED234-BOUNDED-SOURCE-FAMILY-HAS-AN-EXACT-DUAL-CONTRADICTION.md`: adding the 18 harmonic exact-C-orthogonal D5 channels is also excluded. The field system has 235 affine columns, 21,500 rows, 3,119,450 entries; a 108-row dual annihilates all homogeneous columns. The old94 dual was nonzero on all18 new columns, yet the enlarged family was still inconsistent. An old-certificate escape is only a necessary equation, never evidence of solvability.

### Candidate q-middle interface, pending reproduction/publication

- `Q-ORTHOGONAL-A-PLUS-D5-LEGS-AND-FULL-SOURCE-COMPLETION.md`: q-orthogonal quotient has A+D5 legs; full U cancellation, lower q0-valued output, obligatory C3 companion, and C,C anomaly are retained. This is a bounded source-interface construction, not a joint source solution.
- `SPARSE-Q-ORTHOGONAL8-ADDITIVE-SOURCE-ADAPTER.md`: sparse raw8 adapter handles all108 formal symmetric-linear coefficients and six external quadratic monomials, with all26 errors, source ends, quotient companions, and off-image defects retained. Its own note explicitly requires fresh source/coefficient audits and parent review before enlarged-family computation. It is not permission to generate a 260-column family.
- `COMPLETED-Q-MIDDLE-C-SOURCE-FACTORS-ARE-FULL-BOUNDARIES.md`: canonical completed qB construction descends modulo **full** C-source homotopies from physical symmetric-linear B on 12-space (234 coefficient entries) to V⊗Sym²(M9) (135 entries). It retains both source endpoints and 1/cm. Further A-source identifications or other completions remain separate questions.
- `COMPLETE-55-HARMONIC-Q-MIDDLE-QUOTIENT-COEFFICIENTS.md` constructs 55 harmonic and 10 trace-bookkeeping equivariant maps for that prescribed quotient. The ten trace maps are not free unknowns in the fixed-trace system. Coefficient-space completeness is not operator/source independence and not unrestricted-middle completeness.
- `Q-MIDDLE-CANONICAL-INTERFACE-SOURCE-DIVISION-BRIDGE.md` supplies literal full-source residual/quotient identities. `verify_q_middle_source_extension_bridge.log` is **PARTIAL**: its two PASS lines cover the all234 source extension and residual/exterior identities, but the current verifier also requires the absent all-ten-skew-pairs `q0*d(Vactual)=d(errors)` PASS and final disclaimer. It does not establish terminal completion of that verifier. `verify_q_middle_quotient_boundary.log` completes the full18×18 boundary comparison and both source ends, with its final check at 13.7 seconds.

### Unfinished / not certified at the cutoff

- `verify_q_middle_quotient_coefficients.log` is partial: it ends at a `CHECKED harmonic ...AA22...A` line. The script still expects completion of all55 harmonic+10 trace maps and two final PASS reports. Do not call the full65 audit complete from this log or from the theorem note alone.
- `verify_q_middle_source_extension_polar_bridge.log` is zero bytes. The separate direct full234 bridge log is also partial, as noted above; the proposed polarization efficiency replay is not evidenced as finished.
- `verify_sparse_q_middle_source_adapter.log` is zero bytes. `universal_sparse_q_middle_source_adapter.py` exists and defines the arbitrary-qB interface, but the sparse translation's complete comparison is not yet evidenced as passing.
- Separate evidence, not a replacement for the partial bridge log: `audit-q-middle-full-source-independent/verify_q_middle_full_source_independent.log` reaches both terminal PASS lines at339.3s, including full source closure and unchanged frozen files. This is the distinct checker SHA256 `37d783b0f9d117dd519511f2d42d0fb8dcd7e8972a66ddc9114078d30c6ba71d`, log SHA256 `eb50e168bd997256828a5e3a1d65c991fef77f445432aa97a7f958eb9c6cc653`, bound by `audit-q-middle-full-source-independent/INDEPENDENT-AUDIT.sha256` digest `7368cbcd8ecb9134dbd3f448ab2343ba3e508c41175106879bce8f5e61cb5bd7`. Its scope is the frozen qB manifest `8a51729d04e922910d8b5e61e7651fbc7b006ae2a0f6a5597335660e3636e2d2` and corrected C-source companion manifest `a8eb6f73100806abb077359fbe15866fcffbff7ec6d97913d74accdf8d402eb5`; do not transfer that result to changed dependencies or infer completion of the author bridge verifier. These are candidate-artifact hash qualifications, not a new replay or public-provenance certification.
- No inspected artifact establishes a solved joint old-supported+55-q-middle source system, or the physical same-source completion needed for the corrected fourth-boundary target.
- Existing processes must be checked by the coordinator before any launch. Empty/partial logs do not prove failure, inactivity, or safe resumability. Do not duplicate an active producer or overwrite its output.

## Immutable source pins and reproducibility

Candidate artifact manifests establish byte identity only; their presence does not establish public Git commit provenance. The campaign provenance worker must bind repository copies before making a repository-publication claim.

Public commit pins recorded by the source notes:

- PR730 coefficient foundation: `a79c896439bc141dcb07a8891ba391ee8b38fcc9`.
- PR735 identity presentation: `c727e9d15b8a5ea0509875c174c80e99fc1cbb33`.
- PR741 exterior assembler: `eace951d98b0c5adb0462cb2d93c09eac5b08b8b`.
- PR746 traceless coefficients: `b02baa8ef2a8b488d6ef24713933d38aa8a0d2f7`.
- PR755 complete presentation: `fc509daba18d6c3b2a716fd33028f6ee7045d496`.
- Monad coefficient action: `8d8b5be4ce62c3055bb53be9e16d29cc63072f04`.
- Full scalar/N assembly: `bfd96c5ac15753647cbe25dd6085308855ca7f9e` and `e3dae3a9ff6b873b55f89a2c61bb74e38f0bd0b6`.

Candidate import anchors, not public prerequisites (must be reproduced and independently reviewed before use):

- `AUDIT-MINIMAL-SUPPORTED-COEFFICIENT-FACTORIZATION.sha256`: `138f50830d6832f29c9f2e1fc7ae64e22d883b5e0ea15079f3e62373dc867854`.
- `AUDIT-TRACE-FIXED-SOURCE-FULL-BLOCKS.sha256`: `beeb2bd1364389449dec1193f350f749f9d21001071b2a8bc7cc871b45734fcb`.
- `Q-MIDDLE-55-PLUS-10-AUDIT-INPUT.sha256`: `a05dd6e00a203cafa908b611c002824072d3109da16b3103ac1c038eb1ecdb56`.
- `Q-CUBIC-KERNEL-LIFT-AND-FULL-COMPLETION.sha256`: manifest digest recorded in q55 input `8a51729d04e922910d8b5e61e7651fbc7b006ae2a0f6a5597335660e3636e2d2`.
- `universal_q_middle_quotient_coefficients.py`: q55 manifest entry `303200e58b5aafd6fd7cd6f7eeafaba1b43094c281214706eb247da37cc9fb1a`.
- `universal_sparse_q_middle_source_adapter.py`: `2913780fa66b0c781b97de9d2cb2fa36a1e81e77c1b5c11fdb8322a102cd3496`.
- `verify_sparse_q_middle_source_adapter.py`: `07acc6ef811ec69a90cc8889a215ba8721ff1bee22470c7305a769ed14bfd3ed`.
- Raw140 full-U checkpoint recorded in witness: `97db626632b3d042e3dfe3efcaf5fb78fc747f8382d13aeac8de83b8c3d91c3b`.
- Supported234 source-audit manifest: `260904303c3b12a2e7443ef81b69eb6dc44eae6fe11690a88bc70a2696cc40ce`.
- Supported234 original result: `8f8146dccd43a68ce2de3220d65eb3cdc0f81e2b0d45e9a9db4f0fea76cb2d78`; independent replay: `aebbb5929d1f6e1c64ae367cd35e32747e0ee97863719165a0710686267cf066`.

Freeze every transitive import, executable, manifest, environment version, column label ordering, and schema in the new run manifest. Hash old inputs before and after each wave. Never edit a frozen old script to obtain a PASS.

## Work packages and dependency DAG

### SC-00: Freeze inputs and reconcile run ownership

Inputs: pins above, existing logs, process/checkpoint metadata available to the coordinator. Output: `inputs.json`, manifest tree, claim ledger, and a registry identifying every active producer and held historical run. Verify no prior experiment is silently resumed. Establish symbolic variable order and legal Laurent units. Gate G0 requires exact manifest matches and an explicit coordinator launch decision for this new run. A missing pin or uncertain active process blocks only dependent execution; documentation and independent static review may continue.

### SC-01: Finish q55 coefficient-space certification

Inputs: `universal_q_middle_quotient_coefficients.py`, `verify_q_middle_quotient_coefficients.py`, frozen q55 manifest. Shard by SS00, SS04, SS40, SS44, AA22 sectors; expected harmonic counts 1,6,6,31,11 and trace counts 0,1,1,6,2. Independent audit must check whole source/target reconstructions and cross-map inverses, not only nonzero witnesses. Check physical/intrinsic/quotient frame transitions on both indices; R is a regular section, not asserted equivariant. Output exact65-map digest ledger, per-map identity receipts, complete final aggregate checker. Ten trace maps remain bookkeeping only. Gate G1 requires all65 maps and matrix-unit/completeness identities, no partial-log promotion.

### SC-02: Physical-frame regression

Run universal free-entry checks against both raw140 and supported259 boundary scripts in a new run directory. Separate workers cover B6 adjoint conjugation, mixed `up B6` transport, arbitrary W trace term, two independent marking frames, and source channel scaling. All FB,FC,FD,theta,am,bm,cm,kAt stay formal and nonzero when inverted. Include identity-W and traceless signs; raw already-physical caches must not be conjugated again. Output a formal regression certificate plus an independent implementation with no shared assembly helper for its decisive identity. Gate G2 blocks generation if any sign, half, determinant-line, coordinate ordering or scaling mismatch survives.

### SC-03: Complete arbitrary-qB sparse source translation

Inputs: `universal_sparse_q_middle_source_adapter.py`, its verifier, canonical qB bridge, q8 sparse adapter and negative-dual pairing audit. Complete the missing sparse comparison on all234 independent formal coefficients; tag encodings or polarization are allowed only with a proof of full linear coverage. Check all6 external quadratic monomials on the entire record and all right-pairing input coefficients. Verify literal positive derivatives, zero-WW conversion, all26 errors, full source endpoints, and nonzero off-image defects. Compare to the independently executed dense canonical qB interface, not solely to shared sparse helpers. G3 requires a completed receipt plus independent audit; passing q8 alone does not certify arbitrary qB.

### SC-04: Full A/B/U/c identity and converse audit

For old+new combined residuals retain full A and B companions, both U columns, all3 c columns, fixed negative-dual right end and every skew source pair. Establish, with kappa=bm/am and q0=(xy+z²)/theta:

- `R + q0 Vactual = Ehigh + kappa Elow`, with complete channel factors restored.
- `Vactual = Vnorm - kappa^-1 N1 + p(ZN)` for canonical qB, exactly once.
- Source increment `kAt [[0,(cm/am)Pc],[0,-y]]` and its prescribed negative transpose.
- `q0 i_x(Vactual)=i_x(E)` and `q0 d(Vactual)=d(E)` before imposing errors.
- Both `-A(Pc)` and `-B(Pc)` survive, as do old VV/Ylow terms and the C,C anomaly.

Never declare the subtracted q0N or reduced C residual a separately closed monad cochain. Do not apply a C1-zero theorem to the unreduced new middle. Prove necessity and sufficiency for the **exact** chosen enlarged bounded family, or label the new system merely sufficient. Check source-homotopy quotient removes both endpoints, including 1/cm and derivative terms. G4 is the mathematical prerequisite for interpreting an eventual contradiction as a bounded nonexistence theorem.

### SC-05: Generate new universal source columns

Only after G1–G4 and fresh review. Generate the 55 harmonic q-middle columns, one task per coefficient with sector-based scheduling; retain complete source, quotient, error and off-image-defect records. Do not generate selected HM/source instances. Combine with old supported216 in an additive family ledger; proposed count is 271 homogeneous coordinates plus one affine target, **not** 271 independent operators. Do not automatically add old18 or raw8 as independent directions: first prove containment or full higher-weight equivalence, otherwise retain them as explicitly redundant additional blocks with documented family scope. Never add the ten trace channels as free variables. Source error cancellation must be joint, not imposed on each new column separately.

### SC-06: Universal row assembly and exact decision

Union every sector and every old/new row key, keeping zero sectors in the schema and verifying no rows disappear. Test old94/108 duals on the new columns only as cheap universal diagnostic identities; a nonzero pairing opens a necessary equation, not success. Establish exact Laurent row descent for the new columns afresh: do not reuse the old234 all-zero column-weight theorem without proof. Use the original Laurent-field representation if descent is not established. Perform a universal coefficient solve with formal marking units, never a specialized point or instance-rank solve. Produce either a full exact affine solution with residual replay, or an exact dual identity `(1,0,...,0)` over the original row ring. Any heuristic modular guidance must lift and replay exactly without specializing marking/geometry; unlifted heuristic results have no mathematical status.

### SC-07: Corrected fourth-boundary interface

Independent conceptual worker, parallel with SC-01–04. Inputs: `FOURTH-BOCKSTEIN-AFTER-ACTUAL-THIRD-VANISHING.md`, `ACTUAL-FOURTH-SQUARE-INPUT-REQUIRES-A-NONZERO-THIRD-SOURCE-CORRECTION.md`, `ACTUAL-FOURTH-BOCKSTEIN-AS-A-FIFTH-NEIGHBORHOOD-ADJOINT-BOUNDARY.md`, and fixed trace/full-source results. Produce an explicit interface contract distinguishing raw F=kAt a p e_D from the corrected representative `B4|D5-B3|A L`, or `q w_h=a(v_h-b zeta_a)`. Track reduction, source, actual Atiyah scale, trace primitive and dual endpoint normalization. A source completion of the raw target is not automatically the next corrected division. Do not invert beta on exceptional fibers, set b=0, use only square directions for all four channels, or infer a fourth value from third vanishing. If missing exact normalization prevents the bridge, stop the fourth-value conclusion and report the precise missing identity. This lane does not choose actual coefficients or points.

### SC-08: Independent proof and certificate packaging

Two distinct audits: (1) geometric provenance/full-source necessity and (2) independent arithmetic replay. The arithmetic checker must not import the solver and should use standard-library rational/Laurent arithmetic. Test wrong signs, dropped companions, omitted rows, affine-coordinate loss, reordered labels, changed units, trace freedom, duplicate restoration and checksum mismatch. Produce a compact immutable archive, isolated replay, semantic tamper tests, source manifest and precise theorem scope. A compact dual certificate checks a finite identity; it does not regenerate or replace geometric provenance. Final acceptance requires both audits and SC-07 contract status, clearly marking any unresolved fourth-boundary link.

DAG: G0 → {SC-01,SC-02,SC-03,SC-04,SC-07}; G1+G2+G3+G4 → SC-05 → SC-06 → SC-08. Provenance auditing begins at G0 and follows each wave. SC-07 is not forced to claim completion when the raw-family solve finishes.

## Parallelism and resource envelope

Fixed initial envelope: at most six research workers; at most two CPU-heavy local jobs concurrently; initially no more than 1.5 GiB RAM and 20 CPU-minutes per job. No paid capacity, paid APIs or API batch jobs. The first burn wave lasts at most 90 wall-clock minutes **after readiness is accepted**, not from plan creation. Planning does not launch that wave. Work unfinished at the end remains checkpointed and requires a subsequent scheduling decision; the cap is not a mathematical stopping argument.

Use a large task graph with many small, independently checkpointed coefficient/sector/row shards over this bounded pool. Documentation, provenance review and independent proof analysis can occupy the other four workers while the two heavy slots run. No monolithic source solve, dense234 comparison or all65 expansion may be launched merely because it exists as a script: first establish that its shard fits the initial envelope. Refactor into additive, versioned streaming/checkpoint adapters if needed, without changing the frozen mathematics.

Estimates, not commitments: frame/boundary symbolic checks may fit a single 20-CPU-minute shard (the existing candidate boundary log reports 13.7 seconds for its own smaller check); coefficient-space reconstruction, dense/sparse translation, 55 source columns and exact elimination are expected to need multiple shards and potentially multiple waves. The earlier candidate supported234 map has 3,119,450 entries, so unrestricted in-memory elimination should be presumed **not ready under 1.5 GiB** until a streaming representation is justified. Do not start a larger job on the assumption it will be cheap.

Suggested first-wave allocation after readiness: two heavy slots for the highest-priority unfinished q55/sparse-interface certification shards; four research workers for physical-frame audit, full-source converse, fourth-interface contract and independent certificate design. Generation and solving remain gated. Exact CPU/RSS and serialized-size measurements from permitted universal symbolic shards determine subsequent scheduling. A job reaching either cap checkpoints and stops; resource limits must never be evaded by unrecorded subprocess fan-out. If safe subdivision is unavailable, report that blocker rather than requesting paid expansion or silently exceeding the envelope.

## Failure conditions and checkpoint recovery

- Stop the affected lane on hash/provenance mismatch, unsupported denominator (positive/negative base coordinate, q0 or vertex ideal), lost channel scale, unauthorized specialization, trace freedom, omitted source/end block, separate-column closure filter, or an unexplained negative-dual sign. Continue independent read-only review.
- Stop theorem promotion when a verifier lacks a terminal PASS/exit receipt; preserve partial logs as partial. If a verifier is still active, do not restart it. Its eventual failure may trigger a **new** versioned repair task, not in-place frozen-file editing.
- Stop generation at G1/G2/G3/G4 failure; fix in a separate adapter version, rerun only newly affected symbolic identities after explicit checkpoint compatibility review.
- Resource ceiling: atomically checkpoint and suspend the affected producer before allocation failure. Do not treat suspension as mathematical failure or silently drop expensive sectors. Report missing shards and the estimate needed to resume on existing resources.
- Each shard emits run ID, parent manifest hash, code/environment hash, exact label, basis/frame and variable order, complete output hash, start/end status and exception. Write to temporary file then atomic rename. Aggregation accepts exactly one completed record per expected label and rejects missing, duplicate, stale or mixed-version records.
- Persist original Laurent rows, normalized rows with proven weights, pivot/reduction state, and a complete row-label map separately. A recovered elimination resumes only under identical manifest, ordering and normalization; otherwise create a new branch and rebuild from certified columns, not from opaque old pickle state.
- Negative result: archive exact dual and bounded-family theorem; do not rerun the same excluded family to burn more compute. Positive result: exact full-cochain replay first, then SC-07 comparison; do not call original proof repaired on raw-family success alone.
- Final stopping condition: accepted complete bounded-family certificate or explicit documented blocker requiring new mathematical scope/authorization. No automatic new-family escalation, actual-instance fallback or publication follows.
