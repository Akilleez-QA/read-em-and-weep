# Alternating scalar remainder

`PROOF.md` derives an explicit exterior-form expression for the full S4-sign projection of the ordered-nerve raw remainder and proposes the regular edge primitive

    P_ij = −[str(B_i³)+str(B_j³)] ∧ (g_ij^-1 d g_ij) / 72.

The B_i are the exact ambient split-connection differences of the unsymmetrized raw scalar. The gerbe correction and the actual split-to-physical scalar frame difference are retained through their respective cancellations. The statement addresses only this full alternating projection, not the remaining complementary sector or a finite-cutoff executable implementation.

This directory contains public mathematics and invented exact algebra only. No physical source evaluation is used.

Verification:

    python check_exterior.py
    python -O check_exterior.py
    python check_chain_blocks.py
    python -O check_chain_blocks.py

See PROOF.md for status and premises. Independent audit is maintained separately by the reviewer.
