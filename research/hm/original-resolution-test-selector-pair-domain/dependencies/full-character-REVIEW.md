Editorial scope: This is a mathematical source edition. Historical review and check statements describe the original artifact, not a fresh run. Supporting snapshots are dependencies, not additional new results. Later PR145 mixed-class vanishing supersedes historical unknown mixed-class status; it does not resolve the six pure diagonal conditions.

# Independent review: exact raw full-character and strict-End membership

## Verdict and reviewed version

**ACCEPTED.** For the declared product-root model and the exact frozen raw mathematical denotation, every literal residual family has full deck character. The residual R is a meromorphic **row-End(cohomology) cochain component**. The strict-resolution degree-zero statement starts at j(R), not at R. The exact J0–J3 then have strict degrees 0, −1, −2, −3 and full deck character, with branch-safe coefficient multidegrees (−2,−2,−2,−2), (−3,−3,−3,−3), (−4,−4,−4,−4), (−5,−5,−5,−5), respectively.

No mathematical correction is required in the reviewed final proof. This review independently checks the raw branch characters, the actual all-standard-chart formula for j, the two typed homotopy branches, and the finite-flat pushforward. It does not infer closure, a global section obtained by gluing different Čech tuples, a cohomology class, or any detector result.

The reviewed producer PROOF.md has SHA256:

    ce17740962e0f5e7dd23fd1bc3613704ea8d83a81d343827304338e2e686b94f

The reviewed producer checker has SHA256:

    33c34f0226cf17444fc178d7edc2917bc2dfca8e33175315c9a8fc5a1897b364

The exact reviewed proof is retained as reviewed-PROOF.md. The producer's final manifest authenticates twelve inert source/dependency files, including independent accepted reviews of the root/frame, legal-free-homotopy, raw-block and complementary-scalar dependencies. The scalar proof used here has SHA256 ffdcd74399b4265b126ed7ebf5530a369566f6a72d12e2912f3474f20de00601 and is independently accepted unchanged. Its result is used only for raw scalar typing and character, not to import a full-residual purity conclusion.

Only inert source/dependency text, AST structure and hand-written integer metadata were read or checked. No frozen source module was imported or run; no physical source, model polynomial, rational field object, actual matrix product, jet, detector or residue was evaluated. 

## 1. The exact route and full branch coverage

The raw source uses RawSource(model.M), whose override T is PhysicalModel.s_raw. The lift receives that object's residual and the same raw Mat. It therefore does not silently substitute the compiler's distinct N14 complete-solver leaf. Raw Mat.inverse is the entrywise 2-by-2 adjugate; the proof need not evaluate or simplify a determinant. Mat.D denotes the invariant curve derivation V_d entrywise. This is a mathematical denotation, not a newly proved backend-correctness claim.

The frozen compiler has exactly seven kinetic slots and three gerbe slots within the outer G# normalization, two Fk slots outside it, and four ordered terms in each of E12 and E34. Its four mu2 derivative tuples are (0,2;1,3), (0,3;1,2), (1,2;0,3), (1,3;0,2). All use each coordinate once. The seven kinetic slots become fourteen summands upon expanding mu and mu2; the two Fk slots become six upon expanding each F's b and two mu terms. Together with the three gerbe and eight E summands, the independent check examines thirty-one expanded summands per owner-mask triple. This count is only metadata; it is not a matrix expansion or source evaluation.

Let a=m_i XOR m_j, b=m_j XOR m_k and g=m_i XOR m_k. Then a XOR b XOR g=0. Each diagonal entry of D_m and its inverse has character m; primitive coefficients are invariant. Consequently g_ij and its entrywise adjugate have character a, and similarly for the other edges. This remains true when an entry is zero.

For every deck involution σ, σV_dσ^−1=χ_d(σ)V_d. The finite identities V(x)=y and V(y)=(3x²−1)/2 prove this directly, and the infinity identities V(t)=−u and V(u)=(3t²−1)/2 prove the same identity in the regular infinity algebra. Character is therefore **toggled**, including when its bit was already present. It is not generally correct to append an odd factor without reduction.

For a pair p, the two differentiated edge characters in each k_p summand sum to p. Thus k_p has character p and u_p(edge)=g_edge k_p has character edge XOR p. Each mu_p term adds p to the two input characters; each mu2 term adds 15. With p=3 and q=12, outer G# normalization makes each kinetic and gerbe slot character 15. F_p has character p because its b term has that character and g XOR b XOR a=0 in the normalized curvature term. Both F_q k_p and F_p k_q therefore have character 15.

