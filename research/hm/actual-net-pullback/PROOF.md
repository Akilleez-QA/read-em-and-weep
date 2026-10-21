# Exactly twenty-five actual beta nets and their disjoint rank-nine lines

Status: authored structural proof; not formally checked. Independent mathematical review is recorded separately. Characteristic zero over C. No selected actual HM source point, matrix, coefficient, or rank is evaluated.

## 1. Fixed dictionary and hypotheses

Let dim A=dim V=5 and dim W=2. Use the actual Heisenberg intertwiner phi: Lambda^2 A -> V tensor W, and its dual phi*. For a rank-two tensor k in V* tensor W*, put

N_k = phi*(sl(W)^T k).

For k=p tensor epsilon_1+q tensor epsilon_2, p,q independent, this is the span of F_1(q), F_2(p), F_1(p)-F_2(q), where F_a(r)=phi*(r tensor epsilon_a). This is a three-dimensional space.

Here is the universal dictionary explicitly. In Schrödinger bases, with indices modulo five, phi(e_i wedge e_j)=v_(i+j) tensor w_(j-i), where w_(-d)=-w_d and w_1,w_2 are a basis of W. Let epsilon_1,epsilon_2 be the dual basis. Solving i+j=k and j-i=1 or 2 modulo five gives

F_1(v_k*)=e_(3k+2)* wedge e_(3k+3)*,
F_2(v_k*)=e_(3k+4)* wedge e_(3k+1)*.

BHM uses f^+(r)=sum_i r_i e_(i+2)* wedge e_(i+3)* and f^-(r)=sum_i r_i e_(i+1)* wedge e_(i+4)*. Setting r_i=p_(2i) therefore gives F_1(p)=f^+(r) and F_2(p)=-f^-(r). The coordinate Heisenberg intertwiner differs from a fixed full-normalizer-equivariant intertwiner only by a GL(W) change of multiplicity basis. The traceless-orbit construction is covariant under that change: conjugation preserves sl(W), so changing the W basis carries each orbit hyperplane and its graph to the corresponding one. Thus the incidence

Z = {([r],[epsilon]) in P(V*) x P(W*): phi*(r tensor epsilon) is decomposable}

is precisely BHM's S_25, with a harmless automorphism of its P^1 factor. This is a direct intertwiner identity, not a deduction from a coincidence of thirty distinguished points.

BHM Section 3.4 defines S_25 by these equations and proves it smooth (Lemma 4). Section 4.5 Proposition 9 identifies its projection S_15 with the image of S(5) under D=I+2F, with only the stated paired points identified. These finite birational maps from smooth surfaces identify both sources with the normalization of S_15. Consequently Z is S(5); its second projection is the elliptic fibration, with class F, and its first projection pulls back O(1) to D. Finiteness here follows from properness and finite point fibers in Proposition 9 and in the explicit S_25 -> S_15 fiber description. Matching the quintic fibers identifies the two fibrations, up to an automorphism of the base.

We use BHM Section 4.3 Lemma 9:

5I = sum_(a,b in F_5) L_(a,b),

where the L_(a,b) are twenty-five distinct torsion sections. BHM Section 4.2 records they are pairwise disjoint, including at cusps.

## 2. The rank-one conic in each traceless hyperplane

Write L=span(p,q). Identify L tensor W* with 2 by 2 matrices by taking p,q and epsilon_1,epsilon_2 as bases, so that k becomes the identity. Then H_k=sl(W)^T k is the trace-zero hyperplane. Its annihilating bilinear form on L tensor W* is nondegenerate. Therefore, for each nonzero r in L, there is exactly one projective epsilon with r tensor epsilon in H_k. The resulting morphism P(L)->P(W*) is a projective isomorphism: it is the kernel map of a nondegenerate pairing between two two-dimensional spaces.

The rank-one tensors in P(H_k) thus form a graph C_k of bidegree (1,1) in P(L) x P(W*). Under the Segre embedding this is a smooth conic, and it spans the plane P(H_k). These assertions are invariant under changing the bases.

## 3. Zero wedge forces a torsion section

Assume omega wedge eta=0 for every omega,eta in N_k. In particular every nonzero form in N_k is decomposable, so C_k lies in Z. Since its second projection has degree one, C_k is a section of the elliptic fibration. Since its first projection is an isomorphism onto the line P(L),

F.C_k=1 and D.C_k=1.

As D=I+2F, this gives I.C_k=-1.

