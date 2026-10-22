# Independent review of first-normal pair rigidity and the equation complex

## Reviewed artifact

- File: `PROOF.md` in this directory.
- SHA-256: `3284b713ff88ad8a05b33a3bc370f7282302d2e60501643dc384efc970a8756a`.
- Review date: 2026-10-22 UTC.
- Method: independent symbolic derivation followed by an end-to-end reading of the revised proof, verification of the final introductory novelty qualification, and direct retrieval and comparison of the overlapping negative-defect, positive-operator, and midpoint notes identified below. No edits to the proof were made by this reviewer.

## Verdict

**PASS, relative to the explicitly pinned mathematical inputs, with the narrowed contribution claim stated below.** The all-degree invariant hypercohomology bridge, the nonvanishing gauge-image cohomology, the comparison of existing first-normal pairs, and the three-term linearized equation-complex triangle are consistent. The revised proof appropriately treats the overlapping kernel, exact-sequence, and invariant-cohomology results as foundations rather than claiming them as new. No blocking mathematical correction was identified.

This verdict is not an independent reconstruction of the HM geometry or of every upstream source. In particular, the actual regular section, the coarse descent of the adjoint bundle, the primary invariant cohomology groups, PR645's defect vanishing, and the midpoint reference pair are inputs, not conclusions re-established by this review. The credited positive-twist operator comparison is inspected for scope and overlap, not independently re-proved here. No exhaustive repository-wide or external priority claim is certified.

## Overlap and substantive contribution

The following exact files were independently retrieved and read for this rereview:

