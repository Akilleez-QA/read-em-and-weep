# Formal forgetful injectivity and finite detection of reversal compatibility

## 0. Result

Retain the regular invariant differential ambient category, connected complex abelian variety X with geometric inversion, individually invariant affine acyclic cover, and fixed literal reversal-compatible presentation P modulo h^M, M >= 3, of the marked formal tower theorem. Higher local products, maps, and units may all vary.

There are two marked continuation categories:

- R: reversal-compatible products, even overlap maps, reversal-unitary triple units, even chart gauges, and reversal-unitary edge units.
- U: invariant differential ambient presentations and gauges without reversal restrictions.

All objects reduce literally to P; all 1-gauges are identity modulo h^M. Use unitary inner chart 2-units in R and arbitrary inner chart 2-units in U, also identity modulo h^M. Allowing ordinary chart 2-units in R would not change any object-class statement.

Let R_n, U_n denote object-class sets modulo h^n, and let R_infty, U_infty denote the coefficientwise formal class sets. The forgetful maps are J_n and J_infty.

The following are proved:

1. Every J_n is injective, including at orders beyond the single top step.
2. J_infty is injective: an unrestricted invariant marked equivalence between two reversal-compatible formal presentations can be replaced by a reversal-compatible one.
3. A class in U_infty lies in the image of J_infty if and only if its reduction lies in the image of J_n for every finite n. Thus there is no additional purely infinite-order normalization obstruction after all finite orders are normalizable. No uniform detection-order bound is supplied.
4. On a fourfold, J_infty is not surjective. For every M >= 3 there are unrestricted invariant formal continuations of P not equivalent, under gauges identity on P, to any reversal-compatible continuation. Such examples are constructed by choosing a nonzero complementary one-step class at the first new degree and continuing it using the unrestricted literal lifting input.

Injectivity is an object-class statement, not full faithfulness of 2-groupoids: the two choices of chart 2-units have different scalar pi_2. No canonical coordinates, moduli functor, formality theorem, prescribed-product continuation, module quantization, or algebraicity result is asserted.

## 1. Exact inputs and notation

