# Residual-large terminal multiplication forces the conic lift line

## Theorem

Retain the actual source2 nonzero pure-V compatible-radical hypotheses,
and assume specifically the residual-large mechanism: the actual N0
projection of P_h is zero and its actual projection into N8,2 is nonzero.
For the unique quadratic fourth lift in the fixed basis of PR1031,

    R=alpha R1+beta R2,
    R1(a)=rho_D(a)L_a*,    R2(a)=L_a*rho_P(a),

one necessarily has

    beta=0.                                               (1)

Thus R is zero or belongs to the conic line ellDelta=span(R1) of PR1036.
The scalar alpha is unselected and may be zero. Neither this mechanism
nor nonvanishing of R is asserted realized. No conclusion is transferred
to the other endpoint16 mechanism with nonzero N0 projection.

The proof uses actual residual cubic multiplication and the canonical
terminal factorization of PR1094. It does not invoke the earlier excluded
endpoint9, its conditional gate constraint, or a character-only terminal
quotient identification.

## 1. Exact inputs and actual interface

INPUTS.json authenticates nine public originals: PR795, PR1059, PR1068,
PR1072, PR1079, PR1094, PR1031, PR1036 and the universal model.py of
PR1031. Their exact commits and paths are in the manifest. In particular
PR1094 is at79b84d3b21cdbc76bb19d3a973e09981936dda32 and PR1072 at
d03beb727c7e778026dcceb3555c899a0808e093. The model supplies only the
fixed universal representation normalizations; no actual source is
encoded or evaluated, and the retained historical file is not executed.

The inherited exact residual system and fixed-variable spaces are

    0 -> NC -> NR --pi--> N8 -> 0,
    N8,2=A tensor Sym4 W,
    N8,3=A tensor Sym5 W,
    N8,4=(A tensor Sym6 W)/Delta_(2,6)(Sym8 W).          (2)

The constant inclusion in the last quotient is COMPLETE POLARIZATION,
not an abstract summand chosen by character. Negative multiplication
keeps the A coefficient factor fixed and multiplies the second factor.
The actual map pi2:P_h->N8,2 has image its unique P constituent, inside
the top Sym6 W constituent, and is an isomorphism onto that image.
PR1059 identifies that constituent through Delta_(2,4), with the same
fixed variables.

PR1072 identifies the genuine terminal residual block

    NR5=H1(E_R(1))=H1(T O(-2))=T,

including its actual next multiplication maps. PR1079 proves that in
this mechanism the generated F5 is exactly this actual NR5. PR1068
proves that both next negative coordinates kill NC4, and the actual
Koszul restriction delta:NC3->W tensor NC4 is an isomorphism.

Finally PR1094 gives a canonical map ell:im Q3->I3 and the SAME transfer
R as the unique fourth lift. With the coherent actual identifications
I2=i2(Sym4 W), I3=i3(Sym5 W), i_d(f)=f12 f, and
s:I4->P_h the inverse of Q2|P_h, it supplies an equivariant family
U_p in End(Sym4 W), p in I4=P, satisfying

    R(a)p=i2(U_p(a²)),
    ell(c s(p))=i3(x U_p(yc)-y U_p(xc))                (3)

for every formal cubic c. The plus convention for the transfer and the
minus in this Spencer expression are fixed in that proof. Its operator
D(U)(c)=xU(yc)-yU(xc) has kernel C Id; consequently it is injective on
the equivariant P-family space, since Hom_G(P,1)=0.

## 2. The terminal quotient is induced by the actual Koszul maps

The full actual Koszul continuation respects the genuine N0/NR separation
through degree five by PR1072. Its residual part is therefore exact:

    0 -> NR3 --delta--> W tensor NR4 -> NR5 -> 0.

Quotient the actual subcomplex NC3->W tensor NC4. That map is an
isomorphism by PR1068, and its next image is zero. The quotient sequence
is consequently exact with the inherited arrows:

    0 -> N8,3 -> W tensor N8,4 -> NR5 -> 0.             (4)

This uses the actual subspaces and naturality; no horizontal splitting
of NR into NC and N8 is made.

Before dividing by the constant polarization relations, binary Koszul
exactness gives

    0 -> A tensor Sym5 W -> W tensor A tensor Sym6 W
      -> A tensor Sym7 W -> 0.

Its injection is the same determinant formula
x tensor(yu)-y tensor(xu), and its last map multiplies the second
polynomial factor. Inserting (2) into(4) therefore gives the natural
quotient and its multiplication rule

    NR5 ≅ (A tensor Sym7 W)/(W Delta_(2,6)(Sym8 W)).    (5)

