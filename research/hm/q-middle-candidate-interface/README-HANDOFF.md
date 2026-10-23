# Candidate q-middle coefficient and sparse full-source interfaces

Status: candidate handoff only. No new verification, source-column generation,
source solve, old140/259/234 job, or spike burn was run while preparing this
package. A published branch must remain a draft until the campaign gates and
resource review are satisfied. Merely merging these files does not certify them.

Proposed destination: `research/hm/q-middle-candidate-interface/`, additive to
main `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb` (tree
`08e6aaa9e4788dd81984b67a9cd97d952093ecd4`). Campaign lineage supplied to this
handoff: PR #805, `d79b4ed8263076476296066def7f0c5be7752707`.
These are coordination pins, not independently fetched provenance claims.
Current payload bytes were hashed locally; their presence or originating
commits in the remote repository have not been verified.

## Included and excluded

80 unchanged mathematical payload files, 433,182 bytes. The static minimum
for the six entrypoints listed in `HANDOFF-MANIFEST.json` is 67 files,
390,192 bytes. It includes 38 runtime source/schema files (230,356 bytes),
the direct byte-hash inputs required by the q65 verifier, and sparse-verifier
hash/receipt inputs. The remaining 13 files are selected evidence and notes.
`PAYLOAD-SIZES.tsv` gives exact sizes, hashes, roles and minimum membership;
`HANDOFF-MANIFEST.json` gives the origin of each dependency.

No private notes, conversation, permissions, credentials, sessions, pickle
payloads or bulk caches are included. The only cache-path payload is the
small JSON summary whose `error_schemas` field is read by the sparse adapter.
Do not copy the neighboring cached rows or generator payloads.

The frozen `.sha256` files remain byte-for-byte intact. The q65 verifier
checks all 35 direct entries in `Q-CUBIC-KERNEL-LIFT-AND-FULL-COMPLETION.sha256`;
all 35 are included and matched during this static packaging pass. Other
nested manifests are only byte-hash inputs in these entrypoints. This is not
the full transitive historical archive, and recursively replaying every
historical manifest is not promised. Independent-audit logs and note are
included as evidence; their separate audit scripts and entire replay closure
are not included. Do not imply those audits were rerun here.

## Execution interface and hazards

Use Python with SymPy; versions have not been pinned or validated here.
Run candidate entrypoints with this directory as working directory because
the q65 verifier reads its frozen manifest relative to the working directory.
Preserve the internal subdirectories exactly.

The sparse constructor uses `SourceMap.__init__`, which executes only the
prefix of `derive_c_only140_unfiltered_principal_quotient.py` before
`rq_symbols,rh_symbols,Theta=ns['build_symbols']`. That prefix loads the
prefix of `verify_w_action_mixed_interface_one_ninth.py`, then the prefix of
`verify_full_six_space_vertex_correction.py`, plus the full universal Clifford
helper and `universal_complete_w_action_symbols.py`. These historical files
are retained unchanged because the runtime reads their source bytes. Their
presence is NOT an instruction to execute their historical top-level jobs.
Do not run those scripts directly. `STATIC-DEPENDENCIES.json` records these
edges. A next candidate refactor could extract explicit initialization helpers
and the 26-sector schema, then independently verify equivalence; no such
extraction or frozen-file change was made here.

The source API imports the frozen supported source class for helpers only.
The sparse qB verifier installs a tripwire forbidding the old
`SourceMap.source_map` on new middle data. Preserve it.

## Evidence status: no promotion from partial logs

- q65 coefficient verification: PARTIAL. 27 `CHECKED harmonic` lines occur;
  the final two all55+10/completeness PASS reports do not. The last label is
  `a2h_tv1_A__AA22_cg0_D5_outer0_B6_A`.
- Sparse arbitrary-qB verification: EMPTY log (0 bytes); expected
  `verify-sparse-q-middle-source-adapter-receipt.json` is absent. Not passed.
- Polarized dense bridge replay: EMPTY log (0 bytes). Not passed.
- Dense `verify_q_middle_source_extension_bridge.log`: PARTIAL against its
  current script. Two useful PASS lines cover the all234 reconstruction and
  residual identity, but the later all-ten-skew-pairs `q0*d(V)=d(errors)` PASS
  and terminal disclaimer are missing. Do not call this a completed run.
- `verify_q_middle_quotient_boundary.log`: terminal expected PASS/disclaimer
  present, including full18x18 comparison and both source ends (13.7 s).
- Independent full-source audit: terminal `all frozen files unchanged` PASS
  present (339.3 s), after all234 physical residual, five-column, endpoint,
  C,C anomaly, and off-image differential checks.
- Independent boundary/quotient audit: terminal frozen-manifest PASS present.
- Sparse negative-dual/external-cochain helper: both terminal PASS reports
  present for all200 cochain/all20 pairing/all6 external coefficients. This
  helper evidence does not certify arbitrary-qB sparse translation.

These are classifications of inherited log content matched to source text,
not recovered process exit receipts or new executions. `EVIDENCE-STATUS.json`
records every included log. The old campaign description of the dense bridge
needs the above terminal-status qualification.

## Proposed focused PR

Title: Add unverified q-middle candidate interfaces and replay dependencies

Keep this one additive folder in a draft PR. No changes to old certificate
folders or claims of proof repair. The q65 and arbitrary-qB sparse interface
share enough initialization and frozen input dependencies that one small
candidate-interface PR is preferable to two overlapping payloads.

Checks for the eventual authorized burn, all UNRUN in this handoff:
1. Verify payload digest ledger and environment pin in isolation.
2. SC-01: shard q65 reconstruction/completeness under the campaign envelope;
   require all55 harmonic+10 trace maps and final aggregate receipt.
3. SC-03: shard all234 sparse/dense comparisons, all26 errors, all6 external
   monomials, full endpoints, unrestricted duality and retained defects.
4. Preserve independent full-source provenance and finish/replace the partial
   dense-bridge terminal replay without relaunching an already-active job.
5. Complete SC-02/SC-04 and resource review before generating any source columns.

No monolithic all65 expansion, dense234 comparison, raw140/259/234 rerun,
source feasibility solve or new-family escalation is authorized by this note.
New output must use a separate versioned run directory, not overwrite these
inherited logs. Frozen checker code may need a reviewed wrapper or versioned
adapter to support bounded shards. Do not remove checks merely to fit a budget.

The 55 harmonic maps are candidate additional coordinates, not proven
independent operators. Ten trace maps remain bookkeeping, not free variables.
Do not discard q0N, companions or endpoints, conflate raw and corrected fourth
boundary targets, or interpret a candidate interface as an obstruction value.
