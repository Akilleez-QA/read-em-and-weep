# Asymmetric (1,2) quotient degrees and the twelve-defect branch

## Checked conclusion

For a hypothetical maximal rank-three profile (k,l)=(1,2), put

    K=E^-, A=E/K, L=(Q*)^-, B=Q*/L,
    M=L^-, J=L/M, a=deg A, b=deg B.

Then

    -8 <= a <= 6,  -12 <= b <= 2,
    t=length coker(A -> B*(-2)) is 0 or 12.

If t=12, the only degree pairs are

    (a,b)=(-8,-10), (-6,-12),

and the SECOND dual derivative is saturated: J=B(-2). In these two cases M has rank seven and degree -28 or -24, respectively. No full splitting classification or actual-map computation is used. Neither degree pair is claimed to exist or excluded. The four remaining profiles and bounds SF>=3 and square rank>=27 are unchanged.

## 1. Which derivatives have rank three

Use ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md, Section 4. The primal chain is F0=K, F1=E, F2, F3: E and F2 are interior, while K is an endpoint. The reversed dual chain has Q* at index two. Its two interior stages Q* and L have rank-three derivatives; their kernels have ranks ten and seven. Thus J has rank three and injects into B(-2). No rank-three assertion is made for K or M.

The actual E has rank 17, degree -54, degrees between -10 and -2, and

    chi_G(E(2))=-V, chi_G(E(3))=W'+2T6.

Q* has rank 13 and degree -54 and no constant subbundle, hence degrees at most -1. In this profile one MUST NOT import the (2,2) assertion H0(Q*(1))=0. Strict slope decrease from NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md gives

    maxdeg K<=-3, maxdeg K^-<=-4,
    maxdeg L<=-2, maxdeg M<=-3.

All these kernels are saturated in the constant bundle. K^- exists regardless of the endpoint derivative rank. The derivative K -> A(-2) gives H0(K(3)) -> H0(A(1)) injectively.

## 2. Improve the primal degree without any plateau extension

Initially deg K<=-42 gives a>=-12. Since A is a rank-three quotient of E and E(10) is globally generated, every ordinary degree x_i of A is at least -10. A is center-even; its determinant is an equivariant line with even degree, so a is even. (The binary icosahedral group is perfect, and the center of the standard O(a) acts by (-1)^a.)

Riemann--Roch and the preceding section injection give

    2-a = chi(K(3)) <= h0(K(3)) <= h0(A(1)).

For sum x_i=a, x_i>=-10, at a=-12 or -10 one has

    sum max(x_i+2,0) <= a+22.

Indeed, writing y_i=x_i+10>=0, the left side is sum max(y_i-8,0), at most max(sum y_i-8,0)=a+22. At a=-12 this gives 14<=10, impossible. At a=-10 both bounds equal 12. Equality in this elementary inequality requires all positive y_i to be in a single entry: otherwise each additional positive entry subtracts a further positive amount. Therefore the ordinary degrees are (-10,-10,10).

All these degrees are even. Their multiplicity spaces have dimensions two and one, and the binary icosahedral group has no nontrivial center-even irreducible of dimension at most two. Consequently

    A=2O(-10)+O(10)

with trivial coefficient representations. Since H0(K(2))=0, the quotient sequence forces the genuine representation

    H1(K(2))=chi_G(A(2))-chi_G(E(2))
             =Sym^12 W-2Sym^6 W+V
             =1+A_std-V-P4+D5.

Here A_std=Sym^2 W, distinct from the quotient bundle A. The negative V and P4 multiplicities are impossible. Thus a>=-8. This primal bound actually uses no particular maximal profile beyond generic rank three of the original derivative.

## 3. The dual interior bound and original determinant

The equal-rank injection J -> B(-2) gives deg J<=b-6. Since M has rank seven and degrees at most -3, deg M<=-21. It is center-even, so its degree is even; hence deg M<=-22. Using deg L=-54-b gives

    -32-b <= deg J <= b-6,

so b>=-13 and therefore b>=-12 by determinant parity.

The negative-transpose factorization gives the injective equal-rank map A -> B*(-2). Its determinant divisor is invariant and has degree

    t=-6-a-b >=0.

From a>=-8 and b>=-12, t<=14. A nonzero invariant effective divisor for the projective icosahedral action has degree at least 12; the only positive degree at most 14 is 12. Therefore t=0 or 12. The inequality a+b<=-6 also gives a<=6 and b<=2.

## 4. The twelve-defect branch has no second dual torsion

Write s=length coker(J -> B(-2)). The same degree bounds give

    0<=s<=2b+26.

If t=12 then a+b=-18. Evenness and the lower bounds leave exactly (-8,-10) and (-6,-12). Thus s<=6 or s<=2. Its determinant divisor is again invariant, so s=0 in either case. Hence J=B(-2), and

    deg M=deg L-deg J=-48-2b.

The original t=12 divisor itself is the reduced twelve-point orbit; its cokernel has length one at each of those points. This refers only to the original quotient injection. It must not be confused with the second dual injection, which is an isomorphism in this branch.

## 5. Exact dual Euler envelope (valid in both branches)

The two exact sequences and H0(M(2))=0 yield the genuine-character identity

    chi_G(B)+chi_G(B(2))-chi_G(Q*(2))
      = H0(coker(J -> B(-2))(2)) + H1(M(2)).

The actual presentation gives chi_G(Q*(2))=-1-2A_std-V-D5. Thus the left side has nonnegative multiplicities in every irreducible. This is a necessary bounded-character identity, not a claim of realizability. If t=12 the torsion term vanishes by Section 4.

## Verification and sources

Run python3 verify_one_two_asymmetric_degree_bounds.py. The test imports only the read-only abstract character ring in verify_negative_vertex_scalar.py, checks the two exact character identities, the elementary convex bound and its equality case, and the bounded even degree pairs. It uses no actual coefficients, points, matrices, rank tests, arbitrary splitting enumeration, or large computations. The character and integer tests complement, not replace, the saturated-bundle proofs above.

Additional convention cross-check: TWO-TWO-SECOND-INTERIOR-EULER-EXCLUDES-SEVENTEEN-PAIRS.md. Its two-sided rank-three interior argument is deliberately not applied to the primal endpoint here. Earlier files are unchanged.
