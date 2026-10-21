# Lower-twist parity on smooth inversion-even quadrics

## Checked conclusions

Let B=End_0(F) for normalized HM, and let Q be any smooth inversion-even quadric. The actual lower-twist cohomology has no H2 or H3 and has parity Euler characteristics

    B_Q(2):  (chi_+,chi_-)=(-29,-34),
    B_Q(3):  (chi_+,chi_-)=(-19,-26).

Equivalently,

    h1(B_Q(2))_+ =29+h0(B_Q(2))_+,
    h1(B_Q(2))_- =34+h0(B_Q(2))_-,
    h1(B_Q(3))_+ =19+h0(B_Q(3))_+,
    h1(B_Q(3))_- =26+h0(B_Q(3))_-.

These indices do not force twist-three sections on the even family. They also do not prove their vanishing. The actual conic Koszul gate becomes an exact34-to38 presentation of the odd twist-four cohomology if H0(B_Q(3))_+=0. No generic vanishing from outside the even subsystem is used.

## 1. The missing primary trace in degree one

Retain the actual scalar epsilon on U=H0(F(3)), with det U trivial under inversion. On a general smooth beta blowup pi:X -> A, the actual all-even polarization P satisfies pi*P=H+C and the25 exceptional points are Sigma=K(Theta). Put

    V2=H1(A,P^2 I_Sigma^3)=H1(X,2H-C).

The actual restriction sequence for I_X(2) inside I_C(2) gives

    0 -> M2 -> V2 -> det B_beta tensor H1(F(1))* -> 0,
    M2=H1(I_C(2)).

Here H1(I_X(2))=0 follows from the Hilbert-Burch resolution and H2(F(1))=0. Together with H0(I_C(2))=0 this also proves H0(P^2 I_Sigma^3)=0. The notation B_beta denotes the three-dimensional section hyperplane, not the adjoint bundle B.

The ample P^2 has80 sections and inversion trace4. The triple jets on Sigma have length25*6=150 and trace1-2+3=2, since all nonzero points of Sigma are exchanged. Therefore V2 has dimension70 and trace-2. On the fixed HM line C00, O(2) has positive character, so trace H0(O_C(2))=3. Ambient quadrics also have trace3; hence M2 has dimension60 and trace0. The exact quotient has trace-2. As det B_beta has character epsilon,

    trace H1(F(1))=-2 epsilon.

This is an actual equivariant restriction calculation, not a choice of sign from the ten-dimensional size.

## 2. Negative primary twists and their sign

The normalized monad has terms5O(-1), 2 Omega^2(2), 5O. After twisting by-1, all three terms are acyclic by Bott, so F(-1) is acyclic. After twisting by-2, the two line-bundle terms remain acyclic, while Omega^2 has only H2 of dimension1. Consequently

    H^i(F(-2))=0 for i not equal to2,
    h2(F(-2))=2.

The involution on this two-dimensional group must still be identified. We do so from actual fiber characters, without choosing a character for the monad multiplicity space.

The fixed locus of iota on P4 is P(V_+)=P2 and C00=P(V_-)=P1. The fixed plane is disjoint from all25 HM lines: intersection with a nonfixed line would also lie on its distinct exchanged partner, contradicting disjointness. Evaluation U tensor O -> E=F(3) is therefore surjective on that plane, and E has scalar character epsilon there.

On C00 the image line O(6) has character epsilon. Since det E=O(5) has character-1 along that negative eigenspace line, the quotient O(-1) has character-epsilon. Therefore F(-2)=E(-5) restricts there as O(1) with character-epsilon and O(-6) with character epsilon.

Apply the holomorphic Lefschetz formula, with h the hyperplane class on each component. On P2 the underlying Chern character is

    ch(F(-2))=2-5h+(5/2)h^2,

and the normal bundle is O(1)^2 with negative character. The coefficient of h^2 in

    epsilon [2-5h+(5/2)h^2]
      [1+(3/2)h+h^2]/(1+exp(-h))^2

