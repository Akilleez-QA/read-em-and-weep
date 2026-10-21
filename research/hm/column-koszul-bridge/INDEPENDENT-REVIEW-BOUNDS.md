# Independent audit: column Koszul bridge and coupled exclusions

Reviewed proof: `PROOF.md`, SHA256 `7b388da8bffd768a79e74eb73c7d1c89669f04a0cdcbd256d7282db556b76c3c`.

## Verdict and assumptions

The structural arguments pass independent mathematical review, conditional on the pinned actual generalized Eagon--Northcott complementary duality and the binary cubic syzygy calculation of PR511. This is a hand audit, not proof-assistant verification and not a new verification of every historical input. No selected source instance or numerical rank calculation was used.

## Independent checks

1. **Positive-strand argument.** Complementary duality changes `(i,d)=(1,8),(2,10)` in C0 to `(3,7),(2,5)` in C8. In degree 7 the only nonzero Koszul sheaf terms have p=0,...,3, with twists 8,...,5 after twisting by 8. In degree 5 they have p=0,...,2, with twists 8,...,6. Their sections are exactly the C8 positive strands, and these last terms have no boundaries. Consequently x=h0(Z3,7(8)) and y=h0(Z2,5(8)). These identities require neither the general transferred splice nor any fiberwise homology base-change assertion.

2. **PR511 bundle.** Sheafification of its exact cubic binary resolution gives L=10O(-2) plus 5O(-6). The original map has 50 linear generators and no constant redundancy. This is the actual linear-coefficient syzygy bundle used here, not a relative Tor bundle.

3. **Exterior inclusion.** Coproduct embeds the pth exterior power into U tensor its (p-1)st exterior power in characteristic zero: wedge after coproduct is p times identity. Evaluation of the first factor is the Koszul differential. The cycle condition therefore gives Zp,2p+1 inside L tensor exterior^(p-1)U tensor O(-(p-1)). Twisting by 8 gives, respectively, 100O(5)+50O(1) and 450O(4)+225O. Left exactness of sections yields y<=700 and x<=2475. No assertion of surjectivity or a split inclusion is needed.

4. **Coupled inequality.** Each exterior contraction anticommutes with the Koszul differential, hence the contraction coproduct maps Z3,7 injectively into U tensor Z2,5(-1). Put E=Z2,5. Its inclusion into 100O(-3)+50O(-7) forces every splitting degree b<=-3. The elementary inequality 6 max(b+8,0)<=5 max(b+9,0) then gives 6x<=50y, equivalently 3x<=25y. In particular y=0 implies x=0, without proving a converse.

5. **Full derived bridge.** The two-chart Cech transfer places H0(Kp(a)) in homological degree p and H1(Kp(a)) in degree p-1. The missing O(-1) term separates the strands. The only possible cross-row transfer has length two and is the alternating product alpha_u beta_v-alpha_v beta_u, hence the maximal-minor splice; higher transfers have impossible Cech degree. With H0(O(n))=Sym^n G, Serre duality gives H1(O(-m-2))=Sym^m G* tensor det(G*), confirming the determinant convention and shifts. No grade assumption enters this complex-level calculation.

6. **Torsion and universal coefficients.** On a local DVR the exact sequence is H_i tensor residue field -> H_i(fiber) -> Tor_1(H_(i-1),residue field), with an initial zero. Its direction in the proof is correct, and Nakayama permits the stated vanishings without flatness. The hypercohomology filtration is 0 -> H1(sheaf H_(i+1)) -> total H_i -> H0(sheaf H_i) -> 0. No canonical splitting or naive relative perfect pairing is asserted.

## Remaining open problem

The actual sections of the two cycle subbundles are not determined by their ambient splittings. The conclusions are necessary constraints 0<=x<=2475, 0<=y<=700, 3x<=25y, not exact dimensions, fixed-source first-order vanishing, higher-order lifting, or algebraicity.
