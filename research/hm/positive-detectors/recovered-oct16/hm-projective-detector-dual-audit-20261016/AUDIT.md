> Historical mathematical record, 16 October 2026. Statements of PASS and check counts below refer to the original recorded verification, not a new execution. See PUBLICATION-SCOPE.md at the common series root for current scope, imported premises, and source/public hash bindings.

# Independent audit: global detector-dual bridge and first positive quotient

## Accepted result

**PASS.** The specified epsilon generator comparison is global and inversion equivariant. The detector trace coefficients are exactly

    4, 4 v2, 4(v2^2-v1 v3+2v0 v4).

The genuine-degree supertrace signs, all 24 sparse dual-cycle records, their homogeneous degrees and ambient basis indices are correct. The complete first-component quotient and its eight-dimensional positive basis/projection/dual maps are authenticated independently.

The four plus-projected detector classes are independent already in that first component, with minor16. Consequently no nonzero linear combination involving only h,j,p,r is anti-invariant. A stronger corollary is now proved: the eight original and transported detector classes are independent modulo complete dual boundaries. Thus the original four-dimensional detector span is **not** inversion stable; the eight-dimensional span obtained by adjoining its transforms is stable. This replaces the earlier absence of a closure certificate with a definite nonclosure proof for these particular four classes.

None of these statements evaluates an obstruction or implies that any actual detector value is nonzero. The separate global inversion-covariance theorem identifies the actual obstruction as invariant, but does not force a linear relation among just the four original values.

## 1. Specified global generator comparison

Let Y=(P1)^4, let sigma:Y->P4 be the binary-product map, and let T=Q[v0,...,v4], each vi of Segre degree1. With the exact ordered homogeneous coordinates, set

    a=(X1Y2-X2Y1)(X3Y4-X4Y3),
    U=X1X2Y3Y4+Y1Y2X3X4.

For the pair-partition stabilizer H, a has character epsilon and U is invariant. Oddness on each within-pair transposition forces divisibility by the corresponding prime pair bracket in the polynomial Cox ring. Their product divides every epsilon polynomial, and the quotient is H invariant. This argument works along the whole bracket divisor, including infinity, not just after dehomogenizing.

The three distinct generic conjugates of U correspond to the three pair partitions. The generic S4 extension therefore makes its minimal polynomial over the symmetric field have degree3. Consequently 1,U,U^2 are T-linearly independent. Degreewise equality follows from the invariant character dimension

    ((n+1)^4+2(n+1)^3+3(n+1)^2+2(n+1))/8
      = binom(n+4,4)+binom(n+3,4)+binom(n+2,4).

The analogous epsilon expression has the two odd-sign terms negated and equals the sum of binomials shifted by1. These are polynomial dimension identities, not extrapolations from a finite list of degrees. The independently enumerated eight group elements and the controls agree with both identities. Injectivity and equality in every degree give global free bases 1,U,U^2 and a,aU,aU^2.

Sheafification gives the specified polynomial epsilon summands O(-1),O(-2),O(-3). Projection formula with the full-sign O(-2) line gives the actual complex comparison

    C_epsilon = B(-3) direct_sum B(-4) direct_sum B(-5),
    (G0,G1,G2) -> aG0+aUG1+aU^2G2,

where B=End(L) for the original perfect complex in genuine degrees -1,0,1,2. Its differential is T-linear. Finite pushforward and the affine pulled-back carrier cover therefore preserve the full Cech/internal total complex, including the bottom incoming component. No generic-field-only basis, clipped Laurent space or missing incoming differential is substituted.

Exchanging each X_i and Y_i changes the sign of both pair brackets and exchanges the two U summands. Hence a,U and all three generators are fixed. The full-sign factor has i^4=1 and the standard O(-2) linearization. Combined with the authenticated chain reversal, this gives the stated componentwise inversion without an extra generator sign or permutation.

## 2. Exact canonical trace, including infinity

The independent checker constructs polynomials in all eight Cox variables and verifies the exact identities

    Alt(q a U^j)=4 Delta beta_j, j=0,1,2,
    beta=(1,v2,v2^2-v1v3+2v0v4),
    q=X3^2 X4^2 Y1^2 Y2^2,
    Delta=product_(i<j)(XiYj-XjYi).

