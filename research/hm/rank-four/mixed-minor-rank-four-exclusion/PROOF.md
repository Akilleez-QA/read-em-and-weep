# Mixed decic and maximal minors exclude rank-four curves

## Result

Under exactly the established linear-matrix, generic-rank-ten, equivariance, and decic-closure hypotheses used for the existing rank-four curve bounds, the reduced rank-at-most-four curve support Γ4 is empty. Thus Z4 is finite as a support. This does not assert that Z4 is empty, nor control its finite scheme structure.

The new geometric bound is deg Γ4 ≤27. Combined with the audited dichotomy Γ4 empty or degree100, it excludes the nonempty case. The argument uses no component classification, source tensor evaluation, or instance computation.

## Imported inputs

From ../rank-one-middle-curve-exclusion/PROOF.md and ../rank-three-curve-constraints/PROOF.md:

- There is a linear 20-by-15 matrix b on P4, with rank b=4+rank Q at every point, and generic rank14.
- Let Zj denote the reduced support {rank Q≤j}. The span Lk of all k-by-k minors of b is a linear system of degree k with base support Z_(k−5).
- dim Z9≤2, proved in ../quintic-normalizer-exclusion/COROLLARY.md, Section2, and audited in COROLLARY-AUDIT.md there; the additional established decic-closure input gives dim Z5≤1.

From ../rank-four-degree-hundred-lower-bound/PROOF.md and its independent audit, Γ4 is either empty or has reduced degree100. Only that implication is needed for the final exclusion.

## 1. A complete intersection of degrees (10,14,14)

The decic system L10 has base support Z5 of dimension at most one. The maximal-minor system L14 has base support Z9 of dimension at most two.

Choose f in L10 which does not vanish identically on any two-dimensional irreducible component of Z9. This is possible: none of these components lies in the base support Z5, so each condition to be avoided is a proper linear subspace of L10. There are finitely many components, and the field is infinite. Also require f nonzero. It follows that

    dim(V(f) ∩ Z9) ≤1.

Choose g in L14 avoiding every irreducible component of the hypersurface V(f). Those components have dimension three, so none is in Z9. Thus f,g is a regular sequence in the homogeneous polynomial ring. Their intersection is a pure surface, by the Cohen–Macaulay and unmixed properties of a complete intersection.

No surface component of V(f,g) lies in Z9: such a component would lie in V(f)∩Z9, whose dimension is at most one. Consequently choose h in L14 avoiding all surface components of V(f,g). The quotient by f,g is Cohen–Macaulay and has no embedded associated primes, so h is a nonzerodivisor. Thus

    W=V(f,g,h)

is a pure complete-intersection curve of degree

    10·14·14=1960.

This is the key improvement over three decics. A system whose base support is a surface can be used for the last two equations after a decic has cut that base support down to dimension one. It is unnecessary for each individual system to have curve-dimensional base support.

## 2. Orders along a rank-four curve

Let C be an integral curve component of Z4, with generic point η. The regular local ring R=O_(P4,η) has dimension three; let m be its maximal ideal. Write s=rank(b mod m)≤8. Splitting an invertible s-by-s block reduces b over R to diag(I_s,M), with all entries of M in m (and possibly a zero column). Cauchy–Binet and invertible row/column operations preserve all determinantal ideals. Hence

    I10(b)R ⊂ m^(10−s) ⊂ m²,
    I14(b)R ⊂ m^(14−s) ⊂ m⁶.

In particular f∈m² and g,h∈m⁶. Since C is contained in the pure curve W, it is a component, and q=(f,g,h)R is an m-primary parameter ideal. Its colength is W's generic multiplicity along C.

## 3. Elementary mixed-order multiplicity bound

Set q'=(f³,g,h)R. All three generators belong to m⁶. They form a parameter regular sequence. For any parameter ideal a in a three-dimensional regular local ring, the regular-sequence associated graded formula gives

    length(R/a^n)=length(R/a) binom(n+2,3).

Since (q')^n⊂m^(6n), while length(R/m^(6n))=binom(6n+2,3), comparison of leading cubic coefficients gives

    length(R/q')≥6³=216.

On the other hand,

    length(R/(f³,g,h))=3 length(R/(f,g,h)).

Indeed permute the regular sequence and pass to the one-dimensional Cohen–Macaulay ring A=R/(g,h). The image of f is a nonzerodivisor and the filtration of A/(f³) by powers of f has three successive quotients isomorphic to A/(f). Therefore

    length(R/q)≥216/3=72.

This proof does not require any transverse intersections, nonsingularity of C, assumptions on tangent cones, or generality of a rank-stratum scheme. It is valid also if s<8; then the orders, and potentially the bound, only increase.

## 4. Degree consequence and exclusion

Every component C of Γ4 contributes at least72 deg C to the effective fundamental cycle of W. All other components contribute nonnegative degree. Thus

    72 deg Γ4 ≤1960,
    deg Γ4 ≤27.

The independently audited nonempty possibility deg Γ4=100 is impossible. Hence Γ4=0. Because dim Z4≤dim Z5≤1, the absence of curve components means dim Z4≤0, so Z4 is finite as a support (possibly empty).

## 5. A less sharp independent numerical variant

Replacing the two maximal-minor members by degree-eleven members gives a complete intersection of degrees(10,11,11): the same avoidance argument uses Z6⊂Z9. At a rank-four generic point the orders are at least(2,3,3). Replacing the generators by (f³,g²,h²), all of order at least6, yields

    12 length(R/(f,g,h))≥216,
    length(R/(f,g,h))≥18.

Therefore deg Γ4≤floor(1210/18)=67, already strictly below100. This variant uses only dim Z6≤2 in place of the maximal-minor surface bound, though that follows from the imported Z9 bound.

## Scope and limits

The argument depends essentially on dim Z5≤1: without it, the decic system could vanish identically on a surface component of Z9, and Step1 could fail. It also needs dim Z9≤2 and the genuinely linear matrix b. These are imported conditional hypotheses, not newly established here.

No claim about emptiness of the finite rank-four locus, its length, or its nonreduced structure follows. No actual source tensor, coefficient, input, operation value, rank instance, jet, or residue was evaluated. Only local mathematical proof files were read or written;
