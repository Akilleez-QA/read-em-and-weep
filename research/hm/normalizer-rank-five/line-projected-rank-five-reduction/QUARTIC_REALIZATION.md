# Globally realizable isolated quartic fibers

## Theorem

Each squarefree quartic normal form A and B in ../quartic-line-factor-cases/PROOF.md occurs as the exact residual kernel at an isolated middle line of an abstract outer-symmetric, cyclic-zero trilinear operation f:V³→J, with dim V=5 and dim J=20, for which every repeated-input map is injective. More precisely, rank Q_u=5 at the chosen line and rank Q_a=10 at every other middle line. The correction at u is zero.

Set-theoretically, the entire rank-two residual locus at u is the corresponding integral quartic surface. No determinantal scheme-structure claim is made. The ordered independent-zero fiber is the union of two smooth rational ruled surfaces exchanged by outer interchange and meeting in exactly two points. In case A each component is P¹×P¹; in case B each is the Hirzebruch surface F₂. The total separately projectivized independent-zero locus has dimension two, and its affine all-inputs-nonzero version has dimension five.

This proves genuine global occurrence of quartic line-factor fibers under the coarse universal hypotheses. It is not a seven-dimensional counterexample or a nonconstant middle family, and says nothing about occurrence in a specified physical source operation.

## 1. Local models and the exact rank-two locus

Let E=<x,y,z,w>, X=<x,y>, l=sx+ty. The two kernels are

    A: K=<xy,xz,xw−y²,yz−x²,yw>,
       W_l=<-tx+sz, -sy+tw>;

    B: K=<xy,xz−y²,xw,yz−x²,yw>,
       W_l=<w, -t²x−s²y+stz>.

Both have dimension five and full support. Both are contained in XE, and K∩Sym²X=Cxy. Any square belonging to XE has its vector in X, and xy is nonsquare, so K contains no nonzero square.

The displayed W_l have dimension two everywhere. Direct substitution shows they are exactly {m:lm∈K}. In A this is the kernel of the everywhere-surjective pencil

    s m_x+t m_z=0,  t m_y+s m_w=0.

In B replace both m_z,m_w in these equations by m_z. The displayed bases verify the kernel claim at s=0 and t=0 as well as on st≠0.

If q∈K has rank two, factor it as ab. Its image in Sym²(E/X) is abar bbar=0. The polynomial algebra on E/X is a domain, so one factor belongs to X. Therefore q=l m with m∈W_l, and the entire rank-two locus is the image of P(W). Conversely every such product belongs to K and has rank two because K is squarefree.

The projective-bundle surface is smooth, with W=O(-1)² in A and W=O⊕O(-2) in B. Multiplication uses the line bundle O_{P(W)}(1)⊗π*O(1), whose square is 4: equivalently the two scroll summand degrees are (2,2) or (1,3). The map is finite because a nonzero quadratic has at most two factor lines, and a selected line l determines the base and then m. It is generically birational because the second factor is generically outside X. Hence its image is an integral quartic surface.

The ordered-factor map P(W)→P(X)×P(E), (l,m)↦([l],[m]), is a closed embedding: it is the natural projective subbundle incidence. Its swapped image is a second smooth surface. Their intersection requires both factors to belong to X, and hence their product to lie in Cxy. Thus the intersection consists exactly of ([x],[y]) and ([y],[x]). This is a set-theoretic intersection statement; no transverse-intersection or scheme-length claim is made.

## 2. Universal graph realization

Write V=Cu⊕E and put

    T=ker[V⊗Λ²V→Λ³V],  dim T=40,
    f0(a,b,c)=a⊗(b∧c)+c⊗(b∧a).

This map is outer symmetric and cyclic zero. Its repeated map is A0_a(b)=a⊗(a∧b). Define F_a=im[Sym²V→T,bc↦f0(b,a,c)]. Then dim F_a=14, dim A0_a(V)=4, and F_a/A0_a(V)≅Sym²(V/Ca). These follow immediately by splitting V=Ca⊕U: a² maps to zero, aU maps isomorphically to the repeated subspace, and Sym²U maps injectively.

