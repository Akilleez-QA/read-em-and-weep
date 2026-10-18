# Root-line and old-connection arrow: closed on the stated elliptic curve

## Result and precise scope

The actual legal frames, squared-line identification, and old-connection formula in the pinned first-order source are consistent. They imply, on a common frame,

    (nabla_j - nabla_i)|N^k = -(k/2)(m_j-m_i) dlog x,

and contraction with V gives -k q(i,j)/2, where q(i,j)=(m_j-m_i)y/x. This proves the geometric input connecting the raw engine's distinct nu, gamma, and q formulas. It is stronger than matching three formula strings: the line bundle, legal localization, and frame-transport subtraction are proved below. No physical computation, source execution, owner/jet/residual evaluation, polynomial matrix product, or aggregate admission is performed or implied.

## Source anchors

All three pinned documents below are under commit 08b73637d4136f91606aad332c46cafd064417f8 in Akilleez-QA/read-em-and-weep:

- research/hm/current-scalar-residual-attribution/first-order-source.md, lines 33–45: exact opens, e0/e1, ell transition, gamma, and instruction to transport the old connection at infinity; section 4: rf, ga, q and frame-normalization dictionary.
- research/hm/current-scalar-residual-attribution/ambient-second-jet.md, section 1: C, N=O_X(Theta), and the global vector field V=y partial_x + (3x²−1)/2 partial_y.
- research/hm/current-scalar-geometric-dependencies/frames-and-poles.md, sections 2 and 4: infinity ratios and legal channels.

Public first source: https://github.com/Akilleez-QA/read-em-and-weep/blob/08b73637d4136f91606aad332c46cafd064417f8/research/hm/current-scalar-residual-attribution/first-order-source.md

Read-only raw-engine anchor: inputs/raw-engine-excerpt.txt, excerpted source lines 126–138 and 151–154; full source snapshot SHA256 c9804022b362277d63217c7674c4d6d3dff5941ae4210c30f51f3b5cf3868da9. Its nu is product(y/x)^m, its q is delta(m)y/x, and its diagonal subtraction is -k m y/[x(x²−1)]. The current proof binds those displayed expressions, not execution of the guarded class.

## 1. Divisors establish the line convention and legal frames

Work over a field of characteristic zero. Let O denote infinity and P_a=(a,0), a=0,1,-1. On the smooth curve y²=x³−x,

    div(x)=2P_0−2O,
    div(y)=P_0+P_1+P_-1−3O,
    div(y/x)=P_1+P_-1−P_0−O.

These follow directly: at each P_a, 3a²−1 is nonzero, so y is a uniformizer and x−a has order two. At infinity put t=1/x, z=y/x². Then z²=t(1−t²); z is a uniformizer at O and ord_O(t)=2. Thus x has order −2 and y order −3.

Use the divisor-sheaf convention O(D): a rational function f represents a section when div(f)+D is effective. For N_C=O_C(O), e0=1 has section divisor O, so is a frame on U0=C\{O}. The rational function e1=y/x has section divisor P_1+P_-1−P_0, all supported outside U1=C\{P_0,P_1,P_-1}; it is therefore a frame on U1. In particular, e1 is NOT a globally regular function on U1: it has a simple rational-function pole at O, which is exactly absorbed by O_C(O). These prescribed two rational frames identify the source's one-factor N with O_C(O); if the ambient line is their external product on C^4, it is O(sum_r pr_r^*O). Identifying the ambient symbol Theta with that divisor is a separate convention/premise, not a conclusion from one curve.

On U0, A=k[x,y]/(y²−x³+x). Its intersection with U1 is Spec A[1/(x(x²−1))]. Here x, x²−1, and y are units; e1/e0=y/x is a unit. Thus all transition expressions and their inverses used below live on the actual overlap, not on an artificially enlarged affine domain.

## 2. Squared line and old local connections

Set ell0=1 and ell1=x as rational sections of O_C(2O). The section divisor of ell1 is 2P_0, so ell1 is a frame on U1, including O. The transition direction is explicitly ell1=x ell0. The curve equation gives

    e0²=ell0,
    e1²=(y²/x²)ell0=((x²−1)/x)ell0=(1−x^-2)ell1.

The coefficient h=1−x^-2 is a regular unit throughout U1: in infinity coordinates it is s=1−t², with zero set precisely the excluded P_±1. It has no zero or pole at O. This is an isomorphism of squared line bundles on the legal opens, not just an identity of rational functions on a dense set.

Let nabla^(m) be the local connection whose induced connection on N² is flat in ell_m. These are LOCAL connections whose differences form a Cech cocycle; a global flat connection on the positive-degree N is neither claimed nor needed. If nabla e_m=gamma_m e_m, then nabla(e_m²)=2 gamma_m e_m². Consequently

    gamma0=0,
    gamma1=(1/2) dlog h=dx/[x(x²−1)].

Writing f=y/x, the curve equation yields

    dlog f = [ (3x²−1)/(2x(x²−1)) − 1/x ] dx
             = (x²+1)dx/[2x(x²−1)].

A change e1=f e0 gives gamma(in e0)=gamma(in e1)−dlog f. Hence

    nabla^(1)−nabla^(0)
      =gamma1−dlog f
      =−dx/(2x).

For arbitrary bits m_i,m_j and the power N^k this is

    A_ij=−(k/2)(m_j−m_i)dlog x.

