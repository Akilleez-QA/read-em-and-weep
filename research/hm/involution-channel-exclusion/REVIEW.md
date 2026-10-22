# Independent review: involution-channel exclusion

## Verdict

**PASS, conditional on the explicitly pinned canonical-interface and support inputs.** The exclusion proof is mathematically sound. No substantive gap was found in its incidence argument, equivariant determinant bookkeeping, septic factorization, representation-theoretic obstruction, or use of the Plücker identity. The stronger reduced-scheme and two-exceptional-channel conclusions follow from the separately supplied reduced-channel predecessor, not from support exclusion alone, and the proof says so correctly.

The review checks the proof against the canonical-interface dependencies and the reduced-channel theorem at PR668, ca3c34c40363bde6315a0797eb66a5d3ea68c104, and the universal square-rank theorem at PR667, 7d53ea234b99b75e89a29c4caba7ec564e134410. This is mathematical review, not proof-assistant certification. No selected actual evaluation or computation is used.

## 1. Incidence and polarity

The D10 stabilizer of each C5 axis contributes exactly five involutions. Since the fifteen involutions form one conjugacy class, the thirty incidences distribute uniformly, giving exactly two fixed C5 axes per involution. These fixed points cannot be the involution's positive C2 axis, so they lie in its negative eigenspace.

For the invariant nondegenerate bilinear form, the positive and negative eigenspaces are orthogonal. Thus both polar lines contain the positive axis. Distinct C5 points have distinct polar lines, and two distinct projective lines have a unique intersection, establishing the stated intersection formula.

The nonisotropic positive line uniquely determines an orthogonal determinant-one involution: it acts by +1 on that line and by −1 on its orthogonal complement. Hence distinct involutions yield distinct intersections and distinct unordered C5 pairs. The two sets both have cardinality fifteen, so every pair occurs. This also excludes triple concurrence, rather than silently assuming general position. Each of the six polar lines therefore contains five distinct nodes.

The product F6 of the six line equations spans a G-stable line. Its character is trivial because A5 has no nontrivial characters. This establishes invariance of the polynomial itself up to the freely chosen overall constant, not merely invariance of its divisor.

## 2. Double-point septic factorization

For each line, restriction of a surface germ in m² lies in the square of the curve maximal ideal. A nonzero restricted septic cannot have five double zeros. Thus each line divides every scalar septic component in question. The six equations are distinct irreducible factors in Sym(A*), so their product divides each component, with a degree-one quotient.

This argument does not require that the hypothetical channel zero scheme be reduced. Mere vanishing of the channel at the fifteen points puts every entry in m and every exterior minor in m². Thus neither the reduced-channel theorem nor its fixed-channel length bound is being used implicitly.

The asserted optional equality of spaces is also correct: at every node exactly two of the six lines meet, and F6 has order two. Multiplying by an arbitrary linear form preserves the required double vanishing.

## 3. Equivariance and twists

The exact sequence has rank(K)=2 and gives

    det K = det D ⊗ (det A)* ⊗ O(−3) ≅ O(−3).

Both constant determinant representations are trivial characters of A5. The target of t_q is P⊗O(2), whose second exterior power is Λ²P⊗O(4). Consequently its exterior square is a section of Λ²P⊗O(7), exactly as claimed.

Because Q is a trivial G-module, a fixed q gives an invariant section. A kernel channel at one C2 axis therefore vanishes on the entire orbit. The nonvanishing of both pure parity sections forces this channel to have both components nonzero. In particular its symmetric component is nonzero, which is precisely the hypothesis needed for the universal generic-rank-two theorem.

Division by invariant F6 is equivariant and unique in the polynomial ring. The quotient belongs to Λ²P⊗A*, so its interpretation as a G-equivariant linear map A → Λ²P is correct; no A-versus-A* convention or projective twist is lost. Nonzero exterior square gives a nonzero quotient.

## 4. Representation-theoretic and Plücker obstruction

The displayed character calculation yields Λ²P ≅ A⊕A′, with nonisomorphic self-dual three-dimensional summands and multiplicity one. A nonzero equivariant map from irreducible A is therefore an isomorphism onto its summand.

Exterior multiplication on Λ²P is symmetric because its arguments have even degree. It is nondegenerate, as seen by pairing complementary basis bivectors. Its target det P is trivial. Schur's lemma annihilates the off-diagonal block between A and A′; nondegeneracy of the full pairing then forces both diagonal blocks to be nondegenerate. In characteristic zero, the quadratic diagonal of a nondegenerate symmetric form cannot vanish identically. Hence j(a)∧j(a) is a nonzero quadratic polynomial. The stronger identification as a nonzero multiple of B(a,a) follows from uniqueness of the invariant form on irreducible self-dual A.

The exterior square of a map with rank-two source is decomposable in every local trivialization, including at points where it is zero. Therefore w_q∧w_q vanishes identically as a section of det P⊗O(14). After substitution, F6²(j∧j)=0 is an identity in the integral polynomial ring, so cancellation is valid. This contradicts the preceding nonzero quadratic. No conclusion about the value of the actual endpoint map at a selected point enters this step.

## 5. Dependency and consequence audit

The pinned square-rank predecessor's Sections 2–4 establish generic rank two for every channel with nonzero symmetric component, independently of its later actual-normal-variation datum. In particular:

- The symmetric map is proved to be an everywhere embedded osculating bundle using the universal Wronskian argument.
- Hypothetical generic rank one for a mixed channel would force the degree-six covariant to factor through that bundle.
- The resulting Hom group vanishes by the O(−1) twist.

The exclusion uses exactly this universal nonzero exterior-square consequence. It does not import the later actual-channel identification, twelve-point divisor, saturation, or sextic matrix factorization. The chosen binary realization in that predecessor supplies the canonical A in the application; the same representation-theoretic reasoning is unaffected by interchanging the two three-dimensional representations, provided the stated canonical-interface inputs are supplied for that choice.

PR663 supplies rank at least one and the known sixteen rank-one points. Thus a point of the rank-at-most-one locus has a genuine nonzero kernel channel, and the contradiction excludes every C2 point. PR664's finite support alternative then gives exactly the sixteen known points. These are the only additional steps needed for the support theorem.

The reduced-channel predecessor separately proves that every fixed-channel zero scheme and the detection scheme are reduced, and that the C3 and C5 kernel lines are distinct. Its local stabilizer argument correctly supplies the missing implication from reduced channel zeros to reduced detection scheme. Combining these already established results with C2 exclusion yields length sixteen, exactly two exceptional projective channels of lengths six and ten, and empty zero schemes for all remaining nonzero channels.

## Limits and editorial observations

No mathematical correction is required. The conclusion is correctly conditional on the pinned interface results. The proof correctly distinguishes the family-detection rank, the zero scheme of a channel section, and the rank of the associated fixed map. It does not identify the actual HM channel, evaluate actual coefficients or ranks, or establish any later lifting, Bockstein, or original-theorem repair claim.
