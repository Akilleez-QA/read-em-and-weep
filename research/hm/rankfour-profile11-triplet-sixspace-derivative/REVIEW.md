# Independent whole-proof review

Verdict: PASS for the stated necessary actual-map conclusions, conditional on the retained actual-geometric hypotheses of the three complete immutable inputs. No substantive gap or correction was found in the frozen proof.

## Exact review target

- PROOF.md: 16,248 bytes; SHA256 `16823fcb3c9012c02a23406dcf4656e27441fcb05734551e7d2d4b1756085c67`.
- verify.py: SHA256 `540ee5361001b2a087f43b21efd0a10e56402144eb1432a2e7ea3f4b7d79afd7`.
- characters.py: SHA256 `c19423adfb673352bc313c027c2e115dbf3c7b0f01802e452da2d2524b6eaef7`.

The reviewer read all three complete input texts, INPUTS.json, the entire final proof including its dual-annihilator corollary, and the final checker/helper. This is a review of the geometric argument, not merely acceptance of its arithmetic output.

## Source authentication

REVIEW-SOURCE-AUTH.json records independent fresh read-only GitHub fetches at each exact commit and path. The complete decoded source bytes matched the local inputs byte for byte. Byte lengths, SHA256 values, and Git blob SHA1 values were independently recomputed and matched both INPUTS.json and the GitHub returned blob identifiers. No raw connector-response duplicate is required or included in this review's publication records.

## Geometric checks

1. The actual restriction E0 to F18, together with F18's saturated inclusion in the constant V18* bundle, proves the fiberwise identity G0 = E0 intersect N and the subbundle injection N/G0 into C/E0. The derivative comparison uses only the genuine constant subspace N. It does not impose a connection on F18.
2. Multiplicity-free N = A+V and saturation force G0 to span N. The annihilator sequence gives rank S = 3, degree S = -12, H0(S) = 0 and H1(S) = P+D. The projected first-jet subbundle gives u contained in S^-.
3. The rank-one exclusion is valid for actual coherent maps: the physical scalar quotient forces a >= 2, its transpose forces b <= -4, and the two nonhorizontal kernel stages give degree S^- <= (b-2)+(b-4), hence b >= -2. No saturation of a coherent image is assumed in this contradiction.
4. At rank two, saturation identifies S^- with the actual projected line u. Equivariant splitting, center parity, and the genuine P+D cohomology budget leave exactly the four displayed rank-two quotient types. The negative scalar rows exclude both scalar types; physical W tensor Sym3 W excludes W(-1), leaving W'(-1).
5. The sextic maximal-minor divisor bound, compared with the invariant-divisor minimum twelve, proves everywhere surjectivity onto the actual subbundle (S/u)*(-2). The primal kernel is therefore O(-10), without identification with the dual line u.
6. The constant-intersection subbundle comparison makes this actual W'(-1) image saturated in E0/K = A(4). The resulting quotient is O(14). The quotient diagram gives the actual exact sequence 0 -> K/H -> F18 -> O(14) -> 0, with rank 12 and degree -48 kernel. The proof correctly distinguishes this A(4) from beta_K's A(2) image.
7. The local extension space is one-dimensional. The ambient physical Hom vanishing excludes a split S, and the already proved primal exact sequence supplies a nonzero extension with middle bundle V(-4). Thus the abstract equivariant conclusion S is isomorphic to V(-4) follows, without an actual cross-ambient identification.

## Selected-only replay and scope

REVIEW-REPLAY.json records a fresh temporary-directory replay containing only PROOF.md, verify.py, characters.py, INPUTS.json and the three input texts. Both `python verify.py` and `python -O verify.py` passed 56 explicit checks and reported the exact proof hash above. No LOCAL response files, previous output, or scratch data were copied into that replay.

The checker validates fixed universal representation, source-pin and degree arithmetic; it is not proof-assistant certification of the geometric steps or their transitive imported premises. No selected actual coefficient, point, parameter, jet, tensor, matrix, or instance rank was evaluated, and no broad candidate scan was run. Neither inherited F18 alternative nor any whole branch is excluded or realized by this review.
