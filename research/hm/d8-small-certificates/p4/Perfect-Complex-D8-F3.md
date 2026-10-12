# The exact 32-dimensional D8 sector over F3, for the pinned perfect complex

12 October 2026. This is a fresh characteristic-independent small-rank computation followed by a direct geometric argument over the chosen field. It does **not** transfer the obstruction theorem or identify a transferred-coordinate action matrix.

## Result

Let k be a field of characteristic different from 2. Let L be the pinned four-term complex on P4_k,

    5O(-1) -> 15O -> 10O(1) -> 2O(2),

in internal degrees -1,0,1,2, with the explicit integer maps from the pinned source below. Put C: y²=x³-x, X=C⁴, Y=(P1)⁴, q:X->Y, rho:Y->P4 the symmetric-product map, f=rho q, and P=f*L. The complex P is perfect regardless of whether L has already been identified with a vector bundle in this characteristic.

For the full-sign deck character chi and epsilon=sgn|D8, the calculation proves

    dim Ext^j_X(P,P)_chi = (0,0,352,79,1),
    dim Ext²_X(P,P)_(chi,epsilon) = 32.

The same conclusion holds after a line-bundle twist of P. In particular this is an exact dimension statement over F3 for the pinned perfect complex. To replace P by the claimed HM bundle pullback E in characteristic 3, separately establish that the reduced L has only the intended rank-two vector-bundle cohomology in degree zero. To constrain the actual second-order obstruction, separately establish its geometric identification, naturality and full-sign choice independence in that characteristic. None of these latter assertions is proved here.

## 1. New small certificate: all four P4 twists

The script `check_hm_p4_all_twists.js` reconstructs End(L) from the pinned maps and checks the following hypercohomology dimensions, in degrees 0 through 4:

    t =  0: (1,24, 2,0,0)
    t = -1: (0, 5,10,0,0)
    t = -2: (0, 0,20,0,0)
    t = -3: (0, 0,20,0,0).

Every rank used has a complete unit-pivot integer certificate, with zero residual. These are characteristic-independent ranks, not characteristic-zero ranks inferred from floating point or modular traces. Consequently these computations apply directly over F3. There is no need to import the old large-model total 79, nor to assume its base change.

The t=0 global-section ranks are 353,848,350 on dimensions 354->1225->1200->350. The t=-1 ranks are 240,150 on dimensions 245->400->150. These reproduce the prior small certificate.

For t=-2 the only line-bundle cohomology is H4(O(-5))^10 in internal degree -3, and H0(O)^80 -> H0(O(1))^10 in internal degrees 2,3. Thus the transferred finite complex is

    10 --d5--> 80 --d1--> 50

in total degrees 1,2,3. The new ranks are

    rank(d5)=10, rank(d1)=50.

The d5 matrix has 50 nonzero entries, all ±1. It contains an explicit identity 10-by-10 minor at zero-based rows

    50,60,51,61,52,62,53,63,54,64

with columns 0,...,9 in that order. The ordinary map is surjective by 50 unit pivots. Therefore the twist -2 cohomology is exactly H2=k^20. The script also checks d1 d5=0.

For t=-3, use the canonical self-duality of the perfect complex End(L) (the supertrace pairing), valid over every field. Serre duality on P4 pairs degree i, twist -3 with degree 4-i, twist -2. Thus twist -3 also has only H2=k^20. This uses no assertion that L is quasi-isomorphic to a bundle.

### The d5 construction and checks

Use the standard affine cover U_i={x_i!=0}, i=0,...,4. A homogeneous Laurent monomial x^m occurs on the Cech component indexed by nonempty S exactly when every negative-exponent index belongs to S. The Cech degree is |S|-1. Its Cech differential adds an index j with sign (-1)^(number of elements of S less than j).

For each proper, nonempty negative-exponent set N, choose j=min({0,...,4}\N). The contracting homotopy removes j from S when present, with the same insertion-position sign; otherwise it is zero. This is the standard simplex contraction and satisfies dh+hd=id on that acyclic monomial complex. All four intermediate twists in the d5 path have negative line degree, so this acyclic case applies.

Start at the ten matrix units L^2->L^-1, multiplied by x0^-1 ... x4^-1 on the top Cech component. Apply the signed internal commutator Delta=(-1)^q[d,-], alternating with four contractions, and project the resulting degree-zero Cech cocycle to its U0 component. This computes p Delta (h Delta)^4 i; the usual perturbation factor (-1)^4 is positive.

The executable checks, on the states used: Cech/internal anticommutation, internal square zero, all 40 contraction identities, final Cech closedness, final internal closedness, and d1 d5=0. Its largest intermediate sparse state has 165 terms. No large transfer or external computation is needed.

## 2. Direct D8-equivariant splitting over F3

The symmetric-product map rho is finite and flat of degree 24 in every characteristic. Finiteness follows from the symmetric quotient; flatness follows because Y is smooth/Cohen--Macaulay, P4 is regular, and the finite fibers have dimension zero. The degree being divisible by 3 does not prevent flatness.

Let F=rho_*O_Y. For i=1,2,3 and every integer n,

    H^i(P4,F(n)) = H^i(Y,O(n,n,n,n)) = 0.

