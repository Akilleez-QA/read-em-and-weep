# Independent verification of the Type II internal-symbol discriminant theorem

Reviewed on 2026-10-23 against these final bytes:

- PROOF.md SHA256 `f15de9b7966aac66c5391ca1264eb5dfc705baf8554d9d6fe57ad6a8541d9663`
- verify.py SHA256 `5bd5073751b629a9875a84173061c2cfaf495a1639871d5267b97a9ae8ea8ed0`
- INPUTS.json SHA256 `9875efaf0429434ccb9ecd7599a10392e1e32c3886aa3e02708b75fe8c9971de`
- RESULT.json SHA256 `04a7895003b69cf89d73c48d8f04ca13519d2b7cdf154f42c34f17c76b4bdeff`

## Outcome

The theorem and exact rank stratification are valid relative to the two pinned interfaces. No mathematical blocker was found. The actual scalar mu remains unselected, as required. The theorem is about the full internal first symbol in the two stated conditional Type II footprints, not the original first Bockstein or the full original multiplication map.

## Independent mathematical checks

1. The PR961 input bytes agree exactly with the previously independently reviewed Type II joint-annihilator proof. They supply the actual invariant kernel A+D, internal cokernel D, and nonzero A-part of this internal symbol. The PR944 input supplies the needed Sym6 W=V+P decomposition. Neither imported statement is strengthened silently.

2. Clebsch-Gordan gives A tensor A=D+A+1 and A tensor D=Sym6 W+D+A=V+P+D+A. The representations A,V,P,D are distinct, so D appears exactly once in both tensor products. Hence each relevant G-equivariant Hom space has dimension one. Binary-quadratic multiplication spans the first; the alternating first-derivative pairing spans the second. Its nonzero test {x^2,y^4}=8xy^3 uses precisely the stated normalization.

3. Thus the actual G-equivariant symbol must be lambda times multiplication plus mu times the first transvectant, with lambda nonzero by the pinned A-part theorem. This does not assume any SL2 action on the actual module, U, Z, or surrounding geometric data. It first identifies the symbol in binary-form models using G-Hom uniqueness. The resulting universal formula is SL2-covariant, which is sufficient for rank classification by binary-form orbits. Different equivariant identifications change the scalar normalization but not whether mu vanishes or any displayed rank.

4. For mu=0 and a nonzero, multiplication by a is injective on the three-dimensional A domain by the integral-domain property of C[x,y]. The complete symbol therefore has rank three, kernel dimension five, and cokernel dimension two.

5. For a=x^2, the transvectant is 2x partial_y. Its image is precisely the span of x^4,x^3y,x^2y^2,xy^3. Multiplication by x^2 has image inside that four-space. For mu nonzero, the D-domain alone has rank four and no input can produce y^4. This proves rank exactly four, not just a lower bound. The checker uses D columns with coefficients 2,4,6,8, producing minor 384 mu^4 in the specified order.

6. For a=xy, the transvectant is y partial_y minus x partial_x, with quartic eigenvalues -4,-2,0,2,4. It fills all quartic monomials except x^2y^2. The independent A-domain contributes that missing monomial since lambda is nonzero. The stated column order gives the exact minor 64 lambda mu^4, so the full rank is five.

7. Every nonzero complex binary quadratic is, up to a nonzero scalar and determinant-one coordinate change, either x^2 or xy according to whether beta^2-4alpha gamma vanishes. Scaling a scales the full bilinear symbol, preserving rank. Therefore the two normal-form computations exhaust all nonzero directions. For mu nonzero the non-surjective locus in projective A is exactly the discriminant conic as a set. No scheme multiplicity follows or is claimed. At a=0 bilinearity makes the symbol zero.

8. The kernel/cokernel dimensions follow from a domain of dimension eight and target of dimension five. No cancellation can occur between the two domain summands when computing the image sum: the inputs vary independently. No relation between lambda and mu, other than lambda nonzero, is needed for the stated ranks.

## Reproducible execution

Executed `python verify.py` and `python -O verify.py`. Both passed 127 checks. Their complete JSON outputs were byte-identical and matched RESULT.json with SHA256 `04a7895003b69cf89d73c48d8f04ca13519d2b7cdf154f42c34f17c76b4bdeff`.

The exact outputs report 52 rank-three, 8 rank-four, 44 rank-five, and 4 zero synthetic cases, together with the symbolic minors 384 mu^4 and 64 lambda mu^4. Both pinned input SHA256 and Git-blob hashes authenticate. These finite cases support the universal argument above; they do not replace the orbit proof, independently establish the earlier geometry, evaluate an HM instance, or provide a proof-assistant certificate.

## Scope retained

The hypotheses remain actual Type II, whole-J compatibility, and one of the two P-surplus footprints. Neither mu=0 nor mu nonzero is selected as actual. The internal D cokernel maps to zero in the original P cokernel, so internal rank four or five neither contradicts original first-Bockstein vanishing nor proves original full rank. No footprint, source, source-dual pair, or catalogue label is removed by this rank stratification.
