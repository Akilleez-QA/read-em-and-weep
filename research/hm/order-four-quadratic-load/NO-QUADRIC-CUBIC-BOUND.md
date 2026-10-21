# Without a section quadric there are at most five section cubics

## Conclusion

For a general proper section Z of the 25 HM lines, suppose

    a=h^0(I_(Z,H)(2))=0.

Then

    b=h^0(I_(Z,H)(3))<=5.

Together with UNIQUE-QUADRIC-CUBIC-BOUND.md, the surviving generic alternatives become a=0,b<=5 or a=1,4<=b<=6. This does not eliminate a=1 or prove the actual residual trace intersection is zero.

We use the established finite quintic base scheme Z, normalizer transitivity on its 25 labels, spanning of H=P3, and the absence of three collinear points in a general section. No uniform-position statement for integral curves is used.

## 1. Finite cubic base scheme already implies b<=5

If the full cubic system through Z has no positive-dimensional base locus, choose three general members. Their common zero scheme Y is a (3,3,3) complete intersection of length 27 containing the 25 reduced points Z. The quotient I_Z/I_Y has length two. In degree three, h^0(I_Y(3))=3, so the exact sequence of ideal sheaves gives

    h^0(I_Z(3))<=3+2=5.

This counts the full scheme lengths, including any nonreduced residual structure.

## 2. A cubic base curve must contain all section points

Suppose toward a contradiction that b>=6. There is no fixed surface in the cubic system. A common factor of degree at least two would bound b by the dimension of linear forms, namely four. A common factor of degree one would be a canonical plane. The generic subset of section labels lying on that plane is invariant under the transitive normalizer action, so it is empty or all labels. All labels contradict spanning of H; no labels would mean that each quotient quadric vanishes on all of Z, contradicting a=0. Thus there is no common surface factor.

By Section 1 the cubic base locus has a curve. Let D be the reduced union of its one-dimensional components. The generic subset of labels lying on D is likewise intrinsic and invariant, hence empty or all. This can be read over the function field of the hyperplane parameter space: all 25 section points are rational over that field, the base-curve construction is intrinsic, and the normalizer acts semilinearly on the field while permuting the labels. Its transitivity forces the membership set to be empty or all. It does not assert that one fixed hyperplane is preserved by the normalizer.

The empty possibility is impossible. Two general cubics have no common surface and cut a complete-intersection curve of degree nine containing D. Let R be the reduced union of its other components. Its degree is at most eight. A third cubic can be chosen to avoid every component of R, since none is a base component. If all 25 points lie outside D, they lie on R and on that third cubic. Bezout gives 25<=3 deg R<=24, a contradiction.

Therefore all 25 points lie on D. A quintic generator combination avoiding every component of D gives

    25<=5 deg D, hence deg D>=5.

Also I_D(2)=0, because every quadric containing D would contain Z. Every section cubic contains D, so b<=h^0(I_D(3)).

## 3. Elementary curve bound

We prove the needed general fact: a reduced curve D in P3 of degree at least five with I_D(2)=0 satisfies h^0(I_D(3))<=5.

First a general plane section Gamma of D consists of deg D distinct points and is not collinear. Distinctness follows by choosing the plane transverse to the smooth loci and avoiding the finite singular/intersection locus. To prove noncollinearity without uniform position, it suffices to find one proper plane meeting D in three noncollinear points; noncollinearity then holds on a nonempty open set of planes. Such a plane exists as follows.

- If D has a nonplanar irreducible component, take three general points on it. Their spanning plane contains no component of D. Indeed, after fixing two general points, the planes obtained by varying the third fill the pencil through their secant; no fixed curve can lie in every such plane unless it is that secant, and varying the two points excludes this possibility.
- If D has a nonlinear planar component C but is not contained in its plane P, take two general points of C and one point of D outside P. Their spanning planes form a dense family of planes through that outside point, since the secants of a nonlinear plane curve fill the dual plane. A general such plane contains none of the finitely many curve components.
- If D is a union of lines, it has at least three distinct components. Since it is not planar, choose three not all contained in one plane. One can choose points p1,p2 on the first two so that the joining line misses the third. If the first two meet, choose the third outside their plane and avoid its intersection with that plane; if they are skew, choose p1 so the plane spanned by p1 and the third line does not contain the second line, then choose p2 outside that plane. A general plane through p1p2 contains no component line and meets the third in a point outside p1p2.

Planarity of D is excluded by I_D(2)=0. The above cases therefore exhaust the possibilities.

Any five distinct noncollinear points in a plane impose five independent conditions on cubic forms. To separate one of the points, select among the other four a pair whose joining line misses it; such a pair exists unless all five are collinear. Cover each of the two remaining points by a line missing the chosen point. The product of the three lines separates that point. This works for every point, proving the assertion.

Let R=S/I_D be the saturated homogeneous coordinate ring and choose a general linear nonzerodivisor L. Since I_D(2)=0, dim R_2=10. The quotient R/LR surjects onto the saturated coordinate ring of Gamma, so

    dim(R/LR)_3>=h_Gamma(3)>=5.

The exact multiplication sequence gives dim R_3=dim R_2+dim(R/LR)_3>=15. Since S_3 has dimension twenty,

    h^0(I_D(3))=20-dim R_3<=5.

This contradicts b>=6 in Section 2 and completes the proof.

## Boundary

The argument uses reduced base-curve support only. It does not need the cubic base scheme or its complete-intersection components to be reduced, and it does not identify the residual scheme with an arbitrarily chosen complementary curve. The degree bounds count reduced support conservatively. The resulting b<=5 is the numerical threshold needed for possible generic residual product injectivity, but it does not prove that the actual two cubic trace spaces are disjoint. No selected coefficients, ranks, or hyperplanes were evaluated.
