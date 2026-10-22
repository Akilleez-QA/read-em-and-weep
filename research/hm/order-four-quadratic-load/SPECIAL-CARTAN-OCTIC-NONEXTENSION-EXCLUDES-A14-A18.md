# A special Cartan octic cannot extend: exclusion of scalar a=14 and a=18

## Result and scope

At an order-five hyperplane H, the actual boundary delta_H(q0 P4) is nonzero. Consequently the scalar Cartan image alternatives a=14 and a=18 are impossible. The proof uses only the established actual section-curve geometry, weight decompositions, and a Wronskian bound for a four-dimensional binary-octic series. No selected HM coefficients, actual matrix, or rank evaluation is used.

Use the notation of SPECIAL-FIBER-PRIMARY-VANISHING-AND-EXACT-OCTIC-GATE.md. In particular C=Q disjoint-union Y is the zero curve of the actual nonvertex eigensection w, and R=(u=0). Positive-plane coordinates have point weights (x,y,z)=(0,1,4) modulo five. The invariant smooth conic has equation

    q0=rho x²+sigma yz, rho sigma != 0.

The section conics are denoted q_c and q and must not be confused with q0. Write q(y,0)=A y², a=c y, b=kappa z² and tau=cA/kappa != 0. Let Z=C intersect R.

## 1. The actual cubic wedge space

At p=[1:0:0], Z has ideal (z,y²). At r=[0:0:1], it has ideal

    (x-tau y³, y⁴)

in the affine chart z=1. The latter follows from the ribbon chart b!=0: I_Y=(g,q²), with g=kappa xz²-c yq. There is no other support. Direct imposition of these two local conditions on homogeneous cubics gives

    H0(I_Z(3)) = span{S, G, J, K},
    S=x²z, G=xz²-tau y³, J=xyz, K=xy².             (1)

For completeness, at p the coefficients of x³ and x²y must vanish. At r the coefficients of z³, yz² and y²z vanish, while those of xz² and y³ satisfy their single indicated relation. The remaining four directions are exactly (1).

The regular plane-section sequence is

    0 -> O_R --w_R--> F_R(2) -> I_Z(3) -> 0.

Since H1(O_R)=0, wedge against w_R induces an isomorphism

    D5/Cw_R -> H0(I_Z(3)).                         (2)

Choose binary coordinates X,Y on W with order-five weights 1,4, and ell=X. The actual two-space is X³W, with t=X⁴ of weight4 and w=X³Y of weight2. Thus the four other monomials of D5=Sym⁴W map under (2), up to individually nonzero constants, as follows:

    X⁴ -> S, X²Y² -> G, XY³ -> J, Y⁴ -> K.         (3)

Indeed polynomial function weights of S,G,J,K are respectively 1,2,0,3; wedge with w adds weight2. Each displayed weight space is one-dimensional, and (2) makes every constant nonzero. No value of a constant is selected.

## 2. A forced nonzero binary-octic coefficient

The actual Cartan space Sym⁸W decomposes as P4 plus D5. Restricting P4 to the order-five subgroup gives its four nontrivial characters, each once. Its weight1 line therefore lies inside

    span{X⁷Y, X²Y⁶}.

Write a nonzero element of this line as

    v=A1 X⁷Y+A6 X²Y⁶.

We claim A6!=0. Otherwise X⁷Y belongs to the four-dimensional G-stable subspace P4 of H0(P1,O(8)). This subspace has no basepoint: its common-zero divisor would be G-stable of degree at most8, whereas every nonempty orbit of the icosahedral action on P1 has size at least12.

The Wronskian of a basepoint-free four-dimensional degree-eight linear series is a nonzero section of O(20). This follows directly by taking the determinant of a basis and its first three derivatives; in characteristic zero it is nonzero, and its coordinate-change degree is 4*(8-3)=20. At a point with vanishing sequence a0<a1<a2<a3, its order is sum(ai-i).

The section X⁷Y vanishes to order7 at one order-five fixed point. G-stability would give such a section at every point of its orbit of size12. At each point the Wronskian order is at least 7-3=4. That would require a Wronskian divisor of degree at least48, contradicting degree20. Hence A6!=0.

This argument is a representation-theoretic nonvanishing proof, not an evaluation of the actual Cartan coefficients.

## 3. Its actual shadow has a forbidden trace monomial

The Cartan inclusion Sym⁸W into Sym²(Sym⁴W) is the standard polarization. The monomial X⁷Y maps to a nonzero multiple of X⁴ times X³Y and hence has zero wedge shadow. The monomial X²Y⁶ maps to a sum with nonzero coefficients of

    (X²Y²)(Y⁴) and (XY³)².

