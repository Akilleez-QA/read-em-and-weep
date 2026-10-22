# Four cubics without a quadric force an integral sextic base curve

## Conclusion

Under the established generic HM-section hypotheses, the remaining alternative

    a=h0 I_Z(2)=0,  b=h0 I_Z(3)=4

forces the reduced curve part D of the cubic base locus to be an integral degree-six curve containing all 25 section points. Those points lie in the smooth locus of D. This narrows the remaining case; it does not exclude it or prove cubic trace transversality.

Use FINITE-CUBIC-BASE-RIGIDITY.md for the canonical nonempty reduced base curve containing all Z, and the reusable constant-Plucker family exclusion of EXCLUDE-FIVE-CUBIC-ENDPOINT.md, published at c159a09d691605f3254d4d01eca07e042647e6d0. No selected evaluation is used.

## 1. Seven points and cubic separation

Seven distinct points in P2 impose seven independent cubic conditions unless five of them are collinear. For a fixed target p, partition the other six points by their joining lines with p. If no five points are collinear, each class has size at most three. A complete multipartite graph on six vertices whose largest part has size at most three admits a perfect matching. The three joining lines of its pairs avoid p; their product separates p from the other six points. Repeating for each target proves independence.

For completeness, the matching assertion follows by repeatedly pairing vertices from the two currently largest nonempty classes; with an even number of vertices and maximum class size at most half the total, this preserves the required inequality until no vertices remain.

It follows that if a set Gamma of at least seven distinct points satisfies h_Gamma(3)<=6, all but at most two points lie on one line. Some seven points must include five on a line L. If three points lay off L, those three together with four on L would form seven points with no five collinear, a contradiction. The line carrying all but at most two is unique.

## 2. The degree of D is at most six

Every cubic through Z contains D, so h0 I_D(3)>=4. Also I_D(2)=0. For a general linear nonzerodivisor L on R=S/I_D,

    dim R2=10, dim R3<=16,
    h_(D intersect V(L))(3)<=dim(R/LR)3<=6.

Assume deg D>=7. Its general plane section is reduced; Section 1 places all but at most two section points on a unique line. For each fixed irreducible component D_i, the point/plane incidence is an irreducible P2-bundle over D_i. Hence its generic plane-section points form a single Galois orbit over the plane-parameter function field. Membership in the unique line is invariant under that Galois group, so it includes either all or none of the points from D_i.

The components off the line have total degree at most two. The remaining reduced union D' has degree at least five and collinear general plane section. The elementary noncollinearity lemma from NO-QUADRIC-CUBIC-BOUND.md forces D' to be planar. Thus some plane Pi contains all but at most two degrees of D.

This plane is unique. If two distinct planes each contained a reduced subcurve of degree at least deg D−2, their common subcurve would have degree at most one, since the planes intersect in a line. Their union would have degree at least 2 deg D−5>deg D, impossible. Thus Pi is canonical.

Over the generic HM hyperplane parameter, the semilinear normalizer action preserves Pi. The subset of the 25 section labels on Pi is invariant, hence empty or all by transitivity. All is impossible because Z spans its P3. If none lie on Pi, all lie on the outside reduced curve of total degree at most two. An integral conic, one line, or two intersecting lines is planar and again contradicts spanning; two skew lines contain at most four of the points because no three section points are collinear. This also is impossible.

Therefore deg D<=6. A quintic generator combination avoiding D gives 25<=5 deg D, so deg D is five or six.

## 3. The section points avoid all singularities and component intersections

The singular locus of the canonical reduced curve D is finite and canonical. The subset of labels lying in it is invariant under the generic normalizer action, hence empty or all. Choose a quintic generator combination meeting D properly. The intersection has length at most 5·6=30 and contains Z.

If a reduced curve is singular at p, quotienting its one-dimensional local ring by a nonzerodivisor cannot have length one: that would make its maximal ideal principal, and hence make the ring regular. Therefore each singular section point contributes at least two to the intersection length. If all 25 points were singular, the length would be at least50, a contradiction. Thus no section point lies in Sing D; in particular it lies on exactly one component.

## 4. Only one component meets Z

The nonempty subsets of Z on the irreducible components give a canonical partition of the 25 labels. Normalizer transitivity makes all blocks the same size, so the number of components meeting Z divides25. Since deg D<=6, this number is one or five.

If it were five, each component would contain five section points. No such component can be a line, by the no-three-collinear property. Their total degree would then be at least ten, impossible. Hence one integral component D0 contains all 25 points. Intersecting D0 with a general quintic combination gives deg D0>=5.

## 5. Degree five is excluded by the existing family theorem

If deg D0=5, its quintic Cartier cut has length25 and contains Z, so it equals Z scheme-theoretically. The six quintics restrict proportionally to D0: divide each by a quintic whose zero divisor is exactly Z, obtaining a global regular function on the integral projective curve.

Thus the actual Plucker evaluation is constant along D0 minus Z. The curve spans H because it contains Z, and its unique component characterization makes the family rational over the generic hyperplane parameter. These are exactly the hypotheses of the already-proved reusable family exclusion in EXCLUDE-FIVE-CUBIC-ENDPOINT.md. Consequently deg D0 cannot be five.

Therefore deg D0=6. Since D is reduced and has total degree at most six, D=D0 is integral of degree six. Section 3 proves that all 25 points lie in its smooth locus.

## Boundary

The new conclusion is a necessary integral-sextic configuration for a=0,b=4. The argument does not identify its genus, assert its existence or nonexistence, identify a fixed Plucker kernel in degree six, or evaluate any selected HM matrix. The quintic intersection now has length30, not25, so the constant-ratio argument does not apply to this remaining sextic case without further input.
