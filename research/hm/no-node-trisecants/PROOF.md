# No node trisecants, finite cubic normalization maps, and ample polarization

Status: independently mathematically reviewed (PASS); see REVIEW.md. Not formally checked. Work over C. The new argument is a universal theorem about abstract irreducible Heisenberg representations. No selected actual HM/source coefficients, coordinate vectors, matrices, point evaluations, rank tests, numerical searches, or large computations are used. In particular, the inner-product estimate below is proved symbolically for every representation in the stated class; no Gram matrix of a selected configuration is constructed or evaluated.

## 1. Exact inputs and conclusions

Use the following immutable sources:

1. PR587, commit `865ab24e91333688d7ae76303d7d594aae8521f8`, Sections 1 and 4 of [eigenline-interpolation/PROOF.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/865ab24e91333688d7ae76303d7d594aae8521f8/research/hm/eigenline-interpolation/PROOF.md): the actual node set Z of the integral primary surface S in P(A)=P4 is exactly the thirty eigenlines of the six maximal abelian subgroups of the order-125 Heisenberg group on its five-dimensional irreducible module A, with nontrivial central character. These are points in the actual ambient P(A), not eigen-hyperplanes in a substituted dual space.

2. PR602, commit `13647efe962d87c3344729e28c2a5e9ceeb0f2ba`, Sections 1–7 of [cubic-map-geometry/PROOF.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/13647efe962d87c3344729e28c2a5e9ceeb0f2ba/research/hm/cubic-map-geometry/PROOF.md): write

       pi: M=Bl_Z P4 -> P4,
       nu: X -> S,
       b: Y=Bl_W X -> X,     W=nu^(-1)(Z).

   Here X is smooth, W consists of sixty reduced points, and Y is the smooth strict transform of S in M. If H=pi^*O_P4(1) and E is the sum of the thirty ambient exceptional divisors, then the ten actual cubic generators of I_Z generate D=3H-E. Their morphism Phi:M->P9 and its restriction Phi_Y:Y->P9 are birational onto their reduced images V and T. The image V is an integral nondegenerate fourfold of degree 51, and T is an integral nondegenerate surface of degree 75. The curves contracted by Phi are exactly the strict transforms of lines containing three distinct points of Z; Phi_Y contracts precisely those among them contained in S. Also D^4=51 and (D|Y)^2=75.

**Theorem.**

(a) Every three distinct points of Z are projectively noncollinear. In particular no line in P4, whether or not contained in S, contains three nodes.

(b) Phi:M->V and Phi_Y:Y->T are finite birational morphisms. They are the normalization morphisms of V and T, respectively.

(c) D=3H-E is ample on M, and D|Y is ample on Y. Thus the resolved actual cubic system is an ample, globally generated polarization, with the already established self-intersections 51 and 75.

These statements do not assert that V or T is normal, that either morphism is an embedding, or that special fibers are reduced or singletons.

## 2. The actual-node hypothesis is geometric, not a numerical match

For clarity, the node identification used in input 1 has a substantive proof. The six directions in the projective Heisenberg quotient have five distinct eigenlines each. Distinct directions have no common eigenline, because their lifts have a nontrivial central commutator and the central character on A is nontrivial.

At each of those thirty eigenlines, PR553 proves structurally that the actual primary map e has rank eight. Its local maximal-minor equations have size ten. Their first derivatives are sums of differentiated entries times nine-by-nine cofactors, and all such cofactors vanish at rank eight. Consequently the tangent space of its degeneracy scheme is the entire four-dimensional ambient tangent space at every eigenline. The scheme equality D_9(e)=S from PR573 makes every one of these points singular on S. Since S has exactly thirty singular points, all transverse double points, its reduced node set is precisely this eigenline configuration. This is the argument recorded in PR587, Section 4; it is not a fresh selected-point evaluation.

The only new work below is a basis-independent property of that configuration, followed by the consequences of input 2.

