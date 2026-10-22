# The actual second Bockstein factors through one vertex relation class

## Results

Retain the proved invariant-cone closure and the actual cyclic Rao class xi of POSITIVE-FIRST-BOCKSTEIN-VANISHES-BY-CYCLIC-RAO.md. Let A=Sym^2 W be the negative-coordinate quadratics and D5=Sym^4 W' the positive-coordinate quadratics on Q0, modulo q0. For the actual pencil q0+t a, with a in A, write

    a xi=q0 zeta_a,
    theta_a=-[a zeta_a] in H1(B_Q0(2))_+.

There is a canonical vertex square-shadow class

    c_a in H0(L,Q4(4)),

quadratic in a, obtained by mapping theta_a through the stack square sequence and the normalization proved below. If

    omega_a=delta_4(c_a) in H1(P4 O_L(-4))=P4 tensor A*,

where delta_4 is the boundary of the degree-eight square relation, then the actual second Bockstein is

    beta2_a(h xi)=0                              for h in D5,
    beta2_a(h xi)=h omega_a in P4                 for h in A.       (1)

All signs are absorbed by the displayed definition of theta. Thus the entire D5 source survives through second order, independently of any unknown scalar. The second Bockstein has rank at most three and cannot alone remove the four-dimensional cone cokernel.

More strongly, the actual cone multiplication map

    D5 tensor H1(B_Q0(2))_+ -> H1(B_Q0(4))_+

is identically zero. The proof is geometric and does not classify abstract allowed channels or evaluate an actual coefficient.

The quadratic map omega:Sym^2 A -> P4 tensor A* has only one possible equivariant scalar, since Sym^2 A=1+D5 and P4 tensor A*=V+P4+D5. The proof does not decide that scalar.

## 1. Inputs and notation

Let X=P_stack(1,1,2,2), with coarse cone Q0, and let Z be the zero scheme of its actual regular spinor section. Its coarse support is the disjoint union of the reduced conic C0 and a vertex scheme supported on L=P(W). Write

    R_d=pi_*O_(2Z)(d),
    Q_d=pi_*I_Z^2(d),

where the square is the ordinary ideal square on the smooth stack, not the square of the coarse Ext-annihilator.

The established square sequences at the two relevant twists are

    0 -> P_0 -> B_Q0(2) -> Q_4 -> 0,
    0 -> P_2 -> B_Q0(4) -> Q_6 -> 0,

with P_0=F_Q0 tensor S(1) and P_2=F_Q0 tensor S(3). The established rank33 theorem gives H1(P_2)=0 and H2(P_2)=0, hence the canonical isomorphism

    H1(B_Q0(4))_+ = H1(Q_6)_+ = P4.               (2)

The vertex ordinary-square quotient has, at every point of L, the filtered Hilbert function of the square of a regular initial pair of cover degrees3 and5:

    1,2,3,4,5,6,6,6,5,4,2,1.

It has no cover-degree12 or higher part. Uniformity follows from the globally constant actual Loewy layers and the fiberwise regular initial-pair theorem in VERTEX-QUINTIC-RELATION-EXTENSION-AND-SQUARE-P4.md. This is a filtered assertion, not a choice of homogeneous generators.

Let F^j be the vertex positive-coordinate ideal filtration; ordinary positive-coordinate order j corresponds to cover degree2j. Then F^6 R_d,L=0. For even d, the physical inversion-positive graded pieces are exactly

    gr0=O_L(d),
    gr2=Sym^4 W' tensor O_L(d-2)=D5 O_L(d-2),
    gr4=Q4(d),                                  (3)

where

    0 -> P4 O_L(-8) -> Sym^8 W' O_L(-4)
      -> Q4 -> 0.                                (4)

The odd filtration indices have negative physical inversion character. This physical parity is distinct from the local mu2 stabilizer parity already used in the coarse pushforward. In particular (F^4 R_d,L)_+=Q4(d), canonically: all its later positive graded pieces vanish.

The conic first thickening has positive part O_C0(d); its conormal part is inversion-odd. Hence R_d,+ is the direct sum of the conic O_C0(d) and the positive vertex part just described.

## 2. Canonical normalization of every twist-four square obstruction

The ordinary cone coordinate ring is the even Veronese of C[a,b,u,v], with a,b in W' of weight1 and u,v in W of weight2. Its physical inversion-positive quartics have three polynomial pieces, according to ordinary positive-coordinate degree0,2,4:

    H0(O_L(4)),
    Sym^4 W' tensor H0(O_L(2)),
    Sym^8 W'.                                    (5)

