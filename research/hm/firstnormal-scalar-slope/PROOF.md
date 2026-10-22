# Scalar first-normal slope excludes universal local vanishing

Work over k=C(L) in the fixed harmonic frame of PR713, PR716 and PR724. Put S=k[X,Y], n=u[[fg,-f²],[g²,-fg]], with degrees f=3, g=5, (f,g) regular and u nonzero. Let A=a²h with a nonzero scalar and h a nonzero quartic. Let T be a weight-four first-normal nilpotent lift of n. Set P=A n and M=A T+s n+B1(A,n), for a scalar s. Let R be a weight-four solution of the q² square equation for J=P+qM+q²R; C is its cubic scalar square coefficient. Define K=[C/(ah)] in (S/(f))8 whenever h divides C; this divisibility is proved below from these local hypotheses.

Pinned dependencies:
- PR713: https://github.com/Akilleez-QA/read-em-and-weep/blob/5b3943980ecaef78ee7f56fbc015d40955fb24f0/research/hm/leading-vertex-obstruction/PROOF.md
- PR716: https://github.com/Akilleez-QA/read-em-and-weep/blob/2a602d811b904def02bd56518fb0549e2911ff3e/research/hm/firstnormal-trace-variation/PROOF.md
- PR718: https://github.com/Akilleez-QA/read-em-and-weep/blob/2411fcd92acd738d0d8af7bebc79ee9191b276ef/research/hm/trace-obstruction-target-reduction/PROOF.md
- PR724: https://github.com/Akilleez-QA/read-em-and-weep/blob/2061379fe77ec4c82b5f05c7a11d3b7454b97a04/research/hm/canonical-trace-isomorphism/PROOF.md

The theorem concerns abstract local inputs. None of the variations below is asserted to be an actual global completion change.

## 2. Scalar first-normal changes have a controlled slope

We next vary the abstract local input s, not the actual global completion. All products in this section are in the associative, commutative scalar harmonic coefficient algebra, with ordered matrix multiplication. Let

 N=n+qT,     N*N=q² d2 Id+q³ d3 Id+O(q⁴),
 F=A+q s.

Define W to be the q² coefficient of F*N. Set Z=R-W. Then the given truncated matrix J=P+qM+q²R satisfies

 J=F*N+q² Z+O(q³).

The q² square equation therefore says

 tr(nZ)=-A d2.                                      (6)

For a scalar λ in k, put

 Jλ=J+λ q N.

Its leading coefficients are P, M+λ n, R+λ T. These are regular of the same weights, and its first-normal coherence has scalar coefficient s+λ. The coefficients of q and q² in Jλ² still vanish. Indeed N² starts at q², and the coefficients below q² of {J,N} vanish. At coefficient q²,

 {J,N}=2F*N²+q²{Z,n}+O(q³)
       =q²(2A d2+tr(nZ)) Id+O(q³)
       =q² A d2 Id+O(q³).

Consequently

 C(P,M+λ n,R+λ T)-C(P,M,R)=λ A d2.                  (7)

The λ² term begins at q⁴ and cannot contribute. In particular h-divisibility is preserved, and

 K(P,M+λ n)-K(P,M)=a λ [d2] in (S/(f))8.             (8)

This slope law is a root-cause consequence of associativity and the q² square equation; it needs no cubic harmonic expansion.

### Existence and divisibility over the universal regular-pair locus

The nonzero-slope argument is not vacuous because the displayed local hypotheses, including h-divisibility, have solutions over the generic coefficient field. Here are algebraic proofs. Write

 F*N=P+qM+q²W+q³V+O(q⁴).

The coefficients W,V are regular of weights four and zero. Define E=sc(M²+B1(P,M)+B1(M,P)+B2(P,P)), where sc is half the matrix trace. The q² coefficient of (F*N)²=F²*N² says

 E+A tr(nW)=A²d2.

Thus E is divisible by A without any restriction on h. The trace map from weight-four matrices to S12 is surjective: its kernel is the known two-dimensional space l[[f/2,0],[g,-f/2]], while its domain and target have dimensions fifteen and thirteen. Hence an R exists for arbitrary first-normal input and nonzero A. Equivalently choose Z with tr(nZ)=-A d2 and set R=W+Z.

To verify cubic divisibility as well, define

 Psi(Z)=sc(TZ+ZT+B1(n,Z)+B1(Z,n)).

Ordered associativity gives the cubic cross term of F*N with q²Z as

 A Psi(Z)+s tr(nZ)+B1(A,tr(nZ)).

Since J=F*N+q²Z−q³V modulo q⁴, the q³ scalar is

 C=A²d3+(2As+B1(A,A))d2+B1(A²,d2)
       +A Psi(Z)+s tr(nZ)+B1(A,tr(nZ))−A tr(nV).

