# Independent scoped mathematical review

## Frozen target and verdict

Reviewed `PROOF.md` with SHA256
`2d60f124d55bae90989b39051c88057e5a083237b0b4603a6128b483433146fd`.
The reviewer did not author or modify that proof, and did not read another review before reaching this verdict.

**Verdict: no blocking mathematical flaw found in the new septic argument.** Subject to the explicitly imported HM geometry and lower-degree results, the proof establishes

- h^1 B(-2)=0 and h^2 B(-2)=20;
- h^0 I_C(7)=130 and h^1 I_C(7)=0;
- exact ideal-sheaf regularity 8 and the stated full Hilbert function;
- the stated conditional generator/syzygy dimension bookkeeping, without determining the number of minimal septic generators.

This is independent human-readable mathematical checking of an authored argument, not formal proof-assistant verification or independent reconstruction of every earlier dependency.

## 1. Universal cup product

The restriction argument is valid. For a linear plane j:P^2→P^4, the cotangent quotient induces maps on exterior and symmetric powers and therefore a commutative cup-product diagram. The map on H^2 Ω^2 sends the nonzero square of the hyperplane class to its nonzero square on P^2. Both spaces are one-dimensional, so this map is an isomorphism. If U is the three-dimensional ambient subspace defining the plane, the exterior Euler sequence identifies the section restriction with Λ^3 V*→Λ^3 U*, which is onto.

On the plane Ω^2 is O(-3), up to the harmless constant determinant factor when retaining full GL linearizations. Hence the lower cup map is multiplication of H^2 O(-3) by a nonzero constant section of O. It is nonzero. Choose preimages of both nonzero factors under the two restriction maps: the product of these preimages cannot vanish upstairs. This proves nonvanishing of the universal map without assuming surjectivity of the restriction on the target H^2.

The source and target upstairs are irreducible ten-dimensional GL modules after including the trivial one-dimensional H^2 Ω^2 factor. Equivariance and nonvanishing imply the claimed isomorphism. No chosen HM map is evaluated in this argument; the plane is used only to test universal differential-form multiplication.

## 2. Symmetric monad and Bott calculation

Since Sym^2 F=B(-1), twisting the graded symmetric square by O(-1) computes B(-2). The displayed degrees -2 through 2 and their twists agree with the graded symmetric-square construction: the odd exterior factors occur at the ends, and the central cross term is A⊗C_0 O(-2).

The line bundles O(-3), O(-2), O(-1) on P^4 are acyclic. Ω^2 has exactly H^2 of dimension one, whereas Ω^2(1) is acyclic. The two Schur weights in the proof check symbolically:

- (3,5,4,1,0) sorts to (5,4,3,1,0) with exactly two inversions; subtracting (4,3,2,1,0) gives (1,1,1,0,0), of exterior-cube dimension ten.
- (3,5,3,2,0) has a repeated entry and gives no cohomology.

The determinant summand of Sym^2 K(-1) is acyclic as well. Thus the only E_1 entries really are the ten-dimensional term at (-1,2) and the thirty-dimensional term at (0,2). In particular no hidden higher differential can change their kernel/cokernel computation.

A linearization convention deserves only a minor clarification, not a correction of the result: writing Λ^4 Q*=O(-1) suppresses a constant determinant representation under GL_5. Acyclicity is unaffected, and N⊂SL_5 removes this distinction in the equivariant monad argument. The source and target of the cup product themselves have their natural compatible linearizations.

## 3. Identifying and proving nonzero the differential

The first monad morphism is a section-valued map f:A→W⊗H^0 K(1)=W⊗H^0 Ω^2(3). Apply the differential in the graded symmetric square to the A⊗W⊗K(-2) term. Its component in Sym^2(W⊗K)(-1) is multiplication by f; the other component goes to A⊗C_0 O(-2), which is acyclic.

Projecting to Sym^2 W⊗Sym^2 K(-1) symmetrizes the two W factors and the two K factors. On H^2, the latter operation is precisely the universal cup product checked above. The numerical normalization of symmetrization is nonzero in characteristic zero. Therefore the displayed formula for d_1 is valid, not merely a dimension-compatible guess.

For a with f(a)≠0 and any nonzero w∈W, the linear map W→Sym^2 W given by multiplication by w is injective: the symmetric algebra of W is a polynomial domain. Tensoring this injection with T preserves injectivity. Under the cup-product isomorphism the image of f(a) therefore stays nonzero. This proves d_1≠0; it does not yet prove its injectivity without the symmetry argument.

The source A⊗W is irreducible for N. The primary HM paper, section 2, supplies A=V_1, irreducible on the Heisenberg subgroup H, the irreducible quotient representation W, and criterion (2.2). The multiplicity space Hom_H(A,A⊗W) is W, so this criterion applies exactly to the source in question. Functoriality of the symmetric square and of cohomology makes d_1 N-equivariant. Its kernel is an N-submodule of an irreducible module; since the map is nonzero the kernel must be zero.

