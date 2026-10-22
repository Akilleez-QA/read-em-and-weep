# A tensor-quartic constant subsystem and exact residual for the remaining profile-(1,2) source strata

## Result and scope

Let E be the actual rank-17 degree-minus-54 subbundle of the constant thirty-space H O in the formal profile-(1,2) Gauss setup described below. Suppose its equivariant bundle type is either

    E6  = (P+D) O(-2) + T O(-3) + O(-8) + O(-10),
    E13 = (P+D) O(-2) + T O(-3) + W O(-9),

and its actual original Gauss quotient A_q has one O(14) summand and two negative-rank directions of degree at most -8, with original determinant defect zero.

Then the canonical top block F=(P+D) O(-2) forces a genuine invariant constant subspace

    C0 = V tensor Sym^4 W = A+V+P+D,    dim C0=15,

inside H. If U_j^4 denotes the j-th complete degree-four osculating bundle, of rank j+1 and bundle type Sym^j W O(j-4), then, in this actual constant subspace,

    F   = V tensor U_2^4,
    F^+ = V tensor U_3^4.

Moreover the actual sheaf intersections N=E intersect (C0 O) and Nplus=E^+ intersect (C0 O) are saturated subbundles of C0 O and satisfy

    rank Nplus=14,   deg Nplus=-18,   (C0 O)/Nplus=O(18),
    N=(Nplus)^-,     rank N=13,        deg N=-34,
    N/F=P O(-4),     N=(P+D) O(-2) + P O(-4)

as equivariant bundles in the last identity. The locally free image sheaf Z=E/N has rank four and degree minus twenty, maps generically fiberwise injectively into (H/C0) O, and has bundle type

    E6 case:  Z=Wp O(-1) + O(-8) + O(-10),
    E13 case: Z=Wp O(-1) + W O(-9).

Saturation of Z in (H/C0) O is not asserted. Likewise a sheaf intersection is not identified with the full fiberwise intersection at every point; fibers may jump.

This is an actual constant-subsystem and sheaf-intersection theorem, not merely an equality of abstract Euler characters. It does not assert a constant splitting E=N direct-sum Z or a flat splitting of the residual extension. Neither of the two remaining profile-(1,2) labels is excluded by this theorem. No source2 claim is made.

## 1. Immutable public dependencies and notation

All public file dependencies below are at commit

    db51525015bb7c5e825833d550d08dedf6f6ea96

of Akilleez-QA/read-em-and-weep, under

https://github.com/Akilleez-QA/read-em-and-weep/blob/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load/

The exact dependencies are:

- ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md: actual constant inclusion, equivariant source catalog, H0(E(1))=0, and maximal plateau convention.
- NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md: H0(E^-(2))=0.
- ONE-TWO-FINITE-QUOTIENT-PAIRS-AND-ZERO-DEFECT.md and one-two-finite-quotient-pairs.json: genuine original quotient A_q=B_q^*(-2), zero original determinant torsion, and the compatible source entries.
- rank-three-quotient-frontier-144.json: stable label identification. The relevant labels are G3.12.37914c53373c, with A_q=O(-10)+O(-8)+O(14), and G3.12.eed6acb13f3e, with A_q=W O(-9)+O(14). Their old pair IDs are 0 and 12. E6 can occur in both source lists, and E13 in the second.

The reduction of the two labels to exactly these source strata is now public in PR796, pinned at commit d2b43060c83328dd5118aee6b9288fcfa0c873ac:

https://github.com/Akilleez-QA/read-em-and-weep/blob/d2b43060c83328dd5118aee6b9288fcfa0c873ac/research/hm/profile12-quadratic-block-exclusion/PROOF.md

That proof has SHA256 622763aac375db7e17bc7cab472f1afda0477b0f769371a3b3ef845cd5c9e3b1. The present theorem applies to its two surviving profile-(1,2) labels. Its local derivation is also valid directly conditional on E6/E13, without needing the exclusion of the other types.

Work over C with the binary icosahedral group G. Its defining representation is W; the other two-dimensional irreducible is Wp. Put A=Sym^2 W, S=Sym^3 W, D=Sym^4 W, T=Sym^5 W; V and P are the remaining three- and four-dimensional irreducibles. All irreducibles are self-dual. The center acts trivially on the ambient constant space H. Consequently the coefficient representation of a degree-e line block has central sign (-1)^e.

