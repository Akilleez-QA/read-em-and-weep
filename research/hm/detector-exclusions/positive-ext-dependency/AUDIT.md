> Historical mathematical audit, preserved in full apart from nonmathematical process statements and source-link normalization. Original-source hashes identify the audited source text; publication-byte hashes are recorded separately. This is not a claim of a fresh or formal proof check.

# Independent algebraic audit

## Verdict

The countermodel is correct as a statement about bounded cochain complexes of complex vector spaces. It gives every projected rank from 0 through 6 while keeping all displayed cohomology dimensions, the distinguished projection, and the two primary maps on the fixed zero-differential representatives unchanged. The two cone triangles admit a simultaneous degreewise exact four-term realization after contractible mapping-cylinder enlargements.

The necessary scope qualification is important: the enlarged strict middle map varies with the secondary datum. The construction does not keep the entire strict four-term sequence fixed, nor does it produce geometric HM or normalization examples. It disproves a general inference from the stated abstract numerical and primary-map data. It does not establish nondeterminacy for every possible primary-map pair, or for the actual geometric pair without further information.

## 1. Cone convention and cohomology

Use cohomological grading and

    Cone(u)^n = B^n ⊕ A^(n+1),
    d(b,a) = (d_B b + u(a), −d_A a)

for a chain map u:A→B.

For the fixed f:E→L in the proof, the cone K has

    K^0 = C^77,
    K^1 = C^495 ⊕ V,
    d_K^0(e) = (f(e),0).

Because f:E^1→L^1 is injective, H^0(K)=0. The only nonzero cohomology is

    H^1(K) = Q ⊕ V,
    dim Q = 495−77 = 418,
    dim H^1(K) = 418+16 = 434.

Fix T:Q→P^1 of rank 415 and a splitting P^1=im T⊕J, where dim J=10. Every surjection σ:V→J defines the stated chain map

    g_σ^1(l,v) = T([l])+σ(v).

Indeed g_σ^1 d_K^0=0, and no other chain-map condition is nontrivial. Its restriction along L→K is the fixed map h:L→P, h(l)=T([l]); this restriction is independent of σ, and hf=0.

The second cone D_σ=Cone(g_σ) is explicitly

    C^77  --−(f,0)-->  C^495⊕V  --g_σ^1-->  C^425,
      −1                    0                     1.

The first differential is injective, the last is surjective, and their composite is zero. The direct-sum decomposition im T⊕J implies

    ker[Q⊕V → P^1] = ker T ⊕ ker σ.

Consequently

    H^0(D_σ) = ker T ⊕ ker σ,
    dim H^0(D_σ) = (418−415)+(16−10) = 9,
    H^i(D_σ)=0 for i≠0.

Thus the entire cohomology table is independent of the chosen surjective σ:

- E: dimensions 77 in degree 1 and 16 in degree 2.
- L: dimension 495 in degree 1.
- P: dimension 425 in degree 1.
- K: dimension 434 in degree 1.
- D_σ: dimension 9 in degree 0.

All unlisted groups vanish. In particular H^2(L)=H^2(P)=0. The full double-boundary image has dimension 6 in every example; its projection to U is what varies.

## 2. Connecting maps and signs

With the coordinate projections of the two cone constructions, the relevant maps are

    H^0(D_σ)=ker T⊕ker σ → H^1(K)=Q⊕V → H^2(E)=V,
    (q,v) ↦ (q,v) ↦ v.

Therefore the composite has image exactly ker σ. A convention that identifies connecting maps with the ordinary lift-and-differentiate boundary of a short exact sequence may introduce minus signs in the individual cone projection identifications. The explicit cylinders below introduce a minus sign in each of the two boundaries, so their composite is exactly the displayed positive projection. None of the asserted images or ranks depends on this convention.

## 3. Explicit simultaneous exact realization

For any cochain map u:A→B, define a cylinder M(u) by

    M(u)^n = A^n ⊕ B^n ⊕ A^(n+1),
    d_M(a,b,c) = (d_A a−c, d_B b+u(c), −d_A c).

The equation d_M²=0 follows directly from d_B u=u d_A. Define

    j_u:A→M(u),       j_u(a)=(a,0,0),
    q_u:M(u)→Cone(u), q_u(a,b,c)=(b,c),
    p_u:M(u)→B,       p_u(a,b,c)=u(a)+b.

These are chain maps. Degree by degree,

    0 → A --j_u--> M(u) --q_u--> Cone(u) → 0

is exact. Furthermore p_u j_u=u, and p_u is a quasi-isomorphism. To verify the latter without appealing to a cylinder convention, its kernel consists of (a,−u(a),c), identified with pairs (a,c), with differential

    (a,c) ↦ (d_A a−c,−d_A c).

