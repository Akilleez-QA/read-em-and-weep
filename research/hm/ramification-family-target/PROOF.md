# Three-coefficient ramification target on the joining lines

## Result and scope

Let Gamma be the binary icosahedral group. Write W for the negative binary representation, U for the other binary representation, V=Sym^2 U, A=Sym^2 W, and D for the five-dimensional representation. Retain the actual equivariant cubic isomorphism f:Sym^3 W -> Sym^3 U and all nonzero marked monad scalars. Assume the published smooth invariant bicubic and complete global transvection presentation.

The ramification pairs of the projection to P(W) canonically match the positive and negative eigenlines of every order-five subgroup. Their twelve joining lines in physical P(V* + W*) are stabilized pointwise by C5; the center reverses the relative scale. A ramification pair is NOT a canonical point on its joining line.

For any Gamma-equivariant P2=Sym^2 A tensor D family of global skew middle operators of twist four, the forced mixed functional on each joining line has exactly the following *allowed form*:

    lambda_(s w) pi(T_(t v,s w) Y_(t,s))
      = t s^7 L_1 + t^3 s^5 L_3 + t^5 s^3 L_5.        (1)

Here the coefficients are linear in P2, and the actual right-hand side is supported only in the middle coefficient. Their intrinsic receiving bundle on the twelve ramification pairs is

    O_R(3,7) + O_R(7,5) + O_R(11,3).                  (2)

Each summand has section representation V+P+D, with P the even four-dimensional irreducible. Consequently the equivariant family receiving space has dimension 18. This is a codomain theorem, NOT a claim that the 1203-dimensional operator family, or its 1113-dimensional vertex-preserving subspace, maps onto that codomain. It produces three simultaneous coefficient conditions, not merely six conditions at one arbitrarily chosen physical orbit.

## 1. Stabilizer matching from smoothness, with no actual evaluation

Take a generator g of C10 and a primitive tenth root zeta. The eigenweights of W are +/-1; those of U are +/-3. Use bases ell_+,ell_- and r_+,r_- with those weights. Symplectic identification of W with W* is equivariant, so it does not change an eigenweight.

An invariant bicubic monomial with i negative positive-spinor factors r_- and j negative negative-spinor factors ell_- has weight

    3(3-2i)+(3-2j) = 12-6i-2j mod 10.

Thus its only allowed monomials, on the chart x=r_-/r_+, y=ell_-/ell_+, have the exact form

    F(x,y)=a0 y + b0 x^2 + c0 x y^3 + d0 x^3 y^2.     (3)

These symbols denote free coefficients of the invariant restriction; none is evaluated. At (0,0), smoothness forces a0 != 0. At the other positive eigenline with the same negative eigenline, using X=1/x, the equation is

    a0 y X^3 + b0 X + c0 y^3 X^2 + d0 y^2.

Smoothness there forces b0 != 0. Hence at the matched point

    y=-(b0/a0)x^2 + higher-order terms,

and the negative projection has simple ramification. The opposite matched eigenlines give the second such point for this C5 subgroup. Six C5 subgroups give twelve distinct pairs. Riemann--Hurwitz for the degree-three map from the smooth (3,3) genus-four curve gives total ramification twelve, so these exhaust R. This also proves reducedness without an actual coefficient or point computation.

At the matched pair, physical v=r^2 has g-weight 6 and w has weight 1. Under g^2 both have weight 2 modulo ten. Thus C5 fixes their entire joining line projectively. The central element g^5 acts as +1 on v and -1 on w. A mixed physical point has C5 stabilizer and a 24-point Gamma orbit; its central partner is the opposite relative scale. The endpoints have the larger C10 stabilizer. The twelve joining lines are disjoint because both projections of R are injective.

## 2. The matched source vector and its relative-scale dependence

Use the actual marked arrows

    A_x(u)=u i_v tau,
    B_x(u)=i_x(L(u) wedge omega),
    C_x(z)=i_x Ctilde(z),

where Ctilde lies in U tensor Lambda^2 V tensor W. In particular A has only VV output; C has VV and VW output; the WW component of B is M(v)u. Let c=b_m/a_m, a fixed nonzero ratio of monad channel scalars. This c must not be confused with the variable negative quadratic source a(w).

At a ramification pair take u=r in ker M(v). By the published Cartan/source argument there is a unique z0 in Sym^2 W satisfying

    C_VV(w,z0)=A(v,u),       z0(w) != 0.

All fixed actual scales are retained. At x=(t v,s w), for s != 0, use z=(t/s)z0. Set

    C_mix = C_VW(v,z0),       B_mix = B_VW(w,u).

The full VV terms cancel, and B_WW=M(tv)u=0. There is no WW term left. Exactly,

    Y_(t,s) = (t^2/s) C_mix - c s B_mix.               (4)

Multiplying by s regularizes Y. No physical point, source coefficient, matrix, or rank has been selected or evaluated.

## 3. Why a degree-four ambient representative exists

