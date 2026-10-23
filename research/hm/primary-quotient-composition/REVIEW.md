# Independent review: canonical primary doublet retraction

Status: PASS for the exact frozen packet below, conditional on its explicitly pinned mathematical inputs. This is independent mathematical review, not proof-assistant certification.

## Mathematical findings

The actual canonical primary inclusion H=(W'+T6)O(-3) in E and quotient Q of PR1124 imply a stronger partial splitting than an arbitrary choice of its rank-eight complement. Let H'=W'O(-3), using the canonical W' isotypic projection of H. Serre duality gives Hom_G(Q,H')=Hom_G(H1(Q(1)),W')=Hom_G(2T6,W')=0. It also gives Ext1(Q,H')=W' tensor H1(Q*O(-3))=0 because the dual cohomology is H0(Q(1))=0. Taking invariants is exact in characteristic zero. Restriction Hom_G(E,H')->Hom_G(H,H') is consequently an isomorphism. The marked projection therefore has a unique extension p, and p restricted to H' is the identity. The resulting idempotent has actual image H' and canonical kernel E^0 of rank15 degree-48.

This does not require a choice among the four formal bundle types. The exact residual extension is 0->T6O(-3)->E^0->Q->0, whose equivariant section ambiguity remains two-dimensional. It does not select a complement of the entire H.

Every equivariant endomorphism preserves E^0: Hom_G(E^0,H')=0, by first restricting to T6O(-3) and then descending to Q. The complementary image H' need not be preserved. The idempotent is not automatically central.

Natural cohomology of the actual idempotent splits both actual negative terminal coefficient spaces and commutes with their parameter action. H1(H')=W' tensor W=P and H1(H'(1))=W'. This gives the actual4->2 subpencil and complementary33->18 pencil with source2V+3P+3D and target3T6. It is not a full graded module, positive-coordinate, Q, or Gauss-compatible splitting.

For the four conditional Q types, the sheaf Hom formula is Hom_G(R O(-j),S O(-k))=Hom_G(R,S tensor Sym^(j-k)W) for j>=k, and zero otherwise. It gives Hom(H,Q) dimensions(1,2,1,1), Hom(Q,H) dimensions(2,2,2,2), Hom(H',Q) dimensions(0,1,0,0), and Hom(Q,H')=0 in every case. In types1--3 the forward maps land in degree-2 summands and reverse maps annihilate those summands, so every H->Q->H composite vanishes. In type4 the two T6 degree-3 factors admit nonzero scalar feedback. This distinction must be retained.

Full complement-change conjugation is a'=a-vc, b'=av+b-vcv-vd, c'=c, d'=d+cv. Thus a is independent of the complement in types1--3 without implying c=0 or preservation of H. The independent synthetic checker confirms the full formula and the canonical-kernel/noncentrality distinction; these numerical tests do not replace the sheaf Hom arguments.

## Source inspection and scope

Read PR1124 in full at48396766d4e61a9de2455b1d068ba8abe09e05f3, PR1123 in full at504b7eb800407dfc7e6340c98c72cdd553939f54, and full source proofs PR1122 at65c13bb9a3748a19eb8466f748bd29a5a849ecb5 and PR1056 at875e86e2eec36a050e9a626735199681762e43ec. In particular the actual primary inclusions, coefficient naturality, fixed determinant rotation, and source-ledger independence were checked, not inferred from dimensions. This review is conditional on those pinned actual inputs and is not a recursive formal proof-assistant verification of their complete dependency graph.

No actual HM/source coefficient, selected point, matrix, jet, derivative, instance rank or prohibited experiment was evaluated. No complete proof repair or global source coverage follows.

## Exact nonzero compositions and radical classification

Reviewed the complete frozen proof, including the claims that require more than character dimensions. In type1 the two unique relevant channels are restrictions of first polarizations, and their composite is second polarization on V contained in Sym6 W. Second polarization is injective in characteristic zero, so this restriction is nonzero. In type2 the short composition is the P projection of (xq-yp)(p partial_x+q partial_y) on V contained in Sym6 W=V+P. Its three formal coefficients are sl2 generators. Identical vanishing would make the proper nonzero subspace V invariant under sl2, contradicting irreducibility of Sym6 W. Both arguments retain all formal parameter coefficients; neither selects an actual HM parameter. The long channels vanish by their zero Hom spaces. Thus the opposite-composition ideals have dimensions1,1,0 as asserted.

For the radical calculation, write j as a sum of composites c b. The relation b c=0 gives b j=j c=j j'=0. Products of two kernel blocks therefore have only the lower-right c b term, and every such term occurs. Hence the square equals I and the cube vanishes; for type3 the square is zero. The displayed quotient algebras are semisimple, so these ideals are exactly the Jacobson radicals. Type4 must and does use its separate same-slope Mat2 block; its two-dimensional downward-degree arrow radical is square-zero.

## Source-pencil naturality, checked without independent rotations

The6->4->2 refinement also passes. Twisting the original exact pencil by-1 identifies M3 with H1(E(-1)). A direct uniqueness check removes any potential ambiguity in transporting the projection: for an onto pencil 0->F->A O(-1)->B O->0, a map F->F extends uniquely to the middle term because Hom(B O,A O(-1)) and Ext1(B O,A O(-1)) both vanish. The extension descends uniquely to the right term. Thus e on E gives commuting coefficient projectors on the original pencil. Cohomology identifies them with H1(e(-1)) and H1(e). Applying the same argument to the terminal pencil with kernel E(1) gives H1(e) and H1(e(1)); the middle projector is the same. The canonical actual direct summand is consequently6->4->2 and its complement48->33->18, not just an equality of characters. No assertion about M2 or positive variables is needed.

## Hash-bound reproduction record

The following SHA256 values bind this review to the publication packet's relative paths:

- PROOF.md:3101157347802226a3b2638e76375854944d7a41d503b75b1591bc3eb66b1577
- verify.py:9c6308ca2e00c6f6d8fd29568838dc49b15085ad8db3894aaa13422e8778b652
- RESULT.json:e8c7a2950978f4c4dcaa68b5ee90da5132de20a4931c7f3f26b13d0ff05b3ae0
- INPUTS.json:f9b22e20a1ef73e50d309225f6f3cad43f394ca57470f520015a7862f605c0aa

Both python verify.py and python -O verify.py passed185 checks and reproduced RESULT.json byte-for-byte. Fresh immutable connector reads independently confirmed the1123,1124 and1056 source Git blobs43cc2fe6ac82d7cb01b8c32dc2ef906212c3b705,e92d95b31d70fb54cf53200bde3dc5a14e73000c,29cadd1739c37309b31192beef30007acf14e8ef respectively. Copied trailing-newline discrepancies in an earlier1123/1124 draft were corrected before this freeze; all current pin checks pass.

The separately included, relocatable check_block_conjugation.py passes3855 synthetic scalar block identities in both normal and optimized modes, reproducing REVIEW-RESULT.json. Its SHA256 is8e325066573b361566d7cbca92e6368cf3a44abe821a507d649ce80e0bcefc93; REVIEW-RESULT.json SHA256 is8e7da2e79a85d2c0b6a9e1d1a916770c94480791aa972ffc22ef02497820e4c1. These independent controls test conjugation and the distinction between invariant kernel and central idempotent, not the geometric inputs or noncommutative proof by themselves.

No correction or blocker remains for this frozen packet. The original proof repair, actual type selection, and external geometric coverage remain open.
