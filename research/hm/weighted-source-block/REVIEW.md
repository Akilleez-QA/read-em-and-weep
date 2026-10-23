# Independent final whole-package review

Verdict: PASS. No mathematical correction or publication blocker found. This review covers the complete final proof, including the forbidden-alignment theorem in Section6, not only the block-type classification.

This is mathematical review with bounded exact arithmetic, not formal proof-assistant certification.

## Reviewed final bytes

SHA256:

- PROOF.md: 506434eda15b1e96ebc50b39752aa25a5efebb18300b92f011ce14248cb1917c
- verify.py: daec19bb42be954944d67cb0d17b8069175a302590218f0e700d6ec8dd4b37e1
- INPUTS.json: ccc6cdafa5da27b6af59359428b3ad31f376f95059bef1ba4fe2f5dba3ea2a0d
- REPRODUCE.md: c3fc2aff9bdfe6a19020918ab35220cb823e03ffeb43271f4d5259577b6c46e8

The reviewer independently fetched the original PR1009 proof at commit0d75f42c4e79654c8fbef57e6ce56a1f06cdf9a1 and path research/hm/common-target-branches/PROOF.md. Its decoded bytes exactly equal the local audit input, and its recomputed Git blob is 6101c8d1856b55e0e770f9a4ce4c36d0702336d9, matching INPUTS.json. The input's actual presentations and explicit complement-choice caveats support the claimed interface.

## Mathematical checks

1. The weighted coefficient representations are W tensor Sym3W=A+D and A tensor Sym2W=1+A+D. Since the target has no trivial constituent, only A and its two D copies can receive the weighted source. The universal A channels have fiber ranks one and two respectively. Thus an actual fiberwise-injective weighted restriction requires a nonzero D coefficient image.
2. The D channels are the tautological multiplication subbundles l^3W and l^2A in Sym4W. Universal polarization identifies their quotient bundles with A O(2) and W O(3). This proves saturation and local freeness without selecting an actual parameter or matrix.
3. Projection onto D gives the stated extensions by A O. Both invariant Ext spaces have dimension one. Hom_G(D,A)=0 makes the actual pushout boundary injective, and its source has dimension one. Therefore the class is nonzero exactly when the actual A component is nonzero. The proof does not infer nonvanishing merely from the Ext dimension.
4. With both coefficient components nonzero, their distinct irreducible channels span the full A+D target. Dual global sections then give H0(B*)=0. Since B is globally generated, it is ample. Rank and degree force O(1)^6 in the W branch and O(2)+O(1)^4 in the A branch. The cohomology identities H0(B(-1))=W tensor A or A tensor W both reduce to W+S. Together with the absence of one-dimensional characters of 2I, these identify the middle types as (W+S) O(1) and S O(1)+O(2). The split types follow directly when the A component is zero.
5. Quotienting the actual weighted subbundle in the whole target gives the actual E18-source presentations. The new targets are locally free, and the source maps remain fiberwise injective because their quotients are locally free. Their extensions by the constant R16 representation split equivariantly because all four B types have H1 zero. No canonical choice of splitting or replacement of the actual induced map is claimed.
6. The unique S source has coefficient support A+D and a nonzero D vector v: otherwise a rank-four subbundle would inject into rank three. Each allowable weighted-complement shift space is one-dimensional and factors through this S. The multiplication generators compose with its D channel by multiplication by l^3 or l^2, with nonzero scalar. A triangular source automorphism therefore changes the weighted vector d to d+t c v while preserving fiberwise injectivity for every t. Proportional nonzero d and v would permit cancellation of the D component, contradicting item1. Thus the forbidden-alignment conclusion d wedge v nonzero is valid and is invariant under the stated shifts and channel rescalings.
7. The proof accurately retains complement dependence of the individual weighted subbundle and A-component distinction. It does not claim that this distinction is a new intrinsic scalar, nor that any remaining C type or the existing lambda branch has been selected.

## Reproducibility and scope

The reviewer inspected the complete standard-library verifier and ran both python verify.py and python -O verify.py. Both passed with identical output. Independently repeated fixed character calculations confirm the support, one-dimensional Hom and Ext spaces, and section representations. The verifier uses explicit runtime failures rather than optimization-removable assertions.

REPRODUCE.md correctly lists the five publication files, omits the copied original, and reconstructs it by exact immutable git-show before checking its Git blob. The bounded verifier does not replace the universal geometry or mathematical review.

No actual HM/source coefficient, selected point, parameter, jet, derivative, matrix or instance rank was evaluated. All arithmetic uses fixed abstract characters and bundle rank/degree identities. The new theorem excludes the alignment of two actual D multiplicity directions; it does not eliminate a source pair or choose an actual remaining bundle type.
