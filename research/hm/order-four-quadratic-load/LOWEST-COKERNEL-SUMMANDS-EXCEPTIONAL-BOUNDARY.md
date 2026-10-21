# The degree-one cokernel summands reduce to one two-dimensional exceptional boundary

## New conclusion

Let C=C_lin be the actual torsion-free, rank-five degree-26 hyperplane cokernel, with its inversion-even linearization. Assume the already proved absence of degree-zero summands. Then the degree-one isotypic block of C is either absent or exactly W tensor O_T(1), where W is the actual negative binary two-space. In particular the number of O_T(1) summands is zero or two, and the other binary two-space W-prime cannot occur in degree one.

More precisely, it is the dimension of the cokernel of a canonical actual exceptional-divisor boundary

    H0(R,B_R(3)) tensor H1(P1,O(-3)) -> H2(P4,B),

with its natural exceptional-divisor linearizations. The target is the actual binary representation W, of dimension two and inversion-odd. No coefficient, matrix, or rank of this boundary is evaluated here. Thus this result does not choose between zero and two.

## 1. Plane cohomology needed for the calculation

Write E_R=F_R(2), with its actual Steiner resolution

    0 -> A O_R(-1) -> D O_R -> E_R -> 0,
    dim A=3, dim D=5.

The symmetric-square resolution is

    0 -> wedge^2 A O_R(-2) -> (A tensor D) O_R(-1)
      -> Sym^2 D O_R -> Sym^2 E_R -> 0.

Since B_R(j)=Sym^2 E_R(j-3), twisting this resolution by -1 gives

    h0(B_R(2))=3, H1(B_R(2))=H2(B_R(2))=0.

Indeed only H2(wedge^2 A O_R(-3)) survives in the resolution, and its total cohomological degree is zero. Without twisting, one gets

    H0(B_R(3))=Sym^2 D, dim=15,
    H1(B_R(3))=H2(B_R(3))=0.

The action on both bundles over the positive fixed plane is inversion-even.

## 2. Exceptional filtration, with its signs

Let p:X=Bl_R(P4)->P4, let E_exc be its exceptional divisor, and put

    F_k=p*B tensor O_X(k E_exc).

The relation pi*O_T(1)=p*O_P4(1) tensor O_X(-E_exc) gives

    F_3=p*B(3) tensor pi*O_T(-3).

The exceptional divisor is the projectivized rank-two normal bundle of R. Underlying ordinary line bundles, its k-th quotient is

    F_k/F_(k-1) = B_R(k) external-tensor O_P1(-k).

The normal bundle has inversion character minus one; therefore this quotient has total character (-1)^k. This assertion retains the natural tautological linearizations, rather than replacing the exceptional P1 with an unlinearized factor.

For k=1, O_P1(-1) is acyclic, so H^i(F_1)=H^i(B). For k=2, the only possibly relevant connecting map is

    H0(B_R(2)) tensor H1(O_P1(-2)) -> H2(B).

Its source is even and its target is entirely odd, of dimension two, by EXACT-AMBIENT-ADJOINT-DEFORMATIONS.md. Hence this map vanishes. H1(B_R(2))=0 then gives a canonical isomorphism

    H2(F_2)=H2(B).

For k=3, H1(B_R(3))=0 gives the exact sequence

    H1(F_3) -> H0(B_R(3)) tensor H1(O_P1(-3))
       --partial_exc--> H2(B) -> H2(F_3) -> 0.

The source of partial_exc has dimension thirty and is odd. Thus

    H2(F_3)=coker(partial_exc),   dim H2(F_3)<=2,

and H2(F_3) is entirely odd. This is an actual geometric connecting map, not an arbitrary map between spaces of those dimensions.

## 3. Identification with the low-degree splitting invariant

Twist the universal incidence restriction sequence by O_T(-3):

    0 -> B(2) external-tensor O_T(-4)
      -> B(3) external-tensor O_T(-3)
      -> j_*F_3 -> 0.

The ambient vanishing H2(B(2))=0 and projective-line cohomology identify its odd H2 with

    coker[H1(B(2))_- tensor H1(O_T(-4))
       -> H1(B(3))_+ tensor H1(O_T(-3))].

The target/source parity signs follow respectively from the odd O(-3) and even O(-4) linearizations. The exact cokernel presentation

    0 -> A O_T(-6) -> H1(B(2))_- O_T(-1)
      -> H1(B(3))_+ O_T -> C -> 0

shows, by breaking it into two short exact sequences and using H2 on T=0, that the same cokernel is H1(C(-3)). Therefore

    H1(C(-3)) = H2(F_3) = coker(partial_exc).

Since C is globally generated, its splitting degrees are nonnegative. With degree zero already excluded, every degree is at least one, and h1(C(-3)) counts exactly the O(1) summands.

Finally the independently confirmed exact ambient character is H2(B)=W, not W-prime. Since W is irreducible, its equivariant quotient H1(C(-3)) is either zero or W. Equivalently the degree-one coefficient representation of C is either absent or W: H1(O_T(-2)) is the trivial representation for the standard determinant-one binary linearization. Even without the refined character, perfectness of the binary group already excludes an odd one-dimensional quotient.

## 4. Exact remaining gap

