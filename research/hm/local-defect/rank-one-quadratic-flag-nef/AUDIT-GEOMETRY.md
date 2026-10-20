> Publication scope: preserved mathematical proof/audit. Historical statements that rank eight remains open are superseded only after the final assembly and all its prerequisites. No source-instance evaluation or formal verification is claimed here.

# Independent geometry audit

Status: PASS for the frozen proof, Sections 1–7, including the generic-length refinement and component count.

## Bundle construction and global recovery

The repeated-input map is the subbundle injection L²⊗(V/L)→J. Its locally free cokernel makes the obstruction a genuine bundle map L⊗Sym²(V/L)→C. On the line flag, its restriction is a section of C⊗L*⊗(M*)², so its zero scheme is closed and projective.

Solving the repeated-input equation uses an inverse on its image, hence gives regular local sections, not just a pointwise construction. Under u'=a u and p'=b p+c u, the recovered class transforms as q'=(b²/a)q+(2bc/a)p modulo L. Modulo P this gives the global map M²L⁻¹→V/P. Two-plane injectivity excludes a zero geometric fiber. A map from a line bundle that is nonzero in every geometric fiber is locally a split injection, including over a nonreduced base. Thus W is a genuine rank-three subbundle and det W=M³. Passing to the reduction is sufficient for the dimension argument and loses no support information.

## Positivity and dimension

The sign in the projective-bundle relation is correct for the convention of lines: c(V/L)=1+h+h²+h³+h⁴ implies t⁴+ht³+h²t²+h³t+h⁴=0. Here h=c1(L*) and t=c1(M*).

On the quadratic incidence, h is nef and 3t is the pulled-back Plücker class of W, so t is nef. The line bundle with class 2h+t is the restriction of O(1,1) under the closed flag embedding into P(V)×Gr(2,V); it is ample. For an integral component of dimension d≥4, multiply the relation by (2h+t)^(d−4). All five mixed intersection numbers are nonnegative. Their vanishing forces the positive top self-intersection of the ample class to vanish, a contradiction. Operational Chern classes, or pullback to a resolution, justify this on singular components. Therefore the incidence has dimension at most three.

## Component and boundary consequences

Properness gives a closed exceptional subset of P⁴ of dimension at most three. On its complement the previously audited exact local elimination and Nakayama argument isolate the rank-one reduced support. Its irreducible closure D is consequently an actual component. The generic embedding dimension is four, so its generic length is at least five. The coherent nilradical has support containing all of D. All-nonzero rank-one points in the independent-zero closure must lie over the exceptional subset, giving dimension at most six after adjoining three nonzero scalar parameters.

## Independently checked generic-length refinement

At the generic point of D, the four normal variables have quadratic initial equations with empty projectivized common zero locus. Over the infinite residue field, four linear combinations of those quadrics can be chosen as a homogeneous system of parameters. In the polynomial ring on four variables they form a regular sequence of degrees (2,2,2,2), whose quotient has Hilbert series (1+z)^4 and length sixteen. The associated graded local ring is a quotient of this complete intersection because its initial ideal contains the chosen quadrics. Therefore its length, and the Artinian local length, is at most sixteen. Its graded pieces in degrees at least five vanish; Nakayama gives m^5=0. Together with the lower bound, 5≤length≤16. No equality, Gorenstein property, or complete-intersection property for the actual local ring follows.

## Scope

No actual operation value, selected input, matrix rank, jet, or source calculation was used. The exceptional incidence may be empty, its exact geometry remains undetermined, and a quadratic null direction need not integrate to an independent-zero degeneration. There are no outstanding mathematical corrections. The proof and this audit are frozen.

## Component count addendum

Section 7 also passes. The three coordinate components, a component meeting the independent open, and the now-established rank-one component are pairwise distinct. Thus at least five components exist. This does not determine the exact total.
