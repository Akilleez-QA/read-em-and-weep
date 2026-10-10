# An explicit first-order Čech lift from a split-complex transgression

## Scope

This note gives a coefficientwise algebraic proof of a first-order module lift for the determinant-trivial Horrocks–Mumford pullback on \(C^4\), once the specified local constant-differential splittings have been supplied. It gives an explicit rational formula rather than an unspecified Čech primitive. It does not compute a second-order obstruction.

The local splitting identities, frame transitions, and determinant normalizations are hypotheses that an implementation must verify. Point evaluations of the resulting equations are useful regression tests, but are not the proof of the identities below.

## 1. Conventions and local data

Let \(C\) be the smooth completion of \(y^2=x^3-x\), put \(X=C^4\), and let \(V_i\) be the invariant vector fields dual to \(dx_i/y_i\). Set
\[
\pi=V_1\wedge V_2+V_3\wedge V_4,\qquad
\mu_1(f,g)=\tfrac12\pi^{rs}(V_rf)(V_sg).
\]
Repeated vector-field indices are summed, with \(\pi^{12}=\pi^{34}=1\), \(\pi^{21}=\pi^{43}=-1\).

Represent left-module coordinates by rows. Classical transition matrices satisfy
\[
g_{jk}g_{ij}=g_{ik}.
\]
Choose determinant-one frames, so \(g_{ij}\in\mathrm{SL}_2\). Their column counterparts are \(G_{ij}=g_{ij}^{t}\), with \(G_{ik}=G_{ij}G_{jk}\).

Use the total Čech–forms product
\[
(\alpha\otimes\eta)(\beta\otimes\zeta)
=(-1)^{(\deg\eta)(\deg\beta)}
(\alpha\smile\beta)\otimes(\eta\wedge\zeta),
\]
where \(\deg\beta\) in this exponent is the Čech degree. Contraction is \(\iota_{V_r\wedge V_s}=\iota_{V_s}\iota_{V_r}\).

Let \(N=\mathcal O_X(\Theta)\). Use the complex
\[
K=[5N^{-1}\longrightarrow15N\longrightarrow10N^3
      \longrightarrow2N^5]
\]
in degrees \(-1,0,1,2\), with sole cohomology \(E\) in degree zero. On each refined affine chart, assume a degree-preserving invertible change of basis \(U_i\) puts the differential into the same constant split form: a rank-two zero-differential summand and contractible summands. The rank-two basis is the chosen determinant-one frame of \(E\).

The complex determinant has total \(N\)-exponent
\[
-5(-1)+15(1)-10(3)+2(5)=0.
\]
Its fixed trivialization induces a trivialization of \(\det E\). Local cohomology bases must be normalized against this trivialization before using the \(\mathrm{SL}_2\) formulas below.

## 2. An exact transgression without a cyclicity assumption

For each degree of \(K\), choose local old connections \(\nabla_i\). Let
\[
\nabla_i'=\nabla_i+B_i
\]
be the local connections that are flat in the split bases \(U_i\). Write
\[
A_{ij}=\nabla_j-\nabla_i
\]
after transporting both connections to frame \(i\). Thus \(A\) is an End\((K)\)-valued Čech one-cocycle of one-forms. The corresponding new cocycle is
\[
A'=A+\delta B.
\]

Set
\[
\mathcal T=\operatorname{str}
 \bigl(B A+A B+B\,\delta B\bigr).
\]
This is a scalar Čech one-cochain of two-forms. In the declared total product, \(B\) has total degree one and \(A\) has total degree two. Since \(\delta A=0\), the derivation rule gives the exact identity
\[
\delta\mathcal T
 =\operatorname{str}\bigl((A+\delta B)^2-A^2\bigr).
\tag{2.1}
\]
No replacement of \(BA+AB\) by \(2BA\) is made: Alexander–Whitney products do not have the strict cyclicity that would justify that replacement.

