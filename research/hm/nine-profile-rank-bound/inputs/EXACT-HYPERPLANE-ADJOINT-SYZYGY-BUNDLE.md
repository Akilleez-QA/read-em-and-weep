# The exact hyperplane adjoint syzygy bundle

## Theorem

Let X be the universal hyperplane containing the positive fixed plane R in P4. Write

    p:X=Bl_R(P4) -> P4,       pi:X -> T=P(W*),
    B=End_0 F,

where F is the actual normalized HM bundle. Then, equivariantly,

    pi_* p*B(3) = A tensor O_T(-6),       A=Sym^2 W.    (1)

This is an equality of the actual section bundles, not merely an equality on a generic open set. It remains true at the twelve parameters where an individual fiber may have additional sections not extending to nearby fibers. The entire pushforward is inversion-even; its odd part is zero.

Consequently the actual even universal hyperplane multiplication map has the exact sequence

    0 -> A O_T(-6) -> C^44 tensor O_T(-1)
      -> C^46 tensor O_T -> C -> 0,                    (2)

where C is its actual cokernel sheaf. The vector spaces in (2) are the indicated fixed ambient cohomology eigenspaces, not arbitrarily chosen vector spaces. The sheaf C has rank five and degree26, including any torsion in that degree. Any torsion is supported at the twelve exceptional parameters; no assertion that it is nonzero or that C is locally free is made.

For every integer n>=0 there is an equivariant isomorphism

    H0(P4,I_R^n B(n+3)) = A tensor H0(T,O_T(n-6)).      (3)

In particular this space vanishes for 0<=n<=5, and at n=6 it is the actual three-space of products

    Sym^2 H0(P4,I_R^3 F(5))
       = H0(P4,I_R^6 B(9)) = A.                       (4)

No full-adjoint vanishing or rank claim about a smoothing obstruction follows from this theorem alone.

## 1. Inputs

HYPERPLANE-SQUARE-SURVIVORS.md gives the actual section bundle

    Y=pi_*p*F(2)=W tensor O_T(-3),

with h0(F_Hlambda(2))=2 for every lambda. Its two sections are even. Their three quadratic products are independent on every hyperplane, including the twelve exceptional ones. The equivariant identity Sym^2 F_H(2)=B_H(3) identifies the natural square map with

    Sym^2 Y=A tensor O_T(-6) -> pi_*p*B(3).            (5)

HYPERPLANE-ADJOINT-EXHAUSTION-AND-SIX-TO-TEN.md proves that the target has fiber section dimension exactly three off the twelve exceptional parameters, and all those sections are the products in (5). Its geometric proof uses the checked Bănică–Manolache classification and the actual factor-cover polarization, not a generic-moduli transfer.

The actual ambient cohomology used in Section 3 is

    H0(B(2))=H0(B(3))=0,
    H1(B(2)) has parity dimensions (41,44),
    H1(B(3)) has parity dimensions (46,54),
    H2(B(2))=0.

