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
