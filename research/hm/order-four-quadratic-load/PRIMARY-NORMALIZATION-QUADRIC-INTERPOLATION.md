# Quadric interpolation on the primary modular normalization

Work over C. This is a new consequence of the primary-surface dictionary, not a claim that the primary ambient space or its bundle equals the evaluation ambient space in the fifty-point adjoint boundary.

## Pinned inputs and notation

PR570, e5e55594ef2b99cefb81c4c02b22cb45e1ff0025, identifies the primary line-bearing surface S in P(A) with the degree-fifteen modular surface. Its normalization X is smooth S(5); it is an isomorphism away from thirty ordinary transverse double points of S. Put H=nu*O_S(1), K_X=3F, H=I+2F, and C=sum of the twenty-five torsion sections=5I. Thus I^2=-5, I.F=5, F^2=0, H^2=15, H.C=25. Each torsion section L has I.L=-1 and F.L=1. H is ample, since nu is finite. BHM Section 4.4 Lemma 11, printed page 62 (PDF page 69), explicitly computes h0(I+qF)=5q-5 and h1=0 for q>=2. Taking q=2 gives h0(H)=5 and h1(H)=0. Section 4.5 then explicitly identifies H0(I+2F)=V* before Proposition 9; this is not inferred merely from having a map to P4. The elliptic surface has twelve I5 fibers and hence topological Euler characteristic 60; Noether's formula gives chi(O_X)=5.

PR571, 25afc8bfce079492b6b06bb6f52489f8d481c2aa, supplies the six residual quintics and their pullback line bundle O_X(10F). Their image is a rational degree-ten curve. Current PR1 discussion was read through comment 6314078481 before this deduction.

## 1. The smooth quadric section and its elliptic projection

A general ambient quadric avoids the thirty singular points and meets S and C transversely. Its pullback Y is a smooth connected curve in |2H|. Bertini applies off the finite exceptional image; connectedness follows because 2H is ample. Hence Y is integral and is identified with S intersect Q.

Adjunction gives

 degree_H(Y)=30,
 2g(Y)-2=(2H).(2H+3F)=60+30=90,
 g(Y)=46.

The elliptic fibration restricts to a finite map pi_Y:Y -> P1 of degree Y.F=10. Riemann-Hurwitz gives ramification divisor of degree 110. The marked divisor Z=Y intersect C consists of fifty reduced points, two on every torsion section. The residual quintic map on Y factors through pi_Y and its normalization map has degree ten; its pulled-back polarization has degree 100. No simplicity of the ramification or distinctness of the fifty elliptic base values is asserted.

## 2. Exact 45-to-50 interpolation on the normalization

Set A=3H-C=-2I+6F and A-Y=H-C=-4I+2F. Both have negative intersection with the nef fiber F, so neither has sections.

Serre duality gives h2(A)=h0(2I-3F)=0: the latter divisor has H-degree -5. For A-Y, the dual divisor is 4I+F. This divisor intersects each torsion section in -3. If it were effective, it would therefore contain all twenty-five torsion sections as components. Subtracting C=5I would leave an effective divisor of class -I+F, whose intersection with the nef F is -5, a contradiction. Thus h2(A-Y)=0 as well.

Surface Riemann-Roch gives

 chi(A)=5+((-140)-(-30))/2=-50,
 chi(A-Y)=5+((-160)-(-60))/2=-45.

Consequently h^bullet(A)=(0,50,0) and h^bullet(A-Y)=(0,45,0). Restricting to Y gives the canonical exact sequence

 0 -> H0(Y,L) -> H1(X,H-C) --q--> H1(X,3H-C)
   -> H1(Y,L) -> 0,                         (1)

where L=O_Y(3H-Z), of degree 40. Thus (1) is an actual 45-to-50 multiplication map, with kernel h0(L) and cokernel dimension 5+h0(L). This calculation does not assert that this multiplication is injective.

## 3. Fifteen additional normalized cubic sections

