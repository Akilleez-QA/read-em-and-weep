# Global intersections of the primary closure with coordinate components

Work over C. Let R=C[x_1,...,x_5,y_1,...,y_5,z_1,...,z_5], let P=I_2([x y z]), and let Q be the isolated primary ideal defined by the universal square-zero substitution in `../global-rank-one-primary-closure/PROOF.md`. Use the proven exact generation theorem `../primary-graded-geometry/GENERATORS.md`:

    Q=(Q_3)+P^2,

where every element of Q_3 has column multidegree (1,1,1). Let C_x=V(x_1,...,x_5), and define C_y,C_z similarly. All statements below concern Y=V(Q), not a classification of the full scheme X=V(J).

## 1. Exact scheme intersections, including the original vertex

In S=C[y_1,...,y_5,z_1,...,z_5], put I=I_2([y z]). Reduction modulo (x) annihilates Q_3 and carries P onto I. A ring homomorphism carries the square of an ideal onto the square of its image. Consequently

    (Q+(x))/(x)=I^2,
    Y ∩ C_x = Spec(S/I^2).

This is an equality of global ideals, not merely an equality on the punctured cone or after saturation. The same assertion holds for the other two coordinate components.

Putting two columns equal to zero annihilates every generator of Q. Therefore

    Y ∩ C_x ∩ C_y = C_x ∩ C_y = A^5_z

as reduced schemes, and similarly for the other two pairs. The intersection with all three coordinate components is the reduced origin. Equivalently, the pairwise scheme intersections of Y∩C_x, Y∩C_y, Y∩C_z inside Y are these reduced affine 5-spaces; their triple intersection is the reduced origin. This reduction at further intersection is compatible with the nonreduced individual boundary intersections: the quotient by another whole column kills their nilpotent minor classes.

## 2. A vertex-safe conormal calculation for the five-by-two cone

Let U have dimension five, W dimension two, S=Sym(U⊗W), A=S/I, B=S/I², and N=I/I². By the characteristic-zero Cauchy decomposition,

    S_d = ⊕_{lambda ⊢ d, length(lambda)≤2} S_lambda U ⊗ S_lambda W.

Write E_lambda for each summand. The degree-four piece of I² is exactly E_(2,2). Indeed, the minor space is Λ²U⊗Λ²W; its symmetric square maps only to E_(2,2) in S_4, and the square of a formal two-by-two minor gives a nonzero highest-weight vector. The Cauchy–Pieri ideal multiplication rule used and proved in the referenced generation theorem then gives

    I² = ⊕_{lambda containing (2,2)} E_lambda.

In particular

    A_d = E_(d),
    N_d = E_(d-1,1) for d≥2;  N_0=N_1=0.

Unlike the five-by-three case, there is no third-row summand E_(1,1,1), and thus no surviving three-minor vertex torsion.

For completeness this representation calculation identifies the actual graded module, not just its Hilbert function. Put T=P^4×P^1 and L=O(1,1). The conormal bundle of this Segre embedding is

    F=Ω^1_{P^4} ⊠ Ω^1_{P^1}.

The normal derivative of minors defines an A-linear graded map

    N → ⊕_{d∈Z} H^0(T,F⊗L^d).

Euler's sequence identifies the target degree d≥2 with E_(d-1,1), and all target degrees below two vanish. On each source summand the map is nonzero: a minor multiplied by a power of a coordinate has nonzero first normal derivative along the rank-one cone. Equivariance and irreducibility therefore make this map an isomorphism degree by degree, hence an isomorphism of graded modules. This proves equality with the full section module at the vertex as well.

## 3. Primary nilstructure, dimension, and multiplicity

The section module N just obtained is torsion-free over the domain A: multiplication by a nonzero homogeneous section is injective on sections of a vector bundle over the integral scheme T; equivalently the section module embeds in its generic fiber over A. Its rank is rank(F)=4.

The exact sequence

    0 → N → B → A → 0

has N²=0. If b∈B has nonzero reduction a∈A and bc=0, reduction first gives c∈N, and torsion-freeness then gives ac=0 ⇒ c=0. Thus every element outside the nilradical is regular; every element of the nilradical is square-zero. It follows that I² is I-primary. In particular this intersection has no embedded component at the original vertex.

