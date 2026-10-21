# The residual Picard tori and the integral obstruction to averaging

Status: authored structural proof, independently mathematically reviewed in REVIEW.md; not formally checked. Work over C. No selected actual HM/source coefficient, matrix, rank or numerical instance is evaluated.

## 1. Actual geometric inputs

Let ν:X→S be the normalization of the actual primary surface, π:X→B=P¹ its modular elliptic fibration, h:B→Γ the normalization of the six-nodal canonical decic, and g:S→Γ the residual morphism, with gν=hπ. The exact dependencies are:

- PR574, commit **3c92fdc469f6870520e7a9d905b5ab9199a5bf37**, `research/hm/primary-conductor/PROOF.md`: X is smooth projective with H¹(X,O_X)=0; the conductor downstairs is the reduced set Z of thirty points, and upstairs it is W, the sixty reduced preimages. The two branches at every z∈Z are glued by their residues, and there are no other identifications.
- PR577, commit **563fc7036faa4965e55bda3bec5b82ae5360fa6c**, `research/hm/residual-fibration-defect/PROOF.md`: the six nodes q of Γ each have two cusp preimages a_q,b_q∈B and exactly five points Z_q⊂Z above them. At each z∈Z_q, its two preimages lie respectively over a_q and b_q. The additive normalization map repeats the same branch-residue difference at those five points.
- PR580, commit **ed98761a44412318a47740b9bd49119af690a255**, `research/hm/residual-duality/PROOF.md`: the canonical five-point average on conductor differences and its dual canonical-residue trace splitting. The Picard computation below is multiplicative and does not follow merely from this vector-space splitting.
- PR571, commit **25afc8bfce079492b6b06bb6f52489f8d481c2aa**, `research/hm/affine-residual-generation/PROOF.md`, dictionary and §1: the actual projective translation subgroup G=H₅/μ₅≅(Z/5)² acts fiberwise on X, fixes B pointwise, and rotates the components of every I₅ fiber transitively. This is the actual subgroup under the primary coordinate identification, not an inference from an abstract configuration.

We determine Pic⁰(S), Pic⁰(Γ) and their pullback map; construct a canonical norm isogeny decomposition; and prove that canonical linear averaging does not extend to an algebraic group retraction, although it extends to every formal order. The last statement concerns these Picard groups alone, not the separate HM deformation problem.

## 2. Picard tori from finite pinching

The conductor square

    W → X
    ↓   ↓ν
    Z → S

is a pinching square. Algebraically, the conductor ideal gives the fiber-product equality O_S=ν_*O_X ×_{ν_*O_W} O_Z. This can be checked in the actual local rings by their residue gluing, or after faithful flat completion using the transverse double-point rings of PR574. It is an equality on S, not just on its reduced support.

For the Picard functor of a finite pinching of a projective geometrically integral variety, the unit-group quotient is the kernel of pullback to the normalization. This is the exact sequence of Michel Brion, *Which algebraic groups are Picard varieties?*, arXiv:1310.0186v2, Corollary 2.3 and Proposition 2.4(iii), printed pp5–6:
https://arxiv.org/pdf/1310.0186v2
The hypotheses hold here: W and Z are nonempty finite reduced C-schemes, their map is finite and surjective, and X is projective and geometrically integral. The induced map of unit groups is a closed immersion with torus quotient. Thus the assertion applies to group schemes, not merely to their C-points.

In this square the unit groups of W and Z are Gm^60 and Gm^30, with the latter diagonally embedded in each pair. Consequently

    ker[Pic(S)→Pic(X)] ≅ Gm^60/Gm^30 ≅ Gm^30.          (1)

A concrete coordinate is the ratio of the two gluing identifications at a point z. Reversing the order of its branches inverts this coordinate. Automorphisms of the trivial line bundle on connected projective X are constant scalars and act on both sides equally, hence do not change these ratios. There is no further quotient by a global Gm in (1). This cancellation is functorial after base change: the proper geometrically integral X has global functions equal to the base ring, so automorphisms of the pulled-back trivial bundle again act by the same unit on both members of every pair. Equivalently the pinching Picard-functor exact sequence already incorporates these automorphisms.

