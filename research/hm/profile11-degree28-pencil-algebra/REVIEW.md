# Independent review: exact degree-twenty-eight negative-pencil algebra

## Verdict and immutable scope

PASS, as the conditional necessary algebra theorem stated in the proof.

Reviewed file: `PROOF.md` in this directory, read in full.

Exact reviewed SHA-256:

    eb468f88d6d5121fa38a695ecf9c47c97e365590ade8f122be82f0476ec8e79b

This verdict binds that exact file, not later edits. The reviewer did not edit the proof or publish anything. The review is an independent written mathematical audit, not proof-assistant certification. No executable mathematical verifier is needed for this step: the new assertions concern natural exact sequences, all morphisms of fixed pencils, and the multiplication of an explicitly exhausted finite-dimensional algebra.

The following exact dependency files were retrieved read-only from `Akilleez-QA/read-em-and-weep` at their stated commits and compared byte-for-byte with the local copies used in the review:

- PR856, `cee45480686c39a321feaa77d4b669682cc71efe`, `research/hm/profile11-degree28-constant-separation/PROOF.md`; SHA-256 `b971cac17174bb609f096e3bb4a89a14d8f518bd01b1f0a99a9010b59ccfd1c3`.
- PR858, `d3b3134e23d0aa4c4b58fd1457f040856d2d0655`, `research/hm/profile11-degree28-residual-templates/PROOF.md`; SHA-256 `dddfb627c7ff27a68cf887f4e98ee8ba1195181168f9ff5a63f01d8cc5d2d8c9`.
- PR790, `af0e03d26da5e47d18ae732291aca46f4d448dc5`, `research/hm/source2-first-constant-block/PROOF.md`; SHA-256 `0a05b3c947b159e86e332307ebf7e46bfbfce1f12947a6472842d8c133bb6fa4`. Its Section 6 was checked specifically as a general natural-map identity, not as a source2 normal-form theorem.
- PR791, `2cd033a4a5ba549d07330427cd779364cb83c0fb`, `research/hm/source2-pencil-endomorphism-algebra/PROOF.md`; SHA-256 `8b0a5b22fd5221b7532befaee121dcf42edf0bbbc249141b8e029c957c527290`.

The three original presentation files named in Section 1 were also read at commit `db51525015bb7c5e825833d550d08dedf6f6ea96`: `ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md`, `POSITIVE-DOUBLE-HYPERPLANE-GAUSS-GATE.md`, and `UNIFORM-TWIST-FOUR-FIVE-HYPERPLANE-COHOMOLOGY.md`, under `research/hm/order-four-quadratic-load/`.

## 1. The degree-one issue is genuinely resolved

PR791's Section 6 assumes all splitting degrees of `Q*` are at most -2. That hypothesis must not be imported into this branch. The present proof does not import it: its Section 5 supplies a new argument from `H0(E)=0` and global generation of `Q(-1)`. These suffice.

For any ordinary summand `O(d)` of `Q`, global generation gives `d>=1`. Its complete evaluation sequence is

    0 -> H0(O(d-2)) O(-1)
      -> H0(O(d-1)) O -> O(d-1) -> 0.

For `d=1` the kernel is zero and the last map is the identity evaluation of a constant line. There is no omitted kernel or extra degree-one endomorphism. Direct sums give the displayed sequence (11). Its kernel map is canonical multiplication by the linear form vanishing at the parameter, with the fixed symplectic/determinant convention. Consequently intertwining all fixed first-pencil maps gives a sheaf map of this sequence. A noncanonical choice of Birkhoff-Grothendieck splitting is not being used to define that map.

Also `H1(Q(-2))=0`, including the `O(-1)` twists of degree-one summands. The Koszul multiplication sequence therefore gives every section of `Q` as `u x+v y`, with relations exactly `(A_v,-A_u)`. The boundary has kernel precisely the injected constant space `H`, and is onto `H1(E)`. This proves (12) under exactly the stated weakened hypotheses.

For fullness, an arbitrary intertwining triple first induces `h` on (12), and independently induces `q_0` from the evaluation sequence. These two constructions agree on each section coming from `H`: both send its cycle `(x,y)` to the section `u e3(x)+v e3(y)`. Equality on constant sections is equality of the bundle maps out of `H O`. Hence `h` preserves the kernel `E` everywhere, not only on a dense open set.

The recovered `N2` map equals the prescribed `e2`, because multiplication by any nonzero linear form is injective on sections of a vector bundle. The recovered `N4` map equals `e4`, because the second intertwining relation determines the action on the boundary of every section `u x+v y`, and that boundary is surjective. This last step rules out undetected endomorphisms acting only on `N4`.

