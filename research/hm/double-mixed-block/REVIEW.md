# Independent whole-proof review

Status: approved as a structural mathematical proof, conditional on its three authenticated input theorems. This is not a formal proof-assistant certification. No mathematical correction is required for the reviewed bytes.

The complete final versions of PROOF.md, verify.py, INPUTS.json and REPRODUCE.md were read and reviewed together. This review binds these exact SHA256 values:

- PROOF.md: `a9af8bf8c45b6f64eef63028478e14b1131a0bd111e771b788cda8a7fa413b11`
- verify.py: `7ea8c5cae014cde45e930e1631ae2b86d31eb99a663753d07e8cc9c67237e70e`
- INPUTS.json: `1c4f7eefa4b2d5aa837a339c9172c7bb79a881e8d200ed7ea864f706c1af50bd`
- REPRODUCE.md: `e852dc3d59efdceb771e2ccda38b3c83b41eb90277101e1ffdb54dd1c256e939`

## Authentication and replay

Each original was independently fetched from Akilleez-QA/read-em-and-weep at the exact commit and path in INPUTS.json. For each one, the Git blob identity was independently recomputed from the returned UTF-8 bytes. That identity agreed with the connector's returned identity and the manifest, and the bytes agreed exactly with the local audit copy:

- FIRST: 10079 bytes, blob `790c9b90937ab6e435c2f0691ca2ccd9e94795fb`.
- AMPLE: 10865 bytes, blob `3f68598d395b2672462e5529994e4f7788be2f94`.
- MONAD: 12903 bytes, blob `92e389cc07e7c2e61b64a04b17b91d0c1650c7dd`.

Both `python3 verify.py` and `python3 -O verify.py` passed. The checker uses explicit failure tests, so optimization does not disable its conditions. It checks a fixed nine-class representation table, its square-class map, the imported full middle Euler formula, the channel identities, universal rank/degree balances and input identities. These are abstract character and bookkeeping checks, not evaluations of actual HM maps. The geometric deductions remain the mathematical proof's responsibility. The reconstruction commands in REPRODUCE.md produce exactly the audit-copy paths expected by the checker.

## Mathematical findings

1. The inputs concern the same original full cohomological pencil. FIRST supplies its source character, actual kernel A O(-6), and the earlier marked T6. AMPLE proves surjectivity of the complete two-coefficient map W tensor U -> N, not surjectivity of an individual 44-to-46 map. MONAD Section 3 derives the actual 46-dimensional positive target character. Its unrelated formal factorization constructions are not imported.

2. The multiplicity argument is valid. The canonical evaluation Hom_G(T6,U) tensor T6 -> U_T6 is an isomorphism. The fixed decompositions show that only this isotypic source can reach V and that the three channels from it each have intertwiner dimension one. Surjectivity of the full coefficient map therefore forces the multiplicity map f_V:C4 -> C2 onto. Rescaling its intertwiner cannot change its kernel, so K is a canonical two-dimensional multiplicity subspace. No numerical actual map has been evaluated.

3. The argument applies to every nonzero multiplicity direction in K, not only to the old marked line. If both remaining channels vanished, T6 O(-1) would inject into the full kernel A O(-6), contrary to H0(O(-5))=0. If only D remained, its universal contraction has kernel O(-6); the required equivariant injection into A O(-6) would be an invariant vector in A, which does not exist. If only P remained, tensoring quadratic contraction by W' gives kernel W' O(-3), whose maps to A O(-6) vanish because H0(O(-3))=0. The induced maps into the full kernel are genuinely injective because each selected source is an actual subbundle of U O(-1). Thus both f_P|K and f_D|K are injective.

4. The universal contraction sequences used in these contradictions have the correct degrees and equivariant linearizations. They are the dual complete quintic and quadratic evaluation sequences, twisted by -1. The identities T6=Sym5 W=W' tensor A and P=W' tensor W select the required unique channels. In particular the D-only contradiction needs equivariance, whereas the P-only and zero-map contradictions already hold without equivariance.

5. Injectivity on K selects actual canonical target multiplicity images of dimension two each. The resulting source and targets are embedded subspaces, not merely representation labels. Nonisomorphism of V, P and D shows that the complete restricted coefficient map has image exactly N_P,K plus N_D,K and kernel exactly K tensor V. The coefficient kernel must not be confused with the sheaf kernel of the pencil: the latter is zero on this block.

6. Section 4 resolves the potential relative-alignment issue. The maps f_P|K and f_D|K themselves identify their respective images with the same K. These are separate invertible target identifications, so no unaccounted-for relative two-by-two matrix remains. The two nonzero components of the quadratic evaluation model span the respective one-dimensional intertwiner spaces. After choosing them as normalizations, the actual block is K tensored with that model. This proves a locally free quotient isomorphic to K tensor V O(2), everywhere on the line, rather than merely a matching character or generic rank. The statement appropriately distinguishes canonical actual subspaces and cokernel from scalar-dependent model identifications.

7. The old marked T6 lies in U_K because its V channel vanishes. It therefore gives a marked line in K, while neither a second line nor a complementary splitting relative to the first is canonically selected. The doubled block is a genuine structural strengthening of the earlier single-copy statement.

8. The inherited residual presentation in Section 5 is exact. Write E0=U_K O(-1) and B0=m(E0). The block is fiberwise injective, and its locally free quotient inside N_K O implies that Z=N O/B0 is locally free. Since B0=m(E0), the kernel of the induced map U O(-1)/E0 -> N O/B0 is canonically (ker m+E0)/E0. Its intersection ker m intersect E0 is zero, so this kernel is the original A O(-6). The induced cokernel is the original C. This verifies the claimed actual 32-to-34 presentation without discarding remaining off-diagonal maps.

9. The target extension has the stated direction: 0 -> K tensor V O(2) -> Z -> (N/N_K) O -> 0. Its ordinary Ext1 vanishes by H1(O(2))=0; averaging a splitting makes it equivariant. Equivalently, choose a constant equivariant complement to N_K in N. Neither argument supplies a canonical splitting, and the proof does not claim one. Subtracting the selected 2P+2D leaves constant character 1+4A+2V+P+D of dimension 28. The weighted term has rank six and degree twelve. Thus rank Z=34, and the residual complex gives rank C=34-32+3=5 and degree C=12+32-18=26.

10. The scope boundary is preserved. The rank-six weighted term embeds in Z, not necessarily in the rank-five C; the proof explicitly retains possible intersections with the image of other source summands. No identification with separately embedded modules, source-pair selection, surviving opposite-bundle type, terminal string branch or vertex scalar follows.

## Review scope

No actual HM/source coefficient, point, parameter, jet, derivative, instance matrix, instance rank or scan was evaluated. External actions were read-only source authentication. No external write or publication was performed.
