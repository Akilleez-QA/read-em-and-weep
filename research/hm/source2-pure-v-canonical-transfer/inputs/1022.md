# The pure-V source2 quotient has zero first symbol and no P second channel

## Theorem and boundary

Retain the original actual-source hypotheses and suppose that a nonzero
pure-V negative-pencil radical j is Q-compatible. Let M be the original
complex N2 --Q+tT_a--> N4, and let I=im j and U=M/I be the genuine quotient.
Then the quotient original-Q cohomology has canonical equivariant types

    H0(U)=A+P,                  H1(U)=P.

The ENTIRE first Bockstein of U vanishes. Under the natural identification
H1(M)=H1(U), its second Bockstein is exactly

    beta2,U,a(x,p)=beta2,M,a(x),       x in A, p in P.           (1)

In particular its quadratic P-to-P channel is zero. This is not inferred
from character dimensions or a rank count. The proof uses the exact
original third vanishing, the actual image map D->P, and saturation of the
original second-symbol image. No universal quadratic P-endomorphism is
assumed singular or zero without this geometric argument.

Consequently, at a general direction, the quotient has 29 unit Smith
factors, three factors of valuation two, and a residual one-by-four formal
matrix divisible by t^3. The last residual matrix can still be zero or
nonzero. No source pair is excluded and no fourth or later original
Bockstein value is selected.

## 1. Immutable inputs and notation

INPUTS.json authenticates unchanged public originals:

* PR950, 54c7e78bd5351b3ecbdcc4b3b558a0012eb79566: pure-V Q alignments
  and genuine quotient cohomology, dimensions and invariant rank.
* PR792, 2f01f18960ce56b8b2a0c1260c277de3c5f916bf: actual fixed-variable
  pure-V image multiplication.
* Original first vanishing, eeb1a11799ca38a60c37f6ba96f263ef8e20dd1c.
* Original second nonvanishing, 6c724c3b74e2ae4d6992d8c7b99b41c0715d69c0.
* Original third vanishing, db51525015bb7c5e825833d550d08dedf6f6ea96,
  ACTUAL-THIRD-BOCKSTEIN-VANISHES-IDENTICALLY.md. Sections3-4 also retain
  that beta2,A has rank3 away from precisely six projective axes and rank2
  at those axes. These precise lower-symbol statements are imported here.
* PR966, 4d0a6713a9c81fe669967e1d23838bdc8f4162b6: L_a:D->P has rank4
  away from ten directions, in particular generically. Only its generic
  surjectivity is needed below.

The actual source and fixed-variable hypotheses of these originals remain
in force. No abstract bundle splitting is used as a horizontal splitting.
All complexes are in cochain degrees zero and one. The first new secondary
homotopy packet is not needed as a premise; the argument starts directly
from the pinned source2 image and quotient.

Write q for Q, T for T_a when a is fixed. PR950 gives

    I0=D=(ker q)_D, I1=P=im j4 subset im q,
    ker j4=im q, q|I0=0, H0(M)=A+D, H1(M)=P.

Thus I has differential tL_a, where the actual restriction is

    L_a:Sym4 W -> Sym6 W/V6,       d |-> [a d].                 (2)

The original and quotient first/second symbols below are those of the
specified two-term families, not a different obstruction construction.

## 2. Actual long sequence and descended radical

At t=0 the short exact sequence I->M->U gives

    0 -> D -> A+D -> H0(U) --delta--> I1 -> H1(M)
      -> H1(U) -> 0.

The map I1->H1(M) is zero since I1 subset im q. Hence

    0 -> A -> H0(U) --delta--> P -> 0,
    p1:H1(M) -> H1(U) is an isomorphism.                       (3)

Finite-group semisimplicity splits the first sequence equivariantly, and
Hom_G(P,A)=0 makes this splitting unique. Thus the P-isotypical part of
H0(U) maps isomorphically to I1 under delta. Let sigma:I1->H0(U)_P
be its inverse. At the level of actual representatives, if bar x is a
quotient q-cycle and x a lift, then

    delta(bar x)=q x in I1.                                  (4)

The radical j annihilates I because j^2=0, and therefore descends to a
chain map f:U->I for every t and every negative quadratic. Its cohomology
map f0:H0(U)->D vanishes by Hom_G(A+P,D)=0. Its map f1:H1(U)->I1
is an isomorphism: it is induced by j4, whose kernel is im q and whose
image is I1; quotienting first by I1 does not change this assertion.

