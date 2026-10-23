# Independent review: common quadratic homotopy kernel

## Conclusion and binding

The theorem is sound with the residual-large hypothesis retained throughout and the additional condition R=0 imposed only for the correction conclusions. This review binds to `PROOF.md` SHA256 `e3fd2640a8a0bd8b2fc040b4f38b633893c869cd4859a9a3f225828f080d50cf` and `verify.py` SHA256 `5e9334a92ddefadec869356105272324128beb996885053d0f9746b3d3ed70ca`.

The previously missing P and D nonvanishing is established, not assumed. The actual common kernel on NC2 is I2; the residual common map has rank15 and kernel dimension17. On the whole source its common kernel has dimension21. Under R=0 the correction P channel is forced to have a nonzero, hence isomorphic, projection to the genuine separated P. This is not a proof that R=0 occurs or fails, and does not select a fifth obstruction.

## Actual polynomial transport

The retained evaluation reconstruction identifies NC2 with Sym16 W and NC4 with Sym18 W/H_t, with quadratic arrows given by ordinary product in the same negative variables. This is stronger than an identification of characters. The unique D18 is not contained in H_t=A18+V18+P_t. In the residual-large case, the actual isomorphism h:NC4/I4→I2 identifies hT on NC2, up to a nonzero scalar and output isomorphism, with projection of the product onto D18. Nonvanishing of this scalar is a proved consequence of PR1064 in the stated mechanism, not a genericity assumption.

The invariant F12 has the pinned Wronskian normalization. Its Hessian H20 and the map d↦(H20,d)_3 are equivariant universal constructions. A nonzero map from irreducible D, with rank5 and unique D multiplicity in Sym18, gives exactly D18. The invariant nondegenerate apolar pairing restricts nondegenerately to this multiplicity-one self-dual constituent. Thus its transpose-pairing map has precisely the required kernel; any remaining output normalization cannot change the common kernel.

## Independent universal certificate

Before reading the production verifier, I independently constructed the complete 19-by5 D18 matrix and the stacked 15-by17 coefficient matrix for all three quadratic monomials acting on all seventeen Sym16 coefficients. Exact calculation gives ranks5 and12. The full product with the rank5 matrix F12·Sym4 vanishes. Therefore the common kernel is exactly that embedded I2, not only a containing subspace.

The independent calculation also reproduced the same nonzero twelve-minor in rows 0,1,2,3,4,5,6,7,8,9,13,14 and columns 0 through11, including its exact rational multiple of sqrt5 recorded in RESULT.json. These are coefficient matrices of universal maps, not evaluation at any actual direction or source instance. Because NC2/I2=V+P+D and the target contains each once, the calculation proves all three channels, including P and the surviving D.

## Residual and full kernels

The image from NC2 fills the V+P+D constituents of Hom(A,I2). The actual canonical A row hT a_A=mu m, with mu nonzero, fills the remaining A constituent. Consequently the residual map is onto dimension15. Its kernel intersects NC2 in I2, so its projection has dimension12 and character V+P+D in the multiplicity-free N8,2. This proves the actual exact sequence without a horizontal splitting.

The target Hom(A,I2) is valid on J2=ker j2: QhT v=Tj2v=0 and im h∩ker Q=I2. The genuine separated decomposition and the actual radical image give J2=NR2⊕N0,P. Residual surjectivity then proves both the dimension21 kernel and its surjection onto N0,P. On arbitrary source vectors hT need not take values in I2. Nevertheless a vector in its full common kernel has T_a j2v=0 for every a. The common kernel of L on irreducible I2 is zero, since L is nonzero. Thus this vector is in J2. The distinction between target on J2 and kernel on the full source is correctly maintained.

The sandwich puts F2=I2⊕P_h in the residual kernel. Its kernel character V+P+2D has a unique P, so that actual subspace is P_h. No repeated-copy identification is inferred without this containment.

## Correction placement under R=0

The published symmetry of B, together with its actual diagonal R, gives B=0 under the additional hypothesis. Hence k=GTs lies in the common kernel. The actual residual quotient theorem makes A⊗P_h→N8,4 an isomorphism. It follows that Qk is injective and its image is disjoint from I4. Since QF2=I4, the correction image is disjoint from F2. Their dimensions12+9 fill the dimension21 kernel, and applying Q gives QK=F4.

Changing G changes k by a map V+P+D→ker Q=A+I2. The V and P restrictions are therefore independent of G, while the D ambiguity is exactly I2-valued. The equation j2k=hTs=0 places all corrections in J2, so V and D are residual. If kP were residual, it would lie in the unique residual common-kernel P, namely P_h. Its Q image would then be I4, contradicting the nonzero descendant projection to N8,4. Its separated projection is consequently nonzero and irreducibility makes it an isomorphism onto N0,P. This argument does not assume Q preserves NR.

## Replay and authentication

I inspected the verifier and executed it normally and with Python optimization. Both 49-check outputs agree byte-for-byte with each other and with RESULT.json. Reproduce with `python verify.py` and `python -O verify.py`. The bounded pinned model is used for universal normalization only. Arithmetic and character checks supplement, rather than replace, the actual-map arguments above.

All ten immediate resources were freshly fetched at the exact public commits and paths in INPUTS.json. Their remote bytes, SHA256 values and Git blob hashes match the retained inputs:

| Input | Commit | Git blob |
|---|---|---|
| 1064 | `bfc239e1c8624a0346394e1454b0bea3c976d40d` | `20b3b58b92d4c44d1097d47a9e952c4dfa25b569` |
| 1069 | `41bc20cade3198306c492c0c46399d71eb0d51c4` | `827cd956e2eb574fd7d40d408e0450c8581fd7d2` |
| 1089 | `f8dfebc8c12cbefd3b17422fa1220629e90af78e` | `7459702e0b6c28aa6605ca34e2cbd98a9d366417` |
| 1059 | `af2f163e4bcc593b6895ace840c139d2d4668cde` | `2b00a40de04a7084ff2f08c767fdd2f4f13ae5f4` |
| 795 | `3f811311d76914a555c7e7d0c5b887b41805aa6c` | `9358ec81c552913fac20f3a92d7b9f7c58105656` |
| 1019 | `3fb2475ffb275c5789acbaa8f9f84ed272713785` | `bf63c14f76933d59fa7e3ac61aecb3366ac1b442` |
| 1031 | `7150cf97eeebe473bcd7c61c1f968c73625d92ef` | `0694e96e2d17a53b68d625ec6065f8bf513cd083` |
| model | `7150cf97eeebe473bcd7c61c1f968c73625d92ef` | `a7ca4755e50c85fe7fc20a757125127a05de4056` |
| 1036-verifier | `bb22e239e9423b54487236dba8c4f70f9e6b738f` | `e4fc685ce1a2f6e5eafbba385dcf5ec9c8ceae62` |
| 792 | `2f01f18960ce56b8b2a0c1260c277de3c5f916bf` | `76bee93507d1a2d0840926d4e4e27edadfebb7d7` |

The authentication scope is these immediate inputs, not a fresh recursive reproof of all ancestral geometry. No actual source coefficients, parameter values, points, directions, jets or instance ranks were evaluated. The degree-two residual kernel here is not identified with a degree-four kernel carrying similar notation in an earlier input. No full residual-module splitting, Q-preservation, opposite-pencil identification or full-adjoint conclusion is asserted.