This is full 24-term unnormalized alternation. It is not a finite-point control and it is not merely an affine identity later assigned a weight. Every monomial has the required equal multidegree j+3. Restriction to all16 standard finite/infinity chart choices gives the same identities. Polynomial equality establishes extension over ramification and v0=0. Symmetric owned denominators can be retained unchanged.

The previously authenticated finite-duality bridge identifies Alt/Delta with canonical finite trace, with positive elementary-symmetric Jacobian and positive ordered P4 Serre trace. In particular the actual harmonic target (-1,-1,-3,-3) corresponds to multiplication by this q. There is no division by24. There is also no extra1/8: the input is already expressed in the specified epsilon summand.

For the internal -2 part of G_j, the scalar degree is -5-j; beta_j has degree j. Thus every term 4 beta_j L_d(G_j) lies in O(-5), and its Serre trace is exactly the original detector. The identity supplies global sheaf/Cech maps, not an entrywise choice of a rational Laurent expansion.

## 3. Genuine-degree supertrace and exact cycle coordinates

The ranks5,15,10,2 have genuine degrees -1,0,1,2. If F has internal degree -2 and E has degree+2, the diagonal products in FE lie in the first two degrees. Therefore

    Str(FE)=-tr(F20 E02)+tr(F31 E13).

A coefficient c of F20[i,j] must become -c at E02[j,i]; a coefficient c of F31[i,j] becomes +c at E13[j,i]. An unsigned ordinary transpose would be wrong. This transpose belongs to the dual pairing and does not add another physical-source transpose.

The independent check reads the original rows from their authenticated theorem, constructs the duals with these signs, and tests the pairing on every one of the80 matrix units. It finds

    Eh: E02[6,2]=E02[9,3]=E13[1,0]=1;
    Ej: E02[7,3]=E02[5,4]=E13[1,1]=1;
    Ep: E02[3,1]=E02[2,4]=-1, E13[0,5]=1;
    Er: E02[3,0]=E02[4,2]=-1, E13[0,6]=1.

The degree+3 differential is ev E02-E13 gamma. All four original and all four transported matrices are closed by the actual homogeneous literals. Multiplication by beta_j preserves closure since the differential is T-linear; it is not differentiation of beta_j. Perfect/Serre duality pairs B(-3-j) with B(j-2), so the dual triples are exactly(4E,4v2E,4beta2E). The total multiplication sign is (-1)^(2*4)=+1.

The archived ambient basis ordering is independently enumerated for dimensions80,400,1200. Every one of the24 records, all120 nonzero entries, all basis keys and all zero-based indices match the derived cycles. These are ambient closed-cycle coordinates. They are not implicitly asserted to be quotient coordinates.

Coordinate reversal on P4 is even. It fixes beta_j and preserves the canonical Serre trace. The original q is taken to its pair-exchanged version; that pair exchange has epsilon+1 on the already authenticated epsilon summand. Thus the dual action is the ordinary semilinear chain conjugation on these particular cycles, with no further canonical or infinity sign.

## 4. Complete first-component quotient, independently rebuilt d5

For B(-2), the line-bundle cohomology page has only the positions

    (internal -3,Cech4): dimension10,
    (internal +2,Cech0): dimension80,
    (internal +3,Cech0): dimension50.

The ordinary80->50 map has kernel given by the exact graph

    E02[5c+k,a]=sum_b E13[c,b] gamma[b,a,k].

Thus K30 has the30 literal free coordinates e_(15c+b)=E13[c,b]. All50 E02 entries are determined; none is discarded. The graph is an explicit kernel description and proves surjectivity onto the50 ordinary equations without a rank search.

The only additional incoming differential is d5 from the bottom10-dimensional term. I rebuilt its ten columns from the literal gamma/delta/ev maps in the complete standard P4 Cech complex. The independent contraction removes the **largest** eligible nonnegative-exponent index, whereas the archived construction removes the smallest. At every stage the checker verifies internal-square zero, anticommutation with the Cech differential and the actual contraction identity. At the end it verifies both closedness identities and equality of all five constant chart restrictions.

The resulting columns in the literal K30 coordinates are exactly

    b_(2a)=e_a+e_(25+a),
    b_(2a+1)=e_(10+a)+e_(20+a), a=0,...,4.

