# Independent whole-proof review

Status: approved as a structural mathematical proof, conditional on the four authenticated input theorems. This is not a formal proof-assistant certification.

The complete final versions of PROOF.md, verify.py, INPUTS.json and REPRODUCE.md were read afresh and reviewed together. This review binds these exact SHA256 values:

- PROOF.md: `4a11c91ed6f0508b5905200abbe4e62a168ae14189a2c06fb769a531393f0262`
- verify.py: `0f02f0584d3bd46215f624fdc1a497f643ac832fab55c3c2f0fc78673e26638c`
- INPUTS.json: `5941b05366404983c0b11ec4b3718933f6a2ae6979dcbd522530b13d05114102`
- REPRODUCE.md: `3d4ebf94a6e29f6b42d491ae892418d10b2918be911f6a02d1dfbfbf5b8da75d`

## Authentication and replay

Each original was independently fetched from Akilleez-QA/read-em-and-weep at the exact commit and path in INPUTS.json. The returned GitHub blob identity agreed with the independently recomputed Git blob identity of its local audit copy:

- STEINER: `098af4cb145229e6c450dbe863eda8a01a2cace5`
- QUADRIC: `019c1f31773476f0a4877d88632ce5d46fbd4b9f`
- CHAR: `f248e3d4b73a6eec24073bcabfe1a96b185820a0`
- KERNEL: `c9af11e07dd1c4535d9afee94a3c134607d534a3`

Both `python3 verify.py` and `python3 -O verify.py` passed. The verifier uses explicit failure checks, so optimization does not disable its assertions. Its scope is fixed nine-class representation arithmetic, bounded spectral-sequence indexing, input authentication and numerical degree bookkeeping. It does not purport to establish the geometric exact sequences by computation. The reconstruction instructions in REPRODUCE.md match the verifier's expected audit-copy paths.

## Mathematical findings

1. The three-coordinate Koszul argument is valid. In the stated spectral sequence, E2 at position (-3,1) has no incoming higher differential; its only possible outgoing higher differential with nonnegative second index has target (-1,0), which vanishes under H0(E(k+2))=0. Its negative total-degree abutment vanishes. As an independent elementary check, let K be the image of Lambda2 V tensor E(k+1) in V tensor E(k+2). Exactness of the Koszul complex gives 0 -> Lambda3 V tensor E(k) -> Lambda2 V tensor E(k+1) -> K -> 0. Since K embeds in V tensor E(k+2), H0(K)=0, proving the same H1 injection. No unmentioned higher-cohomology vanishing is needed.

2. The determinant conventions are correct. The first Koszul map is intrinsically the determinant twist of the adjoint multiplication map into V* tensor H1(E(k+1)); det V is trivial for the actual positive representation. The proof keeps V* in the joint-map statement and does not conflate it with the coefficient domain V. Positive coordinates preserve central parity and negative coordinates reverse it. H0(B(4))=0 implies H0(B(3))=0 by injectivity of multiplication on sections of a locally free sheaf over integral P4. Thus both applications k=1,2 are justified.

3. Joint-positive injectivity proves that the actual V tensor U1 multiplication is nonzero. Its domain is irreducible T6, so the full coefficient map is injective. This argument selects a definite actual T6 in the full 44-dimensional negative cohomology, rather than merely asserting that this representation occurs. Uniqueness of the starting W and naturality of multiplication make the image canonical. Nothing identifies it with the separately reduced 26-dimensional source.

4. Commutativity correctly transports the determinant relation. The two composites on V tensor W tensor U1 agree, and their common factorization has quotient V tensor A=P+D and kernel V tensor Lambda2 W. The resulting common mixed image equals V U2=W U2,V. Joint-positive injectivity at k=2 ensures this image is nonzero without selecting a coordinate or evaluating a coefficient. Representation multiplicities alone would only give the three alternatives stated at the end of Section4.

5. Section5 supplies the additional geometric argument needed to exclude those two smaller alternatives. The authenticated KERNEL theorem concerns exactly the original map H1(B(2))_- O(-1) -> H1(B(3))_+ O, of dimensions 44 and 46, and gives its equivariant sheaf kernel A O(-6). It is not the reduced kernel W O(-7), and the proof does not replace one with the other. Its validity does not require any assumption about exceptional-fiber torsion or local freeness of the full cokernel.

6. The universal kernels in both contradictions are correct with the standard binary linearizations. Dualizing complete quintic evaluation and twisting by -1 gives 0 -> O(-6) -> Sym5 W O(-1) -> Sym4 W O -> 0. Thus a D-only selected block would force a nonzero equivariant map O(-6) -> A O(-6), impossible because A has no invariant vector. Dual quadratic evaluation gives 0 -> O(-3) -> A O(-1) -> W O -> 0. Tensoring by W', with W' tensor A=T6 and W' tensor W=P, identifies the unique P channel and its kernel W' O(-3). A P-only block would force a map from that kernel to A O(-6), impossible already nonequivariantly because H0(O(-3))=0. In each case the required map of kernels is injective because the selected source is an actual subbundle of the full source.

7. Both mixed channels are therefore nonzero and select canonical actual P and D target copies. Since these representations are nonisomorphic irreducibles, the quotient-domain map P+D -> H1(B(3))_+ is injective. Its coefficient kernel is exactly V and its image has dimension nine. The complete quadratic evaluation sequence tensored by V has precisely the two required nonzero channels. Their one-dimensional Hom spaces show that the actual selected block differs only by invertible target scalings and source identification. It follows that the selected pencil is injective on every fiber and its quotient is V O(2), not merely a bundle with matching rank and degree.

8. The introduction's exact-kernel conclusion is supported by Section5; it is not being inferred from the preliminary factorization alone. The final scope statement correctly leaves separate embeddings, source pairs, the opposite bundle type and vertex scalars undecided. All canonical claims concern actual images or subspaces; identifications with abstract model representations are only asserted up to the stated scalar choices.

## Scope of this review

No selected actual HM/source coefficient, point, parameter, jet, derivative, matrix, instance rank or scan was evaluated. The fixed representation and universal evaluation arguments are structural, not instance tests. Only read-only external source retrieval was used; no external write or publication was performed. No mathematical correction is required for the reviewed bytes.
