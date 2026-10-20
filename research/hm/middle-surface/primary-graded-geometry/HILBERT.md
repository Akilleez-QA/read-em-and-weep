# All multigraded pieces and Hilbert series of the isolated primary closure

## Scope and notation

This is a formal universal-algebra calculation, using the kernel Q established in `../global-rank-one-primary-closure/PROOF.md`. It does not evaluate any source operation or actual model matrix. No claim about generators in all degrees is made.

Over C let V have dimension five, R=C[x_i,y_i,z_i], P the rank-one determinantal prime, and

    φ(x_i)=r_1(u_i+p_i), φ(y_i)=r_2u_i, φ(z_i)=r_3(u_i−p_i),
    Q=ker φ, (p)^2=0, C=R/P, B=R/Q, N=P/Q.

Thus 0→N→B→C→0 is an exact sequence of graded vector spaces, N²=0, and N is canonically a C-module. Put α=(a,b,c), d=a+b+c. Write W=V*, and identify p-linear polynomials of u-degree d−1 with Sym^(d−1)W⊗W. Define

    K_d={Σ_i f_i(u)p_i : deg f_i=d−1, Σ_i u_i f_i=0}.

For d≥1 this is the kernel of multiplication Sym^(d−1)W⊗W→Sym^d W, hence the Schur module S_(d−1,1)W for d≥2; K_1=0.

## The complete multigraded answer

For every α,

    C_α ≅ Sym^d W,
    N_α = 0                         if α has support of size at most one,
    N_α ≅ K_d                      if α has support of size at least two.

These identifications include the multiplication maps, not just their dimensions: represent N_α as r^α K_d inside the square-zero parameter ring. Multiplication by a reduced coordinate r_j u_i is ordinary multiplication by r_j u_i. In particular all three block weights affect the identification of generators by nonzero constants, but do not change the resulting C-module.

For n=5 the dimensions are

    dim C_α = binom(d+4,4),
    dim K_d = 5 binom(d+3,4) − binom(d+4,4)
            = (d−1)(d+1)(d+2)(d+3)/6        (d≥1).

Therefore

    dim B_α = binom(d+4,4)                  (support α≤1),
    dim B_α = 5 binom(d+3,4)                (support α≥2),
    dim Q_α = Π_(j=1)^3 binom(α_j+4,4) − dim B_α.

At d=0, B_0=C and N_0=0.

## Elementary proof by minor multiplication

Diagonal evaluation R_α→Sym^d W is surjective: any u-monomial of degree d can be allocated among the three blocks with their prescribed degrees. This proves the assertion about C_α.

For F∈P_α, its image has the form r^α Σ f_i(u)p_i. Differentiating the zero diagonal identity in the scalar parameters shows Σ u_i f_i=0. Consequently N_α⊂r^α K_d.

If only one block occurs, diagonal evaluation is injective, so N_α=0. Otherwise choose distinct blocks j,k with α_j,α_k≥1. Their weights t_j,t_k are distinct members of {1,0,−1}. For any row indices i<ℓ, the corresponding minor has image

    φ(M_jk;iℓ)=(t_k−t_j) r_j r_k U_iℓ,
    U_iℓ=u_i p_ℓ−u_ℓ p_i.

Multiply this minor by polynomials of multidegree α−e_j−e_k. Their diagonal values span every homogeneous polynomial in u of degree d−2. Products with the first-order part of the multiplier vanish because (p)²=0. Hence N_α contains

    r^α Sym^(d−2)W · span{U_iℓ}.

This equals r^α K_d. For completeness, the Koszul generation has the following direct proof, with no representation-theoretic dimension argument. If w=Σ f_i p_i∈K_d, differentiate Σ u_i f_i=0 and use Euler's identity for the homogeneous f_i. It gives

    w = (1/d) Σ_(i<j) (∂_i f_j−∂_j f_i)(u_i p_j−u_j p_i).