The entire E02 graph is checked for every resulting column. A ten-coordinate identity minor proves independence. Consequently H2(B(-2)) is exactly K30 divided by this image, with retained basis e0,...,e19 and relations

    e_(25+a)=-e_a, e_(20+a)=-e_(10+a).

There are no other possible incoming or outgoing spectral-sequence terms in this small model. This is a complete-boundary certificate, not an inference from a clipped computation. The largest intermediate expression has165 sparse terms. No archived large rank routine or large solve was executed.

## 5. Four positive classes and the full positive-eight interface

Chain reversal gives I(e_(5b+a))=-e_(5b+4-a). It preserves the ten d5 columns and commutes with the exact quotient map. On the retained20-dimensional quotient it is four blocks -J5, with trace -4 and eigenspace dimensions8 and12.

The first components of the actual detectors, including the canonical trace factor4, are

    4Eh=4e15, 4Ej=4e16, 4Ep=4e5, 4Er=4e6.

Their plus projections are

    2(e15-e19), 2(e16-e18), 2(e5-e9), 2(e6-e8).

Coordinates15,16,5,6 annihilate every complete d5 column and read these projections as2I4. The determinant16 proves independence in actual cohomology. Thus no nonzero original-only detector combination can be anti-invariant on the full epsilon space, because its first plus component would already be nonzero.

The saved positive-eight basis p_(b,s)=e_(5b+s)-e_(5b+4-s), b=0,...,3 and s=0,1, is correct. I independently reduce against the freshly rebuilt d5 image, reconstruct every ambient80-cycle lift and verify all saved quotient and dual rows. With q=Qk, the dual coordinate is(q_left-q_right)/2. These maps kill d5, are inversion invariant, pair as the identity with the eight basis cycles and satisfy the full projector/section identity on every K30 basis vector.

Serre duality identifies these linear dual functionals with the corresponding primal cohomology classes. This does not manufacture complete-Cech representatives for those primal classes. The saved interface correctly limits itself to exact cohomology-linear coordinates.

## 6. Stronger corollary: genuine four-span nonclosure

The original and transformed first-component columns occupy the eight distinct positions

    originals:15,16,5,6, each coefficient+4;
    transforms:19,18,9,8, each coefficient-4.

Every one of these coordinates annihilates the complete d5 image. Their eight-by-eight witness minor is diag(4,4,4,4,-4,-4,-4,-4), with determinant65536. Hence the eight classes are independent in H2(B(-2)), and therefore the eight global detector classes are independent after the specified epsilon bridge.

If the span of the four original detectors were inversion stable in complete dual cohomology, each transformed detector would be a linear combination of those four. Projection to this first direct summand contradicts the eight independent classes. Thus nonclosure is proved, not merely unverified. It also rules out such a four-span closure on a larger full-sign target, because restriction to the invariant epsilon summand would preserve any proposed relation.

Adjoining the four exact transforms gives an eight-dimensional invariant span. In the ordered basis(D_h,D_j,D_p,D_r,I*D_h,I*D_j,I*D_p,I*D_r), inversion exchanges the two four-element blocks. No assertion about stability under a different geometric action, a different detector set or the remaining cohomology coordinates is implied.

For an invariant actual obstruction, equality between each original and transported detector value remains valid. Independence of the four restrictions to the plus space shows that this symmetry alone gives no linear relation among only the four original values. Further source-specific vanishing or relations remain possible and unexamined.

## 7. Evidence and scope

The bridge checks pass791 independent controls. The fresh complete d5, quotient, positive-eight and eight-class tests pass1,461 independent controls. Together these give **2,252 independent controls**, with runtimes below0.07seconds and memory below12MiB per process. Producer checkers pass270+314=584 controls in redirected replays. 

Only universal Cox polynomials, the pinned linear differential literals, exact rational metadata and tiny source-free Cech expressions are used. No actual source coefficient, primitive value, residue, detector value or obstruction is acquired.  The remaining two summand reductions are unnecessary for the conclusions proved here; they are separate tasks.

The final manifest pins both reviewed producer folders, their exact sparse interfaces, the original model and source-row/frame/duality certificates. The earlier inversion audit correctly left cohomological closure open before this bridge and complete quotient existed; Section6 is the new certificate that resolves that particular question negatively.
