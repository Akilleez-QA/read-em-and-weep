# Residual-rank-three fibers: swap quotient and eight-branch boundary

## Scope and statement

Work over C with dim V=5. Let f:V^3 -> J be outer symmetric and cyclic zero, and assume every repeated-input map A_a:V/Ca -> J, b -> f(a,a,b), is injective. Fix [u] of residual rank three. Put

    X = {([x],[z]) : f(x,u,z)=0} in P(V) x P(V),
    p = ([u],[u]),  sigma(x,z)=(z,x).

The established universal residual-rank-three bound gives dim X <=2. The seven-equation height bound gives every component dimension >=1. Thus there is an honest dichotomy: X is pure one-dimensional, or it has a surface component. The following new results concern the first alternative; no surface exclusion is claimed.

**Theorem.** If X has no surface component, then:

1. X is a connected complete-intersection curve of seven independent symmetric (1,1) equations, with arithmetic genus 71, Segre degree 70, and dualizing sheaf O_X(2,2).
2. Its finite outer-swap quotient Y=X/<sigma> has arithmetic genus 36. The natural Segre line bundle descends to a line bundle M on Y with degree 35 and h^0(Y,M)=8. Moreover Y is Gorenstein with omega_Y=M^2. These assertions include nonreduced curves.
3. At p the completed local ring has a presentation by three **even** equations in four variables, with quadratic terms exactly the annihilator net W=K_u^perp. The swap acts by minus the identity on all four variables. The point p is the only swap-fixed support point. The quotient has embedding dimension seven at its image, without a net-regularity assumption.
4. If the three net quadrics form a regular sequence, then the tangent cone is their complete intersection and the local multiplicity is eight. If their projective base scheme consists of eight reduced points, then X has exactly eight smooth local branches at p, its local delta invariant is 12, and each branch is preserved by the swap with tangent action -1. The quotient has eight smooth local branches, delta invariant eight, and embedding dimension seven at the image of p.
5. If, in addition to the reduced-eight-point assumption, X is reduced and integral, then its normalization has genus at most 59, the normalization of Y has genus at most 28, and their genera satisfy g(X^nu)=2g(Y^nu)+3. Equality 59 and 28 holds precisely when X has no singularities away from p.

Here delta refers to the length of normalization modulo the reduced local ring. It is used only where reducedness has been established or assumed. The theorem does not assert that a rank-three middle or an excess surface exists for the actual operation.

## 1. The complete-intersection alternative

The middle map b_u:Sym^2 V -> J has rank 4+3=7. It supplies seven independent symmetric bilinear equations. Repeated-input injectivity and cyclic zero imply that a zero triple is either independent or has all three projective lines equal; consequently p is the sole dependent support point. Every component of X has dimension at least one by the height theorem, and its independent part is dense. The universal independent-fiber bound therefore gives dimension at most two.

If no surface occurs, the seven generators have height seven in the regular ambient eightfold. They are a regular sequence, so X is Cohen--Macaulay, with no embedded components, and its Koszul resolution is exact. Adjunction and intersection theory give

    omega_X = O_X(2,2),
    deg O_X(1,1) = integral_(P4xP4) (h1+h2)^8 = 70.

Only the terms k=0,5,6,7 in the untwisted Koszul complex have nonzero ambient cohomology. The negative terms have H^8 dimensions 1,25,225, respectively. Thus

    chi(O_X) = 1 - 21 + 175 - 225 = -70,
    p_a(X)=71.

The same spectral sequence gives H^0(O_X)=C: all negative-term contributions have total degree at least one. Thus X is connected, and h^1(O_X)=71.

## 2. Equivariant Euler characteristic and the quotient

Give O(-k,-k) its natural factor-swap linearization. Every defining bilinear equation is symmetric, so sigma acts trivially on the seven-dimensional equation space, and hence on every exterior power appearing in the Koszul complex.

For k>=5, write U_k=H^4(P4,O(-k)), of dimension binom(k-1,4). Kunneth identifies H^8(O(-k,-k)) with U_k tensor U_k. The cohomological swap sign is (-1)^(4*4)=+1; thus sigma acts by the ordinary tensor flip, whose trace is dim U_k. The equivariant Euler characteristic is therefore

    chi^sigma(O_X)=1 - binom(7,5)*1 + binom(7,6)*5 - binom(7,7)*15
                  =1-21+35-15=0.

Since H^0=C, this yields tr(sigma|H^1)=1. In characteristic zero, taking invariants is exact. For the finite quotient pi:X -> Y,

    H^i(Y,O_Y)=H^i(X,O_X)^sigma.

Consequently h^0(O_Y)=1 and h^1(O_Y)=(71+1)/2=36. In particular p_a(Y)=36. Neither reducedness nor normality is required for this calculation.

The natural swap acts trivially on the fiber of L=O_X(1,1) at p: it interchanges two identical one-dimensional factors. All other closed points have trivial stabilizer. Finite-group descent therefore supplies an invertible sheaf M on Y with pi^*M=L. One can alternatively obtain M from the symmetric Segre map ([x],[z]) -> [xz] in P(Sym^2 V); its pullback is L, and it factors through the quotient. The quotient is generically free on every component, since p is its only fixed support point. Degree consequently divides by two:

    deg M=35.

For completeness the twisted Koszul resolution gives

    H^0(X,L) = (V^* tensor V^*) / W_b,

where W_b is the seven-dimensional symmetric equation space. The symmetric and alternating parts have dimensions 15-7=8 and 10, respectively. Taking invariants yields h^0(Y,M)=8. Thus the quotient has a natural eight-dimensional complete linear series of degree 35. No assertion of smoothness is implicit.

