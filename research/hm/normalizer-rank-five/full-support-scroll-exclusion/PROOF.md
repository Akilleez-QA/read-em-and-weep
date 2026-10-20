# Full-support cubic scrolls: square-contact exclusion and a squarefree exception

## Scope and conclusions

All vector spaces and varieties are over C. Products xy denote symmetric tensor products, identified with commutative quadratic polynomials. Consequently mixed-term polynomial coefficients, rather than unannounced matrix entries, are used throughout.

Let E have dimension four. Consider the parametrized surface

    q=(s x+t y)(a z+b(s p+t r)),                             (1)

where x,y are independent, z is nonzero, and

    K=span{xz,yz,xp,xr+yp,yr}

has dimension five and full support E. The parameters a,b are fiber coordinates, with the usual changes of weight over [s:t]; they are not coordinates of an ordinary product P1 x P1.

The following statements are proved below.

1. This is an embedded smooth cubic scroll S(1,2) in P(K).
2. Up to changes of basis in E and changes of the displayed parametrization, there are exactly three possibilities, represented by:

   I.  (s x+t y)(a x+b(s z+t w));
   II. (s x+t y)(a z+b(s x+t w));
   III.(s x+t y)(a z+b(s y+t w)),

   where x,y,z,w form a basis.
3. In I and II the scroll contains a square x². The intersection of all limiting rank-two support planes at x² is Cx. Thus a linear v:K->E compatible on a dense open of the scroll necessarily satisfies v(x²) in Cx.
4. For I and II, the entire rank-at-most-two locus is the union of the cubic scroll and a common-factor plane. Neither component can have a dense compatible locus for a square-avoiding v. Hence its compatible rank-two locus has dimension at most one. This eliminates the entire explicit full-support K in the parent question, not merely its scroll.
5. III has no nonzero rank-one tensor anywhere in K. Its scroll admits compatible corrections, including v=0, and indeed a five-dimensional space described explicitly below. Hence the square-contact obstruction does not exclude all full-support smooth cubic scrolls.

The classification is of family (1). We do not claim that every abstract smooth cubic scroll embedded in the symmetric rank-two locus admits this factor parametrization. No conclusion about realization of III by a global trilinear operation is asserted.

## 1. General limiting-support lemma

Let S be an integral subvariety of P(K) whose general tensor has rank two, and let [e²] belong to S. Let G be the closure of the graph of the support map

    S_rank2 -> Gr(2,E),  [q] -> im(q).

Let L_e be its set of support-plane limits over [e²]. Every P in L_e contains e. This follows from the closed incidence q in Sym² P.

Suppose v:K->E is linear and v(q) belongs to im(q) on a dense open subset of S_rank2. Compatibility holds on all S_rank2, since membership in the tautological plane is closed on the graph over that open locus. The incidence v(q) in P is closed on the full graph closure, so

    v(e²) belongs to intersection_{P in L_e} P.             (2)

In particular, two limiting planes whose intersection is Ce suffice to force a compatible square. This argument never presumes that rank-two compatibility automatically extends to rank one with its smaller support.

Under the trilinear hypotheses of rank-six-surface-reduction/PROOF.md, Section 6, such a compatible square is forbidden: global repeated-input injection makes A_u(e) and A_e(u) independent, whereas v(e²) in Ce would make them proportional. Only this abstract square-avoidance consequence is used here.

## 2. Why (1) is a smooth cubic scroll

The five coefficient sections of (1), in the indicated order, have scalar coordinates

    [as:at:bs²:bst:bt²].                                   (3)

The standard projective bundle of lines in O(-1) direct-sum O(-2) over P1, embedded by its tautological dual, has precisely these coordinates. For completeness, the chart s=1 maps [a:b],t to [a:at:b:bt:bt²]; the analogous chart t=1 glues by the line-bundle weights. They separate the base point and the fiber point: when a is nonzero the first two coordinates recover the base, and when a=0 the last three form the Veronese conic and recover it; the remaining ratio recovers the fiber. On base charts a nonzero, respectively b nonzero, the displayed coordinates also recover local affine coordinates regularly. Thus this map is a closed embedding of a smooth projective bundle. Its hyperplane self-intersection is 1+2=3 (equivalently the two section degrees sum to three). It is the smooth cubic scroll S(1,2).

Since the five tensors defining K are independent, their linear identification with five coordinate directions transfers this embedding to P(K). In particular (1) never produces the zero tensor at a projective-bundle point. It follows also that m(s,t)=sp+tr is never proportional to z, since otherwise its corresponding quadratic coefficient would lie in the span of xz,yz and the five coefficient tensors would be dependent after changing the base coordinates.

