# Completion changes do not alter the normal-transition term

## Statement and exact scope

Fix the actual nonzero negative quadratic a, positive source h, correction b,
canonical first lift U_a, and marking. Use the same regular normalized physical
charts and homogeneous harmonic convention throughout. These charts are fixed
from N, not chosen again for each completion. All statements concern the
classified even completion and fourth-lift changes of PR685, not arbitrary
source, frame, or Schur-normalization changes.

The required pinned inputs are:

- [PR685](https://github.com/Akilleez-QA/read-em-and-weep/blob/449a8df60662bd7a1d93e318ea4f7e6dab28e5ad/research/hm/third-lift-uniqueness/PROOF.md), §§3–4: every classified difference is
  J4'−J4=−q² U_a tilde(s)+q³ Nt, with s,t in A⊕D5, and
  delta5(aJ4')−delta5(aJ4)=−beta2_a(s) in its q−ta convention.
- [The canonical square-zero first lift](https://github.com/Akilleez-QA/read-em-and-weep/blob/8d8b5be4ce62c3055bb53be9e16d29cc63072f04/research/hm/order-four-quadratic-load/ACTUAL-MULTIPLIED-NILPOTENT-HAS-A-CANONICAL-SQUARE-ZERO-LIFT.md), §§2–4: U_a is a section of B_(2Q)(4), restricts to aN, and satisfies U_a²=0 on 2Q. Its cochain boundary sign is the target-minus-transport Čech sign.
- [PR780](https://github.com/Akilleez-QA/read-em-and-weep/blob/c82c3a3b6b513e80a5af21f06ecc52170cb0a056/research/hm/transition-boundary-formula/PROOF.md), §§1–5: the all-point physical filtration, regular leading pair, normalized charts, faithful isomorphism E, and formula

      C_ij = −M2(B2_j)−M1(B3_j)
             −N2(A1_j)−N1(A2_j)−N0(A3_j).             (1)

The notation M2,M1,N2,N1,N0 means the fixed overlap operators of PR780.
Every input, scalar twist, local equation and coordinate substitution is
transported into chart i before coefficient extraction, as in that proof.
In particular division by q⁴ changes physical twist twelve to four.

Then:

1. The entire total-weight-twelve piece K12 of K=aJ4, and hence each A0,A1,A2,A3, is independent of the classified completion and fourth lift.
2. Only the A-component s_A of s changes the total-weight-sixteen piece. If

       (U_a)8 = H(U0)+q H(U1) modulo q²,
       wt(U0)=8, wt(U1)=4,

   then U0=a n8 and, in the normalized local fifth lifts with B4=0,

       ΔB1=0,  ΔB2=−a s_A U0,  ΔB3=−a s_A U1.       (2)

3. The overlap cochain

       Theta_a(s_A)_ij
          = a s_A [M2(U0_j)+M1(U1_j)]               (3)

   is a genuine J0(4)-valued Čech cocycle, and

       C(K')−C(K)=Theta_a(s_A),
       [Theta_a(s_A)]=−E(beta2_a(s_A)).              (4)

   Thus the exact ambiguity image E(im beta2_a) is the image of the cohomology classes in (3), without any rank assumption.

4. The normal-transition contribution

       C^normal_ij=−N2(A1_j)−N1(A2_j)−N0(A3_j)      (5)

   is independent of every classified completion in these fixed charts.
   This is a statement about a cochain, not a claim that (5) is separately a cocycle or defines an independent cohomology class.

## 1. The needed first-lift weight bound is forced by square-zero

The nonnegative regular even matrix weights are 0,4,8,…; q has weight four.
Since U_a|Q=aN and N starts in weight eight, any term of U_a below weight
eight must, modulo q², have the form qD0, where D0 is a regular weight-zero
trace-free matrix. There is no possible term of weight zero, since it would
have to be q times a regular negative-weight coefficient.

The total-weight-twelve part of U_a² modulo q² is therefore

    q a {n8,D0}.

Here the square of the cone-leading term starts in weight sixteen, and
(qD0)²=0 modulo q². The square-zero first-lift theorem and the last-layer
injection for 2Q imply a {n8,D0}=0 on Q. Write, in a regular normalized chart,

    n8=u [[f3 g5,−f3²],[g5²,−f3 g5]],
    D0=[[x,0],[z2,−x]].

Rank-two polarization gives {n8,D0}=tr(n8 D0) Id, with

    tr(n8 D0)=u(2 f3 g5 x−f3² z2).

The actual regular-pair argument in PR780 §1 makes this trace map injective
on weight-zero coefficients over every point of L. Multiplication by the
nonzero base section a is injective on these locally free coefficient
modules over the integral line. Hence D0=0. This uses no inversion of a at
its zeros. We have proved U_a has total weight at least eight everywhere.

Because U_a is only needed modulo q², its weight-eight piece has exactly the
two terms displayed above. Its cone restriction gives U0=a n8. No value of
U1 is selected or evaluated.

## 2. Locate every classified change in the filtration

Multiply the exact PR685 classification by a:

    ΔK=−q² a U_a tilde(s)+q³ aNt.                    (6)

Take the fixed homogeneous lifts of the A and D5 components of s. On the
negative-coordinate charts, a and s_A are base-only and have weight zero;
s_D has weight four. Consequently the three relevant lower weight bounds
in (6) are respectively

    q² a U_a s_A: 16,
    q² a U_a s_D: 20,
    q³ aNt:       20.

Changing the ambient lift of s by q times a constant adds a term of the
second weight range, so it cannot change anything below weight twenty.
Thus ΔK12=0 and

    ΔK16=−q² a s_A H(U0)−q³ a s_A H(U1) modulo q⁴.   (7)

Multiplication by base-only a s_A commutes with the fixed harmonic lift and
all harmonic coefficient operators. Equation (7) therefore proves (2).

The local N-normalization from PR777 is common to all completions: it is
chosen from the fixed N. Its weight-four frame correction cannot change
the weight-eight piece of U_a, nor the weight-sixteen leading difference
in (7). It transforms all K coefficients simultaneously, as required by
PR780. Choosing B4=0 afterwards is the same fixed harmonic extension rule
for each local section. Other local fifth extensions change the resulting
leading boundary by a coboundary only. No global gauge is asserted.

The physical twists also match: U0 has twist four and U1 twist two;
a s_A has twist four. Hence ΔB2 has twist eight and ΔB3 twist six,
exactly twelve minus twice their normal indices. M2 and M1 remove normal
twists four and two, respectively, so (3) has physical twist four.

## 3. Exact variation and separation

Insert ΔA_r=0 and (2) into (1). Its two transport minus signs cancel the
minus signs in (2), giving (3)–(4) at cochain level. Both full C(K') and
C(K) are actual leading boundary cocycles by PR780, so Theta is a cocycle;
one need not assume the separate transport or normal parts are cocycles.
PR685 then gives its class with the sign stated in (4). The canonical
first-lift theorem §2 explicitly checks that the cochain-division convention
agrees with target-minus-transport Čech boundaries, so no unnoticed sign
switch is being used.

Every s_A is realized by a classified completion, and s_D as well as the
independent fourth-lift freedom has no effect on the normalized C at all.
Consequently (3) realizes the full exact second-symbol image, rather than
only a contained subspace or a generically saturated image. In particular
the already known vanishing of beta2_a on D5 is also visible directly from
the weight bound and faithfulness of E.

Finally ΔA_r=0 proves (5). The actual nonzero transition class κ remains in
the N operators, but this entire explicit κ-dependent contribution cannot
be altered by classified completions. The transport formula for the
ambiguity does not imply that U1, or beta2 itself, is independent of the
underlying first-normal geometry.

## 4. A source-free representative of the same ambiguity

There is a useful further refinement using the exact coherence already
proved in [PR739](https://github.com/Akilleez-QA/read-em-and-weep/blob/9b67dae4d91e81b9e514f4072bfc3774ffd0028f/research/hm/actual-scalar-compatibility/PROOF.md), §§1–2, and its pinned sources. On a negative chart r≠0, put
N_r=U_(r²)/r². This is regular because r is a chart unit, not because the
chosen source a is inverted. Write the scalar in that coherence theorem as
κ_conn, to distinguish it from PR779's transition class κ. The exact
identities are

    U_a=(a−q κ_conn α′)N_r modulo q²,
    N_t−N_r=−2κ_conn qN/(rt) modulo q².

The correction terms on the right start in total weight twelve. The
weight-eight part of N_r is therefore independent of the negative chart
generator, and

    (N_r)8=H(n8)+q H(T4),
    (U_a)8=a[H(n8)+q H(T4)].                         (8)

These are identities of regular coefficients everywhere along L. One can
use the square-zero argument above for the lower bound of U_(r²), divide
only by the chart unit r², and cover the other locus by t≠0. Alternatively
PR692 supplies the generic bound and PR774 extends it to all regular
coefficient bundles. The common weight-four normalization does not affect
these weight-eight terms.

Define the source-free overlap expression

    Theta_ij=M2(n8_j)+M1(T4_j).                      (9)

Its physical twist is −2: n8 has twist two and T4 twist zero, and the
operators remove normal twists four and two. It is a J0(−2)-valued
cocycle, for a reason stronger than multiplying it by a source. Namely,
the exact homogeneous ambient transitions T0 define a reference adjoint
bundle. The local sections m_i=H(n8_i)+qH(T4_i) glue on 2Q in that
reference: the differences of the actual N_r and the difference between
actual and reference adjoint transport both start in total weight twelve.
Their weight-eight differences are therefore q²-divisible. The third-layer
boundary of this reference section is

    [q²](m_i−Ad(T0_ij)m_j)=−Theta_ij.

There is no local q² term in the chosen m_i. The exact T0 cocycle, including
all line and equation transitions, makes this quotient an honest Čech
cocycle in J0(−2). This reference-bundle argument says nothing about whether
the separate normal contribution (5) is a cocycle.

Equations (3), (8), and (9) now give the sharper formula

    Theta_a(s_A)=a² s_A Theta,
    E(beta2_a(s_A))=−[a² s_A Theta].                 (10)

The class [Theta] is Γ-invariant. Indeed the canonical U_a family is
equivariant, its weight-eight quotient is intrinsic, and (8) proves that
division by a locally nonvanishing negative generator yields an object
independent of that generator. The exact homogeneous reference lift and
its boundary are natural under Γ. No equivariant choice of individual
frames is needed.

As a comparison only, the published nonzero second symbol in PR685 §5
and (10) force [Theta]≠0. PR778 proves H1(J0(−2))^Γ is a line, and PR779
proves that its actual transition class κ is nonzero. Consequently
[Theta] and κ span the same invariant line, without identifying their
normalizations. Multiplication by a²A therefore gives the exact image

    E(im beta2_a)=a² A · [Theta]=a² A · κ.            (11)

Here the last equality is an equality of subspaces, not equality of the
maps in (10) with an independently normalized κ-multiplication map. It
does not identify κ_conn with κ. This comparison is not claimed as a new
dimension, exceptional-axis, or generic-rank theorem.

## Contribution and limits

PR685 gives the abstract ambiguity image; PR713 already observes stability
of one leading third-lift coefficient; PR780 supplies the full faithful
linear boundary formula. The additional result here is their filtered
separation: the entire leading input is completion-independent, the only
active completion directions occupy exactly B2 and B3, and their actual
Čech cocycle is (3). In particular the κ-dependent normal-transition term
is fixed throughout the classified completion torsor, even before passing
to the obstruction quotient in the fixed chart convention.

This does not identify the normal term alone with a cohomology class,
eliminate κ by a global frame, show its pairing with any source is nonzero,
evaluate beta4, or strengthen the previously known dimension, exceptional
axis, secant or jet-detection results. All arguments are structural and
use only universal matrix identities and the pinned actual-family inputs.
No selected coefficients, points, derivatives, matrices, ranks, source
values, scans, or large computations are used. This is authored mathematics,
not proof-assistant verification.