Contraction with V(x)=y now proves exactly

    alpha_m=gamma_m(V)=m y/[x(x²−1)],
    V(log nu_m)=m y(x²+1)/[2x(x²−1)],
    q_ij=(m_j−m_i)dlog x(V)=(m_j−m_i)y/x,
    A_ij(V)=−k q_ij/2.

In particular q is NOT the refined frame logarithmic derivative. Substituting log nu for q would be a genuine mismatch, but the inspected raw engine does not do so. Its -k alpha_m subtraction is exactly the old-connection correction in B=−(dU)U^-1−diag(k gamma_m).

## 3. Infinity transport, including actual units

Let B=k[t,z]/(z²−t(1−t²)). The inverse-x chart is C\{P_0}; U1=Spec B[1/s] with s=1−t². U0 intersects this chart in D(t). Near O, z is a uniformizer, and a genuine local frame for N is n_infty=1/z. Since

    e1=z/t=(z²/t)n_infty=s n_infty,

both e1 and n_infty are valid frames on U1; s is a unit. This independently checks the pole cancellation in section 1. The old frame ell1=x=1/t satisfies ell1=s n_infty², and e1²=s ell1, exactly as above.

Under x=1/t and y=z/t²,

    gamma1 = −t dt/s,
    dlog x = −dt/t,
    dlog(y/x) = −(1+t²)dt/(2t s),
    V(t)=−z,       V(z)=(3t²−1)/2.

Therefore gamma1(V)=zt/s, q_ij=(m_j−m_i)z/t, and

    [gamma1−dlog(y/x)](V)=−z/(2t)=−q_01/2.

The apparent t denominator in the last expression is allowed: a 0/1 overlap excludes O. Gamma1 itself is regular on U1. If one CHANGES the actual frame to n_infty, its coefficient becomes gamma1−dlog s=+t dt/s; that is another consistent gauge, not permission to set gamma1 to zero.

The source's normalized squared ratios at infinity are also exact: relative to the old squared reference ell1=x ell0,

    e0²/ell1=t,      e1²/ell1=s.

Their half-logarithmic derivatives are dt/(2t) and −t dt/s. These are normalized ratio jets; they do not assert the existence of a globally chosen regular square-root function sqrt(t). The bit-zero ratio is only needed where t is invertible. Multiplication of every finite normalized root ratio by formal t^(1/2) gives these squares and the same half-log derivatives. This bookkeeping does not replace or reset the old connection in the retained actual e_m frames.

## Verification and remaining boundary

verify_one_curve.py checks the original 12 rational identities plus additional one-curve identities and active negative controls, including the squared-line relation, both distinct logarithmic derivatives, the connection difference, and infinity transport and contraction. The divisor/local-ring argument above supplies the geometric regularity that rational identity checks alone cannot establish.

This closes the one-factor root-line -> local old connections -> common-frame Cech difference/q arrow for the declared source conventions. Conditional on the ambient external-product line and tensor-product connections, pullback and summation give the four-factor version. These ambient identifications are not established by the one-curve checker. It does not close primitive-model identity, differentiation-engine correctness, source-generator equality beyond these leaves, or the full conditional ID0 theorem. All such premises remain separately required.

## 4. Audit at every potentially exceptional point

The two opens cover C: the three omitted finite points belong to U0, and O belongs to U1. At all other points every displayed denominator is a unit in the relevant chart. At P_a, use y as uniformizer: x−a has order 2 and dx has order 1. At O use z: t has order 2 and dt has order 1. Hence:

- At P0, e1 has function order −1; at P±1 it has order +1. All three are excluded from U1. The zero connection in frame e0 is regular there.
- At O, e1 has function order −1 but section order 0 in O(O); ell1 has function order −2 but section order 0 in O(2O). The unit s is 1 at O. The gamma1 form has order 3, as does its evaluation on the nonvanishing V.
- As a rational one-form, gamma1 has simple poles at P0 and P±1; they cause no irregularity on its domain U1. Its coefficient ga in dx has higher function pole orders, which must not be confused with orders of the form.
- dlog x has simple poles only at P0 and O; it is regular at P±1. Its contraction y/x has simple poles at P0 and O and zeros at P±1. Every 0/1 overlap excludes all four points. For equal bits the difference is identically zero on that chart intersection.
- dlog(y/x) has simple poles at all four points. It is only used for common-frame transport on the overlap, where it is regular.

The expression V=−z partial_t in the pinned frames text is shorthand for action on functions of t. As a derivation of the entire curve coordinate ring it is V=−z partial_t+(3t²−1)/2 partial_z. This full formula preserves z²−t(1−t²), and is nonzero at O and at P±1; the finite formula is nonzero at every P_a. It is therefore incorrect to treat −z partial_t alone as the whole derivation on k[t,z]/(z²−t(1−t²)).

## 5. Exact product consequence and remaining premises

If X=C^4 and N=external tensor product of O_C(O), use e_m=product_r pr_r^*e_(m_r), ell_m=product_r pr_r^*ell_(m_r), and the tensor sum of the local old connections. Then

    A_ij|N^k = −(k/2) sum_r (m_jr−m_ir) pr_r^*dlog(x_r),
    A_ij(V_r) = −(k/2)(m_jr−m_ir)y_r/x_r.

These are identities of differences of local connections in a common frame and their evaluations, respectively. No claim of a global holomorphic connection on a positive-degree line is made. Full source semantics still require independent agreement of the ambient N, transition conventions, tensor connection, vector fields, retained actual frames, and interpretation of B. Primitive matrices, source-generator equality beyond these scalar leaves, jets, residuals, and the conditional ID0 theorem remain outside this certificate.
