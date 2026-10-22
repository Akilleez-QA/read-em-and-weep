# Low-corank rigidity of the auxiliary second-jet kernel

This is conditional linear algebra for the actual multiplication subspace W, not a bound on the actual adjoint corank and not a vanishing theorem.

Let V have dimension four, P have dimension five, and W be the actual r-dimensional subspace of V* tensor P from the dual adjoint multiplication. Define P0={p: V* tensor p is contained in W}, j=dim P0. The preceding Schur-resolution identification gives J5=P0 and
J6={a in P tensor V: the coefficients of the symmetric insertion of a all lie in W}.
The common constant determinant factor is suppressed throughout.

New deduction: if r-4j <= 6, then J6=P0 tensor V. Thus dim J6=4j, with no additional second-jet directions. In particular, if r<=6, (dim J5,dim J6) is either (0,0) or (1,4); the latter is possible only when r>=4.

Proof. Since V* tensor P0 is contained in W, form P'=P/P0 and W'=W/(V* tensor P0), a subspace of V* tensor P' of dimension r-4j. Its maximal full V*-block is zero: if V* tensor p' lies in W', every lift p of p' satisfies V* tensor p contained in W, because the entire kernel V* tensor P0 is already contained in W. Hence p belongs to P0 and p'=0.

The image of any a in J6 in P' tensor V lies in the same symmetric prolongation of W'. The kernel of this projection on P tensor V is exactly P0 tensor V. If that image has tensor rank s, its quadratic coefficient span has dimension s(9-s)/2, namely 4,7,9,10 for s=1,2,3,4. The formula follows by choosing bases in which the first s coefficient vectors are independent: the coefficients within the first s indices span Sym^2(C^s), and those with one of the other 4-s indices contribute s(4-s) additional independent vectors.

For dim W'<=6, a nonzero image can therefore only have rank one. A rank-one prolongation tensor p' tensor v, v nonzero, has coefficient span exactly V* tensor p'. This contradicts the absence of a full block in W'. Thus the image is zero. Conversely P0 tensor V always lies in J6 by definition. This proves the assertion.

Consequences for the original jet cokernels, under the same condition: dim C5=75+j and dim C6=180+4j. These follow from the already proved universal Euler counts, not from any selected coefficient evaluation. No claim that r-4j<=6 holds for HM is made.
