# Internal fourth-through-seventh vanishing and the canonical octic gate

## Statement and scope

Assume an actual source126 Type II occurrence with its entire radical J compatible with Q, retaining the exact hypotheses of PR973, PR979, PR982 and PR985. Write A=Sym²W, D=Sym⁴W, X=P(A), and

    0→A O_X(−1) --B--> D O_X→E→0,
    B_a(k)=ak.                                             (1)

Here X is a PLANE. Thus H0(O_X(m))=Sym^m(A*)≅Sym^m A as G-representations, not Sym^m W. G acts through A5 on these even representations.

The internal fourth through seventh symbols of the actual annihilator complex S are globally defined and identically ZERO. In particular:

    r4:D O_X(−4)→E,  r5:D O_X(−5)→E.                       (2)

The sixth and seventh symbols are also ZERO. Before imposing quotient-kernel naturality, each has a canonical one-dimensional rank-one space as its only possible nonzero values. Naturality excludes both entire lines. The internal eighth symbol is globally defined and lies in a canonical one-dimensional line whose nonzero members have generic rank1 and satisfy quotient-kernel naturality. Its actual scalar is unselected.

Thus the universal rank-one exclusion alone is sharp: it holds in degrees4 and5 but fails in degree6; the actual sixth and seventh vanishings require an additional quotient-kernel naturality argument. This is about INTERNAL symbols of S. PR985's all-orders ORIGINAL generic vanishing is already known and is not being counted again. No actual HM coefficient, direction, matrix, parameter or rank is evaluated, no source occurrence is excluded, and no complete repair is claimed.

## 1. Retained actual complexes and rank bound

PR973 gives H0(S)=A+D, H1(S)=D, with first symbol B on A and zero on D. Multiplication by any nonzero binary quadratic is injective, so B is a rank3 subbundle map everywhere on X and E is locally free of rank2. PR979 gives internal second zero. PR985 gives internal third zero, using PR982's global construction and rank-one exclusion.

PR985 also proves rank(M)≤36 over every scalar extension. PR973 identifies the quotient first symbol of T as generically onto, so rank(T)=13 over the generic Laurent-series field. The block-upper-triangular family then gives rank(S)≤23. In particular S, with target dimension24, is NOT onto over that field. After cancelling its 19 Q-unit pairs and three first-order pivots, S has a surviving map from a five-space to a two-space and this map has rank at most1.

## 2. A global recursive construction, without rational division

Fix G-equivariant splittings of the constant map Q_S. Let H be a right inverse onto its image and let p:S1→D identify its cokernel. Start with h in the actual D kernel and homogeneous correction polynomials u_i(a,h) of degree i in a, satisfying

    u0=h,  Q_S u_i=−T_a u_(i−1).                         (3)

Suppose lower internal symbols2 through n−1 are identically zero. We construct u1,...,u_(n−1) globally, with

    p T_a u_i=0 for i≤n−2.                               (4)

The base u1^raw=−H T_a h exists because the first symbol kills D. At a general step, once u_i exists, the class

    π p T_a u_i:D O_X(−i−1)→E

is the next obstruction. If it is zero, the polynomial map p T_a u_i factors uniquely through the subbundle B in (1). The factor is a GLOBAL morphism

    k_i:D O_X(−i−1)→A O_X(−1),

so its entries are homogeneous polynomials of degree i in the three coordinates of A. This is exact sheaf factorization through an injective subbundle, not division by a selected quadratic coefficient. Replace u_i by u_i−k_i, viewing A as its actual kernel summand. Equation (3) is unchanged, while p T_a u_i becomes zero. Then define u_(i+1)=−H T_a u_i. This proves (3)-(4) inductively.

The next symbol is

    rn=π p T_a u_(n−1):D O_X(−n)→E.                     (5)

All choices may be G-equivariant, and every step preserves homogeneous polynomial degree. Thus (5) is a global equivariant bundle map.

