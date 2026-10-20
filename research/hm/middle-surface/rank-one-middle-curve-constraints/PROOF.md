# Universal residual-rank-one surface exclusion and curve constraints

## Conclusions

Work over C with the fixed outer-symmetric, cyclic-zero operation and repeated injectivity hypotheses of `/research/hm/middle-surface/low-metric-rank-middle-exclusion/PROOF.md`. Retain its globally defined residual-rank-one locus D1, bundles U, E=(V tensor O)/U of rank four, everywhere surjective h:Sym²E→M, and actual local corrections ker(h)→E tensor U.

**Primary theorem: dim D1≤1.** No smooth projective surface mapping to D1 can have two-dimensional middle image, without any restriction on metric rank. For every such surface S, the universal quadric and its actual square-avoidance correction give the integral identities

    15m−50a=0 in CH¹(S),
    30a²−25am=0 in CH²(S),
    160a²=0 in CH²(S),

where a=c1(U*) and m=c1(M). The last identity contradicts a surface image. Resolving a surface in D1 proves the theorem. This strengthens the earlier exclusion restricted to metric rank at most two.

**Curve constraints.** For every smooth projective integral curve B→D1, the same construction gives an **integral** relation

    15m−50a=0 in CH¹(B)=Pic(B).

Therefore 3 deg(M)=10 deg(U*). For a nonconstant middle map, deg(U*)=3k and deg(M)=10k for an integer k>0. The Picard relation cannot be divided by five without controlling torsion. If that curve has generic metric rank four, its metric determinant vanishes along an effective nonempty divisor of degree 34k. Thus rank at most three is unavoidable somewhere on every such curve. Multiplicities count; this does not assert 34k distinct points.

## 1. Imported construction and its exact scope

The source proof establishes, directly from repeated injectivity:

- Residual rank zero is impossible, so the reduced locus D1=(rank Q≤1)_red is closed and projective.
- On D1, h:Sym²E→M is everywhere surjective, with locally free kernel K of rank nine.
- A local splitting E→V tensor O gives an actual correction v_s:K→E tensor U. For a change of splitting d:E→U, the difference on a square e² is 2d(e)e, which lies in Ce tensor U.
- Whenever h(e²)=0 and e is nonzero, v_s(e²) does not lie in Ce tensor U. Otherwise the repeated-pencil argument contradicts repeated injectivity.
- These statements and bundle maps commute with pullback.

The argument below uses those actual corrections, not an arbitrary correction independently chosen at each fiber. No extension across rank-zero points is needed, since there are no such points.

## 2. Universal quadric and global section, including singular fibers

Let B be smooth projective and integral of dimension one or two, with a map to D1. Suppress pullbacks. Set

    π:P=P_B(E)→B,   L=O_P(−1),   ξ=c1(L*).

Here P parameterizes lines. The quadratic h restricts to a section of L^(−2) tensor π*M. Let Z be its scheme-theoretic zero locus. Thus

    [Z]=2ξ+m.

Since h is nonzero at every base point, no fiber is the whole projective space. The total space P is smooth and integral and the defining section is nonzero, so Z is an effective Cartier divisor. This remains valid for singular rank-three quadric fibers, reducible rank-two fibers, and nonreduced rank-one double-hyperplane fibers. The construction does not replace Z by its reduction.

On Z, the scheme-theoretic identity h(L²)=0 factors L²→Sym²E through K. Composing the actual correction with E→E/L gives local sections of

    F_Z=((π*E/L) tensor π*U tensor L^(−2))|Z.

The correction's splitting-change term lands in L tensor U, hence vanishes in E/L. The local sections therefore glue on the whole scheme Z, not only on its reduced support.

Square avoidance makes this section nonzero in every closed-point fiber. It consequently defines a locally split injection O_Z→F_Z: around each point at least one section coordinate is a unit, so its cokernel is locally free of rank two. This argument works over nonreduced local rings. Accordingly c3(F_Z)=0 as an operational Chern class, and in particular

    c3(F_Z) cap [Z]=0.

The rank-three bundle itself extends to all of P:

    F=(π*E/L) tensor π*U tensor L^(−2).

For the Cartier immersion i:Z→P, the projection formula gives the integral Chow relation

    (2ξ+m)c3(F)=i_*(c3(F_Z) cap [Z])=0 in CH⁴(P).

