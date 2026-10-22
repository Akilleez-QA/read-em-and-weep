# Independent mathematical review: PASS

Reviewed 2026-10-22. The proof establishes a>=-4 for every generic-rank-three original derivative and excludes the original twelve-defect branch in profile (1,2). The second-dual defect table, including its twenty-point possibility, is correct. No mathematical gap was found.

This is independent mathematical review supported by exact bounded arithmetic, not formal proof-assistant verification or a reproof of the complete HM foundation.

## Geometric inputs and exhaustive quotients

The pinned [actual-presentation source](https://github.com/Akilleez-QA/read-em-and-weep/blob/bcb820f06b0d3df35c96f928360f1e973e552c65/research/hm/order-four-quadratic-load/ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md) supplies all stated rank, degree, parity, splitting, and Euler-character inputs. Global generation of E(10) implies that every degree of its quotient A is at least -10. Perfectness and central parity make a even.

The [strict-top-slope lemma](https://github.com/Akilleez-QA/read-em-and-weep/blob/bcb820f06b0d3df35c96f928360f1e973e552c65/research/hm/order-four-quadratic-load/NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md) applies to successive saturated kernels without assuming their derivative ranks. Its highest-line argument correctly forces a killed top summand to be horizontal, contradicting negative degree. Thus H0(K(2))=H0(K^-(3))=0. The derivative of K lands in A(-2), with kernel K^-, giving the required section injection without extending the rank-three plateau to an endpoint.

The quotient sequence gives C2=H1(K(2)). If C denotes the representation cokernel of that section injection, C3=C+H1(K(3)). Both are genuine, and chi(K(3))=2-a. The [older a>=-8 proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/bcb820f06b0d3df35c96f928360f1e973e552c65/research/hm/order-four-quadratic-load/ONE-TWO-ASYMMETRIC-QUOTIENT-DEGREE-AND-DEFECT-BOUNDS.md) likewise uses only rank three of the original derivative.

The three splitting forms exhaust center-even rank-three equivariant bundles. The degree bounds and section inequality leave exactly six candidates at -8 and fifteen at -6. All displayed character decompositions and twelve exclusion certificates check. The three survivors at -6 each contain the asserted trivial-coefficient equivariant O(12) summand; realizability is not inferred.

## Invariant multiplication and transpose

Equivariant Serre duality identifies H0(Q(-2)) with H1(Q*) dual. Since M2 has no trivial constituent, H0(Q(-2))^G=0. The identity Sym^12 W=1+A_std+P+D supplies a nonzero invariant f12. Alternatively, the twelve-point orbit supplies a stable line of defining sections, and perfectness makes its character trivial.

Multiplication by f12 is injective on the locally free sheaf Q(-14), despite its zeros, because the base is integral. It induces an injection on invariant sections, proving Hom_G(Q*,O(-14))=0. This proof requires no splitting of Q*.

The optional seven-block check is independently correct: negativity, central parity, and genuine H1 contributions give (j-1)dim R<=41 and coefficientwise containment in M2. Exhausting all nine irreducibles for 14<=j<=42 gives precisely the seven listed blocks and zero equivariant Hom for each. This conservative envelope asserts no actual occurrence.

The actual transpose and dual quotient give the sheaf injection A -> B*(-2) -> Q(-2), without assuming saturation. At a=-6 its O(12) summand would give a nonzero map Q* -> O(-14), with exactly the stated twist. This contradiction, the -8 exclusion, and parity prove a>=-4.

## The two different defects

In profile (1,2), the established dual-interior bound b>=-12 gives 0<=t=-6-a-b<=10. Its invariant effective divisor is empty because the smallest projective icosahedral orbit has twelve points. Thus A=B*(-2), -4<=a<=6, and b=-6-a.

The second dual injection is different. Substitution gives s<=14-2a and deg M=-48-2b+s=-36+2a+s. Invariant effective divisors of degree at most 22 have degrees 0,12,20; a doubled smallest orbit already has degree 24. Every row of Section 7 follows, including s=20 at a=-4. No realization or full (1,2) exclusion follows.

## Reproduction and novelty scope

The final python3 verify.py run passes all five PASS checks, including the invariant multiplier and complete ten-row second-dual table. It uses exact Q(sqrt(5)) arithmetic and bounded universal character tests, with no selected actual HM/source coefficients, points, matrices, rank evaluations, or large scan.

The inspected [PR543 asymmetric source](https://github.com/Akilleez-QA/read-em-and-weep/blob/b2c4239ab1f72b94c2630fb16dcb3665d7d47fdb/research/hm/order-four-quadratic-load/ONE-TWO-ASYMMETRIC-QUOTIENT-DEGREE-AND-DEFECT-BOUNDS.md) leaves both original twelve-defect pairs open. The subsequent [c8975a4 theorem](https://github.com/Akilleez-QA/read-em-and-weep/blob/c8975a41912b28938bc5b912e6637698a9652195/research/hm/order-four-quadratic-load/TWO-TWO-ENDPOINT-RANK-DROP-EXCLUDES-LAST-THREE-PAIRS.md) already excludes the complete (2,2) profile and is credited separately. Neither that profile-specific result nor the inspected [PR1 coordination](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6336509239) supplies this profile-independent primal bound or asymmetric twelve-defect exclusion. Novelty is relative to that public frontier, not a historical claim about the techniques.
