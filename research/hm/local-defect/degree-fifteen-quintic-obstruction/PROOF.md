> Publication scope: preserved mathematical proof/audit. Historical statements that rank eight remains open are superseded only after the final assembly and all its prerequisites. No source-instance evaluation or formal verification is claimed here.

# Degree-fifteen quintic systems: the reflexive branch

## Scope and results

Work over C. Retain the rank-six hypotheses of the existing quintic-surface-section-bounds proof. The degree-fifteen side M has rank ten, determinant O(5), at least twenty sections, and is generated outside codimension two. Its central weight is two for E=F*, three for R.

The arguments below prove that c2(E)=15 is impossible, hence exclude the ordered pair (15,10). They do not claim to exclude (10,15). In the latter pair, the degree-fifteen section scheme for R must have general hyperplane section a complete intersection (3,5), while having no cubic or quartic equation itself, and precisely eleven quintic equations. In particular h0(R)=20.

## 1. Plane bound

Let D be a finite plane scheme of length fifteen. Suppose its quintics have no fixed curve. Write i_j=h0(I_D(j)). Bezout gives i_2=0. For two independent cubics, writing their gcd degree t in {0,1,2} and choosing a quintic coprime to the gcd gives

    15 <= 5t+(3-t)^2,

whose right sides are 9,9,11, impossible. Thus i_3<=1. If i_3=1, a coprime cubic and quintic cut a length-fifteen scheme containing D, so D is exactly CI(3,5), with

    (i_3,i_4,i_5)=(1,3,7).

If i_3=0, then i_4<=2. Here are details including nonreduced schemes. Suppose i_4>=3 and let g be the gcd of the entire quartic system, of degree t. Two members can be chosen with gcd exactly g, by avoiding the finitely many proper divisibility subspaces after fixing one member. The residual length inequality gives

    15 <= 5t+(4-t)^2.

Since t<=3, this leaves t=0 or 3. If t=3, the space obtained by dividing all quartics by g contains at least three independent linear forms, hence all plane linear forms. Its sheaf ideal is the unit ideal, so g itself vanishes on D, contrary to i_3=0.

If t=0, choose two coprime quartics and put X=CI(4,4). The residual scheme T of D in X has length one. The standard complete-intersection duality is valid for arbitrary finite subschemes, not only reduced ones: inside the Artinian Gorenstein algebra O_X, annihilators identify I_D/I_X with the dualizing module of O_T tensored by omega_X^{-1}. Here omega_X=O_X(5). Thus the sheaf exact sequence, after twisting by four, is

    0 -> I_X(4) -> I_D(4) -> omega_T(-1) -> 0.

In cohomology the connecting map

    H0(omega_T(-1)) -> H1(I_X(4))

is dual to restriction H0(O_P2(1))->H0(O_T(1)), under Serre duality and the Koszul resolution of X. This is the usual functorial trace duality: the inclusion of the annihilator module is dual to the quotient O_X->O_T. The restriction is surjective, since T has length one and some linear form is nonzero at its point. Hence the connecting map is injective. Consequently H0(I_X(4))=H0(I_D(4)), and i_4=2, contradiction. A length-one finite C-scheme is a reduced point; X and D need not be reduced.

Finally H_D(4)=15-i_4>=13. The Hilbert function of a saturated finite scheme strictly increases until it reaches its length, because an avoiding linear form is regular and its Artinian quotient is standard graded. Thus H_D(5)>=14 and i_5<=7. In particular, in the no-cubic case,

    i_3=0, i_4<=2, i_5<=7.

## 2. Restriction inequalities and absence of global cubics

Take the general-nine-section quotient

    0 -> O^9 -> M -> I_Z(5) -> 0.

The surface degree of Z is fifteen. Its quintics have no fixed divisor and z_5=h0(I_Z(5))=h0(M)-9>=11. Choose successive regular hyperplane sections C in P3 and D in P2 as in the existing proofs; their quintics have no fixed divisor/curve. Set c_j=h0(I_C(j)) and z_j=h0(I_Z(j)). Then

    c_j<=c_(j-1)+i_j,   z_j<=z_(j-1)+c_j.

In particular z_3<=1. Twisting the quotient shows z_j=h0(M(j-5)) for j<5. For E, the central weight of E(-2) is four, so z_3 is divisible by five and is zero.

