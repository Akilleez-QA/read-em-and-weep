# The residual spinor defect is pure and has a rank-seven pushforward

## Result

Let T' be the residual defect, disjoint from C0, in INVARIANT-CONE-CONIC-FIRST-JET-AND-RESIDUAL-DEFECT.md. It has no zero-dimensional subsheaf or associated component. Negative linear projection induces a finite morphism on its support to P(W), and

    D = p_* T'

is exactly the equivariant vector bundle

    D=(A plus 2W-prime) tensor O_P(W)(2).

It has rank7, degree14, h0=21, H1=0. Its global representation is exactly

    H0(D)=1 plus A plus D5 plus 2T6.

In particular every ordinary splitting summand of D has degree exactly two. These statements do not identify the support of T' with the negative vertex line, and do not prove the positive rank33 gate.

## 1. Purity by the actual spinor resolution

The ambient resolution 0->2O_P4(-1)->2O_P4->i_*S->0 makes S maximal Cohen--Macaulay on the quadric threefold Q0, including along its vertex. The same holds for S(2), and E is locally free. At every closed point in Q0, these three sheaves have depth3. Apply the depth lemma to the exact sequences

    0 -> S -> E -> J -> 0,
    0 -> J -> S(2) -> T -> 0.

The first gives depth(J)>=2 and the second depth(T)>=1 wherever T is nonzero. Its support has dimension at most one, so it has no zero-dimensional associated point or isolated component and is Cohen--Macaulay of pure dimension one. The disjoint-support summand T' inherits this property. This is a proved refinement of earlier bookkeeping that retained possible zero-dimensional defect; it does not infer purity merely from a Hilbert polynomial.

## 2. The negative projection is finite on the residual support

The negative coordinates give a morphism p:P4 minus R -> P(W). Every fiber is affine three-space. Since T' is supported on Q0 and disjoint from C0=Q0 intersect R, its projective support lies entirely in this open set. The restriction of p to this support is proper, and each fiber is both affine and proper, hence zero-dimensional. A proper quasi-finite morphism is finite.

Because T' is pure, multiplication by a nonzero local base parameter on P(W) is injective on p_*T': its kernel would be a zero-dimensional subsheaf of T'. Thus p_*T' is torsion-free, hence locally free on the smooth base P1. The pullback of O_P(W)(1) is O_P4(1), so its Hilbert polynomial is the already proved 7t+21. For a rank-r degree-d bundle on P1 this polynomial is r(t+1)+d, proving rank7 and degree14. Finiteness preserves cohomology, so h0=21 and H1=0. By the splitting theorem on P1, H1=0 forces each line degree to be at least -1.

## 3. Exact global character, independent of the unknown primary scalar

The two spinor sequences give in the representation ring

    H0(T)=H0(S(2))-H0(E)+W' +H1(E).

The primary quadric restriction sequence gives the scalar-independent difference

    H1(E)-H0(E)=1+T6-W'.

Consequently H0(T)=H0(S(2))+1+T6. The weighted degree-five polynomial model gives

    H0(S(2))=Sym5(W')
              + Sym3(W') tensor W
              + W' tensor Sym2(W)
            = A+D5+2T6.

The reduced conic summand has H0(O_C0(5))=Sym5(W')=T6. Subtraction proves H0(T')=1+A+D5+2T6, hence the same for D. Semisimplicity of the finite group in characteristic zero justifies reading these exact-sequence differences as the actual representation.

## 4. The lower twists force the exact splitting

The normalized monad makes F(-1) acyclic, as explicitly recorded in LOWER-TWIST-EVEN-QUADRIC-PARITY.md. Since F*=F(1), Serre duality makes F(-3) acyclic as well. The same monad has H2(F(-2))=W-prime and no other cohomology; this is the coefficient W-prime of Omega² in its equivariant form. The rank-two restriction sequence therefore gives

    E(-3)=F_Q0(-1) acyclic,
    H1(E(-2))=A plus 2W-prime,
    H^i(E(-2))=0 for i not equal to 1.

The first assertion uses F(-3) and F(-1). The second uses H1(F)=A+W-prime and H2(F(-2))=W-prime, and the vanishing of the remaining ambient groups. The finite group is semisimple, so the resulting short extension splits at the representation level.

The spinor resolution makes S(-3),S(-2),S(-1) acyclic, while H0(S)=W-prime and all its higher groups vanish. Twist the two spinor sequences to obtain

    T(-3) acyclic,
    H0(T(-2))=A plus 3W-prime,
    H^i(T(-2))=0 for i>0.

The conic summand twists to O_P1(-1) and O_P1(1), respectively. Hence

    T'(-3) acyclic,
    H0(T'(-2))=A plus 2W-prime,
    H^i(T'(-2))=0 for i>0.

Finite projection preserves these statements for D. A bundle on P1 with acyclic twist by -3 has every splitting summand of degree exactly two: a line bundle is acyclic precisely in degree -1. Consequently evaluation of H0(D(-2)) is an equivariant isomorphism

    (A plus 2W-prime) tensor O_P(W)(2) -> D.

No assertion that the residual support lies on L was used. Indeed the finite-projection argument applies to any projective residual support disjoint from C0. The module action of the positive coordinates on this rank-seven bundle remains part of the geometric data and is not discarded.

## Limits and evidence

The depth argument permits nonreduced one-dimensional support and does not make S invertible at the vertex. The projection argument constrains a coherent sheaf, not merely its support cycle. The character computation is universal binary-icosahedral representation arithmetic; no actual bundle coefficient or multiplication rank is evaluated. Source inputs are the two companion cone-spinor and conic-first-jet proofs, and their exact primary-cohomology representations.
