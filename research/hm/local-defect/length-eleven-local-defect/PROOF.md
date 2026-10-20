Publication context: this retained proof or audit may describe an intermediate bound or then-open branch. Read the unit overview for the current scope and later implications. Historical mathematical review is not a new formal verification.

# Length eleven: new exclusions and three remaining filtered families

## Result and precise scope

Let R be the completed regular local complex ring of dimension four at a canonical point, H=μ5×(C5²⋊C4) its full stabilizer, and W=m/m² with B=C5² weights (i,3i²), i∈F5×. Suppose Q=Ext²_R(M,R) for an H-equivariant rank-two reflexive module M, free off the closed point, with equivariantly trivial determinant. Write P=D(Q)=Ext⁴_R(Q,R).

If length Q=11, then P must have one of exactly the following three possible radical Hilbert functions:

    (2,4,5), (2,4,4,1), (3,4,4).

This is a necessary list, not an assertion of existence or realizability. On restriction to L=C5⋊C4 its total representation is 2V plus three clock-trivial character dimensions. The top is clock-trivial; each 4-dimensional layer in the list is V; the 5-dimensional layer is V plus one character; and the 1-dimensional layer is a character. Full-H two-dimensional representations in clock-trivial layers are allowed. No gradedness is assumed for these remaining families.

In particular every square-zero length-eleven Q, every Q with β4(Q)≥4, and every Q with cyclic finite dual are excluded. This is genuine progress beyond length ten, but does not exclude all length eleven or improve the global bound 330.

## 1. Numerical setup and all square-zero modules

We use the audited necessary conditions

    d=β1(P)−2β0(P)=β3(Q)−2β4(Q)≤2,

and, if d=2, Tor₁(P,k) is self-dual as an actual H-representation. These follow from length-five-local-defect/PROOF.md and wedge-defect-equivariant-obstruction/{PROOF,AUDIT}.md. Finite duality incorporates its canonical character; no further determinant twist is introduced.

For m²P=0, set s=dim(P/mP), h=dim mP=11−s. The Koszul first differential has rank h, and the second has rank r≤min(6s,4h). Therefore

    d=44−h−r−2s=33−s−r
     ≥33−s−min(6s,44−4s).

For integers 0≤s≤11 the latter expression is at least four: for s≤4 it is at least 33−7s≥5, and for s≥5 it is at least 3s−11≥4. Thus all square-zero modules fail the necessary bound. Finite duality preserves annihilation by m², so this also excludes square-zero Q.

For m²P≠0, put h1=dim mP/m²P. Independent linear initial relations give β1(P)≥4s−h1, hence d≥2s−h1. Since h1≤10−s, we have d≥3s−10. Consequently s≥5 is impossible. If s=4, necessity forces h1=6, dim m²P=1, m³P=0, and β1(P)=10. We next exclude this equality case.

## 2. Top dimension four: a filtered equality obstruction

Restriction to L shows that the top U is V, and the middle A=mP/m²P is V plus two character dimensions. Indeed a four-dimensional character-only top can generate only a sum of V's in its next layer, whereas that layer has dimension six. The bottom S=m²P is a character.

Let μ:W⊗U→A be multiplication in the associated graded module and K1=ker μ. It has dimension ten. Choose an equivariant minimal free cover F=R⊗U→P, with kernel K. The natural initial-linear map K/mK→K1 is surjective: any linear relation lifts to a relation by correcting in m²F, since m²F→m²P is surjective. Both spaces have dimension ten, so it is an equivariant isomorphism. Hence the equality condition makes K1 self-dual.

We also need the degree-two information without assuming P graded. Choose ten minimal generators of K whose independent initial forms are a basis of K1. A combination of these generators can belong to m²F only if all its constant coefficients vanish, since their linear initial forms are independent. Its quadratic initial form therefore belongs to W K1. Conversely every element of W K1 occurs this way. Thus the degree-two initial relation space is exactly W K1, and

    dim (Sym²W⊗U)/(W K1)=dim S=1.

Let δ:U⊗Λ²W→A⊗W be the degree-two Koszul map. Both sides have dimension 24. The kernel of the multiplication map W⊗K1→Sym²W⊗U identifies with ker δ: inside U⊗W⊗W, its intersection with the alternating subspace is precisely the condition that the induced image in A⊗W vanish. Both W⊗K1 and Sym²W⊗U have dimension 40, so the displayed one-dimensional cokernel gives dim ker δ=1, and hence dim coker δ=1. All maps are equivariant. One-dimensional H-representations restrict trivially to B, so the B-weight multisets of U⊗Λ²W and A⊗W must agree at every nonzero first coordinate.

Here is the exhaustive character contradiction, reproduced explicitly from the length-ten calculation. Write O_c={(i,ci²):i≠0} and Z_z={(0,z),(0,−z)}, with multiplicities retained when z=0. The top U has orbit O_c for some c∈F5. The middle A has weights O_d⊔Z_(3+c), where d must be one of the three nonzero-clock orbit slopes in W⊗U:

    c=0: 2,2,3;   c=1: 1,3,2;   c=2: 0,4,1;
    c=3: 4,0,0;   c=4: 3,1,4.

The clock-zero part of W⊗U has each weight of Z_(3+c) twice. A two-dimensional clock-zero quotient must retain one of each, including two zero weights when 3+c=0. This allows full-H two-dimensional irreducibles, rather than incorrectly restricting to sums of H-characters.