The divisor N=H-F=I+F is nef: on each torsion section its degree is zero, and on any other integral curve the degree of I=C/5 is nonnegative, as is that of F. Since N^2=5, it is big. Kawamata-Viehweg vanishing applied to 3H=K_X+3N therefore gives H^i(X,3H)=0 for i>0. Riemann-Roch gives h0(X,3H)=50.

For H itself, h2(H)=h0(-I+F)=0 by fiber degree, and chi(H)=5. The input h0(H)=5 therefore gives h1(H)=0. The sequence 0 -> O_X(H) --q--> O_X(3H) -> O_Y(3H) -> 0 now gives

 h0(Y,3H)=45,       h1(Y,3H)=0.              (2)

Reference for the vanishing theorem: Osamu Fujino, Kawamata-Viehweg vanishing theorem, Theorem 0.1, https://www.math.kyoto-u.ac.jp/~fujino/kawamata--viehweg2.pdf . Only its integral nef-and-big, smooth-projective case is used.

If cubic restriction V=H0(Q,O_Q(3)) -> H0(Z,O_Z(3)) is injective for this configuration, then dim V=30 and it injects into W=H0(Y,O_Y(3H)), of dimension45. Put E=H0(Z,O_Z(3)), of dimension50, and J=E/V, of dimension20. The exact evaluation sequence on Y and (2) give

 0 -> H0(Y,L) -> W/V -> J -> H1(Y,L) -> 0.   (3)

In particular 0<=h0(Y,L)<=15. The middle fifteen-dimensional term is genuine: it consists of normalized curve cubic sections modulo ambient quadric cubics. Thus the twenty-dimensional cubic interpolation defect has an image of dimension 15-h0(L), with quotient dimension 5+h0(L). It must not be identified with a direct-sum decomposition or with a nondegenerate adjoint lift boundary.

## Scope and missing bridge

Equations (1) and (2), and the genus/projection consequences, concern the exact primary normalization and its torsion sections. Equation (3) additionally assumes cubic evaluation injectivity for its fifty-point section. The configuration identification is supplied by the exact additional dictionary below, not by symmetry alone. Equation (3) therefore applies to the actual cubic interpolation source after transporting coordinates. Nevertheless, it describes the source, not the bundle-dependent boundary map into U H1(F_Q(2)); a compatibility theorem for that lift is still required. Neither boundary nonvanishing nor full Q4 is claimed.

No selected coefficients, matrices, ranks, scans, or experiments were used. All dimensions above follow from the displayed intersection calculations, vanishing, and exact sequences.


## Exact configuration dictionary: evaluation C versus primary C

ADHPR, Syzygies of abelian and bielliptic surfaces in P4, Section3, printed page9 (PDF page8), defines the normalized HM bundle on P(V0), identifies its evaluation-degeneracy configuration with the twenty-five translates of L00=P1-minus, and identifies its determinant quintics with the full Heisenberg-invariant quintic space. Its Section1 fixes the shift, diagonal and reversal coordinate conventions. Source: https://arxiv.org/pdf/alg-geom/9606013 .

PR573 at 6c2dbd48edea0577acf063a60e1edbbbe92ced5c, Section2, fixes precisely the same starting line x0=x1+x4=x2+x3=0, shift and diagonal generators in the primary coordinate copy. The primitive Galois or dual changes replace generators by primitive powers or inverses and preserve this subgroup and starting line. Sending the named coordinate basis of one space to that of the other therefore identifies the reduced unions of their twenty-five translates. This is an ordinary projective coordinate-copy isomorphism of configurations, not an assertion that the differing linear representations are equivariantly isomorphic.

Thus the actual evaluation C and primary C have the same embedded configuration under this specified coordinate transport. Quadrics, cubic restriction maps and their generic-injectivity open transport with it. The source filtration (3) is accordingly available on the actual common good open. This does not transport the primary evaluation bundle into the HM adjoint bundle or supply the missing twenty-boundary compatibility.
