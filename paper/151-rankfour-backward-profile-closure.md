# 151. The complete ordered rank-four backward plateau is excluded

**Craig Ward · 24 October 2026 UTC · All four restricted-image ranks eliminated**

## Exact new reduction

The [integrated backward theorem](https://github.com/Akilleez-QA/read-em-and-weep/blob/cf0bd10ccf99863bf5531de35954dfddc318cfbc/research/hm/rankfour-backward-profile-closure/PROOF.md) excludes actual generic SF rank four with ordered maximal plateau (k,l)=(3,1), conditional on the retained actual-geometric, equivariant primary-module, necessity and transfer premises.

The necessary bad coarse frontier decreases from **22 to 21**. Three rank-four bins remain: (1,1), (1,2), (2,1). Eighteen higher-rank bins remain, grouped as 6,4,2,2,1,1,1,1 at ranks five through twelve. The optional source-labeled refinement decreases from 88 to 84. These are necessary overlist counts, not realizations, equal-work units or a completion percentage.

This is the whole-profile conclusion that [chapter149](149-backward-dual-cubic-image-bound.md) did not supply. It adds the separately checked lower-image and rank-one exclusions rather than retroactively strengthening that partial theorem. Generic SF≥4 and square rank≥28 remain the bounds; SF≥5, positive-square surjectivity, full-adjoint invertibility and original repair are not proved. This does not improve the separate cone specialization.

## Fix one section copy and keep it throughout

The hypothetical ordered chain has ranks 5,9,13,17,21, with E=F₃ and B=E/F₂. The actual E and Q* retain ranks seventeen and thirteen and their different presentations. Forward length one does not force source Z.

The actual Euler character χ_G(Q*(3))=T₆−2W−S₄ and genuine H¹ imply that H⁰(Q*(3)) contains a T₆ copy. Choose one inclusion i:T₆→H⁰(Q*(3)) and form

    ψ_i:T₆ O→Q*(3)→E*(1),   J_i=im ψ_i.

The same choice i is retained in every branch. There is no assumption of uniqueness, canonical splitting, or injective evaluation. The full dual derivative has rank four. Its actual kernel Z=F₄⊥ has H⁰(Z(3))=0 by endpoint persistence, so ψ_i is nonzero. Its image is locally free on the smooth parameter curve, hence has generic rank in {1,2,3,4}.

## Rank four was excluded in the partial theorem

Chapter149's cubic-image result excludes rank four for every chosen copy. It retains all four necessary source types and positive defects until the relevant subcase forces stronger restrictions. The lower-rank argument must therefore treat ranks one, two and three, not assume that the image is the full rank-four annihilator.

## Ranks two and three fail a common upper-endpoint test

The lower-image classification supplies thirteen necessary actual image/kernel/quotient pairs and the genuine exact sequence

    0→N→B→J_i*(1)→0.

Any bundle splitting used there is proved by the invariant Ext calculation, including the two cases where ordinary Ext is nonzero. It is not a horizontal splitting, and the later inverse-image extensions are not declared split.

The complete degree ledger for those thirteen pairs forces the last defect δ₃=0. Thus L₄=B(2), and the actual upper endpoint satisfies

    0→Z→Q*→B*(−2)→0,   maxdeg Z≤−4.

Its actual derivative takes values in B*(−4). At twist four, the section map is injective: a kernel would define a negative-degree top subbundle with no internal or external derivative component, hence a constant subbundle, which is impossible. Therefore

    χ_G(Z(4))≤H⁰(Z(4))≤H⁰(B*).

For every one of the thirteen quotient shapes, exact additivity gives physical V excess exactly one:

    [V:χ_G(Q*(4))−χ_G(B*(2))−H⁰(B*)]=1.

This contradicts the necessary representation inequality. It excludes all ninety-six retained inverse-image torsion partitions, including eighty-three positive-defect partitions. Neither of the earlier two defects is assumed zero. These are formal necessary partitions, not geometric realizations.

## Rank one requires a separate proof

The rank-one branch forces J_i=O(9) and necessary source D. This restriction is not imposed on the other image ranks. Since maxdeg E*(1)≤9, the image is saturated and the actual quotient sequence is

    0→N→B→O(−8)→0,   rank N=3.

The complete determinant ledger gives deg B∈{−2,0,2,4,6,8,10}. The actual embedding N(2)→Q and the retained rank-independent dual-type theorem bound N's slopes above by six; rank and degree bound them below by −6. Consequently H¹(N(8))=0. The extension splits as an ordinary bundle and equivariantly, by proof rather than assumption.

Two complete finite enumerations give fifty-three abstract N shapes. Valid section inequalities and necessary injection tests into the same actual Q leave sixteen:

- Seven have deg B equal to −2 or zero. Their two lower defects vanish. Neither complete endpoint domain, of size thirteen or forty-six, contains a shape satisfying both required Euler identities. The possible upper defect twelve in degree −2 is retained until this contradiction.
- Nine have deg B>0, which forces only the last defect δ₃ to vanish. The same upper-endpoint top-section argument gives physical V excess one in every case, without suppressing earlier defects.

Thus rank one is impossible as well. The rank-one argument proves its own upper-endpoint lemma and does not assume the whole-profile conclusion or the rank-two/rank-three exclusion.

## Exhaustive coverage, not a change of section copy

Every possible nonzero rank 1,2,3,4 is impossible for the same fixed ψ_i. This contradicts the existence established before the case split and excludes the ordered (3,1) plateau.

The dependency chain is acyclic: original premises supply the cubic-image bound and lower-image constructions; these support the uniform lower-image exclusion; the original premises and common constructions support the separate rank-one proof; those branch theorems then integrate. Source D is branch-specific, not a global assumption. Positive determinant and inverse-image torsion defects remain until their particular branch proves a restriction or contradiction.

## Evidence and scope

The frozen integration proof SHA256 is `5a1d34fb57fcda4709e33fd184e762db67f9086238ec38a4a3342b8c2c1ba11b`. Its [independent review](https://github.com/Akilleez-QA/read-em-and-weep/blob/cf0bd10ccf99863bf5531de35954dfddc318cfbc/research/hm/rankfour-backward-profile-closure/reviews/integration/REVIEW.md) SHA256 is `ca050ba4a194367f1a609274864433f4589b820b724c1ab3d17d1aa89f27ab4c`. The integration certificate performs 221 checks and thirteen executed negative controls; the independent integration verifier performs 157 checks and fifteen controls. Normal and optimized runs agree. Replayed dependency totals of 16,582 and 4,207 include shared checks and are not added as disjoint new evidence.

The [portable publication checker](https://github.com/Akilleez-QA/read-em-and-weep/blob/cf0bd10ccf99863bf5531de35954dfddc318cfbc/research/hm/rankfour-backward-profile-closure/check_publication.py) authenticates the complete packet, including all four constituent mathematical reviews and the final integration review. Run `python3 check_publication.py` to replay the normal and optimized checkers, executable controls and five full comparison preflights.

Six complete original sources are retained, with seventeen copies compared across the constituent packets. The independent reviewer read all constituent proofs and their originals, checked same-copy coverage and the dependency order, and authenticated the final bytes. Authentication does not discharge the original geometric hypotheses, and these certificates are not proof-assistant verification of them.

No actual coefficients, parameters, jets, matrices, instance ranks or historical source enumeration are evaluated. Prior partial chapters and the delivered PDF remain unchanged; this chapter adds the separate whole-profile conclusion at its own cutoff.
