# Moving beta sextics force negative discrepancy on a normal surface

## Statement and scope

Suppose a fixed beta degeneracy surface X=X_B is integral and normal, and contains a positive-dimensional algebraic family of distinct integral sextics D_t with arithmetic genus three. Assume B has rank one on a neighborhood of a general D=D_t, as supplied by the active beta branch. Then X is Gorenstein on that neighborhood and ω_X|D≅O_D(Z), of degree 25.

Let π:Y→X be a projective resolution, and let D~ be the strict transform of a general family member. For the exceptional curves meeting D~, write locally around π^{-1}(D)

K_Y=π* K_X+Σ a_i E_i.

Set ε=length(π_*O_{D~}/O_D) and n=(D~)^2. Then ε≥0, n≥0, and the exact identity is

−Σ a_i(E_i·D~)=21+2ε+n.

Consequently the total contribution from negative discrepancies is at least 21. In particular X cannot have only canonical singularities on a neighborhood of D. This argument does not assume that D itself is smooth or Gorenstein.

## Proof

A resolution exists in characteristic zero and can be chosen projective. Because X is normal, its singular locus is finite. The strict transform D~ is an integral curve not contained in an exceptional curve. Its intersection with each exceptional curve is finite, so π|D~ has finite fibers. This map is proper, quasi-finite, and birational onto D, hence finite birational.

The injection O_D→π_*O_{D~} has a finite-length cokernel T. Since the map is finite, χ(O_{D~})=χ(π_*O_{D~})=χ(O_D)+length T. Therefore

p_a(D~)=p_a(D)−ε=3−ε.

No normalization or smoothness of D~ is needed for this calculation. On the smooth surface Y, however, the integral curve D~ is Cartier and therefore satisfies ordinary arithmetic-genus adjunction.

After restricting to an irreducible positive-dimensional parameter family and shrinking its dense open, strict transforms form an algebraic flat family on Y. To see this, take the closure of the inverse-image family over the locus where π is an isomorphism, and apply generic flatness; the fibers over a dense open are exactly the strict transforms. Its distinct members are algebraically equivalent, hence numerically equivalent. Intersections of distinct effective integral curves on the smooth surface are sums of nonnegative local intersection multiplicities. Taking two distinct general members gives n=(D~)^2≥0.

Near D, K_X is Cartier and its restriction has degree 25. The projection formula and the birational degree-one map D~→D give (π*K_X)·D~=25. Adjunction on Y now yields

4−2ε = 2p_a(D~)−2
       = (D~)^2+K_Y·D~
       = n+25+Σ a_i(E_i·D~),

which is precisely the claimed identity.

Each E_i·D~ is nonnegative, since the curves are distinct. If all a_i≥0, the left side of the claimed identity is nonpositive while the right side is at least 21, a contradiction. More generally,

Σ_{a_i<0}(−a_i)(E_i·D~)
 =21+2ε+n+Σ_{a_i>0}a_i(E_i·D~)
 ≥21.

## Boundaries

Only discrepancies near D enter; exceptional curves over points away from D have intersection zero with D~. The canonical-singularity assumption, when used, is therefore needed only near the moving curves. The rank-one hypothesis supplies Cartier K_X near D, even if one does not assume globally Gorenstein X.

This proof must not be transferred unchanged to an individual component S of a reducible X_B. The restriction of ω_{X_B} to S includes gluing/conductor contributions and need not be ω_S; similarly, a nonnormal integral X has normalization-conductor corrections not covered by the displayed discrepancy formula. Those cases remain open. The result supplies an obstruction and a quantitative negative-discrepancy requirement, not a complete proof repair.
