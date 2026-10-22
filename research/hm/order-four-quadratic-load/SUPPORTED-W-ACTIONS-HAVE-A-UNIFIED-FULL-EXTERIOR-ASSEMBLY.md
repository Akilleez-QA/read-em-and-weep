# Supported W actions have a unified full exterior assembly

All coefficient symbols in this statement are free. The statement is a
universal exterior-algebra identity, not an evaluation of a Horrocks–Mumford
source, point, matrix or rank. Use the determinant pairing, positive-form
raising/lowering maps `up,low`, and six-space determinant adjoint `adj6` of
`NEGATIVE-EULER-REPAIRS-HAVE-A-CANONICAL-FULL-SOURCE-BALANCE.md`.

Let K be any six-space coefficient endomorphism, let r be a positive polar
vector, and let T be any endomorphism of the negative two-space W. On VVW
three-forms let F act by K tensor T, and set it to zero on the other
three-form sectors. Its determinant adjoint on mixed two-forms is

    up adj6(K) low tensor (tr(T) I − T).

The scalar term in the second factor is essential. In particular the adjoint
sign for the identity action is opposite to the sign for a traceless action.
No independent rescaling of a pairing frame is silently made.

Write E for the positive wedge matrix of r. If Y_i is the positive one-form
coefficient of an arbitrary input two-form in negative slot i, define

    A = K E + E up adj6(K) low,
    B = E up adj6(K) low.

Then the **entire three-form before the final contraction** in negative slot j
is

    A sum_i T[j,i] Y_i − tr(T) B Y_j.                       (1)

Consequently the full supported skew action is i_x applied to (1), summed
over the two negative slots. This equality is valid for every input two-form;
closedness is not required. The operator ignores input VV and WW and has no
output WW. In particular (1) retains every mixed coefficient, not only the
principal VV shadow.

To prove (1), apply F to r wedge eta and subtract r wedge F-adjoint(eta).
The first term contributes K E tensor T. The second contributes minus
E up adj6(K) low tensor (tr(T)I−T). Collecting these terms proves (1).
The determinant-adjoint formula follows directly from the alternating
pairing on W. The verifier also checks this pairing identity before using it.

## Exact source specializations

Let j=i_w omega_W and let Y_L be the stacked Clifford matrices. The fixed
b-source has mixed coefficients Y_i=−j_i Y_L p. Put

    X_plus = K E Y_L + E up adj6(K) low Y_L,
    X_adj  = E up adj6(K) low Y_L.

Its full precontraction output in slot j is therefore

    −X_plus (T j)_j p + tr(T) X_adj j_j p.                 (2)

The a-source is annihilated completely, since it has only VV coefficients.
For the marked negative Hamiltonian D and N=−2j tensor w, retain

    t=−D j,        [D,N]j=4a j.

Thus the fixed-D, commutator-[D,N], and identity-W contributions to (2) are,
respectively, X_plus tensor t, −4a X_plus tensor j, and
(E up adj6(K)low Y_L−K E Y_L) tensor j. These are complete source identities,
not additional source filters. In particular identity-W additions leave the
principal U reconstruction unchanged but can change its entire mixed error.

`universal_supported_w_action_assembly.py` implements (1).
`verify_supported_w_action_full_assembly.py` checks all36 K coefficients,
all4 W-action coefficients, all3 polar coefficients and all20 input
coefficients simultaneously, the literal determinant adjoint, and both
source identities. No actual fourth division or Bockstein value follows
from this assembly identity alone.
