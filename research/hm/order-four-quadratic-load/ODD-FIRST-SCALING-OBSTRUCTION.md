# The actual first odd scaling obstruction and its two root gates

## Results

Let Q=(q_+(x)+q_-(u,v)=0) be a smooth inversion-even quadric, R the positive fixed plane, C=Q intersect R, I=I_(C/Q), W=V_-*, and B=End_0(F). Assume the established actual plane and conic theorems; in particular every smooth C has splitting parameter a<=1. Balance is not required below.

On the fixed finite neighborhood Z=V(I^9), pull back the actual HM bundle by

    g_epsilon(x,u,v)=(x,epsilon u,epsilon v)

and consider the odd part of

    (I/I^9) tensor g_epsilon*B tensor O_Q(4).

Its special-fiber global sections form the actual thirty-dimensional space

    H0(B_R(3)) tensor W = Sym^2 D tensor W.

The first potentially nonzero parameter obstruction is at epsilon squared. Its ambient normal-degree-three expression is the cup/commutator

    nu_zeta: H0(B_R(3)) tensor W
          -> H1(B_R(1)) tensor Sym^3 W,
    s tensor w |-> [zeta,s] w.                         (1)

The displayed dimensions are 30 -> 24. However, the ACTUAL FIXED-QUADRIC obstruction is not this entire target. It is exactly the projection

    delta_q: H0(B_R(3)) tensor W
           -> H1(B_R(1)) tensor (Sym^3 W / q_- W),      (2)

followed by a canonical injection into the first-cohomology obstruction group of the finite family. Thus its effective target has dimension twelve. The discarded q_-W component dies through H1(B_R(3))=0, rather than being an additional independent obstruction.

If q_- has its two distinct projective roots lambda_1,lambda_2, evaluation identifies (2) with the direct sum of two actual cup maps

    mu_(zeta(lambda_j)): H0(B_R(3)) -> H1(B_R(1)),
    s |-> [zeta(lambda_j),s],           j=1,2.           (3)

Each has dimensions 15 -> 6. The actual cup formula and Steiner fiber injectivity prove that BOTH MAPS ARE SURJECTIVE. In fact the cup map associated to every nonzero coefficient in the actual A-channel is onto. Consequently (2) is onto twelve dimensions, with kernel exactly eighteen.

Equivariance forces the ambient map (1) to have a kernel containing a six-dimensional irreducible binary-icosahedral representation; its exact rank is not needed. The twelve independent actual first scaling obstructions give the generic bound h0(B_Q(4))_- <= 18 along every fixed smooth positive-conic and nondegenerate negative-block scaling direction. They do not prove that the remaining eighteen first-order survivors lift, or that the global odd space vanishes.

## 1. The actual flat finite scaling family

The support of Z is C, which is disjoint from the negative fixed line P(V_-). Consequently g_epsilon is a regular morphism on Z times A1 even at epsilon=0, where it equals the projection p onto R. For epsilon!=0 it is induced by a projective automorphism and carries Q to

    q_+(x)+epsilon^(-2) q_-(u,v)=0.                    (4)

The sheaf I/I^9 is fixed over the parameter line. Tensoring its constant family with the locally free g_epsilon*B and O_Q(4) gives a parameter-flat coherent family on the projective scheme Z times A1. The projection Z->R is finite: its coordinate algebra is generated over O_R by nilpotent negative coordinates. Pushing forward to R and taking inversion eigensheaves is exact; those eigensheaves are parameter-flat direct summands.

These facts justify ordinary deformation theory of sections and semicontinuity. They do not assert that a finite-neighborhood section lifts globally on Q.

## 2. Exact harmonic special fiber and its global sections

Since q_- is a nondegenerate binary quadratic, the polynomial ring in W is free over C[q_-]. Let H_l be its harmonic degree-l space: dimension one at l=0 and dimension two for l>=1. The choice of a harmonic complement can be made canonically using q_-; the final quotient in (2) does not depend on any complement.

In harmonic degree l, the ideal I^m maps under q_-=-q_+ to

    q_+^max(0,ceil((m-l)/2)) O_R(-l).

Thus I/I^9 in the odd degrees l=1,3,5,7, after twisting by four and tensoring B_R, has the exact O_R-module decomposition

    H_1 tensor B_R(3)|4C
      directsum H_3 tensor B_R(1)|3C
      directsum H_5 tensor B_R(-1)|2C
      directsum H_7 tensor B_C(-3).                    (5)

This is a decomposition of the finite module itself, not merely its associated graded. It uses freeness over C[q_-] and the actual equation of Q.

