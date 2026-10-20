# A complete rank-one ternary surface: integral Chern constraints and a second discriminant

## Result and exact scope

Let B be a smooth projective integral complex surface. Assume the actual fixed trilinear family, repeated-input injectivity, and regular support extension of `/research/hm/middle-surface/rank-one-metric-radical-constraint/INTRINSIC_METRIC_EXTENSION.md`. Thus U⊂H⊂V⊗O_B have ranks 1,4 with dim V=5, E=H/U, and the intrinsic everywhere-nonzero metric h:Sym²E→M has generic rank one. It has rank one everywhere. Let R=rad(h), P its inverse image in H, and N=V/H. Write a=c1(U*), p=c1(det P*), n=c1(N), r=c1(R), and T=H/P=E/R.

The actual supported correction, including its regular extension through actual residual-rank drops, is required. No arbitrary assignment of pointwise corrections suffices.

Then:

1. In integral Chow groups,
   7p=9a+3n in CH¹(B), and 7c2(R)=a²+n² in CH²(B).
   Consequently 30(2a²−an+n²)=0 integrally, and 2a²−an+n²=0 in CH²(B)_Q. No torsion-free assertion for CH²(B) is needed or made.
2. R* is nef. There is a canonical morphism g:P_B(R)→Gr(3,V), with g*O(1)=O_{P(R)}(3). If a² has positive degree, then g is generically finite onto its three-dimensional image.
3. There is a canonical, everywhere-nonzero binary quadratic β:Sym²R→T⊗U. Its discriminant δ is a section of the line bundle (det R*)²⊗(T⊗U)², whose first Chern class d satisfies 7d=8a−2n integrally.
   Either δ is not identically zero, in which case its effective (possibly empty) zero divisor forces
       2A≤B₁≤4A,  0≤C≤2A,
   where A=deg a², B₁=deg an, C=deg n²;
   or β has rank one everywhere and defines an additional canonical flag S⊂R of ranks 1,2 satisfying
       3c1(S*)=p,   (R/S)²≅T⊗U.

4. If A>0, then a and n are numerically independent. In particular this excludes constant support, support class numerically proportional to the middle class, and smooth complete bases of Picard number one.

These are structural necessary conditions and specific exclusions, not an exclusion of every rank-one middle surface. In particular the second discriminant need not be generically nonzero. They do not apply a whole-surface equation to an isolated boundary curve of a higher-rank metric surface.

## 1. The nowhere-zero section and its surface Chern classes

Use π:Y=P_B(R)→B with the lines convention, L=O_Y(−1), ξ=c1(L*). The actual supported correction v_s:ker(h)→E⊗U has shear v_{s+d}(q)−v_s(q)=2q(d). On L²⊂ker(h), reduction modulo L eliminates the shear. Repeated-input injectivity supplies square avoidance, so the resulting section of

    F=(π*E/L)⊗π*U⊗L^(−2)

is nowhere zero. Therefore c2(F)=0 in integral CH²(Y).

Put e=c1(E), u=c1(U). On the surface base, the correct formulas are

    c2(π*E/L)=c2(E)+eξ+ξ²,
    c2(F)=c2(E)+ue+u²+(3e+5u)ξ+7ξ²,
    ξ²+rξ+c2(R)=0.

The integral projective-bundle decomposition CH²(Y)=π*CH²(B)⊕ξπ*CH¹(B) gives separately

    3e+5u−7r=0,
    c2(E)+ue+u²−7c2(R)=0.

The tautological flags give

    e=a−n, u=−a, r=a−p,
    c2(E)=a²−an+n²,
    c2(R)=a²−ap+p²−pn+n².

For the last formula, V/P has a filtration with line factors T,N, with c1(T)=p−n, so c2(P)=p²−pn+n²; divide c(P) by c(U).

Substitution yields exactly 7p=9a+3n and 7c2(R)=a²+n². Multiply the latter expanded relation by seven, then use 7p=9a+3n. The result is 30(2a²−an+n²)=0. Rational division by 30 is legitimate only after passing to rational Chow groups; taking degrees is legitimate integrally since Z has no torsion.

The determinant identity also holds as an equality in Pic(B): (det P*)^7≅(U*)^9⊗N³. As in the curve proof, if Q=(U*)³⊗N and Z=Q⊗(det P*)^(−2), then det P*≅Z³ and Q≅Z^7. These assertions do not discard Picard torsion.

## 2. A recovered three-plane makes R* nef

