# Checked outcome

The conditional obstruction survives every finite isogeny q:Y→X over C and every connected finite étale cover of X:

    Hom_Y(q*F,q*σ*F⊗M)=0 for all M∈Pic⁰(Y).

Proof: choose L∈Pic⁰(X) with q*L=M using the dual isogeny. The projection formula expresses this Hom as a direct sum of Hom_X(F,σ*F⊗L⊗T), where T ranges over the torsion kernel-character lines in q_*O_Y. All vanish by the imported all-Pic⁰ theorem, including a possible trivial L⊗T.

A projective isomorphism over Y gives a line twist M with M²=O_Y by the actual trivial determinants; torsion-free NS(Y) puts M in Pic⁰(Y), giving a contradiction. A projective lift covering τ is therefore impossible whenever q∘τ=σ∘q. Such a lift τ is not assumed to exist for every cover. The same q must be used on both sides.

No canonical correction occurs: this uses ordinary pullback–pushforward adjunction. Also ω_Y=q*ω_X=O_Y because the cover is étale. Choose an origin over 0 to make any connected finite étale cover an isogeny without translating X or F.

Primary references checked: Milne, Abelian Varieties, Theorem 11.1 (dual isogeny), Remark 15.3 (connected finite étale covers); Oda, Vector Bundles on an Elliptic Curve, Corollary 1.7, printed p.53 (structure-sheaf splitting in arbitrary dimension, including characteristic zero). Exact links and the full proof are in PROOF.md.

The inherited historical A premise and geometric identification remain necessary. Rational/meromorphic maps, arbitrary base changes and unrelated upstairs automorphisms are not covered. No physical source or jet values were evaluated.
