# Twist-one spectral obstructions require a singular curve and a low-rank pencil member

Assume a primitive surviving section ψ∈H0(End_0(V)(1)), with V=F|Q and Q⊂P4 smooth. Its determinant defines f∈H0O_Q(2), represented by an ambient quadratic polynomial f. Let q define Q. The integral spectral cover is the complete intersection

Y={q(x)=0, λ²=f(x)}⊂P5.

No particular coefficients are chosen or evaluated. The statements below are universal deductions from this presentation and the previously proved zero-scheme length32 when finite.

## 1. Isolated spectral singularities are impossible

The branch singular scheme Σ⊂P4 is defined by q, f, and all 2×2 minors of the matrix with rows ∇q and ∇f. These are homogeneous quadrics. Since Q is smooth, this is exactly the singular scheme of the Cartier divisor f=0 on Q, not a larger rank artifact. The singular scheme of Y is canonically Σ at λ=0: differentiation of λ²−f gives 2λ, and the remaining Jacobian minors reduce to the displayed minors.

Suppose Σ were zero-dimensional. Its defining vector space of quadrics has finite base locus. Four general members of this space have zero-dimensional common intersection: inductively avoid the finitely many positive-dimensional components of the previous intersection not contained in the base locus. They form a regular sequence in the polynomial ring on five variables and define a complete intersection of length2⁴=16 containing Σ scheme-theoretically. Hence lengthΣ≤16.

On Q, write ψ locally as [[a,b],[c,-a]]. Then f=a²+bc up to the irrelevant determinant sign. Both f and its differential belong to the ideal (a,b,c). Therefore the zero scheme Z(ψ) is a closed subscheme of Σ. If Σ is finite then so is Z(ψ), and its top Chern calculation gives lengthZ(ψ)=32. This contradicts lengthΣ≤16.

Thus Σ and Sing(Y) have positive dimension. This conclusion is unconditional within the twist-one branch. It does NOT assert that Z(ψ) itself has positive dimension: a finite zero scheme could still sit on a larger singular locus.

## 2. A low-rank quadratic in the branch pencil is necessary

Let A be the invertible symmetric matrix of q and B a symmetric matrix representing f. A point [x] of Σ satisfies

(B-tA)x=0,  q(x)=0

for some scalar t. The scalar exists because ∇q is nonzero at every projective point of Q. There are only finitely many such t, namely the roots of det(B-tA), a nonzero degree-five polynomial. Hence the reduced singular locus is a finite union of

Q∩P(ker(B-tA)).

Since this union is positive-dimensional, one member is positive-dimensional. Its kernel has dimension at least two. Consequently the pencil contains a quadric of rank at most three.

More precisely, either its kernel has dimension at least three, giving rank at most two; or its kernel has dimension exactly two, and its projective vertex line lies entirely on Q. These alternatives follow because the zero set of a nonzero quadratic on P1 is finite. Rank zero would make f proportional to q, and rank one would make f|Q a square; both contradict the established irreducible spectral polynomial. Thus a suitable pencil member has rank two, or rank three with vertex line contained in Q.

In the rank-two case, over C the member factors as two independent linear forms, so the branch divisor on Q is a union of two hyperplane sections (with their scheme structures). In the rank-three case no factorization is inferred; the vertex-line condition is retained explicitly.

These are restrictions on every actual twist-one obstruction, not numerical tests of a selected quadratic. They do not yet exclude either low-rank alternative or prove vanishing of the original twenty-dimensional boundary.
