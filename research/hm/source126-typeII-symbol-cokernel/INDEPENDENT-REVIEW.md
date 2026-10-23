# Independent verification: hidden-symbol scheme and kernel bundle

Reviewed 2026-10-23 against:

- PROOF.md SHA256 `aaa6466be0a8bf9455a480f0ccec892fed7f2896982f258c0407ed16ef03c8fd`
- verify.py SHA256 `686c5c1eb65bc00d3ddee0d1ee9971f0ec8e5c10c118c2432039e20245e170f4`
- INPUTS.json SHA256 `e78363f3c1110044f92fab432408bcf73ab93369fc9d87dc23e5296fd99e57d5`
- RESULT.json SHA256 `52d9582ae74e931acc0f4dd96a56e7164a6cd47024e975dc181927f93a35572b`

## Outcome

No mathematical blocker was found. The reduced projective conic, exact raw homogeneous ideal, cokernel twist, ambient kernel Chern classes, and Tor-corrected conic restriction are justified. All conclusions retain the explicit nonzero-mu alternative and the pinned internal-symbol hypotheses. They do not determine the actual scalar branch or the original multiplication map.

## Checks of the critical arguments

1. **Universal normalization.** With lambda and mu nonzero, constant rescaling of the two independent domain factors converts the symbol to its normalized universal polynomial matrix. This preserves kernel and cokernel isomorphism classes and the determinantal ideal. It is an invertible change of model, not a selection or evaluation of actual HM coefficients. The available SL2 covariance concerns the forced binary-form expression; no actual HM SL2 symmetry is presumed.

2. **Transversality.** At a=x^2 the displayed pair (y^2,-lambda xy^3/(6mu)) is in the kernel. Its derivative in a=x^2+gamma y^2 is exactly (4lambda/3)y^4. The target image at the square is x Sym3 W, so this derivative is nonzero in its one-dimensional cokernel. Since Delta=-4gamma, the direction is normal to the discriminant. This calculation was independently expanded and reproduced by the checker.

3. **Local Fitting ideal and local freeness.** A unit rank-four minor permits local row/column reduction to an identity block and a remaining row. Every entry of that row vanishes on the smooth reduced conic and is divisible by its local equation t. The nonzero normal derivative makes one quotient by t a unit. SL2 covariance transports this to every conic point. Hence the local shape is diag(I4,t,0,0,0), with the rectangular shape understood. It gives maximal-minor ideal (t), cokernel O/(t), and free kernel rank three. In particular, the cokernel has no unproved thicker support. The image sheaf is locally free (isomorphic to O^4 plus tO); this does not mean it is a saturated subbundle of the target.

4. **Exact homogeneous ideal.** Every maximal minor is homogeneous of degree five and vanishes on the irreducible discriminant, so is Delta times a cubic. The ten displayed quotients agree with exact determinant expansion. Their coefficient matrix has determinant 2^40 and therefore spans every cubic monomial. Thus I5=Delta m^3 exactly, and restoring the nonzero scalar factors does not change the ideal. Saturating by the irrelevant ideal gives (Delta). The distinction between this projective reduced conic and the raw affine ideal with additional origin structure is necessary and is correctly retained.

5. **Cokernel gluing and twist.** On the Veronese parametrization, the image bundle is the injective image of Sym3 W tensor O(-1) under multiplication by the tautological line. Its quotient is Sym4(W/O(-1))=O(4). Since the local normal form already proves that the global cokernel is the pushforward of a line bundle on C, this identifies that line bundle as O_C(2), not just a fiberwise quotient of the correct dimension. The Veronese pullback of O_C(1) is O(2).

6. **Ambient Chern data.** The divisor sequence gives [i_*O_C(2)]=[O(2)]-[O]. Consequently [K]=8[O(-1)]-6[O]+[O(2)], of rank three with ch=3-6H+6H^2. This yields c1=-6H and c2=12H^2. Local freeness was proved separately, so this is not an inference from a virtual class alone.

7. **Kernel of the restricted map.** At a=l^2, the exact factorization of the bracket implies h=l r and k=-(2mu/lambda){l,r}. At l=x the converse follows because partial_y h divisible by x eliminates the y^4 coefficient of h; covariance gives the general assertion. The resulting injective parametrization is linear in l. Before the original domain twist its kernel family is Sym3 W O(-1); after pulling back O_P(-1)=O_P1(-2), the kernel of the restricted map is Sym3 W O(-3), rank four.

8. **Tor orientation and twist.** Writing the full sequence through im Phi, which is locally free by the local normal form, gives an injection of K|C into the kernel of the restricted map. The quotient is Tor1(i_*L,O_C)=L tensor O_C(-C). With L=O_C(2), this is O_C, whose pullback is O_P1. This verifies the exact sequence and rules out identifying the two kernels merely from their equal degree.

9. **Identify the Tor boundary, not just its degree.** For l=x and r=y^3, the parametrized kernel pair has normal derivative -8mu y^4 modulo the square image, nonzero. This is the local boundary after division by a local conic equation, up to the harmless nonzero coordinate factor. The construction is equivariant in the universal model. The SL2-equivariant Hom space from Sym3 W O(-3) to O is one-dimensional, so the boundary is a nonzero multiple of complete cubic evaluation. Its exact kernel is Sym2 W O(-4), by the tautological cubic evaluation sequence. Therefore K|C has rank three and is A O(-4), while the kernel of the restricted map has rank four and is S O(-3). The displayed extension is non-split: there are no global sections of S O(-3) to split its quotient O.

## Reproducible evidence

Executed `python verify.py` and `python -O verify.py`. Both passed 146 exact checks, and their entire JSON outputs were byte-identical, matching RESULT.json at the hash above. These checks include all 56 maximal minors, the ten-minor spanning determinant 2^40, both transverse derivative calculations, the globally parametrized conic-kernel identity, evaluation-kernel rank certificates, local normal-form diagnostics, Chern arithmetic, and immutable-input authentication.

The finite and symbolic tests support the proof; they are not proof-assistant verification, actual HM evaluations, or a replacement for the geometric gluing and Tor arguments. The PR965 interface is used with all its stated hypotheses and was not re-proved in full here.

## Scope retained

The result is conditional on the two P-surplus Type II footprints and mu nonzero. It does not show that this scalar alternative occurs, determine an original higher Bockstein, imply original generic surjectivity, remove a footprint or catalogue pair, or complete the original repair. No publication was performed as part of this review.