If C_k were distinct from all twenty-five torsion sections, nonnegative intersection of distinct irreducible curves on the smooth surface would give

5 I.C_k = sum L_(a,b).C_k >= 0,

a contradiction. Hence C_k is one of the twenty-five torsion sections.

This uses no classification of all lines on S_15 and no matrix evaluation.

## 4. Injectivity: a section graph determines [k]

The conic C_k spans P(H_k), and its first projection determines L. A hyperplane H in L tensor W* defined by a nondegenerate pairing uniquely determines [k]: in arbitrary bases, write its functional as tr(BX), with B invertible; then H= {D^T K: tr(D)=0} precisely when B is proportional to K^{-1}, with the transpose convention adjusted consistently. Thus K is determined up to scalar by H. Equivalently this is the inverse of the projective adjugate map on invertible 2 by 2 matrices.

Therefore the association [k] -> C_k is injective. There are at most twenty-five tensor-rank-two projective k for which N_k is zero-wedge.

Caution: Sections 1–5 alone establish an upper bound, not existence of twenty-five zero-wedge nets; Section 6 below upgrades it. A conic of decomposable forms in a plane only implies that every Plucker quadric on the plane is a multiple of the conic equation; their common coefficient may be nonzero. The converse is not used.

## 5. Actual primary-locus consequence

For the actual primary evaluation, an annihilator k at x gives x in the common radical of N_k. The universal zero-wedge classification says a three-dimensional zero-wedge net is either alpha (common radical dimension one) or beta (common radical dimension two). Thus all primary points admitting a tensor-rank-two zero-wedge annihilator lie in a union of at most twenty-five projective subspaces, each a point or a line.

By the already established actual support-drop result, outside the thirty rank-eight points every rank-nine annihilator has tensor rank two. Therefore the zero-wedge portion of the actual rank-nine locus has dimension at most one. In particular, on every two-dimensional irreducible component of that rank-nine locus the unique annihilator net contains a rank-four form generically.

This does not prove actual transversality, normality, reducedness, algebraicity of a lifting construction, or absence of lower-dimensional components. It does not identify the candidate lines with any previously named configuration.

## 6. Full-normalizer input upgrades the bound to exactly twenty-five beta nets

The full-group input is the N-equivariant decomposition Lambda^2 A = V tensor W, not merely its restriction to the Heisenberg group. Repository source pin: PR543 commit 7bf725bcd857a2deb975f9ecb80fca32e7833ae0, research/hm/order-four-quadratic-load/PRIMARY-INJECTION-AND-FAILURE.md, Section 1, A=A0=M0=V3 and W=W'. This is the third Galois transform of the HM Lemma 3.3 decomposition. The quotient complement I is SL_2(F_5); its central element z acts on A with eigenspace dimensions three and two and acts on W as minus the identity. The first assertion follows universally from the Schrödinger representation: inversion of the Heisenberg quotient is implemented, up to scalar by irreducibility, by the reflection e_i -> e_(-i). This reflection has eigenspaces of dimensions three and two. Since z has square one, the scalar is plus or minus one, merely exchanging the eigenvalue labels. The assertion about W follows from the cited full-module decomposition (equivalently from its central character). BHM Section 3.1 Lemma 2 provides the Weil extension. Only these representation properties are used below, not a selected vector or source matrix.

First, every torsion section produces a rank-two k, whether or not its full net is yet known to be decomposable. Indeed, L_ab has F-degree one and D-degree one: disjointness and self-intersection -5 give I.L_ab=-1 from Lemma 9. Its two projections are isomorphisms onto P^1 and a line respectively. Its Segre graph spans a hyperplane in the resulting two-by-two tensor space with nondegenerate annihilating pairing. Section 4 recovers a unique rank-two [k] from this hyperplane. Thus there are exactly twenty-five candidate [k].

The full normalizer acts on Z and preserves its two projective-factor hyperplane classes. Consequently it permutes these twenty-five section graphs. The translation group T=H_5/Z(H_5), identified with F_5^2, acts simply transitively on them by BHM Section 4.2. In this torsor the central element z of any chosen complement I acts by affine inversion, because it conjugates T by t -> -t. Affine inversion over F_5 has exactly one fixed point. Every element of I commutes with z and hence fixes that unique section. This proves existence of an I-stable candidate without having to identify a preferred modular zero section or compare Galois labels of three-dimensional representations.