This requires proof: an arbitrary bundle endomorphism need not extend automatically. Here it follows from the complete transvection presentation.

Let p=i_x P0 and q=i_x Q0 for constant U-valued three-forms P0,Q0. For eta in E_x=U tensor ker(i_x on Lambda^2 H), the exterior identity gives

    epsilon(q wedge eta)=i_x epsilon(Q0 wedge eta).

The expression epsilon(Q0 wedge eta) is a top five-form, hence a constant ambient linear functional b_Q0(eta) times the fixed volume Omega. Therefore, with the marked determinant-valued middle pairing,

    beta(q,eta)=b_Q0(eta).

There is no coordinate denominator. The transvection

    p beta(q,-)+q beta(p,-)

extends to the ambient polynomial matrix p b_Q0+q b_P0, homogeneous of degree one in x. The complete presentation says cubic scalar multiples span all twist-four global skew operators. Hence each has an ambient polynomial degree-four representative. This extension is asserted only as an ambient linear map, not as an ambient skew map. Its restriction to E is the desired operator.

Averaging the presentation over Gamma provides an equivariant extension for an equivariant family. Since P2 is center-even, its mixed-input-to-VV-output block has odd W-coordinate degree: center acts +1 on U V W and -1 on U Lambda^2 V. Accordingly this block has only bidegrees

    (positive degree, negative degree) = (1,3),(3,1). (5)

Different ambient representatives agree on E. Since Y lies in E, the final functional and all three extracted coefficients are independent of the representative.

## 4. Exact receiving bundle and scalar degrees

The quotient functional lambda_w on the Cartan VV summand is cubic evaluation in w, so lambda_(s w)=s^3 lambda_w. Applying a block t^j s^(4-j), with j=1 or 3 from (5), to (4) gives the terms

    C term: t^(j+2) s^(6-j),
    B term: t^j s^(8-j).

These are precisely the three monomials in (1). The possible pole in Y is canceled; the scalar expression extends across both endpoints. It vanishes at least to order one at the vertex endpoint t=0 and at least to order three at the positive endpoint s=0. This extension does not assert that the chosen source vector z itself extends there.

For the intrinsic degrees, change binary frames r -> alpha r, w -> beta w. Then v -> alpha^2 v and u -> alpha u. The uniquely matched source scales as z0 -> alpha^3 beta^-1 z0. Consequently

    C_mix -> alpha^5 beta^-1 C_mix,
    B_mix -> alpha beta B_mix,
    lambda_w -> beta^3 lambda_w.

The three extracted coefficients have degrees (3,7), (7,5), (11,3) in (r,w), proving (2). This is a statement about the natural homogeneous line-bundle values, not a choice of twelve arbitrary scalars.

The actual forced identity is

    lambda_w pi(TY)=2k a(w)^2 h(v) z(w),

where a is negative quadratic, h is positive quadratic, and z(w) denotes QUADRATIC evaluation because z lies in Sym^2 W. In particular z=(t/s)z0 gives z(s w)=t s z0(w), not t z0(w). Along the joining line the right-hand side is exactly

    t^3 s^5 [2k a(w)^2 h(v) z0(w)].                  (6)

It belongs to O_R(7,5). Thus the full linewise condition is L_1=0, L_5=0, and L_3 equal to the marked expression in brackets. No one of these three conditions is discarded.

## 5. The eighteen-dimensional equivariant target

For O_R(p,q), a stabilizer frame has homogeneous character zeta^(3p+q), while its fiber carries the inverse character. The three exponents are 16,26,36, all congruent to 6 modulo ten. They are center-even, with identical nontrivial C5 character. Each section module is therefore

    Ind_(C10)^Gamma(zeta^-6) = V + P + D.

One can alternatively obtain the dimension without naming irreducibles. D restricted to C5 is its regular representation. Tensoring a regular representation by any six-dimensional representation yields six regular copies. Thus

    P2|C5 = (Sym^2 A tensor D)|C5 = 6 Reg(C5).

By Frobenius reciprocity each of the three weighted 12-orbit targets receives a six-dimensional equivariant source-family space. Therefore

    Hom_Gamma(P2, H0(R,O(3,7)+O(7,5)+O(11,3)))
       has dimension 6+6+6 = 18.                    (7)

Equivalently P2=1+A+V+2P+3D gives 1+2+3=6 against V+P+D. This does not identify the image of the global operator restriction map. The exact map from the 1203-dimensional family, and its restriction to the 1113-dimensional vertex kernel, is a remaining interface with the coupled source equations.

The resulting homogeneous kernel bounds are unconditional: the full family map has kernel dimension at least 1203-18=1185, and the restriction to the vertex-preserving family has kernel dimension at least 1113-18=1095. These are bounds, not assertions of exact rank. They concern homogeneous zero-functional conditions, not existence of an inhomogeneous solution with prescribed vertex data.

## 6. The prescribed middle map fills its scalar target

There is also a stronger statement about the prescribed right-hand side, distinct from operator realization. The polarized map

    P2 -> H0(R,O_R(7,5)),
    (a symmetric-tensor a) tensor h
       -> 2k a(w)^2 h(r^2) z0(w)                     (8)

