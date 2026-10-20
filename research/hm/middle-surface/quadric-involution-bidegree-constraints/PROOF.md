# Smooth-quadric kernel involutions: finite bidegree and base-point constraints

Work over C. Let E have dimension four and K⊂Sym²E have dimension five. Let W=K^⊥ have basis Q₁,…,Q₅, and let M(a) have rows Qᵢ(a,−). Assume an integral ordered-factor surface has both factor images equal to a **smooth** quadric Q⊂P(E), that M has rank three at general a∈Q, and that its unique kernel gives a birational involution τ:Q⇢Q. These hypotheses are established in `../nonplanar-factor-degree-bounds/PROOF.md` and its audit. No compatibility assumption is needed below.

Identify Q=P¹×P¹, with its embedding line bundle O(1,1). Write the two coordinate maps of τ as f,g:Q⇢P¹. Represent each pencil with its common divisorial factor removed. Write their divisor classes as

    f: (r,s),       g: (t,u).

All four integers are nonnegative. Base points can be proper or infinitely near.

## Theorem

The following necessary conditions hold:

1. u=r, r+s≤3, and r+t≤3.
2. Exactly one of the following numerical profiles occurs:
   - r=0, s=t=1;
   - r=1 and 0≤s,t≤2;
   - r=2 and s=t=1.
3. In the r=1 profiles, f has exactly 2s simple base points and g has exactly 2t simple base points. Exactly st of these are common, counting infinitely near points on a simultaneous resolution.
4. In the r=2 profile, both pencils have the same four simple base points.

Consequently τ can be resolved by blowing up at most four points, including infinitely near points. The profiles r=0,s=t=1 and r=1,s=t=0 are automorphisms of Q and extend to projective-linear automorphisms of P³. Under the compatible square-avoiding hypothesis of `../nonplanar-linear-correspondence-exclusion/PROOF.md`, these two profiles are already excluded. Nine numerical profiles remain; the result does not assert that each is realizable by a symmetric matrix M, or by a compatible K.

## 1. Cubic bound along each ruling

Choose a general line ℓ in either ruling. It is not contained in the rank-at-most-two locus of M|Q, so three rows of M restrict to a 3×4 matrix with generic rank three. Its signed 3×3 minors give a nonzero kernel vector whose entries are homogeneous cubics on ℓ≅P¹. At general points they also span the kernel of the whole 5×4 matrix, because that kernel has dimension one. After removing the common polynomial factor, they give τ|ℓ with degree at most three.

Each coordinate pencil f,g has a finite base locus on Q. Choose ℓ avoiding both base loci. Their product gives the Segre coordinates of τ with no base point on ℓ. Thus the pullback of O_Q(1,1) has degree r+t on one ruling and s+u on the other. Both numbers are at most three.

This uses the degree of the pullback line bundle, so does not confuse the degree of an image curve with the degree of a parametrization.

## 2. Symmetry of the graph

Let Γ⊂Q×Q be the graph closure. The involution property says Γ is invariant under exchanging its two Q factors. Write A and B for the divisor classes O(1,0), O(0,1) on Q. Thus A²=B²=0 and A·B=1.

On any smooth simultaneous graph resolution p,q:S→Q, the strict pullbacks of the target pencils have classes

    F=q* A = rA+sB−Σ aᵢEᵢ,
    G=q* B = tA+uB−Σ bᵢEᵢ,

where on the right A,B denote p-pullbacks, Eᵢ are the total-transform exceptional basis for successive point blowups, and aᵢ,bᵢ are nonnegative integers. Graph symmetry identifies the two mixed intersection numbers

    p*A · q*B = p*B · q*A.

They equal u and r, respectively, so u=r. Section 1 now gives r+t≤3 and r+s≤3.

## 3. Birational pencil identities

Resolve both pencils by point blowups so that q=(f,g):S→Q is a birational morphism. Extra blowups, if any, can be assigned zero multiplicity. A general fiber of either target projection pulls back to a smooth rational curve. Its self-intersection is zero, and adjunction gives canonical intersection −2. Also F·G=1 since q is birational. In the total-transform exceptional basis, Eᵢ·Eⱼ=−δᵢⱼ and K_S=−2A−2B+ΣEᵢ. Hence

    Σaᵢ² = 2rs,       Σaᵢ = 2(r+s)−2,
    Σbᵢ² = 2tr,       Σbᵢ = 2(t+r)−2,
    Σaᵢbᵢ = r²+st−1.                         (*)

These are identities of nonnegative integers, including infinitely near multiplicities. No general-position assumption about base points is made.

## 4. Exhausting the integer profiles

If r=0, the first two square-sum equations give aᵢ=bᵢ=0. The linear-sum equations then give s=t=1. This is an automorphism exchanging the rulings.

If r≥1, the cubic bounds imply r≤3 and 0≤s,t≤3−r. Whenever s=0, the first square-sum equation makes every aᵢ zero; its linear-sum equation then forces r=1. Likewise t=0 forces r=1. Thus r=3 is impossible, and r=2 requires s=t=1. The remaining possibility is r=1, 0≤s,t≤2.

For r=1, equations (*) give Σaᵢ²=Σaᵢ=2s. Every integer aᵢ is therefore zero or one, and precisely 2s are one. Similarly precisely 2t values bᵢ are one. The mixed equation gives Σaᵢbᵢ=st, exactly the number of common base points. The union has

    N=2s+2t−st≤4

