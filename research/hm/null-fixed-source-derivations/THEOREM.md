# Bounded derivation constraint for the fixed curve field

## Result and limits

Let k be a field of characteristic zero, E/k the curve y²=x³−x, and K=k(E⁴). Write coordinates x_i,y_i, i=1,...,4, and let V_i be the k-derivation specified by V_i(x_i)=y_i, V_i(y_i)=(3x_i²−1)/2 and zero on other axes. Let G=(Z/2)^4 act by the independent signs of the y_i, fixing every x_i and k. For χ(g)=the product of its four signs, put π15=(1/16)∑_g χ(g)g.

**Theorem.** The centralizer of {V_1,...,V_4} in Der_k(K) is precisely ⊕_i k V_i. Its intersection with the centralizer of π15 is zero. In particular the coefficients are rational when k=Q.

This excludes nonzero *derivations of this fixed field satisfying both specified commutations*. It does not exclude source families, changes of primitive recipes, changes of physical derivations, or variations in a larger coefficient algebra. It supplies no source value, cancellation, nonvanishing, independent H24 direction, or actual source/jet evaluation.

## Proof

1. **Field and constants.** Over any algebraically closed extension of k, x³−x has simple roots and is not a square in the rational function field: its valuation at x=0 is odd. Hence y²−x³+x is irreducible there. Thus E is geometrically integral, as is its fourfold product, and K/k is regular; specifically k is algebraically closed in K. One direct last-step argument is that geometric integrality makes K⊗_k kbar a domain. A proper finite subextension k(a)/k in K would be separable in characteristic zero; after tensoring with kbar it would be a product of at least two copies of kbar, which cannot inject into that domain. Tensoring preserves this injection because a field extension is flat.

The x_i form a transcendence basis of K/k, and K/k(x_1,...,x_4) is finite separable. Consequently Der_k(K) has dimension four over K. The V_i are linearly independent: evaluation of ∑ f_i V_i on x_j gives f_j y_j, and y_j≠0 in K. They are a basis. Equivalently any derivation D has the unique expression D=∑ (D(x_i)/y_i)V_i; the remainder vanishes on the transcendence basis, hence on its separable algebraic extension.

If V_i(f)=0 for every i, then all k-derivations of K kill f by this basis property. If f were transcendental over k, extend {f} to a transcendence basis of K/k. The derivation ∂/∂f of the resulting rational field extends uniquely to K, since the extension is finite separable, and sends f to 1, a contradiction. Therefore f is algebraic over k and hence lies in k. Thus the common constants are exactly k. This is an algebraic argument; no analytic connectedness or point specialization is involved.

2. **Centralizer.** The V_i commute: their commutators vanish on all coordinate generators and therefore on K. Write σ=∑ f_i V_i. With [A,B]=AB−BA, the Leibniz rule gives

 [σ,V_j]=−∑_i V_j(f_i)V_i.

Basis independence shows that all these commutators vanish exactly when each f_i is a common constant, hence f_i=c_i∈k. Conversely every such constant combination commutes with every V_j.

3. **Full-sign projector.** Let b_m=∏_{i: bit_i(m)=1} y_i. It has deck character m; the rational-x coefficient field is fixed. Conjugation by g sends V_i to ε_i(g)V_i, so V_i sends character m to m XOR 2^(i−1).

For each i take the witness f^(i)=x_i∏_{r≠i}y_r. It has character 15 XOR 2^(i−1), so π15(f^(i))=0. For σ=∑ c_j V_j,

 V_i(f^(i))=∏_r y_r,
 V_j(f^(i))=x_i ((3x_j²−1)/2) ∏_{r≠i,j}y_r  (j≠i).

The latter terms have character 15 XOR 2^(i−1) XOR 2^(j−1), different from 15. Thus

 π15 σ(f^(i))=c_i∏_r y_r,       σ π15(f^(i))=0.

