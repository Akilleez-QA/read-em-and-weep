# Generic rank-three curves, including a globally repeated-injective cyclic realization

Work over C. This is an abstract existence construction, not an evaluation of a specified operation, and no normalizer equivariance is asserted.

## Theorem

There is an outer-symmetric cyclic-zero trilinear map f:V^3 -> J, with dim V=5 and dim J=20, such that:

- every repeated-input map V/Ca -> J is injective;
- a prescribed middle line [u] has residual rank three, and every other middle has residual rank ten;
- the middle fiber X in P(V) x P(V) is a reduced integral complete-intersection curve of seven symmetric (1,1) equations;
- X is smooth except at p=([u],[u]), and p has eight smooth branches with distinct tangent directions given by a transverse complete intersection of three quadrics in P3;
- p is its only dependent support point and its only swap-fixed support point.

Consequently all the hypotheses of the pure-curve alternative and the equality case of the swap-quotient theorem occur simultaneously in an abstract globally repeated-injective cyclic operation. Its normalization has genus 59; the quotient normalization has genus 28. The residual-rank-drop support is the single point [u].

## 1. Generic seven symmetric equations through p

Let S=P(V) x P(V), V=Cu direct-sum E. Let H be the fourteen-dimensional vector space of symmetric bilinear forms h on V with h(u,u)=0. Its linear system on S has set-theoretic base locus exactly p. Indeed all symmetric bilinear forms identify the symmetric Segre image of ([x],[z]) with [xz] in P(Sym^2 V); all forms vanishing on u^2 vanish on xz exactly when xz is proportional to u^2, which forces [x]=[z]=[u].

The rational map defined by H has image dimension eight. To verify this rather than assume that projection from a point is finite, start with the symmetric Segre map, whose fibers consist of at most the two ordered factorizations of a rank-two quadratic (and a single point at rank one). Project its eight-dimensional image from [u^2]. For a general rank-two tensor q whose support does not contain u, the line through [q] and [u^2] is not contained in the rank-at-most-two locus: q+c u^2 has rank three for c nonzero. Thus its intersection with that locus is finite, proving generic finiteness of the projection and image dimension eight.

Choose seven general members h1,...,h7 of H. Successive Bertini irreducibility gives an integral intersection of dimension one: after k general cuts, for 0<=k<=6, the remaining system has image dimension 8-k>=2, and its only possible base point is p. Equivalently one applies the standard irreducibility form of Bertini for a linear system whose image has dimension at least two. At each step the image dimension drops by one, since a general hyperplane section of the image has that dimension and the original rational map is generically finite. Bertini smoothness on S minus {p}, applied successively, shows that the intersection is smooth there. These are nonempty open conditions on the ordered seven-tuples.

For precision, the irreducibility assertion here concerns the support. The seven divisors have expected codimension seven and hence form a regular sequence on smooth S. Their intersection is Cohen--Macaulay. Since it is generically smooth, it is generically reduced; a Cohen--Macaulay scheme with irreducible support and generically reduced local ring is reduced. Thus X is integral as a scheme, with no embedded components.

Also, a general seven-tuple has no diagonal zero other than p. For each [a]!=[u], evaluation h -> h(a,a) is nonzero on H, so seven simultaneous vanishings have codimension seven in H^7. The incidence over P(V) minus {[u]} has dimension at most dim(H^7)+4-7. Its image closure is therefore proper. Removing it ensures the asserted diagonal avoidance. (No properness of that punctured parameter base is needed.)

## 2. First jets and the general tangent net

Write x=x0 u+a and z=z0 u+b. Every member of H has unique expression

    h(x,z)=x0 ell(b)+z0 ell(a)+c(a,b),

where ell is in E* and c is a symmetric bilinear form on E. For a general seven-dimensional equation space, the map to E* has rank four. Row reduction gives four equations

    x0 b+z0 a+B(a,b)=0

and three equations

    q(a,b)=0,

