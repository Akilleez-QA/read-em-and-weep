# Degree-100 rank-four curves: integral or five degree-20 components

## Result

Under the established Schrödinger-normalizer rank-four hypotheses, if the reduced curve Gamma_4 is nonempty, exactly one of the following configurations remains:

1. Gamma_4 is integral of degree 100.
2. Gamma_4 consists of five distinct integral degree-20 components, permuted transitively by N. Every component is A-stable, spans P4, and has stabilizer A semidirect H, where H is the order-24 inverse image of an A4 point stabilizer in G/{+/-I}=A5.

In particular, the previously live configuration of twenty degree-five components is impossible. Its exclusion uses disjointness from the canonical odd reflection lines, rather than merely the absence of line components. This is a new necessary-condition theorem, not a claim that either remaining configuration exists.

## 1. Dependencies

Write N=A semidirect G, A=F5^2, G=SL2(F5). Import:

- ../rank-four-degree-hundred-lower-bound/PROOF.md, with ../rank-four-degree-hundred-audit/AUDIT.md and ENDPOINT_125_INDEPENDENT_AUDIT.md: a nonempty Gamma_4 has reduced total degree 100; every component is A-stable, spans P4, and has degree divisible by five.
- The same lower-bound proof, Section 3: an orbit of five components has individual degree divisible by ten, and an orbit of six components has individual degree divisible by twenty-five.
- ../rank-four-degree-fifty-equality/PROOF.md, Section 2: an A-stable integral degree-five or degree-ten curve has N-orbit size at least twenty.
- ../smooth-normalizer-polarization-divisibility/PROOF.md: an N-stable integral curve has degree divisible by fifty; ../rank-four-degree-sixty-lower-bound/PROOF.md excludes integral degree fifty.
- ../rank-four-line-component-exclusion/PROOF.md and its cited ../canonical-line-rank-five-strengthening/PROOF.md: Z4 is disjoint from every canonical odd reflection line. In the standard splitting the central reflection has the honest lift R on V with eigenspace dimensions 3 and 2, hence trace 1, and its odd line is P(W).

The group G is perfect. The quintic argument below also uses Riemann–Roch on an elliptic curve, the very ampleness of degree-five line bundles there, and the holomorphic Lefschetz fixed-point formula for a finite-order automorphism of a smooth curve. No rank-instance calculation is made.

## 2. Complete component-orbit exhaustion

Let D be a component, e its degree, m its N-orbit size, K=N_D, and H=K/A. Since A fixes D, K is the full inverse image of H in G, so K=A semidirect H and m=[G:H]. Every orbit satisfies me<=100.

If m=1, then 50 divides e. Degree fifty is excluded, so e=100 and this is the entire curve.

If m>1, then m>=5: the perfect image of G in S_m is trivial for m<=4 because S_m is solvable. Also 5 divides e.

- If e=5, the imported small-degree bound forces m>=20, while me<=100 forces m<=20. Thus m=20 and this orbit exhausts the degree budget.
- If e=10, the bound m>=20 is incompatible with me<=100.
- If e=15, then m<=6, so m is 5 or 6. The respective divisibilities 10|e and 25|e both fail.
- If e=20, then m<=5, hence m=5 and this orbit exhausts the degree budget.
- If e>=25, then m<=4, contradicting m>=5.

Thus before the new exclusion the only configurations are an integral degree-100 curve, five degree-20 curves, or twenty quintics. This exhausts every possible orbit index without needing a classification of all subgroups of G; in particular mixed component orbits cannot occur.

In the index-five case, the coset image of perfect G is a nontrivial perfect subgroup of A5, hence all of A5 (all proper subgroups of A5 are solvable). Its kernel has order two and is the unique central involution subgroup. Thus H is the inverse image of a point stabilizer A4 and has order 24.

## 3. The quintic component is a smooth elliptic normal quintic

Suppose the twenty-quintic configuration occurs. Take one component D and its normalization nu:E->D. It is nondegenerate in P4, so Castelnuovo gives g(E)<=pi(5,4)=1. The A-action on E is faithful because D spans P4. Genus zero is impossible: a faithful C5^2 subgroup of PGL2(C) cannot exist, since the centralizer of an order-five element is a torus and every finite subgroup of a torus is cyclic. Therefore g(E)=1.

Put L=nu^*O_D(1), of degree five. Riemann–Roch gives h0(E,L)=5 and h1(E,L)=0. Nondegeneracy makes the restriction map V*->H0(E,L) injective; it is therefore an isomorphism. The original morphism E->P(V) is the complete degree-five linear-series morphism. Such a line bundle is very ample, so this morphism is an embedding. Thus D itself is smooth, E=D, and D is an elliptic normal quintic.

For completeness, its component stabilizer quotient H has order six and is cyclic. Every element of A acts by translation on E, since the origin-preserving elliptic automorphism group has order 2, 4, or 6. Conjugation on A by K factors through that cyclic group. Its prescribed quotient action H->Aut(A) is faithful, so H embeds in the cyclic origin-preserving group. Hence H=C6 (and the elliptic curve has j=0). Only the presence of its involution is needed next.

## 4. An invariant elliptic normal quintic meets the odd reflection line

Since |H|=6, Cauchy's theorem and uniqueness of the involution in G imply z=-I belongs to H. Since K is the full inverse image of H, the standard element (0,z) belongs to K. Its normalized lift R on V has three positive eigenvalues and two negative eigenvalues.

The action of z on E is an involution whose conjugation action on A=E[5] is inversion. It cannot be a translation, since translations centralize A. An elliptic involution which is not a translation has the form x->a-x and has exactly four fixed points. At all four its derivative is -1.

Use the R-induced linearization on L=O_E(1). On H0(E,L)=V*, the trace is 3-2=1. Since H1(E,L)=0, the holomorphic Lefschetz formula gives

    1 = sum over p fixed by z of (epsilon_p / (1-(-1)))
      = (epsilon_1+epsilon_2+epsilon_3+epsilon_4)/2,

where epsilon_p in {+1,-1} is the action on the fibre L_p. Thus the sum of these four signs is two: three signs are positive and exactly one is negative.

At an R-fixed projective point [v], the action on O(1) is the inverse of the eigenvalue of R on Cv. For eigenvalues +/-1 this is the same sign. Therefore the unique fixed point with negative fibre action lies in P(W), the canonical odd reflection line. In particular

    E intersects P(W).

But E is a component of Gamma_4 and hence is contained in Z4, whereas Z4 is disjoint from P(W). This contradiction eliminates the twenty-quintic configuration.

The same argument proves the useful stand-alone statement: any smooth elliptic normal quintic preserved by this trace-one projective reflection meets its odd fixed line in a fixed point. No assertion about transverse intersection is required.

## 5. Boundaries and scope

The surviving five-component case has individual degree twenty and order-600 stabilizer A semidirect H with H the binary tetrahedral order-24 subgroup. This proof does not exclude that case or the integral degree-100 case. It also does not determine scheme multiplicities, isolated rank-four points, or nonemptiness.

No actual source tensor, coefficient, selected input, operation matrix/value, rank instance, jet, or residue was evaluated. Only local proof files and abstract finite-group/curve arguments were used.
