# The actual cone upper connection has an a-squared factor

## Result

For the corrected cone operator of symbol H D_a with H=k a h, the upper matrix connection entry in the homogeneous vertex frame is

    A12=-k rho a^2 n_h,                              (1)

where rho is the fixed nonzero normalization identifying D_a with the projective vector field represented by a. The polynomial n_h is independent of a. It is obtained by multiplying h by the actual invariant section

    kappa=(d_L f)/g in H0(O_D(-2,6)),

and uniquely extending to H0(V O_L(6)). This is a statement about the ACTUAL cone operator, not a chosen matrix instance.

Moreover h->n_h factors through

    D5 O_L -> V O_L(2) --M_kappa--> V O_L(6).       (2)

The first map is onto, with kernel Wprime O_L(-3). The second is the unique nonzero equivariant quartic map, up to its fixed scalar. It has rank3 off a single reduced twelve-point orbit on L and rank2 on that orbit. These are geometric rank conclusions; no actual map matrix or selected coefficients are evaluated.

The actual normal shadow also depends on its diagonal connection and scalar correction. Formula(1) alone does not imply any value of the third Bockstein.

## 1. The projective vector field contributes a second a

Choose the invariant volume form on W. The usual quadratic-to-sl2 identification sends a to its Hamiltonian vector field. Its induced vector field on L=P(W) is the same quadratic section of T_L=O_L(2), up to a fixed nonzero scalar rho. This also follows from the uniqueness of the nonzero equivariant identification A->H0(T_L).

For a=s^2 alpha+st beta+t^2 gamma, take D_a=a_s partial_t-a_t partial_s. On z=t/s,

    D_a(z)=2a(1,z).

For a homogeneous cubic F(s,t), the linearized action in this chart is

    D_a F(1,z)=2a(1,z) partial_z F(1,z)
                 -3 partial_z a(1,z) F(1,z).

The second term vanishes on the zero divisor of F. The same conclusion is independent of line-frame choices: changing the derivative by a scalar multiple of f has no effect on D.

The partial differential d_L f along the negative factor, restricted to D=(f=0), is intrinsically a section of O_D(3,1). Local frame derivatives disappear because f=0. Therefore

    (H D_a f)/g = k rho a^2 h (d_L f)/g on D.      (3)

This retains both k and the vector-field normalization rho.

## 2. The extension to a global quadratic polynomial is unique

The actual g trivializes O_D(5,-5), so kappa has bidegree(-2,6). Multiplication by h of bidegree(4,0) yields a section of O_D(2,6). The divisor restriction sequence has kernel O_Y(-1,3):

    0 -> O_Y(-1,3) -> O_Y(2,6) -> O_D(2,6) -> 0.

That kernel has vanishing H0 and H1, since O(-1) is acyclic on the positive projective line. Thus every such section extends uniquely to a polynomial n_h in Sym^2(Wprime) tensor H0(O_L(6)).

For the cone operator, decompose H D_a f=m f+n g in degree7. Coprimality makes this decomposition unique, since a syzygy would have degree-1. Its upper connection entry is A12=-n, independently of the effective scalar line action. Applying the same restriction isomorphism at bidegree(2,10) to (3) proves n=k rho a^2 n_h and hence (1).

## 3. The quartic multiplication map is actual and nonzero

The actual cubic quotient gives

    0 -> Wprime O_L(-3) -> D5 O_L
      -> pi_*O_D(4,0)=V O_L(2) -> 0.

The restriction sequence from Section2 gives pi_*O_D(2,6)=V O_L(6). Multiplication by kappa produces M_kappa in (2).

The actual cubic support is smooth integral genus4, by ACTUAL-CUBIC-SUPPORT-IS-GENUS-FOUR-WITH-EXACT-FIVE-TORSION.md. Its degree3 projection to P(Wprime) is separable in characteristic zero. The partial derivative d_L f is its ramification section, not identically zero. Hence kappa is nonzero. Multiplication by a nonzero section on the integral curve is injective, so M_kappa is generically invertible.

Its equivariant Hom space is one-dimensional:

    Hom_G(V O2,V O6)
      = [End(V) tensor Sym^4 W]^G,
    End(V)=1 plus V plus D5,   Sym^4 W=D5.

Thus this actual map is the unique nonzero quartic channel, not an unspecified linear combination of channels. The map h->n_h is injective on global sections, since h|D is nonzero for every nonzero positive quartic and kappa is nonzero.

As an independent character check, pushing the restriction sequence for O_D(-2,6) gives

    0 -> pi_*O_D(-2,6) -> S4 O_L(3) -> O_L(6) -> 0.

The last map is the complete cubic evaluation determined by f. Its kernel is A O_L(2). Therefore the invariant global section space containing kappa is one-dimensional, since A tensor A=1 plus A plus D5.

## 4. The twelve exceptional fibers

The determinant of M_kappa is a nonzero section of O_L(12). Its zero scheme is invariant, and every nonempty orbit on L has at least twelve points. Consequently its degree12 zero scheme consists of one reduced twelve-point orbit. If the matrix had rank at most1 at one of those points, all cofactors would vanish there and the determinant would have zero first jet, contrary to reducedness. Hence its rank is exactly2 at each exceptional point and3 elsewhere.

Equivalently the multiplication cokernel has length12, matching the degree of the ramification divisor of the degree3 genus4 projection. No root coordinate or actual polynomial coefficient has been selected to establish this conclusion.

## Remaining obstruction

The upper-entry contribution in the harmonic normal cochain now has the uniform factor a^2. The diagonal entry contains the canonical scalar correction, which need not be divisible by a as an ambient polynomial even when its restriction to D is. The exact normal class and its cancellation between these terms remain unresolved.