where B:Sym^2 E -> E and q:Sym^2 E -> C^3 are arbitrary general linear maps, with q surjective. Conversely any such pair (B,q) specifies a seven-dimensional subspace with this rank-four first-jet property. In particular q is a general net of quadrics, so q(t,t)=0 in P(E) is eight reduced transverse points.

Near p, put x0=z0=1, a=s+t and b=s-t. The equations are

    2s+B(s,s)-B(t,t)=0,
    q(s,s)-q(t,t)=0.

Eliminating s leaves three even equations with initial terms -q(t,t). Hence the completed tangent cone is the reduced complete intersection of this net. The blowup/implicit-function calculation in the swap-quotient theorem yields precisely eight smooth local branches. This also independently checks local reducedness and shows that p is singular, with local embedding dimension four and delta invariant twelve.

All the conditions just imposed are nonempty Zariski-open conditions in the same irreducible parameter space. The first-jet/net condition is nonempty from the displayed explicit parametrization. Thus they hold simultaneously; no claim that a specially chosen witness for one condition satisfies the others is needed.

## 3. Exact residual reconstruction and square avoidance

Let K=ker(q), a seven-dimensional subspace of Sym^2 E, and set v=B|K. Let b:Sym^2 V -> E direct-sum C^3 be the seven-dimensional middle map given by the displayed equations. It has b(u,u)=0 and b(u,a)=(a,0). For r in K, b(r)=(v(r),0).

If a^2 is in K and v(a^2)=lambda a for nonzero a, then

    b(a-(lambda/2)u, a-(lambda/2)u)=0.

This is a diagonal zero different from p, a contradiction. Thus v is square-avoiding: v(a^2) is never in Ca when a^2 is in K.

More generally, any zero pair whose residual outer vectors are proportional has both residual vectors zero. If exactly one residual is zero, the injectivity of b(u,E) forces the other to be zero. If both are nonzero proportional, rescale so they equal a; the zero condition gives q(a,a)=0 and B(a,a) proportional to a, again contradicting square avoidance. Hence all points except p correspond to triples independent with u.

For independent a,b with ab in K, the equation for outer lifts a+alpha u and b+beta u is exactly

    v(ab)+beta a+alpha b=0.

It has a unique solution in alpha,beta exactly when v(ab) is in span(a,b). This is the exact correction convention used in the universal quotient construction below, not merely a dimension count of a potentially different incidence.

## 4. Global cyclic realization

Use the universal forty-dimensional space

    W=ker(V tensor wedge^2 V -> wedge^3 V)

and the operation

    f0(a,b,c)=a tensor (b wedge c)+c tensor (b wedge a).

It is outer symmetric and cyclic zero. Write A0_a(b)=a tensor (a wedge b) and F_a=im(f0(-,a,-)); then dim F_a=14 and F_a/A0_a(V) identifies with Sym^2(V/Ca). These statements follow directly by splitting V=Ca direct-sum U.

For r in K, let B0_u(r)=f0(-,u,-)(r), and form the seven-dimensional graph

    L={B0_u(r)-A0_u(v(r)):r in K} inside F_u.

In rows Cu direct-sum E and columns u wedge E, this tensor has matrix

    [-v(r)^T; 2 M(r)],

where M(r) is the symmetric contraction matrix using ab=(a tensor b+b tensor a)/2. Its second-factor support is u wedge (im(r)+Cv(r)). Every nonzero such tensor has support dimension at least two: for rank(r)>=2 this is immediate, and for rank one it follows from square avoidance.

Consequently L contains no repeated-input tensor, since those have tensor rank one. Also L intersect F_a=0 for every [a]!=[u]. Indeed F_a is contained in V tensor (a wedge V). If a tensor from L belonged to F_a, its second-factor support would contain u wedge w1 and u wedge w2 for independent w1,w2 in E. The two containments in a wedge V force a in span(u,w1) intersect span(u,w2)=Cu, a contradiction.

Now put Wbar=W/L, of dimension 33. Choose a general thirteen-plane M in Wbar and let T be its inverse image in W, so dim T=20. We impose:

    M intersect (F_u/L)=0;
    M intersect image(F_a)=0 for every [a]!=[u].