Because the profile is (1,2), E^+ is an interior maximal plateau stage and

    (E^+)^-=E,     H0(E^+)=0.                            (1)

The second statement follows since a constant section of E^+ lies in its backward kernel E, while H0(E)=0. All derivatives below are restrictions and projections of the original constant connection. No abstract complement receives an invented connection.

## 2. The top-block quotient and its exact kernel

The restriction of the actual quotient E -> A_q to F=(P+D) O(-2) lands in O(14). The strict-top vanishing H0(E^-(2))=0 makes its nine degree-sixteen sections linearly independent. Any common zero divisor is G-invariant. A nonempty such divisor has degree at least twelve, whereas nine independent sections of O(16) cannot have a common divisor of degree twelve or more. Thus

    p:F -> O(14)

is onto everywhere. Its kernel K0 satisfies

    0 -> K0(2) -> (P+D) O -> O(16) -> 0,
    H0(K0(2))=0,
    H1(K0(2))=V+D,
    chi(K0(3))=0.                                       (2)

Here Sym16 W=V+P+2D, Sym17 W=Wp+S+2T, PW=Wp+T, and DW=S+T.

Every degree of K0 is at most -3. A block R O(-j), j>=4, contributes R Sym^(j-4)W to H1(K0(2)), a subrepresentation of V+D. The dimension bound is (j-3) dim R<=8, with the stated central parity. The complete possible nonzero contributors are

    V O(-4):   H1 at twist2 = V,     at twist3 = 0;
    D O(-4):   H1 at twist2 = D,     at twist3 = 0;
    Wp O(-7):  H1 at twist2 = V+D,   at twist3 = T;
    O(-8):    H1 at twist2 = D,     at twist3 = S.

For completeness: j4 permits V,D; j5 permits W,Wp but their products with W are 1+A and P; j6 only a trivial coefficient is small enough and gives A; j7 permits W,Wp, with products A+D and V+D; j8 permits only the trivial coefficient and gives D; j9 has no eligible odd coefficient; j10 gives Sym6 W=V+P; j11 has no eligible odd coefficient; and j>=12 exceeds the bound. Thus, using chi(K0(3))=0 and rank K0=8, precisely three kernel types remain:

    (V+D) O(-4),
    S O(-3) + V O(-4) + O(-8),
    T O(-3) + Wp O(-7).                                 (3)

## 3. The internal derivative is forced and saturated

Differentiation of K0, followed by projection, defines the O-linear map

    kappa:K0 -> (E/F)(-2).

It is O-linear because the Leibniz correction lies in F. The target is

    T O(-5) + O(-10) + O(-12),  or
    T O(-5) + W O(-11).

For the first two kernel types in (3), all components vanish by degrees except possibly O(-8)->T O(-5), which also vanishes since T does not occur in Sym3 W=S. Thus those types have kappa=0.

For the last type, the only component is

    Wp O(-7) -> T O(-5),

whose equivariant Hom space is one-dimensional since Wp tensor A=T. Every nonzero map in this space is the standard everywhere-injective map

    Wp tensor O(-2) -> Wp tensor (Sym2 W O),

twisted by -5: at a line l in W it is the inclusion Wp tensor l^2 into Wp tensor Sym2 W. Its image is saturated and isomorphic to Wp O(-7).

Let J be the image of kappa, and I the full image of the derivative of F in (H O/F)(-2). Because p is onto and O(14) is saturated in the genuine Q(-2), where Q=(H O)/E, there is an exact sequence

    0 -> J -> I -> O(14) -> 0.                           (4)

When J is zero or the saturated image just described, I is saturated: its ambient quotient is an extension of the locally free quotients on either side. Therefore

    0 -> F -> F^+ -> I(2) -> 0                           (5)

has no hidden divisor. If J=0, F^+ has rank ten and degree minus two, contradicting H0(F^+)=0 from F^+ subset E^+. Hence only the third kernel in (3) occurs, and its internal derivative is nonzero. We obtain

    K0=T O(-3)+Wp O(-7),
    J=Wp O(-7),
    rank F^+=12,    deg F^+=-12.

