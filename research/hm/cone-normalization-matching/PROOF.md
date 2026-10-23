# Matching an independent cone source row by full scalar gluing

2026-10-23. Conditional written theorem. No actual source, coefficient,
parameter, point, derivative, matrix, primitive, instance rank or response
value is selected or evaluated. This is not formal certification or actual
packet authentication.

## 1. The dependency resolved, and exact inputs

PR908 constructs the source-response leg on the full GLOBAL cone complex.
It permits an independently chosen actual cone contraction, but correctly
requires matching to the ambient contraction used for the full lower y.
PR909's regular-divisibility exclusion was stated for two ambient
contractions. The present result extends that exclusion to an independent
cone contraction WITHOUT assuming it extends to an ambient contraction.
The chain comparison is rederived on Q for nonclosed degree-zero cochains.

The exact inputs are:

- PR908, `e49c18ba7bd8e6b817431b3ca13523f680d36bd1`,
  `research/hm/physical-global-cone-response/PROOF.md`, SHA256
  `aafd5ee2b8a0a1d0876886b4db361c05d2a34cc41ab59e44ecec54580061cfcc`.
  This supplies the full global cone image, canonical source membership,
  factor rows, and existence of a compatible ambient recovery.
- PR909, `ed5df772de551f83abfc0fee5b3bb494b3252b95`,
  `research/hm/normalization-divisor-exclusion/PROOF.md`, SHA256
  `824b6fdb62f835a21f42ad50b038c038a5c035a677f7a6cb454a31328fff1a35`.
  Only its regular coefficient-divisibility/sheaf cancellation argument is
  reused; it is not silently applied to an unextended cone contraction.
- PR866, `25b1d2927294fffbc393e6ac2285f5a58cfd6c60`,
  `research/hm/physical-source-normalization/PROOF.md`, SHA256
  `a7f6afe41fe569cb9a061a047b1d0a140fd198950cda6fe3bace6978f3cf0b14`.
  This fixes comparison orientation, the trace-free projection and the
  distinction between the full comparison operator and source-only rows.
- PR815, `0eaeca734b9e17142da2f1bdfd9a1721d0bb1d42`,
  `research/hm/affine-square-source-response/PROOF.md`, SHA256
  `78a0f462ffd0710d248658aaf95926f926297b0bae43aade85eb4c7fc934d236`.
  This supplies the marked coefficient types, full ambient y, affine term
  Q_i, source-response sign and the physical scalar target bundle.

All paths refer to Akilleez-QA/read-em-and-weep. INPUTS.json gives immutable
URLs and byte/blob bindings. Earlier geometric ancestry remains inherited.

## 2. Fixed input and separate realization/globality gates

Fix an arbitrary nonzero a in H0(L,O(2)), where L=P(W)=P1, and a nonzero
positive binary h in Sym4(U). Here U=Wprime is distinct from W. Fix the
canonical/independently compared full preceding data of PR908, so

    Y=V-bZ,    S=aY,    s=rS=a rY,

with Y of physical twist two and S of twist four. V and Z are closed
GLOBAL degree-one ambient cochains, so

    dY=0,    dS=0,    d_Q s=r(dS)=0.                         (C1)

No d_Q(s) term is discarded without this closure. More strongly, PR908's
canonical raw-cubic identity and global-complex comparison prove

    s in im(d_Q:C_Q^0->C_Q^1),

before choosing W or E. Thus a GLOBAL cone degree-zero primitive e with
d_Q e=s exists. Its existence is used below; no value is chosen or computed.
For any ambient lift E of e, PR908 recovers a compatible closed W by
qW=S-dE. This does not validate an unrelated supplied W.

Let A be an authenticated ambient contraction, including the full lower
projection y_A and all affine lower data of PR815. Write A_Q for its
restriction to the actual monad M_Q on Q. Separately supply B_Q, a regular
contraction of that SAME actual monad onto the SAME F_Q. It need not be the
restriction of an ambient contraction. Require:

1. A_Q and B_Q and their physical frame comparisons are regular on a cover
   inducing a cover of the ENTIRE L, including div(a). No localization at a
   or meromorphic repair is allowed.
2. All twists are tensor twists of these same contractions. The source
   comparison is transported into A's physical frame before extraction.
3. The actual marked weight-four extraction, n8, determinant/equation
   lines and physical twists are retained. The factor a has transverse
   cover weight zero. This is not an arbitrary supported-block projection.
4. Both source rows are the PR908 factors of their authenticated full
   cone projections on im(d_Q). We do not extend either row to arbitrary
   degree-one inputs or infer either row from its values on closed sections.

Finally assume the correctly paired ambient response rho_A is global,
with full y_A and the full affine term Q_A fixed. This is an independent
physical/lower-data prerequisite, not a conclusion of cone exactness.
Global gluing of the mixed scalar defined below is another SEPARATE
hypothesis; none of the preceding factorization statements proves it.

## 3. The nonclosed comparison identity on the cone

All maps in this section are on M_Q; abbreviate A_Q and B_Q by A and B.
Let partial be the monad differential and delta its Hom differential.
For each contraction use

    p i=1,  partial H+H partial=1-i p,
    partial i=0,  p partial=0.

H denotes the degree-minus-one contraction homotopy, not the source h.
No side conditions H^2=Hi=pH=0 are assumed. Put

    g_t=p_B^(t) i_A^(t),       g_0=p_B i_A.

The maps p_A^(t)i_B^(t) are actual inverses: inserting
1-i_A p_A=partial H_A+H_A partial between the chain maps p_B and i_B
makes both error terms zero. Thus comparisons and inverses are regular;
this is not inversion of a source coefficient.

