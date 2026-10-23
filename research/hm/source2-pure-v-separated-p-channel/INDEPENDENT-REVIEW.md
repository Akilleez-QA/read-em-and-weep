# Independent review: separated degree-ten P channel

## Verdict

**PASS**, under the stated actual-source and conditional pure-V homotopy hypotheses. Nonzero projection of the canonical P_h into the genuinely separated degree-ten block forces all three quadratic quotient channels, endpoint dimension 16, and the claimed negative-module direct sum. The argument neither evaluates that projection nor selects the branch, and it does not assert a Q-stable splitting.

Reviewed SHA256:

- `PROOF.md`: `05452a2c52970e36e12914257a6b8666c8fe0faeaa8cd7b0930d434495a192df`
- `verify.py`: `d48b60f9b4f1dd989dbe35bebd9b2509b8a324f6ecb9956d4552c5029d5654a4`

## Authenticated inputs

All four originals were freshly retrieved at their exact immutable commit and repository path in `INPUTS.json`. Retrieved bytes match the retained bytes, and independently computed SHA256 and Git blob hashes match the manifest:

| Input | Commit | Git blob |
|---|---|---|
| PR790 | `af0e03d26da5e47d18ae732291aca46f4d448dc5` | `0641ffadf54324d5520aec89767658e938815223` |
| PR792 | `2f01f18960ce56b8b2a0c1260c277de3c5f916bf` | `76bee93507d1a2d0840926d4e4e27edadfebb7d7` |
| Universal symbols | `6c724c3b74e2ae4d6992d8c7b99b41c0715d69c0` | `0ff4a2fd717842d8df9cf3ce3e3d29fd189bcd6e` |
| PR1054 | `8732cb65fe0e72da59e785f3f85ad197a7092e6c` | `64e6bf9f1bf46440700ebab7c90a18f9d8155fd8` |

Authentication covers these retained originals, not a new recursive authentication of every historical dependency. The historical universal-symbol script was not executed; only its literal P8 matrix was extracted for the independent calculation.

## Actual-map and normalization audit

PR790's splitting is induced by an actual constant equivariant separation of the evaluation sequence. Its reconstruction identifies both fixed negative arrows simultaneously with the original module arrows. Thus the resulting projectors commute with the original first and second multiplications, and consequently with their quadratic composites. This is stronger than a bundle splitting or a character decomposition.

PR792 constructs the entire pure-V image through the residual evaluation sequence, including the injection into its last cohomology space. Therefore I2, I3, and I4 lie in the residual spaces for the separation in use, and the separated projector annihilates I4. The conclusion is not obtained by confusing the two P constituents in an abstract endpoint character.

For the canonical degree-ten block, taking sections of the actual evaluation sequence gives the quotient `(Sym²W⊗Sym⁸W)/Sym¹⁰W`. The degree-ten map is its canonical polarization inclusion, up to an irrelevant common nonzero scalar; the fixed symplectic convention identifies the negative variables with the section variables. Iterated multiplication sends a generator p and quadratic a to the class of their tensor. No unrelated identifications of the three module degrees are introduced.

The apolar transpose `E8=G8⁻¹P8ᵀ` is correctly interpreted as an inclusion of the dual quotient representation. Invariance of G8 and the pinned quotient intertwining identities make its image invariant. Self-duality and multiplicity one identify this image with the unique P constituent. An ordinary transpose without G8 would not justify this conclusion. The verifier checks all four pinned generators and the nondegenerate induced pairing.

The transvectant map has the stated degrees and tensor order. Its exact identities `C Delta=0`, `Mul Delta=45 Id`, and rank 16 identify its kernel with precisely the 11-dimensional polarization image. The displayed nonzero 12-minor then proves the required injectivity over the full universal tensor domain, without a selected quadratic direction.

## Independent intersection certificate

A second exact calculation established injectivity without using either the production transvectant map or its displayed 12-minor:

1. Extract the fixed P8 matrix from the retained universal input and form G8 and E8.
2. Compute a basis K of `ker P8`. Then `B=KᵀG8` has rank five, annihilates E8, and hence has kernel exactly `im E8`.
3. Reconstruct the full polarization matrix by expanding each degree-ten monomial at `(x+X,y+Y)` and extracting terms of auxiliary degree two. This independently obtains the tensor inclusion in the stated ordering.
4. Compute `J=diag(B,B,B) Delta`. Exact arithmetic over `Q(sqrt(5))` gives rank 11 for this 15-by-11 matrix.

Thus no nonzero polarized degree-ten form lies in `Sym²W⊗im E8`. This is precisely the zero-intersection criterion for theta to be injective, and independently confirms the central universal certificate.

## Transport and scope

A nonzero equivariant restriction of e2 to P_h is an isomorphism onto the unique P8. Projector naturality therefore makes the actual quadratic composite into N0,4 injective. Since e4 kills I4, the same quadratic map is injective modulo I4. The already proved surjection onto F4/I4 is consequently an isomorphism. In particular the actual quadratic P image is disjoint from I4, not just abstractly isomorphic to a complement.

Together with PR1054's actual first-arrow injectivity and disjointness, this identifies the P-generated three-space system with the truncated free module through its multiplication maps. Associativity supplies the arrows, and the disjoint intersections in each degree give the direct sum with I. The result concerns only the fixed negative multiplication variables. Q maps P_h isomorphically to I4 across these summands, so no Q-equivariant decomposition, cancellation, or Bockstein equivalence follows.

The contrapositive for endpoint dimension below 16 is valid. Neither its converse nor realizability of either projection branch is asserted.

## Reproduction

Both `python verify.py` and `python -O verify.py` passed all 25 checks with byte-identical output. The independent polarization-intersection calculation above also passed. These are universal representation calculations, not evaluations of actual source coefficients or source-instance ranks. The projector transport and actual module conclusions are written mathematical arguments, not claims of proof-assistant certification.
