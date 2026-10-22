# The actual global weight-twelve quotient has a scalar splitting

## Statement and evidence boundary

Use the actual oriented vertex Serre frames, the global section sigma of G with regular zero scheme (a regular pair on the vertex cover), det G=O(2), and the marked cubic/quintic pair sigma=(f,g). All physical twists are as in PR543 at 3d21e93865152ec961ceaf32d48f845399158b69. Let L=P(W), and write Wprime for the positive binary representation. The coefficient sequence proved there is

    0 -> E4 -> E12 -> V O_L(4) -> 0,

where E4 is the weight-four coefficient of End_0(G)(4), and E12 is the weight-twelve coefficient of G(4). Denote its quotient map by pi.

There is an actual, marked global coefficient-quotient map

    r12: H0(G(4)) -> H0(V O_L(4)).                     (A)

It is defined even when a section has a nonzero weight-four component: the weight-twelve component need not glue in E12, but its quotient does. Map (A) is surjective and has an explicit splitting by global scalar multiples of sigma. The splitting is the positive-coordinate-degree-two, negative-coordinate-degree-two summand U22 of H0(O_Q(4)), followed by multiplication by sigma. In particular dim U22=15, and

    r12: sigma U22 -> H0(V O_L(4))

is an isomorphism. These scalar corrections do not alter any lower vertex weight. A fixed source problem can use this normalization only if its allowed changes include the corresponding scalar correction. No prescribed source, first error, next error, or obstruction value is evaluated here.

## 1. Pinned geometric inputs

All four files below are under research/hm/order-four-quadratic-load/ in Akilleez-QA/read-em-and-weep, at commit 3d21e93865152ec961ceaf32d48f845399158b69:

- ACTUAL-NEXT-WEIGHT-SEPARATES-MIDPOINT-NORMALIZATION-FROM-ENDPOINT-TRANSPORT.md, Sections 3.2 and 4: the actual conic restriction, coefficient sequence, and warning about lower-weight mixing.
- MIDPOINT-HESSIAN-SYMBOL-MATCHING-BY-FULL-FRAME-COVARIANCE.md, Section 2: actual normalized transitions are the homogeneous marked transitions followed by determinant-one stabilizers of the exact pair sigma.
- REGULAR-SERRE-STABILIZERS-HAVE-ZERO-NORMAL-DEFECT-RESIDUE.md: every such stabilizer is exactly I+t n, n=sigma sigma^t J, with t regular.
- UNIVERSAL-CUBIC-EVEN-DEFECT-QUOTIENT-IS-TRIVIAL-V.md: the everywhere-exact cubic quotient, twisted here to

    0 -> Wprime O_L(-1) --f--> Sym4(Wprime) O_L(2)
      -> V O_L(4) -> 0.                              (B)

We use the fixed block decomposition of the quadric coordinate ring: the equation involves only the three positive coordinates, while the two negative coordinates give the vertex line. Thus degree-d pure-positive forms modulo the conic equation identify with Sym^(2d)(Wprime). This is the same actual coordinate-ring input used in the pinned conic argument, not a new splitting of G.

## 2. The lower-weight mixing dies in the quotient

For v in G(4), its weight-w components have cover degrees w-5 and w-3. In the even-weight sector under consideration the first possible weight is four, with

    v4=(0,ell),  ell in Wprime O_L(1).

If other parity sectors are included, they cannot contribute to the even weight-twelve component, since ordinary transitions have even weights. The regular scalar t has nonnegative cover degree. Its first possible contribution t0 n therefore increases chain weight by eight. The only lower component that can mix into weight twelve is v4.

On an overlap, first transport by the homogeneous marked transition and then write the remaining actual transition as I+t n. Suppressing the already transported source notation, its exact contribution to v12 is

    t0 n v4 = sigma p_mix,  p_mix=-t0 f ell.         (C)

The displayed sign uses J=[[0,-1],[1,0]] and n=sigma sigma^t J; changing the uniform sign convention does not change the image. Because n has physical twist two, t0 has physical twist minus two. Thus t0 ell belongs to Wprime O_L(-1), and p_mix belongs to precisely the f-image in (B).

Equivalently t0 n v4=-(t0 tau(v4))sigma, where tau(v)=sigma v^t J+v sigma^t J; t0 tau(v4) has physical twist four and chain weight four, so this is in the image E4 sigma. Hence pi annihilates the entire inhomogeneous term (C). The local sections pi(v12) therefore glue, proving (A). This retains the lower weight-four mixing rather than assuming it absent.

The result is intrinsic relative to the fixed homogeneous pair markings and physical frames. It does not assert invariance under changing that marking by arbitrary nonhomogeneous generator changes. Changes of actual oriented frames preserving the fixed pair are exactly the stabilizers just handled.

## 3. Conic regularity forces the local coefficient to be scalar

For a global actual v, the wedge sigma wedge v is a global section of I_Z(6). The normalized sigma is exactly the homogeneous pair, so its cover-degree-twelve coefficient is exactly sigma wedge v12. The stabilizer mixing in (C) has zero wedge, so this coefficient is genuinely global even if v12 is not.

