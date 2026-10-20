# Characteristic/rank provenance audit

20 October 2026. Static source and formal mathematical audit. No new rank computation is asserted.

## Bottom line

1. The small pinned program has sound **conditional certificate semantics**: a successful output with `unitRank == rank` and zero residual certifies characteristic-independent ranks, not merely rational ranks. Its arithmetic guards cover coefficient products and sums in the new elimination routine.
2. The stored JSON is a **summary of a successful computation**, not a stored full pivot/elimination witness. Static reading verifies what success means, but does not independently establish that the claimed run happened or that every reported pivot/residual equals the reconstructed physical matrix. Do not describe this read-only audit as a fresh rank verification.
3. The four P4 twist tables establish trivial/full-sign deck cohomology through the proved pushforward splitting. They do not, without further descent, establish original weight-two/pair Ext1 vanishing. Original pair vanishing has a separate source in the older large-model staircase, or can potentially be proved by a further geometric pushforward identification without new ranks.
4. Over C, identifying L with the classical HM bundle via its monad is legitimate. The F3 perfect-complex theorem explicitly does not identify its reduction with a bundle. These statements are compatible, not contradictory.

## Sources read at immutable commits

Repository: Akilleez-QA/read-em-and-weep.

At f968b53943ba2312f09fbc3e8f9d462e86bcaa34:
- research/hm/d8-small-certificates/p4/Perfect-Complex-D8-F3.md, blob 3a8c3633e83466b29ea2e5739c6b486f856b91b2.
- research/hm/d8-small-certificates/p4/check_hm_p4_all_twists.js, blob 7adc1d6a733636204b1dd613870c168717be6277.
- research/hm/d8-small-certificates/p4/certificate.json, blob 304d031083bb2a19fb9bc012cfd338bbe0129980.

At add03476d9055aa00e1e00778eea6332cf8e01cc:
- research/hm/ext-model.md, blob fad0e87f0e30ec916e18fd47feea584c7d8eaae6.
- research/hm/verify-hm-ext.js, blob fa5231de92b61143e3406111d4af028284db6d55.

The small code reproduces the original maps/ranks/gamma/incoming-edge definitions. The claims refer to these immutable sources.

## Exact lower and upper bounds

For an integer matrix, a complete unit-pivot row reduction uses only row swaps, multiplication of a row by -1, and integer row additions. All are invertible over Z and every field. The pivot rows provide a triangular unit minor in the transformed matrix, so rank is at least the pivot count in every characteristic. Zero residual rows give the matching upper bound. A nonzero arbitrary integer minor alone would not be enough for characteristic independence.

The stored summary reports:

| Twist/map | Matrix shape (rows, columns) | Unit rank = rank | Recorded elimination maximum |
|---|---:|---:|---:|
| 0, first | 1225,354 | 353 | 1 |
| 0, second | 1200,1225 | 848 | 5 |
| 0, third | 350,1200 | 350 | 1 |
| -1, zero source | 245,0 | 0 | 1 |
| -1, first nonzero | 400,245 | 240 | 2 |
| -1, second nonzero | 150,400 | 150 | 1 |
| -2, d5 | 80,10 | 10 | 1 |
| -2, ordinary | 50,80 | 50 | 1 |

Every entry reports tailMaxBits=0. Conditional on the output's provenance, each equality supplies both lower and upper bounds. In the last two cases the dimension bounds also give rank ≤10 and ≤50. The d5 identity-minor rows are recorded as 50,60,51,61,52,62,53,63,54,64; the source checks these rows are singleton rows with coefficient +1 in columns 0,...,9. Neither the full matrix nor those row entries are stored in the JSON, and they were not recalculated here.

The zero-residual logic is stronger than `tailMaxBits=0` alone. `rankExact` converts the remaining rows to BigInt and computes a tail rank rr; `certify` rejects unless `unitRank == rank`, forcing rr=0. The tail routine checks rows below rr are zero. Consequently accepted output implies the original unit-reduction remainder is zero. A nonzero tail consisting of pivots with no row updates could have tailMaxBits=0, but would fail the rank equality, so this is not a loophole.

## Arithmetic and transfer audit

