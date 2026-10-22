# Independent mathematical review

Verdict: PASS, conditional on the explicitly pinned structural inputs from
PR683, PR684 and the actual normal-neighborhood ladder. No selected HM/source
instance, numerical rank, or actual fourth value was evaluated.

The review independently checked the following points.

1. Because B is locally free on the ambient P4 and q is a nonzerodivisor,
   multiplication by q^r identifies the last layer of B on (r+1)Q with the
   correctly twisted B_Q. This remains valid at the singularities of Q.
   In particular q^2:B_Q(4)->B_(3Q)(8) is injective on sections.
2. Locally split monad end sequences remain split on every rQ. Passing
   from a cochain closed modulo q to q^2 times it modulo q^3 therefore
   commutes with the induced map on F. This justifies the actual bundle
   identity J(C')-J(C)=-q^2 eta without a claimed global homotopy.
3. With D=C'-C and T=V'-V, the differential is dD=-qT, so the published
   connecting convention gives delta_q eta=-[T]. The ambient vanishing
   H0(B(4))=0 makes this connecting map injective. Thus equality of divided
   classes is equivalent to equality of the induced third adjoints.
4. PR683's surjectivity realizes every even eta=Ns. The eight-dimensional
   A+D torsor and four-dimensional equivariant P2-family quotient follow
   from injectivity, not from subtracting unrelated parameter counts.
   The class-fixed 734/829 fibers, and PR684's 680/775 vertex-and-class
   fibers, consequently consist of cochain representatives of one J.
5. The square-zero comparison uses only the reduction J|Q=a^2hN and N^2=0;
   q^4 terms vanish on3Q. It does not impose a new restriction among these
   even completion differences.
6. For a change -q^2Ns in J, the correction -q^2U_a tilde s on4Q has
   differential -q^4Z_a tilde s. Multiplication by a and division by q^4
   gives exactly the fifth-boundary variation -[a tilde s Z_a|Q], of
   twist4. A different ambient lift of s changes it by a section extending
   to5Q, so it does not change the boundary.
7. Two even fourth lifts of the same aJ differ by q^3Nt. After multiplication
   by a, their difference extends to5Q as q^3U_a tilde t, whose differential
   is q^5Z_a tilde t. The fifth boundary is therefore independent of the
   even fourth-lift choice. This argument needs only center parity: the
   quadratic a in Sym^2W is center-even, regardless of the negative
   coordinate terminology or extra Serre involution.

8. The two additional pinned second-symbol sources were fetched and read
   independently. The positive first-Bockstein note, Section4, defines
   beta2(s xi)=-[a s zeta_a] for q+t a. The fourth-after-third-vanishing
   note, Section3, uses q-t a and beta2_a(s)=[a s zeta_a]. It also explicitly
   identifies changing v by g xi with the second-symbol variation
   [a g zeta_a]. In the present proof delta_q eta=s xi and Delta[V]=-s xi;
   hence the compatible variation of w is -s zeta_a and the boundary
   variation is -beta2_a(s) in the latter convention. The signs therefore
   agree with both cited conventions once their definitions are retained.
9. Restriction H1(B(4))->H1(B_Q(4)) kills every q multiple by the restriction
   exact sequence. Thus the ambient second-symbol class maps to precisely
   [a s Z_a|Q], and the variation lies in its image for every s in A+D.
   This argument needs no inversion of beta2, generic-rank hypothesis or
   smoothness assumption on a. Together with the even fourth-lift
   independence above, it proves that the fourth quotient value is
   independent of all even completions for fixed a,h,b,U_a.

10. Section5 correctly separates fixed-direction and polynomial-family
    dimensions. The published second-symbol A map has rank3 away from the
    six axes and rank2 there, while its D restriction is zero. Accordingly
    the eight-dimensional affine third-lift torsor has raw-boundary image
    dimensions3/2 and fibers5/6 for nonzero directions off/on the axes.
    For P2 families the domain instead has dimension4=1+3: the three
    D-valued families are killed. Twisting the sheaf injection
    A O(-2)->P O by four and tensoring with the constant dual h-parameter
    space preserves injectivity on global sections. Thus its restriction
    to the one-dimensional A-valued family is nonzero, giving family
    image dimension1 and kernel3. The polynomial degrees are correctly
    quadratic in a before and quartic in a after the second symbol, and
    linear in h throughout. No affine base value is computed by these ranks.

The identification of the variation with second-symbol indeterminacy is
supported by the independently checked published definitions. It does not
compute the common quotient value, prove it zero, vary the fixed source
correction b, or establish higher lifting/algebraicity. This is mathematical
review, not proof-assistant certification.
