# Independent whole-proof review

Verdict: PASS for the stated actual negative-kernel-bundle construction and its stated limits. The proof establishes a canonical saturated primary image and canonical quotient, existence of equivariant bundle splittings, and a two-dimensional affine space of such splittings. It does not establish a distinguished complement, horizontal splitting, or splitting of the full graded module.

Review date: 2026-10-23 UTC.

## Frozen scope and reproducibility

This review is bound to these SHA256 values:

- PROOF.md: `7f45763ca0ec815b12e8934478e4105e4a3f837c68dca39e31f922166fcb1add`
- verify.py: `f422bea3797cf08069051fbbdd41a92a95e9032786692ac2b059cafd1a4ad5e1`
- RESULT.json: `111c6e61fbb3f1968cffe5b8368815f14ee857cb31d2c4c324ac400df4e2c4a3`
- INPUTS.json: `80e4ae0dcd2c078bdf8de58878a444e42f10570a683310e36cde9e63c42f84f1`
- REPRODUCE.md: `ce417187022d562ec4033878c9d3f8d22d15928afad09002a507ab9a94cf845f`

I independently executed `python verify.py` and `python -O verify.py`. Both terminated successfully, returned 70 checks with status PASS, and produced bytes identical to RESULT.json. I read the checker as well as running it. It performs bounded exact character and bundle-arithmetic checks using the standard library; it neither computes selected actual HM data nor certifies the geometric argument by itself. In particular, its finitely many line-bundle Ext checks are controls, not a substitute for the general Serre-duality proof.

## Independent public authentication

I independently fetched both complete originals from their exact immutable commits using GitHub's file-content API. The repository API identified Akilleez-QA/read-em-and-weep as public. Separate PR metadata reads identified the following pinned SHAs as the respective PR heads at review time. Each fetched UTF-8 content was compared byte for byte with the included input, and its SHA256 and Git blob object ID were independently recalculated. All comparisons passed. Only public provenance is recorded here.

1. PR1122: https://github.com/Akilleez-QA/read-em-and-weep/pull/1122
   - Commit: `65c13bb9a3748a19eb8466f748bd29a5a849ecb5`
   - Original: https://github.com/Akilleez-QA/read-em-and-weep/blob/65c13bb9a3748a19eb8466f748bd29a5a849ecb5/research/hm/primary-terminal-source2-exclusion/PROOF.md
   - Included file: `inputs/PR1122.md`
   - Bytes: 8009
   - Git blob: `7721fe5915ddfd5638a4e9cf2d5dde39a1910e26`
   - SHA256: `7be070050a035ceec64c5698fd1ae70857225a405e1a43d4cbebc4019f5a342a`
2. PR1056: https://github.com/Akilleez-QA/read-em-and-weep/pull/1056
   - Commit: `875e86e2eec36a050e9a626735199681762e43ec`
   - Original: https://github.com/Akilleez-QA/read-em-and-weep/blob/875e86e2eec36a050e9a626735199681762e43ec/research/hm/restriction-socle-kernel/PROOF.md
   - Included file: `inputs/PR1056.md`
   - Bytes: 10582
   - Git blob: `29cadd1739c37309b31192beef30007acf14e8ef`
   - SHA256: `1ee98092e1322841d031d65649dee205299b88d9ba726599f0678d8b1e5b2a1e`

These checks authenticate the precise source documents used. The mathematical review treats their explicitly established actual-module and cohomology statements as inputs; it does not claim to have independently reconstructed every earlier HM dependency cited inside those originals.

## 1. The primary input is unconditional on source2

Section 2 of inputs/PR1122.md constructs the actual primary multiplication curry using physical parity, the injective graded primary-module map, and global levelness. Its injectivity and equal source/target dimensions give the actual evaluation pencil with source A4=P tensor (1+A), target A5=P tensor W, and kernel A5 O(-2). Evaluation is onto on every nonzero parameter line. Both coefficient inclusions into M4 and M5 are actual injective module maps.

This part of PR1122 precedes and does not depend on its conditional source2 projector argument. Using this evaluation pencil therefore does not import source2, a pure-V radical, a chosen source occurrence, or an identification by character. The representation equalities A4=V+2P+D and A5=W'+T6 are compatible with the included checker and with A5 tensor W=A4.

## 2. The ambient terminal pencil has the same actual arrow

Inputs/PR1056.md establishes H1(E)=M4 and H1(E(1))=M5 through actual connecting maps. For the original arrow u m_x+v m_y, its cohomology convention sends multiplication by u to m_y and multiplication by v to -m_x.