The H2 vanishing is PR167, [pin063da90](https://github.com/Akilleez-QA/read-em-and-weep/blob/063da90fc4543304e87e701cdefcc08225412f17/research/conductor-normalization/sharper-hm-regularity/SHARPEST-BOUND.md). The actual equivariant dimensions are those used in the prior lower-twist and hyperplane-obstruction artifacts.

## 2. Why jumps do not alter the pushforward kernel bundle

Set E=pi_*p*B(3). It is torsion-free on the smooth curve T: a nonzero base function acts injectively on the vector bundle p*B(3) on the flat integral family X, hence also on its pushforward. Therefore E is locally free. Its generic rank is three by the exhaustion theorem.

At every t in T the natural base-change map

    E tensor k(t) -> H0(H_t,B_Ht(3))                   (6)

is injective, even if H0 jumps at t. Indeed, work over the local DVR at t, with uniformizer z. Flatness gives the exact sequence

    0 -> p*B(3) --z--> p*B(3) -> B_Ht(3) -> 0.

After pushforward, the kernel of restriction on H0 is exactly zE. Passing to the quotient gives (6). Surjectivity at exceptional parameters is not asserted.

The composition of the fiber of (5) with (6) is the ordinary square map on the actual two-dimensional section space of F_Ht(2). That square map is injective at every t. Since the source and E both have rank three, (5) is consequently a fiberwise isomorphism at every point. Nakayama's lemma proves the global isomorphism (1).

The odd eigensubsheaf of E is torsion-free and has generic rank zero, so is zero. The center acts trivially on A O(-6), in agreement with the even parity of all extending square sections. This does not rule out odd sections of an isolated exceptional fiber; such sections need not lie in the image of (6).

## 3. The actual universal multiplication sequence

The incidence hypersurface X inside P4 x T has the universal restriction sequence

    0 -> B(2) external-tensor O_T(-1)
      -> B(3) external-tensor O_T
      -> j_*p*B(3) -> 0.                               (7)

Its equation is a negative linear form. The standard binary linearization on O_T(-1) is center-odd. Thus the inversion-even block of the pushed-forward map in (7) has source H1(B(2))_- tensor O_T(-1), of rank44, and target H1(B(3))_+ tensor O_T, of rank46. This accounts for the parity reversal; one must not use the 41-to-46 block.

The ambient H0 vanishings identify its kernel with E. The vanishing H2(B(2))=0 identifies its cokernel with the even part of R1 pi_*p*B(3). This proves the exact sequence (2) with its actual maps.

In the Grothendieck group of T,

    [C]=46[O]-44[O(-1)]+3[O(-6)].

Hence rank(C)=46-44+3=5 and deg(C)=44-18=26. These are sheaf invariants including torsion; they do not give the splitting type of its torsion-free quotient.

The exact base-change sequence of this two-term presentation is

    0 -> A O(-6) tensor k(t)
      -> H0(H_t,B_Ht(3))_+
      -> Tor_1(C,k(t)) -> 0.                           (8)

Off the twelve exceptional points the middle space has dimension three, so Tor_1(C,k(t))=0 and C has no torsion there. Formula (8) precisely separates the globally extending square bundle from any extra individual-fiber sections.

## 4. Exact normal-order section spaces on P4

Let E_R be the exceptional divisor of p. The universal hyperplane pencil satisfies

    pi*O_T(1)=p*O_P4(1) tensor O_X(-E_R).              (9)

For n>=0, projection formula and (1) give

    H0(X,p*B(3) tensor pi*O_T(n))
      =H0(T,A tensor O_T(n-6)).                        (10)

Using (9), the bundle on the left is p*B(n+3) tensor O_X(-nE_R). The blowup identity p_*O_X(-nE_R)=I_R^n and projection formula identify its H0 with H0(P4,I_R^n B(n+3)). This proves (3), with all parameter-line twists retained.

At n=6 the source square bundle gives the natural product map

    Sym^2 H0(T,Y(3)) -> H0(T,Sym^2 Y(6)).

Since Y(3)=W tensor O_T, this is the identity on Sym^2 W=A. The corresponding blowup identities are

    H0(T,Y(3))=H0(P4,I_R^3 F(5)),
    H0(T,Sym^2 Y(6))=H0(P4,I_R^6 B(9)).

The multiplication is the actual product of sections, under Sym^2 F(5)=B(9). This proves (4), not just its dimension.

## Scope

The kernel bundle (1) is exact on all of T although fiber cohomology can jump at twelve points. It does not prove that the intermediate rank-nine normal kernel is exhausted by squares before its later obstruction. It also does not compute the six-to-ten global smoothing map. Formula (3) concerns ambient sections with the specified ideal-power vanishing along R; it is not a statement about arbitrary adjoint sections or arbitrary quadrics.
