Publication context: this retained proof or audit may describe an intermediate bound or then-open branch. Read the unit overview for the current scope and later implications. Historical mathematical review is not a new formal verification.

# Every non-square-zero length-ten canonical module fails the defect bound

## Theorem

Let H=μ5×(C5²⋊C4) be the full canonical stabilizer and R the completed regular local complex ring in four equivariant linear parameters. Let W=m/m² have B=C5² weights (i,3i²), i∈F5×. For every H-equivariant finite R-module Q of length ten with m²Q≠0,

    β3(Q)−2β4(Q) ≥ 3.

Thus Q cannot be Ext² of an isolated rank-two reflexive module with equivariantly trivial determinant, for which the audited necessary inequality is ≤2. This leaves square-zero modules to a separate analysis. All constructions and calculations below are universal abstract local algebra and representations. No actual source-model matrix, operation, input, rank instance, jet, or residue is evaluated.

## 1. Reduction to three layers (2,4,4)

Use D=Ext⁴_R(−,R), and put P=D(Q). Then length P=10, m²P≠0, β3(Q)=β1(P), and β4(Q)=β0(P)=s. If s≥4, writing h1=dim mP/m²P gives h1≤9−s, and independent linear initial relations give

    β1(P)−2s ≥ 2s−h1 ≥ 3s−9 ≥3.

Hence assume s≤3. Restrict to L=C5⋊C4, whose irreducibles are characters trivial on the clock C5 and a four-dimensional V. Total representation types are zero, one, or two copies of V, with the remaining dimensions characters. Every radical layer is an L-representation, and consecutive character-only layers are impossible because W times a clock-trivial representation has no clock-trivial quotient.

Zero V forces mP=0. With one V, a non-square-zero P with top dimension at most three must have layers (s,4,6−s), with clock-trivial ends. The standard opposite-pair commutativity argument bounds its last dimension by two, a contradiction. Explicitly, in invariant complements write x_i t=a_i(t)u_i, x_(−i)u_i=b_i in the bottom. No higher correction is possible by clock weights. All a_i and b_i are nonzero and a_i⊗b_i=a_(−i)⊗b_(−i). Therefore the bottom is spanned by at most two opposite-pair vectors. This argument allows arbitrary decomposable clock-trivial H-representations at the ends.

With two V's, precisely two clock-trivial dimensions remain. Since s≤3, the top has dimension one or two and is clock-trivial. There are at most four layers. Four layers must be (1,4,4,1): the other arrangements have consecutive character-only layers or a V-character-V segment. The latter is impossible because the first multiplication is a perfect pairing and the next is an isomorphism, contradicting commutativity for two distinct parameters (as proved in length-nine-local-defect/PROOF.md §4.1). The (1,4,4,1) module is cyclic, and its four-dimensional quadratic layer forces at least six minimal quadratic initial relations, giving β1(P)−2≥4, without assuming gradedness.

For three layers and one-dimensional top, the shape is (1,4,5). Again P is cyclic; all four linear parameters survive, and its five-dimensional quadratic layer forces at least five minimal quadratic relations. Thus β1(P)−2≥3. To justify the relation count even in a filtered presentation R/I: I⊂m², and the kernel of Sym²W→m²P/m³P has dimension 10−5; its elements lift to I and remain independent in I/mI because mI⊂m³.

The only remaining case is

    P/mP=T, dim T=2;  mP/m²P=U, dim U=4;
    m²P=S, dim S=4;  m³P=0.                         (1)

Both U and S restrict to irreducible V under L. Consequently each is irreducible under H. Write a four-dimensional B-weight orbit of slope c as {(i,ci²):i≠0}. Every four-dimensional H-irrep nontrivial on the clock has exactly one such orbit, with each weight multiplicity one. Top T is either two H-characters or an irreducible two-dimensional H-representation. These exhaust the possibilities by length-two-local-defect/PROOF.md §1.

## 2. Top equal to two characters

Every H-character is B-trivial. Multiplication WT→U forces U to have slope 3, and the surjection Sym²W⊗T→S forces S to be a four-dimensional constituent of Sym²W. The latter has four-dimensional B-orbits of slopes 4 and 0, plus two clock-zero weights (0,±1). Thus S has slope 4 or 0.

In particular Hom_H(W⊗T,S)=0: the B-weight slopes of source and target differ. Choose H-invariant vector-space complements lifting T and U. All top-to-bottom correction terms therefore vanish. Middle-to-bottom multiplication is homogeneous automatically, since m³P=0. This proves gradedness here; it is not inferred merely from m³P=0.

Choose weight vectors u_i in U. Write x_i t=a_i(t)u_i, where each a_i is a nonzero linear form on T. The bottom alternatives give the following two cases.

### 2.1 Bottom slope 4

The only parameter products with slope-4 weights are squares: x_i u_i is a nonzero bottom vector v_i, and x_j u_i=0 for j≠i. Indeed the unordered products in Sym²W split into squares of slope 4, nonopposite mixed pairs of slope 0, and opposite pairs of clock weight zero. Surjectivity onto S makes each square action nonzero. Absorb its scalar into v_i.

