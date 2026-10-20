> Publication scope: Universal single conjugacy class and maximal dimension two. Candidate nilpotents need not be actual spectral limits; no actual K_W realization. Historical statements about unresolved mixed classes refer to the source stage; this packet does not supersede the separately stated conditional mixed-vanishing result in PR145.

# Universal classification of rank-one-free nilpotent pencils in sl(3)

## Scope and result

Work over C. Let W have dimension three, and let K ⊂ sl(W) be a two-dimensional linear subspace such that every nonzero member is regular nilpotent (equivalently, nilpotent of rank two).

There is exactly one GL(W)-conjugacy class of such subspaces. After choosing a basis of W and linear coordinates (s,t) on K, its universal member is

    M(s,t) = [ 0  0   s ]
             [ 0  0   t ]
             [ t −s   0 ].

Its kernel-line image is a projective line, its kernel-hyperplane image is a projective line in the dual plane, and its flag curve is described intrinsically below. No rank-one-free linear space consisting entirely of nilpotents can have dimension greater than two.

These are universal linear-algebra statements. They do not establish the realization of any such K as an actual structural kernel in the originating geometric problem. No actual HM/source/model matrices, evaluations, ranks, products, jets, residues, or Massey values are used.

## 1. The kernel map has degree one

Put P=P(K), E=W⊗O_P, and H=O_P(1). The universal endomorphism is a bundle map M:E→E⊗H. The maps M and M² have constant ranks two and one, respectively. Thus L=ker M and F=ker M² are subbundles of ranks one and two.

The maps induced by M identify the successive graded pieces of the filtration 0⊂L⊂F⊂E as

    L, L⊗H, L⊗H².

Consequently det E ≅ L³⊗H³. On P≅P¹ this implies L≅O_P(−1). The inclusion L→W⊗O_P is therefore given by a linear map K→W, which is injective because its value is nonzero at every projective point. The kernel map κ:P(K)→P(W) is a linear embedding onto a projective line.

Choose coordinates on K and a basis e1,e2,e3 of W so that the kernel of M(s,t) is C(s e1+t e2).

## 2. An adapted third basis vector

The polynomial identity M(s,t)(s e1+t e2)=0 implies

    M(s,t)e1 = t a,
    M(s,t)e2 = −s a,
    M(s,t)e3 = s b+t c

for fixed vectors a,b,c∈W. Here a≠0, since otherwise every member has rank at most one.

Let U=span(e1,e2). In fact a∉U. If a=a1e1+a2e2 belonged to U, then

    M(s,t)a=(a1t−a2s)a.

Nilpotency for every (s,t) forces the displayed eigenvalue to vanish identically, so a1=a2=0, contradicting a≠0. Thus (e1,e2,a) is a basis. This avoids any unproved nonvanishing assumption on a coordinate of a.

In this basis, write

    M(s,t) = [ 0  0   A(s,t) ]
             [ 0  0   B(s,t) ]
             [ t −s   C(s,t) ],

where A,B,C are linear forms. Trace zero gives C=0. Nilpotency gives

    0 = tr(M(s,t)²)/2 = t A(s,t) − s B(s,t).

Comparing coefficients yields A(s,t)=αs and B(s,t)=αt for one scalar α. The scalar α is nonzero, because α=0 would make every nonzero member rank one.

Replace the third basis vector a by r a. The matrix becomes

    [ 0  0  rαs ]
    [ 0  0  rαt ]
    [ t/r −s/r 0 ].

Now use parameters s'=s/r and t'=t/r. The upper-right column is αr²(s',t',0)^T. Choose r∈C* with αr²=1. This proves the asserted normal form. Changing the parameters changes only the chosen basis of K, so the conclusion is conjugacy of the subspaces, not merely an equivalence under unrelated left and right transformations.

Conversely, the displayed canonical matrix has rank two for every (s,t)≠(0,0), has cube zero, and has nonzero square. Its square is

    [ st −s² 0 ]
    [ t² −st 0 ]
    [  0   0 0 ].

It therefore supplies the required universal example and completes the classification.

## 3. Intrinsic flag geometry and alternating description

For the canonical pencil,

    ker M(s,t)  = C(s e1+t e2),
    ker M(s,t)² = span(s e1+t e2,e3).

Thus κ(P(K))=P(U), where U=span(e1,e2), and the hyperplane map is

    [s:t] ↦ [t:−s:0] ∈ P(W*).

Its image is the pencil of planes containing A=Ce3. In particular

    U = span of all kernel lines,
    A = intersection of all kernel hyperplanes,
    W = U ⊕ A.

Both U and A are intrinsic to K. The flag curve consists precisely of the flags

    (ℓ, ℓ⊕A),   ℓ∈P(U).

Both projections of this curve are isomorphisms onto lines; its bidegree in P(W)×P(W*) is (1,1).

Choosing a generator a of A and a nonzero alternating form ω on U, the pencil can equivalently be written

    M_u(v+z a)=ω(u,v)a+c z u,    u,v∈U,

with c≠0; suitable choices normalize c and ω to the displayed canonical matrix. In that matrix ω((s,t),(x,y))=tx−sy. This is an intrinsic alternating-extension description, with the choices of generator and normalizations kept explicit.

## 4. Dimension bound and maximality

Suppose a linear subspace V⊂sl(W) consists of nilpotents and contains no nonzero rank-one matrix. Every nonzero member is then regular nilpotent. If dim V≥3, restrict to any three-dimensional subspace and repeat the bundle argument of Section 1 on P².

Since Pic(P²)=Z and L³⊗O(3)≅O, again L≅O(−1). The trivial rank-three bundle would have a filtration with graded pieces

    O(−1), O, O(1).

Multiplicativity of Chern classes would give

    c(E)=(1−h)(1)(1+h)=1−h²,

contradicting c2(E)=0 because h²≠0 on P². Hence dim V≤2.

Every one-dimensional space spanned by a regular nilpotent extends to a pencil of the canonical type: all regular nilpotents in sl(3,C) are conjugate, and any one nonzero canonical member is regular nilpotent. Therefore the maximal-by-inclusion rank-one-free nilpotent subspaces are exactly these two-dimensional pencils, all in the single conjugacy class proved above.

## 5. Quadratic base points versus actual fixed-W degenerations

For this universal K, both q=tr(M²) and det M vanish identically. Thus every point of P(K) is a nilpotent quadratic base point, but the spectral open locus

    X={ [M]∈P(K): det M=0 and q(M)≠0 }

is empty. Its closure Y is empty as well. In the fixed-W spectral-frame framework of ../nilpotent-frame-boundary/PROOF.md, independent zero frames require a nonzero spectral member in X. Hence no independent zero frame exists for this abstract K, and no all-nonzero rank-one triple can be a fixed-W degeneration of such frames.

The kernel-line image P(U) is nevertheless nonempty (indeed a line). Consequently the set of quadratic/nilpotent candidate directions κ(N) can be nonempty while the actual degeneration set κ(N∩Y) is empty. One cannot universally replace N∩closure(X) by N, or infer fixed-W spectral integrability from quadratic vanishing alone.

This illustrates a universal logical obstruction only. It neither proves that an actual structural K_W has this type nor excludes degenerations in which the ambient three-plane W varies. No conclusion about realizability in the originating geometric problem is asserted.
