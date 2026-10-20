Publication context: this retained proof or audit may describe an intermediate bound or then-open branch. Read the unit overview for the current scope and later implications. Historical mathematical review is not a new formal verification.

# Canonical local length fourteen exclusion

## Statement and dependencies

Under the canonical hypotheses of ../length-thirteen-local-defect/PROOF.md, an isolated Ext² defect Q of an equivariant rank-two reflexive module with equivariantly trivial determinant cannot have length fourteen. The stabilizer is H=μ5×(C5²⋊C4), B=C5², and the cotangent weights are W={(i,3i²):i∈F5×}. Write O_c={(i,ci²):i≠0}. An orbit constituent has these four nonzero-clock weights; all other irreducibles have dimension one or two and weights zero or (0,±b). We call the latter clock-trivial.

Set P=Ext⁴_R(Q,R), s=dim P/mP and h_j=dim m^jP/m^(j+1)P. Finite duality preserves length and annihilator. The audited dependencies provide

    β1(P)+a_B(Tor1(P,k)) ≤ 2s+2.

For an equivariant minimal cover F=R⊗T→P, write K1 for its linear initial relations, k=4s−h1, and

    q=dim (Sym²W⊗T)/(W K1).

The filtered initial-relation count in ../length-twelve-local-defect/PROOF.md gives

    β1≥k+max(0,q−h2),     q≥4h1−6s.

If β1=k, then q=h2, and lifts of a basis of K1 generate the entire relation module. The degree-two Koszul map T⊗Λ²W→gr1(P)⊗W has cokernel of dimension q. Square-zero defects have length at most ten, by ../representation-defect-bound/SQUARE_ZERO.md. Cyclic P has length at least31, by ../cyclic-defect-further-bound/PROOF.md. We therefore assume s≥2 and m²P≠0.

The inequalities h1≥2s−2 and h1≤13−s give s≤5. For s=5 they force (h0,h1,h2)=(5,8,1). Then k=12 and q≥2 imply β1≥13>12. Thus s is two, three, or four.

We may complete R and choose equivariant formal parameters and top lifts. All coefficient and weight arguments below therefore apply to arbitrary filtered modules, not only graded ones.

## 1. Top dimension two

The top is clock-trivial, so h1 is divisible by four. Since m²P≠0, it is four or eight. If h1=8, then k=0, q≥20, and h2≤4, giving β1≥16>6.

Thus h1=4 and k=4. Exactly as in the audited length-twelve proof, K1 must be O0: any representation containing O_e for e≠0 has dimension plus B-imbalance at least eight, beyond the budget six. Consequently T has weights (0,±2), and gr1(P)=O1. The quotient by the linear initial relations is the sum of two polynomial planes, each using an opposite variable pair. Its quadratic piece is O1 plus (0,±1), and its cubic piece has no clock-trivial weights.

There are at most three orbit constituents in P. If there is just one, it is in degree one, followed only by a clock-trivial degree-two layer of dimension at most two; length fourteen is impossible. If there are two, either the second occurs in degree two, or a clock-trivial degree-two layer separates the orbits. The latter requires at least four dimensions in that layer: the four opposite products must be linearly independent, by the commutativity argument in the length-thirteen proof, Section 2. But the quadratic quotient has only two clock-trivial dimensions. If the second orbit is in degree two, all later layers would be clock-trivial; the cubic quotient has none. Again length is at most 2+4+6=12.

If there are three orbit constituents, all clock-trivial dimensions are already in the top. Since h1=4 and q=6, the remaining two orbits must occupy degrees two and three, giving shape (2,4,4,4). The quadratic layer is O1. The cubic polynomial-plane quotient has orbits O2 and O3 (directly add the top weights (0,±2) to cubic weights in the respective opposite pairs); the cubic layer is one of these.

All four O0 linear relations are exact, because no O0 weight occurs anywhere in P. Quotienting by them gives N, the sum of two formal power-series planes. The two opposite quadratic products have weights (0,±1). They vanish exactly in P, because their degree-two images vanish and degree three has no clock-trivial weights. They yield two independent minimal relation classes beyond the four linear classes. Since β1≤6, these six exact relations generate the entire kernel. Their quotient is the sum of two modules of the form C[[x,y]]/(xy), with their top twists, hence has infinite length. This contradiction excludes s=2.

