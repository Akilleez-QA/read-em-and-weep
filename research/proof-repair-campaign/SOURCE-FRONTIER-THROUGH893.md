# Source checkpoint through PR893

From published PR890 at92fd2ba79aeece747622d3ded7cbdaf22e97eb26, this append-only checkpoint changes necessary pairs **310 → 269**. All **four stable labels**, profiles **3/0/1**, remain.

- PR892 at88c50be95de2f0c688e7226e6c78c67b751a540d removes32 pairs for index127 g-b, tuple(0,1,0,0,0,0,1,0), G3.11.cce6e3ba4eeb.
- PR893 at7645e2458c3b85c5d814c22255dae8cabc7226bc removes9 pairs for index125 ce, tuple(0,0,1,0,1,0,0,1), G3.11.ea6bced3bddf.

The exact residual row counts are8ae96830fd21:4, cce6e3ba4eeb:160, ea6bced3bddf:27, d610e381ed75:78. Index127 retains five source tuples,32 pairs each. Index125 retains bb,bc,cc,9 pairs each. No whole-label exclusion is encoded.

## PR892: original maximal profile is indispensable

The complete immutable proof and review were read. Its source, quotient endpoints and defect match both original catalogs atdb51525015bb7c5e825833d550d08dedf6f6ea96. The newly included original actual-presentation note, sections4–5, defines the maximal consecutive rank-three plateau and its dual reversal. For original profile11, Q* has rank13, first gain3 and next gain at most2, giving upper bound18. The verifier explicitly requires profile11 in both the preserved row and original label catalog, and separately records the maximal-profile premise.

PR859's divisor12 theorem explicitly includes this g-b tuple. PR867 supplies only its universal section2 five-kernel classification, not its cdf-specific exclusions. PR885 supplies actual image/polar principles and its degree38 obstruction with the same original dual endpoint. Their exact prior proof hashes are checked against the new review and preserved predecessor pins.

The changed W(-11) target is checked independently. All five high-P kernels and every internal-image alternative are covered. The nonconstant C9/C12/C8 cases are excluded; particularly the C12 caseII negative scalar row is proved zero from the actual induced derivative through T(-3), not discarded from a splitting type. The remaining constant first span produces the actual constant ten-space and saturated projected residual.

The projected W(-9) plane is handled as a coherent lattice before saturation. Rank0 and rank1 are excluded; its actual line first-polar lattice is identified; full span then identifies the complete degree-ten system and proves saturation. Actual dual restriction maps provide two nested fixed constant kernels. Rational lifts and constant projection give inner lower bound11+5 and outer additional3, hence second dual osculating rank at least19. This contradicts18 under the original maximal profile. No rank additivity through a moving extension or horizontal splitting is assumed.

The final twist-one character is compatible, not an exclusion. A failed direct-sum family construction is not used as evidence of closure, and the result is not broadened to all abstract bundles with this splitting or all profiles. The separate cdf abstract family remains untouched, retaining32 pairs.

## PR893: complete ce source branches

The complete proof and review were read. PR887's section2 high-P classification is imported only as a universal kernel lemma, not as the be exclusion. PR882 supplies the inherited actual-bundle conventions and exact constant-projection interfaces.

The lower P-row-zero case has both possible internal scalar-V images, each contradicted. With that row nonzero, the high-only P onto branch covers all three kernels and both low-V kernel alternatives, using Hom vanishing on both ends without assuming extension splitting. The divisor12 branch treats zero and full V internal images, including saturation budgets.

For nonzero lower V row, both first spans and all projected channel alternatives are treated. The extra Euler block is retained in the actual constant-V intersection, followed by exact lower-positive graph capture, constant-P high capture and the positive-degree quotient contradiction. For zero lower V row, both values of the complementary restricted high row q are covered: q nonzero is proved basepoint-free and its complete five-kernel list has zero internal image; q zero retains the raw two-O(4) image and proves saturation before the actual constant-V/whole-linear-block contradiction.

## Verification boundary and reproducibility

The source identity uses the full eight-coordinate tuple and decoded degree/irreducible multiset, not local E-ID numbers. Original A/B endpoints, zero defect and stable labels are checked. Counts are intersections of historical necessary pairs, not realized geometries. All41 cuts are distinct; prior snapshots are unchanged.

The code validates provenance, exact scope metadata, finite pair partitions and the explicit original-profile gate. It does not mechanize the written geometric proofs or independently reconstruct the upstream actual HM presentations. Those presentations, characteristic-zero group action, saturation/full-span assumptions and actual connection remain pinned mathematical premises. There is no Lean claim, actual-instance evaluation or production-experiment rerun.

PR869 and PR876 remain nonempty-abstract-family boundaries, not HM realization or exclusion. PR891 calibration is unrelated and causes no source cut. All later results and whole-label gates are deferred.

```sh
python3 verify_source_frontier_through893.py
python3 -O verify_source_frontier_through893.py
python3 -m unittest test_source_frontier_through893 -v
python3 -m unittest discover -p 'test*.py' -q
```

Use Python's standard library with the unchanged predecessor stack. `--write` regenerates only `frontier-source-through893.json`. The20 new tests cover missing branch obligations, maximal-profile mutations, nested rank bounds, both V-row/q branches, exact tuples/blocks and endpoints, arbitrary E-ID renumbering, no duplicate cuts, and unchanged abstract-family rows. All248 stack tests pass.

## Publication files

Five top-level files: this note, `frontier-source-through893.json`, `source-pins-source-through893.json`, `verify_source_frontier_through893.py`, `test_source_frontier_through893.py`.

Five exact inputs: `inputs/pr892_proof.md`, `inputs/pr892_review.md`, `inputs/pr893_proof.md`, `inputs/pr893_review.md`, `inputs/pr892_original_actual.md`.
