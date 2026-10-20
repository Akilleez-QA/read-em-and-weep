Publication context: this retained proof or audit may describe an intermediate bound or then-open branch. Read the unit overview for the current scope and later implications. Historical mathematical review is not a new formal verification.

# A universal exclusion of a length-five isolated defect

## Result and scope

Let (R,m,k) be the local ring of a smooth complex fourfold at a point fixed by a finite group H. Let M be an H-equivariant reflexive R-module of rank two, free off the closed point, with equivariantly trivial determinant. Assume H contains G=C5⋊C4, with clock generator Z and multiplier generator T, such that W=m/m² has the four distinct nontrivial C5 characters and T permutes their lines transitively. Then

    length_R Ext²_R(M,R) ≠ 5.

This uses only universal local algebra and abstract stabilizer representations. In particular it does not evaluate any physical source-model matrix, operation, chosen input, rank instance, jet, or residue. Combined with the separate exclusions of local lengths one through four, the minimum positive local defect length on the canonical orbit is at least six. With the established unique-orbit gap below 250, the minimum positive global defect length is therefore at least 180; this is a necessary lower bound, not an existence assertion.

## 1. Local duality and a general generator inequality

Set Q=Ext²_R(M,R) and A=Ext¹_R(M,R). Reflexivity over a regular local ring of dimension four implies pd_R M≤2, and the isolated-singularity hypothesis makes A and Q finite-length. Rank-two determinant self-duality and natural local double duality give

    A ≅ D(Q),                 D(Q)=Ext⁴_R(Q,R).

These are precisely the local-duality inputs used in `../minimal-local-defect-character/PROOF.md`, Section 1, and `../rank-eight-isolated-singularity/PROOF.md`. We use their underlying R-module identity; character twists in equivariant finite duality do not affect generator counts.

Write β_i(Q) for the minimal Betti numbers of Q, and take a minimal resolution

    0 → F2 → F1 → F0 → M → 0.

The last map in its dual presents Q. Since its entries lie in m,

    rank F2 = β_0(Q).

The images of a basis of F1* generate the kernel J of F2*→Q. Choose among them a minimal generating set of J, and subtract R-linear combinations of those columns from all remaining columns. This turns the map into a minimal presentation map for Q plus u zero columns, for some u≥0. Consequently

    rank F1 = β_1(Q)+u,
    rank F0 = 2+β_1(Q)+u−β_0(Q).

If K=ker(F1*→F2*) and K_min is the kernel of a minimal presentation of Q, then

    K ≅ K_min ⊕ R^u,          μ(K)=β_2(Q)+u.

Put C=im(F0*→F1*). The dual complex gives

    0 → C → K → A → 0.

Tensoring with k, right exactness shows μ(C)≥μ(K)−μ(A). On the other hand F0* surjects onto C. Thus every such defect must satisfy

    β_2(Q)+u−μ(D(Q)) ≤ 2+β_1(Q)+u−β_0(Q),

or equivalently

    β_2(Q)−μ(D(Q)) ≤ 2+β_1(Q)−β_0(Q).       (1)

No assumptions about the maps on Tor, or a special presentation of M, enter this inequality.

For later use, if mQ=0 and length Q=n, then Q≅k^n. The Koszul resolution gives β_0=n, β_1=4n, β_2=6n, and D(Q)≅k^n as underlying modules. Inequality (1) becomes 5n≤3n+2, so n≤1. This independently excludes every semisimple defect of length greater than one, including five.

## 2. The abstract representation at length five

Completion is faithfully flat, preserving all finite lengths, minimal Betti numbers, Ext groups in question, and generator counts. We may work over the completion. Averaging a linear section of m→W over the finite group G gives an equivariant four-dimensional parameter subspace of m. Its elements generate m. Thus the multiplication map by these chosen parameters is a G-equivariant linear map

    W⊗Q → Q,

whose image is mQ. This formulation does not assume m²Q=0 in advance.

The irreducible complex representations of G are its four one-dimensional characters, on which C5 acts trivially, and one four-dimensional representation V, on which all four nontrivial clock characters occur once. Here is a direct proof sufficient for this claim. In an irreducible representation, if C5 acts trivially, the representation factors through C4 and is one-dimensional. Otherwise choose a nonzero clock eigenvector v with nontrivial eigenvalue. The span of v,Tv,T²v,T³v is invariant under both generators, has dimension four because its clock eigenvalues are distinct, and is therefore the whole irreducible representation. Since T⁴=1, this orbit basis also makes all such representations isomorphic. In particular W≅V, W*≅V, and V⊗L≅V for every one-dimensional character L.

A five-dimensional G-module is therefore either a direct sum of five one-dimensional representations, or V⊕L with L one-dimensional. In the first case all clock weights of Q are trivial. Every weight of W is nontrivial, so equivariance forces W⊗Q→Q to vanish. Therefore mQ=0, and Section 1 excludes this case.