## 2. Top dimension three

Again h1 is four or eight. The latter gives k=4, q≥14 and h2≤3, so β1≥15>8. Therefore h1=4 and k=8=β1; K1 is self-dual and q=h2.

The audited top-three calculation in the length-thirteen proof applies without any length-specific assumption: the sole possible linear action has top weights 0,(0,±1), K1=O3⊕O2, first layer O4, and quadratic quotient O3 plus (0,±2), of dimension six. Thus h2=6. The quotient by the linear initial relations is one residue-field summand and two polynomial planes. Its cubic piece has no clock-trivial weights, since every cubic monomial in an opposite pair has nonzero first weight coordinate.

The prefix has length3+4+6=13. A length-fourteen module would have h3=1, a clock-trivial representation, contrary to that cubic quotient. This excludes s=3, with no need to control higher corrections.

## 3. Top dimension four: exhaustive numerical and weight reduction

Here 6≤h1≤9. If T is clock-trivial, h1=8; k=8, q≥8 and h2≤2 give β1≥14>10. Hence T=O_c.

For any T, h1=8 or9 is excluded by the same relation estimate: for h1=8, β1≥14, and for h1=9, β1≥18. Thus h1 is six or seven.

The clock-trivial part of W⊗O_c has dimension four, so the first layer contains another orbit. There can be two or three orbit constituents in all. If there are two, after the orbit in degree one all remaining constituents are clock-trivial; consecutive clock-trivial radical layers are impossible. If there are three, their total dimension twelve leaves only two clock-trivial dimensions. Thus h1=7 is impossible with three orbits, and h1=6 forces shape (4,6,4), with the third orbit in degree two. With two orbits the possible shapes are (4,6,4) with clock-trivial last layer, or (4,7,3).

Suppose h1=7. Its clock-trivial part has dimension three. The clock-trivial weights of W⊗O_c are two copies each of (0,3+c) and (0,−3−c); a three-dimensional H-stable quotient is possible only if c=2, when they are all zero. Now k=9 and β1≤10. Any additional relation representation has dimension at most one and cannot cancel a nonzero-clock imbalance. Hence the two orbit constituents of K1 must form a self-dual pair. The nonzero-clock slopes of W⊗O2 are0,4,1, so K1 contains O4⊕O1 and gr1(P)=O0 plus three zero weights.

At first coordinate one, the second-coordinate multiplicity vectors, in order0,1,2,3,4, of the degree-two Koszul source and target are

    source O2⊗Λ²W:             (0,1,1,3,0),
    target (O0+3·0)⊗W:         (0,0,2,4,0).

Therefore the cokernel contains at least one copy each of O2 and O3, and q≥8. The bound β1≥9+8−3=14 excludes h1=7.

It remains that h1=6. Here k=10=β1, so K1 is self-dual and q=h2=4. The two clock-trivial dimensions in the first layer retain one each of (0,±(3+c)), or two zero weights if c=2. The nonzero-clock part of W⊗O_c has the following slopes:

    c=0: 2,2,3; c=1: 1,3,2; c=2: 0,4,1;
    c=3: 4,0,0; c=4: 3,1,4.

Self-duality of the two removed orbits leaves the following possible (top slope, retained first-layer slope) pairs. Source and target multiplicity vectors of the Koszul map are included:

    (0,2): (3,1,0,0,1) versus (2,2,0,0,1)
    (1,1): (1,1,1,0,2) versus (0,1,2,1,1)
    (2,0): (0,1,1,3,0) versus (0,0,2,3,0)
    (3,4): (0,0,3,1,1) versus (0,1,1,1,2)
    (4,3): (1,2,0,1,1) versus (3,1,0,0,1).