The coefficients have degree d−2. For d=1 the identity forces w=0. This establishes the asserted equality in all multidegrees.

The C-module compatibility follows from multiplication in the parameter ring: the first-order part of any lift of a reduced function kills every element of N. Thus only its constant part acts, by ordinary u,r multiplication.

An optional GL(V)-equivariant vector-space splitting in each positive multidegree can also be made explicit. If φ(F)=r^α(f+g), Euler contraction gives u·g=(a−c)f. Subtracting ((a−c)/d)df leaves an element of K_d. This proves B_α≅Sym^d W⊕N_α as GL(V)-modules. This is not asserted to give an algebra splitting of B→C.

## Identification as a section module

Let X=P^4×P^2 with Segre polarization L=O(1,1), and let Z⊂P^2 be its three reduced coordinate points. The homogeneous ideal of Z in C[r_1,r_2,r_3] is

    I_Z=(r_1r_2,r_1r_3,r_2r_3).

Its degree-d part is spanned exactly by degree-d monomials whose support has size at least two. The twisted Euler sequence on P^4 identifies

    H^0(P^4,Ω^1(d))=K_d.

Combining this with the multiplication-compatible description above gives the exact graded C-module isomorphism

    N ≅ ⊕_(d≥0) H^0(P^4,Ω^1(d)) ⊗ H^0(P^2,I_Z(d))
      = ⊕_(d≥0) H^0(X,(Ω^1_P4 ⊠ I_Z)⊗L^d).

The equality uses the usual external tensor product and the degree-zero Künneth formula. There is no additional twist. Negative twists have no global sections, so this is also the full integer-graded section module. In particular the associated sheaf on Proj C=X is Ω^1_P4⊠I_Z. This identifies the input needed for vertex-depth/local-cohomology calculations without assuming that the square-zero algebra extension splits globally.

## Standard graded Hilbert series and degree

There are binom(d+2,2) multidegrees α of total degree d. For d≥1 exactly three have support one. Thus

    dim C_d = binom(d+4,4) binom(d+2,2),
    dim N_d = [binom(d+2,2)−3]
              [5 binom(d+3,4)−binom(d+4,4)]       (d≥1),
    dim N_0=0.

Summing these polynomial sequences gives

    H_C(t) = (1+8t+6t²)/(1−t)^7,

    H_N(t) = (30t²+70t³−70t⁴+42t⁵−14t⁶+2t⁷)/(1−t)^7,

    H_B(t) = (1+8t+36t²+70t³−70t⁴+42t⁵−14t⁶+2t⁷)/(1−t)^7.

These are exact rational identities, obtained from the displayed dimension polynomials by finite differences of order seven, with the d=0 value treated separately. Initial B dimensions are

    1, 15, 120, 630, 2310, 6678, 16380.

The numerator of H_B at t=1 is 75. Consequently the seven-dimensional affine cone B has multiplicity 75, and its six-dimensional projective scheme has degree 75. This agrees with generic transverse length five times the Segre degree binom(6,2)=15. The nilmodule alone has multiplicity 60 and C has multiplicity 15.

## Exact multigraded rational form

For a compact rational expression without a large expanded numerator, put

    F(s_1,s_2,s_3)=Π_j(1−s_j)^(-1),
    G=F−Σ_j(1−s_j)^(-1)+2,
    E=Σ_j s_j ∂/∂s_j,
    D(E)=(E+1)(E+2)(E+3)(E+4)/24,
    K(E)=(E−1)(E+1)(E+2)(E+3)/6.

Then the exact three-variable Hilbert series are

    H_C(s)=D(E)F,
    H_N(s)=K(E)G,
    H_B(s)=D(E)F+K(E)G.

These are rational functions because they apply finite differential operators to rational functions. G has coefficient one exactly on mixed-support multidegrees and zero elsewhere, including its constant term. Thus the polynomial K(E), whose value at zero would otherwise be −1, introduces no erroneous constant term. This also records all multigraded dimensions independently of the one-variable specialization.
