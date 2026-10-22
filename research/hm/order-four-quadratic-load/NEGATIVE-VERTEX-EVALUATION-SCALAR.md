# Reduction of negative-vertex evaluation to one scalar

## Subsequent resolution

NONZERO-VERTEX-EVALUATION.md at commit c779b2919a36b9d45a6319d46551bd6380154bba proves this scalar is nonzero by reduced-section classification and factor descent. Vertex evaluation has rank one everywhere, and the actual multiplicity map d_W has rank two. The reduction and failed dimension-only arguments below remain valid; statements that the scalar is unresolved describe the endpoint of this earlier argument.

## Checked conclusions

Let L=P(W*) be the negative fixed line and H_lambda=P(V_+ directsum lambda). Normalize the HM linearization so F_R is positive on the fixed plane R. Let

    Y_lambda=H0(F_Hlambda(2)),
    Y=O_L(-3) tensor W,
    A=Sym^2 W,   D=Sym^4 W.

The actual splitting, with inversion characters, is

    F|L=O_L(3)_- directsum O_L(-4)_+,
    F|L(2)=O_L(5)_- directsum O_L(-2)_+.              (1)

Consequently the family vertex evaluation factors as

    ev:Y -> O_L(-2).                                 (2)

The equivariant Hom space of (2) is one-dimensional. There is an exact uniform dichotomy:

1. ev is identically zero, and both sections vanish at the negative vertex for every lambda;
2. ev is everywhere onto, and for every lambda exactly one section line vanishes at the vertex.

In the second case that line subbundle is O_L(-4) inside Y. Under the actual plane identification Y_lambda=ell_lambda^3 W subset Sym^4 W, it is exactly

    C ell_lambda^4.                                  (3)

Thus the vertex-vanishing section would trace the rational normal quartic in P(D).

The scalar deciding these alternatives is NOT settled here. Two attempted routes now have exact outcomes: global generation alone does not decide it because H0(F(5)) contains THREE copies of W; and an actual product-ideal Koszul calculation reduces it to the remaining scalar of a two-by-two multiplicity map with one independently injective column. Neither route licenses an inferred rank.

## 1. The maximal jumping-line split from the actual evaluation

The actual evaluation of E=F(3) has rank one along each of the twenty-five reduced disjoint HM lines, and its maximal minors generate their ideal. On one line write M for the image line, Q for the quotient, and K for the rank-three evaluation kernel. Locally a unit entry puts evaluation into the form

    [1 0 0 0; 0 a b c],

where (a,b,c) is the line ideal. Differentiation therefore gives the actual isomorphism

    N_(L/P4)=K* tensor Q=O_L(1)^3.

The determinant identities, suppressing constant determinant factors, are

    M Q=O_L(5),   M Q^3=O_L(3).

They imply Q=O_L(-1), M=O_L(6), and the extension splits because H1(O_L(7))=0. Hence E|L=O(6) directsum O(-1), and F|L=O(3) directsum O(-4). This is not the smaller O(2) directsum O(-3) jump.

The standard negative fixed line is the normalizer-invariant component of the twenty-five-line configuration. The actual U=H0(F(3)) is inversion-positive, so M has positive character. Since det E=O(5) has negative character along L, Q has negative character. Twisting back by O(-3), which has negative character on L, gives exactly (1).

The line is fixed pointwise by inversion, so its two eigenline bundles are intrinsic. This also gives an equivariant splitting; no choice of a nonequivariant extension splitting is needed.

Source interfaces read for this step: BETA-IMAGE-DIMENSION-DROP.md at f5b50172bd65d1772d1af3d4a511decc8363183e supplies the actual rank/minor scheme; ALPHA-EXCLUSION.md at 212f18bb3afb52171068d1aaf8a0dbfbf9954d2b gives the actual positive four-space character from Horrocks--Mumford equation (4.12); PR541 at 9ce30d8d783da881be68548d158ebcb48e122850, Section 3, identifies the negative fixed line and its normalizer orbit. The same normal-bundle derivation is recorded in KAPPA-RATIONAL-SEXTIC.md, Section 1.

## 2. The scalar and its two uniform geometric outcomes

Every section of F_Hlambda(2) is positive. Therefore its value at the fixed vertex lies in the positive eigenline O_L(-2) of (1). Since G=SL2(F5) is perfect, the linearization of this eigenline has no extra character ambiguity. Thus

    Hom_G(Y,O_L(-2))
       =Hom_G(W,H0(O_L(1)))=C.

The generator is the tautological evaluation W tensor O(-3) -> O(-2). It is onto at every point. This proves the uniform dichotomy: there cannot be an additional finite exceptional set of vertices where its rank changes.

In the nonzero case the Euler evaluation sequence gives

    0 -> O_L(-4) -> Y -> O_L(-2) -> 0.

The kernel of W->lambda* is the annihilator ell_lambda. Combining it with Y_lambda=ell_lambda^3 W yields (3). The conclusion uses the actual section bundle and actual binary contraction dictionary, not a degree-only identification of a line.

## 3. Incidence turns the scalar into a global restriction

Let X be the universal hyperplane incidence variety H_lambda. It is Bl_R(P4), with p:X->P4 and pi:X->L. If E_R denotes its exceptional divisor, then

    pi*O_L(1)=p*O_P4(1) tensor O_X(-E_R).

The constant-dimensional actual section spaces give pi_*p*F(2)=Y. Projection formula and p_*O_X(-3E_R)=I_R^3 therefore give

    H0(P4,I_R^3 F(5))=H0(L,Y(3))=W.                  (4)

