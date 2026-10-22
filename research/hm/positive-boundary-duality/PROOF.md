# The positive operator boundary is a 35-to-4 restriction defect

## New result and scope

Work on the smooth weighted stack X=P(1,1,2,2), using physical O_X(1)=O_wt(2). Let G be the actual Serre rank-two bundle, det G=O(2), with regular section sigma and zero scheme Z. Let B=End_0 G, M=omega_(2Z)(1), where 2Z is the ORDINARY square I_Z^2. Physical inversion-even parts are denoted +; these are not local stack stabilizer invariants. Let

 delta:H0(M(4))_+ -> H1(B(4))_+=P4

be the specified midpoint operator boundary of [ACTUAL-THIRD-VALUE-AS-MIDPOINT-DUALIZING-OPERATOR-DEFECT.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/8c26de8e5e68fd41945373ac1f6ee280f109d716/research/hm/order-four-quadratic-load/ACTUAL-THIRD-VALUE-AS-MIDPOINT-DUALIZING-OPERATOR-DEFECT.md).

Then delta is SURJECTIVE. More strongly, its entire scalar-rescaling subspace H0(O_Z(4))_+ is killed, not just the reduced-conic contribution. It descends to a canonical surjection

 d:H0(G|Z(4))_+ -> P4,
 ker d = im[H0(G(4))_+ -> H0(G|Z(4))_+].             (A)

The source in (A) is vertex-supported and is exactly

 A + 2V + 4P4 + 2D5, of dimension 35.

Thus the actual global restriction image has dimension 31 and representation

 A + 2V + 3P4 + 2D5.                               (B)

This removes the scalar-rescaling layer of the full nonreduced defect and identifies the remaining global quotient with an ordinary evaluation defect on Z. It does NOT compute the image of the actual operator residue in this quotient. In particular it proves neither absolute cubic vanishing/nonvanishing nor a third Bockstein value modulo the second-symbol image, and makes no higher-lifting claim.

## 1. Pinned inputs

All cone files below are at commit 8c26de8e5e68fd41945373ac1f6ee280f109d716, under research/hm/order-four-quadratic-load/ in Akilleez-QA/read-em-and-weep.

1. [WEIGHTED-STACK-SQUARE-SHADOW-AND-PRIMARY-SCALAR.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/8c26de8e5e68fd41945373ac1f6ee280f109d716/research/hm/order-four-quadratic-load/WEIGHTED-STACK-SQUARE-SHADOW-AND-PRIMARY-SCALAR.md) proves H1(G(2))=0 and H^i(G(2))=0 for i>=2, as well as H1(B(4))_+=P4 and H^i(B(4))=0 for i>=2. It proves the ordinary-square sequence and computes H0(E tensor T(1))_+=A+2V+4P4+2D5, H1(E tensor T(1))=0. Here E=F_Q(2), S_hat=O_wt(1), T=pi_*(O_Z S_hat(2)).
2. [ACTUAL-THIRD-VALUE-AS-MIDPOINT-DUALIZING-OPERATOR-DEFECT.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/8c26de8e5e68fd41945373ac1f6ee280f109d716/research/hm/order-four-quadratic-load/ACTUAL-THIRD-VALUE-AS-MIDPOINT-DUALIZING-OPERATOR-DEFECT.md) gives the actual boundary from the complete commutator sequence and the intrinsic filtration 0->O_Z->M->G|Z->0. The first map is represented by sigma/2; the harmless 1/2 is fixed by tau(sigma)=2N.
3. [GLOBAL-NORMAL-ADJOINT-DEFECT-DUALIZING-TWIST.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/8c26de8e5e68fd41945373ac1f6ee280f109d716/research/hm/order-four-quadratic-load/GLOBAL-NORMAL-ADJOINT-DEFECT-DUALIZING-TWIST.md) identifies M=omega_(2Z)(1), with omega_X=O(-3), equivariantly for the finite group.
4. The primary support facts H1(F(t))=0 outside t=0,1,2,3 and H2(F(t))=0 outside t=-2 are stated explicitly in Section 1 of [the actual primary-image extension proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/d5d9bd997145b0ecf7d7bd659a19fb7845afb75f/research/hm/actual-primary-image-extension/PROOF.md). They are the established HM primary cohomology input, not a new assumed rank calculation.

