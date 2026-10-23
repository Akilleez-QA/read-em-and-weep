# Complete 55 harmonic + 10 trace arbitrary-qB coefficient maps

## Scope and exported construction

`universal_q_middle_quotient_coefficients.py` constructs the complete coefficient
space for the **prescribed** arbitrary-qB completion, modulo full C-source
homotopies. Its intrinsic target is

    V tensor Sym²(M9),       M9 = Gmix/Csource = A* tensor V* = P4+D5.

The public builder returns 55 harmonic and 10 trace-bookkeeping maps, each a
physical symmetric12-by-12 matrix linear in positive `(x,y,z)`, quadratic in
the free direction `a`, and linear in the free quartic `h`. Both marking frames
and every nonzero marking unit are retained. The trace maps are explicit
bookkeeping channels, **not** ten new free parameters in a fixed-trace problem.

The constructor also returns intrinsic9-by-9 or literal quotient9-by-9 tensors
through `frame='intrinsic'` or `frame='quotient'`. The default is the regular
physical representative `frame='physical'`. It does not construct physical
source columns or solve source feasibility.

## 1. A Cauchy decomposition with both binary frames explicit

Use the negative binary B2 for A and the positive binary B2 for V. The Cauchy
identity gives

    Sym²(A tensor V)
      = Sym²(A) tensor Sym²(V) + wedge²(A) tensor wedge²(V).

The five sectors and all their pair types are

    SS00 : 1
    SS04 : D5
    SS40 : D5
    SS44 : 1+A+V+2P4+2D5
    AA22 : P4+D5.

Here a pair of binary quadratics is split by normalized CG maps into degrees
4,2,0; the degree2 channel is alternating, the others symmetric. SS44 first
uses the positive B4 tensor B4 CG decomposition, followed by the physical
quartic inverse marking on the negative factor only. AA22 uses the canonical
inclusion into positive V tensor canonical A, then converts the canonical A
back to negative B2 by the checked physical cubic conjugation. There is no
identification of the two binary SL2 frames.

If `H_ab` is the matrix of these two pair labels and `I_n,I_m` their binary
CG inclusions, the literal leg tensor is

    K_(a,i),(b,j) = (I_n H I_m^t)_(a,b),(i,j).

For AA22, both small pair tensors are alternating, so their interleaved
9-by-9 tensor is symmetric. Ordered entries are used throughout: both
off-diagonal entries are present, with no hidden half convention.

The twelve pair inclusions have explicit apolar left inverses. Their exact
Gram constants, in the order returned by `middle_pair_routes`, are

    SS00/1                  9
    SS04/D5                 3
    SS40/D5                 3
    SS44/cg0/P4             451630080000
    SS44/cg0/D5             150543360/7
    SS44/cg1/A              1/2
    SS44/cg1/P4             1/2
    SS44/cg2/D5             7/12
    SS44/cg3/V              5/4
    SS44/cg4/1              5
    AA22/P4                 406467072000
    AA22/D5                 2167824384/49.

Every constant is verified by the whole symbolic Gram identity, not an
evaluated nonzero witness. With `G9=J2 tensor J2`, the pair metric is
`G81=G9 tensor G9`. If `I_t` is a pair inclusion of canonical type k and
`P_k` its exact typed projector, then

    I_t^t G81 I_t = c_t J_k P_k,
    L_t = J_k^(-1) I_t^t G81/c_t,
    L_t I_u = delta_tu P_k,
    sum_t I_t L_t = Sym_9.

Thus this is an exact full-space decomposition, not a character-only count.

## 2. All outer routes and coefficient matrix units

Apply the existing exact positive V tensor pair-type CG inclusions to each
of the twelve separate pair copies. Their thirteen distinct primitive outer
routes have explicit apolar inverses and full reconstructions. Composing
with the pair maps produces 36 separate simple target copies, with

    V tensor Sym²(M9) = 1+8A+8V+9P4+10D5,     dimension135.

For the complete target inclusions T_t and their explicit inverses L_t,
the checker verifies every cross product and the full ordered-entry identity

    L_t T_u = delta_tu P_type,
    sum_t T_t L_t = I3 tensor Sym_9.

The right side acts on all243 ordered tensor entries and has trace135.
Every actual constructor template is compared entrywise with the corresponding
composite inclusion, so route, sign, scaling, and both frame indices are fixed.

The seven harmonic source maps are reused from the independently audited
q8 coefficient package. They decompose the full25-dimensional source

    H25 = 1+A+V+2P4+2D5.

Their explicit projections M_s and right inverses N_s satisfy

    M_s N_u = delta_su P_type,
    sum_s N_s M_s = I25.

An additional trace D5 gives I30. This concerns the whole quadratic-parameter
space, not squares at selected directions. For
`a=k S²-2d ST-l T²`, let c0,...,c4 be the coefficients of a² before the
quartic marking, and let rho=d²+kl. The exact inverse is

    k²=c0,  kd=-c1/4,  kl=(4rho-c2)/6,
    d²=(c2+2rho)/6,  dl=c3/4,  l²=c4.

