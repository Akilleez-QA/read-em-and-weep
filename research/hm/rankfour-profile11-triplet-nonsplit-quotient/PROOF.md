# Orthogonal reduction forces the residual rank-two quotient to be nonsplit

## Statement and scope

Retain the actual-geometric hypotheses of the complete mixed-jet-pairing and rank-six-common-kernel inputs, including all their transitive assumptions. Assume precisely the residual simultaneous rank-seven image case: original local delta=12, I6=E6(-D12), and the forced lower-column k=2 flag. The actual quotient

    M=F6/U4,  0 -> O(-10) -> M -> O(-8) -> 0

is necessarily the nonzero extension

    M = W(-9).                                            (1)

In particular the formerly retained split alternative O(-10)+O(-8) is excluded in this conditional case. The proof also determines two actual quotients:

    T5^(perp_h)/T5 = V_alt O,
    B6/U5 = W'(-3),
    B6/U4 = O(-8) direct-sum W'(-3).                       (2)

Here h is the actual symmetric constant pairing already constructed in the mixed-jet proof, Uj=h(Tj), V_alt is the nonstandard three-dimensional even irreducible, and W' is the nonstandard two-dimensional spin irreducible. All quotient identifications preserve the actual indicated subbundles; no quotient receives a connection and no displayed splitting is asserted horizontal.

This removes one conditional rank-two quotient, not the simultaneous image itself, the alternative cyclic rank-seven image, original delta=12, the separate e9 endpoint, either F18 form, or any whole branch/profile. No remaining case is asserted to occur. No original jets beyond the already proved order nine, algebraicity, or selected actual coefficient, parameter, point, jet, tensor, matrix, instance rank, or invariant normalization is used.

## 1. Complete inputs and actual flags

INPUTS.json records the complete freshly fetched immutable originals, exact commits, repository paths, UTF8 lengths, SHA256 hashes and Git blobs. The direct originals are the mixed-jet-pairing proof and PR1219 at 95137a91303d46fd945f5a2d0fed330f0e32df8c, research/hm/rankfour-profile11-triplet-ranksix-common-kernel/PROOF.md. The mixed-jet original is PR1221 at 84b418e22f03b5718409bdeb23ae353ecc4eb681, research/hm/rankfour-profile11-triplet-mixed-jet-pairing/PROOF.md.

We work over C on the physical binary-icosahedral line, G=SL2(F5), det W=1. Put A=Sym2 W, S4=Sym3 W, D=Sym4 W, T6=Sym5 W. All named irreducibles are self-dual. The scalar characters of G are trivial, and the central element acts trivially on the constant representation

    V=A+V_alt+D+P,  dim V=15.                              (3)

The original actual degree-eighteen jets and their annihilators satisfy

    Tj=Symj W(j-18) subset V O,  0<=j<=9,
    Bj=ann(Tj) subset V* O.                                (4)

In particular T6/T5=O(-6), T5/T4=O(-8). The mixed-jet theorem supplies an actual constant equivariant nondegenerate symmetric isomorphism h:V->V*, with the auxiliary scalar curve u=h v and actual Uj=h(Tj) through order nine. Its nonzero biform has the expression

    <v(x),h v(y)> = Omega(x,y)^12
        [a Polar_(6,6)(f12)(x,y)+b Omega(x,y)^6], a!=0,     (5)

up to fixed nonzero universal conventions. Here f12 is any nonzero vector in the fixed one-dimensional universal invariant space (Sym12 W)^G, never a selected actual HM coefficient. Its divisor is the reduced orbit D12. Neither a, b nor a normalization is selected or evaluated.

The rank-six theorem gives actual saturated inclusions and coherent images

    U4 subset G6 subset F6 subset B6,
    G6=U4 direct-sum L10, L10=O(-10),
    F6/G6=O(-8), B6/F6=O(4),
    U4=D(-14), U5=T6(-13),
    beta_(F6)(U4)=O(-10) in the lower column of
    I6=O(-8)+O(-10).                                      (6)

The formula for U5 in (6) uses the subsequent mixed-jet result, not a full-span assertion imported from the rank-six proof. The lower image in (6) is an exact nonzero coherent image. It is not replaced by its saturation O(2).

## 2. A three-dimensional orthogonal quotient and its norm

Equation (5) vanishes on the diagonal to order at least twelve. Consequently the pairing of original jets of orders i and j vanishes whenever i+j<=11. This is a formal derivative consequence of the displayed biform, valid identically along the base, not an evaluation at selected points.

Thus T5 is isotropic, and T6 is contained in its orthogonal complement. The quotient

    H=T5^(perp_h)/T5                                      (7)

