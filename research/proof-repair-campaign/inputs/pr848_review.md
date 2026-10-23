# Independent review: the index113 two-D source exclusion

## Verdict and exact binding

**PASS for the entire index113 source tuple (0,0,0,0,0,2,0,1), and only the stated conditional neighboring result.**

This review binds to the exact contents of:

- `NEXT-FF-EXCLUSION.md`, SHA-256 `70a85a7fc501598cfd81d8ee91a4c3244cb195a463a05eaf2a3a43ff93f17ca4`;
- `next_verify.py`, SHA-256 `7ed8b6a366429c179b319318300c89ac47dca33c3670db6024d23ed7864b33ff`.

The conclusion is a whole-source-stratum exclusion for G3.11.ad509d55173f at original source index113. It is not a whole-label exclusion. For index127, the scalar-nonzero branch of the separately described source is excluded, but no whole source edge is removed. The review is an independent mathematical and executable-check review, not proof-assistant certification.

## 1. Immutable inputs checked independently

The following files were fetched directly at the commits named in the proof. Their exact fetched bytes were retained under `audit-inputs/NEXT-*`; the Git blob hashes computed from those bytes are:

| Dependency | Commit | Git blob SHA |
|---|---|---|
| ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md | db51525015bb7c5e825833d550d08dedf6f6ea96 | b93e0b3589ef71cf2c029fd07a6bdb1da8ba92b3 |
| NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md | db51525015bb7c5e825833d550d08dedf6f6ea96 | d7506dae49b4be43230450c4132bd5db91f137ef |
| one-one-endpoint-necessary-pairs.json | db51525015bb7c5e825833d550d08dedf6f6ea96 | fe0afa410d89340d3082dc814277f89fbb582c19 |
| rank-three-quotient-frontier-144.json | db51525015bb7c5e825833d550d08dedf6f6ea96 | 8b5971092f9ef762584912609fd5e9301c4e271d |
| PR802, profile11-o16-constant-span-exclusion/PROOF.md | e484640a6565c278321bf6557860262c1ac1b7df | 98a1bd6123e148476da0b997d879aecbf885ec97 |
| PR796, profile12-quadratic-block-exclusion/PROOF.md | d2b43060c83328dd5118aee6b9288fcfa0c873ac | 46a0de762000f21182f6d3168f3ecfd63adaf75f |
| PR828, profile11-horizontal-quotient-exclusion/HORIZONTAL-CONSTANT-QUOTIENT-EXCLUSION.md | ae077cbe42d65cde27d65ce88923dc35851b6952 | 6b43295c16eda2abd79e9d3c774d4d57139e1ff7 |

The first four paths lie under `research/hm/order-four-quadratic-load/`; the last three lie under `research/hm/` followed by the paths shown. The original catalog identifies index113 with G3.11.ad509d55173f, A_q=O(-10)+O(2)+O(16), B_q=O(-18)+O(-4)+O(8), and original defect zero. Its ten source tuples are exactly the ten specified in the proof, with no duplicates. The chosen tuple decodes, by the original eight-parameter formula, to (P+2D) O(-2)+2 O(-8)+O(-10).

The index127 identity, A_q=O(-8)+O(2)+O(16), original defect zero, and membership of both source tuples discussed at the boundary were also checked. These are original necessary overlists, not assertions of realizability or current-frontier counts.

Only the stated interfaces are imported: the actual bundle/strict-top facts, the saturated internal/external image lemma, the complete P+D line-system kernels and polar argument, and the preserved-lattice lemma. None of the later papers' whole-label conclusions or profile-(1,2) interior conditions is used. PR802 restates and proves its first-polar generation interface, so no additional unexamined PR799 conclusion is needed here.

## 2. The high-line subsystem and its two derivative alternatives

Strict-top supplies an injection on coefficient representations, not a fiberwise injection into a rank-two quotient. On the D multiplicity spaces, both source and target have dimension two; the injective map is therefore an isomorphism. Its low-row kernel is a constant D multiplicity line. Since P has no low-row component, F=(P+D) O(-2) is an actual saturated direct subbundle of E. Its restriction to O(16) is injective on its nine coefficient sections. A nonempty invariant common divisor has degree at least twelve, leaving at most seven sections of O(18), so this restriction is onto everywhere.

