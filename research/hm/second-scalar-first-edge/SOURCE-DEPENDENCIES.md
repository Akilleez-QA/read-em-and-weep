# Public replay and external source dependencies

## What a clean copy reproduces

All supplied coefficient data, the full 207-row selector, exact integer
kernels, the reduced-model chain-map/merged-row identities, actual-model right
prefactor ties and contractions, the partial sum 8655/16 and the stated counts
are reproduced by the commands in README.md. The package does not import
another scalar map's evaluator or require another package.

## Recorded source chain, not reproduced end to end here

1. The full geometric interpretation of the normalized rational MODEL,
   whole-matrix contraction side conditions, frame conventions and scalar
   descent/comparison proof for the new map. The small reduced MODEL and the
   specific new-map/merged-row/prefactor checks are included; the broader
   all-entry pole and legal-line comparison chain remains external.
2. The unchanged unsigned carrier-tail (2,3,4), exact integer feature moments
   and left prefactor, combined with the **new column-5 right prefactor**.
3. The fresh A_minus numerator and separate all-four-axis support gates
   47/215/454. The original factor-48 diagnostic was unsuccessful; the
   corrected support gate, not that failed attempt, justifies the new window.
4. The normalized axis-0 source, safe reversed pair-(0,1) circuit and exact
   integer clearing of 141,388 weights. The recorded root denominator is 64;
   the source sign and orientation sign are distinct.
5. The exact evaluation producing all 203 retained quotient terms, followed
   by independent reconstruction of its terminal product using both tuple
   integer arithmetic and Fractions. The recorded independent terminal audit
   compares all quotient coefficients and 207 selected rows, but does not
   independently reevaluate every source node.

Original artifact hashes and byte sizes for these records are preserved in
`provenance.json`. The recorded final manifest has 265 pins and 20 historical
attempt mappings. Neither that manifest, its large source archive nor the
checkpoint files are distributed here. Their digests identify the recorded
evidence and are not evidence that the reader has received or verified it.

The source/model canonical digest is distinct from a JSON file's byte digest.
Likewise, sanitized public exports have their own hashes in `manifest.json`.
Both `model.json` and `right-prefactor.json` are included byte-identically to
their origins. The former's canonical hash is also checked independently of
its original serialization hash.

No verified public link for the complete **new-map** source regeneration or
terminal reconstruction chain is supplied by this package. Those are explicit
external dependencies, not an implicit claim that a different map's published
source pipeline proves this result. Small future regenerators could discharge
them without publishing raw large DAGs or checkpoints; they are outside this
package's claim and reproduction commands.

## Relationship to existing public foundations

- Exact-arithmetic background: [PR #32](https://github.com/Akilleez-QA/read-em-and-weep/pull/32),
  commit `338bec6395f89c9a8f2e14bf98d025c9c2f4c7a9`.
- Original scalar mathematical package: [PR #34](https://github.com/Akilleez-QA/read-em-and-weep/pull/34),
  commit `a100f4e0be453d6e182320b792359f8a04e32b4d`.
- Original-map geometric source package: [PR #40](https://github.com/Akilleez-QA/read-em-and-weep/pull/40),
  commit `dc60a859a0157b1d2d1b57b37324509abc22c600`.

These references identify related foundations. This package does not claim
their source bounds or scalar-specific conclusions automatically apply to
L_minus. MATHEMATICS.md states the new-map identities and all-entry transfer
assumptions explicitly. The old factor-48 bound, old quotient window and old
structural-zero/relationship lists are not used by the checker.
