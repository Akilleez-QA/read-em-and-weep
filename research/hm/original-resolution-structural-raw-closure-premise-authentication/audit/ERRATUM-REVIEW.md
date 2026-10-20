Editorial scope: This is a mathematical source edition. Historical review and check statements describe the original artifact, not a fresh run. Supporting snapshots are dependencies, not additional new results. Later PR145 mixed-class vanishing supersedes historical unknown mixed-class status; it does not resolve the six pure diagonal conditions.

# Independent erratum review: restore the composite-edge first lift

## Decision

**Accepted localized correction.** The original §6 displayed transition equation omitted U_r,ik from its right-hand side. That display was wrong, and the initial independent review missed it. The corrected version restores the term:

    U_r,jk g_ij+g_jk U_r,ij+mu_r(g_jk,g_ij)
        =U_r,ik+b_r,ijk g_ik.

The first-order scalar closure and mixed residual closure conclusions remain valid. The proof's preceding normalized identity, subsequent mixed defect, and original formal control all already use the correct equation. No theorem, domain, scope or execution claim is expanded.

Corrected proof SHA-256:

    50ec1df804dc461c928dfcd8bba8d4428206e36a0b7f1686a9aa2f43731db490

Original proof SHA-256:

    b3c50888630128fc04a784be3a5c2374da017d627c69c504fc6571211a744b5a

Original review SHA-256:

    d7c02a092fc87780b6c3af89c4afb5331ae17a0fe499cfffbd4e39048ade1b41

An exact byte/text comparison proves the corrected proof differs only by this one-line restoration. The originals are preserved in reviewed-PROOF-v1.md and v1-REVIEW.md; the original package, archive and downstream frozen dependencies were not overwritten. The original review is historical provenance, not continuing approval of the erroneous display.

## Independent derivation

Put A=g_ij, B=g_jk, G=g_ik=BA. The proved normalized equation is

    A^-1 x_r,jk A-x_r,ik+x_r,ij=b_r Id-C_r,
    C_r=G^-1 mu_r(B,A),  U_r,ab=g_ab x_r,ab.

Multiply by G on the left. Its three Cech terms become respectively

    U_r,jk A,  -U_r,ik,  B U_r,ij.

The right side becomes b_r G-mu_r(B,A). Rearrangement gives the corrected display. There is no identity allowing the composite-edge term to disappear.

Equivalently, the degree-one coefficient of T_jk*T_ij-h_ijk T_ik is

    U_r,jk A+B U_r,ij+mu_r(B,A)-U_r,ik-b_r G.

This is zero by the correct normalized equation. It is the coefficient used in §7's defect identity, whose tu coefficient is still the same ten-term D. Thus the later mixed-anomaly argument is unchanged, rather than relying on the erroneous displayed shortcut.

The original independent checker defines the composite first lift by

    U_ik=U_jk A+B U_ij+mu(B,A)-b_ijk G.

It therefore already used the corrected equation. Its tetrahedron and mixed-anomaly checks do not support the omitted-term variant.

## Added control and replay

check_first_order_erratum.py uses invented free letters A,B, their formal inverses, three arbitrary x letters, a formal mu letter and a commuting scalar b. It verifies the exact left-multiplication calculation, verifies the later degree-one defect, and rejects omission of U_ik. Without the term the discrepancy is exactly the nonzero invented U_ik. It constructs no numerical or physical matrices and imports no source code.

Both ordinary Python and python -O runs pass identically. The original independent 57 checks and seven mutations and the producer's 20 files, 22 method contracts and 14 mutations also replay identically. The correction-version check binds the exact old/new hashes and unique one-line delta.

This amendment supersedes the initial review only for the erroneous display and its acceptance wording. All other mathematical findings and explicit limitations remain as stated in the versioned full review.
