# Polarized sandwich vanishing in the pure-V source2 branch

## Theorem and scope

Retain the actual source2 hypotheses and suppose a nonzero pure-V radical
j is Q-compatible. Let h:N4→N2 be the canonical equivariant homotopy of
PR1019. Then the following are literal identities of actual linear maps:

    h T_a h =0                         for every negative quadratic a; (1)
    K_a K_b=0                          for all a,b,                     (2)

where K_a=(hT_a,T_a h) is the chain endomorphism of the Q complex. These
are stronger than the previously known square-zero maps on Q-cohomology.

Write X_l:N2→N3 and Y_l:N3→N4 for the actual negative linear multiplication
arrows, l in the fixed two-dimensional NEGATIVE linear space W. All four
variables l,m,r,s below range only in this same W, so mr belongs to
Sym^2 W=A. No positive or arbitrary ambient linear form is included. They satisfy Y_l X_m=Y_m X_l=T_lm. The middle-degree maps

    S_lm=X_l h Y_m:N3→N3

satisfy the fully polarized identity

    S_lm S_rs=0                         for all l,m,r,s.                (3)

The cross-direction defect

    C_ab=T_b hT_a−T_a hT_b:N2→N4

is NOT asserted zero. It has a canonical factorization

    N2/(ker Q+im h) → ker h intersect im Q,                             (4)

with source character 2V+2P+3D of dimension29 and target character
2V+3P+2D of dimension28. The family is alternating in a,b.

No actual two-channel lift coefficient is selected or excluded by this
packet. In particular (2) says that the secondary endomorphisms multiply
to zero; it does not say that K_a commutes with multiplication T_b for
unrelated directions. The new deduction is the exact polarized identities
(1)–(4), using the previously proved raw quotient second vanishing.

## 1. Inputs and actual types

INPUTS.json pins unchanged copies of four public proofs:

- PR1019, 3fb2475ffb275c5789acbaa8f9f84ed272713785: canonical h with
  hQ=j2, Qh=j4, j2h=hj4=0, im h of character D+P, and
  im h intersect ker Q=D. It gives k_a^0(x,d)=mu a x in D for
  (x,d) in ker Q=A+D, with mu nonzero, and T_a h(N4) subset im Q.
- PR1022, 5488bc153029391d647c3e18d9344e4e00e38a7f: for the genuine
  quotient U=M/im j, the entire first Bockstein vanishes and the second
  is zero on the canonical P summand of H0(U)=A+P. This is a RAW
  H1(U) vanishing, not only vanishing modulo the A second image.
- PR1025, 09f1377f83b027ca27eea0b3a9f40a1b92c6c466: the actual image
  pencil L has the sheaf kernel O(−5) in D O(−1). Equivalently,
  ker[D O→P O(1)]=O(−4) on X=P(A).
- PR792, 2f01f18960ce56b8b2a0c1260c277de3c5f916bf: the full graded
  negative image module and its fixed-variable identifications. The
  actual X_l,Y_l are multiplication by the same negative linear forms,
  and their restriction to D→I4 is polynomial multiplication followed
  by Sym6 W→Sym6 W/V6=P.

Here I0=D=im j2 is contained in ker Q, and I1=im j4=P is contained in
im Q. The image complex has Q differential zero and T differential L.
We distinguish I1 from H1(M)=coker Q; j4 induces their isomorphism

    iota:H1(M)→I1.

The quotient U has H1(U)=H1(M), and its descended radical f:U→I has
isomorphism f1:H1(U)→I1 induced by j4. No extension of h to a graded
module homomorphism is assumed. The maps X_l hY_m are well typed without
such an extension.

## 2. The sandwich and the exact quotient-second representative

Put H_a=hT_a h:N4→N2. First,

    Q H_a=j4 T_a h=T_a j2h=0,
    H_a Q=hT_a j2=h j4 T_a=0.

Since H_a lands in im h, its image is in im h intersect ker Q=D.
Its vanishing on im Q shows that it factors through coker Q=P. Thus H
is an equivariant LINEAR family P→D, or a bundle map

    H:P O_X(−1)→D O_X.                                           (5)

We now prove L_a H_a=0 by an actual corrected lift, retaining its sign.
For y in N4, the class of hy in U0 is a Q-cycle because Qhy=j4y is in
I1. Changing y by Qv changes hy by j2v in D, so this quotient cycle
depends only on [y] in H1(M). Its connecting image is j4y. Since this
is an equivariant isomorphism onto I1, and Hom_G(P,A)=0, these cycles
represent EXACTLY the canonical P summand in H0(U), not a chosen mixing
with the A summand.

The map T_a h lands in im Q, by PR1019. Hence choose z in N2 with

    Qz=−T_a hy.