## 3. Universal orthogonality and unbiased eigenbases

We prove the needed representation-theoretic statement for every odd prime p. Let G be the finite Heisenberg group of order p^3, with center C of order p and quotient U=G/C a two-dimensional F_p-vector space. Its commutator is a nondegenerate alternating pairing U x U -> C. Let rho:G->GL(A) be an irreducible complex representation of dimension p whose central character chi is nontrivial, and hence faithful on C.

Average any positive-definite Hermitian form over G. Then rho is unitary for the resulting form. This changes no eigenline or projective incidence.

**Trace lemma.** For g outside C, tr(rho(g))=0; for z in C, tr(rho(z))=p chi(z).

Indeed nondegeneracy of the commutator supplies h with hgh^(-1)=zg for some nonidentity z in C. Conjugation invariance of trace gives

       tr(rho(g)) = chi(z) tr(rho(g)).

Faithfulness gives chi(z)!=1, proving the first assertion. The second follows from the scalar central action. This proof neither chooses matrices nor evaluates an eigenvector.

For a line L in U, let A_L be its inverse image in G. It is a maximal abelian subgroup of order p^2. Its characters extending chi are exactly p in number: one extension exists for a character of a subgroup of a finite abelian group, and all extensions differ by a character of A_L/C, a group of order p. For such a character alpha the character projector is

       P_(L,alpha) = (1/p^2) sum_(a in A_L) alpha(a)^(-1) rho(a).

Because the operators are unitary and commute, this is the orthogonal projector onto the alpha-eigenspace. The trace lemma gives

       tr(P_(L,alpha))
          = (1/p^2) sum_(z in C) chi(z)^(-1) p chi(z)
          = 1.

Thus every one of the p character spaces has dimension one. They form an orthogonal decomposition of A, so the corresponding p projective eigenlines give an orthonormal basis after choosing arbitrary unit representatives. There are p+1 directions L.

Now let L and K be distinct lines in U and let alpha and beta extend chi on A_L and A_K. Expanding the product of the two abstract projectors gives

       tr(P_(L,alpha) P_(K,beta))
          = (1/p^4) sum_(a in A_L, b in A_K)
                alpha(a)^(-1) beta(b)^(-1) tr(rho(ab)).

The trace vanishes unless ab is central. If ab is central, the classes of a and b in U add to zero; since L and K are distinct one-dimensional subspaces, both classes must be zero. Hence exactly the pairs a,b in C contribute. For each such pair, the summand is

       chi(a)^(-1) chi(b)^(-1) p chi(ab) = p.

There are p^2 such pairs, and therefore

       tr(P_(L,alpha) P_(K,beta)) = 1/p.                 (1)

For arbitrary unit vectors u and v spanning these rank-one projector images, the left side is |<u,v>|^2. Consequently distinct eigenbases are mutually unbiased:

       |<u,v>| = 1/sqrt(p)                              (2)

when their directions differ. Within one basis distinct vectors are orthogonal. In particular (1) also excludes a repeated line between different bases, since a common rank-one projector would have product trace one, not 1/p.

Equations (1) and (2) are uniform consequences of the abstract group, its nontrivial central character, and its dimension. They do not depend on a choice of Schrödinger coordinates, root-of-unity matrices, an HM coefficient instance, or a numerical calculation.

## 4. Three eigenlines are independent for p>=5

Choose any three distinct eigenlines from the union of these p+1 bases, and any unit representatives v1,v2,v3. Their pairwise inner products have absolute value at most 1/sqrt(p), including the value zero when two belong to the same basis. For arbitrary complex numbers a1,a2,a3,

       ||a1 v1+a2 v2+a3 v3||^2
          >= sum_i |a_i|^2 - (2/sqrt(p)) sum_(i<j) |a_i| |a_j|
          >= (1-2/sqrt(p)) sum_i |a_i|^2.               (3)

