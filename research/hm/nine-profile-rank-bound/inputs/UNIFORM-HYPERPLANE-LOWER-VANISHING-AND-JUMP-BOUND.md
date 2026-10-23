# Uniform hyperplane lower vanishing and the exceptional jump bound

## Theorem

For every hyperplane H_lambda in the actual negative pencil,

    H0(H_lambda,B(1))=H0(H_lambda,B(2))=0,
    H0(H_lambda,B(3))_-=0.                             (1)

Away from the twelve order-five parameters, h0(B_Hlambda(3))=3. At any of the twelve exceptional parameters,

    3 <= h0(B_Hlambda(3)) <= 5,                        (2)

and all sections are even. The possible excess is not identified with the length of the local torsion module: a length-two cyclic torsion module contributes only one extra fiber section.

More precisely, let C be the cokernel of the actual universal even hyperplane pencil

    44 O_T(-1) -> 46 O_T.

Its torsion is supported on the twelve exceptional points, with a uniform local length j in {0,1,2}. The total torsion degree is 12j, and its torsion-free rank-five quotient has degree 26-12j. None of the three possible values of j is selected here.

## 1. Actual inputs

- The restriction F_Hlambda is stable for every lambda, so H0(B_Hlambda)=0.
- The actual plane Steiner cohomology gives H0(B_R(1))=0 and H0(B_R(2))=A=Sym^2 W.
- The actual second-normal class zeta is nonzero. Its coefficient map identifies Sym^2 W with the unique A constituent in H1(B_R(-2)).
- The geometrically checked cup theorem in SECOND-NORMAL-POSITIVE-BOUND-THREE.md identifies its action

      H0(B_R(2)) tensor A -> H1(B_R)

  with a nonzero scalar multiple of binary multiplication

      Sym^2 W tensor Sym^2 W -> Sym^4 W,

  whose image is the unique five-dimensional constituent of H1(B_R). The scalar is proved nonzero there by the actual invariant-conic boundary, not inferred from dimensions.
- EXACT-HYPERPLANE-ADJOINT-SYZYGY-BUNDLE.md identifies the global kernel as A O_T(-6) and the cokernel C as a rank-five coherent sheaf of degree26. HYPERPLANE-ADJOINT-EXHAUSTION-AND-SIX-TO-TEN.md gives exact dimension three off the twelve exceptional points.

## 2. First twist and parity division

For a fixed H containing R, its normal coordinate u is inversion-odd. Restriction gives

    0 -> B_H(t-1) --u--> B_H(t) -> B_R(t) -> 0.

The fiber involution of B_R(t) is even, because R is the positive fixed plane and B is the adjoint bundle. Stability gives H0(B_H)=0. Since H0(B_R(1))=0, the case t=1 immediately gives H0(B_H(1))=0.

For t=2, restriction embeds H0(B_H(2)) in H0(B_R(2))=A. Its odd part is zero already, because an odd section restricts to zero and division by u would give an even section of B_H(1).

## 3. The actual second-normal obstruction is injective for every direction

It remains to exclude even sections of B_H(2). Any such section has a leading restriction s in A, and that restriction determines it injectively by Section 2.

The hyperplane is linear, so its punctured normal neighborhood is the total line bundle O_R(1), with projection to R. Its first-order projective bundle comparison has no odd normal term by inversion. The second-normal coefficient is the actual restriction zeta(lambda), obtained by evaluating the binary quadratic coefficient tensor at the nonzero normal direction lambda. Under the coefficient-space identification this is the nonzero pure quadratic a=lambda^2, up to the harmless symplectic dual identification.

Thus extending s even through the second normal order requires the vanishing of the actual cup-commutator

    s |-> [zeta(lambda),s] in H1(B_R).                 (3)

By the nonzero cup theorem, (3) is a nonzero scalar multiple of multiplication by a in

    Sym^2 W -> Sym^4 W.

Multiplication by any nonzero binary polynomial is injective. Therefore s=0. The injectivity of restriction then proves H0(B_H(2))_+=0, completing the twist-two assertion in (1).

This argument uses the actual second-normal extension class. It does not replace it by a chosen local matrix or assume that higher even transition terms vanish. A global section must pass this first necessary boundary, so no higher-order hypothesis is needed.

Finally an odd section of B_H(3) restricts to zero on R and divides by u to an even section of B_H(2). The latter space is zero, proving H0(B_H(3))_-=0 for every lambda, including the twelve exceptional ones.

## 4. Uniform torsion length and the exceptional bound

From the exact universal kernel theorem,

    0 -> A O_T(-6) -> 44 O_T(-1) -> 46 O_T -> C -> 0,

with rank(C)=5 and deg(C)=26. The quotient C is globally generated. Its torsion-free quotient C_tf is also globally generated, hence, by the splitting theorem on P1, has nonnegative degree.

Off the twelve exceptional parameters the dimension of H0(B_H(3)) is exactly three, so the base-change sequence shows that C has no torsion there. Equivariance and transitivity on the twelve-point orbit imply that the local torsion length j is the same at all twelve points. Consequently

    deg(C_tf)=26-12j >=0,

so j<=2.

At an exceptional point t, the exact base-change sequence is

    0 -> (A O_T(-6)) tensor k(t)
      -> H0(B_Ht(3))_+
      -> Tor_1(C,k(t)) -> 0.

A finite-length torsion module over the local DVR is a direct sum of modules O/(z^e_i). Its contribution to Tor_1 with the residue field is the number of summands, whereas its length is sum e_i. Thus the fiber excess is at most j, proving (2) together with the odd vanishing.

The alternatives must remain distinct:

- j=0 gives no jump;
- j=1 gives one extra section;
- j=2 allows either one or two extra sections, according to the elementary divisors.

The global torsion lengths are respectively 0,12,24. This theorem does not determine the elementary divisors or assert that the last possibility occurs.

## Boundary

The all-parameter lower vanishing and the jump bound sharpen the known section-space constraints without evaluating a new actual map. They do not decide the remaining six-to-ten smoothing obstruction, the full even corank, or the precise special hyperplane cohomology. In particular the odd vanishing here concerns hyperplane twist three, not odd quadric twist four.
