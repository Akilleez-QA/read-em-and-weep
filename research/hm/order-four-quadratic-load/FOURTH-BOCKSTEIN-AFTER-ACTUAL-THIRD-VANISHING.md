# The fourth Bockstein after actual third vanishing

## 1. Scope and fixed reduction

The actual third Bockstein is zero by ACTUAL-THIRD-BOCKSTEIN-VANISHES-IDENTICALLY.md. This note gives its next exact obstruction formula and representation space. It does not evaluate the fourth obstruction.

Fix an equivariant Schur reduction eliminating the33 unit factors of the positive pencil, with the residual source identified as A+D5 and target as P4. Write its formal residual map, for smoothing direction a, as

    F(t,a)=t^2 B2(a)+t^3 B3(a)+t^4 B4(a)+... .          (1)

Here Br is homogeneous of degree r in a. The coefficient B2 is zero on D5, and its A restriction is the actual nonzero second symbol

    beta:A O_P(A)(-2) -> P4 O_P(A).

This map is injective as a sheaf, even though its fibers have rank2 at the six axes. Its cokernel is I_Sigma(6). No inverse on those exceptional fibers is assumed.

## 2. A unique linear third lifting correction

The proven vanishing of the D5 third gate says that the composition of B3|D5 with P4 O -> I_Sigma(6) is zero. Exactness gives a UNIQUE sheaf morphism

    L:D5 O(-3) -> A O(-2),    B3|D5=beta L.            (2)

In particular L is polynomial and linear in a, not a rational solution whose poles must be removed. Its equivariant coefficient space is

    Hom_G(D5,A tensor A)=C,

since A tensor A=1+A+D5. Thus relative to the FIXED reduction, the third lifting correction is a single scalar times the unique equivariant linear family. This note does not assign that scalar or assert that it is independent of a change of Schur reduction.

For h in D5 use the corrected source h-t L(a)h. Substitution into(1) kills its order-three coefficient and gives the order-four representative

    W4(a)h=B4(a)h-B3(a)|A L(a)h.                    (3)

The actual fourth obstruction is the class of(3) in coker(beta_a), on the surviving D5 family. Adding a source correction t^2 M(a)h changes(3) by beta M, so disappears in this quotient. The usual changes of earlier lifts have the same filtered-obstruction indeterminacy. Equation(3) is NOT merely B4|D5: the already forced third lifting correction must be retained.

At the six rank-drop axes the specialized second kernel has an additional A-line, whose third differential also vanishes. The family here concerns D5; it does not claim to describe the fourth value on that extra specialized line.

## 3. The next actual ambient division

There is also a direct formula in the actual ambient cohomology module, using the fixed Atiyah probe rather than an arbitrary Schur gauge. Write q=q0, with the sign convention that the pencil is q-ta. The already established identities are

    q xi=0,   q zeta_a=a xi,   q v_h=a h zeta_a.

The canonical raw cubic tensor is [a v_h] in the actual P4 cokernel. Its zero third quotient gives a unique linear correction b=b(a,h) in A with

    [a v_h]=beta2_a(b)=[a b zeta_a].

This is a sheaf factorization, not inversion of a rank-drop fiber. Consequently the actual ambient division

    q w_h=a(v_h-b zeta_a)                         (5)

is possible. It is the next unresolved operation. Direct multiplication gives

    (q-ta)(h xi+t(h zeta_a-b xi)
             +t^2(v_h-b zeta_a)+t^3 w_h)
       =-t^4 a w_h.                              (6)

Hence the fourth class on D5 is [a w_h], modulo the actual second-symbol image. Changing w_h by ker(q) changes a w_h by zero in the cokernel because the first Bockstein is zero. Changing v_h by a kernel element g xi changes the resulting fourth representative by [a g zeta_a], which is a second-symbol value (zero on the D5 part of g). This explains the remaining quotient directly.

The b in this fixed-probe formula agrees with L in Section2 when the Schur coordinates are chosen compatibly with those probes. No arbitrary change of third-lift gauge is silently identified with this normalization. A nonzero b does not decide whether the class in(6) is zero.

## 4. Four equivariant quartic channels

Homogeneity gives the global D5 fourth gate

    beta4:D5 O_P(A)(-4) -> I_Sigma(6).

The second-symbol resolution twisted by four is

    0 -> A O(2) -> P4 O(4) -> I_Sigma(10) -> 0.

Its left term has no H1. Therefore

    H0(I_Sigma(10))=P4 tensor Sym^4 A - A tensor Sym^2 A
      =1+A+2V+3P4+4D5,                            (4)

of dimension42. Hence the fourth gate has FOUR possible equivariant coefficients. Their values are not determined by third vanishing.

Since Sigma is disjoint from the discriminant conic Delta, multiplication by its equation gives

    0 -> I_Sigma(8) -> I_Sigma(10) -> O_Delta(10) -> 0.

The twist-two resolution and H2(O)=0 show H1(I_Sigma(8))=0, so this is exact on global sections. The characters are

    H0(I_Sigma(8))=V+2P4+2D5,                     dim21,
    H0(O_Delta(10))=Sym^20 W=1+A+V+P4+2D5,       dim21.

Thus TWO fourth channels are discriminant-divisible and TWO are detectable on square directions. Unlike the cubic stage, there is no one-channel square dichotomy. The exact sequence splits as a G-representation in characteristic zero, without choosing a canonical geometric splitting.

## 5. Remaining mathematical task

To decide the next gate one must compute the actual class of B4|D5-B3|A L, or a geometrically equivalent fourth normal-lifting operation, retaining its fixed-reduction corrections. The previous raw cubic calculation can constrain L only after its unquotiented comparison with this chosen B3 is checked. A nonzero L alone is not a nonzero fourth obstruction.

Run verify_fourth_bockstein_reduction_channels.py. Its checks are universal formal coefficient extraction and exact representation arithmetic, with no chosen actual HM coefficients or actual-instance matrix/rank calculation.
