# Current independent mathematical review: alternative exceptional-fiber proof

Verdict: PASS under the stated bundle identification, cover geometry and natural deck/swap linearization. The complete normalized proof, historical reviews and exact dependency register are bound in CURRENT-REVIEW-BINDING.json.

## Verified derivation

1. Boralevi, arXiv:math/0602002v2, Corollary 2.2, lists the two unstable resolution types used here. Their generators give h0(E)=1, h0(E(1))=3 and no negative sections. The unique section has no divisor of zeros and produces a length-four lci zero scheme and 0→O→E→I_Z(−1)→0.
2. Extension of sections of a locally free bundle across the codimension-two set gives Hom(I_Z(−1),E(t))=H0(E(t+1)). This justifies the negative-Hom dimensions and the untwisted endomorphism algebra. The three non-scalar endomorphisms have image in the distinguished line, so they are square-zero and tracefree.
3. The Euler-sequence H0 map is multiplication by the linear coordinates times a nonzero section on the integral plane and is injective. Duality gives the H2 vanishing of the Ω1 term. The displayed Euler characteristics and all five plane-cohomology triples follow.
4. The universal-divisor calculation gives an actual finite-pushforward splitting. Deckwise trace subtraction yields (4,128,4), h1 deck dimensions (31,33,33,31), and the retained both-odd/swap-odd triple (0,15,3). Ordinary product linearization, not an extra Koszul sign, gives the O(−3) odd summand. Upstairs Serre duality confirms the signs.
5. Proper top-degree base change identifies the degree-two direct-image fibers and hence their support. It does not identify the exceptional degree-one cohomology dimension 15 with the fiber of an extended rank-12 sheaf. Neither the residue dimension three nor the support set gives torsion length, an evaluation map or a global obstruction value.

## Exact overlap and historical review scope

PR116 at e906fb83ca5ae4f5c75e7ca7a61863b984f15a0d already proves the entire dimension and support theorem. Its complete exceptional-surface proof was compared directly. The present contribution is the alternate codimension-two Hom derivation and the carefully bounded historical reviews, not a new dimension theorem or a newly discovered jump.

PR247 at 01c96a7e1b24685eacd5d1dc52ed0ea026490146 already uses the retained fiber dimensions and proves local freeness with base-change defect. The cover, stable-open and swap inputs have exact public references. Boralevi's normalized Chern classes, unstable classification and degree-25 surface agree with those inputs.

The historical audit reviewed its own alternative-proof source, not PR116's different proof text. This current review does not change that historical fact. The exceptional locus is not located or proved finite or nonempty. This theorem imposes no new source vanishing or nonvanishing claim and does not contradict separate mixed-vanishing results under additional premises.
