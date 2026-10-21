# Initial injectivity throughout the divided-power strand

## Setup and new conclusions

Let S=Sym(T) be the established polynomial ring on five variables over a field of characteristic zero. Let phi:F=S(-2) tensor U -> G=S tensor W present H, with dim U=10 and dim W=2. Put D=I_2(phi), Q=S/D, and let C^a, 0<=a<=8, be the generalized Eagon–Northcott complexes normalized as in PR507. Write M_i^a=H_i(C^a).

Every right-strand divided-power differential after the maximal-minor splice,

C^a_i -> C^a_(i-1),  a+2<=i<=9,

is injective on its minimum internal degree 2i+2. In particular:

- M_2^0 has no component in degree 6, and its support is contained in degrees 7 through 10.
- dim M_1^0_6=225; by complementary duality, dim M_3^8_9=225.
- M_3^1 has no component in degree 8, and its support is contained in degrees 9 through 12.
- M_1^7 and M_1^8 have no components above degree 6; each has support contained in degrees 3 through 6.
- M_3^0 has no component in degree 8; its support is contained in degrees 9 through 12.

These are structural claims about auxiliary graded modules. They do not select the remaining determinantal parameter or evaluate the original HM/source instance.

## 1. A universal exterior-contraction lemma

Fix the universal quadratic relation inclusion from PR490. After choosing a basis x,y of W and suppressing the one-dimensional determinant orientation, it identifies

U=E tensor W,  S_2=E tensor Sym^2 W,

and maps

e tensor x |-> e x^2 tensor y - e xy tensor x,
e tensor y |-> e xy tensor y - e y^2 tensor x.

Here dim E=5. The identification is a vector-space tensor description of S_2; no multiplication identification between the auxiliary binary variables and the five polynomial variables is asserted or needed.

Choose a basis e_1,...,e_5 of E, and put a_j=e_j tensor x and b_j=e_j tensor y in U. Write U=A direct-sum B, where A is the span of the a_j and B the span of the b_j. The two rows of phi on the constant generator spaces satisfy

phi_x(a_j)=-e_j xy,  phi_x(b_j)=-e_j y^2,
phi_y(a_j)=e_j x^2,  phi_y(b_j)=e_j xy.

For r>=2 consider the coefficient-space differential

Delta_r: Lambda^r U tensor W* -> S_2 tensor Lambda^(r-1)U,

obtained by exterior coproduct followed by pairing the W* factor against the W output of phi. This is precisely the divided-power differential with divided-power degree one, with irrelevant common determinant lines omitted.

Write an element of the source as P tensor x* + R tensor y*. For a dual basis vector a_j* or b_j*, let i_(a_j*) or i_(b_j*) denote signed exterior contraction. If Delta_r(P tensor x* + R tensor y*)=0, comparison of the independent S_2 basis coefficients gives, for every j,

coefficient e_j x^2:  i_(a_j*) R=0;
coefficient e_j y^2:  i_(b_j*) P=0;
coefficient e_j xy:  -i_(a_j*) P+i_(b_j*) R=0.

The first family implies R belongs to Lambda^r B; the second implies P belongs to Lambda^r A. This follows directly by expanding in the exterior basis of A direct-sum B: any term containing an a_j, respectively a b_j, is detected by the corresponding contraction.

The two terms in the third family then lie in Lambda^(r-1) A and Lambda^(r-1) B. For r>=2 these are disjoint summands of Lambda^(r-1)(A direct-sum B). Consequently every contraction of P by a_j* and every contraction of R by b_j* vanishes. Thus P=R=0, proving injectivity of Delta_r.

The restriction r>=2 matters: for r=1 the two exterior-degree-zero subspaces coincide, so this argument does not apply. No claim for r=1 is used.

## 2. Every positive divided-power order

For p>=1 consider

Delta_(r,p): Lambda^r U tensor D_p(W*) -> S_2 tensor Lambda^(r-1)U tensor D_(p-1)(W*).

Write an input as

sum_(j=0)^p P_j tensor x*^[p-j] y*^[j],

using divided-power monomials. For each j=0,...,p-1, the coefficient of x*^[p-1-j] y*^[j] in its image is precisely

Delta_r(P_j tensor x* + P_(j+1) tensor y*).

The divided-power contraction convention has no binomial factors. Equivalently ordinary monomials give nonzero factors that can be removed by rescaling. Since Delta_r is injective for r>=2, each adjacent pair vanishes. Every P_j belongs to an adjacent pair, so the whole input is zero. This proves injectivity for every p>=1 and r>=2.

The right strand of C^a has terms

C^a_i=Lambda^(i+1)F tensor D_(i-a-1)(G*) tensor det(G*)

