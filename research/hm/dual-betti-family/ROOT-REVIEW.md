# Root mathematical review

Proof reviewed: SHA256 `d304619b07ad080fdb61b6ed5b066ec2dfb2cd6031cc9a40ec8815e000339d0d`.

The two-parameter Betti family is accepted conditional on the pinned actual-module inputs of PR476, PR479 and PR482. I independently audited the spectral positions and retained the middle transgression ambiguity.

For B(1), the q=3 leftmost term is T, because its next cohomology group is H^3(B(-3))=0. The only surviving differential from it goes to Tor_3(H)_6. The latter maps onto Tor_1(K)_2=T tensor U'. All alternative differentials are excluded by the stated low K syzygy and H^0 vanishings. Zero abutment gives the exact sequence, not merely the dimension twenty. Serre–Koszul duality gives Tor_2(H)_4=V tensor (1+U').

For B(0), the first q=3 horizontal map is injective from dimension twenty-four into dimension twenty-five, being dual to the established onto bottom K multiplication. Its cokernel is the one-dimensional dual Euler relation. Tor_3(H)_5 injects into the Euler relation at (-1,1), so its dimension s is at most one. The dual Tor_2(H)_5 receives the corresponding map from that cokernel. Critically, if s=0 the remaining d_3 from (-4,3) to (-1,1) is allowed and must be an isomorphism. The Euler class alone does not force s=1. The proof properly retains both possibilities and does not infer a vanishing scalar from pairing parity.

The complete presentation of H determines the first and fourth free modules; generation and the perfect pairing determine the zeroth and fifth. Minimality bounds the second free module to degrees three through six. The exact twenty-dimensional degree-four term and the Hilbert numerator coefficient twenty exclude Tor_3(H)_4 and hence its dual Tor_2(H)_6. This accounts for every remaining degree and establishes the full displayed family. The cubic and middle alternatives need not be independently realizable.

Adjacent equal-degree summands are minimal-resolution ghost possibilities, not cancelable units. The result does not specify differentials or settle either parameter. This is mathematical review, not formal proof-assistant verification or independent reproof of every dependency. No selected HM/source-instance evaluation, numerical rank calculation or coefficient search was performed.
