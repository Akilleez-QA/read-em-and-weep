# Structural models for the degree-six coefficient quotient

The [complete proof](PROOF.md) refines PR439's still-unevaluated quotient

    Q = H^1(B(6)) / [u H^1(B(4)) + v H^1(B(3))],

where B = End_0(F), F is normalized HM, and deg(u,v) = (2,3).

Two exact descriptions retain all incoming maps:

- With N = V(u,v), there is an exact sequence
  0 -> coker(T) -> Q -> H^1(N,B(6)|_N) -> 0.
  Here T: H^0(N,B(6)|_N) -> H^2(B(1)) is the composite of the
  restriction and Koszul connecting maps. Both surface H^1 vanishing
  and transgression surjectivity are required for Q = 0.
- With M = H^1_*(F) and bar M = M/(u,v)M, the section resolution gives
  35 bar M_2 -> 15 bar M_3 -> Q -> 0. The first arrow is induced by
  the linear block of the section-resolution differential.

Since dim M_3 = 2, this reduces to a quotient of fifteen copies of the
primary top-group quotient, but the incoming differential is essential. Vanishing of
bar M_3 suffices; nonvanishing of bar M_3 does not prove Q is nonzero.
The unknown H^2(B(1)) is retained, and no H^0(B(3)) vanishing is used.

Under PR439, the whole paired order-six ideal coefficient has dual
Q plus Q. Its vanishing remains unresolved. No actual source membership,
primitive, pure-square result, module lift, or algebraicity follows.
No selected HM multiplication or source instance was evaluated.

[Independent review](INDEPENDENT-REVIEW.md),
[second independent review](ROOT-REVIEW.md), and
[exact review bindings](REVIEW-BINDINGS.json) accompany the proof.
All public dependency pins and the bounded prior-work comparison are
recorded in the proof.
