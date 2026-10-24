# Reproduction and precise partial-theorem boundary

This packet is stacked on `null/rankfour-reverse-adjacent` at
`ce63dba8623675e6fa5760917873b29e39a62ce3` (#1178). All additions are under
`research/hm/rankfour-backward-cubic-image`.

## Conditional theorem, not a profile exclusion

In the actual ordered maximal generic-rank-four plateau `(3,1)`, restrict
the dual cubic derivative to any equivariant copy of T6 in H0(Q*(3)).
Its actual image has generic rank one, two, or three, never four. The
rank-one case requires image O(9) and necessary source D.

This treats every chosen copy separately. It assumes neither a canonical
T6 copy nor injectivity or saturation of its evaluation into Q*(3).
The actual rank-17 E and rank-13 Q* remain distinct. All four source labels
are retained. Global unramifiedness is not assumed: the complete necessary
31-row endpoint/defect ledger contains 24 positive-defect rows.

The rank-four image domain is forced by generation, target Hom spaces,
and a section/saturation bound. Its four survivors are rejected by exact
Euler characters, a multiplicity-one intertwiner, ordinary Hom vanishing,
and two intrinsically derived endpoints whose entire derivative Hom spaces
vanish. Only the last image subcase forces the plateau defects to vanish.

Whole `(3,1)` remains open. The coarse necessary overlist remains at 23 bins,
or 92 across all four source labels. No other profile is excluded here,
and no generic SF rank-at-least-five, square surjectivity, full-adjoint
invertibility, or original repair follows. Remaining image ranks one through
three are necessary alternatives, not claims of geometric realizability.

## Reproduce

From the repository root:

```sh
python3 research/hm/rankfour-backward-cubic-image/verify.py
python3 -O research/hm/rankfour-backward-cubic-image/verify.py
python3 research/hm/rankfour-backward-cubic-image/independent/verify.py
python3 research/hm/rankfour-backward-cubic-image/independent/test_controls.py
python3 research/hm/rankfour-backward-cubic-image/independent/check_package.py
python3 research/hm/rankfour-backward-cubic-image/verify_publication.py
```

The author verifier reports 12,643 checks. The independent implementation
reports 603 checks and rejects thirteen executable mutations. It uses exact
conjugacy-class arithmetic and intrinsic partitions without importing author
code. Complete agreement covers all 31 ledger rows, 46 endpoint shapes, two
forced endpoints, and four full-rank image shapes. The reported intertwiner
multiplicity is one; the publication verifier guards that output explicitly.

The portable publication verifier authenticates the included bytes, checks
all fourteen reviewed author deliverables against the published copies,
executes six explicit normal/optimized replays including unrelated working
directories, and reruns the independent mutation and package cross-checks.
Its exact output is `PUBLICATION-CONTROLS.json`; the two independent wrappers
match `CONTROLS.json` and `PACKAGE-CHECK.json`. All programs use only the
Python standard library. Complete public inputs are repeated to make each
runnable package self-contained.

## Frozen identities and boundaries

- Author proof SHA256: `0e291e31481530df3163ed6abc3d433a4e402c98e9258d3a329b05b51a2ea507`.
- Author checker SHA256: `6d4f66ca5ac1be539a09ef791775e782bc4cafba56dbf18131b0bb7586a21242`.
- Author result SHA256: `6ba21af4feb947a9bd90190478c8a5ff5ddfb43754b101e009eb10fd34a94a05`.
- Public independent review SHA256: `7f4cc562718242c1808b69ce70a8180f8d5cf67bfb1a17ac4a5d76bf8bfbd173`.

The author proof and mathematical artifacts are unchanged. The independent
review's mathematical content is unchanged; one authentication sentence was
adapted to the public-only inventory with the reviewer's acceptance.
Publication manifests bind exactly the included files by sizes, SHA256,
and Git blob identity. The author snapshot manifest has fourteen entries.

Five complete immutable public originals are retained, including the primary
four-source theorem and its explicit transitive hypotheses. Hashes identify
bytes rather than establish their truth. The written geometric proof and
retained premises are not replaced by arithmetic or proof-assistant claims.
No actual coefficients, parameters, jets, matrices, instance ranks, historical
enumeration reruns, or local-model experiments are evaluated.
