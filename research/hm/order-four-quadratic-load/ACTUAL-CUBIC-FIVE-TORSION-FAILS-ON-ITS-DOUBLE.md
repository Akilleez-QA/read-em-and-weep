# The actual cubic five-torsion fails on its double

## Result and scope

Let D=(f=0) be the actual (3,3) divisor in Y=P(Wprime) times L, and let 2D=(f^2=0). The local quintic generators trivialize O_D(5,-5), but

    O_(2D)(5,-5) is NONTRIVIAL.                     (1)

Its class in the nilpotent kernel Pic(2D)->Pic(D) identifies exactly with the actual nonzero quintic-relation extension

    e in [V tensor H1(O_L(-8))]^G.

In particular O_(2D)(1,-1) is not5-torsion, although its restriction to D is5-torsion. There is a unique5-torsion line-bundle isomorphism class on2D restricting to O_D(1,-1), and it differs from the ambient line bundle by a nonzero nilpotent correction. This is a first-normal statement about the actual cubic divisor, not the ambient normal bundle or the Bockstein value.

## 1. The nilpotent Picard kernel

The square-zero ideal of D in2D is J=O_D(-3,-3). The unit sequence, using 1+x identified with x, is

    0 -> J -> O_(2D)^* -> O_D^* -> 1.

The divisor sequence and Kunneth give H0(O_D)=C: the relevant H1(O_Y(-3,-3)) vanishes because both factors have zero H0. Thus global units on D are constants and lift to2D. Also H2(J)=0, since D is a curve. Consequently

    0 -> H1(J) -> Pic(2D) -> Pic(D) -> 0.          (2)

The kernel is an additive complex vector space; multiplication by5 is an isomorphism on it. These statements do not require an assumption of smoothness of D.

## 2. Identify the actual class, including its nonvanishing

From the actual relation bundles, f has bidegree(3,3), local g has bidegree(5,-5), and

    g_j = g_i + f p_ij,

with p_ij of bidegree(2,-8). The actual coprimality in every fiber makes g|D a nowhere-zero section of O_D(5,-5). Thus local g_i are also invertible as line-bundle sections on2D. Relative to the resulting trivialization on D, the overlap ratios are

    g_j/g_i = 1 + f p_ij/g_i modulo f^2.

Hence the class of O_(2D)(5,-5) in (2) is represented by p_ij/g_i in J. Reversing a transition convention reverses this class and does not change the nonvanishing assertion.

Multiplication by the global nowhere-zero g on D identifies

    J=O_D(-3,-3) with O_D(2,-8).

The divisor sequence is

    0 -> O_Y(-1,-11) -> O_Y(2,-8)
      -> O_D(2,-8) -> 0.

Projection to L has zero H0 and H1 along the first factor for the kernel O(-1,-11). It therefore identifies

    pi_*O_D(2,-8)=Sym^2(Wprime) O_L(-8)=V O_L(-8).

Under these identifications the cocycle p_ij/g_i becomes p_ij itself. Thus the nilpotent Picard class is EXACTLY the quintic-extension class e proved nonzero in VERTEX-QUINTIC-RELATION-EXTENSION-AND-SQUARE-P4.md. There is no unsupported inference from a nonzero class through an unknown map: the comparison is a sheaf isomorphism. This proves (1).

As a check, h1(J)=3*7=21 and its invariant part is one-dimensional, since Sym^6 W=V plus P4.

## 3. The unique torsion correction

Set T=O_D(1,-1). The quintic trivialization gives T^5=O_D. Let T0=O_(2D)(1,-1); its fifth power has the nonzero class e in the kernel (2). If K(c) denotes the nilpotent line-bundle class corresponding to c in H1(J), then

    T_tors = T0 tensor K(-e/5)

has fifth power trivial. Any other lift of T differs from it by K(c), whose fifth power is K(5c). Thus a5-torsion lift is unique, and the ambient lift T0 is not that lift. The uniqueness is for line-bundle isomorphism classes with the indicated restriction; it does not create a canonical trivialization or a normal bundle identification.

If one uses the independently established exact order5 of T on the smooth genus4 cubic D, the corrected lift also has exact order5. The nontriviality (1) and the correction argument themselves use only the actual relation sequence and the displayed exact sequences.

## Limitation

The nonzero normal Picard class is a structural feature of the actual support and the actual nonsplit quintic relation. No comparison identifying its value or a derivative with the actual cubic operator boundary has been proved here. In particular this theorem does not establish nonvanishing of the third Bockstein.
