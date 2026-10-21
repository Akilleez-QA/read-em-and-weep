# Independent mathematical review

Reviewed PROOF.md with SHA256 328204e5bf0cfe7e63dc752f0edcc096dd6f8418776d64b3ad0d985fa8924231. The structural reduction is valid conditional on its pinned inputs.

## Representation and parity checks

PR453 at 56516a96a7eacfde0c8e272ca38db415cc7f294b, Section 2, explicitly records S1 tensor A = V tensor (U' plus W0) and E tensor E = V tensor (U plus W'). These agree with the stated Galois conjugates of Horrocks--Mumford Lemma 3.3. Combining the latter identity with Lambda2 T = E tensor W0 gives the target multiplicity W0 plus Qspin plus T4. The source U plus R6 is the preceding actual Koszul quotient of PR523, not a representation assigned by dimension.

The genuine quotient action on Hom_Gamma(V,-) is essential. Under that action the central involution fixes the projective base, acts positively on O(2), and separates the stated even and odd coefficient representations. Thus the block diagonal form and the direct-sum cokernel identity follow from actual eigenspaces.

## Even-block rank check

Nonzero constant source in a zero even block would contradict H0(K)=0. For a positive generic rank r, the ideal of r-minors defines an invariant divisor of degree at most 2r, hence at most six. The orbit lower bound twelve makes this divisor empty, so the rank is constant.

For rank one, the image is a globally generated line O(d), with 0<=d<=2 because it injects into 4O(2). Its equivariant quotient from U forces U to occur in Sym^d(W'), which it does not. For rank two, the kernel O(-d) and image degree d satisfy 0<=d<=4; its inclusion into UO gives the same impossible occurrence for d<=4. The perfectness of SL2(F5) excludes an additional character in either line linearization.

Rank three therefore holds everywhere. The line cokernel has degree eight, since the target has rank four and twist two while the source has degree zero. The degree-eight quotient, rather than degree six, is consistent with T4 occurring in Sym6(W').

## Odd block and limitations

The remaining block is square of size six, with source twist zero and target twist two. Its determinant is a section of O(12). Coefficient determinant representations are characters of the perfect group and are trivial, so this section is invariant. If nonzero, its divisor is the unique reduced orbit of length twelve; the Smith-form multiplicity-one argument gives corank exactly one at each point. The proof does not incorrectly infer nonvanishing from invariant existence.

The kernel and fiber-kernel equalities hold because the even block is fiberwise injective. The multiplicity cokernel splits as O(8) plus the odd cokernel because the entire map is the parity direct sum. No assertion about flatness of the odd cokernel is required.

## Verification boundary

This is independent mathematical review, conditional on the exact prior inputs, not formal proof-assistant verification. No selected HM/source-instance evaluation, numerical multiplication-rank calculation, coefficient search, or large computation was used. Determinant nonvanishing and the actual remaining column behavior are not established by this note. Original fixed-pair residual, higher-order lifting and algebraicity remain separate.
