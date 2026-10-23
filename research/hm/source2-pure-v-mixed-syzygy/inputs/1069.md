# Canonical mixed transfer forces the nine-endpoint lift onto one line

## Result

Retain the conditional actual source2 pure-V compatible radical and its
unique homotopy h:N4→N2. Set Z=im Q⊂N4, I2=im j2⊂N2, I4=im j4⊂N4,
and let P_h be the unique P summand of im h. Define

    s:I4→P_h,        Qs=Id_I4.

For any G-equivariant right inverse G_Q:Z→N2 of Q, the family

    Π_a=h T_a G_Q : Z→im h                             (1)

is INDEPENDENT of the choice of G_Q. It kills I4 and satisfies

    Q Π_a=L_a h|Z,          L_a=T_a|I2.                 (2)

The actual full bilinear family

    B(a,b)=Π_a T_b s : I4→I2                            (3)

is well-defined for all a,b∈A=Sym2 W, and satisfies the literal identity

    Π_a T_b h=B(a,b) j4 : N4→I2.                       (4)

Its diagonal is exactly the unique quadratic lift R_a of PR1025, in that
proof's source/target conventions, with PLUS sign:

    R_a=B(a,a)=h T_a G_Q T_a s.                        (5)

The symmetric channel space in (3) has dimension two; the alternating
channel space has dimension one. No mixed commutation or alternating
vanishing is assumed.

NEW COEFFICIENT CONSTRAINT. If the generated endpoint has dimension nine,
then in the fixed universal basis of PR1031,

    R=gamma R1,       R1(a)=rho_D(a)L_a*,               (6)

for an unselected scalar gamma, which may be zero. Thus its second lift
coefficient is zero. If R≠0 in this branch, its projective line is the
conic line ellDelta=[1:0] identified in PR1036. Conversely a nonzero R2
coefficient would force endpoint dimension sixteen, but no such actual
coefficient is asserted. Nothing proves that either branch occurs, that
gamma is nonzero, or that original rank36 is impossible.

## 1. Immutable inputs and actual objects

INPUTS.json authenticates seven exact proofs: PR1019, PR1022, PR1025,
PR1048, PR1059, PR1031 and PR1036, at their stated public immutable
commits. Their actual-source and geometric hypotheses remain in force.
They supply, respectively, the canonical homotopy and secondary channel;
raw quotient-second vanishing; the unique quadratic lift and its
normalizations; the sandwich identity; the9/16 endpoint dichotomy and
actual small-branch descendants; the universal basis R1,R2; and the
conic-line identification. No historical executable is run.

We use their literal endpoint identities

    hQ=j2, Qh=j4, ker j4=Z,
    h(Z)=I2, im h=I2⊕P_h, im h∩ker Q=I2,
    hT_a h=0, hT_a I2=0, T_a I2⊂I4,
    T_a im h⊂ker h⊂Z.                                 (7)

Also ker Q=A+I2 and Z has character2V+3P+3D, hence no A. The map
Q:P_h→I4 is an isomorphism. All these are actual subspaces; repeated
P or D labels elsewhere do not identify embeddings. The parameters a,b
range over the fixed negative quadratic space only.

The canonical transfer below is not a choice of a graded homotopy inverse.
Q is not presumed to preserve NC or NR. The result uses only Q:N2→N4
and actual negative multiplication; it does not duplicate the positive
mixed-channel or weighted-presentation arguments.

## 2. Choice independence and the mixed identity

Equivariant splittings exist over C for the finite group. If G_Q' is
another equivariant right inverse, its difference δ:Z→N2 has image in
ker Q=A+I2. Since Z has no A constituent, equivariance puts im δ⊂I2.
Equation (7) then gives hT_aδ=0. This proves independence in (1).
Non-equivariant right inverses are not covered by this argument.

The restriction G_Q|I4 equals s: their difference is an equivariant map
P→ker Q=A+D, whose Hom space is zero. Hence Π_a I4=hT_as=0 by the
sandwich identity, since s takes values in im h. Thus Π factors through
Z/I4, a29-dimensional representation, without choosing a complement.

Intertwining of the actual radical with each negative quadratic gives

    QΠ_a=QhT_aG_Q=j4T_aG_Q
         =T_a j2G_Q=T_a hQG_Q=T_a h|Z=L_a h|Z.

This proves (2). For y∈Z∩ker h, Π_a y lies in ker Q∩im h=I2.
In particular T_b s takes values there by (7), proving the target in (3).

For any y∈N4, the difference h y−s j4 y belongs to I2: it belongs to
im h and is killed by Q because Qh=j4 and Qs=Id_I4. Multiplying by T_b
puts that difference into I4, which Π_a kills. Consequently

    Π_aT_bh y=Π_aT_b s j4 y=B(a,b)j4 y.

This proves (4) in the actual degree-two target, not merely on cohomology.
It does not exchange a and b.

## 3. Diagonal sign and exact quotient corrections

Use PR1025's source identification H0(N/I)_P≅I4 by the inverse connecting
map σ. The class of s in the quotient realizes σ, because Qs=Id_I4.
Thus s is a legitimate representative for its x0.

