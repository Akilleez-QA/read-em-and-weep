# Source provenance and inherited display correction

The public null-second-order-raw-closure proof is cited at commit 4ae1ba6081db6563389d5ff78597cf2e98ecc04f, Git blob a3894976f186b3f3bfb4d4953497c468ae041b3b. The included snapshot is identical to the earlier accepted packet's snapshot. Its exact SHA256 and the accepted local input hashes are in `source-pins.json`; all included bytes needed by replay are additionally pinned in `manifest.json`.

The accepted structural-closure proof §6 contains an incomplete first-lift display. It prints

    U_r,jk g_ij+g_jk U_r,ij+mu_r(g_jk,g_ij)=b_r,ijk g_ik.

The U_r,ik term is missing from the right. The correct equation is

    U_r,jk g_ij+g_jk U_r,ij+mu_r(g_jk,g_ij)
        =U_r,ik+b_r,ijk g_ik.

The immediately preceding proved identity δ_row x_r=b_r Id−C_r gives the corrected equation directly on multiplying by g_ik. The following defect formula also uses that corrected equation. Both the new producer proof and its independent review disclose this omission and use the correct cochain identity.

The inherited dependency snapshots in this packet are deliberately unchanged. No silent correction, replacement theorem, or historical receipt is introduced. During final packaging the separate versioned correction was completed and independently accepted. Its corrected proof is included as `dependencies/structural-raw-closure-v2-PROOF.md`, SHA256 50ec1df804dc461c928dfcd8bba8d4428206e36a0b7f1686a9aa2f43731db490, alongside `dependencies/structural-raw-closure-ERRATUM.md` and `dependencies/structural-raw-closure-ERRATUM-REVIEW.md`. Use that corrected display for new references. The original proof and review snapshots retain their original names and exact bytes. The new same-pair proof itself remains unchanged at its independently reviewed hash; its explicit correction note is now backed by this included versioned erratum.

The new proof was independently accepted at SHA256 587f953427e40b33c2758e221dfb4f7cdde1798c9ab9bb09a180c78ba4b127cc. Its geometric argument and scope were also read and independently checked by a second reviewer. The included independent word control tests only universal formal identities and rejection sensitivity, never physical source values.
