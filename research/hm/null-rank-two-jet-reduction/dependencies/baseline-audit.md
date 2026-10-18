# Exact full-gerbe scalar-free baseline M0

Use the pinned `crossResidual` and `globalCross` [source formulas](https://github.com/Akilleez-QA/read-em-and-weep/blob/08b73637d4136f91606aad332c46cafd064417f8/research/hm/current-scalar-geometric-dependencies/data/source-formulas.js). Put A=g_ab, B=g_bc, G=g_ac, p=(1,2), q=(3,4), and u0_r,ij=g_ij k_r,ij. These are matrices from the first endpoint to the second; products act right to left.

Define mu_r(X,Y)=((partial_r1 X)(partial_r2 Y)-(partial_r2 X)(partial_r1 Y))/2. The complete raw mixed baseline is

    Z = u0_p,bc u0_q,ab + u0_q,bc u0_p,ab
      + mu_p(u0_q,bc,A) + mu_q(u0_p,bc,A)
      + mu_p(B,u0_q,ab) + mu_q(B,u0_p,ab)
      + (B_13 A_24 - B_14 A_23 - B_23 A_14 + B_24 A_13)/4
      - b_p u0_q,ac - b_q u0_p,ac - b_p b_q G.

Then M0=G^-1 Z. The mixed second derivative block has factor1/4, not1/2. Each mu has factor1/2. A derivative of u0 must expand as (partial g)k+g(partial k), preserving noncommutative order. The k used here is -K/2 with K=((partial_r1 g^-1)(partial_r2 g)-(partial_r2 g^-1)(partial_r1 g))/2. Thus k's direct derivative-product coefficient is -1/4.

## Selected entries and tracefree scope

For entries indexed0,1,

    M0^0_10 = (G^-1 Z)_10,
    M0^0_00 = ((G^-1 Z)_00-(G^-1 Z)_11)/2.

In particular the diagonal request cannot use M0_00 without its M0_11 companion. The complete baseline includes all three gerbe terms. Only after the exact identity G^-1 G=I and tracefree projection may the central term -b_p b_q I be omitted from these two requests. This is an exact matrix projection, independent of any argument about central cohomology. The noncentral terms -b_p k_q,ac and -b_q k_p,ac remain. Dropping them would change the convention for the separate +F_p k_q+F_q k_p contributions in Rsharp.

## Owners and legal reuse

Every raw summand has endpoint type c<-a; left multiplication by G^-1 makes an endomorphism at a. k_ij is an endomorphism at i; u0_ij=g_ij k_ij has type j<-i. Frozen-frame conjugation therefore agrees with the already established adapter for every term.

Exact identical subexpressions may be shared: the same owned transition, derivative, inverse, k or u0 on the same ordered edge and pair; the same normalization inverse G^-1; and entries required by both the10 and tracefree00 requests. Sharing must include endpoint/common-vertex ownership, derivative multiindex, pair, and frame convention. Equal carrier labels alone do not make the transitions or legal jets identical. No commutation of endomorphisms, equality of different edge values, or old scalar-corrected u with u0 is licensed.

If a circuit chooses to simplify G^-1 B=A^-1, it must supply the exact transition cocycle witness G=BA. That simplification is unnecessary for the baseline formula and is not used in these independent controls. G^-1G=I is the only identity needed to remove the central term after projection.

## Formal controls

`test_m0_baseline_formal.py` has6 passing tests. Its17 signed raw free-word terms consist of2 quadratic terms,8 expanded mu terms,4 mixed second-derivative terms and3 full-gerbe terms. It checks exact rational prefactors, endpoint composition, noncommutative ordering, product differentiation, and tracefree scalar cancellation. It uses only formal matrix atoms and rational constants; no physical source polynomial or residual is evaluated. This certifies the formula and interface, not the arithmetic cost or a completed coefficient circuit.

## Conditional selected quadratic contraction

With the exact transition cocycle G=BA, set Xp=A^-1 k_p,bc A and Xq=A^-1 k_q,bc A. The normalized quadratic terms are Xp k_q,ab + Xq k_p,ab. All four matrices are traceless: differentiating the inverse shows tr(K) is the trace of a commutator, and conjugation preserves trace.

For any traceless2x2 matrices X,Y,

    tf(XY)00=(X01 Y10-X10 Y01)/2,
    tf(XY)10=X10 Y00-X00 Y10.

This follows by substituting X11=-X00,Y11=-Y00; the X00Y00 terms cancel in the diagonal difference. Each ordered product uses four scalar entry products for these two selected entries, hence eight for the sum, GIVEN the required entries of Xp,Xq,kp,kq. This is a conditional contraction count, excluding construction/conjugation, derivatives, other baseline terms, weights and coefficient extraction. It does not assume the two ordered products commute or have interchangeable entries. A seventh formal test checks the exact surviving free-entry words and their coefficients.