Then the class of z in U0 is a first correction to [hy]. Because the
entire quotient first differential is zero, the raw second class is
[T_a z] in H1(U). PR1022 makes this class zero on our P input. Applying
f1 and using the exact intertwining identities gives

    0=f1 beta2,U([hy])
     =j4 T_a z=T_a j2z=T_a hQz
     =−T_a hT_a hy=−L_a H_a y.                               (6)

There is no quotient by im beta2(A) in (6): that quotient first appears
on the next page, not in the second differential itself. This distinction
is essential to the argument.

By (6), (5) lands in ker[D O→I1 O(1)]=O(−4). But

    Hom(P O(−1),O(−4))=P* tensor H0(O(−3))=0.

Therefore H=0 as a bundle map, and hence as a homogeneous linear
polynomial family, proving (1). This uses the genuine kernel sheaf;
no pointwise kernel rank, generic specialization, or actual coefficient
value is substituted.

## 3. Mixed square-zero products and the full middle degree

On the two endpoints the products factor literally as

    K_a^0 K_b^0=(hT_a h)T_b=0,
    K_a^1 K_b^1=T_a(hT_b h)=0.

This proves (2) for independent directions, without assuming any relation
between T_a and T_b through h. The operators K_a are Q-chain maps because
QhT_a=T_a hQ follows from j4T_a=T_a j2. In the algebra of Q-chain
endomorphisms, their span is a three-dimensional square-zero subspace:
its parameter map A→End_Q(M) is injective since its action on the actual
A in ker Q is mu times multiplication by a. Together with the identity,
it gives a G-stable algebra C direct-sum A with radical product zero.
It is not asserted to lie in the algebra of endomorphisms of the full
fixed negative pencil: that would require additional cross-direction
intertwining which is not proved here.

For the full negative three-space module, associativity and commutativity
of its multiplication yield

    S_lm S_rs
       =X_l h(Y_m X_r)hY_s
       =X_l(hT_mr h)Y_s=0.

This proves (3) simultaneously for all four linear directions. In
particular it retains the middle degree and mixed linear arrows rather
than replacing the actual module by an abstract one-direction complex.
No claim that the individual S_lm extend to fixed-pencil endomorphisms
is made.

## 4. Exact cross-direction defect and its smaller interface

For D_b(t)=Q+tT_b, the endpoint pair K_a has chain defect

    D_b(t) K_a^0−K_a^1 D_b(t)=t C_ab.                         (7)

The Q term is zero, but (7) does not vanish merely from (1). To identify
what is forced, first take x+d in ker Q=A+D. PR1019 gives
hT_a(x+d)=mu a x in D. Therefore

    C_ab(x+d)=mu([b a x]−[a b x])=0

in the ACTUAL image quotient Sym6 W/V6. This cancellation uses the full
negative multiplication, not an assumption that the sandwich commutes.
Next, (1) gives C_ab h=0 and h C_ab=0. Finally both terms of C_ab land
in im Q because T_b h and T_a h do. Thus C_ab kills ker Q+im h and
lands in ker h intersect im Q, proving the canonical factorization (4).

The dimension and character claims use only exact subspaces:

    ker Q+im h has character A+D+P,
    h|im Q has image D.

Subtracting from N2=A+2V+3P+4D and im Q=2V+3P+3D gives respectively
2V+2P+3D and 2V+3P+2D. Equation (4) is an alternating bilinear family
on A, but no claim that its coefficient tensor vanishes is made.

## 5. Noncommutation control and remaining coefficient question

The checker supplies an exact synthetic three-space module with commuting
negative linear multiplications, square-zero compatible j, hQ=j2,Qh=j4,
j2h=hj4=0, hT_a h=0, and raw quotient-second vanishing on its connecting-cycle input, for which C_ab is the nonzero symbolic entry

    a0 b1−a1 b0.

It uses independent quadratic coefficient variables, not sampled values.
This is only a control against treating sandwich vanishing as formal
cross-direction commutation. It does not have the actual source characters
and is not an actual source realization or a counterexample to any extra
geometric constraint.

The new identities do not yet impose a scalar equation on the two
quadratic-lift coefficients of PR1025. Such an equation would need a
further connection between the remaining cross defect (4), correction
operators, and the actual third quotient symbol. Same-direction naturality
cannot be silently substituted for that missing cross-direction relation.

## Reproduction

Run `python verify.py` and `python -O verify.py`. The checker authenticates
four immutable inputs, checks every displayed composite's types, character
and twist arithmetic, symbolic multiplication cancellation, and the full
synthetic commuting-arrow control including all16 middle products. The
written corrected-lift and kernel-sheaf argument proves (1); finite checks
do not replace the imported geometric theorems or evaluate an actual source.
