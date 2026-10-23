# Independent review: two D-source endpoint exclusions

Verdict: PASS for exclusion of original zero-based records 32 and 52 under the stated actual D-source and maximal profile (1,1) hypotheses. No blocking gap found. This is a written whole-proof mathematical review with exact regression controls, not proof-assistant certification or a global proof-repair conclusion.

## Frozen artifact

- PROOF.md SHA256: fcc0f3479a921935e68738856bf50178bf91d822087f708ee1636f262c02e6ae
- verify.py SHA256: 15e9caab82b299245678708254760786728b9e1f8496272ddd305f9de1b38994
- RESULT.json SHA256: 21b3e2fbd935ee1708326a39f443e3af4e6b359d65b52b259822e067c80b6ca4

The complete proof, checker and all retained mathematical source texts were read. All six immutable sources were freshly fetched through the GitHub connector, independently compared to retained bytes, and checked against SHA256 and Git blob IDs. SOURCE-AUTH.json records this comparison. The fixed JSON records were checked without regenerating the historical enumeration. The frozen version correctly calls their indices zero-based.

## Mathematical checks

1. The original actual inclusion has constant ambient dimension 30, not the unrelated coefficient-presentation dimension. The imported source and maximal-profile hypotheses supply S rank 13 degree -54, H0(S)=0, L rank 10 and derivative rank at most two. All chains use the actual constant connection.

2. Successive kernels are saturated in the same ambient, since each kernel quotient is a torsion-free image on a smooth curve. The induced G_j -> G_(j-1)(-2) has exactly the next kernel removed. Negative nonzero saturated subbundles cannot be horizontal. Thus the positive nonincreasing ranks sum to 10 and the six capacity cases exhaust this chain.

3. The embedded source polynomial frames have degree at most eight without making their bundle splitting horizontal. Repeated differentiated pairings show F_8 annihilates all frame derivatives through eight. Exact Taylor inversion gives all coefficient vectors, whose span is H by H0(S)=0. This proves F_8=0 globally. The proof supplies this argument itself; the separate jet-bound packet is corroboration, not an unpublished dependency.

4. For pair32, capacity and F_8=0 leave exactly h=7 and equality in every determinant bound. The unique highest exterior-degree line forces each actual composite image to equal the corresponding top subbundle, including no torsion defect. This is established from the determinant and not assumed for general Plucker images. At every transition the top line cannot map to a lower line by degree, and its composite channel is nonzero. Therefore derivatives of the terminal O(-8) have nonzero leading components in distinct successive graded terms through G_0, hence eight independent generic directions. Sym8=P+D then forces the nine-dimensional complete coefficient system.

5. The constant ambient splitting in pair32 follows from the coefficient map of the unique source O(-8) summand: its projection to the complete degree-eight coefficient space is an isomorphism. Its image is a genuine constant complement to N, not an arbitrary Birkhoff complement. Quotient local freeness gives saturation of each actual summand. Derivatives are block diagonal only after this constant splitting is proved.

6. The residual argument uses F=D O(-2)+(W'+T)O(-3)+V O(-4), ambient dimension21, B_F=O(-4)+O(-18), and derivative rank at most one. It does not use A_F or the original record's defect. The residual rank-three endpoint has three line quotients with bounds -6,-8,-10 and equality, giving terminal O(-10). Thus adapting PR1145 to A_F=O2+O4 is legitimate; the proof re-establishes the adapted argument rather than merely citing the differently scoped theorem.

7. A possibly partial Sym10 coefficient quotient is handled by its dual injection into the full apolar space. Actual annihilation yields factorization through Sym6 O(-4). Only V O(-4) contributes, with a nonzero scalar. The invariant common-divisor bound proves the sextic net basepoint-free. All rank-two evaluation-kernel splittings with positive a+b=6 give H1 at twist4 equal to zero, so V times Sym4 spans Sym10. This proves completeness when needed, before the rank13-in-rank10 contradiction. Generic osculating containment extends by saturation; no coefficient independence is silently assumed.

8. For pair52, determinants of arbitrary equivariant graded rank-two bundles are standard lines because G is perfect. Their maps land in W O(1-4j)+O(-10-4j); all possible components are covered. The W occurrence gap gives deficit 1 or at least11. Rank-one maps have deficit0 or at least12. No top-plane, decomposability or saturated-image hypothesis is added. The ordinary capacity bound remains valid even with ramification/torsion deficits.

9. At h=6 the total deficit4 forces four rank-two deficits1 and two rank-one deficits0. The terminal line is O(-6). Its derivatives through six lie in S directly from the kernel chain. Taylor inversion puts its nonzero constant coefficient span in S even for a partial or ramified system, contradicting H0(S)=0. At h=7 the mandatory deficit3 leaves6, while the next positive increments are at least10 and12, so no pattern exists. Together with h=5 capacity failure and h>=8 jet failure this exhausts pair52.

## Reproduction and independent controls

Production verifier was rerun in ordinary and optimized Python modes; both outputs equal the frozen RESULT.json byte for byte: 1,866 checks plus 81 character internal checks.

The independent_check.py here does not import the production verifier or its character library. It uses the closed binomial formula for symmetric-power characters and exact class-size inner products in Q(sqrt5), independently confirming W occurrences and invariant gaps. It sums capacities directly over all six nonincreasing rank partitions, enumerates all deficit choices inside the two finite budgets, checks universal apolar complementary monomial indices and all sextic-net splitting bounds, and checks 3,311 formal Taylor coefficients through degree20. Total: 3,369 checks. Ordinary and optimized runs agree byte for byte. See INDEPENDENT-RESULT.json.

Run python3 independent_check.py and python3 -O independent_check.py from this review directory. Production commands are python3 verify.py and python3 -O verify.py from the proof packet directory. These are universal character and polynomial-identity controls, not actual-source parameter samples or instance-rank computations.

## Scope

Only the two stated D-source records in maximal profile (1,1) are excluded here. Pair50 remains outside this reviewed theorem. Original necessity and actual geometric inputs are explicitly imported written results, not inferred from JSON counts. No other-profile coverage, full-adjoint invertibility, smoothing, algebraicity, generic rank-four or complete original repair is established by this packet. No external write, actual-instance experiment or stopped spike was performed in this review.