The plane Steiner resolution gives H1(B_R(2))=H1(B_R(3))=0, hence H1(B_R(-5))=0 by self-duality and Serre duality. The established plane lemma also gives H0(B_R(1))=0. Therefore

    H0(B_R(3)|4C)=H0(B_R(3)),
    H0(B_R(1)|3C)=0,
    H0(B_R(-1)|2C)=0.                                 (6)

The first equality follows from the restriction kernel B_R(-5); the second and third use the same kernel. Finally, the actual splitting bound a<=1 gives

    B_C = O_P1(2a+2) directsum O_P1 directsum O_P1(-2a-2),
    H0(B_C(-3))=0.                                    (7)

Here the plane hyperplane twist has degree two on P1. At twist three the symmetric-square Steiner resolution has terms O(-2),O(-1),O, so

    H0(B_R(3))=Sym^2 D,   dim=15.                      (8)

Combining (5)-(8) proves the thirty-dimensional special-fiber section identification, with every other harmonic summand contributing zero.

## 3. The first parameter obstruction is exactly the commutator cup

The actual first-normal projective comparison along R is uniquely split: inversion kills its obstruction and H0(B_R(-1))=0 makes the comparison unique. The actual second-normal projective class is

    zeta in Sym^2 W tensor H1(B_R(-2)).

Work modulo epsilon cubed. The pullback of J^3 under g_epsilon lies in (epsilon^3), so the pulled-back actual bundle algebra factors through the third normal neighborhood of R. In projective frames relative to the unique first-order comparison, its transitions have the exact form

    reference transition times (1+epsilon^2 ad(zeta_ij(u,v)))

modulo epsilon cubed. Thus the deformation is canonically constant to order epsilon, and its first potentially nonzero obstruction to lifting a special-fiber adjoint section is at order epsilon squared.

For s tensor w in (8) tensor W, the Čech obstruction is

    [zeta_ij,s] w.

It is a cocycle in normal degree three with plane coefficient twist one. This proves (1) as an actual cup/commutator, not a dimension-based replacement. Choosing the opposite transition convention changes its overall sign only. First-order parameter corrections to the section do not change this obstruction, since the bundle deformation has no term of order epsilon.

Equivalently, (1) is the first differential of order two in the epsilon-adic section-lifting spectral sequence, before applying the fixed-quadric relation. The fixed ideal I/I^9 and twist O_Q(4) introduce no additional deformation class: the ambient geometry Q is fixed and g_epsilon*O(4)=O(4) canonically on the projection domain.

## 4. Why the quadric target is twelve-dimensional

The normal cubic multiplication map sends

    B_R(1) tensor Sym^3 W

into the pushforward of the odd special fiber (5). Decompose a cubic modulo q_-W. Its harmonic degree-three component maps by restriction to

    B_R(1)|3C tensor H_3.

The q_-W component maps, using q_-=-q_+, through

    B_R(1) --(-q_+)--> B_R(3) -> B_R(3)|4C,

in harmonic degree one. On H1 this second component is zero because H1(B_R(3))=0. The first component is injective on H1 because

    H1(B_R(-5))=0

in the restriction sequence for B_R(1)|3C.

Consequently the induced map on H1 has kernel exactly

    H1(B_R(1)) tensor q_-W.

It yields a canonical injection

    H1(B_R(1)) tensor (Sym^3 W/q_-W)
       -> H1(odd special fiber).                      (9)

Any change of cubic lift differs by q_-W and therefore has zero image, so this injection and the factorization (2) are independent of a harmonic splitting. This proves that vanishing of (2) is precisely the first parameter-lifting condition; no unrecorded part of the order-epsilon-squared obstruction remains.

## 5. The two root gates are actual, not independently chosen maps

Let Z(q_-) be the reduced divisor of two points in P(W*). Restriction of linear and cubic forms gives canonical isomorphisms

    W = H0(O_(Z(q_-))(1)),
    Sym^3 W/q_-W = H0(O_(Z(q_-))(3)).                 (10)

The first follows because two distinct points impose independent conditions on linear forms. The second is the degree-three part of the ideal of the binary quadratic.

Under (10), polynomial multiplication is fiberwise. Hence the j-th component of (2) is the cohomological commutator with the actual evaluated normal class

    zeta(lambda_j) in H1(B_R(-2)) tensor O_(lambda_j)(2).

The source and target retain the evaluation lines O_(lambda_j)(1) and O_(lambda_j)(3). Trivializing those one-dimensional factors displays the maps as (3); their ranks and kernels are independent of these trivializations.

