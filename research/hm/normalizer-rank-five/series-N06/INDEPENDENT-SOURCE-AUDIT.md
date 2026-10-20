# Independent mathematical source and scope review

Review date: 2026-10-20. Status: no blocking mathematical error found in the final alpha/quaternion/Dic3 chain under its stated actual-representation and geometric inputs. This is an independent human-readable derivation review, not formal proof checking. No selected actual source instance was evaluated. Other source audits remain historical evidence, not newly performed checks.

## Scope and conclusion

The current conclusion is **Z5 is empty or equals the distinguished 600-point orbit M**, conditional on the previously established finite-support, rank-four exclusion, conic/canonical-line exclusion and actual-operation representation hypotheses. This is a statement about reduced support, not determinantal scheme length, higher-order deformation, algebraicity, or realization of M. Earlier alternatives containing 250, 375, 625 or 750 are historical intermediate bounds. They must not be exposed as the current frontier. Neither Sylow necessity nor abstract incidence establishes which final alternative occurs.

## Independently checked derivations

1. Finite support: a degree (10,10,14,14) auxiliary complete intersection has length 19600. At residual rank five the local equations have orders at least (1,1,5,5). Replacing the first two by fifth powers and applying the order-five lower bound yields local auxiliary length at least 25, hence reduced support at most 784. This does not give local determinantal length 25. The constant binary-image pencil restricts to degree-eight minors and excludes the zero-cocycle order-five lines using the size-ten remaining orbits.
2. Order four: the off-conic A5 orbit of size 30 cannot lie on a quintic. The gcd of its translated quintics is invariant because A5 is perfect; low-degree invariants are powers of the conic equation. Removing those factors and applying Bezout excludes an off-conic orbit larger than 25. Thus parity-block minors cannot vanish on a genuine 750 orbit without vanishing on the whole plane, contradicting conic rank five.
3. Quaternion: fifteen rotation axes admit no nonzero cubic through all of them. Odd parity rank is even and at least four. The pure even image has rank four when alpha is zero and five otherwise. The nonzero harmonic cubic mixed map adds a direction with nonzero axis-axis matrix entry, absent from the pure F5 image. Total rank nine therefore forces alpha zero. This statement alone is necessary; alpha nonvanishing completes the exclusion.
4. Alpha: for the universal Schur module U, the sum of the 25 conjugate reflections is C=5L with L an involution and trace zero. The actual irreducible target J has reflection trace -4, so C acts by -5; surjectivity identifies ker(q) with the +5 eigenspace. A pure-T tensor has unequal coefficients from its image under L, forcing its projection nonzero. The calculation depends on the actual J parity 8/12, irreducibility, surjectivity, and the stated determinant-one normalizer lift. It is not a selected geometric source-map evaluation.
5. Dic3: cubic interpolation over the ten order-three axes forces odd parity rank at least three. The pure even image for alpha nonzero has dimension six before the possible extra transverse mixed rho. Full Dic3 action makes the transverse gamma map zero or an isomorphism, not rank one. Gamma cannot vanish: a harmonic cubic x(Ax^2+By^2+Cz^2), with 3A+B+C=0, has at (1,1,1) gradient (0,2B,2C), radial only for the zero cubic. Gamma zero would kill all transverse derivatives, including the invariant line since the tangent has no invariant. Thus even rank is eight, total at least eleven, and residual rank at least seven on O250.
6. Independent gamma check: on harmonic cubics, the SO3-averaged second and fourth angular moments of the rank-three T-prime projector are 12 and 84. Gamma zero would give nontrivial C3-line contributions 8 and 32; the invariant line would contribute second moment 4 and fourth moment 36, totaling fourth moment 68, contradiction. This separately verifies the discharge and removes the provisional even-six/odd-three case.
7. Exceptional Sylow: the quadratic clock correction Q(Z) with exponent 2j^2 gives B=DQ^-1 commuting with the order-125 Heisenberg subgroup. Each source clock space splits into four B-eigenspaces of dimension two, while the target has one copy of each. The actual kernel must therefore choose one line in each source eigenspace, yielding the necessary (P1)^4 locus. This does not prove realization or emptiness of the further rank-five incidence.
8. Incidence: the four-cycle/complete-opposite-pair argument gives I<=4+rho+p. The unique abstract I=6 configuration is L=D. Rank-five equality needs either the cycle dependence or a complete opposite pair; the seven listed numerical strata and examples are consistent. Additional all-repeated-input exclusions and full-normalizer compatibility remain necessary. The exceptional projector has not been evaluated.
9. Local sharpness: the C5-equivariant abstract linear model has rank nine at the origin, generic rank fourteen, determinantal support of length one, but an auxiliary complete intersection of length 25. This sharply separates these two lengths. It does not satisfy all global normalizer and repeated-input hypotheses, so it is not an actual global counterexample.

## Orbit and defect prerequisites

The pure point-orbit gap is 250, not 600. Outside the canonical orbit E of size 30, the classified small orbits are O250, two O300, O375 and two O500. After these exceptions, the next size is at least 600. The even-order stabilizer cocycle is killed using the central involution. The 250/375 order-four line character excludes simple isolated defects; the minus 300/500 lines fail the determinant character identity, while the plus lines fail the stronger alternating-form condition. These checks require the separate minimal-local-defect-character theorem, including its nondegenerate alternating-form conclusion, not merely its determinant identity.

The resulting minimum defect contributions are 500, 600, 750 and 1000 respectively. In particular, these sources alone do NOT establish that every noncanonical isolated defect contributes at least 600: O250 with local length two is not excluded here. A stronger O250 local bound or a separate global exclusion must be supplied if that claim is used elsewhere.

