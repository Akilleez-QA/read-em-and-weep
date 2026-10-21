# Independent mathematical review: Euler exclusion of the middle ghost

Reviewed proof SHA-256: 52f8c40e2370d2f720ebb59b28f75d5fabbcc421aa9763e0614773e8bb93e5fc.

Verdict: the argument proves s=0, conditional on the pinned representation and Betti-family inputs. It determines the free modules of the minimal resolution of H and forces u=0 in the scalar-annihilator family. It does not determine v or explicit differentials.

## Independent checks

1. The degree indices are consistent. After r=0, the only possible targets of a degree-five generator of F3 are the degree-four generators of F2 with linear coefficients and the degree-five scalar with constant coefficients. Minimality kills the latter. No other generator degrees can contribute.

2. Equivariant minimal lifts exist. At each stage the finite group acts on the graded syzygy module and on its quotient by the homogeneous maximal ideal. Characteristic-zero semisimplicity permits equivariant sections of these finite-dimensional graded quotients, giving an equivariant minimal free cover inductively.

3. The Euler column is unique. Taking Heisenberg invariants in T tensor V gives scalars by irreducibility of V. This scalar is the identity endomorphism and is fixed by the full normalizer. Since U' has no quotient-group invariants, there is no invariant component into V tensor U'. The degree-five F3 scalar cannot have zero differential: exactness and minimality would place its basis vector in the maximal ideal times F3.

4. The relevant tensor is the canonical one, not a chosen coefficient model. For f:V -> S2 tensor E tensor W', the canonical Hom identification gives tau_f in T tensor S2 tensor E tensor W'. The composition with the Euler column is exactly (mu tensor id)(tau_f). Thus vanishing of the complex composition is equivalent to membership in ker(mu) tensor E tensor W'. There is no additional antisymmetrization, dual convention, or determinant twist in this step.

5. The multiplication kernel is correctly identified. The pinned decompositions yield T tensor S2=A tensor (T4+J5+W'+Q4). The product U tensor U' has character (9,9,1,0,0,-1,-1,-1,-1), which equals T4+J5. The dimensions are 75=20+25+10+20. Since S3=A tensor (J5+W') has dimension 35 and polynomial multiplication is onto, its kernel consists precisely of the other two inequivalent irreducibles, A tensor (T4+Q4). In particular the ordinary four-dimensional T4 and spin four-dimensional Q4 must not be identified.

6. The invariant-kernel test uses the correct dual. E=A* and W' is self-dual, so (E tensor W')*=A tensor W'. This irreducible is absent from the kernel. Therefore tau_f=0 and f=0. This contradicts exactness at F2 because a nonzero degree-four minimal generator cannot belong to im(d3), which lies in the maximal ideal times F2. The contradiction does not require a rank computation or a selected polynomial.

7. The consequences are correctly delimited. PR483 leaves exactly shifts (0,2,4,6,8,10) and ranks (2,10,20,20,10,2) when r=s=0. In PR492, u<=2s gives u=0; substituting q=u=0 gives the displayed remaining R family. Nothing in this reasoning removes v. The nonzero third differential between the two outer scalars of PR483's B(0) spectral sequence is consistent with, and now required by, s=0.

This is independent mathematical review, not formal proof-assistant verification. The review checks the deduction from the pinned inputs rather than re-proving all upstream cohomology claims. No selected actual HM/source-instance evaluation, numerical matrix/rank computation, coefficient search, generator/checker, or large computation was used. Higher-order lifting, algebraicity, fixed-pair values, and source membership remain outside the conclusion.
