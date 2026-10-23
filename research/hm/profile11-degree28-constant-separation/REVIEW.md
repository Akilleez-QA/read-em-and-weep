# Independent review: constant degree-twenty-eight separation

## Verdict and exact scope

**PASS**, conditional on the established actual-bundle inputs explicitly pinned in Section 1. The proof establishes actual constant separation of the degree-twenty-eight quotient block and the consequent simultaneous fixed-pencil summand. It does not exclude the label, assert realization by the fixed tensors, or test tensor idempotents.

This review is bound to these exact files:

- `PROOF.md`, SHA256 `b971cac17174bb609f096e3bb4a89a14d8f518bd01b1f0a99a9010b59ccfd1c3`.
- `verify.py`, SHA256 `789cde6bcb8b8b3a1713bb8f090633e42c362d74862b683b3d2b427c0c60d011`.

The earlier proof hash `2857e35d59a70ea86c998e0e936ff2c27f66c155672a2cbedd3d86e2c2267b0b` was also read in full. Its only change in the reviewed final version removes an unnecessary, uncited affirmative residual-feasibility sentence. No such assertion is needed for the theorem or this verdict.

This is an independent written mathematical audit, not proof-assistant certification. The review independently rederived the two shear nonvanishing arguments before receiving the finished proof, then checked the entire exact final argument and the pinned fixed-pencil reconstruction.

## Actual residual and first-polar splitting

The onto map from `O(-8)+W O(-9)` to `2 O(-8)` has precisely the form `(a,b e)` because the tail-to-line degree-one channel is unique. The Euler quotient `e` is everywhere onto. Hence the two constant columns must be independent, and the exact kernel is its tautological `O(-10)` line. In particular its quotient is genuinely `2 O(-8)`, not a generic quotient with possible torsion.

The internal derivative of this line is a nonzero constant column into `2 O(-10)`. Nonvanishing follows from the impossibility of a negative horizontal subbundle of a constant bundle in characteristic zero. The column is saturated, and saturation of the actual residual in the constant ambient bundle passes this to the full derivative image. Thus its first transform has rank two and degree minus eighteen. The universal first-polar map has the same rank and degree and generates that transform, giving the actual `W O(-9)` first-polar bundle.

The proof correctly makes this bundle the tail by a graph adjustment. Projection to the original tail is a scalar intertwiner; if zero, an embedded rank-two bundle would factor through the rank-one top. The scalar is therefore invertible. This justifies the new source splitting without incorrectly declaring it horizontal.

Crucially, absence of `P` from the chosen tail follows from its **actual first-polar origin** and absence of `P` in `Sym10 W`. The abstract space of maps `W O(-9)->P O` is not zero. The proof uses the valid first-polar reason, not that false abstract vanishing.

## The V-channel test

Full residual span and absence of `V` in `Sym8 W` force a nonzero projected degree-ten line system in `V`. Its three coefficient sections are independent by irreducibility. In characteristic zero their value-plus-first-derivative map is generically rank two: otherwise all ratios would be constant and the coefficient span would be one-dimensional.

Injectivity of `C->H0(O(28))` follows directly from `H0(F)=0`. Hence the quotient's V component is nonzero. The unique V constituent in degree twenty-eight is `f12` times the unique one in degree sixteen. The latter is basepoint-free: a nonempty invariant common divisor of degree at most sixteen must have degree twelve, leaving a V system in degree four, where no V occurs. The triviality of all one-dimensional characters makes the divisor factor invariant.

If the channel vanished, remove the nonzero scalar polynomial factor `f12`. The projected jet image would lie in the saturated rank-two kernel of `V O->O(16)`. That kernel has degree minus sixteen, whereas the raw jet image is isomorphic as a sheaf to `W O(-9)`, of degree minus eighteen. Their quotient would therefore have invariant torsion length two. Such a quotient cannot exist because every nonempty orbit has at least twelve points. This also independently checks the annihilator-degree sign used in the proof: the annihilator of a saturated rank-two subbundle of a constant rank-three bundle has the **same** degree as that subbundle.

