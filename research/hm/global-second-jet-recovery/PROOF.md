# Recovering the actual second-normal leading jet from its lower data

## Result, novelty boundary, and fixed inputs

This note proves a specialized local-to-global interface for the actual third-neighborhood section. It does **not** claim a new weight-four trace sequence or a new general acyclic-torsor principle: both are already proved in the original sources listed below.

Let `J3` be the physical-even trace-free section of `B_(3Q)(8)` in PR713, where `B=End_0(F)`. Its leading total-weight-twelve harmonic coefficients are

    J3_[12] = H(P) + q H(M) + q^2 H(R) modulo q^3,
    wt(P)=12, wt(M)=8, wt(R)=4, P=A n8, A=a^2 h.

Here `a` is a nonzero negative quadratic, `h` is a nonzero positive source, `n8` is the actual leading nilpotent, and `H` is the fixed homogeneous harmonic lift. The physical twists of `P,M,R` are respectively `8,6,4`. All local equations, scalar-twist factors, homogeneous coordinate changes, determinant factors and frame units are retained.

The conclusion is that the actual-compatible lower data `P,M`, together with the marked leading transitions, determine the entire actual `R`, not only its modular image. More generally, for this weighted third-neighborhood layer the only additional condition is regular local solvability of the scalar square equation. If that condition holds, the trace-compatible affine gluing problem has exactly one solution. In the actual problem, existence of `J3` supplies that condition.

Thus the weight-four coefficient `A2` in PR780 satisfies

    A2 = a^2 R(P,M,T0),

and is no longer an independent jet input once the actual regular lower data and their marked transition law are fixed. Using the separately established existence of the actual fourth lift, Section 6 also recovers `A3` uniquely, at the correct pre-multiplication twist. This does not recover `B2,B3`, construct a full actual lift from arbitrary lower jets, evaluate a fourth-square or fifth-boundary class, or decide algebraicity.

### Pinned sources and what is already known