For a fixed formal quadratic a choose the actual polynomial correction

    x1=−G_Q T_a s.                                    (8)

This is defined because T_a s⊂Z. It satisfies Qx1=−T_as exactly in N4,
not just modulo I4. In the quotient N/I it is therefore a valid first
correction. PR1022 proves that the quotient second symbol on its whole P
summand vanishes in the RAW H1(N/I), not only after dividing by B(A).
It follows that T_ax1 belongs to Z+I4=Z. We may therefore set

    x2=−G_Q T_ax1,     Qx2=−T_ax1.                     (9)

These are equivariant polynomial operators of degrees one and two in a.
They give the corrections of PR1025, and its representative-level rule
for the quadratic lift is R_a=f0 x2=j2 x2. With hQ=j2, (8)-(9) give

    R_a=j2x2=hQx2=−hT_ax1=+hT_aG_QT_as.

Here f0 is the descended radical on N2/I2; j2 kills I2, so this formula
is well-defined on quotient representatives. PR1025's uniqueness among
equivariant quadratic lifts identifies this representative with its R,
not just with another lift modulo im m or the syzygy line. This verifies
both the source identification and the sign in (5).

## 4. Full bilinear channels, without forced commutation

The family (3) is an equivariant bilinear map A×A with values in
Hom(P,D). In characteristic zero it splits canonically into symmetric
and alternating parts. The fixed character identities give

    Sym2 A=1+D,          Lambda2 A=A,
    dim Hom_G(Sym2 A⊗P,D)=2,
    dim Hom_G(Lambda2 A⊗P,D)=1.                        (10)

Thus its diagonal determines exactly its symmetric part by polarization,
but need not determine its alternating part. There is at most one
additional alternating scalar in this ambient family. This is not a
claim that it can vary independently in an actual source, or is nonzero.
Neither (7) nor choice independence licenses Π_aT_bs=Π_bT_as.

## 5. The small generated endpoint forces R2's coefficient to vanish

Assume dim F4=9. PR1059 proves the ACTUAL equalities

    P_h⊂NC2, F4=NC4=I4+D_C, h(NC4)=0,                 (11)

where D_C denotes NC4/I4 (the unique D constituent can equally represent
this quotient). It also proves that the map of quadratic descendants

    (b,p)↦[T_b s(p)] : A⊗I4→NC4/I4=D_C              (12)

is nonzero, with its D restriction an isomorphism. This nonvanishing
comes from actual A-channel transport in PR1059, not characters alone.

By (2), (11), and Π_a I4=0, restricting Π yields an equivariant linear
family

    A⊗D_C→I2.                                        (13)

There is only one such channel: dim Hom_G(A⊗D,D)=1. After any nonzero
equivariant identifications of D_C and I2 with Sym4 W, it is a scalar
multiple λ rho_D(a), where rho_D(a)f=a_x f_y−a_y f_x. This scalar λ is
not computed and may vanish.

Similarly dim Hom_G(A⊗P,D)=1. The map (12) is therefore ν L_b* for a
NONZERO scalar ν, after using the I4=P and I2=D conventions of PR1031
and identifying D_C with D. Here L_b* is the complex bilinear invariant
adjoint, not a Hermitian adjoint. Nondegeneracy of the invariant forms
and nonzero L show that this channel is nonzero. No actual scalar is
matched to a selected numerical value.

Composing (12) and (13) in the literal identity (3) gives the stronger
full bilinear constraint

    B(a,b)=λν rho_D(a)L_b*.                            (14)

Changing the identification of D_C rescales λ and ν inversely, so their
product is well-defined in the fixed source/target convention. Setting
b=a and applying (5) proves (6), with gamma=λν. PR1031 proves that
R1 and R2 are independent; hence the second coefficient really vanishes.
PR1036 identifies the nonzero R1 line as ellDelta. This is a necessary
coefficient relation for the nine-endpoint branch, not a selection of
that branch or of a nonzero lift.

In particular the P graph component of the quadratic relations in
PR1059 does not enter (14), because Π annihilates I4 exactly; its value
is irrelevant to this argument. For endpoint sixteen,
NC4 need not contain F4, so the factorization through the single D_C
used here is unavailable. No comparable coefficient restriction on that
branch is asserted.

## 6. Reproducibility and limits

Run python verify.py and python -O verify.py. The checker authenticates
seven inputs, checks all displayed map-composition types, the exact
finite-group character multiplicities, correction signs, and universal
bilinear/diagonal normalization with all quadratic coefficients formal.
The universal representation matrices used for the last check are not
actual HM matrices. Actual-map identities and the raw quotient-second
premise are justified by the written proofs and independent review.

No actual coefficients, directions, points, jets or instance ranks are
evaluated. No full fixed-pencil commutation, Q-preservation of NC or NR,
or graded extension of h is assumed. The new restriction is conditional
R2-coefficient zero in endpoint nine; its remaining scalar and the
sixteen-dimensional branch remain unselected.
