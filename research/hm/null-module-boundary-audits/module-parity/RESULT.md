# Diagonal inversion: the precise module consequence and its limit

## Result

The new ambient lifting lemma proves an invariant formal ambient algebroid extension of the supplied two-jet, allowing higher product, overlap-map, and triple-unit coefficients to vary. It does not prove an invariant formal module extension. Its symmetry argument has a genuine but strictly smaller module consequence:

**Conditional module statement.** If the classical object has a coherent inversion linearization, the ambient data and already constructed module truncation are inversion-equivariant, and the usual module small-extension obstruction theory is available equivariantly, then the next module obstruction belongs to Ext²(E,E)^+. If this class vanishes, an equivariant correction exists. Consequently Ext²(E,E)^+=0 would suffice to lift every such truncation over a fixed invariant ambient extension. Ambient HH³(X)^+=0 does not imply this sufficient hypothesis, nor does it imply vanishing of the actual module obstruction.

The full deck-sign character F={1,2,3,4} restricts to **+1**, not −1, on diagonal inversion. The full-sign 352-dimensional Ext² block therefore survives this restriction in its entirety. A further previously certified D8-epsilon reduction 32→30 is not improved by diagonal inversion when that block lies inside full sign. No actual obstruction coordinate is determined here.

Under the supplied Ext¹ deck-weight dimensions (79,2,0,0,0), invariant first-order module variations have dimension 79, rather than 81. This is a reduction of the equivariant search space, not a vanishing theorem or a proof that all unrestricted module solutions can be made equivariant simultaneously at all orders.

## 1. Hypotheses that must be kept separate

Work over a characteristic-zero field, with inversion iota fixing h. Write G=(Z/2)^4 for the deck group and iota for the product of its generators.

1. **Classical linearization.** An isomorphism iota*E ≅ E is not by itself a specified action. One needs an isomorphism lambda compatible with iota²=1, namely lambda composed with iota*lambda equals id, with the relevant descent coherence. For a G-action one needs all group multiplication coherences. Only then is the induced action on RHom(E,E), its Ext groups, and characteristic evaluation well defined in the intended equivariant problem. The supplied source asserts a natural deck linearization; the following conclusions accept it as input, rather than verify actual matrices. In a complex model, use an equivariant model or compatible coherent action/strictification; arbitrary chosen contractions need not be equivariant.

2. **Equivariant ambient input.** The new one-parameter lemma supplies an iota-invariant ambient family. The complementary, independently audited [RESULT.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/9e3d8dc8525a7d11ae919dfac2126794c9bdc366/research/hm/null-literal-ambient-extension/two-parameter/RESULT.md) now additionally constructs a full G-equivariant ambient family over k[[s,t]], with s of character P={1,2} and t of character Q={3,4}, whose diagonal two-jet is literally the supplied one. This is semilinear equivariance on the base; it is not full G-invariance with h fixed, since the first-order P and Q directions are not G-invariant. An arbitrarily chosen one-parameter all-order ambient extension need not be a diagonal slice of this constructed family.

3. **A first-order module lift.** Ambient existence alone does not give this. Its obstruction is the characteristic value ev_E(xi) in Ext²(E,E), with the gerbe contribution and conventions included. In the supplied row-module source, it is ev_E(pi)−b id; the prescribed b=−15 Pi cancels it if the asserted evaluation ev_E(pi)=−15 Pi id holds. Accepting that identity establishes abstract first-order solvability in the stated obstruction theory. An explicitly verified finite-model first-order solution and comparison are a separate certificate, not produced here.

4. **Equivariance of a first-order lift.** Once the linearized classical object and invariant first-order ambient data are fixed, the equation is d u = −C1 with C1 invariant. If it has any solution, u+ = (u+iota u)/2 is an invariant solution. This is averaging a linear first-order correction. Up to the usual first-order module gauge, the solution set is an affine torsor under Ext¹(E,E); its equivariant part is a torsor under Ext¹(E,E)^+. For finite groups in characteristic zero, exact invariants ensure that equivariant cohomology here equals the invariant part of ordinary cohomology. This does not average a nonlinear full formal module.

5. **Higher truncations.** To invoke invariant obstruction theory at order n+1, an equivariant module must already have been constructed through order n. If a particular prescribed truncation is not equivariant, the argument does not preserve it literally. If an invariant next-step obstruction vanishes ordinarily, averaging a correcting cochain gives an invariant correction retaining the lower truncation. If it does not vanish, averaging does nothing to remove it.