Consequently the two total degrees are 1 and 2, and the resulting dimensions are 0 and 30−10=20. All other cohomology of B(-2) vanishes.

Primary source inspected for the monad and representation facts: [Horrocks–Mumford (1973), printed pp. 67–68, §2](https://www.dam.brown.edu/people/mumford/alg_geom/papers/1973a--Rk2BdleP%5E4-NC.pdf). No explicit matrix from that source was evaluated.

## 4. Septic Eagon–Northcott calculation

The resolution in section 4 is exactly the additional O(1) twist of the sextic Eagon–Northcott sequence displayed in the supplied order-four dependency. Serre duality on P^4 with B*=B pairs B(-3) with B(-2), interchanging cohomological indices i and 4−i. It gives H^1 B(-3)=H^3 B(-3)=0 and h^2 B(-3)=20.

Splitting at K_7, H^0 F=0 and H^1 B(-3)=0 give H^0 K_7=0. The next segment is an injection of Λ^3 V_s⊗H^1 F into H^1 K_7, followed by a surjection onto D⊗H^2 B(-3), since H^2 F=0. Its dimensions are 20 and 20. The following segment gives H^2 K_7=0 because H^2 F and H^3 B(-3) vanish. The second short exact sequence therefore gives exactly the asserted 90+40=130 sections and zero H^1 I_C(7).

The injection of the ninety-dimensional space is actual multiplication of evaluation minors by quadrics, by the provenance of the Eagon–Northcott map. Thus the quotient is forty-dimensional. It is correctly not identified with the minimal-generator space.

## 5. Regularity, Hilbert function, and syzygies

For 8-regularity the four necessary vanishings are H^1 I_C(7), H^2 I_C(6), H^3 I_C(5), and H^4 I_C(4). The first is new; the others follow from the structure-sheaf sequence of a disjoint union of lines and projective-space cohomology. In particular H^1 O_C(6)=0, and O_C has no cohomology in degrees above one. Nonzero H^1 I_C(6), imported from the sextic calculation, excludes 7-regularity and hence every lower regularity. Persistence of regularity gives H^1 I_C(d)=0 for d≥7.

The dimension formula in degree d≥7 is consequently binomial(d+4,4)−25(d+1). With the imported absence of quartics and lower ideal sections, six quintics, and forty sextics, subtracting ideal dimensions from those of the polynomial ring gives precisely 1,5,15,35,70,120,170,200,225,… . Generation in degrees at most eight follows from 8-regularity of the saturated ideal sheaf.

Let P_7=S_2 I_5. Since I_6=S_1 I_5⊕U_6, one has S_1 I_6=P_7+S_1 U_6. Thus the cokernel of S_1 U_6→I_7/P_7 is exactly the degree-seven minimal-generator space, of dimension g_7. Its image has dimension 40−g_7, yielding kernel dimension 50−(40−g_7)=10+g_7. The full multiplication has image dimension 130−g_7 and kernel dimension 200−(130−g_7)=70+g_7. These are relations modulo quintic products in the first formulation, not necessarily vanishing products by themselves. The proof preserves that distinction.

## Dependencies and boundaries

The review imports the stated upstream premises from these pinned sources:

- [Exact sextic saturation (PR464)](https://github.com/Akilleez-QA/read-em-and-weep/blob/a091db646c2ad9ba73d0893f4d92ff54891aaf0c/research/hm/exact-sextic-saturation/PROOF.md), SHA256 `105812f9f0414a744c3d8b881edf4d3cd3b651ab0a59d6ee4e82a6ef0e9c1a3e`;
- [Order-four residue (PR463)](https://github.com/Akilleez-QA/read-em-and-weep/blob/8ec3631dcd6937e6cc7491d0200c1c78b5d21434/research/hm/order-four-residue/PROOF.md), SHA256 `556ebcc8139e03b804ac9991044aac8eed5af883170d1799db78d6fb12209b3e`;
- [Squared-quadratic residue (PR465)](https://github.com/Akilleez-QA/read-em-and-weep/blob/c990d553bc12aae7d979bf1ccda996449fcea910/research/hm/squared-quadratic-residue/PROOF.md), SHA256 `d26e27c3d54a96352742424728c0f7fa4d365e954f923afd70964670b632cf99`.

Their stated HM line configuration, Eagon–Northcott setup, primary F cohomology, absence of lower-degree ideal sections, and prior quintic/sextic conclusions are dependency assumptions here, rather than claims that every upstream proof was reverified from scratch. I checked that the new argument uses them with the correct twists, indices, and logical scope.

The new dimension 130 supplies the ambient septic dimension needed by the squared-quadratic residue model, but does not determine its intersection with (u²,v)_7 or the mismatch map. The proof does not resolve those, g_7, the full Betti table, fixed-source membership, pure conditions, higher lifts, or algebraicity. No selected HM/source instance, multiplication matrix, numerical rank, coefficient search, computational cohomology table, or large computation was used in this review. Only source inspection, symbolic geometry/cohomology, elementary dimension arithmetic, and file integrity hashing were performed.