If [σ,π15]=0, each c_i=0 because ∏ y_r is nonzero in the field. Commuting with the single full-sign projector suffices; commuting with every deck involution was not assumed. The witnesses are formal identities in the abstract field, not execution on physical source data.

## Finite algebraic normalization extensions

Let L/K be any finite algebraic extension in characteristic zero. Each V_i extends uniquely to a derivation of L, and those extensions commute: their commutator restricts to zero on K, and a derivation of a separable algebraic extension vanishing on K is zero. They still form an L-basis of Der_k(L). The same argument gives

 centralizer_{Der_k(L)}(V_1,...,V_4)=⊕_i C V_i,
 C={a∈L : a is algebraic over k}.

Here C/k is finite, and it is the common constant field. No assumption that L is geometrically integral over k is silently inserted.

There is no canonical π15 on arbitrary L. The original deck automorphisms need not extend to L at all; chosen extensions need not form the same group. If an actual action of G on L extending the original action is specified, and it fixes C pointwise, the same witness proof gives σ=0. Conjugation of the extended V_i still has the required sign because extensions of derivations are unique. More generally the same conclusion holds for σ that preserves K: its restriction is a fixed-field derivation, and the witness proof kills it; uniqueness then kills its extension to L.

**Necessary caveat / counterexample to an unconditional extension claim.** Let k=Q, L=K(u), u²=2. Extend the first deck generator by u↦−u and the other three by u↦u. These are commuting involutions defining a genuine action of G on L. The constant field contains u. Then σ=uV_1 is a nonzero Q-derivation commuting with every V_i. It is invariant under every deck conjugation: the sign on u cancels the sign on V_1. Hence it commutes with π15. Thus an arbitrary extension of deck action plus finite algebraicity does not imply σ=0. If instead every deck generator fixes u, the zero theorem applies. The extension/action is part of the hypothesis, not a harmless convention.

## Added deformation parameters and coefficient changes

On K(t), extend V_i by V_i(t)=0 and all deck actions by g(t)=t. Then ∂t is a nonzero k-derivation commuting with every V_i and π15. It vanishes on K but can differentiate a parameter-dependent family of source expressions. The fixed-field theorem therefore does not prohibit source deformations. A proposed family must separately preserve all required source identities, legal localizations, discrete conventions and physical derivative relations.

For k larger than Q the theorem concerns k-linear derivations. If only Q-linearity is imposed on k(E⁴), derivations of the coefficient field k may introduce further commuting directions (e.g. k=Q(t)). The phrase “constant base field” is not a substitute for requiring that σ annihilate it. Characteristic zero is essential here: in positive characteristic p, all pth powers are common differential constants, so the stated constants theorem fails.

## Static source applicability

The bounded source excerpts supplied in this packet show that `PhysicalModel.nu` is a product of y_i/x_i over legal-mask axes and `Dframe` uses nu and its inverse. These particular normalizations already lie in K. No algebraic root extension is needed for this literal normalization. The primitive recipes are rational functions of elementary-symmetric coordinate functions with chart data as coefficients; applying the theorem to them requires those coefficients to belong to the fixed base field and sigma to annihilate that field.

These observations establish applicability to the stated fixed-field interpretation, not all external source/domain hypotheses. Other root-adjoined normalizations require the separate extension analysis above. The fixed-field zero theorem is not a statement that no source deformation exists.

## Formal controls

Run `python check_derivations.py` and `python -O check_derivations.py`. The script manipulates only abstract character masks, formal first/second derivative labels and integer coefficients. It does not import production modules, evaluate source/owner/jet objects, construct physical matrices or multiply curve polynomials.

Controls verify the vector-field commutator sign by formal Leibniz cancellation; all character/projector commutator transitions; the four separating witness patterns; and negative controls (a nonzero fixed-field V_i fails projector commutation, a coefficient carrying the same character cancels its shift, and an abstract added parameter derivative has zero deck shift). Finite controls do not prove the field/constants theorem: that is supplied by the proof above.
