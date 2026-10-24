# Reproduction and precise claim boundary

This focused packet is stacked on `null/rankfour-short-cubic-plateau` at
`7e915f5febb13719536faadd42e94301a1b03df4` (#1176). Every addition is under
`research/hm/rankfour-reverse-adjacent`.

## Conditional conclusion

The actual ordered maximal rank-four plateau `(k,l)=(3,2)` is impossible
under the retained actual-geometric premises and physical marking.
Endpoint persistence and parity force zero determinant defects and precisely
two endpoint-degree cases. An exact associated-graded K-class identity
eliminates the rank-four quotient without enumerating it. The complete
401-pair intrinsic rank-five endpoint domain leaves fourteen necessary
Euler survivors; every survivor violates a genuine H1-character condition.
The primal and dual bundles remain distinct, and all H1 corrections remain.

Relative to the established coarse necessary overlist after #1176, this
removes exactly one bin: 24 become 23. Across all four source labels, the
corresponding labeled overlist changes from 96 to 92. These are necessary
overlists, not realized strata. All nine bad rank values 4 through 12 remain.
No generic SF rank-at-least-five theorem, square-map surjectivity,
full-adjoint invertibility, or original repair follows. The separate
rank-four `(3,1)` and `(2,2)` cases are not excluded by this result.
The other published rank-four exclusions are not logical inputs here.

## Reproduce

From the repository root:

```sh
python3 research/hm/rankfour-reverse-adjacent/verify.py
python3 -O research/hm/rankfour-reverse-adjacent/verify.py
python3 research/hm/rankfour-reverse-adjacent/independent/verify.py
python3 research/hm/rankfour-reverse-adjacent/independent/test_controls.py
python3 research/hm/rankfour-reverse-adjacent/verify_publication.py
```

The author runs match `RESULT.json` byte for byte: 10,951 checks and 54
contract-mutation rejections. Contract mutations test recorded expected
consequences; they are not independent executions of a modified proof.
The independent verifier performs 470 checks using exact conjugacy-class
arithmetic and ordinary-deficit endpoint enumeration, without author-code
imports. Its nine negative controls execute genuinely modified computations.
The full publication verifier authenticates every included file, compares
all endpoint domains and all fourteen pairs with both character columns,
checks the reviewed author snapshots, executes six normal/optimized replays
(including unrelated working directories), and replays all nine controls.
Its exact expected output is `PUBLICATION-CONTROLS.json`.

All programs use only the Python standard library, with no network access.
Complete public inputs are repeated only to keep the packages self-contained.

## Frozen mathematical identities

- Author proof SHA256: `6e9a8770e4d418e6ba22a3ebaa2b1523605a178ac0522d7f4ab72507d536106a`.
- Author checker SHA256: `361a7f384ce4be88d95a2d19a6ec653ed2a416ee5b6e7a261058fa3160b64500`.
- Author result SHA256: `7b9a975bfb8213b90b06274721627030002ce9b1bcf39a0b2fa2085e2de0e836`.
- Public independent review SHA256: `fd358312450ff6a2dedc9becb7b56ebbab9860618304f93d0bd2d952fb253a01`.

The author proof, checker, result, source manifest, and four originals are
unchanged. The independent mathematical review and arithmetic are unchanged;
only references to a superseded packaging inventory were omitted from its
public copy. Publication-only inventories bind exactly the included files.

Hashes authenticate bytes, not the truth of transitive premises. The written
proof supplies the geometric argument; the arithmetic is not proof-assistant
certification. No actual coefficients, parameters, jets, matrices, instance
ranks, historical candidate reruns, or local-model experiments are evaluated.
