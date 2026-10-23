# Two complete source cuts through PR888

Relative to published PR886 at192a2349475498aa3ea08863bd665a85573ccb20, necessary pairs change **351 → 310**. All **four labels**, profiles **3/0/1**, are preserved. The41 distinct new cuts are:

- PR887,3ab2f311ed2e87828d42c7c0ce0124bcd6e35771: index125 be, tuple(0,1,0,0,1,0,0,1),9 pairs.
- PR888,e9908b1d42d59c844abdb79bc734117a041f3d04: index127 h-b-f, tuple(0,1,0,0,0,1,0,1),32 pairs, only together with the exact PR885 reduction.

Remaining counts: G3.11.8ae96830fd21=4; G3.11.cce6e3ba4eeb=192; G3.11.ea6bced3bddf=36; G3.21.d610e381ed75=78. Index125 retains exactly bb,bc,cc,ce (9 pairs each); index127 retains six source tuples (32 pairs each). No whole label is removed.

## Exact scope and dependency audit

The complete proofs and reviews for PR887/888/885 were read at their immutable commits. Full source tuple and degree/irreducible multiset matching uses the original catalogs at db51525015bb7c5e825833d550d08dedf6f6ea96. Both original A/B endpoints, zero determinant defect and stable label are checked. Local catalog E IDs are only references and can be freely renumbered.

PR887's be argument checks the lower-P row zero and nonzero; the high-P divisor12 branch with its saturation correction; the three complete high-P kernels; all split full-positive kernel extensions; every zero/nonzero saturated internal graph; both surviving constant-V first spans; exact lower-positive graph capture; second constant-P high-line capture; and the negative residual after removing its actual constant sections. It does not assume that the final residual has no constants before proving the bound h0≤8. Its universal dependencies PR846,875,882 are already pinned and replayed in the predecessor stack.

PR888 is complete only with PR885 at53939364de5459822be1a32be08f2b12dbbb4280. PR885 by itself makes no pair cut. Its five high-P kernels and every internal-image alternative, low-D-zero case, constant first span, C9/C12/C8 cases, and scalar-zero branch are accounted for. The sole surviving scalar-nonzero branch still allows the optional T component to be zero or nonzero; PR888 places no restriction on that component.

The prerequisite PR859 at6129e92a26572779003f3295227f688b77ed881c explicitly excludes only the divisor12 branch for this exact h-b-f tuple. PR867 atb2a12c98bc162062a938b7a7a6a90ab45786e340 contributes only its section2 universal five-kernel classification, not its different cdf source's later branch exclusions. Both prerequisite proofs are included as exact pinned bytes, so neither a missing divisor branch nor a source-transfer assumption is hidden.

In PR888 the actual negative-row kernel is taken before the high-row kernel. The globally generated positive rank-two quotient is classified through all five possible splittings. The resulting U0 is not presumed saturated: full span leaves defect0 or12; defect12 contradicts the original Sym7 endpoint dimension bound. With defect0, the exact original dual presentation gives H1=V+P+D and twist-one Euler character−W. All12 permitted negative atoms and the degree−1 contribution are retained in the written support argument.

The JSON coverage metadata records these obligations; its verifier checks exact bytes, proof/review hash bindings, dependency identities, original source scope, pair partitions and stable IDs. It does not mechanize the written geometric arguments. The pinned actual-bundle presentations, group action, full span, original strict-top lemma and defect-zero derivative quotient remain mathematical premises. No Lean certification or actual HM realization is inferred.

PR869's nonempty abstract degree28 family and PR876's nonempty abstract cdf family remain explicit boundaries. The cdf tuple retains32 pairs and8ae retains4. Later results, all other tuples and all label gates are deferred. No actual-instance coefficients, points, derivatives, matrices or ranks are evaluated, and no production proof experiment is rerun.

## Reproduce

Using Python standard library and the unchanged published predecessor stack:

```sh
python3 verify_source_frontier_through888.py
python3 -O verify_source_frontier_through888.py
python3 -m unittest test_source_frontier_through888 -v
python3 -m unittest discover -p 'test*.py' -q
```

`--write` regenerates only the new `frontier-source-through888.json`. The18 new regression tests include rejection of PR885 alone as a full cut, omitted branches, missing scalar/saturation alternatives, duplicate cuts, wrong endpoints, mismatched source blocks, and reapplication; they also check E-ID renumbering and unchanged abstract boundaries.

## New publication files

Five top-level files: this note, `frontier-source-through888.json`, `source-pins-source-through888.json`, `verify_source_frontier_through888.py`, `test_source_frontier_through888.py`.

Eight exact inputs: `inputs/pr887_proof.md`, `inputs/pr887_review.md`, `inputs/pr888_proof.md`, `inputs/pr888_review.md`, `inputs/pr885_proof.md`, `inputs/pr885_review.md`, `inputs/pr859_proof.md`, `inputs/pr867_proof.md`. No predecessor file changes are needed.