For completeness z_3=1 is impossible for R as well. A global cubic f and a global quintic q coprime to f give Z contained in X=CI(3,5), with equal surface degree. This is equality as schemes: the kernel of O_X->O_Z has no surface-dimensional support, while the Cohen--Macaulay pure surface O_X has no nonzero subsheaf supported in smaller dimension. Hence z_5=16 and h0(R)=25. The one-dimensional space H0(R(-2)) is an invariant character line for the full symmetry group. Multiplication by its nonzero section embeds H0(O(2)) (twisted by that character) into H0(R), as R is torsion-free. This is a fifteen-dimensional invariant subspace. The already established irreducible twenty-dimensional J also embeds in H0(R). Its intersection with the fifteen-dimensional subspace is an invariant proper subspace of J and hence zero. This requires h0(R)>=35, contradicting 25. This argument uses the full group preserving R and the established irreducibility of J, not irreducibility under the Heisenberg subgroup alone.

Thus z_3=0 in both cases. Also z_4=h0(M(-1)) is divisible by five for both weights. If D has no cubic, the restriction inequalities give z_4<=2, so z_4=0, and z_5<=c_5<=i_4+i_5<=9, impossible.

Therefore D=CI(3,5). Now c_3<=1, c_4<=4, c_5<=11, and z_4<=4. Divisibility forces z_4=0; consequently

    11 <= z_5 <= c_5 <= 11.

All bounds are equalities. In particular c_3=1, c_4=4, c_5=11, and h0(M)=20. A cubic equation of C and a coprime restricted quintic show, by the same purity argument inside their complete intersection, that

    C=CI(3,5) in P3.

## 3. Lifting when there is no zero-dimensional subsheaf

We record an elementary lifting lemma. Suppose Z is a projective scheme, H is a regular hyperplane, and C=Z intersect H has surjective ambient-polynomial restriction in every nonnegative degree and H0(O_C(t))=0 for t<0. If O_Z has no nonzero zero-dimensional subsheaf, then Z has the same surjectivity property, and every equation of C lifts in the usual ideal restriction sequence.

Indeed H0(O_Z(t))=0 for t sufficiently negative. Here is a precise argument on P4. At each closed point, absence of a zero-dimensional subsheaf means depth(O_Z)>=1 whenever its stalk is nonzero. Over the regular local ring of dimension four, Auslander--Buchsbaum gives projective dimension at most three, so sheaf Ext^4(O_Z,omega_P4)=0. At nonclosed points local dimension is at most three, so the same Ext vanishes automatically. In the local-to-global Ext spectral sequence computing Ext^4(O_Z(t),omega_P4), the terms are

    H^p(sheaf Ext^q(O_Z,omega_P4)(-t)), p+q=4.

For t sufficiently negative, all terms with p>0 vanish by Serre vanishing, and the p=0,q=4 term is zero by the preceding depth argument. Thus this global Ext group vanishes. Serre duality identifies it with H0(O_Z(t)) dual, proving the required vanishing.

The regular hyperplane sequence and negative-degree vanishing on C imply H0(O_Z(t-1))=H0(O_Z(t)) for t<0, hence all these groups vanish. For t>=0, surjectivity of polynomial restriction on C makes every section on C the restriction of an ambient polynomial, which lifts to an ambient polynomial on P4. Induction on t in

    0 -> O_Z(t-1) -> O_Z(t) -> O_C(t) -> 0

then shows every section of O_Z(t) is an ambient polynomial. Thus H1(I_Z(t))=0 for all integers t, and the ideal restriction exact sequence is surjective on H0. In particular a cubic equation of C lifts to a cubic equation of Z.

Apply this to M=E, which is reflexive. At a point of codimension d>=3, the depth lemma in 0->O^9->E->I_Z(5)->0 gives

    depth(I_Z)>=min(depth(E),d-1)>=2.

The structure sequence then gives depth(O_Z)>=1. Thus Z has no associated point of codimension three or four, in particular no zero-dimensional subsheaf. Its general hyperplane C is CI(3,5), hence has surjective polynomial restriction in all nonnegative degrees (by its Koszul resolution) and has no negative sections. The lifting lemma gives z_3>=1, contradicting z_3=0. This excludes c2(E)=15.

## 4. Boundary and caution

For R only torsion-freeness is presently known; the depth argument in Section 3 is unavailable. The surviving possibility necessarily has a zero-dimensional subsheaf in O_Z. This limitation is genuine for unrestricted schemes: a CI(3,5) surface together with five general exterior points has no cubic or quartic equations and has exactly eleven quintic equations. The five point evaluations impose independent conditions on linear and quadratic multiples of the cubic, respectively. Thus the established numerical equalities alone cannot eliminate isolated-point modifications.

Only universal geometry, abstract equivariant representation theory and existing local proof statements were used. No actual operation, source, selected input, rank instance, jet, residue, polynomial instance, or external write was used.
