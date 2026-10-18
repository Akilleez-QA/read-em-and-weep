# Independent review: simultaneous elliptic CM and literal HM carriers

## Finding
The two negative claims are valid with the bounds below. This review strengthens the preliminary denominator nonassociation check to actual nondivisibility and supplies the matrix-level argument needed to exclude cancellation by constant invertible matrices.

Work over any characteristic-zero field containing i. In the affine chart v0=1, write v_j=e_j(x_1,...,x_4). These four elementary symmetric functions are algebraically independent, so R below is a polynomial ring. The source's descending elementary-symmetric recurrence gives these coordinates with positive signs. Each curve is y_a^2=x_a^3-x_a. The simultaneous map sigma:(x_a,y_a)↦(−x_a,i y_a) preserves the relation and gives sigma*(v_j)=(−1)^j v_j. It is order four on the curve product, order two on the v coordinates. The numerator and chart indices below are zero-based.

## Six-edge obstruction
The literal gamma entries at (row,column) are (0,2):v1, (0,3):v4, (9,3):−v1, (9,0):−v2, (6,0):−v3, (6,2):−v4. For the weighted action v_j↦lambda^j v_j, an equality gamma(lambda·v)=A gamma(v) B with diagonal invertible constant A,B forces the edge multipliers to factor as a_r b_c. Alternating around this cycle gives lambda^(1−4+1−2+3−4)=lambda^(−5)=1. Thus lambda=−1 is impossible. Literal minus signs cancel in the entrywise ratios. This is a necessary condition only; lambda^5=1 is not asserted sufficient. This subsection alone excludes diagonal intertwiners. The independently verified stronger addendum below excludes arbitrary constant gamma intertwiners as well; changes of monad presentation remain outside this claim.

## Prime divisor and genuine transformed pole
Let R=k[v1,v2,v3,v4], q=v1v2v3v4, D=v2v3v4+v1^4. As a polynomial in v4 over k[v1,v2,v3], D has relatively prime coefficients v2v3 and v1^4. It is primitive and linear over the fraction field, hence irreducible by Gauss's lemma; the UFD R makes (D) prime. None of v1,v2,v3 is in (D).

Carrier 1's I[5][1] is −(v1^3+v1v2^2v3)/(q−v1^5). After sigma it is (v1^3−v1v2^2v3)/(q+v1^5)=(v1^2−v2^2v3)/D. The transformed numerator is nonzero and independent of v4, so D does not divide it. Therefore the entry has valuation −1 at the height-one prime (D), and the whole transformed matrix is nonregular there.

For formal Laurent monomial reduction modulo symbolic D (not a sample evaluation or numeric residue), localize at v2v3 and use v4=−v1^4/(v2v3). This embeds R/(D) into k[v1,v2^(±1),v3^(±1)]; injectivity follows from primality and v2v3∉(D). The six stored I denominators have the following nonzero images:

- q−1 ↦ −v1^5−1
- q−v1^5 ↦ −2v1^5
- q−v2^5 ↦ −v1^5−v2^5
- q−v3^5 ↦ −v1^5−v3^5
- q−v4^5 ↦ −v1^5+v1^20 v2^(−5)v3^(−5)
- −v1^2v3v4 ↦ v1^6 v2^(−1)

Distinct exponent labels, or the nonzero coefficient −2, certify every image. Thus no stored denominator has D as a factor. Every entry of every original I carrier is regular at (D). The stored dp and dh denominator lists agree with di. Powers of these denominators remain units at (D), as do every v_j coordinate factor (D cannot divide a coordinate); this covers additional coordinate inverses in W/eta, without extending the I-family claim to unevaluated composite sources. Nonassociation of entire denominators by itself would not establish this claim.

## Why constant row/column mixing cannot cure the pole
If constant A∈GL15(k) and B∈GL2(k) made A sigma*(I_1) B regular at (D), multiplying back by the constant inverses would make sigma*(I_1) regular, contradicting the witness. Equivalently, its nonzero leading polar coefficient cannot become zero under an invertible linear map. This is a matrix regularity argument, not an assumption that individual entries cannot cancel. Since every I_b is regular there, no equality A sigma*(I_1) B=I_b holds for any of the six b. In particular there is no permutation of all six literal carriers together with constant invertible row/column intertwiners, even allowing separate constants for each carrier.

The obstruction survives passage from symmetric coordinates to the actual curve function field: k(v1,...,v4) embeds in k(x1,...,x4), which is finite over it, and adjoining the y_a is algebraic. A valuation over (D) exists in a field extension; an element with negative base valuation remains negative (scaled by positive ramification), while every original matrix entry remains nonnegative. This uses formal algebraic independence of elementary symmetric functions, not a numerical specialization or a physical source evaluation.

## Limits and relation to earlier work
The pole argument concerns exactly the stored rational I-carrier family and constant invertible matrices. By itself it says nothing about non-diagonal intertwiners of gamma alone; the separate full-rank addendum excludes all constant gamma intertwiners. Neither argument rules out coordinate-dependent gauge matrices, refined covers, another rational presentation, or an actual bundle isomorphism sigma*E≅E. A rational equality on any nonempty overlap would still be a function-field equality and is excluded for these constant carrier formulas; removing D from that overlap does not create such an equality. A genuine geometric equivariance question needs independent sheaf/monad data.

The reviewed post-spike-symmetry notes concern second-jet cross-Gram symmetry, trace/curvature descent and scalar remainders. Searches of their text and nearby proof files found no existing CM literal-carrier argument. This is a different negative test and gives no residual/ID0 evaluation, vanishing, or global-boundary result.

## Evidence and controls
The portable inputs bind the entire model by SHA256 and contain only selected source excerpts and literal records. The reviewer read source as inert text, did not import production code, and did not construct/evaluate actual source objects, jets, matrix polynomials, or polynomial products. The verifier checks hashes, literal support, degree/parity labels and signed exponent-lattice normal forms only. Its finite checks support the displayed algebraic proof; they do not replace the prime-divisor and valuation arguments.

## Independently verified stronger addendum and weights

An independently assembled coefficient system and integer fraction-free elimination give rank 250 in 250 unknowns for M gamma = gamma(Sv) N. Thus only the zero constant pair exists, over every characteristic-zero extension. As a positive control, the identity coordinate action has rank 249 and its equations annihilate (I15,I5). This strengthens the diagonal-only gamma obstruction, while preserving every bundle/rational-gauge caveat above. See check_constant_independent.py.

The 30 retained metadata requests have unique total-degree parity per request; odd IDs are exactly 21,24,26,28. The resulting 26 even / 4 odd split classifies polynomial weights only. It supplies no detector character or vanishing test. The equivalent derivative identities sigma V sigma^−1=−i V and V sigma=i sigma V are consistent, as is the four-derivative factor 1.
