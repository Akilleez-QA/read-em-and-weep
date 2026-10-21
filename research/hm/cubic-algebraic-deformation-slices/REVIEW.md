# Independent mathematical review

**Verdict: PASS, conditional on the pinned mathematical inputs.**

Reviewed document: `PROOF.md`, SHA-256

`e36f0276e456226ae50fbb4505fec97eed82dd93a4064f5646e3570a46fabde2`.

The argument proves the stated existence of actual nested smooth algebraic slices of dimensions 636 and 576, with universal marked formal class functors and a noncanonical natural section of polarization forgetting. No mathematical correction is required. This is an independent mathematical review, not proof-assistant verification.

## 1. Dependency interfaces

The following supplied input proofs were checked at the interfaces used here:

- Global deformations: SHA-256 `c25a2b4deb850578fee2232da8eeeba3b68f15f245111f1b5fcc3c72e6f09814`. Its affine lemma supplies triviality of arbitrary affine Artin deformations, compatibility with prescribed lower-order trivializations, and lifting of the relevant identity-reducing affine automorphisms. These are stronger statements than first-order local rigidity and are exactly what the new gluing argument needs.
- High-power Hilbert germ: SHA-256 `33b5f65e825d1105190b3471bbb435c325f1f9bef7f7fb61cad9bb475f799b99`. The smooth germ has dimension `(n^2-1)+636`, and its tangent kernel over powered pair classes is precisely `pgl_n`.
- Fixed polarization roots: SHA-256 `4523a90f3b54841d2fc541252af50c0ba68e8b213d10d7f142eb308b349a513f`. The power map is an isomorphism of marked pair class functors over the abstract functor, not merely an isomorphism on tangent spaces. The same proof establishes `H0(O_XA)=A` for every Artin deformation.
- Etale polarization roots: SHA-256 `5b15161d0cce2c1b7c99b129d079c2571812ad93b85163b311006e96fb6e7e3c`. Section 5 provides an actual smooth pointed etale Hilbert chart carrying an actual line bundle and actual power isomorphism. Thus the proposed slices start inside an algebraic family, rather than assuming an algebraization of an independently constructed formal family.

The arithmetic is consistent: the Atiyah sequence, `H0(Theta_V)=0`, and `H2(O_V)=0` give the 60-dimensional Picard kernel and `636=60+576` pair tangent dimension.

## 2. Automorphisms and lift-class torsors

The induction eliminating marked abstract automorphisms is valid. Over a small extension with kernel `J`, an automorphism reducing to the identity differs from the identity by a derivation with values in `O_V tensor J`. This kernel is `H0(Theta_V) tensor J=0`. Induction applies to every deformation object, not just to objects obtained from a selected family.

Consequently a marked pair automorphism is multiplication by an element of `1+m_A`. Such an element lifts to `1+m_A'` and acts on every pair lift. Scalar automorphisms are not absent; their liftability is the decisive property.

For lifts with an identified reduction, the affine-cover comparison is valid on this singular variety. The pinned affine lemma provides local comparisons of scheme lifts inducing any prescribed lower-order comparison. The units sequence on each affine provides the analogous line-bundle comparisons. The discrepancy of two compatible systems of gluing maps is therefore a Cech cocycle in `Theta_V tensor J` or `A_L0 tensor J`. The original line transitions must be retained in the latter case; this produces the Atiyah sheaf and does not replace it by a globally split sum. Since the maximal ideal annihilates `J`, all discrepancy products and higher-order conjugation terms vanish. Changing comparisons gives a coboundary, and modifying transitions by an arbitrary cocycle constructs every lift class. This proves a torsor assertion, including freeness, at every small extension.