For ANY degree-zero cochain u:M_Q->M_Q(t), including a nonclosed one, put

    delta u=partial^(t)u-u partial,
    P_A^t(u)=(p_A^(t)u i_A)_0,
    P_B^t(u)=(g_t^-1 p_B^(t)u i_B g_0)_0.

The second expression is B in A's frame. First, the B contraction gives

    i_B g_0=i_A-partial H_B i_A.

Because p_B^(t) partial^(t)=0, retaining the full delta u gives

    p_B^(t)u i_B g_0
      =p_B^(t)u i_A+p_B^(t)(delta u)H_B i_A.       (C2)

Next, the twist-t A contraction gives

    g_t p_A^(t)=p_B^(t)-p_B^(t)H_A^(t)partial^(t).

Because partial i_A=0, again retaining delta u gives

    g_t p_A^(t)u i_A
      =p_B^(t)u i_A-p_B^(t)H_A^(t)(delta u)i_A.    (C3)

Subtract (C3) from (C2), multiply by g_t^-1 and take trace-free parts:

    P_B^t(u)-P_A^t(u)=R_t^Q(delta u),              (C4)
    R_t^Q(v)=
      (g_t^-1 p_B^(t)(vH_B+H_A^(t)v)i_A)_0.

This calculation is valid for NONCLOSED u. R_t^Q is defined on every local
degree-one input v. No step identifies a nonclosed cochain with an
intrinsic adjoint, applies a closed-cochain homotopy formula to s, or
restricts the nonclosed ambient X=aJ3 in place of its full y_A.

Apply (C4) ONLY to the global degree-zero cone primitive u=e, for which
delta e=s. Using the two already authenticated source-row factorizations
and the same marked trace extraction gives

    eta_i=Lambda_B,i^Q(s)-Lambda_A,i^Q(s)
         =tr(n8_i [R_4^Q(s)]_[4]).                 (C5)

Closure of s follows independently from (C1), and also from delta^2 e=0.
No hidden derivative of s, omitted delta s term, or actual primitive
value enters (C5). Changing e by a global closed cochain does not change
either row by PR908's actual global-cone coefficient theorem.

## 4. Regular divisibility, not a presumed global cone adjoint

Since s=a rY and the contractions are O_Q-linear tensor-compatible maps,

    R_4^Q(a rY)=a R_2^Q(rY).

The marked weight-four extraction retains a, since its cover weight is
zero. Consequently

    eta_i=a_i xi_i,
    xi_i=tr(n8_i [R_2^Q(rY)]_[4]),                 (C6)
    xi_i in (Sym12(U) tensor O_L(-2))(U_i).

The last type is PR815's twist-four trace coefficient bundle tensored
by O(-2). It is not the negative variable W being replaced by U. The
positive binary degree remains twelve while physical twist drops by two.
Each xi_i is regular even at div(a), since it is constructed by a regular
operator and extraction, not by evaluating eta_i/a_i at a root.

If the eta_i glue to a global section of T=Sym12(U) tensor O_L, then
injectivity of multiplication a:T(-2)->T forces the xi_i to glue with
the T(-2) transitions. The coefficient sheaf is locally free and nonzero
a is a non-zero-divisor on the integral L. This cancellation is valid
also at multiple zeros. It is ONLY the extracted xi that is forced to
glue; the full R_2^Q(rY) is not assumed or proved global.

Now H0(L,T(-2))=0. Therefore

    eta glues on all of L  iff  eta=0.             (C7)

This is the sheaf argument of PR909, applied AFTER a cone-specific
realization has been proved. It does not apply the global actual-cone
coefficient-vanishing theorem to eta, and does not assert eta itself is
the coefficient of a closed global cone adjoint.

## 5. Matching the independent cone row to the fixed ambient lower data

In the common A frame, define

    rho_A,i=Q_A,i+a^3h tau_i(y_A,i)-a^3h Lambda_A,i^Q(s),
    rho_B,i=Q_A,i+a^3h tau_i(y_A,i)-a^3h Lambda_B,i^Q(s).

The first is the correctly paired response, using PR908's agreement with
the restricted ambient contraction. The second uses the independent cone
row but keeps the SAME full ambient lower projection and affine data.
Their exact difference is

    rho_B,i-rho_A,i=-a^3h eta_i.                    (C8)

As in PR815/866, multiplication by the nonzero a^3h is a sheaf injection

    T -> Sym16(U) tensor O_L(6).

It is injective at source zeros as a sheaf map, not by pointwise division;
multiplication by nonzero h is injective in the binary polynomial ring.
With rho_A global, (C8) therefore shows rho_B glues iff eta glues.
Combining with (C7) proves the conditional criterion

    rho_B glues on the entire base
      iff Lambda_B^Q(s)=Lambda_A^Q(s) on every chart
      iff rho_B=rho_A.                              (C9)

This matches the trace response ON THE CERTIFIED CANONICAL SOURCE s.
For a whole claimed source family the gates and scalar gluing must hold
for the whole family. A single source test does not prove operator equality
on im(d_Q), and trace equality does not assert equality of the entire
weight-four matrix response.

## 6. Exact improvement and remaining work

The independent cone contraction B_Q need not extend ambiently. Its actual
cone chain maps, homotopy, regular tensor compatibility, marking and frame
alignment are still genuine certificates. When these and the fixed full
ambient lower packet are authenticated, full scalar gluing replaces a
separate source-value calibration for this canonical source. It does not
replace physical authentication by an arbitrary row passing an overlap test.

No globality of eta or rho_B follows from row factorization alone. The
unrestricted thirteen-dimensional associated-graded trace space remains
nonzero. Punctured-cover regularity allows poles in xi and is insufficient.
An unrelated supplied W still requires its ambient compatibility check.
No full y is recovered from cone data, no scalar is evaluated, and no
ambient/fifth-order norm, fifth boundary or original proof repair is proved.
