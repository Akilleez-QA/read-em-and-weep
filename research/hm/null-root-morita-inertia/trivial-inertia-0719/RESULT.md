# Trivial inertia gives effective free-module descent: a local algebra theorem

## Result and scope

Let D be a unital, possibly noncommutative local ring, with Jacobson radical m and residue field D/m=k of characteristic zero. Let a finite group G act genuinely by unital ring automorphisms, and suppose its action on k is the identity. Let M be a finite free left D-module with a genuine semilinear G-action. If G acts trivially on M/mM, then M has a G-invariant D-basis. Consequently, with A=D^G:

- M^G is finite free over A;
- the canonical map D⊗_A M^G → M is an equivariant isomorphism;
- for every G-stable two-sided ideal I of D, invariant formation commutes with the corresponding coefficient reduction in the precise form

      M^G / (I∩A)M^G  ≅  (M/IM)^G,
      A/(I∩A)         ≅  (D/I)^G.

These statements require neither flatness of D as a right A-module nor commutativity. Completeness is useful for interpreting formal deformation objects but is not needed for the algebraic proof. The theorem is local and does not construct a global descent or a root-twisted Morita equivalence.

## 1. Exact hypotheses

Here “local” means that m=Jac(D) is a two-sided ideal and D/m is the stated field; equivalently, in this setting, elements outside m are units. We use ordinary finite free left modules. The action satisfies

      g(dm)=g(d)g(m),
      g(h(m))=(gh)(m),

and is not merely projective or defined up to inner automorphisms. All ring automorphisms preserve m. The hypothesis on the residue action means identity on the entire residue field k, not just on a smaller field of definition.

More generally, characteristic zero can be replaced by invertibility of |G| in k. Indeed the central element |G|·1_D then lies outside m, so is invertible in D; its inverse is central and G-fixed. Thus the Reynolds operator

      R(v)=|G|^(-1) Σ_(g∈G) g(v)

is well-defined on the additive groups of the rings and modules in question. It preserves stable submodules and ideals. No embedded coefficient field k⊂D is needed.

If D is given as a complete local deformation ring, assume it is separated and complete for the specified multiplicative adic filtration and that all actions and module maps under discussion are continuous. For the m-adic topology, continuity of automorphisms is automatic. The algebraic conclusion remains valid without these topological assumptions; topological conclusions require them.

## 2. Averaging lifts and noncommutative Nakayama

Write r=rank_D M. Choose a k-basis w_1,…,w_r of M/mM and arbitrary lifts v_i∈M. Define e_i=R(v_i). Each e_i is G-invariant. Since every w_i is fixed by G, reduction modulo m gives e_i mod mM=w_i.

Consider the left D-linear map

      f:D^r → M,      (d_i) ↦ Σ_i d_i e_i.

Its reduction modulo m is an isomorphism. The cokernel is finitely generated, and its reduction is zero. Noncommutative Nakayama therefore gives surjectivity of f. As M is free, this surjection splits as a left D-module map, giving

      D^r ≅ ker(f) ⊕ M.

The kernel is a finitely generated direct summand of D^r. Reducing this split decomposition modulo m and using that the reduction of f is an isomorphism gives ker(f)/m ker(f)=0. A second application of Nakayama gives ker(f)=0. Thus the e_i form a D-basis.

This proof uses no determinants, no commutative presentation, and no adic approximation. It also avoids a potentially unjustified application of Nakayama to a kernel before proving that the kernel is finitely generated.

## 3. Invariants and local structure of A

Uniqueness of coefficients in the invariant basis gives

      Σ_i d_i e_i ∈ M^G  ⇔  d_i∈A for every i.

Hence M^G=⊕_i A e_i. The canonical map

      ε_M:D⊗_A M^G → M,      d⊗p ↦ dp,

sends a free basis to the invariant basis, so is an isomorphism. Tensoring here uses D as a right A-module and M^G as a left A-module; no centrality of A is being asserted.

