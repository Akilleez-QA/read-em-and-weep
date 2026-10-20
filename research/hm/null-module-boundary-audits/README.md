# Module and semiregularity boundary audits

## Scope

These six existing reports isolate the limits of transferring an ambient result to the bundle/module problem. They are not a new module-existence or obstruction-vanishing theorem.

- `module-parity`: full sign survives diagonal inversion; equivariance narrows choices but does not remove the retained obstruction.
- `module-lifting`: universal row-module defect and correction formulas, conditional on a genuine ambient extension and appropriate cover.
- `retained-remainder`: an exact removal criterion for unrestricted split vector-space maps, not geometric realization.
- `geometric-lift`: regular extension and descent obstructions missing from that criterion.
- `quantization-criteria`: comparison gaps for fixed global algebra-sheaf criteria.
- `semiregularity-sector`: ordinary semiregularity has no U22 target and cannot detect the retained sector.

## Dependencies and pins

Depends on the literal-ambient-extension packet. Ext and character premises remain those of [closure-and-characters at 08b73637d4136f91606aad332c46cafd064417f8](https://github.com/Akilleez-QA/read-em-and-weep/tree/08b73637d4136f91606aad332c46cafd064417f8/research/hm) and the corrected alternating primitive at `a859396a3c39052c837b3bf366bd2cf7f0cec353`; the published retained chain is in [PR79 at 4659e4425c6b5ab6b1899e6af93656ac03ff0862](https://github.com/Akilleez-QA/read-em-and-weep/tree/4659e4425c6b5ab6b1899e6af93656ac03ff0862/research/hm). The retained/geometric reports additionally depend on the homotopy-compensation packet. These imported claims are not recalculated here.

Public discussions: [module boundary](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6259839595), [ambient distinction](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6259871686), [semiregularity](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6259931094).

## Review status

Existing independent reviews accompany `module-lifting` and `retained-remainder`. No separate review files were present for the other four reports. The module audit's acyclic trivializing-cover qualification applies to both H² and H¹/Ext identifications. The original ambient cover is not by itself verified to trivialize E.

## Unresolved boundary

All thirty retained values remain unknown. Ordinary unobstructedness and ambient HH³ vanishing do not imply Ext² vanishing. The split-vector-space criterion is not a regular or module-linear splitting theorem; semiregularity blindness does not rule out different detection methods.

## Imported source pin

The literal scalar presentation is PR16, commit `c8aec970fd65a105f39f4e8aeb8a17f0f0053f89`, blob `a58834ab61e18a5dedd8a7bf20bec7121bfa9165`: [second-order-algebroid.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/c8aec970fd65a105f39f4e8aeb8a17f0f0053f89/research/hm/second-order-algebroid.md). It is linked, not recopied. Source assertions are imported at this pin, not re-evaluated.

This packet preserves existing proofs and audits. No checker, geometric source evaluation, or experiment was rerun for publication.


## Published predecessor pins

- [B2b](https://github.com/Akilleez-QA/read-em-and-weep/tree/9e3d8dc8525a7d11ae919dfac2126794c9bdc366/research/hm/null-literal-ambient-extension)
- [A3](https://github.com/Akilleez-QA/read-em-and-weep/tree/0c7f3f16ddea65616b2c6d4629c8b44f6fdae625/research/hm/null-homotopy-compensation)
- [A4 deck-character index (semiregularity imported premises)](https://github.com/Akilleez-QA/read-em-and-weep/tree/0d79d7be416fc181ece42ff5c6d2c8075d340d79/research/hm/null-deck-character-index)


## Historical source frontier

Statements in this packet that leave thirty obstruction coordinates or values unresolved describe the historical stage of these preserved notes, not the latest project verdict. For subsequent developments and the current project status, see [project status, issue #92](https://github.com/Akilleez-QA/read-em-and-weep/issues/92). Original arguments and historical review scopes are preserved; publication performs no new source evaluation.
