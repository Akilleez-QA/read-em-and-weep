# Linear presentation and quadratic transversality

[PROOF.md](PROOF.md) proves that a finite-length, linearly presented graded module with two-dimensional degree-three piece has a quadratic failure locus of codimension at least two. Its input is an elementary exclusion of rank-at-most-two vector cubics, including both secant and tangent binary normal forms.

At a rank-one quadratic, some maximal minor has nonzero differential. Combining this with the good-square theorem gives an existential choice of nonisotropic square direction for which the actual translated-root family has endpoint quotient killed by the local parameter. The relative coefficient-cohomology consequence is nonlifting of any nonzero exceptional closed-fiber class already over the dual numbers.

Dependencies: PR167 (linear presentation), PR440/442 (endpoint comparison), PR443 (good squares and actual curve), and PR445 (relative duality and thickening transition maps), all at the exact commits linked in the proof. This slice is stacked on PR445.

The original fixed quotient remains unevaluated. The result is not a module-lifting or quantization obstruction. Proof review is mathematical text review, not formal verification. No selected actual HM/source-instance evaluation or numerical computation is used.