Here is an explicit choice-independence argument. Work on any affine open of X trivializing the twists, with an arbitrary pair of normalized correction sequences for the same h. Their differences d_i obey (3) and (4), with d0=0. The first nonzero difference d_m is Q-closed. If m≤n−2, (4) implies B times its A component is zero; injectivity of B makes that component zero. Thus d_m is D-valued. Subtract from the difference sequence the shifted normalized lift sequence starting with d_m, which exists through the required order because all intervening symbols vanish. This eliminates d_m and contributes to the final residual only the internal symbol of order n−m on d_m, zero modulo B by the hypothesis. Repeat. At the final index m=n−1, a Q-kernel difference contributes only its first symbol, which is in B(A) and disappears in E. Hence (5) is choice-independent locally, therefore globally. This is the ordinary higher Bockstein on the unchanged surviving D and E, not merely a same-sized auxiliary polynomial map.

Applying this construction with the already known second/third vanishings gives r4 globally. Once r4 is proved zero below it gives r5, and then r6; sixth vanishing in turn permits r7. No assumptions about a sixth or seventh symbol are used to construct or kill the fourth or fifth.

## 3. Classify possible equivariant rank-one maps

Let f:D O_X(−n)→E be nonzero with generic rank1. Saturate its image in E. The saturated rank-one subsheaf L is locally free: E/L is torsion-free, so at closed points on the smooth surface the depth lemma gives depth(L)≥2; L is reflexive and hence a line bundle O_X(k). Saturation is G-stable. A5 has no characters, so its linearization is the canonical one.

The nonzero factorization is

    D O_X(−n)→O_X(k)→E.                                (6)

From (1), H0(E(−1))=0, using H0(O(−1))=0 and H1(O(−2))=0 on the PLANE. All more negative twists vanish as well. Thus k≤0. The first map requires k+n≥0 and a D constituent in Sym^(k+n)A. The second map requires a nonzero invariant section of E(−k). Hence necessary conditions are

    −n≤k≤0,
    [D:Sym^(k+n)A]>0,
    H0(E(−k))^G≠0.                                    (7)

These statements concern actual equivariant factorizations; no inference from rank dimensions alone is made.

## 4. Exact character calculation and sharp cutoff

Use the A5 conjugacy-class sizes(1,15,20,12,12), with φ=(1+√5)/2, and characters

    χA=(3,−1,0,φ,1−φ), χD=(5,1,−1,0,0).

For h_m=χSym^m A, the determinant-one three-dimensional recurrence is

    h_m=χA h_(m−1)−χA h_(m−2)+h_(m−3).

Here Λ²A≅A. Negative subscripts mean zero, and h0=1. Twisting (1), with H1(O(m−1))=0, gives

    χH0(E(m))=χD h_m−χA h_(m−1),  m≥0.

The resulting multiplicities, for m=0,...,8, are

    [D:Sym^m A]       = (0,0,1,0,2,1,3,2,5),
    dim H0(E(m))^G   = (0,0,0,0,1,1,1,1,2).                (8)

For n4 the source-eligible k are−2,0; their target invariant spaces E(2),E(0) both vanish. For n5 they are−3,−1,0; E(3),E(1),E(0) all have no invariant section. Thus EVERY nonzero equivariant map D O(−4)→E or D O(−5)→E has generic rank2.

For n6 the source-eligible k are−4,−2,−1,0. Only k=−4 survives both conditions. Moreover

    dim Hom_G(D O(−6),O(−4))=1,
    dim Hom_G(O(−4),E)=1.                              (9)

Choose nonzero representatives c and σ. Their composition σc is nonzero and has generic rank1, since each factor is nonzero at the generic point. Every rank-one map in degree6 must factor as in (6) with k=−4 and therefore is a scalar multiple of this composition. Rescaling c and σ leaves its line unchanged. Thus

    L6=C·(σc) ⊂ Hom_G(D O(−6),E)                       (10)

is canonical, and it is exactly the locus of rank-at-most-one maps. The full equivariant Hom space in degree6 has dimension7; the rank-one line is not the full space.