All uses of these cohomology statements are after exact tame coarse pushforward. In particular no noninvertible coarse spinor is naively pulled back.

## 2. The additional positive Serre-bundle vanishing

The spinor resolution and projection formula give, for every integer t,

 0 -> W' tensor F(t) -> W' tensor F(t+1)
   -> i_* pi_*G(t) -> 0.                           (1)

Indeed G(t)=pi^*F_Q tensor S_hat(1+t), since G=pi^*F_Q(2) tensor S_hat^(-1) and S_hat^2=O(1). For t=2 this is exactly the already used primary spinor sequence. For t=4, the primary support facts applied to H1(F(4)), H1(F(5)), H2(F(4)) imply

 H1(G(4))=0.                                      (2)

No positivity shortcut is used.

## 3. Every scalar class is a global quartic rescaling

Twisting the actual Serre sequence gives

 0 -> O(2) -> G(2) -> I_Z(4) -> 0.

Line-bundle intermediate vanishing on the weighted projective stack, together with the pinned G(2) cohomology and H3(O(2))=H0(O(-5))*=0 by weighted-stack Serre duality and the absence of negative-degree polynomial sections, yields

 H1(I_Z(4))=H2(I_Z(4))=0.

The ideal sequence therefore gives

 H0(O(4)) -> H0(O_Z(4)) onto, and H1(O_Z(4))=0.     (3)

Thus every scalar class in the intrinsic filtration of M(4) is represented by a global rho sigma/2 in G(4). Exactness of the defining boundary proves that delta kills the ENTIRE H0(O_Z(4)), with its nonreduced vertex part retained. This extends the earlier conic-only exclusion. No assertion that Z is reduced is involved.

The same filtration and (3) give a surjection

 H0(M(4)) -> H0(G|Z(4)).                           (4)

Consequently delta descends uniquely to d. The complete commutator sequence and (2) show delta is onto P4, so d is onto as well. To identify its kernel, lift a section of G|Z(4) to M(4). If d kills it, the lift is the image of a global G(4) section by exactness of delta. Conversely every such restriction is killed. This proves (A), without choosing a splitting of either filtration.

## 4. Independent Koszul derivation of the quotient

The regular-section Koszul sequence tensored by G(4) is

 0 -> G(2) -> End(G)(4) -> I_Z G(4) -> 0.           (5)

The pinned positive-degree cohomology vanishing of G(2), and End(G)=O plus B in characteristic zero, identify

 H1(I_Z G(4))_+ = H1(B(4))_+ = P4.

Now apply cohomology to

 0 -> I_Z G(4) -> G(4) -> G|Z(4) -> 0.

Equation (2) gives exactly (A). The map agrees, up to the single uniform normalization factor in sigma/2, with the boundary obtained in Section 3: locally the tracefree evaluation X->X sigma and full endomorphism evaluation differ only by their scalar evaluation rho sigma. Passing to the quotient G|Z kills precisely the latter. This independently checks the actual evaluation interpretation, not just its dimension.

## 5. Exact source, global image, and support

There is an equality of actual sheaves after coarse pushforward

 pi_*(G|Z(4)) = E tensor T(1),

because S_hat^(-1)(4)=S_hat(3). This is the conormal sheaf already computed in the pinned square-shadow note, not an associated-graded replacement. Its conic contribution is W tensor O_P1(10), which is physical inversion-odd. Its positive vertex source is therefore exactly

 H0(G|Z(4))_+ = A+2V+4P4+2D5.

Equation (A) now gives (B) by semisimplicity. Representation notation here specifies isomorphism type; it does NOT choose three particular P4 copies inside the four-copy isotypic component. The non-P4 components are killed canonically. What remains is one actual nonzero functional on the four-dimensional P4 multiplicity space, tensored with id_P4. Replacing it by any chosen coordinate projection would be unjustified.

### A dimension check retaining the removed layer

