# The weight-four tangent input surjects onto the faithful fifth boundary

## Result and precise scope

Use the exact homogeneous reference transitions T0 of PR778 and the
normalized notation of PR780. At matrix weight four and physical twist six,
let T be the kernel of trace against n8. Then

    T = U O_L(1),    H0(T) = U tensor W = P4.

For a section D of T, the change B3 -> B3+D changes the reference leading
fifth-boundary cocycle by -M1(D). The resulting map

    mu:H0(T) -> H1(J0(4)) = P4

is an isomorphism. More precisely, its defining reference lifting extension
is isomorphic to the twisted quadratic evaluation sequence

    0 -> U tensor W O_L(-2)
      -> U tensor Sym2 W O_L(-1)
      -> U O_L(1) -> 0.                              (1)

This is proved by a morphism of exact sequences, not by an invariant-Ext
dimension argument. No numerical scalar identifying the two P4 spaces is
chosen.

These directions are homogeneous reference tangent variations, not
classified changes of the actual source ladder. They preserve the retained
total-weight-twenty-eight square constraint on 4Q, but this statement does
not claim a full actual square-preserving or whole-cone realization.
In particular q^3H(D) glues modulo q^4 in the retained total-weight-sixteen
reference problem. Higher non-q terms of the actual transitions can create
higher-total-weight discrepancies; no compensation for those is asserted.

## Pinned inputs

