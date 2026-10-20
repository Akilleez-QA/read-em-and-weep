> Historical mathematical record, 16 October 2026. Statements of PASS and check counts below refer to the original recorded verification, not a new execution. See PUBLICATION-SCOPE.md at the common series root for current scope, imported premises, and source/public hash bindings.

# Independent audit: a second harmonic position detects the missing positive four-space

## Result

**PASS.** At the one additional position

    kappa'=(-2,-1,-2,-1),

the original constant rows indexed by K30 coordinates9,4,5,12 have exact values

    -w0, +w1, -2w2, -w3,                         (1)

on the authenticated inversion-positive epsilon class. No actual w-coordinate is acquired or evaluated here.

Together with all30 constant rows at the earlier position kappa=(-1,-1,-3,-3), these four rows form a complete detector family on the positive12-dimensional target. This follows from the previously proved first-position kernel and the four explicit second-position witnesses, without a rank calculation or an81-position sweep. This result does not assert completeness on the full epsilon32 target or on the full352-dimensional full-sign sector.

## 1. The actual monomial and canonical trace

For the full-sign internal-degree−2 scalar line O(-4,-4,-4,-4), the Serre-dual finite monomial is x^(-kappa'-1)=x1 x3. Its global homogeneous form is

    q'=X1Y1 Y2² X3Y3 Y4².

Let H be the eight-element pair-partition stabilizer12|34, with epsilon its restricted sign character. Since a is epsilon covariant and U is H invariant, the canonical alternation of q'aU^j equals that of its H-average times aU^j. The average is exactly

    average_H(q') = v0(v2-U)/4 = -2 v0 W1,
    W1=(U-v2)/8.                                (2)

The four cross-pair monomials in this average occur twice in the eight-element sum. Here v0=Y1Y2Y3Y4, not the affine constant from a different chart convention.

The authenticated dual-trace identity is Alt(W1 a U^j)/Delta=delta_(1,j), with unnormalized24-term alternation and the fixed ordered volume. Thus

    Alt(q' a)/Delta=0,
    Alt(q' aU)/Delta=-2v0,
    Alt(q' aU²)/Delta=0.                         (3)

The independent checker verifies (2) in all eight homogeneous Cox variables and verifies all three equations(3) directly by their24-term polynomial alternants. No sampled point, affine extrapolation, or source coefficient is used.

For any original constant degree+2 graph cycle E, the q' detector is consequently

    D'_(E)(G0,G1,G2)=-2 Tr_P4 Str(G1 v0E).       (4)

In particular it has no G0 or G2 component. The line degrees are correct: E belongs to B(-2), v0E belongs to B(-1), and G1 belongs to B(-4), so their product belongs to O(-5). The full homogeneous q' has degree2 in each P1 pair and preserves the original scalar-line/canonical-line comparison. No variable inverse is introduced.

## 2. The necessary positive projector

Unlike v2, v0 is not inversion fixed: rho(v0)=v4. Therefore the saved196-dimensional positive twist−1 quotient cannot be applied to an unprojected v0E. The required input is

    z_E=P+(v0E)=(v0E+v4 I(E))/2.               (5)

The actual producer code implements(5). In the stored positive orbit basis e_i+s e_j, a raw e_i contributes1/2 at the representative and a raw e_j contributes s/2. Positive fixed entries contribute1; negative fixed entries are omitted. These are exactly the coordinates of(1+I)/2, with no concealed basis normalization.

The independent checker uses a different route: it explicitly reverses each homogeneous full400-coordinate term using the original chain signs, forms (5) in that full basis, reads its representative coefficients, and re-includes them to verify equality with the full projected vector. It then checks the saved outgoing differential vanishes before applying the saved quotient map Q. This is important because Q's quotient interpretation is certified on cycles, not arbitrary ambient vectors.

The original graph uses E13[c,i] as free coordinate r=15c+i and

    E02[5c+k,a]=sum_i E13[c,i] gamma[i,a,k].      (6)

It is the same original30-row classification and genuine supertrace sign binding authenticated in `../hm-single-kappa-detector-independent-20261016/AUDIT.md`.

## 3. Four exact saved-map witnesses

The input certificate is `../hm-plus-twist-minus1-quotient-20261016/certificate.json`, SHA256

    616006681d2952a3d895e2bf369d2c5813a9091c38a490b9bd936c2299e5de3c.

Its full degree2 basis has400 entries, its positive basis has196 entries, and its supplied quotient map Q has four output coordinates in the fixed C0,...,C3 basis. The complete quotient identities were already independently audited; no elimination is repeated here.

Direct product verification gives

    Q(P+ v0 E9)  =  C0/2,
    Q(P+ v0 E4)  = -C1/2,
    Q(P+ v0 E5)  =  C2,
    Q(P+ v0 E12) =  C3/2.                       (7)

Here Er means the r-th K30 graph basis cycle, not the originally named detector r. Equivalently these four original constant rows are L_(9,0), L_(4,0), L_(5,0), L_(12,0). The positive four-coordinate basis is exactly the one used to define w0,...,w3 in the positive12 interface.

Multiplying(7) by the actual trace factor−2 in(4) yields(1). This explicit diagonal witness is enough to prove the second-position map onto the four positive w coordinates. No rank search, row reduction, claim about the rank of an unspecified multiplication map, or inspection of source values is required.

## 4. Why the pair of positions is complete on positive12

The earlier single-position audit proves that all30 rows at kappa have common positive kernel

    K={(-v2 eta,eta,0): eta in H²(B(-4))^+},     (8)

and the four coordinates of eta in this four-dimensional space are its pairings with C0,...,C3. Equations(1) therefore distinguish every direction in K. If both the first-position30 rows and the four second-position rows vanish, then eta=0 in(8), so the full positive class vanishes.

Equivalently, one can retain just eight first-position rows corresponding to the explicit positive K30 basis P0,...,P7 and the four second-position rows in(7). The P_i are fixed linear combinations of original constant maps. Once the w coordinates vanish, their first-position evaluations are4z_i, so this12-row family is complete. This is a structural existence and explicit-row specification; it does not purport to have computed an unprovided8-by4 multiplication matrix or new source values.

The separate geometric theorem placing the actual obstruction in positive12 remains a necessary premise for that application. Completeness of a detector family supplies no value for the actual obstruction and does not prove its vanishing.

## 5. Historical verification

The actual producer receipt reports80 projector contributions and14 Q products. Those counts are independently recovered from graph support and saved-map metadata without recomputing all30 output columns. Only the four witness columns in(7) are independently evaluated. The original producer code and historical receipt are bound by the source-hash manifest.

The independent run passes85 checks in about0.006 seconds, maximum RSS about12MiB. The recorded controls include the homogeneous polynomial identities and the four column checks. It performs no elimination, source acquisition, full81-position batch, new quotient construction.

## Inputs and documentary pins

- Original homogeneous linear model: `../hm-factored-coefficient-action-20261014/pinned-model-input.json`, SHA256 `635bb12d9986e0dcada161d4173c773c4f134b9225354a3bc74267840ca19926`.
- Positive quotient certificate: the SHA256 in Section3.
- Producer `../hm-two-position-positive-completeness-20261016/v0-map.json`, SHA256 `d0fe1426ff300e9b4f5fd2f4c6ec2e9d4e32eb08a89528e4b50008f2fb10be7c`.
- Global dual traces: `../DUAL-TRACE-IDENTITIES.md`, Section1; independently controlled here by direct polynomial alternation for this particular q'.
- The prior single-position, global detector-dual, and positive12 audits supply the complete hypercohomology and Serre conventions, not a new rank inference.

Every actual source coordinate remains unacquired. Other residue branches, coefficient interfaces, source completeness obligations and global source-to-target comparisons are unchanged.
