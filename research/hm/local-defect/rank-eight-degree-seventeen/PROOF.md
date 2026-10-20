> Publication scope: preserved mathematical proof/audit. Historical statements that rank eight remains open are superseded only after the final assembly and all its prerequisites. No source-instance evaluation or formal verification is claimed here.

# Degree-seventeen rank-eight side: no quadratic subline

## Result

Under the standing full-normalizer equivariance hypotheses, the remaining rank-eight sheaf R satisfies

    h0(R(-j)) = 0 for every j >= 2,
    h0(R(-1)) belongs to {0,5,10},
    h0(R) belongs to {20,25,30,35}.

This is a new structural constraint, not an exclusion of the pair (19,17).

Hypotheses: R is torsion-free and globally generated on P4, rank 8, c1=6, c2=17, central weight 3, and H0(R) contains the established irreducible N-module J of dimension 20. Here N contains H5 with its usual scalar-center action on P4. Twisting down by one raises central weight by one. We use the section quotient

    0 -> O^7 -> R -> I_Z(6) -> 0,

with degree Z=17 and sextics without a fixed divisor. Thus z6=h0(R)-7 and z_(6-j)=h0(R(-j)) for j>=1. No equivariance of the chosen Z is asserted or used.

## 1. Uniform plane bounds

For a general regular flag Z,C,D, let p_i=h0(I_D(i)), c_i=h0(I_C(i)), and z_i=h0(I_Z(i)). The scheme D has length17 and its sextics have no fixed curve. The established residual Bezout argument gives p2=0 and p3<=1: for two cubics with gcd degree t<=2 the bound is 17<=6t+(3-t)^2, whose right side is at most13.

If p3=1, link D inside CI(3,6), with residual length1. Finite-plane liaison (as proved in the intermediate-sextic proof) gives

    (p3,p4,p5,p6)=(1,3,6,11).

If p3=0, then p4<=2. Indeed, if the whole quartic system has dimension at least3, take its gcd h of degree t<=3 and two divided members with no common curve. Residual Bezout gives

    17<=6t+(4-t)^2.

Only t=3 survives. But three independent divided linear forms span all plane linear forms, so their sheaf ideal is the unit ideal; since their products with h vanish on D, h itself vanishes on D. This contradicts p3=0. Consequently H_D(4)>=13. Strict Hilbert-function growth until length17 gives H_D(5)>=14 and H_D(6)>=15, hence

    p4<=2, p5<=7, p6<=13.

The two restriction recurrences c_i<=c_(i-1)+p_i and z_i<=z_(i-1)+c_i therefore give, uniformly,

    z3<=1, c4<=4, c5<=10, c6<=22.

The central weight of R(-3) is1, so z3 is divisible by5 and therefore zero. Thus all lower z_i vanish and z4<=4. Also z5 is divisible by5.

## 2. Three elementary equivariant and generation facts

(1) If an N-equivariant torsion-free sheaf B has rank k, central weight w, and determinant O(b), then

    b == -k*w (mod 5).

Indeed, the standard O(b) linearization has central weight -b. Any two N-linearizations of this line bundle differ by a character. Every character is trivial on the center of H5, which is a commutator subgroup. Apply this also to double-dual determinants.

(2) A globally generated torsion-free sheaf T with determinant O is trivial. Choose rank(T) sections with nonzero generic determinant. Their wedge is a nonzero constant. The resulting map O^rank(T)->T** is an isomorphism in codimension one, hence everywhere by reflexivity. The image lies in T, proving T=T**=O^rank(T).

(3) A globally generated torsion-free sheaf T with c1=d has

    0<=c2(T)<=d^2.

The lower bound and upper bound follow from the usual general-(rank-1)-section ideal quotient I_Y(d): on a regular general plane the finite scheme has length c2(T), and its degree-d system has no fixed curve. Two coprime members give the upper bound by Bezout. Rank one is the same argument directly. For d=0, fact (2) is stronger. These arguments use the same torsion-free section-quotient lemma as the standing proofs.

## 3. At most one section of R(-2)