The diagonal sequence on the product of parameter lines, tensored on the first factor by F(1), gives

    0 -> F(1) -> H1(F) O(-1) -> H1(F(1)) O -> 0

when H0(F)=H0(F(1))=0. Its coefficient arrow from the diagonal equation is v H1(mult_u)-u H1(mult_v). Substitution of PR1056's convention gives v m_y+u m_x, exactly the original parameter combination. H0(E)=0 also follows directly from E's original injection into M3 O(-1).

Consequently the map in the recovered 37-to-20 pencil is the same actual negative multiplication used by the primary 16-to-8 pencil. There is no independent rotation of one pencil, character-only replacement, or generic-parameter argument. The fixed determinant trivialization makes the construction equivariant, with no extra determinant character omitted.

## 3. Saturation uses both coefficient injections

The commutative diagram of the two everywhere exact pencils first gives an injection of the primary kernel into E(1). It is not enough merely to declare this injection saturated.

Here both coefficient injections have constant locally free cokernels. The quotient arrow (M4/A4) O(-1) -> (M5/A5) O is surjective, because the ambient arrow is surjective and sections of the target quotient lift locally. The snake lemma then identifies its kernel with E(1)/(A5 O(-2)). A kernel of a surjective vector-bundle map is locally free. This proves the required saturation and identifies the quotient pencil as an actual diagram quotient, not a model with matching characters.

After twisting, the actual image E_prim is A5 O(-3), of rank 8 and degree -24. The quotient has rank 9 and degree -30; its terminal pencil has source V+2P+2D of dimension 21 and target 2T6 of dimension 12. All rank, degree, and twist computations agree.

Canonicity here is relative to the fixed actual primary submodule and the fixed determinant convention. It is not a claim that the abstract isomorphism type of E alone selects this embedded image.

## 4. Quotient cohomology and actual identifications

The quotient pencil embeds E_bar(1) into 21O(-1), so H0(E_bar(1))=0. This correctly proves that the ordinary splitting degrees of E_bar are at most -2; no invalid inference from negativity of E to negativity of its quotient is made.

Taking cohomology gives H1(E_bar(1))=M5/A5=2T6. Twisting the quotient pencil by -1 gives H1(E_bar)=M4/A4, because O(-1) is acyclic and H1(O(-2)) is the trivial one-dimensional representation in the fixed determinant convention. The same argument applied to the primary pencil gives H1(E_prim)=A4 and H1(E_prim(1))=A5. Naturality of the diagram supplies the actual coefficient inclusions and quotient maps on cohomology. These assertions are stronger than, and are not inferred merely from, matching characters.

## 5. Splitting and exact equivariant ambiguity

For R=A5, the extension group is

    Ext1(E_bar,R O(-3)) = R tensor H1(E_bar* O(-3)).

Serre duality identifies the dual of the latter H1 factor with H0(E_bar(1)), which has just been proved zero. Thus the ordinary extension vanishes. Averaging an ordinary right inverse over the finite group in characteristic zero preserves its right-inverse property and gives an equivariant section, even though G acts nontrivially on the parameter line.

The difference of two equivariant sections lies in Hom_G(E_bar,E_prim). Equivariant Serre duality, again using omega=O(-2) and the fixed determinant trivialization, gives

    Hom_G(E_bar,E_prim)
      = Hom_G(H1(E_bar(1)),R)
      = Hom_G(2T6,W'+T6).

T6 is irreducible and nonisomorphic to W', so this dimension is exactly 2. The checker independently confirms the relevant character inner products. The sections therefore form a nonempty affine space of dimension 2, not a vector space with a specified origin. Distinct sections have distinct image complements, since a section is uniquely determined by its image and the fixed quotient map.

## 6. Claim boundaries

The construction proves a canonical embedded primary direct summand in the sense that its exact sequence splits; it does not choose a splitting projection or complementary subbundle. The proof correctly keeps the following separate:

- The fixed primary image and canonical quotient versus an unchosen complement.
- Equivariant vector-bundle splitting versus compatibility with the original ambient Gauss inclusion or connection.
- Negative terminal-pencil structure versus preservation of positive multiplication, invariant Q, or the full graded adjoint-primary extension.
- Structural consequences for this bundle versus realization or coverage of conditional source alternatives.

No selected actual HM/source coefficient, tensor, matrix, point, parameter, derivative, jet, instance-rank evaluation, or large scan is used in this review or the bounded checker. No public changes were made. No unresolved mathematical gap was found in the stated theorem. This is an independent mathematical audit with reproducible bounded checks, not a proof-assistant certificate.