The raw B_(o,d) blocks and q_(ij,d) each have character d. In every one of the four resolution blocks of s_raw, both wedge traces and all four endpoint-linear terms have character p. The final qq term does too. This retains all twenty-five expanded scalar terms. The accepted scalar theorem independently supplies their exact all-chart tensorial interpretation and branch-safe coefficient construction.

The E currents obey character(A# V_d A)=d and character(A# B# (V_d B) A)=d. A derivative of a q-pair scalar in a p-direction has character q XOR d; multiplication by the complementary p-current gives q XOR p=15. All four terms in each E call pass separately. Tracefree projection preserves the resulting character, since its diagonal correction is tr(M0)Id. No matrix cancellation, cocycle identity, inverse cancellation, residual vanishing or closure was used.

## 2. R's intrinsic interpretation and the exact j frame formula

The product-root theorem fixes the actual legal root frame e_i=ν_i e_ref, the standard square-line frame ℓ_A=τ_A^−1ℓ_ref, and

    c_iA=e_i²/ℓ_A=ν_i²τ_A.

This c is a regular unit on the stated legal/standard intersection. At infinity it is the appropriate t or 1−t² factor, rather than an asserted square root of a standard transition. No square root of τ is necessary.

Write I_A=I_i(v_A) and P_A=P_i(v_A). The homogeneous column and row degrees imply, on the common rational comparison locus,

    I_ref D_i = ν_i I_A diag(1,c_iA^−1),
    D_i^−1 P_ref = ν_i^−1 diag(1,c_iA)P_A.

These are exact identities with the frozen leaves. The exterior ν_i and ν_i^−1 cancel in their composite with R^t. Hence the standard degree-zero End coefficient is exactly

    j_i(R)_A=I_A diag(1,c_iA^−1) R^t diag(1,c_iA)P_A.

This derivation independently checks the producer's formula. It neither replaces the two differently weighted I columns by one weight nor drops the root factors before accounting for them.

For A→B put λ=τ_B/τ_A. Then I_B=I_A diag(1,λ), P_B=diag(1,λ^−1)P_A and c_iB=λc_iA. Substitution cancels the λ factors on both sides of R^t and gives j_i(R)_B=j_i(R)_A. Thus this really is a strict degree-zero End section on each component's intersection, in all standard charts.

The actual owner cohomology frame is fixed during a standard-chart change. Its common-reference columns are I_ref D_i and have the same deck character m_i. Deck conjugation in End(cohomology) cancels this scalar frame character. Therefore full character of R's coefficient matrix is also its intrinsic endomorphism character. This does not identify End(cohomology) with a globally trivial four-dimensional bundle. A rank-two row-End matrix and a strict End(K) block are different objects, and the proof keeps them distinct.

The B terms are differences of two connections, so their common ambient derivative corrections cancel only after both the split and old connections have been transported. This is supplied by the accepted raw-block/scalar dependencies. The proof does not assume connection matrices individually transform tensorially, reset the old connection at infinity, or assert covariance of ordinary derivatives under an arbitrary owner-dependent regauging.

Each R attached to a fixed Čech tuple defines a meromorphic endomorphism in its specified first-owner frame. Agreement across standard representations of that component is enough for the claimed membership. Different tuple components need not agree, be closed, or glue to one global section. Applying j first places the coefficients in the common ambient resolution before the literal alternating restrictions.

## 3. Strict degrees, supports and equivariance of the lift

The original-resolution h leaves have degree −1, while E=I_phys P_phys has degree zero. Their characters are zero: both physical leaves have character m and their intermediate frame factors cancel; the unweighted h leaves are base-rational. The exact homotopy is the pair of typed branches h_v F and (−1)^r E F h_(u+1), the latter only when v=1 and u<3. Both preserve character and lower degree v−u by one.

Starting at block (1,1), the source predicates give exactly the possible supports:

- J0: (1,1)
- J1: (1,0), (2,1)
- J2: (2,0), (3,1)
- J3: (3,0)

They have degrees 0, −1, −2, −3. These are permitted supports and make no nonvanishing claim. Their matrix-entry multiplicities are 225,225,80,10, while the complete ambient strict End spaces in these degrees have multiplicities 354,245,80,10. These numbers clarify that the four repeated entries in a multidegree are not a direct-sum multiplicity.

The accepted root/homotopy bridge gives h_B=λ^−1h_A and E_B=E_A in the actual square-line frames. Applied to a degree-r input with F_B=λ^rF_A, both branches have law λ^(r−1). The same chart factor is independent of the selected owner and therefore commutes with restrictions. Induction proves Js,B=λ^−sJs,A. Deck-stable owner opens and restrictions preserve character, so every component is full-character in its actual strict End bundle.

This is an undifferentiated homotopy result. It does not make a differentiated h covariant by itself, invoke the separate differentiated-boundary cancellation, or establish any HPL class identity.

## 4. Branch-safe pushforward and coefficient lines

On each standard base chart with ring R_A, the product curve algebra is

    R_A[z_0,z_1,z_2,z_3]/(z_d²−f_d).

Successive monic division makes it a free R_A-module on the sixteen square-free monomials. This includes the ramification locus; no z_d is required to be invertible. Invariant base localization preserves this direct sum. The full-character coefficient is the R_A-linear coordinate projection onto z_0z_1z_2z_3. Consequently any invariant factor clearing a full-character section clears its extracted coefficient as well. Literal division by a vanishing branch function would not prove this statement.

The common N twist cancels in strict End(K). A degree-r block is a copy of N^(2r)=q*O_Y(r,r,r,r). The odd basis changes by z_all,A=τ_A²z_all,ref and its line frame by ℓ_A^r=τ_A^−rℓ_ref^r. Equality of the actual section yields coefficient transition b_A=τ_A^(r−2)b_ref. This is the multidegree-(r−2,r−2,r−2,r−2) line. Taking r=−s gives the claimed four lines and nothing stronger.

Regularity after a particular clearing product still uses its independent all-chart pole theorem. Purity alone provides no pole bound, and this packet does not claim that an uncleared expression is regular. Ramification multiplicity is respected because the argument uses the free finite-flat algebra and the actual u=t²y transition.

## 5. Novelty relative to the existing results

Product-root §8 proves the general line dictionary for a strict degree-r full-character section **after membership and degree are established**. Its concluding limitation explicitly leaves particular source/residual attribution open. Legal-free-homotopy likewise preserves a character already known for its input. The present exact branch ledger and j frame identification supply this missing input for the frozen raw R and J0–J3.

The current inner-boundary proof is pinned at commit 4c0e965b4de72e43c39ba863f9aa8eea15571851, blob 1941cb00c420185d976de2c43e51b33498019a25; its supplied exact content has SHA256 3ff8e0634cff39143f2ab57b00741540f545e947a6ae978ca9741bb6f0f5de1d. Its §3 projects a specially treated differentiated boundary expression to full character and explicitly does not need purity of every unselected intermediate entry. That projection theorem neither contains nor obviates this complete raw purity theorem. Conversely, this theorem does not replace its derivative-anomaly or boundary-domain argument.

The precise new claim is rational source-bound membership and full-character purity of the complete undifferentiated raw residual/lift. No novelty is claimed for the general pushforward line identity, the existing raw scalar theorem, or the current differentiated boundary theorem.

## 6. Independent static checks and verification limits

The producer checker was inspected before execution. It reads snapshots as bytes/AST only; its remaining operations are character, degree and frame metadata. Independent reruns in ordinary and optimized Python are byte-identical, preserved as producer-normal.json and producer-optimized.json.

The separately written check_independent_metadata.py authenticates the two frozen source SHA256 values, inspects literal source slot counts, the raw override, adjugate syntax and block predicates, and computes only independent integer metadata. Its normal and optimized outputs are also byte-identical. Results include:

- 4,096 legal-mask triples, thirty-one expanded residual summands each: 126,976 successful full-character checks
- 300 raw-scalar term checks over all twelve ordered distinct pairs
- 16,384 physical-j root/chart cases, including all sixteen legal masks and all 256 standard-chart pairs
- 4,096 strict-line chart/coordinate checks across all four stages
- The exact supports and both actual-support and ambient-End multiplicities above
- Eight active rejection controls for omitted normalization, missing derivative flips, unmatched physical-leaf characters, odd homotopy, wrong degree, missing c transition, missing odd-basis transition and omitted E slot

The rejection controls are integer-counterexample tests, not executions of mutated physical programs. Static source hashes and AST contracts bind the displayed formulas but are not proofs of curve geometry, finite-flat freeness, arbitrary arithmetic semantics, derivative implementations. The mathematical arguments in this review and the accepted dependencies supply the geometric conclusions. The clearing weights 54/29 and standard-factor exponent 5251 are retained. Higher attribution and closure remain outside this historical theorem.