1. [PR713, 5b3943980ecaef78ee7f56fbc015d40955fb24f0](https://github.com/Akilleez-QA/read-em-and-weep/blob/5b3943980ecaef78ee7f56fbc015d40955fb24f0/research/hm/leading-vertex-obstruction/PROOF.md) gives the leading `P,M,R` formula, its square equation, and the local two-dimensional kernel. Its remaining dependency explicitly includes structural determination of the actual `R`.
2. [PR692, 858f96ba1539afb1293f31239b8761af08e46f60](https://github.com/Akilleez-QA/read-em-and-weep/blob/858f96ba1539afb1293f31239b8761af08e46f60/research/hm/vertex-scalar-filtration/PROOF.md) gives the actual generic coefficient bounds `12,8,4`.
3. [PR774, eec909bef4a7e6998737773d5eadd0ad562e79d9](https://github.com/Akilleez-QA/read-em-and-weep/blob/eec909bef4a7e6998737773d5eadd0ad562e79d9/research/hm/matrix-jet-filtration/PROOF.md) supplies the regular adapted physical filtration, its locally free graded modules and saturation over the entire vertex line.
4. [PR778, e527b939f9a8f5cf8967f32048a23a9d830d77c9](https://github.com/Akilleez-QA/read-em-and-weep/blob/e527b939f9a8f5cf8967f32048a23a9d830d77c9/research/hm/normal-transition-channel/PROOF.md), Section 2, proves that the homogeneous weight-zero triangular transitions have exact multiplicative ambient lifts. Its nonzero first ambient correction is not set to zero here.
5. [The old acyclic coefficient theorem](https://github.com/Akilleez-QA/read-em-and-weep/blob/8d8b5be4ce62c3055bb53be9e16d29cc63072f04/research/hm/order-four-quadratic-load/ACTUAL-LOWEST-NEXT-ERROR-TANGENT-COEFFICIENT-IS-ACYCLIC.md), Sections 1–3, already proves the exact sequence, actual nonsplit transport and full acyclicity used below.
6. [The old next-error affine theorem](https://github.com/Akilleez-QA/read-em-and-weep/blob/8d8b5be4ce62c3055bb53be9e16d29cc63072f04/research/hm/order-four-quadratic-load/ACTUAL-LEADING-NEXT-ERROR-HAS-A-CANONICAL-AFFINE-TRANSPORT.md), Section 6, already performs a kernel-valued Cech correction for a different coefficient, the operator next error `R2`, with its harmonic first-error and nilpotent-mismatch affine terms. We use that general recovery principle, not its different affine law.
7. [The actual third-neighborhood square-zero theorem](https://github.com/Akilleez-QA/read-em-and-weep/blob/8d8b5be4ce62c3055bb53be9e16d29cc63072f04/research/hm/order-four-quadratic-load/ACTUAL-CORRECTED-THIRD-NEIGHBORHOOD-LIFT-IS-SQUARE-ZERO.md), at the same pinned commit, supplies the actual global `J3` in `B_(3Q)(8)` and its square-zero identity.
8. [The actual fifth-neighborhood ladder](https://github.com/Akilleez-QA/read-em-and-weep/blob/8d8b5be4ce62c3055bb53be9e16d29cc63072f04/research/hm/order-four-quadratic-load/ACTUAL-FOURTH-BOCKSTEIN-AS-A-FIFTH-NEIGHBORHOOD-ADJOINT-BOUNDARY.md), Sections 1–2, constructs an actual even fourth lift `J4` of `aJ3` by global cochains. [PR685, 449a8df60662bd7a1d93e318ea4f7e6dab28e5ad](https://github.com/Akilleez-QA/read-em-and-weep/blob/449a8df60662bd7a1d93e318ea4f7e6dab28e5ad/research/hm/third-lift-uniqueness/PROOF.md), Section 3, transports that existing lift across all classified even completions of `J3`; it does not independently prove the initial existence. This is an extra existence input for Section 6, not a consequence of acyclicity.
9. [PR780, c82c3a3b6b513e80a5af21f06ecc52170cb0a056](https://github.com/Akilleez-QA/read-em-and-weep/blob/c82c3a3b6b513e80a5af21f06ecc52170cb0a056/research/hm/transition-boundary-formula/PROOF.md), Sections 1 and 3, records `J0(4)=P4 O_L(-2)` and the degree-two bound for harmonic transport by `T0`. The coefficient identification is itself explicitly credited to older sources in PR778.
10. [PR725, 397c7473691a08a839ccf7e9abeed06002b48bab](https://github.com/Akilleez-QA/read-em-and-weep/blob/397c7473691a08a839ccf7e9abeed06002b48bab/research/hm/modular-vertex-elimination/PROOF.md) already eliminates `R` from the immutable quotient modulo the cubic by two modular divisions. It leaves the local trace-kernel translation undetermined. The present statement instead recovers the full actual `R` through regular global compatibility.

The new interface checked below is the actual `J3` affine law and its full square compatibility. It is not a new claim about the abstract coefficient sequence or about all higher normal errors. This is a targeted comparison, not an exhaustive novelty claim about every repository file.

## 1. The old exact coefficient sequence includes the actual twists

Write `U` for the positive binary space and `L=P(W)`. Let `E4` be the weight-four coefficient bundle of `B_Q(4)`, with its actual triangular transition. The old theorem proves

    0 -> U tensor O_L(-1) -> E4 --tau--> Sym^12 U tensor O_L -> 0,
    tau(R)=tr(n8 R).                                      (1)

For clarity, this is not obtained by computing a determinant degree. Its local trace formula, for the retained unit `u`, is

    n8=u [[fg,-f^2],[g^2,-fg]],
    tau([[x,y],[z,-x]])=u(2fgx+g^2 y-f^2 z),
    deg(f)=3, deg(g)=5, (deg x,deg y,deg z)=(4,2,6).

Regularity of the pair in every fiber gives the exact kernel

    D=ell [[f,0],[2g,-f]],    deg(ell)=1.                  (2)

Indeed reduction modulo `f` forces `f|y`, hence `y=0`; then `2gx=fz` forces `x=f ell, z=2g ell`. Relative regularity gives the same sheaf statement. Multiplication by the nonzero unit `u` does not change the kernel. The square-ideal quotient of a regular `(3,5)` pair ends in degree eleven, so the trace map is onto degree twelve in every fiber and therefore surjective as a bundle map.

The physical-twist-four entry presentations are diagonal `Sym^4 U O(2)`, upper `Sym^2 U O(10)`, and lower `Sym^6 U O(-6)`. They are a triangular presentation, **not** a splitting. Trace has physical twist six and binary degree twelve, explaining its `O(6-12/2)=O` coefficient line.

The complete old marked transition proves the kernel identification in (1): the tangent map is `v -> sigma v^t J+v sigma^t J`. At this weight the first component of `v` would have degree minus one and is absent, while its second component is `ell` of degree one. The preimage lies in `G(2)`. The marked lines of `G` are `O(9/2),O(-5/2)`, so its second coefficient line is

    O(-5/2+2-1/2)=O(-1).

Explicitly the marked pair transition is `sigma_x=P D sigma_y`, with `P=[[1,0],[p,1]]` and `D=diag(z^3,z^-5)`. The tangent-preimage transition is

    v_x=P diag(z^7,z^-1) v_y.

Because `v1=0`, it gives exactly `ell_x=z^-1 ell_y`; the actual triangular term has not been dropped. The matrix identity is

    tau_tan(sigma_x,v_x)=z^2(PD) tau_tan(sigma_y,v_y)(PD)^-1,

including the determinant factor. This also proves compatibility with changes of marked trivialization and unit factors; no square root of a frame unit is chosen. The retained factor `u` belongs to the intrinsic trace map, rather than being normalized away.

The diagonal and lower entries of (2) have degrees four and six, and the upper entry vanishes. In the actual physical eigenframe these have precisely the even endomorphism character; all weights involved are multiples of four. Hence we are using the physical-even kernel in its actual linearization, not confusing physical inversion with the residual binary-cover involution. In particular the entire kernel, before taking any finite-group invariants, satisfies

    H0(U O(-1))=H1(U O(-1))=0.                         (3)

## 2. Only the exact leading reference acts on this layer

Transfer PR692's actual generic bounds through adapted regular frames using PR774, and then use saturation of each locally free coefficient module on the integral line. This gives `J3>=12` along all of `L`, without inverting `a` at its zeros. The adapted-frame comparison is the same cubic-first comparison used in PR775 for `J4`: a constant lower-left change would contradict the quintic initial order of the second component.

In physical frames all positive transition weights are at least four. Thus any positive-weight transition correction acting on a section of total weight at least twelve contributes only at weight at least sixteen. The total-weight-twelve part of actual `J3` therefore glues modulo `q^3` using only the leading triangular matrices `T0`.

Those matrices have base-only diagonal entries and an ordinary transverse-linear lower entry. Their exact ambient product and inverse contain no product of two lower entries. PR778 proves that their ambient homogeneous lifts form an exact cocycle, including coordinate substitutions. Consequently they act on the entire harmonic coefficient algebra modulo `q^3`, not merely on its cone restriction. This is why harmonic mixing below cannot produce a hidden triple-overlap defect.

This argument does not discard the nonzero first ambient correction `qZ0`. Its total matrix weight is four, so its first action here is at weight sixteen, outside the layer being recovered.

## 3. The specific affine transport of the J3 coefficient

Use ordered overlaps and a single common trivialization when extracting coefficients. Let `Phi_ij` denote transport by the exact ambient `T0`, together with the physical-twist-eight scalar transition, homogeneous coordinate substitution and the local equation-line transport. If `q_j=nu_ij q_i`, substitution is made **before** extracting any `q_i` coefficient. Equivalently, each original `q_j^r` term carries its factor `nu_ij^r` as well as the section's scalar transition. Its resulting coefficient has physical twist `8-2r`.

The supplied lower data are compatible precisely when

    H(P_i)+q_i H(M_i)
      = Phi_ij(H(P_j)+q_j H(M_j)) modulo q_i^2.         (4)

Define the known affine shift and the linear coefficient transport by

    F_ij(P_j,M_j)=[q_i^2] Phi_ij(H(P_j)+q_j H(M_j)),
    G_ij R_j=[q_i^2] Phi_ij(q_j^2 H(R_j)).              (5)

The result of each extraction is read as its cone harmonic coefficient. The second map is exactly the ordinary leading transport of `E4`, because only the zeroth harmonic coefficient can contribute after the prefactor `q_i^2`. The first retains both the order-two harmonic transport of `P` and the order-one harmonic transport of `M`.

The actual second coefficient obeys exactly

    R_i=G_ij R_j+F_ij.                                (6)

This follows by extracting `q_i^2` from the actual gluing established in Section 2. Conversely (4) and (6) are exactly gluing of this total-weight-twelve truncated section modulo `q^3`.

Since `Phi_ij Phi_jk=Phi_ik` exactly and (4) holds, coefficient extraction gives

    G_ij G_jk=G_ik,
    F_ik=F_ij+G_ij F_jk.                              (7)

Thus (6) is a genuine affine cocycle. There is no use of a guessed multiplicative harmonic lift. Nor is `F` borrowed from the old operator-error formula: it is derived directly for this third-neighborhood section.

## 4. Its affine transport preserves the full square equation

Put

    Q(P,M)=sc(M^2+B1(P,M)+B1(M,P)+B2(P,P)),
    sc=tr/2.

This has scalar binary degree sixteen and physical twist twelve. Since the given lower section is square-zero modulo `q^2`, the complete `q^2` square equation is

    A tau(R)=-Q(P,M),    A=a^2 h.                     (8)

There are no omitted ordered harmonic products. Here `tau(R)` has degree twelve and physical twist six; multiplying by `A`, of degree four and physical twist six, has the required degree sixteen and twist twelve.

For the general local-to-global statement assume the regular divisibility condition

    -Q(P,M) belongs locally to A·(Sym^12 U O_L).      (9)

This is image membership under the actual multiplication map, not a declaration that `a` or `h` is a unit. Since the coefficient polynomial rings over integral base opens are domains and `a,h` are nonzero, multiplication by `A` is injective as a sheaf. Thus (9) defines a unique regular local trace datum `d` by `A d=-Q`. In the actual case (9) follows from existing regular `R`; no new existence of a full `J3` is being presumed for arbitrary inputs.

Equation (8) is preserved by (6). Indeed `Phi_ij` is exact conjugation with the appropriate scalar line factors, so it sends the square of a section to the correspondingly transported scalar square. The coefficients of orders zero and one in that square vanish by hypothesis. Therefore the transformed order-two scalar vanishes if and only if the original order-two scalar vanishes. After harmonic extraction these are precisely the two chart versions of (8).

This proves compatibility of the full affine trace datum. It does **not** say that the individual `d_i` form an ordinary section of the untwisted trace target: the affine shift can change its representative. Its correct transformation includes `tau(F_ij)`.

At fixed lower data, the difference of two regular solutions to (8) satisfies `A tau(D)=0`, hence `tau(D)=0` by sheaf injectivity. The kernel is therefore exactly (1), including across every source zero. One must not first specialize the raw equation to a fiber with `a=0` and cancel there; that would give a different, spuriously enlarged solution problem. Regular sheaf solutions retain the cancellation just proved.

## 5. Unique correction and actual reconstruction

Choose an affine cover refining the regular marked atlas. Condition (9) and surjectivity of (1) supply local regular solutions `R_i^0` of (8). Their affine defects are

    D_ij=R_i^0-G_ij R_j^0-F_ij.

By Section 4 they are sections of `K=U O(-1)`. Equation (7) makes `D` a Cech cocycle in that bundle. By `H1(K)=0`, choose a kernel-valued zero-cochain `t_i` with

    t_i-G_ij t_j=D_ij.

Then `R_i=R_i^0-t_i` obeys (6) and still satisfies (8). Any two corrected families differ by a global section of `K`, which is zero by `H0(K)=0`. Thus the corrected family is unique and independent of the local trace preimages and their chosen Cech primitive. Refinement and changes of marked charts give the same family under the induced transport.

This is an abstract exact reconstruction, not a numerical evaluation or a replacement of the full actual section by a homogeneous global bundle. For the actual lower data the existing `J3` supplies one such compatible family, so uniqueness identifies the recovered family with its actual leading second-normal jet `R4`. No uncomputed local linear-form freedom remains.

## 6. The next leading coefficient is uniquely recovered using actual fourth-lift existence

This corollary uses an additional established existence theorem; it does not claim that the next extension follows automatically from the local square condition in Section 4.

Let `J4` be an actual even section of `B_(4Q)(10)` restricting to `aJ3`, as constructed by the pinned actual fifth-neighborhood ladder and transported across the classified even completions by PR685. Its total-weight-twelve part has the form

    (J4)_[12]=a[H(P)+q H(M)+q^2 H(R)]+q^3 D0,

where `D0` has matrix weight zero and physical twist `10-6=4`. Regular physical-even matrices have no negative weights, so every local fourth-lift correction starts at this total weight. As before, positive-weight actual transitions affect this part only in total weight at least sixteen; only exact `T0` transport enters.

Let `Phi^10_ij` be the exact transport including physical twist ten, and define

    F3_ij=[q_i^3] Phi^10_ij(a_j[H(P_j)+q_j H(M_j)+q_j^2 H(R_j)]).

The lower local expression has no `q_i^3` coefficient. The recovered `P,M,R` already glue modulo `q^3`; hence exact reference composition makes `F3` a genuine cocycle in `J0(4)`. In the target-minus-transport convention the boundary of the lower truncation is `-F3`. The correction equation is therefore

    D0_i-G^0_ij D0_j=F3_ij.                             (10)

The existence of actual `J4` proves `[F3]=0`. It is essential to retain that input: `H1(J0(4))=P4` is nonzero, so arbitrary compatible lower data can have an obstruction at this step. Once existence is known, `H0(J0(4))=0`, from `J0(4)=P4 O(-2)`, makes the solution of (10) unique. Thus the entire actual leading `D0` is recovered from the already known lower jets and their exact transitions.

There is also a smaller formula for the required cocycle. Every entry multiplier in `Ad(T0)` has ordinary transverse degree at most two, including the quadratic term from the square of its lower entry. Harmonic transport of `P` would need order three and therefore vanishes. With all source, equation and scalar factors transported into chart i, PR780's harmonic-conjugation operators give

    F3_ij=a_i[ M2_ij(M_j)+M1_ij(R_j) ].                 (11)

Here `M2` is the order-two harmonic coefficient of conjugation on a matrix of weight eight, and `M1` is the order-one coefficient on a matrix of weight four. These are the same ordered operators as in PR780, applied at the present physical twists. Formula (11) has the positive sign because `F3` is the transported coefficient; the lower-truncation boundary is its negative.

Finally `K=aJ4` gives

    A1=a^2 M,    A2=a^2 R(P,M,T0),    A3=a D0(P,M,R,T0).

The uniqueness statement must be made **before multiplying by a**: `D0` lies in `J0(4)` with zero H0, whereas `A3` lies in `J0(6)=P4 O` and that larger coefficient bundle has nonzero H0. The actual factorization through `J4` is part of the supplied ladder and removes that apparent freedom. No division by `a` at its zeros is used.

## 7. What dependency has, and has not, been removed

PR713's actual scalar quotient can now be written using `R(P,M,T0)` in its eight-term formula. This determines the full actual leading square class from the lower data and their actual global transition law, rather than only the immutable quotient supplied by PR725. It does not determine its value without supplying those lower data.

In PR780 the fixed section is `K=a J4`, and `J4|3Q=a J3`. As `a` is q-independent, `K|3Q=a^2 J3`; therefore its weight-four second coefficient is exactly `A2=a^2 R(P,M,T0)`. The source factors are multiplied, never inverted at their zeros.

The distinction from earlier work is narrow: the old acyclic sequence and old kernel-Cech recovery recipe already existed; the specialized actual `J3` affine transport, its square-compatibility interface, and the resulting removal of PR713/PR780's independent `R4/A2` datum are the principal content proved here. The corollary then uses known actual fourth-lift existence and the old weight-zero coefficient bundle to recover `A3`, rather than claiming a new unobstructed extension theorem. All of `A1,A2,A3` are consequently fixed by the stated lower data, transitions and existing ladder. The first-subleading `B2,B3` data, the full fifth-boundary class modulo the exact second-symbol image, and all higher lifting and algebraicity questions remain open.

No actual source coefficients, points, derivatives, matrices, ranks, models, scans or large computations were evaluated. All work here is universal filtered algebra, regular-pair geometry and line-bundle cohomology. This is an authored mathematical proof, not a formal proof-assistant certificate.
