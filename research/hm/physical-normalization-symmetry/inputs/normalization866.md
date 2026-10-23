# Mixed-contraction normalization defect for the physical source response

New bounded deduction, 2026-10-23. Written mathematics, not Lean certification.
No actual HM coefficients, points, matrices, ranks, or response values are selected.

## Result

The lower nonclosed projection and the source-response row in PR815 cannot be
normalized independently. After genuine ambient frame alignment, their changes
are the SAME cone-level scalar `eta`. A hybrid construction using the lower
projection from contraction A and the source row from contraction B has error

    rho_AB - rho_AA = -a^3 h eta.                         (N1)

Thus `eta=0` is necessary and sufficient for the hybrid scalar to equal the
correctly paired scalar, as a regular section. There is an explicit compensating
counterterm `+a^3 h eta`, computable from the corrected differential source and
the cone restrictions of the comparison operators, without constructing E_h.
Overlap gluing alone is weaker: it only requires the eta_i to be a global trace
section, and the imported trace sequence has a 13-dimensional space of such
sections. This dimension counts possible undetected scalar-error directions in
the affine reconstruction problem, not realized HM source changes.

## 1. Pinned premises and novelty boundary

Read the live PR1 coordination on 2026-10-23, through comment 6355805504. Codex
owns SourceTraceFactorization, Source2TraceKernel, FirstNormalCorrection,
QuadraticProjectorCompatibility and the abstract PR816 defect formalization.
This note does not replace or re-prove those units.

Exact sources read:

1. PR815 at `0eaeca734b9e17142da2f1bdfd9a1721d0bb1d42`,
   `research/hm/affine-square-source-response/PROOF.md`, especially (17), (20)-(25).
   https://github.com/Akilleez-QA/read-em-and-weep/blob/0eaeca734b9e17142da2f1bdfd9a1721d0bb1d42/research/hm/affine-square-source-response/PROOF.md
2. PR816 at `eed6010347fcebc21aef30413b0e1da3be68a9b4`,
   `research/hm/nonclosed-frame-transfer/NONCLOSED-FRAME-TRANSFER-EXACT-DEFECT.md`.
   https://github.com/Akilleez-QA/read-em-and-weep/blob/eed6010347fcebc21aef30413b0e1da3be68a9b4/research/hm/nonclosed-frame-transfer/NONCLOSED-FRAME-TRANSFER-EXACT-DEFECT.md
3. At `8d8b5be4ce62c3055bb53be9e16d29cc63072f04`,
   `research/hm/order-four-quadratic-load/ACTUAL-FOURTH-BOCKSTEIN-AS-A-FIFTH-NEIGHBORHOOD-ADJOINT-BOUNDARY.md`.
   https://github.com/Akilleez-QA/read-em-and-weep/blob/8d8b5be4ce62c3055bb53be9e16d29cc63072f04/research/hm/order-four-quadratic-load/ACTUAL-FOURTH-BOCKSTEIN-AS-A-FIFTH-NEIGHBORHOOD-ADJOINT-BOUNDARY.md

In particular dJ4=q^4 W_h and the fifth-boundary interpretation are OLD inputs,
not new results of this note. The exact nonclosed comparison is also an OLD
input. The added statement is the mixed-contraction scalar error, its
source-only cone-level correction, its necessary/sufficient matching test,
and the strict weakness of scalar overlap tests.

## 2. Alignment and tensor compatibility are required, not assumed away

On one regular ambient chart take two contractions A and B of the same full
monad M onto its actual cohomology F. For each twist t, use their compatible
tensor twists to M(t), not separately chosen splittings. Both satisfy

    p i=1,  d h+h d=1-i p,  d i=0,  p d=0.

The contraction homotopies need not satisfy h^2=0, h i=0, or p h=0. Work in
characteristic zero, so tracefree projection is defined. Let

    g_t=p_B^(t) i_A^(t),       g_0=p_B i_A,
    P_A^t(X)=(p_A^(t) X i_A)_0,
    P_B^t(X)=(g_t^-1 p_B^(t) X i_B g_0)_0.         (N2)

Here P_B means B expressed in the A frame, not B's untransported entries.
The inverses and cocycles are supplied by PR816. Frame, determinant, equation
line, coordinate and physical-twist factors must all be transported before
harmonic extraction. The needed ambient alignment is through the order used
by y=[q^3](P(aJ3))_[16]. Agreement of frames only on Q is not a substitute.

