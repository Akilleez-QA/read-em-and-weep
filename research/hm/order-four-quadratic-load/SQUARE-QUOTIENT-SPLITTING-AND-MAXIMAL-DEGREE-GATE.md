# The moving-square quotient splits exactly; a finite gate for maximal cokernel degree

## Results and scope

Let T=P(W*) be the actual negative hyperplane pencil, A=Sym²W, D=Sym⁴W, and S=Sym²D. The actual moving square inclusion is

    a:A O_T(-6) -> S O_T,
    a_ell(w1 w2)=(ell³ w1) symmetric-product (ell³ w2).

Its quotient is an everywhere locally free bundle with the exact equivariant splitting

    Q_sq := coker(a)
         = O_T + Sym³W O_T(1) + Sym⁶W O_T(2).          (1)

In binary-icosahedral notation this is O + S_4 O(1) + (V+P) O(2); S_4 denotes the four-dimensional odd representation, not the fifteen-dimensional section space S above. In particular Q_sq has rank 12, degree 18, and maximal splitting degree two.

There is also an actual exact sequence

    0 -> Q_sq -> P_2 -> C_lin -> 0,                  (2)
    0 -> H1(B(1))_+ O_T -> H1(B(2))_- O_T(1)
      -> P_2 -> 0.                                  (3)

Here P_2 has rank 17 and degree 44. This identifies exactly the additional actual bundle and map needed to turn (1) into an upper bound for C_lin. No upper bound of six or seven for C_lin is proved below. A quotient of P_2 need not inherit the upper degree bound for its subbundle Q_sq.

The final section gives an independent finite-neighborhood duality formulation, retaining the large R³π term. Neither formulation evaluates actual coefficients or ranks.

## 1. Why the universal square map is the actual map

[HYPERPLANE-SQUARE-SURVIVORS.md](HYPERPLANE-SQUARE-SURVIVORS.md), Section 6, identifies the actual section bundle of F_H(2) with W O_T(-3), whose plane restriction at ell is ell³W inside Sym⁴W. The actual all-parameter square theorem and [EXACT-HYPERPLANE-ADJOINT-SYZYGY-BUNDLE.md](EXACT-HYPERPLANE-ADJOINT-SYZYGY-BUNDLE.md) identify the adjoint section bundle with its symmetric square A O_T(-6). Thus a is the actual plane-restriction inclusion, not an arbitrary degree-six map. The same concrete identification is recorded in [TWO-ROOT-DIVIDED-DIFFERENCE-SMOOTHING-FORMULA.md](TWO-ROOT-DIVIDED-DIFFERENCE-SMOOTHING-FORMULA.md), Section 1.

Although the ambient HM bundle has only the stated finite-group symmetry, this particular binary-form construction is SL(W)-equivariant. We may therefore use SL₂ representation theory for Q_sq alone. No SL₂ action on the entire HM family or on C_lin is asserted.

## 2. The nontrivial universal extension

Clebsch–Gordan gives

    Sym²(Sym⁴W) = Sym⁸W + Sym⁴W + 1.

The invariant component of a is zero: the fourth transvectant of two quartics with a common triple factor vanishes. Its Sym⁸W component is ordinary multiplication,

    b:A O(-6) -> Sym⁸W O,    b_ell(q)=ell⁶ q.

The quotient of b is Sym⁵W O(3). One can see this directly using third directional contraction: at each ell, the map from binary octics to binary quintics obtained by contracting three times in the annihilating direction is onto, and its kernel is exactly ell⁶ Sym²W. These are universal binary-polynomial identities, not selected HM coefficients.

The Sym⁴W component c of a is nonzero. It is the second transvectant, which is nonzero on the pair of universal quartics ell³m, ell³m when ell and m are independent. Equivalently, the weight-four vector (ell³m)² is not solely in the Cartan Sym⁸W summand: lowering the highest-weight square twice also produces the independent vector ell⁴ symmetric-product ell²m². This proves nonvanishing without evaluating any actual HM datum.

Since the invariant component vanishes, Q_sq=O+Q', where Q' is the quotient inside Sym⁸W+Sym⁴W. Projection to the first summand gives

    0 -> Sym⁴W O -> Q' -> Sym⁵W O(3) -> 0.            (4)

