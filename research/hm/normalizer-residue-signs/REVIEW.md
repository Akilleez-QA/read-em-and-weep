# Independent review: normalizer residue signs and exact primary degree-five rank

Verdict: PASS for the mathematical deduction from the pinned actual-geometry and quadratic-generation inputs, with the minor identification-language correction incorporated. Reviewed 2026-10-21 UTC. This is not formal verification or a fresh proof of all upstream theorems. No selected actual HM/source coefficient, map matrix, rank evaluation, large computation, or public write was used.

## Sources independently inspected

The audit covers PROOF.md, the pinned proofs corresponding to PR590 (degree-five-invariants), PR570 (primary-surface-dictionary), PR572 (residual-canonical-decic), and PR573 (global-primary-equality), and the independent review of PR590. The primary texts inspected were Horrocks–Mumford (1973), Sections 1 and 3, Lemma 3.3(vi), and the Appendix character table; and Barth–Hulek–Moore, Sections 4.2–4.5, particularly Propositions 9–10. Primary references are the Brown-hosted HM PDF and the TIFR-hosted Vector Bundles on Algebraic Varieties volume linked in PROOF.md.

## Actual geometry and the two signs

The ambient actual primary surface is a coordinate copy of BHM's S15 by PR570, and its full scheme identification and normalizer invariance are supplied by PR573 and PR590. These are stronger inputs than an abstract thirty-point configuration. Automorphisms of the surface lift uniquely to normalization, so their actions on branch residue fields and the ambient-pullback line bundle are the relevant actual linearization.

At p=[e0], the determinant-one lift m=-P2, where P2(e_i)=e_(2i), has eigenvalue -1. Thus it acts on the O(5) fiber by -1, whether the fiber convention is dual or direct. Its square is the index reversal P_(-1), as required for the central element of SL2(F5).

The branch sign admits an independent direct check that bypasses any possible ambiguity about equivariance of a modular-base identification. BHM Proposition 10, printed page 64, gives the two branch tangent planes at e0 as x2=x3=0 and x1=x4=0. Multiplication of indices by 2 (or its inverse 3) exchanges these planes. Because they are distinct tangent planes of the two smooth local branches, m exchanges the branches. The induced action on the length-one normalization quotient C^2/C_diag is therefore -1. Combined with the O(5) scalar, the twisted conductor fiber has sign +1. Galois changes of the primitive fifth root do not change this rational signed permutation, and contragredience replaces the permutation by its inverse, which still swaps the planes.

The author's modular argument agrees: PR572 identifies the cusp pair with the fixed pair of a C5 on the faithful A5 base. The nontrivial involution in D5/C5 must exchange these fixed points because it conjugates the C5 to its inverse. BHM Proposition 9 says the two preimages of a node lie on the two paired distinct cusp fibers. This again forces branch interchange, not merely permutation of an abstract set of nodes.

The unipotent lift has order five, fixes e0 with eigenvalue one, and cannot exchange two branches. Its twisted fiber action is +1. Evaluation of the G-invariant orbit line at p is an isomorphism by PR590, so these fiber calculations really determine the stabilizer action on that line. Together the torus and unipotent generate the full direction stabilizer. Alternatively, the Borel's commutator subgroup contains its C5, so any one-dimensional stabilizer character is determined by the order-four torus generator. The actual six-line module is consequently the unsigned induced permutation module, not a signed version inferred from the support.

## Target and source representations

The action on the six directions is doubly transitive. The permutation module therefore has one constant line and one irreducible five-dimensional complement. The HM character table contains exactly one five-dimensional irreducible, J5, which has positive central involution. Hence the actual invariant target is 1+J5.

HM Lemma 3.3(vi) is the required full normalizer identity: Sym^3(V0)=V3 tensor (chi5+chi2'). It is not merely a dimension identity or a statement restricted to H5. Its Galois conjugates cover the four nontrivial central characters; dualization is among these conventions. J5 is preserved, while the two-dimensional spin label may change, which is immaterial here.

The extension-uniqueness argument is valid. Transport the actual Q2 action through an H5 intertwiner to the standard five-dimensional representation with the same central character. For each normalizer element the ratio of actions commutes with H5, hence is scalar, and the scalars form a character trivial on H5. Such a character factors through SL2(F5), which is perfect. One elementary check of perfectness is that conjugating an upper unipotent u(b) by diag(2,3) sends it to u(4b), so commutators contain all upper unipotents; conjugacy gives all lower unipotents, and these generate SL2(F5). Thus the scalar character is trivial. There is no undetected linearization twist of Q2.

The five-dimensional factor in the symmetric cube has the central character inverse to that of Q2, so the same argument identifies it as Q2*. Its invariant tensor with Q2 is the scalar endomorphism line, on which the normalizer acts trivially. This gives the genuine seven-dimensional source J5+Wspin. No choice of a Galois or dual convention introduces a trivial source summand.

## Schur deduction and exact scope

Equivariance kills Wspin and forces the J5 restriction to be either zero or an isomorphism onto the unique J5 in the target. PR590's established rank lower bound a>=1 excludes zero. Thus a=5, r5=24+5=29, and h1(O_S(5))=1. The cokernel is the trivial normalizer representation and the invariant kernel is Wspin. All uses of a rank bound are previously proved structural statements, not an actual-instance evaluation performed here.

For precision, an arbitrary K-equivariant isomorphism from the target to the permutation representation is not unique up to one scalar, since its trivial and J5 summands may be scaled independently. The claimed uniqueness is correct for an isomorphism respecting the six specified orbit lines. The sum-of-residues obstruction itself is unique up to scalar, since the trivial quotient has multiplicity one. This correction does not affect the rank or defect conclusions.

The proof settles the primary degree-five conductor rank only. It does not settle a full-adjoint primitive-twist-four connecting map, prescribed-source membership, higher lifting, or algebraicity. The actual geometry, quadratic generation, and pre-existing nonzero-image bound remain explicit upstream dependencies.

## Final version and ambient restriction boundary

The final PROOF.md was reread after the reference and wording corrections. PR572 is correctly cited as research/hm/residual-canonical-decic/PROOF.md at a20545dcc4c0e26dc1bb8af17852db63696ec7b1. The final mathematical verdict is PASS. No ambient-quintic restriction corollary is asserted: h1(O_S(5))=1 does not by itself establish H0(I_S(5))=0 or surjectivity of ambient quintics onto H0(O_S(5)). Those concern the separate ambient restriction map.
