# Finite arithmetic specialization: Čech residue versus Laurent divergence

## Scope and result

This is a universal qualification of the [reduced residue certificate](https://github.com/Akilleez-QA/read-em-and-weep/blob/521135d1d786123e68f4cafd4e3a526c8750138b/research/hm/reduced-massey/reduced-serre-residue-certificates/PROOF.md), not a modular computation, a nonvanishing result, or a positive-characteristic TW comparison theorem. It distinguishes base-variable divergence, signed scalar Čech contraction and simplex integration. The prior public divergence results are credited in [Public sources](PUBLIC-SOURCES.md).

## 1. Integral Čech residue lemma

Let R be any commutative ring and use the ordered standard cover of P^4_R. The homogeneous Laurent degree-minus-five top Čech quotient is canonically R, by the coefficient of x_0^(-1)...x_4^(-1).

Proof. Every term in a top boundary is restricted from an intersection missing an index j, and consequently has nonnegative x_j exponent. It cannot contribute the all-minus-one monomial. Conversely, if an exponent vector a has sum -5 and is not all minus one, then at least one a_j is nonnegative. The monomial belongs to the intersection missing j and is the boundary of its signed degree-three cochain supported on that intersection. All coefficients of this construction are 0, 1, or -1. Therefore the quotient assertion holds over R without inverting any integer. The same signed insertion construction for the scalar contraction at weights 0,-1,-2 is also integral, with the surviving degree-zero constants retained at weight zero as in the scalar contraction identity. This does not assert integrality of an arbitrary homotopy.

In characteristic p a nonordinary exponent vector may have a_i congruent to -1 modulo p for every i. This creates a base-variable divergence obstruction but does not create a new top Čech class: the preceding nonnegative-exponent argument still applies. These two differentials must not be identified.

## 2. Bounded finite TW specialization lemma

Fix a finite supplied collection of regular characteristic-zero TW expressions and a finite collection of identities used to construct and compare their scalar residue certificates. Choose an arithmetic coefficient ring A embedded in C that contains all scalar coefficients of those expressions and the inverses of the finitely many scalar denominators appearing in their construction and in the selected identities. Nonconstant localization denominators remain formal localized functions; a specialization must preserve every localization needed for the chosen expressions. The final scalar coefficients and those in the recorded scalar Cech identities must be homogeneous coordinate-Laurent sections of the standard cover, with its stated regularity on each intersection. This lemma does not extend that Cech argument to arbitrary rational functions with additional poles. Such an A can be taken finitely generated over Z with finitely many elements inverted. If all coefficients are rational, it can instead be taken Z[1/N] for some nonzero integer N. An arbitrary complex coefficient collection must not silently be treated as rational.

For a final scalar top component

    alpha = sum_gamma f_gamma(x) t^gamma dt_1 wedge ... wedge dt_4,
    |gamma| <= D,

where the barycentric exponents gamma_i are nonnegative integers and each f_gamma is homogeneous coordinate-Laurent of weight -5, its final integration and residue formula is defined after additionally inverting (D+4)!:

    Res I(alpha) = sum_gamma gamma_0!...gamma_4!/(|gamma|+4)!
                             [x_0^(-1)...x_4^(-1)] f_gamma.

This is a sufficient denominator bound for this final integration only. The entire reduced construction also requires the denominators of its intermediate I and K operations and the rank-two factors 1/2. Those must be included separately; no bound based solely on D is asserted for the whole construction. These sufficient denominator sets may be reduced only after re-expressing all selected operations and identities over the smaller ring. Cancellation in the final residue expression alone does not permit dropping an intermediate I/K denominator.

Use differentials relative to this arithmetic ring. For any actual ring homomorphism from it to a field k, respecting all coefficient relations and required localizations, the displayed coefficient formula specializes to the same finite formula over k. Every recorded polynomial identity over the arithmetic ring specializes as well. For boundary invariance, the relevant finite Stokes identities and their expressions must be included in that ring; the integral Čech residue lemma then kills the resulting Čech boundaries. A nonzero specialized residue certifies that the original residue in C is nonzero. A zero specialized residue does not certify zero in C.

No primes dividing gcd(a_0+1,...,a_4+1) need to be inverted merely to extract the Čech residue. Such primes arise only if one replaces coefficient extraction with a search for base-variable divergence primitives. Likewise, coefficient arithmetic and geometric good reduction are distinct obligations: this lemma does not establish that the original bundle, dual bases, pair vanishings, or cohomology dimensions retain their properties after specialization.

## 3. Why this is only a finite-expression statement

No fixed localization makes the full polynomial TW contraction work in every surviving positive characteristic. On the affine simplex interval in characteristic p, the nonconstant polynomial t^p is closed. Thus polynomial de Rham forms on the interval are not contracted to constants by the characteristic-zero I,W,K identities on all polynomial degrees. Only the specified finite expressions and identities with invertible denominators are transported by the lemma.

The scalar Čech contraction does not have this problem: its differential uses restriction and alternating signs, and its primitive uses signed insertion, rather than division by Laurent exponents or integration in simplex variables.

## 4. Relation to Laurent divergence and logarithmic tangency

For a complete finite Laurent polynomial H=sum c_a x^a in characteristic p, the coefficient of x^a in partial_i G_i is (a_i+1) times the coefficient of x^(a+e_i) in G_i. The same identity holds after embedding rational functions in a fixed iterated Laurent field. Consequently every simultaneously resonant coefficient vanishes for a divergence, even allowing arbitrary rational poles. Conversely any nonresonant monomial has a Laurent primitive by division in one nonresonant coordinate. This proves the stated necessity and sufficiency criterion for divergence.

For a not all minus one, define g(a)=gcd(|a_0+1|,...,|a_4+1|), omitting zero entries. The coefficient ideal generated by the integers a_i+1 is (g(a)). This proves the Bezout denominator choice. Over the mixed-characteristic DVR Z_(p), a coefficient c_a in Z_(p) has an integral Laurent primitive exactly when v_p(c_a)>=v_p(g(a)), where v_p is the p-adic valuation and v_p(0)=+infinity. For the all-minus-one monomial the coefficient must instead be zero. Factorwise logarithmic tangency requires distinct reduced factors and only those multiplicities nonzero in the residue characteristic; collisions and disappearing factors require rechecking the reduced factorization. These qualifications leave the characteristic-zero Laurent divergence criterion intact.

