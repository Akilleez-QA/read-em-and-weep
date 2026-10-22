# Independent mathematical review

Reviewed document: `PROOF.md`  
SHA-256: `38ec024e8ca4968b3e76618a67f9a06df2b041e0662d22a0acb34f72ac3fcc85`

## Verdict

The proof is correct under the pinned representation-theoretic interface and the stated PR665 actual two-input datum. The generic-rank argument is independent of the actual minors; the reduced degree-twelve degeneracy divisor is proved scheme-theoretically; and the splitting, equivariant factorization, and uniqueness statements follow without additional actual HM evaluations. No unresolved mathematical gap was found.

## Checks

1. **Bundle degrees and pure alternating family.** On X=P(W), the kernel bundle is W⊗O(−3), while the quadratic endpoint twist is O(4). Therefore the normalized map is W⊗O(−7)→P⊗O. The identity (u⁴,u³w)₁=4[u,w]u⁶ has degree seven in u, exactly as required. The pure alternating map has constant rank one, kernel O(−8), and saturated image O(−6).

2. **Nowhere-zero pure powers.** A projective orbit has at least twelve distinct points. Any n+1 distinct points on the degree-n rational normal curve span SymⁿW. For n=6,8, vanishing of a projected pure power would therefore force the whole representation into a proper complementary summand. Both C6 and C8 are nowhere zero.

3. **Wronskian exclusion.** For the five-dimensional D⊂Sym⁸W the Wronskian degree is 5(8−5+1)=20. A section vanishing to order seven forces ramification weight at least three at each orbit point, hence at least 36 in total, impossible. This proves the symmetric osculating map is fiberwise injective. The argument remains valid when the linear series has base points.

4. **Generic rank.** With α≠0, the pure column αC8 is nonzero everywhere. If β≠0 and the generic rank were one, C6 would lie generically in the independently constructed subbundle F≅W⊗O(−7). Its composite with the locally free quotient would then vanish globally, giving a nonzero map O(−6)→F. The vanishing H⁰(O(−1))=0 excludes this. There is no circular dependence on the later saturation calculation.

5. **Complete degeneracy classification.** The minors have degree fourteen and are not identically zero. Their common ideal on the smooth curve gives an invariant effective divisor of degree at most fourteen. The only possible nonempty such divisor is the unique twelve-point C5 orbit, reduced. At a C5 point, the pure and mixed values have distinct weights η⁸ and η⁶. Both P-weight spaces have dimension one: subtracting the Sym⁴W weights from those of Sym⁸W leaves exactly η²,η⁴,η⁶,η⁸. Each channel has nonzero mixed value, so its vanishing defines exactly one family line, disjoint from both parity axes. The supplied actual datum identifies that line with C_act.

6. **Saturation and splitting.** Local Smith normal form identifies the common minor order with length(E/I). Thus deg E=−14+12=−2, and reduced degeneracy gives local elementary divisors (1,t). Irreducibility of P forces H⁰(E)=0: otherwise E would contain every constant section of P⊗O, impossible for rank two. Birkhoff–Grothendieck then gives E=O(−1)². The dual quotient argument is equally valid and gives the underlying quotient O(1)².

7. **Equivariant identification.** R=H⁰(E(1)) is two-dimensional and the inclusion induces a nonzero G-map R⊗W→P. It is an isomorphism by dimension and irreducibility. This also forces R to be irreducible. Since W⊗W=1⊕Sym²W, R is not W and is the other binary doublet W′. The inclusion is uniquely the tautological W′⊗O(−1)→W′⊗W⊗O, up to scalar. The equivariant quotient is W′⊗O(1), by the tautological sequence and det W=1.

8. **Sextic uniqueness and determinant.** The space of equivariant sextic arrows is

   Hom_G(W⊗O(−7),W′⊗O(−1)) ≅ Hom_G(Sym⁶W,P) ≅ C.

   Here H⁰(O(6))=Sym⁶W*, W*≅W, and W′⊗W≅P. Thus the first arrow is unique up to scalar, not merely the image inclusion. Its determinant has degree twelve and exactly the already proved reduced C5 divisor. Both binary doublets have determinant one, so this determinant is invariant. No numerical actual normalization follows or is claimed.

## Input economy and scope

The stated actual input can be weakened. A nonzero pure value at a C5 square already implies α≠0. A zero mixed value then excludes β=0 by the fiberwise injectivity of the symmetric map. Thus the public pure-nonzero/mixed-zero datum alone establishes the needed nonzero parities; retaining PR665's stronger statement is harmless.

The proof concerns restricted rank on the square conic. It does not establish a new ambient rank result, higher Bockstein, source-membership statement, lift, or repair, and does not identify the actual family with an unrelated nonsquare channel. The distinction between a fixed restricted map and the family-detection map is maintained.

## Pinned inputs

- [Square reconstruction](https://github.com/Akilleez-QA/read-em-and-weep/blob/1325647fd916bf2daa71b11efeae6d52cfefa2cd/research/hm/endpoint-square-reconstruction/PROOF.md)
- [Wronskian/base-locus exclusion](https://github.com/Akilleez-QA/read-em-and-weep/blob/f75a18fd411350adda35dedf18751eee002a39bc/research/hm/endpoint-base-locus-exclusion/PROOF.md)
- [Secant-detection exceptions](https://github.com/Akilleez-QA/read-em-and-weep/blob/ad3ab59f6fbbbb3e5bde1da58b3b92a1f49c6889/research/hm/secant-detection-exceptions/PROOF.md)
- [Actual endpoint parity and two-input datum](https://github.com/Akilleez-QA/read-em-and-weep/blob/1cc13d0bf21abc6553c51a48c72896758cbc333a/research/hm/actual-endpoint-parity-consequences/PROOF.md)
