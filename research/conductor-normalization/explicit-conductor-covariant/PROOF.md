# Explicit binary-quartic conductor covariant and its complete syzygies

Work over C. This note determines universal polynomials, not the action of those polynomials on the actual HM cohomology module. No selected quartic, HM map, source, obstruction value, or rank is evaluated.

## 1. Normalization of invariants

Write f=a x^4+4b x^3y+6c x^2y^2+4d xy^3+e y^4 and S=C[a,b,c,d,e]. Set

    i=ae−4bd+3c², k=ace+2bcd−ad²−b²e−c³,
    I=3i, J=54k, Δ=4I³−J².

The nonzero scalar in the usual discriminant is immaterial. For q=u x²+2vxy+w y² and f=q², direct substitution gives

    I=D², J=−2D³, D=2(v²−uw).

These conventions avoid confusing the relation i³=27k² with Δ=0. The triple-root cone N is V(I,J). Write W for the reduced square-quadratic cone. The previously proved conductor theorem gives the reduced ideal K=I_(N∪W), with minimal resolution

    0→S(−5)^4→S(−4)^5→K→0,

and K_4 is an irreducible V_4 of dimension five. All ideal claims below include the affine vertex; alternatively they sheafify on P⁴.


### Regular-pair clarification

For clarity, the regular-pair input used in the uniqueness argument can be checked from the displayed invariants. The quadratic I=3(ae-4bd+3c^2) is nondegenerate in five variables, hence irreducible. If the invariant cubic J were divisible by I, the quotient would be an invariant linear form on the irreducible nontrivial quartic representation; no such nonzero form exists. Thus I,J are a regular sequence. Universal substitution of l^3 m gives I=J=0, so their degree-six complete intersection contains the triple-root surface N. That irreducible surface has degree six by the (3,1) parametrization. The complete intersection is unmixed and has generic multiplicity one, hence is reduced, giving N=V(I,J). This is the same regular-sequence/degree argument used in the fourth-power manuscript, now stated for the displayed invariant normalization. No selected quartic or HM map is evaluated.

## 2. Universal explicit generator theorem

Consider the polynomial covector

    j=2I dJ−3J dI=Σ j_r dr,  r∈{a,b,c,d,e}.

Its five coefficients are quartics. They vanish on N immediately. On the dense open subset of W with D≠0, the discriminant differential vanishes: a quartic with two distinct double roots is a singular point of the discriminant. Thus

    0=dΔ=12I²dI−2JdJ=12D⁴dI+4D³dJ,

so dJ=−3D dI and j=2D²(dJ+3D dI)=0 there. Each coefficient is a polynomial, and W is reduced and irreducible, so j vanishes on all W, including fourth powers. Therefore span{j_r}⊂K_4.

This polynomial covector is SL₂-equivariant since I,J are invariant. Its coefficient map from the five-dimensional quartic representation to S_4 is equivariant; the representation is self-dual and irreducible. It is nonzero: after removing the common factor 162, the a-coefficient is

    2i(ce−d²)−3ke,

whose coefficient of b²e² is 3. This is a formal coefficient identity, not evaluation at a polynomial instance. Hence its coefficient map is injective, its image has dimension five, and

    span{j_a,j_b,j_c,j_d,j_e}=K_4,
    (j_a,j_b,j_c,j_d,j_e)=K.

The last equality uses the proved quartic generation, not merely equality of zero sets. The invariant nondegenerate polar form g(v,w)=(I(v+w)−I(v)−I(w))/2 identifies V_4* with V_4 and turns j into a degree-four vector covariant. Under this convention g^{-1}(dI)=2v, so

    g^{-1}j=2I grad_g(J)−6J v.

This identification is optional; the covector coefficients above already generate the ideal.

## 3. Explicit unique primary factorization

In the displayed basis the unique decomposition j_r=I A_r+J B_r is

    A_r=2∂_rJ,  B_r=−3∂_rI.

Explicitly, in the order (a,b,c,d,e),

    A=108(ce−d², 2cd−2be, ae+2bd−3c², 2bc−2ad, ac−b²),
    B=(−9e,36d,−54c,36b,−9a).

Uniqueness follows because the first Koszul relation for the regular pair (I,J) has total degree five, so there is no relation between the quadratic A coefficients and linear B coefficients in total degree four. In particular B is a basis of S_1, explicitly, not just by an abstract irreducibility argument. Different invariant normalizations rescale these formulas; any other minimal conductor-quartic basis differs by a constant GL₅ matrix. Such a change acts by an invertible transformation on the target of the cofactor map and preserves its kernel and rank. These formulas do not identify a pre-existing ordered cofactor basis without making that basis change explicit.

For the primary convention P(x)=(Ix,−Jx), the factor through P is exactly

    F(u,v)_r=2(∂_rJ)u+3(∂_rI)v,
    α=FP.

Thus the earlier abstract coefficient-existence dependency is removed. The coefficients are universal known invariants and their derivatives. Multiplication by these coefficients on the actual graded cohomology module is still independent data.

## 4. All four linear syzygies, and the complete Hilbert–Burch matrix

Euler homogeneity gives Σr j_r=2I(3J)−3J(2I)=0. Invariance gives j(ξf)=0 for every ξ∈sl₂. With the binomial coefficient convention, take the four column vector fields

    E₀=(a,b,c,d,e),
    E₊=(4b,3c,2d,e,0),
    E₋=(0,a,2b,3c,4d),
    H =(4a,2b,0,−2d,−4e).

Consequently the full linear syzygy matrix is

    L = [ a   4b   0    4a
          b   3c   a    2b
          c   2d   2b   0
          d   e    3c  −2d
          e   0    4d  −4e ],

with (j_a,j_b,j_c,j_d,j_e)L=0.

These columns are linearly independent over C as elements of S_1^5. Indeed their coefficient matrices are the identity and the three matrices of the faithful sl₂ representation V_4. Taking trace kills the latter and detects the identity; faithfulness then kills the remaining combination. The verified Hilbert–Burch resolution says the space of linear syzygies has dimension exactly four and generates the entire first syzygy module freely. Therefore these columns form its basis and L is a Hilbert–Burch matrix for K. Its signed maximal minors are the five j_r up to one common nonzero scalar, after the fixed row convention. Independence over C alone would not establish this conclusion without the prior resolution; no generic-rank evaluation is hidden here.


## Publication boundary

The actual-module consequences are preserved separately as MODULE-APPLICATION.md in the socle-detector unit. Polynomial SL2 symmetry does not identify the action on the actual HM module.
