# Independent whole-proof review

## Verdict and exact object reviewed

PASS, conditional on the complete actual-geometric source theorems stated in the proof. No correction to the written deduction is required.

The reviewed `PROOF.md` has SHA256

    c3d21cb63ffac4c69247e8deba8ef352f673ac3a7b2f91507bc54fbecae943af

The conclusion is exactly that an actual rank-four maximal plateau of ordered profile `(1,1)` must have `maxdeg(A_q)>=3`. This is not a closure of that profile or a new global rank bound. In particular it neither asserts that a surviving quotient exists nor transfers source data from a historical rank-three ledger.

I read the complete written proof, checked its actual bundle and source conventions against the retained originals, and independently derived its finite representation and degree statements. The companion `verify_independent.py` imports neither the author's verifier nor the reference character script. It constructs the physical irreducible characters using the nine conjugacy classes, the Galois conjugate standard representation, and the closed binomial formula for symmetric-power traces. Its assertions are explicit exceptions and remain active under `python -O`. Both normal and optimized runs passed.

All eight retained originals independently match their manifest byte lengths, SHA256 values and Git blob IDs. This authenticates the retained copies against the manifest; it is not a fresh network authentication or a proof of their geometric premises.

## Actual endpoint argument

The successive negative Gauss kernels remain saturated in the same original constant ambient bundle. Their negative top degrees preclude a nonzero horizontal terminal kernel. The coherent quotient injections into `C(-2j)` are sufficient for the exterior-degree bounds; saturated image in the target is not required.

Nonincreasing endpoint ranks at most three give the three ordered height columns with total 13 or 9. Balancing the nonnegative integral columns gives minimum quadratic costs 70 and 36. The displayed inequalities

    a+13u >= 16,     b >= 9v,     a+9v <= -8-t

have the correct signs and retain the original determinant defect. They force `v<=-1`. With four ordinary degrees, `u=1` then gives `a<=2`, contradicting `a+13u>=16`; hence `u>=2`. No stronger dual top bound than `top(S)<=-1` has been imported.

## Exhaustiveness of the low-top reduction

Under `u<=2`, the preceding argument forces `u=2`. The genuine quotient of the globally generated bundle `E(8)` supplies the lower bound `-8` on every ordinary quotient degree. Center parity restricts the central character of each coefficient representation exactly as used in the proof: the coefficient representation has central sign `(-1)^e` at degree `e`. This is central character, not dimension parity.

A four-dimensional irreducible coefficient block fills the entire rank-four quotient and gives only one ordinary degree, contrary to the proved mixed-sign requirement. The remaining proper irreducible blocks have dimensions one, two or three. Direct class-character computation over the prescribed degree interval gives exactly three mechanisms containing `W'` in twist three:

    W' O(-3),     V O,     A_std O(2).

For clarity, this computation includes both odd doublets at degrees `-3,-1,1`, both even three-spaces at degrees `-2,0,2`, and the scalar blocks at the allowed even degrees. Lower degrees have no sections. In particular no omitted proper coefficient block supplies `W'`.

The remaining rank budget and the two required `T6` copies imply exactly the cases asserted:

- After `W' O(-3)`, a remaining doublet contributes at most one `T6`, while a scalar contributes one only at degree two. Thus the remaining rank two is `2O(2)`.
- After `V O`, the remaining scalar must be `O(2)`, contradicting the negative minimum degree.
- After `A_std O(2)`, the remaining scalar has even degree in `{-8,-6,-4,-2}`.

For all four actual source types, the scalar Hom spaces at degrees `-6,-4,-2` vanish. The Hom at degree `-8` has dimension one only for source D, coming solely from its displayed `O(-8)` block. This proves the actual-source forcing in the third case, not merely formal compatibility of a separately selected source.

Consequently the two written shapes exhaust the degree-bounded sublocus by a symbolic rank-and-character argument. No broad quotient or splitting search is used.

## First shape

For `W' O(-3)+2O(2)`, the quotient degree is `-2` and the kernel degree is `-52`. The top-three expression is

    13-5z-h1^2-h2^2-z^2,

with `h1+h2=13-z`. Its real upper bound is

    -365/6 - (3/2)(z-8/3)^2.

The integral capacity is therefore at most `-61`, and heights `(5,5,3)` attain that value. This contradicts degree `-52`. The independent verifier checks the polynomial identity and the attaining height, without enumerating quotient candidates.

## Second shape and the delicate actual Euler-kernel step

For `A_std O(2)+O(-8)`, the actual projection onto `O(-8)` receives no contribution from `E'`. Surjectivity forces a nonzero scalar on the source `O(-8)` block. Hence the actual kernel lies in `E'` and its quotient there is exactly `A_std O(2)`. A possible upper-right component from source `O(-8)` to the positive target does not alter this kernel or the resulting exact sequence. No connection splitting is used.

If `H0(K(3))=S4`, its evaluation is an actual `S4 O(-3)` top subbundle because `top(K)<=-3`. All components into the non-D source blocks vanish by degree or irreducible inequivalence. The sole nonzero component into `D O(-2)` belongs to the one-dimensional Hom space corresponding to

    D tensor W = S4+T6.

The canonical equivariant evaluation sequence has precisely this nonzero map as its kernel inclusion:

    0 -> S4 O(-3) -> D O(-2) -> O(2) -> 0.

Therefore the actual D-row factors through `O(2)`. Its equivariant Hom into `A_std O(2)+O(-8)` is zero: the degree-zero coefficient would have to be an invariant in `A_std`, and the other component has negative degree. This forces the D-row to vanish, contradicting `H0(K(2))=0`. The argument is valid on sheaves, not merely on a generic fiber.

Thus `H0(K(3))=0`. Rank 13, degree `-52`, and top degree at most `-4` force every kernel degree to be `-4`. The exact twisted sequence then gives

    K = (A_std+2V+P) O(-4).

I independently obtain this identity by class characters. In particular

    chi(E'(4)) = A_std+3V+3P+2D,
    chi(A_std O(6)) = V+2P+2D.

Finally, the actual derivative of K lands in `A_q(-2)`. The `O(-10)` component vanishes by ordinary degree. Strict top for K makes the induced map on its fourth-twist sections injective into

    A_std tensor Sym4 W = A_std+V+P+D.

The source has two V copies and the target only one. This contradiction is coefficient-space injectivity, not an unsupported fiber-rank assertion or a horizontal Birkhoff decomposition.

## Scope and remaining work

The proof is mathematically coherent under its explicitly retained premises. The independent checks are limited to universal representation, Hom, degree and capacity identities; they do not certify the underlying HM source theorems or execute an actual coefficient, point, jet, tensor, matrix, instance-rank test or scan.

The rank-four `(1,1)` locus with larger top degree remains open. Other ordered plateau lanes are untouched.
