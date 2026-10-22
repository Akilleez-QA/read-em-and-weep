# A reduced determinant cubic cannot have only isolated singularities

Checked deduction, 2026-10-21.

## Statement

Let E be a stable rank-two vector bundle on complex projective three-space with c1(E)=-1, c2(E)=4, h0(E(1))=0 and h0(E(2))=2. For a basis s,t of H0(E(2)), let

    S = V(s wedge t) subset P3.

Then S cannot be reduced with a finite singular locus. Consequently, if S is the cone over a reduced plane cubic, that plane cubic must be singular. This conclusion does not settle the cases of a nodal/cuspidal irreducible plane cubic or a union of three distinct lines.

## Cohomological inputs checked independently

Bănică–Manolache's 1981 preprint, printed page 3 (PDF page 7), lists the only spectra as (-2,-1,0,1) and (-1,-1,0,0). Printed page 4 (PDF page 8), Lemma 2, says the first spectrum forces h0(E(1))>0. Thus the hypotheses give the second spectrum. The page-3 table explicitly gives

    h1(E(-1)) = 2,    h2(E(-1)) = 0.

Source: https://imar.ro/~increst/1981/104_1981.pdf

There is also a project-specific route not using the spectrum classification. For E=F restricted to H, the sequence

    0 -> F(-2) -> F(-1) -> E(-1) -> 0

gives the same two dimensions from the supplied, already established inputs that F(-1) is acyclic and F(-2) has only H2, of dimension two. This implication was checked directly in its long exact cohomology sequence.

## Zero-curve properties

Set V=E(2); then det(V)=O(3) and c2(V)=6. Every nonzero section is regular: a divisorial zero of degree d>=1 would give a nonzero section of E(2-d), contradicting h0(E(1))=0. Nonemptiness follows from c2(V)=6. Its zero curve C is therefore pure one-dimensional, locally complete intersection, and Cohen–Macaulay, with

    deg C = 6,    omega_C = O_C(-1).

The Koszul and ideal sequences are

    0 -> O(-3) -> E(-1) -> I_C -> 0,
    0 -> I_C -> O -> O_C -> 0.

On P3, O(-3) is acyclic. Hence h1(I_C)=2 and h2(I_C)=0, and therefore

    h0(O_C)=3,    h1(O_C)=0.

This holds for every member of the section pencil, with no generality assumption on E or H.

## What reducedness would imply

If C is reduced, its proper connected components C_i have only constant regular functions over C. Thus there are exactly three connected components. Each has h1(O_Ci)=0, so arithmetic genus zero. Since each C_i is Gorenstein and omega_Ci=O_Ci(-1),

    -deg(C_i) = deg(omega_Ci) = 2*p_a(C_i)-2 = -2.

Each component therefore has degree two. A reduced connected degree-two curve in P3 is a plane conic, possibly a pair of intersecting lines. Hence C is a disjoint union of three reduced plane conics. Their containing planes are distinct, since plane curves of degree two in the same plane cannot be disjoint.

The regular-section sequence

    0 -> O -> V -> I_C(3) -> 0

shows that h0(I_C(3))=1. Its generator is s wedge t; it is independent, up to scalar, of the chosen nonzero section. The product of the three conic-plane equations is another nonzero cubic containing C. Uniqueness therefore forces S to be exactly the reduced union of those three planes.

Important precision: reducedness alone gives reduced conics, not necessarily smooth conics. Smoothness is unnecessary for the determinant conclusion.

## Finite-singular-locus argument

Suppose S is reduced and Sing(S) is finite. On S_sm the evaluation matrix

    ev: H0(V) tensor O -> V

has rank exactly one. Indeed its rank-zero locus is contained in Sing(S), because every first derivative of a two-by-two determinant vanishes when all four entries vanish. Its kernel consequently defines a morphism

    k: S_sm -> P(H0(V)).

On each irreducible component this morphism is nonconstant: a constant kernel would supply a section vanishing on a dense open of a surface component, hence having a forbidden divisorial zero. Generic smoothness in characteristic zero therefore gives a dense open subset of P1 over which all fibers on S_sm are smooth. The finitely many components permit one common such open subset.

Scheme-theoretically these fibers are the zero curves of the corresponding section, restricted to S_sm. Locally, an invertible matrix entry reduces the equations to the determinant equation together with the one equation specifying the kernel line. Thus a general C is smooth on C intersect S_sm.

No one-dimensional component of C is contained in the finite set Sing(S). Therefore C is generically reduced. Since C is Cohen–Macaulay, it has no embedded associated points and generically reduced implies reduced. Equivalently, use the reducedness criterion (R0)+(S1).

The preceding section now forces S to be the union of three distinct planes. Such a surface has a positive-dimensional singular locus, contradicting the assumed finite singular locus. This proves the statement.

Standard commutative-algebra references for the last step: Stacks Project, Section 10.104, https://stacks.math.columbia.edu/tag/00N7 . The explicit reducedness criterion appears in https://stacks.math.columbia.edu/tag/07QJ , citing Algebra Lemma 10.157.3.

## Cone consequence and remaining gap

The cone over a smooth plane cubic is reduced and has only its vertex singular. It is therefore impossible as S. For the actual cone family, every plane-cubic base is singular: the reduced bases are singular by this argument, and a nonreduced plane cubic is not smooth.

This proof does not cover a positive-dimensional singular locus: a curve component of C could then lie inside it, and generic smoothness on S_sm does not control that component's multiplicity. In particular, reducedness of S alone has not been proved sufficient. No generic-moduli statement or special-section counterexample with nonreduced determinant can fill this missing step.
