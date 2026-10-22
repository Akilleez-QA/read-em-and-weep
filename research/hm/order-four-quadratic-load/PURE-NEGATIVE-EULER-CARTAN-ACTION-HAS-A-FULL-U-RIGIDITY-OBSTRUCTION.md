# Pure negative Euler Cartan action has a full U rigidity obstruction

## Dependencies and fixed conventions

Use `CLEAN-SOURCE-BALANCE-TENSOR-FOUNDATION.md` and its companion
`universal_source_balance_helpers.py`, published in PR697 at
715bb7c683988da6cf220f26629b92d3575a0287. The verifier imports only that
module, whose sole repository dependency is the public Clifford verifier
pinned there. The comparison with the existing nonzero source deficit is
`THREE-TERM-MIDDLE-OPERATOR-CANCELS-FULL-U-BUT-RETAINS-A-SOURCE-DEFICIT.md`,
published in PR701 at 4971537812d3dc0b9b8d32dbfeafa3ec6107a19b.
No curve-reduction result is a premise of the rigidity proof.

## New result and scope

A standalone negative-quartic Euler correction cannot change the balanced
source deficit while keeping the full U column canceled. This is a literal
full-tensor obstruction, not a count of representations and not a quotient
on the positive conic.

More precisely, let K(w) be an arbitrary six-space endomorphism with
homogeneous negative coefficient degree four. Allow the full U-to-U source
P(w) of degree four and a reverse U-to-A source R(v,w) with positive/negative
degrees (1,3). Assume the actual cubic marking
f:Sym^3 W -> Cartan is an isomorphism, as supplied by its nonzero
channel scales. For the actual nonzero monad scales, suppose

    T4(K)(a_m A+b_m B)
        =(a_m A+b_m B)P+c_m C R.                         (1)

Then K=P=R=0. No Cartan-annihilation or equivariance assumption on K is
needed. In particular the result applies to every equivariant specialization
linear in the positive H parameter and quadratic in the negative Hamiltonian
parameter. The physical coordinate degree remains four throughout.

This does not exclude a correction that simultaneously changes another
middle sector, a source block in a different homogeneous sector with a
corresponding middle companion, or the prescribed divided cochain. It says
that no additional pure negative Euler symbol, including a Cartan-action
symbol, can be added alone to the existing fully U-balanced construction.

## 1. Complete low U identity

Use the frozen coefficient markings

    cliff spin=I,  Pi=I-spin cliff,  up=G tensor I,
    adj6(K)=J6^(-1) K^t J6,  low=up^(-1).

For a positive one-form with six coefficient vector up spin z,

    B(z)=3 i_x[(up spin z) wedge omega_W].

For every negative quartic K, including all Cartan-to-Spin blocks,

    T4(K)B(p)=-3 i_x[(up adj6(K) spin p) wedge omega_W].    (2)

This follows directly by negative Euler summation. There is no discarded
VV, mixed or WW term. The map L -> i_x(L wedge omega_W) is injective on
positive one-forms: its mixed terms contain -L wedge j, where
j=-w du+u dw, and the polynomial ring has no zero divisors.

The low homogeneous terms of (1) therefore give exactly

    adj6(K) spin=-spin P.                                 (3)

In particular, if a pure negative Euler lift has Cartan image, its whole
B column vanishes, not just its principal coefficient.

## 2. Exact high U balance for image-in-ell coefficients

Keep the actual cubic marking f:Sym^3 W -> Cartan, without rescaling it.
Let ell=uT-wS. Every coefficient with image in f(ell Sym^2 W) has the form

    K_ell=f ell H,

where H:V6 -> Sym^2 W has negative coefficient degree three. This includes
both Cartan-input and Spin-input coefficients. For the whole U input p put

    Y(v,w;p)=H A(v,p),
    delta=S partial_u+T partial_w.

The fixed c-column convention is C(y)_VV=-f(ell y). Its forced reverse
source is R=-(a_m/c_m)Y. The entire U residual is

    T4(K_ell)(a_m A+b_m B)-c_m C(R)
        =(a_m/4) i_v[f(delta Y) wedge j].                  (4)

There is no WW term, and (4) includes every mixed component. Its proof is
the exact binary identity

    ell grad_w Y+3 i_C(Y)=j delta Y,
    i_C(Y)=-T Y tensor du+S Y tensor dw.                  (5)

Thus this extension to Cartan action does not provide a free invisible
principal correction. Its full mixed companion is fixed.

## 3. Why full U cancellation forces zero

First, a Cartan-valued positive-linear VV tensor F satisfying i_v F=0 is
zero. Indeed the positive Koszul identity writes

    F=(1/3) i_v d_v F=A(s)

for a spinor s independent of v. Cartan projection then gives M(v)s=0
identically. The coefficient of z is the invertible fixed Clifford tensor
M2, so s=0. This is coefficient extraction, not evaluation at an actual
point. The verifier also supplies an explicit linear left inverse to
contraction on this entire Cartan sector.

