# Finite pullbacks and isogenies do not remove the Lange mixed obstruction

## Result and precise scope

Work over C. Let F be a normalized original Lange bundle on P=P1 x P3. The [relative-monad lemma](lange-relative-monad.md) and [mixed-nonvanishing proof](mixed-nonvanishing.md) establish

Delta(F) = A_1(F) cup v - u cup A_3(F) != 0

in H^2(P, End(F) tensor Omega^1_P1 boxtimes Omega^1_P3).

Then every finite surjective morphism f:A -> P from an abelian fourfold gives a pullback f*F with three independent nonzero polarized commutative Atiyah evaluations. Here the natural polarization is f*O(1,1). The conclusion also holds for any polarization proportional to it, for all isogeny pullbacks, and for actual isogeny descents of these bundles. Thus changing branch points, degrees, elliptic factors, the general map from an abelian threefold to P3, or the presentation of the abelian fourfold up to isogeny cannot repair this construction.

This is an exclusion of finite pullbacks of the stated source bundles, not a nonexistence theorem for all rank-two squareclass-2 bundles. It is a first-order result; it neither repairs the original ambient theorem nor decides an ambient higher obstruction.

## 1. Isogeny invariance

Let q:A' -> A be an isogeny, of degree e, and let E be any bundle on A. Since q is finite etale,

At(q*E) = (q*At(E)) under q*Omega_A = Omega_A'.

