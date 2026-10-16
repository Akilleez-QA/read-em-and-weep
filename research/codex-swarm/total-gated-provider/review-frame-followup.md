# TP frame correction: independent follow-up acceptance

**Accepted within pure row-frame planning and unconditional-gate scope.** No producer file, historical independent file or JC file was changed by this review. New reviewer files are only `test_frame_followup.py` and this note. The actual provider still supplies no Rsharp End coefficient implementation or execution capability.

## Exact semantics checked

For a normalized raw Rsharp request, the canonical value is based at the sorted tuple's first common vertex. Let the original first vertex be i and canonical first be j. The row-End frame change is

    value_at_i = permutation_sign * g(i,j)^-1 * X_at_j * g(i,j).

The ordered edge is exactly original-first to canonical-first. Sorting that edge and substituting a forward transition would reverse the needed conjugation. This is the same row-End convention as `delta x=g_ij^-1 x_jk g_ij-x_ik+x_ij` in the pinned first-order source at08b73637d4136f91606aad332c46cafd064417f8, `research/hm/current-scalar-residual-attribution/first-order-source.md`. No matrix factors are commuted and no nonlinear raw residual is re-evaluated after sorting.

`frame_plan` compares original/canonical **common keys**, not occurrence identity or physical labels alone. Identity routing when their common keys agree is appropriate; occurrence provenance still remains in the full original/sorted owner tuples. Distinct common tags with equal physical labels survive for Rsharp and retain their exact ordered transport request. A separately proved transition identity could simplify that transport later, but cannot introduce a stronger cochain zero rule.

F and T are scalar coefficients already expressed in their fixed common finite pair frame; their frame route is identity with the single effective parity. The stronger physical-source repeated-vertex zero remains restricted to F. Rsharp gets common repetition only. Empty Rsharp tuples have no base owner or edge request. Zero plans require no transition evaluation. Original owner/prefix positions, occurrences, tags and aliases remain recorded; frame planning neither merges clearings nor repairs aliases. This row-End routing concerns raw Rsharp; it is not a second conjugation to apply to original-resolution J matrices after inclusion.

An independent exact rational countercontrol takes

    G=[[1,2],[3,7]], X=[[2,5],[7,11]].

Then G^-1 X G=[[39,91],[-11,-26]]. With an odd permutation the correct result is[[-39,-91],[11,26]]. This differs from both parity*X and parity*G X G^-1. Looking up only the silently sorted edge fails the exact artificial registry request. No actual physical transition is evaluated.

ToyProvider explicitly declares `scalar_fixture_only`; an artificial table entry named Rsharp tests scalar parity and is not an End evaluator. Matrix table values are rejected. Actual coefficient, alternating-coefficient, factor-stream and owner methods still raise before normalization or frame routing, even after mode/verified fields are forged.

## Historical artifacts and transparent replay

The published producer snapshot checked is commit `d18d9810f7333d9f94a895c4e26985520cc60057`. All five producer files plus the marker and both historical reviewer files match that commit byte-for-byte before/after this review. No pre-correction provider snapshot was retained, so this report does **not** claim an independently reconstructed exact old/new provider diff. Current corrected semantics were read and independently tested.

The original `test_independent.py` anchors its historical marker03dbc4..., so invoking that stale file directly against the corrected producer is intentionally not the follow-up replay. It and `review-independent.md` remain unchanged. `test_frame_followup.py` first authenticates the CURRENT marker and all producer bytes, then loads the original test source in memory with an AST transform replacing **exactly one assignment**, MARKER_SHA, from the known old value to the independently anchored current marker. The original PINS_SHA, every transitive workspace/immutable proof check, every test body, and before/after input checks remain unchanged. The original test's whole file hash is itself anchored before the transform. No replacement is written to disk.

Use these explicit commands, normally and with `-O`:

    timeout 60s python -B research/codex-swarm/total-gated-provider/test_frame_followup.py -v

This executes7 new frame controls and11 preserved historical tests: **18/18 pass in each mode**,0 failures/errors,0.130s normal and0.131s optimized. Direct follow-up runs impose512 MiB address space and59 CPU seconds before authentication/import; external timeout is60 seconds. The9 current producer tests also pass in each mode under an equivalent resource-limit/runpy wrapper:0.066s normal and0.068s optimized. Thus the final bounded set is **27 tests per mode**. The historical replay includes one guarded actual-definition AST description; it forbids actual polynomial/coefficient/fiber execution. New frame controls use only tiny artificial matrices/owners.

## Exact checked hashes

| File | SHA256 |
|---|---|
|producer-ready.json|2b359484048dc31e8e4258f7ea864ec15f9a57c36729f71439f9954e230e750d|
|provider.py|bf9bf8f712fe5c7959097c24521ea01fd8c50010f55003af61870050fbc068af|
|PROOF.md|afc5eb479dc9a24ca569c955644a2823e9a2d20b773d1b64a611a495b732245e|
|README.md|ce8b9791f4e475166953a5157adccd9ecb4ae6ae2fecb3cc578efb656acf454c|
|source-pins.json|84b292ec6a9f9260e0dfd52dd39aa2f8abd9c2f6d16b38948aabca0a675bd186|
|test_provider.py|2519a2ac1e83202bf51c27f1b234dc5df0ca5f77288556ca82a999637b965783|
|historical test_independent.py|5797d6a113fc63676e3373873ffb3dd15a177b4480a6db6b17b8e74bf95ec835|
|historical review-independent.md|23879d3ca96aeb342a59a42550a83c4ad4e569bb316eb3a4b951f9d4be49b1d2|

This acceptance supplies no historical nonlinear-source identity, full T/Rsharp coefficient implementation, aggregate resource schedule, physical value, actual fiber enumeration, execution release or obstruction verdict. No Git commit or post was made.