Applying this fact to (4) forces delta Y=0. But delta on binary/coefficient
bidegree (2,3) is invertible, with regular inverse

    I2(L)=E L-E^2 delta L/4+E^3 delta^2 L/36,
    E=u partial_S+w partial_T.

Consequently Y=0. Since the coefficient tensors A(v,p)=v tensor p span
V6, H=0. Thus no nonzero image-in-ell coefficient can be exactly balanced
on U by its reverse C source.

For general K in (1), the high VV equation says

    (K-I_V tensor P)A(v,p)=-(c_m/a_m)f(ell R(v,w;p)).        (6)

Since R is linear in v and p, it is a linear map on V tensor Spin.
Therefore (6) places K-I_V tensor P in the image-in-ell family just
considered. The full identity

    T4(I_V tensor P)A=A(P)

holds even when P has arbitrary negative quartic coefficients, because
A(P) has zero positive contraction. Subtracting this identity from the
high part of (1), (4) forces K=I_V tensor P and R=0.

Finally (3) becomes

    P^dagger M_i+M_i P=0,    i=0,1,2.                    (7)

This has zero kernel without any rank computation. Write
P=((a,b),(c,d)), and let D_i denote the left side of (7). Then

    P=((D_1[1,0]/2,-D_1[0,0]),
       (D_0[0,0],D_0[0,1]/2)).                           (8)

All four entries are recovered from the defects. Thus P=0 and K=0.
This proves (1).

## 4. Full c companion for the natural Cartan-action family

The same family K=f ell H has an additional lower Cartan companion; the
old B-only source-balance formula does not extend unchanged.

For an arbitrary full quadratic c input z, define

    y_C=H f(ell z),
    D_C=T4(K)C(z)-C(y_C).

Its VV component is exactly zero. Write V3,V4 for its full mixed
positive-one-form coefficient vectors. Define

    L=(partial_u V4-partial_w V3)/5,
    P_C=-(cliff low L)/3,
    L_C=up Pi low L.                                      (9)

These are regular polynomial formulas. Their degrees are

    y_C: (0,4),   L,P_C,L_C: (1,3).

Closure and negative Koszul division give the exact full identity

    T4(K)C(z)=C(y_C)+B(P_C)-i_x(L_C wedge omega_W).         (10)

The denominator five in (9) is the negative degree three of L plus two.
There is no division by u,w, ell, q0, an actual source coefficient, or a
ramification function. In particular (10) retains its WW component.

For direct use without first expanding T4, let p_C=C(z)_VV, and let C3,C4
be the original mixed coefficients. Put

    F_i=-up adj6(K) low C_i,    S_w=u F3+w F4.

The complete un-subtracted mixed and WW coefficients are

    (T4(K)C)_i=[i_v(K_i p_C)+5 F_i-partial_i S_w]/4,
    (T4(K)C)_WW
      =i_v up[adj6(K_u)low C4-adj6(K_w)low C3]/4.          (11)

Subtract C(y_C) from the mixed part of (11) before applying (9).
All derivatives in (11) are coefficient derivatives in the negative
variables. The determinant adjoints and physical source markings remain
fixed.

With source convention dT=T alpha-alpha S, the c-source choices

    S_AA=y_C,      S_UA=(c_m/b_m)P_C

cancel the C and B terms in (10), but leave the literal c residual

    -c_m i_x(L_C wedge omega_W)
        -(a_m c_m/b_m)A(P_C).                             (12)

The Cartan one-form L_C cannot be canceled by a B-source, since their
positive one-form coefficient spaces are complementary. Another retained
middle contribution would be needed if it is nonzero. Equation (12) is
only this correction's c contribution, not the whole current c error.

## 5. Consequence for the balanced source deficit

The current full-U member has a nonzero conic scalar multiple F t and its
unique source correction u=M(v)z. The theorem proves that a standalone
negative quartic Euler correction, even allowing its complete Cartan
input block and both U source blocks, cannot produce a new fully
U-annihilating member that alters t. Left factors such as the negative
binary N=-2 ell(u partial_S+w partial_T) are included whenever their
physical coefficient degree is four.

This closes that bounded route. A successful next attempt must coordinate
its Cartan-action Euler coefficient with a change in another middle
sector rather than simply append it to the fixed fully U-balanced middle.
No claim is made that the existing four-parameter fixed-D family or the
enlarged W-action symbols are exhausted.

Run python verify_negative_cartan_euler_rigidity.py. It checks the complete
universal exterior identities, both explicit injectivity arguments and
all source scales. The all-free symbols are tensor-factorized only to
keep expansion efficient; linearity makes them span every coefficient in
the stated 180- and 72-dimensional symbol spaces. It performs no selected
actual-source evaluation, actual-instance matrix/rank calculation, scan,
or curve normal-form reduction. Frozen files remain unchanged. No fourth
value or complete higher division is asserted.
