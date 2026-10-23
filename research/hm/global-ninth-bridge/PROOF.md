# The actual global-to-ninth cohomology bridge

Work over C with the actual normalized HM bundle F and B=End0 F. Let p:X=Bl_R(P4)->P4 be the blowup of the positive fixed plane, pi:X->T=P(W*) the negative hyperplane pencil, and E its exceptional plane divisor. Fibers of pi are P3, and D9=9E is the actual ninth Cartier neighborhood of R in those fibers. All eigenspaces below are for the central inversion in G=SL2(F5), with actual equivariant linearizations retained.

## 1. Exact inputs and result

INPUTS.json records six immutable originals in Akilleez-QA/read-em-and-weep:

- FINITE, PR986: the actual positive cohomology of B(2)|D9 has H1 bundle ker Theta, of rank18 degree42. Its positive H2 bundle is A O(14). Full-sheaf duality gives H9:=(R1pi_*B(3)|D9)_+=(ker Theta)*O(8). Every hyperplane has exactly three global B_H(3) sections, all positive squares.
- SUMMANDS, PR1032: the actual filtered geometry selects a split subbundle S5=A O(4) plus W O(5) in ker Theta. Its complement K13 has rank13 degree20. Equivalently H9 has selected W O(3) and A O(4) summands.
- OPPOSITE, commit48727e1f5fd5ab079c21b8b39af608f7d91fabab: the actual opposite cokernel is C=(R1pi_*p*B(3))_+, a vector bundle of rank5 degree26 on all of T. Its Sections1–4 retain the actual direct-image identification and global cohomology interfaces, not an abstract character substitute.
- TAIL, PR476 at3aa461bc3581fb72fbf923fbe869ddee023b435a, Section3: H3(P4,B(s))=0 for every s>=-1, proved from the functorial monad and Bott vanishing. In particular H3B(1)=H3B(2)=0.
- POLAR, PR952 at13d0e53e0a64ec6935a2ca83af776942e201c4e9, Section4: H2B(2)=0 and R2pi_*p*B(3)=R3pi_*p*B(3)=0.
- TWIST, PR455 at8cbbe482ee50c35d52ffcdf3efb837fa8cf96af4: H2B(1)=0 structurally.

Define the ACTUAL global positive cohomology bundle

    Jg=(R1pi_*p*B(2))_+.

We prove the two canonical exact restriction sequences

    0 -> Jg -> ker Theta -> C* O(8) -> 0,            (1)
    0 -> C -> H9 -> Jg* O(8) -> 0.                 (2)

They are compatible with full-sheaf relative duality. The first arrows are actual global-to-ninth restriction, not identifications based only on ranks. The bundle Jg has rank13 and degree28, is globally generated, and has its actual positive-parity Steiner presentation

    0 -> H1(B(1))_- O(-1) -> H1(B(2))_+ O
      -> Jg -> 0.                                  (3)

In particular the two coefficient spaces in (3) have dimensions28 and41. This deduces their sizes from the authenticated geometry and degree, without evaluating a multiplication map.

The bridge does NOT identify Jg with SUMMANDS' K13: their degrees are28 and20, respectively. Nor does it identify C with the entire finite cohomology H9.

## 2. Uniform global fiber vanishings

There are no global B_H(2) sections for any hyperplane in this pencil. If s were a nonzero such section, multiplication by s would inject H0(H,O_H(1)), a four-dimensional space, into H0(H,B_H(3)), a three-dimensional space by FINITE. The injection follows because H is integral and B_H is locally free: a nonzero linear form cannot annihilate a nonzero section. This contradiction is uniform and uses no selected hyperplane or section value.

The exact restriction sequence on P4 is

    0 -> B(1) -> B(2) -> B_H(2) -> 0.

H2B(2)=0 and H3B(1)=0 give H2(B_H(2))=0 for every H. Likewise H3B(2)=0 and H4B(1)=0 give H3(B_H(2))=0. The last vanishing follows from Serre duality H4B(1)=H0B(-6)*=0; stability of F forbids a map F->F(-6), hence also its trace-free subspace. Thus pi_*p*B(2)=R2pi_*p*B(2)=R3pi_*p*B(2)=0.

All these assertions hold on the full line, including the exceptional orbit. Proper flat cohomology and base change now show that R1pi_*p*B(2) is a vector bundle and commutes with base change: H0,H2,H3 vanish uniformly and the Euler characteristic is constant. Its positive direct summand Jg is therefore also a vector bundle. The analogous full R1pi_*p*B(3) is locally free: its H0 is uniformly three, while its R2 and R3 vanish by POLAR. This justifies use of ordinary dual bundles in the relative-duality calculation below.

## 3. The first actual restriction sequence and its parity

The projective-bundle and Cartier identities, with their linearizations, are

    omega_(X/T)=p*O(-4) tensor pi*O(1),
    O_X(E)=p*O(1) tensor pi*O(-1).

Consequently restriction of p*B(2) to D9 gives

    0 -> Z:=p*B(-7) tensor pi*O(9)
      -> p*B(2) -> B(2)|D9 -> 0.                  (4)