Since C is contained in Z, sigma wedge v vanishes on the fixed positive conic C. Its degree-twelve positive-cover component is the pure-positive sextic part of a global degree-six coordinate-ring section. Restriction of that summand to C is an isomorphism; every term containing a negative coordinate restricts to zero. Consequently

    sigma wedge v12=0.

The regular-pair Koszul identity now gives, uniquely on each vertex chart,

    v12=sigma p4,  p4 in Sym4(Wprime) O_L(2).       (D)

Uniqueness is literal before quotient: multiplication by the regular pair has no kernel. The p4 cochain need not be a global section of that bundle: its overlap defect is exactly the f multiple in (C). Its image in (B) is r12(v).

If v4=0, the mixing vanishes. Then p4 is global, and (B), together with H0(O(-1))=H1(O(-1))=0, implies

    r12(v)=0 if and only if v12=0.                 (E)

Without v4=0, equation (E) must not be asserted. The exact replacement is that the local p4 values lie in f·Wprime O(-1); their affine overlap defect still records v4 and the actual stabilizers.

## 4. Global scalar splitting and exact normalization

The block-bigraded piece

    U22 = (positive quadratics modulo the quadric equation)
             tensor (negative quadratics)
        = Sym4(Wprime) tensor Sym2(W)

is an actual subspace of H0(O_Q(4)), of dimension 5·3=15. The defining equation is purely positive, so this is a genuine direct summand of the graded coordinate ring. Under vertex restriction its coefficient map is the isomorphism

    U22 -> H0(Sym4(Wprime) O_L(2)).                 (F)

For u in U22, the global section sigma u has only weight twelve in the exact homogeneous pair frames. Thus it has v4=0 and does not change any weight below twelve. Its image under r12 is exactly the composition of (F) with H0 of the quotient arrow (B). Both maps are isomorphisms, proving the stated scalar splitting.

For any global v there is therefore a unique u in U22 such that

    r12(v-sigma u)=0.                              (G)

This gives the split vector-space exact sequence

    0 -> ker r12 -> H0(G(4)) -> H0(V O_L(4)) -> 0.

For v4=0 the normalized section has literally zero weight-twelve coefficient by (E). For general v, (G) kills the quotient, not necessarily the local coefficient. The latter distinction is exactly the surviving affine lower-weight transport.

## 5. Fixed-source criterion and relation to earlier scalar elimination

Suppose a fixed-source construction has a reference global tangent lift v and allows scalar corrections sigma u only for u in a specified linear subspace A of H0(O_Q(4)). Let pr22 denote its block-bidegree-(2,2) projection. Then

    r12(sigma A) = H0(B)(pr22 A),

where H0(B) denotes the isomorphism in (B) composed with (F). The quotient can be normalized to zero within the allowed scalar freedom if and only if

    r12(v) belongs to H0(B)(pr22 A).                (H)

For the actual tangent-error convention R1=tau(v), this scalar freedom has a precise operator meaning: tau(sigma)=2n. Changing the first-normal scalar coefficient Lambda1 by a global lambda in H0(O_Q(4)), while holding the other data fixed, changes R1 by -lambda n and hence v by -(lambda/2)sigma. Therefore the U22 correction in (G) is realized by delta Lambda1=2u, provided that change is permitted by the prescribed source/scalar lift. This is a conditional action formula, not permission to change a fixed Lambda1. It also checks the physical twist: lambda has twist four and n twist two, matching R1 of twist six.

If changes must preserve all lower weights, restrict A to scalars with no cover degree below four. Full U22 remains sufficient. When U22 is allowed, the normalizing correction within U22 is unique; a larger allowed space can retain additional choices in the kernel of pr22. If the source fixes the scalar lift, A may be zero; none of the unrestricted surjectivity licenses altering it.

The earlier [positive-boundary theorem, Section 3](https://github.com/Akilleez-QA/read-em-and-weep/blob/83eb365e87fe3aef3488aa339b73636fa845f630/research/hm/positive-boundary-duality/PROOF.md) already proves that global quartic scalar rescalings kill the scalar layer of the full defect. The new result here is the precise marked weight-twelve restriction map, its descent despite weight-four mixing, its explicit fifteen-dimensional scalar splitting, and criterion (H). It does not claim that scalar liftability itself was previously unknown.

Finally, this does not contradict the pinned exclusion of global K4 adjoint ambiguities. That argument uses the trace map on E4, whose tangent kernel Wprime O(-1) is acyclic. Here global G(4) sections have the additional sigma-scalar kernel Sym4(Wprime) O(2), and its quotient is the entire fifteen-space. Conic regularity kills the wedge, not this scalar kernel. Neither assertion computes the actual first-error section or actual R2.

## Reproduction

Run `python verify.py`. It checks the universal stabilizer formulas, their exact sign, coefficient-line arithmetic, the unique retained mixing weight, and the cohomology/dimension arithmetic. The global extension and conic arguments are mathematical proofs above, not consequences of a numerical rank test.
