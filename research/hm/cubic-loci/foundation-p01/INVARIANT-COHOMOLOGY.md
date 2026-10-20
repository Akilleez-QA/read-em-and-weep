# Independent structural proof of the deck-invariant Ext row

## Status

The deck-invariant Ext row is independently recovered as **(1,79,352,0,0)**. The proof combines the finite-pushforward splitting proved below with the classical HM endomorphism-cohomology proposition of Decker–Schreyer, now visually verified in its primary publication, and formal stability, duality, and Riemann–Roch arguments. In particular D, the invariant Ext¹ dimension 79, no longer depends on the historical finite-model rank certificate.

The [independent exact-presentation proof](../../hm-presentation-independent/PROOF.md) identifies the stipulated literal complex with the classical HM bundle H. This is the presentation input used here; no historical exactness certificate is assumed. The present proof imports the published classical cohomology theorem rather than claiming to re-prove that theorem from scratch.

No matrix, rank, polynomial instance, point, jet, or residual was evaluated. Only static document reads, primary-source literature lookup, and abstract cohomological reasoning were used.

## 1. The symmetric quotient

Work over the complex numbers. Let Y=(P¹)^4 and let σ:Y→Sym⁴(P¹)=P⁴ be the quotient map. It is finite of degree 4!=24. It is flat: Y is Cohen–Macaulay, P⁴ is regular, and this finite map has equidimensional zero-dimensional fibers, so miracle flatness applies. Thus B=σ_*O_Y is a vector bundle of rank 24.

Put L=O_Y(1,1,1,1). The universal effective-divisor description of the symmetric quotient gives σ*O_P⁴(1)=L. Projection formula and finiteness give

H^i(P⁴,B(n)) = H^i(Y,L^n).

For n≥0, each factor O_P¹(n) has cohomology only in degree zero. For n=−1 all factor cohomology vanishes. For n≤−2 each factor has cohomology only in degree one. Künneth therefore gives H^i(Y,L^n)=0 for every integer n and 1≤i≤3. Horrocks' splitting criterion implies B is a sum of line bundles.

There are no positive-twist summands: H⁰(B(−1))=0. Write B=⊕_{a≥0}O(−a)^{b_a}. For n≥0, h⁰(B(n))=(n+1)^4. Consequently

Σ_{n≥0}(n+1)^4 z^n = (Σ_a b_a z^a)/(1−z)^5.

The elementary generating-series identity on the left has numerator 1+11z+11z²+z³. Hence

σ_*O_Y ≅ O ⊕ O(−1)^11 ⊕ O(−2)^11 ⊕ O(−3).

This is an isomorphism of vector bundles. No algebra splitting or compatibility with multiplication is claimed or needed.

## 2. The deck-invariant Ext groups

Let q:X→Y be the product of the four elliptic double covers, let G=(Z/2)^4 be its deck group, and let E=(σq)*H⊗N. Fix the origin-divisor G-linearization of N and the canonical pullback linearization of (σq)*H. The invariants below use the resulting conjugation action on End E. Conjugation cancels the line-bundle twist equivariantly: End N is O_X with its ordinary deck action. Changing the linearization by a scalar character does not change this End action. Since (q_*O_X)^G=O_Y and taking G-invariants is exact in characteristic zero,

Ext^j_X(E,E)^G ≅ H^j(Y,σ*End H).

Finiteness, projection formula, and the preceding splitting give, for every j,

Ext^j_X(E,E)^G ≅ H^j(P⁴,End H)
 ⊕ H^j(P⁴,End H(−1))^11
 ⊕ H^j(P⁴,End H(−2))^11
 ⊕ H^j(P⁴,End H(−3)).

Thus the large historical invariant-character complex is unnecessary once these four classical cohomology groups are available. This is additive information only; it does not identify Yoneda multiplication under the noncanonical splitting.

## 3. Verified classical input

