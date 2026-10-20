# Small-extension obstruction for row-represented left modules

## Scope and hypotheses

This is a universal formal-algebra derivation. No actual model, source-coordinate, jet, physical-matrix, or obstruction-coordinate evaluation was performed. All thirty retained values remain unknown.

Let X have a cover on which a classical vector bundle E is free, with row transitions g_ij satisfying g_jk g_ij=g_ik. Let R'→R be a local Artin small extension with kernel I annihilated by the maximal ideal; in particular one may take k[h]/h^(n+2)→k[h]/h^(n+1). The special fiber is O_X, and all ambient descent maps and triple units reduce to identity and 1. Assume coefficientwise lifting of sections on the chosen intersections. This holds for the truncated formal presentations under consideration.

Fix a genuine ambient algebroid extension over R': associative unital products μ_i, algebra isomorphisms F_ij, and units A_ijk satisfying

F_ij F_jk=Ad(A_ijk)F_ik,
A_ijk⋆A_ikl=F_ij(A_jkl)⋆A_ijl.

Fix a locally free left module over its reduction to R, represented by rows and semilinear maps φ_ij(v)=F_ij(v)⋆G_ij, with

F_ij(G_jk)⋆G_ij=A_ijk⋆G_ik over R.

Choose arbitrary coefficientwise lifts of G_ij to R'. Matrices remain invertible: their special fibers are invertible and the kernel is nilpotent. Entrywise algebra operations and row matrix composition are used only symbolically below.

## 1. Defect and its actual coefficient sheaf

Define the I-valued defect and normalization

D_ijk=F_ij(G_jk)⋆G_ij−A_ijk⋆G_ik,
C_ijk=g_ik^(-1)D_ijk.

Every operation on an I-valued term reduces to its classical operation. The normalized C is a Čech 2-cochain of End(E)⊗_k I, represented in the i row frame. Frame transport is

τ_ij(x)=g_ij^(-1)x g_ij.

For a p-cochain c, the differential is

(δc)_(i_0…i_(p+1))=τ_(i_0i_1)c_(i_1…i_(p+1)) + Σ_(r=1)^(p+1)(−1)^r c_(i_0…omit i_r…i_(p+1)).

In particular δx_ijk=x_ij+τ_ij(x_jk)−x_ik. This is the endomorphism SHEAF of the bundle, not the sheaf of scalar functions and not the ambient shifted Hochschild complex. Row composition reverses the usual presentation of the endomorphism algebra, but does not alter this additive sheaf or its Čech differential.

## 2. Explicit cocycle proof, including signs

Associativity, the F-homomorphism identities, and inner gluing give the exact four-index identity

A_ijk⋆D_ikl + F_ij F_jk(G_kl)⋆D_ijk
 −F_ij(A_jkl)⋆D_ijl −F_ij(D_jkl)⋆G_ij=0.

Proof: expand F_ij(F_jk(G_kl)⋆G_jk)⋆G_ij in two ways. Substituting the jkl and ijl defects gives the common leading term F_ij(A_jkl)⋆A_ijl⋆G_il plus the last two defect terms with positive signs. Substituting the ijk and ikl defects gives A_ijk⋆A_ikl⋆G_il plus the first two defect terms. The leading terms agree by the pentagon. No centrality of A is used.

Reduction on I therefore gives

D_ikl+g_kl D_ijk−D_ijl−D_jkl g_ij=0.

Left multiply by g_il^(-1), using g_il=g_kl g_ik=g_jl g_ij. The result is

C_ikl+C_ijk−C_ijl−τ_ij(C_jkl)=0,

which is exactly δC=0.

## 3. Module corrections for this fixed ambient extension

Every change of lifted transitions has the unique form

G_ij→G_ij+g_ij x_ij,  x_ij∈End(E)(U_ij)⊗I.

Direct linearization gives

ΔD_ijk=g_jk g_ij x_ij+g_jk x_jk g_ij−g_ik x_ik,
ΔC=δx.

Consequently the class [C] is independent of arbitrary lifted transitions and vanishes exactly when they can be corrected to genuine module descent on this cover. Explicitly solve δx=−C. The lower-order module and ambient coefficients remain literally unchanged.

On an End(E)-acyclic cover, notably an appropriate affine cover with affine intersections in the stated separated algebraic setting,

[C]∈H²(X,End(E))⊗I=Ext²_O_X(E,E)⊗I.

This identification uses local freeness of E: the local positive Ext sheaves vanish. Without acyclicity, the literal fixed-cover obstruction is first a Čech class; do not identify it with derived global Ext without a comparison or refinement. Locally free modules lift locally as free modules, so there is no additional local module-action obstruction in this formulation.

Once solutions exist, their differences are Čech 1-cocycles; modulo frame isomorphisms that are identity over R, the solution set is a torsor under H¹(End(E))⊗I, with infinitesimal automorphisms H⁰(End(E))⊗I. This torsor statement does not select or prove existence of a solution.

## 4. Changing the ambient extension: the concrete characteristic map

Now keep the ambient data over R and the module over R fixed, but compare two genuine ambient extensions over R'. Write their difference as

μ_i→μ_i+u_i,  F_ij→F_ij+v_ij,  A_ijk→A_ijk+a_ijk,

