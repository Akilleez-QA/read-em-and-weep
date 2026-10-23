# Independent review: invariant-product branch obstruction

## Verdict and exact scope

PASS. The new argument correctly excludes every compatible idempotent of type (0,1,1,w), including every radical shear, conditional on the stated actual c-d-f occurrence, PR927's represented aggregate interface, and the previously proved universal geometric invariant-product character theorem. The strengthened decision rule and the residual type-F block characters follow. No substantive mathematical gap was found.

Reviewed on 2026-10-23 by an independent review agent. Exact reviewed SHA-256 values:

- PROOF.md: 8374367cbad2c44a0937faf83a2d9ef83bc0c07cbb96d30fab724b08456bef5c
- verify.py: aee81c44ab6e7aa98f3574c5dff94e6fe08e37b91f622d3ec2ad163e5a7d9641
- REPRODUCE.md: a1376a4d18bc1fe8324cdf4a5dbd0bc73ca43b497e7ddff14c74197dd3aac5c6

This review imports the stated earlier geometric theorem; it does not reprove its cone-spinor, preservation, or Ext-annihilator dependencies. It checks the new theorem against the exact original statements rather than substituting an experiment or a numerical rank hypothesis.

## Independent original-source authentication

For each of the following, I separately fetched the immutable commit/path and fetched its Git blob through the GitHub read-only connector. The two returned contents agree, and the local audit-input copy is byte-identical to those contents. I also independently recomputed the Git blob hash from the exact bytes, using SHA-1 of the Git blob header followed by the file bytes.

1. AGGREGATE.md: commit 38235cda736a554ca2c16af504a56e1daf756624; path research/hm/profile11-source127-cdf-aggregate-sharpness/PROOF.md; blob 4dd68998c565b3a34ac95bc8dfa447144a5c9d60; 12,740 bytes; SHA-256 30036ea1ac038e023ff3f147eb104c48585bf741adb19cb3b90022604df80a9b.
2. INVARIANT.md: commit eeb1a11799ca38a60c37f6ba96f263ef8e20dd1c; path research/hm/order-four-quadratic-load/POSITIVE-INVARIANT-VERTEX-RANK-33-PROVED.md; blob 019c1f31773476f0a4877d88632ce5d46fbd4b9f; 2,352 bytes; SHA-256 fc43f4c854b95b487b196cacc2c92d1dde74404bd630e8b39a2baca165749276.

Repository: Akilleez-QA/read-em-and-weep. These are the original immutable inputs, not later summaries. The file-path results returned the same advertised blob IDs.

I additionally read the immutable original sources already cited by PR927 to check notation and the restriction bridge:

- PR818 at f4a73af666900ad2cb34a756d24b88e19dd6feaa, research/hm/negative-truncation-extension/PROOF.md, section 1; returned blob 2ba0a7eee6ef2eb5413683e85618d7902dca3970.
- The splitting/conventions note at db51525015bb7c5e825833d550d08dedf6f6ea96, research/hm/order-four-quadratic-load/ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md; returned blob b93e0b3589ef71cf2c029fd07a6bdb1da8ba92b3.

## Mathematical checks

### 1. The imported invariant theorem applies to the required restriction

PR818 defines K_d=H^1(B(d-1)), N_2=K_3^+, and N_4=K_5^+. Thus its endpoint spaces are exactly H^1(B(2))_+ and H^1(B(4))_+, the endpoints in the imported invariant theorem. The representation conventions retain A=Sym^2(W), the distinct even three-space V, and P=P4 and D=D5; A and V have not been identified merely because they have equal dimensions.

The canonical invariant quadric belongs to Sym^2(T_+): in Sym^2(T_+ direct-sum W), the mixed summand is center-odd, while Sym^2(W)=A is a nontrivial irreducible and has no invariant vector. Therefore an invariant quadratic vector has no component in either of those summands. Restricting aggregate compatibility to q0 tensor X gives e4 Q=Q e2 without any converse or extra compatibility assumption. Invariance of q0 makes Q equivariant. Its imported kernel A+D, image 2V+3P+3D, and cokernel P agree exactly with the original theorem's statement.

### 2. Constituent bottleneck and all shears

Over C the finite-group modules are semisimple. Intertwining two idempotents gives a direct sum of the zero- and one-eigenspace maps. For each irreducible separately, each block's image multiplicity is bounded by the minimum of its endpoint multiplicities. Summing these two independent bounds proves equation (3).

