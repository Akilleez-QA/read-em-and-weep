# The unique possible marked pairing for the cubic normalization

Status: new structural derivation over C, awaiting independent mathematical review. No actual HM/source coefficient, vector, matrix, point evaluation, kernel/rank test, numerical scan, or large computation is used. The finite-field labels below are abstract character labels, not selected coordinates.

## 1. Pinned inputs and result

Use PR608 at 76d49d484c98bf0dd0f714c3e7041389d7cdede4, research/hm/cubic-fixed-directions/PROOF.md, with its pinned PR603, PR604 and PR605 dependencies. Specifically:

- PR603 at c9d38741e6a4c4eb714f61abe62aafdd9bb9ba81 identifies the thirty actual nodes with the disjoint sets of five eigenlines for the six order-five directions in the projective Heisenberg translation group U=F5^2, acting on its faithful-central-character irreducible five-dimensional module A.
- PR604 at a4a0b5ed6e9dd0c18e3a263d1b3f8d9a49f2bf8d gives sixty distinct component lines, four through each node, and the complete cubic system W=H0(I_Z(3)). The associated morphism Phi on Bl_Z P(A) embeds every exceptional divisor and every transformed component line.
- PR608 proves that r is zero or one. If r=1 there are sixty distinct bad values, with two reduced preimages each, all among the 120 marked component-side directions. The pair associated with a component ell lies over its two endpoints, and neither mark is the direction of ell itself. Component stabilizers in U have order five and fix their endpoints and all four incident component directions.

**Theorem.** The 120 marked directions form one orbit under the projective Heisenberg normalizer. The component incidence graph is the disjoint union of six complete graphs K5, each on one order-five eigenbasis. If r=1, its pairing of marked directions is uniquely forced as follows. On any eigenbasis use an affine character label i in F5, and denote by (i,j) the mark at i pointing toward j. Then

    tau(i,j) = (2i-j, 3i-2j),                 i != j.       (1)

In particular the pairing exists combinatorially, is normalizer-equivariant, and meets the endpoint and non-own-direction constraints. It does not exclude r=1. Geometrically, for each edge of either pentagon, its bad value pairs the outward-pointing marks of the two adjacent edges in that same pentagon. This resolves which marks could pair, not whether their actual cubic images coincide.

## 2. Intrinsic K5 incidence

At a node z, each incident component has a projective translation stabilizer of order five. Since it fixes z, z is one of that direction's eigenlines. Different directions have disjoint eigenline sets, so all these stabilizers are the same direction G_z, uniquely associated with z.

For any incident component through z, its other endpoint is fixed by G_z and is therefore another of its five eigenlines. There are four distinct incident lines, and only four possible other eigenlines. No two such lines can have the same pair of endpoints. Thus they are exactly the four joining lines to the other eigenlines of G_z. This proves that each five-point eigenbasis supports all ten joining lines, and all sixty components are obtained once this way. A mark is consequently exactly an ordered pair of different eigenlines in a common eigenbasis.

The translations U act on the five eigencharacters by every additive translation: nondegeneracy of the commutator makes U/G act simply transitively. Each original pentagon is translation-invariant with five edges. Its edges therefore have one fixed nonzero difference modulo sign. There are exactly two such difference classes in F5, giving the two complementary five-cycles inside K5. No assumed identification of paired cusps is needed for this description.

## 3. The actual affine action, and flag transitivity

For completeness the normalizer action used here follows from the abstract Heisenberg representation, rather than an assumed permutation transitivity. Write the finite Heisenberg group intrinsically as U times F5 with multiplication

    (u,t)(v,s) = (u+v, t+s+<u,v>/2),

after choosing a generator of its center; this is the exponent-five Heisenberg group. Every symplectic automorphism of U acts on this group fixing the center. Pullback of A by this automorphism has the same character as A: at the center it is five times the central character, and off the center the character is zero by the commutator trace lemma of PR603. Thus the two representations are isomorphic. Any intertwiner provides a projective normalizer element inducing that symplectic automorphism. Hence the projective normalizer maps onto Sp(U)=SL2(F5).

For a fixed direction G, its five eigenspace characters extending the fixed central character form an affine line under Hom(G,C*). Translations U provide all translations of this affine line. The stabilizer of G in SL2(F5) induces every nonzero scalar on G, and therefore every nonzero scalar on its character differences. Its permutation action together with U is the full affine group AGL1(F5). This action is sharply two-transitive on the five eigencharacters.