Duality sends O_e to O_(−e). Thus self-duality of K1 forces the two unremoved slopes to be invariant as a multiset under negation. The only possible pairs (c,d) are

    (0,2), (1,1), (2,0), (3,4), (4,3).

Since Λ²W has weights O_0⊔Z_1, the second coordinates at first coordinate one on the two sides of δ are respectively

    {4c,4c,c,c+1,c−1},
    {2+d,2+4d,3+4d,c+1,−c}.

Their multiplicity vectors at second coordinates 0,1,2,3,4 are

    (c,d)   source          target
    (0,2)   (3,1,0,0,1)     (2,2,0,0,1)
    (1,1)   (1,1,1,0,2)     (0,1,2,1,1)
    (2,0)   (0,1,1,3,0)     (0,0,2,3,0)
    (3,4)   (0,0,3,1,1)     (0,1,1,1,2)
    (4,3)   (1,2,0,1,1)     (3,1,0,0,1).

Each differs, contradicting the required agreement at nonzero first coordinate. Thus s=4 is impossible, including all filtered corrections.

## 3. Exhaustive remaining layer enumeration

We now have s≤3, so the top is clock-trivial. The total L-representation has zero, one, or two V constituents; all other constituents are clock-trivial characters. Zero V forces mP=0. Consecutive nonzero character-only radical layers are impossible, since W times a clock-trivial representation has no clock-trivial quotient.

With one V, non-square-zero P must have three layers (s,4,7−s), with clock-trivial ends. In invariant complements, clock weights prohibit higher corrections and multiplication has form x_i t=a_i(t)u_i and x_(−i)u_i=b_i in the bottom. All a_i,b_i are nonzero; the b_i span the bottom. Commutativity gives a_i⊗b_i=a_(−i)⊗b_(−i), so opposite b_i are proportional and the bottom has dimension at most two. But 7−s≥4, impossible.

It remains to consider exactly two V's and three character dimensions. We first rule out any associated-graded segment V→C→V in which C is clock-trivial of dimension less than four. Write x_(−i)u_i=l_i∈C; these four vectors span C by surjectivity. Commutativity gives x_j l_i=0 whenever j≠−i. In the surjection W⊗C→V, write x_j c=f_j(c)v_j; each f_j is nonzero by transitivity and surjectivity. Since the l_i span C, each f_j must be nonzero on l_(−j), while zero on the other three l_i. Consequently the four l_i are linearly independent, forcing dim C≥4, a contradiction. This argument applies to the associated graded and is unaffected by filtered corrections.

The first radical layer is either V or 2V. In the latter case, all remaining dimensions are characters. The only non-square-zero possibility is (2,8,1): top one is impossible because h1≤4s, and top three leaves no further layer.

If the first radical layer is V, the second V must occur in the next layer: any intervening character-only layer would give the forbidden segment just proved. That layer can also contain b character dimensions. Any subsequent nonzero layer is character-only, of dimension c, and no further layer can occur. With s+b+c=3 this gives precisely

    (1,4,6), (1,4,5,1), (1,4,4,2),
    (2,4,5), (2,4,4,1), (3,4,4).

Zero terminal layers are suppressed. This enumerates every possibility without assuming gradedness or a decomposition of clock-trivial full-H modules into H-characters.

## 4. Every cyclic case is excluded

For cyclic P=R/I with h1=4, I⊂m². If its second radical layer has dimension h2, there are at least 10−h2 independent minimal quadratic relations: each element of the quadratic initial kernel lifts to I and is independent modulo mI⊂m³. Thus β1(P)−2≥8−h2. The shapes (1,4,5,1) and (1,4,4,2) give strict bounds three and four.

For (1,4,6), the bound is two. Necessity would force β1(P)=4. Here m³⊂I⊂m², so I is homogeneous, determined by its four-dimensional quadratic relation space together with all cubics. Four minimal generators imply that its four quadrics generate I. Since I is m-primary in a regular local ring of dimension four, these four generators are a regular sequence. Their homogeneous quotient therefore has Hilbert series (1+t)^4 and length sixteen, contrary to length eleven (and to m³P=0). This excludes the last cyclic case.

The remaining shape (2,8,1) also violates the numerical bound strongly. Its minimal free cover F=R²→P has kernel K⊂m²F because all eight linear generators survive. The quadratic initial relation space has dimension 2 dim Sym²W−1=19. Its elements lift to K and remain independent in K/mK since mK⊂m³F. Thus β1(P)≥19 and d≥15.

Removing these four shapes leaves exactly the three families stated at the beginning. Their filtered multiplication and full-H linearizations remain unresolved; no additional numerical or representation assumption is imposed on them here.

## Dependencies and permitted scope

The stabilizer and representation classification are from length-two-local-defect/PROOF.md. Numerical defect necessity and the equality self-duality criterion are from length-five-local-defect/PROOF.md and wedge-defect-equivariant-obstruction/{PROOF,AUDIT}.md. The five-row weight calculation is re-established above and agrees with squarezero-length-ten-defects/{PROOF,AUDIT}.md. The filtered arguments and fresh length-eleven layer enumeration are supplied here rather than inferred from length ten.

All calculations concern universal abstract local modules and finite representations. No physical source-model matrix, operation, chosen input, rank instance, jet, or residue was evaluated. No external write, upstream modification, installation, or large computation was performed.