The order-five classification source has rank-three applications, but its sections 1, 3 and 4 independently establish the two complement cocycle classes and the unique nonzero-cocycle 600-point orbit. Only those group-theoretic assertions are used for the final rank-five support result; its rank-three assumptions are not silently imported.

## Packaging and dependency findings

- Preserve the newly added 250-point proof and order-five classification as explicit prerequisites, with full derivations and historical audits.
- Import the exact existing full-normalizer alpha proof, finite-support proof, rank-four/conic and small-curve prerequisites rather than counting duplicated copies as new research.
- Import the local defect-character theorem explicitly for N01 defect applications.
- Curve and rank-four prerequisite audits not independently repeated in this review must remain clearly labeled imported/historical. The conditional line-projected reduction needs its quartic-factor, reducible cubic-web and full-support-scroll dependencies.
- Degree-fifteen determinant and quintic divisorial applications need their separate geometric premises. Their pure group-theoretic exclusions must be separated from these applications if the latter premises are not packaged.
- The source documents contain process/evidence-boundary passages. Public normalization may remove process-only prose but must preserve assumptions, proofs, mathematical limitations and source hashes.

## Exact independently read proof hashes

- `normalizer-minimal-point-orbit/PROOF.md`: `17ce89cc8a4425a92fc137f0683d8677391772ca4f1ceeb57513c66ee4588ad1`
- `normalizer-refined-point-gap/PROOF.md`: `9cd9fd040898092779637c811fceb707131ca86c29106a211e6ca510001f9db6`
- `normalizer-250-simple-defect/PROOF.md`: `95a7e84881d1fd4a899933a310b21c9b40e8d691cda4457433ea73664e45413c`
- `normalizer-300-point-orbits/PROOF.md`: `0ece3a7be4fc9748fb0e6a096cb2aae8d7041fc22836f39e4dde75e2c0fc3c17`
- `normalizer-375-point-orbit/PROOF.md`: `399ed76f24892efb680cac22c844adec5d3f07a2c4ed288522a33e7a05bbf351`
- `normalizer-500-point-orbits/PROOF.md`: `5d68590bffa7d3c4ec6cfd6e4df4b54af5ed5144beb218357ae3730b8ebdc904`
- `order-five-rank-three-classification/PROOF.md`: `9c49938927ee10851f1cc40e86a3448f08f94cd4366fd657eab6dc37b104e1ff`
- `rank-five-finite-support-constraints/PROOF.md`: `4e738e328a50598202d99fd21c5da1e94c9c706507f98a11c1d89386454c0a80`
- `order-four-rank-five-exclusion/PROOF.md`: `f14b82248533531630ab409b9c56545d92aabf0a9ee18c576dadf061d2754166`
- `quaternion-rank-five-coupling-constraint/PROOF.md`: `8e8a343cecfb092cc65afc65add2a1c19d900206014eb2be94460d77f66ef541`
- `full-normalizer-pure-t-nonvanishing/PROOF.md`: `8542bac77147760d985bb203a7cbe070f8b6ef9c76efa502a9e078498c1feba2`
- `dicubic-rank-five-axis-constraint/PROOF.md`: `858164b1bc0a50cfd8590a7d9b2b84aed58609413e58c3f1060d6a63de7bcafe`
- `exceptional-sylow-kernel-constraint/PROOF.md`: `ea1ac73d281bec77ac6f7485147d43530a8f8bb4fc5aed14aba7415d9f453fd8`
- `exceptional-incidence-dependency/PROOF.md`: `6fa8a0753823a372383ffebb5385efaa38bdc2e80bb279b6899b59d201cc37ec`
- `rank-five-local-sharpness/PROOF.md`: `a64c9b8685fce7c8858e3bc756cae6a33709a566c7c1358e93ea4be42b955ef6`

Additional historical audit documents and other prerequisites are not represented by this list as newly independently recertified. Source-manifest preservation and final payload hashes are checked separately below.

## Staged payload integrity check

At review snapshot, all 70 staged source artifacts in COVERAGE.json matched both their recorded original SHA-256 and public SHA-256, with zero missing files or mismatches. The normalization diffs reviewed are dependency-path repairs and process-only heading/prose cleanup; no changed mathematical assertion was identified. The newly authored series scope summaries for N06 and N07 preserve the final alternative and necessity-only limitation. This check excludes future edits and does not represent publication read-back.

COVERAGE.json snapshot SHA-256: `d78e836caf45bc89f7b8716bcdb7b2f9c4a629b20c6d12545343cd511a999ec1`.

The nine unresolved contextual locators do not supply a missing lemma in the checked final N06 chain. Conditional determinant/divisorial applications and the extremal-incidence dimension-bound premise remain imported assumptions, not independently established results of this review.

## Addendum: double-defect prerequisite independently checked

The preceding500 lower bound describes the original simple-defect-only dependency set. The complete normalizer-250-double-defect PROOF and AUDIT are now included in N01B and independently checked. All one-dimensional stabilizer characters restrict trivially to the order-three element, while its cotangent action has no invariant vector. Hence a length-two equivariant module cannot have a nonzero radical and must be k^2. For an isolated self-dual rank-two module in regular local dimension four, isolated duality gives Ext1=k^n when Ext2=k^n; the reproduced Koszul generator inequality 5n+t <=3n+t+2 forces n<=1. Thus length two is excluded. Together with length-one exclusion, O250 contributes at least750. With the other small-orbit exclusions and gap in N01, uniform noncanonical isolated-defect contribution is at least600. This stronger bound explicitly depends on the double-defect lemma, and is not a point-orbit bound. No actual-instance or formal-checker evaluation was performed.
