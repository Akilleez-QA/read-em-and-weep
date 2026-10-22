# The actual cubic probe has zero first-normal variation

## Result

Assume the geometric Serre double-cover theorem in NORMAL-QUADRATIC-NONZERO-BY-SERRE-RESIDUE-DOUBLE-COVER.md. Then the exact linear map L from the one-dimensional first-normal extension direction to the two cubic channels, constructed in POSITIVE-SECONDARY-TENSOR-NORMAL-VARIATION.md with the ACTUAL quadratic probe t(a) held fixed, is ZERO.

Its kernel is the entire one-dimensional direction T. In fact the unquotiented variation of Psi(a,h,t(a)) is zero in P=H1(B_Q(4))_+, before dividing by the actual second-symbol image.

This is not vanishing of the actual third Bockstein. Its unknown absolute value is constant along the auxiliary first-normal torsor when this actual probe is held fixed. Consequently injectivity of this particular extension-to-cubic map cannot prove the desired actual nonvanishing. The symmetry determines the kernel, not the constant value.

## 1. The geometric involution of the affine normal line

Let phi scale the negative coordinate block by mu with mu^2=-1. The companion Serre theorem proves that phi preserves the actual stack zero scheme and that there is a G-equivariant cone isomorphism phi^*F_Q -> F_Q. Use this marking to act on the first-normal torsor. Denote the resulting affine transformation by J.

The two distinct extendable points are furnished by F and phi^*F. They are exchanged: phi^2 is physical inversion, already a central element of G. For precision, H0(B_Q)^G=0 follows from the ambient restriction sequence, stability H0(B)=0, and H1(B(-2))^G=0. Hence End_G(F_Q)=C. The twice-composed determinant-preserving cone marking differs from the central-inversion marking by a scalar of square one, namely +1 or -1, and this scalar extends on every bundle thickening. Thus possible marking differences do not change a marked deformation class. If s=0 is the point furnished by F and s=s_*!=0 is the other point, then

    J(s)=s_*-s.                                           (1)

One can also derive (1) solely from affineness and exchange of the two distinct points. It is not an arbitrary choice of origin for the actual operation.

## 2. The induced action on the target P is +1

Use the stack notation from the companion theorem:

    0 -> O_X --sigma--> G -> I_Z(2) -> 0,
    0 -> G(2) -> B_X(4) -> I_Z^2(6) -> 0.                 (2)

The intrinsic action on the two Serre residue components has weights mu^{-2} and mu^2, both -1 for this phi. Therefore an isomorphism phi^*G -> G has subline/quotient scaling ratio -1. It sends the invariant nilpotent adjoint N to -N. This ratio is unaffected by multiplying the isomorphism by a scalar to adjust its determinant.

The lower-adjoint quotient in (2), locally det(sigma,T sigma) with its determinant normalization, transforms by the inverse subline/quotient ratio. Thus identification of its target with the intrinsically linearized I_Z^2(6) contributes a scalar -1.

It remains to compute the intrinsic phi action on H1(I_Z^2(6))_+=P4. The established positive vertex square filtration has only one piece producing this cohomology: the cover-degree-eight quotient, whose relation sequence after twist6 is

    0 -> P4 O_L(-2) -> Sym^8 Wprime O_L(2)
      -> Q4(6) -> 0.

The extra P4 is H1(P4 O_L(-2)). On a negative chart, a cover-degree-eight term in physical twist6 has block character

    mu^(6-8/2)=mu^2=-1.                                 (3)

The base coordinate v/u is fixed. Hence the entire corresponding quotient and its cohomological P4 carry this character. All lower pieces have zero degree-one contribution to the square-shadow obstruction; this is exactly the previously proved square-filtration identification, not a choice of a generator lift. The homogeneous actual zero scheme permits use of this torus grading for the actual quotient, not just its initial ideal.

Combining the intrinsic -1 in (3) with the adjoint-quotient factor -1 gives

    rho_P = +identity on P=H1(B_Q(4))_+.                  (4)

