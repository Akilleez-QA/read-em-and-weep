# Independent whole-packet review

**Verdict: PASS for exclusion of actual maximal profile (2,1), conditional on the pinned actual hypotheses and the two explicitly imported direct reductions.**

Review date: 2026-10-23. This verdict is bound to these SHA-256 digests:

- `PROOF.md`: `be3e6ef741268733f9ddc02405a3d8e030742d8ff3f2378570a0f0d1fe4d1328`
- `RESULT.json`: `4d5b7ca0967538828003d7889cd1496de9264139e44350439357a93ba2933fe5`
- `verify.py`: `ce60f9ef0bc3803df1e29f2b14a9523fa2b2840be5fac99151caacd0985dd82a`
- `characters.py`: `5b3b1d415f26ca467670afeb73357cbb0e9c125a6b1acd25155b6d85eef4e4f1`
- `INPUTS.json`: `d1ef25085c704f850f8d587f55e75112d5813f0752a9033d59e610ee6f3a6a19`
- `REPRODUCE.md`: `919d71b312f59ddd5e6fcb03bdc1bafd21400053834741992a1fadf2d86882d3`

No mathematical gap was found in the stated scope. This is not a global 182-row coverage certificate, COV, exclusion of profile (1,1), or global generic-rank-three exclusion.

## 1. Artifact, source-pin and original-row audit

I inspected all packet artifacts and the complete source proofs. I independently recomputed byte counts, SHA-256 digests and Git-blob SHA-1 digests for all ten input files. Every identity agrees with INPUTS.json. The author's fresh remote authentication is accepted; this review did not repeat those remote fetches.

The imported PR1134 proof at commit 7cb2e260b2bcbac15df89612b6a2096263a9c89c is byte-identical to the direct-reduction packet previously reviewed here. PR1135 at 24e713fe352f4ff8f70cd2e86940afa70df99c5c is byte-identical to the cubic-rigidity packet supplied for this review. The original equality and intersection proofs agree with the earlier full pinned copies read during the preliminary mathematical review. Neither their historical retained-label coverage nor their longer source classification is needed for the new argument.

The fixed frontier's source hash for `two-one-primal-interior-quotient-summary.json` is

    33c37ec7fe996888465d7950ebab02100c73177fceb85e9fde5434edcbbd575c.

I verified the available original summary against that authenticated hash and matched all thirteen of its ordered entries to the frontier's profile21 rows, including source_index, full equivariant A and B, original_defect, and source commit f7071d29886c83151028576bf32e001c347cafc9. The displayed thirteen-pair theorem agrees with those shapes. Its geometric necessity is an imported theorem, not inferred from the JSON.

The two preceding direct cuts are exactly {0,1,8,11,12} and {3,4,6,7}; the present cut is {2,5,9,10}. They are disjoint and cover the original thirteen rows. Both original defect-12 rows are in the cubic-rigidity cut, and all four rows addressed here have original defect zero. The surviving four stable IDs before this packet are respectively:

    2  G3.21.d610e381ed75
    5  G3.21.ed1df480d8d2
    9  G3.21.1c43993b4f83
    10 G3.21.d41783aef00b

No separate second-primal determinant defect is set to zero or otherwise used.

## 2. Actual dual endpoint orientation

The original primal plateau is M subset K subset E subset E-plus, with E at index k=2 and forward length l=1. The reversed annihilator plateau begins with (E-plus)-perp=L, followed by E-perp=S=Q*. Thus L, not S, is the dual endpoint. Maximality of the rank-three plateau makes its derivative rank at most two. This is also the transpose of the derivative at the primal forward endpoint.

The other parameter k=2 supplies H0(Q*(1))=0 through the pinned section-persistence theorem; hence top S<=-2. These are distinct uses of k and l, not an exchange of the actual E and Q* source bundles. Rank S=13, degree S=-54, rank L=10, and degree L=-54-degree B are consistent with the actual ambient exact sequence.

All derivatives are those of the original saturated inclusions in the constant dual ambient space. No terminal-pencil model or abstract complement is substituted for that inclusion.

## 3. Capacity derivation and eventual descent

For each successive kernel F_j, its quotient by the next kernel is the torsion-free image of its actual derivative, so it is locally free on the parameter curve. Saturation in the original ambient follows by extension from saturation in its predecessor. A local section of F_j differentiates into F_(j-1); after quotienting this gives G_j -> G_(j-1)(-2), with kernel already removed. It remains a sheaf injection at ramification and need not have saturated image in the target.

Consequently q_(j+1)<=q_j<=2. A nonzero F_j has negative degree and cannot have zero derivative: a horizontal saturated subbundle of a constant bundle in characteristic zero is a constant subspace bundle. Every nonzero step therefore decreases rank, and starting from rank-ten L the chain reaches zero after at most ten further kernel operations. This justifies both finite telescoping and sum q_j=10, without assuming a persistent endpoint rank.

The determinant injection gives the top-wedge degree bound. Counting each of the first two columns of the nonincreasing rank partition gives h_1+h_2=10, h_1>=h_2>=0 and

    degree L <= h_1 lambda_1-h_1(h_1+1)
                +h_2 lambda_2-h_2(h_2+1).

With h=h_1, this is the independently expanded quadratic

    -2h^2+(lambda_1-lambda_2+20)h+10lambda_2-110,

