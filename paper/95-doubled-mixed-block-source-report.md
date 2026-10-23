# Doubled mixed block and weighted 32-to-34 presentation: source report

**Craig Ward · 23 October 2026 · Full-source report of mr. slop's PR1062**

[Immutable full proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/2a7565f5828447907ad860c861891ec2fdb4f7cb/research/hm/double-mixed-block/PROOF.md).

This chapter reports the complete immutable proof and accompanying five-file change, not an independent reproof. The result concerns the original full opposite pencil on the negative parameter line, not an identification with separately embedded pure-V homotopy modules.

## A canonical two-copy block

The full source U=2W+2W′+3S+4T6 has dimension 44, and the target N=1+4A+2V+3P+3D has dimension 46. Let M=Hom_G(T6,U), of dimension four. Only the T6 source can reach the V target under negative multiplication. Surjectivity of the complete coefficient map W⊗U→N therefore forces its V multiplicity map f_V:M→Hom_G(V,N) onto. The latter target has dimension two, so K=ker f_V is canonically two-dimensional.

This uses surjectivity of the complete two-coefficient map, not surjectivity of an individual 44-to-46 fiber map. The marked T6 of PR1060 determines a line in K. No canonical complementary line is chosen.

Both remaining multiplicity maps f_P|K and f_D|K are injective. For any nonzero direction in K, a D-only channel would force O(-6) into the actual full kernel A O(-6), contradicting Hom_G(1,A)=0. A P-only channel would force W′ O(-3) into that kernel, contradicting H0(O(-3))=0. Total vanishing likewise contradicts Hom(O(-1),O(-6))=0. These are actual sheaf-kernel arguments, not evaluated coefficient ranks.

Consequently U_K=K⊗T6 selects canonical target subspaces N_P,K and N_D,K of characters 2P and 2D. The coefficient image is their direct sum and coefficient kernel is K⊗V. The corresponding **bundle** map is injective on every fiber, with exact sequence

    0→U_K O(-1)→(N_P,K⊕N_D,K)O→K⊗V O(2)→0.

The source has rank 12, target rank 18, and quotient rank six and degree twelve. The two actual channel maps identify their images with the same K, so the block is two copies of quadratic evaluation without an unaccounted relative matrix. The actual subspaces and cokernel are canonical; the displayed scalar-normalized model identification is not. Coefficient kernel and sheaf kernel are distinct: the latter is zero on this block.

## The inherited weighted presentation

Set N_K=N_P,K⊕N_D,K and Z=(N O)/(U_K O(-1)). This locally free target fits into

    0→K⊗V O(2)→Z→(N/N_K)O→0.

It has rank 34 and degree twelve. Quotienting the original complex by the injective marked subcomplex gives the actual exact sequence

    0→A O(-6)→(U/U_K)O(-1)→Z→C→0,
    U/U_K=2W+2W′+3S+2T6,   dim(U/U_K)=32.

The kernel is still the original A O(-6): it intersects the marked source trivially because that block is injective. The cokernel C is unchanged. This is an inherited 32-to-34 presentation, not merely a new character balance.

The target extension splits equivariantly because H1(O(2))=0, but not canonically. After a choice, its form is

    Z≅(1+4A+2V+P+D)O ⊕ K⊗V O(2).

The constant part has rank 28 and the weighted part rank six. The target is therefore **34, not 28**. The unchanged cokernel has rank 34−32+3=5 and degree 12+32−18=26.

## What the reduction does not discard

All remaining actual off-diagonal maps are retained. In particular the rank-six weighted term embeds in Z, not necessarily in the rank-five C; other source images can meet it. There is no rank-six-into-rank-five contradiction. No second marked line in K, canonical target splitting, opposite-bundle type, vertex scalar or terminal-string branch is selected.

These actual selected 2P and 2D subspaces are not identified with im h-generated subspaces by repeated labels. The theorem changes neither the four necessary source-dual pairs nor the unselected pure-V endpoint-9/16 alternatives. The complete nonic component-scheme classification remains separate.

The source's verifier checks fixed characters, full-middle Euler bookkeeping, universal degree balances and immutable inputs. The actual saturation, quotient exactness and kernel arguments remain written mathematical proofs. Its independent review covers the final source files; this chapter reports that source rather than claiming independent proof-assistant certification or a new actual-instance calculation.
