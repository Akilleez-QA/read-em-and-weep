# Independent audit: universal residual-rank-one surface exclusion

## Verdict

The proof in PROOF.md is valid. Under the stated fixed outer-symmetric, cyclic-zero operation on a five-dimensional V, with repeated-input injectivity at every middle, the reduced residual-rank-one locus D1 is projective of dimension at most one. The argument imposes no condition on the quadratic-form rank of its line-valued metric, no symmetry-group assumption, and no defect budget. The curve identity and determinant degree are also correct. This audit checked the actual construction in /research/hm/middle-surface/low-metric-rank-middle-exclusion/PROOF.md, Sections 1–2, as well as the complete present draft.

## 1. Base locus and weights

The repeated-input injection is U² tensor E → J tensor O, so the residual middle map has domain U tensor Sym²E. On the reduced rank-at-most-one locus, rank zero is absent and constant rank one gives a genuine image line subbundle T. Therefore M=T tensor U* is the correct value line for h:Sym²E→M.

A local splitting of V tensor O→E gives, by inverting the repeated-input injection on its image, a map K→E tensor U, with K=ker h. The twist is U, not U*. A splitting change d:E→U changes a square correction by 2d(e)e, in the line of e tensored with U. This is an algebraic identity of bundle maps, not merely an equality at geometric points.

Rank-zero exclusion is internally justified by the nowhere-zero-section contradiction on P³: the correction would define a nowhere-zero section of (E/O(-1)) tensor O(2), whose third Chern class is 15H³. The repeated-pencil identity used to establish square avoidance follows from precisely the stated symmetry and cyclic identities. Thus D1 really is closed projective, rather than a potentially nonproper rank-one stratum with missing rank-zero boundary.

## 2. Singular and nonreduced quadrics cause no gap

After pullback to a smooth projective integral curve or surface B, P=P_B(E) is smooth integral. The nonzero section h|L² of L^(-2) tensor M cuts out an effective Cartier divisor Z, with class 2ξ+m. This remains true when the entire generic quadric is a double hyperplane; a nonzero section on an integral ambient scheme is a nonzerodivisor locally.

On the scheme-theoretic Z the composite L²→Sym²E→M is zero, so L² factors through the locally free K exactly. Composing the actual correction with E→E/L gives sections of F_Z=((E/L) tensor U tensor L^(-2))|Z. The splitting-change identity makes these sections equal on overlaps over the full scheme Z. It is essential here to retain Z with its Cartier multiplicities, which the draft does.

Square avoidance says the section is nonzero in every closed-point fiber. In a local trivialization at such a point one coordinate is a unit, so the section defines a split injection O_Z→F_Z with locally free rank-two quotient. This argument is valid over nonreduced rings. The possible degeneracy locus is closed and has no closed points, so it is empty. Consequently c3(F_Z)=0 as an operational class, and c3(F_Z) cap [Z]=0.

Projection formula for the Cartier immersion therefore yields (2ξ+m)c3(F)=0 in CH⁴(P). Smoothness of Z is unnecessary. Smoothness of P identifies this cycle relation with a Chow-ring relation, permitting multiplication by ξ.

## 3. Independent Chern and pushforward check

The exact sequence 0→U→V tensor O→E→0 gives c1(E)=a and c2(E)=a². Write t=2ξ−a. For the rank-three quotient E/L its first three Chern classes, on a base of dimension at most two, are

- a+ξ;
- a²+aξ+ξ²;
- a²ξ+aξ²+ξ³.

Thus c3(F)=c3(E/L)+t c2(E/L)+t² c1(E/L)+t³ equals

    15ξ³−10aξ²+5a²ξ.

For the lines convention the relation has positive Chern coefficients: ξ⁴+c1(E)ξ³+c2(E)ξ²+⋯=0. Consequently

    π_*ξ³=1,  π_*ξ⁴=−a,  π_*ξ⁵=a²−c2(E)=0.

Expansion and the first pushforward give 15m−50a=0 in CH¹(B). On a surface the expansion is

    30ξ⁴+(15m−20a)ξ³+(10a²−10am)ξ²=0.

Multiplying by ξ and pushing gives 30a²−25am=0 in CH²(B). Three times this latter identity plus five times a times the former gives −160a²=0. No division or torsion cancellation is involved.

For a smooth projective surface with two-dimensional middle image, deg(a²) is its positive generic degree over the image times the positive projective degree of that image. This contradicts 160a²=0. An integral projective surface in D1, followed by projective resolution, supplies exactly this setup if dim D1≥2. Pullback preserves all the locally split exact sequences and the correction identities. The universal dimension conclusion follows.

## 4. Curve assertions

On a smooth projective curve the exact Picard relation is 15m=50a. Equivalently (M³ tensor (U*)^(-10))^5 is trivial. Dividing by five in Picard is not justified without a torsion argument, and the draft correctly avoids doing so.

After taking degrees, 3 deg M=10 deg U*. A nonconstant middle map has positive deg U*, giving deg U*=3k and deg M=10k for a positive integer k.

The metric determinant lies in (det E*)² tensor M⁴ and has class 4m−2a. When the generic metric rank is four, its nonzero section has an effective divisor of degree 34k=(34/3)deg U*. This divisor is nonempty. The statement counts multiplicities and does not force a rank-at-most-two point. When generic metric rank is at most three, the determinant is identically zero and no such determinant-divisor claim follows.

## 5. Scope

Together with the separately proved rank-one fiber bound of three, dim D1≤1 gives separately projectivized independent-zero dimension at most four over D1 and all-inputs-nonzero affine dimension at most seven. Claims involving higher residual ranks still require their separate fiber/support hypotheses. The proof excludes projective residual-rank-one surfaces, not residual-rank-one curves or isolated points.

This was a symbolic bundle/Chow and local algebra audit only.
