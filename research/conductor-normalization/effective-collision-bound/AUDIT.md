# Preserved mathematical audit

This review concerns the source manuscript and its stated assumptions. It is preserved as mathematical history, not a new independent certification of all publication edits or of unpublished input theorems. Source and publication hashes are recorded in SOURCE-HASHES.json. A split manuscript’s module or polar application remains conditional in its destination unit.

# Independent audit of the effective collision-order bound

## Verdict

The regularity argument is correct over C. It proves that B0=End₀(F) is 11-regular, hence H¹(B0(t))=0 for t≥10 and H²(B0(t))=0 for t≥9. With the adjacent-generator resolution in the cited all-power theorem, the sharper sufficient collision order is **k≥13**. The common-threshold argument also gives the weaker valid bound k≥14.

## Scope and checks

I independently checked `PROOF.md`, read `../sixth-ideal-pushforward/ALL-POWERS.md`, and checked the references below. The geometric contraction and sign-pushforward identities are used under the hypotheses of that theorem; this audit does not independently reconstruct its earlier geometric inputs.

- The normalized monad is 5O(-1)→2Ω²(2)→5O. Its determinants give det K=O(-6), det F=O(-1), and F∨≅F(1).
- Exterior duality identifies M∨ with 2Ω²(3). The displayed Koszul resolution of Ω²(3) has terms O, O(-1), O(-2) in homological degrees 0,1,2, respectively, so M∨ is 0-regular.
- Dualizing the locally split kernel sequence is legitimate. In the resulting cokernel sequence, the direct long-exact-sequence checks make K∨ 0-regular. In particular, the potentially relevant top line-bundle group is H⁴(O(-3)), which vanishes. No invalid general kernel-regularity inequality is used.
- Tensor subadditivity and the characteristic-zero alternating projector make Λ⁶K∨ 0-regular. The identity Λ⁶K∨≅K(6) then makes K 6-regular.
- The second monad sequence makes F 6-regular; the top line-bundle group used here is H⁴(O(2))=0. Thus F∨ is 5-regular and End(F) is 11-regular. The trace splitting makes B0 a direct summand, with the same regularity bound.

## Final collision-order calculation

For n=k-3, the all-power theorem supplies

    0→⊕O(-e_i)→⊕O(-d_i)→K_n→0.

Its ordered minimal generators satisfy d_i≥n and strictly increasing b_i. Thus

    e_i=d_i+3(b_(i+1)-b_i)≥n+3.

For k≥13, n≥10, so d_i-1≥9 and e_i-1≥12. The trace pairing identifies B0 with its dual. Serre duality, using ω_(P⁴)=O(-5), therefore gives

    H²(B0(-4-d_i))∨=H²(B0(d_i-1))=0,
    H³(B0(-4-e_i))∨=H¹(B0(e_i-1))=0.

Tensoring the exact resolution by the bundle B0(-4) and taking its long exact cohomology sequence proves H²(B0(-4)K_n)=0. The stated sign-pushforward identity therefore gives the claimed sufficient vanishing for every k≥13. All twist signs and index shifts agree.

This is a sufficient bound, not an optimality claim, a physical-source membership calculation, or a deformation-order statement. No selected matrix ranks, obstruction coordinates, or source representatives were evaluated.

## Verified references

- Ada Boralevi, [The Horrocks–Mumford bundle restricted to planes](https://arxiv.org/pdf/math/0602002), equation (1.1), PDF page 1, and normalization paragraph, PDF page 3.
- Robert Lazarsfeld, [Positivity in Algebraic Geometry I, §1.8](https://beckassets.blob.core.windows.net/product/readingsample/389723/9783540225331_excerpt_001.pdf): Theorem 1.8.3 (persistence), Example 1.8.7 (resolution criterion), Proposition 1.8.9 (tensor products), Corollary 1.8.10 (exterior powers), and Remark 1.8.14 (characteristic caveat).
