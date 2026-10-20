# No normalizer-invariant integral curves through degree fifty-five

## Result and dependencies

In the complex projective Schrödinger-normalizer setting, there is no N-stable integral curve C in P⁴ of degree at most 55. Consequently, every nonempty N-invariant reduced curve without line or conic components has degree at least 60. Under the previously proved rank-four hypotheses,

    Γ₄ is empty, or 60 ≤ deg Γ₄ ≤ 125 and 5 divides deg Γ₄.

The group notation is A ≅ (Z/5)² normal in N, with N/A ≅ SL₂(F₅) acting faithfully and standardly on A. This text imports the faithful N-action genus lower bound 326 from ../rank-four-degree-fifty-equality/ADDENDUM.md, Section 1, itself based on ../binary-group-genus-thirteen/PROOF.md. It imports the representation identity Sym²V = A₂ ⊗ Sym²W′ from the established HM representation conventions (recorded with the primary-source identification in ../equivariant-massey-multiplicity/PROOF.md, Section 1, and ../lower-weight-image-symmetry/PROOF.md, Section 1; also used in ../cubic-massey-module-reduction/PROOF.md, Section 4). Here A₂ denotes the five-dimensional Heisenberg representation called A in that representation identity, not the projective abelian subgroup A. The three-dimensional multiplicity representation Sym²W′ is irreducible for SL₂(F₅).

The geometric tools are Castelnuovo's bound for a birational linear series and the uniform-position theorem for a general hyperplane section of an integral complex projective curve. The Hilbert-function inequality needed after that theorem is proved below. No arithmetically Cohen–Macaulay hypothesis is imposed.

## 1. Faithfulness and the complete linear series

Let C be N-stable and integral, let ν:X→C be its smooth normalization, and put L=ν*O_C(1), of degree d=deg C. Every A-stable integral curve spans P⁴, since its vector span is stable under the irreducible Schrödinger representation of H₅. A finite-order projective transformation fixing C pointwise has C contained in the union of its projectivized eigenspaces. Integrality places C in one eigenspace, and nondegeneracy makes that eigenspace the whole ambient space. Thus the projective transformation is the identity. It follows that N acts faithfully on X. The imported genus theorem gives

    g(X) ≥ 326.

The standard H₅-linearization of O_P⁴(1) restricts to C and pulls back, functorially under normalization, to an H₅-linearization of L. The central μ₅ acts trivially on X but on L by the nontrivial scalar character inherited from O(1). It therefore acts on H⁰(X,L) by that same nontrivial character (up to the harmless dual convention). Every irreducible complex H₅-representation with a prescribed nontrivial central character has dimension five. Semisimplicity gives

    h⁰(X,L) is a positive multiple of five.

The five ambient linear sections are independent on X and basepoint-free. If h⁰(X,L)≥10, choose a ten-dimensional subspace containing them. Its map X→P⁹ is basepoint-free and nondegenerate. Projection onto the original five sections is ν followed by C⊂P⁴, so the P⁹ map is birational onto its image. Its image consequently has degree d. Castelnuovo's bound gives, for d≤55,

    g(X) ≤ π(55,9) = 8·6·5/2 + 6·6 = 156,

where 55−1=8·6+6. (Nondegeneracy itself forces d≥9 if this map exists.) This contradicts g(X)≥326. Therefore

    h⁰(X,L)=5.

The injections of ambient sections into H⁰(C,O_C(1)) and then into H⁰(X,L) force h⁰(C,O_C(1))=5. Thus C is linearly normal and H¹(P⁴,I_C(1))=0.

## 2. No quadrics and the hyperplane section

The representation Sym²V is irreducible for the linear normalizer: its restriction to H₅ is the isotypic module A₂⊗C³, and its multiplicity module Sym²W′ is irreducible under the quotient. The isotypic tensor-Hom equivalence identifies normalizer-stable subspaces with invariant multiplicity subspaces. The dual Sym²V* is therefore irreducible as well.

The quadrics vanishing on C form an invariant subspace I_C(2) of Sym²V*. They cannot be all quadrics, since all quadrics have empty common projective zero locus and C is nonempty. Hence

    H⁰(P⁴,I_C(2))=0.

Let H≅P³ be a general hyperplane and Γ=C∩H. In characteristic zero, Γ consists of d distinct points in uniform position. Write h(n) for its homogeneous coordinate Hilbert function. The hyperplane ideal sequence

    0 → I_C(n−1) → I_C(n) → I_{Γ,H}(n) → 0

