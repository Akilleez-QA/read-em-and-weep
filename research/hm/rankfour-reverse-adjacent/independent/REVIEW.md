# Independent review: ordered rank-four maximal plateau (3,2)

## Verdict and limits

**PASS, conditional on the retained actual geometric inputs.** The endpoint-degree argument, exact associated-graded K-class identity, intrinsic endpoint enumeration, and final equivariant persistence obstruction exclude the ordered maximal generic-rank-four plateau `(k,l)=(3,2)`.

This does not exclude any other rank-four profile, prove generic rank at least five, prove square-map surjectivity, or complete the original theorem. No exceptional source splitting is assumed. The actual rank-17 bundle E and rank-13 annihilator Q* remain distinct throughout. No actual coefficients, selected parameters, jets, maps, matrices, instance ranks, local experiments, historical candidate enumeration, or external writes enter this review.

## 1. Complete sources and retained assumptions

I read the four complete originals retained in `inputs/` and authenticated by `INPUTS.json`, all pinned at repository commit `db51525015bb7c5e825833d550d08dedf6f6ea96`:

1. `ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md`: actual presentations, equivariant splitting, and the rank-independent persistence argument.
2. `RANK-TWO-GAUSS-PLATEAU-NECESSARY-BOUND.md`: actual ambient character, rank-independent saturation/derivative facts, and determinant parity; no rank-two conclusion is imported.
3. `GAUSS-DETERMINANT-ORBIT-RAMIFICATION.md`: only the projective orbit-size and invariant-divisor fact; no rank-one endpoint theorem or rank-two exclusion is imported.
4. `POSITIVE-DOUBLE-HYPERPLANE-GAUSS-GATE.md`: actual constant-ambient inclusion and its geometric SF identification; no surjectivity assertion is imported.

The conditional input is the actual saturated equivariant inclusion

    0 -> E -> H O -> Q -> 0,
    rank E=17, deg E=-54, dim H=30,
    H=2A+2V+2P+2D,

on the original physical line T=P(W*). The actual presentations are

    [E]=[M3 O(-1)]-[M4 O],
    [Q*]=[M3 O(-1)]-[M2 O],
    M3=3W'+3S4+6T6,
    M4=2V+4P+3D,
    M2=A+2V+3P+4D.

All named irreducibles are self-dual. The physical marking is A=Sym2 W, S4=Sym3 W, D=Sym4 W, T6=Sym5 W, with V the inequivalent even three-space. The center-odd irreducibles are W, S4, T6, W'. In particular

    chi E(2)=-V,
    chi Q*(3)=T6-2W-S4.

The independent checker derives these from the presentations, and also checks the duality consistency chi Q(t)=-chi Q*(-t-2), where Q=H O-E. Authentication establishes source bytes, not their truth or all transitive geometric prerequisites.

## 2. Ordered geometry and endpoint persistence

For the hypothetical profile, use the saturated chain

    F0 < F1 < F2 < F3=E < F4 < F5,
    rank Fi=5+4i.

For each interior stage the derivative kernel is its predecessor and its saturated forward transform is its successor. Every Fi for i<5 has no nonzero constant subbundle; every Fi for i>0 spans H. These statements propagate respectively backward through kernels and forward through transforms to the corresponding nondegeneracy of E.

Put Di=F(5-i)^perp. Then D2=Q*, not E; both endpoint ranks are five. The reversed annihilator chain has the same interior properties.

For i+d<5 and d>=0, the universal persistence argument gives

    H0(Fi(d))=H0(Di(d))=0.

The endpoint i=0 is valid: F0 being the kernel at F1 implies dF0 is contained in F1 tensor Omega, so a saturated line in F0 starts its forward transforms inside the same chain. A degree-e polynomial line reaches its constant coefficient span in at most e steps by the universal triangular derivative identity. If e<=d and i+d<5, this would place a nonzero constant subbundle in an interior stage. Saturation extends the containments across all parameters. No endpoint SF rank assumption or chosen section evaluation is used.

Thus every ordinary endpoint degree is at most -5. The determinants of all stages have even degree, since the ambient is center-even and the perfect group has no nontrivial one-dimensional character. For

    a=deg F0, b=deg F5=deg D0,