where u,v are normalized and all differences are I-valued. In the ambient convention D^q=C^(q+1), d=δ+(−1)^p b, the tuple η=(u,v,a) has total degree 1. Since both ambient extensions satisfy their equations, the literal ambient lifting lemma gives dη=0.

Holding the lifted G fixed, the exact first variation is

κ_g(η)_ijk=g_ik^(-1)[u_i(g_jk,g_ij)+v_ij(g_jk)g_ij−a_ijk g_ik].

Here u is extended to matrices by the usual index summation. There is no u_i(1,g_ik) contribution because u is normalized. In particular the arity-zero ambient term contributes −a_ijk Id in the commutative classical setting. This minus sign agrees with the source's first-order −b Id convention.

With simultaneous module corrections the formula is

C_new=C_old+κ_g(η)+δx.

Because both ambient extensions are genuine, Section 2 proves δκ_g(η)=0. The expression depends on the classical transitions and η only; no lower positive-order coefficient survives multiplication by I.

### Coboundary check, with an explicit primitive

Let an ambient total degree-zero cochain be (t_i,s_ij), where t_i is a normalized unary cochain and s_ij is a scalar arity-zero cochain. Its coboundary is

η=d(t,s)=(bt, δt−bs, δs),  (bs)(f)=fs−sf.

Define

z_ij=g_ij^(-1)[t_i(g_ij)−s_ij g_ij].

Expansion using (bt)(f,g)=f t(g)−t(fg)+t(f)g and g_jk g_ij=g_ik gives

κ_g(d(t,s))=δz.

Thus κ descends to a well-defined map

κ_E:H¹(Tot Čech(D))⊗I → H²(X,End(E))⊗I.

Under the applicable Hochschild comparison the source is HH²(X), and this is the characteristic evaluation map with the row/gerbe sign just fixed. This identification is not needed for the explicit obstruction and variation formulas. It can also be taken as the concrete definition of the map for this presentation. No assertion about a bracket or DGLA on the naive ambient total complex is required.

## 5. Fixed ambient versus joint-pair existence

For a CHOSEN genuine ambient extension, module lifting is equivalent to [C]=0. Ambient unobstructedness alone says nothing about that condition.

For a JOINT choice of ambient extension and module extension, once one ambient extension is chosen as reference, existence is equivalent to finding an ALLOWED closed η with

[C]+κ_E([η])=0.

For unrestricted small-extension ambient corrections this is precisely vanishing of the image of [C] in coker κ_E. Equivalently [C] lies in the image of κ_E, with its negative chosen to cancel it. Literal ambient extensions form a torsor under closed degree-one ambient cochains; passing to their cohomology classes suffices here because boundaries change C only by a module coboundary. If coefficients, symmetries, products, or presentation terms are frozen, restrict to the actually allowed closed corrections. One cannot silently replace that space by all of HH².

This conditional two-stage criterion is appropriate because a genuine ambient extension is already known to exist. It does not assert that the full simultaneous deformation problem is controlled merely by a single Ext group, nor does it assert the coker is zero.

## 6. Consequences for the invariant ambient theorem and the supplied two-jet

The new ambient theorem removes the ambient lifting obstruction by allowing higher μ,F,A coefficients to vary. Its ambient obstruction group is shifted total H² (ordinary HH³). The module obstruction is Ext²(E,E), and the variation between already-existing ambient extensions is governed by shifted total H¹ (ordinary HH²). These are three distinct roles.

If E and its chosen finite-order module lift carry compatible finite-group equivariance, the same constructions are equivariant, and one may use invariant cocycles and invariant allowed corrections. Averaging is legitimate only after the appropriate invariant obstruction class vanishes. Vanishing of invariant ambient HH³ does not imply vanishing of invariant Ext²(E,E), or surjectivity of invariant κ_E. Without compatible module equivariance no invariant-module conclusion is available.

Preserving the supplied ambient two-jet literally means corrections beginning at order three cannot change its order-two module obstruction. A module given only through order one must first pass the order-two test for that fixed two-jet (allowing whatever first-order module choices are genuinely permitted). Only after a module two-jet exists can the all-order ambient theorem be used as the ambient half of successive joint lifting steps. Each subsequent step still requires the fixed-ambient Ext² obstruction to vanish, or to be cancellable by allowed ambient κ_E corrections. Neither condition is proved here.

The source's second-order formula is recovered by taking the arbitrary order-two G lift with zero new coefficient: D=h²R and C=h²g_ik^(-1)R, with δy=−C₂ for correction G_ij→G_ij+h²g_ij y_ij. All thirty retained obstruction values remain unknown. No parity argument or ambient extension theorem supplies those values.

## Inputs

- Local checked ambient lemma: [LEMMA.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/9e3d8dc8525a7d11ae919dfac2126794c9bdc366/research/hm/null-literal-ambient-extension/descent/LEMMA.md).
- Local source for row conventions and second-order residual: https://github.com/Akilleez-QA/read-em-and-weep/blob/c8aec970fd65a105f39f4e8aeb8a17f0f0053f89/research/hm/second-order-algebroid.md, Sections 4–5 and 8.

The cocycle identity, variation, and coboundary primitive above are derived directly; no external theorem is used to assert their signs or any obstruction vanishing.
