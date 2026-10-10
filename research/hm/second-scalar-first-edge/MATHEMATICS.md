# Map conventions and the conditional source-to-edge interpretation

## 1. The new map

The four terms of K have ranks (5,15,10,2). In internal degree -2, X02 is a
5×10 block and X13 is a 15×2 block. Use zero-based indices and define

    L_minus(X) = X02[0,5] - X13[10,1].

In the full 32×32 matrix these are entries (0,25) and (15,31). The corresponding
80-slot functional has +1 at slot 5 and -1 at slot 71. Both entries have type
N^(-4). Set the map to zero on other internal degrees.

For W in internal degree -3, the relevant incoming differential blocks are
W epsilon and gamma W. The source-model identities required here are

    epsilon[:,5] = (0,v0)^t,
    gamma[10,:] = (v0,0,0,0,0).

They give (W epsilon)[0,5] = v0 W[0,1] = (gamma W)[10,1], so this map kills
incoming boundaries. The package contains the pinned reduced MODEL and checks
its actual epsilon column and gamma row at v0=1. All ten independent W[a,b]
coefficient identities are checked exactly over the rational polynomial ring.
The homogeneous notation uses the model's stated grading conventions; the
checker does not independently rederive the bundle types.

## 2. Geometric source assumptions, distinguished from replayed data

For a normalized unsigned tail M, let

    F = I_C M^t P_C,    Z = E_B F H1_B,    E_B = I_B P_B.

The local blocks are X02=-H0_A Z and X13=+E_A Z eta_A. For both first merged
anchors the needed whole-row identities are

    E_A[10,:] = 0,    H0_A[0,:] = e10^t/v0.

Consequently c_minus=-Z[10,5]/v0. Together with the contraction side conditions,
these identities identify the two first-anchor values and kill tuples using
both carriers. The merged cover is D(v0),D(h1),D(h2),D(h3),D(h4). This is scalar
descent, not extension of the entire splitting across D(v0).

For both anchors the public checker verifies the actual reduced-model I row
10 is zero, all 15 numerator entries of E=IP row 10 are zero, and H0 row 0 is
the denominator dh times e10. It verifies the 150 generic-Z coefficient
identities per anchor before denominator cancellation. These exact checks at
v0=1 reproduce the new row calculation. The contraction side conditions and
homogeneous frame conventions still belong to the external geometric proof.

The separately recorded map audit replaces the old column-0 calculation by
this new column-5 whole-row calculation. Its pole argument uses **all-entry**
tail/prefix bounds, frame identities and legal-line bounds before scalar
selection. A column-specific bound for another map would not suffice. The
all-mask comparison and boundary-residue theorem are further source assumptions
of the geometric interpretation below; this downstream replay does not prove
them from the finite model.

On v0=1 the intended fresh source is

    a = row10(I1 P1 I2),
    b_minus = column5(P2 H1_1),
    f_minus = -a Mbar^t b_minus,
    A_minus = f_minus h1^13 h2^14 h3^14 h4^14.

Mbar is the unchanged complete weighted unsigned tail on carriers (2,3,4),
retaining the 4,096 legal-line tuples through 256 integer feature moments.
There is exactly one explicit leading minus in f_minus. It is already in the
source coefficients; the permutation sign is a separate final sign.

The embedded two-component b_minus has denominator dp2 dh1 and four-/six-term
numerators. `right-prefactor.json` includes P2's numerator and H1's column 5.
`replay.py` ties those embedded matrices and both denominator factors directly
to the pinned reduced MODEL, exactly multiplies the polynomials and checks
both numerators. The left factor and weighted tail are not independently
regenerated here.

Let f_minus^hom denote the homogeneous **weighted** scalar whose v0=1
restriction is f_minus. The numerator used in the homogeneous regularity
argument is v0 f_minus^hom h1^13 h2^14 h3^14 h4^14. The all-mask weights are
essential for clearing the legal-line poles; the unweighted refined c_minus
cannot be substituted here. Regularity requires the stated all-entry pole and
legal-line comparison hypotheses, not just a homogeneous degree count. Once
regularity and the source identity hold, its degree
1+5(13+14+14+14)-4=272 gives deg_(x_i) A_minus <=272 for every coordinate.

## 3. Fresh support assumptions and the reversed source

