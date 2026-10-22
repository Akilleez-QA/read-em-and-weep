# Generic elimination of the fourth-order even adjoint branch

## Theorem and remaining gates

For a general smooth inversion-even quadric Q, let C be its positive fixed conic, I=I_(C/Q), and G=End_0(F_Q)(4). The actual fourth-order positive boundary d_4 is injective. Consequently

    H0(I^4G)=0,
    H0(I^3G)_+=0.

Thus even global adjoint sections have leading normal order only0 or2, while odd sections have leading order only1 or3. This is an actual elimination of the quartic-leading positive branch, not an inference from expected rank.

On a nonempty open of the smooth-even family, the actual derived finite-neighborhood obstruction complex has parity ranks

    72 -> 68          and          78 -> 82.

Its positive part is filtered by an actual45-to68 second-jet boundary followed by an actual27-to-cokernel conic boundary. Its odd part remains an actual78-to82 obstruction. The same H1 cokernel eigensheaves give precisely the same Fitting failure ideals as the original85-pencil.

There is a supplementary actual odd-order bound: after shrinking to a further nonempty open, the36-to18 local factor ell_3 has rank at least12. Hence

    h0(I^3G)_- <=24.

No injectivity of the odd factor or full odd boundary is claimed. The remaining positive and odd conditions for exact corank four are unresolved.

## 1. Actual plane input

GENERIC-DOUBLED-CONIC-SIMPLICITY.md proves that, for a general balanced smooth conic C in the positive plane, the actual plane projective class

    eta_C in H1(C,B_C(-2))

has coefficient span at least two in H0(B_C)=sl_2. Equivalently H0(B_R|2C)=0, or the actual squared-conic6-to12 multiplication is injective.

That proof uses the actual stable Steiner bundle and a first-order deformation of the invariant conic. In the zero-class case its next plane class psi is nonzero because H1(B_R(3))=0. The exact scheme-theoretic identity (q0+t f)^2=0, t^2=0 gives q0^2=-2t f q0 and therefore d eta(f)=-2f psi. Complete binary multiplication and A5 irreducibility give a five-dimensional derivative image, which cannot consist entirely of rank-one tensors. The alternative nonzero invariant class has rank three immediately. Thus the plane input is independent of a selected conic or matrix evaluation.

The present note uses the proved plane theorem only for its actual generic conclusion.

## 2. Affine dependence forces the actual top factor to be injective

Fix such a balanced conic C=(q_+=0), and vary the negative quadratic block q_- in Sym^2 W. The actual even equation is q_++q_-=0, and the intrinsic second-normal class satisfies

    xi(q_-)=zeta_C-eta_C tensor q_-.

No choice of representative or formal product neighborhood is involved. In coefficient notation relative to T=H1(O_P1(-4)), write eta_i in sl_2 and zeta_i(w) as sl_2-valued binary quadratics. The top commutator tensor has components

    [xi_i,xi_j]
      = [zeta_i,zeta_j]
        -q_-([eta_i,zeta_j]+[zeta_i,eta_j])
        +q_-^2[eta_i,eta_j].

Because eta_C has coefficient span at least two, some pair eta_i,eta_j has nonzero commutator. Along any nonzero negative quadratic direction q0, the coefficient of t^2 at q_-=t q0 is therefore nonzero. Thus the actual commutator tensor is not identically zero in the negative-block family.

The previously proved exact top-factor criterion says that nonzero commutator tensor is equivalent to injectivity of

    ell_4:E_4 -> H1(gr^6G),       dimensions15 ->63.

This actual local map factors the global boundary

    d_4:E_4 -> H1(I^5G)_+,       dimensions15 ->83.

It follows that d_4 is injective on a nonempty open of negative blocks. That open meets the nondegenerate-block open defining smooth quadrics. All classes vary algebraically over the balanced conic family, so these fiberwise nonempty opens give a nonempty open in the irreducible smooth-even quadric family. Consequently the assertion holds for general smooth even Q.

This proof establishes nonvanishing in the actual family through a universal highest coefficient. It does not select q0 numerically or evaluate an actual presentation matrix.

## 3. Exact lower-order detection

The existing balanced-conic theorem gives H0(I^5G)=0. The boundary d_4 has kernel H0(I^4G)_+, so its injectivity proves positive fourth-order vanishing. The fourth graded piece is even, hence

    H0(I^4G)_-=H0(I^5G)_-=0.

Therefore H0(I^4G)=0. The third graded piece is odd, so in positive parity

    H0(I^3G)_+=H0(I^4G)_+=0.

These are scheme-theoretic ideal-power statements. Thus restriction to O_Q/I^4 is injective on the entire section space, and restriction to O_Q/I^3 is already injective on the positive eigenspace. There is no assertion that arbitrary compatible finite jets extend globally.