Pullback gives the natural isomorphism q^sharp:H^1(T_A) -> H^1(T_A'), and

ob_(q*E)(q^sharp kappa) = q*ob_E(kappa).

The trace q_*O_A' -> O_A, composed with the unit, is multiplication by e. By the projection formula this gives a left inverse (1/e)Tr to

H^2(A,End E) -> H^2(A',End(q*E)).

Consequently the obstruction vanishes after pullback if and only if it vanished before pullback. The same argument applies to the full HKR degree-two evaluation: its source is transported isomorphically by the etale pullback, Atiyah powers are natural, and its target pullback is injective. Its rank, its kernel dimension, and the equality or failure of equality between its kernel and the Chern-character annihilator are preserved.

If E=q*E_0 is an actual descent, the same equality reads in reverse. A new equivariant structure on a fixed bundle does not change this fact. A topologically trivial line twist has zero Atiyah class and changes none of these evaluations. Merely proposing a different bundle downstairs whose pullback is not the given bundle is not descent and receives no conclusion from this argument.

If q*theta_B=r theta_A and c2(E_i)=d_i theta_i^2, then d_A=r^2 d_B. Thus a scalar-polarized isogeny can change the coefficient only by a rational square; multiplication by n changes it by n^4. An isogeny descent may lower that coefficient, but cannot change its squareclass or remove this obstruction. If det(E_0) becomes trivial after pullback, it is a torsion line bundle; normalizing it by a Pic^0 square-root twist has zero Atiyah effect.

Caveats: isogeny pullback need not preserve stability or simplicity. A polarized statement compares q*lambda with lambda, or proportional polarizations, rather than arbitrarily unrelated polarizations. The full HKR-kernel statement is intrinsic and has no such polarization ambiguity.

## 2. The differential-trace splitting lemma

Let b:B -> P^n be finite surjective, with B an abelian n-fold, and write N=deg b and D=b_*O_B. For invariant v in H^0(T_B), differentiating b and contracting with v gives

phi_v:Omega^1_Pn -> D.

For invariant omega in H^0(Omega^1_B), define

tau_omega:D -> Omega^1_Pn,    g |-> Tr_b(g omega).

The trace of one-forms is regular, including across ramification. A global construction is to use the top-form trace and the perfect wedge pairing. For a local one-form eta on B, define Tr_b^1(eta) by

Tr_b^1(eta) wedge beta = Tr_b^top(eta wedge b*beta)

for every local beta in Omega^(n-1)_Pn. The perfect pairing with top forms gives a unique regular one-form. On the etale locus it is exactly the sum over inverse branches, so it is the desired extension everywhere. Finite maps between the smooth equidimensional varieties here are finite flat; the dualizing-sheaf trace is available.

Now tau_omega phi_v is an endomorphism of Omega^1_Pn. The cotangent bundle is simple, so this endomorphism is a constant scalar. Over the etale locus its matrix is a sum of N rank-one operators; the trace of each is omega(v). Its rank-n trace is consequently N omega(v), proving

tau_omega phi_v = (N/n) omega(v) Id_Omega.

Choose dual bases v_1,...,v_n and omega_1,...,omega_n. Then

Phi:(Omega^1_Pn)^n -> D,    (alpha_i) |-> sum_i phi_vi(alpha_i)

has left inverse (n/N)(tau_omega1,...,tau_omegan). Thus it is a split inclusion of vector bundles, not merely an injection away from the branch divisor. This result does not require a Galois cover, deck characters, or equal elliptic branch data.

The simplicity assertion follows from the Euler sequence and H^0(Omega^1(1))=H^1(Omega^1(1))=0, H^1(Omega^1)=C; n=1 is immediate for a line bundle.

A standard reference for traces on differential forms is the Stacks Project, Lemma 50.19.2 and Proposition 50.19.3 for finite syntomic morphisms, https://stacks.math.columbia.edu/tag/0FK6 . The argument above explains precisely which regular trace is used.

## 3. Product maps: exact mixed formula with arbitrary polarizations

Let a:C -> P1 and b:B -> P3 be finite, with C elliptic and B an abelian threefold. Set

lambda_C=a*u,  lambda_B=b*v,  theta=lambda_C+lambda_B,
E=(a x b)*F.

Choose invariant omega_C and xi_C with omega_C(xi_C)=1 and write

lambda_C=omega_C tensor eta_C^lambda.

For w in H^0(T_B), put eta_w=w contraction lambda_B. The theta-polarized mixed tangent is

kappa_w=xi_C tensor eta_w + w tensor eta_C^lambda.

Indeed, the two contractions with theta cancel. Both signs here use factors ordered C first and B second. Let phi_C be the differential-contraction map for a and xi_C, and phi_w the map for b and w. Naturality of the Atiyah class of O(1) gives

H^1(phi_C)(u)=eta_C^lambda,
H^1(phi_w)(v)=eta_w.

Exact finite pushforward and the projection formula identify the actual End-valued mixed class with

ob_E(kappa_w) = (phi_C boxtimes phi_w)_* Delta(F),

up to the single overall convention sign for Atiyah/Kodaira-Spencer evaluation. The relative minus sign in Delta comes from interchanging the two degree-one cohomology factors. This is a formula in actual H^2, not just on traces or an E_1 page.

The preceding splitting lemma, for n=1 and n=3, makes

(Omega^1_P1 boxtimes Omega^1_P3)^3 -> (a x b)_*O_(C x B)

a split inclusion. Tensoring with End(F) and taking H^2 stays split injective. For three independent w_i, the three mixed classes are the images of three independent copies of the same nonzero Delta(F), so they are linearly independent. If Delta(F)=0, all three vanish. Thus, for an arbitrary source bundle F, this formula gives the exact equivalence

all mixed evaluations vanish <=> Delta(F)=0.

For det F=O and c2(F)=4uv+2v^2, c2(E)=2theta^2. The seven product-polarized commutative directions extend by extending the ample line bundles and chosen generating sections locally. The six compensated Poisson directions are the general rank-two identity. Combining those thirteen vanishing directions with these three independent mixed obstructions gives HKR evaluation kernel dimension 13 and rank 15, while the Chern-character annihilator has dimension 16.

## 4. Degree-m elliptic maps and the normalization

For any degree-m map a:C -> P1, m>=2,

a_*O_C = O + O(-1)^(m-2) + O(-2).

Proof: the unit and (1/m)trace split O; the remaining summands have negative degree because h0(O_C)=1. Since h1(O_C)=1, exactly one summand is O(-2), while the others are O(-1). The rank is m. No Galois assumption is used.

The differential-contraction map phi_C:O(-2) -> a_*O_C has nonzero projection to the O(-2) quotient: its H^1 map sends u to m eta_C when alpha_C=omega_C eta_C is the principal class. Hence its image itself is a split O(-2) summand. It need not coincide with an initially chosen noncanonical Birkhoff-Grothendieck summand; overlooking this distinction would be an error.

If a*u=m alpha and b*v=m beta, for a principal product polarization theta_0=alpha+beta, then theta=m theta_0. The theta_0-normalized mixed vector xi_C tensor (w contraction beta)+w tensor eta_C has obstruction

(1/m)(phi_C boxtimes phi_w)_*Delta(F).

The scalar 1/m is nonzero for every m. For four degree-m elliptic root maps followed by Sym^3(P1)=P3, deg f=6m^4 and c2(E)=2m^2 theta_0^2. In particular m=2 gives degree 96. Different elliptic curves, unequal branch data, and absence of S3 symmetry do not alter nonvanishing or mixed rank three.

Unequal degrees may fail the desired scalar-principal-polarization Chern identity. This is a numerical issue, not a vanishing mechanism: using the natural ample theta=f*O(1,1) still gives the same three nonzero mixed classes.

## 5. Every finite map to P1 x P3 reduces to the product case

Let f:A -> P1 x P3 be finite from an abelian fourfold and put

L_1=f*O(1,0),  L_3=f*O(0,1).

These are globally generated nef line bundles. Their numerical dimensions are 1 and 3, and L_1 tensor L_3 is ample. Let K_i be the connected kernel of the homomorphism associated with L_i. Then

C=A/K_1 has dimension 1,   B=A/K_3 has dimension 3.

Here is why the relevant factorization uses the actual maps, not only numerical classes. A globally generated line bundle on an abelian variety is numerically trivial on every coset of its connected kernel. A globally generated numerically trivial line bundle on a connected projective variety is trivial: its associated projective morphism has zero-dimensional image. Consequently each given projective morphism is constant on those cosets and factors through the corresponding quotient. The quotient property descends the actual morphisms. Write M_1=a*O_P1(1) and M_3=b*O_P3(1) on the quotients; these pull back to L_1 and L_3 and have zero-dimensional connected kernels. Therefore M_1 and M_3 are ample, so the induced maps a:C -> P1 and b:B -> P3 are finite.

The intersection K_1 cap K_3 is finite, since the sum L_1 tensor L_3 is ample. Thus

q=(q_1,q_3):A -> C x B

is an isogeny, and f=(a x b)q. The original E=f*F is an isogeny pullback of the product case in Section 3. Section 1 preserves its three independent mixed obstructions.

Equivalently, this follows analytically by representing each nef Chern class by its translation-invariant positive semidefinite Hermitian form. Its rational kernel defines K_i; its rank is the numerical dimension. The sum form is positive definite, so the two kernels are complementary.

If a separate ample class theta_0 satisfies c2(f*F)=d theta_0^2, then theta=f*O(1,1) satisfies theta^2=(d/2)theta_0^2. Diagonalizing the positive forms shows all pairwise products of their four relative eigenvalues are equal; positivity forces every eigenvalue equal. Thus theta is proportional to theta_0, and their polarized tangent spaces coincide. An unrelated choice of polarization therefore does not create a loophole in the scalar-theta^2 setting.

## 6. What remains genuinely unexcluded

There is no remaining finite-map-only alternative with F fixed in the original Lange family, even if the source abelian fourfold is not presented as a product. The original relative-monad lemma makes the same conclusion apply to every original Lange bundle, not merely the explicit Hamiltonian representative.

A sharply bounded remaining source-bundle search is:

Find an O(1,1)-stable rank-two F' on P1 x P3 with det F'=O, c2(F')=4uv+2v^2, and Delta(F')=0, outside the now-excluded original Lange relative-monad class.

If such F' exists, its finite elliptic-product pullbacks have the squareclass-2 character and all three missing first-order mixed evaluations vanish; the existing thirteen directions then give weak first-order kernel equality. This is an exact necessary-and-sufficient first-order target for this source and these numerical data. No such F' is constructed or proved to exist here. Its all-order ambient lift would still be a separate problem.

Changing the target variety/source bundle, or constructing rank-two bundles intrinsically on an abelian fourfold, is also outside this exclusion. Those are genuinely different constructions, not a way to repair the same Lange pullback by choosing a cleverer finite map.
