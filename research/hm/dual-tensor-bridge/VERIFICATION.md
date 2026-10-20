# Exterior truncation and the symmetric dual-algebra bridge

Work over C with S=Sym(T), dim T=5, and H_j=H²(End_0(F)(j−5)) as in PR482. Put W=H_0=W′, I=Ann_S H, R=S/I, and N_j=R_(5−j)*, with the usual dual S-action. Write m=S_+.

The inputs are the actual degree-zero generation and quadratic relation space of PR482, and the scalar-algebra and compatible symmetric pairing results of PR488. In particular H has no linear relations, its quadratic relation space is A*⊗W, S_2=A*⊗Sym²W, and det W is trivial. Also R has Hilbert function (1,5,15,25,15,3) and is level of degree five. The representation identity Sym²W⊗W=W⊕Q_4 has multiplicity one for W.

## 1. Exterior square

Let L=ker(S⊗W→H). The exterior square has presentation

Λ²_S H = (S⊗Λ²W) / image(L⊗_S(S⊗W)→S⊗Λ²W).

There are no relations in degrees zero or one. The quadratic image is the equivariant image of L_2⊗W in S_2⊗Λ²W. It is nonzero: for a basis x,y of W and a nonzero element a⊗x+b⊗y of L_2, wedging with x and y extracts −b and a. Thus at least one wedge is nonzero. The target S_2⊗det W=S_2 is irreducible, so this quadratic image is the whole target. All degrees at least two are therefore zero, and no further relation can change the first two degrees. Consequently

Λ²_S H ≅ (S/m²)⊗det W ≅ S/m².

## 2. The symmetric map

For homogeneous h∈H_i and k∈H_j, define

β(h,k)(q)=b(qh,k),  q∈R_(5−i−j),

where b is the perfect symmetric Serre/trace pairing of total degree five. The value is independent of the representative of q because I annihilates H. Compatibility of b with polynomial multiplication shows β(fh,k)=β(h,fk)=fβ(h,k), with the dual S-action on N. Symmetry of b and compatibility give β(h,k)=β(k,h). Thus β induces a natural graded S-linear map

Φ: Sym²_S H → N.

The degree-zero map is the dual of the isomorphism R_5→Sym²W* proved in PR488, so it is an isomorphism. Since R is level of degree five, N is generated in degree zero. This last assertion can be checked by dualizing: the dual of N/mN is Soc(R), which is concentrated in R-degree five. Hence Φ is onto in every degree. It is an isomorphism in degree one because H has no linear relations and both sides have dimension15 there.

## 3. The quadratic relation image: a universal identity

A dimension inequality alone does not prove that Φ_2 is injective. One must prove that the symmetric quadratic relation image has dimension20. This can be done without evaluating any actual HM coefficients.

For any two-dimensional vector space W, there is a canonical injection

r: W⊗Λ²W → Sym²W⊗W,
r(w⊗(x∧y))=wx⊗y−wy⊗x.

This is the lower Clebsch–Gordan summand. With det W trivial and x,y a basis, write r(x)=x²⊗y−xy⊗x and r(y)=xy⊗y−y²⊗x. Tensor by W and multiply into the final W-factor. The resulting universal map W⊗W→Sym²W⊗Sym²W sends the ordered inputs x⊗x, y⊗x, x⊗y, y⊗y to

x²⊗xy−xy⊗x²,
x²⊗y²−xy⊗xy,
xy⊗xy−y²⊗x²,
xy⊗y²−y²⊗xy.

These four tensors are linearly independent: the first and last have monomial positions absent from the others, and the middle two have respectively the unique positions x²⊗y² and y²⊗x². Equivalently, both the Λ²W and Sym²W summands survive.

The actual inclusion L_2=A*⊗W→S_2⊗W=A*⊗Sym²W⊗W is, up to nonzero scalar, id_(A*)⊗r, by the multiplicity-one identity Sym²W⊗W=W⊕Q_4 and the normalizer irreducible conventions of PR482/488. Therefore the map L_2⊗W→S_2⊗Sym²W is injective. Its image is A*⊗(1⊕U′), of dimension20, inside A*⊗(1⊕U′⊕J_5). No other relations contribute in degree two. Thus

(Sym²_S H)_2 ≅ A*⊗J_5,  dim=25,

and the surjection Φ_2 to N_2 of dimension25 is an isomorphism. In summary, Φ is onto and is an isomorphism in degrees zero, one and two. Its kernel is concentrated in degrees at least three; no global isomorphism is asserted.

## 4. Tensor-square consequence

Over C, the swap involution splits H⊗_S H as Sym²_S H⊕Λ²_S H. The pairing map H⊗_S H→N vanishes on the exterior summand. Its kernel is therefore

(S/m²)⊕ker Φ,

where the second summand is zero through degree two. In particular H⊗_S H has dimensions (4,20,25) in degrees zero, one and two, and the pairing-kernel dimensions in those degrees are (1,5,0). This isolates all antisymmetric degeneracy and leaves the remaining symmetric uncertainty strictly in degrees at least three.

The complete presentation bound for H in PR482 also implies that Sym²_S H has defining relations generated in degrees two and three: its relation module is the image of L⊗W, and L is generated in precisely those possible degrees. This does not exclude additional relations in N, since ker Φ has not been determined.

## Dependencies and limits

- PR482, actual H generation and presentation: https://github.com/Akilleez-QA/read-em-and-weep/blob/30c2f32418bbe68ad5b2635ee424d698f329fe8d/research/hm/dual-cohomology-presentation/PROOF.md
- PR488, scalar annihilator algebra and symmetric pairing: https://github.com/Akilleez-QA/read-em-and-weep/blob/cecc51819d529e270afc9aac73a5715c3beee54c/research/hm/dual-annihilator/PROOF.md

This is a structural independent audit and derivation, not formal proof-assistant verification. The displayed two-variable identity is a universal tensor identity, not a selected HM-instance computation. No actual HM matrix, numerical rank, source-instance evaluation, coefficient search, or large computation is used. The cubic and middle Betti parameters, the higher-degree kernel of Φ, the original fixed-pair quotient, higher-order lifting and algebraicity are not determined.
