# Independent review: collective radical images and the top obstruction

## Verdict and actual scope

No mathematical blocker found. The stated conclusions are conditional on an actual source126 Type II occurrence and compatibility of the entire radical with Q. Under those hypotheses the collective images are exactly I2=P+2D and I4=P+D, the generic original pencil has rank exactly 36, all later original generic Bocksteins after the second vanish, and the internal cubic gate is zero. This neither proves that the hypotheses occur nor excludes a source pair, and it does not establish all later internal-symbol vanishings or compute exceptional-direction extra kernels.

## Image computation independently checked

The proof does not equate a common annihilator with a collective image. The distinction is essential.

- Since J kills F2 and maps into F2, the residual source P+2D permits only P and D image types. The actual F2 multiplicities bound their image multiplicities by two each.
- The residual P cannot be killed by all J, because Ann_J N2 is exactly F2. Therefore the P collective image is nonzero. Q is injective on the full P-isotypical source and carries the P image into the single P in F4. This forces its multiplicity to be one.
- The collective D image at N4 is nonzero by the retained actual geometric result. This is not inferred merely from an annihilator dimension.
- The actual D summand of ker Q lies in I2: a nonzero induced radical map from H0(T)=D to H0(S)=A+D is onto that kernel D. Such a nonzero map must exist, since otherwise every lift of a quotient cycle would be killed by all J, hence belong to U and represent zero. There are no degree-minus-one boundaries to weaken this conclusion.
- Surjectivity of Q on the entire target D isotypical part and Q/J commutation give the equality of actual subspaces I4_D=Q(I2_D). The kernel of this restricted Q is exactly its full D kernel, already shown to lie in I2_D. Thus target multiplicity w equals source multiplicity v minus one. With w at least one and v at most two, v=2 and w=1 follow.

These arguments establish the image dimensions 14 and 9 independently of any synthetic model.

## Consequences checked

1. Every J-linear map preserves the collective images and induces a map on quotients of dimensions 27 and 28. Surjectivity upstairs would imply surjectivity downstairs, impossible. Cokernel dimension is at least one, giving rank at most 36. This remains valid without G-equivariance and after every field extension, so it applies to the actual entire negative pencil under the full-J hypothesis.
2. The retained rank33 at Q and generic second-symbol rank3 supply rank at least36 over the generic Laurent-series field. Therefore rank is exactly36, with kernel dimension5 and cokernel dimension1.
3. After cancellation of the33 unit pairs, original first vanishing makes the4-by-8 remainder divisible by t^2. Three rank-three leading pivots have valuation exactly two. The remaining1-by-5 formal block must be identically zero, because any nonzero entry raises Laurent rank to37. This proves the Smith data and all later original generic differential vanishings, not merely fourth vanishing.
4. Independently, nonzero internal cubic r would be generically onto the rank-two bundle E by PR982. Along with the rank-three internal first and vanishing internal second, this makes S surjective over the generic Laurent field. The quotient T is likewise surjective from its rank-four first symbol. Exactness then makes M surjective, contradicting the top obstruction. Hence r=0 globally.
5. Rank(S) at most23 on the generic quotient-surjective locus is consistent. It does not imply every later internal differential vanishes. The proof expressly keeps that distinction from the all-orders original result.

## Exact execution and final bytes

Read the final proof, the checker, and the directly pinned original-third theorem's lower-order statements. Independently ran normal and optimized Python on the final six-input packet. Both passed all45 checks with identical stdout. The checker authenticates local immutable input copies by SHA256 and Git blob identities, enumerates permitted image multiplicities, and verifies a synthetic constituentwise Q/J diagram, including square-zero products, common kernels, collective images, and the actual type of D-image equality. That model is explicitly not an actual HM occurrence and is not being used in place of the preceding mathematical arguments.

Final reviewed hashes:

- PROOF.md: `f5982f08c7637f61ee3b27883f5eccb9655a81d501d84fc7014349acc7b9604f`
- verify.py: `771dbc284441c645dc2e99a05280e4c367f86fc9f97c857b5f45168d8622fc63`
- INPUTS.json: `88484b4bb3606ad186ce88738f069149709182ec89b958e5bdb76186df5b7542`
- RESULT.json: `4efe97d32de6bac17cdaf2c9ddf99da46f22d49725f166beb1d12781d9d441de`

No actual HM instance, chosen parameter, or actual map rank was evaluated. This is an independent mathematical review with reproducible finite checks, not proof-assistant certification or completion of the original repair.
