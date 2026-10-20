# Independent indexing and pairing-sign audit

## Verdict

The theorem in `PROOF.md` is correct conditional on its explicitly imported, previously audited geometric inputs:

    e ∈ {0,1}.

When nonzero, both internal-degree-five middle Tor spaces are trivial normalizer representations. The argument also independently recovers Tor₁,₅=Tor₄,₅=0. The residual alternative is stated correctly: if e=0, a nonzero d₃ kills the two remaining scalar lines; if e=1, both scalar lines have already disappeared under d₂.

No indexing error, missing differential, or pairing-sign obstruction was found. In particular, symmetric trace duality does **not** make this residual d₃ alternating. Its induced form is symmetric, so duality does not rule out the one-dimensional nonzero d₃ and does not prove e=1.

Reviewed file:

    PROOF.md
    SHA-256: f56a6769c357f4bd39e6bf2b3ca5dafdeae03892388e67f20874dbb593e1d38f

This audit was written on 2026-10-20 UTC. It does not modify the reviewed proof.

## 1. Dependencies actually checked

The following mathematical dependencies were inspected:

- `../quintic-scalar-propagation/PROOF.md`, especially §8. Its actual H¹ multiplication is nonzero and identifies, up to scale, with the quotient of V*⊗V by the identity line. This is stronger than the statement that such a multiplication is allowed by representation theory.
- `../middle-module-relations/PROOF.md`, especially §5, for the self-dual degree bounds and necessary Betti shape. This allows Tor₁,₅ and Tor₄,₅, of dimension c, in addition to Tor₂,₅ and Tor₃,₅, of dimension e.
- `../middle-relation-dependency/PROOF.md`, especially §5, for the compatible earlier c=0 theorem. The final reviewed version independently proves c=0 and no longer requires that earlier theorem as an input.
- `../middle-relation-dependency/LINEAR-STRAND-ADDENDUM.md`, for the imported upper bound d≤30 when a=15. This is the precise source for that additional constraint in §6 of the reviewed proof.
- `../apolar-middle-module/PROOF.md`, for the symmetry convention on the actual middle-cohomology pairing.

The first two input-file hashes at inspection were:

    quintic-scalar-propagation/PROOF.md:
    35a93234687c5d79533f8fc55a7589b3cae6546e683dd3e4c192adbbc3d89c4c

    middle-relation-dependency/PROOF.md:
    3924f27ef5c7573352acc1f0f39858f01aa188b151c29cf3ba83b4eb0d0f6bd0

This is an audit of the new deduction, not a fresh proof of every older HM input.

## 2. The complex, exactness, and Tor indexing

With X=H⁰O(1), the homological-coordinate Koszul complex, written cohomologically, has

    K^(−i)=Λ^iX⊗B(−i),     i=0,…,5.

The homogeneous coordinates have no common zero on P⁴, so their sheaf Koszul complex is locally contractible. Tensoring with the locally free B preserves exactness. The hypercohomology is therefore zero.

For the column filtration,

    E₁^(p,q)=H^q(K^p),
    d_r:(p,q)→(p+r,q−r+1).