Relative Serre duality for the smooth relative threefold pi, using B*=B, pairs p*B(-7) with p*B(3) tensor pi*O(1). Because the relevant full cohomology bundles are locally free, it identifies

    R^i pi_* Z = (R^(3-i) pi_*p*B(3))* O(8).       (5)

In particular R0pi_*Z=R1pi_*Z=0 by POLAR, and

    (R2pi_*Z)_+ = C* O(8).

The positive sign here is important. The relative canonical factor O(1) has odd central character; the normal restriction factor O(9) is also odd. They cancel to the even O(8). Thus (5) pairs the positive source part with the positive B(3) cohomology, not with its opposite eigenspace. The same conclusion follows from the full equivariant relative-duality isomorphism before extracting eigenspaces.

Taking the long exact sequence of (4), using R1pi_*Z=0 and R2pi_*p*B(2)=0, yields exactly (1). FINITE identifies the middle finite cohomology with the actual ker Theta. Thus (1) is an exact sequence of vector bundles everywhere, not merely away from exceptional fibers.

The known ranks and degrees give

    rank Jg=18-5=13,
    deg Jg=42-(5*8-26)=28.                         (6)

## 4. The dual restriction sequence is also geometric

For clarity, derive the reverse bridge directly rather than declaring an abstract dual extension to be restriction. Restrict p*B(3):

    0 -> Z':=p*B(-6) tensor pi*O(9)
      -> p*B(3) -> B(3)|D9 -> 0.                  (7)

Full relative threefold duality pairs its first term with p*B(2), giving

    R^i pi_*Z'=(R^(3-i) pi_*p*B(2))* O(8).

The vanishings in Section2 imply R0pi_*Z'=R1pi_*Z'=0, and the positive R2 is Jg*O(8), with the same parity cancellation as before. Since R2pi_*p*B(3)=0, the long exact sequence of (7) is exactly (2).

Naturality of duality for the Cartier restriction triangles (4) and (7), with the adjunction identity omega_(D9/T)=p*O(5) O(-8), identifies (2) with the dual of (1) twisted by O(8). Equivalently the local residue pairing on O_R[z]/(z^9) pairs complementary normal orders summing to8 and the trace form pairs the B coefficients. This is a universal Cartier-thickening identity, not an evaluated actual jet. It also explains why the finite middle term is H9 and not global C itself.

The quotient in (2) has rank13 degree13*8-28=76. These degrees check against deg H9=18*8-42=102=26+76.

## 5. The global Steiner presentation

The universal hyperplane incidence in P4 times T gives the actual sequence whose first map is multiplication by its universal negative defining linear form:

    0 -> B(1) external O_T(-1)
      -> B(2) external O_T -> p*B(2) -> 0.

Here the last term is understood by pushforward from the incidence X. Applying the product projection, H0(B_H(2))=0 makes the map between the H1 coefficient bundles injective. TWIST gives H2B(1)=0, so its cokernel is exactly R1pi_*p*B(2), with no extra cohomology extension. The positive part is (3): the tautological negative equation contributes the odd line O(-1), so only H1(B(1))_- feeds the positive target H1(B(2))_+.

This is an actual bundle presentation. It proves global generation of Jg. Its degree is the dimension of the O(-1) source, and its rank is the difference of coefficient dimensions. Equation (6) therefore gives28 and41, respectively. No splitting of Jg is asserted. In particular its fiberwise injectivity is a consequence of the uniform zero sections proved in Section2, not a selected pencil-rank computation.

## 6. A first constraint on the selected finite summands

SUMMANDS supplies the actual split S5=A O(4) plus W O(5) inside ker Theta. Compose it with the quotient in (1):

    S5 -> C* O(8).

Both bundles have rank5, but their degrees are22 and14. The determinant is consequently a section of O(-8), and must vanish identically. Thus this actual map has rank at most4 generically, and its kernel is a nonzero subbundle of S5 lying inside the actual global Jg. This is a genuine finite/global compatibility condition, not a choice of an individual A or W channel. It does not determine the rank more precisely or say that either named summand maps to zero.

In particular the rank13 global bundle cannot simply be canceled against the rank13 residual K13 from SUMMANDS. Besides their degree difference, projection Jg->K13 has determinant in O(20-28)=O(-8), so is never a generic isomorphism. The forced nonzero intersection with S5 is the geometric reason such a cancellation is unavailable.

## 7. Contribution and limits

This resolves the missing actual finite/global comparison with complete parity, twists, uniform vanishings and natural maps. It identifies global cohomology as a subbundle of the finite kernel, proves an actual globally generated Steiner presentation, derives the dual restriction bridge, and supplies a first determinant constraint on the selected finite summands.

The individual maps from C into the selected A O(4) and W O(3) pieces of H9 remain unselected. Neither bridge is asserted split. No actual opposite type, top obstruction, vertex scalar, secondary torsion alternative, global source occurrence or source/catalogue exclusion follows. No selected actual HM/source coefficient, point, parameter, derivative, jet, matrix, instance rank or large scan was used.
