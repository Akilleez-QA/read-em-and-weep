# A saturated quadratic-block obstruction excludes one profile-(1,2) label

## Result and scope

Work over C, with the binary icosahedral group G and its defining two-dimensional representation W. Write Wp for the other two-dimensional irreducible, A=Sym^2 W, S=Sym^3 W, D=Sym^4 W, T=Sym^5 W, and V,P for the remaining three- and four-dimensional irreducibles. All representations are self-dual.

The profile-(1,2) label

    G3.12.34bc2083d563,
    A_q = 2 O(-8) + O(14),
    B_q = O(-16) + 2 O(6),

is impossible. This is a full label exclusion, not merely an exclusion of a splitting stratum or of one determinant-defect choice. It uses the actual constant connection, the original zero-defect quotient, and the absence of constant sections in the interior forward stage.

The same argument excludes primal E-catalog entries 0 and 10 whenever they occur for either other retained profile-(1,2) label. A further small syzygy argument also excludes entries 3 and 12. The necessary source lists therefore reduce to:

    G3.12.37914c53373c: only E-catalog entry 6;
    G3.12.eed6acb13f3e: only E-catalog entries 6 and 13.

Neither of those two labels is excluded here. The source2 label G3.21.d610e381ed75 is not involved. Relative to the published 23-label frontier, this removes exactly one label and leaves 22, with profile counts 19/2/1. It does not prove SF>=4, square rank>=28, or the original research goal.

No actual HM coefficients, parameters, points, derivatives, instance matrices, or source-instance ranks are selected or evaluated. Only formal hypothesis branches, exact sequences, universal representation identities, and arbitrary-point arguments are used.

## 1. Immutable public inputs

All paths in this paragraph are under

https://github.com/Akilleez-QA/read-em-and-weep/blob/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load/

The exact inputs are:

1. `ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md`: the actual inclusion E in the constant thirty-space, H0(E(1))=0, the 28 equivariant E types, and the maximal plateau convention.
2. `NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md`: H0(E^-(2))=0.
3. `ONE-TWO-FINITE-QUOTIENT-PAIRS-AND-ZERO-DEFECT.md` and `one-two-finite-quotient-pairs.json`: the actual original derivative quotient A_q=B_q^*(-2), with no determinant torsion, and the E-catalog entries compatible with the old pair IDs 0,6,12.
4. `rank-three-quotient-frontier-144.json`: the stable labels identify those old pair IDs as G3.12.37914c53373c, G3.12.34bc2083d563, G3.12.eed6acb13f3e, respectively.
5. `PRIMAL-SECOND-SPAN-ANNIHILATOR-RANK-OBSTRUCTION.md` and its same-stem JSON certificate: the theorem of PR757 at this commit excludes G3.11.942927348917 and G3.12.8e9af2d08af9. Separately, the public PR757 publication and review report the cumulative preceding frontier as 23 labels with profile counts 19/3/1: https://github.com/Akilleez-QA/read-em-and-weep/pull/757#pullrequestreview-5617908618 . The 23-to-22 accounting above is relative to that reported cumulative baseline; the new full-label exclusion does not depend on that accounting.

Only the listed conclusions are used. In particular, neither a source2 constant-block normal form nor a connection on an arbitrary abstract bundle complement is imported.

For profile (1,2), E^+ is an interior plateau stage and

    (E^+)^- = E.

A constant section of E^+ belongs to this kernel, while H0(E)=0. Consequently

    H0(E^+) = 0.                                            (1)

Every subbundle of E^+ must therefore have zero H0 as well.

The derivative of E factors as its quotient E -> A_q followed by the saturated injection

    A_q = B_q^*(-2) -> Q(-2),
    Q = (H O)/E.                                            (2)

Saturation follows because B_q is the genuine locally free quotient of Q*, and because the original determinant defect is zero. Thus the O(14) summand of A_q is also saturated in Q(-2).

The relevant E-catalog entries, with their actual equivariant bundle splittings, are:

    0:  (P+2D) O(-2) + 2 O(-8) + O(-10);
    10: (P+2D) O(-2) + O(-8) + W O(-9);
    18: 2D O(-2) + Wp O(-3) + V O(-4) + 2 O(-8);

    3:  (V+P+D) O(-2) + V O(-4) + O(-8) + O(-10);
    12: (V+P+D) O(-2) + V O(-4) + W O(-9);
    6:  (P+D) O(-2) + T O(-3) + O(-8) + O(-10);
    13: (P+D) O(-2) + T O(-3) + W O(-9).

For old pair6 the complete necessary source list is exactly {0,10,18}. For pair0 it is {0,3,6}, and for pair12 it is {0,3,6,10,12,13}. These are copied from the pinned catalog, not inferred from the new argument.