Since F^+ has no sections, every ordinary summand has degree at most -1. Rank and degree therefore force F^+=R O(-1). Equation (4), twisted by three, gives

    R = Sym17 W - Wp Sym2 W = Wp+S+T.

In particular

    F^+=(Wp+S+T) O(-1).                                 (6)

## 4. The rank-three quotient is exactly V O(2)

Set X=F^+/F. Equations (4)-(5) give

    0 -> Wp O(-5) -> X -> O(16) -> 0.                    (7)

This is the actual quotient, not its saturation up to torsion. It has rank three and degree six. Since it is a quotient of O(-1)^12, its ordinary degrees are at least -1. From 0->F->F^+->X->0,

    H0(X)=P+D,     chi(X(-1))=T.                         (8)

The short rank-three, degree-six, central-parity list can be checked directly. Three trivial-coefficient line blocks have even nonnegative degrees, hence degree patterns (0,0,6), (0,2,4), (2,2,2); none has H0=P+D. A two-dimensional irreducible block has degree -1,1,or3, with the complementary line of degree8,4,or0. A single three-dimensional block has coefficient A or V and degree2. The only types with the H0 character in (8) are

    V O(2),
    Wp O(1)+O(4),
    W O(-1)+O(8),
    Wp O(-1)+O(8).

Their chi(-1) characters are, respectively,

    T,    Wp+S,    Wp+T-W,    T.

Only the first and last survive (8). In the last case, the component O(8)->O(16) in (7) is zero, since Sym8 W=P+D contains no invariant. Then O(8) would inject into Wp O(-5), which is impossible by degrees. Thus

    X=V O(2).                                           (9)

The exact line quotient is therefore

    0 -> Wp O(-5) -> V O(2) -> O(16) -> 0.               (10)

## 5. The full constant span is a tensor-quartic subsystem

Let C0 be the constant span of F^+. Since F^+ is pure degree -1, its columns are vector-valued linear polynomials on an affine chart. Their values and first derivatives span their constant coefficient space at every affine point. Consequently

    (F^+)^+=C0 O.

Write C=(C0 O)/F^+, of rank s and degree12. This quotient is globally generated. Moreover H0(C*)=0: a constant functional killing F^+ would kill its full span C0. Thus all ordinary degrees of C are positive.

The derivative of F^+ kills F, and so factors through X=V O(2). Its saturated image is C(-2), by the constant-span assertion. Therefore 1<=s<=3.

If s=1, then C=O(12), but Hom_G(V O(2),O(10))=0 since Sym8 W=P+D.

If s=2, central parity and deg C=12 prohibit an irreducible two-dimensional coefficient block: its degree would be6, whose parity is incompatible with W or Wp. Thus C is a sum of two positive even-degree lines, with degree pattern (2,10), (4,8), or (6,6). A component V O(2)->O(c-2) requires V in Sym^(c-4)W. Among these degrees only c=10 works, because the first occurrence of V is in Sym6 W. Consequently such a map has rank at most one, contradicting s=2.

Hence s=3. The generically full-rank map

    V O(2) -> C(-2)

has equal source and target degrees six, so its determinant is a nonzero constant. It is an isomorphism, and C=V O(4).

Since H0(F^+)=H1(F^+)=0, the quotient identifies C0 with H0(V O(4))=V tensor Sym4 W. Thus the actual sequence

    0 -> F^+ -> C0 O -> V O(4) -> 0

is the complete evaluation sequence. Under a constant equivariant identification,

    F^+=V tensor U_3^4.

The backward kernel of this standard complete evaluation kernel is V tensor U_2^4. It contains F, since the derivative of F lies in F^+, and has the same rank and degree as F. Both are saturated; hence

    F=V tensor U_2^4.

This identifies the actual constant subsystem. It does not split the rest of E from it.

## 6. Exact forward intersection with the constant subsystem

Let G0=E intersect F^+. The original quotient of F^+ into E^+/E is the onto O(16) quotient in (7). Hence

    0 -> F -> G0 -> Wp O(-5) -> 0,
    F^+/G0=O(16).                                       (11)

