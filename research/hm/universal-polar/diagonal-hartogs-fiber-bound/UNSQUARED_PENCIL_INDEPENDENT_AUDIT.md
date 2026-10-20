# Prior mathematical audit

This audit concerns the source manuscript. It is not a formal verification or a review of later normalized publication bytes.

# Independent audit: universal K8 compatible-fiber bound

## Verdict

**PASS.** I independently checked `UNSQUARED_PENCIL.md`, together with the diagonal–Hartogs and hyperplane lemmas in `PROOF.md`, the squared-factor branch in `COROLLARIES.md`, and its finite-partner-plane dependency in `../rank-three-compatible-fiber-structure/PROOF.md`, Sections 1–2. The last common-factor branch is valid. All eight-dimensional kernels in Sym²E, dim E=4 over C, with a square-avoiding linear correction have ordered distinct compatible locus of dimension at most two. No genericity assumption is needed.

I also checked the reconstruction and the statement of (H) against `../full-support-rank-five-dimension-bound/PROOF.md`. The new residual-rank-two affine dimension bound seven follows under (H). The asserted aggregate frontier at generic residual rank at most one uses the previously established bounds for the other residual ranks as explicit dependencies.

## 1. Closure and the projected wedge identity

For W=span(zx,zy), with z,x,y independent, the product equations are exactly z(a)ρ(b)+z(b)ρ(a)=0, where ρ=(x,y). Away from P(A)×P(A), A=ker z, one coefficient is nonzero. Thus ρ(a) and ρ(b) are linearly dependent, including the cases where a projected vector vanishes. An integral Z not contained in P(A)×P(A) meets this open densely. The polynomial wedge identity extends to all Z.

Generic compatibility then implies ρ(v(ab))∧ρ(a)=0. This identity has bidegree (2,1), and is genuinely regular on the incidence: extending v linearly to Sym²E gives polynomial representatives, independent of that extension upon restriction. It extends by density to every diagonal point of Z. At a point with ρ(a)=0 it remains an identity, rather than an undefined projective proportionality assertion. No division by x(a) or y(a) occurs in this passage.

## 2. Hartogs and the plane diagonal

The diagonal–Hartogs lemma has the needed hypotheses. Normalization of an integral complex projective threefold is finite; a diagonal intersection of dimension at most one therefore pulls back to codimension at least two. Off the diagonal the tautological rank-two map is a subbundle map, so the two compatibility coefficients are regular sections of the appropriate invertible sheaves. Normality extends those sections across the removed set. Their identity extends by density.

Nonempty diagonal intersection follows from the positive diagonal intersection number: every mixed degree on an effective threefold in P³×P³ is nonnegative, and the ample cubic (h1+h2)³ has positive degree. The diagonal class is the sum of the four degree-three mixed monomials, hence its intersection with Z is positive. Disjointness would force that intersection product to vanish, even without a proper-intersection assumption.

Thus a hypothetical Z must meet the diagonal in dimension at least two. The square support is exactly P(A)∪P(R), with dim P(A)=2 and dim P(R)=1. A closed subset of this union of dimension at least two contains the whole irreducible P(A). Consequently every plane-diagonal point is legitimately available for the restricted wedge identity. Nonreduced structures are irrelevant to this reduced-support argument.

The exclusion of Z contained in P(A)×P(A) also checks: the nonzero normal component of v(a²) restricts its actual diagonal intersection to a curve, so Hartogs applies; if that component vanishes identically, polarization gives a quadratic map A→A and the quotient-bundle Chern number c2(Q_A(2))=7 forces an eigenline. Both alternatives contradict square avoidance.

## 3. Divisibility and common zero

Independence of z,x,y guarantees that x and y restrict to independent linear forms on A. Complete them by w. The identity yF−xG=0 in C[x,y,w] implies x divides F and y divides G, and more precisely F=xℓ, G=yℓ for the same homogeneous linear form ℓ. The zero-polynomial cases are included.

Hence H(a)=v(a²)−ℓ(a)a is an R-valued homogeneous quadratic map on A. R has vector dimension two; A has vector dimension three. Two coordinate quadrics H1,H2 therefore have a nonzero common zero over C. The stated height-theorem proof is valid: the homogeneous ideal they generate is proper and has height at most two, whereas a zero set consisting only of the affine origin would have radical the height-three maximal ideal. This also covers identically zero, dependent, or reducible quadrics. At that nonzero zero e, e²∈K and v(e²)=ℓ(e)e, including possible ℓ(e)=0, contradicting square avoidance.

## 4. Exhaustion of pencils and the other branch

Two independent quadrics can have no common factor, or a common linear factor. A degree-two common factor would make them proportional. In the linear-factor case W=zL, dim L=2, the alternatives z∈L and z∉L are exhaustive; the latter is exactly the independent z,x,y normal form. A coprime pencil has no surface in its common zero support, since a surface in P³ supplies a common irreducible hypersurface factor. Its square locus has dimension at most one, so Hartogs handles it.

For z∈L, the product incidence is P(A)×P(A) union the two products with the line P(R), R=ker z∩ker x. The finite-partner-plane lemma used here is valid for arbitrary K: its parameter space is projective and closed, while square avoidance makes it disjoint from the ample incidence divisor a∈U. Thus it has finite support. Fixed-factor fibers have dimension at most two, with every surface fiber containing a compatible plane; outside finitely many factor points they have dimension at most one. Over P(R), the ordinary fibers contribute at most 1+1=2 dimensions and the finitely many exceptional fibers contribute at most two. This excludes threefolds in either remaining product component.

Taking general ample sections of any larger-dimensional integral compatible closure yields an integral threefold still meeting its compatible open. Therefore the threefold exclusion really gives a dimension-two bound on the whole locus.

## 5. Global bound and limits

For residual rank two, dim K_u=8. The existing reconstruction is an algebraic identification of the compatible ordered residual locus with the separately projectivized independent-zero fiber, with no extra lifting parameter. Under (H), the middle stratum has dimension at most two. Fiber dimension at most two gives total projective dimension at most four, and the three nonzero input scales give affine dimension at most seven.

For an irreducible component generically of rank two, its dense rank-two part already has its full dimension. Special lower-rank boundary fibers do not enlarge that component's dimension. Combining with the stated earlier bounds yields the rank-at-most-one frontier for affine dimension at least eight. This does not prove (H), exclude affine dimension seven, or settle K9/K10.

No mathematical correction is required. 