The affine deformation principle invoked in the proof is consistent with the cotangent-complex classification of extensions and their automorphisms in [Stacks 08SM](https://stacks.math.columbia.edu/tag/08SM). No smoothness of the singular affine opens is assumed.

Passing to fibers of the unrigidified class functors causes no residual quotient: changing a reduction identification by an automorphism of the lower object is implemented by an automorphism of the upper object. For abstract objects this is immediate from triviality of the automorphism group; for pairs it follows from scalar liftability. Thus the fibers of `F(A')->F(A)` and `G(A')->G(A)` really are the indicated torsors. This is the point that makes uniqueness, rather than only versality, possible.

## 3. Algebraic construction of the slices

In a smooth pointed scheme, regular functions whose cotangent classes span the annihilator of a chosen tangent subspace cut a smooth subscheme with exactly that tangent space, after shrinking. Their differentials can be completed to a cotangent basis, producing etale coordinates; the cut is then the inverse image of a coordinate linear subspace. This agrees with the smooth local-coordinate theorem in [Stacks 039P](https://stacks.math.columbia.edu/tag/039P).

Applying this first to a complement of `pgl_n`, and then inside the resulting slice to a complement of the 60-dimensional Picard subspace, gives actual nested finite-type smooth slices. The codimensions and dimensions are respectively `n^2-1`, `60`, `636`, and `576`. Base change preserves flatness, projectivity, relative ampleness, and the actual power isomorphism. No quotient construction, global slice theorem, or integrability condition on the chosen tangent complements is needed.

## 4. All-orders Kodaira--Spencer equivariance

The proof uses more than a first-order tangent isomorphism. The lifting set of a pointed base map over a small extension is a torsor under `T_sS tensor J`, and its map to deformation lifts is equivariant for the central Kodaira--Spencer map.

One precise justification of the stated transition-map calculation is as follows. If two local ring maps `phi,psi:O_S,s->A'` have the same reduction to `A`, their difference is a derivation `delta` with values in `J`. Pull the family back once along the combined map to

    B = A' x_A A'.

Writing an element of `B` as `(a,a+j)` identifies its extra summand with `J`, annihilated by the maximal ideal of `B`. There is a ring map

    B -> C direct-sum J,    (a,a+j) -> (a mod m_A',j),

where `J` has square-zero multiplication. The composite from `O_S,s` is exactly the tangent map `delta`. Choose affine local trivializations over this Artin ring `B`, using the pinned affine lemma. Restriction along the two projections to `A'` compares the two lift systems; restriction to `C direct-sum J` extracts the same discrepancy cocycle as a central first-order deformation. Its cohomology class is therefore `KS_s(delta)`. The pair case uses the unchanged central line transitions and the Atiyah cocycle in exactly the same way.

This also clarifies that no Zariski-local trivialization of the algebraic family over a whole neighborhood of `s` is being assumed. Artin-local trivializations suffice.

Since the selected `KS_s` is an isomorphism, the map of nonempty lift torsors is a bijection. Induction on Artin length proves both surjectivity and injectivity of the classifying transformation. The scalar argument in Section 2 ensures that this induction does not depend on a chosen lower-order pair isomorphism. The transformations are natural pullback transformations, so the pointwise bijections are natural isomorphisms of functors. Completion and smoothness then give the two asserted power-series prorepresenting rings.

## 5. The natural section and the scope of universality

Under the two established natural isomorphisms, the nested inclusion defines

    G -> h_S576 -> h_S636 -> F.

Forgetting the line bundle yields the same restricted underlying family on `S_576`, so the composite back to `G` is the identity. The section is genuinely natural on all local Artin algebras; it is noncanonical because the tangent complements and algebraic equations were chosen. The other 60 polarization directions remain present.

Compatible abstract Artin systems give compatible unique classifying maps, and the actual line bundle on the algebraic slice pulls back compatibly along them. This supplies a universal marked formal germ inside one actual algebraic family. It does not imply algebraicity or convergence of arbitrary formal arcs, representation of the pair groupoid, fine moduli over unrestricted bases, or a canonical/global polarization assignment.

The stated exclusions concerning unmarked automorphisms, generic fibers, original sections, and the original source or algebraicity problems are respected. The review uses no selected source-instance evaluation or large computation.
