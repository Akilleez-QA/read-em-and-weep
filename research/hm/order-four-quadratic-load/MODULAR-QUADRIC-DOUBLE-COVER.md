# General quadric cuts of the compact modular ruling family

This is a theorem about the canonical modular ruling family. Its identification with the normalization of the resolved eigenquotient incidence is a separate, unfinished step. In particular, no primitive twist-three or twist-four section is excluded here.

## Setup

Use the rank-two bundle V of MODULAR-RULING-BUNDLE.md, commit5967472ac1a9afe35628dac672fc88321b429110. On the smooth modular surface S, H=I+2F, I²=−5, IF=5, F²=0, K_S=3F, χ(O_S)=5. The bundle satisfies detV=I+3F, c2V=10. Set p:P_S(V)→S in quotient convention, ξ=O(1), and h=ξ+I.

The source morphism Φ_T:P4_x×P4_z→P14 is defined everywhere (Aure–Decker–Hulek–Popescu–Ranestad, arXiv:alg-geom/9606013, p25 before Lemma4.14; repeated p34). The global factorization T=(λμ,μ²,−λ²)⊗ŵ therefore proves that the five components ŵ have no common zero on P_S(V). They define w:P_S(V)→P4 with w*O(1)=h. On every p-fiber, h restricts to O_P1(1), so w maps that fiber isomorphically onto a line.

## Finite smooth double cover

For a general quadric Q⊂P4, let W=w^*Q∈|2h|. The restricted quadric system is basepoint free on the smooth threefold P_S(V), hence W is smooth by characteristic-zero Bertini.

No p-fiber is contained in W for a general Q: containing its image line imposes three independent linear conditions on the fifteen-dimensional vector space of quadrics. The closed incidence of such pairs over the two-dimensional base S thus has dimension at most 2+11=13 in S×P14, and cannot dominate P14. Consequently π=p|W is proper with all fibers zero-dimensional of length two. It is finite and flat (equivalently use the relative quadratic Cartier equation with no identically zero fiber).

Pushing forward 0→O(−2ξ−2I)→O→O_W→0 and using relative duality gives

0→O_S→π_*O_W→O_S(−3I−3F)→0.

The trace in characteristic zero splits this sequence, canonically as O_S-modules with the trace-zero summand. Thus W is the double cover with branch line bundle M=3I+3F and branch divisor in |2M|. Since (−M)H<0 and H is ample, H0(O_S(−M))=0. Therefore H0(O_W)=C. Smoothness and connectedness imply that W is integral.

## Invariants and torsion sections

Adjunction gives K_W=π*(K_S+M)=π*(3H). Hence K_W is ample, K_W²=2·9·15=270. The double-cover Euler characteristic is

χ(O_W)=2χ(O_S)+M(M+K_S)/2=10+(45+45)/2=55.

Noether's formula gives c2(W)=12·55−270=390.

Using the previously established h0(O_S(3H))=50 and h0(O_S(3F))=4, duality and the trace splitting give p_g(W)=54 and q(W)=0.

Each of the twenty-five torsion sections C_j≅P1 has I·C_j=−1, F·C_j=1, hence M·C_j=0. A smooth branch divisor cannot contain C_j: a contained component would have intersection C_j²=−5 unless it met another component, contrary to smoothness. Thus it is disjoint from every C_j. The restriction of the double cover to C_j is étale and therefore splits into two copies of P1. These fifty pairwise disjoint curves have self-intersection−5 on W, by the étale normal-bundle calculation.

The branch-disjointness argument uses smoothness of the branch, which follows locally from smoothness of a flat double cover of a smooth surface in characteristic zero: its equation is z²=b, and a singular point of b would give a singular point of W.

## Exact scope

These statements prove a compact smooth double-cover model and its invariants for the canonical ruling family. They do not identify W with the unnormalized inverse image of the target sextic, which can be nonnormal; nor do they prove that the actual resolved incidence is a fifty-point blowup of W. That correspondence and its exceptional tautological corrections must be proved before transporting any line-bundle obstruction to W. No full-Q4, delta20 invertibility, or complete repair is claimed.

Source: https://arxiv.org/pdf/alg-geom/9606013 . The double-cover and intersection deductions above follow from the displayed bundle calculation, not from selected-instance coefficient or rank tests.