By (3), its wedge shadow is therefore a nonzero multiple of G K plus some multiple of J². On z=0, J vanishes and G K=-tau x y⁵. Thus

    mu_w(v)|z=0 = nonzero constant times x y⁵.

Multiplication by q0 and restriction to z=0 now give

    (q0 mu_w(v))|z=0 = nonzero constant times x³y⁵. (4)

Every nonzero factor used here has been proved nonzero: A6, the polarization coefficient, both wedge constants, tau and rho.

## 4. Every extendible octic has a different trace space

Suppose f=q0 mu_w(v) were the restriction of F in H0(H,I_C²(8)). On Pi=(z=0), membership in I_Q² gives

    F|Pi=q_c² r4

for a quartic r4. The intersection T=Y intersect Pi has ideal sheaf (x²,q). Since q_c is invertible near T and restriction of an ordinary ideal square has image the ordinary square, r4 belongs to H0(I_T²(4)). The complete-intersection square resolution, or its three independent degree-four generators, gives

    H0(I_T²(4))=span{x⁴,x²q,q²}.

Restricting further to u=0 consequently gives

    F|z=u=0 in span{x⁴y⁴, x²y⁶, y⁸}.              (5)

Equation (4) contradicts (5). Therefore the actual octic f does not extend.

## 5. Boundary and scalar-image consequence

Naturality of the symmetric-square section sequence sends delta_H(q0v) to the ordinary-square extension obstruction of f. Nonextension therefore proves delta_H(q0v)!=0; this implication does not even require the stronger primary vanishing proved in the companion note. That vanishing additionally identifies the entire five-dimensional obstruction spaces.

The actual equivariant Cartan boundary is phi:Sym⁸W tensor O_T -> F4(2). The source v just constructed has stabilizer weight 1. The proven nonzero boundary therefore gives a nonzero weight-1 vector in the actual image fiber at ell=X.

To fix the line-bundle convention, O_T(-1) has fiber C X of weight1 at this point, so O_T(1) has fiber weight -1. This convention independently matches the actual section bundle Y2=W O(-3): its fiber weights are 1+3=4 and 4+3=2, exactly the actual t,w weights used in (3). No sign or character is inferred merely from an unequivariant splitting.

If the actual Cartan image lies in a scalar summand O_T(a+2), its fiber weight here is -(a+2) modulo five. For the three scalar possibilities this is

    a=12: weight1; a=14: weight4; a=18: weight0.

Equivariance and the nonzero source-weight-1 value exclude a=14 and a=18. The a=12 character is compatible and remains open. Independently, the a=18 exceptional-zero theorem in SCALAR-CARTAN-BOUNDARY-OCCURRENCE-GATES.md says its P4 boundary would vanish at all twelve order-five parameters, already contradicting the nonextension result.

In the seven-type classification, type IV is A O(2) plus O(18), and type VII is O plus W O(3) plus O(18). Their established low-coupling vanishings force the nonzero Cartan image into the a=18 scalar summand. They are therefore impossible actual F4 types, reducing seven listed types to five.

For type VI, O plus W-prime O(5) plus O(14), vanishing of the W-prime O(5) coupling would force the a=14 scalar case, now impossible. Thus that coupling is nonzero and the no-off-diagonal-divisor theorem gives generic residual rank four in type VI unconditionally. Combined with the same theorem for types I, II and V, generic residual rank two is now possible only in type III with its V O(4) coupling zero, leaving scalar a=12.

Historical conditional a=14 and a=18 kernel arguments remain valid conditionals about branches now excluded; they need not be rewritten. This result does not exclude scalar a=12 and does not claim the full proof repair is complete. The actual-image alternatives must be updated only after independent checking.

## Dependencies

The actual special curve and its ideal sheaves are in SPECIAL-HYPERPLANE-ADJOINTS-ARE-EXACTLY-SQUARES.md, immutable special-source commit d29d27e5c92cf105b60bce4e828f4860582a2bee. ACTUAL-CHORD-INCIDENCE-AND-CONIC-EVALUATION.md supplies the actual Cartan two-space X³W. SPECIAL-FIBER-ORDINARY-SQUARE-EXTENSION-CRITERION.md gives the naturality comparison. The companion primary-vanishing note supplies the same trace geometry with its full parameter justification. Other filenames here are dependency identifiers, not claims that each exists at the immutable special-source commit.
