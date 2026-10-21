# Intertwining the two plane boundaries and their square subbundles

Retain the actual negative hyperplane pencil T=P(W*), the positive fixed plane R=P(V), and B=End_0 F. The uniform cohomology theorems give exact sequences

    0 -> E4,+ -> H0(B_R(4)) O_T -> D_lin(1) -> 0,
    0 -> G    -> H0(B_R(5)) O_T -> C_lin(2) -> 0,

with source dimensions 30 and 48, respectively. Here E4,+ has rank 17 and degree -54, while G has rank 43 and degree -36.

## 1. An actual surjective cohomology multiplication

Positive linear multiplication is everywhere surjective on the indicated hyperplane cohomology:

    V* tensor H1(B_H(3))_- -> H1(B_H(4))_-.

Relatively this is a surjective bundle map

    V* tensor D_lin -> C_lin(1).                     (1)

Its kernel has rank 34 and degree 92. Equivalently, before untwisting the plane-boundary normal factor, the map

    V* tensor D_lin(1) -> C_lin(2)

has a kernel of degree 126.

Indeed the actual plane Steiner resolution shows that

    V* tensor H0(B_R(4)) -> H0(B_R(5))                (2)

is onto. In detail, at twists four and five its right-hand presentations are obtained from

    A tensor D tensor O_R(t-4)
       -> Sym^2 D tensor O_R(t-3) -> B_R(t) -> 0

with the left kernel Lambda^2 A tensor O_R(t-5). For t=4,5 the relevant higher cohomology does not create an additional cokernel, and multiplication V* tensor H0(O_R(1))->H0(O_R(2)) is onto. Thus every section in twist five comes from (2).

Naturality of the connecting homomorphisms gives the commutative square

    V* tensor H0(B_R(4)) O_T  ->  H0(B_R(5)) O_T
                  |                         |
                  v                         v
    V* tensor D_lin(1)         ->  C_lin(2).

Both vertical arrows and the upper arrow are onto. Hence the lower arrow is onto. This is a consequence of the actual boundary maps and the plane resolution, not a generic rank assertion about a map with these dimensions.

## 2. Canonical constant-rank square subbundles

The actual hyperplane section bundle is Y=W tensor O_T(-3), and its symmetric square is A tensor O_T(-6), where A=Sym^2 W. Restricting the actual three squares to R gives a morphism

    a: A tensor O_T(-6) -> H0(B_R(3)) tensor O_T.

For every parameter, its three sections form a basis of B_R(3) at the generic point of R. To see this, let s,t be the two actual sections of F_H(2). Their restrictions to R have determinant the actual nonzero plane cubic. They are therefore a basis of F_R(2) over the function field of R; their three symmetric squares are a basis of Sym^2 F_R(2)=B_R(3) over that field.

It follows that, for every nonnegative integer d, polynomial multiplication gives a fiberwise injective map

    A tensor H0(O_R(d)) tensor O_T(-6)
        -> H0(B_R(d+3)) tensor O_T.                  (3)

This uses only the absence of a polynomial relation among a rational basis. In particular there is no selected coefficient or rank evaluation. Fiberwise injectivity on the parameter curve makes (3) a subbundle inclusion.

For d=1, each section in (3) extends to the same hyperplane by multiplying its actual square by a positive linear form. Its plane boundary therefore vanishes. For d=2 the same statement holds with a positive quadratic. Consequently there are exact sequences of vector bundles

    0 -> (A tensor V*) O_T(-6)
      -> E4,+ -> Q4 -> 0,

    0 -> (A tensor Sym^2 V*) O_T(-6)
      -> G -> Q5 -> 0,                               (4)

where

    rank(Q4)=8,     degree(Q4)=0,
    rank(Q5)=25,    degree(Q5)=72.

These quotients need not be trivial or balanced. In particular degree zero does not imply Q4 is trivial.

## 3. Scope for the smoothing problem

Equations (1) and (4) constrain the actual plane-boundary kernels. They explain geometrically why the boundary annihilates positive quadratics times the moving square at its own parameter. The six-dimensional divided-difference or Hermite smoothing input instead involves polynomial-division quotients mixing parameters and, at doubled roots, their full jets. None of the statements here identifies those mixed inputs with the subbundles in (4), nor proves that they escape G. The remaining compatibility problem is not replaced by a generic bundle map.

Dependencies: SURJECTIVE-PLANE-BOUNDARY-BY-CONIC-RESIDUALS.md; UNIFORM-TWIST-FOUR-FIVE-HYPERPLANE-COHOMOLOGY.md; EXACT-HYPERPLANE-ADJOINT-SYZYGY-BUNDLE.md; the actual determinant-cone theorem and the plane Steiner resolution.