The three kernels in equation (1) are the complete P+D list from the pinned PR802. I also independently checked its bounded universal support calculation: the only degree-at-most-minus-four atoms fitting H1(K0(2))=A+V+P are A O(-4), V O(-4), P O(-4), Wp O(-5), O(-6), and O(-10). Matching chi(K0(3))=-W gives precisely the three listed kernels. This is a universal representation calculation, not an evaluation of a source instance.

For each kernel, all maps into D O(-4)+2 O(-10)+O(-12) vanish except the O(-10) atom's constant row into the two O(-10) summands. In particular the D-target exclusions include the potentially dangerous O(-6) and O(-10) atoms, using the absence of D in Sym2 W and Sym6 W. A nonzero constant row into 2 O(-10) is everywhere a line subbundle. Hence both possible internal images, zero and O(-10), are saturated. With the saturated external O(16), PR796 applies to the actual raw image without a divisor correction.

In the nonzero case the first-polar and Euler-character calculation gives the actual bundle A O+(Wp+T) O(-1). The pinned polar contradiction applies unchanged. Its input is the actual constant A, saturated quadratic F, and exactly three channels P-to-Wp, P-to-T, and D-to-T. It never uses which lower source summand receives the internal O(-10). Its nonzero-channel argument uses the Euler surjection, tautological multiplication injection, and a basepoint-free degree-seven Wp system, not a selected coefficient calculation. The new two-component constant row therefore introduces no unexamined nonzero branch.

In the zero case F^+ has rank10 and degree0 and is saturated in the constant ambient bundle. It is consequently a genuine constant C0, with coefficient A+V+P. The map C0 O/F -> E^+/E is an isomorphism onto the saturated high line O(18). Therefore E intersect C0 O=F as sheaves, and E+C0 O is saturated. This proves the projected inclusion of Z rather than assuming that projection preserves saturation.

Since constant projection commutes with differentiation and C0 lies in the saturated raw forward span of E, the projected raw span is E^+/C0 O and is saturated. Its quotient by Z is exactly O(4)+O(-8). Equivalently the actual derivative quotient of Z is O(2)+O(-10). There is no torsion or divisor alteration in this identification.

## 3. The residual quadratic block and its actual constant span

The top D0=D O(-2) is saturated in Z and hence in the constant quotient ambient bundle. Its O(-10) component vanishes, while strict-top forces the O(2) component to be nonzero. The latter is the complete quartic evaluation map, with exact kernel S O(-3). That kernel has no map into 2 O(-10)+O(-12), so its internal image is zero and its external O(2) is saturated. Thus M=D0^+ is an actual saturated bundle with M/D0=O(4), rank6 and degree-6.

First-polar generation restricts M's degrees to 0 and -1. Its rank and degree therefore force all six degrees to be -1, and the Euler character at twist one gives M=T O(-1). Its derivative kills D0 and factors through the line M/D0; its rank is at most one. It cannot vanish because a horizontal saturated subbundle of a constant bundle is constant, whereas M has degree-6.

For a pure-linear inclusion, values and first derivatives span the full constant coefficient space. Therefore M^+=C1 O has rank7, and C1 O/M is a genuine locally free line of degree6. Saturation of M in the ambient constant bundle is essential here and has already been established. Taking global sections in this sequence gives C1=H0(O(6))=Sym6 W=V+P. The subsequent contradiction only requires its dimension and line quotient.

## 4. Endpoint removal, exact intersections, and the rank-eight span

Only the O(-10) source summand of Z can map to the negative quotient O(-10). Surjectivity of the actual quotient forces that scalar to be nonzero. Consequently Z'=D O(-2)+2 O(-8) is an actual saturated kernel, with rank7 and degree-26.

Because D0 already surjects onto the positive O(2), the full derivative kernel K fits into

    0 -> S O(-3) -> K -> 2 O(-8) -> 0.

