# Outer quotient bundle and determinant twist

Work over C, with dim V=5, dim J=20, X=P(V), and L=O_X(-1). Assume only outer symmetry and cyclic zero.

The global quotient bundle and the order of its canonical relation

Define F_0:L⊗V⊗V→J⊗O_X by

    F_0(u⊗p⊗q)=f(p,q,u).

The morphism κ:L²⊗V→L⊗V⊗V is canonically

    κ(u²⊗v)=u⊗(u⊗v+2v⊗u).

Its composition with F_0 is f(u,v,u)+2f(v,u,u)=0. The coefficient order matters: with this slot convention the swapped expression 2u⊗v+v⊗u would map to −3A_u(v), which is generally not zero. Only an overall nonzero scalar can be changed harmlessly.

The map κ is a subbundle injection. Locally split V⊗O=L⊕E. Writing v=λu+w, its inner two-factor tensor is

    3λ u⊗u+u⊗w+2w⊗u.

Its three displayed components lie in distinct direct summands, and vanishing forces λ=w=0. Local frames therefore split the injection. Its quotient C is locally free of rank 25−5=20, and F_0 descends to Φ:C→J⊗O.

This identifies a canonical rank-five subbundle contained in ker F_0. It does NOT assert that this is the entire actual kernel at every line. Equality of the actual fiber kernel with this subbundle holds precisely where Φ is invertible.

Taking determinants gives

    det C = det(L⊗V⊗V) ⊗ det(L²⊗V)^−1
          = L^15 ⊗ (det V)^9.

In ordinary Chern-class notation, c₁(C)=−25h−(−10h)=−15h. Consequently

    det Φ ∈ H⁰(X,L^−15 ⊗ det J ⊗ (det V)^−9).

The last two factors are fixed one-dimensional vector spaces. After choosing their trivializations this is H⁰(X,O_X(15)); its zero scheme and divisor class do not depend on these choices. Thus the notation O(15) suppresses only constant determinant factors, not a variable twist.


This reproduces the universal bundle calculation, not the conditional actual outer-boundary local model.
