# Independent review: forbidden secondary target channel

Verdict: PASS within the stated immutable-input scope. No mathematical revision is required. The final proof explicitly states the natural G-equivariance of the actual boundary and distinguishes this secondary target reduction from the earlier ambient first-cup 30-to-24 map.

Reviewed artifacts and SHA256 identities:

- PROOF.md: 49938569c974b55cbc173b2dd8c499fb3c9489a7d61ebaa065bdaf51dd1193ff
- INPUTS.json: 8ca618623f3e2f95eb20c977dc96d0338c675758bbaa592736f15b2305e8f03c
- verify.py: 606e85dd928dd0c4d09ba0ce3fc8372aea152fa6564b9f17955dd1888e27cc7e
- REPRODUCE.md: 39dbd77d8a572bf65e1a4254208a41707ab8bb5e2ce4e1f349aba4765ca37f0c

All three copied inputs were read directly. Their byte counts, SHA256 values and Git-blob identities match INPUTS.json under both verifier runs. This review authenticates their local identities and mathematical interfaces. The originating worker separately reported freshly fetching each pinned original and exactly matching those bytes; this review does not claim an independent remote fetch.

## Mathematical audit

1. **The immediate inputs suffice.** QUOTIENT supplies the actual equivariant Q6=P O(2) directsum W O(-1), rather than an equal-rank substitute. SQUARE supplies the actual square subbundle and its annihilation by beta. SECOND supplies the actual fifth-neighborhood boundary, its G-equivariant construction, its relative cohomological sequence and the exact two-root obstruction criterion. No new evaluation of the actual HM map is required.

2. **The target character is authenticated.** SQUARE identifies H1(End(F_R)(-2)) with Hom(D,A). Trace splitting and H1(O_R(-2))=0 give the same identification for B_R. The trace pairing identifies B_R with its dual; surface Serre duality therefore identifies H1(B_R(-1)) with H1(B_R(-2)) dual. The possible canonical-bundle determinant character is trivial for the perfect group G. Since all named representations are self-dual, the target character is A tensor D=A+V+P+D. Its four multiplicity-one isotypic subspaces and the associated projections are canonical, although chosen identifications with named abstract representations are not unique.

3. **The parameter twists are essential and correct.** The coefficient spaces for the two source summands are Hom_G(P,J tensor Sym2 W) and Hom_G(W,J tensor Sym5 W). The A-target spaces vanish: A tensor A=1+A+D contains no P, while W tensor Sym5 W=Sym6 W+Sym4 W=V+P+D contains no A. This uses coefficient-space equivariance on the entire parameter line, not an illegitimate claim of full G-equivariance at an individual direction. The actual quartic correction remains present inside the surviving target.

4. **Exactly six channels remain.** By self-duality, the first-source multiplicities are those of J in P tensor A=V+P+D, and the second-source multiplicities are those of J in W tensor Sym5 W=V+P+D. For J=V,P,D each is one. Thus all equivariant maps with this source and reduced target form a six-dimensional vector space. The proof correctly does not assert that its actual six coefficients are nonzero, free, independently variable or known.

5. **The cohomology identification is an actual exact-sequence statement.** The layer B_R(-1) has H0=H2=0 by stability and trace Serre duality. SECOND gives p_*E1=K and R1p_*E1=R2p_*E1=0. The long exact sequence of the actual E2-to-E1 extension consequently gives R1p_*E2=coker beta and R2p_*E2=0, with no additional unknown cohomological extension. Surjectivity of K-to-Q6 gives coker beta=coker beta_bar. Since beta_bar has zero A component, its cokernel is canonically A O(4) directsum coker b as a coherent sheaf. This remains valid at rank drops; no local freeness of coker b is inferred.

6. **The kernel statement keeps its extension.** The preimage of ker b under K-to-Q6 is exactly ker beta=p_*E2. Thus 0-to-A O(-6)-to-p_*E2-to-ker b-to-0 is exact as sheaves. There is no assertion of a splitting, no replacement of K by its quotient, and no pointwise base-change conclusion about the kernel sheaf at a rank jump.

7. **The two-root gate loses no obstruction.** For reduced Z of length two, SECOND's source remains H0(Z,K(1)), of dimension 18. Its target factors through the injective 24-dimensional subspace (V+P+D) tensor H0(O_Z(5)) of the old 30-space. Postcomposition with an injection leaves kernel, rank and vanishing unchanged. The unhit six-space is A tensor H0(O_Z(5)). A general Z need not itself be G-invariant; the proof needs only restriction of the globally equivariant family and its canonical target inclusion. It does not claim surjectivity or sharpen the already known secondary rank bound.

8. **The determinantal statement is scheme-theoretic.** In local frames beta_bar is b with three zero rows, and after locally splitting the vector-bundle quotient K-to-Q6, beta is beta_bar with three zero columns. For each fixed minor size the ideals are equal, including the usual zero ideals above the available rank. Local invertible row and column changes preserve these ideals. The conclusion therefore preserves the full determinantal rank schemes, not only ranks or reduced supports. This is not an assertion that identically indexed Fitting ideals of differently presented modules coincide.

## Independent checks and novelty scope

- Ran python verify.py: PASS.
- Ran python -O verify.py: PASS. Explicit exception checks remain active under optimization.
- Independently checked the representation argument by the binary Clebsch decompositions A tensor D=Sym6 W+Sym4 W+Sym2 W and W tensor Sym5 W=Sym6 W+Sym4 W, together with Sym6 W=V+P. An independent invocation of the earlier fixed-character implementation reproduced the target identity and the multiplicity lists (0,1,1,1) from each source for targets (A,V,P,D).
- The verifier uses exact nine-class Q(sqrt(5)) arithmetic and immutable-file checks. It does not evaluate actual HM coefficients, points, directions, jets, derivatives, matrices or instance ranks. The actual sheaf identifications and determinantal claims are established by the mathematical proof, not inferred from its numerical checks.
- A bounded search and reading of the shared SECOND, SQUARE, secondary-quotient, forced-W-extension, first-cup two-types, balanced-first-cup and ambient-fourth-neighborhood material found no prior statement of this A-target exclusion, canonical secondary R1 summand or exact secondary 18-to-24 reduction. The already known ambient FIRST 30-to-24 surjectivity theorem is different and is explicitly distinguished. This is not an exhaustive repository or literature novelty claim.

The contribution is a rigorous exclusion and exact presentation reduction of the actual secondary obstruction. It leaves the actual secondary rank, remaining coefficients, kernel splitting, higher lifting compatibility, opposite-pencil classification and global odd-quadric question unresolved, as the proof states.
