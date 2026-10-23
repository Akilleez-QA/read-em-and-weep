# The actual weight-sixteen affine square law and its missing source row

## Claim and stopping point

This note derives the actual affine transport of the weight-four coefficient
of J4 at physical twist four. It retains the first normal transition qZ
acting on the complete weight-twelve ladder. The resulting affine transport
preserves the full weight-twenty-eight, q-cubed square equation.

It also identifies a precise independent source-row certificate sufficient
to supply that scalar square datum: the physical weight-four trace response
of the full twist-four primitive factors through its full monad differential.
The factorization uses the established ambient H0(End_0(F)(4))=0 and an
authenticated local contraction of the full monad. It does not hold for an
arbitrary projection of a supported middle or a selected coefficient block.

No such source row is evaluated here. Its actual physical matrix and its
value on the corrected source remain missing. Thus this is a new affine
compatibility calculation and a precise remaining source certificate, not
an evaluation of rho16 or beta4. A value of the fourth square alone is not
promoted to the fifth boundary or to its second-symbol quotient.

## 1. Immutable inputs and conventions

Work with the fixed actual marked rank-two bundle F, B=End_0(F), cone
equation q of physical twist two and cover weight four, vertex L=P(W),
and positive binary space U. Sources a and h are nonzero quadratics; a
has transverse weight zero and h has cover degree four. The correction
b=L_can(a,h), actual Atiyah scale, determinant lines and marking units
are retained. No actual coefficient, point, matrix or rank is evaluated.

The immutable inputs in Akilleez-QA/read-em-and-weep are:

- [PR780](https://github.com/Akilleez-QA/read-em-and-weep/blob/c82c3a3b6b513e80a5af21f06ecc52170cb0a056/research/hm/transition-boundary-formula/PROOF.md),
  c82c3a3b6b513e80a5af21f06ecc52170cb0a056: exact homogeneous reference
  transport, the qZ first correction, ordered harmonic operators and the
  faithful leading fifth-boundary formula.
- [PR781](https://github.com/Akilleez-QA/read-em-and-weep/blob/b1b970d232f1e400a8b1c58caafa9080fdfc92da/research/hm/completion-separated-boundary/PROOF.md),
  b1b970d232f1e400a8b1c58caafa9080fdfc92da: fixed normalized charts,
  completion changes, and the exact second-symbol image a^2 A·kappa.
- [PR782](https://github.com/Akilleez-QA/read-em-and-weep/blob/1c0bb2fbcfbe233c669f6a16cbf3ce38d91761d9/research/hm/global-second-jet-recovery/PROOF.md),
  1c0bb2fbcfbe233c669f6a16cbf3ce38d91761d9: the actual leading ladder,
  its coefficient twists and the old exact twist-four trace sequence.
- [PR783](https://github.com/Akilleez-QA/read-em-and-weep/blob/b87bb71fc9fd90cc71d1d9bbe5c27f8d15ac698a/research/hm/b3-tangent-boundary/PROOF.md),
  b87bb71fc9fd90cc71d1d9bbe5c27f8d15ac698a: the distinct twist-six B3
  reference tangent and its nonzero fifth transgression.
- [PR685](https://github.com/Akilleez-QA/read-em-and-weep/blob/449a8df60662bd7a1d93e318ea4f7e6dab28e5ad/research/hm/third-lift-uniqueness/PROOF.md),
  449a8df60662bd7a1d93e318ea4f7e6dab28e5ad: the full-cochain comparison,
  actual completion classification and retained second-symbol quotient.
- [PR683](https://github.com/Akilleez-QA/read-em-and-weep/blob/d4008b924e9ddff9726f86ccccc1574677da9218/research/hm/completion-kernel-dimensions/PROOF.md),
  d4008b924e9ddff9726f86ccccc1574677da9218, Section 6: ambient
  H0(B(4))=0 and the full cochain-to-adjoint map. This vanishing is for
  the actual ambient adjoint bundle, not only a supported subcomplex.
- At [8d8b5be4ce62c3055bb53be9e16d29cc63072f04](https://github.com/Akilleez-QA/read-em-and-weep/commit/8d8b5be4ce62c3055bb53be9e16d29cc63072f04),
  research/hm/order-four-quadratic-load/
  [ACTUAL-FOURTH-BOCKSTEIN-AS-A-FIFTH-NEIGHBORHOOD-ADJOINT-BOUNDARY.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/8d8b5be4ce62c3055bb53be9e16d29cc63072f04/research/hm/order-four-quadratic-load/ACTUAL-FOURTH-BOCKSTEIN-AS-A-FIFTH-NEIGHBORHOOD-ADJOINT-BOUNDARY.md)
  gives the exact global source equations, ladder and global-cochain
  acyclicity for twists at least two. The same commit's
  [CYCLIC-RAO-CUBIC-INJECTIVITY-AND-TWO-S4-LEGS.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/8d8b5be4ce62c3055bb53be9e16d29cc63072f04/research/hm/order-four-quadratic-load/CYCLIC-RAO-CUBIC-INJECTIVITY-AND-TWO-S4-LEGS.md),
  Section 1, explicitly records the established ambient H0(B(4))=0.

The source response below uses those full ambient inputs. It does not
replace them by the supported259 or supported234 exclusions or by the
q-middle coefficient-space construction. Those bounded families address
different source-completion questions.

Let H be the fixed homogeneous harmonic lift. All extractions include
coordinate substitution, physical-twist factors, determinant factors and
the local equation transition before taking a coefficient. In particular,
if q_j=nu_ij q_i, every q_j^r is replaced by nu_ij^r q_i^r first.
Write [q^r] for harmonic coefficient extraction, not restriction before
division. Use the target-minus-transport Cech convention of PR780.

## 2. The two total-weight layers before multiplication by a

The actual J4 lies in B_(4Q)(10), restricts to aJ3, and has total matrix
weight at least twelve. In the fixed regular normalized charts put

    L_i=(J4_i)_[12]=sum_(r=0..3) q_i^r H(c_(r,i)),
    c0=a^3 h n8, c1=a M8, c2=a R4, c3=D0,          (1)

where M8,R4,D0 are the actual leading data of PR782. Their coefficient
weights are 12,8,4,0 and physical twists 10,8,6,4, respectively.
Regularity and the exact leading reference imply that L glues exactly
in the ambient homogeneous reference: a remaining q^4 discrepancy
would have forbidden matrix weight -4.

The normalized N has no weight-twelve correction, so the total-weight-
sixteen part of J4 has no q^0 term. Write it, modulo q^4, as

    D_i=q_i H(s_i)+q_i^2 H(r_i)+q_i^3 H(e_i),       (2)

with coefficient weights 12,8,4 and physical twists 8,6,4. Here r_i is
the first-subleading weight-eight coefficient, not R4 in (1). Put
D_i^<=q_i H(s_i)+q_i^2 H(r_i). The unknown e_i is the weight-four
coefficient of J4 itself. In the notation for K=aJ4 used in PR780,

    B1=a s,   B2=a r,   B3=a e.                    (3)

The factor a in (3) is part of the actual source ladder; it cannot be
removed by a generic division and forgotten at its zeros.

## 3. The actual affine law retains the entire qZ action

Let Phi^10_ij be the exact ambient reference transport at physical twist
ten. Express the first actual correction in the source frame as q_j Z_ij:

    T_ij=T0_ij(1+q_j Z_ij+terms of matrix weight at least eight).

Equation-line units are absorbed by the stated transport convention, not
set to one as an assertion about the geometry. Define the known term

    Omega_ij=Phi^10_ij(q_j[Z_ij,L_j]).              (4)

Because qZ has matrix weight four, the actual gluing law in total weight
sixteen is exactly

    D_i=Phi^10_ij(D_j)+Omega_ij modulo q_i^4.       (5)

Terms of higher transition weight cannot reach this layer. This is the
first layer where qZ acts, unlike the leading layer treated in PR782.

The required lower-data compatibility is

    D_i^<=Phi^10_ij(D_j^<)+Omega_ij modulo q_i^3.   (6)

Define

    G_ij(e_j)=[q_i^3]Phi^10_ij(q_j^3 H(e_j)),
    F_ij=[q_i^3](Phi^10_ij(D_j^<)+Omega_ij).        (7)

Then (5) is equivalent to (6) and the explicit affine equation

    e_i=G_ij(e_j)+F_ij.                             (8)

G is the actual leading transport of the weight-four coefficient bundle
at physical twist four. F retains both harmonic transport of the lower
subleading jets and the transition action on the leading ladder.

In a common equation/scalar trivialization the normal part of F is

    [q^2]Ad(T0)[Z,H(c0)]
      +[q]Ad(T0)[Z,H(c1)]+[q^0]Ad(T0)[Z,H(c2)].    (9)

The c3 term starts in q^4 and does not contribute. The reference part
is [q^2]Ad(T0)H(s)+[q]Ad(T0)H(r). Formula (9) is before any special
weight-zero simplification. In particular c2 has weight FOUR, so its
upper entry need not vanish.

For clarity, if T0=[[alpha,0],[c,delta]], Z=[[t,0],[ell,-t]], and
X=[[x,y],[z,-x]], the full order-zero commutator term is the cone
restriction of the matrix with entries

    diagonal = -(ell+2ct/delta)y,
    upper    = 2alpha t y/delta,
    lower    = 2delta ell x/alpha-2delta t z/alpha
               -2c ell y/alpha-2c^2 t y/(alpha delta). (10)

The other diagonal is its negative. Using the simplified N0 expression
for PR780's weight-zero A3 in place of (10) would wrongly remove entries.
Here alpha and delta are frame units, not the chosen source a.

The exact actual transition cocycle, truncated to its first positive
matrix weight, and the exact reference gluing of L imply that the
transport in (5) composes. With (6), coefficient extraction therefore gives

    G_ij G_jk=G_ik,
    F_ik=F_ij+G_ij F_jk.                            (11)

Thus (8) is a genuine affine cocycle. This uses the first actual normal
transition and does not assume that its nonzero class kappa vanishes.

## 4. The five-term square equation and its affine compatibility

Since J4 restricts to the square-zero aJ3 on 3Q, its scalar norm
n(J4)=tr(J4^2)/2 has the form q^3 rho on 4Q, with rho a global scalar
section on Q of physical twist fourteen. Let rho16 be its cover-degree-
sixteen coefficient. It has coefficient bundle Sym^16 U O_L(6).

There are no intervening matrix weights between twelve and sixteen.
Hence the total-weight-twenty-eight norm is exactly tr(L_i D_i).
There is no additional factor two. Define the scalar lower expression

    Q_i=[q_i^3]tr(L_i D_i^<).

In terms of ordered harmonic products H_k, it is explicitly

    Q_i=tr(H_2(c0,s)+H_1(c1,s)+c2 s
                     +H_1(c0,r)+c1 r).             (12)

All products and contractions use the actual entry degrees. Each term
has cover degree sixteen and physical twist fourteen. The q^3 e term
can pair only with c0 at harmonic order zero, so the exact equation is

    A_i tau_i(e_i)=rho16_i-Q_i,
    A=a^3h,   tau(e)=tr(n8 e).                      (13)

Here A has cover degree four and physical twist eight; tau(e) has cover
degree twelve and physical twist six. They give precisely the types in
(12). This is a square equation on 4Q, not the q^4 norm error of a local
fifth lift and not the surviving degree-twelve fifth norm representative.

For hypothetical lower data, require the lower coefficients of
tr(L D^<) in q^0,q^1,q^2 to vanish, as they do for the actual aJ3.
Let lambda^sc_ij denote transport of the scalar coefficient of rho16.
Then the affine shift satisfies the exact compatibility identity

    A_i tau_i(F_ij)=lambda^sc_ij(Q_j)-Q_i.          (14)

To prove it, use (5) before coefficient extraction. Conjugation preserves
trace, and the new transition contribution has cross pairing

    tr(L_j q_j[Z_ij,L_j])=0                        (15)

identically by cyclicity. Thus tr(L D) transports as the corresponding
scalar section. Its lower q coefficients vanish, so extracting q^3
transports with exactly the equation-line power three. The terms linear
in an arbitrary e_j transport by G and the intrinsic trace map; cancelling
them leaves (14). This also proves square compatibility of (8). Merely
noting (15) cannot justify omitting qZ from the matrix transport (8).

For an independently supplied global rho16, local solvability requires
regular image membership

    rho16_i-Q_i in A_i·(Sym^12 U O_L).              (16)

Multiplication by the fixed nonzero a^3h is an injective sheaf morphism
over the integral base and binary coefficient domain. No source zero
is inverted. The old twist-four sequence is

    0 -> U O_L(-1) -> E_weight4(4)
                  --tau--> Sym^12 U O_L -> 0.      (17)

Equations (14)-(17) make the local solution defects kernel-valued. The
acyclicity H0(U O(-1))=H1(U O(-1))=0 gives one unique globally compatible
regular e. This is the prior acyclic correction principle applied to the
new affine law. It does not supply rho16 independently; defining rho16
from the unknown J4 and invoking this uniqueness would not close a gap.

## 5. The full source equation that supplies the missing scalar datum

Let C^k_t=Gamma(X,D_M^k(t)) in the full fixed-duality trace-free monad
endomorphism complex. Use all source and target blocks, not a supported
middle quotient. The ladder's termwise acyclicity for t>=2 identifies the
cohomology of this global complex with the actual H^k(B(t)). In particular

    ker(d:C^0_4->C^1_4)=im(d:C^-1_4->C^0_4),       (18)

using the established ambient H0(B(4))=0. The source model and this
comparison are required inputs, not numerical rank assumptions.

Choose local splittings of the actual monad into F and contractible
summands, extending on regular ambient charts. Write i_i:F->M and
p_i:M->F for their chain maps, with p_i i_i=1, d_M i_i=0 and p_i d_M=0.
Express the result in the fixed physical frames normalized from N. For
an arbitrary degree-zero cochain X define the local linear projection

    P_i(X)=(p_i X i_i)_0,                            (19)

where the subscript removes scalar trace. On closed cochains (19) is
the induced actual adjoint. On a degree-zero coboundary dY,
p_i(dY)i_i=0 follows immediately from the two chain identities, including
their graded signs. Thus (18) makes P_i vanish on every global closed
twist-four cochain. One may also see this directly: its induced global
adjoint belongs to the zero space H0(B(4)). An arbitrary extraction from
a middle matrix need not have either of these properties.

Define the source trace response, in the fixed chart and normalization,

    ell_i(X)=tr(n8_i [P_i(X)|Q]_[4]),  X in C^0_4.  (20)

It takes values in regular local degree-twelve trace coefficients.
It kills ker d by (18)-(19). Elementary linear algebra therefore gives a
unique map on the actual image of the full differential,

    Lambda_i:im(d:C^0_4->C^1_4) -> local trace coefficients,
    Lambda_i(dX)=ell_i(X).                          (21)

This is a factorization through the SOURCE DIFFERENTIAL, not a map from
H1(B(4)) and not a quotient by the second symbol. Any extension of Lambda_i
off im d is irrelevant and need not be canonical. The individual local
map depends on the authenticated physical contraction; it is not claimed
to be an independently global invariant.

Retain the complete actual source equations with their fixed signs:

    dC_h=a h Z_a-q V_h,
    dE_h=a(V_h-b Z_a)-q W_h,                         (22)
    J3=(a h-q b)U_a-q^2 C_h,
    J4=aJ3-q^3 E_h.

Set Y_i=P_i(aJ3) and y_i=[q_i^3](Y_i)_[16], using the same ambient
contraction and harmonic convention as above. Although aJ3 need not be
closed on 4Q, Y_i is a defined local matrix by (19). No intrinsic global
adjoint is assigned to it. Since projection commutes with multiplication
by q and J4 IS closed on 4Q, its actual coefficient is

    e_i=y_i-[P_i(E_h)|Q]_[4].                       (23)

Combining (13), (20)-(23) proves the independent source-response equation

    rho16_i = Q_i + A_i tau_i(y_i)
       - A_i Lambda_i(a(V_h-b Z_a)-q W_h).          (24)

This is the exact additional source equation needed by the affine square
reconstruction. Its right side is specified from the full lower cochain
and the corrected full differential input; it does not define rho16 by
extracting the square of the unknown J4. Closed changes of E_h with the
same differential disappear under (20). Changes in the cochain choices
V_h,W_h or in source normalization must still be tracked in (22).

Equation (24) is not yet a computation: the local matrices P_i and the
response Lambda_i have not been furnished here. In exact coordinates,
the missing certificate is a row-operator identity on a COMPLETE basis
of global twist-four degree-zero fixed-duality cochains:

    L_i = Lambda_i D,                               (25)

where D is the full monad differential and L_i is (20) independently
assembled from (19). Since the output has binary degree twelve, this is
a block of trace coefficient rows, not a single scalar number. It may
be smaller than constructing a full primitive, but no size estimate or
computational saving is asserted without the actual authenticated maps.

A candidate must retain both source endpoints, all middle channels,
physical frame and marking factors, the actual q, and the -a b Z_a and
-q W_h terms. Checking (25) only on a bounded supported family would
certify only its restriction. Completing the raw target F=kAt a p e_D
does not establish (25) or the corrected source equation in (22).

## 6. Falsification checks and terminal condition

The transport has simple universal tests that require no actual source
specialization. With formal coefficient matrices c2 and Z, retain their
full commutator in q^3[Z,c2]. A formal upper entry y2 in c2 and lower
entry ell2 in Z produce diagonal entries -ell2*y2,+ell2*y2. A formal
diagonal t in Z additionally gives upper entry 2t*y2. Omitting qZ or
copying PR780's weight-zero N0 truncation fails these polynomial
identities. They are free coefficient checks of the transport operator,
not proposed source solutions. The scalar test tr(L[Z,L])=0 still passes
even when a matrix component has been wrongly omitted from a proposed
transport; it cannot replace those matrix tests.

The source certificate has its own required falsification check: for
every global degree-minus-one basis cochain Y, verify P_i(dY)=0, and
verify (25) against every full degree-zero basis cochain. A missing source
block, incorrect physical projection, omitted b term, or independently
renormalized frame must produce a failed identity, not a reported value.
Use regular sheaf image membership (16) at source zeros; fiberwise
cancellation or division by q is not a replacement.

The twist-six reference B3 kernel of PR783 is U O_L(1), with four global
directions and a nonzero fifth transgression. The coefficient in (23) is
instead at physical twist FOUR, with kernel U O_L(-1). Its multiplication
by a gives B3; an arbitrary twist-six reference tangent need not be
divisible by a or satisfy (22). No actual completion freedom is added.

Terminal condition for this lane is an independently replayed certificate
(19),(25) for the actual complete source complex, together with the
corrected right-hand side of (22), the cochain y_i, and regular overlap
checks of (24). Without these, the precise unresolved item is the
authenticated full-source trace-response block (25), not a free choice
of e or of rho16. The affine and square identities above already identify
its required types, signs and transition compatibility.

Even after (24) is supplied, the fifth value is obtained through PR780's
faithful LINEAR cocycle and then reduced modulo the exact image
a^2 A·kappa of PR781, retaining exceptional axes and source divisors.
This note does not infer beta4 from rho16, saturate that image, or decide
the original proof-repair or algebraicity question.
