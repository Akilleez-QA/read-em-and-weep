# Independent review: approved within the stated scope

Reviewed proof SHA256:

`59756d7dac77cfe0f91c323e9d9bf88ef1b4947923beac0f5af5c50ed360099b`

Other reviewed artifact SHA256 values:

- INPUTS.json: `dfb44d7c9e3858639418178720c3a06de8488979f1b977173cc59c3bc04566c4`
- verify.py: `daad4c4c23f6a2294e2f29615e685b200814e9cf6072386d59c5ad0ac6a09374`
- REPRODUCE.md: `8e24980a32bfea6b2209ece32a306914bc1623998a4055eb0e378768e09bb67d`

## Evidence and reproducibility

The reviewer read the entire final proof and all four exact local originals: QUOTIENT, SQUARE, SECOND, and BALANCED. Their byte counts, SHA256 digests, and Git-blob identities agree with INPUTS.json. Both `python verify.py` and `python -O verify.py` pass on the final artifact set. The verifier uses explicit exceptions rather than optimization-sensitive assertions.

The executable checks authenticate the input bytes and perform fixed abstract character, dimension, and degree arithmetic. They do not replace the mathematical arguments below and do not determine an actual secondary coefficient. The review takes the stated actual-geometry results in the pinned originals as inputs; it is not a new audit of every dependency of those originals.

## Mathematical findings

1. Actual source and target are retained. QUOTIENT identifies the actual reduced source and its unique equivariant complement, rather than merely a bundle of the same splitting type. SECOND retains the actual quartic-neighborhood boundary, and SQUARE supplies its factorization through Q6. The target representation follows from SQUARE's actual endomorphism cohomology and equivariant trace/Serre duality. Perfection of G removes a possible determinant character. Thus the six scalar channels belong to the actual map, although their values remain unselected.

2. The base-divisor argument is valid. A finite projective point stabilizer is cyclic; in A5 it has order at most five. Hence every orbit on T has at least twelve points. A common-zero divisor for D8 would be an invariant effective divisor of degree at most eight, which is impossible. The degree-eight evaluation sequence is therefore everywhere exact with locally free kernel of rank four and degree minus eight.

3. The syzygy exclusion is sound. Binary Koszul exactness embeds the multiplication kernel into Sym7 W, while it is already a subrepresentation of D tensor W. Semisimplicity and the displayed decompositions make a nonzero kernel a copy of the six-dimensional T6. Projection of a binary relation to either chosen abstract coefficient is injective, so the kernel has dimension at most five. Consequently H0(M(1))=0. Birkhoff–Grothendieck then forces M=U O(-2); evaluation of its global sections makes this equivariant, and the degree-two exact sequence identifies U=P. This proves the everywhere-injective P channel, including its standard linearization.

4. The W channel is correctly identified. Euler evaluation has kernel det(W) O(-2)=O(-2), and the quartic Veronese section is nowhere zero. Their composite spans the unique equivariant Hom space. The named maps and identifications are canonical only up to the nonzero scalars explicitly allowed in the statement.

5. Nonvanishing of qv is genuinely proved, not inferred from a one-dimensional invariant space. Polarization followed by multiplication is a nonzero scalar on Sym12 W. The polarized invariant must lie in the unique invariant line in D8 tensor D; multiplication on that line is therefore nonzero. The same line defines qv. Its invariant degree-twelve divisor is one reduced twelve-point orbit. The perfect-group observation also justifies uniqueness among orbit divisors, not merely among invariant sections already chosen.

6. The row kernels and determinantal scheme are correct. After quotienting by the P subbundle, the remaining map is f12 times Euler evaluation. Multiplication by a nonzero section is injective as a sheaf, so the row kernel is exactly the Euler line, with zero P-source component. Its cokernel is O(12) restricted to Omega. Locally the P block becomes an identity and the remaining entries generate (f12), because Euler evaluation is onto. Thus the five-by-five minor ideal is the reduced ideal of Omega, with fiber rank exactly four there and five elsewhere. The proof properly distinguishes this fiber statement from the rank-one kernel sheaf.

7. The conditional reduced-map criterion is valid. A nonzero W-to-V or W-to-P channel cannot vanish on the Euler line, since equivariant descent would yield a forbidden O-to-J O(4) map. The resulting nonzero line-to-vector map is sheaf-injective. Conversely, if both channels vanish, every target row kills the Euler line, including the forbidden A row. The degree-six base-divisor exclusion makes a nonzero restriction nowhere zero. Accordingly, when at least one such channel is present, the full reduced map has fiber rank six off Omega; only its behavior on Omega remains undecided.

8. The original-kernel corollary is valid. The preimage of the Euler kernel gives the exact equivariant extension by A O(-6). BALANCED implies Hom_G(O(-2),K)=0, excluding a split extension. Equivariant Ext is the invariant part of ordinary Ext in characteristic zero and has dimension one here. The twisted cubic evaluation sequence gives a nonzero class with middle bundle S O(-5), so all nonzero classes have that equivariant isomorphism type. If a nonzero V/P channel instead kills the reduced kernel, the original kernel is precisely the square subbundle A O(-6).

## Scope and verdict

Approved for the exact bytes bound above. No unresolved mathematical defect was found in the new argument. The assertions are conditional on the pinned actual-geometric inputs and, for Sections 5–6, on both D-row coefficients being nonzero. Neither their nonvanishing nor any other actual coefficient case is selected. Original beta is never claimed injective: it always retains the square subbundle. No global odd-quadric section, full exceptional-fiber rank, top sigma, vertex delta, or source/frontier conclusion is obtained.

The review used local source reading, universal bundle and representation arguments, and the small fixed-character verifier only. It performed no selected actual HM/source evaluation, coefficient selection, point or parameter test, instance matrix/rank calculation, or large computation.