SL2(F5) is transitive on the six directions, and the stabilizer of one direction is transitive on its twenty ordered pairs of distinct characters. Therefore all 120 marks form a single normalizer orbit. The normalizer preserves Z and hence its complete cubic system and resolved morphism; no chosen equivariant HM matrix is required.

## 4. All incidence-compatible equivariant involutions

Assume r=1. Its 120 distinct source preimages exhaust the 120 marks, since there are sixty disjoint two-point fibers. Pairing equal-image marks defines an equivariant fixed-point-free involution tau. For a mark (i,j), its partner lies over an endpoint connected to i by a component. Section 2 puts that endpoint, and its marked direction, in this same eigenbasis.

Normalize a flag to (0,1) using the affine action, and write its partner (a,b). Distinct endpoints imply a != 0, and a mark implies b != a. Affine equivariance forces, for delta=j-i,

    tau(i,j) = (i+a delta, i+b delta).

Let d=b-a. Applying tau twice changes the difference by d^2 and the first endpoint by a(1+d)delta. Thus involutivity forces d^2=1 and a(1+d)=0. Since a != 0, we get d=-1, so b=a-1. The value a=1 would pair (0,1) with (1,0), namely the two own-direction marks of the joining component, prohibited by PR608. The remaining and sufficient combinatorial possibilities are a=2,3,4. Each is fixed-point-free and gives one pair over each unordered component edge, because multiplication of the endpoint difference by a is invertible.

## 5. Cubic character matching forces a=4

The natural evaluation vector of a cubic system lies in W*. Equivalently, W is an invariant subspace of Sym^3(A*), so its dual is an equivariant quotient of Sym^3(A). At the mark (i,j), the exceptional value is the nonzero image of the intrinsic tensor line

    L_i squared times L_j  subset Sym^3(A),

where L_i and L_j are the abstract eigenspaces. This is simply the first-order term of cubic evaluation at L_i in the direction toward L_j; the zeroth term vanishes because i is a base node. Nonvanishing follows from generation of 3H-E, not from evaluating any cubic coefficient. Scalar normalization or the conventional polarization factor does not alter its character.

For a generator of G, choose its eigencharacters as lambda times eta^i. The displayed tensor has character lambda^3 eta^(2i+j). Thus at (0,1) the exponent is 1, whereas at its possible partner (a,a-1) it is 3a-1. Equal projective image lines must have the same eigenvalue for this fixed linear action on W*. Consequently

    1 = 3a-1 in F5, hence a=4.

A common scalar twist of the target action changes neither equality nor conclusion. The result is (1), since 4=-1 and 4-1=3=-2 in F5.

## 6. Incidence compatibility and precise remaining obstruction

Formula (1) is invariant under every change of affine character label. It squares to the identity and its two basepoints differ by i-j != 0. The joining component has endpoints i and 2i-j; the first mark points toward j, not 2i-j, and the partner points toward 3i-2j, not i. Both are therefore allowed. Writing j=i+delta, the paired flags are

    (i,i+delta) and (i-delta,i-2delta).

They are the outward marks on the same difference-class pentagon, at the endpoints of its edge {i-delta,i}. This explicitly verifies that the forced pairing satisfies, rather than violates, the geometric incidence constraint. The normalizer action maps character torsors affinely, so this formula is globally normalizer-equivariant across the six K5 graphs.

The residual target eigenspaces have dimension exactly two. Indeed W* has dimension ten and its central character is the cube of the faithful central character of A, still faithful. Conjugation by a suitable Heisenberg element multiplies the spectrum of a generator of G by a primitive fifth root. The five eigenvalues therefore have equal multiplicities, necessarily two. Thus each relevant projectivized eigenspace is P1.

What remains is equality versus separation of the actual two cubic image lines for these uniquely specified paired marks, inside that P1. Equal characters only place these lines in the same two-dimensional eigenspace; they do not make them equal. No scalar, selected image vector, or actual kernel has been evaluated here. Therefore neither r=0 nor r=1 follows from this classification. The exact contribution beyond PR608 is flag transitivity, full K5 incidence, and a unique possible double-fiber pairing instead of unspecified marked directions. Analytic branch types and the separate full-adjoint and higher-lifting gates remain untouched.