The ring A is itself local. Put a=A∩m. If a_0∈A is outside m, its inverse in D is G-fixed, so belongs to A. Elements of a cannot be units of A. Thus a is its unique maximal ideal. Moreover A→k is surjective: lift any residue scalar to D and average it, which leaves its residue unchanged. Therefore A/a=k.

## 4. Coefficient reduction, including nilpotent and mixed ideals

Let I⊂D be a G-stable two-sided ideal and put J=I∩A=I^G. Averaging a lift of an invariant element of D/I proves that A→(D/I)^G is surjective, with kernel J. In particular

      A/J ≅ (D/I)^G.

The invariant basis also gives

      IM=⊕_i I e_i,
      (IM)^G=⊕_i J e_i=J M^G,
      M/IM=⊕_i (D/I) e_i.

Taking invariants in the last expression yields the asserted canonical isomorphism

      M^G/JM^G → (M/IM)^G.

This is stronger than exactness of invariants alone: it identifies the invariant upstairs reduction kernel with the image of the invariant ideal acting on M^G. It is precisely this equality that fails for the sign-character module in the ramified counterexample.

The argument applies to every stable two-sided ideal, not just a first-order ideal. Thus it includes higher truncations and mixed coefficient ideals whenever they are actually stable. It does not replace J by an ideal guessed from a characteristic class, an associated graded piece, or a normalized trace. Nor does it identify invariants of products of ideals with products of their invariant parts. The ideal in the formula is always the actual intersection I∩A.

## 5. Exact equivalence on the stated free categories

Let Free(A) be the category of finite free left A-modules and A-linear maps. Let Free_G^0(D) be the category of finite free left D-modules with genuine semilinear G-action whose action on the closed fiber M/mM is trivial, with equivariant D-linear maps.

Define

      F(P)=D⊗_A P,       g(d⊗p)=g(d)⊗p,
      H(M)=M^G.

Since P is free, F(P) is free over D. Its residue fiber is k⊗_A P, and G acts trivially because it acts identically on k. Thus F lands in Free_G^0(D). Section 3 shows that H lands in Free(A).

The ordinary tensor–invariants adjunction has unit and counit

      η_P:P → (D⊗_A P)^G,       p ↦ 1⊗p,
      ε_M:D⊗_A M^G → M,        d⊗p ↦ dp.

After choosing any A-basis of P, its tensor basis is invariant, and coefficientwise invariants identify η_P with the identity on a free A-module. Hence η_P is an isomorphism. Section 3 proves ε_M is an isomorphism for every M in Free_G^0(D). These are the natural adjunction maps; their invertibility proves a categorical equivalence, including full faithfulness, not merely an objectwise classification.

Flatness of D over A is not needed: we tensor only free modules in this proof, and the counit is verified on actual bases. No assertion follows about equivalence of all modules, exactness on arbitrary A-modules, derived descent, or faithful flatness.

There is also an exact effectiveness criterion in this local setting. A finite free equivariant M is the pullback of a finite free A-module, with its canonical semilinear action, if and only if its closed-fiber action is trivial. Necessity follows by reducing such a pullback modulo m; sufficiency is the theorem. This is not a criterion for freeness of M^G alone. For example, over the reduced sign cover D=k[[u]], G=Z/2 with u↦−u and e↦−e, M^G=k[[u²]]·(ue) is free, but the canonical map back to De has image uDe and is not an isomorphism.

## 6. Deformation parameters, topology, and flatness

A standard sufficient deformation setting is a complete local commutative ring B with residue k, a commutative Artinian parameter ring T with nilpotent augmentation ideal q, and an associative unital T-algebra D with central image of T, together with a nilpotent ideal qD such that D/qD≅B. If B is local and qD is nilpotent, D is local: units lift across nilpotent ideals, and the inverse image of the maximal ideal of B is Jac(D). A finite-order differential deformation with these properties is therefore within the theorem.

