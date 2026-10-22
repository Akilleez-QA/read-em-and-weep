# The actual quintic scalar cup is a swapped-quotient isomorphism

## Result and scope

Let p represent the actual nonzero equivariant quintic extension

    e in H1(L,V O(-8)),

and use the positive second transvectant tau_2. The actual linear map

    C_e:H0(L,D5 O(2)) -> H1(L,V O(-6)),
    u |-> [tau_2(p,u)]                                      (1)

is an isomorphism of fifteen-dimensional representations. This identifies an actual cup factor, not merely an allowed representation channel. Both sides have character A+V+P4+D5.

Consequently its quotient by the connecting A subspace is onto the twelve-dimensional reduced lower source. For every nonzero smoothing quadratic a, its subsequent multiplication and square-ideal boundary are onto P4. None of these statements evaluates the sum of this scalar term with the other terms in the actual vector cochain R, or its final quotient by the actual second symbol.

## 1. Swap the two actual projections

The actual cubic support D is the smooth (3,3) divisor in P(Wprime) x P(W). The actual local quintics g give a nowhere-zero section of O_D(5,-5). Its inverse is a nowhere-zero section of O_D(-5,5). Retain this inverse, rather than inventing a second unrelated quintic.

Now project onto P(Wprime), treating the W coordinates as the fiber coordinates. Locally on this base, the inverse section lifts to a homogeneous quintic in W. Indeed the restriction sequence is

    0 -> O(-8,2) --f--> O(-5,5) -> O_D(-5,5) -> 0.

The kernel has fiber degree2, hence no higher fiber cohomology. On an affine base chart its H1 vanishes, so local lifts exist. Two lifts differ by f times a W quadratic. Since the restriction is nowhere zero, f and each lifted quintic are fiberwise coprime. Thus the swapped data form the same relative complete-intersection construction of degrees(3,5).

Let R_j denote its degree-j fiber algebra on P(Wprime). The relation bundles are O(-3) in degree3 and O(5) in degree5. Therefore R_2=A O and its socle R_6 is O(2). One can also read the latter degree directly from the degree6 resolution: the source is Sym3(W) O(-3) plus W O(5), of total degree -12+10=-2, and the target Sym6(W) O has degree0.

The perfect complete-intersection pairing R_4 tensor R_2 -> R_6 identifies R_4 with A O(2). Hence the actual swapped quartic quotient is

    0 -> W O(-3) -> D5 O --Q_sw--> A O(2) -> 0.     (2)

All identifications are equivariant. The socle is a line of degree2 with its unique binary-icosahedral linearization. Twisting(2) by2 and using H0(O(-1))=H1(O(-1))=0 gives an isomorphism

    H0(Q_sw(2)): D5_negative tensor V_positive
                  -> A_negative tensor D5_positive.       (3)

No actual matrix or source coefficients have been evaluated.

## 2. Identify the actual tensor, not just its channel

Here the swapped socle functional is being used, not the swapped quintic extension class. The latter instead belongs to A tensor Sym6(Wprime)* and must not be identified with e. The swapped socle functional is a nonzero equivariant map

    lambda_sw:Sym6(W) -> H0(P(Wprime),O(2))=V.

The decomposition Sym6(W)=V+P4 makes this Hom space one-dimensional. Under Serre duality on L=P(W), the actual nonzero e in V tensor H1(O(-8)) gives another nonzero map Sym6(W)->V. Therefore lambda_sw is a nonzero scalar multiple of the ACTUAL e tensor. The unspecified nonzero scalar includes the chosen socle and apolar normalizations; no numerical value is assigned to it.

More explicitly, polarize the original e tensor through the injective Cartan inclusion Sym6(W) -> Sym2(W) tensor Sym4(W). This gives a nonzero invariant tensor in V tensor A tensor D5_negative. That invariant space is one-dimensional because A tensor D5_negative contains V exactly once. The nonzero coefficient tensor of Q_sw lies in precisely this space. Thus it is proportional to this polarized e tensor before any passage to the fifteen-spaces. This is not an identification based on the four-dimensional Hom space between those fifteen-spaces.

The map(3) sends a negative quartic b and a positive quadratic v to the product of v with the V-valued quadratic coefficient obtained from lambda_sw(b r), where r ranges over negative quadratics. This is the socle-pairing definition of Q_sw, followed by multiplication of positive quadratic sections.

Transpose this statement using invariant apolar forms and Serre duality. The negative multiplication b r transposes to cup product of e with r in H0(O(2)). The positive multiplication of two quadratics transposes to the positive second transvectant from a quadratic and a quartic to a quadratic. Thus the transpose of(3) is a nonzero scalar multiple of(1).

For a concrete convention, define the degree-n apolar form on ordinary monomial coefficients by

    <F,G>_n = sum_j (-1)^j F_j G_(n-j) / binomial(n,j).

Then the universal identity is

    <tau_2(r,u),v>_2 = 24 <u,r v>_4,                (4)

for positive degrees2,4,2. Serre duality makes multiplication and cup product transposes without any further vanishing assumption. Equation(4) verifies that the factor is nonzero and that the asserted transpose is the actual operation. Since(3) is an isomorphism, so is C_e.

## 3. Consequences for the scalar part of R

The proven lower-source sequence is

    0 -> A -> H1(V O(-6)) -> P4 tensor A -> 0.

Accordingly, the composite of C_e with this quotient is onto12 and has kernel an actual A subrepresentation of H0(D5 O2). After multiplication by any a != 0, the resulting map to P4 is onto4. This uses the actual lower multiplication theorem, not a nonzero-legs argument.

Combining this result with the previously proved surjectivity of the canonical scalar inverse u(S,h) shows that the isolated u contribution [tau_2(p,u(S,h))] fills the entire fifteen-space. After the connecting A quotient, this isolated polarized u contribution has image V+P4+D5 and kernel 1+A+P4+D5 in D5_positive tensor D5_negative. In particular its V, P4, and D5 output channels are all nonzero. This does not exclude membership in the three-dimensional kernel of the later trace-free family-to-gate map.

The full Gamma correction also includes its prescribed affine-frame term, and the full R includes the a^2 terms. Their cancellations remain to be determined. In particular this theorem does not prove the actual third Bockstein nonzero.

## Sources and verification

Use ACTUAL-CUBIC-SUPPORT-IS-GENUS-FOUR-WITH-EXACT-FIVE-TORSION.md for the actual divisor and quintic trivialization; ACTUAL-CUBIC-FIVE-TORSION-FAILS-ON-ITS-DOUBLE.md for the identification of the actual nonzero quintic class; ACTUAL-CANONICAL-SCALAR-CORRECTION-SURJECTS-ONTO-FIFTEEN-SPACE.md for the scalar inverse; and the actual lower-multiplication and canonical-vector-cochain notes for the final quotient diagram.

The companion verifier checks the universal apolar identity, the complete-intersection line degrees, and the exact representation arithmetic. It does not instantiate HM coefficients or evaluate an actual matrix rank.
