# Arbitrary three-planes: kernel criterion and relative independent-zero incidence

## Result and scope

Work over C. Let V and J3 carry the canonical trilinear operation f of the imported module theorem. For any three-plane W⊂V there is a canonical linear map

    T_W:E_W=Schur_(2,1)W ≅ sl(W)⊗det(W) → J3,
    f(x,y,z)=T_W τ(x,y,z),
    τ(x,y,z)=x⊗(y∧z)−z⊗(x∧y).

Write K_W=ker T_W. Trivialize det(W) to regard K_W as a linear subspace of sl(W), and put q(A)=tr(A²), h(A)=det(A). The following statements are invariant under this trivialization.

1. W admits an independent ordered zero triple if and only if

       X_W = { [A]∈P(K_W) : h(A)=0, q(A)≠0 }

   is nonempty.
2. K_W contains no nonzero rank-one nilpotent endomorphism. Consequently dim K_W≤4 and rank T_W≥4 for every W. These are structural bounds, not evaluations of an actual map.
3. If rank(q|K_W)≥3, independent zero triples exist. If q|K_W=0, none exist. If q is nonzero and h vanishes identically on K_W, they exist. In the remaining case q≠0, h≠0, absence is equivalent to every irreducible factor of h dividing q. Precisely:
   - If rank q=1, write q=cℓ²; absence is equivalent to h=dℓ³.
   - If rank q=2, write q=cℓm with independent linear forms ℓ,m; absence is equivalent to h=dℓᵃm^(3−a), with a∈{0,1,2,3}.
   Here c,d are nonzero scalars, and q,h in these statements mean their restrictions to K_W.
4. On every determinantal constant-rank stratum of Gr(3,V), X_W assembles into a relative locally closed incidence scheme X. Its oriented nonzero-eigenline cover is finite étale of degree two. Over this cover the independent zero-frame scheme is the product of three punctured eigenline bundles, hence a principal (G_m)^3-bundle, without any claim of global triviality. Its geometric fiber over a point of X is a disjoint union of two three-dimensional tori.

No actual K_W is computed, and no generic kernel dimension or generic existence assertion is made. No conclusion about reducedness or smoothness of X is asserted.

## Imports and evidence boundary

Read [the ap three plane cubic frames manuscript](../../two-and-three-plane-zeros/ap-three-plane-cubic-frames/PROOF.md), [the two plane cubic zero scheme manuscript](../../two-and-three-plane-zeros/two-plane-cubic-zero-scheme/PROOF.md), and [the cubic massey module reduction manuscript](../../canonical-cubic-extension/cubic-massey-module-reduction/PROOF.md). We use their universal Schur tensor normalization, trilinearity, outer reversal, cyclic zero, and structural repeated-input nonvanishing for independent inputs. We do not import the special arithmetic-progression kernel as a claim about arbitrary W.

The proof uses universal tensors, polynomial rings, vector bundles, and standard projective dimension theory. It computes no actual HM/source/model matrices, products, ranks, values, selected input points, jets, residues, or Massey values. 

## 1. Universal tensor and invariant criterion

The exterior-multiplication kernel

    E_W=ker(W⊗Λ²W → Λ³W)

is the eight-dimensional Schur module. Its spanning tensors τ obey exactly the argument symmetries of f, so f factors uniquely through T_W. The natural isomorphism

    Φ(u⊗(v∧w))(t)=u⊗(t∧v∧w)

identifies E_W with sl(W)⊗det(W), because exterior multiplication corresponds to trace. If x,y,z are an ordered frame, ω=x∧y∧z, and H is the endomorphism acting by 1,0,−1 on x,y,z respectively, then

    Φτ(x,y,z)=H⊗ω.

Thus τ is nonzero, its endomorphism has determinant zero, and its trace-square is nonzero in every determinant-line trivialization. A zero frame therefore gives a point of X_W.

Conversely take a nonzero A∈K_W with h(A)=0 and q(A)≠0, after trivialization. The characteristic polynomial of a traceless three-dimensional endomorphism is

    t³−(q(A)/2)t−h(A).

Its roots are 0,λ,−λ, where λ²=q(A)/2≠0. They are distinct, so A has a direct sum of three eigenlines. Order them as λ,0,−λ and choose nonzero vectors x,y,z on them. Then Φτ(x,y,z) is a nonzero scalar multiple of A (with the determinant line restored). Since K_W is linear, T_Wτ=0. Every such zero frame arises in this way.

