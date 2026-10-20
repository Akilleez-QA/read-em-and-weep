Publication context: this retained proof or audit may describe an intermediate bound or then-open branch. Read the unit overview for the current scope and later implications. Historical mathematical review is not a new formal verification.

# Complete canonical length-twelve exclusion

## Result and scope

Use the canonical regular local fourfold and full stabilizer H=μ5×(C5²⋊C4), with cotangent B=C5² weights (i,3i²), i∈F5×. Let Q be the isolated Ext² defect of an H-equivariant rank-two reflexive module with equivariantly trivial determinant, and P=D(Q). If length Q=12, then P must be cyclic.

The noncyclic exclusion is proved below. The independently audited theorem in ../cyclic-dual-defect-constraint/PROOF.md gives length at least nineteen whenever P is cyclic. Together these exclude every canonical defect of length twelve. Both component arguments have independent audits. No realizability claim is made.

Write O_c={(i,ci²):i≠0}. The nonzero-clock irreducibles have dimension four; the clock-trivial irreducibles have dimension one or two. Their B-weights are respectively zero or {(0,b),(0,−b)}. Restriction to L=C5⋊C4 makes each O_c a copy of its four-dimensional representation V. The notation “clock-trivial” does not mean B-trivial or a sum of full-H characters.

The necessary conditions are

    β1(P)−2s+a_H(Tor1(P,k))≤2,    s=β0(P).

In particular β1(P)≤2s+2; equality forces Tor1(P,k) self-dual. We may replace a_H by a_B for necessary inequalities. All square-zero defects of length twelve are already excluded by the universal bound length Q≤5 rank M.

## 1. Initial-relation counting, valid for filtered modules

Put h_j=dim m^jP/m^(j+1)P, so h_0=s. In an equivariant minimal cover F=R⊗T→P with kernel K, let K1=ker(W⊗T→mP/m²P), of dimension k=4s−h1. Every initial linear relation lifts to K by correction in m²F, giving a surjection K/mK→K1.

Let q=dim (Sym²W⊗T)/(W K1). The degree-two initial relations have codimension h2, and the degree-two initial space of mK is exactly W K1. Hence

    β1(P)≥k+max(0,q−h2).

This statement uses independent linear classes and then independent quadratic classes modulo their multiples; it does not assume homogeneous relations. The degree-two Koszul map T⊗Λ²W→(mP/m²P)⊗W has cokernel equal to the displayed quadratic quotient, so

    q≥4h1−6s.

When β1(P)=k, all minimal relations have independent linear initial forms. Any combination with vanishing linear part then has coefficients in m, proving that its quadratic initial form lies in W K1. Thus in this case q=h2 exactly.

## 2. Top dimension at least four, including the new three-V possibility

Since m²P≠0, h1≤11−s. Linear relations give 2s−h1≤2, hence 3s−11≤2 and s≤4.

Suppose s=4. Necessity gives h1≥6, while h1≤7. A clock-trivial top would give h1 divisible by four, impossible. Therefore T is one four-dimensional irreducible, with weights O_c. A length-twelve total representation consisting of three V's and no clock-trivial constituents is already impossible: it would require h1 divisible by four, again contrary to 6≤h1≤7. This explicitly treats the new three-V representation rather than importing the length-eleven enumeration.

Consequently the total representation has two V's and four clock-trivial dimensions. The first layer has one V plus h1−4 clock-trivial dimensions, and all later layers are clock-trivial. Consecutive nonzero clock-trivial layers are impossible because multiplication by W has no clock-trivial quotient. Hence the only shapes are (4,7,1) and (4,6,2).

For (4,7,1), k=9 and q≥28−24=4. Section 1 gives β1(P)≥9+4−1=12>10, impossible.

For (4,6,2), k=10 and β1(P)≤10 force equality, self-duality of K1, and q=2. The degree-two Koszul map has equal source and target dimensions 24. Its kernel and cokernel each have dimension two. Every representation of dimension two is clock-trivial, so the nonzero-clock B-weight multisets of source and target must agree.

The following explicit computation checks that this cannot happen. In W⊗O_c, the three nonzero-clock orbit slopes are

    c=0: 2,2,3; c=1: 1,3,2; c=2: 0,4,1;
    c=3: 4,0,0; c=4: 3,1,4.

Its clock-zero weights are two copies each of (0,3+c) and (0,−3−c). The two-dimensional clock-trivial quotient in the first layer retains one of each (or two zero weights when c=2). Self-duality of K1 forces the two unremoved slopes to be a negation-invariant multiset. Thus the possible top/first-layer orbit slopes (c,d) are

    (0,2), (1,1), (2,0), (3,4), (4,3).

Using Λ²W=O0 plus the weights (0,±1), the second-coordinate multisets at first coordinate one for the Koszul source and target are

    {4c,4c,c,c+1,c−1},
    {2+d,2+4d,3+4d,c+1,−c}.

Their multiplicity vectors at second coordinates 0,1,2,3,4 are respectively

    (0,2): (3,1,0,0,1) versus (2,2,0,0,1)
    (1,1): (1,1,1,0,2) versus (0,1,2,1,1)
    (2,0): (0,1,1,3,0) versus (0,0,2,3,0)
    (3,4): (0,0,3,1,1) versus (0,1,1,1,2)
    (4,3): (1,2,0,1,1) versus (3,1,0,0,1).

Each differs. Therefore s=4 is excluded, including every filtered correction.

## 3. Fresh enumeration for noncyclic tops of dimension two or three

