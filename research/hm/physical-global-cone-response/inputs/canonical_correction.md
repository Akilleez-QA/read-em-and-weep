# The canonical raw cubic has a nonzero linear lifting correction

## New actual conclusion and normalization limit

Let

    T(a,h)=Psi(a,h,t(a)) in P4,       t(a)=[a zeta_a],

be the CANONICAL actual fixed-probe secondary tensor, before the second-symbol quotient. The actual third gate is zero, but this unquotiented cubic family is NOT zero. It factors uniquely as

    T=beta2 L_can,
    L_can:D5 O_P(A)(-3) -> A O_P(A)(-2),             (1)

and L_can is a NONZERO member of the one-dimensional equivariant Hom space.

This is not a statement that the cubic block of every arbitrary Schur reduction has the same coefficient. The canonical tensor has a fixed actual cyclic/Atiyah probe. A chosen Schur gauge must be compared with it before identifying its source correction with L_can. No numerical invariant scalar is assigned here. The concrete eigenline ratio below depends on the displayed representation frames, physical normalization, and common boundary/trace convention.

The calculation is uniform for an arbitrary C5 stabilizer, using its abstract eigenline inputs a=t^2 and h=Y^4. All A,B,c,lambda,k remain unassigned nonzero symbols. No actual coefficient, matrix, rank, or source instance is selected.

## 1. Why the normal-operator comparison is BEFORE the quotient

The following chain keeps P4 as target throughout.

1. POSITIVE-THIRD-SECONDARY-MULTIPLICATION-TENSOR.md defines Psi(a,h,[x])=[a v] by q0 v=h x in the ACTUAL ambient cohomology module. Both division ambiguities disappear in P4 itself. For x=a zeta_a this is the canonical raw cubic T.
2. POSITIVE-SECONDARY-TENSOR-NORMAL-VARIATION.md Section2 identifies the tensor on the actual first thickening with this ambient Psi exactly: lift x by restricting its ambient representative, and use y=v|Q. No second-symbol correction is introduced.
3. POSITIVE-CUBIC-NORMAL-VARIATION-VANISHES-BY-SERRE-INVOLUTION.md proves zero variation of this FIXED-PROBE tensor in P4 itself. Consequently its midpoint value equals its actual ambient value before quotienting.
4. ACTUAL-THIRD-VALUE-AS-MIDPOINT-DUALIZING-OPERATOR-DEFECT.md Section3 identifies that midpoint value with the obstruction to lifting the SPECIFIED multiplied cone operator aO, up to the one common boundary sign. The chosen divided class is fixed by the operator, not inferred from a normal multiplication equation with a possible kernel. Changing O by an allowed positive cone section does not change the obstruction: such a section is N times a quadratic and lifts at the midpoint.
5. The full-frame Hessian theorem matches the actual midpoint symbol modulo local normal conjugation. ACTUAL-NORMAL-OPERATOR-SQUARE-SHADOW-BY-HARMONIC-TRANSITION.md then computes its actual degree-eight trace shadow: pure transitions are matched exactly, normal centralizers have zero trace shadow, diagonal/root factors have zero harmonic discrepancy, and the remaining regular stabilizers are above the relevant degree. These are equalities or zero contributions to the raw obstruction, not reductions modulo im(beta2).
6. POSITIVE-MIDPOINT-OPERATOR-BOUNDARY-IS-VERTEX-ONLY.md removes the conic through actual global G(4) images. ACTUAL-DEGREE-EIGHT-NORMAL-OPERATOR-QUOTIENT.md identifies the vertex trace quotient with H1(B_Q(4))=P4 through its commuting wedge diagram and cohomology isomorphisms. The only residual sign is the stated trace/wedge convention. The canonical Gram elimination is an exact Cech boundary, and the meromorphic-source theorem is a global meromorphic coboundary.

Therefore the class of aR/nu in the upper P4 quotient is T, up to that fixed common sign, NOT merely some lift of its value modulo beta2. Only AFTER this chain is the third gate obtained by taking the beta2 quotient. There is no hidden A-valued third-lift correction in the comparison.

## 2. Unique global factorization, including the six exceptional fibers

The actual second-symbol sequence is exact as sheaves:

    0 -> A O(-2) --beta2--> P4 O -> I_Sigma(6) -> 0.