First-symbol naturality is

    L_a f0 = f1 beta1,U,a.

The left side is zero and f1 is invertible. Thus beta1,U vanishes on BOTH
A and P, for every a. This is the whole quotient first vanishing, not only
its restriction to the original kernel image A.

## 3. Second restriction and original-third comparison

Since both first symbols vanish, quotient projection naturality on the
second page gives

    beta2,U,a|A = p1 beta2,M,a|A.                              (5)

Let E_a denote beta2,U,a on the canonical P summand from (3). It is an
equivariant homogeneous quadratic family P->P. We next prove that it is
zero using the original third symbol, not equivariance alone.

Fix d in D and let v=sigma(L_a d). Choose a representative bar x of v in
U0 and a lift x in M0. Equation(4) gives exactly

    q x = L_a d = T d.                                        (6)

Since beta1,U=0, the class of T x in H1(U) is zero. Because I1 subset
im q, this implies T x belongs to im q. Choose y in M0 with

    q y = -T x.                                              (7)

Then bar y is a first correction for v in U, so

    beta2,U,a(v)=[T bar y].                                   (8)

In M, the successive lifts of d are d, -x, -y, since

    q(-x)=-T d,             q(-y)=-T(-x).

Thus its original third obstruction is represented by -T y, modulo the
image of the original second differential. All choices give the same
third-page class; changing a first correction may change the raw target
class by beta2,M(H0(M)), which is precisely the quotient being taken.
Consequently, after identifying targets through p1,

    beta3,M,a(d) = -[ E_a sigma L_a(d) ]
                    in H1(U)/im(beta2,U,a|A).                 (9)

Here beta2,M(D)=0, so every d reaches the third page. Equation(9) is an
identity of actual corrected lifts, with its minus sign retained. It does
not identify raw quotient beta2 values with an unquotiented original
third class.

The imported original beta3 vanishes. On the dense open where L_a is
surjective, equation(9) therefore implies

    E_a(P) subset im(beta2,M,a|A).                            (10)

This is only a GENERIC image containment at this point. The next step,
not a rank estimate, turns it into global factorization and vanishing.

## 4. Saturation kills the entire quadratic P channel

On X=P(A), write B for the universal original second map

    B:A O_X(-2) -> P O_X.

It is injective as a sheaf: it is generically injective, and its source is
locally free on the integral surface. By the retained six-axis theorem,
its rank-drop locus is finite. Its cokernel C is torsion-free, as follows.

Away from that finite locus C is a line bundle, so any torsion would be
supported at finitely many points. At any such point the local ring R is
regular of dimension two, and the exact presentation

    0 -> R^3 -> R^4 -> C_p -> 0

and the depth lemma give depth(C_p)>=1. A nonzero finite-length submodule
would have a nonzero socle and force depth zero. Therefore there is no
such torsion. This proves saturation of im B without assuming that
pointwise images and sheaf kernels commute with specialization.

The quadratic family E defines E:P O_X(-2)->P O_X. Equation(10) says
that its composite with C is zero generically. Since C is torsion-free,
this composite is identically zero. Hence E factors uniquely as

    P O_X(-2) --F--> A O_X(-2) --B--> P O_X.                  (11)

All maps are G-equivariant; uniqueness forces F equivariant as well.
But F is a constant bundle map, since H0(O_X)=C. Its constant matrix
belongs to Hom_G(P,A)=0. Thus F=0 and E=0, proving(1).

This argument avoids assuming a classification or a chosen coefficient
of the two-dimensional quadratic P-endomorphism space. Generic containment
alone would NOT suffice without the torsion-free cokernel, matched degree
twists and inequivalent coefficient representations used in(11).

## 5. Formal consequence and limits

PR950 gives quotient dimensions36->33 and q-rank29. Cancelling those29
unit pairs leaves a four-by-seven formal differential. The entire quotient
first vanishing makes it divisible by t^2. Its second coefficient is
[B,0] on A+P, by(1). Away from the original six axes B has rank3, so three
valuation-two pairs cancel, leaving a one-by-four residual divisible by
t^3. This says nothing yet about that residual coefficient's value.

In particular, the zero P second channel is a new exact quotient-interface
constraint. It does not claim equivalence of M and U, which PR950 explicitly
rules out already on initial kernel cohomology. No fourth original symbol,
third quotient symbol, actual compatible radical or surviving source pair
is selected or excluded here.