The support of K is span{x,y,z,p,r}: every displayed nonzero factor occurs as a factor of a tensor on the scroll, and rank-two supports (or the evident rank-one limit supports) recover the factor lines. Full support therefore says that these five vectors span E.

## 3. Classification within the parametrized family

Put A=span{x,y}.

### 3.1 z belongs to A

Change base coordinates so z=x. Full support then implies that x,y,p,r form a basis. Renaming p,z and r,w gives I. These tensors are visibly independent.

### 3.2 z does not belong to A

Put H=A+Cz, a three-plane. The composition of m:C²->E with E->E/H is nonzero, by full support. It has a unique projective zero. Change base coordinates so that zero is [1:0]. Thus p belongs to H and r is outside H. Replacing m by m+ell(s,t)z, for a linear form ell, only changes the fiber coordinate a and the basis of K. We may therefore assume p belongs to A. Moreover p is nonzero: p=0 would make xp=0 and dim K<=4.

If p is proportional to x, scale m to make p=x. The vectors x,y,z,r are a basis, giving II.

If p is not proportional to x, write p=alpha x+beta y with beta nonzero. Make the base shear s_old=s_new+(alpha/beta)t_new, t_old=t_new. Then the new second coefficient of l is y' = y+(alpha/beta)x=p/beta. Scaling m by 1/beta puts its first coefficient equal to y'; its second coefficient is still outside H. Renaming that coefficient w gives III.

These three cases are exhaustive. They are also distinct as parametrized scrolls: in I the unique square lies on the degree-one directrix b=0; in II it lies off that directrix; III contains no square. The degree-one directrix of S(1,2) is intrinsic. The assertions about squares also follow directly from the normal forms or Sections 4 and 6.

## 4. All square-boundary support limits in I and II

### 4.1 Type I

Near its square, use s=1,a=1 and fiber coordinate b. Then

    q=(x+t y)(x+b z+bt w).

The unique rank-one point is t=b=0. For nearby rank-two points its plane is

    span{x+t y, -t y+b z+bt w}.

As (t,b)->(0,0), all limits, and exactly those limits, are

    span{x, -c y+d z},   [c:d] in P1.                      (4)

Indeed the independent y,z coefficients have orders controlled by t,b; the bt term has strictly higher order than their minimum. The same statement follows along arbitrary algebraic arcs, or from the blow-up of the ideal (t,b). Every ratio is realized by a straight-line arc. The intersection in (4) is Cx.

### 4.2 Type II: the requested example

Near its square use s=1,b=1, so

    q=(x+t y)(x+t w+a z).

The unique rank-one point is t=a=0. The support plane is

    span{x+t y, t(w-y)+a z}.

All its limits are exactly

    span{x, c(w-y)+d z},   [c:d] in P1.                    (5)

The independent coefficients give the same argument as above, with no higher-order term needed. Their intersection is Cx. In particular a=0 gives span{x,w-y}, while t=0 gives span{x,z}. This checks the sign and factor conventions of the parent example.

Because the scroll embedding is an isomorphism onto its image, every rank-two approach to this square is accounted for by the local coordinates just used. The general lemma therefore excludes an identically compatible scroll in both cases, including compatibility originally assumed only on a dense open.

## 5. Entire rank-two loci and full exclusions

### 5.1 Type II

Here

    K=span{x²,xy+xw,yw,xz,yz}.

Every nonzero complex rank-at-most-two symmetric tensor factors as LM. The coefficient conditions z²=w²=zw=0 force one of L,M to have both z- and w-coefficients zero. To see the only potential ambiguity, if one factor has a nonzero z coefficient the other has zero z coefficient, and zw=0 then forces that other's w coefficient zero; if neither has a z coefficient use w²=0. Thus choose

    L=sx+ty.

The coefficient condition y²=0 says t M_y=0, and xy=xw says s M_y+t M_x=s M_w.

If t is nonzero, M_y=0 and t M_x=s M_w, whence

    M=a z+b(sx+tw).

This is the scroll; its t=0 limits are included by closure.

If t=0, then L is proportional to x and M_y=M_w, giving the plane

    P(x U),   U=span{x,y+w,z}.

Conversely both displayed families lie in K and have rank at most two. Hence, set-theoretically,

    R2(K)=S(1,2) union P(x U).                             (6)

