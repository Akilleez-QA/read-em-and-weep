# Independent audit: the finite rank-four support is empty

## Verdict and dependencies

The further degree-(9,10,14,14) construction is valid and upgrades the audited curve exclusion to Z4=∅, conditional on the same imported hypotheses plus the established noncanonical point-orbit gap and canonical eigenpoint rank bound. Thus the residual rank is everywhere at least five.

Use the already audited conclusion dim Z4≤0, dim Z5≤1, dim Z9≤2, the linear matrix b with rank b=4+rank Q, and generic rank b=14. Let Lk denote its degree-k minor system; its base support is Z_(k−5).

For the finite-group endpoint, ../normalizer-refined-point-gap/PROOF.md proves that every point outside the canonical thirty-point orbit has normalizer orbit size at least250; this statement is also recalled explicitly in ../normalizer-250-simple-defect/PROOF.md. By ../heisenberg-eigenpoint-rank-six/PROOF.md, canonical points have rank Q≥6. Its extra hypothesis that the span of operation values has dimension at least20 is explicitly satisfied by the standing irreducible target representation and must remain among the imported hypotheses.

## The four global equations

1. Since Bs(L9)=Z4 is finite, choose f∈L9 nonzero and not identically zero on any curve component of Z5 or surface component of Z9. These are finitely many proper linear avoidance conditions. Then V(f)∩Z5 is finite and V(f)∩Z9 has dimension at most one.

2. Choose g∈L10 avoiding both every hypersurface component of V(f) and every curve component of V(f)∩Z9. The first type has dimension three, so cannot lie in Bs(L10)=Z5. A curve of the second type cannot lie in Z5 because V(f)∩Z5 is finite. All avoidance conditions are therefore proper. The pair f,g is regular, its projective zero locus is a pure surface, and V(f,g)∩Z9 is finite.

3. Choose h∈L14 avoiding every surface component of V(f,g). None lies in Z9, by the preceding finite-intersection conclusion. The triple f,g,h is regular and its zero locus is a pure curve.

4. Choose j∈L14 avoiding every curve component of V(f,g,h). Such a curve is contained in V(f,g), hence cannot lie in Z9. The four equations form a homogeneous regular sequence. Their projective common zero scheme W is zero-dimensional of length

    9·10·14·14=17640.

All these systems vanish on Z4, so Z4 is contained in W. The use of component avoidance in the homogeneous polynomial ring is justified at every stage by the Cohen–Macaulay, unmixed property of the preceding complete intersection. No embedded component invalidates the construction.

## Local multiplicity at every rank-four point

At p∈Z4, R=O_(P4,p) is regular local of dimension four. Modulo its maximal ideal m, the matrix b has rank s≤8. Splitting an invertible block gives orders at least

    f∈m, g∈m², h∈m⁶, j∈m⁶.

Because W is zero-dimensional, q=(f,g,h,j) is m-primary, and its colength is length(O_(W,p)). The parameter ideal

    q'=(f⁶,g³,h,j)

is contained in m⁶. The regular-sequence associated graded formula in dimension four and regularity of R give

    length(R/(q')^n)=length(R/q') binom(n+3,4),
    length(R/m^(6n))=binom(6n+3,4).

The containment (q')^n⊂m^(6n) implies length(R/q')≥6⁴=1296. Successive power filtrations for the regular parameter sequence give

    length(R/q')=6·3 length(R/q)=18 length(R/q).

Thus length(O_(W,p))≥72 at every p∈Z4. All points are closed complex points, so summing the local lengths yields

    72 |Z4,red|≤17640,
    |Z4,red|≤245.

No reducedness of W or Z4 is assumed.

## Orbit contradiction

The finite reduced support Z4 is N-invariant. It contains no point of the canonical thirty-point orbit because canonical residual ranks are at least six. If nonempty, it would contain a noncanonical orbit, hence at least250 distinct points, contrary to the bound245. Therefore Z4 is empty and rank Q≥5 everywhere.

This argument does not assert rank Q≥6: a separate exclusion would be needed for rank exactly five.
