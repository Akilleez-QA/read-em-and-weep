# Independent audit: isolated globally realized cubic-scroll fiber

## Verdict

Accepted. COUNTERMODEL.md supplies one fixed abstract trilinear operation with all the claimed global injection, residual-rank, support, and fiber properties. This is a genuine global realization of the squarefree kernel/correction example, not merely a compatible local graph. It remains an abstract synthetic construction and makes no actual-source or equivariance claim.

The audit used tensor identities and incidence geometry only. No physical source instance, actual source operation, numerical rank experiment, or executable mathematical computation was used.

## 1. Exact compatible residual locus

The previously audited kernel is K=<xz,yz,xy,xw+y²,yw>, with no nonzero square and full support E. Its reduced rank-at-most-two locus is the union of the cubic scroll and P(y span{x,z,w}). The correction v(xy)=x, v(xw+y²)=y, with zero values on the other basis tensors, is the noncontraction parameter choice alpha=1 and all other parameters zero.

On the scroll, q=(sx+ty)(az+b(sy+tw)) has v(q)=bs(sx+ty), proving compatibility. On the plane, q=y(Ax+Bz+Cw) has v(q)=Ax. Modulo y, compatibility requires Ax to be proportional to Ax+Bz+Cw. This holds exactly when A=0 or B=C=0. Those loci are respectively P<yz,yw> and [xy], both already in the scroll. Thus the complete compatible rank-two locus is precisely the scroll as a reduced set. No additional component or isolated point outside it remains. The lack of a compatibility-scheme claim is appropriate.

## 2. Universal model and graph normalization

The alternating map V tensor exterior²V → exterior³V is surjective, so W has dimension 50-10=40. The formula f0(a,b,c)=a tensor (b wedge c)+c tensor (b wedge a) is outer symmetric and has cyclic sum zero. Its repeated-input map is a tensor (a wedge b).

For every nonzero a, splitting off Ca gives dim F_a=4+10=14 and the natural ten-dimensional residual quotient. The graph L is five-dimensional because its Sym²E component recovers q injectively. With symmetric products ab=(a tensor b+b tensor a)/2, its lower matrix block is exactly 2M(q), and its upper row is -v(q). Consequently its second-factor support is u wedge (im q+Cv(q)). All its nonzero tensors have rank at least two because K has no rank-one member.

The rank-one locus in P(W) is exactly the closed flag image [a tensor (a wedge b)]. Every such point lies in F_a. If a nonzero element of L lay in F_a with a not proportional to u, its support would contain two independent u wedge e_i lying in a wedge V. Wedge with a then forces a into both span(u,e_i), whose intersection is Cu. This proves L intersect F_a=0 for every other middle, with no unproved intersection formula.

## 3. One fixed quotient works simultaneously at every middle

In W/L of dimension 35, Gr(15,35) has dimension 300. Avoiding the nine-dimensional subspace F_u/L is a nonempty open condition. Over P(V) minus [u], the F_a images form a rank-fourteen subbundle because the original image map has constant rank fourteen and all intersections with L vanish.

The incidence of a middle a, a line h in its fourteen-plane, and a fifteen-plane M containing h has dimension

    4+13+14(34-14)=297.

Its image closure therefore has dimension at most 297, strictly below 300. Taking that closure is essential because the middle base is not proper; the proof does this correctly. The two nonempty opens intersect by irreducibility. Their inverse-image twenty-plane N satisfies N intersect F_u=L and N intersect F_a=0 at every other middle simultaneously.

Since every repeated-input rank-one tensor lies in some F_a, these same conditions ensure N avoids the entire flag variety. Hence the one fixed quotient f:V³→W/N preserves every repeated-input injection globally. No middle-dependent quotient is being substituted.

The exact residual formula rank Q_a=10-dim(N intersect F_a) gives rank five at u and rank ten at every other line. Projection of L identifies ker Q_u with the stated full-support K, and the graph relation gives the actual correction v with the claimed sign and normalization.

## 4. Exact ordered fiber and disjoint scrolls

Expanding the outer lifts gives A_u(v(q)+beta l+alpha n). Thus if v(q)=c l+d n, their unique ordered zero directions are [l-d u] and [n-c u]. Here this becomes

    ([sx+ty], [u], [az+b(s(y-u)+tw)]).

The fiber-weight transformations rescale each displayed outer vector by a nonzero scalar, so this is a globally well-defined morphism from the projective-bundle scroll. Neither outer vector vanishes. Their residual vectors remain independent because every scroll tensor has rank two.

The spaces X0=span{x,y} and Y0=span{z,y-u,w} have dimensions two and three and zero intersection: the u coefficient of a vector in their intersection first forces its y-u coefficient to vanish, and then the z,w coefficients vanish. Thus V=X0 direct-sum Y0. The displayed component and its outer interchange are disjoint, since a common ordered pair would require an outer line in both spaces.

Multiplying residual factors recovers q, giving a regular inverse to the displayed parametrization onto its image. Each component is therefore isomorphic to the smooth cubic scroll. Every compatible q is on that scroll and has exactly two distinct ordered factor lines, so the two images exhaust the independent-zero fiber. There is no monodromy joining the components and no rank-one branching point.

At other middle lines injectivity of Q_a prevents independent zeros. The total separately projectivized independent-zero locus consequently has dimension two and exactly these two reduced components. Restoring the three nonzero input scalings yields affine dimension five. No degree in a single projective embedding is inferred for these product-embedded surfaces.

## 5. Limits of the conclusion

The construction verifies global realization of one isolated full-support rank-five middle fiber with two scroll components. It does not produce a positive-dimensional rank-drop support, a seven-dimensional affine independent-zero component, an equivariant model, or an occurrence in the intended source operation. The classification scope of the separate PROOF.md remains unchanged.
