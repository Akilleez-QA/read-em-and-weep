# The primary-bad quadratic scheme is integral and rational

Work over C. Let A=M_0 have dimension five, S=S_2 have dimension fifteen, and M=M_2 have dimension ten. Let m:S tensor A -> M be actual primary multiplication. On P(S), let B be the scheme defined by the maximal minors of

    mu: A tensor O(-1) -> M tensor O.

Then B is an integral rational eightfold of degree 210. Its homogeneous maximal-minor ideal is prime, saturated and Cohen-Macaulay. This concerns primary multiplication only; it does not decide the full adjoint quadratic map, a prescribed quadratic, higher-order lifting, or algebraicity.

## Exact dependencies

1. PR543, commit 7bf725bcd857a2deb975f9ecb80fca32e7833ae0, research/hm/order-four-quadratic-load/PRIMARY-INJECTION-AND-FAILURE.md: S=A tensor U', with U'=sl(W'), and actual multiplication (a tensor D)x=c(id tensor D)(a wedge x), c nonzero. In particular its dual evaluation factors through U'^* tensor Omega^1(2).
2. PR543, commit 8d24a12c4af9c922db2052a360c96a053dcba5b8, research/hm/order-four-quadratic-load/PRIMARY-BAD-CODIMENSION-THREE.md, Sections 1–2: the equivariant Euler-composed dual evaluation, perfectness of N, central weight of A, and absence of N-invariant quintics on A. The latter uses (Sym^5 A*)^H=U direct-sum U', with neither quotient summand trivial.
3. PR547, commit 5a8efc999e9b886c51f18232a580407bac4bbe66, research/hm/primary-evaluation-generic-surjectivity/PROOF.md: generic evaluation rank ten.
4. PR554, commit eb16c0e38e5157dc2902273cea3939b3410057c7, research/hm/global-support-finiteness/PROOF.md and EXPECTED-CODIMENSION.md: evaluation has rank eight precisely at thirty points and has rank nine or ten elsewhere; B is arithmetically Cohen-Macaulay, pure of dimension eight, with saturated maximal-minor ideal and degree 210. These are used as established inputs, not re-proved here.

All pins are in https://github.com/Akilleez-QA/read-em-and-weep . The representation source is Horrocks–Mumford (1973), Lemma 3.3 and Theorem 3.5: https://www.dam.brown.edu/people/mumford/alg_geom/papers/1973a--Rk2BdleP%5E4-NC.pdf .

## 1. The rank-nine locus has no divisor

Put X=P(A). The dual evaluation and Euler inclusion give equivariant maps

    beta: M* tensor O_X -> U'^* tensor Omega_X^1(2),
    b: M* tensor O_X -> U'^* tensor A* tensor O_X(1)=S* tensor O_X(1).

The second map has the same fiber rank as evaluation e_x:S->M, q->m(q,x). It is represented by a 15 by 10 linear matrix. Its nonzero maximal minors are degree-ten polynomials, and their span is N-stable. Generic rank ten guarantees this span is nonzero.

Let g be their homogeneous gcd. Unique factorization and invariance of the span imply that Cg is an N-stable line. Perfectness of N makes its character trivial, so g is invariant. The nontrivial order-five central character of A forces 5 to divide deg(g). Thus deg(g) is 0, 5 or 10. The invariant-quintic exclusion rules out five.

Suppose deg(g)=10. Every maximal minor is a constant multiple of g. The Plucker coordinates of the ten-dimensional image of b_x are consequently constant wherever b has rank ten. Hence this image, after ignoring the one-dimensional O(1) factor, is one fixed ten-dimensional subspace L of S*=U'^* tensor A*.

The Euler factorization supplies a contradiction without any irreducibility claim about S*. For every rank-ten x, the fixed subspace L lies in U'^* tensor x^perp, where x^perp is the kernel of evaluation A*->(Cx)*. The rank-ten x form a dense open subset of P(A). If a tensor t in U'^* tensor A* contracts to zero at all such x, the associated linear map A->U'^* vanishes on a dense set and hence is zero. Therefore the intersection of these subspaces is zero. This contradicts dim(L)=10.

Thus g is constant. Any divisorial component of the common zero locus of the maximal minors would have a homogeneous irreducible equation dividing all minors, impossible. Consequently

    D={x in X: rank(e_x)<=9} has dimension at most two.

This is a support-dimension assertion, not a reducedness assertion for D. The twisting by O(1) does not affect a fiber's projective image; in the Euler contraction argument its scalar trivialization cancels.

## 2. A unique top-dimensional incidence component

Let I be the closed incidence subscheme of X times P(S) cut out by m(q,x)=0, with projections p to X and pi to P(S). Its set-theoretic image under pi is exactly the support of B.

Let X_r be the locally closed rank-r stratum of evaluation. The only ranks are 8,9,10. Over each stratum, p has projective-space fibers of dimension 14-r. By the dependencies and Section 1,

    dim p^{-1}(X_8)=6,
    dim p^{-1}(X_9)<=7.

Let X_10=X minus D. It is nonempty, smooth and irreducible. On it the kernel of the universal evaluation S tensor O_X(-1)->M tensor O_X is a vector bundle of rank five. Thus p^{-1}(X_10) is a projective bundle with fiber P4. It is smooth, irreducible, and of dimension eight. Write I_0 for its closure with reduced structure.

The part p^{-1}(D) is closed and has dimension at most seven by the preceding finite rank stratification. Since pi is projective, its image E is closed and has dimension at most seven. Every point of B lies in pi(I_0) or E. But B is pure of dimension eight. Therefore all its irreducible components must lie in the single irreducible closed set pi(I_0). It follows that the support of B is irreducible and pi(I_0) is all of that support.

## 3. Generic rank four and the scheme-theoretic kernel graph

The dominant map I_0->B_red is between irreducible varieties of dimension eight. Its generic fiber has dimension zero. Outside E, every point of the full incidence fiber lies over X_10, and the full incidence fiber over q is P(ker(mu_q)). Thus the generic zero-dimensional fiber forces dim ker(mu_q)=1, equivalently rank(mu_q)=4. In particular the rank-four open subset B_4 of B is nonempty.

There is a scheme-theoretic isomorphism pi^{-1}(B_4)->B_4. To check this even before knowing B is reduced, work where a four-by-four minor of mu is invertible. Invertible row and column operations give the block matrix

    [ I_4  0 ]
    [  0   c ],

where c is a six-by-one column. The maximal-minor ideal on this open is exactly the ideal of the six entries of c. The incidence equations first force the first four kernel coordinates to vanish. The fifth projective coordinate is then nonzero and can be normalized to one, after which the remaining equations are exactly c=0. This identifies the incidence and B_4 with their stated scheme structures, not only their closed points.

Remove E and restrict to B_4. This leaves a nonempty dense open subset of B. Its incidence lies entirely in the smooth projective bundle p^{-1}(X_10). By the preceding isomorphism, this open of B is smooth. Consequently B is generically reduced.

## 4. Integrality and rationality

A Cohen-Macaulay scheme has no embedded associated points. Since B has irreducible support and is generically reduced, it is reduced: any nonzero nilradical would have an associated prime, necessarily the unique minimal prime, contradicting generic reducedness. Thus B is integral.

The same conclusion applies to the saturated homogeneous ideal. If a homogeneous class in the nilradical of R/I vanishes on Proj(R/I), it is irrelevant-ideal torsion; positive depth and saturation exclude such torsion. Reduced irreducibility of the projective scheme therefore gives a reduced irreducible affine cone, so I is prime.

Moreover the rank-four kernel-graph identification makes pi birational from the projective bundle p^{-1}(X_10) to B. Over the function field C(X), its rank-five kernel vector bundle is a five-dimensional vector space, so the bundle is birational to X times P4. Since X is P4, B is rational. This is birational rationality, not an assertion that the incidence is globally a projective bundle or that B is everywhere smooth or normal.

## Verification status and boundaries

This is a structural proof using pinned actual-model results. No selected actual polynomial, HM coefficient, matrix, minor, or numerical rank has been evaluated, and no large computation is used. The proof has been checked step by step by its author; independent review and formal proof-assistant verification are separate statuses. The degree 210 and Cohen-Macaulay assertions are inherited from PR554. The new conclusions are absence of a divisorial evaluation-rank drop and integrality/rationality of the primary-bad scheme. Nothing here identifies primary failure with full-adjoint failure or resolves the original selected source instance.