The nonzero invariant zeta identifies (Sym^2 W)* with its actual irreducible three-dimensional summand in H1(B_R(-2)). A nonzero evaluation vector lambda_j squared therefore maps to a nonzero class. Distinct projective roots give independent squared vectors, so the two evaluated classes are independent.

The nonzero ambient coefficient injection alone does not establish cup surjectivity. The following sections prove the required additional structural fact from the actual Steiner presentation.

## 6. Functorial derivation of the actual cup formula

Write the actual Steiner tensor as

    t:A tensor V -> D,
    phi:(a wedge b) tensor v |-> a tensor t(b,v)-b tensor t(a,v).

The established symmetric-square calculation identifies

    H1(B_R(1))=coker(phi),
    phi:wedge^2 A tensor V -> A tensor D.              (11)

The dual Steiner sequence tensored by F_R(-2) identifies

    H1(End(F_R)(-2))=D* tensor H1(F_R)=Hom(D,A),         (12)

because F_R(1) is acyclic. The isomorphism in (12) is specifically the action of an extension class y on global sections:

    y:D=H0(F_R(2)) -> H1(F_R)=A.

Indeed, pullback of the extension along the evaluation map is exactly the cohomology map induced by the dual Steiner sequence. The trace part contributes nothing since H1(O_R(-2))=0.

A first-order deformation with square-zero coefficient O_R(-2) therefore sends a symmetric product d e in H0(B_R(3))=Sym^2 D to

    sigma_y(d e)=y(d) tensor e+y(e) tensor d

followed by the natural cup quotient A tensor D -> coker(phi). This is the Leibniz rule for the boundary of a symmetric product of locally lifted sections of F_R(2). The determinant correction is canonically trivial, since H1(O_R(-2))=H0(O_R(-2))=0. Hence it is the same adjoint commutator boundary used in (1).

For clarity, the cup quotient is exactly the one in (11), not an arbitrary map with that dimension. Represent a class of H1(F_R) by a Čech cocycle and lift it to D O(-2). Its coboundary lifts through t to a cocycle in A O(-3), representing the standard H2 description of H1(F_R). Multiplying by a constant d in D lifts the symmetric cocycle to Sym^2 D O(-2); its coboundary lifts to the corresponding tensor in A tensor D O(-3). This is precisely the quotient supplied by the symmetric-square resolution. Thus, with a consistent symmetric-product normalization,

    mu_y(S) = class of sigma_y(S) modulo im(phi).       (13)

Any alternate conventional normalization multiplies this whole formula by a nonzero scalar and does not change the conclusions below.

## 7. Surjectivity for every actual nonzero coefficient

Use the invariant nondegenerate quadratic form on A. The genuine five-space is

    D = Sym^2_0 A,

the traceless self-adjoint endomorphisms of A. There is a nonzero equivariant map

    A -> Hom(D,A),    a |-> y_a,    y_a(S)=S a.

The A-constituent occurs with multiplicity one in Hom(D,A). Since the actual zeta is nonzero and Sym^2 W=A, its coefficient injection is this map up a single nonzero scalar. Thus all actual nonzero coefficient classes are covered by y_a with a!=0.

First, y_a is surjective, including for isotropic a. Its dual sends b to the trace-free part of a symmetric b. If this is zero, then

    a tensor b+b tensor a = (2/3)(a,b) Id.

The left side has rank at most two. If (a,b) were nonzero the right side would have rank three, a contradiction. Therefore a symmetric b=0; with a!=0 this implies b=0. The dual is injective, proving the claim. In particular ker(y_a) has dimension two.

For any surjective y:D->A define

    psi_y:A tensor D -> wedge^2 A,
    psi_y(a tensor d)=a wedge y(d).

Then

    im(sigma_y)=ker(psi_y).                            (14)

The inclusion follows immediately from the symmetric formula. To verify equality, split D as ker(y) directsum a copy of A. The symmetric map has image Sym^2 A directsum (A tensor ker(y)), of dimension 6+6=12. The map psi_y is onto a three-space, so its kernel has that same dimension. This is universal linear algebra, not an evaluation of the actual Steiner tensor.

It remains to prove that psi_y(im(phi))=wedge^2 A. For v in V put

    L_v=y_a t_v in End(A).

The scalar trace(L_v) is an invariant bilinear form in a and v. The actual representations A and V are the two DISTINCT irreducible A5 three-spaces, so this invariant bilinear form is zero. Consequently, under wedge^2 A=A* using an invariant volume, the map

    psi_y phi(- tensor v):wedge^2 A -> wedge^2 A

