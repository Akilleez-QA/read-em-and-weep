# Independent review: canonical terminal row and transfer incidence

## Verdict and frozen files

The canonical terminal map, its kernel description, and the two-way vanishing criterion are sound under the retained actual-source hypotheses. Neither terminal incidence is selected; the result does not establish nonzero R or exclude a surviving mechanism.

- `PROOF.md` SHA256: `32de2ab5c3988c6a571cb1ceb2ec76031c5d3cf311ca51c33b528e9c337e9675`.
- `verify.py` SHA256: `4676ffee18903b11ab16a5134b690471d571b833963568427a25b2d556329b2b`.

## Independent actual-map audit

**Canonical factorization.** On J3=ker j3, each hY_n takes values in I2, so the determinant expression theta is well-defined into I3. It kills F3 by the sandwich identity. The T-isotypical part of K3 is exactly F3_T, and its remaining constituents cannot map to I3=T. Thus theta kills K3. The surjectivity j3(ker Q3)=I3 permits adjustment of every Q3 preimage into J3, proving Q3:J3→V5 onto with kernel K3. This gives a unique factor ell on the actual image V5, independent of right inverses or chosen complements. Its surjectivity follows from the actual inclusion NR3⊂J3 and the already established surjectivity of theta on NR3.

**The plane as an embedded image.** The contraction of A_h is theta. Hence Q3(ker A_h) lies in C=ker ell. Its Q3 kernel is exactly ker(A_h|K3), with character 3W′+2S+2T and dimension 26. The full ker A_h has character 3W′+2S+4T and dimension 38. Their actual quotient has character 2T and dimension 12, giving equality with C. The argument first proves containment; it does not identify two arbitrary equal-character subspaces.

**Correction sign and legitimate domains.** For b quadratic, k_b=G T_b s is defined because T_b s lands in im Q2. It satisfies Q2 k_b=T_b s and j2 k_b=0. Therefore X_l k_b(p) belongs to J3 and maps under Q3 to (lb)s(p). Applying theta gives exactly

    X_x B(yl,b)p − X_y B(xl,b)p.

The plus convention in the definition of B is unchanged; the subtraction is solely the Koszul determinant. Products lb span all cubics. Coherent I2 and I3 inclusions transport both terms with the same scalar. No assertion that G commutes with negative multiplication is used.

**Quartic factorization and the full universal kernel.** Symmetry of B and the trivial kernel of Sym2(Sym2 W)→Sym4 W give its unique quartic factor A4, because Hom(P,D)=0. A separately written coefficient computation constructed the entire 24-by-25 operator U↦[c↦xU(yc)−yU(xc)] and verified rank 24 with kernel exactly scalar Id. The written recurrence proof was also checked: the four relations imply U(e_j)=(y/x)^jU(e_0); polynomiality of the last term forces x^4 to divide U(e_0), giving a scalar identity operator. The production certificate additionally checks all three sl2 equivariance identities and the full formal cubic expression.

The kernel is a trivial representation. An equivariant P-indexed family cannot lie nontrivially in it, since Hom(P,1)=0. Thus the induced operator is injective on the two symmetric transfer channels. This is stronger than a generic-rank calculation and retains every coefficient.

**Both directions of the incidence criterion.** Cubic descendants of I2 vanish because W²I2⊂I4 and WI4=0. Hence F5 is exactly the span of cubic P_h descendants. The legitimate correction lifts place those descendants in V5. The family identity then gives ell(F5)=0 exactly when the Spencer operator kills every U_p, hence exactly when A4 and B vanish. Polarization of symmetric B gives equivalence with R=0. In the residual-large mechanism this means the particular NR5 lies in C; in the nonzero-N0 mechanism equal dimensions turn containment of the actual F5 into equality F5=C. A possible graph into NR5 is retained. These are conditional incidence tests inside each mechanism, not equivalences characterizing which mechanism occurs.

**Scope.** The construction concerns the actual negative-coordinate module and the invariant quadratic. It does not require Q to preserve NR, extend h to a module map, impose arbitrary mixed commutation, identify a terminal graph with its separated projection, or determine any positive/full-adjoint rank.

## Input authentication

All eight complete originals were independently retrieved at the exact commits and paths in `INPUTS.json`. Their bytes matched the retained inputs exactly; independently computed SHA256 and Git blob hashes matched the manifest. The authenticated commit/blob pairs are:

| Input | Commit | Git blob |
|---|---|---|
| 1089 | `f8dfebc8c12cbefd3b17422fa1220629e90af78e` | `7459702e0b6c28aa6605ca34e2cbd98a9d366417` |
| 1085 | `7d1c49ea66c54039f6adbbc27cac54222961784e` | `2988fbbb5ed316124769c7157c0592e4c87aaa0f` |
| 1086 | `acb56908fd28ff019515b7ad9945f9b539f8614a` | `d3d0f0546c5b2b7d2453929364287b35f03e4d2e` |
| 1069 | `41bc20cade3198306c492c0c46399d71eb0d51c4` | `827cd956e2eb574fd7d40d408e0450c8581fd7d2` |
| 1079 | `99f4d2458b831b4cfad6f7fc73c2ce85f0cff75e` | `3d426673e0793030335604b661d2f8a7cfb299bb` |
| 1081 | `411b644cdc12938c35b7fedac5bb92664bfc1a47` | `3aa53fa809fa82cef18629cc040cf61fe4eb0a90` |
| 795 | `3f811311d76914a555c7e7d0c5b887b41805aa6c` | `9358ec81c552913fac20f3a92d7b9f7c58105656` |
| 1091 | `e88f289033dd638591b6bf73ff2b2dc890b9708a` | `5615f2b1c73e6753cf9fd18ed8da7f55c0e02c3b` |

This authenticates the immediate inputs and their use, without claiming a recursive reproof of every ancestral geometric theorem.

## Reproduction

Independent executions of `python verify.py` and `python -O verify.py` each passed all 43 checks. Both outputs were byte-identical to one another and to `RESULT.json`. The independent full coefficient-matrix kernel/rank certificate also passed. The checker uses explicit exceptions and does not lose checks under optimization. Its type bookkeeping and formal controls support, rather than replace, the actual-map proof audited above.

No actual source coefficient, direction or instance rank was evaluated. Independent mathematical review completed 2026-10-23.
