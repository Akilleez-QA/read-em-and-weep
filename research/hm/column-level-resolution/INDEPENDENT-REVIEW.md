# Independent mathematical review

## Reviewed artifact and verdict

Reviewed `PROOF.md`, SHA256 `731bb90ceedd66d388b5a217eeab52e6d7f2ba7153c27abd6a80b22066f68fc9`.

**PASS, conditional on the explicitly pinned presentation and Hilbert-function inputs.** The uniform levelness, vanishing of beta_(4,5), exact one-parameter numerical resolution template, and restriction u in {0,5,...,40} follow. This is independent mathematical review, not formal proof-assistant verification. No selected HM/source-instance evaluation was performed.

## Checks

1. **Field and equivariance.** Work after algebraic closure in characteristic zero. The level-five Heisenberg representation remains irreducible; the center acts faithfully. The binary generator space is Gamma-trivial, so contraction by every nonzero binary covector preserves Gamma-equivariance. Socle dimensions and graded Tor dimensions commute with field extension. Thus passage to a splitting field does not weaken the uniform conclusions.

2. **Levelness and last Betti term.** The degree-one socle is a subrepresentation of the irreducible five-dimensional T. If it were all T, every quadratic product would vanish, contrary to dim A_2=5. There is no degree-zero socle, and A_3=0 makes all of A_2 the socle. Top Koszul homology therefore has dimension five solely in internal degree 7: F_5=5S(-7).

3. **Koszul signs and boundary.** Fix a volume omega=x_1 wedge ... wedge x_5 and write omega_i=(-1)^(i-1) x_1 wedge ... omit x_i ... wedge x_5. Associate f to the tensor sum_i f(x_i) tensor omega_i. The incoming differential of omega is sum_i x_i tensor omega_i, hence corresponds exactly to the identity. For i<j, the coefficient of the wedge omitting i and j in the outgoing differential is, up to a nonzero common sign, x_i f(x_j)-x_j f(x_i). Consequently the displayed cycle equations are necessary and sufficient, and the scalar line is precisely the incoming boundary. The determinant line is trivial for the given subgroup of SL(5).

4. **Conjugation-character decomposition.** For each element g of Gamma modulo its center, the nonzero operator rho(g) spans a conjugation-character line. Nondegeneracy of the commutator pairing and faithfulness of the central character make all 25 characters distinct. Distinct character eigenvectors are independent; dimension End(T)=25 proves exhaustion and multiplicity one. The trivial line is the identity. Maschke semisimplicity ensures that a Gamma-stable cycle space larger than this line contains a nontrivial character line.

5. **Simple spectrum and structural contradiction.** For such a nontrivial character operator f, nondegeneracy provides h with h f h^(-1)=zeta f, for a primitive fifth root zeta. The operator f is invertible and finite order up to scalar, hence diagonalizable in characteristic zero. Its nonzero spectrum is stable under multiplication by zeta; dimension five forces one orbit with five distinct eigenvalues. In an eigenbasis, the Koszul equations kill every mixed product. The ten mixed monomials are linearly independent, so the dimension-ten quadratic space J_2 is exactly their span. Quadratic generation then identifies J with the mixed-product ideal. Its quotient maps onto k[x_1] by setting the other variables to zero, which proves x_1^3 survives. This contradicts A_3=0 and excludes all nontrivial cycle characters. Thus beta_(4,5)=0.

6. **Resolution and parameter bound.** Finite length and the stated Hilbert function give regularity 2. Absence of linear generators and minimality give internal shifts at least i+1 in positive homological degree i; regularity bounds them above by i+2. The stated Hilbert numerator is correct. Combining it with F_1=10S(-2), the top term, and beta_(4,5)=0 gives exactly the displayed template with u=beta_(3,4). In internal degree four all Koszul terms have the same nontrivial central character, so every kernel, image, and homology dimension is divisible by five. The incoming exterior coproduct from Lambda^4 T is injective: wedge multiplication composed with it is multiplication by 4. Its image has dimension five. The outgoing differential from T tensor Lambda^3 T is nonzero: choose a nonzero product x_i x_j in A_2 and a three-fold basis wedge containing x_i; the coefficient of the wedge of its other two factors in d(x_j tensor that wedge) is exactly x_i x_j, up to sign. Its image thus has dimension at least five. Therefore u=50-5-rank(d) lies between 0 and 40 and is divisible by five.

## Dependencies and limitations

The review treats the PR511 Hilbert-function result and ten-quadratic presentation at commit `55bc80b2cb660edd741c93747df7304ee51a061e` as pinned inputs, rather than claiming a new independent verification of that entire dependency chain. The representation assertions agree with Horrocks–Mumford (1973), section 1 and the multiplicity-space statement in section 2.2, cited in the proof. Choosing an eigenbasis here is a universal representation-theoretic argument, not evaluation of a selected source instance.

No assertion that every allowed u occurs is established, and no value of u is determined. No first-order source-lifting, higher-order lifting, or algebraicity conclusion is supplied. There is no mathematical blocker to publication of this conditional result.
