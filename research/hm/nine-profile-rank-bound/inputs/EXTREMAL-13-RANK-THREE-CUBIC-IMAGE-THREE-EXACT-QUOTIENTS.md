# Three exact quotients for the (1,3) rank-three cubic image

## New deduction and scope

Suppose the actual inclusion E in H O has maximal rank-three Gauss
profile (k,l)=(1,3). Let U=W'+2T6 and let J be the actual image of
its canonical cubic evaluation under the derivative,

    U O -> E(3) -> Q(1).

If J has rank three, then J is saturated in Q(1), and equals the full
actual derivative image I=(E/E^-)(3). Exactly three necessary possibilities
remain:

    I = W' O + O(17),       E/E^- = W' O(-3) + O(14);
    I = W' O + O(19),       E/E^- = W' O(-3) + O(16);
    I = W' O(2) + O(7),     E/E^- = W' O(-1) + O(4).

In the last case E^-=(2V+2P4) O(-4). In the second case the formal
splitting of Q* must contain O(-18).

This is a new conditional reduction, not an exclusion of (1,3) or of
rank-three SF. The cubic image ranks one and two are not settled here.
No actual coefficients, points, instance matrices, or experiments are
used. All old files are unchanged. Splittings below are bundle splittings,
never horizontal splittings.

## 1. The correct dual persistence envelope

Use ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md and
ADJACENT-RANK-THREE-GAUSS-EXCLUSION-AND-CONSTRAINTS.md for the actual
presentations, character notation, and invariant divisor semigroup
<12,20,30>. Forward length three forces

    E=U O(-3)+V O(-4),       H0(E^-(3))=0.

Consequently U injects into H0(J). J is globally generated. Assume
rank J=3, and let Sbar be its saturation in Q(1). Write D=deg Sbar.
The reversed dual plateau is

    L0 subset L1 subset L2 subset L3=Q* subset L4,
    ranks 4,7,10,13,16.

Set Kd=L2, Kd2=L1, A0=Q*/Kd. Negative-transpose duality identifies
Sbar=A0*(1). This is an equality of saturated subbundles: both have
the same generic subspace, the annihilator of Kd in Q(1). It is NOT
yet an equality with either actual image J or I.

Thus deg Kd=D-57 and chi(Kd(3))=D-17. The two derivative maps are

    Kd(3) -> A0(1),          kernel Kd2(3),
    Kd2(3) -> (Kd/Kd2)(1),  kernel L0(3).

The actual image gives Kd/Kd2 subset A0(-2), while persistence gives
H0(L0(3))=0. Hence, in representation order,

    H0(Kd(3)) <= H0(Sbar*(2)) + H0(Sbar*).             (1)

In particular the right side minus chi_G(Kd(3)) is genuine. Using
the actual identity chi_G(Q*(3))=T6-2W-S4, this reads

    T6-2W-S4-chi_G(Sbar*(4))
                <= H0(Sbar*(2))+H0(Sbar*).            (2)

The rank-ten kernel is essential: its numerical Euler characteristic
is D-17, not the D-1 appearing in the opposite (3,1) problem.
Only the two interior dual derivatives are used; no rank-three claim
is made after either endpoint of the plateau.

## 2. Exhaustive finite character reduction

The composite U O -> Sbar is generically surjective, so every ordinary
summand of Sbar has nonnegative degree. Further, projection to each
irreducible equivariant summand R O(e) is nonzero. Necessarily

    dim R<=3, e>=0, center(R)=(-1)^(e+1),
    Hom_G(U,R Sym^e W) != 0.

Since J is globally generated of rank three and contains U in its
sections, deg J=h0(J)-3>=11. Thus D>=11. The right side of (1) has
dimension at most 9+3=12, so D<=29. In particular every e<=29.

Enumerate all sums of the displayed eligible blocks of total rank three,
with 11<=D<=29. Require U<=H0(Sbar) and inequality (2). Exact abstract
character arithmetic leaves precisely

    W' O + O(15),  W' O + O(17),  W' O + O(19),
    W' O(2) + O(7).                                  (3)

The companion verifier enumerates all irreducibles, degrees, and block
sums, not a guessed list of maps. It uses no target splitting constraint
at this stage, so its list is a safe overlist.

## 3. Actual images coincide with saturation

From (3), D<=19. The determinant of J subset Sbar is an invariant
effective divisor of degree D-deg J. This degree is at most 19-11=8,
so the invariant divisor gap forces it to vanish. Therefore J=Sbar.
Since J subset I subset Sbar (all have the same generic rank-three
subspace), I=J=Sbar as sheaves. In particular the canonical cubic
sections generate the full derivative image; this has been proved,
not assumed by discarding the quartic part of E.

## 4. Remove the degree-fifteen line using actual target constraints

Every irreducible block R O(-j) of Q* satisfies central parity and the
positive character bounds

    R Sym^(j-1) W <= M3,
    R Sym^(j-2) W <= M2          (j>=2).

For j=1 the second contribution is zero. The actual presentations give
these bounds without any cohomology cancellation; j dim R<=54 makes
the list finite. Among j>=14 its only eligible individual blocks are

    O(-16), W O(-17), O(-18), O(-28).

A map O(15)->Q(1) could only reach the corresponding blocks of degrees
17,18,19,29. Their equivariant Hom spaces from O(15) all vanish:
there are no invariants of degrees 2,4,14, and W does not occur in
Sym^3 W. Therefore the first case of (3) is impossible.

Likewise the only eligible Q* block receiving the line O(19) in Q(1)
is O(-18). Thus that block is required in the degree-nineteen case.
No compatibility of other formal blocks is asserted.

## 5. A forced kernel in the degree-eleven case

For I=W' O(2)+O(7), E/E^-=I(-3) has degree two. Hence E^- has rank
14 and degree -56. Persistence H0(E^-(3))=0 forces every ordinary
summand of E^-(3) to have degree at most -1. Their sum is -14, so all
are O(-1), and E^-=R O(-4) for a fourteen-dimensional representation R.
The exact quotient, twisted by four, gives

    R=chi_G(E(4))-chi_G(I(1))
     =U W+V - W' Sym^3 W - Sym^8 W
     =2V+2P4.

This proves the final assertion without any assumption on the rank of
the endpoint derivative.

## Reproduction

Run python3 verify_extremal_13_cubic_image_reduction.py. It verifies
all finite character lists, the section envelope, saturation gap, target
Hom exclusions, and the forced kernel coefficient representation.
The derivative and saturation arguments are proved above.
