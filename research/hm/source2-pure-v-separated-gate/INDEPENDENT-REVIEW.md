# Independent review: separated terminal channels and gate coordinates

## Verdict and frozen files

The explicit universal channel correspondence is correct. Under the retained nonzero-N0 mechanism, the separated terminal graph contributes two formal functional components whose map to the symmetric gate plane is an isomorphism. This supplies no further linear restriction from the graph description alone. It does not assert that arbitrary components, graphs or gates occur in an actual HM source.

- `PROOF.md` SHA256: `82c4016e4cfe3a3fafd30c5339cdfb125190c796fd8b89758941a31c02b5bcec`.
- `verify.py` SHA256: `66143247452dc535c7167ac981a032ed34801e6c6301d769d6c5bfbd253e90d0`.

## Actual quotient and graph audit

PR1081 identifies the separated terminal space through its actual Koszul quotient with Sym7 W plus Sym5 W, and the projected cubic P_h descendants with its entire two-copy T part. The projection of the actual F5 is an isomorphism onto that part. Its inverse includes the actual graph into NR5; it is not replaced by the zero graph. Consequently the actual row composed with this inverse has exactly the two functional components described in the proof, with all graph dependence retained.

The universal P8 inclusion p↦(F12,Ep)_5 is nonzero and equivariant, and Sym8 has P multiplicity one. Thus the actual projected map e2s differs by one common nonzero scalar eta, not by independent changes of the two channels. Naturality gives the stated cubic comparison on the actual F5. The coherent I2/I3 identifications retained in PR1094 fix the Spencer convention and transport both functional components consistently. Neither actual scalar is evaluated.

The map J7=(F12,−)_7 has rank six, kills W′, and identifies the unique T in Sym7 with Sym5. The two cubic families C5 and C7 have stacked rank twelve. Thus their pullbacks are independent equivariant channels, not duplicate descriptions of one multiplicity row.

## Independent exact coefficient checks

A separately written computation used falling-factorial coefficient formulas for transvectants, rather than the production verifier's symbolic differentiation. It reconstructed the full Spencer matrix from the monomial relation xU(e_(k+1))−yU(e_k), appended the trace equation, and inverted that square system to obtain the unique trace-zero inverse. With the pinned apolar model, all formal quadratic coefficients gave exactly:

    U5_p(a²) = 6131220480 sqrt(5) (R1(a)−4R2(a))p,
    U7_p(a²) = −78316384529940480000 (3R1(a)+2R2(a))p.

The first inverse was also independently checked on all 36 cubic/octavic monomial pairs: U_f(v)=−(v,f)_4/20 satisfies Spencer(U_f)(c)=(c,f)_3. The negative sign and factor twenty agree with xU(yc)−yU(xc).

The trace-zero complement of scalar Id is invariant under conjugation, so its inverse gives an equivariant family, not arbitrary per-column solutions. Any remaining scalar-identity correction in a P-indexed family vanishes because Hom(P,1)=0. Therefore these full coefficient identities determine the two actual normalized gate components through the unique Spencer correspondence.

The normalized channel vectors (1,−4) and (3,2) have determinant fourteen. This verifies both the isomorphism and the inverse coordinate formulas. The corrected final text includes the zero gate in the linear conditions beta=−4alpha and 2alpha=3beta, and uses projective ratios only for nonzero gates. No projective normalization is imposed at zero.

## Authentication

All six complete input artifacts were independently retrieved at the exact repository commits and paths in `INPUTS.json`. Retrieved bytes matched the retained files exactly. Independent SHA256 and Git blob computations matched the manifest:

| Input | Commit | Git blob |
|---|---|---|
| 1031 proof | `7150cf97eeebe473bcd7c61c1f968c73625d92ef` | `0694e96e2d17a53b68d625ec6065f8bf513cd083` |
| 1031 model | `7150cf97eeebe473bcd7c61c1f968c73625d92ef` | `a7ca4755e50c85fe7fc20a757125127a05de4056` |
| 1094 proof | `79b84d3b21cdbc76bb19d3a973e09981936dda32` | `dd21bc9302ea9ffcd84dddf72ce7a676c326600d` |
| 1036 proof | `bb22e239e9423b54487236dba8c4f70f9e6b738f` | `718f987511b5bf6144a85fc14e8ef343612a4491` |
| 1081 proof | `411b644cdc12938c35b7fedac5bb92664bfc1a47` | `3aa53fa809fa82cef18629cc040cf61fe4eb0a90` |
| 1036 verifier | `bb22e239e9423b54487236dba8c4f70f9e6b738f` | `e4fc685ce1a2f6e5eafbba385dcf5ec9c8ceae62` |

The invariant F12 is the pinned universal Wronskian, and the production verifier reconstructs it from ker Pi. It is not a selected actual source form. The historical 1036 verifier was authenticated as a normalization source, not executed as an experiment. This review authenticates immediate inputs and their interfaces without claiming a recursive reproof of every ancestral theorem.

## Reproduction and boundaries

Independent runs of `python verify.py` and `python -O verify.py` passed all 27 checks. Outputs were byte-identical to one another and to `RESULT.json`. The verifier uses explicit failures, so checks remain active under optimization. The independent coefficient-only reconstruction described above also passed.

The absence of a universal linear equation is a statement about the formal channel map. It is not freedom to choose the actual terminal row, a realization theorem, a gate nonvanishing result, or a conclusion for the residual-large mechanism. No actual source coefficients, directions or instance ranks were evaluated.

Independent mathematical review completed 2026-10-23.