In particular the class of a cubic times an N8,2 representative computes
the actual residual cubic descendant under this identification. One may
alter all target identifications by a common nonzero scalar, but not
independently change the maps at the different degrees.

Define transvectants by

    (a,f)_k=sum_j (-1)^j binom(k,j)
       (partial_x^(k-j)partial_y^j a)
       (partial_x^j partial_y^(k-j) f).

The map C2:A tensor Sym7 W->Sym5 W, C2(a tensor g)=(a,g)_2,
kills the entire relation subspace in(5). The checker proves its rank
is6 and that W Delta_(2,6)(Sym8 W) has rank18. Thus that relation
subspace is its exact kernel; C2 identifies the ACTUAL quotient(5)
with Sym5 W, rather than merely matching the target character.

## 3. Exact residual cubic channel and Spencer inverse

Let Pi:Sym6 W->P and E:P->Sym6 W be the fixed projection and orthogonal
inclusion of PR1031, with Pi E=Id. For the binomial complete
polarization used in(2), write f_p=E p. Since the top constituent contains
P once, there is an unselected NONZERO scalar eta such that

    pi2 s(p)=eta Delta_(2,4)(f_p).                    (6)

This compares actual maps after their specified P identifications; it
does not identify arbitrary P copies by character alone. The map is
nonzero precisely because the residual projection is nonzero here.

The full polynomial identity for every cubic c and sextic f is

    C2(c Delta_(2,4)f)=(c,f)_2.                       (7)

The checker verifies all28 coefficient pairs. By(5)–(7), the actual
cubic map Sym3 W tensor P_h->NR5, in the C2 identification, is eta
 times (c,f_p)_2. Since NR5 and I3 are irreducible T, ell restricted
to the actual NR5 is a scalar tau times the coherent i3 identification.
Unlike eta, tau may be zero. Put lambda=eta tau. Equations(3) and(7)
then give the exact family equation

    D(U_p)(c)=lambda (c,f_p)_2.                       (8)

No value of eta, tau or lambda is assigned.

For every quartic q define

    U_p^0(q)=-(lambda/12)(q,f_p)_3.

The universal identity

    x(yc,f)_3-y(xc,f)_3=-12(c,f)_2                   (9)

shows that D(U_p^0) equals the right side of(8). The family is
equivariant. Hence U_p-U_p^0 takes values in C Id and is an equivariant
map P->1; it vanishes. Thus the actual family is exactly this Spencer
inverse, with no remaining scalar-identity correction in the P family.

## 4. The diagonal is the R1 channel

Use the fixed apolar normalizations from PR1031:

    Gn(i,n-i)=(-1)^i/binom(n,i),
    E=G6^(-1) Pi^t (Pi G6^(-1) Pi^t)^(-1),
    GP=E^t G6 E,   L_a(d)=Pi(ad),
    L_a*=G4^(-1) L_a^t GP,
    rho_D(a)g=(a,g)_1.

In those conventions exact formal identities give

    L_a*p=(a,f_p)_2/60,
    (a²,f_p)_3=6(a,(a,f_p)_2)_1=360 R1(a)p.          (10)

All quadratic coefficients of a and all four P basis coefficients are
retained; no negative direction is selected. Combining(3),(8)–(10)
gives, in these coherent source/target conventions,

    R(a)p= -30 lambda i2(R1(a)p).                    (11)

A different overall reference scalar changes the displayed scalar in
(11), but not the single line it spans or the conclusion beta=0 in
the fixed universal basis. If lambda=0 then R=0; otherwise it is the
R1 line. PR1031 proves R1,R2 independent, so(11) proves(1). PR1036
identifies that line as ellDelta, the conic line.

This does not force lambda nonzero: by PR1094, lambda=0 is precisely
the unselected terminal incidence ell(NR5)=0 in this mechanism. The
new result constrains the entire lift channel, not just its zero locus.
No analogous conclusion is asserted for the nonzero-N0 terminal graph.

## Verification and limits

Run python verify.py and python -O verify.py; both reproduce RESULT.json.
The bounded verifier authenticates all nine inputs, reconstructs both
polarization maps and the exact terminal quotient kernel, proves(7),(9)
and(10) on full coefficient spaces, and checks the Spencer scalar kernel.
No selected actual HM/source coefficient, parameter, point, jet, tensor
or instance rank is evaluated. Written exact-sequence and naturality
arguments are necessary for transporting these universal identities.
No public files are modified and no source occurrence is selected.