is -9 epsilon/8. On C00 the equivariant Chern character is epsilon(exp(-6h)-exp(h))=-7 epsilon h, while its normal bundle is O(1)^3 with negative character. Its contribution is -7 epsilon/8. Their sum is-2 epsilon. Since cohomology is concentrated in degree2,

    trace H2(F(-2))=-2 epsilon.

Both signs are thus compatible with the actual ambient involution and determinant linearization.

## 3. Ambient Euler characteristics, retaining the middle term

Use the actual exterior-symmetric resolution at any twist t:

    0 -> d O(t-10) -> wedge^2 U O(t-5)
      -> U F(t-2) -> B(t) -> T_t -> 0,
    T_t=ell^2(t-5),  ell|C_i=O(-1),  d=det U.

For t=0,1,2,3, all tails have only H1. Their dimensions are150,125,100,75, respectively. Only C00 contributes to the trace. Since ell^2 has positive character and O(t-5) has character(-1)^(t-5), the H1 tail traces are-6,+5,-4,+3, respectively.

The left line bundles O(t-10) have only H4. Their dimensions at t=0,1,2,3 are126,70,35,15, and their traces are6,6,3,3. At t=0 the middle term is wedge^2 U O(-5), whose H4 has dimension6 and trace6. This term must not be dropped. The middle terms at t=1,2,3 are acyclic.

The primary terms contribute as follows:

    t=0: U F(-2) has H2 dimension8 and trace-8;
    t=1: U F(-1) is acyclic;
    t=2: U F has H1 dimension20 and trace4;
    t=3: U F(1) has H1 dimension40 and trace-8.

Thus, summing the exact complex with its alternating signs, the ambient ordinary and equivariant Euler characteristics are

    B(0):  chi=126-6+8-150=-22,
           chi^iota=6-6-8+6=-2;
    B(1):  chi=70-125=-55,
           chi^iota=6-5=1;
    B(2):  chi=35-20-100=-85,
           chi^iota=3-4+4=3;
    B(3):  chi=15-40-75=-100,
           chi^iota=3+8-3=8.

At t=0 no concentration in H1 is asserted. The extension between the primary H2 term and the tail boundary must be retained.

## 4. Higher vanishings and uniform restriction to Q

The image sequences of the ambient resolution show H3(B(t))=H4(B(t))=0 for t=1,2,3. At t=0 the top-cohomology map

    d H4(O(-10)) -> wedge^2 U H4(O(-5))

is onto: its dual is the actual injection of the six independent determinant quintics into H0(O(5)). The image sequences again give H3(B)=H4(B)=0, without identifying H1(B) or H2(B) individually.

For t=2,3, the tail boundary is dual, under the actual adjunction and local Koszul normal form, to ambient restriction in degrees3 and2. The pinned H0(I_C(3))=H0(I_C(2))=0 makes that boundary onto. Thus H2(B(2))=H2(B(3))=0.

Now use the actual restriction sequences

    0 -> B(k-2) --q--> B(k) -> B_Q(k) -> 0,
    k=2,3.

The preceding higher vanishings give H2(B_Q(k))=H3(B_Q(k))=0. This argument does not require Q to be transverse to C; it applies to every smooth Q. For even q the restriction sequence carries no extra sign character on its first term. Consequently

    chi(B_Q(2))=-85-(-22)=-63,
    chi^iota(B_Q(2))=3-(-2)=5;
    chi(B_Q(3))=-100-(-55)=-45,
    chi^iota(B_Q(3))=8-1=7.

Taking half the sum and difference gives the claimed parity indices(-29,-34) and(-19,-26). In particular the main conclusions do not require an unverified no-quartic-equation input or any separate knowledge of the individual cohomology of B(0).

## 5. The precise34-to38 conic gate

Let C_+=Q intersect P(V_+) be the fixed conic. The actual evaluation is surjective there and B_Q(4) has only positive fiber character. Thus every odd section vanishes on C_+, and all cohomology of its restriction to C_+ has positive character.

