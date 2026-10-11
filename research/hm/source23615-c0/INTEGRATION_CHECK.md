# Additive integration check for C0 version 1

The original C0 files and manifest remain unchanged. This supplement records a direct structural check of the already pinned graph, without evaluating source coefficients or reading target output values.

The graph's paired originalSumIdentifiers and tag/sum nodes map module128045 to source22866, module128874 to source22874, and module133174 to source23615. The two weighted-sum terms at module133174 are:

1. Coefficient 1; residual module133169; no outside weight. Flattening only its product nodes gives source factors [0,1,15,37,23117].
2. Coefficient 2; residual module133173; outside factors [(9,1),(13,1)]. Flattening only its product nodes gives source factors [10,10,14,14,23543].

Thus the receiving module's exact integrated component is

C_r(s_0 s_1 s_15 s_37 s_23117)(y)
 + 2 s_9(y) s_13(y) C_r(s_10^2 s_14^2 s_23543)(y).

By the cube-weight identity proved in C0, this equals

C_r(s_0 s_1 s_15 s_37 s_23117 + 2 s_9^3 s_10^2 s_13^3 s_14^2 s_23543)(y)
 = C_r(s_23615)(y).

This checks the prescribed SUM against its receiving module before any result exists. It proves structural integration compatibility, not a candidate's coefficient correctness. It neither verifies an unlisted transformed graph nor discharges the final independent source oracle.

At final integration, compare the exact typed mathematical-input manifest used to compute the candidate with the one required by the receiving construction: field, ordered coordinates, tags and normalized source, target, residue, seed definitions, and any proved transformation. Verify actual source mapping and the displayed SUM identity again if the receiving construction changes. Record execution/continuation dependencies separately. A digest of an operator set must not be compared for equality to a digest of a coefficient artifact: these hash different typed objects. Equal input-manifest digests show the same input contract; an output digest identifies bytes of the resulting output. Both are necessary provenance records and neither replaces coefficient equality.

This contract is specific to F3. A cross-check at a prime different from 3 requires a separately valid source specialization, denominator checks, and field-appropriate identities. In particular H(x)^3=H(x^3) and the cube-weight Cartier pullout used here must not be imported unchanged into a different characteristic. No such cross-check has been performed here.
