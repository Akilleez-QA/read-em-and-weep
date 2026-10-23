# Reproduction

Run python verify.py and python -O verify.py. The checker uses just the four fixed constituent multiplicities A,V,P,D; it does not construct or evaluate a multiplication matrix. It verifies the constituent bottleneck for the discarded idempotent type, equality of the two surviving block maxima with the imported actual image, and the consequent kernel/cokernel characters.

The universal proof in PROOF.md is essential. In particular the checker does not prove the original geometric q₀ theorem, the form of the negative-pencil algebra, actual compatibility, or the assertion that all radical shears have target eigenspaces with the stated characters.

The original theorem's rank33 is not a newly tested selected-instance rank. Its geometric result gives kernel A+D, image2V+3P+3D and cokernelP without coefficient selection. This package imports that immutable theorem and uses only its exact image character to rule out a compatibility branch.

If audit-inputs/manifest.json and the two exact UTF-8 original files are present, verify.py authenticates their Git blob IDs. Without those copies it checks the fixed character arithmetic only; source authentication then requires retrieving the two manifest commit/path pairs separately.

Expected result: TypeB has at most one V in its invariant-product image, contradicting the imported two V. The residual TypeF has image dimensions12 and21, kernelsD andA, and cokernelsP and0. The actual compatible algebra is scalar if χ_B≠0; when χ_B=0 it is C² exactly if both cross-block aggregate maps vanish.

No source is excluded, no frontier count changes, no actual model is produced, and no full-module lift is asserted.