Prescribe L=B0_u(K)⊂F_u, with B0_u(q)=f0(-,u,-)(q). It has dimension five and prescribes correction zero. A nonzero member has second-factor support u∧im(q), of dimension at least two because K has no square.

The rank-one tensors in P(T) are exactly [a⊗(a∧b)] for independent a,b. Indeed a⊗β belongs to T iff a∧β=0, which forces β=a∧b after splitting off a. Thus P(L) contains no repeated tensor.

Moreover L∩F_a=0 whenever [a]≠[u]. A nonzero element of this intersection would have second support containing u∧e1 and u∧e2 with e1,e2 independent in E, both lying in a∧V. Hence a lies in span(u,e1)∩span(u,e2)=Cu, contradiction.

## 3. Generic quotient and exact residual ranks

Set Tbar=T/L, dim Tbar=35, and use G=Gr(15,Tbar), dim G=300. A point M determines a twenty-plane N⊂T containing L.

The condition M∩(F_u/L)=0 is a nonempty open because dim(F_u/L)=9 and 15+9≤35. Away from u, the images H_a of F_a in Tbar form a rank-fourteen subbundle. The incidence of (a,[h],M) with [h]∈P(H_a)∩P(M) has dimension

    4+13+dim Gr(14,34)=4+13+280=297<300.

Its constructible image has closure of dimension at most 297. Choose M in the intersection of its nonempty open complement and the previous nonempty open. Then

    N∩F_u=L,   N∩F_a=0 for every [a]≠[u].

These conditions also ensure that N contains no repeated rank-one tensor: each such tensor lies in some F_a, and L contains none. Thus J=T/N, dim J=20, and the quotient f of f0 have injective repeated-input maps at every line. Outer symmetry and cyclic zero descend.

Since the repeated images have dimension four,

    rank Q_a=dim(im F_a in J)−4=10−dim(N∩F_a).

This gives the stated exact ranks. At u, projection of L modulo A0_u(V) identifies the residual kernel exactly with K, and B_u(K)=0 gives correction zero.

## 4. Exact independent-zero fiber and dimensions

For q=lm∈K, lifting the outer factors as l+αu,m+βu yields

    f(l+αu,u,m+βu)=A_u(βl+αm).

Since A_u is injective and l,m are independent, α=β=0. Thus the ordered independent-zero fiber is exactly the ordered-factor union in Section 1, with u as fixed middle. At any other middle Q_a is injective, so no independent zero occurs. An independent zero with one residual outer factor zero would contradict repeated injection. If both residual outer factors vanish, all three inputs are collinear, which is excluded from the independent locus. Dependent nonzero residual factors would produce a square in K, also impossible.

Therefore the projective independent-zero locus has dimension two. Restoring three independent nonzero scalings gives affine dimension five. The construction is an isolated-fiber example, not an example with dimension seven.

## 5. Why the rank-six annihilation mechanisms do not capture these examples

Neither quartic K contains a common-factor plane eU with dim U=3. If e belongs to X then U is contained in the exact two-dimensional W_e. If e does not belong to X, projecting each product e a to Sym²(E/X) forces a∈X, again bounding dim U by two.

Nor does K contain a product A B with dim A=dim B=2. Projecting to Sym²(E/X) forces one of A,B to lie in X, hence equal X. The other would then be a fixed two-plane contained in every W_l, making W constant, contrary to degree -2.

In the constructed operation, any (1,3) or (2,2) zero rectangle at middle u would project injectively in both outer spaces to E by repeated-input injection. Its zero equation and correction zero force each projected product into K (and its u-cross correction to vanish). The preceding two exclusions therefore show that neither old annihilation mechanism occurs at u. At other middles residual injectivity already forbids such rectangles. This is not a claim about the different rank-one (2,3) rectangular incidence, which remains an open comparison here.

## Audit

This is the same universal Grassmannian quotient method as ../full-support-scroll-exclusion/COUNTERMODEL.md, with the graph correction set to zero and the squarefree quartic K substituted. Every hypothesis needed by that argument is verified above. Only symbolic tensor identities and algebraic incidence dimensions are used; no physical source rank, input or value is evaluated, and there is no external write. Source heads and current discussion were checked in the companion PROOF.md.
