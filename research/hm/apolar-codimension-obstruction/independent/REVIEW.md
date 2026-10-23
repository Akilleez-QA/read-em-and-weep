# Independent review: sharp sextic-channel apolar codimension obstruction

Verdict: PASS. The uniform theorem, stronger nonzero-high-block bound, and both abstract sharpness models are correct under the stated hypotheses. This is a written-proof review with reproducible formal controls, not proof-assistant certification or another actual-profile exclusion.

## Frozen binding and authenticated sources

- PROOF.md SHA256: `18ad6a68fdc672e505d2c9e607152dbe7e6a6d42c20898acbafbd807aaf78fd5`.
- verify.py SHA256: `0d11f210891a3c90add9df62e567ff59c8afac43e455238262bafcce84bb50eb`.
- RESULT.json SHA256: `67921217e9542480a4849a87709f988a63671a1bc858351bb9b3a5f7a97216a2`.

All three complete public input files were independently fetched through the GitHub connector at their immutable original commit URLs. The full PR1145 and PR1147 proofs were read. Fresh retrieved bytes match the packet, declared SHA256 values and Git blob IDs exactly; AUTHENTICATED.json records the bindings. In particular PR1147 is at `176645bb2f022b68f86414ced87667a45e4930e2` and PR1145 at `2e2da6c1226b7671c79e55b3c9f8bb14a0f8719b`. The universal multiplication conclusion from PR1147 is the mathematical input, not merely its character identity.

## Mathematical checks

1. The coefficient map of the actual line is allowed to be a proper quotient initially. Constant differentiation commutes with that quotient even if its projected osculation is dependent or ramified. Dual injection therefore correctly pulls annihilation back to the full universal degree-n osculating bundle. Generic annihilation extends everywhere as a vanishing bundle morphism; completeness is not assumed in this step.
2. With n=d+6 and k=d-1, the osculating fibers are l^7 Sym^(d-1) W. Their apolar annihilator is precisely l^d Sym6 W, of rank seven and degree -7d. The monomial pairing calculation and complementary dimensions establish equality, while multiplication supplies a constant-rank saturated universal subbundle on both standard charts.
3. Every higher-degree source block has zero ordinary Hom to that bundle. The sole V O(-d) channel is scalar because Sym6 W contains V once. A zero scalar would force the nonzero coefficient space R to annihilate F identically and hence give constant sections of S, prohibited by hypothesis. The nonzero scalar consequently puts every l^d V inside the fixed R*. PR1147 supplies their full span for all d>=2, proving that the coefficient map is injective.
4. The high block lies in the actual constant kernel of H->R*. Its rank bound is exactly codimension(F)>=n-2. Since F_high is a bundle direct summand of the saturated F, it is itself saturated in the original constant bundle. Its quotient in the smaller constant kernel is torsion-free. Equal ranks would therefore make F_high equal to that constant kernel, contrary to strict negativity when F_high is nonzero. This proves codimension(F)>=n-1 in that case, without assuming a horizontal Birkhoff splitting.
5. The first sharp model V O(-d)->Sym^(d+6) W O by multiplication with l^d is fiberwise injective and saturated. Its full coefficient span, supplied by PR1147, gives no constant sections in the dual quotient. The complete line l^n and all derivatives through order d-1 are contained in that annihilator by the same apolar identity. Its rank is three and codimension n-2.
6. Adding W O(-1)->Sym2 W O, fiber lW, gives a genuine saturated negative high block of rank two. Its span is the whole three-dimensional constant factor. The direct sum still satisfies the no-constant-section and osculating-containment hypotheses and has codimension n-1. Thus the stronger bound is also sharp. The source high degree -1 is strictly greater than -d for all d>=2.
7. There is no parity restriction for an arbitrary ambient representation, which may contain both central characters. A center-even ambient forces n even through the equivariant nonzero line inclusion. For even n both displayed sharp examples have center-even ambients. No unsupported odd center-even example is asserted.

## Reproduction and independent evidence

Both normal and optimized execution of the supplied verify.py reproduce the retained RESULT.json exactly: 11,736 formal controls. The independently written independent_check.py executes without importing the production checker or character module and reproduces its own RESULT.json normally and under optimization: 28,355 controls, including 2,450 full formal apolar pairing identities for n=8 through32, two-chart triangular immersion controls, source authentication, both sharp rank bounds, parity, and rank/codimension equivalences. The polynomial parameter remains indeterminate; no parameter value or actual source instance is sampled.

From the production packet run `python verify.py` and `python -O verify.py`. From this review directory run `python independent_check.py` and `python -O independent_check.py`; both outputs equal its distinct RESULT.json. The review's originals/ directory contains the independently retrieved public sources required for its checks.

## Scope

The unbounded theorem is proved by the bundle argument; finite formal tests are supporting evidence only. It gives a reusable sharp obstruction for any source satisfying the stated actual osculating hypotheses. Those hypotheses still require proof in each application. The n=10, rank16, ambient21 case was already excluded by PR1145 and is not counted again. The abstract sharp models are not asserted to occur in HM geometry. No actual-instance coefficients, points, parameters, jets or ranks were evaluated, and no full profile11 closure or original proof repair is established.
