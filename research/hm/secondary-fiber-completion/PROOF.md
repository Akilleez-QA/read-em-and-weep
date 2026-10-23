# Completing the exceptional fibers of the secondary boundary under the two-D-channel hypothesis

Work over C with the actual normalized HM adjoint B, G=SL2(F5), negative two-space W, and direction line T=P(W*). Write A=Sym2 W, D=Sym4 W, S=Sym3 W, T6=Sym5 W, V=Sym2 W', and P=W tensor W'. All line-bundle linearizations are retained.

The sole immediate input DROW is PR991 at commit 1ac03caea0564db40acabf8d8d5a0a39984216a2, research/hm/secondary-d-row/PROOF.md in Akilleez-QA/read-em-and-weep. Its exact bytes are recorded in INPUTS.json. All its actual-family hypotheses and immutable dependencies remain in force.

## 1. Statement and retained conditional scope

The actual reduced secondary boundary, including its quartic corrections, is

    b: Q=P O(2) plus W O(-1) -> (V+P+D) O(4).

The omitted A target row is identically zero. Each of the two source blocks has a one-dimensional equivariant Hom space to each of V,P,D. Choose nonzero universal channel generators i_J and j_J from the P and W sources respectively, and write its J row as

    (a_J i_J, b_J j_J),       J=V,P,D.

The six actual coefficients remain unselected. Throughout the new theorem assume a_D b_D is nonzero. This is precisely the conditional D-row branch of DROW, not a newly proved fact about the actual coefficients.

DROW proves that the D row has rank5 off the reduced twelve-point orbit Omega, rank4 on Omega, and kernel sheaf the Euler O(-2) inside W O(-1). We prove that the other channel generators can be normalized universally so that the two scalar expressions

    delta_V=a_D b_V-b_D a_V,
    delta_P=a_D b_P-b_D a_P                             (1)

complete the fiber test. Put e=1 if (b_V,b_P) is nonzero and e=0 otherwise; put r=1 if (delta_V,delta_P) is nonzero and r=0 otherwise. Then

    rank(b) off Omega = 5+e,
    rank(b) on Omega  = 4+e+r.                         (2)

In particular r=1 gives constant rank and torsion-free cokernel. If r=0, the generic-rank determinantal ideal is exactly the reduced ideal of Omega; the cokernel has torsion of length12, with length one at every point of Omega. This is a full scheme-theoretic completion within the stated branch, without selecting that branch or either indicator for the actual map.

## 2. Two canonical P-source channels

First consider the unique P-to-V channel. The P-isotypic subspace P6 of Sym6 W=V+P has no basepoints. Any nonempty base divisor would be G-invariant of degree at most6; the projective A5 action has no orbit of fewer than12 points. Its evaluation kernel is therefore

    0 -> M -> P O -> O(6) -> 0,

with rank3 and degree -6. The space H0(M(1)) is the kernel of binary multiplication P6 tensor W -> Sym7 W. Binary Koszul exactness embeds it into Sym5 W=T6, while P tensor W=W'+T6. Thus a nonzero kernel has dimension6. But a relation x f+y g=0 is determined by f in P6, so that kernel has dimension at most4. Consequently H0(M(1))=0. Birkhoff–Grothendieck forces M=U O(-2), and the equivariant sections of the sequence twisted by2 give

    U=P tensor A-Sym8 W=(V+P+D)-(P+D)=V.

Dualizing and twisting yields the canonical exact sequence

    0 -> O(-4) -> P O(2) --i_V--> V O(4) -> 0.        (3)

The fixed character identity P tensor A=V+P+D shows that this is the unique nonzero P-to-V channel up to scalar.

Next use P=W tensor W'. The Euler sequence gives maps

    W O(2) -> O(3) -> W O(4),

where the first is onto and the second is an inclusion. Their nonzero composition, tensored with W', has kernel W' O(1) and image W' O(3). Since P occurs once in P tensor A, this is the unique nonzero i_P. Hence

    ker i_P=W' O(1),       im i_P=W' O(3).             (4)

Both (3) and (4) are universal equivariant bundle statements, not evaluations of an actual map.

## 3. The other W-source channels are everywhere injective

For J=V or P, let j_J be its nonzero channel W O(-1)->J O(4). Its Hom space has dimension1 because J occurs once in W tensor Sym5 W=V+P+D.

It cannot have generic rank1. Otherwise its saturated image is an equivariant line O(d). G is perfect, so the linearization has no extra character. A nonzero map from W O(-1) implies d>=-1; a nonzero map into J O(4) implies d<=4. Central parity makes d even, so d is0,2, or4. The multiplicity of W in Sym^(d+1) W is nonzero only for d=0. In that case the second factor O->J O(4) is forbidden since Sym4 W=D contains neither V nor P. This contradiction proves generic rank2.

The common zero divisor of its two-by-two minors has degree at most10, since each entry has degree5. It is G-invariant, so a nonempty such divisor would have degree at least12. Hence there is no rank drop: j_V and j_P are everywhere injective. This argument bounds a divisor of universal minors; it does not compute any selected actual rank.

## 4. Abstract stabilizer characters on Omega

The following computation applies uniformly to the whole orbit and selects no actual point or coordinate. A binary stabilizer above the order-five projective stabilizer is C10. Choose its character lambda to be the fiber character of O(1), and set zeta=lambda^2. The two-space W has weights lambda and lambda^-1; W' has weights lambda^3 and lambda^-3. Thus, recording zeta exponents modulo5, the fiber characters are

    P O(2): 0,2,3,4;
    W O(-1): 0,4;
    D O(4): 0,1,2,3,4;
    V O(4): 0,2,4;
    P O(4): 0,1,3,4.                                 (5)

