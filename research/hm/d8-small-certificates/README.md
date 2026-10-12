# Small D8 review certificates for the pinned HM perfect complex

This package contains two independent, reproducible mathematical certificates.
They share the pinned four-term line complex, but establish different facts.

## Results and limits

1. **P4 twists and characteristic three.** [The proof](p4/Perfect-Complex-D8-F3.md)
   and [checker](p4/check_hm_p4_all_twists.js) compute the four twists of End(L).
   The new twist -2 connecting map is 80 by 10, has 50 nonzero entries,
   and has a 10 by 10 identity minor. The ordinary 50 by 80 differential
   has rank 50. Together with the direct D8-equivariant geometric splitting,
   this proves that the epsilon-isotypic Ext2 full-sign sector has dimension
   32 over F3 for the pinned **perfect complex**. It does not establish that
   the reduced complex resolves the intended HM bundle, or identify, evaluate,
   or prove naturality/choice independence of an obstruction in characteristic 3.
2. **One actual transferred generator.** [The action package](generator/README.md)
   implements T_a = P rho((12)) I in the existing ordered full-sign model.
   Its nonzero correction blocks have 568 and 1664 entries in degrees 2 and 3.
   Exact exhaustive tests check dT_a = T_a d and T_a squared = 1 on all finite
   cochains, alongside differential-square and source-regression checks.
   This is one generator, not the full D8 action, a completed epsilon projector,
   a complete detector, or a decision about the geometric obstruction.

The dimension argument does not use a naive harmonic permutation or a claim
that integral transferred generators alone form a strict group action.
The one-generator computation does not supply a characteristic-zero to F3
cohomology-dimension transfer.

## Reproduce

Node.js 18 or newer is sufficient; publication checks used Node v24.19.0.
No third-party package, installation, network access, or unpublished data is needed.
From the repository root:

```sh
node research/hm/d8-small-certificates/p4/check_hm_p4_all_twists.js
node research/hm/d8-small-certificates/generator/verify-generator.js
node research/hm/d8-small-certificates/generator/full-sign-boundary-oracle.js --self-test
node research/hm/d8-small-certificates/generator/generator-action.js --apply research/hm/d8-small-certificates/generator/sample-basis-column.input.json
```

The P4 output is saved in [p4/certificate.json](p4/certificate.json).
The action verifier regenerates [generator/certificate.json](generator/certificate.json)
and the optional generator-a-matrices.json in the generator directory.
The latter is deliberately omitted from the committed package because its full
contents are reproducibly generated and checked by the verifier. Its compact
serialization SHA-256 is recorded in the action certificate.
The rational CLI output is checked against
[the included sample](generator/sample-basis-column.output.json), which is a
synthetic basis vector and makes no cocycle or obstruction claim.

## Provenance and independent review

Source complex: [verify-hm-ext.js at add03476](https://github.com/Akilleez-QA/read-em-and-weep/blob/add03476d9055aa00e1e00778eea6332cf8e01cc/research/hm/verify-hm-ext.js).
The action bundles unchanged, hash-checked source dependencies from the
[finite model at a100f4e0](https://github.com/Akilleez-QA/read-em-and-weep/tree/a100f4e0be453d6e182320b792359f8a04e32b4d/research/hm/current-scalar-proof/finite-model).
File-byte digests are listed in SHA256SUMS; source pins are also enforced at runtime.

The two detailed notes state the sign conventions and review targets. In the P4
certificate the remaining independent audit is the small Cech zigzag, identity
minor, and geometric D8 splitting argument. In the action package it is the
P-rho-I expansion, quotient/pruning argument, swap sign, and exhaustive basis
indexing. This package supplies review inputs without modifying another
construction or expanding the obstruction claim.
