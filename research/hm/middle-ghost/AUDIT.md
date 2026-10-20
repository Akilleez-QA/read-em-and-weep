# Independent audit of the middle ghost bound

## Verdict and fingerprint

PASS, conditional on the explicitly imported audited HM cohomology, normalizer linearization, and actual low-H¹ multiplication theorem. No mathematical correction is required. The proof establishes e∈{0,1}; if e=1, both degree-five middle Tor groups are trivial representations of the full normalizer N, not merely Heisenberg-invariant lines.

Reviewed file: PROOF.md.

SHA-256: f56a6769c357f4bd39e6bf2b3ca5dafdeae03892388e67f20874dbb593e1d38f

Audit date: 2026-10-20 UTC.

## Inputs independently checked

I read the proof and audit pairs in the imported middle-relation-dependency, middle-module-relations, and quintic-scalar-propagation directories, together with the linear-strand addendum in middle-relation-dependency. The relevant input is the actual multiplication theorem in quintic-scalar-propagation §8: H¹B(−1)=V and H¹B(0)=End(V)/C·id, with multiplication a nonzero scalar times the quotient. It is not enough merely to identify the representations; the imported theorem proves nonvanishing and hence the stated kernel and surjectivity. I do not re-prove its underlying HM cohomology or the primary-paper calculations here.

The previously established trace pairing is symmetric and compatible with multiplication; N lies in SL(V), so equivariant Serre duality carries no determinant-character correction. The vanishing H¹B(t)=0 for t≤−2 and H⁰B(t)=0 for t≤0 suffices for the present spectral sequence. The stronger twist-one section vanishing is an upstream input to the multiplication theorem, not a new direct entry needed here. Neither twist-two section vanishing nor h¹B(2) is used.

## Exact complex, grading, and filtration

The complex Λ^iX⊗B(−i), placed in column −i, is the usual homogeneous-coordinate Koszul complex tensored with a bundle. It is exact on projective space because the coordinates have no common zero. More precisely, when one coordinate is a unit, wedging by the corresponding inverse-coordinate basis vector contracts this complex whose differential is contraction by the coordinate vector. Thus its bounded hypercohomology is zero.

For the stated column convention the differential has bidegree (r,1−r), not its negative. In row two, Λ^iX⊗H²B(−i)=Λ^iX⊗L_(5−i), precisely the internal-degree-five strand of the chain Koszul complex for L. Its homology in column −i is Tor_i(L,C)_5. There is no filtration ambiguity in that E₂ identification. Convergence to zero forces every E∞ graded piece to vanish; no cancellation between different filtration pieces is being assumed.

I also checked the same calculation in the cochain convention Λ^pV⊗B(p−5), p=0,…,5. The conversion uses Λ^pV≅Λ^(5−p)X⊗det(V). Since det(V) is trivial for N, this gives the same full-normalizer representations and sends p=2,3 to Tor_3,5 and Tor_2,5, respectively.

## Complete page and equivariance check

The extreme rows vanish: row zero has twists −5,…,0, and row four is their Serre-dual reflection, again involving only nonpositive H⁰ twists. Row one has only X⊗H¹B(−1)→H¹B(0). Its cokernel is zero and its kernel is the actual identity line in End(V). Conjugation by every normalizer element fixes the identity, so E₂^(−1,1) is the trivial N-module.

Row three has only Λ⁵X⊗H¹B(0)*→Λ⁴X⊗H¹B(−1)*. Exterior and Serre pairings identify this map with the transpose of row one's map, up to a nonzero sign. It is therefore injective, and its cokernel in column −4 is the dual of the identity line, again the trivial N-module. There is no hidden quotient-group character.

The endpoint bounds initially leave Tor_4,5, Tor_3,5, Tor_2,5, and Tor_1,5 in row two. The final proof independently excludes the outer two: (−4,2) has no incoming higher differential and zero outgoing targets (−2,1) and (−1,0); (−1,2) has no outgoing higher differential and zero incoming sources (−3,3) and (−4,4). All later sources or targets lie outside the page. Each therefore survives to the zero abutment and vanishes. Thus all four remaining possible E₂ entries in §4 are correctly identified, and no cohomology row or column has been omitted.

## Differential audit

Write A=(−4,3), P=(−3,2), Q=(−2,2), D=(−1,1).

- The only d₂ maps are A→Q and P→D.
- Q has zero d₂ target (0,1), and its possible incoming d₃ source (−5,4) is zero. For r≥4 its incoming source lies outside the columns or rows. Its d₃ target (1,0) and later targets are outside the complex. Hence coker(A→Q) survives and is zero.
- P has zero d₂ source (−5,3). Every later incoming source is outside the columns. Its d₃ target (0,0) is zero, and its later targets are outside the rows or columns. Hence ker(P→D) survives and is zero.

Consequently Q is a quotient of one trivial line and P a submodule of one trivial line. The dimension bound and the exact N-representation conclusion follow directly. The equality of their dimensions is consistent with, and already supplied by, the audited degree-ten resolution duality. No a, b, or d term enters these positions, since those parameters occur in different internal degrees.

After d₂, A and D become ker α and coker β. The only possible remaining differential is d₃ from A to D. No higher differential can touch either slot. It must therefore be an isomorphism. The proof correctly distinguishes the two necessary patterns and does not pretend that the residual d₃ has a fixed one-dimensional domain before its E₃ page is formed. It neither evaluates that differential nor asserts that both patterns are realized. No parity conclusion is required or used.

## Resolution and scope

The updated six free-module terms agree exactly with the previously audited shape after c=0. Substituting e∈{0,1} changes only the two degree-five middle coefficient spaces. The listed a and b bounds and conditional d≤30 agree with the imported relation proof and linear-strand addendum. Neither the ghost bound nor self-duality proves quadratic generation, excludes quartic relations, or proves an even pure resolution.

The final reviewed version includes the independent c=0 argument above and does not use the earlier shadow/orbit exclusion as an input. I re-read the complete final proof after the relative-reference, c=0, and contracting-homotopy wording changes and verified its exact fingerprint. All conclusions remain PASS.

This audit used static proof reads, abstract Koszul/Serre duality, and exact symbolic grading checks. No actual HM instance, multiplication matrix, source, cofactor, or physical obstruction was evaluated.
