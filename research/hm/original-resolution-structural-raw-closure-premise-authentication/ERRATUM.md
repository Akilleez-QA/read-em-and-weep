Editorial scope: This is a mathematical source edition. Historical review and check statements describe the original artifact, not a fresh run. Supporting snapshots are dependencies, not additional new results. Later PR145 mixed-class vanishing supersedes historical unknown mixed-class status; it does not resolve the six pure diagonal conditions.

Supporting dependency only: this complete source text is not a fresh result of this packet.

# Version 2: missing first-order transition term restored

The first version's PROOF.md §6 contains a genuine error in one displayed equation. After the correct identity delta_row x_r=b_r Id-C_r, the final transition equation omitted U_r,ik from its right-hand side.

Incorrect v1 display:

    U_r,jk g_ij+g_jk U_r,ij+mu_r(g_jk,g_ij)=b_r,ijk g_ik.

Correct v2 display:

    U_r,jk g_ij+g_jk U_r,ij+mu_r(g_jk,g_ij)
        =U_r,ik+b_r,ijk g_ik.

Indeed the definition of the row Cech differential is

    g_ij^-1 x_r,jk g_ij-x_r,ik+x_r,ij=b_r Id-C_r.

Multiplication by g_ik=g_jk g_ij, followed by U_r,ab=g_ab x_r,ab and g_ik C_r=mu_r(g_jk,g_ij), gives

    U_r,jk g_ij-U_r,ik+g_jk U_r,ij
        =b_r,ijk g_ik-mu_r(g_jk,g_ij).

Moving the two negative terms proves the corrected display. The U_r,ik term is essential; the v1 displayed equation is not accepted as written.

The immediately preceding delta_row identity was correct. The subsequent mixed defect T_jk*T_ij-h_ijk T_ik=tu D_ijk in §7, its ten terms, and the independent formal recurrence already use the corrected first-order equation. The two closure conclusions, regularity scope and exclusions are unchanged. No additional theorem or execution claim is introduced. This is the only mathematical change to PROOF.md.

## Preserved provenance

- Corrected v2 proof SHA256: 50ec1df804dc461c928dfcd8bba8d4428206e36a0b7f1686a9aa2f43731db490.
- Original proof SHA256: b3c50888630128fc04a784be3a5c2374da017d627c69c504fc6571211a744b5a. Its exact bytes are retained as provenance/v1-PROOF.md.
- Original review SHA256: d7c02a092fc87780b6c3af89c4afb5331ae17a0fe499cfffbd4e39048ade1b41. Its exact bytes are retained as provenance/v1-REVIEW.md. That review missed this displayed omission; it is historical provenance, not acceptance of the erroneous equation.
- Original archive SHA256: 60889c1aeb1591f6e70411c137f0d125678e94dba3e0c66b4b6cf002e79a418b, 221,772 bytes, structural-raw-closure-20261018.zip.

This version is separately named structural-raw-closure-20261018-v2. The original package and its archive, and all downstream frozen dependency copies, remain untouched. New downstream use should cite the corrected proof and this erratum; historical citations keep their original hashes.

Independent approval of this localized correction and its additional rejection control is recorded in the version-2 REVIEW.md and audit/. The complete bundle manifest and clean portable replay bind the delivered version.