Changing the determinant generator rescales A by a nonzero scalar; q and h rescale by its square and cube. Their vanishing conditions, and the rank of the restricted quadratic form, are unchanged. There is no GL(W)-equivariance assertion about T_W: only τ and Φ are natural.

## 2. Rank-one nilpotent exclusion and the uniform kernel bound

Any nonzero rank-one traceless endomorphism is x⊗ℓ with x≠0, ℓ≠0, and ℓ(x)=0. It squares to zero. Fix a determinant generator ω. The inverse to the contraction isomorphism Λ²W≅W*⊗det(W) sends ℓ⊗ω to a nonzero bivector β satisfying x∧β=0. In dimension three this says β=x∧y for some y independent of x, with any nonzero coefficient absorbed into y. Hence

    (x⊗ℓ)⊗ω = Φ(x⊗(x∧y)) = Φτ(x,x,y).

The imported structural assertion f(x,x,y)≠0 excludes this tensor from K_W.

The projective locus N of nonzero rank-one traceless endomorphisms is closed in P(sl(W)): it is cut out by rank≤1 minors inside the trace hyperplane. It is canonically the incidence flag variety

    { (L,H)∈P(W)×P(W*) : L⊂ker(H) },

where a covector line is denoted H and gives the associated kernel hyperplane. The Segre map (Cx,Cℓ)↦[x⊗ℓ] realizes this identification. Its dimension is 2+1=3. If k=dim K_W>0, the projective dimension theorem in P(sl(W))=P^7 implies that P(K_W) must meet N whenever (k−1)+3≥7. Disjointness therefore gives k≤4. The case k=0 is immediate. Since dim E_W=8, rank T_W=8−k≥4.

The bound uses only universal projective dimensions and the imported nonvanishing theorem, not the rank of any actual numerical or symbolic HM map.

## 3. Exact polynomial exclusion test

Let K be any finite-dimensional complex vector space with homogeneous restrictions q∈Sym²K*, h∈Sym³K*. The criterion is existence of a nonzero vector with h=0 and q≠0. If K=0 or q=0, there is none. If q≠0 and h=0 identically, the nonempty principal open q≠0 supplies such vectors, hence projective classes.

Suppose q,h are both nonzero. Absence is equivalent to V_aff(h)⊂V_aff(q); the affine origin causes no difference because it belongs to both loci. The Nullstellensatz says this is equivalent to q∈√(h). In the unique factorization domain Sym K*, factor h into homogeneous irreducibles. Its radical ideal is generated by the product of its distinct irreducible factors. Thus the containment is equivalent to every irreducible factor of h dividing q.

A nonzero quadratic over C has rank one precisely when it is a nonzero multiple of a square of a linear form, rank two precisely when it is a product of two independent linear forms, and rank at least three precisely when it is irreducible. Consequently:

- For rank one, all factors of h must be proportional to ℓ, giving h=dℓ³.
- For rank two, all factors must be proportional to ℓ or m; degree three gives exactly h=dℓᵃm^(3−a).
- For rank at least three, the only possible irreducible factor of h would be the irreducible quadratic q. A nonzero homogeneous cubic cannot be a scalar times an integral power of that quadratic. Thus absence is impossible.

This proof includes one-dimensional and two-dimensional K without a hidden projective-dimension assumption. Rank at least three automatically implies dim K≥3. The test is exact for the restricted polynomials; it does not assert that every listed algebraic possibility occurs for the actual kernels K_W.

## 4. Relative construction on the Grassmannian

Let G=Gr(3,V), S its tautological rank-three bundle, D=det S, and

    E=ker(S⊗Λ²S → D) ≅ sl(S)⊗D.

Restriction of the global Schur-linear operation gives a bundle map T:E→J3⊗O_G. For each r let G_r be its determinantal rank-exactly-r stratum: the closed scheme defined by (r+1)-minors, restricted to the open where some r-minor is invertible. On this scheme T is locally equivalent by invertible source and target operations to a rank-r identity block and zeros. In particular K=ker T is a subbundle of E|G_r of rank 8−r, and formation of K commutes with arbitrary base change within G_r. One could instead work on any locally closed base on which this split constant-rank condition holds. No assertion is made about the geometry or nonemptiness of any particular G_r.

On P(K), using the convention of lines, let L=O(−1) be the tautological subline of E. The inclusion gives a universal line-valued traceless endomorphism

    B:S → S⊗M,       M=L*⊗D.

Consequently Q=tr(B²) and H=det(B) are sections of M² and M³, respectively. Define the relative incidence scheme

    X=Z(H) ∩ {Q invertible} ⊂ P(K).

