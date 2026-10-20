> Publication scope: preserved mathematical proof/audit. Historical statements that rank eight remains open are superseded only after the final assembly and all its prerequisites. No source-instance evaluation or formal verification is claimed here.

# Rank five cannot have residual kernel degree two

## Result

Under the hypotheses of ../global-linear-image-plucker/PROOF.md and the normalizer irreducibility and perfectness proved in ../rank-nine-kernel-splitting/PROOF.md, generic rank(Q)=5 forces

    k=2, d=0, e=7.

In particular both previously allowed rank-five branches with residual kernel degree e=2 are impossible. The argument does not assert that a constant exterior lift is decomposable. It replaces that invalid inference with a small-Chern-class bound for a globally generated bundle.

## 1. A universal section bound

Let E be a globally generated vector bundle of rank six on complex P^4, with det(E)=O(2). If H^0(E*)=0, then

    h^0(E) <= 14.

Choose five general global sections of E. They give a sheaf injection O^5 -> E. Their rank-four degeneracy locus Z is either empty or a smooth surface, and there is no rank-three locus. Here is a direct justification of the generality statement: for each point x, evaluation from H^0(E)^5 onto Hom(C^5,E_x) is surjective. Consequently the universal rank-four stratum has codimension two, while the locus of rank at most three has codimension six. Generic smoothness over C and the dimension count, together with properness of P^4, show that a general choice has a smooth codimension-two rank-four locus or an empty locus, and no rank-three points.

The cokernel is I_Z(2). Locally at a rank-four point, elementary invertible operations reduce the map to four identity blocks and a column (f,g) into a free rank-two module. Smooth codimension two means f,g are a regular sequence; the cokernel of that column identifies with the ideal (f,g). The determinant identifies the line twist globally as det(E)=O(2). Thus

    0 -> O^5 -> E -> I_Z(2) -> 0.

If Z is empty, this sequence splits because Ext^1(O(2),O)=H^1(O(-2))=0. This contradicts H^0(E*)=0. Hence Z is a nonempty surface.

A nonempty projective surface imposes at least six independent conditions on quadrics. Indeed, choose one irreducible surface component Y with its reduced structure. Linear Noether normalization gives three linear forms algebraically independent in the homogeneous coordinate ring of Y. Their six degree-two monomials are linearly independent. The restriction map H^0(O(2)) -> H^0(O_Z(2)) therefore has rank at least six. Consequently

    h^0(I_Z(2)) <= 15-6=9,
    h^0(E) = 5+h^0(I_Z(2)) <=14,

where the equality uses H^1(O)=0. This proves the bound.

## 2. The exterior lift produces a genuine global subbundle

Write W=Sym^2 V, dim(W)=15. Suppose the generic kernel has dimension six and its primitive Plucker vector kappa has degree two. The low-degree lifting theorem in ../low-degree-kernel-lifting/PROOF.md gives

    kappa(u)=u^2 wedge a,       a in Lambda^5 W.

The kernel determinant linearization has no character ambiguity because N is perfect. Equivalently the primitive degree-two kernel coordinates can be chosen N-equivariantly with their natural O(-2) linearization. Averaging a therefore gives an N-invariant lift with the same nonzero kappa.

Consider the linear wedge-annihilator

    L(a)={w in W : w wedge a=0}.

It is N-stable. It is proper: if every basis vector wedged with a were zero, every coefficient of a would be zero, since 5<15. Also a is nonzero because kappa is nonzero. Irreducibility of W therefore forces L(a)=0.

Thus kappa(u) never vanishes for u nonzero. It is decomposable on the dense open set of generic kernel definition, so the closed Plucker equations show that it is decomposable everywhere. It defines a morphism P^4 -> Gr(6,W) and a rank-six subbundle

    K subset W tensor O,       det(K)=O(-2).

Its determinant is O(-2) because the nowhere-zero degree-two Plucker vector is precisely its determinant line inclusion. The condition u^2 wedge kappa(u)=0 also shows that K contains the canonical O(-2) square line everywhere. No decomposability of a is used.

If desired, K identifies with the actual saturated kernel sheaf: both are saturated subsheaves of W tensor O with the same generic fiber. This identification is not needed for the contradiction.

## 3. Irreducibility contradicts the section bound

Put E=K*. The subbundle inclusion makes E a globally generated rank-six bundle, with det(E)=O(2).

The space H^0(K) is an N-stable subspace of H^0(W tensor O)=W. It cannot equal W because K has rank six, so irreducibility gives H^0(K)=0.

The global sections coming from the surjection W* tensor O -> E give an N-equivariant map

    W* -> H^0(E).

This map is nonzero, since it globally generates a nonzero bundle. Its kernel is an invariant subspace of the irreducible W*, so the map is injective. Therefore h^0(E)>=15. Section 1 instead gives h^0(E)<=14, a contradiction.

## 4. Consequence for the determinant table

At generic rank five the previous table allows:

    (k,d,e)=(2,0,7), (2,5,2), or (7,0,2).

The two e=2 branches are excluded. Only (k,d,e)=(2,0,7) remains. In particular the maximal minors have no common divisorial factor, and det(I)=O(7-k)=O(5).

This is a conditional restriction, not a proof of generic rank five or its exclusion. Only universal bundle geometry, existing equivariance and irreducibility, and finite-group averaging are used. No actual HM source matrix, operation product, input, polynomial instance, rank instance, jet, or residue is evaluated. No external writes or computations are involved.
