# Exact septic saturation and regularity of the HM lines

Work over C on P^4. Let F be the normalized Horrocks–Mumford bundle, B=End_0(F), and C its transverse union of twenty-five disjoint evaluation-degeneracy lines. Write E=F(3), V_s=H^0E (dimension four), and D=det V_s. We prove

h^1B(-2)=0, h^2B(-2)=20, h^0I_C(7)=130, h^1I_C(7)=0, reg I_C=8.

## 1. The remaining symmetric-monad differential

Use the N-equivariant monad of PR464, A O(-1) -> W tensor K -> C_0 O, with A=V_1, C_0=V_3, dim W=2, K=Omega^2(2). The symmetric-square complex, twisted by O(-1), has cohomology B(-2). Its five terms, in degrees -2 through 2, are

Lambda^2A O(-3), A tensor W tensor K(-2),
Sym^2(W tensor K)(-1) direct-sum A tensor C_0 O(-2),
W tensor C_0 tensor K(-1), Lambda^2C_0 O(-1).

All line-bundle terms and K(-1)=Omega^2(1) are acyclic. K(-2)=Omega^2 has only H^2=C. Decomposing the central term as in PR464, the summand Lambda^4Q*(-1)=O(-2) is acyclic. For S_(2,2)Q*(-1), the shifted Bott weight is (3,5,4,1,0); sorting requires two transpositions and gives highest weight (1,1,1,0,0). Its sole cohomology is an irreducible ten-dimensional GL_5-module in degree two. For S_(2,1,1)Q*(-1), the shifted weight (3,5,3,2,0) repeats, so it is acyclic.

Thus the hypercohomology page has only

E_1^(-1,2)=A tensor W, dimension ten,
E_1^(0,2)=Sym^2W tensor T', dimension thirty,

where T'=H^2(Sym^2Omega^2(3)) is the ten-dimensional irreducible just obtained. The only differential is d_1 between these entries. We now prove it is nonzero without evaluating the HM monad map on any selected instance.

## 2. A universal projective-plane cup lemma

On P^4 consider the natural product

mu: H^2(Omega^2) tensor H^0(Omega^2(3)) -> H^2(Sym^2Omega^2(3)).

This is GL_5-equivariant. Its first factor is one-dimensional and trivial, its second factor T=Lambda^3(ambient vector space)^* is irreducible of dimension ten by the exterior Euler sequence, and the target T' is irreducible of dimension ten by the Bott calculation above.

To show mu is nonzero, restrict to any linear plane P^2. The natural cotangent surjection gives a commutative product diagram with bottom row

H^2(Omega^2_P2) tensor H^0(Omega^2_P2(3)) -> H^2(Sym^2Omega^2_P2(3)).

Since Omega^2_P2=O_P2(-3), this is H^2O(-3) tensor H^0O -> H^2O(-3), the nonzero scalar product. The restriction H^2Omega^2_P4 -> H^2Omega^2_P2 is an isomorphism: it sends the square of the hyperplane class to its nonzero square on the plane. The map H^0Omega^2_P4(3) -> H^0Omega^2_P2(3) is surjective, identified by the exterior Euler sequence with the surjection on third exterior powers of dual vector spaces. Consequently mu is nonzero, hence is an isomorphism after fixing a nonzero generator of H^2Omega^2.

This lemma concerns only universal differential forms on projective space. It does not select or evaluate an HM/source matrix.

## 3. Injectivity forced by the universal lemma and symmetry

Let f denote the monad's first map. Equivalently f is a nonzero linear map A -> W tensor T. In the symmetric-square differential, the component landing in Sym^2W tensor T' is, up to a nonzero normalization scalar,

a tensor w -> sym_W(f(a) tensor w),

where T is identified with T' by mu. This follows directly from the differential on a symmetric square: it multiplies f(a) by the degree-zero middle factor w, while the other component lands in the acyclic A tensor C_0 O(-2).

Choose a with f(a) nonzero. For any nonzero w, multiplication by w from W to Sym^2W is injective, and stays injective after tensoring with T. Hence d_1 is nonzero. The source A tensor W is irreducible as an N-module by HM's criterion (2.2): A is irreducible on the Heisenberg subgroup and W is irreducible on its quotient. Since d_1 is N-equivariant, its kernel is zero.

The two-entry spectral sequence now gives h^1B(-2)=0 and h^2B(-2)=30-10=20, with all other cohomology of B(-2) zero. No coefficient, numerical rank, or selected differential was computed.

## 4. Septic saturation

Twist the evaluation Eagon–Northcott sequence by two:

0 -> D tensor B(-3) -> Lambda^3V_s tensor F -> Lambda^2V_s tensor O(2) -> I_C(7) -> 0.

Let K_7 be the image of Lambda^3V_s tensor F in Lambda^2V_s tensor O(2). Self-duality of B and Serre duality give H^1B(-3)=H^3B(-2)^*=0, h^2B(-3)=20, and H^3B(-3)=H^1B(-2)^*=0. The primary cohomology of F is H^0F=0, h^1F=5, H^2F=0. The first short exact sequence therefore gives