The negative line is disjoint from R. Twisting the vertex evaluation by O_L(3) identifies its scalar with the actual restriction

    W=H0(I_R^3 F(5)) -> H0(F|L(5)).                  (5)

Here

    F|L(5)=O_L(8)_+ directsum O_L(1)_-,

and the map (5), whose source is the negative binary W, lands in H0(O_L(1))=W. Thus it is zero or an isomorphism of the two representation spaces. Equivalently,

    ev=0 iff h0(I_R^3 I_L F(5))=2;
    ev!=0 iff H0(I_R^3 I_L F(5))=0.                 (6)

The ideals multiply because the two linear subspaces are disjoint; no scheme-theoretic union shortcut at an intersection is being used.

## 4. Why global generation does not decide the scalar

Write W' for the other irreducible binary two-space, so Sym^2 W'=V and Sym^2 W=A. The actual weight-three Schrödinger module and plane Koszul sequence give

    N=H1(F)=A directsum W',
    T=H2(F(-2))=W'.

The normalized equivariant HM monad has coefficient representations

    N* tensor O(-1) -> W' tensor Omega^2(2) -> N tensor O.

The left identification follows also from F*=F(1) and the self-dual monad. All these irreducible representations are self-dual. The ambient coordinate five-space is V directsum W; denote its symmetric powers by S_j. The Euler sequence gives

    H0(Omega^2(7))
       =[wedge^2(V directsum W)] S_5
         -(V directsum W) S_6+S_7

in the representation ring. Since the actual positive primary cohomology vanishes at twist five, the monad yields the actual character

    H0(F(5))
       =W' H0(Omega^2(7))-(A directsum W')(S_4+S_5).  (7)

The exact binary-icosahedral character calculation in the companion verifier gives

    H0(F(5))
      = A +4V+4P+5D+3W+W'+3S+4T_6,                 (8)

where P is the genuine four-space, S=Sym^3 W is the binary four-space, and T_6=Sym^5 W is the binary six-space. The dimensions sum to 100. In particular the W multiplicity is three, not one. As an independent consistency check the same monad calculation gives H1(F(1))=P directsum W directsum S, agreeing with the actual plane restriction computation.

Restriction H0(F(5))->H0(F|L(5)) is onto. Indeed the Koszul resolution of I_L tensored by F(5) shows H1(I_L F(5))=0 from H1(F(4))=H2(F(3))=H3(F(2))=0. Its target is Sym^8 W directsum W, with exactly one W. Thus its kernel contains two W copies. Global generation, or even this stronger global restriction surjectivity, does not decide whether the distinguished copy (4) is one of them.

## 5. A genuinely actual two-channel Koszul criterion

Use the ideal resolutions

    0 -> Sym^2 W O(-4) -> Sym^3 W O(-3) -> I_R^3 -> 0,
    0 -> wedge^3 V O(-3) -> wedge^2 V O(-2)
      -> V O(-1) -> I_L -> 0.

Their tensor product is exact because the disjoint supports make all positive Tor sheaves zero. Tensoring by F(5) gives terms in homological degrees zero through three:

    F(1) tensor Sym^3 W tensor V;
    F tensor [(Sym^2 W tensor V) directsum
               (Sym^3 W tensor wedge^2 V)];
    F(-1) tensor [(Sym^2 W tensor wedge^2 V) directsum
                   (Sym^3 W tensor wedge^3 V)];
    F(-2) tensor Sym^2 W tensor wedge^3 V.

F(-1) is acyclic. The possible cohomology terms relevant to H0 are therefore the actual primary multiplication map

    d: N tensor [(Sym^2 W tensor V) directsum
                  (Sym^3 W tensor wedge^2 V)]
       -> H1(F(1)) tensor Sym^3 W tensor V,           (9)

and a possible higher differential from H2(F(-2)) tensor Sym^2 W. The latter is W' tensor A=T_6 and has no W constituent. Both sides of (9) have W multiplicity two. Consequently

    Hom_G(W,H0(I_R^3 I_L F(5)))=ker(d_W),
    d_W:C^2 -> C^2,                                  (10)

where d_W is the ACTUAL multiplicity-space map induced by (9), not a selected matrix.

There is already one provably independent column. Since F_R(1) is acyclic and F(-1) is acyclic, the plane Koszul sequence identifies actual negative-coordinate multiplication with an isomorphism

    W tensor H1(F) -> H1(F(1)).

Under this identification, the first summand of (9) maps by the injective binary syzygy Sym^2 W -> W tensor Sym^3 W, tensored with N tensor V. Its W multiplicity is one, so this column of d_W is nonzero. The second source summand has W multiplicity one as well. Quotienting the known column leaves a one-dimensional-to-one-dimensional actual test.

Because H0(I_R^3 I_L F(5)) embeds in the distinguished W of (4), the only possibilities are

    rank d_W=1 iff ev=0,
    rank d_W=2 iff ev!=0.                            (11)

No value of this last scalar has been proved. Character counts do not determine whether the second column is proportional to the first. The test retains the actual primary multiplication rather than replacing it by a general equivariant map.

## Boundary and next missing input

The splitting and signs, uniform dichotomy, pure-fourth-power section line, three-copy obstruction to the generation argument, and the exact two-channel criterion are checked deductions. Determining the remaining scalar requires an additional actual geometric or functorial identity for (5) or (9). No access or permission failure is involved: the unresolved point is mathematical.

The conditional local geometry of the zero curve when evaluation has rank one is separate. In particular, degree equal to multiplicity must not be used to assert that an arbitrary nonreduced curve is a cone. Nothing here asserts that the sextic zero curves are reduced or smooth, or that all hyperplane adjoints are squares.
