# Independent audit: geometric-return sign barrier

## Verdict

The geometric coefficient-sign result is correct for the specified two-axis external-product ambient, with its retained multiplication marking and bounded ideal structure. It genuinely extends the preceding identity-reduction argument to all biregular automorphisms of P² × P², including factor exchange, and to arbitrary invertible coefficient multipliers.

The result is a necessary condition on a proposed return. It does not construct a return, prove return of a boundary module, compute the action on the retained obstruction space, or establish vanishing or nonvanishing. The proof expressly maintains these distinctions. No fatal gap was found in that scoped conclusion.

Two hypotheses/conventions deserve more explicit wording before the statement is reused independently: the bounded external-product ideal relations used in the mixed step, and the direction of the local algebra map supplied by a bimodule. They are detailed below. 

## 1. Geometry: pass

An automorphism preserves the integral Picard lattice and the nef cone in both directions, hence permutes its primitive extremal generators H_z and H_h. Primitivity matters: it rules out positive rescaling of a generator. If the generators are fixed, the associated complete linear systems show that the two projections are each transformed by a projective linear automorphism. The exchange case follows by composition with the factor swap. Thus the stated semidirect-product description is justified.

The differential identifies the corresponding factorwise cotangent bundles and their determinant lines. Under exchange, identification of the tensor of two 2-forms with a 4-form contributes (−1)^(2·2)=+1. There is no missing orientation sign here. All maps are understood to be algebraic C-automorphisms, as in the statement.

## 2. Naturality and arbitrary units: pass

In a square-zero extension with symmetric kernel, the commutator of lifts is well-defined. An algebra homomorphism carries that commutator to the target commutator. Taking the opposite algebra negates it, regardless of a chosen local splitting or Hochschild representative.

Fix the direction F: φ* A^op → A. Let j_i be canonical differential pullback and λ_i the induced pure coefficient identification. Since these are identifications of the same line bundles, λ_i=c_i j_i for a local unit c_i. Naturality gives

    β_target(φ*f,φ*g) = −λ_i(φ*β_i(f,g)),

whereas the chain rule identifies the left side with j_i(φ*β_i(f,g)). Wedges of differentials locally generate the line, so c_i=−1 pointwise as a sheaf identity. This is stronger than merely knowing that a bracket is nonzero somewhere. It needs no global constancy argument and excludes arbitrary units, not just the two signs. For an ordinary automorphism, the same reasoning gives c_i=+1.

Factor exchange changes the target index, not the sign in this calculation. The intrinsic differential-form-valued bracket is essential: one cannot import an anti-Poisson sign arising from a different, scalar-valued trivialization without tracking its coefficient action.

## 3. Opposite multiplication and the mixed step: pass in the specified ambient; make assumptions explicit

The positive mixed conclusion uses more than the two isolated pure commutators. It uses the fixed product identification of the pure coefficient lines with J, and the fact that the bounded external-product ambient has the ordinary commuting product on those coefficient factors. In an opposite algebra, the product of a z coefficient with an h coefficient is the original product in reversed order. For the specified external product this is the same marked product after ordinary tensor interchange. There is no additional opposite sign.

Accordingly, multiplicativity forces the mixed map to be the tensor of the two pure maps, with the required target-factor interchange. The two minus signs cancel. Compatibility with the wedge identification J=ω_X then gives exactly canonical differential pullback, not an independent mixed scalar.

Likewise, the displayed higher-order calculation is valid because, writing I for the combined nilpotent ideal, the bounded external-product structure has I·J=J·I=0 and J²=0. Adding J-valued corrections to the pure images cannot change their product.

Suggested clarification: state these bounded product/annihilation relations explicitly, or explicitly say that they are inherited from the specified external-product ambient. The pure square-zero restrictions alone would not, for an arbitrary unrelated ambient, establish the reversed-product identification or these annihilation relations. This is a scope clarification, not a counterexample to the named ambient.

## 4. Locally right-free line bimodules: pass with direction convention

An invertible (B,A)-bimodule P locally free of rank one as a right A-module identifies the left-action map with

    B → End_A(P) ≅ A.

The endomorphism algebra is A, not A^op: for a chosen right generator e, the endomorphism determined by e ↦ e a composes with the one determined by e ↦ e b as multiplication a b. Invertibility makes the left-action identification an isomorphism.

To apply the displayed naturality formula verbatim, orient this local isomorphism as φ* A^op → A. Depending on which side is called the source and on the convention for the graph of φ, the bimodule instead supplies the inverse direction, covering φ^−1. In that case invert it first, or apply the same proof in that direction. Inverting canonical differential pullback gives canonical pullback for the inverse map; the pure relative minus signs and mixed relative plus sign are unchanged. The statement should make this convention explicit rather than silently identify φ with φ^−1.

A change of right generator conjugates the map by a unit. On a pure symmetric square-zero kernel such conjugation acts trivially: the unit's classical reduction is central and nilpotent corrections have zero product with that kernel. For J, the same conclusion follows from the bounded annihilation relations and its symmetric classical coefficient action. Thus the local coefficient test is independent of the generator and glues.

The graph hypothesis alone does not imply local right-freeness or preservation of the pure coefficient filtration and product marking. Those are separate hypotheses already required by the statement's marked-action language. Neither a classical determinant line nor an arbitrary derived/Morita equivalence automatically supplies them. The new proof correctly avoids such an inference.

## 5. Relative coefficient scalar versus cohomological action: crucial distinction preserved

The conclusion “positive mixed coefficient map” means positive scalar relative to canonical pullback between φ*ω_X and ω_X. It does not mean that the resulting operator on a retained obstruction or detector space is +Id.

A cohomological operator additionally depends on pullback by φ, the classical module identification, the action on its endomorphism coefficients, the prescribed boundary return, and any separately specified band identification. None of these actions is computed by the local bracket test. Canonical pullback itself should not be replaced by identity just because the relative coefficient scalar is +1. A negative eigenspace in the relevant retained cohomology is not excluded by this coefficient theorem; its presence is also not established by it.

There is a further logical boundary: even finding a negative eigenvalue somewhere in a cohomology representation does not force the particular obstruction class to vanish. A vanishing argument must show the required equivariance/fixed-class relation for that particular class together with its transformation by a genuinely negative operator in the relevant setting. The existence of the full return and return of the specified boundary remain independent obligations.

The new proof's opening disclaimer and final section correctly respect all of these boundaries. Its statement that geometric automorphisms “may still have negative eigenspaces” is permissive, not an exhibited eigenspace calculation.

## 6. Comparison with the preceding proof and verification boundary

The previous theorem intentionally left nontrivial base automorphisms, permutations, and nonsign coefficient maps outside its exclusion. The new argument closes those loopholes for this geometric differential-form-valued bracket and its marked external product. It does not contradict the earlier allowance for anti-Poisson base maps under other coefficient markings.

The result does not extend automatically to partial opposites, changed coefficient-product markings, arbitrary filtered deformations lacking the bounded product relations, or general derived equivalences. It does not determine the full returned tracefree operator.

This audit checks the algebraic arguments in the two proof files; the linked discussions are not used as mathematical evidence.
