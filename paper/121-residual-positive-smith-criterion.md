# Surviving residual-large: the exact positive Smith threshold

**PR1103/1104 update:** The earlier 5–31 bound below is sharpened to generic 5–24 and square 5–21, or absence, by [negative quadratic ranks](123-negative-rank-and-smith-bounds.md). When R=0, the [two-dimensional fifth gate](124-original-fifth-gate.md) selects exponent five iff nonzero; its actual value remains unselected. The α≠0/order-ten equivalence is unchanged.

**23 October 2026 · PR1102, local and immutable full proofs read**

[Immutable proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/ef9149e72db4ff501ff969d736660e8aa2aa32bd/research/hm/source2-pure-v-residual-positive-smith/PROOF.md), blob `bf15288e0cbcc78f5ea81eda4af6f577996f88ed`.

## Four equivalent conditions, with α still unselected

Assume specifically residual-large endpoint sixteen. PR1097 gives R=αR1. For the **original positive rectangular map** M_a(t)=Q+tT_a from dimension 41 to 37, over K[[t]] with K=C(P(A)), these are equivalent:

1. α≠0.
2. The original fourth Bockstein on surviving D is generically nonzero.
3. The ideal of maximal 37-minors is (t¹⁰).
4. The Smith exponents are 33 zeros, three twos and one four.

When they hold, the formal kernel is free of rank four and the cokernel is (K[[t]]/(t²))³⊕K[[t]]/(t⁴), of length ten. This gives maximal Laurent-series row rank 37, **not full adjoint invertibility or completion of the original repair**.

The determinant-embedded original-fourth D row has ideal sheaf I_E, where E consists of Z and the reduced twelve-point conic orbit. Its length is 46 and its support has 28 points. The same Smith profile holds over C[[t]] at every direction outside that support. No profile at the 28 exceptional points or conclusion for nonzero-N0/opposite parity is supplied.

## If α vanishes, later pivots remain possible

If α=0, all generic maximal minors are divisible by t¹¹. The last pivot is either absent or has exponent **5≤e≤31**. A later nonzero pivot still gives Laurent-series row rank 37. Therefore **α=0 does not imply row-rank loss**. No value of α or realization of residual-large is selected.

## Why this is a surviving-branch theorem

The proof audits PR1077 but does not import its excluded endpoint-nine line or nonvanishing hypotheses. Instead it uses PR1097's residual-large line constraint and explicitly retains α≠0 as a condition. Independent original-page inputs give rank Q=33, β1=0, generic second rank three, β3=0, and the corrected original-fourth identity iota β4|D=−sL. The universal nonzero-R1 component scheme and determinant ideal transfer apply under their own hypotheses.

Outside E the whole surviving source is D and the target is a line; the determinant embedding is a fiber isomorphism there. Thus nonzero component row means actual fourth rank one, without importing singular-target fiber injectivity or specialized A-kernel conclusions.

Formal elimination removes 33 unit pivots and three t² pivots. In the remaining block the corrected fourth is the Schur term E−CB, not the raw coefficient E. Third vanishing eliminates the preceding term. For α≠0, a t⁴ pivot remains, giving determinantal valuations 0 through size 33, then 2,4,6,10.

For α=0 the last row has order at least five. If nonzero, some original maximal minor is a polynomial of degree at most 37 because the original pencil is linear. Its order is at least 6+e, so e≤31. This degree bound establishes the later-pivot alternative without selecting it. Exact formal checks support the elimination; original-map identification is supplied by the written proof and pinned sources.
