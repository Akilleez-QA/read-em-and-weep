# Total self-duality and its failure to commute with boundary restriction

## Assumptions and contribution

Use the family in [PR228](https://github.com/Akilleez-QA/read-em-and-weep/pull/228), commit `06c7e2f13e902d819bb6945c033fd455a5f28eac`. Set B=C[lambda,lambda^{-1}], S=B[x1,x2,x3,x4], and center its entire complex by a shift of one: A=S(1)^4, E=S^10, and A*=S(−1)^4. Use the same displayed matrices L:E→A and b=JL^t:A*→E. Here A and E are free of ranks four and ten, J is invertible alternating, LJL^t=0, and P=coker L is supported on the axis Z=V(x1,x2,x3,x4). Write I=im L, K=ker L, N=K/im b. Thus P and N in this note are the degree-one shifts of the uncentered modules bearing those names in PR228, and Q_c is shifted likewise. The underlying ungraded modules are unchanged. PR228 proves B-flatness of N and, at c^4=1, the exact sequence

    0 → N_c → M_c → Q_c → 0,

where M_c is the reflexive true middle cohomology of the specialized complex, and Q_c is the length-one origin module. It also proves the corresponding centered projective sheaf F_c is slope stable, its hull G_c=M_c~ is slope stable, and their quotient is a vertex skyscraper Q.

The new statement is that N is reflexive and alternating self-dual on the total regular five-dimensional space. Nevertheless the natural ordinary-dual base-change map is not an isomorphism at a fourth root: its cokernel is precisely Q_c. On the centered projective fiber every nonzero scalar-valued bilinear pairing is a scalar multiple of this alternating pairing and has this same length-one defect. Thus the failure is intrinsic, not a poorly chosen form or a defect of total-space self-duality.

All dual statements use this centered convention. The length table can also be read ungraded. Returning to the uncentered complex requires its corresponding degree shifts. Derived duals use cohomological grading, so Ext^i occurs in degree i. No assertion about an actual Horrocks–Mumford source, c2=5 realization, or the remaining pure diagonal conditions is made.

## 1. Reflexivity on the total space

Off Z, L is surjective and the symplectic quotient is locally free of rank two. The only primes on Z correspond to primes of B. They have height four (the generic point of Z) or five (its closed points). At such a prime p, put T=S_p. It is regular of dimension d=4 or 5. The free modules A_p and E_p have depth d. Repeated use of the depth lemma in

    0→I_p→A_p→P_p→0,
    0→K_p→E_p→I_p→0,
    0→T^4→K_p→N_p→0

gives depth(I_p)≥1, depth(K_p)≥2 and depth(N_p)≥2. The last inequality uses d−1≥3. These bounds do not assume B-flatness of P; its boundary torsion causes no problem.

A torsion submodule of N would have an associated prime on Z, because N is locally free elsewhere. At an associated prime N has depth zero, contradicting the preceding bounds. Hence N is torsion-free. It satisfies S2 at all primes, so it is reflexive over the regular normal domain S.

This argument is about the total space. It does not assert that an S2 total module has S2 fibers: here the B-flat quotient by lambda−c lowers the boundary depth from two to one.

## 2. Perfect alternating form on the total reflexive sheaf

The alternating form J^{-1} on E restricts to K. Its radical contains im b, since for k∈K and a∈A*,

    (JL^t a)^t J^{-1} k = −a^t Lk = 0

with the stated transpose sign. Equivalently, im(JL^t) is the symplectic orthogonal complement of ker L wherever L is surjective. Thus it descends to an alternating pairing on N. On S\Z this pairing is perfect by ordinary symplectic linear algebra.

Both N and N*=Hom_S(N,S) are reflexive. A morphism between reflexive modules that is an isomorphism off a closed set of codimension at least two is an isomorphism: each module and each morphism is the unique extension of its restriction across that set. Here Z has codimension four. Consequently the descended map

    psi:N → N*

is an isomorphism. Equivalently, the perfect alternating form on the rank-two bundle off Z extends uniquely and remains a perfect module pairing on the total reflexive module. The fact that N need not be locally free does not contradict perfect module self-duality.

The same conclusion holds for the centered sheaf F on P4_B. Its non-locally-free locus is contained in the vertex section, of codimension four. The alternating form has values in O after centering.

## 3. Exact failure of ordinary-dual base change

Fix a fourth root c and write t=lambda−c. For a finitely generated S-module N that is B-flat, multiplication by t gives 0→S→S→S/(t)→0. Applying Hom_S(N,−) gives the exact sequence

    0 → N*/tN* → Hom_{S/(t)}(N/tN,S/(t))
      → Ext_S^1(N,S)[t] → 0.

Here [t] denotes the kernel of multiplication by t; no surjectivity of arbitrary Hom base change has been assumed. The middle identification is the elementary adjunction for S→S/(t).

In this family Ext_S^1(N,S)≅P, with the grading convention retained. To see this directly, P has grade at least four since its support has codimension four in the regular S. Thus Ext_S^i(P,S)=0 for i<4. Dualizing 0→I→A→P→0 and 0→K→E→I→0 identifies K* with E*/im L*. Dualizing 0→A*→K→N→0 then identifies Ext^1(N,S) with the cokernel of the induced K*→A. The alternating invertible J identifies this cokernel with coker L=P. This is a total-space calculation, not an inference from the fibers.

The B-module calculation of PR228 gives P[t] one-dimensional at c^4=1, zero elsewhere. Consequently

    0 → N*⊗_B C_c → (N_c)* → Q_c → 0.

Using psi identifies the first arrow with the specialized alternating pairing N_c→(N_c)*. Under (N_c)*≅(M_c)* and the symplectic self-duality M_c≅(M_c)*, it is exactly the inclusion N_c→M_c from the boundary calculation. This follows either by restricting the common J^{-1} pairing off the origin and extending, or by the same kernel diagram defining N_c→M_c.

The identification with Q_c is therefore also equivariant when the original pairing is equivariant. It is the correction character of PR228, not a character inferred by forgetting canonical duality factors. In particular the C4 eigenvalue is c, not c^{-1}. The central convention is the one fixed in PR228. This statement concerns the cokernel of ordinary-dual base change, not the character of its Ext-dual.

## 4. Complete total-to-fiber Ext defect table

Here is a finite change-of-rings proof that does not assume a relative-duality theorem without checking its hypotheses. Work ungraded and nonequivariantly in this paragraph, choosing the displayed coordinates to identify the orientation lines. Because the uncentered P of PR228 has no degree at least four, each x_i^4 annihilates it and also annihilates its centered shift P. Put

    T=S/(x1^4,x2^4,x3^4,x4^4).

The four elements form an S-regular sequence. The Koszul resolution gives RHom_S(T,S) with its only cohomology in degree four, equal to T (with the regular-sequence grading and determinant shift). The change-of-rings adjunction therefore gives

    Ext_S^{4+j}(P,S) ≅ Ext_T^j(P,T),

and Ext_S^i(P,S)=0 for i<4. One may obtain this adjunction from free resolutions and the Koszul resolution; its change-of-rings spectral sequence has a single nonzero row, so no extension or differential ambiguity occurs.

The B-algebra T is finite free, with basis x1^a1...x4^a4 for 0≤a_i≤3. The functional taking the coefficient of x1^3 x2^3 x3^3 x4^3 makes the pairing (u,v)↦coefficient(uv) perfect over B: its matrix pairs each basis monomial with its unique complementary monomial and is a permutation matrix. Thus

    T ≅ Hom_B(T,B)

as T-modules, ungraded after the chosen orientation. For an injective B-module J, Hom_B(T,J) is injective as a T-module, since the adjunction Hom_T(−,Hom_B(T,J))=Hom_B(−,J) is exact. Also Hom_B(T,−) is exact because T is B-free. Applying this to an injective resolution of B proves

    Ext_T^j(P,Hom_B(T,B)) ≅ Ext_B^j(P,B).

This establishes the needed relative duality here by a finite complete-intersection calculation. In graded notation the net shift is +4: the Koszul shift +16 and the Frobenius shift −12 combine. Equivariantly the corresponding orientation character must likewise be retained; the following dimensions and lengths do not discard it to make a character claim.

PR228's B-module normal forms now give

    Ext_S^4(P,S) ≅ Hom_B(P,B), B-free of rank 16,
    Ext_S^5(P,S) ≅ Ext_B^1(P,B) ≅ B/(lambda^4−1),
    Ext_S^j(P,S)=0 for j≠4,5.

The first two isomorphisms in this display suppress the just-described shift and orientation only. The B/(lambda^4−1) calculation uses the two-term B-free resolution of that cyclic summand; the other sixteen summands are free.

The same three monad short exact sequences used in Section 3 give, beyond Ext^1(N,S)=P,

    Ext_S^2(N,S) ≅ Ext_S^4(P,S),
    Ext_S^3(N,S) ≅ Ext_S^5(P,S),
    Ext_S^i(N,S)=0 for i≥4.

For example Ext^i(N,S)=Ext^i(K,S) for i≥2, then Ext^i(K,S)=Ext^{i+1}(I,S)=Ext^{i+2}(P,S). Consequently N has projective dimension three at the four closed boundary points on Z, depth two there, and projective dimension two at every other point of Z. The total sheaf's reflexive self-duality is compatible with these facts.

To check restriction in every degree, choose a finite projective S-resolution of N. Tensoring it with B/(lambda−c) remains a resolution of N_c because N is B-flat; its Hom complex therefore restricts to the complex computing Ext_R(N_c,R). The long exact sequence for multiplication by lambda−c on the original Hom complex yields

    0 → Ext_S^i(N,S)⊗_B C_c → Ext_R^i(N_c,R)
      → Tor_1^B(Ext_S^{i+1}(N,S),C_c) → 0.

At c^4=1 this gives the full table:

- i=0: the left term is N_c via total self-duality; the middle term is M_c via fiber hull duality; the right term is Q_c.
- i=1: P_c maps isomorphically to Ext_R^1(N_c,R), of length 17, since Ext_S^2(N,S) is B-flat.
- i=2: a length-16 specialization of Ext_S^2(N,S) injects into Ext_R^2(N_c,R)=D(P_c), of length 17, with length-one cokernel Tor_1^B(Ext_S^3(N,S),C_c).
- i=3: Ext_S^3(N,S)⊗C_c maps isomorphically to Ext_R^3(N_c,R)=D(Q_c), of length one.

Away from the four roots, both torsion corrections vanish, and the positive Ext lengths are 16,16,0. Thus a single total Ext^3 torsion module explains the second-Ext jump, whereas torsion in total Ext^1 explains the failure of ordinary-dual base change. They occupy different positions in the exact sequence and must not be conflated. No canonical splitting of these short exact sequences is asserted.

## 5. Classification of global boundary pairings

Let F=F_c and G=F** on P4_C at a fourth root. The inclusion i:F→G has quotient Q of length one. Since G is reflexive and F=G away from the vertex, any morphism F→G extends uniquely to G→G. Indeed restrict to the complement of the vertex, extend the map between reflexive hulls, and compare on F: the difference has image supported at the vertex inside torsion-free G, so vanishes. Thus

    Hom(F,G)=Hom(G,G).

Slope stability of G implies Hom(G,G)=C. For completeness, a nonzero endomorphism has full rank by stability, and equal Hilbert polynomials make it an isomorphism. An endomorphism has a complex eigenvalue: choose one in any fiber where G is a bundle. The difference from that scalar is not invertible on that fiber, and hence cannot be a nonzero endomorphism. It is zero.

Dualizing 0→F→G→Q→0 gives F*=G* because Hom(Q,O)=Ext^1(Q,O)=0 on the smooth fourfold. The centered alternating form identifies G*≅G. Therefore

    Hom(F,F*) = C.

The nonzero generator is the restriction of the alternating form of G. Every bilinear O-valued pairing F⊗F→O is therefore a scalar multiple of that alternating form. Every nonzero pairing has injective associated map F→F* and cokernel Q. None is perfect. In particular a different choice of symmetric, nonsymmetric, or alternating form cannot repair this boundary fiber. This is stronger than merely observing that the originally displayed form degenerates.

The zero-dimensional degeneracy scheme of each nonzero associated map, defined by Fitt_0(coker), is the reduced vertex: Q has length one. This definition does not pretend F is a vector bundle or use a determinant matrix on a nonexistent local frame.

## 6. Derived distinction and the obstruction to restoring self-duality

Locally at the vertex let R be the regular four-dimensional ring and D(U)=Ext_R^4(U,R) for finite-length U. PR228 gives

    Ext^1(F,R)=P_c,  Ext^2(F,R)=D(P_c),  Ext^3(F,R)=D(Q),

with lengths 17,17,1, and Hom(F,R)=G. The exact triangle from 0→F→G→Q→0 is

    D(Q)[−4] → RHom_R(G,R) → RHom_R(F,R) → D(Q)[−3].

Thus the derived difference between the duals of F and G is exactly D(Q)[−3]. It must not be replaced by Q or by an unshifted skyscraper. Even G's derived dual has its own positive Ext groups, so ordinary reflexive self-duality G≅G* is not a statement G≅RHom(G,R).

The ordinary alternating form supplies the canonical composite F→H^0(RHom(F,R))→RHom(F,R). If C is its cone, the cohomology sequence gives

    H^0(C)=Q,  H^1(C)=P_c,
    H^2(C)=D(P_c),  H^3(C)=D(Q),

and no other cohomology. This records both the new boundary defect and the pre-existing isolated reflexive singularity defects. It follows at once that F is not isomorphic to its unshifted derived dual, nor to any shift of it: the latter has nonzero cohomology in four distinct degrees.

Together with [PR248](https://github.com/Akilleez-QA/read-em-and-weep/pull/248), commit `905ad4ea6000cbd7c26d01261a17ba4574e6238f`, this excludes a slope-semistable flat filling of the same fixed generic sheaf whose special fiber carries a perfect scalar-valued pairing. Any such filling would have special fiber isomorphic to F, while Section 5 rules out a perfect pairing on F. This remains true after the finite DVR base changes covered there. It does not exclude unstable fillings or changed generic sheaves.

## Verification status

The new derivation checks total-space depth before asserting reflexivity; separates ordinary duality from derived duality; derives the dual-base-change correction from an exact Hom sequence; and classifies all global pairings rather than one chosen matrix. PR228 supplies its already published boundary normal forms and Ext calculation. This text is an authored proof, not a machine-formal verification. No source instance or large computation is evaluated. Independent review is required before publication.
