# Independent review: residual-large positive Smith criterion

Verdict: PASS, with alpha nonvanishing explicitly conditional and scope limited to the original positive component.

## Frozen artifact hashes (SHA256)

- PROOF.md: 07fba65d999d06ff9e96f761975a9980e2b1f5934e24ea0edcc1ae6b05241ffa
- verify.py: 030095fbeed8fb87de3c4697bd430523d192e89ce671c4d0a16b57c57dd9e68e
- INPUTS.json: 5bb8152d2b9d0ad9a8942da1aaebad14250894c2d48c905d8856f50e0935203a
- RESULT.json: 7bfce63dd9f06b695d2d2ae9e6d3fc594536b73833623809f672cd7a75020d6e

## Authentication and replay

All eight complete files were freshly fetched at the immutable manifest commits. Contents matched retained bytes and returned Git blob hashes matched the manifest:

- PR1019: bf63c14f76933d59fa7e3ac61aecb3366ac1b442
- Original first vanishing: fe4410bbba05060545b22ac6bc80aac8e7c62ce4
- Original third vanishing: 7c09fe95015d7c8d932b3a27be302ca09888112d
- PR1025: d036adcf5bc2bfc53e07cd752ff180c5993251f7
- PR1044: 516408c24d036634f0e03e29350815c2442d2880
- PR1046: 018672738b8f206aef51ae163053ecad3400075a
- PR1077: 12e4cbd71fd9f2d9320c310a533c2f30fd38bd8b
- PR1097: 990fa9adedade88b951b805aed94e6a395a7d71b

Independent normal and optimized executions passed all 57 checks. The outputs were byte-identical to each other and RESULT.json. The verifier uses explicit exceptions, so its checks remain active under optimization. Its matrices carry independent formal coefficients and do not evaluate the actual pencil.

## Mathematical and hypothesis audit

1. The old endpoint-nine line constraint and its nonvanishing theorem are not imported. PR1097 instead gives the residual-large line constraint, and alpha nonzero remains a separate condition. The invariant-cone first vanishing, actual second-symbol formula and full original third vanishing have their own retained actual-source premises and do not require endpoint nine.
2. The generic second symbol has rank three, with exactly the six C5 support points as its rank-drop set. The retained third theorem includes the specialized extra A-kernel, although the present Smith profile is only asserted outside E. The original surviving generic source is precisely D and the surviving target is one-dimensional.
3. PR1025 compares the corrected original fourth with -sL and gives equivalence of its identically vanishing with R=0. The torsion-free target prevents a nonzero global gate from being generically zero. PR1044 supplies the nonzero R1 nonic scheme, and PR1046 transports its ideal sheaf to the composed original-fourth row, including the C3 axes where L fails to be onto.
4. Outside E, Sigma is excluded and the determinant embedding identifies the actual target fiber with a line. Thus the component scheme really detects the fourth rank there. Length46 and support28 count six length-four ideals, ten reduced axes and twelve reduced conic points; no equality of raw differently graded ideals is claimed.
5. The formal reduction splits 33 units and three t-squared pivots. After these, the third coefficient vanishes and the fourth coefficient is the corrected Schur expression E-CB, not E. A nonzero fourth row gives one t-fourth pivot and four free source columns. This gives maximal-minor ideal (t^10), cokernel length10 and the stated determinantal orders.
6. Conversely a maximal-minor ideal (t^10) requires a nonzero fourth row once the previous pivots and vanishing pages are fixed, hence alpha nonzero. If alpha=0, the residual row has order at least five, so every maximal minor has order at least eleven or is zero. If a finite last exponent e occurs, some original maximal minor is a nonzero polynomial of degree at most37, forcing 6+e at most37 and hence e at most31. This does not assert that any such later exponent occurs, and does not confuse fourth vanishing with failure of Laurent-series full row rank.

The packet asserts no exceptional-direction Smith profile, no conclusion for the nonzero-N0 mechanism, no full-adjoint invertibility and no completed original repair. No actual coefficient, point, direction, jet, source matrix or instance rank was evaluated, and no public write was performed.
