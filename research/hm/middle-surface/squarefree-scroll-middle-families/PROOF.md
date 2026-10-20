# Rank-one rectangular restrictions and squarefree scroll middle families

## Main theorem

Work over C. Let dim V=5, and let J be a finite-dimensional complex vector space, and let f:V³→J be a trilinear map that is outer symmetric and cyclic zero. Suppose every repeated-input map

    A_a: V/Ca → J,   b ↦ f(a,a,b)

is injective. Define the projective incidence

    R = {([u],X,Y) ∈ P(V)×Gr(2,V)×Gr(3,V) : dim f(X,u,Y) ≤ 1}.

Then the image of R in P(V) has dimension at most one.

Consequently, the middle points admitting a compatible full-support type III cubic scroll, as parametrized in /research/hm/normalizer-rank-five/full-support-scroll-exclusion/PROOF.md, lie in a closed projective subset of dimension at most one. In particular they cannot be dense in a middle surface. No assumption on the residual ranks or scroll types at the boundary is needed, and no classification of all rank-five kernels is used.

The essential improvement over a complete-uniform-family argument is that degenerations of the splitting are controlled on the entire closed rectangular incidence. They occur only over finitely many middle points, and normal extension of regular functions removes this boundary.

## 1. The finite exceptional middle set

We use the theorem proved in /research/hm/middle-surface/extremal-surface-geometry/PROOF.md: the closed locus

    D = {([h],[u]) : rank[z ↦ f(h,u,z)] ≤ 2}

has finite support. Let F⊂P(V) be its finite middle image.

For clarity, its inputs are exactly the three hypotheses above. Off the diagonal, A_u(h) and A_h(u) are independent: a dependence A_u(h)=tA_h(u) would give A_{u+th}(h)=0. Thus a rank-two polar has kernel complementary to Cu⊕Ch. On every reduced projective component of D, the two tautological lines and the rank-three polar kernel split the trivial V-bundle. Their projector matrices have regular entries, hence are constant. The two coordinate lines are then constant, so the component is a point. The diagonal has polar rank four and does not enter D.

## 2. Boundary lemma for the rectangular incidence

Fix any point ([u],X,Y) of R, and write L=f(X,u,Y), a vector subspace of J of dimension at most one.

First u∉X and u∉Y. If u∈X, then A_u(Y)⊂L, whereas injection gives dim A_u(Y)≥2. If u∈Y and u∉X, then A_u(X)⊂L has dimension two, again impossible.

Next dim(X∩Y)≤1. Otherwise X⊂Y. For every a∈X, the vector

    f(a,u,a) = -2 A_a(u)

belongs to the fixed line L. It is nonzero for every nonzero a, because u∉X. If L=0 this is immediately impossible. If dim L=1, choosing a coordinate on L gives a homogeneous quadratic on a two-dimensional complex vector space which never vanishes away from zero. Every such quadratic has a projective zero over C, a contradiction.

Finally, suppose X∩Y=Ch. By outer symmetry,

    f(h,u,X+Y) ⊂ L.

Since dim(X+Y)=4, extending from X+Y to V increases the polar image dimension by at most one. Therefore rank f(h,u,-)≤2, so [u]∈F.

We have proved, on the entire closed incidence including all degenerations,

    [u]∉F  ⇒  V=X⊕Y.                                    (1)

This is a genuine boundary localization statement. It does not presume a scroll normal form at the limit. In fact the image dimension cannot be zero at any point of R: otherwise every [x]∈P(X) gives a polar with the three-plane Y in its kernel, producing infinitely many points of D. Thus all restrictions parametrized by R have image dimension exactly one, although this strengthening is not needed below.

## 3. Projective compactification and normal extension

The incidence R is closed and projective: on P(V)×Gr(2,V)×Gr(3,V), trilinearity defines a bundle map from the tensor product of the three tautological bundles to the trivial J-bundle; its two-by-two minors impose image rank at most one.

Suppose an irreducible component C of R has middle image B of dimension d≥2. Give C and B their reduced structures. Let T→C be the normalization, and let g:T→B be the proper surjective middle map. Its Stein factorization is

    T --h--> B' --π--> B,

where π is finite, B' is normal integral and projective, and h_*O_T=O_{B'}. These standard properties hold for a proper map from a normal integral projective variety in characteristic zero; equivalently B' is the finite normal intermediate space in the Stein factorization. In particular dim B'=d.

Remove the finite set π⁻¹(B∩F) from B', obtaining U. On h⁻¹(U), (1) gives a direct-sum decomposition of vector bundles

    V⊗O = X_bundle ⊕ Y_bundle.