Reversing the stabilizer generator changes names consistently and does not change any conclusion.

The DROW injection i_D has image the four characters 0,2,3,4; its quotient O(12) has character1. The map j_D is quartic Veronese composed with Euler evaluation, so it maps the W character0 nontrivially into the D character0 and kills the Euler character4. Under a_D b_D nonzero, the two-dimensional D-row fiber kernel on Omega is therefore the sum of:

- the Euler character4 line, entirely in the W source;
- a character0 graph line involving the P and W character0 sources.

For i_V the kernel O(-4) has character3, so its character0 source map is nonzero. For i_P the kernel W' O(1) has characters2,4, so its character0 source map is also nonzero. Each j_V,j_P is everywhere injective by Section3 and therefore nonzero on both of its source character lines. Their target character0 spaces are each one-dimensional. This supplies two nonzero comparisons rather than merely permitted character channels.

## 5. Universal normalization and the complete fiber-rank formula

We justify the normalization implicit in (1). Over the reduced orbit Omega, let U be the character0 line of the W source and L the character0 line of the P source, using the transported stabilizer descriptions above. These equivariant lines are well-defined over the orbit; the trivial stabilizer character does not depend on a generator choice. Equivalently, Euler evaluation restricts to an equivariant isomorphism U=O_Omega and has a unique equivariant right inverse into W O(-1)|Omega, because the complementary character4 is nontrivial. The quartic Veronese section lies in im i_D on Omega and defines the analogous character0 line L. Thus the construction is intrinsic on the homogeneous reduced scheme Omega. The nonzero maps i_D|L and j_D|U define an isomorphism

    h:U -> L,       i_D h=j_D.

For J=V,P the two maps j_J|U and i_J h are nowhere-zero maps into the same character0 target line. Their ratio is a G-invariant invertible function on the reduced transitive orbit, hence a single nonzero scalar. Rescale i_J by this scalar so that

    i_J h=j_J on U over Omega.                         (6)

This construction depends only on universal channel maps and the entire orbit; it chooses no actual parameter, point, or coefficient value.

For a source vector w in U, the character0 D-kernel graph is represented by

    (-(b_D/a_D)h(w), w).

Its J-row image, by (6), is

    (delta_J/a_D) j_J(w).

Hence its image under the other two rows is nonzero exactly when r=1. Independently the Euler character4 kernel line has nonzero image exactly when e=1. Since the two characters are distinct, their images are independent whenever both occur. The D-row rank on Omega is4. This proves the second formula in (2).

Away from Omega the D kernel is just the Euler line. Any nonzero j_V or j_P restricts nontrivially to that line: otherwise it would descend to an equivariant O->J O(4), forbidden as in Section3. Such a restriction O(-2)->J O(4) is nowhere zero, since a common-zero divisor of degree-six forms would have degree at most6 and be G-invariant. Therefore it contributes precisely e additional ranks everywhere off Omega, proving the first formula in (2).

## 6. The determinantal ideal and cokernel torsion

If r=1, (2) gives the same rank at every point. Thus b has locally free image and cokernel, and the cokernel has no torsion.

Suppose r=0 and e=1. At an arbitrary local ring along Omega, use the everywhere-injective i_D to turn its four columns into an identity block. The remaining D row is a unit times f12 times Euler, where f12 cuts out the reduced orbit, as proved in DROW. Locally split the W source into the Euler kernel and a complement. The complement has unit Euler image. Since e=1, an additional V or P row has a unit coefficient on the Euler-kernel column, including at Omega by Section5. The minor formed from the five D rows and this extra row is therefore a unit times f12 after clearing the four identity columns. Thus the ideal of six-by-six minors contains (f12). By (2), all such minors vanish on the reduced orbit, so their ideal is contained in (f12). Equality follows locally and hence globally. The rank is5 on Omega, so local Smith form has one positive exponent, and its value is1. The cokernel torsion has length one at each of the twelve points.

If r=0 and e=0, then b_V=b_P=0 and (1), together with b_D nonzero, forces a_V=a_P=0. The entire reduced map is its D row plus zero rows. DROW proves directly that its generic-rank five-by-five minor ideal is (f12) and its cokernel torsion has the same twelve simple lengths. This covers all cases with r=0.

The original boundary beta:K->(A+V+P+D) O(4) has the same image after adding the zero A row, and K->Q is a locally split surjection. Thus its generic-rank minor ideal and cokernel torsion are identical to those just computed. This preserves scheme structure, not only rank-drop support. The torsion is a length-twelve equivariant skyscraper sheaf in the r=0 case; no character identification beyond that is needed.

## 7. Actual-kernel consequences and limitations

DROW already identifies the original kernel sheaf under the retained two-D-channel hypothesis: A O(-6) when e=1, and S O(-5) when e=0. Those prior results are retained, not counted as new here. Formula (2) now determines exactly when the fibers acquire an additional kernel dimension: precisely r=0, at every point of Omega, with simple cokernel torsion. If r=1 there is no fiber-rank jump anywhere.

Thus within this branch the remaining exceptional-fiber and torsion question is reduced to the two explicit comparison expressions (1). They are universal normalized coefficient relations, not asserted actual equalities or inequalities. The actual values of all six channels, the occurrence of a_D b_D nonzero, and any global odd-quadric, top-sigma, vertex-delta, or catalogue conclusion remain open.

No selected actual HM/source coefficient, point, parameter, jet, derivative, matrix or instance rank has been evaluated. The proof uses universal binary polynomial multiplication, equivariant bundle exactness, fixed stabilizer characters, and local algebra valid uniformly over the entire orbit.