H2(B(1))=0 does not by itself identify or make partial_exc surjective in the above exact sequences. At k=2 parity forces the boundary to be zero; at k=3 parity permits, but does not force, surjectivity. The remaining alternatives are:

- partial_exc is onto: C has no O(1) summands;
- partial_exc is zero: C has exactly two O(1) summands.

A rank-one image is excluded by irreducibility of the actual target W. An additional geometric identification or structural nonvanishing/vanishing theorem for this actual exceptional boundary is required to select the alternative. Matching dimensions or permitted characters alone does not supply it.

## Sources and scope

Actual ambient H2(B)=(0,2) and H2(B(1))=0: EXACT-AMBIENT-ADJOINT-DEFORMATIONS.md and [PR455 at immutable 8cbbe482ee50c35d52ffcdf3efb837fa8cf96af4](https://github.com/Akilleez-QA/read-em-and-weep/blob/8cbbe482ee50c35d52ffcdf3efb837fa8cf96af4/research/hm/twist-one-structural-vanishing/PROOF.md). The latter proof uses the [Horrocks–Mumford primary monad, Section 2](https://www.dam.brown.edu/people/mumford/alg_geom/papers/1973a--Rk2BdleP%5E4-NC.pdf), and establishes the actual ambient H2 bound and twist-one vanishing structurally. The exact dimension and inversion character additionally use the actual projective-orbit argument in EXACT-AMBIENT-ADJOINT-DEFORMATIONS.md, not only that bound. Actual universal kernel and parity: EXACT-HYPERPLANE-ADJOINT-SYZYGY-BUNDLE.md. Torsion-freeness follows from the all-parameter hyperplane square theorem at [5ce98e6bef1fd849353f563b1ccfc62f4d28b8d9](https://github.com/Akilleez-QA/read-em-and-weep/commit/5ce98e6bef1fd849353f563b1ccfc62f4d28b8d9) and its torsion-free corollary at [f5361eacee42eb3b7df75c69f01508b66722d395](https://github.com/Akilleez-QA/read-em-and-weep/commit/f5361eacee42eb3b7df75c69f01508b66722d395).

This is a new low-splitting bound and identification of its precise remaining boundary. It does not prove full-adjoint or smoothing injectivity. No selected actual coefficient, point, matrix, numerical rank, or experiment is used.

## Exact ambient character provenance

The independently reproduced universal representation calculation is recorded in [COKERNEL-SPLITTING-NINE-CANDIDATES-AND-LOW-QUOTIENT.md](COKERNEL-SPLITTING-NINE-CANDIDATES-AND-LOW-QUOTIENT.md), with standalone verifier [verify_h2_B0_character.py](verify_h2_B0_character.py) and output [h2_B0_character.json](h2_B0_character.json). It uses the actual normalized monad K-class and the already proved H1(B)=End_0(V+W), giving

    chi(B)=W-1-A-V-D-2T_6,
    H1(B)=1+A+V+D+2T_6,
    H2(B)=W.

This is a representation-ring computation, not an actual coefficient or matrix evaluation. The character confirmation was supplied independently on 2026-10-21; the boundary partial_exc remains unevaluated.

## The unique scalar and its dual first-neighborhood interpretation

The exact character identity

    H0(B_R(3)) tensor H1(O_P1(-3))
      = Sym^2 D tensor W = W + W-prime + 2S + 3T_6

shows that Hom_G(source,H2(B)) is one-dimensional. Thus partial_exc is one actual scalar on its unique W-channel. This observation does not decide whether that scalar vanishes. The H2(B)=W verifier has SHA256 aaf281eade310a9d4285f940cf5567c2d7d68fe23812647bb592da91edbf1e2c; its companion proof has SHA256 b40a57c7eb189bb1380bcc2c264a4d64720eeed5f15217322bde030d37ed3290.

There is a useful intrinsic dual description. The blowup canonical bundle is p*O(-5) tensor O_X(E_exc), and B is self-dual via trace. Therefore Serre duality and the standard blowup pushforward of negative exceptional powers give

    H2(F_3)* = H2(P4,I_R^2 B(-5)).

Here higher direct images of O_X(-2E_exc) vanish and its pushforward is I_R^2. Let 2R denote the ordinary first infinitesimal neighborhood defined by I_R^2. The actual first-normal splitting, also forced by inversion, identifies

    B(-5)|2R = B_R(-5) directsum (B_R(-6) tensor W)

as plane modules with their even and odd characters respectively. The geometric projection to R is defined on the complement of the negative line and supplies the underlying first-neighborhood module structure. Plane Serre duality and Section 1 give H1 of both summands zero. Consequently

    H2(I_R^2 B(-5))
      = ker[H2(B(-5)) -> H2(B(-5)|2R)].

The source is W* (canonically isomorphic as representation to W); only the odd target contributes. That target is

    H2(B_R(-6)) tensor W = H0(B_R(3))* tensor W,

of dimension thirty. Under the natural duality pairings, this first-neighborhood restriction is the transpose of partial_exc, up to the harmless overall boundary-sign convention.

Thus the same unanswered scalar asks whether the actual ambient obstruction W is detected on the first infinitesimal neighborhood 2R. The known nonzero second-normal class zeta is not automatically this restriction map: proving a relation between them remains an additional task. No implication from uniqueness of the W-channel alone is asserted.
