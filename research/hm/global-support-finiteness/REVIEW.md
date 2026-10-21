# Independent mathematical review

## Reviewed artifact

The reviewer read PROOF.md in full and independently derived its classification before reading the completed artifact. Its reviewed SHA256 is f27a7faec3fe4ea0e10d80b4f480554926882d791c050c11afc09bb17ee41b96. The proof itself establishes a codimension lower bound; the exact codimension named in its Section 5 heading is established by the separately reviewed EXPECTED-CODIMENSION.md below.

## Checks and verdict

The proof is mathematically sound under its pinned representation and exterior-model dependencies.

1. The annihilator equations have the correct signs and indices. In the coefficient of w_d, the two summands arise from i=b-d and i=b+d, and alternation gives their difference. With (i,k)=(b-d,2b-d), the opposite cell is (2i+2k,i+3k). This transformation is an involution over F5, with fixed cells k=2i. All nonfixed cells are covered by the ten equations.

2. The support argument covers every possible zero pattern. Invariance of the rectangular nonzero support gives 2S+2t=S for each t in T. Two distinct t force invariance of S under a nonzero translation, hence S=F5. The other projected inclusion then forces T=F5. If T is a singleton, S must be a singleton, and invariance gives T=2S. No additive-combinatorics theorem or computation is needed.

3. On the full torus, the four-step cyclic products in E2 omit exactly r_(b+2) and s_(2b+2). Thus s_(2i+3)=r_i^(-1). Substituting into E1 yields r_(b-1)r_b=r_(b-2)r_(b+1). For t_i=r_i/r_(i-1), this is t_(b+1)=t_(b-1). Step two generates F5, so the t_i are constant. Periodicity and the product-one relation give q^5=r_0^5=1.

4. The converse is valid, including cyclic consistency at the last coordinate. The formula for x has exactly the prescribed ratios, and the prescribed s have product one. They therefore integrate to a unique projective y. The two original equation families follow. Different ratio pairs yield different projective x, and the five singleton pairs are disjoint from the twenty-five torus pairs.

5. Finiteness follows from the complete incidence classification, not from a Chern-class count or from the existence of isolated eigenlines. The thirty distinct eigenlines supplied by PR553 exhaust the support. Its local normal-derivative theorem then proves the entire support determinantal scheme reduced. The proof does not identify the primary evaluation determinantal scheme with this support scheme. Uniqueness of the projective annihilator implies support rank exactly four.

6. The primary-bad incidence estimates are correct: the rank-eight, rank-nine and rank-ten strata contribute dimensions at most 6, 8 and 8. Generic rank ten bounds the rank-nine stratum by dimension three. Proper projection of the projective incidence gives a closed bad locus of dimension at most eight in P14. A general P5 therefore avoids it. Projection away from any prescribed point gives an image closure of dimension at most eight in P13; a general P4 avoids this closure, proving the punctured-P5 statement whether or not the prescribed point is bad.

## Scope of verification

This is independent mathematical review, not proof-assistant verification. No selected actual HM/source matrix, coefficient evaluation, numerical rank, or numerical experiment was used. The conclusions remain primary-only and do not establish full-adjoint rank, a selected source instance, higher-order lifting, or algebraicity.

## Exact-codimension supplement

EXPECTED-CODIMENSION.md was read in full at SHA256 c69b5bfa3b50d9bc664ab8303d8c3cc7817d5f90e45351c0cb85b6b98f6d6ba2. Its mathematical derivation is approved.

- Nonemptiness follows directly from the positive-dimensional evaluation kernel for any x, without selecting an actual quadratic.
- A nonempty projective homogeneous zero locus has affine-cone dimension one larger. The previous dimension bound therefore gives height at least six, and the general maximal-minor height bound gives height at most six.
- The resulting grade-six hypothesis in the regular polynomial ring is exactly the Eagon-Northcott maximal-minor acyclicity hypothesis. The quotient is Cohen-Macaulay of dimension nine. Positive depth at the irrelevant maximal ideal gives saturation; perfection gives unmixedness. None of these steps requires generic entries.
- For ranks five and ten with rank bound four, the Porteous determinant has size one and is c6(F-E). Its value is the h6 coefficient in (1-h)^(-5), namely 210. This is the degree of the determinantal scheme with its multiplicities, not a count of reduced points or components.
- Reducedness and irreducibility are not inferred. The support-drop scheme on P4 and the primary-bad scheme on P14 remain correctly distinguished.
