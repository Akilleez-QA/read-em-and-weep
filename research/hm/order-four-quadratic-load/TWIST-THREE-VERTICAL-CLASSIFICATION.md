# Primitive twist-three nondominant images and their quadratic exclusion

## Standing input

Use the actual fifty-point blowup and projection proved in EIGENQUOTIENT-PROJECTION-BOUNDS.md (published at 3c4ab4b2cdfb9e54012f92f798a8da34768413d0). Thus X=P_Q(V(3)), L=O_X(1), H is the quadric hyperplane class, rho:Xhat->X blows up the fifty simple evaluation base points, A=L-sum E_i defines f:Xhat->P3, and every E_i maps isomorphically to P3. Let psi be a primitive trace-free twist-three endomorphism with irreducible characteristic polynomial. Its integral eigenquotient divisor has strict transform

    T=2L-2H-sum m_i E_i.

Assume T does not dominate P3. The intersection identity gives sum m_i=40.

## 1. Exact alternatives before an additional general-position input

Exactly as in TWIST-TWO-VERTICAL-IMAGE-CLASSIFICATION.md, the positive sum of multiplicities implies the integral image D=f(T) is a surface. For e=deg D, the effective pullback f*D contains T with coefficient one, and every positive multiplicity is exactly e. The proof restricts to any exceptional E_i with m_i>0: T|E_i is a positive integral multiple of D, while (f*D)|E_i=D. Also

    H^3(f*D-T)=2e-4 >= 0,

so e>=2.

The local eigenquotient equation is c+2au-bu^2, where u is the fiber coordinate centered at an evaluation base point. Multiplicity m implies ord(c)>=m, ord(a)>=m-1, ord(b)>=m-2, hence ord(det psi)>=2m-2. The determinant is a nonzero nonsquare section of O_Q(6). A nonzero degree-six section has order at most twelve at a point, and an order-twelve section is a scalar sixth power of the tangent hyperplane section; see QUADRIC-JETS-EXCLUDE-HIGH-VERTICAL-DEGREES.md for the homogeneous-weight proof. Such a section is a square. Consequently m<=6.

Combining e|40, 2<=e<=6 gives precisely

    (degree D, number of positive multiplicities) = (2,20), (4,10), (5,8).

All positive multiplicities equal the indicated degree. This conclusion needs no additional genericity or hyperplane count.

## 2. A quadratic image forces a quadric section singular at thirty marked points

For e=2, let J consist of the twenty indices with m_i=2. Then

    f*D-T = 2H-2 sum_{i not in J} E_i.

This is effective with no exceptional component. Its pushforward is a divisor of class 2H on X, hence the pullback of a nonzero section g of O_Q(2), since p_*O_X=O_Q. The exceptional coefficients show that g has order exactly two at each of the other thirty marked points and is nonzero at the twenty indexed by J.

## 3. Elementary singular-support lemma for a quadric section

Let Q be any smooth complex quadric threefold and Z a finite reduced subset such that every projective hyperplane contains at most N points of Z, with N>=2. Then every nonzero section g of O_Q(2) has at most max(N+2,4) singular points belonging to Z.

Proof. Write Q={q(x)=0} in P(W), dim W=5, with q nondegenerate. An ambient quadratic representative of g is q(Ax,x) for a q-self-adjoint operator A. The section is nonzero precisely when A is not scalar. At a point [x] of Q, its differential along Q vanishes precisely when Ax is proportional to x. Thus the singular support is the union of the isotropic projectivized eigenspaces of A.

If A is not diagonalizable, its eigenspaces together span a proper vector subspace of W. All singular points then lie in a projective hyperplane, giving the bound N.

If A is diagonalizable, its distinct eigenspaces are mutually orthogonal and each is nondegenerate. A one-dimensional eigenspace has no isotropic projective point; a two-dimensional one has exactly two; a three-dimensional one has a smooth plane conic; and a four-dimensional one has a quadric surface in a hyperplane. Since A is not scalar, the partitions of five are as follows. The partition 4+1 gives at most N marked singular points. The partition 3+2 gives at most N+2; 3+1+1 gives at most N. Partitions with no part of size at least three give at most four singular points in total. This proves the lemma. It applies to nonreduced or reducible g as well; diagonalizability is a case distinction, not an assumption.

