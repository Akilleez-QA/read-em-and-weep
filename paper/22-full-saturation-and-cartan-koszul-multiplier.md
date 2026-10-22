# 22. Full (1,3) exclusion and the Cartan–Koszul multiplier

**Checked-source cutoff: 22 October 2026, 08:05 UTC.** This chapter supersedes Chapter 21's open (1,3) profile, unevaluated C_mult, and unresolved leading weight-four affine transport. It does not supersede the higher-weight or fourth-obstruction boundaries.

The general section count remains **four or five**, the finite last Smith exponent remains **4–31** (or the cokernel is permanent), and **SF ≥ 3** and positive-square rank **≥ 27** are unchanged. The original source-recovery, lifting, and algebraicity goals remain open.

## 22.1 Strict descent of the highest Gauss splitting degree

Let F be a saturated subbundle of a constant bundle on P¹, with every splitting degree at most −d, d>0. Its Gauss kernel F⁻ satisfies

    H⁰(F⁻(d))=0.

A hypothetical section gives a saturated direct O(−d) summand C. Since the derivative of F kills C, its internal derivative lands in (F/C)(−2). That bundle has degrees at most −d−2, so the derivative is zero. The saturated horizontal C would be constant in characteristic zero, contradicting its negative degree. No plateau-rank or equivariance assumption is needed.