for precisely h=5,...,10. Repeated ordinary degrees are counted with multiplicity; in particular W'O(-11) contributes two degrees -11. There is no uniqueness-of-top-wedge assumption in the strict-capacity cases.

The independently recomputed capacity lists, in that height order, are:

- Index 2: -50,-42,-38,-38,-42,-50; actual degree -38.
- Index 5: -60,-50,-44,-42,-44,-50; actual degree -36.
- Index 9: -70,-58,-50,-46,-46,-50; actual degree -34.
- Index 10: -85,-70,-59,-52,-49,-50; actual degree -38.

Thus indices 5,9,10 are strictly impossible, and index 2 can only have heights (7,3) or (8,2).

## 4. Equality, actual symbols and the full polynomial span

For index 2, all individual degree losses in the summed determinant bounds are nonnegative. Equality of the total therefore forces equality at every stage. Its target degrees 6,-4,-18 are distinct. For ranks one and two the maximal wedge summand is unique, so the determinant has no components into lower wedge summands. The generic image is the corresponding top-degree flag, the map factors through that flag globally, and its equal-degree nonzero determinant is nowhere vanishing. Each composite graded injection is therefore an isomorphism onto that flag, including at ramification.

Compatibility of the composites then identifies each intermediate derivative symbol with the appropriate top-flag inclusion. In particular the highest-line channels cannot vanish. This is the extra connection information required for osculation; a degree match alone would not suffice.

In the packet's indexing the last nonzero bundle is F_h=G_h=O(6-2h). Strict top decrease from F_0=S gives top F_h<=-2-h. The h=7 line would have degree -8 instead of at most -9, so that height is impossible. For h=8 the last line is C=O(-10).

Starting with C, each of its first eight derivatives has a nonzero leading component in a new filtration quotient. Lower derivatives lie in the previous filtration term and cannot cancel that component. Thus its eighth forward span has rank nine in S. This is valid under saturation and does not require a splitting of the filtered connection.

The equivariant inclusion C -> H*O has coefficient map Sym10 W -> H*. Its constant image has dimension at least nine. The decomposition Sym10 W=A_std+V+D consists of distinct irreducibles of dimensions 3,3,5. Every proper equivariant quotient has dimension at most eight. Semisimplicity therefore forces the full eleven-dimensional polynomial system, defining the actual invariant constant subspace V_0.

For that complete system, the universal kth osculating fiber is l^(10-k) Sym^k W, and the bundle is Sym^k W O(k-10). The multiplication map is fiberwise injective, so it is a subbundle of V_0 O. Its generic containment in the appropriate saturated actual F_(8-k) extends everywhere. At k=8 this gives U=Sym8 W O(-2) inside S, in the actual constant V_0. No unspecified projected polynomial system or jet-bundle splitting is assumed.

## 5. Annihilator contradiction

The invariant apolar pairing identifies the annihilator of l^2 Sym8 W in Sym10 W with l^9 W. Hence U-perp inside V_0*O is W O(-9).

Because E is exactly the annihilator of S in the original dual pairing, its restriction to V_0*O factors through this subbundle. The pinned direct reduction has forced the exact actual D-type, whose least ordinary degree is -8. Therefore Hom(E,W O(-9))=0 even without equivariance. The restriction is zero, so the entire constant V_0 O annihilates E and lies in S. This contradicts H0(S)=0.

This argument uses only restriction to a genuine constant subspace and annihilators. It requires neither a horizontal complement nor the longer general-source classification from the historical intersection proof.

## 6. Independent character and execution checks

I independently recomputed the needed symmetric-power characters by size-weighted class averaging, not by importing characters.py or using its McKay recurrence. For standard trace x, the calculation used

    s_n(x)=sum_k (-1)^k binom(n-k,k) x^(n-2k),

on the nine trace classes 2,-2,phi,-phi,phi-prime,-phi-prime,1,-1,0 with sizes 1,1,12,12,12,12,20,20,30. Here phi=(1+sqrt(5))/2 and phi-prime=(1-sqrt(5))/2. The irreducible table was independently orthogonality-checked; V and W' are the sqrt(5)-Galois conjugates of A_std and W, and P is the A5 five-point permutation character minus its trivial constituent. This gives

    Sym8 W=P+D,
    Sym10 W=A_std+V+D,

with dimensions 9 and 11 and the stated proper-quotient bound eight. The separate quadratic-capacity and original-row checks also passed, both normally and with Python optimization.

The production commands `python verify.py` and `python -O verify.py` both succeed and each internally reproduces RESULT.json exactly, with 154 recorded checks. Their stdout streams are identical; the ordinary final print adds one trailing newline beyond the serialized file, without changing the exact internal replay. No imported historical verifier was executed.

Only this REVIEW.md was added to the packet. No production file was edited and no public write, selected actual coefficient, point, map, matrix, instance rank, historical enumeration, or unapproved experiment was used.

## Certified conclusion

Under the explicitly pinned actual hypotheses, the original thirteen-pair necessity theorem, PR1134's direct reduction and PR1135's cubic rigidity, all four remaining actual profile-(2,1) shapes are impossible. The resulting maximal-profile-(2,1) exclusion is proved. The proof correctly withholds any global profile-exhaustion, profile-(1,1), COV, or global generic-rank-three conclusion.
