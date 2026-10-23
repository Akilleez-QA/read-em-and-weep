# Independent review: source127 universal abstract family

## Verdict: PASS

The theorem in the reviewed `PROOF.md` is valid as stated: it constructs a nonempty one-dimensional open family of abstract equivariant constant-bundle inclusions with the source127 c-d-f splitting, the displayed zero-defect Gauss quotients, and maximal profile (1,1). It does not establish actual HM realization, remove a source edge or stable label, or classify all abstract realizations. No correction is required for this bounded conclusion.

This review binds to the exact SHA256 hashes:

- `PROOF.md`: `181c81c415427abef3b0e046a2791eea39bbbb65084c64afdab9227c515d1547`
- `verify.py`: `690c1e3ba33a488b98f4bef7faee5b67a9c1e55363d0e27b655afbafac350a08`
- `REPRODUCE.md`: `c992480faf4fdc85a525da17a798615cfb5feee98ed6aab5e98d332e367e645b`
- `audit-inputs/manifest.json`: `152a32f04a6828c2fef7ea3d89a1902f03d54d72fc9ba937492113c4deaca014`

The proof and verifier were not edited. Review date: 2026-10-23 UTC.

## 1. Scope and immutable inputs

I read the original actual/sheaf and strict-top notes, the source127 entry and its stable-label entry, and the relevant original first-polar and saturated derivative-image arguments in PR802 and PR796. The input bytes pass their recorded Git blob checks:

- ACTUAL.md: `b93e0b3589ef71cf2c029fd07a6bdb1da8ba92b3`
- STRICT-TOP.md: `d7506dae49b4be43230450c4132bd5db91f137ef`
- pairs.json: `fe0afa410d89340d3082dc814277f89fbb582c19`
- frontier.json: `8b5971092f9ef762584912609fd5e9301c4e271d`
- PR802.md: `98a1bd6123e148476da0b997d879aecbf885ec97`
- PR796.md: `46a0de762000f21182f6d3168f3ecfd63adaf75f`

The original actual note supplies necessary equivariant bundle data, not a realization theorem. The construction correctly preserves that distinction. In the original tuple formula, c=d=f=1 and the other five entries zero give the quadratic block P+D, quartic blocks V+P, and scalar degree-minus-eight block. The pinned pair127 has the asserted A, B and zero defect; the frontier identifies it with G3.11.cce6e3ba4eeb.

## 2. Nonemptiness is proved, not inferred from equal characters

All four necessary channel assertions are justified.

1. Contraction by the alternating covector associated to the tautological variable gives a surjection A O(18) -> W O(19), whose kernel is the squared tautological line O(16). Its invariant-section sequence is exact because H1(O(16))=0 and taking invariants is exact over C for finite G. Since Sym16 W has no invariant and the other invariant spaces are one-dimensional, the A-to-W channel is nonzero.
2. Multiplication by the nonzero formal line gives an injective fiber map Sym2 W -> Sym3 W. Thus the A-to-S covariant is nonzero. The same conclusion for the V-to-T channel follows from the isomorphism V W=T.
3. The Wp-tensored Euler sequence identifies the P-to-Wp channel with a surjection from a two-dimensional covariant space to a one-dimensional one, with a one-dimensional kernel.
4. Using P=W Wp and T=Sym2 W Wp, the P-to-T map is multiplication by the formal line in the W factor. It is fiberwise injective, hence injective on covariants. The two covariant spaces both have dimension two, so this channel is an isomorphism.

These are precisely the Clebsch channels in the degree-19 multiplication map, up to nonzero scalar choices of irreducible identifications. In particular no possible zero reduced coefficient is hidden by a character count. Since the fixed V-to-T vector is nonzero, its determinant with the isomorphic P-to-T image is a nonzero linear functional. The P-to-Wp functional is also nonzero. Their zero sets remove at most two projective points. Their coincidence would not harm the argument.

Thus Omega is genuinely nonempty. The construction is algebraic in this parameter: if a single universal representative is wanted, the already nonvanishing P-to-Wp functional provides a normalization throughout Omega, after choosing a basis of its fixed one-dimensional target. This does not select a point of Omega.

## 3. Balanced kernel and raw saturation

Surjectivity of the degree-19 multiplication map rules out a common zero of the degree-18 coefficient system: such a zero would also be a base point of every degree-19 image section. The quotient is therefore a line bundle O(18), not a line bundle modified by base-point torsion.

The twisted sequence gives H0(F(1))=H1(F(1))=0. Birkhoff-Grothendieck then forces every summand of F(1) to be O(-1). Equivariantly, H1(F)=Sym18 W-C0=P+D identifies F=(P+D) O(-2).

The raw-image argument is also valid without assuming saturation in advance. The quotient curve is nonconstant, so the raw first span B has full rank ten in C0 O. Its image in O(18) is O(18)(-Delta) for an effective divisor Delta. Therefore deg B=-deg Delta. For a quadratic inclusion, Euler's identity and polarization identify B with the image of (P+D) W O(-1); hence B(1) is generated. Since B is torsion-free on P1 it is locally free. Its inclusion in a trivial bundle bounds all splitting degrees above by zero, and generation after twisting bounds them below by minus one. Consequently deg Delta<=10.

