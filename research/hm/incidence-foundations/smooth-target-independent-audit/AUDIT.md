# Independent audit of the smooth-target exclusion

## Verdict

The proposed exclusion is valid over C. In particular, if five independent quadrics in four variables have generic Jacobian rank four and admit a nondegenerate quadratic relation, their Jacobian maximal-minor gcd is a double linear form. It cannot be an integral quadric. This removes the rank-five target relation from the quadratic-gradient-syzygy reduction.

This audit read the full proofs in `quadratic-gradient-syzygy/PROOF.md`, `nonplanar-factor-degree-bounds/PROOF.md`, `nonlinear-curve-factor-exclusion/PROOF.md`, and `one-planar-factor-exclusion/PROOF.md`. The latter two pure linear-system lemmas, and the bounded-rank plane classification invoked by the nonlinear-curve proof, are dependencies. There is no use of the conclusion that both nonplanar factor surfaces are impossible.

## 1. Exact ternary relation calculation

Let U have dimension three. Identify the six coordinates of Sym²U with the entries of a symmetric matrix

    X = [[A,F,E],[F,B,D],[E,D,C]].

The quadratic ideal of the Veronese image [u] -> [u²] is six-dimensional. Indeed the multiplication map Sym²(Sym²U) -> Sym⁴U is surjective, with dimensions 21 and 15. The six entries of adj(X) are independent quadratic equations vanishing on rank-one matrices, so they form its kernel.

Consequently every quadratic Veronese relation is tr(H adj(X)) for a symmetric 3 by 3 matrix H (off-diagonal coefficient normalizations are immaterial). Under X -> P X Pᵗ, adj(X) transforms by det(P)² P^(-ᵗ) adj(X) P^(-1). Thus the corresponding action on H is congruence up to a nonzero scalar. Over C, H can be diagonalized with precisely r nonzero diagonal entries, r=1,2,3.

For H=diag(a,b,c), the relation is

    a(BC-D²) + b(AC-E²) + c(AB-F²).

Its matrix splits into the A,B,C block and three one-dimensional square blocks. When exactly one of a,b,c is nonzero, the first block has rank two and the square block rank one, giving rank three. When exactly two are nonzero, those ranks are two and two, giving rank four. When all three are nonzero, the first block has nonzero determinant proportional to abc, so the total rank is six. The possible nonzero relation ranks are therefore exactly 3, 4, 6, never 5.

## 2. Every hyperplane supplies a product

Let V be the four-dimensional space of linear forms and W ⊂ Sym²V the span of the five quadrics. Suppose W admits a relation of rank five. For any nonzero l∈V, consider restriction modulo l:

    W -> Sym²(V/Cl).

If injective, its symmetric square sends the rank-five relation to a quadratic relation of the ternary Veronese with the same rank: extending a basis of the five-dimensional image to the ambient six-dimensional space merely adds one zero row and column. Section 1 makes this impossible. Thus the restriction has a nonzero kernel for every l. Since the full restriction kernel in Sym²V is lV, we have

    W ∩ lV ≠ 0  for every nonzero l.

The original Jacobian's generic rank four implies full support of W: otherwise all five quadrics depend on at most three independent linear forms, and their differentials lie in that fixed at-most-three-dimensional space.

## 3. Precisely what is borrowed from the factor-incidence proof

Form the annihilator evaluation matrix of W, treating V as the factor space. For a∈V, its vector kernel is

    N_a = {b∈V : ab∈W}.

Section 2 implies generic kernel dimension at least one, so generic matrix rank at most three. The pure nonlinear-curve lemma gives the following observation independently of any preselected surface: no nonlinear integral curve C can have dim N_a≥2 generically along C. To apply that lemma, select a rational rank-two subbundle on a good open of C and projectivize it. The resulting ordered-factor family is a surface, generically rank two, and its product image is a surface because factorization has finite fibers. Its first factor image is C, contradicting that lemma.

This rules out ambient generic rank at most two. At generic rank three there is a rational kernel map f:P(V) --> P(V), with image D. Symmetry gives every inverse fiber over b inside P(N_b), hence dim N_b≥4-dim D at general b∈D.

- If dim D=2, select a nonlinear curve in the good open of D and apply the observation.
- If dim D=1, the observation forces D to be a projective line P(L). The argument of Section 2 of `nonplanar-factor-degree-bounds/PROOF.md` then gives W=Sym²L+Lv for one v, contradicting full support. This argument uses only generic uniqueness of the kernel and dim W=5.
- If dim D=3, symmetry and uniqueness make f a birational involution. A general source plane has surface image, and the pure plane/nonplanar lemma forces that image to be a plane. The degree-one argument in Section 3 of the same proof then makes f an ambient projectivity. The span of aT(a) for invertible T has dimension at least six, contradicting dim W=5.
- If dim D=0, let D={[e]}. Closure of ae∈W for general a gives eV⊂W. Thus W=eV+Cq.

Crucially, the original proof's subsequent exclusion of this last constant case used its specified both-surface family X. That exclusion is not imported here. The constant case is retained, and is the only survivor. This is the only change needed to reuse Sections 1–3; no circularity results.

For completeness, the degree-one step does not presume regularity of the birational map. The induced map on general planes is rational and generically injective, hence dominant on the dual P³. A general target plane has plane strict inverse transform. Exceptional divisors are among the finitely many components of the complement of an isomorphism open, and a general target hyperplane contains none of their images. The primitive homogeneous coordinate system has no fixed divisor. Therefore its generic degree-d linear combination defines just that reduced plane, and d=1.

## 4. Exact Jacobian gcd in the survivor

Choose coordinates e,x,y,z and use eV to remove every term divisible by e from q. Thus

    W = span(e², ex, ey, ez, q(x,y,z)),    q ≠ 0.

Constant changes of basis of W preserve the maximal-minor ideal up to invertible recombination, and changes of source coordinates preserve its gcd up to the same coordinate substitution and a nonzero scalar. We may therefore calculate in this normal form.

The Jacobian is

    [2e, 0, 0, 0]
    [ x, e, 0, 0]
    [ y, 0, e, 0]
    [ z, 0, 0, e]
    [ 0, q_x, q_y, q_z].

Up to signs and nonzero constants its five maximal minors are

    e²q, e³q_x, e³q_y, e³q_z, e⁴.

The first formula uses xq_x+yq_y+zq_z=2q. Their gcd is exactly e², because the gcd divides e⁴ while e does not divide the nonzero ternary q. No irreducibility or nonsingularity assumption on q is needed for this gcd calculation.

The unique image relation in these coordinates is Y0 Y4 - q(Y1,Y2,Y3)=0; its rank is 2+rank(q). Thus the original rank-five relation additionally forces q to have rank three. This extra fact is consistent but unnecessary for the gcd contradiction.

## 5. Scope of the resulting exclusion

In the original incidence setting, the cofactor gradient syzygy produces a symmetric relation of rank at least three. Rank three was excluded by its fixed-line kernel image. Rank four produces an ambient linear involution and is excluded only after using the separate dense compatibility and square-avoidance hypothesis. Rank five is excluded here purely from the integral-quadric gcd.

Therefore the combination excludes both-nonplanar compatible rank-two factor surfaces with a full-support five-dimensional residual kernel, under the stated compatibility and square-avoidance hypotheses. It does not by itself settle moving-middle components having only curve fibers or any broader global theorem.

Only local proof reading and small symbolic reasoning were used.
