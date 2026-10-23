# Independent review: reverse c-d-f quadratic intertwiners

## Verdict and mathematical assessment

PASS for the structural argument in the final bytes below, for fixed, parameter-independent G-equivariant endpoint pairs intertwining the invariant Q and every negative quadratic. This review does not extend the result to parameter-dependent formal chain maps or maps for a single chosen direction. The parameter-independence restriction was made explicit before final freeze. The complete proof, verifier and all immediate dependency proofs were read; the immediate inputs match the exact copies already reviewed in the preceding c-d-f reviews.

## Endpoint-to-middle reconstruction

The middle-extension lemma is valid under its two distinct hypotheses. Source generation allows every middle vector to be written as a sum of A_l x. Applying every target B_m to a proposed image of a zero relation gives zero by the endpoint quadratic intertwining equations. The target joint-kernel condition then forces that image itself to be zero. Thus the definition is independent of all relations, is linear on the full source middle, and intertwines the second arrows as well as the first. Uniqueness follows from source generation. Equivariance follows from uniqueness, since the family has equivariant parameter action. Mixed products are retained: symmetry and polarization in characteristic zero recover B_m A_l from the complete quadratic family. Checking only two squares would not suffice.

Both hypotheses are actually verified for F→B. PR924's same-variable reconstruction identifies the source multiplication with W⊗H⁰(O(16))→H⁰(O(17)), a universal surjection. It does not require evaluation of the balanced F parameter. On the target B, the actual B-arrow kernel presentation twisted by one has global-section kernel H⁰(E_B(1))=H⁰((V+P)O(−3))=0. The coefficient arrows are the same fixed B_u,B_v, up to the common determinant-one convention. This is the required joint kernel, not merely pointwise surjectivity of individual arrows.

The block kernel presentation is justified naturally, rather than by ranks alone: the actual total E presentation is the kernel of the B-arrow sheaf map; the simultaneous fixed-pencil decomposition and its block idempotents split that exact presentation. Under the covariant reconstruction its B summand is precisely E_B. The original actual-presentation note read in the preceding review explicitly gives the total presentation. PR924's source-specific constant decomposition and simultaneous natural reconstruction preserve these marked summands.

The reconstructed full F→B pencil morphism must vanish because its extension by the source F projection and target B inclusion is an element of PR924's entire represented algebra supported only in the absent F→B block. The algebra includes singular maps; no invertibility or projector compatibility with Q is presumed here.

## Exact lost endpoint ambiguity

On the quotient negative pencil, N₂,L=0 and all quadratic images from X_F land in Y_F. Restricting a reverse endpoint pair to F therefore kills both f₂ and f₄|Y_F by the reconstruction argument. Conversely any G-map Y_L→Y_B, with the other components zero, intertwines every negative quadratic. Its dimension is exactly one V multiplicity plus two P multiplicities, hence three. This is an exhaustive description, not an upper bound or a generic rank calculation.

Every nonzero such pair fails full-linear extension by PR924's isolated B vertex. This explicitly prevents conflating the full-linear and quadratic-only Hom problems. The proof reconstructs only the F component, not the ungenerated L middle component.

## Actual generation eliminates the residual maps

The exact generation input is PR935 Section 3, equation (5), Y=im Q+im q₋. For independent source checking, the reviewer also read PR925 and PR933 in full from existing immutable copies. Their Git blobs match the exact IDs quoted in PR935: becd3300950c2379d1f03294863d8335a83a1087 and a428ac4b4b8cb6b67b7b8e3b1625352468adeb05.

PR925's degree-zero parity argument gives an equality of embedded actual images Y=im q₊+im q₋, with q₋ the complete Sym²W aggregate B_u A_v. PR933 gives equality of embedded actual positive-coordinate images im q₊=im Q, not merely matching representation characters. No assumption from its separate conditional Type F corollary is needed. Their combination is consequently applicable here under the actual c-d-f hypotheses.

One-sided Q preservation and actual negative-block preservation make the B-source contributions vanish after passage to Y/Y_B. Thus the quotient is spanned by im Q_T and its negative-quadratic images. The residual f₄ kills the latter and, by the invariant intertwining equation with f₂=0, also kills the former. Hence f₄=0. Equivalently projection of the generation identity to Y_L shows that the Y_L component of Q_T is onto, so no nonzero target-only map survives.

