# Exact alternating normalization of the nine-endpoint mixed transfer

## Result and immutable inputs

Use the invariant bilinear adjoints and Hamiltonian normalization of
PR1031, commit 7150cf97eeebe473bcd7c61c1f968c73625d92ef,
research/hm/source2-pure-v-lift-rank/PROOF.md. For formal quadratics a,b,
put [a,b]=a_x b_y-a_y b_x. The exact universal identity is

    rho_D(a)L_b* - rho_D(b)L_a* = -2 L_[a,b]*.             (1)

The coefficient is unchanged by the pinned quotient pairing on P.
In particular it is not an unspecified nonzero scalar.

PR1069, commit 41bc20cade3198306c492c0c46399d71eb0d51c4,
research/hm/source2-pure-v-canonical-transfer/PROOF.md, proves that the
actual full bilinear transfer in the conditional pure-V endpoint-nine
branch has the form B(a,b)=gamma rho_D(a)L_b*, with diagonal
R(a)=gamma R1(a). This factorization and the R1-line constraint are OLD
inputs here. The new normalization yields

    B(a,b)-B(b,a) = -2 gamma L_[a,b]*,
    Alt(B)(a,b)   = -gamma L_[a,b]*,                     (2)

where Alt includes the factor 1/2. Thus the alternating coefficient is
fixed by the SAME scalar as the diagonal, not an independent coefficient.
Moreover, in this branch only,

    R identically zero iff gamma=0 iff B identically zero
                         iff Alt(B) identically zero.   (3)

No actual scalar is selected, and gamma may be zero. These statements do
not imply commutation of the full fixed pencil, nor exclude any source.
For endpoint sixteen the diagonal need not determine the alternating
channel; the factorization used in (2) is not asserted there.

## 1. Adjoint normalization

Write the UNNORMALIZED binary transvectants as

    (f,g)_k = sum_{i=0}^k (-1)^i binom(k,i)
              (partial_x^{k-i} partial_y^i f)
              (partial_x^i partial_y^{k-i} g).

In particular rho_n(a)f=(a,f)_1. In monomial coordinates let G_n have
anti-diagonal entries (-1)^i/binom(n,i), as in PR1031. Full multiplication
M_b:Sym4 W -> Sym6 W has bilinear adjoint

    M_b* = G_4^{-1} M_b^T G_6,
    M_b* f = (b,f)_2 / 60.                              (4)

This follows coefficientwise from the displayed Gram matrices; the
checker verifies the whole 5-by-7 polynomial matrix with all three
coefficients of b free. The factor 60 is 2! times 6 times 5.

Use the pinned projection Pi and orthogonal inclusion

    E=G_6^{-1} Pi^T (Pi G_6^{-1} Pi^T)^{-1},
    G_P=E^T G_6 E.

These satisfy Pi E=Id and G_6 E=Pi^T G_P. Consequently

    L_b*=G_4^{-1}(Pi M_b)^T G_P=M_b* E
         =(b,E(·))_2/60.                               (5)

Thus one must apply the transvectant to the included sextic E(p), not
to arbitrary quotient coordinates as if they were monomial coefficients.
The checker verifies (5) using the exact pinned Pi over Q(sqrt5).
No Hermitian conjugation is used.

## 2. Alternating identity on all sextics

For independent formal quadratics a,b and any formal sextic f, expansion
of the derivative definitions gives

    (a,(b,f)_2)_1 - (b,(a,f)_2)_1
                       = -2 ((a,b)_1,f)_2.             (6)

This holds on the ENTIRE Sym6 W, not only its P summand. To make the
calculation reproducible, write a=p x^2+q xy+t y^2 and
b=u x^2+v xy+w y^2. Then

    [a,b]=(2pv-2qu)x^2+4(pw-tu)xy+(2qw-2tv)y^2.

The checker expands (6) with seven independent sextic coefficients and
verifies that every coefficient vanishes. Dividing by 60 and restricting
f=E(z) proves (1). Both sides receive the same adjoint factor, which is
why no extra quotient-pairing factor appears in (1). Rescaling the two
invariant forms scales every L* coherently and leaves the coefficient -2
unchanged, when rho and bracket retain their displayed conventions.

## 3. Recovering the full transfer and the zero implication

Combining (1) with the old endpoint-nine factorization proves (2).
Polarization of the diagonal also gives the explicit recovery formula

    B(a,b) = [R(a+b)-R(a)-R(b)]/2 - gamma L_[a,b]*.      (7)

PR1031 proves R1 nonzero. The universal alternating family L_[a,b]* is
also nonzero: the bracket Lambda2 Sym2 W -> Sym2 W is onto, and L* is a
nonzero channel. Both nonvanishings are checked as polynomial identities,
without substituting any direction. Hence (3) follows over C. Here
'identically zero' means the whole polynomial family, not vanishing at a
particular direction. A specialized diagonal zero does not imply B zero.

The ambient bilinear channel space still has two symmetric channels and
one alternating channel, as PR1069 states. Equation (3) is a consequence
of the actual small-branch factorization, not of polarization alone.

## 4. Verification and novelty boundary

INPUTS.json records two freshly read immutable proofs and their Git blob
and SHA256 digests. Run python verify.py and python -O verify.py; the
outputs agree. The checker uses only universal representation data and
independent formal polynomial coefficients. It does not execute any
historical source-evaluation program.

The existing canonical-transfer proof and the local source2 pure-V
proof packets were searched for this exact mixed alternating identity;
the former contains the factorization but not its normalized alternating
coefficient. We do not count that factorization or the R1-line deduction
as new. The additional deliverable is the exact -2 normalization, its
whole-sextic certificate, and the conditional equivalence (3).

No actual HM coefficient, selected parameter, direction, point, jet,
source matrix or instance rank is evaluated. Neither actual nonvanishing
nor realization of endpoint nine is proved.
