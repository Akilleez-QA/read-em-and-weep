# The global graph-cover algebra and an obstruction to the proposed trace bundle

## 1. Separate source and target surfaces

Write S_x and S_w for the source and target copies of the smooth modular surface S(5). Both map to the same modular parameter line. Let P=P_{S_x}(V), with projection b, and let h=ξ+I be the fixed w-polarization. The canonical map η:P -> P1 x P4_w is finite, including at cusps, by CANONICAL-CUSP-COMPONENTS.md. The graph divisor J_P has exact class h+H_x and is defined by the regular rank-two section u in K(3H_x-F), as proved in GLOBAL-GAMMA-CONDUCTOR-GRAPH.md. Its zero locus on S_x is finite.

On the smooth modular open, J_P maps to the target elliptic curve by multiplication by two. Its image closure is precisely the target modular incidence S_w. Hence the restriction

    p:J_P -> S_w

is finite of degree four. Since J_P is an effective Cartier divisor in the smooth threefold P, it is Cohen–Macaulay; since S_w is smooth, the finite map is flat. Therefore

    A=p_*O_J_P=O_S_w directsum T

is an actual rank-four finite-flat algebra, with T the rank-three trace-free bundle. This is not an identification of the two copies of S(5), nor of either with the nonnormal degree-fifteen image in P4.

The graph is the blowup of the zero ideal of u: locally its equation is the usual graph equation for a regular sequence of two functions. The zero scheme has length

    c2(K(3H-F))=10+(-H-F)(3H-F)+(3H-F)^2
                =10-55+105=60.

This length calculation alone does not assert that those sixty zeros are reduced. The finite-flat cover statement does not require that extra assertion.

## 2. Exact sheaf presentation from the incidence resolution

Let j:S_w -> P1 x P4_w be the target incidence embedding. Since η is finite, pushing forward the graph divisor sequence is exact:

    0 -> η_*O_P(-h-H_x) -> η_*O_P -> j_*A -> 0.

The first map is multiplication by the actual graph equation u. This gives an exact global algebra presentation, rather than a bundle guessed from fiber types or Chern classes. The trace-free bundle T is the kernel of trace A -> O_S_w, or equivalently A/O_S_w using the canonical trace splitting.

Also Rb_*O_J_P=O_S_x. Indeed the graph sequence has first term O_P(-ξ) tensored with a base line bundle, whose two relative cohomology groups vanish. Thus the graph resolution introduces no higher direct image of its structure sheaf. In particular χ(O_J_P)=χ(O_S_x)=5 and χ(T)=0.

The same resolution yields the exact modular acyclicity constraint. Let q_x:S_x -> P1 and q_w:S_w -> P1 be the two modular projections. Since q_w p=q_x b and Rb_*O_J_P=O_S_x,

    Rq_w* A = Rq_x* O_S_x.

Both modular structure-sheaf direct images are O in degree zero and O(−5) in degree one. The unit O_S_w -> A induces the identity on degree zero and a nonzero multiplication-by-two map on degree one over the smooth locus. A nonzero map between these two O(−5) line bundles is an isomorphism globally. Taking the trace-free direct summand gives

    q_w* T=0,     R1 q_w* T=0.

## 3. Restriction to a target five-torsion section

Let J0 in S_w be a five-torsion section. Since multiplication by two permutes the five-torsion sections, there is a unique inverse five-torsion section in S_x. It avoids the nodes of every I5 fiber and the finite graph indeterminacy locus; its graph maps isomorphically to J0.

This inverse section is in the smooth group locus of the semistable elliptic family. Multiplication by two is etale there in characteristic zero, including at the smooth points of cusp components. Hence after restricting p to J0, this degree-one section is open and closed and is disjoint from the other three sheets. There is a finite-flat rank-three algebra B on J0 with

    A|J0 = O_J0 directsum B

as algebras. Taking the quotient by the diagonal unit gives T|J0 isomorphic as a bundle to B. Its own trace splitting shows

    T|J0 has O_J0 as a direct summand.

In particular H0(J0,T|J0) is nonzero. This conclusion is about the actual extension across cusps, not just the smooth elliptic fibers.

## 4. The proposed End0(V)(-2F) identification is false

There is a direct argument using the already established fixed-w morphism, without a separate tangent-conic identification. On every five-torsion section J0, the entire ruled surface P(V|J0) maps to the same fixed HM line: this holds on the dense smooth modular locus, hence globally by closedness. The map is basepoint free and its polarization is h=ξ+I. Its two line coordinates therefore generate V|J0 tensor O_J0(I). Since I.J0=−1 and deg(V|J0)=2, this is a surjection from O_J0² to a rank-two degree-zero bundle. Its determinant is a nowhere-zero section of a degree-zero line bundle, so the surjection is an isomorphism. Thus

    V|J0=O(1) directsum O(1).

Consequently

    End0(V)(-2F)|J0=O(-2)^3,

which has no sections and no trivial direct summand. It cannot be isomorphic to T|J0. Thus the candidate global identification

    T = End0(V)(-2F)

is false, even though its rank, first Chern class, Euler characteristic, and generic elliptic-fiber decomposition can agree with those of T. The missing information is the actual cusp extension, which the graph-algebra presentation retains.

## Scope

The exact graph presentation and torsion-section obstruction do not by themselves give a simpler decomposition of T, identify its restriction to the conductor curve Y as a sum of line bundles, or prove the remaining eigenquotient vanishing. They provide a valid global algebra and rule out one proposed replacement for it. No selected coefficients, ranks, or prohibited experiments are used.

Primary source: https://arxiv.org/pdf/alg-geom/9606013, Remarks4.9–4.10, Lemmas4.14–4.15, and Proposition4.19. The finite canonical map and corrected polarization are established in the preceding project notes cited above.

## 5. Exact trace-pairing modification at the graph exceptional divisor

Let E_Z denote the exceptional Cartier divisor of b:J_P=Bl_Z(S_x) -> S_x, where Z is the regular zero scheme of u. The source and target canonical classes are both 3F. Adjunction for the graph, or the codimension-two blowup canonical formula, gives the relative dualizing line

    omega_{J_P/S_w}=O_J_P(E_Z).

Furthermore b_*O(E_Z)=O_S_x and R1 b_*O(E_Z)=0. Indeed the quotient in O -> O(E_Z) is O_{E_Z}(E_Z), the relative O(-1) on the projectivized rank-two normal bundle over the zero-dimensional regular center; both its relative cohomology groups vanish. Thus H0(O(E_Z)) is one-dimensional.

Finite Gorenstein duality identifies A^dual with p_*O(E_Z). The trace functional is a global section of this relative dualizing line and is generically nonzero. Since that space of sections is one-dimensional, it is a nonzero scalar multiple of the canonical exceptional section. The trace-pairing map A -> A^dual is therefore induced by O -> O(E_Z), giving

    0 -> A -> A^dual -> p_*O_{E_Z}(E_Z) -> 0.

The unit summand has the invertible trace pairing 4 and is orthogonal to the trace-free summand. Removing it yields the exact global sequence

    0 -> T -> T^dual -> p_*O_{E_Z}(E_Z) -> 0.

This is an actual cusp modification of the trace bundle, with its map determined by the finite cover. It is stronger than matching its Chern classes. If one additionally verifies that Z consists of the sixty reduced cusp nodes, the last term is the direct sum of the sixty exceptional O_P1(-1) sheaves pushed to their target cusp components. The exact sequence does not require that additional simplification.