The nowhere-zero section above is equivalently a line subbundle

    K=L²⊗π*U^(−1) → π*E/L.

Let A₂⊂π*H be the inverse image of L under π*H→π*E. Since π*H/A₂≅π*E/L, let W be the inverse image of K under π*H→π*H/A₂. This defines a rank-three subbundle W⊂π*H⊂V⊗O_Y with successive line factors π*U,L,K. No splitting of either extension is asserted.

Thus det W=(π*U)⊗L⊗(L²⊗π*U^(−1))=L³. The Grassmannian morphism g determined by W satisfies g*O_Gr(1)=L^(−3). Hence ξ is nef. Equivalently, R* is nef, since Y parameterizes one-dimensional quotients of R* and L* is their tautological quotient line.

Pushforward of the projective-bundle relation gives

    π*(ξ³)=r²−c2(R)=−ap+pn−n².

In rational CH²(B), the first part therefore gives

    π*(ξ³)=(6an−9a²−4n²)/7=(3a²+2n²)/7.

Both a and n are nef: they are pulled back from P(V) and P(V*). If A>0, then deg ξ³>0. Since 3ξ=g*O(1), the image of g has dimension three, and g is generically finite onto that image. This proves the assertion without claiming any ampleness of ξ or nefness of arbitrary relative tangent bundles.

## 3. The induced binary quadratic and its discriminant

Restrict the correction to Sym²R, and project E⊗U onto T⊗U. Its shear lies in R⊗U, so this projection is independent of the splitting. It defines the canonical β.

At any point, β cannot vanish identically. Otherwise the entire restriction of the correction would be a quadratic map R→R⊗U. After trivializing U at that point, its eigenline obstruction is a section of Q(2) on P(R)=P¹, where Q is the rank-one quotient of R. This line bundle has degree three and every section has a zero. At such a zero the correction of r² belongs to Cr⊗U, contrary to square avoidance. Therefore β has rank either one or two at every point.

For a binary quadratic with value line D₀=T⊗U, its determinant is a section of (det R*)²⊗D₀². Its class is

    d=−2r+2(c1(T)+u)=4p−4a−2n,
    7d=8a−2n.

If δ is not identically zero, its zero scheme is an effective Cartier divisor (or empty), and nefness of a implies deg(ad)≥0. Thus B₁≤4A. The surface identity gives B₁=2A+C, and nefness gives C≥0, proving the displayed bounds. No positivity of a divisor on its own component is used.

If δ is identically zero, the everywhere-nonzero β has constant rank one. Its radical S is a line subbundle, and the induced nondegenerate line pairing gives (R/S)²≅D₀. On S² the correction lands in R⊗U. Its projection to (R/S)⊗U is splitting-independent and nowhere zero by square avoidance. It is consequently a line-bundle isomorphism

    S²≅(R/S)⊗U.

Taking first Chern classes gives 3c1(S)=r+u=−p, proving the extra flag identity. These two line identities are compatible with, and do not contradict, the earlier surface identities.

## 4. Numerical exclusions when the middle map has surface image

If the middle map B→P(V) has surface image, its hyperplane pullback has A>0. Suppose n=t a numerically, for a real scalar t. Taking degrees in the surface identity gives

    (t²−t+2)A=0.

The polynomial is (t−1/2)²+7/4>0 for every real t, a contradiction. Thus a and n must be numerically independent. This excludes Picard number one and constant H (which would give n=0), as well as any numerically proportional support polarization.

More explicitly, B₁=2A+C makes the intersection matrix on their span have determinant

    AC−B₁²=−(4A²+3AC+C²)<0,

where C≥0 by nefness. The span is therefore a nondegenerate two-dimensional subspace of signature (1,1), consistently with the Hodge index theorem. This is an exclusion of the proportional-class cases, not a contradiction in Picard number at least two. On a smooth resolution of a singular middle surface, the assertion concerns that smooth base and its pulled-back regular flags; it does not automatically bound the Picard number of a singular original model.

## Limits and audit targets

The proof retains regular H and actual supported-correction hypotheses. It supplies no automatic extension of H, no second-fundamental-form vanishing, and no exclusion by nefness alone. In particular 2A−B₁+C=0 is compatible with nonnegative intersection numbers. The new effective discriminant inequality is conditional on δ not being identically zero; the alternate rank-one binary branch is explicitly retained.

All calculations used abstract bundles and the fixed-family identities.  Independent audit should check the integral factor 30, the recovered W filtration and twist, and the distinction between the two binary-discriminant branches.
