# Exact trace restriction to torsion sections and five-step divisor recursion

## 1. The actual residual cover, including its cusp closure

Let p:J_P->S_w be the finite flat degree-four graph cover, with p_*O=O directsum T. Its source is the smooth blowup of S_x at the sixty reduced cusp nodes, and its ramification divisor is the reduced exceptional divisor E. Each exceptional curve maps isomorphically onto one target cusp component. These statements are proved in TRACE-THIRD-TWIST-CUSP-JET-PRESENTATION.md, published at 8a3d83959ece33e52028556f5eb086bda120cdd6.

Fix a five-torsion section C_i on the target. Its unique five-torsion inverse under multiplication by two is a source section mapping isomorphically to C_i. The map is etale along this section, so it splits as an open-and-closed component of p^-1(C_i). Write the residual degree-three cover as r:B_i->C_i. Over the smooth modular locus it parametrizes translates of the three nonzero two-torsion points.

This residual cover is smooth also over each cusp. The target C_i meets a cusp component at a smooth point, transversely to that fiber, never at a polygon vertex. At a preimage on E the map of smooth surfaces has ramification index two, restricts isomorphically on E, and has no other ramification divisor nearby. Choose a coordinate along the target component, whose pullback is a coordinate along E. The transverse target parameter pulls back to a unit times a square of a local equation of E; absorbing the unit by an analytic square root gives the local form

 (u,v) -> (u^2,v).

The preimage of the transverse target section is consequently smooth, with simple degree-two ramification over its modular parameter. All other points are etale. Thus B_i is the smooth compactification of the residual modular three-cover, not a possibly singular curve sharing only its generic function field.

BHM Section1.3(b), printed page33, identifies this nonzero-two-torsion three-section with Bring's curve and its modular degree-three map. Since the covers above have the same smooth-locus function field, their smooth compactifications agree. In particular B_i is connected of genus four. The twelve simple ramification points give the independent check 2g-2=3(-2)+12=6.

## 2. Its triple-cover algebra is balanced

The canonical model of Bring's curve is given by

 sum x_i=0,   sum x_i^2=0,   sum x_i^3=0

in P4. This primary model is recorded in Braden and Disney-Hogg, 'Bring's curve: old and new', Definition2.1 and Section2.1. On the four-dimensional vector space sum x_i=0 the quadratic form sum x_i^2 is nondegenerate: its orthogonal complement in C5 is spanned by (1,1,1,1,1), which is not in that hyperplane. Thus the canonical quadric Q is smooth, and B_i is a (3,3) curve on Q=P1 x P1.

Every degree-three pencil on a canonical genus-four curve on a smooth quadric is one of its ruling pencils. Indeed a general fiber divisor spans a line in the canonical P3 by Riemann–Roch; that line meets Q in length three and hence is contained in Q. The varying lines belong to one ruling. For L=r^*O_P1(1), it follows that L=O_Q(1,0)|B_i, up to swapping rulings. The sequence

 0 -> O_Q(-1,-3) -> O_Q(2,0) -> O_B_i(2L) -> 0

has zero H1 in the first term by the Kunneth formula. Hence h0(B_i,2L)=3.

Write r_*O_B_i=O directsum O(-a) directsum O(-b), with a<=b. Connectedness makes a,b positive, and genus four gives a+b=6. Clifford's inequality for the degree-three pencil gives h0(L)=2, excluding a=1. The only remaining possibilities are (a,b)=(2,4) or (3,3). The former gives h0(2L)=4, while the latter gives three. Therefore

 r_*O_B_i=O directsum O(-3)^2.

The full degree-four algebra restricted to C_i is O directsum r_*O_B_i. Quotienting by its diagonal unit identifies the trace-free bundle, as a bundle, with r_*O_B_i. Thus the actual global restriction is

 T|C_i = O directsum O(-3)^2.                         (1)

This conclusion retains the cusp extension; it is not inferred from generic elliptic fibers alone.

## 3. Exact five-step pushforward recursion