Use (6) and the scalar associativity identity

 B1(A,A)d2+B1(A²,d2)=A B1(A,d2)+B1(A,A d2)

to obtain the exact factorization

 C=A(Ad3+s d2+B1(A,d2)+Psi(Z)−tr(nV)).              (10)

Thus every such abstract local solution has h-divisible C, not merely the actual one. This proves the generic family used in the exclusion exists. It does not provide actual global completions. For two such solutions differing by D=l[[f/2,0],[g,-f/2]], their cubic scalars differ by A Psi(D), since tr(nD)=0. By PR718, f divides Psi(D), so K is independent of R; the notation K(P,M) is therefore justified.

## 3. The slope is lift-independent and not universally zero

If T changes to T+D with D=l[[f/2,0],[g,-f/2]], the change in d2 is

 sc(TD+DT+B1(n,D)+B1(D,n))+D²
   =Psi(D)+l² f²/4.

PR718 proves f divides Psi(D). Therefore [d2] in (S/(f))8 is independent of the nilpotent lift T. It may be computed with PR724's canonical T:

 x/u=(6FG''-16F'G'+20F''G)/112,
 y/u=(F')²/5-3FF''/10,
 z/u=5GG''/36-(G')²/9,

where F=f(1,t), G=g(1,t) are unspecified polynomials and all derivatives are formal.

For clarity the bounded verification uses ordinary multiplication, not B2 expansion. In the quadric chart x=1,y=t,z=t²+q with q=xz-y², a binary harmonic lift of degree d has expansion

 H(p_d)=P+q P''/[2(d-1)]
            +q² P''''/[8(d-1)(d-3)]+O(q³).

For x^m H(t,Q), with m=d/2 and Q=q/x², the Laplacian is x^(m−2)((m−1/2)H_Q−QH_QQ−H_tt/4). Thus its coefficient recurrence is c_(j+1)=c_j/[2(j+1)(d−1−2j)], proving the displayed formula. Here only d=6,8,10 and d-4=2,4,6 occur. Put n=(uFG,-uF²,uG²) for diagonal, upper, lower entries, and let T=(x,y,z) above. Their ordinary q and q² coefficients are

 a1_i=T_i+n_i''/[2(d_i-1)],
 a2_i=T_i''/[2(d_i-5)]+n_i''''/[8(d_i-1)(d_i-3)],
 (d_diag,d_upper,d_lower)=(8,6,10).

Since the square's first two coefficients vanish, its ordinary q² coefficient equals its harmonic q² coefficient d2. Thus

 d2=a1_diag²+a1_upper a1_lower
       +2n_diag a2_diag+n_upper a2_lower+n_lower a2_upper.

Formal product-rule simplification modulo F gives exactly

 [d2](1,t)= (u² G²/48)(3(F'')²-8F'F''') mod F.      (9)

The accompanying verify.py checks this fixed-size identity with free jet symbols. It assigns no actual coefficients or points and substitutes no regular pair or selected model.

### The slope is nonzero for every regular pair

In fact (9) never vanishes for a regular pair, including pairs with repeated factors in f. For this proof choose an SL2 linear frame in which the dehomogenized cubic F has degree exactly three. Such a frame exists over the infinite field k: choose the Y-axis away from the zero set of the nonzero cubic. This is an existence argument in the proof, not an actual point evaluation. The harmonic product and canonical T are SL2-equivariant, so nonvanishing of the intrinsic class [d2] may be proved in this frame.

Write the arbitrary cubic as F=c3 t³+c2 t²+c1 t+c0, with c3 nonzero. Formal differentiation gives

 3(F'')²−8F'F'''=−36c3²t²−24c3c2t+12c2²−48c3c1.

This is a nonzero quadratic. It cannot be divisible by F, whose degree is three. Regularity makes G a unit in k[t]/(F); since u is nonzero and the characteristic is zero, (9) is nonzero in that quotient. Hence [d2] is nonzero in (S/(f))8. No actual coefficients were obtained, substituted or evaluated.

Together with (8) and the established existence/divisibility, this rigorously excludes universal local vanishing from the listed hypotheses. For any fixed admissible input, the λ-family is an affine line with nonzero direction a[d2] in the three-dimensional immutable quotient. At most one λ can have K=0. In particular there are always abstract local inputs satisfying all the listed equations and divisibility for which K is nonzero. This is not an assertion that actual global source geometry permits changing s. Additional actual-global coherence may prescribe the particular s and R, and may make their K zero. Any proof for the actual base must use that extra information.

## Remaining actual dependency

The immutable class for the fixed actual input remains unevaluated. The slope theorem proves that the named local coherence and square equations alone cannot force it to vanish: actual global information prescribing the first-normal scalar input and its remaining compatibility is essential. The two modular divisions in the separate modular-elimination theorem give an exact criterion from P,M without evaluating the actual R. No actual fourth-square vanishing or later Bockstein conclusion is inferred.
