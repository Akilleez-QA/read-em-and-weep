# A rank-two residual kernel cannot be isotropic

## Theorem

Let P=P(Sym^2 W), let E=S6*, and let

    m: W tensor E -> K8

be the actual equivariant residual multiplication map. The canonical alternating forms on the rank-two factors W and E give the source a nondegenerate symmetric O_P(-5)-valued form

    q(w tensor e, w' tensor e') = (w wedge w')(e wedge e').

If m has generic rank two and N=ker(m), then q restricted to N is generically NONDEGENERATE. In particular the generic kernel is not a maximal isotropic plane.

This does NOT exclude a nondegenerate rank-two kernel, assert the actual map is orthogonal, or establish rank four. The argument uses no selected coefficients, matrices, or fiber evaluations, and does not require choosing among the seven possible C_lin splittings.

## 1. Canonical form and the two generic rulings

The representation W has determinant one. The rank-two bundle E=S6* has determinant O(-5). The product of their alternating pairings is symmetric and nondegenerate, valued in O(-5). It is G-equivariant, since the determinant linearizations are the canonical ones; G is perfect and has no characters with which to alter them.

Over the function field of P, the isotropic quadric in P(W tensor E) is the Segre quadric P(W) x P(E). Its maximal isotropic two-dimensional vector subspaces are exactly

    ell_W tensor E,       or       W tensor ell_E,                (1)

where ell_W or ell_E is a one-dimensional subspace of the respective factor. This follows directly by viewing the quadratic equation as the determinant of a two-by-two tensor: a projective line of rank-one tensors has one factor constant. The given tensor-product G-action preserves each ruling.

The kernel N is saturated in W tensor E, since its quotient is the actual torsion-free image of m. It is locally free on the smooth surface, by the depth lemma applied to that torsion-free quotient.

## 2. Saturation extends the ruling through codimension two

Take the saturated intersection of the generic line in (1) with its rank-two bundle, either W tensor O or E. Call it L. A saturated rank-one subsheaf of a locally free rank-two bundle on a smooth surface is reflexive by the depth lemma, hence is a line bundle. In either case L and its inclusion are G-equivariant, since the generic line is determined by the G-equivariant N and its ruling.

In the first ruling L is a center-odd equivariant line bundle contained in W tensor O. No such line bundle exists on P: the center acts trivially on P and on the standard O(1), and every linearization differs from the standard one by a character of the perfect group G. Thus the first ruling is impossible.

In the second ruling write L=O(-a) with its unique G-linearization. The subsheaf W tensor L is saturated in W tensor E because E/L is torsion-free. It has the same generic fiber as N. Uniqueness of saturation therefore gives the equality of actual sheaves

    N = W tensor O(-a).                                             (2)

No assumption of a pointwise subbundle has been made. The quotient can, and necessarily does, retain a finite degeneracy scheme.

## 3. Exact zero scheme and the actual image

The saturated inclusion O(-a)->E has quotient a torsion-free rank-one sheaf, so

    0 -> O(-a) -> E -> I_Z(a-5) -> 0,                              (3)

where Z is a finite scheme. Its length is fixed by c1(E)=-5,c2(E)=15:

    length(Z)=a^2-5a+15.                                            (4)

This is always positive. In particular (3) cannot be replaced by a line-subbundle quotient sequence with a locally free last term.

Taking the actual quotient of the residual source by (2) gives

    I=im(m)=W tensor I_Z(a-5),
    I**=W tensor O(a-5),
    length(I**/I)=2(a^2-5a+15).                                    (5)

Because K8 is locally free, every homomorphism I->K8 extends uniquely to I**->K8. Indeed it extends across the finite set Z by applying Hartogs extension to the entries of a morphism between locally free sheaves on the smooth surface. The resulting map is nonzero and generically injective when m has generic rank two.

## 4. Negative-twist vanishing of the target

The established residual target is a subbundle

    K8 -> C_quad=nu_*eta*(C_lin(1)).

On the ordered-root model Z_root=P1 x P1 of the universal root scheme, eta is projection to the first root and nu*O_P(t)=O(t,t). Therefore, for every t<0, the projection formula gives

    H0(P,C_quad(t))
      = H0(P1 x P1, pr1*(C_lin(1+t)) tensor pr2*O(t))
      = 0.                                                         (6)

The second-root degree is negative. No splitting assumption or cohomology estimate for C_lin is needed. Thus H0(K8(t))=0 for all t<0.

The nonzero extension I**=W O(a-5)->K8 in Section 3 now forces

    a <= 5.                                                        (7)

This extension step is essential: simply forgetting the finite zero scheme in (3) would not justify (7).

## 5. The source and equivariance contradict a<=5

The established root-duality identity is

    E=S6*=nu_*eta*O(-6) tensor O_P(1).

Consequently

    H0(P,E(a)) = H0(P1 x P1,O(a-5,a+1)).                             (8)

It is zero for a<5. For a=5 it is Sym^6 W. The inclusion O(-a)->E in (3) is equivariant, so its nonzero section lies in H0(E(a))^G. But

    Sym^6 W = V directsum P4

has no trivial constituent. Thus a=5 is impossible too. Equations (7) and (8) exclude the second ruling, completing the exclusion of isotropic rank-two N.

For comparison, without the target-extension obstruction, the source-only invariant section gate first allows a=8: the spaces for a=5,6,7 have no invariant, whereas at a=8 the invariant multiplicity is one. This source-only observation is strictly weaker than the complete contradiction above.

## 6. Why the restricted form has rank two, not merely nonzero

The restricted symmetric morphism is

    q_N: N -> N* tensor O(-5).

If it had generic rank one, its saturated radical would be a G-equivariant rank-one torsion-free sheaf with central character -1. Its double dual would again be a forbidden center-odd equivariant line bundle on P. Generic rank zero was excluded in Sections 1-5. Therefore q_N has generic rank two.

Writing c1(N)=-d, its determinant is consequently a nonzero invariant section of O(2d-10). The previously established finite Chern gates force even d>=6, so this divisor has positive degree congruent to 2 modulo 4. This records a necessary discriminant divisor, not its actual equation or a guarantee of any particular vanishing locus.

## Dependencies and checks

- RESIDUAL-SMOOTHING-NONVANISHING-AND-EVEN-RANK.md: actual source W tensor S6*, root-duality identity, actual K8 inclusion, and rank-two-or-four alternative.
- RANK-TWO-RESIDUAL-KERNEL-FINITE-CHERN-GATES.md: kernel local freeness and central-line obstruction; the present proof restates the required arguments.
- verify_no_isotropic_residual_kernel.py independently checks the universal character invariant multiplicities and Chern identities. It does not evaluate an actual residual map.

No conclusion about the separate primary cubic problem is used.