The first is nonempty open since dim(F_u/L)=7 and 13+7<=33. For the second, the images of F_a form a rank-fourteen bundle on the four-dimensional punctured middle space. The incidence of a middle a, a line in its image F_a, and a thirteen-plane containing that line has dimension

    4+13+dim Gr(12,32)=17+240=257,

strictly less than dim Gr(13,33)=260. Its image closure is therefore proper. The two nonempty opens intersect.

Set J=W/T and f to be f0 followed by the quotient map. Then dim J=20 and

    T intersect F_u=L;  T intersect F_a=0 for [a]!=[u].

For a!=u the repeated-input maps remain injective automatically. At u, L intersects A0_u(V) trivially, as projection to the Sym^2 E part recovers r. Thus all repeated-input maps are injective. Residual ranks are

    rank Q_a=10-dim(T intersect F_a),

giving rank three at u and rank ten elsewhere.

Finally F_u/L is canonically the image of the earlier middle map b: both have kernel, on Sym^2 V, exactly Cu^2 plus the graph generated by r-u v(r) for r in K. Indeed b(r-u v(r))=v(r)-v(r)=0, and the universal graph maps to B0_u(r)-A0_u(v(r)). Thus the global operation has exactly the previously constructed middle fiber, scheme-theoretically.

## 5. Consequences and limits

The swap-quotient theorem applies with no additional genericity assumptions: p_a(X)=71, delta_p(X)=12, and there are no other singularities. Therefore g(X^nu)=59. Its swap quotient has arithmetic genus 36 and local delta eight, hence normalization genus 28. The eight branches give the eight ramification points of the normalized double cover.

This proves that the pure-curve equality case cannot be universally excluded from outer symmetry, cyclic zero, global repeated-input injectivity, isolated residual-rank-drop support, or the bounded K7 square-avoidance hypotheses alone. It does not realize a specified normalizer action or a prescribed target representation. In particular, if a group moves [u], this particular operation cannot be equivariant because residual rank singles out [u]. It makes no claim about the actual source operation or the existence of any surface component there.

## 6. Scheme-theoretic symmetric Segre quotient

Here is a separate ring-level identification, also valid beyond the generic construction. Let R be the Segre homogeneous coordinate ring, generated by r_ij=x_i z_j with the rank-one matrix relations. The swap sends r_ij to r_ji. Set a_ij=r_ij+r_ji and b_ij=r_ij-r_ji. They generate R; the a's are invariant and the b's anti-invariant. An invariant element of R lifts to an invariant polynomial in the a's and b's by averaging any lift. Such polynomials are generated by the a's and products b_ij b_kl. In R the identity

    b_ij b_kl = a_il a_jk - a_ik a_jl

expresses every such product using the a's. Thus R^swap is generated in degree one by the fifteen symmetric coordinates a_ij. Consequently the quotient of P4 x P4 is a closed subscheme of P(Sym^2 V).

Its closed points are exactly symmetric tensors of rank at most two: any rank-two quadratic over C factors as a product of two independent linear factors on its two-dimensional support, uniquely up to ordering, and a rank-one quadratic is a square. Since R^swap is a domain, its image scheme is reduced. It is therefore precisely the reduced symmetric rank-at-most-two variety, scheme-theoretically, rather than merely set-theoretically. No unproved claim about generators of its homogeneous prime ideal is needed.

If I is generated by any seven invariant linear forms h_i, averaging proves

    (R/I)^swap = R^swap/(h1,...,h7).

Indeed an invariant element in I has an expression sum h_i c_i; averaging the c_i gives an expression with invariant coefficients. Exactness of taking invariants proves surjectivity as well. Taking Proj identifies the swap quotient with the scheme-theoretic linear section of the reduced symmetric rank-at-most-two variety by the seven hyperplanes. In the generic model it is the curve in a P7 specified by the complete descended Segre linear series. This proof supplies the ring-level identification without assuming that a bijection on closed points is an isomorphism.
