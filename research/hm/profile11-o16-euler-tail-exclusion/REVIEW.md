# Independent exact-version audit

## Verdict and exact object

PASS for the mathematical conclusions in `PROOF.md`, SHA256

    1f2c7ffb18c9a4e74b1f398c0edc5da87f08a6cd3d94acb0eea53b3836501218

The accompanying `verify.py`, SHA256

    1d056abb88f1b1982447b051003503225285bfe74815a65866369384009c2a54

was independently inspected and run successfully. The final proof edit explicitly requires D0+L to be a direct summand in the scalar-line lemma; both applications satisfy that hypothesis by construction.

The proof excludes exactly the two stated source edges at source_index127 / G3.11.cce6e3ba4eeb. Both the scalar-nonzero and Euler-only branches of the g-f edge are covered. The h-f-f edge is covered independently of the g-f argument. No substantive mathematical gap was found in this exact version.

This review is an independent written audit, not proof-assistant certification. Its result is conditional on the pinned actual-bundle and strict-top inputs and the cited published lemmas, whose needed interfaces were checked. It does not claim actual HM realization, exclude a whole stable label, or complete source2 or the global rank goal.

## Inputs checked

The complete original catalog entry127 has A_q=O(-8)+O(2)+O(16), B_q=O(-18)+O(-4)+O(6), original defect zero, and the thirteen tuples reproduced in the proof. The original frontier maps that entry to G3.11.cce6e3ba4eeb. Applying the original source decoder gives exactly the two displayed source bundles, each rank17 and degree-54.

All seven dependency files in `audit-inputs/manifest.json` were read as needed. Their Git blob hashes were recomputed from their bytes using the standard Git blob header and matched all seven manifest values. The inputs used for the mathematics are:

- Original actual splitting, strict-top, pair catalog, and frontier at db51525015bb7c5e825833d550d08dedf6f6ea96.
- PR796, d2b43060c83328dd5118aee6b9288fcfa0c873ac, Section3: saturation of the actual full derivative image from saturated internal and external images.
- PR802, e484640a6565c278321bf6557860262c1ac1b7df, Sections3 and5: the complete P+D line-system kernel list and the three-channel polar contradiction. Sections6-7 also corroborate the exact constant-projection mechanism, which is re-established in the reviewed proof.
- PR828, ae077cbe42d65cde27d65ce88923dc35851b6952, Section1: no divisor defect for a coherent lattice preserved by the trivial connection.

The review does not depend on an unpublished source113 exclusion or on a whole-label conclusion from PR802.

## Actual-sheaf and high-line checks

Strict-top gives an injection on the top coefficient representation. The D-isotypic source and target multiplicity spaces both have dimension two, so their map is an isomorphism. Its low-row kernel and the P source therefore give the actual saturated F=(P+D)O(-2). Its nine independent degree18 sections are basepoint-free by the invariant-divisor bound twelve. This identifies the saturated external O(16) image, not just a generic line.

For each of the three exact P+D kernels, the internal components to D O(-4) vanish by the listed representation identities. The only remaining channel is the constant row from O(-10) to the O(-10) target summands. A nonzero such row is saturated. The PR802 polar argument has precisely the same actual F, constant A, and three projected linear channels here; it does not require the O(-10) internal image to occupy a particular lower source summand. It therefore excludes that case.

When the internal image is zero, the resulting F^+ is an actual constant ten-space, and its quotient by F maps isomorphically to the saturated O(18) summand of E^+/E. Thus E+C0 O is saturated, E intersect C0 O=F, and the projected Z is a saturated actual subbundle. Constant projection removes exactly that positive quotient, leaving the actual saturated raw Gauss quotient O(2)+O(-8). No connection on an abstract complement is introduced.

## The actual M, C1, and quotient character

The D0 map is the nonzero complete quartic system, with exact kernel S O(-3). Its internal target degrees are at most -10, so its internal image is zero. The actual-image lemma gives

    0 -> D O(-2) -> M -> O(4) -> 0.

First-polar generation and saturation force M to have only degrees zero and minus one. Its rank6 and degree-6 force M=T O(-1); twisting the exact sequence identifies the coefficient as T.

The derivative of M kills D0. It has rank at most one, and is nonzero because a negative subbundle cannot be horizontal. A pure-linear embedded bundle reaches its full constant coefficient span in one forward step. Consequently that actual constant span has dimension7. Since M is saturated, C1 O/M is an honest line bundle of degree6.

There is no hidden one-dimensional character: G is perfect, as explicitly recorded in the original actual-splitting input, Section2. Therefore this equivariant line is the standard O(6). Moreover H0(M)=H1(M)=0, so the quotient sequence identifies C1=H0(O(6))=Sym6 W=V+P equivariantly.

## Bounded invariant checks

The standard Clebsch recurrence

    Sym(n+1) W = W tensor Sym(n) W - Sym(n-1) W

