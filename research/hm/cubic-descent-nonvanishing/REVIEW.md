# Independent review of structural cubic descent nonvanishing

Reviewed PROOF.md SHA256: `70c2d77d9ba9e1b66c4d0b6dcf2258f8f2aedb84c7fd296b524667ff45abb719`.

Verdict: **PASS**, conditional on the explicitly pinned interpolation, character, and deformation-map inputs. This is an independent mathematical audit, not formal verification. No selected coefficient, point value, derivative value, matrix, numerical rank, or source-instance test was performed.

## 1. The actual quotient and its full-support dual

The paired exceptional derivative functionals are two distinct monomial tensor lines in Sym^3(A), with the same joint D-weight. Their common value in S* determines their difference after identifying the target fibers. Both coefficients are nonzero, so that difference is a nonzero functional on the ambient cubic space, even though it annihilates S. Its restriction to cubics vanishing at the two centers is the intrinsic functional of PR620. The homogeneous coefficient description gives the required equivariant extension without evaluating a coefficient ratio.

The target Q_sigma has the section weight dual to the common tensor weight, so the extension is D-equivariant as a map to Q_sigma. The actual surjection rho' has kernel exactly S, not merely a kernel with the same character. Therefore the factor alpha exists uniquely and is nonzero. Equivariance and transitivity on the twenty-five fibers imply that if any component alpha_z were zero, every component would be zero. All components are consequently nonzero. No claim of independent conditions on derivatives is used.

## 2. Nonvanishing before spectral projection

The universal cyclic action of any other direction on the G-eigenlines proves that its eigenvectors have no zero G-coordinate. This argument uses only a nontrivial Heisenberg commutator and the eigenvector equation, not selected eigenvectors.

For every nonzero pair of coefficients a,b, the cubic a x_1^2 x_4+b x_3^2 x_0 has singular locus exactly x_1=x_3=0. Necessity follows from its x_4 and x_0 partials, and sufficiency follows because all partials then vanish. Thus none of the twenty-five other-direction centers is singular for this cubic. Because the cubic vanishes there, Euler's identity makes its nonzero homogeneous differential a well-defined nonzero projective tangent covector.

Every direct-sum component alpha_z composed with ds_z is nonzero. A covector on a direct sum vanishes only if each component vanishes, so L is nonzero. This proof does not select or evaluate a velocity or a point; it establishes a universal nonvanishing statement from supports.

## 3. The crucial normalization-compatibility step

Nonvanishing on all center motions would not suffice. The proof correctly supplies an additional spectral argument. The target Hom(K_sigma,Q_sigma) has joint weight equal to missing tensor weight minus value tensor weight, namely (0,2) in the normalized case. Hence L factors through that joint D-character projection.

On the g-fixed source, h preserves the individual U-character spaces because the conjugation correction is a power of g and the center acts trivially. There are no U-invariants in T_Z, so all these characters are nontrivial with kernel G. The normalization target for each such character has h-weights 1 and4 only. Thus the entire h-weight2 source is killed by b_N. In particular the projected support of the nonzero L lies in the actual normalization kernel.

The projective-coordinate summand in these characters has h-weight0. It has no intersection with the supported h-weight2 source. The nonzero motion therefore survives the quotient by pgl(A). These facts exclude both possible gaps: using an incompatible unrestricted motion, or obtaining only a coordinate change.

## 4. Identification with the canonical residual map

For a normalization-compatible motion, the lifted cubic solves the full evaluation equation. Restricting it to the twenty-five-center quotient and applying alpha gives exactly L(v)(s). At the two paired centers the first jet of s is zero, so the lift vanishes there and the extended functional agrees with the intrinsic paired first-jet difference. PR620 then identifies that difference with the actual residual descent obstruction, up to its uniform harmless sign.

No target splitting or independently chosen map with matching representation type is substituted. The argument therefore proves actual b_J nonvanishing. PR619 pairs the two descent statuses, and the normalizer carries the nonzero channels to all nontrivial characters. Together with the already proved normalization rank, this gives rank b=96, zero kernel, and embedded tangent dimension99.

## 5. Scope

The conclusion is first-order embedded rigidity modulo projective coordinates for the canonical cubic image. The note explicitly does not transfer this conclusion to the original full-adjoint or prescribed-source problem, or infer higher-order statements without a separate argument. The calculation restrictions are respected: all polynomial statements concern universal symbolic supports with unevaluated nonzero coefficients, and the nonvanishing follows structurally rather than by a selected-instance rank test.
