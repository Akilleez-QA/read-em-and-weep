# Independent whole-proof review

Verdict: PASS for the final bytes identified below. This is a mathematical review with bounded abstract verification, not formal proof-assistant verification. The four cited published results are treated as authenticated inputs; their role and the deductions from them were checked against their exact local copies.

## Reviewed final files

SHA-256:

- PROOF.md: `351d8906b3401365d61731c8db439488abc05e5871d8111c120289822aa961e7`
- INPUTS.json: `b974c8cbad5659f9f9c7e9a57ea14bccbdd95bf2bf218df3d7ff19d1bb2f401a`
- verify.py: `60a7e390aae3d589c5fda69529409fab162269f487ae923df32182ff2a2c391b`
- REPRODUCE.md: `3feba6c354bf3364dc9ee5ffb051d168d978bf8868fe108bd1ea0e6366b91d5f`

## Mathematical checks

1. FOURTH proves nonvanishing of the actual plane commutator, not merely existence of an allowed representation channel. Its sole possible channel is the unique D in A tensor A. The family map therefore lies in the one-dimensional space Hom_G(A,D tensor Sym2 W) with a nonzero scalar. Comparison with the actual coefficient family from SQUARE is legitimate. Dualizing its sequence and twisting by O(2) gives precisely A O into D O(2), with quotient W O(5); the dual and parameter twists are correct.

2. The universal negative-direction normal line has conormal O_R(-1) tensor O_T(1). Hence normal degree k contributes B_R(2-k) tensor O_T(k), with inversion sign (-1)^k. The actual third-neighborhood positive extension uses degrees zero and two, and its boundary is the authenticated commutator. The negative part is exactly the degree-one layer. The stated H0 and H2 vanishings, positive and negative R1 bundles, and rank/degree totals follow from the actual exact sequence. Constant fiber ranks at this stage justify ordinary cohomology and base change.

3. The injective actual first cup kills every nonzero section at the passage from 2R to 3R. Thereafter each ordinary-thickening kernel has zero H0, so restriction is injective at every step. This proves the claimed uniform vanishing for every direction and every m at least three, not only invariant vanishing or generic-direction vanishing.

4. The W O(5) term is the maximal-slope Harder–Narasimhan subbundle. The ambiguity in its equivariant complement is Hom_G(V plus P,W tensor Sym3 W), which is zero because W tensor Sym3 W is A plus D. Thus the intrinsic equivariant decomposition is justified without claiming scalar-normalized identifications or uniqueness of an arbitrary nonequivariant complement.

5. The even steps 3R to 5R and 5R to 7R add exactly degrees four and six. Their cohomology extensions split as ordinary bundles because the relevant O(d) have d equal to 2,-1,4,2,1, all with zero H1 on the parameter line. Averaging gives equivariant splittings. This does not split the original sheaf extensions or formal transitions. The resulting source has rank 30 and degree 120.

6. The even step 7R to 9R adds B_R(-6) tensor O(8), whose sole cohomology is H2 equal to Sym2 D tensor O(8). The associated derived triangle produces the actual boundary from the displayed rank-30 source to the rank-15 target in degrees one and two. The finite normal family is flat over the parameter line, so derived base change identifies fiber kernels and cokernels with actual neighborhood cohomology. No constant-rank claim or unsupported underived base-change assertion for this final boundary is needed.

## Reproduction and scope checks

Both `python3 verify.py` and `python3 -O verify.py` were run successfully. The verifier's explicit checks remain enabled in optimized mode. Its arithmetic is limited to nine fixed abstract character classes, ordinary Ext degree inequalities, rank/degree totals, and authentication of four Git blobs. The reconstruction instructions preserve the immutable input bytes and describe the verifier's geometric limitations accurately.

No selected actual HM coefficients, points, jets, derivatives, matrices, instance ranks, or scans were evaluated in this review. No rank of the final boundary, opposite-bundle row, top polar map, or vertex scalar is inferred. No external write was performed.
