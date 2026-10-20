# Classifying the marked reversal-compatible formal continuation tower

## 0. Result and exact scope

Let X be a connected complex abelian variety of dimension g, with geometric inversion iota fixing h. Work on the individually inversion-stable affine acyclic cover and in the regular normalized differential descent category specified below. Fix a literal reversal-compatible ambient presentation P modulo h^M, where M >= 3. All higher local products, overlap maps, and triple units may vary.

An equivalence is an invariant even chart gauge and invariant reversal-unitary edge unit which are literally the identity modulo h^M. Chart units implementing 2-morphisms are initially required to be invariant, reversal-unitary, and identity modulo h^M as well. Thus this is a marked continuation problem, not an unmarked moduli problem.

For n >= M, let S_n(P) be the equivalence classes of such presentations modulo h^n. In particular S_M(P) is a singleton. Define

  P_n = H^1(X,T_X)^iota                            if n is even,
  P_n = H^0(X,Lambda^2 T_X)^iota + H^2(X,O_X)^iota  if n is odd.

The plus in the second formula denotes a direct sum. Under the invariant literal lifting input retained by PR416:

1. Every restriction map S_(n+1)(P) -> S_n(P) is surjective. Each fiber is canonically a torsor under P_n. It is not a further quotient by hidden lower-order relative automorphisms.
2. The map from formal marked continuation classes to the inverse limit of these finite class sets is a bijection.
3. Choosing an origin separately in every fiber gives a noncanonical isomorphism of towers of sets, and hence a noncanonical bijection

     S_formal(P)  ~=  product_(n >= M) P_n.

   The finite truncation corresponds to forgetting the later coordinates. On a fourfold these factors have dimensions 16 at even n and 12 at odd n.
4. Every finite or formal relative 1-automorphism is 2-isomorphic to the identity. Formal relative 2-automorphisms of the identity are exactly

     exp( product_(n >= M, n odd) C h^n )

   in the unitary-2-morphism convention. If all ordinary inner 2-morphisms which preserve the allowed 1-gauges are retained, the object classes and conclusion (3) are unchanged, while this group becomes

     exp( h^M C[[h]] ).

Conclusion (3) is only a classification of sets with their truncation tower after noncanonical choices. It supplies no preferred origin, intrinsic linear or affine structure on the full set, moduli scheme, representability theorem, period map, or classification of arbitrary non-parity continuations. In particular this is not the earlier one-step torsor result merely restated: the new work is removal of the lower-automorphism quotient and proof of effectiveness and faithfulness at the formal inverse limit.

No fixed-product all-orders statement, module lift, first-star-to-second-star implication, actual-source obstruction value, algebraicity, or pure diagonal six-condition vanishing is asserted.

## 1. Exact sources and retained hypotheses

The mathematical inputs are:

- PR409, exact commit `59fc9cdc40cf9a21fbb38549767829ff7471294f`: [parity-separated lifting](https://github.com/Akilleez-QA/read-em-and-weep/blob/59fc9cdc40cf9a21fbb38549767829ff7471294f/research/hm/parity-separated-ambient-lifting/PROOF.md), especially its reversal-unitarity lemma and gauge-preservation facts, and the [odd-bivector repair](https://github.com/Akilleez-QA/read-em-and-weep/blob/59fc9cdc40cf9a21fbb38549767829ff7471294f/research/hm/parity-separated-ambient-lifting/ODD-BIVECTOR-REPAIR.md).
- PR416, exact commit `c71356722bc7bd1a426d26ea0ca6d050f4c3ed81`: [reversal-compatible continuation](https://github.com/Akilleez-QA/read-em-and-weep/blob/c71356722bc7bd1a426d26ea0ca6d050f4c3ed81/research/hm/parity-separated-ambient-lifting/REVERSAL-COMPATIBLE-CONTINUATION.md). Nonemptiness retains its invariant literal small-extension input, not merely existence of a lift of some equivalent presentation.
- PR425, exact commit `df433cdd359fa9c7750bf9c8b9765229eac534f6`: [one-step relative lift freedom](https://github.com/Akilleez-QA/read-em-and-weep/blob/df433cdd359fa9c7750bf9c8b9765229eac534f6/research/hm/reversal-relative-lift-freedom/PROOF.md), Sections 2–7. This supplies the one-step torsors and explicit gauge and 2-morphism formulas.
- The [literal small-extension argument](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6259748725) applies explicitly to the stated elliptic fourfold. The general abelian formulation here retains the same invariant literal lifting input, regular normalized polydifferential complex including arity zero, and acyclic-cover hypotheses, exactly as PR416 does.

All cochains and restrictions are strictly invariant. The affine cover has affine finite intersections and computes the required coherent cohomology. Positive-arity cochains are normalized; coefficients are regular differential operators of finite order. There is no imposed uniform differential-order bound across all h-coefficients.

Write A_n = C[h]/(h^n). An object x over A_n consists of associative local products mu_i, differential algebra maps F_ij, and triple units A_ijk, reducing classically to ordinary multiplication, id, and 1, and satisfying

  F_ij F_jk = Ad_i(A_ijk) F_ik,
  A_ijk *_i A_ikl = F_ij(A_jkl) *_i A_ijl.

Formal reversal tau fixes ordinary functions and sends h to -h. Products have coefficient parity mu_r(g,f)=(-1)^r mu_r(f,g), maps commute with tau, and tau(A_ijk)=A_ijk^(-1). Formal reversal is not geometric inversion.

For chart changes E_i and edge units B_ij, the transported presentation is

  mu_i^E(f,g) = E_i^(-1)(mu_i(E_i f,E_i g)),
  F_ij^E = E_i^(-1) Ad_i(B_ij) F_ij E_j,
  A_ijk^E = E_i^(-1)(B_ij *_i F_ij(B_jk) *_i A_ijk *_i B_ik^(-1)).

The E_i are unital invertible differential linear maps commuting with tau; the B_ij satisfy tau(B_ij)=B_ij^(-1). They need not stabilize a fixed object: their purpose is to transport its presentation. They have E_i=id and B_ij=1 modulo h^M.

For chart units C_i in the unprimed product, the 2-morphism formula is

  E_i^new = Ad_i(C_i) E_i,
  B_ij^new = C_i *_i B_ij *_i F_ij(C_j^(-1)).

It keeps both endpoints fixed. If C is unitary, it preserves the even/unitary conditions. These formulas make the usual invertible transport groupoid and its inner 2-morphisms. All compositions, inverses, and endpoint equalities below can be read in these explicit formulas.

## 2. What lifts freely, and what is not being assumed

### Lemma 2.1. Lifting admissible gauge data

Let x_(n+1) be a presentation over A_(n+1), and let x_n be its reduction. Every admissible gauge out of x_n lifts to admissible gauge data out of x_(n+1). The lift need not have a separately prescribed target; its target is the transported presentation. Every invariant unitary chart unit for x_n likewise lifts to such a unit for x_(n+1). Identity modulo h^M is preserved.

Proof. Lift an even unital chart map E by retaining its coefficients and setting its new coefficient to zero. It remains even and unital, is formally invertible since its classical term is id, and has differential coefficients. One could instead choose an arbitrary normalized invariant coefficient when n is even.

For either an edge unit or a chart unit, write D for the lower unit and choose any invariant lift D_hat, with constant term 1. Its norm has the form

  tau(D_hat) * D_hat = 1 + h^n d.

The norm is fixed by tau, since anti-multiplicativity and tau^2=id give

  tau(tau(D_hat) * D_hat) = tau(D_hat) * D_hat.

Hence d=0 for odd n. If n is even, replacing D_hat by D_hat+h^n e changes the norm coefficient by 2e; choose e=-d/2. The resulting unit is unitary and has the original reduction. All operations preserve regularity and invariance. This proves the claim. QED.

The lemma is deliberately not an assertion that every equivalence lifts between two preselected higher objects. The obstruction to such an equivalence can be precisely their different class in P_n. It only lifts freely chosen coordinate data and uses gauge transport to determine the new target.

### Lemma 2.2. Completeness

A compatible sequence of literal presentations, admissible gauges, or unitary chart units has a coefficientwise formal limit of the same kind. All identities and inverse identities hold in the limit.

Proof. Each coefficient stabilizes, and every coefficient in a product, composition, inverse, or descent equation involves finitely many lower coefficients. Its regular differential character is preserved by the finitely many sums and compositions at that coefficient. The finite-level identities therefore imply each formal coefficient identity. Formal inverses are obtained by the same recursive calculation. No analytic convergence or effectivity outside the formal category is used. QED.

## 3. Finite relative automorphisms are 2-trivial

### Lemma 3.1

For every n >= M and object x over A_n reducing literally to P, every automorphism of x whose gauge data are identity modulo h^M is connected to the identity gauge by an invariant unitary chart 2-unit which is identity modulo h^M.

Proof by induction on n. At n=M the gauge itself is literally the identity, and take the identity chart unit.

Suppose the result holds over A_n and g is an automorphism of x over A_(n+1). Its reduction g_bar is 2-isomorphic to id by the induction hypothesis. Lift a chart 2-unit implementing this 2-isomorphism by Lemma 2.1, using the given product of x. Apply the 2-morphism formula to g, with the orientation or inverse of the chosen 2-unit as appropriate. The resulting automorphism g' is literally identity modulo h^n.

It is now a one-step automorphism as computed in PR425. If n is even, its data are E=id+h^n t and B=1, with bt=0 and delta t=0. Thus t is an invariant global vector field. On an abelian variety geometric inversion acts by -1 on H^0(T_X), so t=0 and g'=id literally.

If n is odd, its data are E=id and B=1+h^n c, with delta c=0. Geometric inversion acts by -1 on H^1(O_X), so the invariant class of c vanishes. Choose an invariant Cech zero-cochain s with delta s=c. The chart unit C=1+h^n s is unitary at odd n and changes c to c-delta s=0. It therefore 2-trivializes g'.

Composing the chart 2-units gives the required 2-isomorphism for g. Every unit used is identity modulo h^M. QED.

This proves vanishing of the entire finite relative pi_1, not just its separate top-order graded pieces. Literal automorphisms need not themselves be identity: odd-order Cech-boundary edge automorphisms are removed by 2-morphisms.

### Corollary 3.2. Compatibility of equivalences

Let x_(n+1), y_(n+1) be two higher presentations and suppose at least one equivalence q between them exists. Then any specified equivalence g between their reductions, identity modulo h^M, is the exact reduction of an equivalence between x_(n+1) and y_(n+1).

Proof. The reduction q_bar and g differ by an automorphism of one endpoint. Lemma 3.1 makes that automorphism 2-isomorphic to the identity, so q_bar and g are 2-isomorphic. Express this using the chart-unit formula and lift that chart unit by Lemma 2.1 for the corresponding higher endpoint. Applying it to q gives a new equivalence with exactly reduction g. The endpoints are unchanged by the 2-morphism formula. QED.

Existence of q remains essential. This corollary is a coherence statement for already equivalent endpoints, not a lifting theorem asserting every pair of objects is equivalent.

## 4. The genuine fibers of the finite tower

Fix a class [x] in S_n(P), and a literal representative x. Let T(x) be the PR425 one-step classes of lifts of x, with gauges literally identity modulo h^n. By PR416 this is nonempty, and by PR425 it is a P_n-torsor.

There is a natural map from T(x) to the fiber of S_(n+1)(P) over [x]. We prove it is a bijection.

Surjectivity: Given y in that fiber, choose a gauge identifying y modulo h^n with x. Lift its admissible coordinate data by Lemma 2.1, and transport y. The resulting representative reduces literally to x. Thus it defines a point of T(x).

Injectivity: Suppose two literal lifts of x are related by a gauge which is identity modulo h^M, but not assumed identity modulo h^n. Its reduction is an automorphism of x. By Lemma 3.1 it is 2-isomorphic to the identity. Lift its trivializing chart unit to the source higher presentation and apply the 2-morphism formula. This replaces the gauge by one with the same endpoints and literally identity reduction modulo h^n. The two lifts were therefore already equal in T(x).

This is precisely where an unsupported passage from relative torsors to a classification would otherwise fail. A lower automorphism could have acted on T(x); here its action is proved trivial by an actual endpoint-preserving correction.

The P_n-torsor structure on the fiber is independent of the representative x. Indeed a gauge between two representatives has classical chart and edge parts id and 1. The same lifted gauge data can be used for two upper lifts of one lower presentation: if their products differ by h^n u, the difference of the two edge-unit norms is h^n u(1,1)=0 by normalization. Thus an edge unit lifted to be unitary for one upper product is also unitary for the other. At the new top coefficient h^n, all positive-order parts of the common gauge disappear after multiplication by h^n; its product-dependent inner effects likewise vanish because u is normalized and the units reduce to 1. Direct expansion of transport therefore sends differences (u,v,a) to the same differences (u,v,a), so it acts linearly as the identity on the corresponding P_n. Two choices of gauge differ by a lower automorphism, whose action on the relative classes is trivial by the preceding paragraph. Different choices of lifted gauge also differ only by a top relative gauge. Thus the induced identification is well-defined and P_n-equivariant.

It follows that the true finite fibers, not merely the fibers over literal presentations, are the claimed torsors. Since every representative lifts, all restriction maps are surjective.

## 5. Passing from finite classes to formal classes

There is a map

  rho : S_formal(P) -> inverse_limit_n S_n(P)

by reduction. We prove both directions rather than exchange inverse limit and quotient without justification.

### 5.1 Surjectivity: strictifying the objects

Let ([x_n]) be a compatible system of finite classes. Choose a literal representative x_M=P. Suppose x_n has been chosen. Pick any representative z_(n+1) of the specified next class. Its reduction is equivalent to x_n. Lift the gauge giving this equivalence as in Lemma 2.1 and transport z_(n+1); call the resulting presentation x_(n+1). It represents the same next class and has reduction exactly x_n.

Inductively this produces compatible literal representatives. Lemma 2.2 gives their formal limit. It maps to the chosen system of classes.

### 5.2 Injectivity: strictifying the equivalences

Suppose formal objects x and y have the same finite class at every n. Start with the identity equivalence at n=M. If a compatible equivalence g_n has been selected, there exists some equivalence between x_(n+1) and y_(n+1), because their finite classes are equal. Corollary 3.2 replaces that equivalence by g_(n+1) reducing exactly to g_n.

The resulting compatible gauges have a formal limit by Lemma 2.2. It is an equivalence x -> y, identity modulo h^M. Hence rho is injective.

No arbitrary independently chosen finite isomorphisms were simply presumed compatible. Their discrepancy was a lower automorphism, and the lifted chart 2-unit explicitly corrected it.

### 5.3 The product and the precise absence of a limit obstruction

Choose a torsor origin in every fiber of every map S_(n+1)(P) -> S_n(P). Such choices, with the usual set-theoretic choice convention, recursively identify S_n(P) with the finite product of the P_r for M <= r < n, compatibly with truncation. Taking inverse limits and applying rho gives conclusion (3).

There is no residual nonabelian lim^1 ambiguity for object classes: the proof explicitly constructs compatible gauges, and the finite relative pi_1 groups are trivial. One should not infer this just from nonemptiness of the object fibers. The relevant automorphism and gauge-lifting statements have been established separately.

In particular no canonical product is claimed. Origins may depend on all earlier choices, and changing them can produce a triangular, lower-coordinate-dependent change of coordinates. The parameterization is a filtered-set statement, not an intrinsic affine product or a moduli-functor representability theorem.

## 6. Formal automorphisms and the two 2-unit conventions

### 6.1 Formal pi_1

Let g be an automorphism of a formal object, identity modulo h^M. Build compatible chart units C_n trivializing g modulo h^n. Start with C_M=1. Given C_n, lift it using Lemma 2.1 to the next product. Apply this lifted unit to g at order n+1. Its remaining automorphism is literally identity modulo h^n, so the top-order argument of Lemma 3.1 removes it with a chart unit which itself is identity modulo h^n. Composing this correction with the lifted C_n gives C_(n+1) reducing exactly to C_n.

Lemma 2.2 now gives a formal unit C trivializing g. This proves formal pi_1=0 directly; finite pi_1 vanishing alone was not substituted for the coherence argument.

### 6.2 Formal pi_2

A 2-automorphism of the identity has chart units C_i satisfying

  Ad_i(C_i)=id,
  C_i = F_ij(C_j),
  C_i=1 modulo h^M.

We prove these are precisely the common scalar formal units. Suppose coefficients below degree r have already been shown to be common scalars. Every normalized higher differential coefficient of a unital map annihilates constants, so the order-r coefficient in C_i=F_ij(C_j) gives c_(r,i)=c_(r,j). The coefficient is therefore a global regular function on X. Connected properness gives H^0(X,O_X)=C. The initial induction starts with C_i=1 modulo h^M, so every coefficient is scalar. Conversely every common scalar formal unit satisfies both displayed identities because all maps are C[[h]]-linear and unital and scalar units are central.

The unitary condition for these scalar units is C(-h)C(h)=1. In characteristic zero formal logarithm identifies this with the condition that log(C) is odd in h. Therefore unitary pi_2 is the exponential of the odd powers starting at degree M. Without a unitary condition on 2-units, every scalar unit 1+O(h^M) is allowed, yielding exp(h^M C[[h]]).

At finite levels the same induction proves the truncated scalar formulas. Their restriction maps are surjective: truncate the logarithm and lift it by adding zero later coefficients. Thus the scalar pi_2 tower also has the explicit surjectivity that rules out a would-be lim^1 pi_2 obstruction. The coherent construction in Section 6.1 is independent of invoking any general inverse-limit theorem.

### 6.3 Why the ordinary-2-unit convention changes no object classes

Both conventions have exactly the same objects and exactly the same admissible 1-gauges. Object equivalence is existence of such a gauge, not a choice of its 2-morphism class. The object quotient is therefore identical. Moreover every correction used above was already unitary, so retaining extra admissible ordinary 2-morphisms cannot obstruct any argument or create new object equivalences. It only enlarges pi_2 as just computed; pi_1 remains zero.

## 7. Dimensions and boundaries

Write V=H^0(T_X) and W=H^1(O_X). Geometric inversion acts by -1 on both, and

  P_even = V tensor W,
  P_odd  = Lambda^2 V direct_sum Lambda^2 W.

Their dimensions are g^2 and g(g-1). For g=4 the successive factors are C^16 at even degrees and C^12 at odd degrees, after choosing bases as well as the torsor origins. Starting with a literal two-jet, M=3, the first new factor is the 12-dimensional degree-three factor, then the 16-dimensional degree-four factor, and so on.

The theorem deals with lower automorphisms which are identity on the fixed initial presentation P. If one also allows changes of the initial marking, geometric automorphisms, or arbitrary classical gauge parts, their action on the tower is an additional quotient problem. It has not been silently discarded. The theorem also does not show an arbitrary unrestricted continuation can be brought into reversal form.

All-order here means coefficientwise formal ambient continuation with adjustable higher local products. It is distinct from first-star module deformation, higher-star module deformation, convergence, algebraization, or constructing algebraic cycles. The fixed fifth-product obstruction of PR409 remains valid, as do the independent source-dependent and pure diagonal six-condition boundaries. No selected HM/source function, module, matrix, detector, jet, or model computation is performed.