Now suppose Q≅V⊕L and mQ≠0. The subspace mQ is a G-subrepresentation. Because V and L are irreducible and nonisomorphic, its only possibilities are 0, V, L, and Q. Nakayama excludes mQ=Q. Thus mQ is V or L. The invariant subspace m²Q of mQ is either zero or all of mQ by irreducibility. The latter would give m(mQ)=mQ, contradicting Nakayama for the nonzero finite module mQ. Hence

    m²Q=0, and either (top Q, mQ)=(L,V) or (V,L).       (2)

This rules out all alternative radical filtrations; in particular no longer Loewy filtration has been silently discarded.

### Case I: top dimension one, radical dimension four

The nonzero multiplication map W⊗L→V is an isomorphism: its source and target are irreducible and isomorphic. A lift of a nonzero generator of the top generates Q by Nakayama. Its annihilator contains m², giving a surjection R/m²→Q. Both modules have length five, so this is an isomorphism. Equivariantly one may choose the lift in an invariant complement L, giving Q≅(R/m²)⊗L.

### Case II: top dimension four, radical dimension one

Multiplication gives a nonzero map W⊗V→L. The associated map V→W*⊗L is an isomorphism by irreducibility, so this pairing is perfect. After choosing a generator of the radical, Q has underlying vector space W*⊕k with multiplication

    x·(f,a)=(0,f(x)),       x∈W,

and m kills the second summand. This is exactly the R-module dual Hom_C(R/m²,C): if R/m²=k⊕W, the action is (x·φ)(b)=φ(xb), which sends the W*-part to the k*-part by evaluation. Hence Q is isomorphic, as an underlying R-module, to D(R/m²). Equivariantly the two duals can differ by the one-dimensional canonical-duality twist, immaterial here. Thus (2) gives exactly the two claimed module types.

## 3. Elementary Betti calculations

Let B=R/m². Choose parameters x_1,…,x_4 spanning W. Compute Tor_i^R(B,k) using the Koszul resolution of k tensored with B. As a vector space,

    B⊗Λ^iW = Λ^iW ⊕ (W⊗Λ^iW).

The differential vanishes on the second summand because m²B=0. On the first summand it is

    Δ_i: Λ^iW → W⊗Λ^(i−1)W,
    w_1∧…∧w_i ↦ Σ_j (−1)^(j−1) w_j⊗w_1∧…∧ŵ_j∧…∧w_i.

Exterior multiplication after Δ_i is i times the identity. Thus Δ_i is injective for i≥1 in characteristic zero. Consequently, for 1≤i≤4,

    Tor_i^R(B,k) ≅ (W⊗Λ^iW)/im Δ_(i+1),
    β_i(B)=4 binom(4,i)−binom(4,i+1).

With β_0(B)=1 this gives

    β(B)=(1,10,20,15,4).                         (3)

For a finite-length R-module N, Ext^j_R(N,R)=0 for j<4. Indeed this holds for k by the Koszul resolution, and follows for every finite-length N by induction on a composition series and the long exact Ext sequence. Dualizing a minimal free resolution of B therefore produces a free resolution of D(B), exact everywhere except its last cokernel. The differentials remain minimal because their entries remain in m. Reading its ranks in reverse order gives

    β(D(B))=(4,15,20,10,1).                      (4)

The same dual-resolution argument gives D(D(B))≅B (or equivalently use finite-length local duality). In particular μ(D(B))=4 and μ(D(D(B)))=1.

## 4. The contradictions

If Q≅B, equations (3) and the general calculation give

    rank F2=1, rank F1=10+u, rank F0=11+u,
    μ(K)=20+u, μ(A)=4.

Therefore μ(C)≥16+u, whereas μ(C)≤rank F0=11+u, impossible.

If Q≅D(B), equations (4) give

    rank F2=4, rank F1=15+u, rank F0=13+u,
    μ(K)=20+u, μ(A)=1.

Therefore μ(C)≥19+u, whereas μ(C)≤rank F0=13+u, again impossible.

All semisimple cases were excluded in Section 1, and Section 2 exhausts the nonsemisimple cases. This proves the length-five exclusion.

## 5. Canonical-orbit application and precise dependencies

At the canonical point [e_0], the clock Z and determinant-one order-four lift −T described in `../minimal-local-defect-character/PROOF.md`, Section 3, generate the required order-twenty subgroup. Multiplication by the scalar −1 does not change the projective local action. The four nonzero coordinate indices give the four distinct nontrivial clock characters on cotangent space, transitively permuted by the multiplier. Thus the theorem applies at every point of the canonical thirty-point orbit by conjugacy.

The global numerical conclusion additionally depends on the separate length-one-through-four exclusion and the refined unique-orbit gap used in `../rank-eight-refined-defect/COROLLARY.md`. Under those inputs, a positive defect supported on the canonical orbit has total length at least 30·6=180. Any noncanonical support orbit has at least 250 points, also exceeding 180. For totals strictly below 250, the only remaining necessary values are 180, 210, and 240, corresponding to local lengths six, seven, and eight. This proof makes no claim to exclude or realize those values.