Each same-type source/target pair gives `F_(t,s)=T_t M_s`. The dual
coefficient functional is

    lambda_(t,s)(F) = tr(L_t F N_s)/dim(type).

The checked cross identities give delta_tu delta_sv on the returned maps;
Schur's lemma and the complete source/target reconstructions prove completeness.
The sector totals are

    SS00 :  1 harmonic + 0 trace
    SS04 :  6 harmonic + 1 trace
    SS40 :  6 harmonic + 1 trace
    SS44 : 31 harmonic + 6 trace
    AA22 : 11 harmonic + 2 trace.

## 3. Literal regular physical representatives, not equivariant R

The intrinsic leg index is `(negative binary A, positive binary V)`. The
literal D-coordinate quotient index is `(negative C-source dual, x/y/z dual)`.
The exact frame change on **each** tensor index is

    U = J2 tensor M,
    J2 = antidiag(1,-1/2,1),
    M = [[0,0,1],[-1,0,0],[0,1,0]].

Indeed a positive binary quadratic with coefficients `(c0,c1,c2)` corresponds
to the positive-linear polynomial `-c0*y+c1*z+c2*x`. Thus

    B9 = U K U^t,
    Bphysical = R B9 R^t,
    K = (U^(-1)D) Bphysical (U^(-1)D)^t.

The imported regular split obeys `DR=I9`, `RD+C Zeta=I12`, and `DC=0`.
No claim that R is equivariant is made or needed. The intrinsic quotient maps
are equivariant; any change of representative is handled by the full source
homotopy below. Denominators are nonzero marking units, never a positive
coordinate, q, or a vertex-ideal localization.

For a completely arbitrary physical symmetric-linear B, put

    P=RD,  M0=Zeta B,  N=Zeta B Zeta^t,
    F=B Zeta^t-CN/2.

The full234-coefficient identity is

    B-PBP^t = C F^t+F C^t.                            (1)

Likewise a section change `R'=R+CX` has

    R'B9R'^t-RB9R^t = C L^t+L C^t,
    L=R B9 X^t+C X B9 X^t/2.

These formulas retain C/C as well as both mixed C factors.

## 4. The entire completion and both source endpoints are transported

Let `q0=(xy+z²)/theta`, and let `Q_j=L2(q0 e_j)` be the prescribed full
degree-two completed legs. Let `H_i=L1((M0)^t_i)`, differentiating every
physical coefficient of M0. Since Q C=q0 C and all Euler partners of a
positive-polynomial C-source factor vanish, the completed difference in (1)
is exactly

    F_q(B-PBP^t) = sum_i S(C_i,l_i),
    l_i = [Q(M0)^t_i+q0 H_i-q0(CN)_i]/2.              (2)

Here S is the **unhalved** symmetric transvection. In particular the factor
1/2 in l is essential. Also `Q(M0)^t` is not `L3(q0(M0)^t)`; the coefficient
derivatives occur separately in H and must not be lost.

Equivalently, for each linear column f_i of F, the mixed coefficient of l_i
is q0 f_i, while its full VWW partner is

    Z_l = [Z_Q f_i+q0 Z1(f_i)]/2.

`verify_q_middle_quotient_boundary.py` checks (2) on all234 free coefficients,
as the whole18-by-18 symmetric tensor in `(mixed12,VWW6)` **before** exterior
contraction. Thus both higher weights and their cross terms are retained,
not merely equality of the lower q-middle. The exported
`projected_completion_boundary` returns every l_i through literal derivatives.

For the physical source arrow `alpha_C(e_i)=cm C_i`, take

    h = sum_i e_i [l_i,-]/cm,
    hd(phi)=sum_i l_i phi(e_i)/cm,
    T=alpha h+hd beta,
    Psource=h alpha,
    Pdual=beta hd=-Psource^t.

The checker verifies, with wholly free arrows and the fixed alternating
duality,

    T alpha-alpha Psource = hd(beta alpha),
    beta T-Pdual beta = (beta alpha)h.

After monad isotropy, this is a full cochain boundary with **both** source
endpoints, including the physical nonzero factor1/cm. Any global normalization
such as kAt/kappa multiplies the entire homotopy and both endpoints together.
No source correction is silently fixed to zero.

## Reproduction and limits

    python verify_q_middle_quotient_coefficients.py
    python verify_q_middle_quotient_boundary.py

The coefficient verifier checks the frozen qB package manifest
`8a51729d04e922910d8b5e61e7651fbc7b006ae2a0f6a5597335660e3636e2d2`
and every listed file before and after its run. No frozen file is edited.
All variables and marking units remain formal; there are no selected points,
actual-instance matrices/ranks, source feasibility solves, or external writes.

The conclusion is coefficient-space completeness for this specified completed
family modulo full C-source boundaries. It does not assert independence of
supported middle operators, disappearance of any A-source relation, equivalence
to every other q8 completion, vanishing of source-extension errors, or any
obstruction value.
