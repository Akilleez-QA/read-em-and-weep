# Independent review of the global weight-twelve scalar splitting

## Verdict

The theorem in `PROOF.md` is correct relative to its explicitly pinned geometric inputs and fixed homogeneous pair marking. In particular, the weight-four mixing does not obstruct the quotient map, although it can obstruct literal extraction of a global weight-twelve coefficient. The global scalar splitting is established without evaluating any prescribed first error or source instance.

This review distinguishes the mathematical proof from the checks in `verify.py`: that script passes, but verifies formal matrix identities and elementary arithmetic only. The global geometric assertions require the arguments and sources described below.

## 1. Actual oriented transitions and regular stabilizers

The actual-frame comparison is justified by Section 2 of [Midpoint Hessian symbol matching by full frame covariance](https://github.com/Akilleez-QA/read-em-and-weep/blob/3d21e93865152ec961ceaf32d48f845399158b69/research/hm/order-four-quadratic-load/MIDPOINT-HESSIAN-SYMBOL-MATCHING-BY-FULL-FRAME-COVARIANCE.md). That source does not merely assume that every frame change has determinant one. It first matches the entire Serre residue, corrects the initial frames to the prescribed physical orientation, and proves that the actual and homogeneous transition determinants agree exactly. Their remaining quotient therefore fixes the exact pair and has determinant one.

Completeness of the stabilizer description follows from regular-sequence algebra, as in [Regular Serre stabilizers have zero normal defect residue](https://github.com/Akilleez-QA/read-em-and-weep/blob/3d21e93865152ec961ceaf32d48f845399158b69/research/hm/order-four-quadratic-load/REGULAR-SERRE-STABILIZERS-HAVE-ZERO-NORMAL-DEFECT-RESIDUE.md). If P sigma=sigma, the two rows of P−I are multiples of (g,−f), so

    P−I = [[a g,−a f],[b g,−b f]].

The determinant-one condition gives a g=b f. Modulo f, regularity of g gives a=f t for a regular t; cancellation of f gives b=g t. Thus P=I+t n everywhere locally, including the zero locus of the pair. There is no meromorphic t or omitted pole term. This argument concerns the regular pair on the vertex cover, not a claim that sigma is nowhere zero.

## 2. Quotient descent with the lower term retained

The exact coefficient sequence and the actual lower-weight warning are both present in Section 4 of [Next-weight midpoint normalization and endpoint transport](https://github.com/Akilleez-QA/read-em-and-weep/blob/3d21e93865152ec961ceaf32d48f845399158b69/research/hm/order-four-quadratic-load/ACTUAL-NEXT-WEIGHT-SEPARATES-MIDPOINT-NORMALIZATION-FROM-ENDPOINT-TRANSPORT.md).

For the even-weight sector, the component cover degrees of a regular G(4) section are w−5 and w−3. Consequently its minimum possible even weight is four, with v4=(0,ell). Since n raises weight by eight and t has nonnegative cover degree, the only lower contribution to weight twelve is t0 n v4. Direct multiplication gives

    t0 n v4 = −sigma t0 f ell.

The physical coefficient line of ell is O(1), while t0 has physical twist −2. Therefore t0 ell lies in Wprime O(−1), exactly the kernel term in

    0 -> Wprime O(−1) -> Sym4(Wprime) O(2) -> V O(4) -> 0.

Equivalently, the mixing is the action on sigma of the weight-four adjoint −t0 tau(v4). Hence it is killed by the quotient E12 / E4 sigma. This proves actual descent of pi(v12); no assumption v4=0 is needed. Composition and triple-overlap consistency are inherited from the actual section transitions after this annihilation.

The conclusion is relative to the fixed marking. It does not assert invariance under arbitrary nonhomogeneous changes of the generators or physical determinant normalization.

## 3. The conic argument is a scalar statement, not a false coefficient-gluing claim

The wedge sigma wedge v belongs to H0(I_Z(6)). In the exact homogeneous pair frames its cover-degree-twelve coefficient is sigma wedge v12. The inhomogeneous term just computed has zero wedge, so this coefficient does glue.

Section 3.2 of the pinned next-weight source supplies the necessary actual geometry: the fixed positive conic lies in Z, and the pure-positive sextic summand of H0(O_Q(6)) restricts isomorphically to its degree-twelve binary sections on that conic. Terms involving negative coordinates restrict to zero. Thus vanishing of the whole wedge on the conic forces this pure-positive coefficient to vanish. This is not inferred from vanishing near the vertex alone.

The regular-pair Koszul identity then yields the unique local expression v12=sigma p4, with p4 in Sym4(Wprime) O(2). The resulting p4 values need not glue before quotienting: their defect is the cubic multiple produced by v4. If v4=0, they do glue, and the acyclicity of Wprime O(−1) proves r12(v)=0 if and only if v12=0. Without that hypothesis only quotient vanishing follows. The proof preserves this essential distinction.

## 4. The scalar splitting is global and has dimension fifteen

The coordinate-ring relation involves only the three positive variables. Its quotient therefore retains the positive/negative bidegree decomposition. In ordinary degree four, the (2,2) summand is

    U22 = (positive quadratics modulo the conic equation)
          tensor (negative quadratics).

Its dimension is (6−1)·3=15. The positive factor is Sym4(Wprime); the negative factor is H0(O_L(2)). Thus vertex coefficient restriction identifies U22 with H0(Sym4(Wprime) O(2)), not merely with a generic fiber of that bundle.

The everywhere-exact cubic sequence is established in [The universal cubic even-defect quotient is the trivial V-bundle](https://github.com/Akilleez-QA/read-em-and-weep/blob/3d21e93865152ec961ceaf32d48f845399158b69/research/hm/order-four-quadratic-load/UNIVERSAL-CUBIC-EVEN-DEFECT-QUOTIENT-IS-TRIVIAL-V.md). After twisting, both H0 and H1 of its kernel Wprime O(−1) vanish. Its induced map on global sections is consequently an isomorphism onto H0(V O(4)), also of dimension fifteen.

Multiplication by the actual global section sigma sends U22 to actual global sections of G(4). In the fixed pair frames these sections have only weight twelve. The stabilizer fixes sigma exactly, so it introduces no hidden lower-weight terms in this construction. This gives the claimed right inverse and proves surjectivity of r12. It does not produce a global splitting of G or of every actual coefficient filtration.

## 5. Fixed-source applicability and what remains unresolved

For an allowed linear scalar space A, the image of sigma A under r12 depends only on the (2,2) projection of A. The stated image-membership criterion is therefore necessary and sufficient for normalization by those allowed scalar corrections. If preserving lower coefficients is required, that condition must be imposed on A as well. The unique U22 correction is usable only when permitted by the source constraints; a unique correction in U22 does not imply uniqueness among all allowed scalar corrections, whose other bidegrees may lie in the kernel.

The conditional operator realization is also correct: tau(sigma)=2n, so changing Lambda1 by lambda changes a tangent representative v by −(lambda/2)sigma when R1=tau(v). Therefore delta Lambda1=2u produces the stated normalization. This factor, sign, and physical twist are consistent; the change still requires the prescribed source/scalar freedom to allow it.

The result does not identify a prescribed first-error section, assert that it is tangent and globally compatible, or compute its quotient value. It does not calculate R2 or remove the need to retain endpoint transport and operator-source conditions. It is compatible with the earlier exclusion of global adjoint K4 ambiguity: the G(4) problem has a scalar kernel that the adjoint trace argument does not eliminate.

## Verification scope

`verify.py` successfully checks the mixing sign, the tau identity, determinant and pair preservation for I+t n, zero wedge of the mixing, the relevant line arithmetic, the fifteen-dimensional scalar space, the thirteen-dimensional pure-positive sextic space, and the acyclic kernel dimensions. It does not test stabilizer completeness, actual frame normalization, the inclusion of the conic in Z, or the global coordinate-ring identifications. Those points are proved above using the pinned sources. No selected actual HM coefficient, prescribed source instance, parameter scan, or large computation is used.