Write A_i=[x_i^272]A_minus. The new independently recorded support gates give

    product_(j != i) x_j^47 divides A_i,
    deg_(x_j) A_i <=215,   total_degree A_i <=454.

These are enclosures, not claims that the extreme degrees occur. They were
checked separately for all four axes in the recorded source calculation; the
large sources and gate programs are not bundled here. The earlier attempted
factor-48 support test failed and was replaced by these fresh bounds. A failed
bound test is not a zero coefficient or residue result. No factor of
(e1 e2 e3)^47 is assumed.

For this orientation only, use (u,a,b)=(x1,x2,x3) and

    C = A_0/(uab)^47,
    R(v,w,z) = v^168 w^313 C(1/(vw),1/w,z/w).

Indeed 215-47=168 and 454-3×47=313. The supplied quotient is the complete
retained image of this claimed R in Q[v,w,z]/(v^9,w^44,z^23), with common
denominator 64. Its sparse list contains all 203 nonzero retained terms;
missing slots inside the window are zero as part of the supplied data.
The public arithmetic checks cannot prove that R is the true geometric source.
In particular, correct early truncation requires separately certified
nonnegative nodewise shifts and integer clearing. Hashes of those sources and
certificates are provenance, not replacements for this obligation.

## 4. Selector derivation

Let m∈{0,1,2}^4, S=sum(m), and e=(i,j,k,l) be a permutation with m_i=2.
Under the characteristic-independent boundary-residue comparison, the
contributing component of A_i has total degree 419-S, with denominator
q^70, where q=e1(u,a,b)e2(u,a,b)e3(u,a,b). Thus the contributing C_i-degree is
278-S. For the revised bounds, set

    d=6+m_j,    L=22-m_l,
    G(T,z)=1+z+(1+3z+z^2)T+z(1+z)T^2,
    K_t(z)=[T^t]G(T,z)^(-70) modulo z^23.

The edge functional is

    sign(e) sum_(r=0)^d sum_(ell=0)^L
      [x_i^272 x_j^(215-r) x_k^(157-S+r-ell) x_l^(47+ell)] A_minus
      × [z^(L-ell)] K_(d-r)(z).

The selected physical exponents total 691-S. Reversal sends the coefficient
to slot (r,35+S,ell), because 313-(278-S)=35+S. Homogeneous degree stays
separate until this selection; setting w=1 first is invalid.

One way to derive the integer kernel is to expand

    q = ab[(a+b)u^3 + ((a+b)^2+ab)u^2 + (a+b)ab u].

For a prime-power P>=71 in characteristic p>5, multiplying by q^(P-70)
gives u-deficit 6+m_j and low b-degree 22-m_l after the coordinate factor is
removed. The displayed homogeneous expansion gives G^(P-70). Frobenius makes
G^P=1 modulo (T^9,z^23), so that finite kernel equals G^(-70). Together with
the characteristic-independent residue theorem and integral linearity, the
agreement at infinitely many primes gives the stated rational functional.
This is a formal identity under the source hypotheses, not an inference from
a modular value of the geometric obstruction. The public replay itself uses
only exact rational/integer arithmetic, never modular substitutions.

For m=(2,2,2,0), e=(0,1,2,3), one obtains S=6, d=8, L=22, w=41 and sign(e)=+1.
Therefore the 207 selected slots are (r,41,ell), with physical exponent

    (272,215-r,151+r-ell,47+ell),

and weight K_(8-r)[22-ell]. The checker derives all these rows. Their 24
nonzero coefficients have exact weighted sum 8655/16.

## 5. Exact claim and remaining unknowns

Without any source-attribution assumption, the finite arithmetic claim is:
**the supplied quotient, under the displayed selector, yields 8655/16.**
The accompanying model chain-map/merged-row checks and prefactor contractions
are exact polynomial identities in the reduced model.

Interpreting the quotient as an actual geometric edge additionally uses the
source/model, comparison, fresh-support, safe-reversal, clearing and terminal
evaluation chain described above. Those records were checked in the original
calculation, but are not end-to-end reproducible from this small package.

For m2220 the first role can be 0,1 or 2, and each permits 3!=6 orders of the
remaining roles: 18 contributions in all. Only 0123 is evaluated here. The
other 17 have no assigned value in the data or code. Thus 8655/16 cannot be
reported as the scalar pairing, a scalar-class result, or obstruction
nonvanishing. No previously computed scalar map's zero list or relation
certificate applies to this separate map without a new proof.
