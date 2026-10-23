# 132. Canonical primary subbundle and the four remaining formal bundle types

**23 October 2026 · Checkpoint through PR1124.** This chapter reports Mr. Slop's [PR1123](https://github.com/Akilleez-QA/read-em-and-weep/blob/504b7eb800407dfc7e6340c98c72cdd553939f54/research/hm/primary-terminal-slope-obstruction/PROOF.md) and [PR1124](https://github.com/Akilleez-QA/read-em-and-weep/blob/48396766d4e61a9de2455b1d068ba8abe09e05f3/research/hm/primary-negative-summand/PROOF.md) after full-source reading. The former's actual-map argument has also received independent whole-proof review in this collaboration. These are structural results relative to pinned actual Horrocks–Mumford inputs, not a proof-assistant certificate, a source-instance search or a complete original repair.

## From a source-specific contradiction to a canonical slope constraint

PR1122's 16→8 primary evaluation pencil was obtained before imposing the later source2 hypotheses. PR1123 applies that unconditional primary subpencil to the canonical quotient E→E_{<-3} of the actual rank 17, degree −54 negative kernel bundle. Here E_{≥-3} is its canonical slope-filtration subbundle of degrees −2 and −3; E_{<-3} has degrees at most −4.

Terminal reconstruction is functorial for this quotient and uses the same fixed determinant convention as actual negative multiplication. The induced primary kernel map 8O(-2)→E_{<-3}(1) vanishes by its target's slopes. Keeping both coefficient arrows, the middle map then factors through a constant bundle into an O(-1) bundle and also vanishes. Hence the actual primary terminal subspace lies in

    H1(E_{≥-3}(1)) ⊂ H1(E(1)).

The degree −2 slope piece becomes acyclic after twisting by 1. Thus this subspace is canonically the degree −3 coefficient representation R3, and the actual injection yields

    W′ + T6 ↪ R3.

This assertion does not come from an arbitrary injection 8O(-2)→E(1), nor from equality of characters. It uses both actual coefficient maps and naturality of the reconstructed terminal pencil. It does not require source2, a compatible pure-V radical, R=0 or residual-large.

## Exactly four formal bundle types survive these necessary equations

Intersecting the new inclusion with the pinned complete 28-type representation equations leaves exactly these four formal types:

| Type | Necessary equivariant Birkhoff form of E |
|---|---|
| I | D O(-2) + (W′+T6) O(-3) + V O(-4) + O(-8) |
| II | P O(-2) + (W′+T6) O(-3) + V O(-4) + W′ O(-5) |
| III | V O(-2) + (W′+T6) O(-3) + 2V O(-4) |
| IV | (W′+2T6) O(-3) + V O(-4) |

The reduction is exact within that specified formal classification: its equations force a=1 and d=g=h=0, followed by b+c+e+f=3 with b,c≥1 and e,f≥0. The four remaining tuples are (1,1,0,1), (1,1,1,0), (1,2,0,0), (2,1,0,0). None of the four types is asserted realized. They are not the historical four source pairs, and counting them is not a completion percentage.

The earlier specified types E10 and E14 have R3=0; E13 has R3=T6. All three are incompatible with the actual inclusion W′+T6↪R3. Accordingly the old four-pair ledger is preserved only as historical provenance, not a list of currently compatible possibilities. Passing from these specified-type exclusions to a global rank-three source exclusion still requires independent verification of the geometric coverage and actual-source transfer bridge. The ledger itself cannot supply that bridge. No empty actual catalogue, HM nonexistence or complete repair is claimed.

## The primary image is a canonical saturated subbundle

PR1124 constructs more than a slope-multiplicity constraint. The actual primary coefficient inclusions A4⊂M4 and A5⊂M5, of dimensions 16 and 8, induce a canonical image

    E_prim = A5 O(-3) ⊂ E,     A5 = W′+T6.

Its degree is −24. Both coefficient inclusions are constant subbundle inclusions. Their quotient arrow is onto, so the snake lemma identifies E/E_prim with the kernel of an onto vector-bundle map, after twisting. This proves saturation, which would not follow from an injection alone. The resulting canonical quotient E_bar has rank 9, degree −30, and the actual everywhere-exact terminal pencil

    0 → E_bar(1) → (V+2P+2D) O(-1) → 2T6 O → 0.

The coefficient dimensions are 21→12. In particular H0(E_bar(1))=0, H1(E_bar)=V+2P+2D and H1(E_bar(1))=2T6. These are natural identifications induced by the original primary inclusions, not a character-matching replacement pencil.

## Canonical subbundle and quotient; noncanonical complement

Serre duality identifies the dual of H1(E_bar* O(-3)) with H0(E_bar(1)), which vanishes. Therefore Ext1(E_bar,E_prim)=0, and the sequence splits as vector bundles. Averaging a section over the finite group gives an equivariant section.

But the differences between equivariant sections form

    Hom_G(E_bar,E_prim) = Hom_G(2T6,W′+T6),

which has dimension 2. Thus equivariant complements form a nonempty affine space of dimension 2. The actual image E_prim and quotient E_bar are canonical; no distinguished complement is selected by this argument. There is no assertion of horizontality for the ambient Gauss inclusion, positive-coordinate or Q preservation, or splitting of the full graded adjoint-primary extension.

This provides a smaller canonical quotient for further work. It does not evaluate an original obstruction, identify an actual source occurrence, establish full-adjoint invertibility or settle algebraicity.

## Dated PDF addendum and scope freeze

The delivered Craig Ward v0.3 PDF remains the fixed **23 October 2026, 19:16 UTC** historical snapshot through PR1117. It has not been replaced. Chapters 131–132 record later changes through PR1124: the complete source2 package exclusion, the canonical degree −3 inclusion and four-type reduction, and the saturated primary image with its 21→12 quotient. Later developments are outside this checkpoint.

Earlier source2 gate continuations remain valid conditional deductions with their written proofs and tests retained; the full actual antecedent used by that branch is now contradictory. They are not active source2 outcomes. Archive 52 is unchanged. The original proof repair remains open.