The second inequality follows by adding the three elementary inequalities 2|a_i||a_j|<=|a_i|^2+|a_j|^2. For p>=5, the coefficient in (3) is strictly positive. Thus every nonzero coefficient triple has nonzero vector sum, and the three representatives are linearly independent.

Equivalently, every such abstract three-vector Gram form is positive definite by a uniform strict diagonal-dominance estimate. We do not construct or evaluate a selected Gram matrix. For the actual ambient representation p=5, three projective points would be collinear only if their representative vectors spanned a space of dimension at most two. Equation (3) excludes this. By Section 2, it excludes every three-node line of the actual primary surface, proving (a).

## 5. Finiteness and normalization of both cubic images

By input 2, every curve contracted by Phi would be the strict transform of a three-node line. Part (a) rules out all such lines, so Phi contracts no integral curve. Its restriction Phi_Y likewise contracts no curve.

Both morphisms are projective, because their sources are projective. Every positive-dimensional projective fiber over a closed point would contain an integral projective curve, for example by taking successive hyperplane sections of a positive-dimensional irreducible component. Such a curve would be contracted. Therefore all closed fibers are zero-dimensional. For these finite-type proper morphisms over C this implies quasi-finiteness: fiber dimension is upper semicontinuous, so any positive-dimensional fiber would give a positive-dimensional closed fiber. Proper quasi-finite morphisms are finite. This proves finiteness without asserting reducedness of any fiber.

Birationality of Phi and Phi_Y is independently proved in input 2, including its separate argument for the surface. The source M is smooth, since it is the blowup of P4 at distinct reduced smooth points. The source Y is smooth by input 2. In particular both sources are normal and integral.

A finite birational morphism from a normal integral scheme to an integral variety is its normalization morphism. One can see this on an affine open of the target: the source has a finite integral coordinate algebra B over A in their common function field. Since B is integrally closed, every element integral over A is integral over B and belongs to B. Conversely every element of B is integral over A. Thus B is exactly the integral closure of A. Applying this to both maps proves (b).

The conclusions identify the normalizations of the already known degree-51 fourfold V and degree-75 surface T. They do not change either degree.

## 6. Ample rather than merely nef and big

The morphism defined by the generated cubic line bundle satisfies

       O_M(D) = Phi^* O_V(1),
       O_Y(D|Y) = Phi_Y^* O_T(1).

The restrictions O_V(1) and O_T(1) are ample. Pullback of an ample line bundle by a finite morphism is ample. The finiteness proved in Section 5 therefore gives (c).

This is stronger than positive intersection with every curve taken in isolation: strict nefness alone would not justify ampleness. Here ampleness follows from the exact finite-morphism criterion, so no unproved cone criterion or special-fiber separation claim is needed.

As an immediate geometric check, if a projective line ell contains r nodes then r<=2, and its strict transform has D-degree 3-r, which is positive. In the case r=2, the restricted generated bundle is O_P1(1), so that strict transform maps isomorphically onto a projective line. This statement concerns each such curve individually; it does not assert that different curves have different images.

## 7. Scope and remaining boundary

The three-node-line possibility left open by PR602 is now absent everywhere in P4, not only on S. Consequently both resolved cubic maps are finite normalization maps, and their actual cubic polarizations are ample. The new representation proof is uniform in all nontrivial central characters and all dimensions p>=5 arising from these prime-order Heisenberg groups; the geometric application uses only p=5 and the pinned actual-node identification.

Nothing here identifies a normalization map with an isomorphism. Normality of V or T, separation of finite special fibers, infinitesimal separation, very ampleness of D or D|Y, and global extension of the quartic inverse remain separate questions. In particular a finite birational morphism can still fail to be an embedding. The primitive-four/full-adjoint gate, prescribed-source membership, higher lifting, and the original algebraicity problem are untouched. The proof is structural mathematics relative to explicit pinned inputs, not formal proof-assistant verification.