Let u,v be the two odd ambient linear forms. The equivariant Koszul resolution of the conic ideal, tensored by B_Q(4), yields the exact odd cohomology sequence

    0 -> H0(B_Q(2))_- -> H0(B_Q(3))_+^2
      -> H0(B_Q(4))_- -> H1(B_Q(2))_-
      --kappa_Q--> H1(B_Q(3))_+^2 -> H1(B_Q(4))_- -> 0.

The multiplicity two retains the sign representation of the odd generators; the displayed subscripts have already accounted for that sign. The final zero uses H2(B_Q(2))=0.

Assume only H0(B_Q(3))_+=0. Then H0(B_Q(2)) vanishes in both parities: an even twist-two section multiplied by a nonzero even linear form, or an odd section multiplied by a nonzero odd linear form, would give a nonzero even twist-three section. Such multiplication is injective on sections of this locally free sheaf because Q is integral.

The indices therefore identify the remaining exact sequence as

    0 -> H0(B_Q(4))_- -> C^34 --kappa_Q--> C^38
      -> H1(B_Q(4))_- -> 0.

The actual map is the Koszul multiplication by u,v, not a freely chosen34-by38 matrix. Its injectivity remains an additional gate. The dimensions allow injectivity, but do not imply it. The positive twist-four H1 vanishing needed for exact total corank4 remains separate.

## 6. What a twist-three section would imply

A nonzero even twist-three section, multiplied by the two independent odd linear forms, gives at least two independent odd twist-four sections. A nonzero odd twist-three section, multiplied by the three independent even linear forms, gives at least three independent odd twist-four sections. In both cases injectivity follows because a nonzero linear form cannot annihilate a nonzero section of a locally free sheaf on integral Q.

Since the previously proved invariant twist-four index already forces at least four even sections, these alternatives force total twist-four dimensions at least6 and7, respectively. Thus exact twist-four corank4 requires full twist-three vanishing. The lower-twist Euler calculation does not itself force either alternative. It leaves a genuine parity-specific cohomology problem, now with the exact34-to38 gate above.

## 7. The actual ambient twist-three pencil

The preceding uniform index proof did not need H0(I_C(4))=0. Its independent provenance is now available: PR455 proves H2(B(1))=0 by the symmetric-square monad, a universal exterior-image estimate, and the normalizer dimension gap, without assuming a no-quartic statement. PR463 Section2 then uses the actual resolution-duality map of PR457 to prove injectivity of degree-four restriction, hence H0(I_C(4))=0.

Concretely, tail restriction duality gives

    H2(B(1))=d H0(I_C(4))*,
    H1(B(1))=d M4*,   M4=H1(I_C(4)).

Thus B(1) is concentrated in H1 with parity(27,28). The verified degree-two restriction injectivity similarly gives B(3) concentrated in H1 with parity(46,54). The actual even twist-three multiplication is exactly

    (27 -> 46) directsum (28 -> 54),

which forces no kernel. These are actual multiplication blocks; their injectivity is not inferred from their dimensions.

The immutable source pins are PR455, 8cbbe482ee50c35d52ffcdf3efb837fa8cf96af4, research/hm/twist-one-structural-vanishing/PROOF.md, and PR463, 8ec3631dcd6937e6cc7491d0200c1c78b5d21434, research/hm/order-four-residue/PROOF.md, Section2. The latter identifies its boundary-duality input as PR457 at961694c4f3c805f0d58508811a42da4030dce7a6. This is the25-line scheme C, not a no-quartic assertion for a different HM surface.

Dependencies: normalized HM monad and primary support, ADHPR Section3, https://arxiv.org/pdf/alg-geom/9606013v2 ; actual exterior-symmetric resolution at d5d9bd997145b0ecf7d7bd659a19fb7845afb75f; compatible tail duality at22bdcb7e9c833e7a1819d0ec28e5e615be9c7a4f; the companion actual beta, inversion, and full-pencil notes. No selected coefficients, evaluated matrices, ranks, or experiments occur.
