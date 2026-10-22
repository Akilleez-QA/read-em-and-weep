# Both involution components of the actual corrected fourth input are nonzero

## Complete lower-source interface

For the actual detecting input a=t^2, h=X^2Y^2, write b=L_can(a,h)=gamma a in the already fixed physical and boundary convention. There is a canonical decomposition

    C/J = Cminus direct-sum (Cplus/J)
        = H0(D,O_D(-2,10)) direct-sum P4.

Under this decomposition the actual corrected lower source is

    [v_h-b zeta_a]
      = ( ((r_mid/nu-gamma r_t)/g^2)|D,
          c_eta ke/(3Bc) s(AX^2s+2BY^2t) ).          (1)

BOTH entries are nonzero. Here r_mid is the complete absolute midpoint numerator from ACTUAL-MIDPOINT-ABSOLUTE-SECTION-FOR-THE-FOURTH-SQUARE-INPUT.md and r_t is the complete Atiyah numerator from ACTUAL-ATIYAH-CLASS-HAS-AN-ABSOLUTE-DOUBLE-CUBIC-REPRESENTATIVE.md. The parameters gamma, nu and c_eta are retained separately. In particular c_eta denotes the actual endpoint-minus-midpoint displacement in the same positive-transition convention as the secondary endpoint operation; it is not set equal to the bracket-normalized displacement without its sign comparison.

All symbolic source parameters remain unassigned. Formula (1) determines the lower representative in terms of its fixed actual nonzero normal scale. It does not evaluate that scale, identify a full ambient lift with its cone restriction, or perform the next ambient division.

## Proof of the two entries

The canonical reduced-curve realization and actual first entry were proved in ACTUAL-CORRECTED-FOURTH-SQUARE-SOURCE-IS-NONZERO-ON-THE-CUBIC.md. Its exact polynomial remainders show the first entry is nonzero for every constant gamma: proportionality would require simultaneously nu gamma=1/12 and nu gamma=-1/6. This argument includes the scalar source correction and all polynomial-nine data, not merely the effective twelve-dimensional quotient.

The actual midpoint class is in Cminus, whereas the actual endpoint normal variation modulo J is in Cplus/J. The explicit family reconstruction in ACTUAL-FOURTH-INPUT-ENDPOINT-RECONSTRUCTED-BY-TWO-UNIVERSAL-TENSORS.md gives the second entry of (1). Its canonical P4 projection was calibrated against BOTH fully corrected actual endpoint values. The displayed polynomial is nonzero, and its actual scalar c_eta is nonzero because the actual endpoint differs from the midpoint and the invariant normal direction has nonzero lowest apolar component.

Finally b zeta_a=gamma a zeta_a is entirely in Cminus: the involution fixes the actual restricted Atiyah class and negates a, with the same fixed probe normalization as in the absolute Atiyah theorem. Therefore the canonical source correction changes only the first entry. It neither removes nor renormalizes the second entry. This proves (1) and the two nonvanishing assertions.

## The exact remaining operation

The actual ambient relations are still

    q0 v_h=a h zeta_a,
    q0 w_h=a(v_h-b zeta_a),
    beta4(a,h)=[a w_h] modulo im(beta2_a).

The previously proved third vanishing ensures that the corrected lower source is killed by a in the cone target. It does NOT supply w_h or its final value. In particular, neither entry in (1), nor their simultaneous nonvanishing, proves a nonzero fourth Bockstein. Reconstructing a cone class and dividing its specified actual ambient lift are different steps. The existing generic Smith bound and the unresolved 4-or-5 section alternative are unchanged.

## Reproduction

Run python verify_corrected_fourth_input_two_components.py. It reruns the exact reduced-cubic nonproportionality and the full universal endpoint-family reconstruction. Those verifiers certify the two separate values; their pinned actual comparison theorems and the canonical involution decomposition supply the global interpretation in (1).
