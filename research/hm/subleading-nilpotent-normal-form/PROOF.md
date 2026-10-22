# First-subleading nilpotent jets modulo regular gauge

## Scope and theorem

Let k=C(L), S=k[X,Y], and S_d its degree-d homogeneous part. Fix a regular homogeneous pair f in S_3, g in S_5 and u in k^×. Regular means gcd(f,g)=1; f need not be squarefree. A trace-free matrix of weight d has diagonal, upper, and lower degrees d, d-2, and d+2. Set

    n = u [[fg, -f²], [g², -fg]],
    Z_12 = { D of weight 12 : nD+Dn=0 }.

This is an ordinary polynomial calculation on the binary cover, not a splitting of the harmonic deformation algebra. In a fixed frame there is an exact sequence of k-vector spaces

    0 -> sl_2(S)_[4] --(X -> [X,n])--> Z_12
      --nu--> (S/(f))_4 -> 0.                         (1)

The last space has dimension three over k=C(L), not three global complex parameters. The map nu sends v n to [v]. Consequently every D in Z_12 has an expression

    D = v n + [X,n],    v in S_4, X in sl_2(S)_[4],   (2)

with unique residue [v] modulo f S_1. After choosing a representative v of that residue, X is unique. There is no canonical representative v without an additional splitting. This identifies the surviving first-subleading nilpotent data under regular weight-four gauge, not the whole first-subleading jet of the lifted section.