for 0≤s,t≤2. This includes N=0 for s=t=0, where both coordinate maps are independent degree-one P¹ automorphisms and τ is an automorphism of Q.

For r=2,s=t=1, each of the square and linear sums is four. Both pencils have four simple base points. Their mixed sum is also four, so their base-point sets coincide.

Blowing up the union of the two pencil base-point clusters resolves both pencils, and hence τ. The counts include all required successive infinitely near points; they are not just counts of distinct points on the original Q. This proves the four-blowup bound.

Finally an automorphism of Q preserves O(1,1), hence acts on its four-dimensional complete space of sections and extends to an ambient projectivity. The previously audited linear-correspondence exclusion therefore applies to the two automorphism profiles when its compatibility and square-avoidance hypotheses are imposed.

## 5. Scope and next bounded target

This is a new finite numerical reduction for the **smooth** quadric case. It does not treat a quadric cone. It neither assumes nor proves that the nonlinear profiles extend to ambient projectivities. It does not eliminate them. The remaining profiles are the eight pairs (s,t)∈{0,1,2}² other than (0,0), with r=1, and the single r=2,s=t=1 profile.

A concrete next step is to impose the five symmetric (1,1) ambient graph equations on these at-most-four-point models, or apply compatibility at their diagonal points. The numerical constraints above use only a rank-three linear matrix along ruling lines and graph symmetry, so additional symmetry of each Qᵢ has not yet been exhausted.

 

## 6. Additional exclusion: no ruling can be preserved pointwise on its base

There is a further pure-span obstruction. The nontrivial involution τ cannot satisfy pr₁∘τ=pr₁, and cannot satisfy pr₂∘τ=pr₂. Here equality means equality of rational maps, not merely preservation of the ruling family with a nontrivial automorphism of its base.

To prove this, suppose the first equality holds. Write E=U⊗V and a=u⊗v on the Segre quadric. On a general fiber u, τ acts by a nontrivial involutive projectivity T_u of P(V): birationality and the involution identity hold over C(P(U)). The restriction is nontrivial, since otherwise τ would be the identity generically, contrary to the generically rank-two product hypothesis. After a scalar normalization at each general u, T_u has two opposite eigenvalues. Consequently the products vT_u(v) span a two-dimensional subspace H_u⊂Sym²V.

The symmetric products aτ(a) lie in the nine-dimensional summand

    D=Sym²U⊗Sym²V ⊂ Sym²(U⊗V),

and their span J has dimension at most five. Its annihilator J^⊥⊂D* has dimension at least four. Each h∈J^⊥ is a row of three homogeneous quadratic polynomials in u, obtained by evaluating its Sym²U* factor at u². The rows for linearly independent h are linearly independent over C. For every general u each row annihilates H_u, so all these rows have rank at most one over C(u).

We claim any vector space R of such degree-two rows with generic rank one has dimension at most three. Choose a primitive polynomial row w (the gcd of its nonzero entries is one) generating their common one-dimensional span over C(u). The UFD property of C[u₀,u₁] shows that each polynomial row in this span is p·w with polynomial p: every denominator in a reduced rational multiplier would have to divide every entry of w. Take w homogeneous of degree d≥0. For a homogeneous degree-two row, p then has degree 2−d. Thus dim R≤dim C[u₀,u₁]_(2−d)≤3. This contradicts dim J^⊥≥4.

The other ruling is identical. In particular, in a profile r=1,s=0, the degree-one induced map on the first ruling base must be a nonidentity involution; in a profile r=1,t=0, the analogous induced map on the second ruling base must be nonidentity. This assertion does not eliminate those numerical profiles: a nontrivial involution of the ruling base remains possible.

## 7. Conditional compatibility obstruction at a regular fixed point

Suppose v:K→E satisfies dense compatibility and square avoidance as in the audited linear-correspondence exclusion. If e∈Q is fixed by τ and τ is regular near e, then

    rank(dτ_e−I)≤1.

Indeed choose local vector lifts a(x), b(x) of x and τ(x), with a(e)=b(e)=e. Dense compatibility gives the identically vanishing local wedge v(a b)∧a∧b. Differentiating at e gives

    v(e²)∧e∧(db−da)=0.

Modulo Ce the image of db−da is the image of dτ_e−I, up to the harmless common lift normalization. If this image has dimension two, the two corresponding planes through Ce intersect only in Ce, forcing v(e²)∈Ce, a contradiction. Products ab lie in K throughout this neighborhood by closedness of membership.

Because τ²=I as rational maps and τ is regular at its fixed point, shrink the neighborhood so that the identity holds there. The derivative is an involution. If the fixed point is isolated, its +1 eigenspace is zero: locally a finite-order action in characteristic zero is linearizable, directly by averaging local coordinates against its linear derivative. Thus dτ_e=−I and the rank is two. Therefore a regular isolated fixed point on the original smooth Q is forbidden.

No assertion is made that an isolated fixed point on a resolution descends to such a point on Q. It can lie over a base point or an exceptional curve; those cases require separate analysis. No existence claim for a regular isolated fixed point in the nine nonlinear profiles has been established here.
