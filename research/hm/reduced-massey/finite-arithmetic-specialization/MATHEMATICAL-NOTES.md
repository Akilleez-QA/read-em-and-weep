# Verification details and exact mathematical limits

These arguments supplement [the proof](PROOF.md). They retain the signed, domain and effectivity qualifications of the statements, without adding a selected-instance conclusion.

## 1. Integral standard-cover Cech quotient

The argument is valid over every commutative base ring. In homogeneous Laurent weight -5 on the top intersection of the ordered standard cover of P^4, a monomial having all exponents negative must have all five exponents equal to -1. Every other monomial has a nonnegative exponent in some coordinate and is the signed boundary of a cochain on the intersection omitting that coordinate. Conversely such a boundary cannot contain the all-minus-one monomial. Thus extraction of that coefficient identifies the top quotient with the base ring without division.

The integral signed scalar contraction at weights 0, -1, and -2 is consistent with this monomial argument. The proof retains the degree-zero constants at weight 0 and does not claim that every possible homotopy is integral. Simultaneous congruences a_i = -1 modulo p can obstruct Laurent divergence without creating new Cech classes.

The theorem requires homogeneous coordinate-Laurent sections with the regularity required on each standard-cover intersection. Its Cech argument is not extended to arbitrary additional rational poles. 

## 2. Finite TW specialization and boundary invariance

The result transports only a specified finite collection of expressions and identities. The relevant finite Stokes identities, their expressions, and their denominators must be included. The integral Cech argument then annihilates the resulting Cech boundaries. This is not an assertion that every boundary in an unrestricted characteristic-p polynomial TW complex is annihilated by a globally defined integration operator.

The stated obstruction to a global contraction is sound: on the characteristic-p interval, the nonconstant polynomial t^p is closed. Equivalently, its two endpoint values differ although its differential vanishes, so unrestricted characteristic-zero Stokes and contraction identities cannot survive. The finite-expression statement does not assert a positive-characteristic TW comparison theorem or preservation of geometric cohomology dimensions.

## 3. Denominator ledger

The statement distinguishes the necessary categories:

- Scalar coefficient and formula denominators, with all needed coefficient relations and localizations preserved.
- The rank-two factors 1/2 used by the selected construction.
- Denominators of every selected intermediate I and K operation and of the identities, including Stokes identities, used in the certificate.
- The sufficient final-integration denominator (D+4)! for polynomial barycentric exponents of total degree at most D.

The final simplex integral of a barycentric monomial has coefficient gamma_0! ... gamma_4! / (|gamma|+4)!. Its denominator divides (D+4)!, independently of the Laurent x-exponents. The theorem states that the barycentric exponents are nonnegative integers and the x-coefficients are homogeneous coordinate-Laurent of weight -5.

In particular, reducing the sufficient denominator set requires re-expression of all selected operations and identities over the smaller ring. Cancellation only in the final residue does not license discarding an intermediate I/K denominator. The document makes no unsupported claim that the final degree D bounds all intermediate denominators.

## 4. Embedded arithmetic coefficient ring and nonvanishing

For a finite collection of arbitrary complex coefficients, the appropriate ring is a finitely generated arithmetic subring A embedded in C, with the necessary elements inverted. Z[1/N] is asserted only in the rational-coefficient case. The document requires relative differentials and an actual specialization homomorphism respecting the coefficient relations and localizations.

Consequently, if a residue c in A has nonzero image under A -> k, then c is nonzero in A and hence in C. This implication needs no cohomological base-change theorem. A zero image supplies no converse. The target field need not be F_p itself. An abstract presentation mapping noninjectively to C, together with a specialization that ignores its actual coefficient relations, would not justify this implication; the embedded-ring requirement excludes that error.

No extra exclusion of primes dividing the Laurent divergence gcd is needed merely for integral Cech coefficient extraction. A concrete modular certificate would still have to exhibit a valid specialization and check every denominator and selected identity in its own finite ledger.