Their dimensions are5,15,9. The last piece restricts isomorphically to H0(O_C0(4))=H0(O_P1(8)); the first two vanish on C0. The first two pieces map isomorphically to the global sections of R_4,L,+/F^4: on its two associated graded pieces they are the identity maps. These are statements about actual polynomial restriction and filtered maps, not an assumed splitting of the vertex quotient.

Thus every global section of R_4,+ can be reduced uniquely, modulo ambient positive quartics, to a section which vanishes on C0 and lies in F^4 on L. Conversely no nonzero such section is the restriction of an ambient positive quartic: vanishing on C0 eliminates the last piece of (5), and vanishing in the two low vertex grades eliminates the first two. Therefore

    H1(Q_4)_+ = H0(R_4)_+/H0(O_Q0(4))_+
              = H0(L,Q4(4)),                     (6)

canonically for the fixed positive/negative coordinate decomposition. Here H1(O_Q0(4))=0. The restriction of ambient quartics is injective by the same argument, so no assumption about H0(Q_4) is needed.

Twisting (4) by four gives

    0 -> P4 O_L(-4) -> Sym^8 W' O_L
      -> Q4(4) -> 0.

Consequently

    0 -> Sym^8 W' -> H0(Q4(4)) --delta_4-->
         H1(P4 O_L(-4)) -> 0.                    (7)

The dimensions are9,21,12, and the representation of the middle term is

    H0(Q4(4))=V+2P4+2D5.

The same normalization at twist six first removes the low vertex grades and the conic value. The remaining quotient is

    H1(Q_6)_+ = H0(Q4(6)) /
        H0(Sym^8 W' tensor O_L(2))
              = H1(P4 O_L(-2))=P4.              (8)

This follows from (4) twisted by six. The conic degree-twelve polynomial part vanishes on the vertex quotient because F^6=0; the cover-degree-eight part gives exactly the denominator displayed in (8).

## 3. Multiplication from twist four to twist six

Take a class c in the normalized description (6).

If h is a positive-coordinate quadratic, h has vertex filtration order2. Hence

    h c belongs to F^6 R_6,L=0.

The chosen representative also vanishes on C0. Therefore its product is zero as a section of R_6, and certainly zero in H1(Q_6). This proves

    D5 tensor H1(Q_4)_+ -> H1(Q_6)_+

is identically zero. Arbitrary representatives give the same conclusion, because multiplying a subtracted ambient quartic by h gives an ambient sextic.

If h is a negative-coordinate quadratic, it restricts to the binary quadratic h on L and preserves the vertex filtration. Multiplication of (4) by h gives a commutative diagram of exact sequences at twists four and six. Naturality of connecting maps and (8) imply

    [h c] = delta_6(h c)=h delta_4(c).

Under Serre duality this last map is precisely evaluation

    H1(O_L(-4)) tensor H0(O_L(2)) -> H1(O_L(-2)),

tensored with P4. This proves the claimed contraction description without choosing a local quintic generator or a splitting of its nonsplit extension.

Naturality of the stack square sequences and the isomorphism (2) now prove the stronger cone-cohomology multiplication vanishing in the result section.

## 4. Comparison with the actual second Bockstein

The actual cyclic construction supplies zeta_a in H1(B)_A, uniquely and equivariantly, with a xi=q0 zeta_a. Let rho_2:H1(B(2))_+ -> H1(B_Q0(2))_+ be restriction, and set

    theta_a=-rho_2(a zeta_a).

The second Bockstein derived from the actual pencil is

    beta2_a(h xi)=-[a h zeta_a].

Restriction commutes with polynomial multiplication. Hence this actual obstruction equals h theta_a in H1(B_Q0(4))_+, using the established identification of its cokernel with that group. Map theta_a to H1(Q_4)_+ by the square sequence, and apply (6) to define c_a. Applying Section3 yields exactly (1).

No assertion is made that theta_a, c_a, or omega_a is nonzero. The lower square projection may have a kernel, and the boundary delta_4 kills the nine-dimensional polynomial subspace in (7). Both are retained by the construction.

Finally zeta_a is linear in a, so omega_a is quadratic. Finite-group semisimplicity and

    Sym^2 A=1+D5,
    P4 tensor A*=V+P4+D5

show that omega is confined to one D5 channel. This is a precise actual comparison and a vanishing theorem for the D5 source, not a determination of the remaining scalar or of generic positive maximal rank.

## Evidence and scope

Inputs: the invariant-cone rank33 theorem; the globally uniform vertex ordinary-square filtration; the exact degree-eight relation bundle; and the proved cyclic first-Bockstein vanishing. The companion verifier checks only universal characters, ordinary-square Hilbert coefficients, twists, and dimensions. No actual HM coefficient, selected actual matrix, rank experiment, restarted spike, or external write is used.
