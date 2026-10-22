# Independent review: PASS

Reviewed on 2026-10-22.

## Exact artifacts

- `PROOF.md` SHA-256: `ab47bd14294583750d64f6f47d1b82ac11abccffe942edab0a2a3169bb831fe8`
- `verify.py` SHA-256: `4d78ffcb0d7dbb9c21ee6c34babbca3bd94f1114f63cd33b5ee488f70b191013`

The review treats the two specified prior results as inputs: PR696 at `958244d6d9d3b326f66c073a9d669717c953ec32` supplies the actual equivariant bidegree-(3,1) map into `A + 2V + 2P + 2D`, and PR766 at `a43b46c98e53716978d0a7750843f2224b4d2408` supplies its nonvanishing for every pair of nonzero inputs. This review audits the new deductions, not the proofs of those prior inputs. Since the map is linear in its second argument, the latter input gives the required fiberwise injectivity.

## Checked deductions

1. **Output module and twist convention.** Equivariance makes the linear span of all outputs a subrepresentation. Semisimplicity over the complex numbers gives the stated multiplicity bounds. If `ga = chi(g)a`, then `g rho(a,h) = chi(g)^3 rho(a,gh)`, so the indicated injection from `D|K tensor chi^3` has the correct twist, rather than its inverse.

2. **Klein-four argument.** Independently recomputed the character multiplicities by Fourier inversion on the four group elements. They are `(0,1,1,1)` for each of A and V, `(1,1,1,1)` for P, and `(2,1,1,1)` for D. The three nontrivial character lines in A exist over the complex numbers. The three twisted source restrictions together require target multiplicities at least `(1,2,2,2)`. These are precisely `z + 2w >= 1` and `x + y + z + w >= 2`, forcing P or D.

3. **Order-10 dihedral argument.** Independently recomputed all four restrictions by exact character inner products over `Q(phi)`, with `phi^2 = phi + 1`, using conjugacy-class sizes `(1,2,2,5)`. In coordinates `(1, epsilon, E1, E2)`, the results are A `(0,1,1,0)`, V `(0,1,0,1)`, P `(0,0,1,1)`, and D `(1,0,1,1)`. The rotation-axis line in A is the epsilon line: reflections have trace zero on its two-dimensional summand and total trace -1. Twisting either two-dimensional irrep by epsilon preserves it. The complete injection inequalities are therefore `x + y >= 1`, `x + z + w >= 1`, and `y + z + w >= 1`. Together with the Klein-four inequalities these are exactly `x + y >= 1` and `z + w >= 1`. Thus no omitted two-dimensional multiplicity condition invalidates the claimed equivalence.

4. **Minimal supports and dimensions.** The two support conditions are equivalent to containing one of A+P, V+P, A+D, or V+D. Their dimensions are respectively 7, 7, 8, and 8. Hence dimension at least 7 follows, and the only permitted dimension-7 representation types are A+P and V+P. This is a lower bound and conditional classification, not an existence claim.

5. **Cyclic restrictions.** The tables for orders 2, 3, and 5 agree with the standard abstract character restrictions. At order 2, the two character lines in A yield the two twists of D, requiring at least `(3,3)`. At order 3 the cubic character twist is trivial, requiring `(1,2,2)`. At order 5, D is regular, so every twist requires `(1,1,1,1,1)`. Each of the four minimal supports satisfies every one of these conditions; adding constituents preserves them.

6. **Bounded verifier.** Read the full script and executed it successfully. It enumerates exactly 54 allowed multiplicity tuples, finds 40 passing tuples, verifies the claimed equivalence for every tuple, and finds exactly the four stated minimal supports. Its dimension-7 and excluded-block assertions pass. An independent count confirms `54 - 9 - 6 + 1 = 40`, by excluding tuples missing one or the other required block. The script uses only abstract character multiplicities and does not inspect any actual-family data.

7. **Independent bundle check.** Fiberwise injectivity gives a constant-rank morphism `O(-3)^5 -> O^dim(M)` on projective 2-space, with locally free cokernel of rank `dim(M)-5`. The inverse total Chern class is correctly expanded as `1 + 15t + 135t^2`. The nonzero first and second Chern classes rule out cokernel ranks 0 and 1 respectively. This independently proves the same dimension lower bound.

## Scope and caveats

The proof correctly distinguishes necessary stabilizer tests from sufficient conditions for a uniformly injective equivariant polynomial family. It does not establish existence in any minimal support, compute the actual multiplicities, or identify the actual output span with the parameter space of possible maps. Its limitations concerning the physical quadric, the fourth Bockstein, and higher-order conclusions are preserved.

No mathematical defect or required correction was found in the reviewed artifacts. The computations performed in this review were limited to the supplied 54-tuple abstract verifier and the small exact subgroup-character checks described above. No actual HM/source coefficient, selected point, derivative, or rank was evaluated. No external service was written to.
