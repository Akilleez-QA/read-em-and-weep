# The ef source of G3.11.ea6bced3bddf is impossible

## Claim and immutable scope

This note excludes exactly the original source125 tuple

    (a,b,c,d,e,f,g,h) = (0,0,0,0,1,1,0,1)

for the stable label G3.11.ea6bced3bddf. The original catalog at commit
db51525015bb7c5e825833d550d08dedf6f6ea96 gives

    E = (2P+D) O(-2) + Wp O(-5) + O(-8) + O(-10),
    A_q = O(-10) + O(4) + O(16),
    B_q = O(-18) + O(-6) + O(8),

and original determinant defect zero. This is a whole-source exclusion, not a claim that all remaining sources or the full label have been excluded.

Original actual-bundle and strict-top inputs are the files
ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md,
NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md,
ONE-ONE-ENDPOINT-DEGREE-WINDOWS-AND-159-NECESSARY-PAIRS.md,
one-one-endpoint-necessary-pairs.json, and
rank-three-quotient-frontier-144.json under research/hm/order-four-quadratic-load at that commit.

The actual internal/external derivative-image lemma and profile-free quadratic rank-one gap are in PR796 at d2b43060c83328dd5118aee6b9288fcfa0c873ac, research/hm/profile12-quadratic-block-exclusion/PROOF.md, Sections 3 and 8. First-polar generation is recalled in PR802 at e484640a6565c278321bf6557860262c1ac1b7df, research/hm/profile11-o16-constant-span-exclusion/PROOF.md, Section 5. The exact conventions and the separate source125 ee exclusion appear in PR846 at 1644b5221fe6f8c23f30401fd6f2dc64230c0f5f, research/hm/profile11-o16-six-source-exclusions/PROOF.md. The ee exclusion is not used to exclude ef here.

We work over C with the binary icosahedral group. Write W for its defining two-space, Wp for the other two-space, A=Sym2 W, S=Sym3 W, D=Sym4 W, T=Sym5 W, and V,P for the other even irreducibles of dimensions 3,4. All irreducibles are self-dual. Every nonzero invariant effective divisor on P1 has degree at least12.

The actual E is saturated in a constant bundle H O, its highest degree is -2, and H0(E^-(2))=0. Its derivative has saturated image A_q inside Q(-2), where Q=H O/E. Saturation here follows from original determinant defect zero. All equivariant direct-sum decompositions below are bundle decompositions, never presumed horizontal.

## 1. A forced high subsystem and its complete kernels

The O(4) component of the derivative on the top block is a map on its P multiplicity space to the single P occurrence in Sym6 W=V+P. Its kernel has dimension at least one. Take one P multiplicity line in this kernel and let

    F = (P+D) O(-2) subset E.

This is a saturated constant-multiplicity subblock. D has no O(4) component, and negative targets vanish by degree. Hence the external derivative of F lands only in the saturated O(16). Strict-top gives an injection P+D into H0(O(18)). A common divisor would have degree at least12 and leave at most seven independent sections, whereas dim(P+D)=9. Consequently

    p:F -> O(16)

is onto everywhere. No selected coefficient or parameter is used in this kernel construction, including when the entire lower P row is zero.

Set K0=ker p. The exact sequence and Sym18 W=A+V+2P+D, Sym19 W=W+Wp+S+2T give

    H0(K0(2))=0,
    H1(K0(2))=A+V+P,
    chi_G(K0(3))=-W.

Its complete list of possible equivariant splittings is

    K1=(V+P) O(-4)+O(-6),
    K2=Wp O(-3)+V O(-4)+Wp O(-5)+O(-6),
    K3=T O(-3)+O(-6)+O(-10).                    (1)

Here is the completeness argument. An atom R O(-j), j>=4, contributes R Sym(j-4) W to the genuine budget A+V+P of dimension10. The dimension bound (j-3)dim R<=10 and central parity restrict the possibilities. The complete atoms fitting this budget are

    atom             H1 at twist2       H1 at twist3
    A O(-4)               A                  0
    V O(-4)               V                  0
    P O(-4)               P                  0
    Wp O(-5)              P                  Wp
    O(-6)                 A                  W
    O(-10)                V+P                T.

