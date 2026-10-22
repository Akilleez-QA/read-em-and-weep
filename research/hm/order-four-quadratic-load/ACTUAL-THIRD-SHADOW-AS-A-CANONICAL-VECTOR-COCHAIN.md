# The actual third shadow as a canonical vector cochain

## Result and convention

The actual lower normal-operator shadow can be represented entirely in the V-valued cohomology of O_L(-6), with its diagonal eliminated by the unique primitive from the Gram theorem. On a pure quintic overlap, let p=p_ij and g_j=g_i+p f. The harmonic discrepancy K is in the TARGET j-frame. Choose the fixed physical normalization q0=nu q and retain its factor 1/nu throughout.

Let v_i be the unique local scalar primitive furnished by the actual Gram lift, normalized so that

    v_j-v_i=tau(p_ij,n_h).

Then the actual vector cochain is

    R_ij=-K21+(2k/3)a^2 p_ij v_i.                  (1)

The lower class is represented by R/nu in H1(V O_L(-6)), modulo the actual connecting image of A. Multiplication by a and the upper connecting quotient yield its class in P4, after which the actual second-Bockstein image is still to be divided out. Formula(1) is an actual representative reduction, not a calculation of its final value.

All displayed ordinary differences use the matching coefficient frames. On a base-frame overlap they mean the corresponding transported Cech differences; the physical factor nu is transported as well. A fixed global positive Gram normalization may make nu constant, but the argument does not discard it.

## 1. Exact elimination in the target frame

The harmonic theorem and the canonical diagonal theorem give

    S_ij=2f g_j K11-f^2 K21,
    K11=-(k/3)a^2 tau(p_ij,n_h).

Set d_i=-(k/3)a^2 v_i. In these frames the Cech difference is

    delta(2f g_i d_i)
      =2f g_j(d_j-d_i)+2p_ij f^2 d_i.

Since d_j-d_i=K11, subtracting this exact square-ideal cochain from S gives

    S-delta(2f g_i d_i)=f^2[-K21-2p_ij d_i]=f^2 R.

This proves (1). Using g_i in S instead of g_j would change the intermediate formula and omit an essential p-dependent term if not compensated. The source/target convention is part of the assertion.

The unique primitive exists because tau(p,n_h) is the connecting obstruction under the actual dual quintic sequence

    0 -> O(-2) -> P4 O4 -> V O6 -> 0.

Its class is an equivariant map D5->H1(O(-2))=1, hence zero, while H0(O(-2))=0. The actual Gram theorem identifies its unique lift with c i(5)Qh. Evaluating the corresponding functional on local quintic lifts gives v_i, so this primitive is pinned to the actual nonsplit extension rather than an arbitrary local model.

## 2. Exact global quotient and final cup

The degree-eight square-ideal sequences at the two twists are

    0 -> V O(-6) -> P4 O(-4) -> O2 -> 0,
    0 -> V O(-4) -> P4 O(-2) -> O4 -> 0.

Here the first inclusion is multiplication by f^2 and the quotient records the fg coefficient in local quintic frames. Their connecting maps yield

    H1(P4 O(-4)) = H1(V O(-6))/A,
    H1(P4 O(-2)) = H1(V O(-4))/D5 = P4.

The injections of A and D5 follow from the vanishing global sections of their middle bundles; they are the ACTUAL extension boundaries, not freely chosen representation embeddings. Multiplication by a commutes with these exact sequences. Consequently the A ambiguity in the lower class maps into the D5 ambiguity upstairs. This is the sheaf-level reason (1) defines the correct final P4 class.

The dimensions are 15-3=12 below and 9-5=4 above. The actual third value is the resulting P4 class modulo im(beta2_a), with the already fixed normalization and boundary sign. The canonical vector representative does not remove that final quotient.

## 3. A shorter universal expression

For binary quadratics p,n, the exact transvectant identity is

    tau(p^2,n)=6p tau(p,n)-2tau(p,p)n.

With Gamma and the SOURCE coefficient m_h,i=(h f_z-n_h g_i)/f from the canonical diagonal theorem, equation(1) becomes

    R = k a^2[-2tau(p,m_h,i)/15+2p tau(p,n_h)/5
              +tau(p,p)n_h/5-tau(h,p_z)/15+(2/3)p v_i]
        -tau(p,Gamma)/30.                         (2)

The occurrence of m_h,i remains in the source frame even though the trace and K discrepancy use the target frame. No m_h,j substitution is made. The last term retains the actual global scalar inverse and its f-linear local corrections. The other terms retain the actual quintic extension and Gram primitive. Neither part can be independently discarded, and no value of their sum in the global quotient has yet been proved.

## Sources and verification

Use ACTUAL-UPPER-QUARTIC-IS-A-GRAM-COMPOSITE.md for the unique actual lift; ACTUAL-CONE-DIAGONAL-IS-CANONICAL-RESIDUE-INVERSE.md for K and Gamma; and VERTEX-QUINTIC-RELATION-EXTENSION-AND-SQUARE-P4.md for the actual square extension. The global trace-to-square-ideal comparison is the one proved in ACTUAL-DEGREE-EIGHT-NORMAL-OPERATOR-QUOTIENT.md.

The companion verifier checks the target-frame subtraction, the universal transvectant identity, and the cohomology dimensions. It contains no selected HM coefficients or actual map/rank evaluation.
