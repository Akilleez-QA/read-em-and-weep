# Vanishing scalar leading jets determine four exact residual kernel bundles

## Theorem and scope

Use the actual source, pure injection, scalar-target factorization, and notation of SCALAR-TARGET-SATURATION-AND-NORM-TORSION.md. Assume the scalar target is O_T(a), and that its nonzero divided pure section f in H0(O(a,6))^G has POSITIVE exact diagonal order k. Then the universal invariant filtration leaves precisely these cases:

    a=18, k=2: N=ker(m)=S7(-16),    (c1,c2)=(-26,181);
    a=18, k=6: N=ker(m)=S5*(-1),   (c1,c2)=(-6,15);
    a=14, k=4: N=ker(m)=S3(-10),   (c1,c2)=(-18,83);
    a=12, k=3: N=ker(m)=W O(-9),   (c1,c2)=(-18,81).

All are exact isomorphisms of G-equivariant bundles on P2, including the discriminant and finite base loci, not merely generic-fiber descriptions.

The a=18 cases apply to target types IV and VII when their leading diagonal scalar vanishes. The a=14 case applies to type VI when both the low coupling mu and the leading diagonal scalar lambda vanish. The a=12 case applies to type III when its low V O(4) component is zero: its scalar invariant space automatically has exact diagonal order three. No actual target type, coupling, or diagonal order is selected here. When the leading diagonal scalar is NONZERO, the same-root blocks need not vanish and this theorem makes no kernel-bundle claim.

The actual image I, its double dual, and its finite singularity length are also determined:

    a=18,k=2: I**=S19(-1),  length(I**/I)=136;
    a=18,k=6: I=I**=S7*(1), length=0;
    a=14,k=4: I**=S15(-3),  length(I**/I)=44;
    a=12,k=3: I**=S13(-2),  length(I**/I)=60.

The divisorial target quotient cycles are respectively

    D_(S19/I) = Delta;
    D_(S19/I) = 5 Delta + nu_*div(F12(r));
    D_(S15/I) = 3 Delta;
    D_(S13/I) = 2 Delta.

Here F12 spans the degree-12 binary invariant line. The norms of its vertical divisor have degree 12, while Delta has degree 2. Thus the target defects have degrees 2,22,6,4, matching d=26,6,18,18 via d=a+10-deg(D_(H/I)). Finite singularities of the image are retained, not discarded.

## 1. Positive diagonal order removes the same-root blocks

Set R(r,s)=D(r,s)^2 f(r,s). For w in W, the actual residual Cartan vector b(s)w is ell_s^7 w, with the fixed Cartan multiplication normalization. Therefore

    delta_r(q0 b(s)w) = (1/8) d_s R(r,s)[w],

where d_s is the homogeneous directional derivative in the second binary vector, with r and its actual boundary held fixed. This differentiation does NOT freeze the varying boundary in r; it differentiates only the independent source root s.

