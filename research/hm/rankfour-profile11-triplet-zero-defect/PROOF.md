# The actual triplet top-four quotient has zero original determinant defect

## Statement and imported boundary

Work over C on the original physical binary-icosahedral line P(W*), with G=SL2(F5) and its fixed determinant convention. Retain the actual saturated constant-ambient inclusion E in H tensor O, dim H=30, and S=Q* in the dual constant ambient. Their actual ranks are 17 and 13 and both degrees are -54. Suppose the original derivative has rank four, maximal ordered plateau (1,1), and

    A_q=E/E^-=A_std(4)+O(-8),  A_std=Sym2 W.

PR1194 at e4de44641a53b0b3424102cd5fbaf3cf5821996d proves this is one of exactly three remaining necessary top-degree-four shapes, forces source E_D, and explicitly leaves it open. Its actual section gates are retained: H0(A_q) embeds in M2=A_std+2V+3P+4D, and H0(A_q(1)) embeds in M3=3W'+3S4+6T6. This shape passes them: its characters are respectively A_std+V+P+D and W'+S4+2T6. No kernel argument is used before these gates.

Set L=S^-, B=S/L. The actual endpoint L has rank nine and derivative rank at most three. The actual transposed derivative gives a coherent injection

    B -> A_q*(-2)=C=O(6)+A_std(-6),

whose original determinant defect is

    t=deg C-deg B=-12-deg B>=0.

No saturation or zero defect is initially assumed. Then necessarily

    t=0,  B is equivariantly isomorphic to O(6)+A_std(-6),
    deg L=-42.

In particular the original rank-four graded derivative is an everywhere bundle isomorphism A_q -> B*(-2). This does not exclude or realize the triplet form, close (1,1), or change a coarse-bin count.

The actual Gauss-filtration construction and endpoint capacity are imported from PR1185 at 236e0a3723c3d73ea7fb9e549376540a8e70508b, Section 2, which proves them before making a low-top assumption. The complete immutable proofs of PR1194 and PR1185 are retained in inputs/. Their transitive actual geometric hypotheses remain assumptions. No rank-three classification with central rank seventeen is transferred to another actual rank.

## 1. Exact all-height dual capacity

Recursively set F1=L and F(j+1)=Fj^- inside the same original dual constant ambient. Let Gj=Fj/F(j+1), j>=1. The actual derivative supplies coherent injections

    Gj -> G(j-1)(-2) -> ... -> B(-2j) -> C(-2j).

The ranks qj are nonincreasing, at most three, and sum to rank L=9. The chain terminates because S has top degree at most -1, whereas a nonzero saturated horizontal subbundle of the constant ambient is constant. This is exactly the negative-horizontal argument of the imported capacity lemma; it imposes neither a horizontal splitting nor a connection on a quotient.

Put hi=#{j:qj>=i}. Thus h1>=h2>=h3>=0 and h1+h2+h3=9. Exterior powers of the actual coherent injections bound every deg Gj by the sum of the top qj ordinary degrees of C(-2j). Summing gives

    deg L <= 6h1-6h2-6h3 - sum_i hi(hi+1)
           = -30 - (h1-7)^2 - (h2-1)^2 - (h3-1)^2.

The displayed identity holds on the entire plane h1+h2+h3=9. It includes all heights, all three columns and every unsaturated image. Since deg L=deg S-deg B=-42+t, it implies t<=12.

The determinant cokernel of B -> C has effective G-invariant divisor of length t. On P(W*) the projective A5 orbits have sizes 12,20,30,60: a point stabilizer is cyclic of order at most five, so no nonempty invariant effective divisor has degree below twelve. Consequently t is either zero or twelve. No fiber character or reducedness assertion is needed.

## 2. The positive-defect equality contradicts equivariant determinants

Assume t=12. Then deg L=-30, so equality holds in the capacity bound. Its square completion forces exactly

    (h1,h2,h3)=(7,1,1).

In particular q1=3. Every individual degree deficit in the sum of exterior-power bounds is nonnegative; since their sum is zero, every deficit vanishes. Hence the first actual graded bundle G1=L/L^- has rank three, degree -12, and its actual coherent injection is

    G1 -> C(-2)=O(4)+A_std(-8).

Take its third exterior power. The determinant line of G1 is equivariantly O(-12), with no nontrivial coefficient character: G is perfect, so two G-linearizations of the same line bundle can differ only by the trivial character. Also A_std is a self-dual determinant-one three-dimensional representation, so wedge^2 A_std=A_std and wedge^3 A_std=1. Therefore

    wedge^3(C(-2)) = A_std(-12)+O(-24).

But

    Hom_G(O(-12), A_std(-12))=Hom_G(1,A_std)=0,
    Hom(O(-12), O(-24))=H0(O(-12))=0.

Thus no nonzero equivariant determinant map exists. The third exterior power of a rank-three coherent injection on the integral curve is generically nonzero, a contradiction. This rules out t=12 without assuming a saturated intermediate image or analyzing any stabilizer character of the original defect.

## 3. Consequence and scope

Therefore t=0. The injection B -> C is between equal-rank vector bundles of equal degree; its torsion cokernel has length zero and vanishes. It is an everywhere equivariant isomorphism. Its transpose A_q -> B*(-2) is likewise an isomorphism, since it is the same actual graded derivative and its transpose, not an unrelated map with matching splitting. Finally deg L=-54-(-12)=-42.

This is a new necessary actual image relation for the previously open triplet form. No kernel tail is removed or realized. All actual-source and ambient premises remain explicit. The proof uses an exact symbolic square completion and two universal exterior-power identities only: no selected HM/source coefficient, parameter, point, jet, tensor, instance matrix/rank, broad candidate search, historical enumeration, or scan of heights occurs.

## Source links

- PR1194: https://github.com/Akilleez-QA/read-em-and-weep/blob/e4de44641a53b0b3424102cd5fbaf3cf5821996d/research/hm/rankfour-profile11-top-four/PROOF.md
- PR1185: https://github.com/Akilleez-QA/read-em-and-weep/blob/236e0a3723c3d73ea7fb9e549376540a8e70508b/research/hm/rankfour-profile11-low-top/PROOF.md