Thus the V shear is zero on the top and nonzero on the tail, with no missing saturation assumption.

## The P-channel test and dual conventions

Use `P=W tensor Wp` and the symmetric self-duality given by the product of the two alternating forms. Contracting the nonzero P component `r8` of the top with the tautological vector gives a degree-nine Wp covariant. Since this representation is absent in degree nine, the Euler kernel sequence gives the unique factorization `r8(w)=w tensor a7(w)`. The degree-seven covariant has no common zero divisor, by the orbit bound, so its line in the constant Wp bundle is saturated.

For a convention-independent description of the other contraction, define `c29` by

    q_P(w)(w tensor v) = epsilon_Wp(c29(w),v).

The sequence twisted by one has acyclic kernel `F(1)=(P+2D)O(-1)`. Its global multiplication map is therefore an actual isomorphism, not just a character equality. The unique Wp constituent of `C tensor H0(O(1))` comes from `P tensor H0(O(1))`; its image is precisely this contraction, up to a nonzero scalar or the harmless alternating-form sign. Thus `c29` is nonzero.

Pairing with the top now gives `epsilon_Wp(c29,a7)`. Its vanishing would force the degree-twenty-nine line map to factor globally through the saturated degree-seven line. The factor has degree twenty-two. Uniqueness of the factorization makes it equivariant, hence invariant; there is no invariant of that degree. This proves the P shear is nonzero on the top. In fact it is also zero on the chosen first-polar tail, although only independence is needed.

The Hom dimensions are both one. These nonvanishing results therefore make the restriction of constant shears surjective onto the entire two-dimensional gluing space. The final shear is an actual equivariant constant automorphism, fixes C, and induces the identity on the constant quotient. Taking preimages of the zero graph genuinely gives the claimed constant direct sum and preserves the original connection.

## Fixed-pencil reconstruction

The full file at the following immutable source was fetched through the read-only GitHub connector and Section 6 was inspected directly:

https://github.com/Akilleez-QA/read-em-and-weep/blob/af0e03d26da5e47d18ae732291aca46f4d448dc5/research/hm/source2-first-constant-block/PROOF.md

Returned Git blob: `0641ffadf54324d5520aec89767658e938815223`. The available local dependency has this same Git blob and SHA256 `0a05b3c947b159e86e332307ebf7e46bfbfce1f12947a6472842d8c133bb6fa4`.

That section's reconstruction applies to the general actual quotient presentation; it does not depend on its source2-specific splitting conclusions. The formal homogeneous-variable formulas recover both multiplication pencils simultaneously, with the same identification of the negative two-space and compatible boundary conventions. Direct sums of constant inclusions induce direct sums of these cohomology spaces and maps. Applying this to the newly separated block gives exactly `Sym26 W`, `Sym27 W`, and `H1(F)=P+2D`, with the second pencil retaining the actual quotient `Sym28 W/C`. Thus the claimed fixed-tensor summand is stronger than, and is not confused with, a representation-only decomposition.

## Bounded verification and restrictions

The supplied verifier was read and executed successfully. Independently, the declared symmetric-power, multiplicity, ambient, and multiplication identities were checked against the existing exact character-table helper using rational arithmetic in `Q(sqrt(5))`, rather than merely repeating the verifier's McKay recurrence. In particular `Sym16 W=V+P+2D`, the V multiplicities in degrees sixteen and twenty-eight are one, the two gluing Hom dimensions are one, and the summand dimensions are `(27,28,14)` with complement `(14,26,23)`.

Only those declared, small universal identities were checked. No selected actual source coefficients, source parameters, points, derivative values, matrices, ranks, selected models, scans, or large computation were used. No external app was modified and nothing was published during this audit.