For p_B(w), its target action in the stated coordinates is (y_F,y_B,z) mapped to (eta_w(z),y_B,z). Its kernel is exactly Y_F and its image is exactly Y_B direct-sum graph(eta_w). The graph projects equivariantly and bijectively onto Y_L, independently of w. Thus the zero-eigenvalue block has V multiplicities 1 to 0, and the one-eigenvalue block has 1 to 2. Their combined image contains at most one V, contradicting the imported two. No choice of shear is omitted; no identification of the graph with a canonical complement is made. The separate dimension bound 9+21=30<33 is also correct.

### 3. Exact surviving decision rule

PR927's injection of D(q_+) into C^2 and its idempotent classification are stated for the whole represented aggregate algebra, including singular endomorphisms. Once all p_B(w) are excluded, every nonscalar algebra contains p_F and equals C1 direct-sum Cp_F. Its compatibility equations are precisely chi_B=Q_FB=Q_BF=0. Therefore chi_B nonzero alone forces scalarness, and when chi_B=0 the two cross-component vanishings are necessary and sufficient for the residual C^2 algebra.

The added chi_F=0 observation is valid: the invariant product of X_F's V cannot reach Y_L when the full quotient row is zero. Since Y_F has no V, vanishing of its Y_B component would kill that entire source V. The only remaining source V could then supply at most one target copy, contrary to image multiplicity two. This argument does not prove or assume that chi_F is always nonzero.

### 4. Type-F saturation and intrinsic quotient support

For p_F, the two target eigenspaces are Y_F direct-sum Y_L and Y_B. The respective image bounds are V+P+D and V+2P+2D. Their sum is exactly the imported image, irreducible by irreducible. Both blocks must therefore attain their bounds for every irreducible; equality of total dimensions alone is not being substituted for this character argument.

Subtracting these image characters from the respective endpoints gives kernels D and A, cokernels P and zero. In particular the B map is actually onto Y_B. The proof correctly avoids selecting a particular copy of D in X_F or a particular P line in the F target's multiplicity space.

The quotient map restricted to Y_F direct-sum Y_L has kernel Y_F. Its V constituent therefore maps isomorphically onto Pi_V, and the saturated F image forces the unique source V to map isomorphically there. No analogous assertion holds for Pi_P: the F image's one P may lie in Y_F, or have nonzero quotient projection. Aggregate surjectivity of chi_F does not imply surjectivity of its invariant slice on Pi_P. The proof distinguishes these statements correctly.

### 5. Scope boundaries

The formal examples in PR927 all land in Y_L, so they cannot have this invariant-product image character. They were never claimed to satisfy the additional geometric theorem. For the contextual factorization reference in section 5, I also read the separate proof and its independent review at ../source127-cdf-positive-factorization/. Its constructions preserve those very aggregate maps, so the present statement that they still fail the additional invariant-product character follows directly. The contextual proof was authenticated against commit 1a8fb75aa886f9bb6c07e357759d37630cdd127d, research/hm/profile11-source127-cdf-positive-factorization/PROOF.md, with local SHA-256 5b0dff3dd55c0d9ca9bb26c2b3cbadc3456e6a829ef96aa4e36b7c97639f283c. It is not an imported premise of this branch theorem, and I did not repeat its separate full independent audit.

There is no deduction that an actual c-d-f occurrence has a nonscalar compatible idempotent. Neither the scalar case nor the residual C^2 case is excluded or realized. Consequently this result does not exclude c-d-f, change frontier counts, establish actual-source membership, or supply a full-module lift.

## Checker and reproduction

I read verify.py and ran both python verify.py and python -O verify.py. Both completed successfully with the expected input-authentication, type-B obstruction, and type-F character outputs. The checker uses explicit require calls rather than optimization-sensitive assertions. It performs only arithmetic on four fixed multiplicity tuples and hashes two small source files; it constructs no multiplication matrix and evaluates no actual source instance.

The checker certifies the stated finite bookkeeping and, with the manifest and source copies present, their blob hashes. It does not prove the geometric theorem, equivariance, the restriction-to-q0 implication, sheared eigenspaces, PR927's algebra classification, or the logical compatibility criterion; those require the written arguments checked above. Its documented arithmetic-only mode when the manifest is absent is not an authentication result. In this review the manifest was present, and authentication was also performed independently against GitHub.

No external mutation or publication was performed. No actual HM/source parameter, coefficient, point, derivative, selected map, multiplication matrix, or numerical rank was evaluated, and no large computation was performed. PROOF.md was not edited by the reviewer.
