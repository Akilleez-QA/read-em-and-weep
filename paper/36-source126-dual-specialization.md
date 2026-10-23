# Source126 quotient specialization leaves four necessary pairs

**Craig Ward · 23 October 2026 · After PR941**

[The new source126 proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/c14af3d39881197edd781aa06cb1e918ef8fd42a/research/hm/source126-dual-specialization/PROOF.md) removes two of the four source126 catalogue pairs retained at the [six-pair checkpoint](35-six-pair-specialization.md). The resulting necessary relation has **four pairs across three stable labels**, distributed **2 + 1 + 1**. This is a new quotient specialization of the existing actual-template geometry, not overdue ledger propagation and not a complete repair.

## The two remaining source126 quotient types

For E10 of G3.11.8ae96830fd21, the three exhaustive residual templates specialize as follows:

- Types I and II: Q* = O(-28) + O(-6) + W' O(-1) + (P+D) O(-2), catalogue index129.
- Type III: Q* = O(-28) + O(-6) + (W'+T) O(-1) + V O(-4), catalogue index157.

Thus (10,231) and (10,249) are removed. The already retained c-d-f pair (14,148) and source2 pair (13,21) are unaffected. All three stable labels remain; profiles remain 2 / 0 / 1.

## Why Types I and II coincide

The projected degree-eight line factors through W' O(-1) inside P O. The quotient is O(6) + W' O(1), since H1(O(5)) vanishes. The full degree-ten first-polar quotient is B=(P+D) O(2).

Type I separates in constant summands. Type II retains a shared-D graph, giving the correctly oriented exact sequence

    0 → B → Q_R → O(6) + W' O(1) → 0.

Its equivariant extension group vanishes: H1(O(1))=0 for the W' term, and the O(6) term reduces by Serre duality to Hom_G(A,P+D)=0. Hence both templates have the same equivariant quotient bundle. This is not a claim that the graph disappears under a constant shear or horizontal splitting.

## Why Type III selects the other quotient

The proof establishes a universal first-polar lemma: a homogeneous vector polynomial whose coefficients span its target has no homogeneous linear covector annihilating both first derivatives. Euler's identity first forces that covector to annihilate the polynomial; differentiation then forces both constant derivative covectors to vanish. No parameter or point is evaluated.

Applied to the saturated projected first-polar system, the lemma gives H0(Q*(1))=W'+T. The four retained catalogue entries have degree-minus-one characters W', W'+T, 2W', and 2W'+T. Only index157 matches. The full splitting conclusion uses the exhaustive pinned retained catalogue; rank and degree alone do not determine it.

## Exact four-pair composition

The [four-pair composition certificate](https://github.com/Akilleez-QA/read-em-and-weep/blob/3cd8a620e7268cf86fb8cc019d35f04d3cb6b448/research/proof-repair-campaign/four-pair-composition/README.md) applies exactly the source126 removal to the pinned PR940 relation. It verifies **6 = 2 removed + 4 retained**, **4 = 2 + 1 + 1**, unchanged three labels, and preservation of both unrelated pairs. Its 19 integration tests pass in ordinary and optimized modes; the prerequisite 288-check source126 verifier was replayed in both modes. The [exact frontier](https://github.com/Akilleez-QA/read-em-and-weep/blob/3cd8a620e7268cf86fb8cc019d35f04d3cb6b448/research/proof-repair-campaign/four-pair-composition/frontier.json) has SHA256

    b31a01ca80f80500f493ae507a308003226c85e9b941976d02466d956bc1078e

## Evidence and limits

The proof is pinned at commit c14af3d39881197edd781aa06cb1e918ef8fd42a, with SHA256

    4530b934749d8702571df45a30aaa3eb7a8fea3a2e5c07fdefe00bf551fa33fa

The package records 288 checks in both ordinary and optimized Python modes, covering exact input authentication, catalogue profiles, rank/degree consistency, the 4=2+2 filter, and universal coefficientwise differentiated Euler identities. Independent mathematical review checks the graph extension and first-polar argument against their pinned geometric premises. These checks do not constitute a Lean proof of the full geometric chain.

PR869 establishes nonempty abstract template families, not fixed HM realizations. Type III’s full-profile selection here is conditional on the retained actual-candidate catalogue; catalogue completeness is not asserted for every abstract family member. Neither surviving pair is identified as an actual realization, and further exclusion requires additional actual-source structure.

The cumulative relation is now 1,790 → 146 at burn closeout → 114 after a-b-c-f exclusion → 37 after overdue source2 integration → 6 after c-d-f specialization → 4 after this source126 theorem. These counts describe a fixed necessary catalogue relation, not proof-completion percentages or equally difficult remaining tasks. Actual source compatibility, physical construction, decisive higher-boundary evaluation, lifting and algebraicity remain open.