The degree −1 map (a,c)↦(0,−a) is a contracting homotopy: ds+sd=id. Also s_B(b)=(0,b,0) is a chain-map section of p_u, and q_u s_B is the usual inclusion B→Cone(u).

Apply the construction to f:E→L and g_σ:K→P. The two short exact sequences are

    0→E→M(f)→K→0,
    0→K→M(g_σ)→D_σ→0.

Their splice is the genuine degreewise exact four-term sequence

    0 → E --j_f--> M(f) --j_g q_f--> M(g_σ) --q_g--> D_σ → 0.

Its intermediate image is the embedded copy j_g(K), hence is isomorphic as a complex to K. Its second and third terms are quasi-isomorphic to L and P, respectively. The first primary map represents f exactly because p_f j_f=f.

For the second primary map, it is useful to check the homotopy explicitly rather than infer it solely from dimensions. Write m=j_g q_f. Then

    p_g m = g_σ q_f.

On M(f)^n with coordinates (a,l,e), the difference between this map and h p_f is zero except in degree 1, where it equals σ(e). Define a degree −1 map S:M(f)→P by

    S^2(a,0,0)=−σ(a) for a∈E^2=V,
    S^n=0 for n≠2.

Since d_{M(f)}^1(a,l,e) has E^2-coordinate −e, one gets

    p_g m − h p_f = d_P S + S d_{M(f)}.

Thus the second primary map is identified with the same fixed h in the homotopy category, and in particular on cohomology. The dependence on σ remains in the compatible secondary/homotopy datum and the enlarged strict maps; it has not disappeared.

For the ordinary short-exact-sequence boundary, lift a cone cocycle (b,c) to (0,b,c). Its differential in M(u) is (−c,0,0), so the boundary is −[c]. Applying this to both short exact sequences gives the asserted double boundary with the two signs cancelling.

The replacements are genuinely necessary. The original E^2→L^2 is V→0 and is not injective, so the original zero-differential E,L,P cannot themselves be the first three terms of the proposed degreewise exact sequence. The proof correctly uses replacements instead.

## 4. Rank identity, sharp bounds, and all intermediate ranks

Let V be any subspace of U⊕W and let σ:V→J be linear. Put

    A=V∩W, v=dim V, a=dim A, d=v−a,
    s=rank σ, b=rank(σ|A).

The kernel of the projection restricted to ker σ is

    ker σ ∩ W = ker(σ|A).

Rank-nullity therefore gives, without any genericity assumption,

    r := dim pr_U(ker σ)
       = (v−s)−(a−b)
       = v−a−s+b = d−s+b.

The restriction rank satisfies b≤min(a,s). Since the quotient image σ(V)/σ(A) is generated by V/A, it has dimension s−b≤d. Thus

    max(0,s−d) ≤ b ≤ min(a,s),
    max(0,d−s) ≤ r ≤ min(d,v−s).

These bounds, and every integer between them, are attainable whenever rank s is feasible, namely 0≤s≤min(v,dim J). Split V=A⊕C. For any permitted integer b, map A onto a b-dimensional image and C onto a disjoint (s−b)-dimensional image, with remaining basis vectors sent to zero. This realizes rank s and restriction rank b, hence the corresponding r.

In the countermodel v=16, a=6, d=10, and s=10, so the interval is exactly 0≤r≤6. For every integer k in this interval choose

    Z_k = U_k ⊕ W_(6−k),

where U_k⊂U has dimension k and W_(6−k)⊂W has dimension 6−k. Any quotient map V→V/Z_k followed by an isomorphism V/Z_k≅J gives a surjection σ_k with

    ker σ_k=Z_k,
    dim ker σ_k=6,
    dim pr_U(ker σ_k)=k.

The endpoint descriptions in PROOF.md are special cases of this same construction and are correct.

When V=U⊕W, projected surjectivity onto all ten dimensions of U is equivalent to s=b, or equivalently σ(V)=σ(W). Projected rank zero is equivalent to ker σ⊂W. If V is a proper subspace, s=b only establishes rank d=dim pr_U(V); full surjectivity onto U additionally requires d=dim U.

## 5. Audit of the surrounding proof and limits

The numerical substitutions in PROOF.md are correct:

    χ(B(1))=−55, χ(B(2))=−85,
    5+3·24=77, 10+3·2=16,
    9·55=495, 5·85=425,
    −425+495−77+16=9.

The implications for h^1 at positive twists are conditional on exactly the additional vanishing assumptions stated there. This audit does not independently establish any HM cohomology table, the negative-twist source assertions, stability hypotheses, the actual geometric primary maps, or the surface Euler-characteristic computation. It confirms the algebra and arithmetic once those inputs are assumed. 

The abstract example therefore supports the proof's carefully qualified conclusion: even simultaneous positive-H² vanishings, the displayed favorable numerical table, and fixed abstract primary maps need not determine the normalized projected rank. An actual geometric rank still requires geometric or secondary-map information.