is a rank-three degree-zero vector bundle with a nondegenerate symmetric pairing. Indeed T5 is saturated in the constant bundle, and nondegeneracy of h makes V O -> T5* surjective. Its kernel is T5^(perp_h); quotienting this kernel by T5 leaves a nondegenerate pairing. The rank is 15-2*6=3 and the degree is zero.

The actual line

    N=T6/T5=O(-6) subset H                                (8)

is saturated, because T6 is saturated in V O. Its restricted quadratic norm is nonzero and proportional to f12:

    N tensor N -> O corresponds to c f12, c!=0.          (9)

For completeness, differentiate (5) six times in each formal affine variable and then restrict to the diagonal. The Omega^18 term vanishes. In the other term all twelve derivatives must strike Omega^12; this contributes a nonzero universal factorial, times a times the diagonal of Polar_(6,6)(f12), namely f12. Lower-jet modifications do not change the norm because all pairings of total order at most eleven vanish. This proves (9) without choosing coefficients, points, or a normalization. Nonzero norm means generically nonisotropic; it is not claimed nonzero on D12.

The equivariant Euler character of (7) is fixed. Since T5=T6(-13), additivity and Serre duality give

    chi_G(H)=V-chi_G(T5*)-chi_G(T5)
       =A+V_alt+D+P - T6 tensor Sym13 W
                           + T6 tensor Sym11 W
       =V_alt.                                           (10)

The last equality is a fixed universal representation identity, checked by the bounded character recursion and independent review. The two signs in (10) use chi(O(-13))=-Sym11 W and chi(O(13))=Sym13 W.

## 3. The orthogonal quotient must be constant

Self-duality of the ordinary rank-three degree-zero bundle H makes its Birkhoff degrees symmetric. Hence either H is ordinary trivial, or its degrees are (d,0,-d) with d>0. In the latter case the three distinct-degree Harder-Narasimhan graded lines are equivariant scalar lines. Their linearizations have no nontrivial character, and the physical central action forces d even.

Suppose d>6. The composite N=O(-6)->H->O(-d) is zero by degree, so N maps into the canonical nonnegative Harder-Narasimhan subbundle H_(>=0). Its composite with H_(>=0)/O(d)=O is zero because

    Hom_G(O(-6),O)=(Sym6 W)^G=0.

Thus N maps into the positive line O(d), which is isotropic: a pairing O(d) tensor O(d)->O is zero by degree. This contradicts (9). This uses only the canonical filtration and does not require an orthogonal or horizontal splitting.

Therefore a nontrivial H would have d=2,4,6. Its Euler character, determined by its actual equivariant graded lines, would be

    1+Symd W-Sym(d-2) W.

For d=2,4,6 these are respectively

    A,  1+D-A,  1+V_alt+P-D.                             (11)

None equals V_alt, contradicting (10). Hence H is ordinary trivial. Evaluation H0(H) tensor O -> H is then a canonical equivariant isomorphism, and (10) identifies its constant multiplicity representation:

    H=V_alt O.                                           (12)

No ordinary Birkhoff complement is called canonical; only this trivial-bundle evaluation and the earlier canonical filtration are used.

## 4. The actual perpendicular kernel has type W'(-3)

The nondegenerate pairing on H and the saturated inclusion N give a surjection H->N*=O(6). Set R=N^perp in H. Then

    0 -> R -> V_alt O -> O(6) -> 0.                     (13)

This is an everywhere exact sequence despite the zeros of the norm (9). Surjectivity follows from nondegeneracy on the whole H and the fiberwise injectivity of N, not from its restricted norm. Therefore R has rank two, degree -6 and ordinary top degree at most zero.

Under the actual h identification, T5^(perp_h) maps to B5, and T6^(perp_h) maps to B6. Since T5 pairs trivially with T6, quotienting by h(T5)=U5 gives the actual identification

    R=B6/U5.                                             (14)

If R has unequal Birkhoff degrees, write them e and -6-e with e>-3. Its canonical top line is a scalar equivariant O(e), with -2<=e<=0. None can inject into V_alt O equivariantly, since

    Hom_G(O(e),V_alt O)
      =(V_alt tensor Sym(-e) W)^G=0, e=-2,-1,0.          (15)

Thus the ordinary type is 2O(-3). Twisting (13) by three and taking Euler characters identifies its constant multiplicity representation:

    H0(R(3))=chi_G(R(3))
       =V_alt tensor Sym3 W - Sym9 W = W'.              (16)

Consequently the actual quotient (14) has type W'(-3). This derivation does not infer the quotient's type from the generic norm alone.

## 5. The actual three-dimensional quotient splits uniquely

Let E=B6/U4 and let A8=U5/U4=O(-8) be its given subline. By (14),

    0 -> A8 -> E -> R=W'(-3) -> 0.                      (17)

