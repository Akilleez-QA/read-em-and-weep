# Structural nonvanishing of the paired cubic descent obstruction

Status: independently mathematically reviewed (PASS); see REVIEW.md. Not formally checked. Work over C. This proof uses universal character support, the free Heisenberg orbit, and intrinsic maps. It evaluates no selected source coefficient, point, derivative value, matrix or numerical rank.

## 1. Dependencies and conclusion

Pinned repository inputs:

- PR610 at e4898406ed2552dd40e9695f9fda3d9f1d270301: for a direction G, ambient cubic restriction rho':P=H0(P4,O(3))->F_Z'=H0(O_Z'(3)) onto the other twenty-five centers is surjective with kernel S=H0(I_Z(3)). The group D=<g,h>, with g L_i=zeta^i L_i and h L_i=zeta^(i^2)L_i, acts freely transitively on Z'.
- PR616 at cf7a16cff86cf6cd7ee982b5fa6c309835d25eac: T_Z is the direct sum of center tangent spaces and has no U-invariant vectors. The normalization obstruction is b_N(v)(s)=[(ds_z(v_z))]. For each nontrivial U-character chi trivial on G, the normalization target has h-weights1,4, whereas the descent target has weights2,3. The local descent quotient is J_sigma=Hom(K_sigma,Q_sigma), with simultaneous singular cubic line K_sigma. At the normalized pair (0,1)/(4,3), its cubic support is a x_1^2 x_4+b x_3^2 x_0 with a,b nonzero and unevaluated.
- PR618 at 28f9ad6d73a557935366a9e9398a3ffcbc815c5d: normalization has rank48, ker b_N and J_nt each have dimension48.
- PR620 at 17f7f38695fa00a27d586191a60562c3a5ebba59, the Hessian-free opposite-edge descent lemma: on ker b_N, a lifted cubic s+epsilon t_s satisfies b_J(v)_sigma(s)=ell_sigma(t_s), up to a uniform sign, where ell_sigma is the paired exceptional first-jet difference. All direct mixed Hessian terms vanish for s in K_sigma.
- PR619 at 07aacb6c5024f0f7bdee23e2c0d8506388c7d245, the nonsquare Galois pairing theorem: the two descent channels vanish together. Consequently b_J:ker b_N->J_nt is either zero or an isomorphism.
- PR615 at 24bc9b741c287f8ac207bd9df4de4c07c50bea2f: embedded tangent dimension is99+dim ker b.

We prove b_J is nonzero, hence an isomorphism. Thus b has rank96, ker b=0 and the embedded tangent dimension is exactly99. This is a first-order assertion about the canonical cubic image, not the original full-adjoint or prescribed-source problem.

## 2. Extending the paired jet functional equivariantly

Fix G and the normalized paired marks sigma=(0,1)/(4,3). The two homogeneous exceptional derivative coefficient functionals on ambient cubics P are represented by the distinct tensor lines L_0^2 L_1 and L_4^2 L_3. They have the same D-character (1,1). The central identification of the two value fibers specifies a nonzero multiple of each, whose difference

    ell:P -> Q_sigma

restricts to the intrinsic paired first-jet functional on cubics vanishing at both centers. This extension is D-equivariant: its source character is precisely the section character dual to (1,1), equal to the character of Q_sigma. It is nonzero, since the two tensor monomials are linearly independent before passage to S*. Their difference annihilates S because every section in S descends to the cubic image. No coefficient ratio is selected or calculated.

By surjectivity and ker rho'=S, there is a unique nonzero D-equivariant map

    alpha:F_Z' -> Q_sigma,       ell=alpha rho'.             (1)

Write alpha_z for its restriction to the one-dimensional fiber O(3)_z. Every alpha_z is nonzero. Indeed D acts transitively on Z'; equivariance transports a zero component to all components, which would imply alpha=0. Each nonzero component is therefore an isomorphism between one-dimensional vector spaces. This is a full-support conclusion, not an independence assertion about derivatives.

## 3. A nonzero covector on center motions

Using the natural first jets of sections vanishing on Z, define

    L:T_Z -> Hom(K_sigma,Q_sigma),
    L(v)(s)=-sum_(z in Z') alpha_z(ds_z(v_z)).              (2)

No contribution is used from the five G-centers. The construction is D-equivariant because rho', ell, the section line K_sigma and the derivative pairing are D-equivariant.

We show L is nonzero. Every eigenline of a direction different from G has nonzero projection to each G-eigenline coordinate. To see this universally, choose its direction lift w. Its nontrivial commutator with g makes w cyclically permute the five g-eigenlines. If a w-eigenvector had one zero coordinate in that decomposition, the eigenvector equation and the cycle would force all its coordinates zero. This is impossible.

A nonzero s in K_sigma has the universal support

    s=a x_1^2 x_4+b x_3^2 x_0,       a b !=0.

Its homogeneous singular locus is exactly the coordinate plane x_1=x_3=0: the partials with respect to x_4 and x_0 force these two equalities, and then every partial is zero. Thus s is nonsingular at every center in Z'. Equivalently, ds_z is a nonzero fiber-valued tangent covector there. This uses only the singular-locus identity and the preceding coordinate-hyperplane avoidance, not a point value or a selected derivative calculation. Since s vanishes at z, its nonzero homogeneous gradient annihilates the radial line by Euler's formula and defines the nonzero projective first jet.

Each coefficient alpha_z is nonzero, and the summands T_z P4 are independent. Thus every component alpha_z composed with ds_z in (2) is a nonzero covector on its own summand. Their direct-sum covector L is nonzero. No center or velocity is selected for an evaluation.

## 4. Character support places the covector on the normalization kernel

By PR616 the target line J_sigma=Hom(K_sigma,Q_sigma) has g-character0 and h-character2 for this normalized pair: Q_sigma has the negative value weight -(1,1), K_sigma has the negative missing weight -(1,3), and their Hom has missing-minus-value weight (0,2). Let pi be the joint D-character projection onto g-character0, h-character2 in T_Z. D-equivariance implies

    L=L pi.                                                (3)

Every vector in im pi belongs to ker b_N. Indeed the source T_Z has no U-invariants. On its g-fixed subspace the only U-characters are therefore nontrivial characters chi with kernel G. The shear h preserves each such chi-space: its conjugation on the other generator differs only by a power of g, which acts trivially here. On each such character the normalization target has only h-weights1 and4, by PR616. Equivariance forces b_N to kill the h-weight2 source. The same argument would apply to weight3.

Thus (3), together with L nonzero, proves L is nonzero on ker b_N. This avoids inferring nonvanishing from an unrestricted center velocity: the character projection first produces an actual normalization-compatible motion.

The pgl(A) summand has h-weight0 in each nontrivial character with kernel G, again by PR616, so this projection contains no ambient-coordinate motions. Equivalently the formula below annihilates those motions intrinsically. Consequently the nonzero class survives in the quotient H1(Theta_M).

## 5. Identification with the actual descent obstruction

For v in ker b_N and s in K_sigma, choose a lifted cubic t_s satisfying rho(t_s)=-(ds_z(v_z)) on all centers. Restrict to Z' and apply (1):

    ell(t_s)=alpha rho'(t_s)
            =-sum_(z in Z') alpha_z(ds_z(v_z))
            =L(v)(s).                                    (4)

At the two centers over sigma, s has zero first jet, so t_s vanishes there and the extension ell agrees with the intrinsic paired first-jet functional. The Hessian-free lemma now identifies (4) with b_J(v)_sigma(s), up to the uniform obstruction sign. Changing t_s by S changes neither side.

Section4 supplies a normalization-compatible v with L(v) nonzero, so the actual b_J is nonzero. The Galois pairing theorem then makes both descent channels nonzero. The normalizer transports this conclusion to all twenty-four nontrivial character blocks, giving

    b_J:ker b_N -> J_nt is an isomorphism,
    rank b=96,
    ker b=0,
    dim T_embedded=99.

No scalar value or determinant has been computed. The proof combines a full-support dual interpolation map, universal absence of singular centers for the simultaneous singular cubic, and disjoint character supports.

## 6. Boundary

The result eliminates non-projective first-order embedded deformations of the canonical cubic image V_51. It does not assert a full-adjoint vanishing for the original HM bundle, a prescribed-source membership result, higher-order algebraicity, or a solution to the original research goal. Any further assertion about the local Hilbert scheme requires its own argument beyond the first-order conclusion proved here.
