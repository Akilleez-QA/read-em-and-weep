# A canonical quadratic evaluation block in actual global multiplication

Work over C with G=SL2(F5), T=P(W*), A=Sym2 W, S=Sym3 W and T6=Sym5 W. The determinant pairing identifies W with W*. All subspaces below belong to the actual cohomology module. No selected actual coefficient or parameter is evaluated.

## 1. Immutable inputs and theorem

INPUTS.json pins five exact originals in Akilleez-QA/read-em-and-weep:

- RECEIVER, PR1041 at 7f219bef07cb4bbbe761df6c6363673b5a1e492d, research/hm/global-receiver-constraints/PROOF.md: the finite geometry selects a genuine subbundle L=O(2) in actual global Jg.
- BRIDGE, PR1038 at e567a431830f6dd37fe5fd2a65e24fc1210eedb3, research/hm/global-ninth-bridge/PROOF.md: Jg has rank13 degree28 and the actual exact incidence presentation

      0 -> E O(-1) --m--> N O -> Jg -> 0,          (1)
      E=H1(B(1))_-, N=H1(B(2))_+.

  Its map is negative-coordinate multiplication, and its cokernel is locally free everywhere.
- CHAR, PR938 at e5aa6e4695eee79cd0222d8f6b57aa60b7a0dab5, research/hm/opposite-source-weights/PROOF.md, Section2: the actual normalized-monad lambda-ring Euler formula and N=A+2V+3P+4D. Only that section is used; its earlier conditional torsion cases play no role.
- TWIST, PR455 at 8cbbe482ee50c35d52ffcdf3efb837fa8cf96af4, research/hm/twist-one-structural-vanishing/PROOF.md: H2(B(1))=0.
- TAIL, PR476 at 3aa461bc3581fb72fbf923fbe869ddee023b435a, research/hm/five-generator-module/PROOF.md: H3(B(t))=0 for t>=-1.

We prove a canonical actual residual presentation

    0 -> (2S+3T6) O(-1) --mbar--> (2V+3P+4D) O
      -> Jbar:=Jg/L -> 0.                         (2)

Here the source and target are canonical isotypic subspaces/quotients of the actual coefficient spaces, not chosen abstract replacements. Jbar is locally free of rank12 degree26. The source map is injective on every fiber.

More concretely, E has a unique W-isotypic subspace E_W, and N a unique A-isotypic subspace N_A. Actual negative-coordinate multiplication satisfies

    W tensor E_W -> N_A,

and this map is a nonzero multiple of the symmetric projection W tensor W -> A. Its kernel is the invariant determinant line. Thus this gives an actual first-multiplication constraint, not merely a compatible pair of characters.

## 2. Authenticate the source character

We need the character of E, not only dim E=28. First H0(B(1))=0: CHAR imports H0(B(2))=0, and multiplication by any nonzero linear form is injective on sections of the locally free sheaf B(1). TWIST kills H2; TAIL kills H3. Finally H4(B(1))=H0(B(-6))*=0 by Serre duality and stability of the normalized HM bundle F: a section of End(F)(-6) would be a map F->F(-6) between stable bundles of strictly decreasing slopes. Trace-free B is a direct summand. Hence H1(B(1))=-chi_G(B(1)).

For a self-contained bounded character calculation, use CHAR's H=V+W, Nmon=A+W', L2=Lambda2 H and

    c_-1=-Nmon, c_0=W' L2-Nmon, c_1=-W'H, c_2=W'.

The K-class of F is sum c_i O(i). Since B(1)=Sym2 F(2), the lambda-ring identity gives

    chi_G(B(1)) = 1/2 sum_(i,j=-1)^2 c_i c_j Sym^(i+j+2) H
                 +1/2 sum_(i=-1)^2 psi2(c_i) Sym^(2i+2) H.       (3)

All exponents lie between0 and6, so ordinary nonnegative symmetric-power characters suffice. The signs in c_i and the Adams operation are taken in the representation ring, as in CHAR; no monad differential is evaluated. The exact nine-class calculation in verify.py gives

    H1(B(1)) = A+2V+2P+2D + W+2S+3T6.            (4)

The central negative part is therefore

    E=W+2S+3T6, dim E=28.                         (5)

The same checker replays CHAR's twist-three calculation for B(2), giving N=A+2V+3P+4D, dim N=41. Thus W and A each have multiplicity exactly one in the required source and target. Equation (3) is a fixed abstract character computation, not an actual-instance rank computation.

## 3. The complete evaluation diagram selects the coefficient subspaces

