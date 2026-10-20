Publication context: this retained proof or audit may describe an intermediate bound or then-open branch. Read the unit overview for the current scope and later implications. Historical mathematical review is not a new formal verification.

# Canonical local length thirteen exclusion

## Statement and inputs

In the canonical regular local fourfold with full stabilizer H=μ5×(B⋊C4), B=C5², cotangent weights W={(i,3i²):i∈F5×}, let Q be the isolated Ext² defect of an equivariant rank-two reflexive module with equivariantly trivial determinant. Then length Q cannot equal thirteen.

Put P=Ext⁴_R(Q,R), s=dim P/mP, h_j=dim m^jP/m^(j+1)P. Write O_c={(i,ci²):i≠0}. A nonzero-clock irreducible has dimension four and these B-weights; a clock-trivial constituent has dimension one or two, with B-weights respectively zero or a pair (0,±b). The former will be called an orbit constituent. This terminology concerns the first B-coordinate, not the whole B action.

We use the proved necessary inequality

    β1(P)+a_B(Tor1(P,k)) ≤ 2s+2.

For a minimal cover R⊗T→P, set K1=ker(W⊗T→gr1 P), k=4s−h1, and q=dim (Sym²W⊗T)/(W K1). The filtered initial-relation count gives

    β1≥k+max(0,q−h2),    q≥4h1−6s.

If β1=k, then q=h2. These facts, including validity for nonhomogeneous relations, are proved in ../length-twelve-local-defect/PROOF.md §1. We also use that square-zero defects have length at most ten, from ../representation-defect-bound/SQUARE_ZERO.md. Finite duality preserves length and Loewy length. Thus m²P≠0 here. The inequality h1≥2s−2 and h1≤12−s implies s≤4. The cyclic case s=1 is excluded by ../cyclic-dual-defect-constraint/PROOF.md (bound twenty-two).

Completion may be taken throughout: it preserves all finite-length modules, Betti numbers, and representation data. Choose equivariant parameters and equivariant lifts of each generator space by averaging.

## 1. Top dimension four, including three orbit constituents

For s=4, 6≤h1≤8. If T is clock-trivial, h1 is a multiple of four, hence eight. The remaining length is one, so the shape is (4,8,1). Here k=8 and q≥8, whence β1≥15>10.

Otherwise T is one orbit O_c. A total representation with three orbit constituents has just one clock-trivial dimension. Its first layer, of dimension at least six, must contain both remaining orbit constituents. Thus it again has shape (4,8,1), excluded above. With just one total orbit, h1≤9 and clock-trivial, but a clock-trivial quotient of W⊗O_c has dimension at most four, contrary to h1≥6. (There are four opposite-index products.)

The remaining possibility has two orbit constituents and five clock-trivial dimensions. The first layer must contain the second orbit, since its clock-trivial part has dimension at most four. All later layers are clock-trivial. Multiplication of a clock-trivial representation by W has no clock-trivial quotient, so there can be only one later nonzero layer. The possible shapes are therefore (4,6,3), (4,7,2), and (4,8,1). For (4,7,2), k=9 and q≥4 give β1≥11>10.

For (4,6,3), k=10 and the bound force β1=10, K1 self-dual on B, and q=h2=3. The degree-two Koszul map

    T⊗Λ²W → (gr1 P)⊗W

has source and target both dimension24. Its kernel and cokernel both have dimension3, and thus are clock-trivial. Consequently source and target must have identical nonzero-clock B-weight multisets. This is impossible by the following explicit computation, identical to the dimension-two kernel/cokernel test at length twelve.

In W⊗O_c the three nonzero-clock slopes are

    c=0: 2,2,3; c=1: 1,3,2; c=2: 0,4,1;
    c=3: 4,0,0; c=4: 3,1,4.

The two retained clock-trivial dimensions are weights (0,±(3+c)), or two zero weights if c=2. Self-duality of K1 requires the two removed nonzero-clock slopes to form a negation-invariant multiset, leaving the candidate pairs (top slope c, first-layer slope d)

    (0,2), (1,1), (2,0), (3,4), (4,3).

Since Λ²W=O0 plus (0,±1), the source and target second-coordinate multiplicity vectors at first coordinate one, ordered by second coordinates0,1,2,3,4, are

    (0,2): (3,1,0,0,1) versus (2,2,0,0,1)
    (1,1): (1,1,1,0,2) versus (0,1,2,1,1)
    (2,0): (0,1,1,3,0) versus (0,0,2,3,0)
    (3,4): (0,0,3,1,1) versus (0,1,1,1,2)
    (4,3): (1,2,0,1,1) versus (3,1,0,0,1).

They differ in every case. This excludes s=4.

## 2. Enumeration for tops of dimension two or three

Such a top is clock-trivial, so three orbit constituents cannot fit into total length13. There must be at least one orbit constituent, since otherwise multiplication by W is zero and mP=0.

With exactly one orbit constituent, the only non-square-zero shape is (s,4,9−s). Indeed the first layer is the unique orbit; the next is clock-trivial and multiplication cannot continue. In this situation the bottom dimension is at most two: writing x_i t=a_i(t)u_i and x_(−i)u_i=b_i, commutativity gives a_i⊗b_i=a_(−i)⊗b_(−i). Surjectivity and orbit transitivity make these maps nonzero. Thus each opposite pair of bottom vectors is proportional. But 9−s≥6, impossible.

