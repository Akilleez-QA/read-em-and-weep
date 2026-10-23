# Independent review of the quotient-third / original-fourth interface

Verdict: PASS for the conditional two-dimensional gate and its stated comparison. This review verifies the theorem; it supplies no additional progress claim and selects no actual gate coefficients.

The entire proof and verifier were read. All six unchanged input proofs were read across this and the immediately preceding independent source2 reviews, including the full PR1000 target-section argument. All six were independently fetched at their immutable commits for this review. Each remote Git blob matched the manifest and the locally recalculated blob. SHA-256 authentication also passed. INDEPENDENT-REMOTE-AUTHENTICATION.json records remote matches.

## Mathematical checks

- Endpoint identifications are explicit and correct. The source P is identified with I1 by the inverse connecting map sigma; the target H1(U) is identified with I1 by the descended radical. Thus B=iota beta2,M=-mu Lm lives in precisely the same target as L, not merely an abstract isomorphic P.
- Fixed equivariant qbar splittings give polynomial x1 and x2 globally. Whole quotient first vanishing and the zero P second channel justify the two correction equations in the raw qbar image. Third correction ambiguity is killed modulo im B. Applying the actual endpoint identity f1 Tbar=L f0 before taking quotients proves global membership in im L, including at the ten exceptional points. No generic inference into a torsion cokernel is used.
- PR966's reduced rank-three points give a locally free rank-one kernel of L, via the local row (u,v) and syzygy (-v,u). Its determinant twist is O(-5), with no equivariant character ambiguity.
- The preimage of im B is the actual direct sum im(m) plus ker(L). The intersection is zero as a sheaf because Lm is sheaf-injective; pointwise rank drops do not invalidate this. Local preimages in im B lift uniquely through the image sheaf of B, establishing exactness, not only matching characters.
- Projecting kappa to E(-1) gives a nonzero invariant O(-5) -> E(-1), hence the unique invariant E(4) section up to scalar. The regular-section quotient has twist det(E(-1)) minus the source twist, namely 1-(-5)=6. Therefore J is genuinely I_Z(6), using PR1000, not merely a sheaf with the same Chern data or support.
- Twisting the resolution by three gives A O(1) plus O(-2) -> D O(2). Vanishing of H1 of line bundles on P2 makes the section sequence exact on the right. Hom_G(P,A tensor A)=0 and multiplicity two in D tensor Sym2(A) prove both exact dimension two and uniqueness of the equivariant quadratic lift. The kappa ambiguity has no section because H0(O(-2))=0.
- For the fourth comparison, qx=Td, qy=-Tx, qz=-Ty give original successive terms d,-x,-y,-z. Quotient corrections are x,y,z. The obstruction signs are therefore opposite: iota beta4,M(d)=-s(Ld). The original target is modulo im B: first and third vanish, while second vanishes on D. No raw original-fourth value is equated with an unquotiented target. The statement expressly excludes any additional specialized A-kernel.
- Generic surjectivity of L and torsion-freeness of J establish the identity-zero equivalence. Torsion-freeness follows either from J=I_Z(6) or its injection into the previously proved torsion-free coker B. This does not evaluate either side.

No full-radical compatibility assumption, source exclusion, coefficient selection, actual parameter/jet evaluation, or actual-instance rank test appears. The old length-34 scheme result is properly treated as an input, not a new result.

## Reproduction and exact reviewed hashes

python verify.py and python -O verify.py both passed all 49 checks with byte-identical JSON. Synthetic symbolic checks supplement the written geometry and do not replace it.

SHA-256:
- PROOF.md: 50ab70de6aa5d7489faf88e61bb30f49e809dee68c0bc9370970b83522c621f0
- verify.py: d164ffffbf43d5fca3cda682ff2beca84dc790570fefb68a4da697a18ee09aaa
- INPUTS.json: 211409134a4c0a784ff961b8433545e8065a3aec943695c1e73faa74ae693fae
- Identical normal/optimized output: d1ef16f331c105451263fb7f48a0985fc61c5bb83483b0b9c430e672bc577673

Input SHA-256:
- PR950: d86b7ebf11aa7684a522f408a641b2a0d74c239d521ef9bf829815ae58551fb4
- Original third: 243e242a15ff2bb678b6c1c3cb33f203bbbed5b8bb0c23d8564e14536d9075cd
- PR966: a62f8f6266601987fbfb2f67690a912a9eb9ccb41b04e1d8915652e545390ac4
- PR1000: 97c734b913f4603a4bb1f34e36d66bc3dfb46929ef48ae5beeb7dce5617ee7a3
- PR1019: 42bf6d6a1934410de15829108a397180bb8493fe49798fb1b7945ce0e252f682
- PR1022: 02ebe069509e1087c5987fed757e9283d83156cd280ae27819afffc406d261e0
