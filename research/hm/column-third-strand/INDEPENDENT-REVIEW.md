# Independent mathematical review

Verdict: PASS, conditional on the pinned PR511 and PR513 inputs. This is an independent mathematical review, not a proof-assistant or formal machine check.

Reviewed artifact: `PROOF.md`.

SHA-256: `d519873b34285f437bb06a968078d8791a32f468ec95fac7c38fcd52c95037f5`.

## Checks

1. The comparison ideal has the exact full Hilbert function, not merely the same quadratic component. Its ten quadratic generators are the first ten lexicographically largest degree-two monomials in five variables. Adding all cubics gives Hilbert function (1,5,5,0,...). Concretely, the additional minimal cubic generators are x3*x4^2, x3*x4*x5, x3*x5^2, x4^3, x4^2*x5, x4*x5^2 and x5^3. Thus the comparison ideal need not, and does not, satisfy the quadratic-generation property of the actual column ideal. This is harmless: the Betti comparison requires only the full Hilbert function.

2. The precise external graded statements were checked in the publisher's full text of Martina Juhnke-Kubitzke and Lorenzo Venturello, *Graded Betti Numbers of Balanced Simplicial Complexes*, Acta Mathematica Vietnamica 46 (2021), 839–871, Section 2.2, Lemmas 2 and 3: https://link.springer.com/article/10.1007/s40306-021-00449-8 . Lemma 2 states the graded Bigatti–Hulett–Pardue inequality for every homogeneous ideal. Lemma 3 gives the graded Eliahou–Kervaire formula for the quotient by a lex ideal. Neither statement imposes a genericity condition. The characteristic-zero assumption in the proof is sufficient. The use here does not rely on reading a total-Betti-number statement as a graded one.

3. Substituting i=3 and j=1 in Lemma 3 restricts the sum to quadratic minimal generators. Their maximal-variable-index multiplicities are (1,2,3,2,2). Consequently the sum is 3+6+12=21. Cubic generators cannot contribute to this bidegree. Lemma 2 then yields beta_(3,4)(A_lambda)<=21.

4. The reviewed PR513 input supplies the nontrivial internal-degree-four central character and five-dimensional irreducible constituents. It applies to every nonzero lambda, not only a generic column. Thus u is a nonnegative multiple of five, giving precisely the asserted necessary list 0,5,10,15,20.

5. The consequences use the PR513 template correctly. In internal degree four the source has dimension 50 and incoming boundaries have dimension 5, so u=45-rank(d). Hence rank(d)>=25. This is a structural lower bound, not a computed rank of any selected tensor. The PR516 identity a=5+u-rho-sigma, with a>=0, gives rho+sigma<=25. No positive existence assertion is extracted from the formerly allowed, now impossible u=40 case.

## Scope

The exclusion of u=25,30,35,40 is new relative to the pinned u<=40 result. The remaining values are not asserted to occur. This argument neither proves u=0 nor resolves the Gorenstein cubic-generation or middle-Tor-rank questions. No selected actual HM/source-instance evaluation, multiplication-matrix computation, coefficient search or large computation was performed for this review. No first-order, higher-order or algebraicity conclusion is certified here.