for i>=a+1. For i>=a+2 put r=i+1 and p=i-a-1. The minimum internal degree is 2(i+1), and the differential on that degree is Delta_(r,p), tensored with the common determinant line. Here r>=3 and p>=1, so the lemma applies.

Consequently M_i^a has no components in degrees at most 2i+2 whenever i>=a+2. This excludes the initial right-strand kernel; it makes no claim that the full polynomial differential is injective in higher degrees. For i>4 the homology already vanishes by PR507, so the new middle-homology consequences occur at lower indices.

## 3. Ordinary Eagon–Northcott: a new exact component

For a=0, the chain terms in question are

C^0_1=45S(-4),  C^0_2=240S(-6).

The initial differential C^0_2 -> C^0_1 is injective, so M_2^0_6=0. Since C^0_2 has no components below degree 6, M_2^0 starts in degree at least 7.

The Hilbert function of Q vanishes in degree 6. Therefore D_6=S_6 has dimension 210. The degree-six kernel of C^0_1 -> S has dimension

45*dim S_2 - dim S_6 = 45*15-210=465.

The image of C^0_2 in degree 6 has dimension 240 by the proved injectivity. Hence

dim M_1^0_6=465-240=225.

This calculation uses only small free-module dimensions and a structural injectivity proof, not a numerical matrix-rank evaluation. PR508 already gives dim M_1^0_4=10 and dim M_1^0_5=102. Thus the first three nonzero component dimensions of this ordinary defect are 10,102,225 in degrees 4,5,6. The third number is a component dimension, not a new minimal-generator count.

## 4. Reflected support constraints

PR507 establishes

M_i^a = (M_(4-i)^(8-a))^vee(-15) tensor Omega,

where Omega is one-dimensional. PR508 proves initial-degree injectivity on each left strand.

Applying the latter to M_2^8 gives no components below degree 5. Reciprocity then bounds M_2^0 above by degree 10. Combining with Section 3 gives support M_2^0 in degrees 7 through 10. Equivalently M_2^8 is supported in degrees 5 through 8.

The component M_1^0_6 reflects to M_3^8_9, so its dimension is 225. Together with PR508's endpoint values, the reflected dimensions are

dim M_3^8_9=225,  dim M_3^8_10=102,  dim M_3^8_11=10.

No vanishing below degree 9 is inferred from this list.

For a=0 and a=1, Section 2 proves M_3^a has no component in degree 8 and hence starts in degree at least 9. Reciprocity with M_1^8 and M_1^7, each starting in degree at least 3, bounds both modules above by degree 12. Thus M_3^0 and M_3^1 are supported in degrees 9 through 12. Reflecting again, M_1^8 and M_1^7 are supported in degrees 3 through 6, strictly sharpening the earlier degree bounds. Their already known degree-three and degree-four dimensions are respectively (85,255) and (70,220). The degree-five and degree-six dimensions remain unresolved here.

## Exact dependencies and limits

- PR490, universal quadratic relation inclusion, commit 1c5ad353bb5f1808150f64cde3c29b92c6e13d91: https://github.com/Akilleez-QA/read-em-and-weep/blob/1c5ad353bb5f1808150f64cde3c29b92c6e13d91/research/hm/dual-tensor-bridge/VERIFICATION.md
- PR495, determinantal quotient Hilbert function, commit b972aa22b72658b419e2c8948a56e0eec7f59e13: https://github.com/Akilleez-QA/read-em-and-weep/blob/b972aa22b72658b419e2c8948a56e0eec7f59e13/research/hm/fitting-thickening/PROOF.md
- PR507, normalized complexes and homology reciprocity, commit 87c9b317bd4b1116e63212a6d7ec2730486b2032: https://github.com/Akilleez-QA/read-em-and-weep/blob/87c9b317bd4b1116e63212a6d7ec2730486b2032/research/hm/generalized-en-defects/PROOF.md
- PR508, left-strand injectivity and low defect components, commit a59d3dbfdad8b5516cd17c91890b669f2567bdb7: https://github.com/Akilleez-QA/read-em-and-weep/blob/a59d3dbfdad8b5516cd17c91890b669f2567bdb7/research/hm/middle-defect-duality/PROOF.md

The generalized-complex differential conventions can be compared with Andrew R. Kustin, “Canonical complexes associated to a matrix,” Section 3, https://arxiv.org/abs/1509.04367 . The coefficient calculation above verifies the relevant differential directly in the pinned normalization.

This is an authored structural proof conditional on the pinned inputs, awaiting independent review; not formal proof-assistant verification. No selected actual HM/source-instance evaluation, numerical multiplication matrix or rank computation, coefficient search, or large computation was performed. Exact full middle-defect modules, the remaining determinantal connecting parameter, original fixed-source vanishing, higher-order lifting and algebraicity are not settled.