Both are irreducible surfaces, and they are distinct (the plane contains x(y+w), outside the scroll's t=0 ruling). They are consequently exactly the surface components. There are no further rank-two components of higher dimension. The only square in K is x²: the missing y²,z²,w² coefficients of a square force its y,z,w coefficients zero.

If v is compatible on a dense open of the plane, approaching x² along x(x+epsilon z) and x(x+epsilon(y+w)) forces

    v(x²) in span{x,z} intersect span{x,y+w}=Cx.

Together with Section 4, neither component of (6) can contain a compatible surface when v avoids compatible squares. A closed compatible locus inside the rank-two open would otherwise be dense in one of these two irreducible surface components. Its dimension is therefore at most one.

This proves the stronger whole-kernel exclusion for the explicit K and every GL(E)-equivalent kernel. In the trilinear reconstruction, the ordered factor cover is finite, so it also excludes a projective independent-zero surface fiber at any middle point with this residual kernel.

### 5.2 Type I also has a full-kernel exclusion

Here K=span{x²,xy,xz,xw+yz,yw}. Again z²=w²=zw=0 permits the factor choice L=sx+ty. The two remaining coefficient conditions are t M_y=0 and s M_w=t M_z. If t is nonzero, they give M=a x+b(sz+tw), hence the scroll. If t=0, they give M_w=0, hence the common-factor plane P(x span{x,y,z}). Conversely both families lie in K. Thus this too is exactly the union of its scroll and that plane. The plane forces v(x²) in span{x,y} intersect span{x,z}=Cx whenever densely compatible. Section 4 excludes the scroll. Consequently the compatible rank-two locus has dimension at most one for every square-avoiding v on type I as well.

## 6. The genuine squarefree exception III

Now

    K=span{xz,yz,xy,xw+y²,yw}.                             (7)

If h² belongs to K, its x²,z²,w² coefficients vanish, so h is proportional to y. But y² alone does not belong to K, because its coefficient is tied to that of xw. Thus K contains no nonzero square.

In particular the zero linear map v:K->E is square-avoiding and is compatible on the entire scroll. This is an abstract counterexample to any attempt to exclude every full-support smooth cubic scroll by the no-compatible-square condition alone. It does not construct a global trilinear operation.

The whole rank-two locus is, by the factor argument of Section 5,

    R2(K)=S(1,2) union P(y span{x,z,w}).                    (8)

For detail choose L=sx+ty, using z²=w²=zw=0. The x² coefficient gives s M_x=0. If s is nonzero, M_x=0 and the relation xw=y² gives s M_w=t M_y, hence M=a z+b(sy+tw). If s=0, L=y and the same relation forces M_y=0, giving the second plane. The latter plane is transverse to its factor y, so it need not force a compatible square.

### 6.1 All corrections compatible on the scroll

Write k1=xz, k2=yz, k3=xy, k4=xw+y², k5=yw. Exactly the following linear maps are compatible on its dense rank-two locus, where lambda,mu,nu,alpha,beta are arbitrary scalars:

    v(k1)=lambda x+mu z,
    v(k2)=lambda y+nu z,
    v(k3)=alpha x+mu y,
    v(k4)=beta x+(alpha+nu)y+mu w,
    v(k5)=beta y+nu w.                                    (9)

Proof: the directrix b=0 forces the first two equations (the induced map on A preserves every line). Fix [s:t], put l=sx+ty and m=sy+tw. In E/Cl the vectors z,m are independent. Along the ruling, linearity and compatibility of

    a(s k1+t k2)+b(s²k3+st k4+t²k5)

force the quotient of V=s²v(k3)+st v(k4)+t²v(k5) to equal (mu s+nu t)m. Thus

    V-(mu s+nu t)m=(alpha s+beta t)l.

To justify the linear coefficient on the right, its x and y coordinates form homogeneous quadratics satisfying s times the y coordinate equals t times the x coordinate; coprimality of s,t gives the displayed homogeneous linear factor. Comparing coefficients gives (9). Conversely (9) yields the explicit compatible expression

    v(q)=[a lambda+b(alpha s+beta t)]l
           +(mu s+nu t)[a z+b m],

proving sufficiency.

The four-dimensional contraction subspace q->2q(d), d in E*, is given by alpha=nu, with d(z)=lambda, d(x)=mu, d(y)=nu, d(w)=beta. The extra scalar alpha-nu is real algebraic freedom in this calculation. Compatibility on the additional plane of (8) holds identically precisely when alpha=nu: modulo y, the images of yx,yz,yw have respective scalar eigenvalues alpha,nu,nu, and preservation of every line forces their equality. Thus a compatible scroll does not even force the accompanying plane to be compatible.

## 7. Limits and provenance

The fixed-middle square obstruction comes from rank-six-surface-reduction/PROOF.md and extremal-surface-geometry/PROOF.md. The whole rank-two-locus factorization for II is checked in Section 5. The ternary family in rank-five-middle-families/PROOF.md is a different support stratum; none of its classification conclusions was assumed for full-support kernels.

Only universal tensor geometry and local mathematical artifact writing were used. No actual source operation, source matrix instance, physical input, numerical rank calculation, or external action was evaluated. The substantive whole-kernel exclusion is complete for types I and II; III remains a precisely described exception, and no unproved classification outside family (1) is claimed.