## 2. The actual top block gives a basepoint-free degree-sixteen system

In any of the seven displayed E types let

    F = R O(-2)

be the canonical top-slope subbundle. Every other summand has degree at most -3. Each A_q under consideration has one positive summand O(14), and its other summands have degrees -8,-9, or -10. Hence the restriction of E -> A_q to F lands in O(14).

The exact quotient sequence and H0(E^-(2))=0 show that

    H0(E(2)) -> H0(A_q(2))

is injective. Its source is exactly R, and the only target sections are those of O(16). Thus the morphism

    p:F -> O(14)                                           (3)

is represented by an injective equivariant linear system R -> H0(O(16)). This independence is a consequence of the actual Gauss kernel; it is not inferred merely from rank F.

The possible dimensions of R are 14,12,10,9. If the common zero divisor of this system had degree d>0, it would be invariant and so d>=12, because every projective A5 orbit has at least twelve points. But then its space of sections would have dimension at most h0(O(16-d))<=5, contradicting dim R>=9. Therefore (3) is onto at every point.

Set K0=ker p. Twisting (3) by two gives

    0 -> K0(2) -> R O -> O(16) -> 0.                       (4)

The map on H0 is injective, so every splitting degree of K0(2) is at most -1. In particular K0 has degrees at most -3. Since H1(R O)=0, (4) also gives the exact quotient representation

    H1(K0(2)) = Sym^16 W / R.                              (5)

The universal decomposition is

    Sym^16 W = V+P+2D,
    Sym^17 W = Wp+S+2T.                                  (6)

## 3. A saturated derivative-image lemma

This lemma retains the original ambient connection.

Suppose F is a subbundle of E, and the projection of its derivative to Q(-2) factors through an onto map p:F -> O(14), followed by the saturated inclusion in (2). For K0=ker p, differentiation followed by projection defines an O-linear map

    kappa:K0 -> (E/F)(-2).                                (7)

It is O-linear because a change by f times a section contributes df times that section, which lies in F and disappears in E/F. Let J be its image. If J is saturated in (E/F)(-2), then the full image I of the derivative of F in (H O/F)(-2) has an exact sequence

    0 -> J -> I -> O(14) -> 0.                            (8)

Both end images are saturated in the respective actual subbundle and quotient. Hence I is saturated in (H O/F)(-2): the quotient is an extension of the two locally free quotients. The actual saturated forward transform therefore satisfies

    0 -> F -> F^+ -> I(2) -> 0.                          (9)

No hidden divisor is introduced on taking F^+. In particular, if J has rank u and degree v, then

    rank F^+ = rank F + u + 1,
    deg F^+ = deg F + v + 2u + 16.                       (10)

Because F is an actual subbundle of E in the same constant ambient space, F^+ is contained in E^+. By (1),

    h0(F^+)=0,  hence chi(F^+)=rank F^+ + deg F^+ <=0.    (11)

This is an interior-stage obstruction, not a formal splitting-count inequality.

## 4. Exclude source entries 0 and 10

Here rank F=14, deg F=-28, and rank K0=13. From (4), K0(2) has degree -16 and thirteen strictly negative splitting degrees. Write these as -b_i, with b_i>=1 and sum b_i=16. Thus every b_i<=4, and

    -6 <= each degree of K0 <= -3.

For both entries 0 and 10 every degree of (E/F)(-2) is at most -10. Therefore (7) is zero by ordinary degree considerations. Taking J=0 in the saturated-image lemma gives

    rank F^+=15,   deg F^+=-12,   chi(F^+)=3.

This contradicts (11). Both entries are impossible in any of the three stated profile-(1,2) labels.

## 5. The exact kernel for source entry 18

Here R=2D, so (5) gives H1(K0(2))=V+P. The tensor identities

    D W=S+T,
    Wp W=P

give

    chi(K0(3)) = 2D W - Sym^17 W = S-Wp.                 (12)

We now determine K0 without choosing a map. An irreducible block R' O(-j) with j>=4 contributes R' Sym^(j-4)W to H1(K0(2)); this must be a subrepresentation of V+P. Its dimension is (j-3)dim R'<=7, and its central sign is (-1)^j. Checking this short bound gives exactly the following four supported blocks:

    block             H1 at twist2      H1 at twist3
    V O(-4)          V                  0
    P O(-4)          P                  0
    Wp O(-5)         P                  Wp
    O(-10)           V+P                T

Completeness can also be seen directly: at j4 only V,P fit; at j5 only W,Wp have small enough dimension, and W W=1+A whereas Wp W=P; at j6 only the trivial representation can fit and gives A; at j7 no odd irreducible has small enough dimension; at j8 the trivial representation gives D; at j9 again no odd irreducible fits; at j10 the trivial representation gives Sym6 W=V+P. No j>10 is possible. Degree -3 blocks contribute no H1 at twist2.

