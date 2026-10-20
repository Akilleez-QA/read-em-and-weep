# Independent mathematical review: the lower Rao graph scalar

Reviewed exact PROOF.md SHA256: baa36da6e53f5474707918584a3889f38305177f05d974321cdd1689b3a66747. The full proof was read back and checked.

Status: mathematically checked conditional on the pinned PR455 and PR471 inputs and the stated HM normalizer identities. This is not formal proof-assistant verification and uses no selected coefficient evaluation.

Put T=V*, P_e=Hom(M_(6-e),C). The exact last cokernel of the dual PR471 resolution gives the COMPLETE graded presentation

S(-1) plus 45S(-2) -> V tensor S plus R6 tensor S(-1) -> P -> 0.

This does not require exactness elsewhere in the dual complex. Local duality identifies its last cokernel with the shifted dual Rao module. In particular there are no additional higher-degree relation generators.

Naturality of Eagon--Northcott identifies P2 with H1 B(1): H2 F(-3)=H3 F(-3)=0. The canonical nontrivial H-character summand of P1 is H1 B, and equals T P0 by PR471's actual top multiplication. Thus the map T(TP0) -> P2 is the actual B-cohomology multiplication T H1 B -> H1 B(1).

The representation calculation is consistent: Sym2(T)=A* tensor U'; V tensor A*=T tensor (U' plus W); U' tensor U'=1 plus U' plus J5; W tensor U'=R6. Thus Sym2(T) tensor V=T tensor (1 plus U' plus J5 plus R6). Multiplying the nonzero Euler relation by T injectively removes the single T tensor 1 copy. The remaining degree-two free space is T tensor (U' plus J5 plus 2R6), whereas P2=T tensor (J5 plus R6).

Generation of M gives surjectivity of T tensor M4 -> M5. Its R6 projection is a nonzero multiple of evaluation V tensor T -> C on the R6 summand of M4=V tensor (J5 plus R6). This follows by taking H-invariants of End(V); its invariant part is the trivial representation, and Hom_G(J5,R6)=0. Consequently the linear-R6-generator map T tensor R6 -> P2 is an isomorphism onto its R6 channel. The J5 channel from quadratic V-generators must also be an isomorphism, as it has no other source.

Normalize these two maps. The remaining quadratic-V R6 channel is a scalar alpha. The degree-two relation module consists of the forced T tensor U' channel and a graph T tensor R6. If alpha=0, this graph lies entirely in Sym2(T) tensor V; its projection to the linear-R6 free block is zero. The Euler relation has the same zero projection. Since the displayed presentation has no other relation generators, P would then split off the free module R6 tensor S(-1). This contradicts finite length of M and P. Hence alpha is nonzero.

It follows that Sym2(T) tensor P0 -> P2 is surjective, equivalently T H1 B -> H1 B(1) is surjective. In the presentation, the relation projection onto T tensor R6 is now an isomorphism. Hence P/(S P0)=R6 tensor k(-1). In every degree j>=2, Pj=S_j P0. Dualizing proves injectivity of the joint multiplication map M_d -> Hom(S_(6-d),M6) for d<=4, and identifies M/Soc(M)5 as a level module with socle concentrated in degree six and of dimension five. This is a simultaneous-multiplication assertion, not surjectivity or injectivity for a single selected polynomial.

No claim about original fixed-pair source membership, higher-order lifting or algebraicity follows. Normalizing a nonzero scalar requires a compatible rescaling of chosen irreducible-channel identifications; this is not a coefficient computation.
