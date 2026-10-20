# Independent mathematical review: first minimal HM syzygies

## Reviewed object and verdict

Reviewed file: `PROOF.md` in `hm-minimal-linear-syzygies`.

Exact SHA-256: `4e5077a2fb440633a0d2f0c26baad272e3ab7144d2e17d2e0d8028bcc218e7d9`.

**Verdict: approved as a structural mathematical deduction from the stated imported premises.** No blocking mathematical error was found. This review is not formal proof-assistant verification or a fresh verification of the entire earlier HM dependency chain. It does not certify that local dependency files equal their cited Git commits, which was not needed to check the argument supplied for review.

I read the complete frozen proof and the local proofs `hm-septic-primary/PROOF.md`, `hm-octic-generation/PROOF.md`, `hm-septic-saturation/PROOF.md`, and `hm-sextic-saturation/PROOF.md`. The relevant imported statements are present in these dependencies. No selected HM/source instance, coefficient matrix, numerical rank computation, or polynomial coefficient search was used.

## 1. Actual minimal presentation and symmetric placement

The imported generation result makes the free cover exactly S(-5)⊗H ⊕ S(-6)⊗U_6. Injectivity of quadratic quintic multiplication makes projection from Z_7 onto the sextic component injective. Conversely, being in the quotient kernel X means precisely that the sextic product admits a compensating quadratic quintic product; injectivity makes that compensation unique. Thus Z_7 ≅ X is an identification of actual syzygies, not just an abstract representation match.

The earlier injectivity of linear quintic products and directness of U_6 imply Z_d=0 for d≤6. Thus every degree-seven syzygy is minimal.

Under an equivariant U_6 ≅ T⊗W′, the alternating projection of X is an N-map from the irreducible A*⊗W′ to the inequivalent irreducible A*⊗T_4. It vanishes by Schur's lemma. In characteristic zero, the kernel of this alternating projection is precisely Sym²T⊗W′. Consequently the required symmetric placement is established for the actual embedded X. The arbitrary nonzero normalization of the equivariant identification does not affect this conclusion.

## 2. Universal injection and passage to Betti numbers

For v in the last-two-slot symmetric tensors, t v=v where t=(23). Being killed by first-two-slot symmetrization says s v=−v where s=(12). Directly,

s t s v = −s t v = −s v = v,

t s t v = t s v = −t v = −v.

Since sts=tst, v=0 over C. This proves injectivity of the specified map, with no dimension or genericity assumption on T. Equal source and target dimensions give the optional isomorphism assertion. Tensoring with W′ and restricting to T⊗X preserve injectivity.

With slots ordered as the multiplying variable, the coefficient variable already in a septic relation, and the T factor of U_6, actual polynomial multiplication symmetrizes exactly the first two slots. This verifies that the universal map is the U_6-component of T⊗Z_7 → Z_8. An injective component forces the whole map to be injective.

For clarity, the conversion to β_(2,8)=0 also accounts for degree-eight minimal first-syzygy generators: choose a complement to T Z_7 in Z_8 as their representatives. A degree-eight relation in the first free syzygy cover would have linear coefficients on the degree-seven generators and constant coefficients on the degree-eight generators. Projection modulo T Z_7 first forces all the latter coefficients to vanish; the proved injectivity then forces all the former coefficients to vanish. Hence there is no degree-eight second syzygy, minimal or otherwise.

Since dim Z_8=6·35+10·15−270=90 and dim(T Z_7)=5·10=50, the forty-dimensional quotient gives exactly β_(1,8)=40. The ten degree-seven minimal syzygies give β_(1,7)=10. The separate 70-dimensional nonminimal presentation kernel is correctly distinguished.

## 3. Hilbert numerator

The quoted dimensions I_5 through I_11 follow from the supplied Hilbert function. Applying coefficients 1,−5,10,−10,5,−1 gives the displayed numerator

6t^5+10t^6−10t^7−40t^8+45t^9−5t^10−5t^11.

I independently checked all five displayed arithmetic expressions. Coefficients in degrees below five are zero. For degree n≥12, all six quotient Hilbert values used in its fifth difference have indices at least seven, where they are linear; their fifth difference is zero. The polynomial-ring contribution vanishes in positive numerator degrees. Thus there are no omitted terms from degree twelve onward.

## 4. Depth, regularity and remaining shape

For R=S/I, saturation gives H^0_m(R)=0. The standard section/local-cohomology exact sequence identifies H^1_m(R)_6 with the cokernel of R_6→H^0(C,O_C(6)); the restriction sequence identifies that cokernel with H^1(P^4,I_C(6)), of dimension five. Thus depth R=1. The depth lemma in 0→I→S→R→0 gives depth I=2, and Auslander–Buchsbaum gives pd_S I=3.

The imported regularity eight supplies j−i≤8 for the graded ideal resolution. The use of sheaf regularity here is legitimate for this saturated ideal: H^0_m(I)=H^1_m(I)=0, and higher local cohomology is identified with the corresponding sheaf cohomology. Thus the module and sheaf regularity agree in this setting.

Minimality forces every nonzero differential coefficient to have positive degree. As F_1 starts in degree seven and there is no second syzygy in degree eight, F_2 starts in degree nine. Then F_3 starts in degree ten. A generator with zero image cannot evade these restrictions: exactness would place it in the image of the next minimal differential, which lies in m times the free module, contradicting its being a basis generator.

Regularity now permits only degrees 7,8,9 in F_1, degrees 9,10 in F_2, and degrees 10,11 in F_3. Comparing numerator coefficients gives

β_(2,9)−β_(1,9)=45,
β_(2,10)−β_(3,10)=−5,
β_(3,11)=5.

Writing a=β_(1,9) and b=β_(2,10) recovers exactly the three displayed free modules. The proof correctly leaves a,b nonnegative and undetermined; the Hilbert numerator alone cannot set them to zero.

## Citation precision correction verified

The initial reviewed version attributed the explicit formula U_6=T⊗W′ to PR464, whereas local PR464 establishes canonicity and directness and local PR468 displays the formula using PR467. This nonblocking editorial issue was corrected by the author in the final frozen version identified above. I checked the corrected dependency entry and verified that reversing only that exact text replacement reproduces the original SHA-256 `addb5ad2a827ec1ad7f3d7509377a404a189fbb3f2cc74c6f2e455147d141083`. No mathematical text changed. This final approval applies to the corrected hash. I did not edit the proof.

## Scope of approval

Approval covers the universal lemma, its application to actual minimal syzygies, the exact Betti values β_(1,7)=10, β_(1,8)=40 and β_(2,8)=0, the Hilbert numerator, depth/projective dimension, and the asserted two-parameter necessary resolution shape, conditional on the imported HM premises. It does not determine a,b, construct remaining differentials, or resolve fixed-pair membership or the other expressly excluded open goals.
