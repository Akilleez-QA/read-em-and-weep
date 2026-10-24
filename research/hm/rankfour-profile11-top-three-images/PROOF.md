# Matched Euler images and a two-value defect bound at the actual top-three boundary

## 1. Conditional setting and conclusions

Retain the actual geometric hypotheses of the preceding top-three theorem, PR1188 at 518b3f2686269f83e4f788fe4ed30d0e36dac37b, research/hm/rankfour-profile11-top-three/PROOF.md. Work over C with the fixed physical G=SL2(F5) action on P(W*) and the actual saturated inclusion E in the constant thirty-space. The actual derivative has generic rank four and maximal ordered profile (1,1), and the primal quotient has maximum ordinary degree three.

The preceding theorem forces

    E=D O(-2)+(W'+T6)O(-3)+V O(-4)+O(-8),
    A_q=E/K=W O(3)+O(2)+O(-8),
    U=H0(K(3)) O(-3)=S4 O(-3),
    N=K/U in {
       V O(-4)+T6 O(-5),
       (V+P)O(-4)+W' O(-7),
       (V+D)O(-4)+O(-10) }.

Here A_std=Sym2 W, S4=Sym3 W, D=Sym4 W and T6=Sym5 W; V is the other three-space, P the even four-space and W' the other doublet. U is the actual canonical top splitting subbundle of K, not an arbitrarily chosen cubic subspace. The quotient N has rank nine and degree -42.

We prove four further necessary facts.

1. The actual D-row of E->A_q factors through a saturated equivariant graph j:O(2)->W O(3)+O(2). Its two possible cokernels are W O(3) and O(4)+O(2). Cancelling this graph produces an actual exact quotient of (W'+T6)O(-3)+V O(-4) with kernel N.
2. The derivative of U inside K uses the SAME graph, twisted by -2. Its actual coherent image is precisely j(-2)O, its kernel is A_std O(-4), and the induced quotient map on N has generic rank at most two with an explicit exact kernel sequence.
3. The actual derivative of K has generic rank two or three, never one. If the scalar component of j is nonzero, its rank is exactly three.
4. The original primal/dual determinant defect is either zero or twelve. If twelve, its divisor is the reduced exceptional orbit of twelve points, and its cokernel is an equivariant line sheaf on that orbit.

These statements do not assert that either graph case, either defect value, or any of the three kernel forms occurs. They do not close the top-three boundary or the full rank-four profile, and do not improve a global rank bound.

Eleven complete immutable inputs are retained in INPUTS.json. The earlier nine copies retain their authenticated identities; the preceding theorem and the orbit-ramification original were freshly fetched from immutable public commits for this packet. The latter is db51525015bb7c5e825833d550d08dedf6f6ea96, research/hm/order-four-quadratic-load/GAUSS-DETERMINANT-ORBIT-RAMIFICATION.md. Only its arbitrary-rank invariant-divisor argument is used, not its rank-two profile exclusions. The original actual/source prerequisites remain imported.

## 2. The actual D-row is a saturated Euler graph

Write F=D O(-2) and M=(W'+T6)O(-3)+V O(-4). The projection of the actual quotient E->A_q onto O(-8) can only come from the source O(-8). Surjectivity makes that scalar nonzero. Thus K lies in E0=F+M, and restriction gives an actual exact sequence

    0 -> K -> E0 -> P_plus -> 0,
    P_plus=W O(3)+O(2).                                (1)

This is ordinary cancellation in the actual quotient map. An upper-right component from the source O(-8) does not change its kernel. No connection splitting is asserted.

The inclusion U=S4 O(-3)->E has zero components into M and O(-8), by degree and irreducible inequivalence. Its component into F belongs to the one-dimensional space Hom_G(S4,D tensor W), since D tensor W=S4+T6. Consequently it is the nonzero standard evaluation-kernel inclusion

    0 -> U=S4 O(-3) -> F=D O(-2) -> O(2) -> 0.         (2)

Because U lies in K, the actual F-row of (1) factors through the O(2) quotient. The row is not zero: otherwise F would lie in K, contradicting H0(K(2))=0. We obtain a nonzero equivariant map

    j:O(2) -> W O(3)+O(2).

Let i:O(2)->W O(3) be the standard Euler injection, whose cokernel is O(4). Both relevant Hom spaces are one-dimensional, so for scalars alpha,beta, not both zero,

    j=(alpha i, beta id).                              (3)

This is an abstract description of the actual row; neither scalar is selected or evaluated.

If beta is nonzero, the target automorphism (x,y)->(x-alpha i(y)/beta,y) makes j the scalar-coordinate inclusion. Its cokernel is R=W O(3). If beta=0, alpha is nonzero and the Euler sequence gives cokernel R=O(4)+O(2). In both cases j is a subbundle inclusion, not merely a generically nonzero map. Therefore

    R=coker j = W O(3)       if beta!=0,
                O(4)+O(2)   if beta=0.                 (4)

Quotient (1) by the canonical U and then by the embedded O(2). Since j is a subbundle, projection to M identifies the actual quotient kernel and gives

    0 -> N=K/U -> M -> R -> 0.                         (5)

The splitting type of N is the corresponding one of the three tails already stated; U is the entire canonical degree-minus-three piece of K. Sequence (5) is regular at every parameter and does not assume that M or N has a descended flat connection.

## 3. Differentiation forces the same graph, not an independent choice

Consider the actual second fundamental form of U in the original constant ambient. Since U lies in K=E^-, its derivative lands in (E/U)(-2). Its projection to (E/F)(-2) is zero: E/F has top degree at most -3, so the latter target has top at most -5, whereas U has degree -3. Therefore beta_U factors through

    (F/U)(-2)=O.

This factor is nonzero. If it vanished, the whole actual beta_U would vanish, making the saturated negative subbundle U horizontal and hence constant in characteristic zero, a contradiction. The space Hom_G(S4 O(-3),O) is one-dimensional. Thus for a nonzero scalar kappa the factor is kappa times the canonical cubic evaluation

    e:S4 O(-3) -> O,
    ker e=A_std O(-4).                                (6)

Projection from E/U to E/K=A_q now identifies the restriction of beta_K:

    beta_K|U = j(-2) composed with kappa e.             (7)

In particular the quotient D-row and the top-kernel derivative have proportional coefficient pairs and the same scalar-component vanishing. They are not two independently adjustable graph choices.

Let I=j(-2)O. Because e is surjective and j is saturated, I is the actual coherent image of beta_K|U and is a subbundle of A_q(-2). Its actual kernel is U^-=A_std O(-4). Quotienting beta_K by U and I gives a well-defined O-linear map

    gamma:N=K/U -> A_q(-2)/I = R(-2)+O(-10).           (8)

At the generic point,

    rank gamma = rank beta_K-1 <=2.                    (9)

The surjectivity U->I gives the exact kernel sequence

    0 -> A_std O(-4) -> K^- -> ker gamma -> 0.          (10)

For example, locally a section of ker gamma can be lifted to K; its derivative lies in I and can be cancelled by a section of U because U->I is onto. This proves the right-hand surjectivity in (10), not just an equality of generic dimensions.

N is an ordinary quotient of a nonhorizontal subbundle. We do NOT identify gamma as a Gauss derivative for a flat connection on N, do not iterate it as such, and do not apply horizontal-negativity or endpoint capacity directly to N. Statements (8)-(10) are actual O-linear sheaf consequences of the original derivative.

For the first two N types, every ordinary degree is at least -7, so the O(-10) component of gamma is zero by degree. In the third type it can come only from the displayed O(-10) through a constant scalar, which is not presumed zero.

## 4. The V-row has rank two, so the endpoint cannot have rank one

Every surviving K contains a degree-minus-four V block in its equivariant splitting. The near-top coefficient lemma in the preceding theorem applies to the ACTUAL beta_K and makes its V coefficient map nonzero. More explicitly, any killed coefficient line O(-4) would have derivative inside a quotient of top at most -3, shifted by -2, and would therefore be a forbidden negative horizontal line.

The scalar component of this V-row into O is zero because

    Hom_G(V O(-4),O)=Hom_G(V,Sym4 W)=Hom_G(V,D)=0.

Its O(-10) component is zero by degree. Thus its nonzero image lies in W O(1), the rank-two part of A_q(-2).

Suppose this coherent image had generic rank one. On the smooth parameter line it would be an equivariant line bundle O(d), a quotient of V O(-4) and a subsheaf of W O(1). Global generation after twisting by four gives d>=-4; the injection into W O(1) gives d<=1. But for every such d,

    Hom_G(V O(-4),O(d))=Hom_G(V,Sym^(d+4) W)=0,

since Sym^n W for 0<=n<=5 is respectively 1,W,A_std,S4,D,T6, never V. There is no additional one-dimensional character because G is perfect. This contradicts the nonzero row. Its generic rank is therefore exactly two.

As K is an endpoint of the maximal rank-four plateau, rank beta_K<=3. We have proved

    rank beta_K is 2 or 3.                            (11)

If beta in (3) is nonzero, I has a nonzero scalar O component while the V-row spans W O(1) generically. They are independent, so rank beta_K=3. If beta=0, both ranks in (11) remain possible from the present argument. Combining (9) and (11), gamma has generic rank one or two, and has rank two whenever beta!=0.

This is an actual all-row rank obstruction derived from representation and sheaf constraints, not an evaluation of an instance matrix or a chosen coefficient.

## 5. Only two original determinant defects remain

Let S=Q*, L=S^- and B=S/L be the actual dual objects. The quotient A_q has degree zero, so the original negative-transpose determinant identity gives

    deg B=-8-t,   deg L=-46+t,   t>=0.

The actual coherent injection

    B -> A_q*(-2)=O(6)+O(-4)+W O(-5)                   (12)

bounds the top three ordinary B degrees by 6,-4,-5 respectively. To justify the componentwise bound, order both splittings decreasingly. If the j-th B degree exceeded the j-th target degree, its first j summands could map only into the first j-1 target summands, contradicting generic injectivity. No saturation of (12) is required.

The same three-column endpoint capacity applies to L, whose rank is nine and derivative rank at most three. Thus

    deg L <= max [6h1-4h2-5h3-sum hi(hi+1)],
    h1>=h2>=h3>=0, h1+h2+h3=9.                        (13)

Put y=h2, z=h3. The bracket equals

    -36+8y+7z-2y^2-2z^2-2yz
      = -53/2-2[(y-3/2)^2+(z-1)^2+(y-3/2)(z-1)].

The square bracket is nonnegative. Since the expression is integral, it is at most -27. Heights (6,2,1) or (7,1,1) attain -27, although equality is not required. Therefore

    -46+t<=-27, hence t<=19.                           (14)

The projective action factors through A5 of order60. A finite point stabilizer in P1 is cyclic, and A5 has nontrivial cyclic subgroup orders only2,3,5. Thus its orbits have sizes60,30,20,12. There is one exceptional orbit of each of the latter three sizes. Every effective invariant divisor has degree in the semigroup generated by12,20,30. The determinant of (12) is equivariant, so its effective zero divisor is invariant, including every ramified parameter. Combining this with (14) gives

    t is 0 or 12.                                      (15)

If t=0, (12) has nowhere-zero determinant and is an actual bundle isomorphism B=A_q*(-2). If t=12, its determinant divisor is the reduced exceptional orbit Delta of twelve points. At each point the determinant vanishes to order one; local Smith normal form gives a cokernel of length one. Hence the actual cokernel is an equivariant invertible O_Delta-module, not twelve trivial coefficient characters. Neither case is selected by this proof.

## 6. What remains open

The matched-graph identity is new actual-map information: the top source row, top derivative image, residual quotient target and kernel sequence are synchronized. The rank-two V-row removes derivative rank one at this specific endpoint, and the dual capacity/orbit argument restricts the original determinant defect to zero or twelve. These facts retain all three necessary K types until a further argument actually excludes one.

No horizontal splitting, canonical flat connection on N, arbitrary saturation replacement, or zero-defect premise is used. No actual coefficients, points, parameters, jets, tensors, instance matrices/ranks or scans are selected or computed. The small checks concern only universal representation identities, Euler kernels and quadratic degree bounds.

The top-three boundary and the full rank-four profile (1,1) remain open. No coarse-bin exclusion, generic rank improvement, square surjectivity, full-adjoint invertibility, smoothing, algebraicity or original repair follows. The inherited actual-source hypotheses remain explicit and are not certified merely by the arithmetic checks.