Kunneth gives only degree zero for n>=0, only degree four for n<=-2, and no cohomology for n=-1. Horrocks splitting, valid over the field in question, and the Hilbert series give

    F = O + 11O(-1) + 11O(-2) + O(-3)

as an ordinary vector bundle. Equivalently, its graded section module R is free over A=k[x0,...,x4], with graded-generator dimensions (1,11,11,1).

The actual factor-permutation action of D8 fixes A. Since 8 is invertible in k, in each degree the quotient map R -> R/A_+R has a D8-equivariant section (average an arbitrary linear section over D8). Lift the graded minimal generators equivariantly. They form a free A basis by graded Nakayama and the known free ranks. Consequently, directly over k,

    F = O⊗W0 + O(-1)⊗W1 + O(-2)⊗W2 + O(-3)⊗W3

as D8-equivariant bundles. No S4 semisimplicity or division by 24 is used. No integral splitting is assumed, no semicontinuity argument is used, and no ordered transferred-cochain operators T_g are used.

## 3. Integer invariant dimensions without modular-trace ambiguity

This proof can avoid Brauer characters entirely. R_n has its actual monomial permutation basis indexed by {0,...,n}^4. Thus dim(R_n^D8) is exactly the number of D8 orbits, over any field. Burnside's orbit-counting identity gives the integer

    b_n = [(n+1)^4 + 2(n+1)^3 + 3(n+1)^2 + 2(n+1)] / 8.

The class counts are one identity, two transpositions, three double transpositions, and two four-cycles. This is an orbit count, **not** a trace computed in F3 and then treated as an integer.

Because the graded splitting is D8-equivariant and A is D8-trivial,

    sum_n dim(W_n^D8)t^n = (1-t)^5 sum_n b_n t^n = 1+t+t².

Hence

    (dim W0^D8, dim W1^D8, dim W2^D8, dim W3^D8) = (1,1,1,0).

The scalar extension to an algebraic closure does not change these dimensions. In particular no choice of a fourth root of unity or a naive reduced trace is needed.

## 4. Recover the full-sign degrees and the exact sector

Let B=End(L). Projection formula and the equivariant splitting give

    H^i(Y,rho*B) = direct_sum_j H^i(P4,B(-j))⊗Wj.

The four new twist computations give trivial-deck dimensions (1,79,352,0,0), and in degree two give the actual D8 representation

    H²(Y,rho*B) = 2W0 + 10W1 + 20W2 + 20W3.

Its invariant dimension is therefore

    2·1 + 10·1 + 20·1 + 20·0 = 32.

The full-sign deck summand of q_*O_X is O(-2,-2,-2,-2), with the product linearization: the local generator y1 y2 y3 y4 is permutation-invariant. The canonical sheaf of Y is this line bundle with the additional permutation sign from wedging four one-forms. Thus equivariant Serre duality, using End(L) self-duality, gives

    Ext^j_X(P,P)_chi = H^(4-j)(Y,rho*B)^* ⊗ sgn.

Consequently its epsilon-isotypic dimension in degree two equals the trivial-isotypic dimension just computed, namely 32. The other full-sign dimensions are (0,0,352,79,1). Also the epsilon multiplicities in degrees three and four are 24+5=29 and 1, respectively.

The perfect-complex self-duality and finite-flat projection formula suffice. This calculation neither uses nor proves bundle exactness, obstruction-class specialization, naturality, or choice independence.

## Reproducibility and provenance

Run:

    node check_hm_p4_all_twists.js

The complete output is saved in `certificate.json`. The only new matrix maps are 80-by-10 and 50-by-80; the existing twist 0/-1 matrices have at most 1225 rows or columns. The entire certificate is a small exact calculation requiring only Node.js.

The exact formulas for ranks, gamma, all three d maps, and incoming edges are taken from lines 10--21 of:

- [Pinned verify-hm-ext.js](https://github.com/Akilleez-QA/read-em-and-weep/blob/add03476d9055aa00e1e00778eea6332cf8e01cc/research/hm/verify-hm-ext.js), blob fa5231de92b61143e3406111d4af028284db6d55.
- [Pinned geometric model and degree conventions](https://github.com/Akilleez-QA/read-em-and-weep/blob/add03476d9055aa00e1e00778eea6332cf8e01cc/research/hm/ext-model.md).

No earlier large-model output file is an input to this certificate.

## Minimal remaining gates

1. **For the perfect-complex dimension statement:** independent audit of this short Cech certificate and the standard geometric arguments above. No missing twist or large-model rank remains.
2. **For the HM-bundle dimension statement in characteristic 3:** verify that the specified reduced L is exact outside degree zero and has locally free rank-two degree-zero cohomology. Equivalently its fiber maps have ranks 5,8,2 throughout geometric P4. The certificate here does not establish this.
3. **For a statement about the actual obstruction:** verify the geometric carrier comparison and the characteristic-3 naturality/choice-independence hypotheses. Equal target dimensions alone do not provide these, nor identify an ordered finite-model epsilon projector or the actual obstruction coordinates.