For explicit exhaustion: trivial atoms have even j=4,6,8,10,12, giving respectively 1,A,D,V+P,P+D; only6,10 fit. Odd two-space atoms have j=5,7; W gives 1+A and A+D, neither fitting, while Wp gives P and V+D, only j5 fitting. Even three-space atoms have j=4,6; at j6, A^2 contains1 and V A=P+D contains D. Even rank4 and rank5 atoms have only j4, where P fits and D does not. The odd rank4 atom has only j5 and gives A+D. No rank6 odd atom fits the dimension bound. Thus the table is complete.

The negative W in chi_G(K0(3)) forces O(-6), consuming A. The remaining V+P budget is either V O(-4)+P O(-4), V O(-4)+Wp O(-5), or O(-10). The degree-minus-three coefficient is respectively0,Wp,T, giving (1). Every branch has rank8 and degree-34.

## 2. All internal images, with saturation

The internal derivative on K0 has target

    (E/F)(-2)=P O(-4)+Wp O(-7)+O(-10)+O(-12).

For K1 its only possible nonzero component is the scalar P O(-4) -> P O(-4). For K2 its only possible nonzero component is Wp O(-5) -> P O(-4). For K3 its only possible components are O(-10) -> P O(-4) and O(-10) -> O(-10). All other components vanish by degree or the character identities

    P W=Wp+T,
    P Sym2 W=V+P+D,
    P Sym3 W=S+2T,
    Wp absent from Sym3 W,
    P absent from Sym2 W.

The K2 map is the unique tautological inclusion Wp O(-5) -> (Wp W) O(-4)=P O(-4), hence saturated. The nonzero K3 map to P O(-4) is a degree6 P-covariant. Its base divisor is invariant of degree at most6, hence zero. If its O(-10) component is also present, it is a graph; a nonzero scalar component itself ensures saturation. Thus every possible nonzero K3 image is a saturated copy of O(-10), regardless of which scalar components vanish.

It follows that the complete actual saturated internal-image list is

    J=0, P O(-4), Wp O(-5), or O(-10).            (2)

The external O(16) is saturated too. The internal/external image lemma therefore gives the actual raw derivative image I, already saturated, and M=F^+ through

    0 -> J -> I -> O(16) ->0,
    0 -> F -> M -> I(2) ->0.                     (3)

In particular no generic-image or hidden divisor correction occurs in the following degree and character arguments.

## 3. The three nonzero internal images

First polars of the quadratic F give an onto map (P+D) W O(-1) -> M. Since M is saturated in a constant bundle, its splitting degrees are exactly0 or-1. Additivity in (3) determines the constant coefficient C and the linear coefficient L in M=C O+L O(-1):

    J=P O(-4):   M=(A+V) O+(Wp+T) O(-1),
    J=Wp O(-5):  M=(A+V) O+T O(-1),
    J=O(-10):    M=A O+(Wp+T) O(-1).             (4)

For example chi_G(M) is A+V+P plus chi_G(J(2)); chi_G(M(1)) is Sym19 W plus chi_G(J(3)). Subtracting C W from the latter gives precisely the three L above.

C is the actual constant space H0(M) inside H. Projecting by it gives a saturated actual linear bundle

    L0=L O(-1) subset (H/C) O.

The projected F and all its first derivatives lie in L0. If the image of F contains a complete nonzero direct linear summand of L0, local lifts through F show that the derivatives of that summand stay inside L0. But the first span of any embedded pure linear bundle is its nonzero constant coefficient space. This would put a nonzero constant subbundle in L0, contradicting H0(L0)=0. We now show that (4) always has this forbidden property.

The map D O(-2) -> L0 can only have a T component, in a one-dimensional Hom space. This component is nonzero. Otherwise D O(-2) embeds in C O. For C=A, dimensions already contradict injectivity. For C=A+V of dimension6, its saturated first span is C O: it has rank strictly greater than5, since a negative saturated bundle cannot be horizontal, and at most6. Hence C/D O(-2)=O(10). The external derivative on D then factors through O(8). The derivative D O(-2)->O(8) is generically onto, and its composite in Q(-2) lies in the saturated O(16); consequently the induced O(8)->Q(-2) itself factors through O(16). The required equivariant map O(8)->O(16) is zero because Sym8 W=P+D has no invariant. This would kill the D top block under the original derivative, contradicting strict-top. Thus the D-to-T scalar is nonzero in every case.