For n7 the source-eligible k are−5,−3,−2,−1,0. Only k=−5 survives, because H0(E(5))^G is one-dimensional and the invariant spaces E(3),E(2),E(1),E(0) vanish. Its source row has degree2 and is again the SAME one-dimensional factor space. Thus the rank-at-most-one maps of degree7 also form a canonical line L7=C·(σ5 c), where σ5 spans H0(E(5))^G.

The invariant σ in degree6 cannot have a divisorial zero: saturation would yield an equivariant inclusion O(k)→E with k>−4, contradicting the first four invariant vanishings in (8). This is consistent with, but not needed for, the nonzero composition argument.

## 5. Apply the universal result to the actual internal symbols

If r4 were nonzero, §4 would make it generically onto the rank2 E. After the 19 constant and three first-order cancellations, the first remaining differential would then have rank2 over the generic Laurent field, making S onto. This contradicts §1. Therefore r4=0 as a global bundle map: it is zero generically, and X is integral.

Now §2 constructs r5. The identical rank2 contradiction using §4 gives r5=0 globally. Section2 then constructs r6. Its generic rank cannot be2 by the same nonsurjectivity argument, so r6 lies in the canonical line L6. Section6 now excludes every nonzero value in that line.

This argument does not identify any later original Bockstein as newly nonzero; all later original generic Bocksteins were already killed in PR985. It also does not prove all later INTERNAL symbols zero. Degree6 admits an abstract rank-one possibility, but the actual-complex naturality in the next section excludes it. Section7 gives the bounded degree8 continuation; degree9 and above are not classified here.

## 6. Quotient-kernel naturality kills the sixth and seventh lines

PR973 and PR982 identify the quotient first symbol b_T:D O(−1)→P O and its kernel inclusion

    κ:O(−5)→D O(−1).

The quotient first symbol is onto on a dense open, so its first-kernel vectors admit quotient corrections to every finite order over the generic Laurent-series field. Each radical element descends to a chain map T→S for the ENTIRE family, and some such map induces a nonzero scalar on the D degree-zero cohomology. Applying that radical map to the quotient correction strings and using the zero internal symbols2 through5 gives

    r6 κ(−5)=0:O(−10)→E.                               (11)

This is higher-differential naturality on actual liftable cycles. The canonical choice-independence from §2 identifies the resulting sixth class with r6, regardless of the lift choices. The maps in (11) are globally regular, so equality on the dense onto locus extends over X. No assumption that kernel formation commutes with specialization at the ten exceptional directions is made.

We show that the unique rank-one generator σc from §4 violates (11). The unique source factor c is, up to nonzero scalar, the apolar pairing

    c_a(h)=⟨a²,h⟩,                                    (12)

since multiplication Sym² A→D followed by the invariant perfect pairing on D is a nonzero equivariant degree-two scalar form. The dimension-one statement in (9) makes this the SAME source factor, not an unrelated quadratic.

The exact PR982 §3 argument uses the universal sextic V linear series and its nonzero Wronskian: at a GENERAL, UNSELECTED square a=ℓ² outside the finite flex divisor, the quotient first kernel is generated by h=v/ℓ², where v has zero of exactly order2 at the zero of ℓ. Thus h is not divisible by ℓ. In universal coordinates with ℓ=x, write h=Σ h_i x^(4−i)y^i. Then h4≠0 and the normalized apolar pairing gives

    ⟨x⁴,h⟩=h4≠0.

This is a symbolic identity on the universal binary representation, not selection or evaluation of an actual HM parameter. Consequently c κ(−5):O(−10)→O(−4) is a NONZERO map. Its scalar polynomial has degree6 on the parameter PLANE; no binary-versus-plane degree is interchanged.

Since σ:O(−4)→E is nonzero and X is integral, composing σ with that nonzero scalar map cannot give zero. Therefore no nonzero element of L6 satisfies (11). It follows that r6=0 globally.

