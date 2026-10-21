# Every primitive twist-four eigenquotient is dominant for general source Q

## Scope and checked inputs

Use the fifty-basepoint resolved eigenquotient projection of EIGENQUOTIENT-PROJECTION-BOUNDS.md (3c4ab4b2cdfb9e54012f92f798a8da34768413d0). The source Q is a simultaneous-good smooth quadric threefold, X=P_Q(V(3)), L=O_X(1), H is the source hyperplane class, and Xhat is the blowup of fifty simple evaluation base points with exceptional E_i. The class A=L-sum E_i resolves f:Xhat->P(U*)=P3; each E_i maps isomorphically onto the target P3.

Let psi be a primitive trace-free twist-four endomorphism with nonsquare nonzero characteristic determinant. Its eigenquotient divisor T on X is integral; its strict transform has class

    That=2L-H-sum m_i E_i.

The result below excludes nondominance for general Q. It does not exclude dominant twist-four endomorphisms or claim a complete repair.

Additional inputs are the universal quadric-jet lemma in QUADRIC-JETS-EXCLUDE-HIGH-VERTICAL-DEGREES.md, the actual kappa sextic theorem (3edb50b13b8a5ce876f52a2085ecc8d16b3181c0), EIGHT-ROOT-POSITION-DOMINANCE.md, and the integral elliptic pencil theorem GENERAL-EIGHT-SEXTIC-POINTS-ELLIPTIC-PENCIL.md (dd6ffc10117710404a042fd5e08730aa3f543bd1).

## 1. A local multiplicity bound

At a simple evaluation base point, choose base parameters and fiber coordinate u so the eigenquotient equation is

    c+2au-bu^2.

If its multiplicity is m, independence of the powers of u gives ord(c)>=m, ord(a)>=m-1, ord(b)>=m-2. Thus ord(det psi)>=2m-2. The determinant is a nonzero section of O_Q(8). A nonzero degree-eight section on a smooth quadric has order at most sixteen at a point. If its order is sixteen, it is a scalar eighth power of the tangent hyperplane section, hence a square. Both statements follow by choosing the quadric affine chart x_4=q(x_1,x_2,x_3), where an ambient degree-eight polynomial has local degree at most sixteen and its top degree-sixteen part is a scalar q^8.

Consequently m>=9 would force the determinant to be a square or zero. Therefore every m_i<=8.

## 2. Exact nondominant image alternatives

Assume f|That is not dominant. The intersection identity gives

    0=A^3 That=70-sum m_i,

so sum m_i=70. The positive sum forces the image D=f(That) to be a surface: a positive-degree divisor That|E_i cannot map into a curve under E_i=P3 -> P3.

Write e=deg D. Since D is integral, the effective pullback f*D contains That. Restriction to any E_i with m_i>0 shows its coefficient is one and That|E_i=D. Hence every positive m_i equals e. Also

    H^3(f*D-That)=2e-4>=0,

so e>=2. Combining e|70 with e<=8 leaves exactly

    e=2, with 35 positive multiplicities;
    e=5, with 14 positive multiplicities;
    e=7, with 10 positive multiplicities.

## 3. The quadratic image would give fifteen double points of a hyperplane section

For e=2, let J be the thirty-five indices with m_i=2. Then

    f*D-That=H-2 sum_{i not in J} E_i.

This divisor is effective and has no exceptional component. Pushing forward to X yields the pullback of a nonzero section of O_Q(1). The exceptional coefficients give multiplicity exactly two at each of the fifteen remaining marked points. A nonzero hyperplane section of a smooth quadric is either smooth or tangent, and in the tangent case its singular locus is a single point. It cannot have fifteen distinct double points. Thus e=2 is impossible, with no further genericity.

The number fifteen is essential bookkeeping: the thirty-five points are the positive eigenquotient multiplicities, and the residual divisor is double at their complement among fifty.

## 4. Image multiplicities on Gamma

At any positive basepoint, That|E_i is the degree-e initial form of c+2au-bu^2. It has u-degree at most two. Therefore its image D has multiplicity at least e-2 at the fiber-axis point [1:0:0:0]. Under E_i->P(U*), that point is the original rank-one evaluation functional kappa(z_i), lying on the actual smooth rational sextic Gamma.

Thus e=5 forces an integral quintic triple at fourteen kappa-images, while e=7 forces an integral septic of multiplicity at least five at ten kappa-images. General Q makes all fifty kappa-images distinct. More importantly, the eight-root dominance theorem says that for general Q EVERY choice of eight source marks has independently general kappa-position on Gamma^8. Its finite-pattern statement covers choices depending on the endomorphism. Hence any selected eight among the fourteen or ten points satisfy the elliptic-pencil open condition.

## 5. The quintic image is impossible

Choose eight such points. There is a smooth target quadric S containing them and a second target quadric whose intersection C with S is integral of class (2,2), arithmetic genus one, and smooth at the eight points. The points are noncoplanar.

The integral quintic D cannot contain S. Its restriction has class (5,5) and multiplicity at least three at each point. Intersecting with C gives twenty, whereas the eight local intersections contribute at least twenty-four unless C is a component. Thus subtract C. The residual class is (3,3), still double at the eight points. Its intersection with C is twelve, below sixteen, so C is again a component. Subtracting it leaves an effective (1,1) divisor through all eight points, contradicting noncoplanarity. Therefore e=5 is impossible.

## 6. The septic image is impossible

Use the same target quadric S and integral C for eight of the ten marked points. The integral septic D does not contain S. Its restriction has class (7,7) and multiplicity at least five at each point.

Its intersection with C is twenty-eight, below forty; hence C is a component. After subtraction, the effective residual has class (5,5) and multiplicity at least four, with intersection twenty below thirty-two. Subtract C again. The residual is (3,3), of multiplicity at least three, with intersection twelve below twenty-four. Subtract C a third time. The final effective divisor has class (1,1) and multiplicity at least two at all eight points. In particular it passes through all eight, impossible for a hyperplane section because they are noncoplanar.

All local multiplicity decrements are by one because C is smooth at the marked points. Global smoothness of C is not required. This excludes e=7.

## Conclusion

All nondominant primitive twist-four eigenquotients are excluded on the common general-source-quadric open. Every remaining primitive twist-four eigenquotient therefore dominates the target P3. This conclusion has no exceptional source-root patterns, because each image exclusion needs only eight selected marks and eight-root dominance holds for every pattern. Dominant twist-four cases remain outside this theorem.

No selected HM coefficients, source-rank computations, numerical experiments, or external writes were used.