The boundedness suffices for convergence. The two cited Stacks Project references were opened and checked: [Lemma 13.21.3](https://stacks.math.columbia.edu/tag/015J) gives the hypercohomology E₁ page and convergence; [Section 12.25](https://stacks.math.columbia.edu/tag/012X), particularly Lemmas 12.25.1 and 12.25.3, gives the double-complex page convention and bounded convergence. They support the general machinery, not the HM-specific vanishings.

Since L_d=H²B(d−5), the q=2 row at column −i is

    Λ^iX⊗H²B(−i)=Λ^iX⊗L_(5−i).

This is precisely the internal-degree-five Koszul strand of L, with no omitted grading shift. Thus

    E₂^(−i,2)=Tor_i^S(L,C)₅.

## 3. Every row of E₂

For q=0, every twist −i is nonpositive, so the row is zero.

For q=4, Serre duality gives H⁴B(−i)=H⁰B(i−5)*. Again every indicated twist is nonpositive, so this row is zero.

For q=1, only columns −1 and 0 remain. The differential is the actual surjection

    X⊗V → sl(V),

whose kernel is C·id. Hence this row has just E₂^(−1,1)=C, with trivial N-action.

For q=3, Serre duality leaves columns −5 and −4. The resulting differential is dual to the q=1 differential, with the harmless exterior sign. The determinant factor is genuinely trivial because N⊂SL(V) and X=V*. Hence the unique q=3 survivor is E₂^(−4,3)=C, also with trivial N-action.

The imported Betti shape initially allows middle-row columns −4,−3,−2,−1. At (−1,2), all outgoing higher arrows leave the column range; the only incoming sources with permissible rows are (−3,3) and (−4,4), both zero. Therefore Tor₁,₅ would survive to E∞ and is zero. At (−4,2), all incoming higher arrows leave the column range; the only outgoing targets with permissible rows are (−2,1) and (−1,0), both zero. Therefore Tor₄,₅ is zero as well.

This independent c=0 argument is valid. It leaves only E₂^(−3,2)=Tor₃,₅ and E₂^(−2,2)=Tor₂,₅ in q=2. Therefore the four-entry page in §4 is exhaustive.

## 4. Arrow audit and the bound

Write A=(−4,3), P=(−3,2), Q=(−2,2), D=(−1,1).

The only d₂ arrows between nonzero terms are A→Q and P→D.

At Q, the d₂ target (0,1) is zero. A later incoming arrow would have source (−2−r,r+1): for r=3 the source is (−5,4), which is zero, and for larger r it is outside the range. Every later outgoing arrow has positive column. Consequently coker(A→Q) survives to E∞ and must vanish.

At P, the d₂ source (−5,3) is zero. Every later incoming arrow has column below −5. The d₃ target is (0,0), which is zero, and later targets leave the allowed range. Consequently ker(P→D) survives to E∞ and must vanish.

Thus A→Q is surjective and P→D is injective. Since A and D are trivial one-dimensional representations, e≤1 and both Tor spaces are trivial when nonzero.

On E₃ the residual terms are ker(A→Q) at (−4,3) and coker(P→D) at (−1,1). Both have dimension 1−e. Their only possible remaining arrow is d₃ from the former to the latter, necessarily an isomorphism. No higher differential is missing.

## 5. Why the residual d₃ is not forced to be alternating

The trace pairing on B is symmetric. Combine it with exterior multiplication

    Λ^iX⊗Λ^(5−i)X → det X

and Serre trace on H⁴O(−5). This pairs bidegrees (p,q) and (−5−p,4−q). The complementary total degrees therefore sum to −1.

For a consistent totalization, the product of a term of bidegree (p,q) with one of bidegree (p′,q′) includes the sign (−1)^(q p′). Exterior interchange contributes (−1)^(p p′), and cohomological interchange contributes (−1)^(q q′). Together they give the usual total-degree symmetry

    ⟨x,y⟩ = (−1)^(|x||y|) ⟨y,x⟩.

The pairing is compatible with the total differential:

    ⟨dx,y⟩ + (−1)^|x| ⟨x,dy⟩ = 0.

These identities pass to the paired spectral-sequence pages. Both A and P have total degree −1, whereas both Q and D have total degree zero. For two degree −1 source classes x,y, differential compatibility and interchange give

    ⟨d_r x,y⟩ = ⟨x,d_r y⟩ = ⟨d_r y,x⟩.

Thus the bilinear form induced by a middle differential is symmetric. In particular, on the residual A line, the form

    (x,y) ↦ ⟨d₃x,y⟩

is symmetric, not alternating. A symmetric form on a one-dimensional complex vector space can be nonzero and nonsingular. There is no parity contradiction when e=0.

Equivalently, the paired d₂ maps A→Q and P→D are transposes after compatible identifications; the rank-one e=1 pattern also respects the same duality.

As a purely formal check, both patterns admit acyclic filtered paired complexes: for e=0 use a scalar isomorphism from A to D of filtration displacement three; for e=1 use the two transpose scalar isomorphisms A→Q and P→D of displacement two. These are checks of spectral-sequence and pairing consistency, not constructions of HM bundles or a realization theorem.

## 6. Rank-three geometry and scope

The bundle's rank-three orthogonal structure supplies the symmetric trace pairing used above, but rank three does not change this totalization sign. The reviewed proof does not establish an additional geometric identity that forces either of the two d₂ maps to be nonzero, or forces the residual d₃ to vanish or be nonzero.

Accordingly, the valid conclusion here is e∈{0,1}, not a selected value. This audit does not assert that the full HM geometry permits both values. It asserts that the displayed page, convergence, representation theory, and symmetric self-duality do not choose between them.

The proof correctly avoids treating d₃ as one fixed scalar on the original E₂ lines: its domain and codomain are the residual E₃ spaces and are both zero when e=1.

The audit used proof-file reads, the cited general spectral-sequence sources, abstract sign and degree calculations, and hashes. No selected HM, source, cofactor, catalecticant, or obstruction instance was evaluated.
