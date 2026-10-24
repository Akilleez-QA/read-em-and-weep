# Independent whole-proof review

Status: PASS for the exact frozen proof and selected checker slice below. This is a conditional mathematical review under the complete imported actual-geometric hypotheses, not a realization claim or a reconstruction of the actual maps.

## Exact reviewed artifacts

- PROOF.md: 15,271 UTF-8 bytes; SHA256 `7f1567617b78898bcd218107de5bac5a71342a4cb34411862f7342d13699c4bd`.
- verify.py: SHA256 `02856bf7b47bfb124ef17a2a890beb356d18d8e55b543d9bf949be2007baac76`.
- characters.py: SHA256 `c19423adfb673352bc313c027c2e115dbf3c7b0f01802e452da2d2524b6eaef7`.
- REPRODUCE.md: SHA256 `c3f05644dd74d5b6b19fc34f48d9f347e9814de66e9fde2f3698bb221cec0be2`.
- INPUTS.json: SHA256 `ba4d8bf05de5fd32b0ef61ee55eb9d701971d48bb3f3c75a34cdeca65bce28c5`.

All three complete direct source texts and the entire final PROOF.md were read. Each source was independently fetched afresh from its exact GitHub commit and path. Its full UTF-8 byte length, SHA256, and computed Git blob SHA1 matched both the retained local text and the immutable source record; each computed blob SHA1 also matched the remote response. Compact details are in REVIEWER-AUTHENTICATION.json. Raw response duplicates remain local-only and are not selected publication artifacts.

## Mathematical audit

1. The actual saturated flag, full fifteen-dimensional constant span, second and third jets, and full coherent image of the earlier beta_K are retained hypotheses from the complete PR1209 input. No smaller bundle is assigned a theorem valid only for the original rank-seventeen bundle.
2. The equivariant extension for J/F is correctly split by H1(O(-8))^G=(Sym6 W)^G=0. Constant restriction, rather than a connection on a quotient, places derivatives of F inside J. The resulting normal target is a genuine subbundle O(2)+O(10).
3. The partial coefficient system injects into the complete degree-eighteen system. The universal complete order-three kernel Sym14 W(-4) contains the actual J^-; completeness of the actual fifteen-dimensional system is not inferred. This justifies top F<=-4. Full span of F independently gives H0(ann F)=0 and hence negative top for the dual rank-five bundle.
4. The rank-one capacity lemma uses the actual successive saturated kernels. Each derivative quotient coherently injects into the preceding quotient twisted by -2; nonzero negative horizontal subbundles are impossible. Thus the chain terminates after the specified number of ranks, while arbitrary zero divisors in the injections remain allowed. No quotient connection or saturated-image substitution is used.
5. Center-evenness and the absence of nontrivial characters justify even a and b. The annihilator transpose gives the coherent injection O(b)->O(-a-2), not an unproved equality. The nine-step primal and four-step dual capacities yield a>=4 and b>=-8, hence a<=6. The only remaining even choices a=4,6 have zero equivariant Hom into O(2)+O(10). In particular a possible O(10) scalar quotient is excluded by the dual bound, not overlooked. Rank zero is independently excluded by negative degree.
6. Rank two of the dual derivative gives rank S^-=3. Actual containment dT2 in T3 in S yields T2 subset S^-; equal generic rank and saturation in the same constant ambient justify equality of sheaves. Dualizing the genuine flag gives the stated split quotient S/S^-. Generic rank two fills the rank-two normal subbundle only after saturation, giving F^+=J without asserting coherent surjectivity.
7. The actual coherent image I is torsion-free and therefore locally free on the smooth curve. Its torsion quotient in its saturation has length delta, so deg I=12-delta and deg F^-=-76+delta. The determinant divisor is invariant and supplies delta>=12 when nonzero. This delta is correctly kept distinct from the original t=0.
8. The strict-top argument is valid: a hypothetical O(-4) line in F^- is an ordinary direct summand of F by its top bound. Its derivative into (F/U)(-2) vanishes by degree, contradicting negative horizontality. No chosen splitting is assumed horizontal. Rank eight and top at most -5 give delta<=36.
9. All stopping boundaries are respected: no actual instance data or evaluations, fourth-jet separation, exact new defect, coherent fullness, longer flag, algebraicity, realization, or whole-branch exclusion is asserted.

No mathematical gap requiring revision was found in this exact proof.

## Independent selected-only replay

A fresh temporary directory contained only PROOF.md, INPUTS.json, REPRODUCE.md, characters.py, verify.py, and the three complete retained source texts. It excluded all raw responses, reviewer records, existing caches, and later research. Both `python verify.py` and `python -O verify.py` returned PASS with 51 reported checks and the exact frozen proof hash. The helper's physical-W recurrence checks remained active as well. REVIEWER-CHECKER-REPLAY.json records the exact selected-file hashes and both successful runs.

The checker replay verifies the specified source pins and small fixed universal representation, capacity, and degree identities. It is not a substitute for the whole-proof sheaf, differentiation, saturation, and negativity audit recorded above.
