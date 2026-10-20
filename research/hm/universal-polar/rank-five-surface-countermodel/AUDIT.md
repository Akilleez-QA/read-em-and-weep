# Prior mathematical audit

This audit concerns the source manuscript. It is not a formal verification or a review of later normalized publication bytes.

# Independent audit of the isolated rank-five construction

## Verdict

The frozen `PROOF.md` is correct as stated. The construction establishes a
global repeated-input-injective quotient with residual rank five at one
middle line, residual rank ten everywhere else, and a nonempty
two-dimensional separately projectivized independent-zero fiber over the
exceptional line. No repair to the proof is required.

This audit checks the abstract argument only. It performs no evaluation
of the source operation, no source-rank computation, and no numerical or
symbolic computational experiment. The only new artifact is this review.

## 1. The ternary symmetric kernel and its rank strata

The functional ell corresponds to a nondegenerate symmetric form on the
three-dimensional space E0, so K_res has dimension five. Its projective
rank-one locus is the Veronese image of the isotropic conic and has
dimension one. The proof correctly distinguishes that degree-four curve
in P(K_res) from the original plane conic.

The claimed description of the rank-two locus T is valid. For every
covector line [lambda], restriction of ell to Sym²(ker lambda) is
nonzero: a totally isotropic two-plane would have to be contained in its
one-dimensional orthogonal complement. Its kernel therefore forms a
rank-two vector bundle R. Every projective-line fiber of P(R) contains
rank-two forms, because the rank-one binary forms constitute a conic
containing no line. On the rank-two open, the kernel covector is unique
and algebraic. Thus T is indeed smooth, irreducible, and of dimension
three.

## 2. Simultaneous choice of the correction v

Both generic conditions are established, including the necessary
dominance argument.

- On each nonzero square line, v(e²) in Ce imposes two independent
  linear conditions on Hom(K_res,E0). The bad incidence is a rank-13
  vector bundle over a projective curve. Its image is closed and has
  dimension at most 14 inside the 15-dimensional parameter space.
  Hence square avoidance is genuinely nonempty open.
- On each rank-two tensor line, v(q) in im q imposes one independent
  linear condition. The universal compatibility incidence is a smooth
  irreducible rank-14 vector bundle over T, of dimension 17.
- At the chosen pair (q0,v0), the equation
  lambda(q)(v(q))=0 has nonzero derivative in a q-direction. The term
  involving the derivative of lambda vanishes because v0(q0)=0.
  Therefore the projection to the 15-dimensional parameter space has
  surjective differential, is smooth at that point, and is dominant.
- A dominant finite-type morphism has a dense constructible image;
  thus one may first take a nonempty open contained in the image and
  then use the generic-fiber dimension theorem. This justifies
  nonempty fibers of dimension 17−15=2 without any improper assumption
  of properness.

The two parameter opens intersect because the parameter space is
irreducible. The proof also correctly avoids asserting that its special
witness v0 itself satisfies the square-avoidance condition.

For clarity, the argument does not need irreducibility of the eventual
surface or its double cover. If desired, one could shrink the parameter
open further by generic smoothness in characteristic zero to obtain a
smooth compatibility locus pure of dimension two, but this additional
claim is not used in the frozen proof.

## 3. Tensor normalization and support

The symmetric-algebra convention is consistent throughout. In
particular,

    M(ab) = (ab^T + ba^T)/2,
    B0_u(ab) = a ⊗ (u∧b) + b ⊗ (u∧a).

Consequently the graph tensor B0_u(q)−A0_u(v(q)) has the exact block
matrix shown in the proof: the first row is −v(q)^T and the remaining
block is 2M(q). Its second-factor support is
u∧(im q+Cv(q)).

For rank-one q, square avoidance makes this support two-dimensional.
For rank at least two it is automatically at least two-dimensional.
Thus P(L) avoids the entire rank-one tensor variety X, including the
otherwise dangerous rank-one points of P(K_res).

The argument L∩F_a=0 away from [u] is uniform and sound. Two independent
support bivectors u∧w1 and u∧w2 can both belong to a∧V only if a lies
in both span(u,w1) and span(u,w2), hence in Cu. This uses only tensor
support, so no unnoticed assumption about symmetric matrix rank enters
that step.

## 4. Quotient-kernel incidence bounds

All dimensions and openness arguments are correct:

    dim(W/L)=35,
    dim Gr(15,35)=300,
    dim Gr(14,34)=280,
    dim(F_u/L)=9.

The repeated-input bad incidence has dimension at most 7+280=287.
The uniform other-middle incidence has dimension
4+13+280=297. Each is strictly smaller than 300.

For the other-middle incidence, the proof correctly removes the
closure of its constructible image. This is necessary because the
middle base P(V) minus [u] is not proper, and the closure still has
dimension at most 297. The resulting nonempty open is therefore
legitimate. It intersects the other required opens in the irreducible
Grassmannian.

These conditions give exactly K_tot∩F_u=L and K_tot∩F_a=0 away from
[u]. Since the repeated-input image has dimension four everywhere,
the residual-rank formula is

    rank Q_a = 10−dim(K_tot∩F_a).

It yields five at [u] and ten everywhere else, with kernel K_res at
the exceptional point. The graph relation becomes exactly
B_u(q)=A_u(v(q)); there is no missing sign or factor of two.

## 5. Factor reconstruction and final dimensions

An independent outer pair has a rank-two residual product. If that
product lies in K_res⊂Sym²E0, its two residual factors belong to E0,
because their span is the contraction image of the product.

For q=ab and v(q)=nu a+mu b, the expansion

    f(a+alpha u,u,b+beta u)
      = A_u(v(q)+beta a+alpha b)

shows that the unique zero lifts for that ordered factorization are
a−mu u and b−nu u. Their residual vectors remain independent, so the
three reconstructed inputs are independent. Conversely every
independent zero has this form.

Over the rank-two locus, the two ordered factorizations form the usual
finite étale degree-two cover of a nondegenerate binary quadratic.
Restricting to C_v and applying the reconstruction therefore preserves
dimension and gives exactly the exceptional projective fiber. Its
dimension is two. There are no independent zeros over other middle
lines, because their residual maps are injective.

Restoring the three independent nonzero input scales gives a
(G_m)^3-torsor and affine dimension five. Fixing an actual middle
vector restores only the two outer scales and gives affine-fiber
dimension four. These counts use separate projectivization and do not
confuse it with quotienting by one common scalar.

## 6. Limits of the result

The proof appropriately makes no claim of a two-dimensional middle
family, a seven-dimensional affine component, normalizer equivariance,
or occurrence in the actual source operation. It rules out the stated
pointwise fiber bound under the coarse hypotheses, while leaving the
global affine bound six untouched.

All final dimensions can be read on reduced supports. Possible
nilpotents in the global zero scheme or the rank-drop scheme do not
affect these dimensions, and no unjustified reducedness assertion is
made. No compactification or K3 claim is included in this audit.