This is the pushout of the osculating sequence for b along the nonzero c. It is a nonzero SL₂-equivariant extension. Indeed

    Hom_SL2(Sym⁸W O, Sym⁴W O)=0,

so c cannot extend to the middle term of the osculating sequence. The extension group is one-dimensional:

    Ext¹_SL2(Sym⁵W O(3), Sym⁴W O)
       = Hom_SL2(Sym⁵W, Sym⁴W tensor W),

using H¹(O(-3))=W and determinant-one linearization. Thus the extension in (4) is the unique nonzero class up to scalar.

## 3. Exact splitting of Q_sq

Twist (4) by -3. The connecting map is the nonzero equivariant map

    Sym⁵W -> Sym⁴W tensor W = Sym⁵W + Sym³W.

It is injective. Therefore H0(Q'(-3))=0, so all splitting degrees of Q' are at most two. Global generation of Q' gives nonnegative degrees.

There are no degree-zero summands of Q'. Dualizing its defining presentation, the map on global sections is

    Sym⁸W + Sym⁴W -> A tensor Sym⁶W
                      = Sym⁸W + Sym⁶W + Sym⁴W.

Its two irreducible components are nonzero, by the checks on b and c above. It is injective, so H0(Q'^*)=0. All eleven degrees of Q' are therefore one or two. Rank 11 and degree 18 force four copies of O(1) and seven copies of O(2).

The canonical degree-two multiplicity module is H0(Q'(-2)). In the sequence (4) twisted by -2 it embeds in

    Sym⁵W tensor W = Sym⁶W + Sym⁴W

with quotient mapping to Sym⁴W. Its dimension is seven, so it is exactly Sym⁶W. Twisting (4) by -1 gives

    H0(Q'(-1)) = Sym⁵W tensor Sym²W
              = Sym⁷W + Sym⁵W + Sym³W.

The degree-two part accounts for Sym⁶W tensor W=Sym⁷W+Sym⁵W. Thus the degree-one multiplicity module is Sym³W. Equivariant Birkhoff–Grothendieck splitting proves (1). One may average a splitting over the compact form SU₂ and then use Zariski density to obtain SL₂ equivariance; equivalently use reductivity in characteristic zero.

This gives, in particular,

    Q_sq* (5) = O(5) + Sym³W O(4) + Sym⁶W O(3),
    h0(Q_sq* (5))=6+20+28=54,
    H1(Q_sq* (5))=0.                                (5)

## 4. The actual extension with C_lin

Let pi:X=Bl_R(P4)->T and write p:X->P4. The relative plane restriction sequence is

    0 -> p*B(2) tensor pi*O_T(1)
      -> p*B(3) -> B_R(3) external-tensor O_T -> 0.  (6)

Every B_H(3) section is a square and restricts injectively to the plane section space S. Consequently H0(B_H(2))=0: multiplication by a nonzero equation of R in H would otherwise give a B_H(3) section with zero plane restriction. This works at every parameter, including the twelve special hyperplanes.

The actual ambient vanishings H²(B(1))=H²(B(2))=H³(B(1))=0 also give H²(B_H(2))=0. Thus all relevant first direct images are vector bundles and commute with base change. Set

    P_2 := (R1 pi_* p*B(2))_- tensor O_T(1).

Taking the even part of the pushforward of (6), and using H¹(B_R(3))=0, gives (2). Universal hyperplane restriction at twist two, together with H²(B(1))=0 and the section vanishing just proved, gives (3). The spaces in (3) have dimensions 27 and 44. Thus P_2 has rank 17 and degree 44, and P_2(-1) is globally generated.

Dualize (2) and twist by five. Since (5) has no H¹, the exact global cohomology sequence is

    0 -> H0(C_lin* (5)) -> H0(P_2* (5))
      -> H0(Q_sq* (5)) -> H1(C_lin* (5))
      -> H1(P_2* (5)) -> 0.                         (7)

By Serre duality on T, H¹(C_lin* (5))=H0(C_lin(-7))*. Hence maximal splitting degree at most six is equivalent to BOTH:

1. H¹(P_2* (5))=0;
2. the actual restriction map H0(P_2* (5))->H0(Q_sq* (5)) is onto.

If the first holds, the second is an actual 58-to-54 surjectivity question: chi(P_2* (5))=17*6-44=58. Neither assertion follows from the dimensions or from (1).

For maximal degree at most seven, replace five by six. The analogous dimensions, conditional only on H¹(P_2* (6))=0, are 75-to-66. These are exact reductions, not new rank assumptions.

## 5. Independent finite-neighborhood duality, retaining R³π

Put C_tot=R1 pi_*p*B(3), so its even component is C_lin. The established fiber cohomology gives R²pi_*p*B(3)=R³pi_*p*B(3)=0 and pi_*p*B(3)=A O(-6). The relative dualizing bundle is

    omega_(X/T)=p*O_P4(-4) tensor pi*O_T(1).

Relative Serre duality therefore gives

    R2 pi_*p*B(-7) = C_tot* tensor O_T(-1),
    R3 pi_*p*B(-7) = A* tensor O_T(5),               (8)

and the lower direct images vanish. The second term is the dual of the square kernel. Its degree is +5, not -7, and it must not be discarded.

For every k>=1, apply Leray to p*B(-7) tensor pi*O_T(k-1). Taking central parity (-1)^k gives

    0 -> H0(C_lin(-k))*
      -> H3(P4, I_R^(k-1) B(k-8))_((-1)^k)
      -> A tensor Sym^(k+4)W -> 0.                 (9)

Here A*=A and all powers of W are self-dual. To identify the middle term, use pi*O(1)=p*O(1) tensor O(-E_exc), p_*O(-nE_exc)=I_R^n and R^i p_*O(-nE_exc)=0 for i>0 and n>=0. The last term in (9) is H0 of the R³pi term from (8). The opposite-parity part of C_tot contributes nothing to the chosen parity.

At k=7 the exact sequence becomes

    0 -> H0(C_lin(-7))*
      -> H3(P4,I_R^6 B(-1))_-
      -> A tensor Sym¹¹W -> 0,                     (10)

whose right side has dimension 36. Thus maximal degree at most six is equivalently injectivity of this canonical top-edge map. This is a sixth infinitesimal-neighborhood invariant, not an asymptotic or generic-balancedness assertion. The vanishing H³(B(-1))=0 identifies its middle term with the cokernel of actual restriction

    H²(B(-1))_- -> H²(B(-1)|_(6R))_-.

The individual ambient negative-twist middle groups are not replaced by their Euler characteristics. In particular neither (9) nor the known eventual plane vanishing H¹(B_R(-m))=0 for m>=5 by itself determines the edge kernel.

## Dependencies and limitation

- Actual all-parameter torsion-freeness and square theorem: [TORSION-FREE-HYPERPLANE-AND-QUADRATIC-TARGETS.md](TORSION-FREE-HYPERPLANE-AND-QUADRATIC-TARGETS.md), based on the immutable special-hyperplane theorem at 5ce98e6bef1fd849353f563b1ccfc62f4d28b8d9.
- Actual kernel and cohomology/base-change: [EXACT-HYPERPLANE-ADJOINT-SYZYGY-BUNDLE.md](EXACT-HYPERPLANE-ADJOINT-SYZYGY-BUNDLE.md).
- Lower ambient vanishings: [LOWER-TWIST-EVEN-QUADRIC-PARITY.md](LOWER-TWIST-EVEN-QUADRIC-PARITY.md) and [PR455, immutable 8cbbe482ee50c35d52ffcdf3efb837fa8cf96af4](https://github.com/Akilleez-QA/read-em-and-weep/blob/8cbbe482ee50c35d52ffcdf3efb837fa8cf96af4/research/hm/twist-one-structural-vanishing/PROOF.md).
- H³(B(-1))=0 and its distinction from the middle index are recorded in [FIXED-CONIC-PARITY-JETS-AND-POSITIVE-GATE.md](FIXED-CONIC-PARITY-JETS-AND-POSITIVE-GATE.md).

The exact new splitting (1) concerns Q_sq, not C_lin. Equations (7) and (9) retain the precise missing actual maps. There is no inferred bound from dimension, generic balance, or the mere surjectivity of the separate 48 O -> C_lin(2) boundary. No external post, selected HM coefficient, numerical experiment, or actual rank evaluation is used.
