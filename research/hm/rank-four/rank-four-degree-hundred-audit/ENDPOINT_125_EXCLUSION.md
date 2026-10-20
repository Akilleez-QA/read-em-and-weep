# Excluding the degree-125 endpoint: exact degree 100

## Statement and dependencies

Under the hypotheses and imported results in `AUDIT.md`, a nonempty rank-four reduced curve has degree exactly 100.

The preceding audit already proves that its only possible total degrees are 100 and 125. This extension excludes 125. It uses the established honest G-representation V=T plus W, where T and W are inequivalent irreducibles of dimensions three and two, and T is an icosahedral representation factoring through A5. These are the same representation conventions used in `../rank-four-degree-three-four-exclusion/PROOF.md`.

## 1. The only possible non-A-stable endpoint configuration

Suppose Gamma has total degree 125. Every component has degree at least five. If every component is A-stable, each spans P4 and the disjoint-normalization lemma in `AUDIT.md`, Section 2, gives 50|125, impossible.

There is therefore a non-A-stable component C. An A-orbit of size five forces at least 30 N-translates, of total degree at least 150, impossible. Thus its A-orbit has size 25. Its degree is at least five, so this orbit already contributes at least 125. Equality of the total degree forces:

- deg C=5;
- Gamma consists of exactly these 25 translates;
- the entire N-orbit of C equals this free A-orbit.

Consequently K=N_C has order 3000/25=120, intersects A trivially, and maps isomorphically onto G=N/A. It is a complement to A.

## 2. Conjugating the complement and restricting the span

In the fixed splitting N=A semidirect G, K is the graph of a cocycle c:G->A. Let z=-I be the central involution of G. Since z acts as -1 on A, comparing the cocycle identities for zh and hz gives

    c(z)-c(h)=c(h)+h c(z),
    2c(h)=(1-h)c(z).

Writing a=c(z)/2 in the F5-vector space A gives c(h)=a-ha. Thus conjugation by a translation carries K to the standard G. Replace C by the corresponding translate, so G preserves C.

Let U be the vector span of C. It is a G-subrepresentation of V=T plus W. Complete reducibility and multiplicity-freeness show that U is T, W, or V. The case U=W is impossible: an integral projective curve contained in P(W)=P1 must be that line and has degree one. Hence C either spans the plane P(T) or all P(V).

## 3. Full-span quintics

If C spans P4, its smooth normalization X has genus at most

    pi(5,4)=1

by Castelnuovo's bound. The G-action on X is faithful because the embedded integral curve spans P4.

A faithful G-action is impossible in genus zero. The unique central involution z would be a nontrivial central involution in PGL2(C). Its centralizer is the solvable group G_m semidirect C2. The image of all G would lie in this centralizer. But G is nontrivial and perfect, and a solvable group has no nontrivial perfect subgroup.

A faithful G-action is also impossible in genus one. After choosing an origin on the elliptic curve X, Aut(X) is the semidirect product of its abelian translation group with the cyclic origin-preserving automorphism group (of order two, four, or six). The homomorphism from perfect G to the latter abelian quotient is trivial. Therefore the image of G consists of translations and is abelian, forcing the image itself to be trivial. This contradicts faithfulness.

Thus the full-span case cannot occur.

## 4. Plane quintics: direct character average

Suppose C spans P(T). Its homogeneous plane equation f has degree five and spans a G-invariant line in Sym^5(T*). Since G is perfect, every one-dimensional G-character is trivial. Thus f would be a nonzero invariant vector. Because T factors through G/{plus or minus I}=A5, it is enough to compute A5-invariants.

The conjugacy-class sizes of A5, ordered by element orders 1,2,3,5a,5b, are

    1,15,20,12,12.

We compute the corresponding characters of Sym^5(T*) directly.

- Identity: dim Sym^5(C^3)=binomial(7,2)=21.
- Order two: eigenvalues are 1,-1,-1, giving generating function 1/((1-t)(1+t)^2). Its coefficient of t^5 is sum from k=0 to 5 of (-1)^k(k+1)=-3.
- Order three: eigenvalues are 1,omega,omega^2, giving 1/(1-t^3). Its coefficient of t^5 is zero.
- Order five: eigenvalues are 1,zeta^a,zeta^(-a), with a=1 or 2 and zeta a primitive fifth root. Completing to all five roots rewrites the generating function as

      (1-zeta^(2a)t)(1-zeta^(-2a)t)/(1-t^5).

  The numerator has degree two and constant coefficient one, so the coefficient of t^5 is one. This works for both order-five classes; dualizing the representation does not alter these eigenvalue multisets.

The character list is therefore

    (21,-3,0,1,1).

Averaging gives

    dim (Sym^5(T*))^A5
      = (21 +15(-3) +20(0) +12(1) +12(1))/60
      = 0.

This contradicts the existence of f and excludes the plane case.

## 5. Conclusion and scope

Every degree-125 possibility is impossible. Combining with the previous independently audited alternatives proves

    Gamma_4 is empty, or deg Gamma_4=100.

This is a necessary condition on reduced one-dimensional support, not an existence assertion. It does not determine the component structure of a possible degree-100 curve, its scheme multiplicities, or isolated points. No actual source-instance evaluation is claimed. The only calculation is the elementary five-class character average above.