Now the top is clock-trivial. Zero V constituents force mP=0. With one V constituent, a non-square-zero module has layers (s,4,8−s). In the associated graded, write x_i t=a_i(t)u_i and x_(−i)u_i=b_i in the bottom. Surjectivity and transitivity make every a_i,b_i nonzero. Commutativity gives a_i⊗b_i=a_(−i)⊗b_(−i). The opposite bottom vectors are proportional, so the bottom has dimension at most two; but 8−s≥5. This is impossible.

Thus there are two V's and four clock-trivial dimensions. A segment V→C→V with C clock-trivial forces dim C≥4: writing x_(−i)u_i=l_i and x_jc=f_j(c)v_j, commutativity makes f_j vanish on all l_i except l_(−j). Surjectivity makes every f_j nonzero and the l_i spanning, hence the four l_i linearly independent. There are at most 4−s≤2 clock-trivial dimensions after a noncyclic top, so no such intervening segment is possible.

If h1=8, the only shapes are (2,8,2) and (3,8,1). Section 1 gives β1≥18 and β1≥17 respectively, exceeding 2s+2.

If h1=4, the second V must occur immediately in the quadratic layer, possibly accompanied by clock-trivial constituents. Only a terminal clock-trivial layer can follow. Thus the complete noncyclic list remaining is

    (2,4,6), (2,4,5,1), (2,4,4,2),
    (3,4,5), (3,4,4,1).

This is a new length-twelve enumeration; no length-eleven exhaustive list was reused.

## 4. Both top-three shapes are impossible

Here k=8, and β1≤8 forces equality and self-duality of K1. A three-dimensional clock-trivial top has B-weights either three zeros or zero plus a pair ±b.

Three zero weights leave two O3 orbits in K1, not self-dual. For b=±1, the slopes in W⊗T are 3,4,2, and a self-dual remaining pair requires the first layer to be O4. For b=±2, the slopes are 3,0,1 and no deletion leaves a self-dual pair.

In the sole candidate, top vectors t0,t+,t− have weights 0,(0,1),(0,−1). Each x_i acts in the first layer only on the unique top line of weight (0,i²). The linear relations kill all parameters on t0 and the wrong opposite variable pair on each of t+,t−. Their quadratic quotient consists of the three quadratic monomials in each allowed pair, of total dimension six. But h2≤5. Section 1 forces at least one additional relation beyond the eight linear ones, a contradiction.

## 5. Representation imbalance reduces every top-two case to one linear action

The first layer is one orbit O_c. If T is a sum of characters, W⊗T consists of two copies of O3 and K1 is O3. If T is irreducible with weights (0,±b), W⊗T has the two distinct orbits O_(3+b), O_(3−b); K1 is the orbit not retained in the first layer.

We claim K1 must have slope zero. Indeed Tor1(P,k) contains K1 as a B-representation, by semisimplicity and the surjection of Section 1. If it contains O_e with e≠0, the four weights of O_e and their negatives are disjoint. For any representation Z containing these four weights, let A≥4 be their total multiplicity and C be the total multiplicity of their negatives. Then a_B(Z)≥|A−C| and dim Z≥A+C, giving

    dim Z+a_B(Z)≥2A≥8.

Thus β1(P)−4+a_B(Tor1(P,k))≥4, contrary to the rank-two bound. This excludes the character top and forces b=±2 with K1=O0 and first layer O1.

For this remaining action, the four initial linear relations are exactly x_i on the wrong top line. Their generated quotient is the direct sum of two polynomial modules, each in one opposite variable pair. Its quadratic component has weights

    O1 plus (0,1),(0,−1),

coming respectively from four squares and two opposite mixed monomials. Its cubic component has no clock-trivial weights: in a pair {i,−i}, cubic first coordinates are 3i,i,−i,−3i, all nonzero.

The shape (2,4,5,1) is impossible because its quadratic layer contains a one-dimensional clock-trivial full-H constituent, which must have B-weight zero, absent from the displayed quadratic quotient.

The shape (2,4,4,2) is impossible because its terminal cubic layer is clock-trivial, whereas the cubic quotient by the linear initial relations has no such weights. Further relations cannot create them. Both arguments apply directly to the associated graded module.

Finally suppose the shape is (2,4,6). The quadratic layer has the full six-dimensional quotient just displayed. The wrong-top linear relations have weights O0, absent from every radical layer of P (whose nonzero-clock weights are O1). They are therefore exact relations, with no higher corrections: choose equivariant top lifts and parameters; each wrong product is necessarily zero. Let L be their generated submodule of F. Then F/L is the direct sum of two formal power-series modules in two parameters. The induced kernel J of F/L→P lies in m³(F/L), since the maps on top, linear, and quadratic associated-graded pieces are isomorphisms. Conversely m³P=0 gives m³(F/L)⊂J. Thus J=m³(F/L).

This module has eight independent cubic generators (four cubic monomials in each opposite pair). Since L is generated by the four exact linear relations, K/mK has at least these eight additional generator classes, beyond its four independent linear classes. Equivalently the cubic classes remain independent after quotienting K by L+mK because J/mJ has dimension eight. Hence β1(P)≥12>6, a contradiction.

This excludes the last noncyclic shape and proves the stated theorem.

## Dependencies and permitted scope

The full stabilizer representations and weights are those in length-two-local-defect/PROOF.md. The rank/imbalance necessity and square-zero bound are representation-defect-bound/PROOF.md and SQUARE_ZERO.md. The five-row calculation and filtered relation-count arguments have also been checked in length-eleven-local-defect/PROOF.md and its audits; they have been explicitly adapted here to the new dimensions. The cyclic complement is independently audited in cyclic-dual-defect-constraint/AUDIT.md; the present noncyclic argument is independently audited in AUDIT.md.

All arguments concern universal abstract local algebra and finite representations. No physical source-model matrix, operation, chosen input, actual rank instance, jet, or residue was evaluated. No external write, upstream modification, installation, or large computation was performed.