Every \(\nabla_i'\) preserves the differential of \(K\), because that differential is constant in its split basis. Consequently \(A'\) is a degree-zero chain endomorphism with coefficients in one-forms. Supertraces of products of such endomorphisms equal traces of the induced products on cohomology. In a split complex this is a direct block-matrix identity: the paired contractible diagonal blocks cancel. Therefore
\[
\operatorname{str}((A')^2)
 =\operatorname{tr}((A^E)^2),
\tag{2.2}
\]
where \(A^E\) is the difference cocycle of the frame-flat connections on \(E\).

Equations (2.1)–(2.2) are identities of cochains, not only cohomology classes.

## 3. The old connections and the gerbe representative

On each elliptic factor, let \(\ell_i\) be the original local frame of \(N^2\), with transition \(x\). Refine the cover so that \(N\) has a frame \(e_i\), and write
\[
e_i^2=u_i\ell_i.
\]
The connection induced from the frame-flat connection on \(N^2\) has local connection form
\[
\gamma_i=\tfrac12 d\log u_i
\]
in frame \(e_i\). On \(N^{k}\), use \(k\gamma_i\).

For the refinement
\[
U_0=C\setminus\{\infty\},\qquad
U_1=C\setminus\{(0,0),(1,0),(-1,0)\},
\]
one can take \(e_0=1\), \(e_1=q=y/x\). Then \(u_0=1\) and \(u_1=1-t^2\), where \(t=1/x\). These are invertible on the respective charts.

In the old \(K\) frames, the splitting connection and its difference are thus
\[
\nabla_i'=d-(dU_i)U_i^{-1},\qquad
B_i=-(dU_i)U_i^{-1}
     -\operatorname{diag}(k_r\gamma_i),
\tag{3.1}
\]
with \(k_r=(-1,1,3,5)\), repeated according to the summand ranks.

Let \(\theta_0\) be the Čech–forms representative
\[
\theta_0=\tfrac12\sum_r d\log x_r.
\]
The difference cocycle for the old connection on \(N^k\) is \(-k\theta_0\). Hence
\[
\operatorname{str}(A^2)
 =(-5+15-90+50)\theta_0^2=-30\theta_0^2.
\tag{3.2}
\]

Write \(Q_{rs}=q_r\smile q_s\). The exact antisymmetric representative of
\(\Pi=\iota_\pi(\theta^2)/2\) is
\[
\Pi_{\mathrm{AW}}
 =-\tfrac18(Q_{12}-Q_{21}+Q_{34}-Q_{43}).
\]
The desired shorter left-module gerbe cocycle is
\[
b=\tfrac{15}{4}(Q_{12}+Q_{34}).
\]
Define the ordinary pointwise product cochain
\[
r_{ij}=q_{1,ij}q_{2,ij}+q_{3,ij}q_{4,ij}.
\]
The cocycle identities for the \(q_i\) give
\[
\delta r=-(Q_{12}+Q_{21}+Q_{34}+Q_{43}),
\]
so
\[
-15\Pi_{\mathrm{AW}}=b+\tfrac{15}{8}\delta r.
\tag{3.3}
\]

Combining (2.1)–(3.3), define
\[
\boxed{\displaystyle
s=-\tfrac14\iota_\pi\mathcal T-\tfrac{15}{8}r.}
\tag{3.4}
\]
Contraction commutes with restriction and the Čech differential. Therefore
\[
\delta s=b-\tfrac14\iota_\pi
                  \operatorname{tr}((A^E)^2).
\tag{3.5}
\]

## 4. Row/column calibration

With column transitions \(G_{ij}=g_{ij}^{t}\), the frame-flat difference cocycle is
\[
A^E_{ij}=-dG_{ij}\,G_{ij}^{-1}.
\]
The total Čech–forms product yields
\[
\operatorname{tr}((A^E)^2)_{ijk}
=-\operatorname{tr}
 \bigl(dG_{ij}\wedge dG_{jk}\,G_{jk}^{-1}G_{ij}^{-1}\bigr).
\]

Put
\[
C_{ijk}=g_{ik}^{-1}\mu_1(g_{jk},g_{ij}).
\]
Transposing this expression reverses the matrix order. Swapping the two skew bivector indices then gives exactly
\[
\boxed{\displaystyle
\operatorname{tr}(C)
=\tfrac12\iota_\pi\operatorname{tr}((A^E)^2).}
\tag{4.1}
\]
Thus (3.5) is
\[
\delta s=b-\tfrac12\operatorname{tr}(C).
\tag{4.2}
\]
The second factor \(1/2\) here is the scalar projection of a rank-two matrix; it explains the factor \(1/4\) in (3.4).

## 5. The trace-free equation

For a determinant-one matrix \(g\), define
\[
K(g)=\mu_1(g^{-1},g).
\]
Its logarithmic derivatives are traceless, and
\[
K(g)=-\tfrac12\pi^{rs}
 (g^{-1}V_rg)(g^{-1}V_sg),
\qquad \operatorname{tr}K(g)=0.
\]

On a triple overlap abbreviate
\[
a=g_{ij},\quad b_0=g_{jk},\quad c=b_0a,\quad
P_r=a^{-1}V_ra,\quad
Q_r=a^{-1}b_0^{-1}(V_rb_0)a.
\]
Then
\[
C=\tfrac12\pi^{rs}Q_rP_s
\]
and
\[
K(a)+a^{-1}K(b_0)a-K(c)
 =\tfrac12\pi^{rs}[Q_r,P_s].
\]
For traceless \(2\times2\) matrices,
\[
[Q,P]=2QP-\operatorname{tr}(QP)\,\mathrm{id}.
\]
Consequently the following is an exact rational identity:
\[
\boxed{\delta K=2C-\operatorname{tr}(C)\,\mathrm{id}.}
\tag{5.1}
\]

Set
\[
x_{ij}=s_{ij}\,\mathrm{id}-\tfrac12K(g_{ij}),
\qquad u_{ij}=g_{ij}x_{ij}.
\tag{5.2}
\]
Using (4.2) and (5.1) gives
\[
\delta x=b\,\mathrm{id}-C.
\]
Equivalently,
\[
u_{jk}g_{ij}+g_{jk}u_{ij}-u_{ik}
=b_{ijk}g_{ik}-\mu_1(g_{jk},g_{ij}),
\]
which is the complete first-order left-row module equation.

This proof is coefficientwise: it does not rely on numerical or rational-point sampling.

## 6. Fixed-line-chart simplification and remaining execution

If all three charts refine one fixed old line chart, then \(A=0\) and \(b=0\). Since the supertrace of \(B_i\wedge B_i\) vanishes,
\[
\mathcal T_{ij}=-\operatorname{str}(B_i\wedge B_j),
\qquad
s_{ij}=\tfrac14\iota_\pi
              \operatorname{str}(B_i\wedge B_j).
\]
This is a useful exact local regression formula.

If a splitting is first expressed in projective-chart frames of the pulled-back \(\mathcal O(k)\) summands, these may differ from the chosen \(N^{2k+1}\) frames by powers of the nonvanishing coordinate section \(v_j\). Apply this diagonal frame conversion before (3.1), or include its logarithmic derivative in the old connection. Omitting this conversion would invalidate the connection-difference formula in those coordinates.

For a fully instantiated global certificate one must still record the actual normalized \(U_i\), their inverses and constant-differential identities; use the half-connection units in (3.1); form the cochains (3.4) and (5.2); and verify all transition conventions against the chosen atlas. These formulas do not supply the second-order residual’s cohomology value or its comparison to a finite RHom model.
