# Reduced all-mask source generator bridge

This focused package bridges the original public primitive model to the exact
unsigned carrier (2,3,4) coefficient DAG used by the current scalar computation.
It regenerates the DAG from small source code, so the generated 3.5 MB DAG need
not be committed.

## Reproduce

Python 3.10+ and Node.js 18+; standard libraries only. From this directory:

```sh
python3 verify_bridge.py
```

The verifier checks source-file hashes, proves 1,710 primitive rational-function
identities by integer polynomial cross multiplication, regenerates the reduced
model, and regenerates the complete unsigned carrier coefficient DAG. It checks
the exact bytes, node count, graph ordering and coefficient-index structure.
All generated data are temporary; the package itself is not modified. Run
without Python `-O`. Each Node subprocess has a 1,536 MiB old-space limit and a
300-second timeout; those are resource guards, not numerical truncations.

To retain the generated files yourself:

```sh
node public_reduce_hm_primitive_factors.js --emit-model > reduced-model.json
node public_generate_hm_mask_coefficients_reduced.js --carriers '[2,3,4]' --emit-dag > carriers-234.json
```

Use new output filenames to avoid overwriting existing results.

## Pinned results

- Reduced model: SHA-256
  `635bb12d9986e0dcada161d4173c773c4f134b9225354a3bc74267840ca19926`.
- Carrier (2,3,4) DAG: 3,533,626 bytes and 178,251 nodes; SHA-256
  `31cd62eb3062801ca19073464c276fbe016fa4024fbcdcf48d3893358e3fcc18`.
- Original model's canonical compact JSON plus newline: SHA-256
  `9e808b52f263679a548656fa57bcb3a621f5264c20873621208b06acf4003614`.

Fresh execution reproduced both output hashes exactly. No previously generated
DAG is read by the verifier.

## Construction and provenance

The original MODEL is already public in
[the historical cochain generator](https://github.com/Akilleez-QA/read-em-and-weep/blob/5d9ddb2a1e85b3bd6b43111e25e97cfe59d8cc86/research/hm/generate-hm-second-order-dag.js),
introduced by PR #31. The reducer embeds that same original model. It cancels
common polynomial factors from the frame/contraction numerators and their
denominators, verifying every entry by cross multiplication. The reduced model
therefore represents the same rational functions wherever their original
expressions are defined; this assertion does not supply an extra regularity
claim across removed divisors.

`generate-hm-mask-coefficients-original.js` and the reduced generator have
identical source text outside their MODEL declarations. Both construct the
normalized mixed residual and extract its exact group-multilinear line-mask
coefficients. The group-degree check raises if a coordinate group exceeds one.
The reduced generator is required for the pinned DAG bytes. Running the
original generator is not promised to produce the same graph serialization.

`expected.json` records the unchanged script hashes and output pins. The public
filename prefix is historical naming, not a claim that the files were public
before this PR.

## What remains downstream

This is the unsigned row residual source. It does not yet construct or verify
the final scalar numerator. The remaining source-to-result chain requires:

1. Exact inverse-seed and denominator factorizations, scalar prefactors and
   weighted-mask moments.
2. The tagged rational constructor combining all mask choices and applying
   exactly one explicit J2 minus, producing numerator SHA-256
   `0254c93650e6ca6c1e9cbbb01810704eede98d10d0b75229fcff5d8fa2123e66`.
3. Four leading-axis windows, normalized circuits, twelve secondary reverse-jet
   pairs, per-node denominator clearing, and independent source/support gates.
4. Portable exact quotient evaluation and independent terminal reconstruction.

The current supplied-quotient replay is [PR #33](https://github.com/Akilleez-QA/read-em-and-weep/pull/33),
the scalar proof checks are [PR #34](https://github.com/Akilleez-QA/read-em-and-weep/pull/34),
and exact integer arithmetic is [PR #32](https://github.com/Akilleez-QA/read-em-and-weep/pull/32).
Their scope boundaries remain in force. No scalar coordinate is evaluated here,
and no full-obstruction vanishing or theorem repair is claimed.