The preceding marked theorem is [PR436](https://github.com/Akilleez-QA/read-em-and-weep/pull/436), exact commit `502c978a17cd7037d740d4d08d373c1cb8bd5829`, [PROOF.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/502c978a17cd7037d740d4d08d373c1cb8bd5829/research/hm/formal-parity-tower/PROOF.md). Its finite torsors and formal inverse-limit comparison concern R. The present proof supplies the additional comparison with U; it does not infer that comparison from the existence of noncanonical product coordinates.

The one-step comparison is [PR425](https://github.com/Akilleez-QA/read-em-and-weep/pull/425), commit `df433cdd359fa9c7750bf9c8b9765229eac534f6`, [PROOF.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/df433cdd359fa9c7750bf9c8b9765229eac534f6/research/hm/reversal-relative-lift-freedom/PROOF.md), Sections 2, 3, 5, and 6.

Nonemptiness and continuation retain:

- [PR416](https://github.com/Akilleez-QA/read-em-and-weep/blob/c71356722bc7bd1a426d26ea0ca6d050f4c3ed81/research/hm/parity-separated-ambient-lifting/REVERSAL-COMPATIBLE-CONTINUATION.md), commit `c71356722bc7bd1a426d26ea0ca6d050f4c3ed81`, for reversal-compatible literal continuation.
- The [unrestricted invariant literal small-extension proof](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6259748725), for continuation of a specified unrestricted finite presentation, with all three new coefficient types allowed to vary. Its explicit application is the stipulated elliptic fourfold; the general abelian formulation retains the same literal lifting premise, as PR416 does.

No weaker claim of existence of a deformation of some equivalent lower object is substituted for either literal premise.

All cochains are strictly invariant and regular; positive arities are normalized. The cover computes the required coherent cohomology. Each formal differential coefficient has finite order, without a uniform order bound. Put A_n=C[h]/(h^n). The top layer for A_(n+1) -> A_n is epsilon=h^n, with epsilon^2=h epsilon=0.

At that layer, writing differences between objects as (u,v,a), the equations are

  bu=0,  delta u=bv,  delta v=0,  delta a=0.

An unrestricted top gauge E=id+epsilon t, B=1+epsilon c acts by

  (u,v,a) -> (u+bt, v+delta t, a+delta c).

An arbitrary top chart 2-unit C=1+epsilon s fixes t and sends c to c-delta s. These are direct expansions of the transport and inner 2-morphism formulas of PR425. In particular they hold at every top order, regardless of parity of the lower U-object.

## 2. The unrestricted lower-automorphism calculation

### Lemma 2.1. Finite unrestricted automorphisms are 2-trivial

Every invariant automorphism of a U-object over A_n whose gauge data are identity modulo h^M is 2-isomorphic to the identity using an invariant ordinary chart unit which is identity modulo h^M.

Proof. First compute a literal top automorphism. Its equations are

  bt=0,  delta t=0,  delta c=0.

Thus t is an invariant global vector field. Inversion acts as -1 on H^0(T_X), so t=0. The invariant class of c in H^1(O_X) is also zero, since inversion acts as -1 there. Choose an invariant scalar Cech zero-cochain s with delta s=c. The chart unit 1+epsilon s is an allowed ordinary 2-unit at every parity and removes c.

For a full automorphism, proceed inductively from n=M. A chart unit trivializing its reduction lifts freely to the next product: retain its coefficients, add any invariant next coefficient, and use the fact that constant term 1 makes it invertible. Its endpoint-preserving 2-morphism changes the upper automorphism to one literally identity at the lower order. The top calculation then removes the remainder. Both operations preserve the identity marking on P. QED.

This is vanishing of the full finite unrestricted relative pi_1, not merely of its associated graded. The proof allows arbitrary lower products in U and uses no reversal.

### Lemma 2.2. Specifying the lower part of an existing upper equivalence

Suppose two U-objects over A_(n+1) are equivalent, and prescribe any equivalence g between their reductions. Then an equivalence of the higher objects exists whose reduction is exactly g.

Proof. Choose some higher equivalence q. Its reduction and g differ by a lower automorphism. Lemma 2.1 gives a chart-unit 2-isomorphism from q_bar to g. Lift that chart unit in the higher source algebra, and apply

  E_i^new=Ad_i(C_i)E_i,
  B_ij^new=C_i *_i B_ij *_i F_ij(C_j^(-1)).

Both endpoints are unchanged, and the new reduction is g. QED.

This does not assert that an arbitrary prescribed lower equivalence lifts between arbitrary higher endpoints. Existence of some higher equivalence q is an explicit premise.

## 3. Finite forgetful injectivity

### Lemma 3.1. The top replacement

Two reversal-compatible lifts of the same literal lower reversal-compatible presentation, equivalent by an unrestricted top gauge, are equivalent by a reversal-compatible top gauge.

Proof. At even n, reversal forces the top triple-unit difference to vanish. Drop c from the unrestricted gauge and retain t. The endpoint products and maps depend only on t, and the scalar endpoint remains unchanged. This is an admissible even chart gauge with trivial edge unit.

At odd n, the top product difference is alternating, while bt is symmetric in its two inputs for every linear t on a commutative classical algebra. Thus if their difference equals bt, both vanish. The top overlap difference is zero as well, so delta t=0. Dropping t while retaining c preserves both endpoints. At odd n, 1+epsilon c is reversal-unitary. This gives the required gauge. QED.

This repeats the precise PR425 one-step injection, not a general normalization of arbitrary objects.

### Theorem 3.2. J_n is injective for every n

Proof by induction on n. At n=M there is only the fixed object P. Suppose J_n is injective, and x,y are R-objects over A_(n+1) joined by an unrestricted gauge q.

Their reductions are unrestricted equivalent, so by induction choose a reversal-compatible lower gauge g between them. Lemma 2.2 replaces q by an unrestricted upper gauge with exact reduction g.

Lift the admissible coordinate data of g by PR436 Lemma 2.1: even unital chart maps lift coefficientwise, and the norm-defect correction lifts unitary edge units. Transport x by this lift; call the target z and the gauge p. Then z is reversal-compatible, and its reduction is literally y modulo h^n.

The composition from z through x to y, using p^(-1) and the adjusted q, reduces exactly to the identity. It is therefore an unrestricted top gauge between the two reversal-compatible lifts z and y of the same literal lower object. Lemma 3.1 replaces it by a reversal-compatible top gauge. Composing with p gives a reversal-compatible gauge x -> y.

All gauges remain identity modulo h^M. This proves injectivity at n+1. QED.

The use of Lemma 2.2 is indispensable. One-step injectivity alone does not permit discarding unrestricted lower gauge coefficients independently at every order.

## 4. The formal comparison and finite detection

### Lemma 4.1. U_infty -> inverse_limit U_n is a bijection

The proof is the unrestricted version of the constructive argument in PR436, and is given here to specify the additional premise used for the image criterion.

For surjectivity, choose a representative of the first finite class. Given a chosen representative at order n and any representative of the next class, their reductions are equivalent. Lift that equivalence as unrestricted coordinate data and transport the latter representative so its reduction is literally the former. Unrestricted chart maps and units lift freely because their classical terms are id and 1. The target of transport is determined, not preselected. This produces compatible literal presentations.

For injectivity, suppose two formal objects have equal finite classes. Inductively choose upper equivalences with exactly the already specified lower equivalence by Lemma 2.2. Their coefficientwise limit is a formal equivalence.

The coefficientwise limits of both objects and gauges exist because every coefficient identity contains only finitely many lower terms. Differential regularity and finite order at each coefficient are preserved under those finite operations. No uniform order bound or analytic convergence is used. Thus the map is a bijection.

### Theorem 4.2. Formal injectivity

If x,y in R_infty have equal classes in U_infty, each pair of reductions is U-equivalent. Theorem 3.2 makes them R-equivalent at every finite order. The injective inverse-limit comparison of PR436 then makes x and y R-equivalent formally. Hence J_infty is injective.

Equivalently, one can keep the finite parity gauges compatible using the same construction and then pass to the limit. The conclusion is existence of a parity equivalence, not that the initially supplied unrestricted gauge already has parity.

### Theorem 4.3. Finite detection of membership in the image

A class u in U_infty belongs to the image of J_infty if and only if its class u_n lies in the image of J_n for every n.

Proof. The forward implication is reduction. Conversely, select r_n in R_n with J_n(r_n)=u_n. By injectivity of J_n, the reduction of r_(n+1) equals r_n: both map to u_n. Thus (r_n) is a compatible system of R-classes. The surjective inverse-limit comparison of PR436 gives r in R_infty realizing it. The images J_infty(r) and u have equal finite classes, so Lemma 4.1 makes them equal in U_infty. QED.

This proves the absence of a purely infinite-order gap for the specified marked normalization problem. It does not provide a numerical bound for the first failing order. It also does not claim that all finite classes are normalizable.

## 5. Properness of the formal image on the fourfold

For a fixed literal lower reversal-compatible presentation, choose a reversal-compatible one-step lift as origin, using PR416. The unrestricted one-step torsor has translation space

  H = H^0(Lambda^2 T_X)^iota
      direct_sum H^1(T_X)^iota
      direct_sum H^2(O_X)^iota.

The image of the reversal-compatible lift torsor has translation subspace

  P_n = H^1(T_X)^iota                              at even n,
  P_n = H^0(Lambda^2 T_X)^iota + H^2(O_X)^iota      at odd n.

Its complementary subspace is therefore

  Q_n = H^0(Lambda^2 T_X)^iota + H^2(O_X)^iota      at even n,
  Q_n = H^1(T_X)^iota                              at odd n.

The splitting is the indicated coherent-cohomology decomposition; origins are still not canonical. In dimension four the complements have dimensions 12 at even n and 16 at odd n, so are nonzero at either parity.

Fix the first new order n=M and choose a nonzero class q in Q_M. It is realized by actual normalized cochains satisfying the top difference equations:

- If M is odd, choose an invariant derivation-valued Cech 1-cocycle v representing a nonzero H^1(T_X) class and add h^M v to the overlap maps, with u=a=0.
- If M is even, one may choose a nonzero invariant global bivector u and add h^M u to the local products, with v=a=0. Alternatively, an invariant scalar Cech 2-cocycle gives the H^2(O_X) part.

The equations bu=0, delta u=bv, delta v=0, delta a=0 verify the resulting presentation literally modulo h^(M+1). It is unrestricted and inversion-invariant. Its class is outside the image of J_(M+1), since its difference from the chosen parity origin is q not in P_M.

Now use the unrestricted invariant literal lifting input to extend this chosen presentation successively, preserving every preceding coefficient. The compatible limit is an unrestricted formal continuation of P. If it were equivalent to a reversal-compatible formal continuation by a gauge identity modulo h^M, reduction modulo h^(M+1) would put the chosen finite class in the image of J_(M+1), a contradiction.

Thus J_infty is not surjective. This is a universal cohomological construction, not an evaluation of a selected source presentation. In dimension g>=2 both complementary spaces are nonzero. In dimension g=1 the even-degree complement is zero but the odd-degree complement is nonzero; a later odd degree supplies the analogous example when the first new degree is even.

## 6. Contribution and limits

PR425 proved injectivity for gauges literally identity below one new degree. The present argument proves injectivity for full formal continuations with a fixed initial marking, including gauges having many nonzero intermediate coefficients. The missing steps are unrestricted lower-automorphism 2-triviality, exact lower-gauge alignment, and formal coherence.

The image criterion additionally rules out an obstruction appearing only at the infinite limit after every finite order is normalizable. The proper-image construction proves that a blanket formal parity-normalization theorem is false in this marked category, even though PR416 supplies many parity continuations.

Neither result concerns gauges changing the initial marking, geometric or discrete automorphisms, non-invariant equivalences, immutable local products, modules, periods, convergence, algebraization, or algebraic cycles. First-star and higher-star module problems remain separate. The pure diagonal six conditions and actual-source obstructions are not evaluated. No selected HM/source function, module, matrix, detector, jet, or model computation is performed.

