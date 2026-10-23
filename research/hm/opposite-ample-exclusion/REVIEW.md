# Independent final whole-package review

Verdict: PASS. No mathematical correction or publication blocker found.

This review covers the final nine-row refinement, not merely the earlier eleven-row draft. It is mathematical review with bounded exact arithmetic, not formal proof-assistant certification.

## Final reviewed bytes

SHA256:

- PROOF.md: f48000f35baca29dc049cefb628c58902739b5e5a69d71e858817c33f94425f8
- verify.py: 3cfc111211be50a8d7172c126f454fee8accd268ff37117f42c5ec0b6ec32eba
- INPUTS.json: 076819b998a9cac0c53c2b77652da49ce7cabb11748ee118f342733c11f104ca
- REPRODUCE.md: 07a7b97ede4f96ba16c8e40e56f2737c697a2631dc2f141183e2f943097ea67e

The reviewer independently fetched all six originals from GitHub at the exact commits and paths in INPUTS.json, compared their decoded bytes with the local verification copies, and recomputed their Git blob identities. Every comparison was equal. Their SHA256 values are:

- TWIST: baabea589839f5b8ceba93f9e458b794fb66690384540cbd7746f621a723fa19
- PENCIL: 69e72653c1b7fe6925743c877210f0ee5714b284d9e1d370afd8bff279e4c1d8
- FREE: 873d031bb3e936438875225b7d8e5ea31ef94e0b063489341d02a3d379f19f2c
- TYPES: 2bf246913d0eb0456b7939b73ccc09d83baac4d39b5b9841e151afab221803d8
- PLANE: 03f7909a73ebe2cd2ff7c8639f3bea3384741058297156f51f38b2b6094354e6
- MONAD: 5b0dff3dd55c0d9ca9bb26c2b3cbadc3456e6a829ef96aa4e36b7c97639f283c

## Mathematical review

1. The plane Koszul and restriction sequences give surjectivity of the complete two-coefficient negative multiplication map. Exactness of inversion eigenspaces selects precisely W tensor H1(B(2))_- onto H1(B(3))_+. This is not surjectivity of a selected hyperplane map.
2. Dualizing the original pencil identifies H0(C*) with the annihilator of that same coefficient map. The determinant pairing only changes the two-dimensional coefficient convention by an invertible identification. The proof uses the actual original cokernel and its canonical identification with the reduced C, rather than replacing maps by their characters. Since C is already a globally generated vector bundle, H0(C*)=0 proves ampleness.
3. For M=p*B tensor O(3E), the exceptional layers are B_R(2) and W tensor B_R(3). The actual extension need not split. Their H1 vanishings imply H1(R1p_*M)=0. The two-row p-Leray sequence correctly retains the possibly nonzero transgression and identifies H2(X,M) with its cokernel in H2(B).
4. The dimension-one base supplies an injection H1(R1pi_*M) into H2(X,M), independently of higher-direct-image vanishings. C(-3) is a summand of the full R1pi_*M. The proof correctly accounts for the odd twist's parity change and does not incorrectly identify it with an unchanged positive eigenspace. Serre duality has the stated twist C*(1).
5. TWIST's dimension bound concerns the entire H2(B). Its functorial symmetric-square monad makes this space a quotient of the exterior-square right-target coefficient tensored with the coordinate representation. MONAD fixes that same actual interface in the current labels, N=A+W' and Hcoord=V+W. Independently recomputing exterior characters via the nine-class squaring map gives Lambda2 N=1+A+T6 and target 3W+2V+2P+2S+2D+2T6. The absence of both 1 and W', together with dimension at most two and semisimplicity, forces H2(B)=0 or W. Quotient, subrepresentation and equivariant duality arguments then prove H0(C*(1))=0 or W. No old-label identification is silently imported.
6. Independently parsing the original twenty-one-row table reproduces the constant-degree and degree-one exclusions. Applying the representation refinement leaves exactly rows 7,9,10,12,14,15,17,18,20. Only row9 has invariant Ext dimension one, through its unique O(12) summand. PLANE's actual identification ker sigma=H0(C(-12))^G therefore proves rank sigma=1 if and only if C has row9; all other survivors give rank two. The stated split and nonsplit vertex middle bundles follow from the already authenticated Euler extension.

## Verification and limits

The reviewer inspected the complete standard-library verifier and independently ran both `python verify.py` and `python -O verify.py`. Both passed with identical output, the exact nine surviving labels and unique row9 conclusion. Runtime checks use explicit failures rather than optimization-removable assertions. The reproduction instructions correctly reconstruct all six omitted originals from immutable Git commits before verification.

No actual HM/source coefficient, selected point, parameter, jet, derivative, matrix or instance rank was evaluated. The arithmetic consists of fixed nine-class characters and the twenty-one previously authenticated abstract rows; it is not a new geometric scan. The prior completeness and geometric premises are imported from the stated immutable originals rather than reconstructed through every earlier dependency.

This result excludes twelve previously allowed abstract types for the actual C. It does not claim any surviving abstract type is realized by HM, choose the actual remaining row, evaluate sigma or delta, decide the row9 extension scalar, change the source/frontier ledger, or establish algebraicity. Those boundaries are accurately retained.
