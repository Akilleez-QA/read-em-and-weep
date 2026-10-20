# Read-only source checks for the subgroup-rigidity corollary

Checked 2026-10-19. These are imported mathematical source statements, not new executions of their calculations.

## Public sources

1. [PR 1 comment 6260553958](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6260553958), created and last updated 2026-10-19 05:43:54 UTC. This expressly identifies the corrected pure coefficient with the deck character (11;00), inner-swap signs (−;+), and exchanges the pairs for the other pure direction. It says the tuple (79,2,0,0,0) records dimensions per deck character by weight, with total 87. It uses the weight-two zero for pure rigidity and the weight-four zero for mixed rigidity. It expressly keeps the corrected model versus actual physical mixed-ambient identification open.

2. [The pinned finite Ext-model specification](https://github.com/Akilleez-QA/read-em-and-weep/blob/add03476d9055aa00e1e00778eea6332cf8e01cc/research/hm/ext-model.md), Git blob `fad0e87f0e30ec916e18fd47feea584c7d8eaae6`. The source defines X=C⁴ and the carrier E=f*H⊗N, identifies the specified strict endomorphism model with RHom_X(E,E), and states that each row of its weight table corresponds to one deck character. Its Ext¹ entries at weights two and four are zero. It also explains that tensoring by N does not change the endomorphism algebra. This is the relevant imported identification for the root-transported coefficient, subject to its stated source premises.

3. [The pinned independent degree-one certificate output](https://github.com/Akilleez-QA/read-em-and-weep/blob/e25436992df659f1aaaab01d13b942a3e644e1ff/research/hm/expected-hsd-unpruned-h1.json), Git blob `e60cb0d4a7529ab0719b30548c66ff9377d15860`. Its `pinnedHead` is `add03476d9055aa00e1e00778eea6332cf8e01cc`; it records `ext1ByWeight=[79,2,0,0,0]`, multiplicities `[1,4,6,4,1]`, and `ext1=87`. It was read, not rerun.

The existing independent review `premise:hsd-pr25-review/REVIEW.md` was read as corroborating provenance. Its earlier executions are not executions made in this task.

## What follows, and what does not

For H=(Z/2)^4 and pure coefficient I=ε O_X with character {1,2} or {3,4}, the imported coefficient identification yields

    H¹(X,End(M₀)⊗I)^H = 0.

For the mixed coefficient of character {1,2,3,4}, it yields the analogous H-invariant Ext¹ vanishing. This is invariant rigidity. It does not imply vanishing of the entire upstairs H¹, whose other characters may be nonzero.

Combined with Section 10 of PROOF.md, an actual H-equivariant marked pure lift can retain its underlying module and its specified H-action while receiving a full signed-pair action. This conclusion still requires a verified genuine H-action on that actual pure lift, compatible with the fixed classical full-group action. The numerical table and the corrected-model comment do not supply that verification by themselves.

No module obstruction or retained physical value was evaluated. No source was modified and no numerical verifier, operator, matrix construction, or large computation was run.
