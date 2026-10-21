# The generic sextic flag cannot be alpha

## Statement and scope

Assume the actual Horrocks–Mumford Rao branch a=0,b=4 and the integral sextic D_H supplied by PR543 for general hyperplanes H. Write E=F(3), U=H^0(E), dim U=4, and C for the actual degeneracy locus, a reduced union of 25 disjoint lines. Then the kernel-map image of D_H is generically a plane quintic in a beta plane of Gr(2,U). Neither the alpha-plane case nor the Grassmannian-line case can hold for general H.

This excludes a generic configuration, not every exceptional hyperplane. It does not exclude the remaining beta-plane case, prove Q4, or evaluate a selected source instance.

## 1. No global section vanishes on all of C

**Lemma.** H^0(I_C tensor E)=0.

The full normalizer N preserves C and acts equivariantly on E. Therefore the kernel

    W = ker[U -> H^0(C,E|C)] = H^0(I_C tensor E)

is an N-subrepresentation. The actual space U is the irreducible four-dimensional representation with character chi_4. Evaluation on C is not zero: indeed it has rank one at every point of C. Thus W is a proper subrepresentation of U, and irreducibility gives W=0.

The rank assertion uses the actual ideal-generation input, not a selected calculation. Rank is at most one on C. If evaluation had rank zero at a point p, all its entries would lie in the maximal ideal at p and all maximal minors would lie in its square. They could not generate the ideal of the smooth reduced line C at p, whose conormal space is nonzero. Hence rank is exactly one.

For the representation input, Horrocks–Mumford's original bundle has c_1=5 and is our E. Equation (4.12), printed page 74, identifies its section representation as chi_4. The appendix character table, printed page 81, gives this irreducible four-dimensional character, with value +4 on the central element -I; it is distinct from the other four-dimensional character chi_4^*, with value -4.

## 2. A generic alpha or line family would contradict the lemma

By the sextic flag reduction, an alpha-plane image or a Grassmannian-line image has a unique common kernel line A_H in U. Equivalently,

    H^0(I_{D_H} tensor E) = A_H,  dim A_H=1.

Indeed, away from Z_H=C intersect H the kernel map is the actual evaluation kernel. The intersection of all kernels along an alpha-plane-spanning quintic, or along a Grassmannian line, is precisely its flag line A_H. A section vanishing there vanishes on all of the integral D_H.

The canonical cubic-base construction of D_H spreads algebraically after restricting to a dense open set of hyperplanes and flattening the family. On the alpha/line stratum, the restriction map from the fixed space U has constant one-dimensional kernel. This produces the rational map

    H |-> [A_H] in P(U)=P^3.

If alpha or line were generic, its domain would have dimension four. The fiber-dimension theorem therefore supplies a positive-dimensional irreducible family T of distinct hyperplanes with a single fixed nonzero section s vanishing on every D_H, H in T. Shrink T as necessary so that all established generic properties hold.

The zero scheme X_s has no divisorial component: a divisorial zero of degree d>=1 would give a nonzero section of E(-d), contrary to H^0(E(-1))=0 and its lower-twist consequences. Since c_2(E)=10, X_s is a pure codimension-two local complete intersection of degree 10. Each integral D_H lies in one of its finitely many integral surface components. After restricting to a dense subset of T, one fixed component S contains D_H for all those H.

A general H in this family does not contain S. Otherwise S would lie in the intersection of two distinct hyperplanes and would be planar; it could not contain the integral sextic D_H spanning H. Hence D_H is contained in the proper hyperplane section S intersect H and

    deg S >= deg D_H = 6.

The Heisenberg group acts trivially on U, so it preserves X_s and permutes its surface components. Its projective quotient has order 25, and the orbit of S has size 1, 5, or 25. Any nontrivial orbit would contribute at least 5*6=30 to the degree of X_s. Since deg X_s=10, S is Heisenberg-invariant.

Suppose S contained no line component L_i of C. Every S intersect L_i would then be finite. For H in the irreducible family T, the point p_i(H)=H intersect L_i belongs to D_H and therefore S. The algebraic map H |-> p_i(H) into that finite set must be constant. Thus all 25 points p_i(H) are constant. These points span H, so H itself is constant, contradicting dim T>0.

Consequently S contains one L_i. Heisenberg transitivity on the 25 lines and invariance of S imply C subset S. Since C is reduced, the section s vanishes on C scheme-theoretically. This contradicts the lemma.

The generic alpha/line alternatives are therefore impossible. The flag reduction leaves only a plane quintic spanning a beta plane for general H.

## Dependencies and source pins

All repository links below refer to Akilleez-QA/read-em-and-weep, PR543, under research/hm/order-four-quadratic-load/.

- [FOUR-CUBIC-SEXTIC-BASE.md at fd58cd7d25b213841fce0c34e5207bc84e62c42f](https://github.com/Akilleez-QA/read-em-and-weep/blob/fd58cd7d25b213841fce0c34e5207bc84e62c42f/research/hm/order-four-quadratic-load/FOUR-CUBIC-SEXTIC-BASE.md): canonical integral sextic, smoothness of Z_H, and the actual generic branch.
- [INTEGRAL-SEXTIC-ACM-RESOLUTION.md at 7c7bf54af204daa4a00ddfec0b69e3c3dda94424](https://github.com/Akilleez-QA/read-em-and-weep/blob/7c7bf54af204daa4a00ddfec0b69e3c3dda94424/research/hm/order-four-quadratic-load/INTEGRAL-SEXTIC-ACM-RESOLUTION.md): ACM genus-three sextic.
- [SEXTIC-PLUCKER-FLAGS.md at a82e9aeaad55a4e58a0fea12581bab1dcf42e4b0](https://github.com/Akilleez-QA/read-em-and-weep/blob/a82e9aeaad55a4e58a0fea12581bab1dcf42e4b0/research/hm/order-four-quadratic-load/SEXTIC-PLUCKER-FLAGS.md): image bundle, degree-five Plucker line bundle, and alpha/beta/line alternatives.
- [EXCLUDE-UNIQUE-QUADRIC-ENDPOINT.md at 8e209e366d157281706bc0f83bf526c5ac46ec60](https://github.com/Akilleez-QA/read-em-and-weep/blob/8e209e366d157281706bc0f83bf526c5ac46ec60/research/hm/order-four-quadratic-load/EXCLUDE-UNIQUE-QUADRIC-ENDPOINT.md): previously established section-zero geometry, Heisenberg action, and surface-family method. Here the irreducibility lemma replaces the degree-five/degree-ten end cases.
- [Horrocks–Mumford, A rank 2 vector bundle on P4 with 15,000 symmetries (1973)](https://www.dam.brown.edu/people/mumford/alg_geom/papers/1973a--Rk2BdleP%5E4-NC.pdf): section representation, equation (4.12), printed p.74; character table, printed p.81. The preceding discussion on pp.73–74 also proves all sections are Heisenberg-invariant.

## Verification and remaining problem

The argument was proposed by Mr. Slop and independently checked, including the primary representation pin. It is an ordinary mathematical proof review, not a formal proof-assistant verification. No selected HM/source-instance coefficient, minor, or rank was evaluated. The remaining generic beta-plane configuration is not analyzed here.
