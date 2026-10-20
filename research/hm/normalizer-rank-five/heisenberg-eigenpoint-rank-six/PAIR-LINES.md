# Every point of the sixty Heisenberg eigenpair lines has residual rank at least five

Retain the assumptions and theorem of PROOF.md. Define Z4={ [u]∈P(V):rank Q_u≤4 }. Then Z4 is disjoint from every line joining two eigenpoints belonging to the same Heisenberg axis. There are sixty distinct such lines: six axes and ten unordered pairs per axis.

## 1. A determinantal bound on any line through a canonical eigenpoint

Let U⊂V have dimension two and let L=P(U). The universal binary argument in ../order-three-rank-point-bound/PROOF.md, Section 1, gives a fixed two-dimensional subspace H_U⊂J such that

    b_u(Sym²U)=H_U   for all [u]∈L,

where b_u(xy)=f(x,u,y). This uses outer symmetry, cyclic zero, and repeated-input injectivity only. Quotienting source and target gives the linear matrix pencil

    B_U: O_L(−1)⊗(Sym²V/Sym²U) → (J/H_U)⊗O_L,
    rank B_U(u)=rank b_u−2=rank Q_u+2.

The last equality uses dim R_u=4, supplied by repeated-input injectivity.

Suppose L contains a canonical Heisenberg eigenpoint p. The theorem gives rank Q_p≥6, hence rank B_U(p)≥8. Some eight-by-eight minor d of this pencil is therefore a nonzero homogeneous polynomial of degree eight on L≅P1.

At q∈Z4∩L, rank B_U(q)≤6. Every eight-minor vanishes to order at least two there. Indeed, over the local DVR at q one can split off an invertible rank-r block, r≤6, leaving a matrix all of whose entries are in the maximal ideal. Every eight-minor then lies in the (8−r)th power of that ideal. Thus

    2·|Z4,red∩L|≤8,
    |Z4,red∩L|≤4.

In particular this intersection is finite; no independent global finiteness theorem for Z4 is required.

## 2. The axis clock excludes all intersection points

Take the coordinate-axis pair line L_ij=P(span(e_i,e_j)), i≠j. The projective clock Z acts on it by

    [a:b]↦[ζ^i a:ζ^j b].

Its only fixed points are the endpoints [e_i],[e_j]. Every other orbit has exactly five points, since ζ^(j−i) is primitive of order five. Both endpoints have residual rank at least six and are outside Z4. The intersection Z4∩L_ij is clock-invariant by equivariance, has at most four distinct points by Section 1, and contains no endpoint. Hence it is empty.

Normalizer transport proves the same statement for each of the six axes. Equivalently, every point on their pair lines satisfies rank Q_u≥5. The larger dihedral stabilizer of a pair line may also be used, but is unnecessary: its C5 subgroup already gives the contradiction.

## 3. Count of the lines

Each of the six axes has five independent eigenvectors, so its ten pair lines are distinct. Pair lines from different axes cannot coincide. To see this, choose one axis as the diagonal clock. A noncentral Heisenberg element on any different axis has form X^a Z^b up to a scalar, with a≠0. Its eigenvector recurrence around the five-cycle shows that every coordinate of any nonzero eigenvector is nonzero: a zero coordinate would force all five to vanish. Thus none of the other axis's eigenpoints can lie on any coordinate pair line, whose vectors have at most two nonzero coordinates. Coincidence of pair lines would put both of the other pair's endpoints on that coordinate line, a contradiction.

There are therefore exactly 6·10=60 distinct eigenpair lines, all disjoint from Z4. This is a pointwise exclusion of rank at most four on these lines, stronger than exclusion of line components alone. It is not a rank-at-least-six assertion away from their endpoints, and it makes no claim about points outside the union of these sixty lines.

## Audit

The consequence was independently checked from the proposed eight-minor argument:

- The binary constant-image quotient removes exactly two image dimensions at every point; it is a global linear pencil, so an eight-minor has degree eight.
- At an endpoint the main theorem gives rank b≥10 and quotient rank≥8, ensuring that a chosen eight-minor is genuinely nonzero.
- At a Z4 point the quotient rank is at most six, forcing multiplicity at least two, including when the actual rank is smaller.
- The divisor bound counts distinct points and needs no assumed reducedness or global finiteness.
- The clock has no nonendpoint shorter orbits, and both endpoints are already excluded. This proves emptiness without needing a reflection or its lift normalization.
- The count sixty uses full coordinate support of eigenvectors for a different Heisenberg axis and is independent of any source-operation evaluation.

Only the main theorem and the imported universal binary identity are used. No actual operation values, coefficients, or rank matrices are evaluated.