the rank-five bounds sharpen to a,b<=-26.

## 3. Intrinsic endpoint alternatives and zero defects

Let Li=Fi/F(i-1) and ci=deg Li. The regular rank-four derivative maps Li -> L(i+1)(-2) have effective determinant defects delta_i, so

    c(i+1)=ci+8+delta_i.

The divisor of a determinant map is invariant under the projective A5 action. The only orbit sizes are 12,20,30,60, so a nonzero defect is at least 12. The actual rank-four identity obtained by eliminating c1 is

    2a+3b = -150 + 2delta1+4delta2+6delta3+3delta4.

Writing a=-26-2u, b=-26-2v gives

    4u+6v+2delta1+4delta2+6delta3+3delta4=20.

The least possible nonzero weighted defect costs 2*12=24>20, so every delta is zero. The complete nonnegative integer solutions of 2u+3v=10 are (u,v)=(5,0),(2,2). Therefore:

    Case I:  (a,b)=(-36,-26), ci=(-14,-6,2,10,18).
    Case II: (a,b)=(-30,-30), ci=(-16,-8,0,8,16).

All four derivatives are now equivariant bundle isomorphisms. Put B=L3, so

    (L1,L2,L3,L4,L5)=(B(-4),B(-2),B,B(2),B(4)).

This is only an associated-graded statement. No filtered or horizontal splitting is asserted.

## 4. Exact K-class identity and independent dual-twist check

The lower three quotient sequences give

    [E]-[F0]=[B(-4)]+[B(-2)]+[B].

The upper two quotient sequences and the exact endpoint quotient H O/F5=D0* give

    [Q]-[D0*]=[B(2)]+[B(4)].

Twisting the second identity by -6 and subtracting yields the exact identity

    [B]=[E]-[F0]-[Q(-6)]+[D0*(-6)].

The final plus sign, use of Q rather than Q*, dual on D0, and twist -6 are all necessary. This identity is derived from actual exact sequences, not inferred from agreement at two Euler twists.

Every actual pair of endpoint bundles must then satisfy the necessary equalities

    chi B(t+2)+chi B(t+4)+chi D0*(t)=chi Q(t), t=0,1.

The argument uses these only to construct an overlist of endpoint pairs. No claim that two Euler evaluations characterize equivariant K0 or imply realization is needed.

For the final tests, the exact sequence 0->F2->E->B->0 and H0(F2(2))=0 force

    -chi F2(2)=chi B(2)-chi E(2) >= 0

coefficientwise in the irreducible representation basis.

Independently, D1=F4^perp and D2=F3^perp=Q*, so

    D2/D1=(F4/F3)*=L4*=B*(-2).

Twisting by 3 gives chi D1(3)=chi Q*(3)-chi B*(1). Equivariant Serre duality on the determinant-one physical line gives chi B*(1)=-chi B(-3). Since H0(D1(3))=0,

    -chi D1(3)=-chi B(-3)-chi Q*(3) >= 0.

The exponent -3 is correct. In both persistence uses i+d=4<5. Neither test assumes H1=0; in fact the displayed nonnegative characters equal the relevant H1 representations.

## 5. Complete intrinsic degree and parity domains

An endpoint is a rank-five center-even bundle of total degree d, all ordinary degrees at most -5. The other four ordinary degrees therefore force every degree e to satisfy

    d+20 <= e <= -5.

The domains are consequently:

    d=-36: -16<=e<=-5;
    d=-30: -10<=e<=-5;
    d=-26:  -6<=e<=-5.

At each e the coefficient is a genuine sum of irreducibles with central parity e mod2. Only irreducibles of dimension at most five may occur: 1,W,A,S4,D,P,W',V. T6 cannot occur in a rank-five endpoint. The sum of coefficient dimensions is five, and the dimension-weighted degree sum is d. These conditions give a complete finite domain, not an empirical cutoff or a quotient-slope hypothesis.

The independent enumeration first partitions the five ordinary degree deficits from -5. Their sums are respectively 11,5,1. For each repeated degree it independently decomposes its multiplicity into all irreducibles of the required parity. This gives exactly 44,15,4 endpoint shapes. The generated complete lists are in `ENDPOINTS.json`. Thus the two complete pair domains contain 44*4=176 and 15*15=225 pairs, 401 total.

