# Independent review: zero endpoint-core restriction

## Conclusion and binding

The theorem is sound: under the retained actual pure-V compatible-radical hypotheses, h|NC4=0 forces R≠0. Equivalently, R=0 forces the nonzero isomorphism NC4/I4→I2. The proof excludes the joint zero conditions, not the separated mechanism or source2 itself.

This review binds to `PROOF.md` SHA256 `a9375537fc958a26fce4ad194c4fd1a9832f25a07e6c737f693a776fb7e47333` and `verify.py` SHA256 `7eea37883b53fe126eca72c0b8c17142cbe8e738ff50b7c04b33379caddf7973`.

## Independent universal check

I independently constructed every coefficient of the 15-by15 map Phi using falling-factorial formulas for monomial derivatives, separately from the production symbolic differentiation code. Its determinant is exactly 5222734824996864=2^25·3^3·7^8 and its rank is15. After the stated apolar identification, its eigenvalues and multiplicities are 4 with multiplicity7, 28 with multiplicity5, and 84 with multiplicity3.

The production full lowering families and simultaneous sl2 commutation correctly identify these eigenspaces with Sym6, Sym4 and Sym2, respectively. The external A factor and the quadratic multiplier are kept distinct. Thus the certificate proves an isomorphism on the entire representation, including all finite-group V, P, D and A channels, not a nonzero value at selected directions.

## Actual quotient transport and mechanism

Under h|NC4=0, h|NR4 descends through the actual residual quotient. Its nonzero D component follows from the unconditional marked D_can and h(NR4)=I2 statements, not the residual-only part of PR1064. The full zero-core case of PR1089 identifies that descended map with a nonzero scalar times C2. This gives the literal Gamma factorization through Phi and pi2, hence residual kernel exactly NC2 and residual rank15.

The target Hom(A,I2) is correctly restricted to J2=ker j2. Indeed QhT v=Tj2v=0 there, and im h∩ker Q=I2. The actual radical orientation gives J2=NR2⊕N0,P, so its common kernel has dimension21. The sandwich places P_h in this kernel. If its separated projection vanished, residual kernel equality would put P_h in NC2, contradicting the retained small-branch exclusion. Hence its projection is nonzero, and K=NC2⊕P_h is an equality of actual embedded subspaces.

This proves the separated hypothesis before invoking the separated descendant results. No residual-large common-kernel conclusion is used.

## Conditional correction and terminal contradiction

If R also vanished, the published symmetry and diagonal identification of the transfer would give B=0. The actual correction k=GTs then lies in the common kernel; its J2 membership also follows independently from j2k=hTs=0.

The genuine separated P multiplication theorem makes Qk injective on A⊗I4 and its image disjoint from I4. Consequently k is injective and disjoint from F2, because QF2=I4. Dimensions9+12=21 give K=F2⊕im k and QK=F4. This is a new use of the separated theorem, not a reuse of a residual-only decomposition.

Combining with K=NC2⊕P_h gives F4=Q2(NC2)+I4. The stated directness is justified as well: the canonical A is not in K, whereas I2 is, so ker(Q|K)=I2; Q2(NC2) has dimension12 and I4 has dimension4. No Q-stability of NC or NR is inferred.

Applying the actual negative variables gives F5=Q3(NC3), using WNC2=NC3, WI4=0 and Q3(lv)=lQ2(v) in the correct degrees and parities. The retained PR1106 proves this exact image is one T of dimension6, in every retained branch. Its proof factors through NC3/I3 and establishes nonvanishing using the actual V image and full joint-negative kernel. Even its upper bound6 would suffice. The separated terminal theorem instead gives dimension12 under the nonzero projection already proved. This is the required contradiction.

The final contrapositive uses only h(NC4)⊂I2, hI4=0 and irreducibility of the quotient D. It does not select the remaining nonzero scalar or prove R nonzero when h|NC4 is nonzero.

## Replay and immediate-input authentication

The verifier was inspected and run normally and with Python optimization. Both 80-check outputs agree byte-for-byte with each other and with RESULT.json. Reproduce with `python verify.py` and `python -O verify.py`. Its arithmetic and universal representation identities supplement the written actual-map argument; they are not source-instance computations.

All nine immediate public resources were freshly retrieved at their exact manifest commits and paths. Their bytes, SHA256 values and Git blob hashes match the retained inputs:

| Input | Commit | Git blob |
|---|---|---|
| 795 | `3f811311d76914a555c7e7d0c5b887b41805aa6c` | `9358ec81c552913fac20f3a92d7b9f7c58105656` |
| 1019 | `3fb2475ffb275c5789acbaa8f9f84ed272713785` | `bf63c14f76933d59fa7e3ac61aecb3366ac1b442` |
| 1058 | `1435873de29d39e14ceee3de8d879e90f90b437a` | `3d42713aaaf4078e3a1b44d8eb3d9f545daa880c` |
| 1064 | `bfc239e1c8624a0346394e1454b0bea3c976d40d` | `20b3b58b92d4c44d1097d47a9e952c4dfa25b569` |
| 1069 | `41bc20cade3198306c492c0c46399d71eb0d51c4` | `827cd956e2eb574fd7d40d408e0450c8581fd7d2` |
| 1081 | `411b644cdc12938c35b7fedac5bb92664bfc1a47` | `3aa53fa809fa82cef18629cc040cf61fe4eb0a90` |
| 1082 | `6f1cf5ad484bd6c3d6608345da576fb1221f8222` | `34cfd846c86f7af4da8db0270e44d70f45e0d3dd` |
| 1089 | `f8dfebc8c12cbefd3b17422fa1220629e90af78e` | `7459702e0b6c28aa6605ca34e2cbd98a9d366417` |
| 1106 | `26ab0ded8bbe635d8aa81798e8fe8a6032e81ce2` | `8b9919723955714338edae3b6c354239f8846e8d` |

Exact paths and SHA256 values are recorded in INPUTS.json. This authentication covers the immediate inputs, not a recursive reproof of their entire geometric ancestry. No actual source coefficients, parameters, directions, points, jets or source-instance ranks were evaluated.