Its equivariant extension group vanishes:

    Ext1_G(W'(-3),O(-8))
      =H1(W'(-5))^G=(W' tensor Sym3 W)^G=0.             (18)

The splitting section is unique because Hom(W'(-3),O(-8))=0 by degree. We thus have a unique actual equivariant splitting of (17), relative to the specified A8,

    E=A8 direct-sum R.                                  (19)

The line L10=G6/U4 is a saturated subline of E, because E/L10=B6/G6 is a vector bundle. Its component to A8 in (19) vanishes by

    Hom_G(O(-10),O(-8))=(Sym2 W)^G=0.

It therefore lies in the actual R component and is saturated there. Determinants give the everywhere exact extension

    0 -> L10=O(-10) -> R=W'(-3) -> O(4) -> 0.           (20)

Its extension class c is nonzero: the middle ordinary bundle 2O(-3) is not O(-10)+O(4). The class belongs to the one-dimensional space

    Ext1_G(O(4),O(-10))=H1(O(-14))^G,
    dim H1(O(-14))^G=dim (Sym12 W)^G=1.                (21)

No actual matrix or representative of c is chosen. Quotienting (19) by its actual L10 produces

    E/L10=B6/G6=A8 direct-sum O(4).                     (22)

The first line here comes from U5/U4, not from F6/G6; these two actual O(-8) sublines need not coincide.

## 6. The actual F6 graph has a nonzero invariant component

Let N8=F6/G6=O(-8), a saturated subline of (22). Its projection to A8 is a scalar. It cannot be zero: otherwise its only component would be a map O(-8)->O(4). Every nonzero such equivariant map is a multiple of f12 and has the nonempty divisor D12, so it would not be a subbundle of (22). The zero map cannot be an inclusion either. Thus the projection to A8 is an isomorphism.

Use that actual isomorphism to express N8 as the graph of a map

    phi:A8=O(-8) -> O(4),  phi=lambda f12.              (23)

This notation selects no value of lambda or normalization of f12. In fact lambda is nonzero. If phi were zero, the preimage of N8 in B6 would be U5+L10, so F6=U5+L10 and U5 would lie in F6. But then the lower component of beta_(F6)|U5 would be an equivariant map

    U5=T6(-13) -> O(-10)

into the coherent lower summand in (6). Its Hom is

    Hom_G(T6,Sym3 W)=0.

It would vanish, contradicting the exact nonzero lower image beta_(F6)(U4)=O(-10), since U4 subset U5. This proves phi!=0 using the actual derivative and its coherent image. It does not confuse a projected D12 zero with intrinsic ramification.

## 7. Pullback of the nonzero extension cannot split

Inside E=A8+R, the actual subbundle M=F6/U4 is the full inverse image of the graph (23) under E->A8+O(4). It contains L10, and the quotient M/L10=N8 maps isomorphically onto A8. Thus its given extension

    0 -> L10 -> M -> A8 -> 0

is precisely the pullback of (20) along phi, with class phi* c. On cohomology the pullback is multiplication by phi:

    H1(O(-14))^G -- times lambda f12 --> H1(O(-2))^G.   (24)

This is an isomorphism of one-dimensional vector spaces. Indeed Serre duality makes its dual the map

    H0(O)^G -> H0(O(12))^G,  1 |-> lambda f12,          (25)

which is nonzero by (23). The finite-group invariant pairing remains perfect by averaging, so (25) proves (24) nonzero without evaluating any apolar pairing or actual coefficient. Since c!=0, its pullback is nonzero.

For clarity, the nonzero extension in Ext1_G(O(-8),O(-10))=H1(O(-2))=C has middle type W(-9). Twist by nine. The standard equivariant Euler sequence

    0 -> O(-1) -> W O -> O(1) -> 0

represents a nonzero class, and every nonzero class is isomorphic after an automorphism of an endpoint, because the extension space is one-dimensional. Hence (1) follows.

## 8. Contribution and retained open cases

The new obstruction is not an abstract reclassification of two possible bundles. The symmetric mixed pairing forces the actual orthogonal quotient (12), hence the actual perpendicular rank-two quotient (14). The unique extension splitting (19) and the actual derivative force a nonzero graph (23). Its pullback acts nontrivially on the one-dimensional invariant Ext space, excluding the split M.

Only the split rank-two quotient inside the residual simultaneous k=2 case is excluded. The remaining M=W(-9), the simultaneous image, the cyclic rank-seven image, delta=0 or12, original t=0, the independent e9 endpoint, both F18 forms, realization, algebraicity and whole-profile questions remain distinct and unresolved. The argument assumes the actual original and auxiliary jets only through the already established orders and never chooses an actual source instance.