The unnumbered Proposition on printed p.218 of W. Decker and F.-O. Schreyer, “Pullbacks of the Horrocks–Mumford bundle”, Journal für die reine und angewandte Mathematik 382 (1987), 215–220, states:

(C) h¹(End H)=24, h¹(End H(−1))=5, and h¹(End H(t))=0 for every t≤−2.

The primary [GDZ page scan](https://gdz.sub.uni-goettingen.de/id/PPN243919689_0382?tify=%7B%22pages%22%3A%5B222%5D%2C%22view%22%3A%22info%22%7D) was visually checked, together with the complex-field and classical-HM normalization context on pp.215,217–219. The bundle is normalized by c₁=−1,c₂=4. Twisting normalization does not affect End H. See the accompanying [primary-source verification note](../../hm_primary_source_verification.md).

The published proof uses geometric and representation-theoretic arguments. The value 24 is attributed there to Decker's 1984 paper; the remaining twists are proved on pp.218–219. Importing this established proposition closes the cohomological dependency. This is distinct from executing or re-certifying any matrices from the historical Ext calculation.

Only twists down through −5 are needed for the complete invariant row; for D alone, the values at 0,−1,−2,−3 suffice.

## 4. Formal consequences: all four cohomology rows

The normalized HM bundle is stable with c₁=−1,c₂=4. Stability also follows directly from its classical monad: H⁰(H)=0, and a destabilizing rank-one saturated subsheaf has double dual O(d), d≥0. Its inclusion extends over codimension at least two to a nonzero map O(d)→H because H is locally free. This gives a nonzero section of H(−d); multiplying by a nonzero section of O(d) then contradicts H⁰(H)=0. Stability gives h⁰(End H)=1 and h⁰(End H(t))=0 for t<0.

The trace pairing makes End H self-dual. Serre duality on P⁴ therefore reads

h^j(End H(t)) = h^{4−j}(End H(−t−5)).

For t=0,−1,−2,−3 this gives h⁴=0 by stability; by the verified (C), it also gives h³=0.

From c₁(H)=−h,c₂(H)=4h², formally

ch(End H)=4−15h²+(75/4)h⁴.

Since td(P⁴) has degree-two coefficient 35h²/12 and degree-one coefficient 5h/2, Hirzebruch–Riemann–Roch gives

χ(End H(t)) = 4 binom(t+4,4) − (15/2)t² − (75/2)t −25.

At t=0,−1,−2,−3 these Euler characteristics are −21,5,20,20. Combining with (C), h⁰, h³ and h⁴ yields the following rows, in degrees 0 through 4:

- End H: (1,24,2,0,0)
- End H(−1): (0,5,10,0,0)
- End H(−2): (0,0,20,0,0)
- End H(−3): (0,0,20,0,0)

Weighting by (1,11,11,1) gives

(1,79,352,0,0).

This proves D and the full deck-invariant row independently of the historical finite Ext model. The ingredients are the classical presentation identification, the proved splitting, the verified published theorem (C), and formal duality/Riemann–Roch. No historical rank table has been replayed.

## 5. Characteristic-zero base change

The analytic/classical input above is used over C. The stipulated curve, quotient maps, literal presentation, and deck action are defined over Q, as is the averaging idempotent for G. The independent presentation identification is likewise defined over Q. Proper coherent cohomology commutes with extension of the ground field, and the invariant subspace is the image of that idempotent, whose formation also commutes with field extension. Consequently the invariant dimensions over C are the dimensions over Q. Extending Q to any characteristic-zero field k then gives the same row for the stipulated base-changed data. No embedding of k into C is required. This does not assert a positive-characteristic extension or a claim about arbitrary forms not identified with these stipulated data.

## 6. Limits

This proves additive cohomology dimensions for the specified deck action. It does not identify products under the noncanonical splitting, calculate a source-level obstruction, prove star-module admission, certify particular rational primitive identities, or establish the nontrivial deck-character rows. Previously proved structural bridge identities remain separate inputs and are neither weakened nor re-evaluated here.
