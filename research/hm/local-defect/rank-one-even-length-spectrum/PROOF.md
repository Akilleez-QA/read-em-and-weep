> Publication scope: preserved mathematical proof/audit. Historical statements that rank eight remains open are superseded only after the final assembly and all its prerequisites. No source-instance evaluation or formal verification is claimed here.

# Rank-sensitive generic length bounds and a gap in the spectrum

## Result

Import the exact graded normal form from `../rank-one-even-normal-form/PROOF.md`: the generic local ring A along the rank-one component has associated graded algebra

    gr_m A = S/(W),       S=K[p1,p2,p3,p4],

where W is the space of quadratic equations of the intrinsic normal obstruction, and W has empty projective common zero locus even over an algebraic closure. Let r=dim W, equivalently the rank of the linear quadratic map Sym^2(K^4) -> K^16. No value of r for the actual operation is calculated here.

Then:

- r=4: length A=16, with Hilbert function (1,4,6,4,1).
- r=5: 10 <= length A <=12.
- r=6: 9 <= length A <=11.
- r=7: 8 <= length A <=10.
- r=8: length A=7, with Hilbert function (1,4,2).
- r=9: length A=6, with Hilbert function (1,4,1).
- r=10: length A=5, with Hilbert function (1,4).

For every r>=5, m^4=0 and h_3(A)<=2. For every r>=8, m^3=0. Consequently

    length A belongs to {5,6,7,8,9,10,11,12,16}.

In particular lengths thirteen, fourteen, and fifteen are impossible. Length five is equivalent to injectivity of the quadratic map, and length sixteen is equivalent to quadratic rank four.

The rank-conditioned conclusions are not assertions that a particular rank or allowed length occurs. Generic injectivity remains open. All arguments concern universal commutative algebra. No actual HM matrix, operation value, product, rank instance, polynomial instance, selected input, residue, or jet is evaluated. Files are written only locally.

## 1. Reduction to a quadratic complete intersection

The imported exact associated graded presentation gives h_0=1, h_1=4, and

    h_2=10-r,
    h_3=dim_K(S_3/(S_1 W)).

Since W has no projective basepoints, r>=4 and four linear combinations q1,...,q4 in W form a regular sequence. The argument is the usual avoidance of the finitely many relevant associated primes over the infinite field K. Put B=S/(q1,...,q4). Its Hilbert function is (1,4,6,4,1), with zero in higher degrees. There is a graded surjection B -> gr_m A, and m^5=0.

If r=4, W is precisely the span of this regular sequence, so gr_m A=B. Thus the length is sixteen.

## 2. An extra quadric removes at least four dimensions

Suppose r>=5, and choose q in W outside the span of q1,...,q4. Its class in B_2 is nonzero. The Artinian quadratic complete intersection B is graded Gorenstein with socle degree four. In particular multiplication B_2 times B_2 -> B_4 is a perfect pairing. Hence q B_2=B_4, so (B/(q))_4=0. The surjection onto gr_m A and Nakayama give m^4=0.

Let rho be the rank of multiplication q:B_1 -> B_3. We claim rho>=2. Extend scalars algebraically if necessary; dimensions are unchanged. The quotient

    C=B/ann_B(q)

is Artinian standard graded Gorenstein with socle degree two and Hilbert function (1,rho,1). To verify the perfect-pairing assertion directly, for a nonzero class represented by a with qa nonzero choose b in complementary degree such that qab is nonzero, using the perfect pairing of B.

If rho=0, C_1=0 would imply C_2=0 because C is standard graded, contradicting C_2=K. If rho=1, C is isomorphic as a graded algebra to K[t]/(t^3). The composite S -> C sends pi to lambda_i t, with not all lambda_i zero. Each qj maps to zero, so

    qj(lambda_1,...,lambda_4)=0, j=1,...,4.

This contradicts the empty projective common zero locus of the regular sequence. These are formal consequences concerning arbitrary quadrics and a hypothetical point; no actual operation polynomial is evaluated. Thus rho>=2.

Consequently

    h_3(A) <= dim(B/(q))_3 = 4-rho <= 2.

Combining h_2=10-r, m^4=0, h_0=1, and h_1=4 gives

    15-r <= length A <= 17-r.

For r=5,6,7 this gives the intervals in the theorem. For every r>=5 the upper bound is at most twelve.

For r=5 there is only one extra independent quadric after the complete intersection, so the exact formula is length A=14-rho with rho in {2,3,4}. This is again a conditional algebraic formula, not an evaluation of the actual multiplication map.

## 3. At most two missing quadrics force m cubed to vanish

Suppose r>=8 and put d=10-r<=2. We prove (S/(W))_3=0. It suffices to work over an algebraic closure.

Use the characteristic-zero differential pairing between S_j and homogeneous degree-j polynomials in dual variables. Write H=W^perp, a subspace of dual quadrics of dimension d. Empty projective common zero locus of W means H contains no nonzero square of a linear form: such a square represents evaluation at the corresponding projective point, up to a nonzero scalar.

If (S/(W))_3 were nonzero, there would be a nonzero dual cubic F annihilating S_1 W. Every first partial derivative of F would then belong to H. Thus the span of the first derivatives has dimension at most two.

A homogeneous polynomial in characteristic zero whose first derivatives span an e-dimensional space depends, after a linear change of variables, on exactly e variables. Indeed the kernel of the directional-derivative map is a vector subspace of codimension e; in coordinates adapted to this kernel, the derivatives in the remaining directions vanish and the polynomial is independent of those variables.

Here e is one or two: it cannot be zero for a nonzero cubic. If e=1, a derivative is a nonzero square, contradicting the property of H. If e=2, the two-dimensional derivative space lies in the three-dimensional space of binary quadrics. Its projectivization is a projective line in P^2. Over the algebraic closure every projective line meets the Veronese conic of squares. Hence again H contains a nonzero square, a contradiction.

Therefore (S/(W))_3=0. Since this is a standard graded algebra, all higher graded pieces vanish. Equivalently Nakayama gives m^3=0. The length is exactly

    1+4+(10-r)=15-r.

In particular length five forces h_2=0 and hence r=10; conversely r=10 gives length five. The upper bound twelve when r>=5 and the r=4 computation also show that length sixteen is equivalent to r=4.

## Boundary

These arguments sharpen the generic Hilbert-function possibilities and exclude three lengths allowed by the earlier interval five through sixteen. They neither establish a lower bound greater than four on the actual generic quadratic rank nor determine which permitted rank or length occurs. They do not claim that every number in the allowed set is realizable by the actual operation, or even by an arbitrary basepoint-free quadratic algebra with this structural origin.