The quotient Y is Cohen--Macaulay. Locally this follows from the Reynolds direct-summand map and a system of parameters: an invariant parameter which is a nonzerodivisor on the pure curve X is also one on its invariant ring. Finite-map duality and invariants identify

    omega_Y = (pi_* omega_X)^sigma.

One way to verify the identity is to write pi_*omega_X as Hom_Y(pi_*O_X,omega_Y); its invariant part is Hom_Y((pi_*O_X)_sigma,omega_Y)=omega_Y, since averaging identifies coinvariants with O_Y. Equivariant adjunction identifies omega_X with L^2 with its natural linearization: swapping the ambient four-dimensional tangent blocks has sign (-1)^16=+1, and the seven equations are invariant. It follows that

    omega_Y = (pi_*pi^*M^2)^sigma = M^2.

In particular the quotient curve is Gorenstein, and its descended Segre polarization is a square root of its dualizing sheaf.

## 3. The even local net

Choose V=Cu direct-sum E. Split im b_u as im A_u direct-sum R, dim R=3, and identify im A_u with E. There are symmetric bilinear maps B:E x E -> E and q:E x E -> R such that, in affine coordinates x=u+a, z=u+b, the exact equations are

    a+b+B(a,b)=0,   q(a,b)=0.

The three scalar forms q(t,t) span W=K_u^perp. Set a=s+t, b=s-t. The equations become

    2s+B(s,s)-B(t,t)=0,   q(s,s)-q(t,t)=0.

The first four equations eliminate s uniquely as a formal series s(t), with

    s(-t)=s(t),
    s(t)=(1/2) B(t,t)+terms of degree >=4.

Thus the remaining three equations are even, with expansion

    g(t)=-q(t,t)+(1/4)q(B(t,t),B(t,t))+terms of degree >=6.

The swap is exactly t -> -t. These equations have no linear terms, so the embedding dimension at p is four. In the pure-curve alternative p is necessarily singular.

Without any regularity assumption on the net, write A=C[[t1,t2,t3,t4]]^sigma for the even power-series subring. Exactness of taking invariants gives the quotient completed local ring A/(g1,g2,g3): an invariant relation sum h_i g_i can be averaged to use invariant coefficients. The maximal ideal of A is generated by the ten quadratic monomials, and the three independent q_i impose exactly three independent linear relations on its cotangent space. Thus the quotient embedding dimension is 10-3=7. Higher even terms lie in the square of that maximal ideal and cannot change this count.

 If the three quadratic initial terms are a regular sequence, the standard filtered regular-sequence argument gives

    gr_m O_(X,p) = C[t1,t2,t3,t4]/(q1,q2,q3),
    Hilbert series = (1-z^2)^3/(1-z)^4 = (1+z)^3/(1-z).

Its multiplicity is eight.

## 4. Reduced net base and local normalization

Assume the projective complete intersection of the three quadrics in P3 consists of eight reduced points. Blow up the origin in the four-variable formal ambient space. Dividing each equation g_i by the square of a local exceptional parameter yields three strict-transform equations. Along the exceptional divisor they restrict to the three net quadrics. Their derivatives in the three projective directions have rank three at each of the eight base points. The formal implicit function theorem therefore makes the strict transform smooth there, with the exceptional parameter a local coordinate. There are eight branches, all smooth and with distinct tangent directions. This also proves local reducedness.

For the delta calculation, let R be this reduced completed local ring and Rbar the sum of its eight branch normalizations. A general linear function ell restricts to a parameter on every branch, hence m Rbar=ell Rbar. Moreover

    R intersect m^n Rbar = m^n R.

Indeed the associated graded ring of R is the reduced cone over the eight points; a nonzero initial form cannot vanish at all eight points. A function outside m^n consequently has order <n on at least one branch. It follows that the associated graded pieces of Rbar have dimension eight, while those of R have dimensions

    1, 4, 7, 8, 8, ... .

The finite normalization defect is therefore

    delta_p(X)=(8-1)+(8-4)+(8-7)=12.

The swap fixes each tangent direction and hence each of the eight branches. On a branch one may choose an anti-invariant parameter r (average any parameter with its negative transform); sigma(r)=-r. Thus on the degree-n associated graded normalization piece its action is (-1)^n. The same is true for the graded local ring. Taking invariant parts of the normalization-defect sequence is exact, so only even degrees contribute to the quotient delta:

    delta_(pi(p))(Y)=(8-1)+(8-7)=8.

Its local genus, defined as delta minus the number of branches plus one, is therefore 8-8+1=1. This numerical statement makes no analytic classification claim.



## 5. Normalization and Riemann--Hurwitz

Assume X reduced and integral. Then Y is reduced and integral, and the quotient of the smooth normalization X^nu by sigma is Y^nu. Away from p the action on X is free, so the normalized double cover has no ramification there. Over p there are exactly eight points, each fixed with tangent action -1. Riemann--Hurwitz gives

    2g(X^nu)-2 = 2(2g(Y^nu)-2)+8,
    g(X^nu)=2g(Y^nu)+3.

Since p contributes delta 12 and pi(p) contributes delta eight,

    g(X^nu)<=71-12=59,
    g(Y^nu)<=36-8=28.

Equality holds when there are no additional singularities; conversely equality for X forces all other delta contributions to vanish, hence smoothness away from p. The genus relation makes the two equalities equivalent.

## Limitations and relevance

The new quotient genus, quotient polarization, local eight-branch delta defect, and normalization genus relation restrict the pure-curve branch of the rank-three problem. Finiteness of actual rank-three middles and the global rank lower bound are compatible with these results but are not needed in their proofs. In particular they do not by themselves exclude an excess surface, guarantee transverse net quadrics, or prove global reducedness or irreducibility.