Because P is smooth, its Chow groups form an intersection ring, and this relation may also be multiplied by ξ. Smoothness, reducedness, or irreducibility of Z is never assumed.

## 3. Chern signs and formulas

Write a=c1(U*). The exact sequence 0→U→V tensor O→E→0 gives c(E)=(1−a)^(−1). On bases of dimension at most two, c1(E)=a, c2(E)=a², and base classes of higher codimension vanish.

With Q'=π*E/L and c1(L)=−ξ,

    c1(Q')=a+ξ,
    c2(Q')=a²+aξ+ξ²,
    c3(Q')=a²ξ+aξ²+ξ³.

The twisting line has t=c1(U tensor L^(−2))=2ξ−a. The rank-three twisting formula gives

    c3(F)=c3(Q')+t c2(Q')+t² c1(Q')+t³
         =15ξ³−10aξ²+5a²ξ.

On a curve, the last term vanishes. This verifies the sign of the U twist as well as the sign of the quotient bundle contribution.

The lines-convention projective-bundle relation is

    ξ⁴+c1(E)ξ³+c2(E)ξ²+c3(E)ξ+c4(E)=0.

In particular π_*ξ³=1, π_*ξ⁴=−a, and on a surface

    π_*ξ⁵=c1(E)²−c2(E)=0.

The minus sign in π_*ξ⁴ is essential.

## 4. Curve computation and determinant boundary

On a curve, a²=am=m²=0, and

    (2ξ+m)c3(F)=30ξ⁴+(15m−20a)ξ³.

Its pushforward to B is 15m−50a, proving the integral Picard identity. Taking degrees and dividing integers gives

    3 deg(M)=10 deg(U*).

If B→D1⊂P(V) is nonconstant, U* is the pullback of O_{P(V)}(1), with strictly positive degree. Coprimality of three and ten gives the asserted k>0. The integral identity says that the line bundle M³ tensor (U*)^(−10) has fifth power trivial; it need not itself be trivial.

The symmetric map h defines E→E* tensor M. Its determinant is a section of

    (det E*)² tensor M⁴,

of first Chern class 4m−2a. If the generic metric rank is four, this section is not identically zero, and its effective zero divisor is exactly the determinantal rank-at-most-three locus, with its divisor multiplicities. Its degree is

    4 deg(M)−2 deg(U*)=40k−6k=34k>0.

If the generic metric rank is at most three, the determinant section is identically zero and this divisor assertion is not applicable. The curve calculation does not exclude such curves, nor does it force a rank-at-most-two point.

## 5. Stronger surface computation

Now let B=S be a smooth projective integral surface. Expanding the same vanishing relation yields

    0=(2ξ+m)c3(F)
     =30ξ⁴+(15m−20a)ξ³+(10a²−10am)ξ²,

where the omitted term 5a²mξ vanishes because its base codimension is three.

Pushing directly to S gives

    15m−50a=0 in CH¹(S).

Multiplying by ξ before pushing and using π_*ξ⁵=0 gives

    (15m−20a)(−a)+(10a²−10am)=0,

hence

    30a²−25am=0 in CH²(S).

Multiply this last identity by three and the first identity times a by five. Adding them gives

    −160a²=0.

This elimination is integral throughout. It uses no cancellation of torsion classes.

If S→D1 has two-dimensional middle image, the pullback a of the hyperplane class has positive self-intersection: for its integral image T, the projection formula gives deg_S(a²)=d deg_T(O(1)²)>0, where d is the positive generic degree S→T. This contradicts 160a²=0.

If dim D1≥2, choose a reduced integral projective surface T⊂D1 (using hyperplane sections if necessary) and a smooth projective resolution S→T. Pullback preserves the global h and the local actual correction construction. The preceding contradiction applies. Therefore dim D1≤1.

## 6. Consequences and limits

This excludes every residual-rank-one projective middle surface, including those of generic metric rank three or four. It does not exclude projective residual-rank-one curves. Such curves obey the degree constraint above, and generic rank-four curves must meet their rank-at-most-three boundary.

Using the separately imported residual-rank-one independent-zero fiber bound of three in the separately projectivized variables, the locus over D1 has separately projectivized dimension at most four, hence affine dimension at most seven after restoring the three nonzero input scales. Any broader dimension conclusion involving higher residual ranks still depends on the relevant imported bounds and hypotheses; they are not proved here.


## 7. Dimension-seven corollary under the separate middle-support hypothesis

Assume additionally

    (H) dim{[u] in P(V): rank Q_u<10}≤2.

Use the following established pointwise bounds for separately projectivized independent-zero fibers:

- Residual rank one: dimension at most three, from `/research/hm/universal-polar/rank-one-residual-fiber-model/PROOF.md`, Section 1.
- Residual rank two: dimension at most two, from `/research/hm/universal-polar/diagonal-hartogs-fiber-bound/UNSQUARED_PENCIL.md`, Section 5.
- Residual rank three: dimension at most two, from `/research/hm/universal-polar/diagonal-hartogs-fiber-bound/PROOF.md`.
- Residual rank four: dimension at most two, from `/research/hm/universal-polar/rank-four-compatible-fiber-bound/PROOF.md`.
- Residual rank five: dimension at most two, combining full and ternary support as recorded in `/research/hm/universal-polar/full-support-rank-five-dimension-bound/PROOF.md`, including Section 6.

The rank-one middle base now has dimension at most one, so its projective incidence has dimension at most four. For ranks two through five, (H) and the pointwise bound give projective incidence dimension at most 2+2=4. The integrated higher-rank result `/research/hm/middle-surface/rank-six-surface-reduction/COROLLARY.md` bounds ranks at least six by affine dimension at most six and excludes independent zeros at rank ten. Restoring the three nonzero input scales in the lower-rank strata gives

    dim{independent zero triples}≤7.

Only the operation axioms, repeated injectivity, (H), and the listed pointwise/higher-rank imports enter this corollary. No full-normalizer hypothesis or separate degree-70 defect assertion is required.

For completeness, the locus of **all-three-nonzero** zero triples has dimension exactly seven. Indeed, its dependent part is precisely the triples with all three projective input lines equal, as proved in `/research/hm/universal-polar/full-support-rank-five-dimension-bound/PROOF.md`, Section 1. These are parametrized by P⁴ and three nonzero scalings, and hence have dimension seven. They are zeros because cyclic zero in characteristic zero gives f(v,v,v)=0. The independent part has dimension at most seven by the preceding argument.

This exact statement excludes triples with any zero input. Each zero-input coordinate piece in V³ has dimension ten, so the unrestricted affine zero locus cannot have dimension seven.

## 8. Optional full-normalizer curve consequence

This section assumes the additional projective Heisenberg-normalizer setting of `/research/hm/rank-four/normalizer-small-curve-exclusion/PROOF.md`: H=H5/Z(H5)≅F5² is normal in N, N/H≅SL2(F5) with its standard conjugation action, V is the Schrödinger representation, and D1 is N-stable. These extra assumptions are not used in the universal theorem or Section 7.

For every integral curve component C of D1, its smooth normalization maps birationally to C. Therefore deg(U*) on that normalization is exactly the embedded degree deg(C). Section 4 proves that **each component degree is divisible by three**.

Let C_total be the reduced union of all one-dimensional components, if any. Its degree is also divisible by five. One way to verify this familiar Heisenberg divisibility directly is to use its H5-linearized Hilbert polynomial. For all sufficiently large n, H⁰(C_total,O(n)) has dimension d n+χ, where d=deg(C_total). For n not divisible by five, its central character is nontrivial, so the dimension is divisible by five: in any representation with nontrivial central character, a pair of Heisenberg generators cyclically permutes five equally sized eigenspaces. Choose large successive integers n=5t+1 and n+1=5t+2. Their Hilbert polynomial values are both divisible by five, and subtracting shows 5 divides d.

Thus d is a positive multiple of fifteen. The imported small-cycle theorem excludes d=15, since it excludes every nonzero N-invariant effective curve cycle of degree at most twenty. Its separately audited `/research/hm/rank-four/normalizer-small-curve-exclusion/ADDENDUM_DEGREE_30.md` excludes d=30. Consequently, if D1 has a curve component, then

    deg(C_total)≥45.

This is a lower bound for the total reduced curve degree. It is not an upper bound, does not prove existence of such curves, and does not address isolated points of D1.
