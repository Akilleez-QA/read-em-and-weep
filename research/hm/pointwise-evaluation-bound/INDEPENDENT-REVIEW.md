# Independent mathematical review

Verdict: PASS for the stated deductions from the three pinned repository inputs.

Reviewed PROOF.md SHA-256:
`aa82c0fa97dfdd2b26d736e37dbfe37c113fa3abfa664fcb1aa0fdd7b44519ae`

## Universal lemma

The two off-diagonal images are exactly B direct-sum 0 and 0 direct-sum A, not merely subspaces of these spaces. Modulo their sum, H maps L with kernel L intersection (C direct-sum C), because a vector of L already has its first component in A and its second component in B. This proves dim Y=s+4-d.

The cases exhaust all possibilities since dim L=4 forces s>=4. For s>=6 the off-diagonal sum suffices. For s=5 and dim Y<=5, d=4 implies both projection images equal C, contradicting the odd sum of their dimensions. For s=4, L=A direct-sum B and d=2dim C. A value dim Y<=5 forces dim C>=2; dim A+dim B=4 then forces A=B=C of dimension two. Conversely this tensor-product plane has Y=L. Thus dimension five is impossible without any geometric assumption.

The abstract sharpness example has dimension four: its coefficients give components (alpha e1+beta e2+gamma e3, beta e1+gamma e2+delta e3), whose simultaneous vanishing forces all four coefficients to vanish. Both projections equal E, so Y=E direct-sum E has dimension six. Its intersections with the two coordinate copies of E are respectively C(e1,0) and C(0,e3). Since e1 and e3 are independent, no nonzero full fiber occurs. This checks sharpness only for the universal four-plane problem; it does not assert that this example is an actual HM star.

## Actual application and dependency check

The following exact public repository files were read during review:

- PR543, 7bf725bcd857a2deb975f9ecb80fca32e7833ae0, PRIMARY-INJECTION-AND-FAILURE.md: the nonzero exterior-plus-sl2 multiplication formula, four-dimensional star, and Galois-conjugated HM Lemma 2.5 no-full-fiber assertion are explicitly recorded. The new lemma applies to that exact star and proves the pointwise rank-six bound.
- PR543, 8d24a12c4af9c922db2052a360c96a053dcba5b8, PRIMARY-BAD-CODIMENSION-THREE.md, Sections 1–2: the actual Euler-composed matrix has the same fiber rank; the invariant-gcd argument yields dimension at most two for the rank-at-most-six locus. No stronger degeneracy assertion is used here.
- PR547, 5a8efc999e9b886c51f18232a580407bac4bbe66, primary-evaluation-generic-surjectivity/PROOF.md: generic rank ten follows from its universal annihilator-support lemma and its credited preceding rank/full-support inputs. This review checks its use as a pinned input, rather than claiming a new independent verification of all upstream representation-theoretic dependencies.

## Incidence and projective spaces

The rank-r kernel has dimension 15-r, so its projectivization has dimension 14-r. Rank six contributes at most 2+8=10. Ranks seven, eight, and nine occur in the proper rank-at-most-nine locus in P4, hence have base dimension at most three; their respective bounds are 10, 9, and 8. Rank ten contributes at most 4+4=8. Finite locally closed rank stratification therefore gives dim Z<=10. Projectivity of the first factor makes its image B closed and does not increase dimension. Consequently codim(B,P14)>=4.

A general P3 avoids B by 3+10<14. For an arbitrary prescribed point p, the closure of the image of B minus {p} under projection from p has dimension at most ten. A general P2 in P13 avoids this closure by 2+10<13. The inverse linear space with vertex p is a P3 whose intersection with B is contained in {p}. This argument is valid whether or not p belongs to B and makes no membership decision at p.

## Scope and verification status

No expected-codimension premise is needed. The deductions concern primary multiplication only, not full adjoint invertibility, residual surjectivity, its twenty-dimensional lift boundary, Q4, a selected source pair, higher-order lifting, or algebraicity. No selected actual HM/source-instance calculation, coefficient search, numerical matrix evaluation, or large computation was used in this review. This is independent mathematical review, not proof-assistant verification.