The V+P budget can therefore be assembled in only three ways: V O(-4)+P O(-4); V O(-4)+Wp O(-5); or O(-10). In the first case (12) would make H0(K0(3))=S-Wp, impossible. In the third it would make H0(K0(3))=S+T-Wp, also impossible. The middle case gives H0(K0(3))=S. Since rank K0=9, the remaining degree -3 block is precisely S O(-3). Thus necessarily

    K0 = S O(-3) + V O(-4) + Wp O(-5).                  (13)

This is an equivariant bundle identity, not a horizontal splitting.

## 6. Exclude source entry 18 and the whole label

For entry18,

    (E/F)(-2)=Wp O(-5)+V O(-6)+2 O(-10).

By (13), every component of (7) is zero except possibly the constant scalar map from its Wp O(-5) summand to the identical Wp O(-5) target. Schur's lemma makes this either zero or an isomorphism. Consequently J is either zero or the full saturated subbundle Wp O(-5).

If J=0, (10) gives

    rank F^+=11,  deg F^+=-4,  chi(F^+)=7.

If J=Wp O(-5), its rank is two and degree is -10, so (10) gives

    rank F^+=13,  deg F^+=-10,  chi(F^+)=3.

Both violate (11). Source entry18 is impossible.

The complete pinned source list for G3.12.34bc2083d563 was {0,10,18}. Sections4 and6 exhaust it, proving the label excluded. The proof never distinguishes or assumes the separate second-dual determinant defect: all its possible strata are covered simultaneously.

## 7. Additional source reductions for the other two labels

For entries3 and12, R=V+P+D. Equations(5)-(6) give

    H1(K0(2))=D,
    chi(K0(3))=T.

The same small dimension/parity argument as in Section5 shows that the only blocks contributing to the D budget are D O(-4) and O(-8). Indeed (j-3)dim R'<=5; j4 permits D, j5 permits W,Wp but their products are 1+A and P, j6 gives A, j7 has no eligible odd irrep, and j8 gives D. Thus the only possible kernels are

    K0=T O(-3)+D O(-4),
    K0=(S+T) O(-3)+O(-8).                               (14)

For entry3 the target (E/F)(-2) is V O(-6)+O(-10)+O(-12), and for entry12 it is V O(-6)+W O(-11). The only component not excluded by ordinary degrees in (14) could be O(-8)->V O(-6). Its equivariant Hom is zero because V does not occur in Sym2 W=A. Therefore J=0 in both cases.

Now rank F=12 and deg F=-24, so

    rank F^+=13,   deg F^+=-8,   chi(F^+)=5,

again contradicting (11). This excludes entries3 and12. The remaining source lists stated at the beginning follow from the complete original lists; entries6 and13 are not excluded by this argument.

## 8. A separate reusable quadratic Gauss-gap lemma

The exclusions above used the stronger profile-(1,2) interior condition. The following connection lemma independently verifies the entry0/10 obstruction and applies without that profile assumption.

Let F=O(-2)^r be a saturated subbundle of a constant bundle. Suppose its derivative has generic rank one, and the saturated first forward quotient is F^+/F=O(b). Then

    b=2r, or b<=r-1.                                    (15)

To prove this, trivialize O(-2) on an affine chart. The inclusion is represented by r vector-valued polynomials of degree at most two. At every affine point, their values and first two derivatives span precisely their constant coefficient space: the triangular change of generators has nonzero factorial diagonal. Thus the second saturated forward transform F^{++} is the full constant span V O.

The derivative of F^+ kills F and therefore factors through its line quotient O(b). Hence dim V is at most r+2 and at least r+1. If dim V=r+1, F^+=V O and its degree zero gives b=2r. Otherwise dim V=r+2, and V O/F^+ is the line O(2r-b). The nonzero derivative of F^+ gives a nonzero map

    O(b) -> O(2r-b-2),

so b<=r-1. This proves (15). In particular r14,b16 is impossible. No constant change of coordinates or abstract bundle complement is assumed in this argument.

## Verification boundary

All derivative maps are between established subbundles and quotients of the same original constant bundle. The only splitting computations are for kernels of the actual top-block quotient and use exact cohomology and a complete small dimension bound. The decisive step is the saturated image sequence (8), followed by the already-established absence of constant sections in E^+.

No use is made of the withdrawn recursive symbolic-division method or of an extension of the previously exhausted all-twist envelope. This is a written structural proof. It is not proof-assistant certification or an actual HM tensor computation.
