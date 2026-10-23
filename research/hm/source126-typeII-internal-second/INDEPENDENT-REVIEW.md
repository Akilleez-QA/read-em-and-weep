# Independent mathematical review

## Scope and verdict

The new result is conditional internal second-Bockstein vanishing for the source126 Type II annihilator subcomplex under compatibility of the entire radical with Q. The original third-Bockstein vanishing is an imported theorem, not a new result here. No original fourth symbol, full-radical occurrence, catalogue exclusion, or complete repair follows.

The proof was independently checked for the following substantive points.

1. A fixed equivariant right inverse of Q on its image constructs the internal second as a global quadratic bundle morphism D O(-2) to E. Changing the inverse changes the representative by the internal first image, exactly the quotient used to define E.
2. The quotient first kernel is reflexive on the smooth parameter surface because its image is torsion-free. Its determinant identifies it with O(-5). Radical chain maps descend for the whole pencil, and a nonzero scalar action on the quotient D implies that the internal second kills the shifted kernel O(-6).
3. The map Delta times the quotient D O to E witnesses a nonzero restriction on that kernel. If its generic restriction vanished, the quotient-first kernel would meet the multiplication subspace aA, contradicting generic rank three of the original second symbol. Thus the two-dimensional equivariant Hom space has a one-dimensional naturality kernel.
4. For a rank-one equivariant map into E, saturating the image gives a rank-one reflexive sheaf: the quotient is torsion-free and the depth lemma gives depth two at closed points. Hence the saturation is O(k). The induced linearization has no character ambiguity since A5 is perfect. Source and target force -2 <= k <= 1; the only possible D channel occurs at k=0, but H0(E)^G=0. Thus every nonzero equivariant quadratic map D O(-2) to E has generic rank two.
5. The actual third comparison retains the necessary corrections. Choose the first correction u within S. A second correction v in M projects to a quotient cycle with delta(vbar)=-[T u]. Projection of the third representative T v therefore equals minus the quotient first applied to delta inverse of the internal second. The quotient by the original second image is exactly what makes this independent of the internal correction ambiguity. Changing v contributes original first Bockstein, which is zero.
6. In the reduced block form, the cubic term on D is -q1 delta0^-1 s2. Potential terms involving q2 or delta1 multiply s1 restricted to D, which is zero. There is no missing such correction term.
7. On the common dense open, quotient first rank four and original second rank three make the induced map from E have rank one. Imported original third vanishing puts the image of the internal second in its rank-one kernel. Point 4 forces the internal second to be zero globally. This does not require a false interchange of specialization and kernel formation at the exceptional directions; the internal first has constant rank, and the final bundle morphism is globally zero.

## Verification scope

The finite checker supports the representation arithmetic and synthetic correction identities. It is not proof-assistant verification of the imported geometry or of the entire original proof repair. No actual HM instance or parameter evaluation was used in this review.

Final-byte authentication and checker outcomes are appended below when the author freezes the packet.

## Frozen-byte authentication and execution

Independently ran both `python verify.py` and `python -O verify.py`. Both passed all **58** checks, and their outputs were byte-identical to each other and to `RESULT.json`. The checker was read; it authenticates the three local immutable input copies against their manifest SHA256 and Git blob identities, computes exact A5 character multiplicities, and tests synthetic correction identities and a noncommutative formal cubic expansion. It does not evaluate any actual HM coefficients.

Reviewed final hashes:

- `PROOF.md`: `15c1aaaa1517b06a86f942d9b416f920f87251e95f0ad2ab8e00585199564f24`
- `verify.py`: `3af2682e206120b3b5759d6b2c361c8b023ca44784faba29e9c1d8c3395efebc`
- `INPUTS.json`: `84e1d3327d54592e2a20f87399c09084f2d0a10555f4c46dc6bff1ee58eb6c01`
- `RESULT.json`: `0059c3a4ef9b789fd7e2c2a7d64eefbe03a9c2af2b461215d788b022b72d56b9`

The imported original third theorem is pinned to commit `db51525015bb7c5e825833d550d08dedf6f6ea96`, path `research/hm/order-four-quadratic-load/ACTUAL-THIRD-BOCKSTEIN-VANISHES-IDENTICALLY.md`, Git blob `7c09fe95015d7c8d932b3a27be302ca09888112d`, SHA256 `243e242a15ff2bb678b6c1c3cb33f203bbbed5b8bb0c23d8564e14536d9075cd`.

No mathematical blocker found in the stated conditional theorem. This review is not a formal proof-assistant certificate or a complete repair of the original theorem.
