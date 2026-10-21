# Independent review of the smooth cubic Hilbert germ

Reviewed PROOF.md SHA256: `1286bafee1d03442960970cbf8329d6c2d4002f8c52cf8e5ffddd26d86b39385`.

Verdict: **PASS**, conditional on the pinned tangent-dimension99 result, H0(Theta_V)=0, and the integral nondegenerate cubic-image construction. This is an independent mathematical audit, not formal verification. No selected source-instance evaluation or computation was used.

## 1. Infinitesimal stabilizers

The proof correctly distinguishes an intrinsic vector field from an ambient vector field vanishing on V. The former vanishes by the pinned H0(Theta_V)=0. For the latter, a projective endomorphism vector field vanishes exactly on its projective eigenvectors. There are finitely many eigenspaces even for a nondiagonalizable endomorphism. Irreducibility forces V into one of them; nondegeneracy makes that eigenspace the whole coordinate vector space. The endomorphism is scalar and its projective field is zero. Thus the orbit differential is injective, and the equal dimensions make it an isomorphism.

This extra argument is necessary: H0(Theta_V)=0 alone would not exclude ambient fields vanishing on a degenerate subscheme. The proof supplies it explicitly.

## 2. Local dimension and regularity

The finite-type stabilizer has zero tangent dimension and therefore zero dimension. Its translates have the same local dimension, so the orbit has dimension99. Standard algebraic group orbit properties give a locally closed orbit; over C its reduced homogeneous structure is smooth. Its closure gives a99-dimensional subvariety through the closed point [V]. Therefore the Hilbert local dimension is at least99, while its embedding dimension99 bounds it above.

Equality of local dimension and embedding dimension proves regularity of the Noetherian local ring. Over C the finite-type Hilbert scheme is then smooth at [V]. The proof does not incorrectly deduce smoothness merely from a tangent count without exhibiting the matching orbit dimension.

The cited Stacks Project [dimension and regular-local-ring criterion](https://stacks.math.columbia.edu/tag/00KD) and [regularity versus smoothness at closed points over an algebraically closed field](https://stacks.math.columbia.edu/tag/00TQ), specifically Lemma10.140.2, were checked and support these uses.

## 3. Open orbit and arbitrary Artinian order

After passing to the smooth neighborhoods, the source and target have dimension99 and the orbit differential is an isomorphism. Hence the orbit map is etale near the identity. Its image is an open neighborhood of [V], contained in the projective orbit.

For a local Artinian C-algebra, an embedded flat family with central fiber V is a Hilbert-scheme point. Formal etaleness uniquely lifts the identity through the nilpotent filtration, producing a projective transformation reducing to the identity. The condition on the reduction is essential: the global stabilizer need not be trivial. The open neighborhood used for etaleness does not exclude an infinitesimal lift because the Artinian spectrum has only one topological point.

The cited equivalence of finite-presentation etale and formally etale maps in [Stacks Project Lemma10.150.3](https://stacks.math.columbia.edu/tag/00UP) was checked. It gives the asserted existence and uniqueness, not just first-order lifting. The corresponding equality of completed local rings and the99-variable formal power-series description are valid.

## 4. Scope

The conclusion is genuinely stronger than first-order rigidity: it proves a smooth Hilbert germ, an open projective orbit near the given embedded cubic image, and projective triviality at every Artinian order. It remains specific to this embedding and Hilbert functor. The separate576-dimensional abstract deformation space, other surfaces, original HM full-adjoint problem, prescribed source, and algebraicity goal are not conflated with it. No global closed-orbit or global Hilbert classification claim is made.

## 5. Dependency-only publication rebind

The final proof pins its descent input to repository commit c48c8ce745396028965f9bb64454a22e351b2b36, path research/hm/cubic-descent-nonvanishing/PROOF.md, and retains the independently reviewed SHA256 70c2d77d9ba9e1b66c4d0b6dcf2258f8f2aedb84c7fd296b524667ff45abb719. The updated dependency was inspected and the matching local dependency content hash verified. The mathematical argument and PASS verdict are unchanged. The repository commit identity is supplied by the publishing parent; this rebind does not claim a separate remote readback.