The group may fix T pointwise, or act compatibly on T, provided the resulting action on D is genuine and the coefficient ideal used for reduction is G-stable. Central parameters need not be G-fixed: a parameter may transform by a character. A parameter setting, specialization, or individual ideal that is not preserved by G does not carry the induced quotient action needed above. When T is pointwise fixed and I is the ideal generated by a collection of its parameters, averaging also identifies I∩A with the ideal generated by those same parameters in A; without those hypotheses that additional identification is not available.

Flatness over T, a prescribed identification of the nilpotent coefficient layers, and bidifferential formulas are customary parts of being the intended deformation. They must be checked if an application relies on them. They are not needed for this descent lemma. In particular the proof neither assumes nor establishes them for any unspecified deformation. Likewise, the word “differential” supplies no extra descent property: the proof concerns the underlying associative algebra and modules, not horizontal frames or compatibility with extra connections.

For m-adically complete D, A is complete and separated for the induced filtration A∩m^n: it is a closed fixed-point subring of D, and averaging gives A/(A∩m^n)≅(D/m^n)^G. The invariant basis identifies the induced filtration on M^G with ⊕_i(A∩m^n)e_i. This does not, without a separate comparison of filtrations, assert that the induced topology is the a-adic topology, where a=A∩m.

For a general complete parameter-adic deformation, the same statement applies to its specified stable filtration, provided D is genuinely local with the residue properties above. With finite free modules and the induced complete topologies, the displayed tensor isomorphisms also hold for the corresponding completed tensor products, since finite free tensors identify with finite direct sums. No adic-flatness hypothesis is needed for this finite-free assertion. A limit of finite-order objects with unspecified effectivity, freeness, or compatibility is not automatically such a module.

## 7. Local stabilizer versus full group

At a point of a finite quotient, only the decomposition subgroup fixing that point acts on its completed local ring. Its inertia subgroup is the kernel of the action on the residue field. The theorem applies directly to a finite subgroup acting on that local ring and trivially on that residue field; in particular, to inertia itself.

At a geometric point with residue field fixed by the stabilizer, this is the usual full local stabilizer. Elements moving the point are not automorphisms of that one completed local ring. They cannot be inserted into the above averaging argument on that ring without first supplying an appropriate semilocal or orbit construction.

At a non-geometric point the full decomposition subgroup can act nontrivially on the residue field. Trivial inertia on the fiber is then different from trivial action of the decomposition subgroup on the entire fiber. Applying the theorem to inertia gives descent to the inertia-invariant local ring, but passage to full-group invariants requires additional residue-field/semilinear descent. That extra step is not proved here. The stated equivalence deliberately assumes the full acting group fixes k.

## 8. Conditional relevance to root/Morita transport

The ramified example shows that a nontrivial scalar root character survives on the module fiber even when it disappears from the endomorphism algebra. The theorem supplies a sufficient positive replacement: establish a genuine local equivariant free module with trivial inertia fiber, and then invariant free-module descent and coefficient compatibility follow formally.

If a proposed root correction is implemented by an actual equivariant deformed Morita bimodule or another specified invertible transport, one may apply the theorem to the transported module only after proving that its target algebra satisfies these local hypotheses, that the transported module is finite free, that its fiber has trivial inertia action, and that the transport respects the coefficient ideals relevant to the comparison. An ordinary root line, an equality of endomorphism sheaves, or a cohomological half-class alone supplies none of these deformed structures or compatibilities. In a noncommutative setting an ordinary line is not automatically an invertible bimodule.

This result proves the local descent portion once those hypotheses are supplied. It neither constructs such a root correction nor proves that local corrections glue globally.

## Input and scope record

Read: ../../null-ramification-guard/ramified-descent-0644/RESULT.md. All arguments above are formal local ring and module arguments. No physical source or jet values are evaluated in this argument.