Hence there are two orbit constituents and five clock-trivial dimensions. A segment consisting of one orbit, a clock-trivial layer C, and one orbit requires dim C≥4. For completeness, write x_(−i)u_i=l_i∈C and x_jc=f_j(c)v_j. Commutativity forces f_j(l_i)=0 unless i=−j. The l_i span C and each f_j is nonzero, so all four l_i are linearly independent. There are at most5−s≤3 clock-trivial dimensions after the top. Thus this intervening segment is impossible.

If h1=8, the remaining length is5−s≤3, and the initial-relation bound gives

    β1 ≥ (4s−8)+(32−6s)−(5−s)=19−s>2s+2.

Otherwise h1=4, and the second orbit occurs in degree two. After that, only a terminal clock-trivial layer can occur. These arguments also exclude a square-zero shape directly; square-zero was already excluded universally.

## 3. Top dimension two

Here K1 has dimension4. It must have slope zero: if Tor1 contains an orbit O_e with e≠0, its dimension plus its B-imbalance is at least8. To see this, let A≥4 be its total multiplicity on O_e and C its multiplicity on −O_e; then a_B≥|A−C| and dim≥A+C. This contradicts β1+a_B≤6.

A character top gives two copies of O3 in W⊗T, and cannot leave O0 in K1. A two-dimensional top with weights (0,±b) gives slopes3+b and3−b. Thus necessarily b=±2, K1=O0 and gr1 P=O1.

The quotient by these four linear initial relations is a direct sum of two polynomial modules, each using one opposite variable pair. Its quadratic component has weights O1 plus (0,±1), so h2≤6. Its cubic component has no clock-trivial weights: in an opposite pair the cubic first coordinates are3i,i,−i,−3i, all nonzero. Since both orbit constituents have already appeared in degrees one and two, any degree-three layer would have to be clock-trivial, hence is zero. Therefore length P≤2+4+6=12, contradiction.

## 4. Top dimension three: the nonlinear correction is controlled

Now k=8 and β1≤8, so β1=8, K1 is self-dual, and q=h2. A clock-trivial three-dimensional top has B-weights either three zeros or zero plus (0,±b). Three zeros leave two O3 copies, which are not self-dual. For b=±2 the slopes3,0,1 do not admit a self-dual pair after deletion. For b=±1 the slopes3,4,2 leave the unique candidate K1=O3⊕O2 and gr1 P=O4.

Choose top vectors t0,t+,t− of weights0,(0,1),(0,−1). A variable x_i acts to first order only on t_b with b=i². Thus the four x_i t0 relations have slope3, and the four wrong-top relations x_i t_(-i²) have slope2. Quotienting the free polynomial module by these linear initial relations leaves a copy of k on t0 and two polynomial planes, one on each of t+,t−. Its quadratic component has dimension6 and weights O3 plus (0,±2). Since q=h2=6 and the total length is13, the shape is exactly (3,4,6), and m³P=0.

The O2 wrong-top products are exact zero in P: there is no O2 B-weight anywhere in P, whose radical layers have nonzero-clock slopes4 and3. Quotient the free completed cover by these four exact relations. The result is

    G=N⊕R t0,
    N=R/(x2,x3)t+ ⊕ R/(x1,x4)t−,

with index squares1 for the first opposite pair and4=−1 for the second. In particular N is a direct sum of two formal power-series planes. Let U⊂P be generated by t+,t−. The map N→U is an isomorphism in associated-graded degrees0,1,2: its dimensions there are2,4,6, and these exhaust the corresponding contributions to P. Since m³P=0, its kernel is exactly

    J=m³N.

This can be checked directly: an element in the kernel cannot have initial degree0,1,or2, and every element of m³N maps to zero. Hence μ_R(J)=8, the four cubic monomials on each plane.

The four remaining minimal relations in G can be chosen as

    x_i t0−f_i,    f_i∈m²N,    i=1,2,3,4.

Indeed x_i t0 is in m²P by its initial relation. Thus m²t0⊂m³P=0; since P is generated by t0 and the image of N, m²P is exactly the image of m²N. These four relations, together with the four exact wrong-top relations, have independent linear initial forms and form a minimal generating set of the original kernel: its minimal number of generators is exactly8. Thus the kernel of G→P is generated by the four displayed relations.

An element Σa_i(x_i t0−f_i) lies in N precisely when Σa_i x_i=0 in R. Since the parameters form a regular sequence, their syzygies are generated by the six Koszul syzygies. Therefore the intersection of this kernel with N, which is J, is generated by the six elements

    x_j f_i−x_i f_j,    1≤i<j≤4.

It follows that μ_R(J)≤6, contradicting μ_R(m³N)=8. This explicitly handles the possible quadratic corrections to the O3 relations; it does not silently assume that they vanish.

## Conclusion and scope

Every possible top dimension is excluded, proving that the canonical local defect cannot have length thirteen. Combined with the already established exclusions1 through12, every nonzero canonical local defect has length at least14. On the canonical thirty-point orbit this yields a contribution of at least420, conditional on the same support/orbit hypotheses used for the prior390 bound. No realization at fourteen is asserted.

This proof uses abstract local algebra and finite-group representation weights only. No physical source/model matrices, operation, chosen input, actual rank instance, jet, residue, or detector evaluation was performed. There were no external writes, upstream modifications, installations, or large computations.

Audit status: independently reviewed and passed; see AUDIT.md.
