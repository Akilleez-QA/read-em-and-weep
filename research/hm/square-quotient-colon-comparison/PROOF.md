# Exact square-versus-linear fixed-pair comparison

Work over a field with a graded commutative polynomial ring S. Let K be any graded S-module, u in S_2 and v in S_3. Set M=K/vK and define Q_d=(M/uM)_d and P_d=(M/u^2 M)_d. No regularity on K or M is assumed.

## New comparison

There is a natural short exact sequence
0 -> Q_(d-2)/image[(0:_M u)_(d-2) -> Q_(d-2)]
  --u--> P_d -> Q_d -> 0.                                  (1)

Proof. The right map is the natural quotient. Its kernel is (uM/u^2M)_d. Multiplication by u maps M_(d-2) onto this kernel. Its kernel consists exactly of uM_(d-4)+(0:_M u)_(d-2): if ua=u^2b, then a-ub is annihilated by u, and the converse is immediate. Quotient first by uM and then by the image of the annihilator. This proves (1), including injectivity of its left map.

For K_j=H^1(B(j-1)), the fixed-pair notation of PR477 gives Q5=Q_6 and P5^(2,1)=P_6. Consequently:
P5^(2,1)=0 if and only if Q5=0 AND
M_4=uM_2+(0:_M u)_4.                                      (2)

Equivalently, every degree-four class of M/uM must have a lift annihilated by u in M. This retains a new, explicit intermediate obstruction instead of treating the known surjection P5^(2,1) -> Q5 as an equivalence.

In K coordinates the left term of (1) at d=6 is
K_4 / [uK_2 + (vK:_K u)_4],                               (3)
where (vK:_K u)_4={a in K_4 : ua in vK_3}.
The subspace vK_1 is already contained in this colon subspace. Equations (1)-(3) use actual multiplication, not just Hilbert or Betti numbers.

For finite-dimensional graded pieces,
dim Q_6 <= dim P_6 <= dim Q_6 + dim Q_4.
The difference is exactly dim Q_4 minus the rank of the annihilator-to-Q_4 map. Here Q_4 denotes the degree-four quotient defined above; it is NOT the separately named order-four quotient Q4 in the project.

## All powers

For every m>=1, the same calculation gives
0 -> M_(d-2m)/[uM_(d-2m-2)+(0:_M u^m)_(d-2m)]
  --u^m--> (M/u^(m+1)M)_d -> (M/u^m M)_d -> 0.             (4)
Indeed u^m a=u^(m+1)b is equivalent to a-ub being killed by u^m. Thus higher-power thickening retains successive annihilator corrections; regularity of the polynomial pair in S alone cannot erase them.

## A symbolic counterexample to the missing implication

Take S=C[x,y,z], K=S/(x^3,y,z^5), u=x^2, v=y^3.
The pair (u,v) is S-regular, and K is generated in degree zero and has finite length. Nevertheless vK=0 and u^2K=0. In degree six K has the single basis monomial x^2 z^4. It belongs to uK_4, so Q_6=0, but P_6=K_6 has dimension one.

For a direct check of the correction, K_4 has basis z^4, xz^3, x^2z^2; uK_2 is spanned by x^2z^2; and (0:_K u)_4 is spanned by xz^3 and x^2z^2. The left quotient in (1) is one-dimensional, represented by z^4, and multiplication sends it to x^2z^4.

This is an abstract counterexample, not an HM/source-instance evaluation or an assertion about the original pair.

## Relation to existing work and boundary

PR463 distinguishes the order-four summands and notes that P5^(2,1) only surjects Q5. PR465 gives a separate septic mismatch criterion. PR477 keeps the primary Tor correction. The present result supplies the kernel of the square-to-linear quotient itself, its exact vanishing criterion, and its all-powers extension. It does not discard the primary Tor correction or establish either condition in (2) for the original pair.

Sources:
- https://github.com/Akilleez-QA/read-em-and-weep/blob/8ec3631dcd6937e6cc7491d0200c1c78b5d21434/research/hm/order-four-residue/PROOF.md
- https://github.com/Akilleez-QA/read-em-and-weep/blob/c990d553bc12aae7d979bf1ccda996449fcea910/research/hm/squared-quadratic-residue/PROOF.md
- https://github.com/Akilleez-QA/read-em-and-weep/blob/ff87076794e97238150485b12183c3cd0f4711e4/research/hm/adjoint-primary-extension/PROOF.md

No complete proof repair, selected source value, filtration membership, pure condition, module lift or algebraicity conclusion is claimed.