Its first map is injective even where its fiber rank is two. ACTUAL-THIRD-BOCKSTEIN-VANISHES-IDENTICALLY.md says the composition of T with the last map is zero. The kernel property gives (1), uniquely as a SHEAF map. In particular L_can is polynomial and linear in a; there is no division by a minor and no pole-removal assumption at Sigma.

Equivariance follows from uniqueness. Moreover

    Hom_G(D5 O(-3),A O(-2))
       =Hom_G(D5,A tensor A)=C,
    A tensor A=1+A+D5.                              (2)

It remains to prove that this particular factor is nonzero. The detecting square and semisimple inputs cannot do that, since their vector cups already vanish before quotienting. The following nondetecting input does.

## 3. Exact actual data for a=t^2, h=Y^4

Use the same divisor-defined global meromorphic g0 and regular target transitions as the square and semisimple calculations. In z=t/s,

    f=A X^2Y+B Y^3z+Ac X^3z^2-Bc XY^2z^3,
    g0=-lambda/(2Ac)(B XY^4z^(-3)+A X^3Y^2z^(-4)).

The exact identity h f_z=m f+n g0 gives

    n=A/(B lambda)[-3Ac^2 X^2z^4-2Ac XYz^2
                      +A Y^2+4Bc^2 Y^2z^5],
    m=Y^2[-3Ac X^2z^2+A XY+2Bc Y^2z^3]/(2Bc z^4). (3)

The restriction isomorphism identifies this with the actual n_h.

The actual socle quotient has

    Q(Y^4)=e[-(Ac/B)X^2t^2+(A/B)XYs^2]/2,
    Q(X^2Y^2)=-(e/2)XYst.

The canonical inverse equation consequently has the unique solution

    u=(4kA/B)X^2Y^2t^2,
    Gamma_x=(4kA/B)X^2Y^2z^2+4kY^4z^3,
    Gamma_y=(4kA/B)X^2Y^2.                         (4)

Here the y coordinate is w=-s/t, so a_y=1. The inhomogeneous Gamma frame correction is included in(4).

In this particular source frame the ACTUAL Gram primitive is zero. This is proved, not chosen: the full target changes are

    tau(p_x,n_x)=-20c^2z^3,
    tau(p_y,n_y)=2A(2Aw^5-5Bc^2)/(B^2c^2),          (5)

both regular on their affine charts. Thus eta0=0 gives regular target primitives with the required actual cocycle. Uniqueness from H0(O(-2))=0 identifies it with the pinned Gram lift. The primitive was nonzero for both earlier detecting calculations; no general zero-primitive rule is being used.

## 4. Full cochain principal parts and the raw P4 value

Substitute (3)-(5) into the ENTIRE pinned vector formula. The companion verifier proves that the only principal parts are

    R_x=(k lambda/(3Bc))XYz^(-2)
           +(k lambda/(10Bc^2))Y^2z^(-4),
    R_y=-(4Ak lambda/(3B^2c^2))X^2w^(-1)
           +(4k lambda/(15Bc^2))Y^2w^(-2).        (6)

The source m, all transition products, derivative term, Gamma, and actual Gram primitive are retained. The source/frame theorem identifies (6) with the actual cohomology representative, divided by the fixed nonzero physical nu.

After cup by a, the XY term at x is regular. Remove the remaining x pole by the global V O(-4) meromorphic section with x coefficient (k lambda/(10Bc^2))Y^2z^(-2). The upper class is then represented solely at y by

    U_y=-(4Ak lambda/(3B^2c^2))X^2w^(-1)
             +(k lambda/(6Bc^2))Y^2w^(-2).        (7)

Its character is4. To project to the raw P4, use the ACTUAL P4-dual character6 line

    i^t c=Y^2t^2-(2A/B)X^2st,
    (i^t c)_y=Y^2+(2A/B)X^2w.                    (8)

This line is independently identified by product-apolar orthogonality to Q(XY^3), as in the semisimple audit. It annihilates the upper connecting D5. It is NOT the character2 annihilator of the square second-symbol image; that final quotient has already been proved zero.

With the unnormalized positive quadratic pairing, the Serre residue is

    Res_y tau(U_y,(i^t c)_y)/nu
          =-4Ak lambda/(B^2c^2 nu) != 0.         (9)

Every factor is nonzero without assigning any parameter value. Hence the actual raw cubic T is nonzero, although it lies in im(beta2). By uniqueness in(1), L_can is nonzero.

## 5. Relative eigenline comparison, not an invariant scalar assignment

