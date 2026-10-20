# What transgression and Euler-module data cannot force

## Result

The following is a bounded exclusion, not a counterexample in Horrocks–Mumford geometry. The injective ten-dimensional d5, the thirty-dimensional global-cycle target, the irreducible twenty-dimensional quotient, the Euler/PGL tangent module, and even all coordinate-module structures on H1 and H2 can coexist abstractly with a canonical identically zero ordered triple Massey operation. Consequently none of these additive, filtered, or module-theoretic inputs, taken alone or together as specified below, forces m011 nonzero.

The construction deliberately does not realize the actual endomorphism complex of the linear HM resolution. In particular, it does not realize the inner differential and universal commutator transgression formula in cech-transgression-primitives/PROOF.md. It cannot be used to decide actual HM vanishing.

## 1. An S-linear construction

Work over a characteristic-zero field. Let S=Sym(W), with dim W=5, and give W weight -1. Let M be any graded S-module with M_r=0 for r>=2, dim M_1=5, and dim M_0=24. Let T be any graded S-module with dim T_2=20. All modules can be equivariant for a finite group N; assume the specified structures are equivariant. Put

J=Lambda^2_S M, and let P be an isomorphic copy of J.

Define a unital cohomologically graded S-DGA by

A^0=S, A^1=M direct-sum P, A^2=J direct-sum T,

and no other cohomological degrees. Its differential is the identity P -> J and is zero elsewhere. Its only positive-degree multiplication is

M tensor_S M -> J, (m,n) -> m wedge n.

All other products of positive-degree elements are zero. The given S-module actions define products with A^0.

Associativity follows because all triple products of positive-degree elements vanish, and exterior multiplication is S-balanced. The differential is a derivation: its nonzero values are in J, whose products with positive-degree elements vanish. Thus A is a DGA, not merely a complex with an assigned spectral sequence.

Projection killing P and J is an S-DGA quasi-isomorphism

A -> H=S direct-sum M[-1] direct-sum T[-2],

where the notation specifies cohomological degrees 1 and 2 and all positive-degree products in H vanish. Hence A is formal as an S-DGA.

For closed degree-one inputs in M choose their product primitives in P. Both terms of every triple Massey representative then vanish strictly. Indeterminacy vanishes because every product of degree-one cohomology classes is zero. Therefore all these triple Massey sets are the singleton {0}; in particular the weight-(0,1,1) operation is canonically zero. This is a universal algebra argument, not evaluation of any HM value.

## 2. The exact d5 and dimensions

Use a decreasing filtration assigning indices

S:0, M:1, P:-3, J:2, T:2.

F^p is the sum of summands with index at least p. This filtration is multiplicative, including products with S; the only nonzero positive multiplication has indices 1+1=2. The sole differential raises filtration by 5. Thus d0 through d4 vanish and d5 is exactly P -> J.

In weight 2, M_2=0. Since all weights in M are at most 1 and S has nonpositive weights, the weight-two part of Lambda^2_S M is canonically Lambda^2_k M_1: no balancing relation involving a positive polynomial degree can occur in this top weight. Therefore J_2 and P_2 both have dimension 10. The only differential is

E5^(-3,4)=P_2 -> E5^(2,0)=J_2 direct-sum T_2,

injective with thirty-dimensional target and twenty-dimensional cokernel T_2. Its image is precisely the independent wedge-product boundaries of M_1. The q=0 degree-two cycle space is J_2 direct-sum T_2; there are no q=0 degree-one weight-two boundaries.

Thus the transgression, its source, its target quotient, and its identification with the exterior-product relations all match the stated abstract HM data. If T_2 is the actual irreducible N-module, the image-zero-or-all representation constraint also holds, with the zero alternative realized.

## 3. Euler multiplication, and the stronger module version

A concrete choice preserving the full polynomial Euler presentation is

M=(S tensor B)/S e, dim B=5, W=B*, e=sum_i x_i tensor b_i.

The generators B have weight 1 and e has weight 0. Then M_1=B and M_0=(B* tensor B)/k Id, with the actual Euler multiplication W tensor B -> M_0. This is an Euler cokernel module, not a free S-module.

More strongly, one may take M to be the actual graded coordinate module direct-sum_r H1(End H(-r)) and T the actual graded coordinate module direct-sum_r H2(End H(-r)), with their actual S-actions. The imported vanishing H1(End H(-r))=0 for r>=2 makes Section 2 apply unchanged. No action coefficients need be known or evaluated. This construction preserves all coordinate-module data of these two cohomological degrees, not just their first Euler multiplication. It does not preserve actual Yoneda products in other degrees, a sheaf realization, or an endomorphism-algebra realization.

## 4. Smooth families and formal adjugation do not repair the gap

For any basis a1,...,a24 of M_0, eta=sum_i t_i a_i obeys d eta+eta^2=0 over the formal power-series base: d eta=0 and eta wedge eta=0. Its tangent map is an isomorphism onto M_0. Thus a smooth formal Maurer–Cartan family of the correct tangent dimension is compatible with this example. This is not a construction of the actual PGL orbit of HM bundles.

There is also a graded anti-involution tau, equal to -1 on M,T and +1 on S,P,J. It commutes with d and obeys tau(ab)=(-1)^(|a||b|)tau(b)tau(a). The scalar sub-DGA C=S direct-sum P direct-sum J has no positive cohomology. Define trace to C as twice the identity on C and zero on M,T; then tau=inclusion composed with trace minus identity. The rank-two adjugation normalization and scalar vanishings used to deduce reversal therefore hold formally. This is not an actual locally free rank-two endomorphism sheaf and must not be described as one.

## 5. Where an actual nonvanishing proof must add information

The actual HM resolution has d=sum_i v_i D_i and differential on its Hom complex given by the graded commutator with d. Its operators T_i=[D_i,-] determine both the d5 transgression and multiplication primitives. The present artificial DGA has no such realization: in the Euler-cokernel example sum_i x_i b_i is already zero, while its differential P -> J is nonzero. Thus the internal differential cannot be that inner commutator.

The universal identity involving T0...T4 and the fourfold deleted products is genuine extra multiplicative/homotopy information. A proof that this information forces a nonzero quotient component would settle the problem, but it is not a consequence of d5 injectivity, irreducibility, Euler multiplication, smoothness, or coordinate cohomology modules alone. Similarly an abstract theorem that the entire derived endomorphism algebra is nonformal would still need to localize its obstruction to this weight-(0,1,1) arity-three component: nonformality may occur in another weight or a higher arity.

A genuinely different structural next step is therefore to study the multiplicative Postnikov extension of the actual twisted derived-endomorphism algebra, retaining its inner-linear-resolution realization. One would need to prove that its arity-three obstruction survives specifically on U0 tensor U1 tensor U1, modulo defining-system changes. Merely showing that some multiplicative Postnikov extension or some Hochschild obstruction is nontrivial is insufficient. This is a precise missing theorem, not a claimed proof or a guarantee that the route succeeds.

## Evidence boundary

Only static reads of the specified proofs, formal S-module/DGA/filter identities, and local mathematical notes were used. No actual Massey value, HM source/model matrix product, point, jet, rank, polynomial instance, or residual was evaluated; no geometric model was evaluated. The countermodel is an abstract algebraic consistency construction, not an execution of any geometric model.