The extension splits equivariantly: its ordinary extension group is a sum of H1(O(5)) terms and vanishes, and averaging preserves a splitting. Thus Hom(K,O(-12))=0. Derivatives of K lie in Z, and their remaining component modulo Z' is exactly this zero map. The internal image for Z' is therefore zero, and its external O(2) is saturated. PR796 proves that G=(Z')^+ is saturated, with G/Z'=O(4), rank8 and degree-22.

The identity G=Z'+M is an identity of actual sheaves. Indeed M/D0 maps isomorphically onto the external O(4), and M intersect Z=D0 by the zero-internal-image sequence for D0. In particular M intersect Z'=D0. Both Z'+M and G contain Z', have the same image in the ambient quotient by Z', and have no hidden torsion correction. No arbitrary horizontal splitting of Z or G is assumed.

## 5. The horizontal-lattice contradiction

Set S0=Z'+C1 O. Local sections lift locally to the direct sum defining this image. Their derivatives lie in Z'+M+C1 O=S0 because G=Z'+M and C1 is constant. Thus the possibly unsaturated coherent sum is genuinely preserved by the ambient trivial connection.

Its saturation is horizontal: its second fundamental form vanishes on the generic locus, hence everywhere. In characteristic zero its Grassmannian map is constant. In that constant saturation, S0 is a full-rank locally free lattice. The determinant argument from PR828 applies to the preserved lattice itself: a local determinant t^m would have derivative m t^(m-1)dt outside its own lattice for any m>0. Hence m=0 everywhere, and S0 itself is saturated and constant. This disposes of the possible divisor defect rather than overlooking it.

Since C1 O/M has rank one and G=Z'+M, the rank of S0 is8 or9. Rank8 is impossible: G is already saturated in the ambient bundle, so a same-rank enlargement inside that ambient bundle cannot be a nontrivial torsion enlargement. It would give G=S0 constant, contradicting degree-22. Thus rank S0=9.

The quotient S0/G is locally free, since G is saturated in the same ambient bundle. Its rank is one and its degree is22. The sum identity gives a sheaf-surjective map

    C1 O/M=O(6) -> S0/G=O(22).

A sheaf-surjective map between line bundles is an isomorphism, not merely a generically nonzero polynomial map. The degrees differ, so this is impossible. This establishes the whole stated index113 source exclusion, without an additional open saturation or intersection branch.

## 6. The index127 statement remains conditional

For the source (P+2D) O(-2)+O(-8)+W O(-9) at index127, the same high-line argument gives the projected Z=D O(-2)+O(-8)+W O(-9) with derivative quotient O(2)+O(-8).

If the O(-8)-to-O(-8) scalar is nonzero, its kernel is the graph of a map from W O(-9), so Z' is isomorphic to D O(-2)+W O(-9). The derivative kernel is an extension of S O(-3) by W O(-9); it splits because the relevant H1(O(6)) vanishes. Hence it has no map to O(-10). The exact same preserved-sum proof then gives a forbidden surjection O(6)->O(24), with deg G=-24. This branch exclusion is valid.

If that scalar is zero, the negative quotient is supplied by the nonzero Euler map W O(-9)->O(-8). Its kernel is O(-10), so Z' includes O(-8)+O(-10) in addition to D O(-2). The full derivative kernel has an O(-10) summand and can have a constant internal derivative into (Z/Z')(-2)=O(-10). The internal-image-zero premise used above is not automatic. The proof correctly leaves this branch open.

For index127's h-f-f tuple, removal of the O(-8) quotient likewise leaves an O(-10) block and the same possible internal channel. No whole index127 edge follows from this review.

## 7. Executable check and scope

At the bound hashes, running `python next_verify.py` returned:

    PASS: three pinned P+D kernels; all internal channels; both first-polar characters; residual degree22 contradiction.
    The preserved-lattice and actual-image statements remain mathematical arguments, not executable assumptions proven by this check.

The verifier uses exact Q(sqrt(5)) character arithmetic and checks orthogonality, fixed kernels, internal Hom channels, polar characters, and the degree22 arithmetic. It does not claim to prove saturation, differential preservation, kernel-list completeness, or the actual-image identities by execution. Those were reviewed mathematically above. The independent catalog audit and bounded universal support check agree with its inputs and claims.

No selected actual source/HM coefficients, points, derivative values, matrices, instance ranks, selected models, or large computations were used. No publication, submission, merge, frontier recount, whole-label exclusion, source2 result, O26 result, or global rank conclusion was performed or obtained. No mathematical gap was found within the exact stated source113 exclusion and conditional source127 branch.