## 4. The reduced actual derived obstruction complex

Write J_4=G/I^4G. The balanced normal graded pieces of orders0,1,2,3 have H1=0, characters +,-,+,- and section dimensions

    27, 42, 45, 36.

Consequently H1(J_4)=0 and its section parities are(72,78). The exact restriction sequence, H0(I^4G)=0, and the uniform higher vanishings H2(G)=H3(G)=0 imply that I^4G has cohomology only in degree one. The actual indices chi(G)_+=4 and chi(G)_-=-4 give

    h1(I^4G)_+=68,       h1(I^4G)_-=82.

For the universal family pi over the resulting open, the relative ideal powers and finite neighborhoods are flat. Their fixed fiber cohomology dimensions and vanishings give vector bundles

    J=pi_*(G/I^4G),       ranks(+,-)=(72,78),
    K=R1 pi_*(I^4G),      ranks(+,-)=(68,82).

The actual restriction triangle gives

    R pi_*G = [J -> K],

with J in degree zero. These bundles are not declared trivial. The complex is a presentation of the same actual derived pushforward as the ambient85-pencil, which retains its source parameter twist O(-1).

In particular both presentations have canonically the same H1 cokernel eigensheaves. The positive failure ideal is their Fitt_0, computed by68-by68 minors in the finite-jet presentation or37-by37 minors in the actual ambient positive block. The odd failure ideal is their Fitt_4, computed by78-by78 minors or44-by44 minors, respectively. These are exact equalities of ideal sheaves attached to the same cokernels, not comparisons based only on rank differences.

## 5. The remaining positive and odd interfaces

The even part of I^2G/I^4G is the actual second graded piece. Its H0 is E_2 of dimension45 and its H1 vanishes. Thus the new positive boundary is exactly

    d_2:E_2 -> H1(I^4G)_+,        dimensions45 ->68,

with

    ker d_2=H0(I^2G)_+,
    coker d_2=H1(I^2G)_+.

Writing k_2=dim ker d_2, its cokernel has dimension23+k_2. The actual conic restriction boundary is

    d_0:E_0 -> coker d_2,          dimensions27 ->23+k_2,

and H1(G)_+=coker d_0. Hence positive excess vanishes exactly when this actual d_0 is onto. In particular k_2<=4 is necessary, but neither it nor d_2 injectivity has been proved.

On the nonempty intersection with the independently proved lower-good even open, this45-to68 presentation and the earlier64-to87 power-Koszul presentation have the same actual kernel/cokernel and represent R Gamma(I^2G)_+. No preferred19-dimensional matrix cancellation is asserted.

The odd staged interface remains

    d_3:E_3 -> H1(I^4G)_-,         dimensions36 ->82,
    d_1:E_1 -> coker d_3,          dimensions42 ->46+k_3,

where k_3=dim ker d_3. Odd vanishing requires both stages injective. The fourth-power detection does not prove either requirement.

## 6. A new generic lower bound for the odd local factor

The actual local factor ell_3:E_3->H1(gr^5G) has dimensions36-to18. For fixed C and q_-=t q0 its coefficient of t is, up the fixed sign,

    (sl_2 tensor H0(O_P1(2)) -> sl_2)
       tensor (Sym^3 W --q0--> Sym^5 W).

The first map is s tensor f -> [eta_C(f),s], where contraction of eta_C uses the Serre multiplication pairing into H1(O_P1(-2)), a one-dimensional trace line. It is onto when the coefficient span of eta_C has dimension at least two. Indeed the annihilator of im(ad a) under the nondegenerate trace pairing is the one-dimensional centralizer of a. The annihilator of the sum for two independent a,b is their zero common centralizer, so the commutator images span sl_2.

The second map is injective for every nonzero binary quadratic q0 and has rank4. Thus this leading coefficient of the actual ell_3 pencil has rank12. Rank lower semicontinuity, or the leading coefficient of a maximal nonzero minor, implies that generic actual ell_3 has rank at least12. This is an existence/rank theorem from the actual affine dependence, not a selected coefficient computation. It can be imposed simultaneously with smoothness and ell_4 injectivity, since all are nonempty open conditions in each relevant irreducible family.

Since ell_3 factors the global d_3, its kernel contains H0(I^3G)_-. Therefore

    h0(I^3G)_- <= dim ker ell_3 <=36-12=24.

This controls only the third-leading odd subspace. It does not turn its formal kernel into global sections, assert rank18, or prove full odd vanishing.

## Scope

These results prove an actual generic geometric reduction: the fourth-order even branch disappears, and the odd third-order compatibility factor has rank at least12. The final positive45-to68/27-to-cokernel and odd obstructions remain actual unresolved maps. No selected HM/source coefficients, actual rank evaluations, scans, experiments, or external writes enter this deduction.