This argument does not substitute scalar commutant for endpoint reconstruction, and it does not assume complementary Q preservation. It proves the disappearance of the fixed reverse chain-map mechanism. It does not prove rκ≠0, rκ=0, actual one-sided preservation, an actual cubic value, or any source/pair exclusion.

## Review restrictions

Only universal representation, polynomial, sheaf-cohomology and formal map arguments were used. No actual HM coefficients, parameters, points, jets, instance ranks or local-model spike were evaluated, and no public writes were made. Imported geometric inputs are retained as established theorems rather than reconstructed through every transitive dependency. This review itself is verification, not an additional deduction.

## Supplementary generation-source authentication

The exact original generation inputs consulted beyond this packet's immediate manifest were:

- PR925: SHA-256 af574b04eb9d96a1117f8cfee327429bb9e38b4bad3932db4f45af849d4480a2; Git blob becd3300950c2379d1f03294863d8335a83a1087.
- PR933: SHA-256 6dcdb17796696fe627489d865ba0a5e2913305dd9c5cbe07d87b7453c9d6b0e1; Git blob a428ac4b4b8cb6b67b7b8e3b1625352468adeb05.

They were read from the existing source126-nilpotent-generation input copies and matched the PR935 pins. Authentication here is independent content-hash comparison, not a fresh remote commit retrieval.

## Final verification

Independent normal and optimized executions both pass all 36 checks and match the stored JSON reports. All three immediate input SHA-256 values and Git blob hashes match their manifest pins. The final proof and manifest match the author’s frozen hashes. Explicit exception checks remain active under Python optimization.

The verifier includes exact universal binary multiplication/relations, the target degree vanishing, and both explicit negative controls for absent reconstruction hypotheses. The missing-source-generation control was strengthened during review from placeholder inequalities to a complete symbolic toy: zero degree-two sources, one-dimensional middle and target spaces, opposite source/target coefficient arrows, an injective target joint map and vacuous endpoint quadratic equations, yet an impossible middle intertwining equation for every symbolic middle map. This changes no theorem.

The tuple-rewrite relation checks and formal generation distributivity are consistency checks rather than independent formal proofs of the lemma or the geometric generation theorem. The actual-reconstruction and generation arguments reviewed above remain essential. No proof-assistant certification or actual-instance experiment is claimed.

## Exact final reviewed hashes

| File | Bytes | SHA-256 | Git blob SHA-1 |
|---|---:|---|---|
| PROOF.md | 9266 | 6e16af3e6c5eefe938b91c7c046b3ad07fa6956f0ceed3fac25a971c4390004b | 6da87baf51825d2d482f60c4176aa024e94c56dc |
| verify.py | 4695 | c170c485f07a8468194684f0ccf3eaca641c15ecb4304a94fc41be81f9f2b354 | f692e180d055d7a665c45c50ffaa07dc105ba522 |
| INPUTS.json | 715 | e0d20c96fe4c1bd2024ebe9131c4f37fa99cecce609eb3ef689014f07e73bf19 | c4ab11eaf319a6870360573afb479e72c1e16c95 |
| README.md | 853 | ac13ff2dc3afeb616e2b547dec6027589fa3e9a8e54804d9957dc8cac168c8bf | 52cc1498e71d3229471fd79f35854840e8574bfb |
| checks-normal.json | 279 | 7e81263e061098297f7822738c5dc6f4554bd7a0fd35f00e700d50c183d4756f | ab9f7583f51fd81ca38b217120e365cd8bf836fd |
| checks-optimized.json | 279 | 7e81263e061098297f7822738c5dc6f4554bd7a0fd35f00e700d50c183d4756f | ab9f7583f51fd81ca38b217120e365cd8bf836fd |
| inputs/1001.md | 7335 | e07a59e7b8e8d35b2f9a164515ff65eeddeca4baca4a0964c731b36b7713e38d | eebebae694f59e786aaebc64c3838d732b2a3832 |
| inputs/924.md | 18095 | 0d740d6f70de924b0442af71cb37e050165efbe9ab984a76f0e1e40b5d27a599 | 83f5aee293995257459229e6b323522224ce8f3d |
| inputs/935.md | 11636 | 06fe9d6bf5f51d1d38ff5f594f93703cf91b48d6cffcf7256c3e281de631365d | 187fe2a8c1499e11afdb5002091aa3c144e1b4a3 |
