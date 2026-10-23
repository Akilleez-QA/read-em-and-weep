# A forbidden target channel in the actual secondary obstruction

Work over C with the actual normalized HM bundle F, B=End0 F, and G=SL2(F5). Let T=P(W*) be the negative-direction line, A=Sym2 W, D=Sym4 W, V the other even three-space, P the even four-space, and T6=Sym5 W. All line bundles on T retain their standard G-linearizations.

## 1. Immutable inputs and statement

The exact originals and their raw-byte identities are recorded in INPUTS.json. QUOTIENT is PR968 at 148e2eed1fbf50729941365c8fd3ae56a115fe62, research/hm/secondary-quotient-splitting/PROOF.md. SQUARE and SECOND are at db51525015bb7c5e825833d550d08dedf6f6ea96, respectively research/hm/order-four-quadratic-load/HYPERPLANE-SQUARE-SURVIVORS.md and ODD-SECOND-SCALING-OBSTRUCTION.md.

These prove the actual square subbundle L=A O(-6) in the first-cup kernel K, the canonical equivariant splitting

    Q6=K/L=P O(2) directsum W O(-1),

and the actual secondary boundary

    beta: K -> H1(B_R(-1)) O(4),
    beta = beta_bar composed with (K -> Q6).

SECOND defines this boundary from the fifth ordinary neighborhood of R inside each hyperplane H_lambda. Its definition retains the actual quartic transition correction and its interaction with the first lift. No associated-graded or purely quadratic replacement is used here. The actual family and its ideal-power extensions are G-equivariant, so naturality of the connecting morphism makes beta G-equivariant with the stated linearizations.

We prove that the A-isotypic target component is identically zero. Thus the entire actual map factors canonically as

    beta_bar: Q6 --b--> (V+P+D) O(4)
                       -> (A+V+P+D) O(4).               (1)

The space of all equivariant maps b has dimension six, with precisely one channel from each of the two source summands to each of the three target summands. This does not select any of those six scalar coefficients.

## 2. Authenticating the target and excluding its A component

The trace form identifies B_R with its dual. Equivariant Serre duality on R=P2 gives H1(B_R(-1))=H1(B_R(-2))*; the canonical bundle carries no extra determinant character, because G is perfect. SQUARE identifies H1(End(F_R)(-2))=Hom(D,A). The scalar summand has H1(O_R(-2))=0. All the named representations are self-dual, and the fixed character identity is

    A tensor D=A+V+P+D.

Consequently the target in (1) is the actual cohomology representation. Each of its four irreducible isotypic subspaces occurs once and is canonical. Identifications with named abstract representations may be rescaled, but the projections and subspaces themselves are intrinsic.

For equivariant line-bundle maps on T, Hom_G(U O(a),J O(b))=Hom_G(U,J tensor Sym^(b-a) W) when b>=a. Hence the two possible maps to the A target are measured by

    Hom_G(P,A tensor Sym2 W),
    Hom_G(W,A tensor Sym5 W).

The first space is zero because A tensor A=1+A+D. By self-duality, the dimension of the second equals the multiplicity of A in W tensor T6. The binary Clebsch decomposition and restriction to G give

    W tensor T6=Sym6 W+Sym4 W=V+P+D,

so the second space is also zero. This proves (1) for EVERY equivariant map with the actual source and target, and therefore for the actual quartic boundary. No vanishing of its quartic transition term has been assumed or inferred.

For J equal to V, P, or D, the multiplicity of P in J tensor A is one: use A V=P+D, A P=V+P+D, and A D=A+V+P+D. The multiplicity of J in W tensor T6 is also one. Thus

    dim Hom_G(P O(2),J O(4))=1,
    dim Hom_G(W O(-1),J O(4))=1,                         (2)

which proves the six-channel restriction. It is a linear presentation restriction, not a claim that the actual coefficients are independently variable or nonzero.

## 3. Actual fifth-neighborhood cohomology

Let E^1 and E^2 denote the actual inversion-even pushforwards to R, relative over T, of B(3) on the third and fifth hyperplane neighborhoods as in SECOND. Their actual extension is

    0 -> B_R(-1) O(4) -> E^2 -> E^1 -> 0.

For the projection p:R times T -> T, SECOND proves p_*E^1=K and R1p_*E^1=R2p_*E^1=0. Also H0(B_R(-1))=H2(B_R(-1))=0. The actual long exact sequence therefore gives

    0 -> p_*E^2 -> K --beta--> H1(B_R(-1)) O(4)
      -> R1p_*E^2 -> 0,       R2p_*E^2=0.              (3)

In particular no unexamined extension remains between coker beta and R1p_*E^2. Since K -> Q6 is onto, coker beta=coker beta_bar. The canonical target decomposition and (1) now give the canonical direct sum

    R1p_*E^2 = A O(4) directsum coker b.                (4)

This is an actual sheaf decomposition, valid even if coker b has torsion or jumping fiber dimension. It does not assert local freeness of coker b or a splitting of p_*E^2. On the kernel side the precise sequence is only

    0 -> A O(-6) -> p_*E^2 -> ker b -> 0.              (5)

No splitting of (5) is claimed.

## 4. Exact reduction of the two-root gate and degeneracy schemes

For a nondegenerate negative binary quadratic q_-, let Z be its reduced two-root divisor. SECOND identifies the complete secondary scaling obstruction with

    H0(Z,K(1)) -> H1(B_R(-1)) tensor H0(O_Z(5)),

of source dimension 18 and target dimension 30. Equation (1) gives its canonical factorization through

    (V+P+D) tensor H0(O_Z(5)),                         (6)

of dimension 24. The inclusion of (6) in the old target is injective; therefore the reduced operator has EXACTLY the same kernel, rank, and obstruction-vanishing criterion as the original one. The complementary A tensor H0(O_Z(5)) has dimension six and is identically unhit. This is target reduction, not an improved bound on the secondary rank or global quadric sections. It is also distinct from PR976: that result proved surjectivity of the ambient FIRST cup from a 30-dimensional source to a 24-dimensional target. Here the SECONDARY source remains 18-dimensional and only its old 30-dimensional target is reduced to 24; no surjectivity is asserted.

The deletion also preserves every determinantal rank scheme. Locally split Q6 and the target. The matrix of beta_bar has the matrix of b and three zero rows. Every minor involving a zero row vanishes, while the remaining minors are exactly those of b. Thus their ideals of minors agree in every size, not merely after taking radicals or at closed points. Likewise K -> Q6 is locally a split surjection with kernel L, so the matrix of beta locally has the matrix of beta_bar and three zero columns. The determinantal ideals of beta, beta_bar and b agree. These statements are independent of the chosen local splittings and include any nilpotent structure in the degeneracy loci.

## 5. Contribution and limits

The new restriction removes an entire canonical three-dimensional target channel from the actual quartic obstruction, identifies its contribution as a canonical A O(4) summand of fifth-neighborhood R1, confines the remaining map to six one-dimensional equivariant channels, and reduces the exact two-root target from 30 to 24 while preserving every determinantal rank scheme. It requires the previously proved actual quotient, not a replacement of K by a trivial nine-space.

Neither the actual six scalars nor the rank, kernel splitting, or rank-drop divisor of b is selected. The actual quartic corrections remain inside b. No secondary survivors are declared global quadric sections. No claim about top sigma, vertex delta, source/catalogue cuts, or algebraicity is made. No selected actual HM/source coefficients, points, parameters, derivatives, jets, matrices, or instance ranks were evaluated; only fixed abstract character identities and exact universal sheaf arguments are used.
