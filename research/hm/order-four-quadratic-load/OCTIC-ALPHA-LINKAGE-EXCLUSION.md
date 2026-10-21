# Linkage syzygies exclude the remaining octic alpha defect

## Conclusion and exact scope

In the actual two-cubic marked-octic family, the three-dimensional alpha-type differential defect is impossible. This conclusion uses the intrinsic kernel line of the two-cubic differential symbol, but does not infer that its cubic equation lifts to an ambient cubic.

Together with the separate exclusions of compatible spans at most two and four, and the zero-symbol differential descent, this removes the marked ACM octic alternative. The nonic alternative and the smaller cubic-space cases are not addressed here; no complete Q4 claim follows.

## 1. Inputs read and retained

TWO-CUBIC-CARRIER-CLASSIFICATION.md gives an integral degree-eight carrier D⊂H=P3 of arithmetic genus seven, containing all 25 reduced marked points Z. Its two-dimensional cubic space cuts a (3,3) complete intersection Y. The residual curve R=Y:D is a reduced line. There are linear equations ℓ1,ℓ2 of R and quadrics a,b,c,d with

F=ℓ1 a+ℓ2 b,       G=ℓ1 c+ℓ2 d,

and, on setting T=ad−bc,

I_D=(F,G,T).

The Hilbert–Burch resolution is 0→2O(−5)→2O(−3)⊕O(−4)→I_D→0. The marked points lie in the smooth locus of the reduced support Y_red and in particular avoid R.

THREE-DIMENSIONAL-OCTIC-DEFECT.md proves that the remaining nonzero compatible defect forces

M=O_D(4)(−Z)≅O_D(1)(−p)

for a unique smooth point p∈D outside Z. Any nonzero compatible differential tuple has three-dimensional span and its components generate M everywhere. Moreover the intrinsic symbol map from the two-dimensional cubic space has rank one. Its kernel is a canonical line.

Work over a dense open of the hyperplane parameter space where these objects and ranks are constant. Choose a local algebraic cubic basis F,G with F spanning that kernel and G having nonzero symbol. Such a choice is possible after shrinking because a rank-one kernel in a rank-two bundle is a line subbundle. The residual line varies algebraically, and its linear equations ℓ1,ℓ2 can likewise be chosen locally. The displayed quadratic decompositions and T then vary algebraically: multiplication by the linear ideal of a line onto its cubic part is a constant-rank bundle surjection, locally split.

Thus the displayed identities are identities of families, and may legitimately be differentiated. Their validity is not merely fiberwise after unrelated choices.

## 2. The residual intersection is a quartic divisor on the line

Put Q=D∩R scheme-theoretically. Since F and G vanish identically on R, the presentation of I_D gives

I_{Q,R}=(T|R).

The restriction T|R is nonzero: otherwise R would be contained in integral D, impossible since D has degree eight and is not a line. Hence Q is an effective Cartier divisor of length four on R≅P1, including all multiplicities.

Its support is disjoint from Z. Indeed the marked points lie in the smooth locus of Y_red and on D, whereas any point belonging to both distinct components D and R is singular on that reduced curve. Alternatively, Q is canonical and has length four, so normalizer transitivity of the 25 distinct marked labels forces its marked subset to be empty.

Neither Q reduced nor D smooth at Q is required.

## 3. Differentiate the two linkage syzygies

Use the affine hyperplane chart H_t: X4=Σ_(i=0)^3 t_i X_i and homogeneous coordinates x_i on H_t. For any parameter-dependent homogeneous polynomial A(t,x), denote its fixed-point differential tuple by

P(A)_ij=x_i ∂_(t_j)A−x_j ∂_(t_i)A.

The operator is a derivation on products in the form P(AB)=A P(B)+B P(A), componentwise. For F and G its entries are quartics; for T its entries are quintics.

By the kernel choice,

P(F)|D=0.

By the alpha-defect theorem, P(G)|D is obtained by multiplying a tuple generating M by the canonical section cutting out Z. Thus on any subscheme of D supported away from Z, its six components generate the restriction of O_D(4). In particular they generate that invertible sheaf on Q.

The algebraic identities

dF−bG−ℓ1T=0,       cF−aG+ℓ2T=0

are exact, as follows by expansion. Apply P and restrict to D. Every term containing F,G, or T themselves vanishes, and P(F)|D=0. We obtain

b P(G)|D = −ℓ1 P(T)|D,
a P(G)|D =  ℓ2 P(T)|D.                         (1)

Restrict (1) to Q. Both ℓ1 and ℓ2 vanish scheme-theoretically there, so

a P(G)|Q=0,       b P(G)|Q=0.

Because the components of P(G)|Q generate an invertible sheaf, these equations force

a|Q=b|Q=0.                                      (2)

This remains true on a nonreduced Q: locally one component of a generating tuple is a unit after trivializing the line bundle, so its annihilator in O_Q is zero. No pointwise-to-scheme inference has been made.

## 4. Degree on the residual line gives the contradiction

The restrictions a|R and b|R are sections of O_R(2). By (2), both vanish on the length-four Cartier divisor Q. They therefore belong to

H0(O_R(2)(−Q))=H0(O_P1(−2))=0.

Consequently a|R=b|R=0. But then

T|R=(ad−bc)|R=0,

contradicting the nonzero quartic defining Q in Section 2. This excludes the alpha defect.

## 5. Why this does not assert an unjustified cubic lift

The kernel cubic F was only assumed to satisfy P(F)|D=0. Its fixed-point derivatives were not assumed to vanish on the full cubic surface V(F), on all of Y, or in the ambient projective space. The proof propagates that limited vanishing through the exact degree-five linkage syzygies and the basepoint-free nonzero symbol of the complementary cubic. The contradiction occurs on the finite residual intersection Q, not through an ambient lifting assertion.

For comparison, the weaker residual-symbol observation can also be made rigorously. Modulo (F,G), each quartic P(F)_ij is a constant multiple c_ij T, since the quotient I_D/(F,G) has one degree-four generator. Its exact Koszul identity gives

(x_i c_jk−x_j c_ik+x_k c_ij)T=0 modulo (F,G).

The annihilator of T in O_Y is I_R/I_Y by linkage. Thus x∧c=0 for every x on R, forcing the constant bivector c to be a scalar multiple of the Plücker bivector of R (or zero). This leaves a residual-line-supported derivative and by itself is not a cubic lift. The syzygy argument above is the additional ingredient that excludes the actual alpha configuration.

## Provenance and boundary

Read the two octic-defect notes and the two-cubic classification before deriving this argument; current PR1 was checked through 6313516070. The two-cubic classification was publicly handed off at e0d0c123934f06cb63937225881a83e5e5906cfb. The three-dimensional alpha defect and four-dimensional exclusion inputs are pinned at ae1e612bc5a56e6a3cd0d158ee317babf51b662c and 8146e2a2a7c2ed3b37fc8e79603bf4021d441c5a, respectively.

No selected HM/source coefficients, ranks, parameter scans, local-model spike, consumed experiments, or external writes were used. The proof treats residual intersection multiplicities and singular carrier points explicitly. It does not settle the remaining nonic case or the full source-lift boundary.
