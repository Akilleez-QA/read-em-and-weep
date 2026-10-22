# Five necessary first quotients for the extremal rank-two dual image

## Result and scope

Assume the hypothetical maximal rank-three Gauss plateau has (k,l)=(3,1),
and the dual cubic derivative psi:T6 O -> E*(1) has generic rank two.
Write K=E^- and A0=E/K. Then its actual image is saturated, and exactly
one of the following five necessary pairs remains:

    im psi = W' O(2),  A0 = O(2) + W' O(-1);
    im psi = W' O(2),  A0 = O(4) + W' O(-1);
    im psi = W' O(2),  A0 = O(6) + W' O(-1);
    im psi = W' O(4),  A0 = O(4) + W' O(-3);
    im psi = W' O(4),  A0 = O(6) + W' O(-3).

This is a necessary overlist, not an existence assertion or a complete
exclusion of (3,1). The rank-one branch is not treated here. Frozen
lower bounds remain unchanged. Only universal representation and bundle
degree arguments are used; no actual coefficients, points, matrices,
rank experiments, or parameter scans are used.

## 1. Inputs and the saturated rank-two image

Use EXTREMAL-31-DUAL-CUBIC-IMAGE-HAS-RANK-AT-MOST-TWO.md and its frozen
inputs, especially the global H0(E(1))=0 and the 28 necessary primal
splittings. The global vanishing is not inferred from forward length one.
Use the five necessary Q* splittings in
EXCEPTIONAL-CUBIC-GAUSS-CORNER-EXCLUSION.md. Their duals Q have largest
ordinary degree at most eight.

Let J=im psi and Lbar its saturation in E*(1); set m=deg Lbar. The
individual-block test in the rank-at-most-two note applies also to
Lbar, although J->Lbar need not initially be surjective. Indeed the
composite T6 O->Lbar is generically surjective. Projection to each
irreducible equivariant splitting block R O(e) is nonzero; hence e>=0
and T6 occurs in R Sym^e W. Its inclusion into E*(1) supplies the same
target Hom test. Consequently the rank-two possibilities are

    W' O(2), W' O(4), W' O(6), W O(8), W O(10),
    O(9)+O(9), O(9)+O(11), O(11)+O(11).

For every one of the 28 target splittings, the sum of its two largest
ordinary degrees is at most 20. Taking determinants of a rank-two
subbundle gives m<=20, excluding the final pair. Also
Hom_G(T6,Sym^9 W) has dimension one: the two projections to O(9) are
scalar multiples of the same map. Thus O(9)+O(9) cannot be the generic
rank-two image. These are necessary tests only and do not presume
cooccurrence or generation of a candidate target.

## 2. The first quotient and its extension

Let I=im(beta_E(2):E(2)->Q). As a locally free sheaf it is canonically
A0(2). Transpose duality shows that the generic image of psi lies in
A0*(1), and therefore Lbar lies in this subbundle: the composite to
E*(1)/A0*(1) vanishes generically and hence everywhere. Because Lbar
is saturated in E*(1), it is saturated in A0*(1) too. Dualizing the
inclusion gives a surjection

    I=A0(2) -> Lbar*(3).

Its kernel is an equivariant line O(n), with n even since I is
center-even and the group has no nontrivial one-dimensional characters.
This line injects into Q, so n<=8. We have the exact sequence

    0 -> O(n-2) -> A0 -> Lbar*(1) -> 0.          (1)

This uses the actual derivative image, not its saturation in Q.
Since deg E=-54 and rank K=14,

    chi(K(3))=2-n+m.                            (2)

Let K2=E^{--} and F0=E^{---}. Persistence supplies H0(F0(3))=0.
The derivative K(3)->A0(1) has kernel K2(3), while
K2(3)->(K/K2)(1) has kernel F0(3). The actual derivative identifies
K/K2 with a subsheaf of A0(-2). Hence, in the representation order,

    H0(K(3)) <= H0(A0(1)) + H0(A0(-1)).         (3)

Here X<=Y means Y-X is a genuine representation. In particular
chi_G(K(3)) is bounded above by the right side of (3).

All ordinary degrees of Lbar are at least two. If n<=0, sequence (1)
gives h0(A0(1))+h0(A0(-1))<=h0(Lbar*(2))<=2. But (2) is at least
2+m>=6, a contradiction. Thus n is one of 2,4,6,8. Now

    Ext^1(Lbar*(1),O(n-2)) = H1(Lbar(n-3)) = 0,

because every ordinary degree in the last bundle is at least one.
Averaging a splitting gives an equivariant splitting. Thus

    A0=O(n-2)+Lbar*(1).                         (4)

No lifting of a map through a guessed splitting of E is used.

## 3. The equivariant inequality

Put U=W'+2T6=chi_G(E(3)). For Lbar=sum R O(e), (4) gives

    chi_G(K(3)) = U - Sym^(n+1) W
                     - sum R chi_G(O(4-e)).

The right side of (3) equals

    Sym^(n-1) W + H0(O(n-3)) + sum R H0(O(2-e)).

The terms H0(Lbar*) vanish. Testing whether the difference between
this bound and chi_G(K(3)) is genuine gives exactly:

    Lbar=W' O(2):       n=4,6,8;
    Lbar=W' O(4):       n=6,8;
    Lbar=W' O(6):       none;
    Lbar=W O(8):        none;
    Lbar=W O(10):       n=8;
    Lbar=O(9)+O(11):    n=8.

The accompanying verifier performs exact character arithmetic, not
only dimensions. This calculation deliberately allows incompatible
formal targets: as an overlist its exclusions remain valid without
an unproved target-cooccurrence assertion.

## 4. Excluding both degree-twenty cases without a lifting assumption

For either remaining case with n=8 and m=20, (4) is

    A0=O(6)+W O(-9),  or  A0=O(6)+O(-8)+O(-10).

The identities

    W Sym^4 W = S4+T6 = Sym^9 W,
    Sym^3 W+Sym^5 W = S4+T6,
    Sym^7 W+Sym^5 W = W'+2T6=U

show that chi_G(K(3))=U and the bound in (3) is exactly U.
Since H0(K(3))-H1(K(3))=U, inequality (3) forces

    H0(K(3))=U,  H1(K(3))=0.

Therefore every ordinary summand of K has degree at least -4.
The derivative K->A0(-2) cannot reach the rank-two low-degree part
of A0(-2), whose degrees are -11,-11 or -10,-12. It can reach only
the O(4) line, so its generic rank is at most one. This contradicts
rank three at the interior plateau stage K. Both cases are excluded.

This proof does not need to cancel target tails, prove generation by
quadratic sections, or lift a residual map. In particular it does not
assume injectivity of the primal quadratic-section map at l=1.

## 5. Actual image equals saturation in the five surviving cases

For the five cases left, m is four or eight. The actual image J is
rank two and satisfies the same individual-block overlist, so deg J>=4.
The saturation defect m-deg J is the degree of an invariant effective
divisor. It belongs to the semigroup generated by 12,20,30 and is
between zero and four. It is therefore zero, so J=Lbar. Substitution
in (4) gives precisely the five pairs stated at the start.

## Reproduction

Run python3 verify_extremal_31_rank_two_five_quotients.py. It checks the
rank-two overlist and target degree bound, the equivariant inequality
for every allowed even n, both degree-twenty Euler identities, and the
small saturation defect. Geometric assertions are proved above.
