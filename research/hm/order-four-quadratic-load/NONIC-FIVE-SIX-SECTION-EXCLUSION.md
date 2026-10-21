# A universal-pencil obstruction excludes both large nonic endpoints

## New theorem

For the integral nonic CI(3,3) branch, h0(M)<=4. Both previously possible values five and six are excluded by the absence of quadrics on D and a Chern-class calculation on the auxiliary parameter plane of pencils. No selected HM matrix or rank is computed.

This strengthens the preceding linear-product equality argument, and gives a self-contained proof not requiring its external equality-case theorem.

## 1. Quadratic independence implies a translate-intersection bound

Let A be an r-dimensional subspace of a field L over C, and suppose Sym^2 A -> L is injective. For t in L not in C,

dim(A intersect tA)<=1.                            (1)

Proof. Otherwise choose independent a,b in A such that u=ta and v=tb also lie in A. The products ub and va agree in L. Injectivity forces the equality ub=va in the polynomial algebra Sym(A). The linear polynomials a,b are independent and hence relatively prime. The equality forces a to divide u, so u=c a for a scalar c; it then forces v=c b. Thus t=c in L, contradiction. This uses equality of formal quadratic products, not an assertion that their numerical values were selected.

Consequently, if B0 is any two-dimensional subspace of L, then

dim(A B0)>=2r-1.                                  (2)

Indeed choose a basis b0,b1, put t=b1/b0 not in C, and use AB0=b0(A+tA).

## 2. A three-dimensional partner forces one more product dimension

Under the same hypothesis, for every B with dim B>=3,

dim(A B)>=2r.                                     (3)

Proof. Choose a three-dimensional subspace B' of B. If dim(AB)<=2r-1, then(2) forces dim(AB')=2r-1 and forces every pencil B0 subset B' to have AB0=AB'. Let P=Gr(2,B')=P2 and S be its universal rank-two subbundle in B' tensor O. The fixed multiplication map then induces an everywhere surjective vector-bundle map

A tensor S -> (AB') tensor O_P.

Its source has rank2r and target rank2r-1; hence its kernel is a line bundle. Let h=c1(O_P(1)). The universal sequence gives c(S)=1-h+h^2. Therefore

c1(A tensor S)=-r h,
c2(A tensor S)=[r+binomial(r,2)]h^2=r(r+1)/2 h^2.

But an extension of a trivial bundle by a line bundle has second Chern class zero. The displayed positive multiple of h^2 is nonzero in the Chow ring of P2, contradiction. Thus(3) holds.

Every rank assertion in this proof follows from the universal inequalities and the assumed product dimension. The auxiliary P2 parametrizes all two-dimensional subspaces of B'; it is not a scan of actual source parameters.

## 3. Apply to the nonic

Let D be an integral CI(3,3) curve in P3. Put H=O_D(1), so deg H=9, genus10 and omega_D=2H. Let R=3H-Z have degree2 with h0(R)=0, M=H+R have degree11, and N=omega_D R^-1 have degree16. Serre duality and Riemann--Roch give h0(N)=7.

Set P=N-H=omega_D M^-1. Its degree is7 and

h0(P)=h1(M)=h0(M)-2.

Take rational trivializations and regard A=H0(H) and B=H0(P) as subspaces of C(D). Here dim A=4. Since D is ACM and has no quadric equation, H0(H) is exactly the four-dimensional ambient linear system and Sym^2 A -> C(D) is injective. Multiplication AB embeds in H0(N), so its dimension is at most seven.

If h0(M)>=5, then dim B>=3. Inequality(3) instead requires dim(AB)>=2*4=8. This contradiction proves h0(M)<=4. The argument applies unchanged to singular integral D; it uses its function field, the complete-intersection dualizing line bundle, and the absence of quadratic equations, not smoothness.

## 4. Consequence in the actual residual family

Together with NONIC-COMPATIBLE-DEFECT-CONSTRAINTS.md, the only actual surviving nonic section counts are h0(M)=3 or4: h0(M)=2 gives zero differential symbol and is excluded by the established invariant-surface descent argument. Every nonzero compatible tuple then has alpha span three, and the entire compatible tuple space is one-dimensional. The actual two-cubic differential-symbol map has rank exactly one, with a canonical kernel cubic and unique alpha center p in D, generically outside Z.

The center can still be singular. Its defining adjoint basepoint condition is given in the companion note. No assertion that the kernel cubic lifts globally, or that this rank-one configuration is excluded, is made. The nonic carrier, b=1, and full Q4 remain unresolved by this theorem. The separate octic exclusion is at936b652b228d9169a242f962f6053dec00df6382.

No external source theorem is needed beyond elementary bundle Chern classes, curve duality and Riemann--Roch. No selected source coefficients, matrices, ranks, parameter scans, local-model spike, consumed experiment, or external write was used.

Companion public pin: NONIC-COMPATIBLE-DEFECT-CONSTRAINTS.md at 277400cb97e3308a15c1f45e7e98a970c1e3a034. The nonic carrier classification is at e0d0c123934f06cb63937225881a83e5e5906cfb, both in Akilleez-QA/read-em-and-weep PR543.