Its projector P_X, with image X_bundle and kernel Y_bundle, is a global regular endomorphism of the trivial bundle. Every matrix entry is therefore a regular function on h⁻¹(U). The Stein identity, restricted to U, identifies these entries with regular functions on U.

Because B' is normal and d≥2, regular functions extend across the removed finite set, which has codimension at least two. Thus every projector entry extends to B'. Since B' is integral projective, all these entries are constant. Consequently X and Y are fixed subspaces on the dense open h⁻¹(U), hence on all of T by separatedness of the Grassmannians. Denote these fixed subspaces by X₀ and Y₀. They are complementary, since they are complementary at a point of that dense open.

It follows that every [u]∈B satisfies ([u],X₀,Y₀)∈R. Section 2 gives

    B ∩ P(Y₀) = ∅.

But B⊂P(V)=P⁴ is projective of dimension at least two, and P(Y₀) is a projective plane. The projective dimension theorem forces their intersection to be nonempty. This contradiction proves dim B≤1 for every component C, and hence proves the main theorem.

Notice that exceptional divisors of T lying over F cause no problem. One does not incorrectly apply Hartogs directly on T. One first descends the projector entries through the proper connected-fiber map to the normal finite Stein base B', where the omitted set really is finite and has codimension at least two.

## 4. Intrinsic splitting of a type III scroll fiber

Use the type III normal form in the cited full-support-scroll proof. Relative to V=Cu⊕E with basis x,y,z,w of E, the residual scroll is

    q=(s x+t y)(a z+b(s y+t w)).

Every correction compatible with this scroll has parameters λ,μ,ν,α,β and the formulas given in that proof, Section 6.1. Its ordered zero lifts are

    l=s(x−μu)+t(y−νu),
    n=a(z−λu)+b[s(y−αu)+t(w−βu)].

Set

    X=span{x−μu,y−νu},
    Y=span{z−λu,y−αu,w−βu}.

They have dimensions two and three. The first factor projection of this ordered scroll has image P(X), of dimension one. The second factor projection has image P(Y), of dimension two: the parameters [a:bs:bt] cover P². Thus the ordered scroll intrinsically recovers X and Y as the spans of its projection images. The two orientations are distinguished by their projection dimensions, so interchanging the factors does not produce an ambiguity in which subspace has dimension two.

These statements concern the given ordered scroll component, not an arbitrary selection of coordinates on E. When α≠ν, X⊕Y=V. When α=ν, their intersection is the line C(y−νu). This follows directly by comparing the x,z,w,y coefficients of a common vector.

For families, the intrinsic spans vary algebraically whenever the corresponding projection spans have constant dimensions and formation of the degree-one linear spans commutes with base change. For example this holds on a dense open of any integral parameter space carrying a flat projective family of the ordered scrolls: relative degree-one equations and generic base change recover the kernels of the evaluation maps, hence the two Grassmannian maps. Shrinking to this open suffices to construct the usual rational splitting map. No extension of that rational map, no global flatness assertion, and no uniqueness among several scroll components in a fiber are required by the main theorem: it uses the closed incidence containing every individual choice.

## 5. Every compatible type III scroll produces a point of R

Write

    p=x−μu,  q=y−νu,  r=z−λu,  s₀=y−αu,  t₀=w−βu.

The identity f(l,u,n)=0 for all scroll parameters implies, by comparing coefficients,

    f(p,u,r)=f(q,u,r)=f(p,u,s₀)=f(q,u,t₀)=0,
    f(p,u,t₀)+f(q,u,s₀)=0.

Thus all values of f(X,u,Y) are multiples of the single vector f(p,u,t₀). Therefore ([u],X,Y)∈R.

The main theorem immediately implies that all such middle points, even without a preselected algebraic family of scrolls, are contained in the closed set pr_middle(R) of dimension at most one. The contraction case α=ν lies over F by Section 2, recovering the finite exceptional-middle phenomenon without needing to prove compatibility of the additional common-factor plane separately.

This also treats limits that leave the type III stratum entirely. Compactify the rectangular triples in R, rather than attempting to compactify only the scroll normal forms. At every limiting triple the rank-one condition persists. A failed splitting lies over F; a preserved splitting admits the same projectors. The Stein-base argument then excludes a surface regardless of the residual kernel, rank, or scroll geometry at that boundary.

## Scope

This is universal tensor geometry over C. It proves a dimension-one upper bound for the middle image of the rank-one (2,3)-rectangular incidence and excludes a middle surface of the explicit compatible type III scrolls. It does not classify all rank-five kernels, exclude isolated scroll fibers, or exclude curves of scroll middles. The isolated global countermodel in /research/hm/normalizer-rank-five/full-support-scroll-exclusion/COUNTERMODEL.md is fully consistent with the theorem.