Since O(-1) has H0=H1=0, (1) identifies N canonically with H0(Jg). The map N O->Jg is its complete evaluation map, not merely a surjection from a space of the correct dimension.

The subbundle L=O(2) supplies an injection H0(L)=A->H0(Jg)=N. By the multiplicity-one statement this image is exactly N_A. Naturality of evaluation gives the commutative diagram with exact rows

    0 -> M_L -> N_A O -> L -> 0
          |         |       |
    0 -> E O(-1) -> N O -> Jg -> 0.

Here M_L is the usual quadratic-evaluation kernel, equivariantly W O(-1). For example this follows by the two linear syzygies of the complete degree-two binary evaluation; it is the universal exact sequence 0 W O(-1)->A O->O(2)->0. The vertical kernel map is injective. As both its source and target are O(-1)-twisted constant bundles, it comes from a constant injective equivariant map W->E. Equation (5) makes its image exactly E_W.

This identifies the selected L intrinsically: it is the image of N_A O under complete evaluation. In particular it is independent of any choices made to describe the finite summands which first supplied it. A scalar change in the isomorphism L≅O(2) changes no image, kernel or quotient.

Taking quotients in the diagram gives (2), with source E/E_W=2S+3T6 and target N/N_A=2V+3P+4D. Exactness can also be checked by the snake lemma. RECEIVER says L is a subbundle, so Jbar is locally free; thus this exact sequence remains left-exact on every fiber. This is not a generic-rank assertion. The rank and degree are 38-26=12 and26, also equal to rank Jg-1 and deg Jg-2.

The quotient is globally generated, H1(Jbar)=0 and H0(Jbar)=N/N_A. Both follow either from (2) or from the cohomology of 0 L->Jg->Jbar->0. Thus (2) is again the complete-evaluation presentation of the actual quotient.

## 4. Actual multiplication, and the corrections not removed

The upper row of the diagram is the restriction of actual m to E_W. Its complete linear coefficient map is W tensor E_W->N_A. Since W tensor W=1+A, equivariance forces the invariant line to vanish and makes the remaining A map scalar. It is nonzero because the upper-row kernel inclusion is nonzero (indeed fiberwise injective). Hence the map is the nonzero symmetric projection, up to the harmless identifications of the two irreducible spaces. This statement concerns all negative linear forms simultaneously; no form or HM coefficient is chosen.

Distinct isotypic components give canonical complementary coefficient spaces E'=2S+3T6 and N'=2V+3P+4D. Relative to E_W plus E' and N_A plus N', actual m has blocks

    m = [ i   alpha ]
        [ 0   mbar  ],                            (6)

where i is quadratic evaluation's kernel map. The zero block and the nonzero universal i are proved; alpha is retained as the actual off-diagonal map. Because A tensor W=W+S, Hom_G(E' O(-1),A O) has dimension2 and only the two S copies contribute. The T6-to-A part is zero. No value of the two S-channel coefficients is asserted.

There is a precise extension interpretation of these remaining coefficients. Apply equivariant Hom(-,L) to (2). Since Hom_G(N',A)=0, Hom_G(N' O,L)=0. Also Ext1_G(N' O,L)=0 because H1(O(2))=0. Thus

    Ext1_G(Jbar,L) ≅ Hom_G(E' O(-1),L)
                  ≅ Hom_G(E',Sym3 W) ≅ C^2.       (7)

Compose alpha with N_A O->L. This represents the actual extension 0 L->Jg->Jbar->0, up to the standard sign convention for a presentation. The map from alpha's two-dimensional space to the middle Hom space in (7) is an isomorphism: applying Hom_G(E' O(-1),-) to 0 E_W O(-1)->N_A O->L->0 gives zero kernel Hom_G(E',E_W) and zero Ext1, since H1(O)=0. Consequently this extension splits equivariantly if and only if the actual alpha is zero. We do not claim either alternative.

## 5. Contribution and limits

The actual finite/global line now becomes a canonical coefficient-module evaluation block. The source character identifies its coefficient W uniquely; removing this block produces an everywhere-injective 26-to-38 actual global pencil and an exact two-dimensional description of the unremoved extension channels. This is different from the opposite C's 26-to-31 presentation and its own quotient constructions.

No source/catalogue occurrence or exclusion, opposite splitting type, secondary coefficient, vertex scalar or top-obstruction value is determined. No selected actual HM/source coefficient, point, parameter, derivative, jet, matrix, instance rank or large scan was used. The proof is mathematical, with a bounded arithmetic checker, not a formal proof-assistant certification.