Let A be the image of all sections of R(-2), regarded as a subsheaf of R, and put k=rank(A). Suppose k>0. Then A(-2) is globally generated and has central weight0. Writing det A=O(a), fact (1) gives

    a-2k == 0 (mod5).

Generation gives a>=2k. Let B be the saturation of A in R. The quotient R/B is torsion-free and globally generated, so c1(B)<=6, while c1(A)<=c1(B). Hence 0<=a-2k<=6-2k<=4. It follows that a=2k; by fact (2),

    A=O(2)^k.

Both A and its saturation B are invariant. Their determinant difference is the degree delta of an effective invariant divisor. By fact (1), delta is divisible by5; but 0<=delta<=6-2k<=4. Thus delta=0. Since A is reflexive, a torsion-free saturation with the same codimension-one stalks embeds into A**=A. Hence B=A and Q=R/A is torsion-free and globally generated.

Necessarily k<=3. Chern classes give

    c1(Q)=6-2k,
    c2(Q)=17-10k+2k^2.

For k=2 these are (2,5), contradicting fact (3). For k=3 they are (0,5), contradicting fact (2). Hence k=1. Since all sections of R(-2) factor through A(-2)=O, there is exactly one such section. This proves z4 is either0 or1.

## 4. The single-section case is impossible

Suppose z4=1. Its unique section line is N-invariant; multiplication by quadrics injects an invariant 15-dimensional space into H0(R), since R is torsion-free. Its intersection with the irreducible20-dimensional J is zero. Therefore

    h0(R)>=35.

On the other hand z5<=z4+c5<=11 and z5 is divisible by5, so z5<=10. Then z6<=z5+c6<=32, hence h0(R)<=39. Untwisted central weight3 makes h0(R) divisible by5. Consequently

    h0(R)=35, z6=28, z5=10.

The last equality uses 28=z6<=z5+22 and divisibility of z5.

The preceding section supplies an invariant exact sequence

    0 -> O(2) -> R -> Q -> 0,

where the line bundle may carry a character twist, and Q is torsion-free, globally generated, rank7, c1=4, c2=9. Line-bundle cohomology gives

    h0(Q)=20, h0(Q(-1))=5, h0(Q(-2))=0.

Moreover H0(Q) is precisely the irreducible module J: J injects into it and both have dimension20.

Let B now denote the saturation in Q of the image of all sections of Q(-1), and write k=rank(B), det B=O(b). This is invariant. Its untwisted central weight is3, so b==2k (mod5). Generation of the unsaturated image after twisting by -1 gives b>=k. The torsion-free globally generated quotient Q/B has nonnegative first Chern class, so b<=4. These inequalities and congruence leave only

    (k,b)=(1,2) or (2,4).

For (1,2), B embeds in B**=O(2). Its five independent sections after twisting by -1 inject into H0(O(1)), also dimension5. They are all linear forms and generate O(1) as a sheaf, so B(-1)=O(1). Thus O(2) embeds in Q, contrary to h0(Q(-2))=0.

For (2,4), the quotient Q/B is globally generated and torsion-free of rank5 with determinant O; therefore it is O^5. The map H0(Q)->H0(O^5) is surjective: global generation of Q implies that its image spans every fiber, and sections of O^5 are constant. Since B is invariant, this is an equivariant quotient of dimension5 of the irreducible20-dimensional H0(Q)=J, impossible.

Both cases contradict the single-section assumption. Therefore h0(R(-2))=0. Its lower twists vanish as well.

## 5. Remaining numerical bounds

Now z4=0, so z5<=c5<=10 and z5 belongs to {0,5,10}. Also z6<=z5+c6<=32, so 20<=h0(R)<=39. Central-weight divisibility yields the claimed list {20,25,30,35}.

In particular, the surviving pair cannot be explained by an equivariant quadratic line subbundle or by two or more independent quadratic sections.

## Evidence boundary

Only universal torsion-free sheaf geometry, plane Hilbert functions, abstract central-weight congruences, and the already established irreducibility of J are used. No actual source, matrix, operation, input, rank instance, jet, residue, or large computation was used. The only new write is this local proof artifact.