is onto as an ordinary Gamma-module map. Here pure squares span the symmetric square, so polarization defines the displayed linear map on all P2.

Indeed multiplication Sym^2(Sym^2 W*) -> Sym^4 W* is onto, with one-dimensional invariant kernel, and D identifies with Sym^4 U*. Thus source multiplication fills H0(P1 x P1,O(4,4)). The ramification scheme is the complete intersection of the two positive partials of F, each of bidegree (2,3). Its twisted Koszul sequence is

    0 -> O(0,-2) -> 2 O(2,1) -> I_R(4,4) -> 0.

On P1 x P1, H1(O(2,1))=0 and H2(O(0,-2))=0. Hence H1(I_R(4,4))=0, proving that restriction to H0(R,O_R(4,4)) is onto. Finally z0(w) is a nowhere-zero section of O_R(3,1), by the marked source lemma. The equivariance of the marked source inverse makes this section Gamma-invariant; consistently, its stabilizer homogeneity is 3*3+1=10, hence trivial. Multiplication by it and by the nonzero constant 2k is therefore a Gamma-equivariant isomorphism onto O_R(7,5).

Its ordinary source kernel consequently has representation 1+A+P+2D and dimension eighteen. This ordinary parameter kernel is different from the eighteen-dimensional space of equivariant coefficient homomorphisms in (7); the equal dimensions must not be conflated.

This proves that the required middle-coefficient map uses the entire V+P+D value representation, not only a proper subrepresentation. It is a structural consequence of exact multiplication, cohomology, and the known nonvanishing statement, not an actual source-instance matrix/rank evaluation. It does NOT show that the global operator-family map attains this prescribed homomorphism together with both zero outer coefficients and all coupled source conditions.

## 7. What one physical orbit misses

After setting s=1, the functional is rho L_1+rho^3 L_3+rho^5 L_5. One nonzero relative scale imposes only one six-dimensional combination of the three coefficient targets. It cannot certify the polynomial identity on all joining lines.

Formally, three nonzero scales rho_i with pairwise distinct squares recover all three coefficients: divide each value by rho_i and use the Vandermonde matrix in rho_i^2, whose determinant is the product of their pairwise differences. Central partners add no independent condition. This is a universal polynomial identity, not an instruction to evaluate the actual source at three selected points. Coefficient comparison directly avoids any such evaluation.

## Dependencies and verification status

Pinned public dependencies:

- [Actual mixed-value identity](https://github.com/Akilleez-QA/read-em-and-weep/blob/8d8b5be4ce62c3055bb53be9e16d29cc63072f04/research/hm/order-four-quadratic-load/ACTUAL-RAMIFICATION-DETECTS-A-NONZERO-MIXED-FORM-MIDDLE-VALUE.md), PR543: the marked Y, nonzero z0(w), and forcing identity.
- [Actual ramification and source correction](https://github.com/Akilleez-QA/read-em-and-weep/blob/8d8b5be4ce62c3055bb53be9e16d29cc63072f04/research/hm/order-four-quadratic-load/ACTUAL-RAMIFICATION-FORCES-A-NONTRIVIAL-PRINCIPAL-U-SOURCE-CORRECTION.md), PR543: the smooth bicubic, cubic-evaluation functional, and source inverse.
- [Universal marked channel formulas](https://github.com/Akilleez-QA/read-em-and-weep/blob/8d8b5be4ce62c3055bb53be9e16d29cc63072f04/research/hm/order-four-quadratic-load/UNIVERSAL-MONAD-CLIFFORD-HOMOTOPY-AND-HAMILTONIAN-DEFECT.md), PR543: A, B, C and the determinant-valued middle pairing.
- [Scalar ramification interpolation](https://github.com/Akilleez-QA/read-em-and-weep/blob/14aa94109bd251bc5921038142a4ea95fe605202/research/hm/ramification-interpolation/PROOF.md), PR675: the (2,3),(2,3) complete intersection and O(4,4) restriction used in Section 6.
- [Complete global skew-middle presentation](https://github.com/Akilleez-QA/read-em-and-weep/blob/b7fd2c946b39301bdb226af362674e1b2e755097/research/hm/global-skew-middle-presentation/PROOF.md), PR676: cubic-transvection spanning.
- [Complete equivariant middle family](https://github.com/Akilleez-QA/read-em-and-weep/blob/e8dc002a6de60d5feac936b2b291188fd2bdc6a9/research/hm/equivariant-middle-family/PROOF.md), PR677: the source representation and dimensions 1203 and 1113.

The proof is structural. The bounded verifier checks only universal integer weights, degrees, regular-representation convolution, and the three-monomial determinant. It does not formally verify the geometric inputs, evaluate f, select actual HM points or parameters, construct actual matrices, or compute source ranks. No operator-restriction surjectivity, coupled primitive, higher-order Bockstein, or algebraicity conclusion is claimed.