In the small routine each elimination update is `exact(old - exact(m*v))`, and `exact` requires Number.isSafeInteger. Sparse accumulation also checks every sum. Initial polynomial coefficients are signs; other coefficient multiplications in Cech/internal operations are by signs. Therefore the guarded coefficient operations have no hidden large product cancellation problem. The integer-to-BigInt conversion is from guarded safe integers. The reported `max` is a bound on updated entries, not a full trace or a global bound on every Cech coefficient. This distinction does not defeat the guards, but should not be obscured.

The code checks line differential square-zero, ordinary compositions, the signed Cech/internal anticommutation and square-zero on the ten d5 paths, forty contraction identities, final closedness, and d1 d5=0. The monomial contraction is the standard simplex contraction on proper nonempty negative support. The four intermediate negative degrees are acyclic; final constant closed Cech sections can be read on U0. Thus the formal construction of d5 is appropriate. Static reasoning validates the construction, while its concrete pass/fail claims remain imported from the stored run summary.

The twist -3 result is not a separate numerical rank: perfect-complex self-duality and P4 Serre duality identify it with twist -2 in complementary degree. No bundle exactness is used in this inference.

## What the four vectors do and do not prove

Write B=End(L). The asserted hypercohomology vectors in degrees 0,...,4 are
- B: (1,24,2,0,0);
- B(-1): (0,5,10,0,0);
- B(-2): (0,0,20,0,0);
- B(-3): (0,0,20,0,0).

The geometric splitting rho_*O_(P1)^4 = O + 11O(-1) + 11O(-2) + O(-3), followed by projection formula and duality, supplies the trivial/full-sign deck statements. It does **not** identify rho_*O(-2,-2,0,0), the original elliptic pair-character coefficient.

For the pair quotient p:(P1)^4→P2×P2, that coefficient has four summands with offsets (-2,0), (-3,0), (-2,-1), (-3,-1). The local product generator does not justify replacing it by O(-1,-1,0,0). Tensoring the original object by a common line bundle cancels in End and cannot change this deck algebra.

Three pushforwards under multiplication m:P2×P2→P4 can be obtained formally from all-twist Kunneth vanishing, finite flatness, Horrocks splitting, and the Hilbert series:
- m_*O(-2,0) = 6O(-2);
- m_*O(-3,-1) = 6O(-3), by the diagonal twist;
- m_*O(-2,-1) = 3O(-2) + 3O(-3).
These three have H1 after tensoring B equal to zero by the existing vectors.

The exceptional m_*O(-3,0) has nonzero intermediate H2 at twist zero, so it is not a sum of line bundles. A candidate is Ω²_P4, but matching a rank, Hilbert polynomial, or isolated cohomology dimension alone is not a proof of that identification. The small source does not supply this identification.

**Useful refinement:** if m_*O(-3,0) ≅ Ω²_P4 is established geometrically, no additional physical map ranks are needed for the desired H1 vanishing. The Euler coresolution

Ω² → 10O(-2) → 5O(-1) → O

in cochain degrees 0,1,2 gives a hypercohomology spectral sequence after tensoring B. The four tables put every nonzero E1 term in total degree at least two. Therefore H1(B⊗Ω²)=0 regardless of the remaining differential ranks. The missing gate is a rigorous descent identification or another suitable coresolution/vanishing proof, not automatically an extra numerical calculation.

## Independent older provenance for original pair Ext1

The older ext-model records the weight-two staircase:

720×640, rank 450; then 354×190, rank 100 on the previous kernel; then 720×90, rank 90 on the new kernel.

Thus the source claims 640→190→90→0 surviving degree-one dimensions and Ext1=0. This is a distinct computation absent from the small certificate. Its source constructs and verifies kernel bases and checks expected outcomes. The first two reductions require unit pivots and zero residual; the final rank routine can use a BigInt tail. The text identifies the weight-one final map as needing the nonunit tail and gives small bounds for the other integer calculations, but these are imported run claims, not ranks established by this audit. If an independently accepted original certificate is already in scope, original pair Ext1 can be cited to it; do not attribute that conclusion to the small four-twist table alone.

## Characteristic-zero bundle versus F3 perfect complex

The older geometric model is over C. Inserting the Euler coresolution into the classical HM monad and cancelling the constant surjection identifies L with H in degree zero. Pullback is exact here (the maps used are finite flat), and twisting by N does not alter End. This is the legitimate characteristic-zero bundle identification, conditional on the stated classical monad.

