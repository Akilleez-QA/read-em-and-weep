# Independent review: actual Q-image transversality

## Verdict and reviewed artifacts

**PASS**, under the retained compatible pure-V actual-source hypotheses. The twelve-dimensional image and its radical-endpoint intersection hold in every remaining branch. Transversality to all of NC4 is proved only under the separately stated residual-large hypothesis. No preservation of NR or NC by Q is used or inferred.

Reviewed SHA256:

- `PROOF.md`: `15b88b01ffd442456a4f672be6ba0d62581de19572f804db0160f3734524f4c8`
- `verify.py`: `3be6463791ee96e442558635b6cb31ff10fca32408307e3314d9dea4a29b9dca`

## Authentication

All five originals were freshly retrieved from their exact repository paths at the immutable commits in `INPUTS.json`. Retrieved bytes equal the retained bytes, and independently computed SHA256 and Git blob hashes match the manifest:

| Input | Commit | Git blob |
|---|---|---|
| PR1019 | `3fb2475ffb275c5789acbaa8f9f84ed272713785` | `bf63c14f76933d59fa7e3ac61aecb3366ac1b442` |
| PR795 | `3f811311d76914a555c7e7d0c5b887b41805aa6c` | `9358ec81c552913fac20f3a92d7b9f7c58105656` |
| PR1059 | `af2f163e4bcc593b6895ace840c139d2d4668cde` | `2b00a40de04a7084ff2f08c767fdd2f4f13ae5f4` |
| PR1061 | `90f33f808c2962cdd4c41d11ac32a10c30b0d353` | `aae98e9c7bfdd084b342d222bbdb2c8b06c53c20` |
| PR1064 | `bfc239e1c8624a0346394e1454b0bea3c976d40d` | `20b3b58b92d4c44d1097d47a9e952c4dfa25b569` |

This authenticates these five proofs, not every historical dependency recursively. The specific conditional input from PR1064 is used only for full NC4 transversality.

## Preimage and actual isotypical intersections

The preimage equality is exact linear algebra on the actual maps. Since Q maps P_h isomorphically onto I4, every x whose Q-image lies in I4 has a unique p in P_h with Qp=Qx. Subtracting p puts x in ker Q. Conversely both ker Q and P_h map into I4. Therefore

`Q⁻¹(I4)=ker Q+im h=A⊕I2⊕P_h`.

This neither extends an inverse of Q beyond I4 nor asserts that any ambient residual summand is Q-stable.

NC2 is an actual equivariant subspace, contains the embedded I2, and has no A constituent. Isotypical projections preserve NC2, so intersecting the displayed preimage removes the A summand and leaves exactly I2 together with `P_h∩NC2`. Because P_h is irreducible, its intersection with NC2 is all or zero. A graph in a larger P multiplicity space creates no mixed cancellation with A or D. This validates the key step at the level of embeddings rather than just characters.

The same reasoning gives `NC2∩ker Q=I2`. Thus Q induces an isomorphism from NC2/I2 onto its actual image U_Q, proving dimension 12 and character V+P+D. The pure-V radical kills NR2, so `hQ(NC2)=j2(NC2)=0`; consequently U_Q lies in ker h. This uses radical orientation, not Q-invariance of NR.

## Endpoint detector

For a linear map, the image intersection identity

`Q(NC2)∩I4 = Q(NC2∩Q⁻¹(I4))`

holds without injectivity or any complement choice. Applying it to the established preimage intersection kills I2 and either retains all of I4 or nothing, according as P_h lies in NC2 or not. PR1059 identifies this condition exactly with generated endpoint dimension nine versus sixteen. Hence the detector covers both kinds of endpoint-sixteen branch.

The quotient map to N4/I4 therefore has image dimension eight in the small branch and twelve in the large branch, with the stated kernel P or zero after quotienting NC2 by I2. These conclusions do not require an assertion about where U_Q lies relative to NR4.

## Stronger residual-large conclusion

Under the explicitly stated residual-large hypothesis, PR1064 gives `ker h∩NC4=I4`. If y lies in U_Q∩NC4, the already proved containment U_Q⊂ker h puts y in I4. The endpoint-sixteen detector then forces y=0. This proves full NC4 transversality by two actual intersection identities, with no hidden projection argument.

The induced map NC2/I2→N4/NC4 is thus injective, and NC4⊕U_Q has dimension 21 and character V+2P+2D. These numerical data match NR4 but do not identify the embedded subspaces. The proof correctly emphasizes that Q(NC2)⊂NR4 has not been established and that the stronger conclusion is not asserted for the nonzero-N0-projection branch.

## Executed verification and scope

Both `python verify.py` and `python -O verify.py` passed all 31 checks with byte-identical output. The verifier's abstract block calculation uses an invertible complementary block over a rational-function field to illustrate the general preimage lemma; it is not an evaluated source matrix. The isotypical and membership checks likewise supplement, rather than replace, the written actual-map proof.

The review independently derives the preimage equality by section subtraction, the image intersection through its exact preimage, and the residual-large implication above. The literal identities hQ=j2 and Q(P_h)=I4 are used with their original domains and codomains. No actual coefficients, parameters, directions, points, or source-instance ranks were evaluated. No branch is selected, and no new Bockstein vanishing, residual splitting, or source exclusion follows.