Equivariance makes Delta invariant. The effective projective group is A5, whose smallest orbit on P1 has size twelve, so a nonempty invariant effective divisor has degree at least twelve. Delta must vanish. This proves the raw first span is C0 O and the second fundamental form is actually onto O(16). It is stronger than a generic-image identification and justifies the later transpose argument.

## 4. Standard blocks and dual quotient

The standard quotient formula can be checked directly, independently of a splitting heuristic. For the universal line l, contraction by its alternating covector, repeated k+1 times, is a fiberwise surjection

    Sym^n W O -> Sym^(n-k-1) W O(k+1).

Its kernel consists exactly of l^(n-k) Sym^k W. This proves the exact sequence used in Section 4, including its equivariant quotient and saturation. Differentiating the power l^(n-k) adds the next osculating direction with nonzero coefficient n-k. Thus the first span is U_(k+1)^n with no divisor defect, and the line increment has degree 2k-n+2.

For U_6^10 and U_0^8 the derivative quotients are therefore O(2) and O(-8). Their ordinary quotients are S O(7) and (Wp+T) O(1). Together with O(18) from F these give the asserted Q of rank thirteen and degree fifty-four. Its dual has no sections and Q(-1) is generated.

The connection preserves the explicitly constructed constant direct sum. It is not being asserted to preserve an arbitrary Birkhoff-Grothendieck splitting. Hence the direct sum of these three raw images is saturated. The dual second fundamental form is the negative transpose; a locally split constant-rank map has a locally split transpose. It follows that the dual Gauss quotient is exactly A_q^*(-2), not a torsion modification. This yields O(-18)+O(-4)+O(6).

The strict-top conclusion follows from the original strict-top lemma for any saturated negative subbundle; the proof's shorter argument is consistent with it. In this direct-sum construction a quadratic-block derivative cannot acquire a component in either other constant factor. A top degree-minus-two summand killed by the derivative would have zero internal derivative by degree and would be horizontal, contradicting its negative degree.

## 5. Generic second osculation in the backward direction

The forward ranks follow directly from the standard block increments and the constant first span of F: the first and second gains are three and two.

Under the invariant apolar pairing, the annihilator of U_k^n is U_(n-k-1)^n. Thus the dual blocks are indeed the nondegenerate line curve O(-18), U_3^10 and U_7^8. Their first gains are one each. At the next step the standard gains are one and zero.

The remaining line-curve gain is genuinely one. Here is an independent universal justification of the Wronskian step. If its value, first derivative and second derivative had generic span at most two, divide the coordinate functions by one nonzero coordinate. The normalized coordinates include 1 and a nonconstant function u. For each other normalized coordinate v, the vanishing three-function Wronskian gives u'v''-u''v'=0. In the characteristic-zero function field C(P1), this means (v'/u')'=0, hence v=a u+b with constants a,b. All original coordinate sections would then span a vector space of dimension at most two. This contradicts the injective ten-dimensional coefficient system.

This uses no chosen parameter or evaluation. It proves the next generic dual gain is one even if higher osculating maps have ramification. Thus the opposite total gains are also three and two. The endpoints on both sides have rank two, so the rank-three plateau containing E has exactly the claimed maximal profile (1,1) in the original convention.

## 6. Parameter inequivalence

The highest-slope subbundle F is intrinsic to E: it is the degree-minus-two part of the canonical slope filtration. Any constant equivalence over the identity of P(W) must preserve it and, by compatibility with the constant connection, preserve its first span C0 O. It therefore induces an equivalence of the degree-18 quotient sequences.

An automorphism of O(18) over that fixed base is scalar. Changing basis in C0 does not change the image coefficient subspace inside H0(O(18)). That subspace contains the fixed unique A and V constituents and the P constituent selected by p. Equality of these image subspaces forces equality of their lines in the two-dimensional P-multiplicity space. Hence different points of Omega are inequivalent under the equivalence asserted in the proof. This does not assert a normal form for inclusions with couplings between the three constant blocks, nor a classification modulo unspecified base changes.

## 7. Executed verification and evidence boundary

I ran `python3 verify.py` successfully. It checked all six input blob hashes, the fixed character identities and Euler-space dimensions, the bundle/cohomology characters, the source tuple and stable-label identification, and the universal rank/degree arithmetic. I also inspected the checker: it performs only exact finite abstract character arithmetic and reads the pinned catalogs. It does not contain a parameter search or selected-instance test.

The geometric proof, especially channel nonvanishing, absence of raw defect, and generic second osculation, was audited separately above; the script's passing status is not substituted for those arguments. No actual HM/source coefficients, parameters, points, derivatives, matrices or source-instance ranks were selected or evaluated. No selected model, scan, large computation or publication was performed.

The verified contribution is an obstruction to exclusions based solely on these structural conditions: they are consistent on the source127 c-d-f edge. Any exclusion of the fixed actual HM source must use additional actual-module constraints. The actual HM realization question and the original research goal remain open.
