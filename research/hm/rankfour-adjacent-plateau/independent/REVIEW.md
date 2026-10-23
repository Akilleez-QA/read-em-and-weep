# Independent review: the actual rank-four maximal plateau (2,3)

## Verdict and scope

**PASS, conditional on the retained actual geometric inputs.** The new proof excludes the ordered maximal generic-rank-four plateau `(k,l)=(2,3)`. Its exact Euler-character obstruction is sound. It does not exclude other rank-four profiles, establish generic rank at least five, establish square-map surjectivity, or complete the original problem.

The reviewed final proof does not depend on the preceding `(3,3)` exclusion, its slope window, the abandoned 50/8/2 quotient enumeration, or the classification of the exceptional source splitting. In particular the only source character needed is the direct actual identity `chi_G(E(2))=-V`.

This review contains no actual selected coefficients, parameters, jets, matrices, instance ranks, local-model experiments, historical enumeration, or external writes. The executable checks use universal integer identities, very small abstract deficit partitions, and exact finite-group characters.

## 1. Inputs read and authenticated

The complete original notes read for this review are:

1. `ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md`, at repository commit `db51525015bb7c5e825833d550d08dedf6f6ea96`, SHA-256 `a52685fc9e7c89abf26171a15989cedeaf3bd101a2edde790a24f9cfe0179256`.
2. `GAUSS-DETERMINANT-ORBIT-RAMIFICATION.md`, at the same repository commit, SHA-256 `783454715e967929ad81e6f09f8f4a155073fbdab89974bee056416e4f866e71`.

The first note is the sole retained source dependency: it supplies the actual presentation, fixed physical marking, and rank-independent Gauss-persistence argument. The second was read only to cross-check saturation and determinant conventions; its rank-two endpoint conclusions and invariant-divisor gap are not imported or included in this package.

The author's complete final `PROOF.md` is retained under `author/`, together with the exact verifier and output replayed in this review. `MANIFEST.json` binds the reviewed bytes. Hash authentication does not independently prove the imported actual geometry or all transitive source claims.

## 2. Saturation and both endpoint persistence bounds

For the hypothetical profile, write

    F0 < F1 < F2=E < F3 < F4 < F5,
    rank Fi = 9+4i.

The actual saturated stages satisfy the interior kernel and forward-transform equalities. Consequently every stage before F5 has no nonzero constant subbundle, while every stage after F0 has full constant span. The reversed annihilator sequence has the corresponding properties.

The persistence proof is valid even at F0. Since F0 is the sheaf derivative kernel at F1, differentiation of a local section of F0 lands in F1. Thus the first forward containment does not require the derivative rank at F0 to equal four. The subsequent containments use the actual interior transforms. The identical argument holds at the lower endpoint of the reversed annihilator sequence.

A nonzero section at twist d saturates to O(-e), with e at most d. Its image is also saturated in the constant ambient: both the inner and outer quotients are locally free. The universal derivative-to-coefficient triangular identity reaches the line's constant span in at most e steps. Saturation extends the generic containment across all parameters. This proves H0(Fi(d))=0 for i+d<5 and its dual counterpart. It uses no equivariant choice of section and no horizontal splitting.

Accordingly the ordinary top degree of F0 is at most -5. Its rank is nine, so a=deg F0 is at most -45. The annihilator F5-perp has rank one and degree b=deg F5 at most -5.

The stage determinants are center-even. Every equivariant line bundle is the standard O(d) linearization up to a one-dimensional character, and the perfect group has no nontrivial such character. Hence stage degrees are even. This sharpens the endpoint bounds to

    a <= -46,    b <= -6.

This parity step is essential; the weaker bounds -45 and -5 do not force equality below. No endpoint rank-one theorem or invariant-orbit ramification gap is required.

## 3. Exact determinant identity and graded isomorphism

Let Li=Fi/F(i-1), ci=deg Li. The induced regular derivative maps

    Li -> L(i+1)(-2)