Since X is smooth projective and H¹(X,O_X)=0, its connected Picard variety is trivial. For example the tangent space of Pic(X) at the identity is H¹(X,O_X)=0; the identity component is consequently a reduced point. The torus in (1) is connected, while the image of Pic⁰(S) lies in Pic⁰(X). It follows that

    P := Pic⁰(S) ≅ Gm^30.                             (2)

Applying the same pinching computation to twelve points of B=P¹ glued in six pairs gives

    A := Pic⁰(Γ) ≅ Gm^6.                              (3)

These tori have intrinsic descriptions as pairwise unit quotients; the displayed coordinates require branch orientations but the underlying group schemes do not.

## 3. The actual pullback is a fivefold diagonal

Choose, for each q, an ordering (a_q,b_q) of its two normalization branches. Orient the branches at all five z∈Z_q using their images a_q,b_q. A line bundle in A is the trivial bundle on B glued with a ratio t_q∈Gm at the node q. Pulling back along g makes the same identification at each of the five surface points above q. Thus the actual pullback j=g*:A→P is

    j((t_q)_q)=(t_q)_{q,z∈Z_q}.                      (4)

It is a closed immersion. Its differential is exactly the diagonal additive map on the corresponding normalization quotients. Indeed a ratio 1+εu has first-order difference u, and (4) repeats u at all five marks.

Define a morphism of algebraic groups

    N:P→A,       N((x_z)_z)_q=∏_{z∈Z_q}x_z.          (5)

This is canonical relative to g and the actual pairing: an ordering of the five surface points is unnecessary, and reversing (a_q,b_q) inverts every x_z and the target t_q, leaving the intrinsic map unchanged. This is a norm on the gluing tori, not a claim that the nonflat positive-relative-dimensional map g has a usual finite-flat norm on all line bundles.

Equations (4)–(5) give

    N∘j=[5]_A.                                      (6)

The kernel B₀:=ker N is a connected torus of dimension24. In each five-coordinate block, solving x_5=(x_1x_2x_3x_4)^{-1} identifies its kernel with Gm^4. No choice is needed to define B₀; a choice only writes its coordinates.

Multiplication gives a canonical homomorphism

    Φ:A×B₀→P,       (a,b)↦j(a)b.                    (7)

It is surjective: for x∈P, choose a fifth root a of N(x), then b=j(a)^{-1}x belongs to B₀. This argument establishes surjectivity as a morphism of tori, or as an fppf sheaf map; it does not choose roots canonically. Its kernel is

    {(a,j(a)^{-1}): a∈A[5]} ≅ μ₅^6.                 (8)

Thus Φ is an isogeny of degree 5^6, finite étale over C. This is the precise canonical replacement for a product decomposition by these two distinguished subtori. In particular j(A)∩B₀=j(A[5]) is not trivial, so (7) is not an isomorphism.

## 4. The actual translation symmetry and an integral obstruction

The group G fixes B pointwise and hence Γ pointwise. It therefore acts trivially on A. It acts transitively on each Z_q: by PR571 its action on the dual graph of either I₅ fiber is the nontrivial order-five rotation, which is transitive on the five vertices as well as on the five components. PR577 identifies each such vertex bijectively with one point of Z_q. The normalization and its pairing are equivariant, so this is the action on the actual surface nodes. Because G fixes a_q and b_q individually, it preserves their orientations and only permutes the five gluing coordinates, without inversion. The action on the Picard gluing ratios is precisely this permutation action; changing a trivialization on connected X multiplies both branch values by the same scalar and has no effect.

Suppose an algebraic group retraction r:P→A were G-equivariant and rj=id_A. Every character of a split torus is a Laurent monomial with integer exponents. Write its q-th output character as

    r_q(x)=∏_{p}∏_{z∈Z_p} x_z^{n_{q,p,z}},
    n_{q,p,z}∈Z.

