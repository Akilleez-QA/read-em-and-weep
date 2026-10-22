# The fourth square-detecting input requires a nonzero third source correction

## Precise new conclusion

At any C5-fixed square direction a=t^2, the sole positive-quartic input character capable of contributing to the fourth quotient is h=X^2Y^2. Its canonical third lifting correction L_can(a,h) is a NONZERO multiple of a itself. Hence the fourth calculation in a reduction compatible with the canonical raw cubic must retain the B3|A(a) contribution; it cannot set this source correction to zero or discard it by C5 weights.

This is uniform over the full stabilizer orbit. It uses arbitrary abstract eigenspace bases and the universal cubic tensor with all coefficients symbolic. No actual coefficient, source-instance matrix, rank evaluation, or selected-point experiment occurs. No fourth value or nonzero composite is asserted.

## 1. The fourth detecting character

Use the fixed linearizations from the C5 theorem. At a=t^2, a has character2. The actual second-symbol image has characters2,4,6 and the quotient has character8. A fourth symbol is quartic in a, so its detectable input has character

    8-4*2=0 modulo10.

The unique such line in D5_positive is h=X^2Y^2. The canonical linear third source correction has total character2+0=2 in A. Therefore

    L_can(t^2,X^2Y^2) is a multiple of t^2.          (1)

Weights alone do not prove that the multiple is nonzero. The next exact tensor identity does.

## 2. An intrinsic model of the unique correction line

The actual cubic, in arbitrary stabilizer eigenlines, is

    f=A X^2Y s^3+B Y^3 s^2t+Ac X^3 st^2-Bc XY^2t^3,
    A B c != 0.

Let ( , )_r denote the UNNORMALIZED rth binary transvectant. Put

    H=(f,f)_(1,1),

meaning first transvection in the positive variables and independently in the negative variables. Equivalently

    H=2(f_Xs f_Yt-f_Xt f_Ys).

This is an invariant tensor of bidegree(4,4). Positive fourth transvection with h gives a G-map

    I_f:D5_positive -> Sym^4 W,
    I_f(h)=(H,h)_4^positive.

The following explicit identity proves it is nonzero, hence an isomorphism of irreducible D5 representations. Therefore

    C_f(a,h)=(a,I_f(h))_2^negative                    (2)

is a nonzero map A tensor D5 -> A and spans the same one-dimensional Hom space as L_can. Since the latter was proved nonzero in ACTUAL-CANONICAL-RAW-CUBIC-HAS-A-NONZERO-LINEAR-LIFTING-CORRECTION.md, it is a nonzero scalar multiple of(2).

The complete universal identity is

    H=-36A^2c X^4s^3t+36AB XY^3s^4
       -108ABc X^2Y^2s^2t^2-36ABc^2 X^3Yt^4
       +36B^2c Y^4st^3.                            (3)

Consequently

    I_f(Y^4)=-20736A^2c s^3t,
    I_f(X^2Y^2)=-10368ABc s^2t^2,

    C_f(t^2,Y^4)=-248832A^2c st,
    C_f(t^2,X^2Y^2)=-41472ABc t^2.                 (4)

Both are NONZERO for every abstract tensor satisfying the actual symplectic and smoothness hypotheses. In particular(1) is nonzero. This uses the whole nonzero scalar already established for L_can, not an inference that arbitrary nonzero composable maps have nonzero composite.

## 3. Relative normalization and its limit

Write

    L_can(t^2,Y^4)=ell st.

The raw cubic theorem proves ell!=0. Equations(2)-(4) give the exact relative identity

    L_can(t^2,X^2Y^2)=(B/(6A)) ell t^2.            (5)

Thus the two correction values are linked without a second actual cochain computation.

In the DISPLAYED raw-cochain/second-symbol conventions of that theorem, ell is represented by -A/(2Bnu), up to the common fixed trace/boundary sign. In those same frames (5) is correspondingly represented by -t^2/(12nu), with the same sign. This is not an assignment of an invariant numerical scalar: the physical equation normalization and representation conventions remain part of the identification. The invariant conclusions are nonvanishing and the proportionality to a in(1).

## 4. Why the term can affect the fourth detecting quotient

In a reduction whose D5 cubic block is identified with the canonical raw tensor, the fourth representative is

    B4(a)h-B3(a)|A L_can(a,h).

For a=t^2,h=X^2Y^2, equation(5) makes its second term a nonzero scalar times B3(a)|A(a). Its C5 target character is

    3*2+2=8,

exactly the character of the square cokernel. Thus the term is NOT excluded by weights. Its actual value might still vanish or cancel the first term; neither its composite nor the fourth quotient is evaluated here.

An arbitrary Schur reduction has its own transformed third source correction. The comparison with L_can must be retained before transporting(5) into that reduction. This note does not identify all gauges or remove the four-channel fourth-order problem.

## Verification

Run python verify_fourth_square_input_third_correction.py. It checks the universal mixed-transvectant identity, both extracted quartic forms, both contractions, the relative factor B/(6A), and all detecting-character arithmetic. Every coefficient remains formal. Sources are the canonical raw-cubic correction theorem, its exact unquotiented comparison, the C5 linearization theorem, and FOURTH-BOCKSTEIN-AFTER-ACTUAL-THIRD-VANISHING.md.