1. [PR780](https://github.com/Akilleez-QA/read-em-and-weep/blob/c82c3a3b6b513e80a5af21f06ecc52170cb0a056/research/hm/transition-boundary-formula/PROOF.md), c82c3a3b6b513e80a5af21f06ecc52170cb0a056,
   research/hm/transition-boundary-formula/PROOF.md, gives the exact T0
   transport, the faithful leading boundary, and its M1 term. In particular
   J0(4)=P4 O_L(-2), and trace against n8 identifies this bundle with the
   degree-eight square-relation bundle R in Sym8 U O_L(2).
2. [PR781](https://github.com/Akilleez-QA/read-em-and-weep/blob/b1b970d232f1e400a8b1c58caafa9080fdfc92da/research/hm/completion-separated-boundary/PROOF.md), b1b970d232f1e400a8b1c58caafa9080fdfc92da,
   research/hm/completion-separated-boundary/PROOF.md, Section 4, gives a
   genuine section on reference 2Q whose total matrix weight is eight:

       m = H(n8) + q H(T4).                          (2)

   This follows from the exact multiplied-nilpotent coherence, not from an
   assumed globally framed actual first-normal nilpotent. Its square is
   zero on reference 2Q: it is the weight-sixteen square component of the
   actual square-zero U_a, whose lower weight is eight. Equivalently this
   follows chartwise from the square-zero chart sections N_r used there.
3. [PR718](https://github.com/Akilleez-QA/read-em-and-weep/blob/2411fcd92acd738d0d8af7bebc79ee9191b276ef/research/hm/trace-obstruction-target-reduction/PROOF.md), 2411fcd92acd738d0d8af7bebc79ee9191b276ef, and [PR724](https://github.com/Akilleez-QA/read-em-and-weep/blob/2061379fe77ec4c82b5f05c7a11d3b7454b97a04/research/hm/canonical-trace-isomorphism/PROOF.md),
   2061379fe77ec4c82b5f05c7a11d3b7454b97a04, prove the following universal
   regular-pair facts. For n=u[[fg,-f^2],[g^2,-fg]], with degrees (3,5),
   first-normal nilpotent coefficient T4, and

       D_ell = ell [[f/2,0],[g,-f/2]],
       Psi(D) = tr(T4 D) + tr H1(n,D),

   one has f | Psi(D_ell), and

       ell -> [Psi(D_ell)/f] in (k[X,Y]/(f,g))5     (3)

   is an isomorphism. These are universal identities and regular-pair
   duality, with no selected actual coefficient evaluation. The convention
   D=ell[[f,0],[2g,-f]] in the present question doubles (3), which has no
   effect on invertibility. PR724 proves (3) for every regular pair, not
   only for one generic example.
4. At 8d8b5be4ce62c3055bb53be9e16d29cc63072f04, under
   research/hm/order-four-quadratic-load/, the old notes
   [ACTUAL-LOWEST-NEXT-ERROR-TANGENT-COEFFICIENT-IS-ACYCLIC.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/8d8b5be4ce62c3055bb53be9e16d29cc63072f04/research/hm/order-four-quadratic-load/ACTUAL-LOWEST-NEXT-ERROR-TANGENT-COEFFICIENT-IS-ACYCLIC.md) and
   [VERTEX-QUINTIC-RELATION-EXTENSION-AND-SQUARE-P4.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/8d8b5be4ce62c3055bb53be9e16d29cc63072f04/research/hm/order-four-quadratic-load/VERTEX-QUINTIC-RELATION-EXTENSION-AND-SQUARE-P4.md) give respectively the
   trace kernel U O_L(-1) at twist four and the exact quintic relation
   channel

       0 -> P4 O_L(-1) -> Sym5 U O_L -> U O_L(2) -> 0. (4)

   The latter is id_U tensored with complete quadratic evaluation, under
   Sym5 U = U tensor Sym2 W. Its kernel is U tensor W O_L(-1).

All uses of the finite-group and physical-even markings are the ones in
these sources. The ordinary stack-square relation is retained; no coarse
annihilator square is substituted.

## 1. The intrinsic reference extension defining mu

Twisting the old trace-kernel coefficient sequence by two gives
T=U O_L(1). Locally its elements are exactly

    D=ell [[f,0],[2g,-f]],    deg(ell)=1.             (5)

This is a bundle identity with its triangular transition, not a product of
independently global f and g. The reference lift of T0 is exactly
multiplicative. Hence ambient homogeneous matrices of weight four and
physical twist six give an honest coefficient bundle. Let E_mu be the
inverse image of T under restriction of that bundle to q=0. Division by q
identifies the kernel with weight-zero coefficients of physical twist four:

    0 -> J0(4) --q--> E_mu -> T -> 0.               (6)

Every local section is uniquely H(D)+qX0. Higher powers of q would require
negative regular physical-even matrix weight and are absent. The harmonic
choice need not glue, which is precisely what (6) measures.

For a global D, use local lifts H(D_i). With PR780's target-minus-transport
convention the connecting cocycle is

    c_ij = [q](H(D_i)-Ad(T0_ij)H(D_j)) = -M1(D_j). (7)

Indeed the only harmonic correction here is order one. Multiplying by q^3
turns (7) into the q^4 boundary of q^3H(D). Thus the connecting map of (6)
is exactly mu, including its agreement with PR780's sign convention.

## 2. A scalar map identifies the entire extension

Let R be the actual degree-eight relation bundle inside Sym8 U O_L(2).
The old cubic relation is a nowhere-zero map O_L(-2)->Sym3 U O_L(1).
Equivalently its local polynomial f has coefficient twist three. Therefore
multiplication by f defines a subbundle

    F = f . (Sym5 U O_L(-1)) subset Sym8 U O_L(2).

The local description R=f^2 Sym2 U + k fg shows R is a subbundle of F.
Twisting (4) by minus one and multiplying by f gives the exact sequence

    0 -> R=P4 O_L(-2) -> F=Sym5 U O_L(-1)
      -> T'=U O_L(1) -> 0.                         (8)

This construction respects the nontrivial quintic-generator transition;
the symbol f . (...) denotes the image bundle, not a chosen global quintic.

For an ambient reference lift d_tilde in E_mu, define

    Lambda(d_tilde) = (tr(m d_tilde)/q)|Q.          (9)

The numerator restricts to tr(nD)=0, so the division is regular. Both m
and d_tilde are sections on reference 2Q, hence (9) is intrinsic and glues.
It has physical twist 2+6-2=6 and cover degree 8+4-4=8, so its coefficient
bundle is Sym8 U O_L(2). Only the two terms of (2) are used.

Locally, for d_tilde=H(D)+qX0, formula (9) is

    Lambda(d_tilde)=Psi(D)+tr(nX0).                 (10)

The H1 here is the first harmonic product operator, not sheaf cohomology.
PR718 puts Psi(D) in f S5, and tr(nX0) lies in R subset F. Thus Lambda
takes values in F.

On the kernel in (6), Lambda is the known bundle isomorphism

    X0 -> tr(nX0): J0(4) -> R.                     (11)

On the quotient, (10) induces the map T->F/R=T'. Its local expression is
(3), up to the factor two of (5). PR724 proves that it is an isomorphism
for every regular cubic/quintic pair. Uniform regularity along L and the
intrinsic definition (9) therefore make it an everywhere invertible,
Gamma-equivariant bundle map. No extension of a generic rational inverse
through unexamined exceptional points is being assumed.

Equations (9)-(11) define a commutative diagram from (6) to (8), with the
left and right arrows isomorphisms. The short-five-lemma proves that the
middle arrow is an isomorphism too. This identifies E_mu with
Sym5 U O_L(-1)=U tensor Sym2 W O_L(-1), and proves (1).

In particular H0(E_mu)=H1(E_mu)=0. The long exact sequence of (6) now gives

    mu: H0(U O_L(1)) -> H1(P4 O_L(-2))

as an isomorphism. Nonzero is a conclusion of this exact diagram, not an
assumption inferred from the one-dimensional equivariant Ext space.

## 3. Physical character and retained square constraints

The source has the actual even character: U and W are center-odd binary
representations and U tensor W=P4 is center-even. Equivalently the matrix
has weight four, which is an allowed physical-even weight in PR780. The
odd cover-linear parameter ell is multiplied by the odd Serre pair in
(5); it must not be mistaken for an odd endomorphism. The target J0(4)
has the same physical-even marking. No claim about the extra Serre
involution is needed or substituted for physical parity.

Now change only the total-weight-sixteen reference input by q^3H(D).
The weight-twenty-four square is unchanged because K12 is unchanged. At
total weight twenty-eight the only possible term modulo q^4 is

    q^3 {A0,D} = q^3 a^4 h tr(n8D) Id = 0.

Terms involving positive q coefficients of K12 are already q^4-divisible;
the q^6 square of the correction also vanishes on 4Q. Higher total matrix
weights are outside this retained constraint. Thus the retained square
and jet conditions admit all four tangent directions, while their faithful
reference fifth-boundary classes vary through the entire P4 target.

This does not show that q^3D with only its homogeneous coefficient preserves
the full actual norm. For an actual correction q^3 D_full, the exact identity
on 4Q is

    n(K+q^3D_full)-n(K)=q^3 a^4h tr(N D_full).

For the fixed nonzero sources, preservation of the full norm is therefore
equivalent to tr(N D_full)=0, not merely tr(n8D4)=0. The higher pieces of N
and D_full, their actual transition compatibility, and whole-cone and
source-divisor realization remain required. Locally the full regular-pair
tangent map supplies trace-orthogonal extensions of a chosen leading
tangent coefficient; this is not a claim that these local extensions glue.

In fact PR781 excludes every nonzero pure B3 variation from the classified
actual completion freedom. Its exact formula is

    Delta B2=-a^2 s_A n8,    Delta B3=-a s_A U1.

Keeping B2 fixed forces s_A=0, since a is nonzero, n8 is nonzero, and the
coefficient sheaves are torsion-free over the integral line. This is a
regular sheaf identity, not inversion of a at its zeros. Then Delta B3=0.
The D5 and independent fourth-lift directions have no weight-sixteen effect
and cannot restore a pure B3 change. Thus none of the nonzero directions
detected by mu is a classified freedom.

A separate necessary source-divisor check gives the same warning for a
pure q^3 change over a fixed third lift: K=aJ4 requires D4=aE4 at its
leading tangent layer, while the twist-four kernel U O_L(-1) has no global
sections. This check does not replace the stronger complete classification.

## 4. Novel comparison and limits

The trace-kernel bundle, quintic evaluation sequence, and PR724's local
first-normal trace isomorphism are prior results. They are not new claims
here. The additional step is the intrinsic trace morphism (9), using the
genuine source-free exact-T0 reference lift, which identifies their
extension with the particular -M1(B3) boundary in PR780. This proves the
nonzero global transgression that neither an Ext dimension nor the local
isomorphism alone identifies.

The older full-homogeneous-normal-matrix note warns that coefficient lifts
are not automatically global actual tangent sections; the present result
retains exactly that distinction. It also does not concern the unrelated
normal-variation trace null-homotopy or promote the old tangent coefficient
at physical twist four from O(-1) to a new acyclicity theorem.

Consequently the B3 trace-kernel dependence cannot be discarded from the
faithful linear formula on the basis of the retained local conditions.
The result neither computes actual beta4, changes its classified
second-symbol quotient, nor proves a new actual completion freedom.
No actual coefficients, points, derivatives, matrices, ranks, selected
source instances, models, scans, or large computations were used.