together with the PR802 Section3 identities and T tensor W=V+P+D from its Section5 gives the following short chain:

    Sym6  W = V+P
    Sym7  W = Wp+T
    Sym8  W = P+D
    Sym9  W = S+T
    Sym10 W = A+V+D
    Sym11 W = W+S+T
    Sym12 W = 1+A+P+D
    Sym13 W = W+Wp+S+T
    Sym14 W = A+V+P+D.

Thus (Sym10 W)^G=(Sym14 W)^G=0. Also Sym2 W=A has no invariant. These are fixed abstract representation identities, not selected actual-instance calculations. They justify the two scalar-line Hom vanishings and the auxiliary O(-10)->O(-8) vanishing without an invariant-ring computation.

## Scalar-line obstruction

The premise beta_Z(L)=0 puts the actual derivative of L in Z tensor Omega^1. Modulo L, ordinary degree vanishing confines it to D0 tensor Omega^1. Projection by the actual constant C1 therefore makes the image sheaf N of L preserved by differentiation.

This conclusion applies to the image sheaf before saturation: every local section has a local lift, differentiation commutes with constant projection, and D0 is killed. If the image is nonzero, a nonzero morphism from the line L to a torsion-free sheaf is injective, so N is isomorphic to O(-8), including at zeros of the projection. Its saturation is a constant line because its generic line is horizontal. The local t^m lattice argument forces m=0. This contradicts degree-8. Hence L lies in C1 O as an actual sheaf.

The equivariant composite L->C1 O/M is zero by the verified Sym14 invariant vanishing, so L lies in M. The sum D0+L is a saturated rank6 subbundle of the ambient bundle in both applications: L is chosen in an O(-8) multiplicity summand complementary to D0. More generally, in the two displayed Z types, an independent O(-8) direct summand has no map to the strictly lower O(-9)/O(-10) blocks and projects by a nonzero constant row into the O(-8) multiplicity space, so the sum is again a direct summand.

Consequently M/(D0+L), a torsion sheaf of rank zero, embeds in the locally free ambient quotient by D0+L and vanishes. Equality would identify degrees -6 and -18, which is impossible. Saturation, rather than generic rank equality alone, is used at exactly the required step.

## Exhaustion of the two source edges

For h-f-f, the kernel of the constant row 2O(-8)->O(-8) contains an actual O(-8) summand L. This remains true even if the row is zero; in fact surjectivity and the auxiliary invariant vanishing exclude a zero row. The positive component of L is zero by Sym10, and its internal target outside D0 has degrees -10 and -12. The scalar-line lemma therefore excludes this entire edge.

For g-f with zero scalar component, L=O(-8) has zero negative component by hypothesis and zero positive component by Sym10. Its only possible internal component modulo L goes to D O(-4), because Hom(O(-8),W O(-11))=0. The scalar-line lemma excludes this branch. The Euler-kernel O(-10) is not used and its possible internal derivative is not assumed zero.

For g-f with nonzero scalar component, the endpoint kernel is an actual graph Z'=D O(-2)+W O(-9), of rank7 and degree-28. Its full Gauss kernel is an extension of W O(-9) by S O(-3). H1(O(6))=0 and equivariant averaging split that extension, so Hom(K,O(-10))=0. The actual-image lemma gives the saturated G0=Z'+M with rank8 and degree-24.

The coherent sum S0=Z'+C1 O is preserved and therefore equals its constant saturation. Its rank is eight or nine. Rank eight contradicts the saturated negative-degree G0. In rank nine, S0/G0 is an honest line bundle of degree24 because G0 is saturated. The sum identity gives an onto O(6)->O(24), impossible for line bundles. This covers the complementary branch without modifying any Euler-only hypothesis.

## Computational and scope boundary

This audit read fixed inputs, recomputed file hashes, checked bounded abstract representation identities, and verified exact rank/degree arithmetic. It selected or evaluated no actual HM/source coefficients, parameters, points, derivatives, matrices, or source-instance ranks, and performed no large computation.

The accompanying verifier was inspected before execution. It uses exact fixed characters of the binary icosahedral group in Q(sqrt(5)), the standard symmetric-power recurrence, finite Hom checks for the three stated kernels and their two targets, and reads of the fixed catalog and manifest. It performs no actual-source evaluation, parameter search, network operation, installation, or unbounded scan. Running `python verify.py` completed successfully with these outputs:

    PASS: seven immutable blobs; complete original source127 list; both exact two-D sources.
    PASS: three high-line kernels, every internal Hom channel, first-polar characters, invariant-free degrees10/14, scalar-line and scalar-branch arithmetic.
    Only fixed abstract characters and original catalog data were checked. Connection, saturation, and coherent-lattice proofs remain written mathematics.

The verifier does not independently establish the completeness of the published kernel classification, the geometry of the actual connection, or the saturation and coherent-lattice lemmas. Those are the written mathematical inputs and arguments audited above. `REPRODUCE.md` was also checked for consistency with the files, command, pinned input set, and these limitations.