Now §2 constructs r7 because all previous internal symbols through6 vanish. Its generic rank is at most1 by nonsurjectivity, so §4 places it in L7. The same higher-cycle argument gives

    r7 κ(−6)=0:O(−11)→E.

Its source row c is still the quadratic pairing (12), now from D O(−7) to O(−5). The composite cκ(−6) is the SAME nonzero degree-six scalar polynomial. Multiplication by the nonzero invariant section σ5 cannot kill it. Thus L7 has no nonzero element satisfying naturality, and r7=0 globally.

Both universal rank-one lines remain valid representation-theoretic objects; it is their realization as actual sixth or seventh obstructions under these hypotheses that is excluded. The next section handles degree8 separately; no all-orders internal vanishing is claimed.

## 7. The canonical octic line survives both universal constraints

Section2 now constructs r8 globally, since all lower internal symbols2 through7 vanish. It has generic rank at most1 and satisfies

    r8 κ(−7)=0:O(−12)→E.                               (13)

For degree8, the saturated-line conditions (7)-(8) leave precisely k=−6 and k=−4. At k=−6 the source is again the unique quadratic pairing c, while the invariant section space H0(E(6))^G has dimension1. Its κ restriction is nonzero by §6, so this case cannot satisfy (13).

At k=−4 the invariant section σ spans H0(E(4))^G, while the quartic source-covector space is

    C4=Hom_G(D O(−8),O(−4)),  dim C4=2.                (14)

Restriction along κ(−7) defines a linear map from C4 into H0(O(8))^G. This restriction is nonzero: the invariant discriminant Δ(a), of degree2 on the plane, times the quadratic covector c of (12) is in C4 and has nonzero restriction Δ·cκ. Both factors are nonzero on the integral plane.

There is also a canonical NONZERO covector in the restriction kernel. The plane cubic representation has

    Sym³ A=A+V+P.

Choose a nonzero equivariant P-valued cubic cP(a), unique up to scalar, and a nonzero invariant perfect pairing on the irreducible P. Define

    ψ4(a)(h)=⟨cP(a), b_T,a(h)⟩_P.                     (15)

The quotient first symbol b_T is the actual nonzero linear family from PR973. Thus (15) is an equivariant quartic covector, and ψ4κ=0 because b_Tκ=0. It is nonzero: on the dense open where b_T has rank4 its dual is injective; intersecting that open with the nonzero locus of cP gives a nonzero covector. This is a generic open-set proof, not a selected-point calculation.

Therefore the restriction map from the two-dimensional C4 has nonzero kernel and nonzero image, so its kernel is exactly the canonical line C·ψ4. Every rank-one map in degree8 satisfying (13) must consequently lie in

    L8=C·(σψ4) ⊂ Hom_G(D O(−8),E).                    (16)

Conversely σψ4 is nonzero, has generic rank1, and satisfies (13). Hence (16) is EXACTLY the locus of equivariant maps of generic rank at most1 satisfying the quotient-kernel naturality condition. It is a line, not merely a dimension upper bound or a claimed realized coefficient. The full equivariant degree8 Hom space has dimension10.

The actual r8 therefore lies in L8. Its scalar is not determined. This is the first degree in the bounded analysis4 through8 at which the two tested universal constraints admit a nonzero map. It does not prove occurrence, a later original obstruction, or the absence of additional actual restrictions. No assertion about degree9 or higher is made.

## Verification and novelty boundary

The checker authenticates pinned inputs, uses the PLANE symmetric-power recurrence, verifies all possible saturated-line factors for degrees4,5,6,7,8, checks the full equivariant Hom dimensions, and checks the recursive polynomial normalization in a symbolic reduced complex. It evaluates no actual HM input.

A local search of the source126 proof packets and the existing higher-followup packet found no prior internal fourth/fifth theorem. The original all-orders vanishing is explicitly imported, not presented as new. The new result is global internal fourth-through-seventh vanishing, rigorous polynomial construction of these symbols, exclusion of the sixth/seventh rank-one lines by actual quotient naturality, and the canonical one-dimensional octic gate with unselected actual scalar.