Present P as a graded quotient of F=Sym(W)⊗T with T in degree zero, and write K for its kernel. Its degree-one part is

    K1=direct-sum_i x_i ker(a_i),

so there are four independent minimal linear relations. There are also at least four independent minimal cubic relations. For each i choose t_i with a_i(t_i)=1. Then x_i³t_i∈K3. To check independence modulo (mK)3, project the coefficient of the pure monomial x_i³ to T/ker(a_i). Every element of K1 has its pure x_i coefficient in ker(a_i), and every element of K2 has its pure x_i² coefficient in ker(a_i), because x_i²t=a_i(t)v_i and the four v_i are independent. Therefore this projection vanishes on (mK)3. Applied to the four chosen cubic relations, the four projections give the standard coordinate basis. Thus

    β1(P)≥4+4=8,  β1(P)−2β0(P)≥4.

### 2.2 Bottom slope 0

Each bottom weight corresponds to one unordered nonopposite mixed pair {i,j} (j/i=2 or 3). Its two ordered action coefficients must both be nonzero: at least one is nonzero by surjectivity, and commutativity gives a_i⊗b_(j,i)=a_j⊗b_(i,j). Hence a_i and a_j are proportional along every such edge. These four edges form a connected four-cycle on F5×, so all a_i are proportional.

Their common kernel is a one-dimensional top subspace killed by all parameters. Since there are no correction terms, choose a complementary top line and obtain an actual underlying R-module splitting P≅k⊕N. Here N is cyclic of Hilbert function (1,4,4), so β1(N)≥6. Consequently β1(P)≥4+6=10 and β1(P)−4≥6. The splitting need not be equivariant to establish this Betti bound.

## 3. Irreducible two-dimensional top: exact filtered normal form

The B-weights of T are (0,b),(0,−b), b≠0, with one-dimensional weight spaces t_+,t_−. Any central character is retained but plays no role in the following weight restrictions. W⊗T has two four-dimensional B-weight orbits, of slopes 3+b and 3−b. Therefore U has slope c∈{0,1,2,4}. For each i, only the unique top weight

    (0,(c−3)i²)

can map under x_i to u_i; denote a nonzero vector in that line by t(i). The two opposite indices i,−i use the same top line, while indices with different squares use the other line. Surjectivity makes all four initial action coefficients nonzero.

If i and j use different top lines, x_j t(i) has zero middle component, so it lies in S and is killed by m. Commutativity applied to t(i) implies x_j u_i=0; this reasoning is valid before removing any filtered corrections. If j=−i, the product x_j u_i has clock weight zero and hence is zero in S. Thus only x_i u_i can be nonzero. Surjectivity from U to S forces all four to be nonzero. Their weights show that S has slope

    d=(3+c)/4=2+4c modulo 5.                 (2)

The other orbit in W⊗T has slope 6−c=1−c. It never equals d, since 2+4c=1−c would give 2=1 in F5. Also d=c holds exactly when c=1. Therefore top-to-bottom filtered corrections are absent unless c=1; in that case they occur only in the same weight spaces and from the same top lines as the existing top-to-middle actions. Normalize lifts by defining

    u_i := x_i t(i),     v_i := x_i u_i,

rescaling t(i) or the middle basis as needed. This absorbs every allowed correction. Every other action x_j t(i) with the wrong top line is zero, because neither a middle nor bottom weight occurs. We have an exact underlying module normal form:

    x_i t(i)=u_i,  x_i u_i=v_i,
    x_j u_i=0 (j≠i),  x_j v_i=0 (all j),

with x_i killing the other top line. The module splits into two cyclic summands, one for each opposite-index pair {a,−a}. Each is isomorphic to

    R/(x_j for j outside {a,−a}, x_a x_(−a), x_a³, x_(−a)³).

The displayed quotient has basis 1,x_a,x_(−a),x_a²,x_(−a)² and maps onto the corresponding five-dimensional summand, so it is exactly that summand. Its ideal has five minimal generators: two independent linear generators, one mixed quadratic, and two independent pure cubics. Hence each has β1=5. It follows that

    β0(P)=2, β1(P)=10, β1(P)−2β0(P)=6.

This explicitly treats the only case where a higher filtered correction can occur and proves its removability instead of assuming a graded structure.

## Conclusion and dependencies

All non-square-zero length-ten modules satisfy the strict bound. The result does not exclude square-zero length ten, does not realize any local defect, and does not by itself raise the established global lower bound 300.

Dependencies: length-ten-local-defect/{PROOF,AUDIT}.md for the general large-socle count; length-nine-local-defect/PROOF.md for radical-layer and opposite-pair arguments, re-established where needed above; length-two-local-defect/PROOF.md for the full stabilizer and small irreducible representations; wedge-defect-equivariant-obstruction/PROOF.md for the fixed B-weight convention and the necessary rank-two defect bound. No equality-case representation constraint is needed: every case here violates the numerical inequality strictly.
