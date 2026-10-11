# C0: source 23615, residue 41 pre-output contract

This package publishes a mathematical target definition and formal integration identities for the complete residue-41 component of source 23615 over F3, with ordered coordinates (x1,x2,x3,x4), residue digits (2,1,1,1), and receiving module 133174.

It contains no target output coefficients, expected support size, nonzero verdict, or result hash. It neither authorizes execution nor certifies any current or future continuation, computed component, downstream stage, or complete solution.

## Distributed files and integrity

The six original contract files are preserved unchanged: C0.md, source-definition.json, manifest.json, SHA256SUMS, INTEGRATION_CHECK.md, and integration-check.json. This README is an additive publication-boundary note.

SHA256SUMS checks C0.md, source-definition.json, and manifest.json. The original manifest binds the first two contract files and identifies external dependencies. The integration-check.json supplement binds C0.md, manifest.json, the external graph, and INTEGRATION_CHECK.md. It does not extend SHA256SUMS to all seven published files. Immutable Git tree/blob identities bind the entire published package.

Original manifest SHA-256: 4ce8c55f5029a932b60048ebb911a7a094c05efa02324e4949d307425171e955.

## Explicit distribution and reproducibility boundary

None of the thirty dependency artifacts listed in manifest.json, nor its separately identified initial plan, is distributed in this package. Their basenames, sizes and SHA-256 digests identify external evidence only. Hash references cannot reconstruct those artifacts or independently establish their contents, execution, correctness, or availability.

source-definition.json contains all sixteen input tag polynomials and four displayed source-definition rows. It does not contain the complete transitive source DAG or all intermediate source definitions needed to regenerate source 23615. It does not include the accepted full-source seed maps or their independent receipts.

The mathematical identities in C0.md can be inspected directly. INTEGRATION_CHECK.md and integration-check.json record a structural comparison against the pinned external graph; this package does not distribute that graph or a standalone checker that reproduces the comparison. The manifest's verifiedAgainstAcceptedInitialPlan fields record prior checks, not checks independently reproducible from these seven files alone.

Accordingly this is a pinned pre-output contract and formal-identity review package, not a standalone source-regeneration or coefficient-verification package. Independent source evaluation would require the complete identified dependencies, validated seed data and separately reviewed implementation/provenance. A future candidate still requires the mandatory complete independent source oracle specified in C0.md, including coefficients absent from either map.

The contract and its integration identities are specific to characteristic three. No alternate-prime cross-check is claimed. No output or full-obstruction conclusion follows from this publication.