Recovery of [k] from its graph is equivariant. Thus the corresponding k-line is I-stable. Since SL_2(F_5) is perfect, its character on this line is trivial; choose a nonzero invariant k. Then

sl(W) -> N_k,  D -> phi*(D^T k)

is an equivariant linear isomorphism, since k has rank two.

For completeness, sl(W) is an irreducible three-dimensional representation. W is irreducible: a one-dimensional summand of a representation of the perfect group I would be trivial, incompatible with z=-1 on W. Hence End(W)^I consists of scalars, so sl(W) has no trivial constituent. Its central action is trivial, so it factors through A_5. There is no nontrivial two-dimensional complex representation of A_5: such a representation has determinant one, and any nontrivial involution in SL_2(C) is -Id; faithfulness would contradict the distinct involutions in a Klein four subgroup, while simplicity forces a nontrivial representation to be faithful. There are also no nontrivial one-dimensional representations of A_5. Complete reducibility now forces the three-dimensional sl(W) to be irreducible.

Let A* = E_3 direct-sum E_2 be its z-eigenspace decomposition, labeled by dimension (not sign). The z-even part of Lambda^2 A* is

Lambda^2 E_3 direct-sum Lambda^2 E_2,

of dimensions three and one. Since N_k is z-even and irreducible of dimension three, its equivariant projection to the one-dimensional summand vanishes. Therefore

N_k = Lambda^2 E_3.

It is a beta zero-wedge net. Translation by T gives the same conclusion for all twenty-five candidates. Combined with Section 3, these are exactly all tensor-rank-two projective k having zero-wedge N_k. In particular, no such actual net is alpha.

## 7. Exact geometry in the actual primary parameter space

Define the primary evaluation e_x: A tensor sl(W) -> V tensor W by e_x(a tensor D)=(id_V tensor D)phi(a wedge x). Its annihilator space is ker(e_x*) contained in V* tensor W*. Passing to the usual Euler quotient does not change its image or rank.

For each candidate k, its common radical R_k is the annihilator of E_3, of dimension two, giving a projective line P(R_k) in P(A). For every x on that line, k is an annihilator of the primary evaluation e_x, so its rank is at most nine.

The established actual support theorem says the only points of rank below nine are the thirty rank-eight support-drop points; their V-support has dimension exactly four. At such a point, let p0 span the annihilator of that four-dimensional support. Then p0 tensor W* is contained in ker(e_x^*), and both spaces have dimension two, so they are equal. Every nonzero tensor in this kernel has tensor rank one. Thus no rank-two k can annihilate a rank-eight evaluation.

It follows that each of the twenty-five radical lines avoids the thirty rank-eight points and consists entirely of rank-nine points. The lines are distinct: a beta net is determined by its common radical, and its corresponding projective k is recovered uniquely from the net's inverse image under phi* as in Section 4.

The lines are pairwise disjoint. Otherwise a common point would have two independent annihilators k and k', forcing evaluation rank at most eight, which is impossible since either rank-two annihilator already excludes rank eight.

Finally, the rank-nine annihilator is unique. Thus its zero-wedge net occurs exactly on this union of twenty-five pairwise disjoint lines. Outside them, every rank-nine annihilator net contains a rank-four form; its radical is the unique Pfaffian line from PR560. This is an exact structural description of the zero-wedge obstruction in the actual family, not a selected-source computation.

No assertion of transversality, normality, scheme-theoretic reducedness along these lines, or lifting/algebraicity follows merely from this classification. In particular, exactly twenty-five geometric points does not assert reducedness or scheme length twenty-five of the zero-wedge locus in k-space. The result is geometric and set-theoretic; its proof uses ordinary characteristic-zero representation theory and the cited surface theorems, not formal proof checking.

## Public primary source

W. Barth, K. Hulek and R. Moore, Shioda's Modular Surface S(5) and the Horrocks-Mumford Bundle, in Vector Bundles on Algebraic Varieties. Sections 3.4, 4.2, 4.3 Lemma 9, 4.5 Proposition 9.
https://mathweb.tifr.res.in/Documents/Publications/Studies/Vector-Bundles-On-Algebraic-Varieties.pdf

Dependencies in this repository: PR560 (common-radical and alpha/beta classification), commit b9ee9b3b105967ee4d9e423d30cfa961ce0824d7; PR561 (universal net geometry), commit 7ebf187d7e45d43763bbf07436460f3c951aa8bd; PR554 (actual thirty-point support drop). The argument here makes the missing actual-family restriction, rather than importing generic universal transversality.