This classification also follows directly: an invertible regular function in a Laurent polynomial ring is a nonzero scalar times a Laurent monomial, and the homomorphism law forces the scalar to be1. Equivariance, since the target action is trivial and G is transitive on each Z_p, forces n_{q,p,z}=n_{q,p}, independent of z. Restricting to j(A) then gives

    (rj)_q(t)=∏_p t_p^{5n_{q,p}}.

The identity would require 5n_{q,q}=1 and 5n_{q,p}=0 for p≠q. This is impossible in Z. Therefore

    there is no G-equivariant algebraic group retraction of j.  (9)

This does not assert that j has no algebraic retraction at all. Choosing one point z_q from each Z_q and setting r_q(x)=x_{z_q} gives a non-equivariant algebraic retraction. The obstruction is the symmetry-compatible integral character lattice, not a failure of the underlying torus exact sequence to split abstractly.

## 5. Canonical tangent and formal splitting, but no algebraic averaging

Differentiating (6), the canonical map

    r_Lie=(1/5)dN: Lie(P)→Lie(A)                    (10)

is a retraction of dj. It averages the five additive gluing parameters at each node, is G-invariant, and gives

    Lie(P)=dj(Lie(A)) ⊕ Lie(B₀),
    dim Lie(A)=6,   dim Lie(B₀)=24.

Under the tangent-space identification Lie(Pic⁰(Y))=H¹(Y,O_Y), this is the actual canonical average of the conductor residues. It is dual to the average-residue trace section for the canonical duality calculation. No independent equality with the full-adjoint twenty-dimensional boundary is asserted.

In fact (10) has a unique extension to a homomorphism of the formal groups at the identity. Write x_z=1+u_z in the completed torus, and define

    r̂_q((1+u_z)) = exp((1/5)Σ_{z∈Z_q}log(1+u_z)).  (11)

The characteristic-zero formal series converge in the maximal-ideal-adic topology; on Artinian nilpotent test rings they truncate. The formal logarithm turns multiplication into addition, so (11) is a formal group homomorphism, is G-invariant, and satisfies r̂∘ĵ=id. Equivalently it is the unique fifth root of N congruent to1. Formal logarithms also show uniqueness with the specified differential: an additive formal group homomorphism in characteristic zero is linear, as comparison of homogeneous terms in f(x+y)=f(x)+f(y) shows.

However no algebraic group homomorphism P→A has differential r_Lie. Its matrix in the gluing character coordinates would have entries1/5 in each own block and0 elsewhere, whereas the differential of an algebraic torus homomorphism is its integer exponent matrix. This gives a stronger formulation of the obstruction than (9): the specific averaged differential does not extend to a global algebraic group homomorphism P→A, even without imposing equivariance separately.

The formal fifth roots in (11) are algebraic power series, satisfying y_q^5=N_q(x). They do algebraize étale-locally near the identity: use the finite étale cover P×_{N,A,[5]}A and its point (1,1); its completed local branch gives exactly (11). No failure of local or étale algebraization is claimed.

Thus the canonical averaging extends through every infinitesimal order of these Picard tori, and exists étale-locally, but not as a global algebraic group retraction. The isogeny (7), with its explicit μ₅^6 kernel, measures the integral discrepancy.

## 6. Contribution and boundaries

This determines the actual connected Picard groups and residual pullback, rather than inferring a group decomposition from H¹ dimensions. It identifies the canonical norm, connected rank24 kernel and degree5^6 isogeny, and locates the exact obstruction to symmetry-preserving algebraic averaging in divisibility by5 in the character lattice. At the same time it supplies the formal retraction to all orders, so a first-order/global distinction is proved rather than merely cautioned about.

The assertion is entirely about Picard tori of the primary surface and its residual curve. It neither proves nor disproves algebraicity of the original HM repair, does not identify its deformation functor with a Picard functor, does not settle the full δ20 boundary, and does not evaluate any selected source instance. Mathematical verification is separate from formal proof-assistant checking.
