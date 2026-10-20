# Independent audit: low-metric-rank middle surface exclusion

Result: PASS for the principal theorem and its stated projective scope. Audited the complete PROOF.md on 2026-10-19. The final fiber-dimension corollary remains conditional on its explicitly imported fiber bounds and (where stated) hypothesis (H); those imports were not re-proved in this audit.

## 1. Rank-zero exclusion and residual extension

The pencil identity is correct. Outer symmetry and cyclic zero give f(e,u,e)=-2A_e(u), and expansion gives A_(u+te)(e)=A_u(e)-tA_e(u). If the actual correction on e² is proportional to e, repeated injectivity forces a nonzero proportionality A_e(u)=c A_u(e), and t=1/c contradicts injectivity. This establishes square avoidance wherever the actual correction exists.

At residual rank zero the correction is defined on every square. Its quotient section on P³ lies in Q(2), whose exact sequence is 0→O(1)→O(2)^4→Q(2)→0. Thus c3(Q(2))=15H³, nonzero. This excludes rank zero globally. Consequently the reduced rank≤1 determinantal support is closed and consists entirely of rank-one points.

On this reduced support, constant rank one is enough for a locally split image line and locally free kernel: after inverting a nonzero entry, all larger minors vanish as functions. No extension across absent rank-zero points is needed. This reduced-support qualification matters and is stated correctly.

## 2. Correct middle-line weight and gluing

The numerator U⊗K→I, inverted through U²⊗E≅I, yields K→U⊗E, not U*⊗E. A splitting change d:E→U contributes d(a)b+d(b)a and hence 2d(e)e on a square. Restricting to L² and quotienting by L gives a globally defined section of (E/L)⊗U⊗L^(-2). Its nonvanishing is precisely the verified square-avoidance condition. All these operations remain valid after arbitrary pullback to the cover and its resolution.

## 3. Rank-one boundary of the isotropic cover

The incidence Z⊂Gr_B(3,E) is closed and projective. Every geometric rank-two fiber has exactly two underlying isotropic hyperplanes, while every rank-one fiber has exactly one. Scheme nonreducedness at rank one does not obstruct quasi-finiteness: zero-dimensional finite-type fibers suffice. Thus proper plus quasi-finite makes Z→B finite, even across rank drop.

An irreducible reduced component dominating the integral B exists because the finite incidence is surjective and has finitely many components. In characteristic zero its generic degree is at most two. A projective resolution of that component is still generically finite of the same degree, though generally not finite. The pulled-back tautological sequence remains an exact sequence of vector bundles with a line quotient everywhere. The identity Sym²R→M=0 holds on the entire resolution because it holds scheme-theoretically on the incidence. No unsupported extension of a radical or a rational hyperplane is used.

## 4. Integral Chern calculation

Use a=c1(U*), n=c1(E/R), and ξ=c1(L*). Since E is the quotient of a trivial rank-five bundle by U, c1(E)=a and c2(E)=a². On the smooth surface, base classes of codimension three vanish. For Q'=E/L,

c1(Q')=a+ξ,
c2(Q')=a²+aξ+ξ²,
c3(Q')=a²ξ+aξ²+ξ³.

Twisting by first Chern class 2ξ−a gives

c3(F)=15ξ³−10aξ²+5a²ξ.

For the lines convention, ξ³+c1(R)ξ²+c2(R)ξ=0. The integral projective bundle decomposition makes the ξ² and ξ coefficients separately zero. Since c1(R)=a−n and c2(R)=a²−an+n², the resulting equations are

A=15n−25a=0,
B=10a²−15an+15n²=0.

The exact polynomial identity

3B−(3n+2a)A=80a²

verifies the claimed integral conclusion without cancelling any torsion factor. Taking degree yields deg(a²)=0.

## 5. Completeness and scope

For an integral projective B whose middle image is a surface, the pullback of O(1) has strictly positive self-intersection: after the degree-d cover and resolution its degree is d times the positive intersection on B. This contradicts 80a²=0. Projectivity/completeness and a two-dimensional middle image are essential to this positivity argument; the proof does not assert an exclusion for arbitrary nonproper surfaces or surfaces with lower-dimensional image.

Because residual rank≤1 is closed and rank zero is absent, taking the projective closure of an integral generically residual-rank-one middle surface does not introduce an unhandled residual boundary. Metric rank≤2 is itself closed there. Thus the generic formulation legitimately reduces to the complete incidence argument. The main exclusion is independent of (H); the concluding equality-case reduction is appropriately qualified by its additional imports.

No mathematical defect found in the proof.