For a=t^2, h=Y^4, equivariance forces L_can(a,h) into the weight-zero line of A, represented by st. One can compare its scale with the actual second symbol in the SAME frames.

Use the published convention beta2_a(b)=-k j_*(b a D_a e_gen), where e_gen is the actual quintic-extension class. The natural O(-8) line operator on a coefficient p is

    D_a p=2a p_z+8a_z p.

This is the coefficient-line operator in the Atiyah-quintic theorem, not the cover-Euler expression for p inside the cone connection. For a=t^2 and b=st, the x representative is regular; the y upper principal part is

    V_y=-(2k lambda/(Bc^2))X^2w^(-1)
                +(2k lambda/(Ac^2))Y^2w^(-2).    (10)

Its pairing with(8) is 8k lambda/(Bc^2). Thus the ratio of the DISPLAYED raw representative aR/nu to the DISPLAYED second-symbol convention on this eigenline is

    -A/(2Bnu).                                    (11)

The canonical ambient tensor may carry the common trace/boundary sign from Section1. Furthermore rescaling the abstract eigenvectors or the physical equation changes the presentation of(11). It is therefore not a numerical invariant scalar. The invariant assertion required for the lifting correction is that (11) is NONZERO.

For an intrinsic description of the Hom line in(2), let H=(f,f)_(1,1), using first transvectants in the positive and negative variables. The map h -> (H,h)_4 in the positive variables is a nonzero G-isomorphism D5_positive -> Sym^4 W. Composing with the negative second transvectant (a,-)_2 spans (2). Nonvanishing follows directly on the same ABSTRACT eigenline: its image is a nonzero multiple of st. This supplies a tensor description of the correction line, not an extra normalization of L_can.

## 6. Uniform image theorem for the canonical raw cubic

There is a stronger coefficient-free consequence of the NONZERO scalar. Give A its nondegenerate invariant symmetric form. The unique representation identification

    D5 = Sym^2_0 A

identifies h, up to a fixed nonzero scalar, with a trace-free self-adjoint endomorphism S_h of A. Equation(2) then gives

    L_can(a,h)=gamma S_h(a),       gamma != 0.       (12)

This uses the symmetric, not alternating, part of A tensor A: Sym^2 A=1+D5 and wedge^2 A=A. The possible common sign in Section1 does not affect the argument.

For EVERY nonzero a, the map h -> S_h(a) is onto A, including isotropic a. To prove this, let a covector ell annihilate every S_h(a), and identify ell with a vector using the invariant metric. The symmetric tensor sym(a tensor ell) annihilates the trace-free symmetric endomorphisms, hence is proportional to the metric. But its rank is at most two, whereas the nonzero metric has rank three. Its scalar of proportionality is therefore zero. Finally sym(a tensor ell)=0 implies ell=0: equivalently the product of the two corresponding linear forms is zero in the symmetric algebra, which is an integral domain. No positive-definiteness assumption is used.

Consequently L_can is fiberwise onto at every projective direction. From T=beta2 L_can one obtains

    image(T_a)=image(beta2_a) for EVERY a != 0.     (13)

The canonical raw cubic thus has rank three off Sigma and rank two at each of its six axes. These are consequences of the actual factorization and an intrinsic universal rank proof, not source-instance rank evaluations. Although the third quotient is identically zero, its canonical raw lift uniformly fills the entire previous image. In a compatible reduction the required source correction cannot be silently set to zero.

## 7. Consequence for the next obstruction, and its exact limit

The canonical third lifting correction is genuinely nonzero and must be retained when a fixed reduction is chosen compatibly with the canonical raw cubic. In such a reduction, the fourth representative has the form B4|D5-B3|A L_can. In an arbitrary Schur reduction its L must first be transported from the canonical one; it need not have the same scalar and may be modified by source gauges.

No fourth Bockstein coefficient is evaluated here. Nonzero L_can does not imply a nonzero composite B3|A L_can or a nonzero fourth quotient. See FOURTH-BOCKSTEIN-AFTER-ACTUAL-THIRD-VANISHING.md for the four-channel remaining problem.

## Reproduction

Run python verify_canonical_raw_cubic_nonzero_correction.py. It checks the exact relation, canonical inverse, both regular Gram transforms, complete vector cochain and its four principal coefficients, the raw P4 residue, the actual second-symbol relative residue, and the nonzero Clebsch line. All parameters are formal. The unquotiented geometric comparison is the explicit chain in Section1, not a conclusion from the symbolic expansion alone.
