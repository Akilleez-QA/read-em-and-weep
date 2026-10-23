# Independent review: no thirty-point base orbit

## Verdict and scope

PASS for the full nonzero universal pencil. The exact whole-mirror restriction, homogeneous resultant, exceptional gcd analysis, and finite-group interpretation together exclude every basepoint with stabilizer exactly C2, hence every thirty-point orbit.

This is not an evaluation of actual source coefficients. It does not determine ambient local reducedness at the fifteen-axis orbit or identify any universal coefficient line as an actual source's gate. The corrected scope language is appropriate: the computed p²−t² divisor does exhibit universal fifteen-axis basepoints on the rank-three coefficient line, but it does not establish actual-source occurrence.

Reviewed PROOF.md SHA256:

    605e949f6f543c9603d068a844f34ee13835b13284d2bfaf152126c2a0eb9723

Reviewed verify.py SHA256:

    9e10b22b0feecb6de9cb97098dacc9fe4846f6cf9bd45546d8152643e8a8f929

## 1. Fresh immutable-input authentication

The reviewer independently fetched all four files in INPUTS.json through the GitHub connector at their stated commit references and repository paths. Returned UTF-8 content matched retained bytes exactly; independently recomputed SHA256 and Git-blob SHA1 values matched the manifest. Matching blobs are:

- PR1031 model at 7150cf97eeebe473bcd7c61c1f968c73625d92ef: a7ca4755e50c85fe7fc20a757125127a05de4056.
- PR1035 support theorem at 6effcd9b61b1942447a2c3f136a6776dda213c15: eb0b5dc78615331526b679eea952e4a46f7d01ea.
- PR1036 placement theorem at bb22e239e9423b54487236dba8c4f70f9e6b738f: 718f987511b5bf6144a85fc14e8ef343612a4491.
- Universal-symbol source at 6c724c3b74e2ae4d6992d8c7b99b41c0715d69c0: 0ff4a2fd717842d8df9cf3ce3e3d29fd189bcd6e.

Only the pinned generators and representation conventions are imported from the historical universal-symbol script; that script was not executed. Authentication covers the four direct dependencies, not a fresh replay of every transitive geometric theorem. No pending fifteen-axis theorem is used.

## 2. Genuine finite-group mirror

The first two relevant matrices are the actual pinned binary-group elements h1=diag(i,−i) and h2=[[0,1],[−1,0]], not arbitrarily chosen SL2 elements. Independently taking their symmetric squares yields the displayed A1,A2,A3. The Pi-intertwining identities and the Klein-four relations hold exactly.

The minus eigenspace of A1 is q=0. Thus the projective line used in the calculation is genuinely one of the finite group's involution mirrors. The plus eigenspaces of A2 and A3 have equations q=0,p−t=0 and q=0,p+t=0. Both projective points are stabilized by the entire Klein four. They are therefore the order-two axes of the unique fifteen-point orbit, not points with stabilizer exactly C2. This distinction is essential: an arbitrary mirror coordinate calculation without the pinned group identification would not suffice.

All fifteen involutions of A5 are conjugate. Each individual coefficient combination is equivariant, so its component base scheme is G-stable without any action on the coefficient ratio. Classification on the whole q=0 line consequently propagates to every mirror for the same pencil member.

## 3. Independent reconstruction of the mirror restriction

The reviewer reconstructed B, its alternating maximal-minor row N, and F1=NLR1,F2=NLR2 by iterative exterior multiplication, independently of the production permutation routine. The exact whole-mirror polynomial identity is

    alpha F1+beta F2=(20/3) U²V (sqrt(5) f,0,0,g),

with U,V,f,g exactly as stated in the proof. Both p,t and both coefficient variables were retained as independent homogeneous variables.

Independent homogeneous gcds of the restricted axis-ideal components give U and V. In addition, after dividing by those gcds, the residual component systems generate the unit ideal on both charts of the mirror P1. Thus U and V give the complete projective intersection supports, including the two coordinate endpoints; there is no missing point arising from dehomogenization. Their squarefreeness and pairwise disjointness, including disjointness from p²−t², are exact.

Away from U²V, common base support is precisely the common projective root set of f and g. The fixed factor contributes only already identified C5 and C3 axes. This factorization changes no target or coefficient normalization from PR1036.

## 4. Homogeneous resultant, exceptional gcds, and boundaries

The independent reviewer assembled the fixed-size 6×6 Sylvester matrix directly from the four homogeneous cubic coefficients of f and g. Its determinant is

    −65536 sqrt(5)/2025 · (alpha−beta/2)²
                         · (alpha+beta/2)² · (alpha+beta)².

Using a fixed-degree Sylvester matrix matters when a leading coefficient later vanishes. This is the homogeneous binary resultant, rather than a sequence of affine resultants computed after dropping specialized leading terms. Its zeros leave exactly the three stated projective coefficient lines. The squared factors describe resultant multiplicity; the proof correctly uses the exceptional gcds, not those exponents alone, to classify direction support.

The reviewer independently divided both cubics by the proposed degree-two gcd on each exceptional line. The two remaining linear forms have coefficient determinants

- beta=2alpha, divisor U: −4 sqrt(5).
- beta=−2alpha, divisor V: −4 sqrt(5)/5.
- beta=−alpha, divisor p²−t²: −4 sqrt(5)/5.

Each determinant is nonzero. Hence the residual linear forms have no common projective zero, proving that each claimed divisor is the complete homogeneous gcd. This is stronger than checking that the divisor merely divides both cubics. All three quadratics are squarefree.

The direction endpoints are checked separately. At t=0 the coefficient pair is (alpha,alpha+2beta); at p=0 it is ((alpha+2beta)/5,alpha), up to nonzero common factors. Both maps of (alpha,beta) have rank two. Therefore neither endpoint is a residual common root for a nonzero pencil member. This directly closes the potential degree-drop issue at direction infinity.

At coefficient infinity alpha=0, the resultant is −4096 sqrt(5) beta^6/2025, nonzero whenever beta is nonzero. No additional projective coefficient class is lost by expressing the exceptional lines using beta/alpha. The zero coefficient pair is excluded throughout, as required.

## 5. Propagation and the thirty-orbit exclusion

The complete common-root classification on q=0 permits only U=0, V=0, and p²−t²=0. These are respectively C5 axes, C3 axes, and Klein-four-stabilized order-two axes. None has stabilizer exactly C2.

The exact conjugacy argument therefore excludes C2-only basepoints on every involution mirror. PR1035 establishes that every thirty-point orbit has stabilizer exactly C2 and lies on those mirrors, meeting each mirror in two points. Such an orbit would contradict the just-proved whole-mirror classification. The exclusion is therefore global, for every nonzero coefficient ratio, and does not rely on an unbounded global Groebner computation or a search through possible orbit representatives.

The remaining-support consequence is appropriately bounded by the existing support theorem: only the fifteen-axis orbit and the twelve-point conic orbit remain possible additional supports. Their local lengths and actual-source occurrence are not inferred here. The calculation also need not assume any separate occurrence theorem for the fifteen-axis orbit; its identification follows directly from the pinned Klein-four matrices.

## Reproducibility

The bundled primary commands are `python verify.py` and `python -O verify.py`. The reviewer replayed both: all 32 production checks passed with byte-identical output. Independently executed exterior-minor reconstruction, fixed-size homogeneous Sylvester calculation, residual-linear determinant tests, both-chart axis-ideal checks, endpoint tests, and exact group calculations all passed. These separate methods are documented as executed review checks rather than as additional bundled scripts. The written finite-group and support arguments supply the geometric interpretation of the polynomial identities.