In these four cases k>=2, so R is divisible by D^(k+2), with k+2>=4. At s=r its first three source-root jets vanish. Consequently

    delta_r(q0 b'(r)w)=0 for every w.

Indeed b'(r)w=7 ell_r^6 v w is a combination of the first two pure-power derivatives at r. These are among the vanished jets. The established actual division formula therefore gives, at distinct roots, no same-root block and the cross-root formula

    m_r(w_s)=-(1/8) d_s R(r,s)[w_s]/D(r,s)^2.

Natural root-value coordinates are used; there are two complementary-root denominators. The two target rows use disjoint root copies of W. This statement is NOT asserted when k=0.

## 2. The exact divisors common to the two gradient coordinates

Write f=D^k h, with h not divisible by D. Then

    d_s R = D^(k+1) [(k+2) h d_s D + D d_s h].

The factor D^(k+1) is exact at the generic point of D, because h|D is nonzero and d_s D is a nonzero covector there. Away from D, an irreducible factor g of h with multiplicity e contributes e-1 to the common gradient divisor if g depends on s, and e if g depends on r only. This follows from Euler's identity and differentiation in characteristic zero: the two gradient coordinates recover R by contraction with s, and a nonvertical irreducible factor cannot divide both its source derivatives.

The following invariant-divisor argument determines every such factor needed here. A nonempty G-stable effective divisor on T x T which does not contain D has a nonzero invariant diagonal restriction. Its total bidegree is therefore at least 12, the smallest positive binary-icosahedral invariant degree. A defining section is invariant because G has no nontrivial characters.

For a=18,k=2, h has bidegree (16,4) and total degree 20. It is reduced: a repeated prime factor would give a G-stable reduced orbit cycle of total degree at most 10, contrary to the preceding bound. A nonzero vertical part must have degree 12 and be F12(r). Dividing h by it would leave an invariant biform of degree (4,4). That space is spanned by D^4, forcing D to divide h, a contradiction. Thus h is reduced and has NO vertical factor.

For a=14,k=4, h has bidegree (10,2) and total degree 12. The same repeated-factor argument proves it is reduced. A vertical part would have degree at least 12 but its first degree is at most 10, so none exists.

For a=12,k=3, h has bidegree (9,3) and total degree 12. It is the unique indicated polarization of F12. The preceding repeated-factor and vertical-degree arguments again show it is reduced with no vertical factor. The scalar invariant filtration has dimensions 1,1,1,1,0,0,0, so exact order three is forced.

For a=18,k=6, h has bidegree (12,0) and is a nonzero multiple of F12(r). This polynomial is reduced: any repeated orbit of roots would have size at most six, whereas a nonempty invariant divisor on T has degree at least twelve.

Accordingly the EXACT common divisors of the two components of d_s R are

    D^3,                 for a=18,k=2;
    D^7 F12(r),          for a=18,k=6;
    D^5,                 for a=14,k=4;
    D^4,                 for a=12,k=3.

No isolated gradient basepoint is removed by this statement.

## 3. Saturated root syzygies determine the global kernel

Use coordinates (x,y) on T x T in which x is the SOURCE root and y is the other, target root. Swap the two variables in the preceding gradient and divide by its exact common divisor. This gives a nonzero covector

    alpha: W tensor O -> O(p,q)

whose two coordinates have no common divisor, with

    (p,q)=(4,17), (0,1), (2,11), (3,10)

in the four cases, respectively. Its image is I_Z(p,q), where Z is a finite scheme, and its saturated kernel is a line bundle. Since det W is trivial, the exact sequence is

    0 -> O(-p,-q) -> W tensor O -> I_Z(p,q) -> 0.

This line-bundle assertion includes the basepoints: the quotient is torsion-free, so the kernel is reflexive on the smooth root surface and hence invertible. The absence of a common divisor fixes its first Chern class. Equivariance fixes its linearization, because G is perfect.

The actual source is nu_*[W tensor O(-6,0)] tensor O_P(1). Tensor the preceding sequence by O(-6,0), then by nu*O_P(1)=O(1,1), and push forward by finite nu. This gives a saturated inclusion

    N0=nu_*O(-5-p,1-q) -> E4,

with torsion-free quotient nu_*I_Z(p-5,q+1). A finite pushforward of this torsion-free sheaf is torsion-free on the integral base: every nonzero base function remains a nonzerodivisor after pullback. Since N0 agrees with the actual kernel off the discriminant and both are saturated in E4, uniqueness of saturation gives N=N0 on ALL of P.

The pushforward identity

    nu_*O(u,v)=S_(u-v)(v)

now gives N=S7(-16), S_-5=S5*(-1), S3(-10), and S1(-9)=W O(-9), respectively. This proves the exact bundle claims without independently assigning values at the double root.

## 4. Actual image, double dual, and finite lengths

The same exact source quotient proves

    I = nu_*I_Z(p-5,q+1),
    I** = nu_*O(p-5,q+1),
    length(I**/I)=length(Z).

The second equality follows because its right-hand side is locally free (finite-flat pushforward of a line bundle) and differs from I only at finitely many points. The length is unchanged by finite pushforward over C. The two sections of O(p,q) form a regular sequence at their finite common-zero scheme; hence

    length(Z)=c1(O(p,q))^2=2pq.

This yields lengths 136,0,44,60. Swapping the root factors, which does not change their pushforward, gives the stated double duals S19(-1), S7*(1), S15(-3), S13(-2).

There is also an exact description of their maps into H. Before pushforward, the cross-root formula identifies the quotient line on the source root, after swapping, with O(q+1,p-5) on the target root. Its map to O(a+1,0) is multiplication, up to a fixed nonzero scalar, by

    D^(k-1) V(r),

where V=F12 in the second case and V=1 in the other three cases. The degrees agree:

    q+1+(k-1)+deg(V)=a+1,
    p-5+(k-1)=0.

Since k>=2 this is a regular morphism on the whole root surface, not a rational interpolation rule. Its finite pushforward is the unique extension I** -> H of the actual image embedding. Taking its determinant gives the norm of this multiplier, proving the four displayed target defect cycles, including their exact discriminant multiplicities.

## 5. Chern and nondegenerate-form checks

For every n>=1, c1(S_n)=n-1 and c2(S_n)=n(n-1)/2. Twisting a rank-two bundle by O(t) adds 2t to c1 and adds t c1+t^2 to c2. These identities give

    N=S7(-16): c1=-26, c2=181;
    N=S5*(-1): c1=-6, c2=15;
    N=S3(-10): c1=-18, c2=83;
    N=W O(-9): c1=-18, c2=81.

Their normalized second Chern defects c2-c1^2/4 are respectively 12,6,2,0, all consistent with the established even nonnegative defect theorem. The corresponding actual image Chern pairs are (16,290), (-4,16), (8,116), and (8,118), and their differences from the double-dual second Chern classes are exactly 136,0,44,60.

The source-form theorem requires a nonzero det(q_N) in degrees 42,2,26,26, respectively. In the middle case its degree is two, so its divisor is exactly the discriminant conic: the invariant quadratic space on P(Sym^2 W) is one-dimensional. This is compatible with, and does not contradict, the nondegenerate-source-form theorem. No isotropic kernel is introduced.

## 6. The kernel-form discriminant is the root discriminant times a square

There is a stronger form-theoretic consequence. Let alpha(x,y) be the divided root covector of Section 3 and identify its kernel generator with a vector v(x,y) in W using the fixed alternating form on W. The wedge

    J(x,y)=v(x,y) wedge v(y,x)

is an invariant biform of bidegree (p+q,p+q), anti-invariant under root exchange. Hence J=D g, where g is symmetric of bidegree (p+q-1,p+q-1), and descends to an invariant section G on P of degree p+q-1=d-6.

In the natural root evaluation frames, q pairs the two different root copies by their W wedge. The determinant of the evaluation map for either rank-two root pushforward contributes exactly one D. These two evaluation factors cancel in the determinant comparison for the restricted form. It follows that, up to a fixed nonzero scalar,

    nu*det(q_N) = J^2,
    det(q_N) = Disc times G^2.

One may verify the evaluation factor without any rank experiment: for a finite-flat double cover, the value evaluation in the basis (1,z) has determinant s-r. Line-bundle twists only change this identity by units. For the source E=S6* the evaluation determinant is a section of O(1,1); the same is true for nu_*O(-5-p,1-q). Thus the same D factor occurs in both places and cancels as stated.

The nondegenerate-source-form theorem now says G is NOT the zero section. Its degrees in the four cases are respectively 20,0,12,12. Thus the exact kernel discriminant divisors have the constrained forms

    Delta + 2 div(G20),
    Delta,
    Delta + 2 div(G12),
    Delta + 2 div(G12_prime).

This refines the necessary degree-only discriminant condition; it does not identify any actual G20, G12, or G12_prime. In particular all odd-multiplicity discriminant components are confined to the root discriminant conic.

## Verification and limitations

verify_scalar_zero_jet_kernels.py checks only universal character multiplicities, invariant-degree exclusions, root-pushforward degrees, Chern identities, and finite lengths. No actual coefficient, selected residual matrix, evaluated fiber rank, or local-model experiment is used. The differential and saturation arguments above are mathematical proofs, not numerical tests.

This theorem identifies conditional first-order kernels. It does not show that these cases actually occur, that their kernels survive higher smoothing, or that the full HM proof repair is complete. No external publication is performed here.
