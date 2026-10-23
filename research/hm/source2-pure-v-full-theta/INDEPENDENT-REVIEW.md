# Independent review: the full Koszul-homotopy operator

## Verdict and frozen scope

The full-domain operator theorem is sound under the retained actual-source hypotheses. Its canonical image complement and regular-module isomorphism type are justified by actual maps, not by choosing multiplicity lines. The statement remains confined to the indicated degree-three spaces and does not establish an extension to the negative pencil or any gate incidence.

- `PROOF.md` SHA256: `6ec3128eb895d0b1fed4da0230c21f2ba8ac0814438f7a28e2110bb83d638b05`.
- `verify.py` SHA256: `882afc2bc8254852ce5a223ee034d25817878bf5928a2ec85b7a667525bf0da1`.

## Actual-map audit

**Full-domain identities.** The composition Theta=X(Id tensor h)delta is defined on all M3 and lands in F3=W im h. The sandwich identity makes it kill F3. Radical intertwining and j2h=0 give j3Theta=0; since im j3=I3⊂F3, Theta j3=0 as well. These facts give all four zero products with the retained j3²=0. Actual Q commutation and Q2h=j4 give Q3Theta=xY_yj3−yY_xj3=0. The cancellation is ordinary negative-coordinate commutativity into degree five and assumes no mixed commutation involving h.

**Exact quotient formula and determinant sign.** For arbitrary v, hY_l(v)−sY_lj3(v) belongs to I2 because both terms are in im h and have the same Q2 image. Passing through first multiplication and quotienting by I3 gives qTheta=dj3 with d=(Id tensor s)delta|I3. This uses the actual injectivity of W tensor P_h→F3 and the actual Koszul injection on I3. Thus d is injective and qTheta has rank six. The ordering x tensor Y_y−y tensor Y_x is preserved; neither the section s nor an abstract D/T identification introduces a new sign.

**Full image versus odd-kernel image.** From qTheta=dj3, qTheta(v)=0 exactly when v lies in J=ker j3. On J the pinned surjection Theta(NR3)=I3 gives im Theta∩I3=I3. Therefore the full image has dimension twelve. Its quotient image is T and its intersection with I3 is T, so equivariance excludes a hidden W′ component and proves im Theta=(F3)_T. This is not an inference from a rank alone.

On H=ker Q3, j3 is onto I3 with kernel K. The restricted factorization from PR1094 gives Theta(K)=0. The quotient formula then makes Theta|H have exactly kernel K and rank six. Its image meets I3 trivially, so L_Theta=Theta(H) is the actual canonical complementary T inside (F3)_T. The full image of Theta is twelve-dimensional; its image on H is only six-dimensional. The proof maintains this distinction throughout.

**Two-generator action.** On H, both operators kill K and have distinct image lines whose sum is K_T=(F3)_T. Any lift of a nonzero multiplicity generator of H_T/K_T is cyclic: it and its j3 and Theta images are independent. The resulting multiplicity module is therefore the regular module of C[epsilon,eta]/(epsilon,eta)^2. The other 3W′+3S constituents are annihilated by both operators. This proves the asserted isomorphism type, faithfulness, common-kernel statement and rank-six assertion for every nonzero scalar combination. It does not canonically select the cyclic lift. The two image subspaces themselves are canonical.

**Strict domain boundary.** The formula qTheta=dj3 implies ker Theta⊂J. On J, and only there, the previously constructed terminal factorization Theta=ell Q3 identifies the full kernel with J∩Q3^{-1}(C), of character 3W′+3S+4T and dimension forty-two. Extending that factorization to all M3 would force Theta(H)=0, contrary to its proved rank six. The proof explicitly avoids that invalid extension. Its operator socle on H is K and is not identified with the negative-coordinate socle.

## Authentication and reproduction

The four complete originals were independently retrieved at the exact commits and paths in `INPUTS.json`. Retrieved bytes matched the retained files exactly; independently computed SHA256 and Git blob hashes matched the manifest:

| Input | Commit | Git blob |
|---|---|---|
| 1085 | `7d1c49ea66c54039f6adbbc27cac54222961784e` | `2988fbbb5ed316124769c7157c0592e4c87aaa0f` |
| 1086 | `acb56908fd28ff019515b7ad9945f9b539f8614a` | `d3d0f0546c5b2b7d2453929364287b35f03e4d2e` |
| 1089 | `f8dfebc8c12cbefd3b17422fa1220629e90af78e` | `7459702e0b6c28aa6605ca34e2cbd98a9d366417` |
| 1094 | `79b84d3b21cdbc76bb19d3a973e09981936dda32` | `dd21bc9302ea9ffcd84dddf72ce7a676c326600d` |

This authenticates the immediate dependencies and audits their interfaces, without claiming a recursive reproof of all ancestral geometry.

Independent runs of `python verify.py` and `python -O verify.py` each passed all 33 checks. Outputs were byte-identical to each other and to `RESULT.json`. The checker uses explicit exceptions. Its regular-module matrices are normal-form controls after the actual-map proof, not source realizations or evidence of actual coefficients. The proof's kernel, image and cyclic-basis arguments were independently checked rather than inferred from those controls.

No actual source coefficient, direction or instance rank was evaluated. Independent mathematical review completed 2026-10-23.