In particular, if every hyperplane contains at most twenty-six points of Z, a quadratic section cannot be singular at thirty marked points. Thus the degree-two image is excluded under that single explicit hyperplane-count input.

## 4. How the required hyperplane count follows on a general-quadric open

Assume the previously established primary-surface input that any hyperplane contains at most five of the twenty-five mutually skew lines C_i. Choose Q generally enough to avoid the following finite set of points: for each hyperplane containing at least two C_i, its intersections with every C_j not contained in that hyperplane. There are only finitely many such hyperplanes, since two skew projective lines span a unique hyperplane. This condition is open and nonempty in the parameter space of quadrics and is compatible with transverse intersection with each C_i.

A hyperplane containing no C_i contains at most twenty-five points of Z=C intersect Q. A hyperplane containing exactly one C_i contains at most 2+24=26. A hyperplane containing at least two contains, by the chosen avoidance, only the two marked points on each contained line, hence at most ten. Therefore the cap twenty-six holds on this general-quadric open.

Here is the needed line-count proof. Transport the configuration using PRIMARY-NORMALIZATION-QUADRIC-INTERPOLATION.md at 6117e44aec3caec4887b7160aa41466397306134. On the modular normalization, a hyperplane divisor has class H=I+2F and H.F=5, while each of the twenty-five line sections has intersection one with the nef fiber F. If the hyperplane contains c of these lines, subtract their corresponding section components from its effective pullback divisor. The remainder is effective, so its intersection 5-c with F is nonnegative. Thus c<=5. This uses the exact embedded-configuration transport, not an identification of the primary evaluation bundle with the adjoint bundle. The quadratic-image exclusion is therefore valid on the stated nonempty general-quadric open.

## Consequence and boundary

On the stated general-quadric open, a primitive twist-three nondominant eigenquotient has only the alternatives

    degree-four image with ten multiplicities equal to four;
    degree-five image with eight multiplicities equal to five.

This does not exclude these two alternatives or any dominant twist-three eigenquotient. The proof uses symbolic divisor classes, a universal local equation, and elementary self-adjoint linear algebra, with no selected HM coefficients, rank experiments, or external writes.

## 5. Further necessary singularities on the image surface

For either remaining alternative, at each positive-multiplicity evaluation point the degree-e initial form of the eigenquotient equation is the equation of D under E_i=P3 -> P(U*). In local coordinates (u,a_1,a_2,a_3), the equation c(a)+2a(a)u-b(a)u^2 has degree at most two in u. Therefore its degree-e initial form vanishes to order at least e-2 at [u:a_1:a_2:a_3]=[1:0:0:0]. That exceptional direction maps to the original rank-one evaluation functional, namely kappa(z_i) on the known smooth rational sextic Gamma.

Consequently a degree-four image has multiplicity at least two at the kappa-images of its ten positive evaluation points; a degree-five image has multiplicity at least three at the kappa-images of its eight positive evaluation points. When those images are distinct, these are ten or eight distinct prescribed singular points respectively. This last distinctness can be imposed by a further general-Q condition, but is not needed for the local assertion. No contradiction follows merely by restricting D to Gamma: the forced total multiplicities are twenty and twenty-four, while the respective restriction degrees are twenty-four and thirty.

For completeness, distinctness is an elementary incidence condition. For two different C-lines, their kappa-identifications with Gamma give two distinct points p_i(t),p_j(t) for each t in Gamma. Requiring a quadric to contain both imposes two independent linear conditions, since O_P4(2) separates distinct points. Letting t vary in one dimension gives a closed bad locus of dimension at most thirteen in the fourteen-dimensional projective space of quadrics. Avoid the finite union over pairs of C-lines. Points on a single C-line have distinct kappa-images because kappa on that line is an isomorphism and the quadric intersection is transverse.
