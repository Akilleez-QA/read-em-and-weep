# Independent review: the exact middle homotopy pairing

## Verdict and frozen files

The exact image, radical, marked-string comparison and Euler quotient follow from the retained actual maps. This review approves the conditional mathematics, without selecting a source, surviving endpoint mechanism or actual coefficient.

- `PROOF.md` SHA256: `792748b4fee0ee2173e8601beb958de6380513c7cd2daf8554dfc5eda96b0da2`.
- `verify.py` SHA256: `f1af74705339283b8de7796a08b782ed5d24c1fa0567c1bf83166b78783f8932`.

## Actual-map audit

1. **Domain and target.** For v in ker j3, Q2 hY_n v=Y_n j3v=0. Together with hY_n v in im h this puts the value in I2, not merely an abstract D constituent. Currying gives W* tensor I2 with the correct central parity. PR795 §6 proves that every radical kills the actual residual submodule, so NR3 and NC3 are legitimate subspaces of this domain.

2. **Surjectivity in both restriction cases.** If h|NC4 is nonzero, the actual δ isomorphism NC3→W tensor NC4 and the onto map h:NC4→I2 prove surjectivity after the determinant rotation. If h|NC4=0, the descended map on N8,4 is a nonzero scalar times the pinned C2 channel, because of the marked D_can comparison. Actual quotient naturality gives the paired map U(u)(ell)=C2(ell u), with ell multiplying the second polynomial factor. No residual splitting or Q preservation is assumed.

3. **Independent universal verification.** A separately written exact coefficient computation constructed the 10-by-18 paired map and found rank ten. Complete polarization Sym7→Sym2 tensor Sym5 was independently reconstructed; its matrix has rank eight and is killed identically, proving the full kernel. A fully formal cubic/linear expansion independently verified C2(ell epsilon²g)=84 ell g. The determinant convention was separately checked: on paired quartics (u,v), contraction is xv−yu; its kernel is precisely the rank-four image f↦(xf,yf). Thus the S channel is the ordinary multiplication channel with the stated variables, not a swapped dual convention.

4. **Restriction to the simultaneous kernel.** A_h kills F3 by the actual inclusion Y_W F3⊂F4⊂ker h. All S-isotypical vectors lie in K3, since the Q3 and j3 targets contain no S. Equivalently J3/K3 embeds into the purely T image of Q3. Hence restricting the onto map from J3 retains its full S image. The entire T part of K3 equals the T part of F3 by PR1089 and is killed. The induced map on K3/F3 therefore has image exactly S, not only an upper bound. Its joint radical is the actual kernel, of character 2W′+2S and dimension twelve.

5. **Euler quotient and marked comparison.** The source after quotienting by the radical is the actual S coefficient space of the pairing. Uncurrying its embedding into W* tensor I2 gives the unique nonzero W tensor S→D channel, so its pencil is ordinary cubic-to-quartic multiplication and has quotient O(4). The marked S_can from PR1064 lies in K3 and is disjoint from F3. Coherent multiplication into the marked D_can, followed by the isomorphism h|D_can, proves that its pairing maps isomorphically onto this S image. Consequently its quotient image is a canonical complement to the radical, with the displayed inverse-and-forward projector independent of scalar normalization. This uses actual canonical string maps, not arbitrary copies of S or D, and supplies no identification with an opposite-pencil channel.

6. **Scope.** These are actual vector-space and parameter-pencil conclusions. They do not extend h to a module map, provide a negative-horizontal or positive-module splitting, select a complement to F3 inside the pairing kernel, or decide either surviving source mechanism. Character subtraction occurs only after proving the relevant actual surjections and inclusions.

## Authentication

All seven complete originals were independently retrieved at the exact commits and paths specified in `INPUTS.json`. Their bytes matched the retained inputs exactly; independent SHA256 and Git blob computations matched the manifest. Authenticated commit/blob pairs:

| Input | Commit | Git blob |
|---|---|---|
| 1019 | `3fb2475ffb275c5789acbaa8f9f84ed272713785` | `bf63c14f76933d59fa7e3ac61aecb3366ac1b442` |
| 1064 | `bfc239e1c8624a0346394e1454b0bea3c976d40d` | `20b3b58b92d4c44d1097d47a9e952c4dfa25b569` |
| 1068 | `05e8b33eb87e9f36aa30500145cc42bc0ea00df8` | `5ae07c02624d70c0ccd33d7ec34202504173ff83` |
| 792 | `2f01f18960ce56b8b2a0c1260c277de3c5f916bf` | `76bee93507d1a2d0840926d4e4e27edadfebb7d7` |
| 795 | `3f811311d76914a555c7e7d0c5b887b41805aa6c` | `9358ec81c552913fac20f3a92d7b9f7c58105656` |
| 1054 | `8732cb65fe0e72da59e785f3f85ad197a7092e6c` | `64e6bf9f1bf46440700ebab7c90a18f9d8155fd8` |
| 1089 | `f8dfebc8c12cbefd3b17422fa1220629e90af78e` | `7459702e0b6c28aa6605ca34e2cbd98a9d366417` |

This authenticates the immediate inputs and audits their interfaces, without claiming a recursive reproof of all ancestral geometry.

## Reproduction

Independent executions of `python verify.py` and `python -O verify.py` passed all 38 checks, with outputs byte-identical to each other and `RESULT.json`. The explicit failures survive optimized execution. The additional independently written paired-map, polarization-kernel, determinant-convention and factor-84 checks also passed. Formal controls support rather than replace the actual-map reasoning above.

No actual HM coefficient, direction or source-instance rank was evaluated. Independent mathematical review completed 2026-10-23.
