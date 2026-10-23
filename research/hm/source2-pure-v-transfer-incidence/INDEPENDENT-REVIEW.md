# Independent review: small-branch transfer incidence

## Verdict and reviewed artifacts

**PASS**, under the stated compatible pure-V hypotheses and endpoint-nine assumption. The remaining transfer scalar vanishes exactly when NC4 lies in Q(NC2); otherwise their intersection is precisely I4. This is an actual incidence criterion, not a selection of either alternative or an assertion that Q preserves the residual module.

Reviewed SHA256:

- `PROOF.md`: `ba59ef2b41b4430f5234700440972f508ffa6639af86272b32ab7f5b15a9b440`
- `verify.py`: `8e69b620b25d44201b66e1784ff6ed2cc91591358cdd4177e89dfbe8d3f3c0ef`

## Authentication

All four originals were freshly retrieved from their exact repository paths and immutable commits in `INPUTS.json`. Retrieved bytes equal the retained files, and independently computed SHA256 and Git blob hashes match the manifest:

| Input | Commit | Git blob |
|---|---|---|
| PR795 | `3f811311d76914a555c7e7d0c5b887b41805aa6c` | `9358ec81c552913fac20f3a92d7b9f7c58105656` |
| PR1064 | `bfc239e1c8624a0346394e1454b0bea3c976d40d` | `20b3b58b92d4c44d1097d47a9e952c4dfa25b569` |
| PR1065 | `fd75633464cd587856287cc7866520fb4105ef5b` | `41f7dada9c1606c4a2a47b330b676b1f090ec1b4` |
| PR1069 | `41bc20cade3198306c492c0c46399d71eb0d51c4` | `827cd956e2eb574fd7d40d408e0450c8581fd7d2` |

Authentication covers these retained proofs, not every historical dependency recursively.

## Section domain, separated D, and choice independence

D_C is explicitly the unique actual D subspace of NC4, not merely the quotient NC4/I4. In endpoint nine, NC4 lies in ker h and hence in im Q, so an equivariant Q section is defined on D_C. For k=G_Q|D_C, the identity hQ=j2 gives j2k=0.

The genuine separated projector sends k(D_C) into the unique D of N0,2=P+D. The radical kills NR2 and has full image I2 of dimension five. Its P restriction is zero by equivariance, so its restriction to that unique separated D is nonzero and therefore an isomorphism. It follows that the separated component of k is zero. This proves k(D_C)⊂NR2 using actual radical orientation and image, not a character-compatible placement or Q-preservation hypothesis.

Differences of equivariant Q sections land in ker Q=A+I2; the domain im Q has no A, so their image lies in I2⊂NC2. Thus π2k is independent of the section. Multiplicity one of D in N8,2 then makes this projected map either zero or an isomorphism onto its unique D8,2. It does not identify an arbitrary residual D embedding with k.

## Universal normalization and independent checks

The biform `(Xy−Yx)(X f_x+Y f_y)` is a nonzero equivariant inclusion of Sym⁴W into bidegree (2,4). Its coefficient formula is correct. The exact quotient of bidegree (2,6) by the polarization image is the pinned transvectant quotient, and only its second component projects onto D8,4: the first component is Sym⁶W=V+P.

Independent full biform differentiation, keeping all three quadratic and five quartic coefficients formal, confirms

`C2(a e_D(f))=−14 rho_D(a)f`.

A second independent check used coefficient formulas without derivative expansion. For the i-th quartic monomial the three inclusion coefficients are `(4−i), (2i−4), −i` at their respective shifted indices. Combining these with the explicit second-transvectant monomial coefficients verifies all fifteen quadratic/quartic coefficient pairs and gives exactly the same factor −14. These are full coefficient-tensor checks, not directional specializations.

The formula proves nonvanishing of the D projection. It does not make the V+P projection zero, and the proof correctly refrains from asserting that. The actual reconstruction may rescale the source and target identifications by nonzero constants, but cannot erase this nonzero channel.

## Transfer comparison and incidence equivalence

PR1064 supplies the descended map from N8,4 to I2 in endpoint nine: it kills V8+P8 and is an isomorphism on D8,4. Actual quotient naturality consequently gives `Pi_a|D_C=hbar T_a^8 π2k`. The exact nonzero D-to-D calculation shows that this family is zero precisely when π2k is zero. PR1069's nonzero descendant factor then identifies this with gamma=0. Exactness of the residual quotient converts π2k=0 into k(D_C)⊂NC2.

The remaining incidence step is not automatic from characters. If D_C⊂Q(NC2), semisimplicity supplies an equivariant lift D_C→NC2. Its difference from k lands in ker Q. Since Hom_G(D,A)=0, the difference lies in I2, already in NC2. Thus k(D_C)⊂NC2. The reverse implication follows directly from Qk being the actual inclusion. This handles both D copies in NC2 without choosing a complement to I2.

Finally endpoint nine gives I4⊂Q(NC2). The endpoint NC4=I4⊕D_C has multiplicity-free nonisomorphic P and D constituents, so its equivariant intersection with Q(NC2) is either all NC4 or exactly I4. This proves both alternatives of the theorem and rules out a hidden partial D intersection or mixed P/D graph.

## Reproduction and scope

Both `python verify.py` and `python -O verify.py` passed all 29 checks with byte-identical output. The independent full biform and fifteen coefficient-tensor checks also passed. Actual maps, radical orientation, and residual exactness were reviewed in the authenticated proofs, not replaced by universal matrix calculations.

No actual source coefficient, scalar value, direction, point, jet, Q section, or source-instance rank was evaluated. The incidence alternatives remain unselected; no extension to endpoint sixteen, Q-stability of NC or NR, or inference from a nonzero P graph to nonzero gamma is made.