The reduced cone is the six-dimensional affine Segre cone over P^4×P^1. Away from its vertex it is smooth, regularly embedded in A^10 with codimension four. There the thickening is its first infinitesimal neighborhood, with locally free square-zero conormal of rank four. It is locally Cohen–Macaulay of type four at every nonvertex point: locally choose the six reduced smooth parameters and four regular normal parameters; after quotienting by a system of parameters the square-zero normal algebra has four-dimensional socle. At its generic point B has length 1+4=5. The reduced Segre cone has degree binomial(5,4)=5; the associativity formula gives

    dim B=6,  generic multiplicity=5,  degree B=25.

The vertex Hilbert–Samuel multiplicity is likewise 25, since B is standard graded. Its embedding dimension is ten. Its defining ideal starts in degree four, with fifty independent quartic minimal generators E_(2,2); therefore its vertex tangent space and tangent relations through degree three fill those of affine 10-space. These statements do not assert a global algebra splitting B=A⊕N.

The intersections with two coordinate components have dimension five, generic length one, and degree one. The triple intersection has dimension zero and length one.

## 4. Exact vertex depth: three, not six

Let m=A_+ (or its inverse image in B). Because N is the full section module of F, its local cohomology satisfies

    H^0_m(N)=H^1_m(N)=0,
    H^i_m(N)_d = H^{i-1}(T,F⊗L^d) for i≥2.

Euler's sequence on P^4 gives the following sufficient cohomology facts for Ω^1(d): for d≥2 only H^0 can occur; d=1 is acyclic; at d=0 the only cohomology is H^1=C; and for d<0 only H^4 can possibly occur. On P^1, Ω^1(d)=O(d−2): its H^0 occurs for d≥2, H^1 for d≤0, and d=1 is acyclic. Künneth therefore yields

    H^1(T,F⊗L^d)=0 for every d,
    H^2(T,F)=H^1(P^4,Ω^1)⊗H^1(P^1,Ω^1)=C.

Thus H^2_m(N)=0 and H^3_m(N)_0=C, so depth_m N=3. The Segre coordinate ring A is Cohen–Macaulay of dimension six: this follows directly from the analogous line-bundle Künneth computation, which has no intermediate cohomology for O(d,d), together with projective normality. Applying local cohomology to 0→N→B→A→0 gives

    H^i_m(B) ≅ H^i_m(N) for i<6,
    depth_m B=3.

More precisely H^3_m(B) is a single copy of C in degree zero, while H^4_m(B)=H^5_m(B)=0. All local-cohomology functors in this exact sequence can be computed using the same coordinate-generated ideal S_+ and its images in A and B. Its image in B is the vertex maximal ideal, so these are also the local-cohomology and depth statements for the local ring B at the original vertex. Thus the failure of Cohen–Macaulayness is isolated at the vertex, despite primaryness and the absence of embedded components.

One may additionally record the exact Hilbert series, obtained from the degreewise decomposition in §2 and Euler's sequence:

    H_B(t)=(1+4t+10t²+20t³−15t⁴+6t⁵−t⁶)/(1−t)^6.

For d≥2 the Hilbert function used here is

    dim B_d = (d+1) binomial(d+4,4)
              +(d−1)[5 binomial(d+3,4)−binomial(d+4,4)].

Degrees zero and one have dimensions 1 and 10. The numerator evaluates to 25 at t=1, agreeing with the independent generic-length degree calculation.

## 5. Scope relative to the full trilinear scheme

For the original trilinear equations J, all equations vanish upon setting any one whole column to zero. Thus X∩C_x=C_x as schemes (and similarly for y,z), whereas the isolated primary component intersects C_x in the proper six-dimensional nonreduced determinantal thickening above. The individual coordinate spaces have dimension ten. The calculation describes the scheme intersection of distinct components and how the primary rank-one closure meets them; it does not equate this intersection with the full local structure of X or rule out other components or embedded structure of J.

Only abstract polynomial rings, representation theory, sheaf cohomology, and exact ideal manipulations enter. No source operations, actual input matrices, or rank evaluations are used.