The weighted conventions and actual regular-pair setting are those of [PR713](https://github.com/Akilleez-QA/read-em-and-weep/blob/5b3943980ecaef78ee7f56fbc015d40955fb24f0/research/hm/leading-vertex-obstruction/PROOF.md). The nearby weight-four trace-kernel and modular-division statements appear in [PR717](https://github.com/Akilleez-QA/read-em-and-weep/blob/7362df9da60a3b87b3200078a0145a376cc3056b/research/hm/nilpotent-trace-lift-invariance/PROOF.md) and [PR725](https://github.com/Akilleez-QA/read-em-and-weep/blob/397c7473691a08a839ccf7e9abeed06002b48bab/research/hm/modular-vertex-elimination/PROOF.md). They concern a weight-four unknown with fixed n. Here the unknown is instead the weight-twelve nilpotent perturbation, and the equivalence relation is weight-four conjugation.

## 1. Parametrize the nilpotent tangent equation

Write D/u=[[x,y],[z,-x]], where x,y,z have degrees 12,10,14. Trace-free rank-two polarization identifies nD+Dn=0 with

    2fg x + g² y - f² z = 0.                          (3)

Reduction modulo f, respectively modulo g, and coprimality give f|y and g|z. Thus uniquely

    y=-2f p,   z=2g r,   x=g p+f r,
    p in S_7, r in S_9.                               (4)

The expression for x follows by substituting into (3) and cancelling 2fg in the domain S. Conversely every pair (p,r) defines an element of Z_12. Multiplicities in f do not affect this argument: g is a nonzerodivisor modulo f and modulo each power of f by coprimality.

For X=[[alpha,beta],[gamma,-alpha]] of weight four, direct multiplication gives

    [X,n]/u = [[2alpha fg+beta g²+gamma f²,
                -2alpha f²-2beta fg],
               [2gamma fg-2alpha g²,
                -2alpha fg-beta g²-gamma f²]].        (5)

In the parametrization (4), this is exactly

    p=alpha f+beta g,   r=gamma f-alpha g.             (6)

Here alpha,beta,gamma have degrees 4,2,6. In particular the signs in (2) use [X,n]=Xn-nX.

## 2. Eliminate the first component and identify the residue

The multiplication map

    S_4 direct-sum S_2 -> S_7, (alpha,beta) -> f alpha+g beta

is an isomorphism. Indeed f alpha=-g beta implies f|beta, forcing beta=0 since deg beta<deg f, and then alpha=0. Its source and target both have dimension eight. Thus write p=f alpha+g beta uniquely. Subtracting the gauge with these alpha,beta and gamma=0 eliminates p and leaves

    r' = r+alpha g in S_9.                            (7)

The remaining gauge gamma changes r' by f gamma. The quotient is therefore S_9/f S_6. Multiplication by g induces an isomorphism

    g : (S/(f))_4 -> (S/(f))_9.                       (8)

It is injective by regularity, and both graded spaces have dimension three: dim S_d-dim S_(d-3)=3 for d=4,9. Define

    nu(D) = g^{-1}[r+alpha g].                        (9)

Equation (9) uses the inverse of the graded isomorphism (8), not division by g in the polynomial ring or an evaluation of any actual coefficient.

For D=v n, equation (4) has p=vf/2 and r=vg/2. Its unique decomposition of p is alpha=v/2, beta=0, so (7) gives r'=vg. Hence nu(vn)=[v], with no extra factor of two or u. The unit was handled by D/u in (3)-(4).

If nu(D)=0, equation (7) is f gamma for a unique gamma in S_6. Then (6) reconstructs D=[X,n]. Conversely every commutator has zero image. Finally [X,n]=0 implies p=0 in (6), which forces alpha=beta=0 by the same degree argument, and r=0 forces gamma=0. This proves exactness and injectivity in (1), and proves (2).

For an explicit reconstruction, use alpha_0,beta_0 in the unique decomposition p=f alpha_0+g beta_0. Choose v representing (9), and put

    alpha=alpha_0-v/2, beta=beta_0,
    gamma=(r+alpha_0 g-vg)/f.                         (9a)

The last quotient is a polynomial by the defining residue equation. Substitution in (6) verifies (2) directly.

## 3. All ambiguity is explicit

For ell in S_1 put

    X_ell = ell [[f/2,0],[g,-f/2]].

Equation (5) gives the identity

    [X_ell,n] = f ell n.                              (10)

Thus changing v to v+f ell in (2) changes X to X-X_ell. There is no further ambiguity. In particular the quotient of nilpotent tangent directions by gauge is genuinely the three-dimensional residue space, although the scalar multiples v n form a five-dimensional space before quotienting.

As an independent dimension check, (4) gives dim Z_12=8+10=18, while the gauge source has dimension 5+3+7=15. These are universal graded dimensions, not a selected actual matrix-rank computation. Identity (5), the exact divisions, and the explicit ambiguity (10) give a deductive check independent of this dimension count.

## 4. Realization at the first subleading order

Suppose a trace-free formal nilpotent matrix on the binary cover has expansion

    N=n+D+terms of weight at least 16,

with no intervening weights. The weight-twenty coefficient of N²=0 is nD+Dn=0, since n²=0. The hypotheses therefore apply to D. Writing (2) and conjugating by 1-X in the formal transverse completion gives

    (1-X) N (1-X)^(-1)
      = n+v n+terms of weight at least 16.             (11)

The inverse exists because all entries of X have positive transverse degree. To this precision, the commutator is -[X,n], cancelling the gauge part of D; terms involving X²n or XD have weight at least 16. This is a regular formal frame change over k, not one with transverse poles.

There is also a direct universal realization of the tangent direction (4): set F=f+p and G=g+r. Then u[[FG,-F²],[G²,-FG]] is exactly square-zero, and its first two homogeneous matrix pieces are n and D. The quadratic terms in p,r start at weight 16. Thus the tangent equation used here does not create a spurious local first-subleading direction. This construction uses only ordinary products on the cover and supplies no harmonic lift of the odd forms F or G.

## 5. Contribution and limits

[PR774](https://github.com/Akilleez-QA/read-em-and-weep/blob/eec909bef4a7e6998737773d5eadd0ad562e79d9/research/hm/matrix-jet-filtration/PROOF.md) establishes the intrinsic physical matrix filtration. [PR775](https://github.com/Akilleez-QA/read-em-and-weep/blob/af2fc052d3da2c4abc315dca268ed65b62f5cde5/research/hm/first-subleading-norm-formula/PROOF.md) isolates the leading/first-subleading bilinear norm pairing and its gauge cancellation. The present result separates the weight-twelve part of the underlying nilpotent coefficient N into a removable commutator and a scalar residue. It does not normalize all first-subleading coefficients of the total-weight-sixteen lifted section K: its other normal coefficients and their equations remain.

The statement is over C(L) in a fixed regular adapted frame. It neither chooses a global f,g nor proves that the k-linear splitting or the resulting gauge is regular over every point of L. Compatibility on overlaps, determinant/equation units, source-zero behavior and global descent must still be supplied in any global use. The residue description is relative to the fixed leading data and frame; no unproved frame-independent global trivialization is asserted.

The scalar residue is genuine retained data. Equation (11) is not authorization or a proof that one can rescale the fixed actual N by a global scalar unit to erase it.

No actual residue nu(D), beta4 value, beta2-image membership, further-neighborhood existence, or algebraicity conclusion is determined. All arguments are universal structural identities with a regular pair, with no selected actual coefficients, points, derivatives, matrices, ranks, model experiments or large computation. This is a deductive proof, not proof-assistant verification.

## 6. Formal finite determinacy for a factored nilpotent

There is a stronger conclusion if the full ordinary-cover factorization is supplied. This is an additional hypothesis, not a consequence asserted from the first tangent equation alone. Work in R=k[[X,Y]], with the same homogeneous f,g,u. Suppose

    F=f+f_7+f_11+...,   G=g+g_9+g_13+...,
    U=u+u_4+u_8+...,
    N=U [[FG,-F²],[G²,-FG]].                          (12)

Every subscript denotes ordinary homogeneous degree. A physical adapted gauge here means an invertible formal matrix Q whose diagonal corrections have degrees 4,8,..., upper corrections 2,6,..., and lower corrections 6,10,...; equivalently Q=I+terms of positive matrix weight in 4Z. No global frame or harmonic lifting of F,G is assumed.

Then N is conjugate by such a gauge to

    (1+v_4)n,                                        (13)

where v_4 in S_4 has a uniquely determined residue in

    (S/(f,g))_4 = (S/(f))_4.

This residue agrees with nu(D) for the weight-twelve piece D of N. Higher physical-even scalar degrees and higher pair jets carry no additional formal conjugacy invariants within the factored class (12). This is exact formal local finite determinacy, not a global statement and not a normal form for the full lifted K.

### 6.1 Reduce the full pair to its leading pair

The regular sequence of degrees 3 and 5 has Hilbert series

    Hilb(S/(f,g),t)=(1-t³)(1-t⁵)/(1-t)².

For completeness its Koszul resolution is

    0 -> S(-8) -> S(-3) direct-sum S(-5) -> S -> S/(f,g) -> 0.

Thus S/(f,g) is zero in degrees at least seven and has last possible degree six. Every f_(3+4j), j>=1, can therefore be written f alpha_(4j)+g beta_(4j-2), and every g_(5+4j) can be written f gamma_(4j+2)+g delta_(4j). Summing these choices degree by degree gives

    (F,G)^t=M(f,g)^t,
    M=I+[[alpha,beta],[gamma,delta]],                 (14)

with diagonal corrections in degrees 4,8,..., upper in degrees 2,6,..., and lower in degrees 6,10,... . All entries lie in R. The determinant of M has constant term one, so M is invertible formally.

Put s=(f,g)^t, r=(g,-f), and n_0=sr=n/u. The two-by-two alternating identity gives

    n_0(Ms)=det(M) M n_0(s) M^(-1).

Consequently conjugation of (12) by M^(-1) yields a n, where

    a=(U/u)det(M)=1+a_4+a_8+... .                     (15)

In particular the determinant factor multiplies, rather than divides, the scalar in this first reduction. Choices in (14) will not affect its quotient residue, as the uniqueness argument below proves.

### 6.2 Remove exactly the scalar units trivial modulo the ideal

Let I=(f,g)R. Completion does not change the finite-dimensional quotient: R/I=S/(f,g). Its physical-even part, meaning degrees divisible by four, has only degrees zero and four. Choose v_4 representing the degree-four class of a-1. Then

    b=a/(1+v_4) belongs to 1+I,

and b has only degrees divisible by four. Choose degreewise

    b-1=g w_1-f w_2.                                 (16)

For degree 4j, the degrees of w_1,w_2 are 4j-5,4j-3 respectively; the first is absent when negative. These choices exist because b-1 lies in I. Define

    T=I_2+w r,    w=(w_1,w_2)^t.

Here I_2 denotes the identity matrix, distinct from the ideal I. Since r s=0, T s=s. The rank-one determinant formula gives

    det T=1+r w=b.

It is a unit, and the degrees in (16) show T is an allowed positive-weight gauge, including the possible degree-one term of w_2, which contributes a weight-four matrix. The alternating identity now gives

    T n T^(-1)=n/(det T)=n/b.

Thus conjugation by T after M^(-1) sends N exactly to (1+v_4)n. This removes scalar units congruent to one modulo I by genuine frame conjugation; it does not rescale the fixed actual N by fiat.

### 6.3 Uniqueness under all allowed formal gauges

Suppose Q conjugates a n to c n, where a,c are units with constant term one. Over the fraction field of R, the image line of n is spanned by s. Hence Qs=lambda s. Since f,g are coprime in R and lambda f,lambda g both belong to R, lambda belongs to R. The same argument applied to Q^(-1) shows lambda is a unit. Coprimality persists on completion: the homogeneous regular pair generates an ideal of finite colength in R, whereas a common nonunit divisor would give an ideal of height at most one. Equivalently R is a factorial regular local ring and the denominator of lambda must divide both f and g.

Each row of Q-lambda I_2 annihilates s. The regular-pair syzygy is generated over R by (g,-f), so

    Q=lambda I_2+w r,
    det Q=lambda²+lambda r w
          congruent to lambda² modulo I.             (17)

The alternating identity, or direct multiplication, gives

    Q n Q^(-1)=(lambda²/det Q)n.

Therefore c/a=lambda²/det Q is congruent to one modulo I, so [c]=[a] in R/I. In particular two representatives (13) can be conjugate only if their degree-four residues agree. Conversely agreement of residues makes their ratio a unit in 1+I, and the construction (16) supplies an allowed gauge. This proves both uniqueness and completeness of the stated invariant. No choice of a complement to f S_1 becomes canonical.

Taking the first positive-weight term of this exact conjugation recovers (2), so the formal residue is precisely nu(D), with the same normalization. The finite-determinacy result permits simplification of the nilpotent coefficient in a fixed local frame only. Whether the actual full factorization and gauges extend over all of L, their overlap compatibility, and the induced changes in the other normal coefficients of K remain separate dependencies. In particular this cone-cover conjugation does not normalize the q-normal coefficients B_1, B_2, B_3 or the whole K_[16]. No actual value of the residue or of the global adjoint obstruction has been calculated.

## 7. Application to the first-subleading fifth-norm formula

Use the fixed harmonic convention and generic regular physical frame of PR775. Distinguish its source multiplier s=a^4 h of cover degree four from the cubic f used above. On the cone, K|Q=s N. Thus, in the notation of PR775,

    A_0=s n,     B_0=s D.

Take the weight-four matrix X from (2), and lift it entrywise by the fixed harmonic lift H. Its entries have even degrees 4,2,6, so this uses only the even cone algebra, not harmonic lifts of odd f or g. The ambient matrix 1-H(X) is invertible in the formal transverse neighborhood. Conjugate the local fifth lift K by this matrix. Up to total weight sixteen this gives

    K'_[12]=K_[12],
    K'_[16]=K_[16]+[K_[12],H(X)].

In particular the zero-normal coefficient becomes

    B'_0=B_0+[A_0,X]=s(D-[X,n])=v_4 A_0.             (18)

The other coefficients must be transformed as well. Explicitly, for 0<=j<=4,

    B'_j=B_j+sum_(0<=i<=min(3,j))
        (H_(j-i)(A_i,X)-H_(j-i)(X,A_i)).              (19)

These are the fixed ordered harmonic products of PR775. Before harmonic extraction the complete pairing changes by

    tr(K_[12][K_[12],H(X)])=0.

Hence the complete fourteen-term norm sum is unchanged, not merely its individual zero-normal contribution. One may subsequently choose a local q^4 correction to make B'_4=0, as in PR775; this changes only the full source-multiplied relation class. The resulting thirteen-term representative may therefore be written using B'_0=v_4 A_0 while retaining all transformed B'_1,B'_2,B'_3, together with the same scalar-reference subtraction and exact global quotient specified there.

No identity H(v_4 A_0)=H(v_4)H(A_0) is assumed: the latter product generally has nonzero higher harmonic terms. Equation (18) is an identity for the zero-normal coefficient, and (19) records the additional changes that are essential to the full norm pairing. This is a generic local input simplification for the open norm problem, not a calculation of that problem's value, a global descent statement, or permission to discard the other normal coefficients.