is the exterior derivation induced by L_v, namely

    trace(L_v) Id-L_v* = -L_v*.

If their images failed to span wedge^2 A, a nonzero common annihilator w in A would satisfy

    L_v w=0 for every v in V.

That says t(w,V) is contained in ker(y_a), a two-dimensional space. But t_w:V->D is injective whenever w!=0: if t(w,v)=0 with v!=0, the Steiner fiber map t_v:A->D at [v] would fail injectivity. Thus t(w,V) has dimension three, a contradiction. We have proved psi_y(im(phi))=wedge^2 A.

Combining this with (14) gives

    A tensor D = im(sigma_y)+im(phi).

Formula (13) therefore proves the ACTUAL SURJECTIVITY

    mu_(y_a):H0(B_R(3)) -> H1(B_R(1))

for every a!=0. Each root gate (3) is an instance of this theorem. Hence delta_q has rank exactly twelve for every nondegenerate q_-.

## 8. The actual generic odd-section bound

Let M be the coherent finite scaling family of Section 1. Near epsilon=0, its pushforward of global sections is a torsion-free module over the parameter local ring: multiplication by epsilon is injective on M because M is flat. Over the discrete valuation ring this pushforward is free. Its fiber injects into H0(M_0), by the cohomology sequence of multiplication by epsilon, and its image consists of sections lifting to every parameter order. In particular that image lies in ker(delta_q).

Thus the generic fiber of M has at most eighteen global sections. For epsilon!=0 it is the actual odd finite-neighborhood space on the quadric (4). Uniform H0(I^9 B_Q(4))=0 follows from the established H0(I^7 B_Q(4))=0. Therefore global odd adjoint sections inject into that finite space, and

    h0(B_(Q(epsilon))(4))_- <= 18

for general epsilon!=0. The same argument works for every fixed smooth positive conic and every nondegenerate negative-block direction. It does not assert that all eighteen first-obstruction survivors lift to actual global sections. Higher parameter and neighborhood obstructions may reduce this bound further.

## 9. Forced binary-normalizer representation constraints

Write A=Sym^2 W, let V be the other genuine three-dimensional A5 representation, let D be the genuine five-space, and let P denote the genuine four-dimensional A5 representation. Let S and T be the irreducible binary representations of dimensions four and six with negative central character. Let W' be the other binary two-space. The universal character identities are

    Sym^2 D = 1 directsum P directsum 2D,
    W tensor P = W' directsum T,
    W tensor D = S directsum T,
    A tensor S = W directsum S directsum T,
    V tensor S = W' directsum S directsum T,
    Sym^3 W=S.                                        (12)

They follow equally from the binary-icosahedral character table or the symmetric-power recurrence for a determinant-one two-space. The accompanying verifier checks them using only the abstract conjugacy-class sizes and traces, with exact arithmetic in Q(sqrt(5)). It evaluates no HM presentation.

Since H1(B_R(1))=V directsum A, (12) gives

    source of (1) = W + W' + 2S + 3T,
    target of (1) = W + W' + 2S + 2T.                  (13)

The actual zeta is invariant, so (1) is equivariant. Semisimplicity forces its kernel to contain at least one copy of T, of dimension six. Equality would require all actual multiplicity maps to have maximal rank and is not claimed.

A fixed general q_- is not normalizer-invariant. Thus the projected map (2) must not be assigned the full equivariant block decomposition (13). Its exact root decomposition, not a fictional invariant target, is the appropriate structural statement.

## Scope

This proves the exact first deformation obstruction of the actual finite scaling family, the necessary projection from 24 to 12, surjectivity of both actual root gates, the resulting generic odd-section bound eighteen, and the representation-forced ambient kernel. It does not prove that a survivor extends to higher epsilon order, extends through a thicker conic neighborhood, or is a global section on Q. The separate generic I^3-vanishing theorem ensures global odd sections are detected by their leading first normal jet, but does not remove these lifting conditions.

Dependencies: the actual zeta nonvanishing theorem is published at b3fc992ebba27fc28967f934bf9966148eb86961; its definition and affine law at 028320f238a8a8cae5f14faf6b6836201baa496d; the plane Steiner and uniform conic splitting results, plus the exact H0(B_R(1)) and H1(B_R(1)) lemma, are the established fixed-plane notes. The finite scaling construction and exact harmonic decomposition are those checked in the generic I^3 theorem. No selected coefficients, matrix evaluation, rank scan, experiment, or public write is used.
