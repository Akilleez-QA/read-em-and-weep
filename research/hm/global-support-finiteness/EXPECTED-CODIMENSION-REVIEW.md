# Independent review of exact codimension and degree

Reviewed EXPECTED-CODIMENSION.md at SHA256 c69b5bfa3b50d9bc664ab8303d8c3cc7817d5f90e45351c0cb85b6b98f6d6ba2, together with its dependency PROOF.md at SHA256 f27a7faec3fe4ea0e10d80b4f480554926882d791c050c11afc09bb17ee41b96.

## Mathematical verdict

Approved. Nonemptiness follows from the evaluation kernel dimension, without evaluating a selected quadratic. The affine cone of the nonempty projective determinantal locus has dimension one greater. The prior bound and the maximal-minor height bound therefore force height exactly six. In the regular polynomial ring, grade equals height. Eagon-Northcott then yields a Cohen-Macaulay quotient of dimension nine. Positive depth at the irrelevant maximal ideal eliminates saturation torsion, and perfection gives unmixedness. These arguments require expected grade, not generic matrix entries.

For the rank-five to rank-ten bundle map and rank bound four, the Porteous determinant has size one. The degree is the coefficient of h6 in (1-h)^(-5), equal to binomial(10,6)=210. This is a scheme degree including multiplicities. Reducedness, irreducibility, and any full-adjoint conclusion remain unproved, exactly as stated.

## Public-source checks

The following accessible source statements were checked directly:

- Eisenbud, Huneke and Ulrich, [Heights of Ideals of Minors](https://arxiv.org/pdf/math/0209184), introduction, pages 1–2. It recalls the classical determinantal height bound; its displayed Bruns bound also specializes to six when the matrix has ranks 10 by 5 and the minor size and generic rank are five. The projective codimension bound is also stated directly in Fulton's chapter below.
- Booms-Peot and Cobb, [Virtual criterion for generalized Eagon-Northcott complexes](https://arxiv.org/pdf/2111.13773), introduction and Section 2.2. The introduction explicitly recalls that the classical complex resolves the maximal-minor ideal at maximal depth, and Section 2.2 gives the complex of length f-g+1. The argument under review uses this ordinary exactness theorem, not a weaker virtual-resolution conclusion. The author's preprint is an accessible counterpart of the journal link in the proof.
- Fulton, [Degeneracy Loci and Grassmannians](https://link.springer.com/chapter/10.1007/978-1-4612-1700-8_15), publisher chapter preview from Intersection Theory. It states the codimension bound, the determinantal Chern-class formula, and the identification with the natural scheme cycle under expected dimension and nonsingularity. It also defines the degeneracy scheme by the appropriate minors and c(F-E)=c(F)/c(E).

This is mathematical and source review, not formal proof-assistant verification. No selected HM/source coefficient matrix, numerical rank, or experiment was evaluated.
