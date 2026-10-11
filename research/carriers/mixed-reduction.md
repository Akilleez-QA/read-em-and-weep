# Mixed Atiyah reduction for the symmetric elliptic pullback

This note proves an End-valued reduction for the symmetric elliptic pullback used in [PR21](https://github.com/Akilleez-QA/read-em-and-weep/pull/21). It applies to every bundle on P1×P3. The actual nonvanishing for the explicit ribbon monad of [PR23](https://github.com/Akilleez-QA/read-em-and-weep/pull/23) is proved in [mixed-nonvanishing.md](mixed-nonvanishing.md).

## 1. The invariant summand and the derivative map

Write `sigma : (P1)^3 -> P3 = Sym^3(P1)`, distinguishing the first root, and let `tau` interchange the other two roots. Quotient by `tau` first. The resulting finite triple cover `mu : D -> P3` has

`D = {(a,f): f(a)=0} subset P1 x P3`,

an incidence divisor of bidegree `(3,1)`. It is also `P1 x P2` by recording the distinguished root and the residual quadratic. The double-cover residual-root direct image is `O + O_P2(-1)`; hence

`sigma_* O(-2,0,0) = mu_* O_D(-2,0) + mu_* O_D(-1,-1)`.

Here the last two bidegrees are in the incidence `P1 x P3` coordinates: the residual `O_P2(-1)` equals `O_D(1,-1)`. The first summand has `tau=+1`, and the second has `tau=-1`.

Push the incidence sequence twisted by `(-2,0)`. It gives

`0 -> mu_* O_D(-2,0) -> H1(P1,O(-5)) tensor O_P3(-1) -> H1(P1,O(-2)) tensor O_P3 -> 0`.

The map is the universal cubic coefficient vector, with a harmless choice of dual basis in `H1(O(-5))`. This is precisely an Euler sequence, identifying the kernel with `Omega^1_P3`. The sequence twisted by `(-1,-1)` similarly gives

`mu_* O_D(-1,-1) = H1(P1,O(-4)) tensor O_P3(-2) = O_P3(-2)^3`.

Now differentiate `sigma` in the distinguished-root direction. Adjunction gives a sheaf map

`phi : Omega^1_P3 -> mu_* O_D(-2,0)`.

Both sides are isomorphic to `Omega^1_P3`. Crucially, this is not merely a map between bundles with the same Chern classes: `Hom(Omega^1_P3,Omega^1_P3)=C`. One proof tensors the dual Euler sequence by `Omega^1`; `H0(Omega^1(1))=H1(Omega^1(1))=0` and `H1(Omega^1)=C` give the assertion. The map `phi` is nonzero, since at a cubic with three distinct roots, varying its distinguished root changes the cubic. Therefore it is an isomorphism everywhere, including above the discriminant. Equivalently, over the distinct-root locus its three evaluated cotangent maps have a Vandermonde matrix of nonzero determinant.

Only after proving this isomorphism may the line-bundle normalization be used. If `v=c1(O_P3(1))` and `h=c1(O_P1(1))`, then

`H1(phi)(v)=h`

under finite-pushforward cohomology: `sigma^*v=h_1+h_2+h_3`, and the distinguished cotangent projection retains `h_1`. Thus the derivative map and the scalar degree-one cohomology generator use exactly the same nonzero scale. There is no extra factor of 3 in the mixed formula. Choices of bases in the incidence Euler sequence can rescale both descriptions, but do not change their relative normalization.

## 2. Elliptic descent and the polarization normalization

For a degree-two elliptic map `x:C->P1`, let `L=O_P1(-2)` be the anti-invariant summand of `x_*O_C`. Fix a nonzero holomorphic differential `omega` and its dual vector `xi`. The adjoint of

`x^*Omega^1_P1 -> Omega^1_C --contraction xi--> O_C`

is a nonzero map `phi_x:Omega^1_P1 -> L`. Both line bundles have degree `-2`, so this is an isomorphism. In a model `y^2=f(t)`, `omega=dt/y`, this map sends `dt` to `y`. Although `y` vanishes upstairs at ramification, it is the local generator of the anti-invariant direct-image module; this does not create zeros of `phi_x` downstairs.

Let `alpha` denote the principal degree-one polarization class on `C`, and choose `eta in H1(O_C)` by `alpha=omega tensor eta`. Since `x^*h=2alpha`, the cohomology map induced by `phi_x` sends `h` to `2eta`. Consequently `eta` becomes `h/2` under the inverse descent identification.

Using the same `x`, `omega`, and principal-polarization convention in all factors, the symmetric mixed tangent `xi_1 tensor eta_2 + xi_2 tensor eta_1` therefore descends, up to the single global sign in the Atiyah/Kodaira-Spencer convention, to

`(1/2) [ A_1(H) cup h_2 - h_1 cup A_2(H) ]`.

The minus sign is the ordinary degree-one cohomology interchange sign, with factors written in increasing product order. It also follows directly by applying contraction to `a omega_1 eta_1 + b omega_2 eta_2`, but the sheaf maps above establish the equality for the complete End-valued class, not just its trace. If a differently scaled generator is called the mixed tangent, the factor `1/2` changes by one common nonzero scalar. The two terms cannot acquire different branch-dependent scales.

The mixed evaluation has deck character `chi_1 chi_2` and is invariant under swapping factors 3 and 4. Exact finite pushforward, its eigenspace decomposition, and the invariant isomorphism `phi` therefore identify it with a common nonzero multiple of

`Delta(F)=A_1(F) cup v - u cup A_3(F)`

in `H2(P1 x P3, End(F) tensor Omega^1_P1 boxtimes Omega^1_P3)`. This proves the stated iff, for every bundle `F`. The three mixed evaluations are permuted by `S3`, hence vanish together. For fixed `F`, their vanishing is independent of the elliptic branch parameters. Changing the bundle `F` itself with those parameters would of course be a different assertion.

## 3. The Euler sufficient detector for a global split-line complex

Let `K` be a bounded complex of sums of `O(a,b)` representing `F`, with global bihomogeneous matrix differential `d`. For the Euler injection

`i:Omega^1_P3 -> O_P3(-1)^4`,

the pushed Atiyah class `i_*A_3(F)` is represented in the hypercohomology of `Hom(K,K(0,-1))^4` by the global degree-one chain map

`(partial d / partial x_j)_(j=0,...,3)`.

A simultaneous overall sign depends on whether the Atiyah class is defined by `[nabla,d]` or its negative. The formula follows by taking ordinary homogeneous-coordinate differentiation of graded free representatives on the affine cone. It descends to the Euler pushout; the line summands' diagonal Atiyah cocycles become Cech coboundaries there, and removing those coboundaries produces exactly the derivative terms. Thus diagonal terms have been nullhomotoped, not silently discarded. The identity

`d (partial_j d) + (partial_j d) d = partial_j(d^2)=0`

checks the chain cocycle condition. The homogeneous Euler identity is

`sum_j x_j partial_j d = B d - d B`,

where `B` records the P3 degrees of the line summands. This gives the expected chain nullhomotopy after the Euler quotient to `O` and is a useful independent implementation check. Coordinate-frame or locally split models require connection/gluing corrections; the bare derivative formula is justified only for the genuinely global split-line complex.

Since `i_*(v)=0` as an Ext class (it is the boundary of `1` in the Euler sequence), functoriality of Yoneda cup gives

`i_*Delta(F) = -u cup [(partial_j d)_j]`

up to the same harmless convention sign. This is a sufficient nonvanishing detector. Its vanishing alone does not prove `Delta(F)=0`: the Euler long exact sequence permits a kernel contributed by `H1(End(F)(-2,0))`.

Finally the cup product must be evaluated in actual hypercohomology. A calculation retaining only the line-bundle cohomology row is valid only when the relevant spectral-sequence differentials cannot occur, or after explicit Cech contractions/higher transferred differentials have been included. A zero on an uncorrected E1/E2 model is not a certificate of zero in Ext, and a surviving entry can still be killed by a higher differential.