The derivative of F^+ induces the isomorphism X=V O(2) -> C(-2)=V O(2) from Section5. Project it further to (H O/E^+)(-2). Since (E^+)^-=E, the kernel on F^+ is exactly G0. Therefore the kernel on C(-2) is G0/F=Wp O(-5). Equivalently, putting Nplus=E^+ intersect (C0 O),

    Nplus/F^+=Wp O(-3),
    (C0 O)/Nplus=O(18).                                (12)

The last quotient is locally free by the twist-by-two of (10). Thus Nplus is saturated inside C0 O. Equation (12) gives rank Nplus=14 and degree Nplus=-18. This is an exact identity of sheaves; it does not assert that Nplus has the full fiberwise intersection at every point. In particular the induced sheaf injection O(18)->(H O)/E^+ has not been proved saturated.

All differentiation is still in C0 O, an actual constant subspace. The derivative of Nplus has target O(16). Its restriction to F^+ is exactly the onto line quotient (10). Hence it is onto everywhere. Its kernel is E intersect (C0 O): indeed vanishing in (C0 O)/Nplus is equivalent to vanishing after inclusion in (H O)/E^+, whose kernel is E. Thus

    N=E intersect (C0 O)=(Nplus)^-,
    0 -> N -> Nplus -> O(16) -> 0,
    rank N=13,    deg N=-34.                            (13)

## 7. The exact internal Euler extension and residual type

From (11)-(13), projection to Nplus/F^+ induces an onto map N -> Wp O(-3). Surjectivity follows by subtracting a local section of F^+ with any prescribed derivative in O(16). Its kernel is G0. Modulo F, this gives the genuine exact sequence

    0 -> Wp O(-5) -> N/F -> Wp O(-3) -> 0.               (14)

The equivariant extension space is one-dimensional:

    Ext^1_G(Wp O(-3),Wp O(-5))
      = (End(Wp) tensor H1(O(-2)))^G = C.

The split extension is impossible. If split, its Wp O(-3) summand would map to E/F=T O(-3)+lower terms. The same-degree map vanishes because Wp and T are distinct irreducibles; all maps to lower degrees vanish as well. This contradicts the inclusion N/F subset E/F.

Thus (14) is the nonzero Euler extension, obtained by tensoring Wp with

    0 -> O(-5) -> W O(-4) -> O(-3) -> 0.

Consequently

    N/F=(Wp tensor W) O(-4)=P O(-4).                    (15)

The extension of (15) by F splits as equivariant bundles, since the ordinary H1 groups have positive twist and vanish. This proves N=(P+D) O(-2)+P O(-4), without claiming a horizontal splitting.

The inclusion P O(-4)->E/F has zero components in the lower summands. Its component into T O(-3) lies in a one-dimensional equivariant Hom space. It is nonzero, and under P=Wp tensor W and T=Wp tensor Sym2 W is the standard saturated inclusion

    Wp tensor (W O(-4)) -> Wp tensor (Sym2 W O(-3)).

The quotient is Wp O(-1), by the complete quadratic evaluation sequence. Therefore

    E/N = Wp O(-1)+O(-8)+O(-10),  or
    E/N = Wp O(-1)+W O(-9),

as claimed. The original projection E->(H/C0) O has kernel exactly N as a sheaf, so it induces an injective sheaf map from the locally free Z=E/N of degree -20. This identifies its actual image sheaf and its generic rank four. It does not prove a locally free cokernel: a torsion defect in the saturation remains possible.

## 8. Verification boundary and contribution

The only small support calculations are complete dimension/parity classifications of a rank-eight kernel and a rank-three quotient. They use universal G characters and exact cohomology, not actual coefficients or a search over source instances. The crucial maps are the actual original derivative, the kernel derivative, the complete evaluation sequence forced by linearity, and actual intersections inside the original constant bundle.

This gives a fifteen-dimensional constant tensor-quartic subsystem, exact sheaf intersections, and a rank-four degree-minus-twenty locally free image sheaf in a fifteen-dimensional constant quotient. The next missing dependency is saturation of that image, equivalently constancy of the full fiberwise intersection E_x with C0. The quotient O(18)->(H O)/E^+ also requires a separate saturation argument if used fiberwise. The residual still carries possible couplings and torsion defects; this theorem does not remove them or assert either remaining profile-(1,2) label impossible. It uses neither the withdrawn recursive symbolic-division method nor a new run of the previously exhausted all-twist section envelope. Source2 remains separate and open.