For the actual E, the global input H⁰(E(1))=0 therefore implies H⁰(E⁻(2))=H⁰(E⁻⁻(3))=H⁰(E⁻⁻⁻(4))=0. In particular, with K=E⁻ and A0=E/K, the actual derivative gives an injection H⁰(K(3)) → H⁰(A0(1)). This is a global-section/multiplicity constraint, not fiberwise injectivity of the derivative. [Strict highest-degree descent](https://github.com/Akilleez-QA/read-em-and-weep/blob/3165561818b782a97baa0b29443d6fdf7ce1129c/research/hm/order-four-quadratic-load/NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md)

## 22.2 Full saturation excludes the entire (1,3) profile

For maximal profile (1,3), write

    E=U O(−3) ⊕ V O(−4),   U=W′⊕2T6,
    rank E=17,   deg E=−54,
    K=E⁻,   I=(E/K)(3),   S=saturation of I in Q(1).

Here I and S have rank three. The cubic subimage J of U O is NOT substituted for I. Persistence gives H⁰(K(3))=0, U ⊂ H⁰(S), and deg I≥11. The full source E(4) is globally generated and generically maps onto S(1), so every degree of S is at least −1. A negative summand can only be the quartic-only block V O(−1); because it would fill the rank-three S and have no sections, U ⊂ H⁰(S) excludes it. Thus all degrees of S are nonnegative, independently of the rank of J.

In the reversed dual plateau, the rank-ten kernel Kd satisfies

    χ_G(Kd(3))=T6−2W−S4−χ_G(S*(4)),
    H⁰(Kd(3)) ≤ H⁰(S*(2))⊕H⁰(S*),
    11 ≤ deg S ≤ 29.

The full-source eligibility condition for an irreducible block R O(e) is

    Hom_G(U,R Sym^e W) ⊕ Hom_G(V,R Sym^(e+1) W) ≠ 0.

Exact character enumeration, with the section inclusion and dual envelope, leaves W′ O⊕O(15), W′ O⊕O(17), W′ O⊕O(19), and W′ O(2)⊕O(7). The first cannot embed into the actual Q(1). The determinant divisor of I ⊂ S has degree at most 19−11=8, below the smallest positive invariant divisor degree twelve. Hence I=S. The three exact quotients are

    E/K=W′ O(−3)⊕O(14),
        W′ O(−3)⊕O(16), or W′ O(−1)⊕O(4).

The earlier three-quotient reduction assumed rank J=3. The full-saturation proof removes that hypothesis rather than treating the conditional result as the whole exclusion. In every remaining kernel splitting, two top V O(−4) copies have only a one-dimensional equivariant map space to (E/K)(−2). A direct top V summand is killed; its internal derivative has target degrees at most −6, so it too is horizontal and cannot have negative degree. All cases are impossible. [Conditional three exact quotients](https://github.com/Akilleez-QA/read-em-and-weep/blob/3165561818b782a97baa0b29443d6fdf7ce1129c/research/hm/order-four-quadratic-load/EXTREMAL-13-RANK-THREE-CUBIC-IMAGE-THREE-EXACT-QUOTIENTS.md) [Entire (1,3) full-saturation exclusion](https://github.com/Akilleez-QA/read-em-and-weep/blob/4341dcd851b3d449db31a9e59af400ac20677c5d/research/hm/order-four-quadratic-load/EXTREMAL-13-FULL-SATURATION-EXCLUDES-THE-PROFILE.md)

Together with the previous exclusions, the only remaining possible maximal profiles are

    (1,1), (1,2), (2,1), (2,2).

They are necessary possibilities, not realized geometries. This does not prove SF≥4 or improve the smoothing rank.

## 22.3 The leading affine error is now canonically glued

The leading weight-four next error satisfies the complete affine law

    R2,j=Ad(P)R2,i+F_P(R1,i)+L2,j(Zij,0),
    F_P(R)=B1(P,R)P⁻¹+B1(PR,P⁻¹),
    L2(Z)=H0 DZ+[A0,Z]+(2H0ρ−Λ0)Z.

Both inhomogeneous terms matter: the first transports qR1 harmonically; the second is the second-normal mismatch of the locally truncated nilpotent. With the ordered mismatch and Čech conventions of the source,

    [Z0]=−(Bλ/4)[η_ap].

Conversion from q to q₀=νq divides that coefficient by ν². It is nonzero and is not discarded. Regular second-normal transition choices do not affect these leading coefficients. The triple cocycle, full scalar compatibility and equation-frame covariance are proved before acyclicity is used.

More precisely, let C(n,T,R1)=tr(TR1)+tr B1(n,R1). The trace datum is affine:

    tr(nR2)=H0Dχ+2(H0ρ−Λ0)χ−C(n,T,R1),

not an assumed zero. In the trace sequence

    0 → W′ O(−1) → E4 → Sym¹²(W′) O → 0,

the complete compatible affine discrepancy lies in W′ O(−1). H¹=0 gives a correction, and H⁰=0 makes it unique. This establishes the canonical leading weight-four affine family, not vanishing of raw R2 matrices. Higher weights, endpoint first-order mismatch contributions, and final ambient division remain separate. No global square-zero midpoint on a third neighborhood, full R2 solution, or fourth Bockstein follows. [Canonical leading affine transport](https://github.com/Akilleez-QA/read-em-and-weep/blob/ec48bfc075f6cfcb001fd7c7c8b50fc6513e0839/research/hm/order-four-quadratic-load/ACTUAL-LEADING-NEXT-ERROR-HAS-A-CANONICAL-AFFINE-TRANSPORT.md)

## 22.3a The next weight separates midpoint normalization from endpoint transport

The newly checked next-weight interface does not solve the full weight-eight error. First, the midpoint nilpotent mismatch Z4 has physical coefficient bundle J4=E4(−6), not E4:

    0 → W′ O(−7) → J4 → Sym¹²(W′) O(−6) → 0.

Its invariant tangent H¹ vanishes and H⁰(J4)=0. In normalized actual midpoint frames, the full square comparison gives δχ12=tr(n8 Z4). The invariant class of Z4 is therefore zero, and there is a unique compatible partial correction S4 with δS4=−Z4 and tr(n8S4)=−χ12. It leaves the nonzero Z0 and degree-eight scalar residue unchanged. In the stronger matched midpoint gauge, χ12=Z4=S4=0. **This is not vanishing of all intermediate weights:** arbitrary q² transition repairs can contribute [C,n8] starting at weight six, so Z6 may be present.

At the actual endpoint the complete lowest η0, including its lower quadratic entry and actual scale, instead forces

    D1,8=−[η0,n8],
    Ω4(η0)=[η0,T4]+B1(η0,n8)−B1(n8,η0),
    Z4,end=Z4,mid−Ω4(η0).

The degree-twelve square comparison retains tr(T4 D1,8)+tr B1(n8,D1,8). Thus the midpoint's zero-class proof cannot be copied to the endpoint. The η-dependent first-normal connection change is also affine, δK4=−(H0D+ad A0+H0ρ)η0, with other prescribed affine terms still included.

Associated-graded K4 lies in E4, with a thirteen-dimensional homogeneous section space. Global conic regularity excludes any nonzero K4 that is the coefficient of a global actual adjoint section: the pure-positive degree-twelve trace restricts isomorphically to the conic, where the actual ideal-square trace vanishes, and the acyclic trace kernel then forces K4=0. Consequently two fully prescribed global operators cannot differ at this coefficient if their difference is such an adjoint section. This proves **at most one admissible member**, not existence or the value of the actual selected coefficient; it does not set the endpoint affine family to zero.

The tangent weight-twelve first-error coefficient has the exact interface

    0 → E4 → E12 → V O(4) → 0,   K ↦ Kσ,
    rank/degree: (18,10)=(15,−2)+(3,12),
    h⁰(E12)=28,   H¹(E12)=0.

The actual V O(4) section is not computed. Extracting E12 from a full actual lift must retain possible weight-eight stabilizer mixing of a lower weight-four component.

Finally, for a general first-order mismatch, the second-error transport has all of the following terms:

    R2,j=Ad(P0)R2,i+F_P0(R1,i)+[Q,Ad(P0)R1,i]
          +L2(Z)+C1(D1)+Op2(n).

Here C1 is the complete first-normal operator action, including symbol, scalar, normal-line and both ordered harmonic terms. Op2(n)=h2Dn+[a2,n]−λ2n is the remaining second-normal operator-compatibility defect; it is not presumed zero. The endpoint η contribution includes

    [η0,R1,8]−L2(Ω4(η0))−C1([η0,n8]),

while harmonic transport of the actual R1,12 and the separate Op2 contribution remain. The general F_P0 also includes its harmonic inverse correction; the two-term marked formula is sufficient only at the retained weight under the established degree bounds. These are precise interfaces for the missing calculation, not its value. [Next-weight proof][NEXT] and [companion verifier][NEXTV].

## 22.4 The complete five-equation problem

With normalized arrows A0,B0,C0 and actual nonzero channel parameters, write α=[c_m C0 | a_m A0+b_m B0]. Equivariance and parameter weights give the complete ansatz

    T_middle=a_m M_a+b_m M_b,
    T_AA=a_m P_a+b_m P_b,   T_UU=a_m Q_a+b_m Q_b,
    T_UA=c_m R,   T_AU=(a_m b_m/c_m) S.

The middle operator is determinant-pairing skew; the right-source operator is the negative adjoint of the left-source operator. All five coupled equations must hold:

    M_a A0=A0 Q_a,
    M_a B0+M_b A0=A0 Q_b+B0 Q_a+C0 S,
    M_b B0−B0 Q_b=2a B0,
    M_a C0−C0 P_a−A0 R=−C_mult q₀ δ_D C0,
    M_b C0−C0 P_b−B0 R=0.

There are fourteen, eight, and twelve possible coefficient intertwiners in the two middle and combined source spaces. These are not ranks of actual maps. The reverse source S cannot be omitted. The possible extra middle weight a_m²/b_m is absent by Hom_G(A,V⊗V)=0. [Complete five-equation ansatz](https://github.com/Akilleez-QA/read-em-and-weep/blob/f366c7e78511942f974072e76c4834e29a9146f9/research/hm/order-four-quadratic-load/UNIVERSAL-MONAD-HOMOTOPY-HAS-FIVE-CHANNEL-EQUATIONS.md)

For the gradient partial ansatz M_a=−C_mult R_D, P_a=Q_a=0, R=C_mult s_D, the Clifford/Fierz compression gives

    B0* R_D B0=−(g_L/χ)a M,
    Q_b=(−1−C_mult g_L/(2χ))a I_U.

This alone neither determines the multiplier nor makes the gradient ansatz without loss. The complete construction below proves existence of a solution and uses the actual multiplier's uniqueness. [Gradient/Fierz source scalar](https://github.com/Akilleez-QA/read-em-and-weep/blob/5f0ab21fa3b4c46d27d1e7b8b02c6d22275ecc94/research/hm/order-four-quadratic-load/UNIVERSAL-GRADIENT-HOMOTOPY-FIXES-THE-U-SOURCE-SCALAR.md)

## 22.5 The full Cartan–Koszul construction determines C_mult

Retain the fixed algebraic Clifford tensor M(v)=i_v L and the a-channel volume τ. Define nonzero χ and g_L by

    M(v)²=χ q₀(v) I,
    tr(M(ξ)[M(η),M(ζ)])=g_L τ(ξ,η,ζ).

The trace is the full two-dimensional trace. No channel parameter, actual cubic coefficient, or normalization constant is assigned a source-instance value. The complete global two-arrow homotopy proves

    C_mult=−χ/g_L,
    κ=−(χ/g_L)(a_m/b_m).

The invariant numerical coefficient is C_mult g_L/χ=−1, not a choice setting C_mult or χ to one. [Complete Cartan–Koszul multiplier homotopy](https://github.com/Akilleez-QA/read-em-and-weep/blob/6ebbf04da44a2b1b1a4e3b7659d519cfad6c0884/research/hm/order-four-quadratic-load/UNIVERSAL-CARTAN-KOSZUL-MULTIPLIER-HOMOTOPY.md)

Here are the checks that distinguish the completed proof from a partial channel calculation.

1. A global polynomial quadratic Cartan lift T_S is constructed for arbitrary End(P), not just its symplectic-skew sector. Its paired coefficient blocks are R and −R†. Coefficient-space adjoints prove skewness for the determinant-valued pairing, including the selfadjoint sector; it lands in the middle kernel and kills B.
2. Under the actual conformally symplectic cubic identification f:Sym³W→P, use S_comb=3DN−ND, with commutator and anticommutator parts both retained. The conformal scalar cancels only in transported adjoints; the scale of the actual cubic is retained in its coefficient and inverse maps.
3. A full cubic identity forces the reverse-source remainder into the Clebsch image. Exact polynomial divisibility constructs the global S block, without division at a chosen coordinate point.
4. In the final C-channel residual, the same projected operator J_v is used in every term. Its universal normalization is −(2/3)ρ³(M(v)); after f-transport it lies in Sym⁶W. The complete identity 36Z_K+2Z_minus+Z_plus=0 cancels the Cartan component with that common scale, not independently rescaled proportionalities.
5. The remaining spin component is globally regular b-type, E_C=B t, by coprimality of the negative coordinate variables. The full reverse equation, skewness, isotropy and the already checked C equation give M(v)t=0. The Clifford square yields χq₀t=0 in the polynomial domain, hence t=0. Nonzero separate factors are not being mistaken for a nonzero composite.
6. The prescribed negative dual source operator supplies the second monad arrow. The existing actual cyclic/multiplier theorem gives uniqueness, identifying the exhibited scalar with the actual C_mult.

In explicit source notation the solution includes M_a=(χ/g_L)R_D, M_b=−3K/2−T_(S_comb)/24, P_a=Q_a=0, Q_b=−a I_U/2, P_b=−3a I_A/2−P_comb/24, and R=−(χ/g_L)s_D. The globally regular reverse S is defined by the Clebsch inverse, not omitted.

The algebraic M=i_v L must be distinguished from the pairing-defined cross operator under an independent determinant-frame change. They agree in the compatible frame Ω=τ∧ω, not automatically after changing only Ω. Under L→sL and τ→tτ, χ/g_L has weight t/s, canceled by the same-monad change of a_m/b_m. The physical equation weight is likewise retained. This does not identify C_mult with a normal-cup constant.

## 22.6 Mr. Slop: exact sixteen-axis detection and residue reconstruction

These complementary results concern the universal endpoint-family interface on X=P(A):

    0 → K → D⊗O_X → A⊗O_X(1) → 0,
    F=K*⊗P⊗O_X(2),   E:Q⊗O_X → F,   dim Q=2.

Here F has rank eight, P has dimension four, and Q is the two-dimensional trivial family representation. This local F is the endpoint-interface bundle, not the Horrocks–Mumford bundle denoted F in Chapter 1. Keep three notions separate: the detection scheme Δ where E has rank at most one, the zero scheme Z_q of one section t_q∈H⁰(F), and the rank of its fixed map K→P(2).

PR668 first proves reducedness and separates the C3/C5 channels. The exterior minors of a fixed map are septics because det K=O(−3). At six hypothetical fat C5 axes, all minors would vanish to order four. The six distinct smooth conics through five of those axes force every septic to vanish by Bézout (twenty intersections versus fourteen). If C3 and C5 kernel channels coincided, each septic would have four double points on each of fifteen mirror lines, again forcing zero (eight versus seven). Either conclusion contradicts the earlier universal generic-rank-two square-conic theorem for a mixed channel.

Reduced fixed-channel zeros do not by themselves prove reduced detection. The additional stabilizer argument is essential: the tangent space at each possible exceptional axis has no trivial stabilizer constituent, while a complementary nonzero invariant section spans a trivial line. The derivative of the vanishing section remains injective after quotienting by that line. Nakayama therefore identifies the local detection ideal with the maximal ideal. [PR668][P668]

PR669 excludes the C2 orbit without requiring an actual family evaluation. The six polar lines of the C5 axes have exactly fifteen distinct pairwise intersections, the C2 axes, with no triple concurrence. A hypothetical C2 channel has exterior septics doubly vanishing at all those points; five double points on each line force

    Λ²(t_q)=F6·j,   0≠j:A → Λ²P.

The unique A summand of Λ²P=A⊕A′ has nondegenerate wedge pairing. Thus j∧j is not the zero quadratic, contradicting the decomposability/Plücker identity of Λ²(t_q). Consequently Δ is exactly the **sixteen reduced C5/C3 axes**. There are precisely two exceptional projective channels, with reduced zero schemes of lengths six and ten; all other nonzero channels are nowhere zero as sections of F. Their actual numerical parity ratios and membership of the actual endpoint family are not determined. [PR669][P669]

PR670 upgrades this scheme statement to an exact image and reconstruction theorem. Let ℓ5,ℓ3⊂Q be the distinct exceptional lines and I5,I3 their orbit ideals. Joint local row operations, not merely separate projections, give

    im(E*)=(ℓ5*⊗I5)⊕(ℓ3*⊗I3).

At a C5 point the image is m⊕R (reversed at C3), and E has regular local form (b,c)↦(c,bx,by,0) in R⊕R²⊕R⁵. Thus H=ker(E*) is a rank-six vector bundle, T=coker(E) is torsion-free with local form R⁵⊕m, and its locally free reflexive completion S=T**=H* fits into

    0 → T → S → R_Δ → 0,
    R_Δ=⊕(ℓ_i⊗Ext²(O_(Σ_i),O_X)).

The sixteen residue fibers have reflection-sign stabilizer character, unlike the trivial-character fibers of coker(E*). Since Ext²(O_p,O_X)=det(T_pX),

    H⁰(R_Δ)=(A⊕A′) ⊕ (A⊕A′⊕P).

For every integer n, a section of S(n) lifts to F(n) exactly when its canonical residues vanish; lifts form a torsor under Q⊗H⁰(O_X(n)). At n=0, h⁰(F)=84, h⁰(T)=82, h⁰(S)=98 and all sixteen residues interpolate. T is 0-regular and S is (−2)-regular; h⁰(S(−2))=36. These follow from the exact resolutions, not Chern-class counts alone.

At an axis O_X(n) has character ε^n, so residues have character ε^(n+1). Invariant sections of S(n) always lift for even n. Odd n has two orbitwise invariant residue tests, genuinely independent for odd n≥−1; one must not assert independence for all negative odd twists merely from the character count.

Finally the division-free wedge test is exact at F:

    0 → Q⊗O_X → F → (det Q)*⊗Λ³F,
    u ↦ [q∧r ↦ E(q)∧E(r)∧u].

Off the sixteen axes it is ordinary rank-two span membership. Its unique coefficient sections extend across the codimension-two set by Hartogs, proving the global statement without choosing a nonvanishing minor everywhere. Thus for u∈H⁰(F(n)), wedge vanishing is equivalent to u=E(f) for unique f∈Q⊗H⁰(O_X(n)). This tests a section already in F; it is different from lifting a reflexive quotient datum. Neither test has been evaluated on the prescribed higher-obstruction source. [PR670][P670]

## 22.7 Evidence and the remaining frontier

The full proof and independent audit check the arbitrary-End(P) lift, the reverse-source cubic identity, both components of the sextic identity, and the exact common projected normalization. The companion verifier additionally checks the full coefficient-space adjoints and all five channel equations. These are universal polynomial and representation identities with free coefficients, not actual-instance rank experiments or proof-assistant certificates. [Independent Cartan–Koszul tensor audit](https://github.com/Akilleez-QA/read-em-and-weep/blob/6ebbf04da44a2b1b1a4e3b7659d519cfad6c0884/research/hm/order-four-quadratic-load/UNIVERSAL-CARTAN-KOSZUL-HOMOTOPY-INDEPENDENT-AUDIT.md)

The multiplier problem and leading weight-four affine gluing are now closed in their stated markings. They do not supply the actual second division, compare all higher-weight endpoint errors, or evaluate any of the four actual fourth-obstruction channels. The third remains zero; the fourth-or-later versus permanent-cokernel alternative remains unresolved. The checked next-weight interface above is included; later multiplied-square-zero-lift and operator-class notes are not incorporated here. The checked PR668–670 results above are universal family statements, not actual source membership or fourth values.

## Immutable source ledger and reproduction

Run the companion scripts in the research source directory, retaining their imported helpers. The mathematical proofs supply the saturated-bundle, channel-identification, uniqueness and global regularity arguments; the scripts supplement them.

- [Strict highest-degree descent](https://github.com/Akilleez-QA/read-em-and-weep/blob/3165561818b782a97baa0b29443d6fdf7ce1129c/research/hm/order-four-quadratic-load/NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md); [companion verifier](https://github.com/Akilleez-QA/read-em-and-weep/blob/3165561818b782a97baa0b29443d6fdf7ce1129c/research/hm/order-four-quadratic-load/verify_negative_gauss_strict_top_slope.py). Commit `3165561818b782a97baa0b29443d6fdf7ce1129c`.
- [Conditional three exact quotients](https://github.com/Akilleez-QA/read-em-and-weep/blob/3165561818b782a97baa0b29443d6fdf7ce1129c/research/hm/order-four-quadratic-load/EXTREMAL-13-RANK-THREE-CUBIC-IMAGE-THREE-EXACT-QUOTIENTS.md); [companion verifier](https://github.com/Akilleez-QA/read-em-and-weep/blob/3165561818b782a97baa0b29443d6fdf7ce1129c/research/hm/order-four-quadratic-load/verify_extremal_13_cubic_image_reduction.py). Commit `3165561818b782a97baa0b29443d6fdf7ce1129c`.
- [Entire (1,3) full-saturation exclusion](https://github.com/Akilleez-QA/read-em-and-weep/blob/4341dcd851b3d449db31a9e59af400ac20677c5d/research/hm/order-four-quadratic-load/EXTREMAL-13-FULL-SATURATION-EXCLUDES-THE-PROFILE.md); [companion verifier](https://github.com/Akilleez-QA/read-em-and-weep/blob/4341dcd851b3d449db31a9e59af400ac20677c5d/research/hm/order-four-quadratic-load/verify_extremal_13_full_saturation_exclusion.py). Commit `4341dcd851b3d449db31a9e59af400ac20677c5d`.
- [Canonical leading affine transport](https://github.com/Akilleez-QA/read-em-and-weep/blob/ec48bfc075f6cfcb001fd7c7c8b50fc6513e0839/research/hm/order-four-quadratic-load/ACTUAL-LEADING-NEXT-ERROR-HAS-A-CANONICAL-AFFINE-TRANSPORT.md); [companion verifier](https://github.com/Akilleez-QA/read-em-and-weep/blob/ec48bfc075f6cfcb001fd7c7c8b50fc6513e0839/research/hm/order-four-quadratic-load/verify_leading_next_error_affine_transport.py). Commit `ec48bfc075f6cfcb001fd7c7c8b50fc6513e0839`.
- [Complete five-equation ansatz](https://github.com/Akilleez-QA/read-em-and-weep/blob/f366c7e78511942f974072e76c4834e29a9146f9/research/hm/order-four-quadratic-load/UNIVERSAL-MONAD-HOMOTOPY-HAS-FIVE-CHANNEL-EQUATIONS.md); [companion verifier](https://github.com/Akilleez-QA/read-em-and-weep/blob/f366c7e78511942f974072e76c4834e29a9146f9/research/hm/order-four-quadratic-load/verify_universal_monad_five_channel_homotopy.py). Commit `f366c7e78511942f974072e76c4834e29a9146f9`.
- [Gradient/Fierz source scalar](https://github.com/Akilleez-QA/read-em-and-weep/blob/5f0ab21fa3b4c46d27d1e7b8b02c6d22275ecc94/research/hm/order-four-quadratic-load/UNIVERSAL-GRADIENT-HOMOTOPY-FIXES-THE-U-SOURCE-SCALAR.md); [companion verifier](https://github.com/Akilleez-QA/read-em-and-weep/blob/5f0ab21fa3b4c46d27d1e7b8b02c6d22275ecc94/research/hm/order-four-quadratic-load/verify_gradient_homotopy_u_source_scalar.py). Commit `5f0ab21fa3b4c46d27d1e7b8b02c6d22275ecc94`.
- [Complete Cartan–Koszul multiplier homotopy](https://github.com/Akilleez-QA/read-em-and-weep/blob/6ebbf04da44a2b1b1a4e3b7659d519cfad6c0884/research/hm/order-four-quadratic-load/UNIVERSAL-CARTAN-KOSZUL-MULTIPLIER-HOMOTOPY.md); [companion verifier](https://github.com/Akilleez-QA/read-em-and-weep/blob/6ebbf04da44a2b1b1a4e3b7659d519cfad6c0884/research/hm/order-four-quadratic-load/verify_universal_cartan_koszul_multiplier.py). Commit `6ebbf04da44a2b1b1a4e3b7659d519cfad6c0884`.
- [Independent Cartan–Koszul tensor audit](https://github.com/Akilleez-QA/read-em-and-weep/blob/6ebbf04da44a2b1b1a4e3b7659d519cfad6c0884/research/hm/order-four-quadratic-load/UNIVERSAL-CARTAN-KOSZUL-HOMOTOPY-INDEPENDENT-AUDIT.md); [companion verifier](https://github.com/Akilleez-QA/read-em-and-weep/blob/6ebbf04da44a2b1b1a4e3b7659d519cfad6c0884/research/hm/order-four-quadratic-load/verify_cartan_koszul_homotopy_independent_audit.py). Commit `6ebbf04da44a2b1b1a4e3b7659d519cfad6c0884`.

[P668]: https://github.com/Akilleez-QA/read-em-and-weep/blob/ca3c34c40363bde6315a0797eb66a5d3ea68c104/research/hm/reduced-channel-degeneracy/PROOF.md
[P669]: https://github.com/Akilleez-QA/read-em-and-weep/blob/8c17fe9c5736d657cf07f894b24917ec301e09af/research/hm/involution-channel-exclusion/PROOF.md
[P670]: https://github.com/Akilleez-QA/read-em-and-weep/blob/d71dbafcca050adadd353d6a417f23c527948f64/research/hm/endpoint-detection-resolution/PROOF.md

[NEXT]: https://github.com/Akilleez-QA/read-em-and-weep/blob/3d21e93865152ec961ceaf32d48f845399158b69/research/hm/order-four-quadratic-load/ACTUAL-NEXT-WEIGHT-SEPARATES-MIDPOINT-NORMALIZATION-FROM-ENDPOINT-TRANSPORT.md
[NEXTV]: https://github.com/Akilleez-QA/read-em-and-weep/blob/3d21e93865152ec961ceaf32d48f845399158b69/research/hm/order-four-quadratic-load/verify_next_weight_midpoint_endpoint_interfaces.py
