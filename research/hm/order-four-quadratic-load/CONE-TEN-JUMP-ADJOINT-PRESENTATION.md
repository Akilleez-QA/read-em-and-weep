# Ten reduced jump corrections in the cone adjoint presentation

## Scope and inputs

Use the general rank-four cone Q and one small resolution pi:Y->Q, p:Y->P1 from RANK-FOUR-CONE-RULING-GATE.md. Write H=pi^*O_Q(1), T=p_*O_Y(H)=O+O(1)^2, J=p_*pi^*(F_Q(2)). The actual primary-good open gives H0(J)=0; J has rank5 and degree -10. The twist-four adjoint pushforward E has rank30 and degree -30. Its actual multiplication presentation is

    0 -> M -> Sym^2(J) tensor T -> E -> 0,
    rank M=15, deg M=-120.

Every ruling plane is either generic Steiner or divisor-stratum type, with exactly ten distinct latter planes. The corrected count uses Boralevi Proposition4.7, printed pp18–19, https://arxiv.org/pdf/math/0602002: the divisor meets a Grassmannian line in degree five, hence has Plücker class5H; the ruling conic has Plücker degree two. It is not a divisor of ambient projective degree five.

## 1. The relative evaluation kernel

Let E0=pi^*(F_Q(2)). Fiberwise global generation gives a bundle sequence

    0 -> K -> p^*J -> E0 -> 0.

On a generic plane, K=3O(-1). On a divisor-stratum plane, E0 has resolution O(-2)->D=O(1)+2O. Evaluation of D has kernel Omega^1(1), so

    0 -> Omega^1(1) -> K_P -> O(-2) -> 0.

This splits because Ext^1(O(-2),Omega^1(1))=H1(Omega^1(3))=0, as follows from the Euler sequence. Therefore

    K_P=Omega^1(1)+O(-2),
    K_P(1)=Omega^1(2)+O(-1).

For both plane types K_P(1) has h0=3 and higher cohomology zero. Hence A=p_*(K tensor O_Y(H)) is a rank-three vector bundle with higher direct images zero. Pushing evaluation twisted by H gives

    0 -> A -> J tensor T -> p_*pi^*(F_Q(3)) -> 0.

The last pushforward has no higher direct images, from the two plane resolutions. Its Euler characteristic is chi(F_Q(3))=chi(F(3))-chi(F(1))=2-(-10)=12. Also chi(J tensor T)=15-20=-5. Thus chi(A)=-17, and deg A=-20.

## 2. The wedge term and its jumping cohomology

Define L=(wedge^2 K) tensor O_Y(H), not wedge^2(K tensor O_Y(H)). On generic planes L_P=3O(-1), which is acyclic. On a divisor-stratum plane,

    L_P = O + Omega^1,
    h0(L_P)=h1(L_P)=1, h2(L_P)=0.

The ordinary direct image p_*L is zero: it is torsion-free on the smooth integral base because L is a vector bundle on the flat integral total space, and its generic rank is zero. One must not replace it by the one-dimensional H0 of the special fiber; H0 base change fails there. The only nonzero possible higher direct image is R1p_*L, a torsion sheaf supported at the ten jump points. R2 vanishes by fiberwise H2=0. At each jump the R1 fiber is nonzero by cohomology/base change (or the top-cohomology base-change theorem with R2=0).

## 3. Exact length-one corrections

The symmetric-square complex of evaluation, twisted by H, is

    0 -> L -> K tensor p^*J tensor O_Y(H)
      -> Sym^2(p^*J) tensor O_Y(H)
      -> pi^*(B_Q(4)) -> 0.

Pushing its two short exact pieces, using the already proved higher-direct-image vanishings, gives

    0 -> A tensor J -> M -> R1p_*L -> 0.

The first two terms are bundles of rank15. Their degrees are

    deg(A tensor J)=5(-20)+3(-10)=-130,
    deg M=-120.

The torsion quotient therefore has total length ten. Its support includes every one of the ten distinct jump points, so each local length is exactly one. Consequently

    0 -> A tensor J -> M -> direct_sum_(j=1)^10 k(t_j) -> 0.

The one-dimensional quotients have no chosen trivializations. This reduced-length conclusion is deduced from total degree and support, not assumed from a fiber rank or a generic local matrix model.

## 4. The actual 115-to-105 gate

Because A embeds in J tensor T and every summand of J is negative, every summand of A has degree at most zero. Thus every summand of A tensor J is strictly negative. It follows that H0(A tensor J)=0 and h1(A tensor J)=115. The earlier multiplication source V=Sym^2 J tensor T has H0=0 and h1=105; its subbundle M has H0=0 and h1=105. The jump sequence yields

    0 -> direct_sum_(j=1)^10 H0(k(t_j))
      -> H1(A tensor J) -> H1(M) -> 0.

The actual composed map

    H1(A tensor J) -> H1(M) -> H1(V)

has source dimension115 and target dimension105. Its kernel contains the canonical ten-dimensional subspace supplied by the jump boundaries, and

    H0(Q,B_Q(4))
      = ker[H1(A tensor J)->H1(V)] / (canonical jump subspace).

Hence twist-four cone vanishing is exactly the assertion that this kernel is no larger than the canonical ten-dimensional one. No maximal-rank assertion is made. The result identifies the actual correction maps and their lengths without a coefficient sample, experiment, or generic-balance assumption on A or J.
