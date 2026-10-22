# Minimal normal ramification for fourth-neighborhood characteristic lines

## Statement, physical locus, and dependencies

Work over C with the actual rank-two bundle F on X=P4 and integral quadric Q=(q=0), retaining the fixed marking and classified physical-center-even fourth lifts. Fix any permitted nonzero source pair (a,h); this is a universal assertion, not a selected-source evaluation.

The exact dependencies are:

- [PR687, commit 2874402c884a6b426cfd521a674c962a738f84a6](https://github.com/Akilleez-QA/read-em-and-weep/blob/2874402c884a6b426cfd521a674c962a738f84a6/research/hm/fourth-square-invariance/PROOF.md): J4 is trace-free of twist ten, J4|Q=a^3 h N, and J4^2=q^3 sigma Id on 4Q, where sigma is an intrinsic section of O_Q(14), common to all classified lifts.
- [PR766, commit a43b46c98e53716978d0a7750843f2224b4d2408](https://github.com/Akilleez-QA/read-em-and-weep/blob/a43b46c98e53716978d0a7750843f2224b4d2408/research/hm/uniform-full-scalar-exclusion/PROOF.md): sigma=a^3 h rho4 is a nonzero GLOBAL SECTION for every such source pair. It is not asserted nowhere zero.

Let U be the intersection of the smooth locus of Q, the nonvanishing locus of sigma, and the locus where a^3 h N is nonzero of rank one. Each is a nonempty open of integral Q, so U is nonempty. Only local neighborhoods over U are considered below.

After trivializing the relevant line bundles and F near an arbitrary point p of U, let S=O_{X,p}, R=S/(q), and let s in S be a lift of the local scalar sigma. Here q is a regular parameter, R is a regular local domain, and s is a unit. The represented endomorphism J over S/(q^4) satisfies

    tr(J)=0,             J^2=q^3 s I.                 (1)

For each positive integer e form the local normal ramification and its truncation

    C_e=S[t]/(t^e-q),      B_e=C_e/(t^(4e)).           (2)

The relevant local ring is at the point lying over p with t=0. The pullback J_e exists on B_e without requiring any extension of J beyond 4Q.

**Theorem.** On these local ramified thickenings, allowing finite etale unit-root covers, a J_e-invariant line direct summand exists if and only if e is even. Consequently the minimum normal ramification index is two. For even e there is an explicit pair of distinct invariant lines reducing to the same line on t=0; they do not split the rank-two bundle as an eigenline direct sum.

## 1. Odd ramification is impossible

The ring C_e is free over S by the monic relation. Multiplication by q is injective on C_e, hence multiplication by t is injective as well, since t^e=q. Also C_e/(t)=R. Consequently its successive t-adic layers are R, and the layers of B_e are R t^j for 0<=j<4e.

If a line direct summand L is invariant, J_e acts on L by a scalar lambda locally. Equation (1), restricted to the free rank-one module L, implies

    lambda^2=t^(3e) s in B_e.                         (3)

The right side has exact t-order 3e, strictly less than 4e. If lambda has order m, its nonzero leading coefficient in the reduced ring R has nonzero square. Thus either 2m>=4e and lambda^2=0, or lambda^2 has exact order 2m. Equation (3) forces

    2m=3e.                                           (4)

In particular e must be even. The same proof applies after any etale localization or etale cover: the residue ring along t=0 is still reduced, the t-adic layers are preserved by flatness, and s stays a unit. Thus etale base change alone cannot remove the unramified obstruction.

The argument also permits the normal equation q=v t^e with v a unit in a regular normal chart: it only replaces the unit s by v^3 s. The minimality claim concerns such regular normal ramification, not arbitrary nonreduced base changes with extra nilpotents.

## 2. Even ramification constructs characteristic lines

Suppose e is even and put m=3e/2. On B_e take the finite faithfully flat etale algebra

    B'=B_e[u]/(u^2-s).

It is free of rank two and etale because u and 2u are units. This is a unit-root cover, separate from the ramification t^e=q. Set

    lambda=t^m u.

Then lambda^2=t^(3e)s. In particular e=2 gives lambda=t^3 u on t^8=0.

Because J mod t is nonzero rank-one nilpotent at p, a local basis can be chosen with a unit off-diagonal entry. Write

    J_e = [[x,y],[z,-x]],       y a unit.

For completeness, if a diagonal entry is initially the available unit, x^2+yz=t^(3e)s implies yz is a unit, so both off-diagonal entries are units. Interchanging the basis handles a unit z. Equation (1) reads

    x^2+yz=lambda^2.

The two vectors

    v_+=(y,lambda-x),        v_-=(y,-lambda-x)

satisfy J_e v_+=lambda v_+ and J_e v_-=-lambda v_-. Their first coordinate is a unit, so each spans a free rank-one direct summand L_+ or L_- of B'^2. In fact these are the respective kernels of J_e-lambda I and J_e+lambda I: the first row solves the second coordinate uniquely, and the second row is then zero by x^2+yz=lambda^2. This verifies existence for every even e and proves the stated minimality.

No square root of a selected actual scalar value has been computed. The etale algebra is the universal algebraic adjoining of a root of a unit.

## 3. Exact coalescence and failure of diagonalization

Normalize generators to w_+=(1,(-x+lambda)/y) and w_-=(1,(-x-lambda)/y). Their slope difference is 2lambda/y, of exact order m. Thus L_+ and L_- are distinct over B', but reduce to the same kernel line of J mod t. More precisely they coincide after reduction modulo t^k exactly for k<=m, and become distinct modulo t^(m+1).

The annihilator of lambda in B' is (t^(4e-m)): this holds in B_e by its regular t-adic layers and is preserved by the free etale extension. It follows directly from the two first coordinates that

    L_+ intersect L_- = t^(4e-m)L_+ = t^(4e-m)L_-,
    B'^2/(L_++L_-) is isomorphic to B'/(t^m).          (5)

Indeed a common vector has the same scalar coefficient in both normalized generators, and that coefficient must annihilate 2lambda/y. Subtracting the two normalized columns also proves the quotient formula. The exponent 4e-m is 5e/2.

The determinant of the eigenvector columns is -2y lambda, not a unit. Thus this pair does not diagonalize J_e. Nor can ANY pair of invariant line direct summands decompose B'^2: modulo t, J is nonzero nilpotent over the reduced residue ring, while scalar actions on any invariant lines square to zero and hence vanish. A splitting into two such lines would make the reduction of J zero, a contradiction.

For the minimal index e=2, the explicit lines coincide through t^3, separate on t^4, intersect in t^5 L_+ = t^5 L_-, and have sum quotient B'/(t^3). These are exact truncated-ring identities, not a splitting on a reduced spectral cover.

We do not assert that these two lines exhaust invariant lines. Nilpotent perturbations of eigenvalues can produce additional roots of (3) on a thickening. The construction and formulas (5) concern the specified pair of opposite roots.

## Contribution and limits

PR687 excludes an unramified characteristic line when the intrinsic square scalar is nonzero. PR766 makes that exclusion apply uniformly to every nonzero source pair. The present result identifies the exact local cost of removing that characteristic-line obstruction: even normal ramification is necessary, index two is sufficient after an etale unit-root cover, and characteristic lines still cannot furnish an eigenline splitting. Equation (5) quantifies the residual coalescence on the nilpotent thickening.

All claims are local over U, where sigma is a unit and the reduced matrix is regular nilpotent. No extension across the scalar zero divisor, source divisors, zero scheme of N, or singular locus of Q is asserted. Choices of local equations and twist trivializations are retained; no global square-root line bundle, global ramified cover, global descent, or equivariant eigenline is constructed. This neither extends J to a fifth neighborhood nor determines the separate beta4 adjoint boundary modulo im(beta2). It proves no first-order, higher-order integrability, or algebraicity claim.

This is an authored structural proof. Its verification consists of the displayed ring-order argument and universal rank-two identities; independent review must be recorded separately. No selected actual HM/source coefficient, point value, matrix, rank, derivative, or large computation is evaluated, and no proof-assistant certification is claimed.
