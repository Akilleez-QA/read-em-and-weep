# Attribution and reuse boundaries

`examples/LogConcaveCore.lean` contains the `log_concave_core` lemma from:

- Google DeepMind, **AlphaProof Nexus Results**
- Upstream repository: https://github.com/google-deepmind/alphaproof-nexus-results
- Immutable commit: `0647711a71183c1ea492ad60860776617ce1ea88`
- Original file and lines: [hilbert_functions_5.lean, 504–516](https://github.com/google-deepmind/alphaproof-nexus-results/blob/0647711a71183c1ea492ad60860776617ce1ea88/APNOutputs/AICollaborator/AlgebraicGeometry/hilbert_functions_5.lean#L504-L516)
- Copyright 2026 Google LLC
- License: Apache License, Version 2.0; complete text is retained in
  `licenses/Apache-2.0.txt` and the original file header is retained in the example.

The proof body is unchanged. The local example adds `import Mathlib`, an
explanatory comment and the `AlphaProofNexusExample` namespace, and omits the
other declarations and source-wide options. These are local modifications,
not changes endorsed by Google DeepMind. Byte pins and the exact excerpt
range are in `example-origin.json`.

The upstream [README license section](https://github.com/google-deepmind/alphaproof-nexus-results/blob/0647711a71183c1ea492ad60860776617ce1ea88/README.md)
identifies the software as Apache-2.0 and other materials as CC-BY-4.0, subject
to third-party exceptions. It identifies third-party sources including OEIS,
Erdős Problems, Gergely Bérczi and Mario Krenn; OEIS-derived material has
CC-BY-SA-4.0 requirements. Refer to those upstream notices before copying,
modifying or redistributing additional files. This integration copies no
OEIS entries, Erdős problem text, paper text or screenshots. The complete
inventory is metadata and does not grant a license over the linked corpus.

The original validation scripts and integration documentation in this directory
are also provided under Apache-2.0. This directory's license declaration does
not change licenses elsewhere in the fork or in any fetched dependencies.

Scientific reference: the [AlphaProof Nexus paper, version 2](https://arxiv.org/html/2605.22763v2).
Use that corrected version when describing the pure O-sequence result.