For a degree-one map T:M->M(t), define the regular local operator

    R_t(T)=(g_t^-1 p_B^(t) (T h_B+h_A^(t) T) i_A)_0. (N3)

This is defined on ALL local degree-one maps, not only on im(d). Transporting
the known PR816 formula gives

    P_B^t(X)-P_A^t(X)=R_t(dX).                       (N4)

Compatible tensor twists and O-linearity imply

    R_(t+2r)(q^r T)=q^r R_t(T).                     (N5)

This implication uses the actual same contraction tensored by line bundles.
If a proposed implementation supplies unrelated maps at twists 2, 4 and 10,
(N5) is an additional certificate to check; (N4) at each twist alone does not
prove it. This explicitly separates chain contraction, physical-frame
alignment and q-multiplication compatibility.

## 3. The new paired-normalization theorem

Use PR815's fixed actual cochains and signs:

    X=a J3,                    dX=q^3 S,
    E=E_h,                     dE=T=S-q W_h,
    S=a(V_h-b Z_a),             J4=X-q^3 E.          (N6)

The twists of X, E, S, W_h are 10, 4, 4, 2. No endpoint or middle channel
is discarded. Put A0=a^3 h; the name A0 avoids confusing this multiplier with
contraction A. In the common frame let

    tau(u)=tr(n8 u),
    y_A=[q^3](P_A^10(X))_[16],
    y_B=[q^3](P_B^10(X))_[16],
    eta=tau([R_4(T)|Q]_[4]).                         (N7)

Equation (N5) gives R_4(q W_h)=q R_2(W_h), so

    eta=tau([R_4(S)|Q]_[4]).                         (N8)

Thus eta needs only cone restrictions of the operators in (N3), the source S,
and the fixed physical n8/weight extraction. It does not need a primitive E.
In particular the variation of a third-normal coefficient is controlled by
a zeroth-normal operator after the factor q^3 in dX is retained.

Apply (N4)-(N6) to X. The resulting difference is q^3 R_4(S). Taking its
total-weight-sixteen q^3 coefficient, with q of weight four, proves

    tau(y_B)-tau(y_A)=eta.                            (N9)

Now assume the authenticated *full-global-source* factorization of PR815
for each contraction, in the same common frame:

    Lambda_A(dE)=tau([P_A^4(E)|Q]_[4]),
    Lambda_B(dE)=tau([P_B^4(E)|Q]_[4]).

The existence and uniqueness of these maps on im(d) is not a new claim here.
Apply (N4) to E to obtain the second normalization equation

    Lambda_B(T)-Lambda_A(T)=eta.                     (N10)

Consequently

    tau(y_B)-Lambda_B(T)=tau(y_A)-Lambda_A(T).        (N11)

This establishes simultaneous contraction independence of the COMBINATION;
neither summand is guaranteed to be separately contraction-independent by
these premises. A nonzero eta for genuine HM contractions is not claimed.
Both terms of (N3) matter. Scalar central pieces vanish under the tracefree
projection and tau, but the generic comparison formula need not vanish.

The paired projections of J4 agree modulo q^4, by the old closure identity
and (N4). Therefore the leading ladder and lower q, q^2 coefficients that
define PR815's Q agree in this common ambient frame. Keep this fixed Q and
define a deliberately mixed scalar

    rho_AB=Q+A0 tau(y_A)-A0 Lambda_B(T),
    rho_AA=Q+A0 tau(y_A)-A0 Lambda_A(T).             (N12)

Subtracting and using (N10) proves (N1). Multiplication by the fixed nonzero
a^3 h is injective on the regular binary coefficient sheaf, including at
its divisor as a SHEAF map. Hence

    rho_AB=rho_AA  if and only if  eta=0.             (N13)

No value of a or h is inverted. This is not a fiberwise cancellation claim.
An implementation can equivalently add the source-only counterterm +A0 eta
to rho_AB. For a whole claimed source subspace, compatibility is the operator
identity eta|_(that subspace)=0, not a test on one chosen source value.

