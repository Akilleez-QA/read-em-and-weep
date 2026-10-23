# Independent review: universal rank and separated residual correction

## Conclusion and binding

The theorem is sound with its stated scopes. The Gamma ranks15 and kernel dimensions17/21 hold in every retained mechanism. The residual correction section and its consequences additionally require R=0 and nonzero separated projection of P_h.

This review binds to `PROOF.md` SHA256 `b90ccb4dbfea5721b020b26ea683412bce3fcb7dd058cf2012dff8aaccbcf642` and `verify.py` SHA256 `bf6a05ddfecaac77b718a741c2ba7e76b00438b291d8d8a66c6cbd6f6bffbc8c`.

The exact I4-valued Q defect is essential and is retained. The normalization is not an unchanged-Q correction, not a horizontal splitting and not a determination of a fifth gate. The complement retains its D/I2 ambiguity; its quotient identification is canonical with the fixed genuine separation.

## Rank transport in both core-row cases

For h|NC4 nonzero, actual multiplication NC2→NC4 is the degree-sixteen polynomial model followed by the genuine endpoint quotient. The quotient kills no D18 constituent, and h induces a nonzero map on its unique D quotient. Thus Gamma|NC2 is the universal D18 projection of quadratic multiplication up to a nonzero output identification. This argument needs only the nonzero core row, not residual-large placement of P_h.

The complete coefficient certificate has rank12 and kernel F12 Sym4=I2. I independently reconstructed this matrix in the preceding common-kernel review and reran that separate calculation here, reproducing the full rank, kernel product and exact twelve-minor. The nonzero canonical A row then fills the remaining target constituent and proves residual rank15. The kernel intersects NC2 in I2 and projects onto the canonical multiplicity-free V+P+D in N8,2.

For h|NC4 zero, the separately authenticated whole N8 Hom isomorphism of PR1117 proves residual rank15 with kernel NC2. These cases exhaust the possibilities, so the all-mechanism rank assertion is justified. The J2 target is correctly typed using QhT=Tj2 and im h∩ker Q=I2; no such target is assigned on arbitrary M2. Its additional separated P gives the dimension21 common kernel.

The universal certificate from PR1113 is transported afresh under the weaker nonzero-row hypothesis. Its residual-only correction conclusions are not imported into the separated mechanism.

## Separated zero-gate correction decomposition

PR1117 makes the core row nonzero under R=0. In the separated case, e0|P_h is an isomorphism onto N0,P, while the sandwich puts P_h in K. Hence K=K_{R,2}⊕P_h as actual degree-two subspaces.

The actual transfer is symmetric and has diagonal R, so R=0 puts k=GTs in K. Its J2 membership also follows directly from j2k=hTs=0. The separated quadratic descendant theorem makes Qk injective of dimension12 and disjoint from I4. Since QF2=I4, the correction image is disjoint from F2. Dimensions give K=I2⊕P_h⊕im k and QK=F4. This is a separated-case argument using its actual projector, not an invocation of the residual-large theorem.

## Canonical quotient versus noncanonical complement

The inverse sigma of e0|P_h is a fixed actual map. Therefore r=Id-sigma e0 is a projection of J2 onto NR2, with kernel P_h, and fixes I2. On K its image is K_{R,2}. If rk(u) lies in I2, then k(u) lies in F2, forcing u=0. Thus rk gives a twelve-dimensional complement to I2.

A change of equivariant Q inverse changes k by a map V+P+D→A+I2. Only its D part can be nonzero, and that part lands in I2. Since r fixes I2, the same ambiguity remains after normalization. Hence the quotient map and pi2 rk are independent of G; V and P are canonical actual maps, whereas the D lift is defined modulo I2. The actual residual P obtained this way is not P_h, whose separated projection is nonzero. No claim of a canonical D complement or horizontal module section is made.

## Defect, cross-block isomorphism and terminal image

Applying Q to the literal formula rk=k-sigma e0k gives

    Qrk=T_As-Qsigma e0k.

The subtracted term lands in I4 and is supported only on the P input constituent. It is independent of G but its value is not selected. In particular the residual mechanism's earlier forced nonzero separated correction scalar is not imported here.

Only after applying the genuine target projector e0 does the defect vanish. The resulting e0Qrk=e0T_As is the actual separated quadratic descendant isomorphism onto E0. Since QI2=0, it proves e0Q:K_{R,2}/I2→E0 is an isomorphism. It also proves Q(K_{R,2}) has dimension12 and is disjoint from I4. Combining with QK=F4 yields F4=I4⊕Q(K_{R,2}). The two degree-four complements differ by precisely the retained defect, not by an assumed equality.

Finally actual multiplication gives Q3(WK_{R,2})=WF4=F5 because WI4=0 and the same invariant Q commutes with negative variables. The separated terminal theorem gives dimension12. Negative stability puts the source in NR3; no Q3-preservation of NR is inferred. These statements do not supply a new raw higher correction or determine a fifth class.

## Replay and immediate-input authentication

I inspected the production verifier and executed it normally and with Python optimization. Both 77-check outputs agree byte-for-byte with each other and RESULT.json. The full arbitrary formal leakage and I2-gauge matrices correctly test the projection and defect algebra without claiming source realization. Reproduce with `python verify.py` and `python -O verify.py`.

All ten immediate public resources were freshly fetched at the exact commits and paths in INPUTS.json. Their remote bytes, SHA256 values and Git blob hashes match the retained copies:

| Input | Commit | Git blob |
|---|---|---|
| 795 | `3f811311d76914a555c7e7d0c5b887b41805aa6c` | `9358ec81c552913fac20f3a92d7b9f7c58105656` |
| 792 | `2f01f18960ce56b8b2a0c1260c277de3c5f916bf` | `76bee93507d1a2d0840926d4e4e27edadfebb7d7` |
| 1019 | `3fb2475ffb275c5789acbaa8f9f84ed272713785` | `bf63c14f76933d59fa7e3ac61aecb3366ac1b442` |
| 1058 | `1435873de29d39e14ceee3de8d879e90f90b437a` | `3d42713aaaf4078e3a1b44d8eb3d9f545daa880c` |
| 1064 | `bfc239e1c8624a0346394e1454b0bea3c976d40d` | `20b3b58b92d4c44d1097d47a9e952c4dfa25b569` |
| 1069 | `41bc20cade3198306c492c0c46399d71eb0d51c4` | `827cd956e2eb574fd7d40d408e0450c8581fd7d2` |
| 1081 | `411b644cdc12938c35b7fedac5bb92664bfc1a47` | `3aa53fa809fa82cef18629cc040cf61fe4eb0a90` |
| 1089 | `f8dfebc8c12cbefd3b17422fa1220629e90af78e` | `7459702e0b6c28aa6605ca34e2cbd98a9d366417` |
| 1113 | `09b03061644e417b44b2ea97a00c73618794c268` | `923cdf608b02448fd24d2f415e06a22e5664ec73` |
| 1117 | `630d92dbca7dba13a99f31f7be94b53e785e18c6` | `b51cc55b7f130840814f022c2c774a66662f2579` |

Exact paths and SHA256 values are in INPUTS.json. This authenticates the immediate inputs, not a recursive reproof of all ancestral geometry. No actual source coefficients, parameters, points, directions, jets or source-instance ranks were evaluated.