## 6. Exact surviving pairs and their contradictions

Exact class-character evaluation of the two necessary Euler equalities leaves four pairs in Case I and ten in Case II. They have the following compact product form. Here `1` denotes the trivial representation; a coefficient on O is an irreducible multiplicity space.

### Case I

The two lower endpoints are

    X1=O(-10)+O(-8)+V O(-6),
    X2=W O(-9)+V O(-6).

Each pairs with either upper annihilator

    Y1=O(-6)+S4 O(-5),
    Y2=O(-6)+(W+W') O(-5).

For either lower endpoint the primal test is -1+2D+2P for Y1 and D+3P for Y2. For all four pairs the dual test is

    -chi D1(3)=2W+T6-W',

which has multiplicity -1 at W'. All four are impossible.

### Case II

The two lower endpoints are

    X1=O(-10)+S4 O(-5),
    X2=D O(-6).

Each pairs with one of five upper annihilators:

    Y1=O(-10)+S4 O(-5),
    Y2=O(-10)+(W+W') O(-5),
    Y3=W' O(-7)+O(-6)+W' O(-5),
    Y4=(1+P) O(-6),
    Y5=D O(-6).

For either lower endpoint, the primal test is 3P+V for Y2 and

    -1+D+2P+V

for Y1,Y3,Y4,Y5. The latter has trivial multiplicity -1, excluding those eight pairs. For Y2 the dual test is

    W+S4+T6-W',

whose W' multiplicity is -1, excluding the last two. For completeness the dual test is the same W+S4+T6-W' for Y1,Y5, and 2W+T6 for Y3,Y4.

Thus every one of the fourteen necessary Euler survivors violates a genuine cohomology requirement. No actual endpoint pair remains.

## 7. Independence, controls, and reproducibility

The reviewed author proof SHA-256 is `6e9a8770e4d418e6ba22a3ebaa2b1523605a178ac0522d7f4ab72507d536106a`. The exact proof, checker, input manifest, output, and originals are retained under `author/`. I read the full final proof and checker, replayed its normal and optimized outputs byte for byte, and matched all fourteen endpoint pairs and both final character columns against the independent calculation.

`verify.py` was implemented independently and does not import the author's code, any historical enumeration, or any McKay graph. It uses exact conjugacy-class characters in Q(sqrt5), checks all nine irreducibles' orthogonality, dimensions, and center signs, derives the source and ambient characters, verifies the formal determinant and K identities, and computes every endpoint and pair from the intrinsic domain above.

Run:

    python3 verify.py
    python3 -O verify.py
    python3 test_controls.py

The first two outputs must match `RESULT.json` byte for byte. The controls rerun genuinely modified computations and require failure for source-hash corruption, physical A/V exchange, omitted H1 corrections, a changed defect weight, reversed endpoint parity, wrong K twist, wrong dual quotient twist, substitution of Q* for E, and replacing exact character equalities by dimensions alone. The source/dual control deliberately uses the unequal rank-13 and rank-17 presentations and is rejected. The dimension-only mutation is also rejected: ordinary dimensions cannot supply this equivariant obstruction.

The verifier is an arithmetic check of universal necessary consequences. It is not a proof assistant for the actual geometry, saturation, differentiation, source presentations, or all their transitive inputs.

## 8. Final frozen-byte reconciliation

After the first review, the author added exactly three verifier checks: the formal Laurent-class elimination at shift -6, the recorded dual quotient twist -2, and the two interior persistence inequalities. No other computation changed. The final author output differs only in its check counter, now 10,951 rather than 10,948; the proof and all endpoint/table results are unchanged. The final author normal and optimized runs both reproduce the retained final RESULT.json byte for byte. The independent review still has 470 checks and nine rejected executable mutations.

Final author hashes:

- PROOF.md: `6e9a8770e4d418e6ba22a3ebaa2b1523605a178ac0522d7f4ab72507d536106a`
- verify.py: `361a7f384ce4be88d95a2d19a6ec653ed2a416ee5b6e7a261058fa3160b64500`
- RESULT.json: `7b9a975bfb8213b90b06274721627030002ce9b1bcf39a0b2fa2085e2de0e836`