Important domain distinction: (N8) permits evaluating R_4(S), because R_4 is
defined on every local degree-one map. It does NOT permit replacing
Lambda_B(S-q W_h) by Lambda_B(S). S need not lie in im(d), and Lambda is
defined only there. Although q W_h disappears from the CONE NORMALIZATION
DEFECT, the corrected full source S-q W_h remains the only certified input
to the response row. Its next-boundary contribution is not erased.

## 4. Gluing is strictly weaker than correct normalization

Apply the construction on the chart cover. Write T_trace=Sym^12 U O_L and
R_rho=Sym^16 U O_L(6), as in PR815. Multiplication by A0 is an injective
global map T_trace->R_rho. Let theta_ij and lambda_ij be the respective
transitions, so A0_i theta_ij=lambda_ij A0_j. If the correctly paired rho_AA
is global, (N1) gives

    rho_AB,i-lambda_ij rho_AB,j
      =-A0_i (eta_i-theta_ij eta_j).                (N14)

Injectivity shows that the mixed scalar glues if and only if the eta_i form
a global section of T_trace. Correctness requires that section to be ZERO.
Therefore a scalar overlap test cannot by itself detect a global nonzero
normalization error.

This is a real nonzero space in the imported reconstruction problem, not
just a formal possibility: L=P(W)=P^1 and U is two-dimensional, so

    H0(T_trace)=Sym^12 U,   dim H0(T_trace)=13.

The exact sequence imported from PR815 is

    0 -> U O_L(-1) -> E_weight4(4) --tau--> T_trace -> 0.

Since H0 and H1 of the kernel vanish, H0(tau) is an isomorphism. Hence every
global eta has exactly one global coefficient shift v with tau(v)=eta.
Replacing e by e-v preserves its affine overlap law and changes its scalar
square datum by -A0 eta, exactly the error in (N1). This proves that the
affine gluing/square reconstruction can consistently absorb a wrong global
normalization. The thirteen directions are an information-theoretic blind
spot of THOSE TESTS. This does not assert they all occur from genuine HM
contraction changes, that they lift to global ambient adjoints, or that
they are freedom in the actual corrected source problem.

### Conditional one-fiber calibration criterion

There is a sharper stopping condition once (N14) has established gluing.
Over the algebraically closed base field, let x be ANY base point for which
the binary form A0(x) is nonzero. Such points form a nonempty open set because
A0 is a nonzero global section. A global eta in Sym^12 U O_L is constant in
the L direction, so evaluation at x is an isomorphism

    H0(Sym^12 U O_L) -> Sym^12 U.

Multiplication by the nonzero binary form A0(x) is injective in the binary
polynomial ring. Hence, AFTER gluing has been proved,

    rho_AB(x)=rho_AA(x) as full binary degree-sixteen vectors
       if and only if eta=0 globally.                         (N15)

This does not select or evaluate an actual point. It identifies a bounded
kind of possible normalization certificate: one complete eligible fiber
calibration, together with global overlap, can replace a redundant family
of fiber tests. A single numerical evaluation in the binary variables is
not such a certificate; it is just one functional and cannot test the full
13-component error vector. A fiber on the zero divisor of A0 is also useless
for this conclusion. No pointwise cancellation at a source zero is used.
To use (N15), its reference fiber must itself be independently authenticated;
comparison to an unknown rho_AA does not supply that missing reference.

## 5. Checkable interface and remaining premise

A future independently produced physical response packet can be checked
against an existing lower projection without constructing E_h by supplying:

1. Full actual contractions and ambient physical-frame comparison (N2)-(N3).
2. Tensor/q compatibility (N5), not merely per-twist chain identities.
3. The full-global-basis row identities L_A=Lambda_A D and L_B=Lambda_B D.
4. The source-only comparison eta from the COMPLETE corrected source, with
   eta=0 if the lower projection is left unchanged, or the counterterm in
   (N12). Equality just on overlaps is insufficient by section 4.

This note removes ambiguity about the normalization-matching condition and
identifies the finite normal jet needed for its correction. It does not
construct the actual i,p,h, physical marking maps, n8 rows, y, or Lambda.
It does not evaluate rho16 or beta4, prove a source exclusion, or repair the
original theorem. The numerical-free tests accompanying this note verify
the new mixed/paired q-adic identities in a universal free-word model; they
are supporting diagnostics, not Lean or actual-HM certification.
