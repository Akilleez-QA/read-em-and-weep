# The actual second Bockstein scalar is nonzero by Atiyah differentiation

## Theorem and exact scope

Under the proved invariant-cone closure and uniform cubic/quintic vertex filtration, the actual second Bockstein for q0+t a has the following properties:

* It vanishes on the D5 summand of the original kernel, by POSITIVE-SECOND-BOCKSTEIN-SQUARE-FILTRATION.md.
* Its remaining A-to-P4 quadratic family is a NONZERO multiple of the unique equivariant channel Sym^2 A tensor A -> P4.

This selects the actual second scalar without selecting an HM coefficient or evaluating an actual matrix. It uses the natural projective-orbit tangent isomorphism, not merely the character identity H1(B)=sl5. It does not claim that this second obstruction alone gives generic maximal rank: its source A has dimension three, while the original cokernel has dimension four.

The geometric comparison is explicit. Let e be the nonzero quintic-generator extension class

    e in V tensor H1(O_L(-8)),

and let D_a be the negative SL2 vector field corresponding to a in A=Sym^2 W. Then the actual class omega_a which controls the A source is, up to one nonzero scalar and the common boundary sign,

    omega_a = j_*(a D_a e),                       (1)

where

    j_*:H1(V O_L(-6)) -> H1(P4 O_L(-4))

comes from the cubic-multiple inclusion. Its kernel is the irreducible A. The expression a D_a e is a nonzero D5-valued quadratic family, so it cannot be killed by that kernel.

## 1. Actual orbit classes, rather than arbitrary representation identifications

Write B=End_0(F). EXACT-AMBIENT-ADJOINT-DEFORMATIONS.md proves that the tangent to the actual projective pullback orbit is an isomorphism

    At_F:H0(T_P4)=sl(V plus W) -> H1(B).

It is the trace-free Atiyah contraction: locally, its cocycle differentiates the transition matrices of F. The same construction is O-linear after allowing twists, so multiplication of its cohomology class by an ordinary polynomial is the Atiyah contraction with the corresponding polynomial-valued vector field.

The negative block sl(W) is the unique A constituent of the source and target. The actual cyclic construction gives a nonzero equivariant linear map a -> zeta_a into that target A, with

    a xi=q0 zeta_a.

Identify A with sl(W) through the usual invariant volume form, so a maps to its Hamiltonian vector field D_a. Uniqueness of this irreducible constituent implies

    zeta_a=k At_F(D_a),                           (2)

for a scalar k different from zero. No value of k is needed.

The vector field D_a acts only on the negative coordinates, hence is tangent to Q0. It lifts to the weighted stack X=P_stack(1,1,2,2), leaving the positive root coordinates fixed. Restriction of Atiyah classes is compatible with tangent vector fields. Twisting F_Q0 to E and then to G=pi*E tensor S_hat^(-1) changes only a scalar Atiyah class, which disappears in the trace-free part or in the wedge shadow below. Consequently

    theta_a=-[a zeta_a]|Q0=-k At_G(aD_a)

in the actual lower cohomology H1(B_Q0(2))_+.

## 2. A frame-independent Atiyah square-shadow primitive

Let sigma be the regular section of the rank-two stack bundle G, with det G=O(2) and zero ideal I=(f,g) in a local frame. For a tangent vector field D, choose any local first-order lift of D to G. Define

    w_D=sigma wedge D(sigma),

locally f Dg-g Df, with values in det G=O(2). A change of local lift is an O-linear endomorphism M; its contribution is sigma wedge M sigma, a quadratic expression in f,g and therefore an element of I^2. Thus the class of w_D modulo I^2 is independent of that choice. A change of frame has exactly the same quadratic error, so these local classes form a global section of O_(2Z)(2).

On overlaps, the difference of the local representatives is the lower square shadow of the differentiated transition matrix. Hence the connecting class of w_D in H1(I^2(2)) is the image of At_G(D) under the square sequence. This is the direct Cech definition of the Atiyah class and its connecting map; a simultaneous opposite convention changes only the common sign.

Multiplying by a gives the primitive for At_G(aD_a) at twist four. Near C0, the vector field is tangent to C0 and preserves its ideal, while sigma vanishes to first order. Therefore w_D belongs to I_C0^2 and its square-thickening class is zero there. Near L, in a frame adapted to the cubic and quintic initial generators, D preserves cover order and the primitive starts in cover degree eight. It has no lower vertex component.

Thus the class c_a in the canonical normalization of POSITIVE-SECOND-BOCKSTEIN-SQUARE-FILTRATION.md is exactly

    c_a=-k a w_(D_a),                             (3)

with the same harmless boundary sign convention. There are no subtracted lower polynomial or conic terms in this particular representative.

## 3. Leading generators and their line-bundle operators

Let F denote the nowhere-zero universal cubic relation, viewed in the coefficient convention as

    F in Sym^3 W' tensor H0(O_L(3)).

This letter F in this section denotes the cubic, not the ambient bundle. The already established quintic relation sequence is

    0 -> V O_L(-3) -> P4 O_L(-1) -> O_L(5) -> 0.