H^0K_7=0, 0 -> Lambda^3V_s tensor H^1F -> H^1K_7 -> D tensor H^2B(-3) -> 0, H^2K_7=0.

Both outer spaces in the middle sequence have dimension twenty. The second short exact sequence gives

0 -> Lambda^2V_s tensor S_2 -> H^0I_C(7) -> H^1K_7 -> 0, H^1I_C(7)=0.

Hence h^0I_C(7)=6*15+40=130. The ninety-dimensional first term is precisely the quadratic multiples of the six quintics; it injects. The forty-dimensional quotient records classes beyond these quadratic multiples, not automatically forty minimal septic generators.

## 5. Exact regularity and the full Hilbert function

PR464 proves h^1I_C(6)=5, so I_C is not 7-regular. To prove 8-regularity, we already have H^1I_C(7)=0. The restriction sequence, the disjoint-line description, and the cohomology of projective space give

H^2I_C(6)=H^1O_C(6)=0, H^3I_C(5)=0, H^4I_C(4)=0.

Thus reg I_C=8 exactly. In particular H^1I_C(d)=0 for every d>=7, and

h^0I_C(d)=binomial(d+4,4)-25(d+1) for all d>=7.

There are no ideal sections through degree four by PR463 section 2's restriction injectivity; PR458 gives h^0I_C(5)=6 and PR464 gives h^0I_C(6)=40. Therefore the homogeneous coordinate ring has Hilbert function

1, 5, 15, 35, 70, 120, 170, 200, 225, ...,

with value 25(d+1) in every degree d>=7. Regularity also implies that the saturated homogeneous ideal is generated in degrees at most eight.

## 6. The remaining septic generator/syzygy dependency

Let U_6 be PR464's canonical ten-dimensional new sextic complement. Multiplication induces

S_1 tensor U_6 -> H^0I_C(7)/(S_2 H^0I_C(5)),

a map from dimension fifty to dimension forty. If g_7 denotes the number of minimal degree-seven generators, its cokernel has dimension g_7 and its kernel has dimension 10+g_7. Indeed the image adds exactly the products of all sextics beyond the already included quadratic quintic products. Equivalently the full multiplication S_1 tensor H^0I_C(6) -> H^0I_C(7) has kernel dimension 70+g_7.

Thus at least ten linear relations among the new sextic products occur modulo the quintic-product space. The exact value of g_7 requires this multiplication map, not merely the Hilbert function or the forty-dimensional quotient. No value of g_7 or a full minimal Betti table is asserted here. The exact septic target dimension now supplies a previously missing ambient dimension for PR465's intersection with (u^2,v)_7, but does not determine that intersection or its local mismatch kernel.

## Sources and scope

- HM (1973), equivariant monad and irreducibility criterion, section 2: https://www.dam.brown.edu/people/mumford/alg_geom/papers/1973a--Rk2BdleP%5E4-NC.pdf
- PR464, a091db646c2ad9ba73d0893f4d92ff54891aaf0c, symmetric monad, exact sextic saturation and canonical complement: https://github.com/Akilleez-QA/read-em-and-weep/blob/a091db646c2ad9ba73d0893f4d92ff54891aaf0c/research/hm/exact-sextic-saturation/PROOF.md
- PR463, 8ec3631dcd6937e6cc7491d0200c1c78b5d21434, Eagon–Northcott setup and degree-four restriction injectivity: https://github.com/Akilleez-QA/read-em-and-weep/blob/8ec3631dcd6937e6cc7491d0200c1c78b5d21434/research/hm/order-four-residue/PROOF.md
- PR167, 063da90fc4543304e87e701cdefcc08225412f17, primary F cohomology: https://github.com/Akilleez-QA/read-em-and-weep/blob/063da90fc4543304e87e701cdefcc08225412f17/research/conductor-normalization/sharper-hm-regularity/SHARPEST-BOUND.md
- PR457, 961694c4f3c805f0d58508811a42da4030dce7a6, cubic restriction injectivity: https://github.com/Akilleez-QA/read-em-and-weep/blob/961694c4f3c805f0d58508811a42da4030dce7a6/research/hm/fixed-cubic-interpolation/PROOF.md
- PR458, b46c3b48a8b10a7d0656fde247f2c3f258d1fd23, exact quintic dimension: https://github.com/Akilleez-QA/read-em-and-weep/blob/b46c3b48a8b10a7d0656fde247f2c3f258d1fd23/research/hm/pair-interpolation/PROOF.md
- PR465, c990d553bc12aae7d979bf1ccda996449fcea910, the septic intersection dependency: https://github.com/Akilleez-QA/read-em-and-weep/blob/c990d553bc12aae7d979bf1ccda996449fcea910/research/hm/squared-quadratic-residue/PROOF.md

These are structural arguments using universal forms, Bott theory, symmetry and exact sequences, not an imported computational tensor-cohomology table. No selected actual HM/source-instance evaluation, numerical multiplication matrix or rank, parameter search, generator/checker or large computation is used. The original fixed-pair quotients, actual-source membership, pure conditions, higher-order lifting and algebraicity remain separate. Mathematical proof text is not formal proof-assistant verification.
