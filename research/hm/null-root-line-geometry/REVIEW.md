# Independent one-curve review

Verdict: the geometric arrow is sound over characteristic zero, with the specified divisor-sheaf and transition conventions. The claim is local root line → induced old connection → transported difference → contraction −k q/2. It does not certify a physical calculation or the entire source pipeline.

The original 12-identity checker passes normally. Its original optimized invocation also prints PASS, but that is not evidence: its assertions disappear under Python optimization. This bundle replaces assertions with explicit RuntimeError checks. Both normal and optimized runs pass 16 symbolic identities and reject 9 wrong variants; injected reversed-sign runs fail in both modes. Logs are supplied.

The proof now explicitly handles P0, P1, P−1 and O, distinguishes rational-function poles from line-section regularity, distinguishes differential forms from their dx coefficients and evaluations, and makes the ambient external-product premise conditional. It also clarifies that the pinned shorthand −z partial_t only describes the vector field on t-functions; the whole derivation has the additional (3t²−1)/2 partial_z component.

Source provenance: the three documentation snapshots were read from previously fetched copies at the stated immutable repository commit. Their Git blob SHA-1 values match recorded fetch metadata. SHA-256 pins are included. The raw-engine excerpt has a full-snapshot SHA-256 and exact source line ranges, but no independently established repository commit. No source document, raw-engine excerpt, or production module was executed or imported. Full documentation files are inert reference material and contain broader claims not audited here.

Remaining premises: identification of ambient Theta with the sum of four origin divisors; external-product/tensor-connection conventions; agreement of source scalar leaves with actual source semantics; primitive model identity; derivative and jet engines; common-frame matrix transport and source-generator equality; residual/HPL computations and the aggregate theorem. The proof derives the product scalar formula only after the first two premises are supplied.

No external publication was performed.