Tensor it by O_L(-5):

    0 -> V O_L(-8) -> P4 O_L(-6) -> O_L -> 0.      (4)

Choose local lifts g_i of 1 in the quotient of (4). Under the ambient quintic inclusion these are local sections of Sym^5 W' tensor O_L(-5). Their differences are

    g_j-g_i=F p_ij,
    p_ij in V O_L(-8).

The class [p_ij]=e is nonzero: a splitting of the original sequence would give a nonzero map O_L(5)->P4 O_L(-1), which is impossible. No global quintic generator is chosen.

Every O_L(n) has its canonical SL2(W) linearization. For D in sl(W), write D also for its induced first-order operator on each O_L(n), acting trivially on the constant positive-coordinate coefficient spaces. These operators obey the product rule. Applying them to the coefficient expressions for the actual generators differs from any local ordinary derivative only by zero-order frame terms. Such a change modifies fDg-gDf by an element of I^2, as proved in Section2. This justifies using these line-bundle operators without assuming an SL2-linearization of the actual bundle E or of the quintic sequence itself.

In cover degree eight, local representatives of w_D are therefore

    r_i=F Dg_i-g_i DF
       in Sym^8 W' tensor O_L(-2),                (5)

because the coefficient degrees are3 and -5. Differentiating the overlap relation and using the product rule gives the exact identity

    r_j-r_i=F^2 Dp_ij.                            (6)

All higher terms of the actual generators have larger cover degree and cannot affect the degree-eight class. The square quotient has no later physical inversion-positive graded piece, so (5)-(6) determine the actual class w_D, not merely one potentially incomplete associated-graded approximation.

## 4. The actual boundary is the differentiated extension

The square relation at twist two is

    0 -> P4 O_L(-6) -> Sym^8 W' O_L(-2)
      -> Q4(2) -> 0.

Its left map is multiplication by the cubic on the quintic relation bundle. Equation (6) shows that the boundary of w_D is the image of D e under

    H1(V O_L(-8)) -> H1(P4 O_L(-6)).

Multiplying by a, and using naturality, gives the corresponding twist-four boundary

    delta_4(a w_(D_a))=j_*(a D_a e).

Together with (3), this is formula (1), up to the nonzero scalar -k.

The kernel of j_* is determined by the same quintic sequence twisted by -3:

    0 -> V O_L(-6) -> P4 O_L(-4) -> O_L(2) -> 0.

Both left and middle have no H0, while H1(O_L(2))=0. Its cohomology gives

    0 -> H0(O_L(2))=A -> H1(V O_L(-6))
      --j_*--> H1(P4 O_L(-4)) -> 0.              (7)

Thus the only kernel is A. This kernel is retained explicitly; nonzero extension alone would not have sufficed without the calculation that follows.

## 5. A universal derivative map cannot kill e

Use H1(O_L(-8))=Sym^6 W up to the canonical self-duality. Define

    T:H1(O_L(-8)) -> Hom(Sym^2 A,H1(O_L(-6))),
    T(v)(a,a)=a D_a v.

Polarization defines the symmetric bilinear form. This is SL2(W)-equivariant: the Hamiltonian identification A=sl(W), the line-bundle operators, and multiplication are all equivariant.

The map T is nonzero. For any nonzero highest-weight quadratic q, the dual of v -> q D_q v is, up to sign,

    H0(O_L(4)) -> H0(O_L(6)),
    s -> D_q(qs)=q D_q s.

Here D_q q=0. The nonzero nilpotent D_q acts nontrivially on the irreducible binary-quartic representation, and multiplication by q is injective. Hence this dual map is nonzero. This is a universal SL2 statement, not a test of an actual bundle coefficient.

The source of T is the irreducible Sym^6 W. A nonzero equivariant map out of an irreducible representation is injective. Therefore id_V tensor T is injective, and the already proved e !=0 implies

    (a -> a D_a e) !=0.                           (8)

The actual extension class e is G-invariant, so (8) is a nonzero G-equivariant quadratic family

    Sym^2 A=1+D5 -> V tensor H1(O_L(-6))
                   =V tensor D5=A+V+P4+D5.

The target has no invariant line, and D5 occurs once. Consequently the family has nonzero image of type D5. By (7), the kernel of j_* has type A, not D5. Hence its image under j_* is nonzero.

Equations (1)-(3) and k !=0 prove that the actual second-Bockstein scalar is nonzero.

## Dependencies and restrictions

The natural orbit-map theorem is EXACT-AMBIENT-ADJOINT-DEFORMATIONS.md, Section2. The nonsplit quintic sequence and globally uniform initial pair are VERTEX-QUINTIC-RELATION-EXTENSION-AND-SQUARE-P4.md. The actual Bockstein and its canonical square normalization are POSITIVE-FIRST-BOCKSTEIN-VANISHES-BY-CYCLIC-RAO.md and POSITIVE-SECOND-BOCKSTEIN-SQUARE-FILTRATION.md. No flat spinor deformation is asserted, and no unique ambient first normal extension is assumed. The proof differentiates the actual Atiyah class and the actual forced extension, preserving all line-bundle and square-ideal corrections.
