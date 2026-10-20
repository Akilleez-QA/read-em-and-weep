Publication context: this retained proof or audit may describe an intermediate bound or then-open branch. Read the unit overview for the current scope and later implications. Historical mathematical review is not a new formal verification.

# Additional exclusion: finite-dual Hilbert function (3,4,4)

Retain all hypotheses and conventions of PROOF.md. Suppose P=D(Q) has Hilbert function (3,4,4), with clock-trivial top T and middle U≅V. There are dim(W⊗T)−dim U=8 independent linear initial relations, so β1(P)≥8. The necessary inequality β1(P)−6≤2 forces equality. Thus the generator representation Tor₁(P,k) identifies with K1=ker(W⊗T→U), and K1 must be self-dual. This identification uses the same initial-linear lifting argument as PROOF.md §2 and is valid for filtered modules.

A three-dimensional clock-trivial H-representation T has B-weights either three copies of (0,0), or {(0,0),(0,b),(0,−b)} with b≠0. In the first case W⊗T has three copies of O3 and U removes one; K1 has two copies of O3 and is not self-dual on B.

In the second case W⊗T has slopes 3,3+b,3−b. Up to replacing b by −b, b is 1 or 2. For b=1 these slopes are 3,4,2, and deleting one leaves a negation-invariant pair only when U has slope 4. For b=2 the slopes are 3,0,1, and no deletion leaves a negation-invariant pair. Therefore the only possible case has top weights (0,0),(0,1),(0,−1) and U=O4.

Choose top weight vectors t0,t+,t−. For each i≠0, the only top weight which x_i can map to U is (0,i²), since U has weight (i,4i²). The corresponding coefficient is nonzero by surjectivity. Consequently K1 is spanned by all four x_i t0 and by each x_i applied to the wrong one of t+,t−. There are no other linear initial relations. In the quadratic quotient

    (Sym²W⊗T)/(W K1),

all monomials times t0 vanish. For t+, precisely the degree-two monomials in the two variables with i²=1 survive, and for t− those in the two variables with i²=−1 survive. These give three plus three independent monomials, so the quotient has dimension six.

The actual quadratic radical layer has dimension four. Hence there are at least two quadratic initial relations beyond W K1. These give two further independent minimal relations, even with filtered corrections: if K⊂R⊗T is the presentation kernel, the degree-two initial forms of mK are exactly W K1. Thus the two classes cannot belong to mK, and their classes are independent of the eight relations with independent linear initial forms. This yields β1(P)≥8+2=10, contradicting β1(P)=8.

Therefore (3,4,4) is excluded. Combined with PROOF.md, the only remaining necessary length-eleven finite-dual Hilbert functions are (2,4,5) and (2,4,4,1). This does not exclude those two families and does not improve the global lower bound 330. All steps are universal local algebra and finite representations, with no physical-instance calculation or external writes.