The P projection to L0 is also nonzero. If P O(-2) embedded in C O, its A component would vanish since P is absent from A Sym2 W=1+A+D. Its image would lie in the rank3 V constant block, when present, contradicting injectivity of a rank4 bundle.

The unique nonzero D-to-T channel is the tautological sequence

    0 -> D O(-2) -> T O(-1) -> O(4) ->0.         (5)

A nonzero P-to-T channel induces a nonzero map to O(4): otherwise it factors through D O(-2), but Hom_G(P,D)=0. This degree6 line system is onto everywhere because there is no invariant divisor of degree<=6. Therefore, when L=T, the P+D image covers the complete T O(-1), contradiction.

For L=Wp+T, denote the P-to-Wp and P-to-T scalars by a,b. At least one is nonzero. If a=0, the preceding paragraph gives the entire T summand. If b=0, the P-to-Wp map is the tensor-Wp Euler surjection P O(-2)=(Wp W) O(-2)->Wp O(-1), giving the entire Wp summand.

Finally suppose a,b are both nonzero. Modulo the D image in (5), the P map is

    P O(-2) -> Wp O(-1)+O(4).

Its projection to Wp O(-1) is the Euler surjection, with kernel Wp O(-3). The restriction of the O(4) component to this kernel is nonzero: if zero, it would factor through Wp O(-1), whereas Hom_G(Wp O(-1),O(4))=0 because Wp is absent from Sym5 W=T. Its degree7 line system has no invariant divisor and is onto. The displayed rank3 target is therefore covered everywhere. Adding the D image covers all of L0, again contradiction. This exhausts every scalar-zero and nonzero case and excludes all three nonzero J alternatives.

## 4. The zero internal image and constant descent

Suppose J=0. Equations (3) give rank M=10 and degree0. Since M is a saturated subbundle of H O, it is the actual constant bundle C O, with

    C=chi_G(M)=A+V+P.

Moreover C O/F=O(18) maps isomorphically to the saturated high O(18) summand in Q. Hence E intersect C O=F exactly, and the actual constant projection gives a saturated embedded bundle

    E'=E/F=P O(-2)+Wp O(-5)+O(-8)+O(-10)
       subset (H/C) O.

Its derivative has saturated image O(-10)+O(4), obtained by quotienting the original A_q by O(16). This identification uses the actual constant projection, not a horizontal splitting of E or Q.

Let F'=P O(-2) be the top block of E'. Strict-top for E' forces a nonzero map to O(4); the negative target is zero by degree. Its degree6 P-covariant has no invariant base divisor, so it is onto. Its kernel is exactly V O(-4): at twist2 the H1 budget is Sym6 W-P=V, and at twist3 the Euler character is P W-Sym7 W=0; dimension, parity, and genuineness leave only V O(-4).

The internal target for this kernel is

    (E'/F')(-2)=Wp O(-7)+O(-10)+O(-12),

so every internal component vanishes by degree. The derivative image is exactly the saturated O(4). Consequently

    (F')^+/F'=O(6).

The profile-free rank-one quadratic gap says that for quadratic rank r with saturated raw derivative and line quotient O(b), either b=2r or b<=r-1. Here r=4,b=6, whereas the alternatives are8 or at most3. This is impossible.

For clarity, the gap uses only the constant connection: the second span of a quadratic bundle is its constant coefficient span. With first increment1, that span has rank r+1 or r+2. In the former case degree zero forces b=2r; in the latter the nonzero derivative O(b)->O(2r-b-2) gives b<=r-1. No interior-profile or section-free hypothesis is used.

All branches in (2) are now excluded. This proves the stated ef source exclusion.

## Boundary

The attached verify.py checks the declared six kernel atoms, three kernels, all 40 fixed internal Hom spaces, first-polar and Euler-channel characters, and the exact original source identity against immutable Git blob pins. REPRODUCE.md gives the input-download instructions. These bounded arithmetic checks do not replace the connection and saturation proofs above.

No selected actual HM/source coefficients, parameters, points, derivatives, matrices, instance ranks, scans, or large computations are used. The proof treats the entire source stratum with universal characters, bundle kernels, saturation, and the actual constant connection. It does not remove any other source, assert a current source-pair count, exclude the full stable label, or establish source2/global completion. This is written mathematics, not Lean certification.
