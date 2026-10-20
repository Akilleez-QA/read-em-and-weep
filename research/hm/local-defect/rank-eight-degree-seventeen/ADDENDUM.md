> Publication scope: preserved mathematical proof/audit. Historical statements that rank eight remains open are superseded only after the final assembly and all its prerequisites. No source-instance evaluation or formal verification is claimed here.

# No negative-twist sections on the remaining R branch

## Result

In the actual standing application, the invariant irreducible20-dimensional space J generates R via J tensor O -> R. Combining this fact with PROOF.md gives

    H0(R(-j))=0 for every j>=1,
    h0(R) belongs to {20,25}.

This is still a structural restriction, not an exclusion of (19,17).

## 1. The possible saturated images of linear-twist sections

Suppose W=H0(R(-1)) is nonzero. PROOF.md gives dim W in {5,10}. Let A be the image of W tensor O(1)->R and B its saturation in R. Set k=rank B, det B=O(a), and det A=O(a0). All these sheaves are N-invariant and have untwisted central weight3. Both determinants therefore have degree congruent to2k modulo5.

The globally generated torsion-free sheaf A(-1) has effective determinant, so a0>=k. The torsion-free quotient Q=R/B is globally generated, hence has nonnegative determinant degree, giving a<=6. Saturation gives a0<=a. Thus

    k<=a0<=a<=6,   a0==a==2k (mod5).

In particular a-a0 is a nonnegative multiple of5, but at most6-k. The permitted pairs (k,a) are exactly

    (1,2), (2,4), (3,6), (5,5).

For each of these pairs a-k<5, so a=a0. Consequently A and B agree in codimension one, and B(-1) is generated outside a subset of codimension at least two. This establishes, rather than assumes, the generation property of the saturated image needed below.

## 2. The Chern bound with codimension-two base locus

For a torsion-free sheaf T generated outside codimension two with c1(T)=d,

    0<=c2(T)<=d^2.

Indeed, the same general-(rank-1)-section quotient lemma used throughout the standing proofs gives an ideal quotient I_Y(d), with degree Y=c2(T). Its degree-d system has no fixed divisor, because generation holds at all codimension-one points. A general plane section is a finite scheme of length c2(T), and two coprime degree-d equations yield the upper bound. This does not require generation at the finite base locus on that plane. Rank one follows directly from the ideal-sheaf description.

We also use the established full-support Heisenberg Chern congruence from ../full-support-equivariant-chern-congruences/PROOF.md:

    c2(T) == binom(rank T,2) w^2 (mod5)

for every equivariant coherent sheaf of uniform central weight w.

## 3. Exclusion of all four image types

### Type (1,2)

The rank-one torsion-free B embeds into B**=O(2). All sections W factor through B(-1), hence W injects into H0(O(1)), of dimension5. Therefore dim W=5 and its image is the full space of linear forms. These generate O(1) sheaf-theoretically; since their evaluation factors through B(-1), it follows that B=O(2). This gives a section of R(-2), contradicting PROOF.md.

### Type (2,4)

B(-1) is torsion-free, generated outside codimension two, and has c1=2. Hence

    0<=c2(B(-1))<=4.

The rank-two twisting formula gives c2(B(-1))=c2(B)-3, so 3<=c2(B)<=7. The central-weight3 congruence gives c2(B)==9==4 modulo5. Consequently c2(B)=4.

The globally generated torsion-free quotient Q has rank6 and

    c1(Q)=2,
    c2(Q)=17-c2(B)-c1(B)c1(Q)=17-4-8=5.

This contradicts c2(Q)<=c1(Q)^2=4.

### Type (3,6)

Now Q has rank5 and determinant O. Since it is globally generated and torsion-free, it is O^5 by PROOF.md, fact (2). The invariant quotient induces an equivariant linear map

    J -> H0(Q),   dim H0(Q)=5.

Irreducibility of J forces this map to vanish. But J generates R and therefore generates every quotient of R. A zero image cannot generate the positive-rank Q. This is a contradiction.

This step uses the actual surjection J tensor O -> R, a stronger hypothesis than merely having an injected copy of J in H0(R).

### Type (5,5)

Here a0=a=5, and A(-1) is globally generated and torsion-free with trivial determinant. Thus A(-1)=O^5 and A=O(1)^5. Because A is reflexive and A and its saturation B agree in codimension one, B=A. The quotient Q has rank3 and

    c1(Q)=1,
    c2(Q)=17-c2(O(1)^5)-5*1=17-10-5=2.

This contradicts c2(Q)<=1.

Every permitted saturated image is impossible. Therefore W=0.

## 4. Section count

All twists below -1 already vanish by PROOF.md, so every negative twist of R has no sections. In the general-seven-section quotient, z5=0 and z6=h0(R)-7. The uniform plane/curve bound c6<=22 from PROOF.md gives

    13<=z6<=22,
    20<=h0(R)<=29.

Central weight3 forces h0(R) divisible by5. Hence h0(R) is20 or25.

## Evidence boundary

This proof uses only universal sheaf geometry and the already established equivariant Chern congruence, irreducibility of J, and generation by J. It evaluates no source, matrix, operation, input, rank instance, jet, or residue. The only new write is this local proof artifact.