The identification of these two cohomology spaces uses BOTH H1(G(2))=0 and H2(G(2))=0 from the established primary square-sequence calculation; the positive obstruction P4 is the same P4 throughout.

## 3. The actual quadratic probe is ODD, despite degree two

Recall the actual orbit-tangent identification

    zeta_a=k At_F(D_a),   k!=0,
    t(a)=[a zeta_a|Q] in C=H1(B_Q(2))_+.

Here D_a belongs to the negative-block sl(W), using the fixed G-equivariant identification A=Sym^2 W -> sl(W). Its restriction is tangent to Q, and restriction of the Atiyah class gives

    zeta_a|Q=k At_(F_Q)(D_a).                            (5)

The coordinate transformation phi is scalar on W and therefore COMMUTES with every D_a. Naturality of the Atiyah class under the cone bundle isomorphism implies that (5), for each fixed a, has eigenvalue +1 under the induced action on H1(B_Q).

On the other hand the polynomial a, a negative quadratic, has eigenvalue mu^2=-1. Multiplication is natural, so

    rho_C(t(a))=-t(a).                                  (6)

This is the essential distinction: the fixed coefficient k and the fixed assignment a -> D_a in (5) are held as the actual probe. The assignment is G-equivariant, not equivariant for scalar block multiplication with a treated as a polynomial. The word 'quadratic' describes dependence on a, not the cone automorphism character of its value.

The actual probe for the OTHER ambient extension is not silently identified with this fixed probe. With compatible invariant xi normalization, its cyclic scalar changes sign under the symmetry, consistently with a xi=q zeta_a and naturality. The present argument does not require choosing that normalization: it uses only the fixed probe in (5)-(6). In particular, transforming the separately normalized actual probes for two ambient bundles is a different comparison from evaluating the affine family at this one fixed probe.

## 4. Naturality forces the exact variation to vanish

The secondary operation exists intrinsically for every first-normal extension e, and is natural under pullback and the fixed cone isomorphism:

    rho_P Psi_e(a,h,x)
      =Psi_(J e)(rho_a a, rho_h h, rho_C x).              (7)

Here h in D5 is a positive quadratic, so rho_h=+1, while rho_a=-1. Apply (4) and (6) to (7):

    Psi_e(a,h,t(a))=Psi_(J e)(-a,h,-t(a))
                  =Psi_(J e)(a,h,t(a)).                 (8)

The affine-variation theorem proves that the left side, as a function of e, is affine even before quotienting by im beta2. Write it as V0+s V1. Equations (1) and (8) give

    V0+s V1=V0+(s_*-s)V1.

Since the ground field has characteristic zero, V1=0. Therefore the actual unquotiented probe has zero variation. Passing to the fixed actual second-symbol quotient proves L=0 and ker L=T. This quotient is preserved: rho_P is the identity and therefore preserves im beta2_a for every a individually. Moreover beta2 is quadratic in a, so im beta2_{-a}=im beta2_a. No equality between separately normalized second-symbol scalars for the two ambient bundles is needed.

More generally the variation of Psi(a,h,x) vanishes for every x in the -1 eigenspace of C. No assertion about the +1 eigenspace is needed here.

## Scope

This settles the kernel of the specific first-normal-to-cubic variation map. It neither computes its constant value nor proves any positive third Bockstein vanishing or nonvanishing. The remaining task is an absolute secondary multiplication calculation, or a genuinely different geometric exclusion. This result also explains why exchange of two ambient extensions and odd total cubic degree do not by themselves locate the actual cubic gate away from zero.

Inputs: the Serre double-cover theorem; the actual Atiyah-quintic second-obstruction theorem; the weighted-stack square sequence; the cover-degree-eight square-filtration P4 calculation; the intrinsic secondary tensor and its exact affine variation. No actual HM coefficients, matrices or ranks are evaluated.
