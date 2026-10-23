# Independent review: global alternating-transfer vanishing

## Verdict and frozen scope

The global theorem is sound under the retained actual-source hypotheses. It proves j3(ker Q3)=I3, combined T-multiplicity rank four, and κ=0 without selecting either remaining endpoint-sixteen mechanism. It also proves the stated common-kernel quotient and rules out an odd nullhomotopy. It does not prove the diagonal transfer nonzero or exclude full transfer zero.

This review binds to:

- `PROOF.md` SHA256 `8c3591fbe0c79f553a71aa4d7c7edbf0f6cc7a12557921f95cd02c777afd1d97`.
- `verify.py` SHA256 `03406cecae613ee57e8b07966f2dc64ba76c8910b4a5f6c9d4481d559251cfd2`.

## Actual-map and normalization audit

1. **The lift is defined on the stated domain.** The actual residual submodule property gives δ(NR3)⊂W⊗NR4. PR1064 supplies NR4⊂im Q2. Thus the right inverse G is only applied on its legitimate domain. Actual polynomial commutation and Koszul exactness give Q3 X(Id⊗G)δ=0. Radical intertwining and hQ2=j2 give j3 X(Id⊗G)δ=X(Id⊗h)δ. Both are literal equalities of the indicated maps; neither assumes Q preserves NR nor extends h as a graded module map. The invariant quadratic preserves central parity and the negative coordinates reverse it.

2. **The section does not affect the detected radical image.** The difference of two right inverses lands in ker Q2, annihilated by j2=hQ2. Consequently the two lifted maps differ by a map into ker Q3∩ker j3. The resulting θ is independent of the section, although the lift need not be.

3. **Nonzero restriction case.** If h|NC4 is nonzero, it is onto I2 because it kills I4 and the quotient NC4/I4 is the unique D. The actual isomorphism δ:NC3→W⊗NC4 from PR1068, followed by W⊗h and the coherent surjection W⊗I2→I3, makes θ onto I3. Mere equality of dimensions would not replace the pinned δ restriction.

4. **Zero restriction case, without a small-endpoint assumption.** If h|NC4=0, exactness gives a descended hbar on N8,4. The actual marked D_can projects isomorphically onto D8 and maps isomorphically under h to I2, so hbar is nonzero. Its V+P channels vanish by equivariance. In the pinned transvectant quotient it is therefore λ i2 C2 with λ≠0. This conclusion follows directly from the zero restriction and marked maps, not from an endpoint-nine implication with a discarded premise.

5. **Coherent quotient formula.** Naturality of the actual quotient arrows identifies the descended θ on A⊗Sym5 W with λ i3[x(a,yg)_2−y(a,xg)_2]. PR792 supplies i2(f)=f12 f and i3(g)=f12 g with ordinary inherited multiplication. Thus the two terms have the same λ; independent choices of abstract D and T normalizations are not being mixed. No splitting or chosen lift of N8 into NR is required.

6. **Independent universal certificate.** A separately written exact symbolic computation expanded all eighteen quadratic/quintic coefficient pairs and also the fully formal expression. It verified

   x(a,yg)_2−y(a,xg)_2=2(a,g)_1.

   Its exact 6-by-18 coefficient matrix has rank six. The sign agrees with δ=x⊗Y_y−y⊗Y_x and the pinned unnormalized transvectants. This proves surjectivity in the zero restriction case; no actual source parameter was substituted.

7. **Consequences and their limits.** In both cases θ is onto I3 and comes from vectors in ker Q3, so j3(ker Q3)=I3. The exact rank formula gives combined T-rank 3+1=4. The contrapositive of PR1085 then forces κ=0. Subtracting I3 from the kernel character in PR1086 gives K3=3W′+3S+2T; the pinned actual inclusion F3⊂K3 gives K3/F3=2W′+3S, dimension sixteen. The nonzero action on ker Q3 excludes the odd nullhomotopy. Symmetry and polarization concern B alone and do not assert commutation of ambient mixed-direction operators. R=0 implies B=0, but neither possibility is excluded.

8. **Jordan consequence.** On the three-dimensional T multiplicity space of ker Q3, j3 has rank one, image I3, and square zero because j3 kills F3 containing I3. Its Jordan type is therefore (2,1). Its two-dimensional T-multiplicity kernel is exactly the T-isotypical part of F3: the actual inclusion and equal multiplicities prove equality, not just abstract isomorphism. This is confined to the stated kernel and makes no claim about a Jordan form on the full source.

## Input authentication

All seven complete originals were independently retrieved at their exact repository commits and paths from `INPUTS.json`. Retrieved bytes matched the retained files exactly; independently computed SHA256 and Git blob hashes matched the manifest. The authenticated commit/blob pairs are:

| Input | Commit | Git blob |
|---|---|---|
| 1019 | `3fb2475ffb275c5789acbaa8f9f84ed272713785` | `bf63c14f76933d59fa7e3ac61aecb3366ac1b442` |
| 1064 | `bfc239e1c8624a0346394e1454b0bea3c976d40d` | `20b3b58b92d4c44d1097d47a9e952c4dfa25b569` |
| 1068 | `05e8b33eb87e9f36aa30500145cc42bc0ea00df8` | `5ae07c02624d70c0ccd33d7ec34202504173ff83` |
| 1085 | `7d1c49ea66c54039f6adbbc27cac54222961784e` | `2988fbbb5ed316124769c7157c0592e4c87aaa0f` |
| 1086 | `acb56908fd28ff019515b7ad9945f9b539f8614a` | `d3d0f0546c5b2b7d2453929364287b35f03e4d2e` |
| 792 | `2f01f18960ce56b8b2a0c1260c277de3c5f916bf` | `76bee93507d1a2d0840926d4e4e27edadfebb7d7` |
| 795 | `3f811311d76914a555c7e7d0c5b887b41805aa6c` | `9358ec81c552913fac20f3a92d7b9f7c58105656` |

This authenticates the immediate inputs and audits their use, without claiming a recursive reproof of their full geometric ancestry.

## Reproduction

Independent executions of `python verify.py` and `python -O verify.py` each passed all 64 checks. Outputs were byte-identical to one another and to `RESULT.json`. The checker uses explicit exceptions rather than optimization-sensitive assertions. Its type labels and formal controls do not independently establish actual-map premises; those were separately audited above. The additional independently written universal identity/rank computation also passed.

No actual HM coefficient, direction or source-instance rank was evaluated. Independent mathematical review completed 2026-10-23.