“Invertible” means that Q is a nowhere-zero trivialization of M² on this open. The definition is intrinsic and its geometric fibers are precisely X_W with their indicated locally closed scheme structures.

Let F=Fr(S) be the bundle of ordered frames over G_r, and let Z⊂F be the zero scheme of f on the three universal frame vectors. The ideal of f=Tτ equals locally the ideal of the projection of τ to E/K, because the induced map E/K→J3⊗O is a locally split injection. This equality survives arbitrary base change. Since τ for a frame is nowhere zero, Z carries a canonical morphism to P(K) by its line, and the characteristic-polynomial identities force this morphism to factor through X scheme-theoretically.

### Global incidence without a global kernel bundle

There is also a construction across all kernel-dimension jumps. On P(E) let L be its tautological line and define Y as the zero scheme of the composite L→E→J3⊗O. Its fiber over W is P(K_W), but Y is not asserted to be a projective bundle. Define B, M, Q, H on P(E) as above and set X_global=Y∩Z(H)∩{Q invertible}. This is a single locally closed incidence scheme over G. Its restriction to every G_r is the X just constructed. The zero-frame scheme over all G maps to X_global, and the proof in Section 5 gives the same finite étale orientation cover and product of punctured eigenline bundles globally. Here the kernel condition is imposed directly by the equation Tτ=0, so no global locally free kernel or constant-rank assumption is needed. The constant-rank strata remain useful for the explicit projective-bundle description and the restricted-polynomial analysis.

## 5. Oriented eigenline cover and frame bundles

Over X define the double cover

    π:X~→X,      λ∈M,  λ²=Q/2.

Formally this is the zero scheme of λ²−Q/2 in Tot(M). Since Q is invertible, λ is nowhere zero on the cover and the derivative 2λ is invertible in local trivializations. Thus π is finite étale of degree two, including over nonreduced bases. Its deck involution sends λ to −λ.

The normalized endomorphism N=B/λ on π*S satisfies tr N=0, det N=0, and tr(N²)=2. Cayley–Hamilton gives N³=N. Its spectral idempotents are

    P_+=(N²+N)/2,   P_0=I−N²,   P_-=(N²−N)/2.

They are orthogonal and sum to I, and their fiber ranks are each one; their images therefore form line subbundles S_+, S_0, S_- splitting π*S. This works over arbitrary base schemes here, not only geometric points. The involution exchanges S_+ and S_- and preserves S_0.

The zero-frame scheme Z is canonically isomorphic to

    S_+^× ×_(X~) S_0^× ×_(X~) S_-^×.

To prove this functorially, an ordered choice x,y,z from these three punctured line bundles is a frame. Its τ is in the universal line L because its endomorphism is proportional to B, so it gives a zero frame. In the other direction, a zero frame determines L=O·τ and ω=x∧y∧z. Evaluation on τ identifies M=Hom(L,D); there is a unique λ∈M with λ(τ)=ω. Under this identification the universal B evaluates to H_frame⊗ω, so λ²=Q/2 and the frame vectors lie in the λ,0,−λ eigenlines. These constructions are inverse and preserve the scheme structures, not merely their complex points.

The displayed product is a principal split-torus (G_m)^3-bundle over X~ under independent rescaling of its three vectors. It is Zariski locally trivial there because the three eigenline bundles are locally trivial. It need not be globally trivial. Viewed over X, it has geometric fibers consisting of two such tori, and their components can be exchanged by monodromy. We do not identify Z globally with X×(two tori), nor choose a global orientation.

For comparison, if a specific nonzero kernel tensor a above a point of X is fixed and one imposes τ(x,y,z)=a, then in each orientation the product of the three scaling parameters is fixed to a nonzero constant. Each of the two geometric fibers is a torsor under {(s,t,u)∈(G_m)^3:stu=1}≅(G_m)^2. This is a statement about fibers with a fixed tensor, distinct from the projective incidence fibers above.

## 6. Consequences and limitations

Independent zero frames over G_r are exhausted scheme-theoretically by this incidence and eigenline construction. If X is empty there are none. If X is nonempty, the local frame geometry adds relative dimension three after a finite étale orientation cover; any singularities or nilpotents of X are retained, so no unconditional smoothness or reducedness assertion follows.

For each W, the universal bound leaves dim K_W in {0,1,2,3,4}. In dimensions three or four, a restricted trace-square form of rank at least three guarantees independent zeros; lower rank requires the exact factor test above. Determining which alternatives occur for arbitrary W remains a separate problem. The theorem does not compute the actual Grassmannian strata, restricted quadratic ranks, cubic factors, or any generic behavior.