The same Serre sequence gives H0(I_Z(4))_+=0: its preceding injection H0(O(2))_+ -> H0(G(2))_+ identifies two copies of A+D5. Hence H0(O_Z(4))_+=H0(O(4))_+, whose dimension is

 5 + 5*3 + 9 = 29.

These are respectively negative-coordinate degrees four, two, and zero of a physical even quartic. Therefore the full source has dimension 64, the image H0(G(4))_+ in it has dimension 60, and the intrinsic scalar elimination reduces this 64/60 quotient to the 35/31 quotient above. Independently, (5) gives h0(I_Z G(4))_+=29 from 37-8. These equalities check that no scalar or conic contribution was silently dropped.

## 6. The transpose is the actual ordinary-square cohomology map

Proper duality on 2Z identifies H0(M(4))* with H1(O_(2Z)(-5)); Serre duality on X identifies H1(B(4))* with H2(B(-7)), using the trace pairing. The transpose of delta is, up to its uniform boundary-sign/normalization convention, the following composite:

 P4* = H2(B(-7))_+
   -> H2(I_Z^2(-5))_+
   = H1(O_(2Z)(-5))_+.                           (6)

The first arrow is induced by the actual symmetric-square quotient

 0 -> G(-9) -> B(-7) -> I_Z^2(-5) -> 0,            (7)

and the second is the inverse boundary for 0->I_Z^2(-5)->O(-5)->O_(2Z)(-5)->0. The H1 and H2 of O(-5) vanish. To verify (6), dualize the full locally free resolution

 0 -> O(2) -> B(4) -> G(4) -> M(4) -> 0

against omega_X. Its dual complex is

 G(-9) -> B(-7) -> O(-5),

with image of the second arrow I_Z^2(-5) and final cohomology O_(2Z)(-5). Locally that arrow is the lower quadratic component beta f^2-2alpha fg-gamma g^2, with the trace-pairing convention; hence it is the actual ordinary-square map rather than a map identified only by source/target characters. Naturality of the cohomology/duality spectral sequence gives (6). In particular delta* is injective by the proved surjectivity.

The scalar exclusion has a precise dual strengthening. Adjunction on the lci curve Z gives omega_Z=O_Z(-1). Hence H0(O_Z(-5))=H1(O_Z(4))*=0 by (3). In the conormal sequence

 0 -> G*|Z(-5) -> O_(2Z)(-5) -> O_Z(-5) -> 0,

we get an injection

 H1(G*|Z(-5)) -> H1(O_(2Z)(-5)).                   (8)

The dual of the restriction O_(2Z) -> O_Z is the canonical inclusion omega_Z -> omega_(2Z). After twisting by five, its image is precisely the scalar submodule O_Z(4) -> M(4): locally the latter is the class of fg in I/(f^2,g^2), and the elements annihilated by I=(f,g) are exactly its multiples. Thus this identification agrees with the fixed scalar-filtration map up to its uniform normalization and does not merely compare isomorphic line bundles. Consequently, because delta kills that scalar submodule, its transpose annihilates the corresponding quotient cohomology. The image of delta* lies in (8). Under duality on Z its preimage is precisely the injective transpose of d:

 P4* -> H1(G*|Z(-5))_+ = H0(G|Z(4))_+*.

Thus the actual four-dimensional dual test lives in the conormal cohomology, not in the reduced-structure quotient. This is an intrinsic containment, independent of choosing local f,g or a quintic-generator splitting.

## 7. Consequence for the specified operator and remaining task

For the actual r(a,h) supplied by the midpoint comparison, set v(a,h) to its image in H0(G|Z(4))_+. Then

 Psi(a,h,t(a))=d(v(a,h)).

Any change of r by a class from H0(O_Z(4)) is irrelevant automatically, even if supported nontrivially on the vertex. The absolute vanishing test is now exactly whether v lies in the 31-dimensional actual evaluation image in (B), equivalently whether it annihilates the canonical four-space (6)/(8).

This removes a whole intrinsic filtration layer and proves that the global quotient is exactly P4. It does not establish the value of this pairing on v, identify its four-copy multiplicity functional by representation theory alone, or substitute the ordinary square for the ambient thickening 2Q. No selected actual HM coefficients, points, matrices, ranks, scans, or large computations were used.
