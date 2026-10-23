# Independent review: canonical mixed transfer and endpoint-nine coefficient constraint

## Verdict and reviewed artifacts

**PASS**, with the stated compatible pure-V actual-source hypotheses. The transfer is independent of its equivariant section, its bilinear factorization is literal, and the diagonal agrees with the uniquely normalized quadratic lift with a plus sign. In endpoint nine the actual lift lies in the pinned R1 line, allowing zero. No alternating scalar or source branch is selected.

Reviewed SHA256:

- `PROOF.md`: `05554bd1bd93401fd77f6430cd93318cc81413665e029d03af173cd8fb3883d9`
- `verify.py`: `b70c87b414d9f9368eda8206a70a2d4f6365c1ecb5dec22200a65db4ace00169`

## Authentication

All seven originals were freshly retrieved at their exact repository paths and immutable commits in `INPUTS.json`. Retrieved bytes equal the retained files, with independently computed SHA256 and Git blob hashes matching the manifest:

| Input | Commit | Git blob |
|---|---|---|
| PR1019 | `3fb2475ffb275c5789acbaa8f9f84ed272713785` | `bf63c14f76933d59fa7e3ac61aecb3366ac1b442` |
| PR1022 | `5488bc153029391d647c3e18d9344e4e00e38a7f` | `ed25430f8e5ffb0f46c2b642d8d27467db492985` |
| PR1025 | `09f1377f83b027ca27eea0b3a9f40a1b92c6c466` | `d036adcf5bc2bfc53e07cd752ff180c5993251f7` |
| PR1048 | `9eaed2dfadf9c4877327d21db5974b6c94d3863d` | `0710577541a79a5d8d56e5aa693a8fc01c559112` |
| PR1059 | `af2f163e4bcc593b6895ace840c139d2d4668cde` | `2b00a40de04a7084ff2f08c767fdd2f4f13ae5f4` |
| PR1031 | `7150cf97eeebe473bcd7c61c1f968c73625d92ef` | `0694e96e2d17a53b68d625ec6065f8bf513cd083` |
| PR1036 | `bb22e239e9423b54487236dba8c4f70f9e6b738f` | `718f987511b5bf6144a85fc14e8ef343612a4491` |

This authenticates the retained proofs, not all historical dependencies recursively. The graph component's value is not a premise: exact annihilation of I4 removes it from this argument.

## Domains, equivariant choice independence, and bilinear target

The domain of G_Q is Z=im Q, not all N4. Differences of equivariant sections land in ker Q=A⊕I2. Since Z contains no A, they actually land in I2, and hT_a annihilates that subspace. Equivariance is essential to this argument; independence from arbitrary nonequivariant sections is neither proved nor claimed.

On I4, the section equals the canonical s because Hom_G(P,A⊕D)=0. Its image is in im h, so the sandwich identity gives Pi_a(I4)=0. The computation of QPi uses only the actual radical intertwining identity j4T_a=T_a j2 and hQ=j2. All factors have their stated domains, and h(Z) lies in I2, giving QPi_a=L_a h.

The image T_b s is contained in Z∩ker h, so Pi_a T_b s is defined. It lies in im h by construction and is killed by Q by the preceding identity. Therefore it lands in im h∩ker Q=I2. This target conclusion cannot be obtained merely from Q-closedness alone, since ker Q also contains A.

For an arbitrary y, the actual difference h(y)−s j4(y) lies in I2. Applying T_b places it in I4, which Pi_a kills. This proves Pi_a T_b h=B(a,b)j4 without interchanging a and b or imposing mixed commutation.

## Exact diagonal and sign

In PR1025's conventions, the class of s is the inverse connecting representative of the source P because Qs=Id on I4. The first correction x1=−G_Q T_a s is literal: its Q-image is −T_a s, not just that vector modulo I4.

PR1022 supplies raw quotient-second vanishing on this P, not merely vanishing after quotienting by the A second-symbol image. Thus T_a x1 lies in Z+I4=Z. The second correction x2=−G_Q T_a x1 is consequently defined and satisfies its exact correction equation. PR1025's descended f0 is induced by j2, so

`R_a=j2 x2=hQx2=−hT_a x1=+hT_aG_QT_as`.

The two correction minus signs yield the stated plus sign and preserve operator order. The correction operators are equivariant homogeneous polynomials. PR1025's unique equivariant quadratic lift therefore identifies this R exactly, not only modulo an A correction or the kernel syzygy. Its source P is the same connecting identification used in defining B.

The symmetric and alternating channel dimensions are respectively two and one. Polarization recovers the symmetric part from the diagonal; it supplies no alternating vanishing. Neither a free actual alternating parameter nor nonzero mixed defect is asserted.

## Endpoint-nine constraint and fixed-basis identification

PR1059 supplies two indispensable actual facts: F4=NC4 with h(NC4)=0 in endpoint nine, and the quadratic descendant map A⊗P_h→NC4/I4 is nonzero and surjective onto its D quotient. The latter is proved there through a specific actual A-channel map, not inferred from its one-dimensional Hom space.

Since NC4 lies in ker h⊂Z, Pi restricts to it. Since Pi kills I4, this restriction factors through D_C=NC4/I4 and lands in I2. The space Hom_G(A⊗D,D) has dimension one, with nonzero representative rho_D. The nonzero descendant channel has the one-dimensional type Hom_G(A⊗P,D), with nonzero representative L*. Invariant apolar forms define the complex bilinear adjoint used in the pinned basis; no Hermitian conjugation is involved.

Consequently the full bilinear family factors in the actual order

`B(a,b)=lambda nu rho_D(a)L_b*`, with nu nonzero.

The intermediate D_C identification rescales the two factors inversely. It cannot exchange their order or replace the result with `L_a* rho_P(a)`. Hence the diagonal is precisely gamma times the pinned R1, not an unspecified line in the two-dimensional pencil. Independence of R1 and R2 makes the second coefficient genuinely zero. The nonzero R1 line is the conic line identified in PR1036. Lambda, and therefore gamma, may vanish; the proof neither rules out the zero lift nor selects the endpoint-nine branch.

Any P graph component of the descendant relations maps into I4 and is annihilated exactly. Its value is irrelevant. The converse coefficient implication uses only the established 9/16 dichotomy and does not assert an actual nonzero coefficient.

## Executed verification and scope

Both `python verify.py` and `python -O verify.py` passed all 38 checks with byte-identical output. Independently executed checks derived the relevant channel multiplicities by the binary-icosahedral McKay recurrence rather than the production A5 character table, checked correction word order in noncommuting symbols, and verified full coefficientwise polarization with arbitrary bilinear coefficients. The production universal polynomial checks also confirm the adjoint convention, bilinear diagonal order, and independence of the pinned R1 and R2.

The actual-map and raw-cohomology premises were reviewed in the authenticated proofs; symbolic checks do not replace those premises. No actual HM coefficient, direction, point, jet, or source-instance rank was evaluated. No Q-preservation of NC or NR, graded homotopy extension, mixed commutation, source occurrence, or new branch exclusion is inferred.
