# Supporting regularity theorem

This existing result is included as a prerequisite for the selected pole, detector and socle manuscripts. The older intermediate bounds are preserved as history; SHARPEST-BOUND.md records the stronger proved bounds under its precise hypotheses. No source membership is inferred.

# Stronger H² vanishing from the tensor monad

## Result

For B₀=End₀(F), with F the normalized Horrocks–Mumford bundle,

    H²(B₀(t))=0 for all t≥3.

Together with H¹(B₀(t))=0 for t≥8 from PROOF.md, this improves the common sufficient UNWEIGHTED source collision order to 8. The first and second weighted coefficient orders are 9 and 10 respectively. A common downstairs coordinate-detection surface thickening has degree 42.

## Proof of the stronger H² threshold

Use the normalized monad and its two short exact sequences

    0→K→M=2Ω²(2)→5O→0,
    0→5O(−1)→K→F→0.

The exterior Koszul resolution 0→O(−3)→5O(−2)→10O(−1)→Ω²(2)→0 proves M is 1-regular. Equivalently, twist the 0-regular resolution of Ω²(3) used in ../effective-collision-bound/PROOF.md. By PROOF.md, F∨=F(1) is 4-regular. Thus F∨⊗M is 5-regular by tensor subadditivity, and

    H²(F∨⊗M(t))=0 for t≥3.

Tensor the first short exact sequence by F∨(t). Its long exact sequence contains

    H¹(5F∨(t))→H²(F∨⊗K(t))→H²(F∨⊗M(t)).

The left group is 5H¹F(t+1), which vanishes for t≥3 by the primary Hilbert-series computation. The right group vanishes by 5-regularity. Therefore H²(F∨⊗K(t))=0 for t≥3.

Tensor the second short exact sequence by F∨(t). The controlling part is

    H²(F∨⊗K(t))→H²(End(F)(t))→H³(5F∨(t−1)).

Since F∨(t−1)=F(t), Serre duality identifies the right group with the dual of 5H¹F(−t−4), which vanishes for t≥3 (indeed already t≥−3). Both outer groups vanish, proving H²End(F)(t)=0. The trace splitting gives the same vanishing for B₀.

This argument evaluates no HM matrix or selected source instance. It relies only on the primary cohomology module, exact vector-bundle sequences, duality and standard regularity subadditivity.

## Updated common collision order

Keep precisely the imported geometry and regular class-transport hypotheses of prerequisite full-target-collision-criterion, document PROOF.md. (see the unit INPUTS.md) For r=0,1,2 the coefficient is B₀(r−5)K_n with n=k−3. The controlling dual groups are H²B₀(dᵢ−r) and H¹B₀(eᵢ−r), where dᵢ≥n and eᵢ≥n+3. If n≥r+5, then

    dᵢ−r≥5≥3,   eᵢ−r≥8.

Both vanish. Therefore

    H²(Y,(q_*(I^k EA^r))_sign)=0 for k≥r+8.

In particular a closed regular UNWEIGHTED R∈I⁸E gives e_sign(σR)∈I⁹EA and e_sign(τR)∈I¹⁰EA²; both weighted classes vanish. Under the exact regular transport and injectivity premises, both retained coordinates vanish. The constant coordinate also vanishes under its corresponding transport. The condition may be imposed on the H-sign projection R_H of a raw source instead, with the same separate closure, regularity, ideal-membership and class-comparison premises.

These are sufficient, not optimal, orders. They are ordinary collision-ideal orders, not deformation orders. No source is asserted to satisfy them.

## Common degree-42 detector thickening

The individual downstairs neighborhoods N₅,N₆,N₇ suffice for r=0,1,2 respectively, and T=N₇ is common to all three global coordinate restrictions. In the notation u=t₂,v=t₃,

    K₇=(u⁴,u²v,uv²,v³).

Its generator degrees are (8,7,8,9) and consecutive syzygy degrees (11,10,11). Thus

    0→O(−11)²⊕O(−10)→O(−8)²⊕O(−7)⊕O(−9)→O→O_T→0.

The weight-less-than-seven monomials are 1,u,u²,u³,v,uv,v². Hence the transverse length is 7, and degree(T)=7 degree(N)=42. The imported flatness argument makes T a Cohen–Macaulay surface thickening. Dualizing gives

    0→O(−5)→O(3)²⊕O(2)⊕O(4)→O(6)²⊕O(5)→ω_T→0.

The three obstruction restrictions H²(Y,B₀(r−5))→H²(T,B₀(r−5)|T) are injective; their Serre-dual detector maps

    H⁰(T,B₀(5−r)|T⊗ω_T) ↠ H²(Y,B₀(−r))

are surjective. Neither claim gives a canonical detector basis or evaluates a detector.

The natural upstairs order-eight quotient leads to downstairs K₅,K₆,K₇ for r=0,1,2. The common N₇ restriction concerns already-defined global coordinate classes, not an unjustified stronger chain quotient for r=0 or 1. This preserves the distinction explained in the original detector theorem.

## Relation to earlier files

The exact regularity result in PROOF.md remains valid. Its regularity-only order-ten source bound and the degree-sixty construction in DETECTOR-COROLLARY.md are weaker valid consequences; the tensor-monad argument above improves both. No claim concerning H²B₀(1) or H²B₀(2) is made.