Let C be the disjoint union of all twenty-five target torsion sections, so C=5I and O_C_i(I)=O_P1(-1). The established modular acyclicity is Rq_*T=0. Apply it to

 0 -> T -> T(5I) -> T(5I)|C -> 0.

Equation (1) proves immediately

 q_*T(5I)=O(-5)^25 directsum O(-8)^50,
 R1 q_*T(5I)=0.

More generally, induction through C gives, for every integer m>=1,

 q_*T(5mI)=directsum_(r=1)^m [O(-5r)^25 directsum O(-5r-3)^50],
 R1 q_*T(5mI)=0.                                    (2)

The extensions really split: at step m the quotient is O(-5m)^25 plus O(-5m-3)^50, whereas the smallest degree in the preceding bundle is -5m+2. Every relevant Ext1 is therefore an H1 of a line bundle of degree at least two, hence zero. No general positive-twist vanishing is being assumed.

Running the restriction sequence in the negative direction gives

 q_*T(-5mI)=0,
 R1 q_*T(-5mI)=directsum_(r=0)^(m-1)
                  [O(5r)^25 directsum O(5r-3)^50].    (3)

Here the new subbundle at step m has minimum degree 5m-8, while the old quotient has maximum degree 5m-10; again all relevant Ext1 vanish. This proves the splitting inductively.

For example, since H=I+2F, (3) with m=1 gives the exact next checkpoint

 R1 q_*T(-5H)=O(-10)^25 directsum O(-13)^50.

Its rank75 and degree minus900 agree with the independent Euler calculation. These splittings do not determine R1 q_*T(-3H), because the intervening actual restriction maps are not diagonalized by the five-step recursion. Nor do they prove H0(K4)=0.

## Sources

BHM, Section1.3(b), printed page33, identifies the twenty-five three-sections with Bring's curve and the modular three-cover:
https://mathweb.tifr.res.in/Documents/Publications/Studies/Vector-Bundles-On-Algebraic-Varieties.pdf

Braden and Disney-Hogg, Definition2.1 and Section2, give the canonical model used solely to verify that its quadric is smooth:
https://link.springer.com/article/10.1007/s40879-023-00706-0

The exact graph cover and trace algebra are pinned at 83cfae3ee74dd32cdb476be617489131c115f7f3; the reduced cusp center and exceptional-component identifications are pinned at 8a3d83959ece33e52028556f5eb086bda120cdd6. No selected HM coefficient or rank experiments are used.

## 4. A sharper upper bound for the third negative twist

For the fixed smooth target quadric section Y in |2H|, the restriction sequence gives a surjection

 R1 q_*T(-5H) -> R1 q_*T(-3H) -> 0,

because q_Y is finite and both degree-zero negative direct images vanish. Dualizing and twisting by O(-5) therefore gives the actual injection

 B_3=(R1 q_*T(-3H))^dual(-5)
      -> O(5)^25 directsum O(8)^50.

Every line-bundle summand of B_3 has degree at most eight. This is sharper than the degree bound from its inclusion into E_12(15), but does not prove the tempting balanced splitting O(4)^45. The map depends on Y and is retained as an actual restriction map.

## 5. Exact global cohomology of the third-twist middle bundle

Set M_3=(R1 q_*T(-3H))(12)=B_3^dual(7). Since all summand degrees of B_3 are at most eight, all summand degrees of M_3 are at least minus one. Consequently

 H1(P1,M_3)=0,   h0(P1,M_3)=rank(M_3)+deg(M_3)=45+135=180.

The already established twist-four value sequence

 0 -> V_4 -> M_3 -> O(6)^15 -> 0

therefore has the exact global cohomology sequence

 0 -> H0(V_4) -> C^180 -> C^105 -> H1(V_4) -> 0.

In particular h0(V_4)=75+h1(V_4). The arrow from 180 to105 is the actual quadric-induced map; its global surjectivity is not assumed. This fixes the middle bundle's cohomology without fixing its splitting or the remaining map rank.