Thus the new ambient theorem plus accepted first-order cancellation allows one to pose an invariant module extension problem. It does not solve its order-two obstruction.

## 2. Proof of the conditional module statement

Let M be the classical module deformation complex, with H^j(M)=Ext^j(E,E). For a small extension R'→R with kernel I killed by the maximal ideal, fix an invariant ambient lift and an invariant module over R. Choose invariant coefficientwise module lifts; such choices exist by linear averaging. Their equation defect is a cocycle o in M² tensor I. Naturality of the equations implies iota(o)=o. Changing the chosen module lift by v in M¹ tensor I changes o by d v (up to a globally consistent sign convention). Thus the obstruction is [o] in Ext²(E,E)^+ tensor I. It vanishes exactly when a module lift exists in the stated deformation category. If d v=−o is solvable, averaging gives d(v+)=−o, hence an equivariant lift.

The complementary [RESULT.md](../module-lifting/RESULT.md) now proves this fixed-ambient module obstruction statement directly for row-represented locally free modules on an appropriate acyclic trivializing cover: its normalized defect C is a Čech End(E) 2-cocycle and changing transitions by g x changes C by δx. Thus in that explicit setting one need not leave the module obstruction assertion as an unproved formalism hypothesis. The acyclic-cover/cohomology comparison and compatible equivariant structure must still be available. At infinitesimal small-extension order the differential is the classical one because the maximal ideal annihilates I. No formula depending on actual transition matrices was evaluated here.

## 3. The joint deformation homotopy fiber and its exact sequence

Here shifts are essential. Let A denote the ambient deformation tangent complex normalized so that

H¹(A)=HH²(X),   H²(A)=HH³(X).

Let M denote RHom(E,E) in the module normalization above. In an appropriate algebra/object deformation theory, let P be the joint algebra-plus-object deformation tangent complex. Forgetting the object gives a homotopy fiber sequence of tangent complexes

M → P → A → M[1].

Equivalently, P is the homotopy fiber **as a complex** of the characteristic map c:A→M[1]. The connecting map H¹(A)→H²(M) is characteristic evaluation ev_E. Do not identify this linear fiber description with an assertion that all nonlinear joint deformations are determined by this linear map alone. Brackets and higher operations remain necessary.

The relevant long exact sequence is

HH¹(X) → Ext¹(E,E) → H¹(P) → HH²(X)
  →[ev_E] Ext²(E,E) → H²(P) → HH³(X) → Ext³(E,E).

For an equivariant model, taking finite-group invariants is exact, so the same sequence holds with + superscripts. If HH³(X)^+=0, exactness gives the canonical isomorphism

H²(P)^+ ≅ coker( HH²(X)^+ →[ev_E] Ext²(E,E)^+ ).

Thus ambient invariant unobstructedness leaves the invariant module obstruction quotient. The fixed-ambient obstruction lives in Ext² itself; allowing next-order ambient changes quotients by the characteristic image. These are distinct existence problems.

Concretely, fix a joint lower-order solution and some invariant next-order ambient extension. Its module obstruction o changes by ev_E(eta) when the ambient next coefficient is varied by the cocycle eta. Therefore its class modulo im(ev_E) is the obstruction to finding some compatible joint extension at that step. It vanishes if and only if one can choose an ambient change whose module obstruction is zero, within the stipulated deformation theory and allowed ambient variations. If the ambient coefficient is frozen, this quotient does not apply.

This tangent-complex argument is conditional on an actual joint deformation theory/comparison. The literal ambient lemma alone does not construct P or certify its identification with a supplied finite RHom model. Independently of constructing P, the direct module-lifting artifact proves the same stepwise cokernel criterion by the explicit formula C_new=C_old+κ_g(eta)+δx and κ_g(d(t,s))=δz. Thus the practical cokernel conclusion in its locally free acyclic-cover setting does not depend on an unproved nonlinear homotopy-fiber comparison.

## 4. What deck weights do and do not remove

For a deck character S, chi_S(iota)=(-1)^|S|. Consequently all even-weight components (weights 0,2,4) survive iota invariants. The supplied ambient HKR computation says HH³ is odd and HH² has only deck weights 0,2. Hence:

- HH³^+=0 kills ambient lifting obstructions.
- Ext²_F is entirely invariant; its supplied dimension 352 is unchanged.
- A G-equivariant classical characteristic map has no image in Ext²_F, since its HH² domain has no F character.
- Therefore Ext²_F injects into H²(P), by the exact sequence, and its 352-dimensional image lies in H²(P)^+. This is a statement about an obstruction space, not a claim that a nonzero obstruction is attained by the actual family.
- If the 30-dimensional remaining D8-epsilon target is a subspace of Ext²_F as supplied, inversion is identity on it. No 30→0 inference follows.
- Ext¹^+ has dimension 79 and Ext¹^− dimension 2 under the supplied certificate. Removing the odd first-order variations may simplify an equivariant search. The already reviewed full-sign second-order independence from all first-order variations means this simplification cannot change the full-sign order-two class.

Full G-equivariance of the classical evaluation map is sufficient for the no-F-image assertion; it is not necessary that the chosen one-parameter ambient family be G-invariant. At each higher small-extension step with lower-order data held fixed, next-coefficient ambient changes likewise cannot change a full-sign obstruction through the classical characteristic map. This local-in-order statement does NOT make higher obstructions independent of earlier ambient choices, which can interact nonlinearly.

Also, iota fixes h, so it forces even **deck weights**, not even **h-orders**. The separate reviewed two-parameter selection theorem gives full-sign terms st B(s²,t²) under its stronger G-equivariant two-parameter hypotheses. The new two-parameter ambient artifact now supplies the ambient-family existence part of those hypotheses. For each available G-equivariant module truncation and equivariant defect construction over that family, full-sign defect coefficients therefore obey this selection rule. An all-order module is still not supplied: an obstruction can prevent continuation, and no parity argument makes an allowed full-sign coefficient zero. Diagonal inversion alone cannot rule out full-sign terms at odd powers of h.

There is a useful first-order strengthening, conditional on the accepted first-order characteristic cancellation and classical G-linearization. Write xi=xi_P+xi_Q. Since κ_E is G-equivariant and P,Q are distinct characters, κ_E(xi)=0 implies κ_E(xi_P)=κ_E(xi_Q)=0 separately. Choose first-order primitives in the respective character subcomplexes by projection. Multiplying them by s and t gives a G-equivariant module lift over k[s,t]/(s,t)². Passing it through total degree two still requires vanishing of its module obstruction; that is precisely where the full-sign st coefficient is allowed and remains unknown.

## 5. A fully explicit synthetic counterexample

The following abstract DGLA extension is invented universal algebra, not a geometric model, source evaluation, or computation of the actual bundle.

Let A be an abelian DGLA concentrated in degree 1, with basis x,y of characters P,Q. Thus H²(A)=0, every formal ambient series is Maurer–Cartan, and iota acts trivially on A.

Let K have zero differential and zero bracket, with

K¹ = k^79 of character 0, direct sum k² of one chosen singleton character;
K² = k^352 of character F;
K^j = 0 otherwise.

Choose nonzero w in K². Let L=A direct sum K as graded vector spaces, with d=0 and the sole nonzero brackets

[x,y]=[y,x]=w.

All brackets with K are zero. Symmetry on degree-one arguments is exactly graded skew-symmetry. Every nested bracket vanishes, so Jacobi holds. Character compatibility holds since P times Q = F. Projection L→A is a surjective DGLA morphism with central kernel K. This is an abstract joint deformation problem, with kernel the module-direction deformation complex. At the tangent level the characteristic connecting map is zero, and K→L→A gives precisely the fiber triangle above. The nonzero bracket is additional nonlinear information.

Consider the invariant formal ambient deformation a(h)=h(x+y). It lifts to L modulo h²: the Maurer–Cartan equation has no first-order term. Any first-order lift with the same ambient direction is h(x+y+u), u in K¹. Every possible extension adds terms in h² L¹ and higher. Its curvature at order h² is

(1/2)[h(x+y+u),h(x+y+u)] = h² w,

because K is central. No h² correction changes this coefficient, since d=0. The nonzero class w obstructs extension modulo h³. It has full-sign character and is iota invariant. This remains true for all first-order module variations, equivariant or otherwise, and all second-order ambient accelerations.

The example simultaneously has:

- unobstructed invariant ambient deformation and H²(A)^+=0;
- an invariant first-order joint lift;
- the supplied Ext¹ weight dimensions (79,2,0,0,0) in the abstract module complex;
- a 352-dimensional invariant full-sign degree-two module obstruction space;
- a nonzero second-order invariant module obstruction.