are between locally free rank-four bundles and are generically invertible. Their cokernels are torsion of nonnegative length delta_i, so

    c(i+1) = ci+8+delta_i.

Direct elimination of c1 from deg E=-54 gives

    3a+2b = -150 + 3delta1+6delta2+4delta3+2delta4.

The endpoint upper bound equals -150. All defect weights are strictly positive, so a=-46, b=-6, and all four defects vanish. This forces

    quotient degrees: -8, 0, 8, 16, 24;
    stage degrees: -46, -54, -54, -46, -30, -6.

A generically invertible map of bundles with zero torsion-cokernel length is an everywhere isomorphism. Thus with B=L2=E/F1, one has L1=B(-2). Only an associated-graded identification is used. Neither exact sequence below is asserted to split, and no torsion quotient has silently been discarded.

## 4. Exhaustive low-stage tails and physical parity

Persistence bounds the degrees of F0 by -5 and those of F1 by -4. Their total deficits are respectively one and two. These are complete ordinary splitting classifications at those deficits, not computational cutoffs.

Equivariant splitting and central parity therefore give

    F0 = R8 O(-5) + O(-6),

with R8 an arbitrary genuine odd representation of dimension eight, and exactly three possibilities for F1:

    R11 O(-4) + W O(-5),
    R11 O(-4) + W' O(-5),
    R12 O(-4) + O(-6).

R11 and R12 are arbitrary genuine even representations of the indicated dimension. At degree -5 the coefficient has dimension two and odd parity, forcing W or W'; at degree -6 the coefficient line is trivial. There is no overlooked reducible odd two-space, since the only one-dimensional representation is even.

## 5. Exact sequences and all H1 corrections

The relevant actual short exact sequences are

    0 -> F0(4) -> F1(4) -> B(2) -> 0,
    0 -> F1(2) -> E(2)  -> B(2) -> 0.

For each, the full long exact sequence is

    0 -> H0(left) -> H0(middle) -> H0(right)
      -> H1(left) -> H1(middle) -> H1(right) -> 0.

The last zero uses that the base is P1. Taking alternating characters is valid without any assumption that the map on sections is onto. Eliminating the same B(2) gives

    chi F1(4) + chi F1(2) = chi F0(4) + chi E(2) = -1-V.

For F0(4), the R8 O(-1) term is acyclic while O(-2) contributes -1. The source identity chi E(2)=-V is obtained directly from the actual presentation, not from a quotient-shape search.

For either doublet tail X=W or W', the left side is

    R11 + (-R11-X tensor W) = -X tensor W.

For the line tail, it is

    (R12-1)+(-R12-A) = -1-A.

Thus all H1 terms, including the trivial correction at twist four for the O(-6) tail, are present. There is no surviving unknown coefficient representation.

The fixed physical products are W tensor W=1+A and W tensor W'=P. The three discrepancies, left minus right, are consequently

    V-A,    1+V-P,    V-A.

All are nonzero in the representation ring. In particular A and V are physically distinct irreducible three-spaces; equality of their dimensions cannot replace equality of characters. Each discrepancy has dimension zero, confirming that the contradiction is genuinely equivariant.

## 6. Independent controls and reproducibility

Run:

    python3 verify.py
    python3 -O verify.py
    python3 test_controls.py

The first two outputs must equal `RESULT.json`. The independent verifier does not import the author's verifier. It reconstructs exact class characters in Q(sqrt(5)), checks all nine irreducibles' orthogonality, dimensions and central signs, derives chi E(2) directly from the presentation, checks the endpoint identity symbolically, checks the complete tiny deficit partitions, and computes the three contradictions with all cohomology corrections.

There is no McKay-graph input to the independent character computation. The checker is an arithmetic validation of the displayed universal consequences, not a machine proof of actual saturation, the source presentations, or the universal geometric persistence lemma.

The negative-control runner changes one essential ingredient at a time and requires nonzero exit: source bytes, endpoint parity, defect weights, quotient twist, physical marking, and the line-tail H1 correction. It also replays the unchanged package successfully under ordinary and optimized Python.

