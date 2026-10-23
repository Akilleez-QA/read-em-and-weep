# Source checkpoint through PR897, after publication PR898

Relative to published PR898 at5d2345090aecc2240555fb6f39a1f2ea813dcd62, necessary pairs change **269 → 228**. All **four stable labels**, profiles **3/0/1**, remain. The checkpoint name follows the source-proof PR, not the later-numbered predecessor publication.

- PR895 atf720acbe80547fd1bccd5ff54e6b62a4daa41834: index125 cc, tuple(0,0,2,0,0,0,0,1), removes9 pairs.
- PR897 at0429ef1290e71e48987474dc7787c9e9f2b812d3: index127 a-c-e-f, tuple(1,0,1,0,1,1,0,0), removes32 pairs.

Residual counts are G3.11.8ae96830fd21=4, G3.11.cce6e3ba4eeb=128, G3.11.ea6bced3bddf=18, G3.21.d610e381ed75=78. Index125 retains bb and bc (9 pairs each). Index127 retains four tuples (32 pairs each). No whole-label exclusion or realization assertion is encoded.

## Scope checked from the full immutable proofs and reviews

Both proofs and reviews were read in full. Exact source identity is matched against both original catalogs atdb51525015bb7c5e825833d550d08dedf6f6ea96, including tuple, stable label, A/B endpoints and original defect zero. The complete decoded degree/irreducible multiset, rather than a local E-ID, selects the removed pairs.

### PR895 is not a strict-top exclusion

The target has two V copies, exactly enough for the two top V copies. The index113 cc multiplicity contradiction does not transfer to index125. The new proof first classifies every kernel of a hypothesized onto full positive pair through the complete eleven-atom list and the two remaining kernels. Both give zero internal image and positive first-span degree4.

It then forces the high P row to have the invariant divisor12, retaining the zero high-P row as well. The two V rows prove that the raw external image is exactly two O(4) lines, not the saturated positive pair. The raw first span has degree−8; a positive invariant saturation defect would have degree at least12, so saturation is proved before the polar calculation.

Projection by the actual constant P has rank7 and all three nonzero channels, giving the saturated complete degree6 inclusion and an actual constant nine-space in the quotient, hence a constant thirteen-space upstairs. The two quartic V tails have only one high-row channel; its multiplicity kernel supplies a genuine tail summand with zero external derivative. Its projected coherent image is proved connection-preserved and saturated before treating image ranks0/1/2/3. This traps the tail in the same constant thirteen-space. The saturated top-plus-tail has rank13 and degree−32, contradicting equality with that constant space.

### PR897 retains every changed Wp channel

PR859 explicitly includes the a-c-e-f tuple and closes its divisor12 branch. PR867 supplies only the universal five-kernel classification, not its different cdf-specific exclusions. The complete changed internal target is D(-4)+Wp(-5)+V(-6)+Wp(-7)+O(-10). In particular the degree13 Wp covariant from O(-18) is retained; replacing it by T or assuming every channel zero would be incorrect. All zero/nonzero images and simultaneous saturated combinations are covered.

The remaining constant first span uses two actual constant projections, after which the negative Wp(-3) becomes horizontal. The rank-eight C9 alternative is excluded independently. For C12, exact actual coefficient maps, intersections and the saturated Y give both possible negative scalar rows. The zero row has the precise degree38 obstruction with its saturation bound established first. The nonzero row reconstructs every hypothesis of PR888 Sections1–4 before invoking that interface: actual negative-row kernel first, all five positive rank-two splittings, defect0/12 alternatives, original endpoint bound, and the exact twelve-atom cohomology contradiction. It does not transfer the h-b-f whole-source theorem by name.

In the rank-six C8 case, Wp(-3) can indeed inject into the changed target. The contradiction instead uses the necessary rank3 degree−10 quotient: after excluding degree−2, its degrees must be(-3,-3,-4). Central parity forces a scalar O(-4) companion, and that companion has zero map into every target block. The allowed Wp channel cannot repair its zero map. Both this distinction and the degree13 covariant are explicit verifier metadata and mutation-tested.

## Reproducibility and limits

`source-pins-source-through897.json` binds the four new proof/review files by immutable commit, path, URL and Git blob. Proof SHA256 values are also bound to the reviews. The inherited dependency stack authenticates PR859/867/885/888 and PR875/882; their exact interface references are checked again. Original actual presentations, characteristic-zero group action, saturation/full span, strict-top and zero-defect derivative quotient remain mathematical premises.

The executable validates those bytes, scope metadata, exact source identity and disjoint finite pair partitions. It does not formalize the geometric proofs, evaluate actual instances, select coefficients/points/matrices/ranks, or rerun production proof experiments. There is no Lean claim. PR869/876 abstract-family boundaries and the cdf tuple remain unchanged; later cuts and all whole-label gates are deferred.

```sh
python3 verify_source_frontier_through897.py
python3 -O verify_source_frontier_through897.py
python3 -m unittest test_source_frontier_through897 -v
python3 -m unittest discover -p 'test*.py' -q
```

Use Python standard library with the unchanged predecessor stack. `--write` regenerates only the new snapshot. The21 new tests reject omitted branches, false cc strict-top exclusion, discarded Wp channels, mismatched endpoints/blocks, duplicate cuts and reapplication. They check arbitrary local E-ID renumbering, both scalar-row alternatives and unchanged abstract-family rows. All269 stack tests pass.

## New publication files

Five top-level files: this note, `frontier-source-through897.json`, `source-pins-source-through897.json`, `verify_source_frontier_through897.py`, `test_source_frontier_through897.py`.

Four immutable inputs: `inputs/pr895_proof.md`, `inputs/pr895_review.md`, `inputs/pr897_proof.md`, `inputs/pr897_review.md`. No predecessor file changes are required.