at n=2, together with H⁰(I_C(2))=0 and H¹(I_C(1))=0, gives H⁰(I_{Γ,H}(2))=0. Thus h(2)=10. Likewise h(1)=4: at n=1 use nondegeneracy and H¹(I_C)=0, the latter following from H⁰(O_C)=C and the ideal sequence. In particular d≥10.

## 3. The uniform-position growth inequality

For points in uniform position, every subset of cardinality s imposes rank min(s,h(n)) on forms of degree n. Fix nonnegative n,m, and put a=h(n), b=h(m). Set s=min(d,a+b−1), and choose any subset T⊂Γ of size s. For each point p∈T, partition T\{p} into disjoint sets U and W with |U|≤a−1 and |W|≤b−1.

Uniform position implies that the evaluation map of degree-n forms onto U∪{p} is surjective. Choose such a form vanishing on U and nonzero at p. Similarly choose a degree-m form vanishing on W and nonzero at p. Their product vanishes at all points of T except p. Doing this for every p proves surjectivity of degree-(n+m) evaluation on T. Consequently

    h(n+m) ≥ min(d,h(n)+h(m)−1).

Starting with h(1)=4 and h(2)=10 and iterating with m=2 gives

    h(2k) ≥ min(d,9k+1)         (k≥1),
    h(2k+1) ≥ min(d,9k+4)       (k≥0).

## 4. The genus inequality does not require ACM

Let R be the homogeneous coordinate ring of C and let ℓ define H. Since C is integral and is not contained in H, ℓ is a nonzerodivisor on R. Define q(n)=dim_C(R/ℓR)_n. The exact graded multiplication sequence gives

    q(n)=dim R_n−dim R_{n−1}.

The saturated coordinate ring of Γ is a quotient of R/ℓR. Therefore q(n)≥h(n) for every n, with equality for all sufficiently large n. For large n, q(n)=d, and dim R_n=dn+1−p_a(C). Since dim R_0=1, telescoping yields

    p_a(C)=Σ_{n≥1}(d−q(n)) ≤ Σ_{n≥1}(d−h(n)).

This remains true when some q(n)>d: individual terms in the first sum may be negative, and the termwise inequality still has the stated direction. All sums are finite. Finally, normalization gives g(X)≤p_a(C).

The lower bounds in Section 3 give the monotone-in-d upper bound

    p_a(C) ≤ B(d)
           := Σ_{k≥0} max(0,d−9k−4)
              + Σ_{k≥1} max(0,d−9k−1).

For d≤55,

    B(d) ≤ B(55)
         = (51+42+33+24+15+6) + (45+36+27+18+9)
         = 171+135 = 306.

Thus 326≤g(X)≤p_a(C)≤306, a contradiction. This excludes every N-stable integral curve of degree at most 55. As a check on the former equality case, B(50)=251. In fact B(56)=318<326 and π(56,9)=162<326, so the same integral-curve argument excludes degree 56 as well. The bound through 55 is the relevant threshold after five-divisibility.

## 5. Reduced invariant curves and Γ₄

Let D be a nonempty N-invariant reduced curve of degree at most 55, with no line or conic components. A component's A-orbit has size 1,5, or25.

An orbit of size25 contributes degree at least75. If the A-orbit has size5, its stabilizer is an order-five subgroup of A. Conjugation by N carries this stabilizer through all six such subgroups. The corresponding A-orbits are disjoint, so its N-orbit contains at least30 components and contributes degree at least90. Both are impossible.

Hence every component is A-stable, and its degree is a positive multiple of five by the Heisenberg Hilbert-polynomial divisibility theorem. The action on components factors through the perfect group SL₂(F₅). A nontrivial orbit has size at least five, since a perfect subgroup of S_m for m≤4 is trivial. If such an orbit has size m and common component degree e, then me≤55 forces e=5 or10. But ../rank-four-degree-fifty-equality/PROOF.md, Section 2, proves that the orbit of any A-stable component of degree at most ten has at least20 components, and hence degree at least100. Thus all components would have to be N-stable. Section 4 excludes each of them, a final contradiction.

Therefore deg D>55. Its degree is divisible by five by the same Hilbert-polynomial argument, so deg D≥60. For Γ₄, import N-invariance, the no-line and no-conic component theorems, and deg Γ₄≤125 from the existing rank-four arguments. This proves the stated empty-or-degree-at-least-60 alternative.

## Evidence boundary

This is a reduced-support theorem. It asserts neither existence nor emptiness of Γ₄, and does not determine multiplicities, isolated points, or a scheme-theoretic length. No actual source tensor, coefficient, selected source input, problem-specific operation matrix, rank, point, jet, residual, or Massey value has been evaluated. No actual source-instance evaluation is claimed.