It refutes any universal inference from the first four properties to module extendability. It does not assert that this DGLA is realized by the actual geometric object. Conversely, replacing the bracket [x,y] by zero preserves every listed vector-space and character dimension and makes the displayed joint deformation extend to all orders. Therefore those static dimensions and diagonal parity alone determine neither vanishing nor nonvanishing of the actual obstruction.

## 6. Exact remaining claim for the actual problem

Accepting the supplied linearization and first-order characteristic cancellation, one can choose an inversion-equivariant first-order module lift and study its next obstruction in Ext²(E,E)^+. The ambient theorem removes the ambient existence gap for a flexible invariant all-order presentation. It supplies no value of that module obstruction, and no extra elimination of the full-sign or its stated D8-epsilon remainder. Establishing a module lift still requires either a valid separate module vanishing/existence theorem with its hypotheses verified, or an exact obstruction/solution certificate. No such certificate is supplied here.

### Inputs read; scope of verification

- [LEMMA.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/9e3d8dc8525a7d11ae919dfac2126794c9bdc366/research/hm/null-literal-ambient-extension/descent/LEMMA.md): checked ambient extension and its explicit limitation to ambient descent.
- [review.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/03f681c944e6997b14117aad06dd562c408c63c8/research/hm/null-ordinary-character-audits/characters/review.md): conditional weight support, two-parameter selection, and limits of higher-order independence.
- https://github.com/Akilleez-QA/read-em-and-weep/blob/c8aec970fd65a105f39f4e8aeb8a17f0f0053f89/research/hm/second-order-algebroid.md: formal module equations, first-order sign, asserted deck linearization, characteristic comparison and missing computational certificate.
- Supplied task facts: Ext¹ weight totals (79,2,0,0,0), full-sign Ext² dimension 352, D8-epsilon reduction 32→30 unknown.

All proofs above are abstract linear algebra, exact-sequence reasoning, or a synthetic DGLA construction. No actual matrix products, source values, model/owner/jet evaluations, production imports, geometric experiments were performed. No external posting was performed.

## 7. Independent audit of the complementary proofs

The two-parameter ambient artifact was reviewed without actual evaluations. The split data have the claimed characters. Commutation of the four derivations gives the mixed star coefficient m₀ DP DQ/4. Expanding Ad(1+β+β²/2) through degree two gives s²{bP,-}_P+t²{bQ,-}_Q because the two cross Hamiltonians vanish by factor separation; thus F_st=0 and F=id+s²TP+t²TQ are justified. The scalar mixed triple-unit coefficient is bP bQ. In the pentagon, normalized star corrections involving two positive-degree unit terms begin at degree three, so ordinary scalar exponentiation proves every quadratic coefficient, including st. These are independent mixed-coefficient checks, not inference from diagonal specialization.

The multivariate extension uses m I_N=I_N²=0, exactly the small-extension hypotheses of the checked ambient lemma. All I_N characters lie in {0,P,Q,F}, whereas ambient HH³ has only odd-weight characters. Hence (HH³ tensor I_N)^G=0, and exact invariants provide a primitive which can be averaged under all of G. Literal compatible induction produces the claimed ambient two-parameter family. No gap was found, subject to the stated ambient HKR, cover, and static scalar-input hypotheses.

The direct module artifact was also audited: expanding F_ij(F_jk(G_kl) star G_jk) star G_ij in the two orders gives exactly its four-index defect identity, with no unjustified centrality of A. Multiplication by g_il^{-1} gives the negative of the standard Čech cocycle expression, hence δC=0. Its ambient variation κ_g has the correct minus arity-zero term. For eta=d(t,s), cancellation of t_i(g_jk) terms leaves the Čech differential of z_ij=g_ij^{-1}(t_i(g_ij)−s_ij g_ij), proving κ_g(d(t,s))=δz with the asserted sign. This supplies a direct cochain proof of the stepwise characteristic-cokernel criterion. Its restriction to acyclic trivializing covers and actual allowed ambient corrections is necessary and correctly stated.

These complementary results remove the previously missing ambient two-parameter existence premise and provide the direct module small-extension formulas. They do not compute any of the 30 retained obstruction values, prove a module two-jet, or prove an all-order equivariant module.