The same integer formulas define a perfect complex in F3, but do not prove its sole cohomology is a locally free rank-two sheaf. That needs geometric fiber ranks 5,8,2 everywhere, or another exactness/local-freeness proof. Unit-pivot global hypercohomology ranks, d²=0, and equality of dimensions do not establish those local ranks. The pinned small article explicitly preserves this gate, as well as separate obstruction naturality and choice-independence gates.

## Safe downstream wording

“The pinned small source and stored output certify characteristic-independent P4 hypercohomology for the perfect complex, subject to acceptance of that computation's provenance. This audit validates the certificate logic, not a fresh execution. The C bundle identification comes from the classical HM monad. Original pair Ext1 vanishing requires either its distinct old staircase certificate or a further rigorous pair-descent argument; an Ω² pushforward identification would complete the latter without new map ranks.”

## Addendum: the missing pair-descent gate closes formally

After the initial source audit above, the incidence construction in PROOF.md was independently checked. It resolves the formerly pending Ω² identification without reading/evaluating any physical matrix. Thus the caveat above describes what is absent from the pinned small source, not a remaining mathematical gap after this addendum.

Let V_d=H0(P1,O(d)), P2_q=P(V2), P4_F=P(V4), and define Q on P2_q by

0 → V2⊗Oq(-1) → V4⊗Oq → Q → 0.

The quotient has rank two and determinant Oq(3). The universal quartic supplies a section of Q⊠OF(1). Its vanishing scheme is the multiplication incidence Z ≅ P2_q×P2_r, embedded by (q,r)↦(q,qr); it is a regular codimension-two zero locus. The projection of Z to P4 is m. Twist its Koszul resolution by Oq(-3). The three terms on P2_q×P4 are

Oq(-6)⊠OF(-2) → (Q*⊗Oq(-3))⊠OF(-1) → Oq(-3)⊠OF.

Their only nonzero direct images along P2_q occur in degree two, with dimensions 10,5,1. For the middle term this follows from the dual defining sequence twisted by Oq(-3): 0→Q*(-3)→5Oq(-3)→3Oq(-2)→0. Since m is finite, its higher direct images vanish. Therefore the pushed complex yields

0 → E → 10OF(-2) → 5OF(-1) → OF → 0,

where E=m_*Oq,r(-3,0). The right map is contraction against the universal quartic, i.e. its five coordinates after basis choice; its kernel is Ω1_P4. Twist by two. H0(E(2))=H0(P2×P2,O(-1,2))=0, so the resulting map from a ten-dimensional vector space to H0(Ω1(2)), also ten-dimensional, is injective and hence an isomorphism. Consequently 10O(-2)→Ω1 is the standard evaluation map up to a constant basis change. Its kernel is Ω²_P4 by the Euler exterior sequence. Thus E≅Ω²_P4.

Combined with the three ACM pushforward splittings and the spectral-sequence degree argument above, this proves original pair Ext1=0 from the four imported P4 vectors without importing the old pair staircase ranks and without new physical rank calculations. It is an additional geometric descent theorem, not a claim already present in the small pinned certificate. The imported small-computation provenance qualification and the independent F3 bundle-exactness gate remain unchanged.

### Full original pair dimension, also without map ranks

The same degree argument gives H0(B⊗Ω²)=0 as well as H1=0. Since B is perfectly self-dual and (Ω²)*⊗ω_P4≅Ω², Serre duality gives H3=H4=0 (and rules out degrees outside the usual range). Euler additivity in the displayed coresolution gives

χ(B⊗Ω²)=10χ(B(-2))−5χ(B(-1))+χ(B)=200−25−21=154.

Therefore its cohomology is concentrated in degree two with dimension 154. The other three pushforward summands have degree-two dimensions 120,120,120. Original pair cohomology is consequently (0,0,514,0,0), conditional only on the accepted four P4 vectors and these geometric arguments. This is ordinary pair-character dimension; an additional finer equivariant decomposition must retain induced linearizations. In characteristic zero the HM-bundle interpretation follows from the classical monad; in F3 the conclusion is for the perfect complex unless the separate bundle gate is proved.
