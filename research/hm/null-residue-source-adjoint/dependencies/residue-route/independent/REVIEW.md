# Independent residue certificate audit

## Verdict

Accept the theorem and both polynomial certificate identities in the inspected residue-divergence-reduction-public/PROOF.md. The derivatives are ordinary coordinate partial derivatives on the complete extracted scalar, not physical curve derivations. Characteristic zero, finite Laurentness, the same-source geometric identification, and the designated trace orientation are essential hypotheses. This audit does not establish any production vanishing result or authorize execution.

The rational-to-Laurent implication is sound: embed the rational function field into k((x1))((x2))((x3))((x4)); the iterated all-minus-one coefficient kills every coordinate derivative. Rational primitives may introduce poles, because this is a formal field argument. Expansion order independence is needed only for the Laurent left-hand side.

The ID0 correctness-boundary proof fixes exactly p=(x1*x2+x3*x4)^2 and the three exponents (-3,-3,-1,-1), (-2,-2,-2,-2), (-1,-1,-3,-3), weighted 1,2,1. There is no extra deck division, frame factor, or sign. The retained whole-Laurent certificate is a separate sufficient way to authenticate the domain; a rational divergence witness does not independently authenticate the intended geometric pairing or alter an inert implementation.

## Additional theorem: denominator exponent one is complete

Let F=N/D be a finite Laurent polynomial over a characteristic-zero field, with polynomial N,D,p and D nonzero. If pN=0, choose all A_i=0. Otherwise the following are equivalent:

1. The all-minus-one coefficient of pF is zero.
2. There exist polynomial A_i, each of total degree at most deg(pN)+1, such that

   p*N*D = sum_i (D*partial_i A_i - A_i*partial_i D).

Proof. Write D=x^d C with no coordinate variable dividing C. Laurentness implies N=CQ for polynomial Q: C is relatively prime to every coordinate monomial, so divisibility after coordinate localization descends to the polynomial ring. Hence pF=x^-d pQ.

For every nonzero monomial c*x^b of pQ, its corresponding exponent in pF is a=b-d. The resonant monomial a=(-1,-1,-1,-1) is absent by hypothesis. Choose an index i with a_i != -1 and assign c*x^(a+e_i)/(a_i+1) to G_i. Then pF=sum partial_i G_i.

Every x^d G_i is a polynomial: its exponents are b+e_i, which are nonnegative. Let A_i=D G_i=C*(x^d G_i). These are polynomials of degree at most deg C + deg(pQ)+1 = deg(pN)+1. More precisely, for each numerator A_i and each variable x_j, deg_(x_j)(A_i) <= deg_(x_j)(pN) + delta_(ij), since the assigned primitive monomials have exponents b+e_i and degrees add under multiplication by C. Zero numerators satisfy these bounds trivially. The quotient rule gives the displayed identity. Conversely, the identity gives a rational divergence, which the audited theorem shows has zero Laurent residue.

Thus, conditional on Laurentness, no denominator exponent search is necessary: m=1 suffices, and a known finite-degree linear system is complete. This is a mathematical existence/decision boundary, not a promise that dense linear algebra or identity construction fits any operational cap. The proof uses C,Q only existentially; certificate verification need not construct the whole Laurent quotient.

A smaller chosen degree/support cutoff is merely a heuristic. Failure below the displayed complete bound does not prove nonvanishing. Outside the Laurent premise, this completeness statement does not apply.

## Independent invented control

Write u=x1*x2 and v=x3*x4. Choose

   F=2*u^-3*v^-1-u^-2*v^-2,
   G1=-3/(x1*x2^2)-x3*x4/(x1^2*x2^3)-x1/(x3^2*x4^2),
   G2=G3=G4=0.

The weighted coefficients are (2,-1,0), so their 1:2:1 sum is zero. Direct expansion gives pF=3*u^-2+2*u^-3*v-v^-2=partial_1 G1.

Take D=x1^3*x2^3*x3^2*x4^2*(1+x1+x2*x3). The polynomial N=DF and A1=DG1 verify the m=1 identity. Here deg A1=9=deg(pN)+1, so the proposed total-degree bound is attained by this explicit construction. Adding u^-2*v^-2 to F changes its weighted residue to 2 and breaks the same certificate identity. The independent checker passes under ordinary Python and Python -O. It imports no production source and evaluates only invented expressions.

## Essential negative boundary

For an arbitrary rational function, vanishing of one iterated residue is not equivalent to rational exactness. For example

   H=1/((x1-1)*x2*x3*x4)

has zero chosen all-minus-one coefficient when expanded at x1=0. Yet after t1=x1-1 its all-minus-one coefficient at (t1,x2,x3,x4)=0 is 1. A rational divergence would have zero residue in this translated iterated field too, so H has no rational divergence representation. This counterexample explains why the Laurent hypothesis cannot be discarded.

## Next symbolic step

Define the denominator-one linear operator T_D(A)=sum(D partial_i A_i-A_i partial_i D), together with the explicit total-degree domain above, and prove its kernel/image interface once over a symbolic coefficient field. For each authenticated test section, the certificate target is pND. This is independent of the earlier adjoint/source reduction, requires no production evaluation to state or prove, and gives a precise complete search boundary if Laurentness is supplied. It does not imply that the 30 target pairings are known, share one scalar, or are all zero.
