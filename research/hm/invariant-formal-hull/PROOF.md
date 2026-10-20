# Conditional formal smoothness of the deck-equivariant ordinary deformation problem

## Result and separated premises

Let k have characteristic zero, let X=C⁴, and retain E=N⊗f*H and the specified locally free presentation from [FULL-COEFFICIENT-FAMILY.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/2b03992b32d2f5cf0509b6f4840adf08369f54b7/research/hm/cubic-loci/foundation-p01/COEFFICIENT-FAMILY.md). Let G=(Z/2)⁴ act by the four deck involutions. Fix the natural G-linearization of N coming from its invariant origin divisors, and equip E with the resulting linearization. The action on X remains fixed throughout; G acts trivially on every deformation base.

The following two inputs have different evidentiary status:

1. **Geometric input P.** The exact-presentation premise and literal first differential in the full-coefficient theorem. Under P, that theorem and [its structural audit](https://github.com/Akilleez-QA/read-em-and-weep/blob/2b03992b32d2f5cf0509b6f4840adf08369f54b7/research/hm/cubic-loci/foundation-p01/historical-audits/projective-target-directions-FULL-COEFFICIENT-FAMILY-AUDIT.md) give an actual smooth 79-dimensional family U of ordinary bundles and an injective Kodaira–Spencer map at u=[v].
2. **Historical numerical input D.** For this same bundle and induced deck action on its endomorphisms, dim Ext¹_X(E,E)^G=79. This is the weight-zero assertion in the [bundled historical source](https://github.com/Akilleez-QA/read-em-and-weep/blob/add03476d9055aa00e1e00778eea6332cf8e01cc/research/hm/ext-model.md), Sections 0 and 4, and its [immutable public version](https://github.com/Akilleez-QA/read-em-and-weep/blob/add03476d9055aa00e1e00778eea6332cf8e01cc/research/hm/ext-model.md). D is assumed here. Its historical rank certificates have not been rerun or freshly verified.

**Conditional theorem.** Under P and D, the ordinary fixed-X deformation problem of the specified G-linearized E has a smooth miniversal formal base of dimension 79. The completed full-coefficient family itself is miniversal: every marked G-equivariant ordinary bundle deformation over a local Artinian k-algebra is obtained from it, and its classifying maps can be lifted compatibly across Artinian extensions. A Noetherian hull is isomorphic to k[[t₁,…,t₇₉]].

This is a higher-order ordinary background statement. It is not a star-module admission theorem, a universal fine-moduli assertion, or an assertion that the unrestricted deformation problem is smooth.

## 1. The exact deformation problem

Let Art_k be local Artinian commutative k-algebras with residue field k. For A in Art_k set X_A=X×Spec A. Define the deformation groupoid D_G(A) as follows:

- An object is a finite locally free O_{X_A}-module E_A, a G-linearization covering the fixed action on X_A, and a G-equivariant identification E_A⊗_A k≅E.
- A morphism is a G-equivariant bundle isomorphism compatible with that identification.

Write F_G(A) for its set of isomorphism classes. This marking is an identification of the special fiber, not a framing of the whole bundle. In particular, automorphisms reducing to the identity are allowed. No connection, star action, differential operator, source deformation, quotient by source automorphisms, or moving group action is included. We do not define F_G as the fixed-point subset of an unmarked coarse moduli space: genuine linearizations and their compatibility are part of the objects.

There is a canonical tangent identification

    T F_G = Ext¹_G(E,E) = Ext¹_X(E,E)^G.

The first identification follows by taking the extension associated with multiplication by the dual-number parameter, with its induced G-action; conversely an equivariant self-extension gives a dual-number deformation. The second uses exactness of G-invariants: averaging by |G|⁻¹Σ_g g makes invariants exact in characteristic zero. Equivalently, the equivariant Ext spectral sequence has higher group-cohomology columns zero. For E locally free the ordinary Ext groups are H^i(X,End E), finite-dimensional by properness of X. None of these statements needs the historical differential-rank computation.

## 2. Why the actual family is equivariant

The map F_X:X×U→P⁴ factors through q×id_U, so F_X is G-invariant. Consequently F_X*H has its canonical G-linearization. The invariant origin divisor on each elliptic factor supplies O_C(O), and thus N, with a G-linearization; its pullback to X×U has the same fixed linearization. Their tensor product gives

    𝓔=p_X*N⊗F_X*H

a G-linearization, with G trivial on U. Its restriction to u is the chosen linearized E. Thus the completed family defines an object of the completed groupoid D_G and a natural transformation h_S→F_G, where

    S=Ō_{U,u}≅k[[t₁,…,t₇₉]],
    h_S(A)=Hom_cont,local,k(S,A).

The forgetful map on tangents is the inclusion Ext¹_X(E,E)^G→Ext¹_X(E,E). Hence the injection proved in the full-coefficient theorem is an injection into the invariant part. By D the dimensions agree, so its equivariant Kodaira–Spencer map is an isomorphism. Write K for its image; then K=Ext¹_X(E,E)^G.

Twisting the chosen linearization of N by a deck character would not change the conjugation action on End E. Nevertheless the functor here fixes one linearization and its marked special fiber, rather than silently varying between such choices.

## 3. Hull existence: applicability of the usual framework

The required existence statement is a hull, not a representing object for the whole groupoid. The classical hull criterion is finite tangent dimension together with the Schlessinger gluing conditions. In groupoid language the Rim–Schlessinger condition implies the needed gluing conditions on isomorphism classes. The general hull/miniversal theorem and the passage from groupoids to isomorphism classes are stated in [Stacks Project, Section 90.15, Theorem 90.15.5 and Remarks 90.15.6–7](https://stacks.math.columbia.edu/tag/06IL).

Here the gluing conditions can be checked directly. For a diagram A'→A←A'' with A''→A surjective, put B=A'×_A A''. Compatible vector bundles over X_{A'} and X_{A''}, together with an identification of their reductions over X_A, patch to a vector bundle over X_B. Locally on X this is finite-projective module patching over the corresponding fiber product of rings. To see local freeness directly, shrink so the special-fiber bundle is free; it remains free on its Artinian thickenings, and the transition matrix between the two reductions lifts across the surjection. After adjusting a basis, the patched module is free. Morphisms patch as well, and the construction is compatible with restriction, so these local constructions glue on X.

The two compatible G-linearizations patch by the same fully faithful morphism construction. Their group law holds because it holds after both projections. The special-fiber marking patches too. Conversely reduction of a patched object recovers the two objects and their chosen identification. This proves the groupoid gluing equivalence, not just existence of some object with the right restrictions. The same finite-projective patching mechanism is used in [Stacks Project, Lemma 93.4.2](https://stacks.math.columbia.edu/tag/0DVP).

Thus D_G satisfies the Rim–Schlessinger condition. Its finite-dimensional tangent space gives a Noetherian minimal versal formal object ξ over a complete local k-algebra R with residue field k. The induced h_R→F_G is a hull. One can also take this standard hull framework as an explicit premise: the ring-theoretic implication below is independent of the manner in which hull existence was established.

Under D, choose elements x₁,…,x₇₉ mapping to a basis of m_R/m_R². Completeness and the topological Nakayama argument give

    P=k[[x₁,…,x₇₉]] →> R=P/I,
    I⊂(x₁,…,x₇₉)².

The coefficient field is already supplied by the k-algebra structure. No algebraic closure hypothesis on k is needed.

## 4. Producing the map R→S without assuming universality

Versality is enough. Put S_n=S/m_S^{n+1}, so S_0=k. Start with the residue map R→S_0 and the marked special fiber. Inductively apply formal smoothness of h_R→D_G to S_{n+1}→S_n and the actual coefficient-family object over S_{n+1}. This gives a map R→S_{n+1} extending the previously chosen map, together with an isomorphism from the pulled-back ξ to that family object extending the previous isomorphism.

The successive kernels are annihilated by the maximal ideal (or may be filtered into one-dimensional small extensions if that convention is used). Taking inverse limits gives a continuous local k-algebra homomorphism

    φ:R→S

and an isomorphism of formal objects φ*ξ≅Ē_U. This is a noncanonical choice, which is exactly why universality is unnecessary. Using the groupoid version ensures compatible isomorphisms, rather than assuming that an arbitrary sequence of unrelated isomorphism classes has coherent representatives.

On tangent spaces the coefficient-family map is the composite of the map induced by φ and the hull tangent isomorphism. Since both the coefficient Kodaira–Spencer map and the hull tangent map are isomorphisms, φ induces an isomorphism on cotangent spaces m_R/m_R²→m_S/m_S².

## 5. The elementary formal-ring argument

Compose the chosen presentation with φ:

    ψ:P=k[[x₁,…,x₇₉]] → R → S=k[[t₁,…,t₇₉]].

Its linear coefficient matrix is invertible. A continuous homomorphism between these two formal power-series rings with invertible linear term is an isomorphism: after a linear change of variables, its degree-one part is the identity; correct a putative inverse successively in homogeneous degrees 2,3,…, and pass to the complete inverse limit. This is a formal coefficient argument, not an evaluation of the geometric model.

For every a∈I the image ψ(a) is zero. Since ψ is injective, a=0. Therefore

    I=0,     R≅k[[x₁,…,x₇₉]],     φ:R≅S.

Transporting ξ along this isomorphism identifies the completed coefficient family with a minimal versal formal object. Thus its map h_S→D_G is formally smooth with tangent isomorphism; h_S→F_G is a hull. This proves the theorem.

The proof excludes hidden higher-order equations, embedded nilpotent relations, and higher-order relations with zero quadratic term just as effectively as it excludes quadratic equations. It needs the actual family over S, not merely a list of 79 first-order classes or separate one-parameter extensions.

## 6. Precise consequences and limits

### Ordinary formal completeness and unobstructedness

For every A in Art_k and every marked G-equivariant E_A, some map S→A pulls the coefficient family back to E_A. Given a surjection A'→A, a classifying map over A and a deformation over A' with an identified reduction, the classifying map and the identification can be lifted. This is formal versality, stronger than a tangent-space statement.

Every object over A extends across every Artinian surjection A'→A: first classify it by S→A, then lift the 79 parameter values to m_{A'} and pull back the family. The base is a formal power-series ring, so there are no relations to preserve. Compatible formal systems over a complete Noetherian local k-algebra are similarly induced by a continuous map from S, using successive compatible lifts.

In particular all invariant tangent vectors admit compatible ordinary lifts to every order. In the usual Yoneda obstruction theory this implies a∘a=0 in Ext²_X(E,E)^G for a∈Ext¹_X(E,E)^G. Polarizing gives a∘b+b∘a=0 for invariant a,b. It does not give the individual ordered product a∘b=0. Smoothness also does not imply Ext²_X(E,E)^G=0: an obstruction space may contain nonzero classes that are never realized as obstructions. No higher associative A∞ product table, formality, or vanishing of every Massey product is asserted.

### Automorphisms, determinants, and algebraicity

Scalar automorphisms 1+c, c∈m_A, already show that the marked groupoid generally has automorphisms. A hull gives existence and compatible lifting, not uniqueness of the classifying map or of a bundle isomorphism. No claim of universal representability of F_G is needed or made. Scalar automorphisms alone do not prove that the isomorphism-class functor is non-prorepresentable; that is a separate question. No historical Ext⁰=1 assertion is needed here.

The theorem is stated without an independently chosen determinant trivialization. Adding a fixed determinant, an identification of it, or a determinant-one restriction changes the definition of the deformation problem and its automorphisms; such variants require their own comparison. In particular, the unrestricted trace-free dimension quoted in the historical source is not the tangent dimension of the present functor.

The family U is algebraic and its completion is miniversal. The result does not by itself identify a Zariski-open neighborhood in a coarse moduli scheme, establish uniqueness of algebraic parameters, or algebraize every formal classifying map. A formal power series need not be an algebraic map from an originally specified algebraic base. Any further étale-local algebraic-moduli statement must invoke and check the appropriate algebraicity and versality theorems.

### Excluded deformation problems

The result concerns fixed-X, fixed-deck-action, G-linearized ordinary bundles. It does not claim smoothness of the unrestricted ordinary deformation space with nontrivial deck-character directions, of a source-varying problem, or of an unmarked coarse fixed locus. It supplies no star-module structure, star-order lift, residual cancellation, detector response, or conclusion about mixed operations involving noninvariant or star directions. The formal parameters here are ordinary background parameters.

## 7. Self-check and evidence boundary

The argument was checked against the following potential failure points:

1. The family genuinely carries the chosen linearization; invariance of a numerical tangent vector alone would not suffice.
2. P proves only an injection. D is separately required to make it a tangent isomorphism and is never promoted to a fresh calculation.
3. Hull existence uses proper finite-type geometry, finite tangent dimension, and equivariant bundle patching. Simplicity and a fine moduli space are unnecessary.
4. The map from the hull is obtained by compatible versal lifting, with the ring arrows R→S in the correct direction.
5. The relation ideal lies in the kernel of an injective power-series coordinate substitution, so it vanishes in every order.
6. The conclusion is miniversality and ordinary unobstructedness, with no uniqueness, ordered-product, star, or global moduli overclaim.