Faithfulness follows from reconstruction (12), or from global generation determining `q_0` from `e3`, followed by the injection `H' -> H0(Q')`. These arguments concern arbitrary morphisms, including singular ones, and preserve addition and rightmost-first composition. Thus the conclusion is an isomorphism onto the entire fixed-variable pencil commutant, not merely an injection or a subgroup statement.

The actual hypotheses are verified independently of the stronger source2 slope bound. `E` has negative splitting degrees. The original exact first multiplication presentation makes `D_lin` a locally free quotient of `M3 O`, and identifies the actual quotient as `Q=D_lin(1)`. Hence `Q(-1)` is globally generated. The original Gauss gate supplies the same actual constant inclusion and Koszul quotient map used in PR790 Section 6. That section's universal identities identify both reconstructed pencils simultaneously with the fixed actual tensors. No arbitrary representation isomorphisms are substituted for these natural maps.

## 2. Exhaustion of the entire constant algebra

For every constant endomorphism preserving `E=F+R`, its lower block restricted to `F` is a bundle map `F -> R`. It vanishes because the source has degree -2 and every target summand has degree at most -8. Since `F` spans `C`, the whole constant lower block vanishes. This does not assume invertibility, a rank condition, or preservation of a chosen complement.

The remaining `C` diagonal block preserves `F` and induces a scalar on the line quotient `O(28)`. Since `H0(F)=0`, the coefficient map `C -> H0(O(28))` is injective. Thus that diagonal block is the same scalar on all of `C`, including when the scalar is zero.

Every remaining endomorphism is exactly `(a,d,b)`, with `d` in the full residual algebra and `b` in the kernel of the constant restriction map `Theta`. Conversely these conditions suffice. PR856 supplies the actual surjectivity of `Theta`, not only its character dimensions; its four-dimensional source and two-dimensional target give `dim J=2`. Composition is exactly

    (a,d,b)(a',d',b')=(aa',dd',a b'+b d').

Therefore the proof has not discarded any extra singular endomorphism or lower off-diagonal channel.

## 3. Every right action and arrow checked

The disjoint-support claims use the actual residual spans of PR858 and the actual first-polar origin of `Y`. They do not confuse abstract bundle Hom spaces with restrictions of constant maps.

- Type I: only the P channel restricts to `X`, and it is nonzero there. Thus every element of `J` has zero P component. The remaining A,V,D channels map onto the one-dimensional tail Hom space, with a two-dimensional kernel. Right multiplication on all of `J` is by the scalar on `A+V+D`, not by the scalar on P. The P vertex is isolated, giving `C times T(J)`.
- Type II: the shared D forces the same scalar on the spans of both intrinsic lines. Thus the entire residual algebra is scalar, including its nonunits, and the result is exactly `T(J)`.
- Type III: the P,D channels have only top restriction, onto by P; their kernel has dimension one. The A,V channels have only tail restriction, onto by V; their kernel also has dimension one. The former right action is the scalar on P+D, and the latter is the scalar on A+V. Both kernels contain nonzero actual constant maps. Since `R` spans `Hbar`, no such map disappears on the inclusion. Hence there is one actual radical arrow from each residual vertex into `F`.

The multiplication formula covers zero diagonal scalars and arbitrary radical components. In particular it classifies the full algebras, not merely their unit groups.

## 4. Radical, center, and covariant orientation

Each radical map kills `C` and maps `Hbar` into `C`, so every product of two radical maps is zero. The quotient by this ideal is exactly `C^3`, `C^2`, or `C^3`. Nilpotence gives inclusion in the Jacobson radical; the semisimple quotient gives the reverse inclusion. Thus no further radical component is missing.

Commutation with vertex idempotents kills the off-diagonal component of any central element. Each nonzero arrow then equates its source and target diagonal scalars. This gives center dimensions 2, 1, and 1 in Types I, II, and III. In particular the two five-dimensional algebras of Types I and III are not isomorphic.

The computation is for `E` inside `H O`. Reconstruction takes its constant maps covariantly to pencil triples. There is no annihilator dualization at this stage and therefore no opposite-algebra reversal. The Type III arrows really point into `F`, as seen both from the block maps and from the right actions in the product. No unsupported self-opposite claim is needed.

## Boundary

No blocking defect was found. The result remains conditional on the cited actual branch and previously proved structural inputs. It does not compute the fixed HM commutant by evaluating actual tensors, realize any residual class in HM, exclude a label, lift an endomorphism to the full module, or settle the global rank goal. The review used no selected actual coefficients, parameters, points, derivatives, matrices, source-instance ranks, selected models, scans, large computations, or source-application writes.