- [Negative-defect note at a9082a2](https://github.com/Akilleez-QA/read-em-and-weep/blob/a9082a22472000723d62fe3479bef20aa09baf91/research/hm/order-four-quadratic-load/FIRST-NORMAL-ADJOINT-DEFECT-IS-INVARIANT-ACYCLIC.md), returned blob `39c9362a9a3bd314d891f0eda5accbe561b6edcb`.
- [Positive-operator comparison at 17c039f](https://github.com/Akilleez-QA/read-em-and-weep/blob/17c039f361f7f1083ee2cf5607f04cc263de0ce4/research/hm/order-four-quadratic-load/ACTUAL-THIRD-VALUE-AS-MIDPOINT-DUALIZING-OPERATOR-DEFECT.md), returned blob `5d98fa0658adfe1cbbcc7087db35c53510453f6e`.
- [Midpoint theorem at a0ccfe4](https://github.com/Akilleez-QA/read-em-and-weep/blob/a0ccfe44a4d2b528622d591888b8cc1cddb47792/research/hm/order-four-quadratic-load/MIDPOINT-NORMAL-EXTENSION-HAS-UNIQUE-SQUARE-ZERO-ADJOINT.md), returned blob `cf53e49359ee1a27c719f11c4cf49510583a12e4`.

The negative-defect note explicitly contains the two short exact sequences, the centralizer's invariant vanishing, and the invariant degree-one image isomorphism. The revised attribution accurately recognizes that overlap. Its final conditional statement about a genuine defect-sheaf cocycle is not the total-complex construction comparing existing bundle-and-adjoint pairs in Section 4.

Section 4 supplies a substantive explicit comparison construction: it identifies the actual transition and adjoint differences with a degree-one cocycle of the stated two-term complex and identifies changes of local bundle identification with total coboundaries. It obtains rigidity in the category of determinant-preserving marked equivariant pairs. This construction and formulation are not displayed in the three notes compared here. However, midpoint uniqueness and the nonzero affine bracket already make the underlying uniqueness phenomenon essentially implicit. The defensible contribution is the explicit marked-pair comparison and unique-isomorphism formulation, not a newly discovered uniqueness of the midpoint or a new existence theorem.

Section 6 constructs a distinct explicit comparison with the three-term classical linearized equation complex and retains the residual `O_(2Z)(2)[-2]` term. Neither the negative-defect note's two short exact sequences nor the positive-operator note's different-twist connecting map supplies this displayed triangle. This is a structural reduction of the remaining linearized equation groups, not their evaluation or a solution of the positive operator-residue problem.

## Checks performed

### 1. Regular-sequence kernel and twists

For a local regular sequence `(f,g)`, the equations `fa+gb=0` and `fc-ga=0` force

    (a,b,c) = u(fg,-f^2,g^2).

The proof's reductions modulo `f`, and subsequent cancellation of `f`, are valid. They use regularity of `g` and hence `g^2` modulo `f`; they do not divide by a generator that vanishes on `Z`. Uniqueness follows from regularity of `f^2`. Away from `Z`, the same assertion is immediate on a chart where one component is a unit.

The generator is the actual adjoint `N` up to its convention-dependent sign. Since `N` has twist two, its inclusion into `B(-2)` has source `O(-4)`, as claimed.

As an additional twist check, dualizing the regular square resolution

    0 -> G(-3) -> B(-1) -> O(1) -> O_(2Z)(1) -> 0

against `omega_X=O(-3)` gives

    0 -> O(-4) -> B(-2) -> G* -> omega_(2Z)(-1) -> 0.

This independently matches the displayed kernel and the stated dualizing twist of the cokernel.

### 2. The actual tangent and gauge maps

The universal rank-two identity `[T,N]=J(2 sigma(T sigma))` identifies evaluation followed by multiplication with the adjoint gauge map. The square resolution identifies the image of multiplication by `2 sigma` with the entire sheaf kernel of `B -> O(2)`, `A -> tr(NA)`. Thus the degree-one term is the actual homogeneous nilpotent tangent sheaf, not a rank-based replacement. The scalar normalization can be chosen consistently throughout.

These are sheaf statements. They do not assert that taking this kernel commutes with fibers at the zero scheme, or that the evaluation map is locally surjective.

### 3. Derived shifts and all-degree vanishing

With `C` in degrees zero and one, the truncation triangle is correctly

    O(-4) -> C -> D[-1] -> O(-4)[1].

In this convention `D[-1]` is in degree one. Serre duality gives `H^i(O(-4))=H^(3-i)(O(1))*`; the positive line's higher-cohomology vanishing and its invariant-free `H^0` prove invariant acyclicity of the kernel. Before taking invariants, `H^3(O(-4))` need not vanish. Exactness of finite-group invariants over `C` makes the passage to the invariant hypercohomology legitimate. The proof therefore establishes vanishing in every degree, not only degrees zero through two.

The two short exact sequences give actual-map identifications `H^i(B(-2))^Gamma -> H^i(J_im)^Gamma -> H^i(G*)^Gamma`. In particular the nonzero invariant `H^1(J_im)` survives, exactly as stated.

### 4. Comparison of existing pairs and the fixed-bundle distinction

The Section 4 comparison is valid for existing determinant-fixed, tracefree nilpotent pairs with fixed reduction markings. Across the square-zero ideal, transition and adjoint differences have the asserted coefficients, quadratic products of differences vanish, and the equations are the total degree-one cocycle equations, up to a consistent sign. Changes of local identification give the corresponding total coboundaries. The vanishing of invariant degree-one hypercohomology gives an isomorphism; degree-zero vanishing makes it unique among determinant-preserving marked isomorphisms.

The coarse formulation is justified under the stated input `B=pi*B_Q`: exact tame pushforward preserves the tangent kernel, so it is unnecessary to posit an extension of the stack spinor itself to the coarse thickening.

This argument does not establish existence of a first-normal pair merely from homogeneous tangent vanishing. The proof explicitly requires existing pairs and cites the midpoint input for a reference object. Section 5's cancellation by a unique bundle-extension parameter is conditional on having established the relevant local lifts and affine overlap obstruction. On a prescribed bundle the obstruction remains in `H^1(G*)^Gamma`, rather than being discarded by allowing a change of bundle.

The warning about Hessian formulas is essential and correct: a local difference must have zero image in the generally nonzero sheaf `D` to be removable by a regular gauge. Global invariant acyclicity does not force every local residue to vanish or preserve prescribed local operator formulas.

### 5. Section 6: classical linearized equation complex

The displayed three-term complex is correctly described in the body as a **linearized equation complex**, not as a full derived cotangent or deformation complex. Its maps compose to zero, and its quotient by `C` is represented in degrees one and two by

    I_Z^2(2) -> O(2).

Consequently that quotient is quasi-isomorphic to `O_(2Z)(2)[-2]`, giving the asserted triangle and invariant hypercohomology identification. The twist is two, not one. The proof correctly does not import PR645's different-twist vanishing into these groups and explicitly disclaims a full derived-deformation or differential-operator interpretation.

## Scope retained

- No selected HM/source coefficients, point evaluation, numerical rank computation, or large computation was used.
- No claim of priority for the overlapping untwisted kernel lemma is needed for the negative-twist result.
- No conclusion about the positive-twist operator residue, arbitrary Hessian descent, higher normal lifts, or the absolute positive cubic obstruction follows from this review.
- The literal gauge term is tracefree because the determinant extension is fixed. If that condition is dropped, the central `O(-2)` gauge summand must be restored, although its acyclicity leaves the global vanishing conclusion unchanged.