These are the explicit weight additions already audited at lengths twelve and thirteen. Here the source and target both have dimension24, and kernel and cokernel both have dimension4. In rows (1,1), (3,4), (4,3), the positive part of source minus target already requires at least two orbit constituents in the kernel, of total dimension8, impossible. In the two remaining rows the forced kernel and cokernel exhaust their dimensions:

    top O0: kernel O0, cokernel O1;
    top O2: kernel O1, cokernel O2.

In particular the clock-trivial last-layer possibility is excluded. The only remaining representations, with shape (4,6,4), are

    A: top O0, first O2 plus (0,±2), last O1;
    B: top O2, first O0 plus two zero weights, last O2.

## 4. All relations in the two residual cases are exact linear

In case A, K1 consists of O2⊕O3 plus (0,±2). Its weights are disjoint from the degree-two layer O1. In case B, K1 consists of O1⊕O4 plus two zero weights; these are disjoint from the degree-two layer O2.

For either case, take any B-eigenvector linear relation and form its product expression using equivariant top lifts and parameters. Its image lies in m²P, since it is a linear initial relation. By the disjoint weights just observed, that image is zero. Hence every linear initial relation is exact. Since their ten independent classes already exhaust β1=10, they generate the whole kernel. Thus P is the completion of the homogeneous module presented by these ten linear relations. There are no additional nonlinear relations or filtered corrections.

## 5. Excluding case B by a polynomial-line quotient

Let t_j denote the top vector of weight (j,2j²). The weight of x_i t_j has second coordinate3i²+2j². Its nonzero-clock slope is zero precisely when j=i; the case j=−i has first coordinate zero. Consequently the retained O0 consists of the four products x_i t_i. All products x_i t_j with j≠±i are relations. The two remaining relations are among the opposite products x_i t_(−i).

Set x2=x3=x4=0 and t2=t3=t4=0. Every relation maps to zero, and t1 survives as a free generator over C[[x1]]. Thus the presented module has an infinite-length quotient, contradicting the finite length of P.

## 6. Excluding case A by a two-variable cubic count

Here t_j has weight (j,0). For each i≠0:

- the product x_i t_(3i) is the unique product at its O3 weight, so it is a relation;
- each O2 weight has two products: x_i t_i and x_(−i)t_(3i). There is one linear relation between these two products, with arbitrary coefficients, possibly one zero;
- the clock-trivial relations are one relation among x1t4 and x4t1, and one among x2t3 and x3t2.

This is all ten relations: four O3 relations, four O2 relations, and two clock-trivial relations. The assertions follow directly from the alternatives j=i,2i,3i,−i: slope2 occurs for j=i or2i, slope3 for j=3i, and clock zero for j=−i. No constraint on the coefficients is needed.

Now quotient by x2=x3=0, retaining all four top generators. Of the ten relations, at most five remain nonzero:

    x1t3, x4t2;
    the two O2 relations indexed by i=1,4;
    the relation between x1t4 and x4t1.

The other five involve only x2,x3. Therefore this quotient has a homogeneous presentation over S=C[x1,x4] with four degree-zero generators and at most five linear relations. Its degree-three part has dimension at least

    4 dim(S3) − 5 dim(S2) = 4·4 − 5·3 = 1.

Relations among the five relations can only increase this lower bound. Completion does not change these finite graded pieces. This contradicts m³P=0, which would also force the third power to vanish in every quotient. Thus case A is excluded.

## Conclusion and scope

All possible top dimensions and representation configurations are excluded. Therefore canonical local length fourteen is impossible. Combined with the audited exclusions1 through13, a nonzero canonical local defect has length at least15. On the canonical thirty-point orbit, its contribution is at least450, conditional on exactly the prior support/orbit hypotheses. No realization at15 is asserted, and the cyclic bound31 remains a separate stronger conditional statement.

This is universal abstract local algebra and finite-group representation arithmetic only. No physical source or model, actual matrix instance, operation, chosen input, rank instance, jet, residue, or detector was evaluated.  A small graph check of the final abstract relation family motivated the two-variable argument, but the proof above does not depend on computation.

Audit status: independently reviewed and passed; see AUDIT.md.
