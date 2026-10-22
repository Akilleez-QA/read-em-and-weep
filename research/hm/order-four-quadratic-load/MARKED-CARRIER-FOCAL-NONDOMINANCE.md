# A normalization focal bound prevents the marked sextic or heptic from sweeping P4

## New conclusion

Let T be a dense open subset of the four-dimensional space of hyperplanes in P4. Suppose D_t⊂H_t is an algebraic family of geometrically integral curves, and D_t contains the 25 points Z_t=C∩H_t on the fixed union C of 25 skew lines. Assume these marked points are smooth on D_t, as established for the canonical marked cubic-base carrier.

If either

- deg D_t=7 and p_a(D_t)=5, or
- deg D_t=6 and D_t is nondegenerate in H_t=P3,

then the reduced closure of the swept image ⋃D_t has dimension at most three. In particular, neither family can dominate ambient P4. For the intrinsic Heisenberg-equivariant marked-carrier family, the swept image is in fact an invariant integral hypersurface containing C, and its degree is a positive multiple of five.

The argument allows arbitrary singularities away from the marked points, does not assume the original curves are Gorenstein or locally complete intersections, and does not claim that a three-dimensional swept hypersurface is excluded.

## 1. A smooth normalization family is available on a dense open

Start with the geometrically integral generic curve over the function field K of T. Its normalization is a smooth projective curve over K in characteristic zero. The finite birational normalization map, the smooth projective curve, and its morphism to P4 spread out over a dense open subset of T. Shrink the base so the spread is smooth and proper with geometrically connected fibers, the map to the original family is finite, and it is an isomorphism on a dense open of each fiber. These conditions hold generically and spread after shrinking. Thus the map on each retained fiber is its normalization. A finite generically étale base change can alternatively be used when choosing a geometric generic model; characteristic zero permits shrinking away its branch locus, and the tangent-space arguments below are unchanged.

Write q:𝒩→T for this smooth family of curves, and F:𝒩→P4 for evaluation. For a general t let N_t denote its smooth curve fiber and f:N_t→P4 its finite birational map onto D_t. Let g be its genus and d=deg D_t. Then g≤p_a(D_t), and deg f*O_P4(1)=d.

Each marked section p_i(t)=L_i∩H_t lifts uniquely near the general fiber to a section s_i of q: the marked points lie in the smooth locus of D_t, where normalization is an isomorphism. Consequently the 25 lifted points on N_t are distinct. This does not require simultaneous resolution of the singularities of D_t or smoothness of D_t away from these points.

## 2. Saturated normal bundle and its degree

The differential T_Nt→f*T_P4 is generically injective, because f is birational onto a curve in characteristic zero. Saturate its rank-one image in the rank-four vector bundle f*T_P4. On the smooth curve N_t the saturation is a line subbundle S and the quotient

N_f = f*T_P4 / S

is a rank-three vector bundle. There is an effective divisor R such that S≅T_Nt(R): the map from T_Nt to its saturation has a torsion cokernel of length deg R. Thus

deg det N_f = 5d + 2g − 2 − deg R ≤ 5d + 2p_a(D_t) − 2.       (1)

This sign is important: ramification decreases, rather than increases, the degree available for focal zeros. The construction uses the normal bundle of the normalization map modulo torsion, not the possibly defective normal sheaf of the singular embedded curve.

## 3. A globally regular characteristic map

Restrict the tangent sequence of the smooth morphism q to N_t:

0→T_Nt→T_𝒩|Nt→T_tT⊗O_Nt→0.

The differential dF followed by the quotient to N_f annihilates T_Nt. It therefore induces a globally regular bundle map

χ_t:T_tT⊗O_Nt→N_f.                                       (2)

No choice of a global splitting of the tangent sequence is required. Local splittings give the same map because their differences have image in T_Nt, killed by the quotient.

If F were dominant onto P4, characteristic-zero generic smoothness would make dF have rank four at a general point of 𝒩. The relative tangent has rank-one nonzero image there. Hence (2) would have generic rank three for general t. Conversely this rank implication alone suffices below; no claim about special fibers is needed.

## 4. Each fixed-line marked point is a double zero of every maximal minor

Fix a marked section s_i and a general base point t. The hyperplanes through the fixed ambient point p_i(t) form a codimension-one subspace of the hyperplane parameter space. Infinitesimally, the kernel of the map

T_tT→T_{p_i(t)}L_i

has dimension three: varying H while keeping its intersection with the fixed transverse line L_i stationary imposes one independent condition. Along these three parameter directions, d(F∘s_i)=0. Since ds_i lifts the corresponding base tangent directions, the definition of χ_t shows that its fiber at s_i(t) annihilates that three-dimensional subspace. Therefore

rank χ_t(s_i(t))≤1.                                     (3)

Choose any three of four constant basis vectors of T_tT. Their exterior product under χ_t is a global section of det N_f. At a point where the fiber matrix has rank at most one, every 3-by-3 minor vanishes to order at least two. Indeed over the discrete valuation ring of N_t at that point, constant invertible row operations make two of the three target rows divisible by a local parameter; each determinant is divisible by its square. The same conclusion follows after also changing source basis and holds for all maximal minors.

Thus all maximal-minor sections vanish along 2Σ_i s_i(t), a divisor of degree 50. If χ_t has generic rank three, some such section is nonzero, forcing

50 ≤ deg det N_f.                                      (4)

This is an intersection multiplicity statement on a smooth curve, so no singular-curve determinant correction or unproved Gorenstein identity enters it.

## 5. Numerical contradiction and exact boundary

For the ACM heptic, d=7 and p_a=5. Equations (1) and (4) would imply

50 ≤ deg det N_f ≤ 35+10−2 = 43,

which is impossible.

For an integral nondegenerate sextic in P3, the arithmetic Castelnuovo bound gives p_a≤4. Hence even without the stronger genus restrictions of the three-cubic branch,

50 ≤ deg det N_f ≤ 30+8−2 = 36,

again impossible. In particular the argument does not silently identify this sextic with the already excluded genus-three four-cubic sextic.

Therefore ambient dominance is impossible in both cases. The family image has dimension at most three. Its dimension is at least two: the original curve incidence has dimension five and ambient evaluation fibers lie in the three-dimensional space of hyperplanes through a point.

For the canonical marked-carrier family, dimension two is also impossible. If its image were an integral surface S, the closure of the original incidence family would equal the full point/hyperplane incidence of S: containment and equality of dimensions five force this, since the latter is integral. Its general hyperplane section would consequently have reduced support D_t and generic multiplicity one. Therefore deg S=d, either six or seven. The family is intrinsic and Heisenberg-equivariant, hence S would be invariant. The degree of an invariant integral surface is divisible by five, by the central-character Hilbert-polynomial argument given in HEPTIC-EXTRA-QUARTIC-NECESSITY.md. Neither six nor seven is divisible by five.

It follows that the canonical swept image is exactly an integral hypersurface W⊂P4. It contains C because each marked section L_i∩H_t sweeps a dense open of its fixed line L_i as H_t varies. It is invariant. Let e be its degree. The unique defining polynomial spans a one-dimensional representation of the linear Heisenberg group. Its center is the commutator subgroup, so every one-dimensional representation has trivial central action. The central weight of a degree-e polynomial is e modulo five (up to the harmless dual sign). Thus e is divisible by five. In particular e≥5, consistently with H0(I_C(4))=0.

This does not classify or exclude the invariant hypersurface W. Its general hyperplane section is a surface containing D_t, not equal to D_t. Rank-two characteristic maps for such a three-dimensional swept image are not addressed by the maximal-minor contradiction, and smoothness of W along C is not asserted.

## Inputs and reproducibility boundary

The geometric input is the canonical marked-carrier result THREE-CUBIC-SEXTIC-HEPTIC-DICHOTOMY.md, published at 435a20fc680c7ccecc3cbfd762a3d5ae97b76299. Its marked-point smoothness and heptic arithmetic genus are used explicitly. The classical arithmetic Castelnuovo bound for integral curves is stated in Section 2(v) of https://link.springer.com/article/10.1007/s12215-022-00788-x; for degree six in P3 it gives four. The normalization, saturation, tangent-sequence, and minor arguments above provide the new deduction.

No actual source coefficients, selected ranks, scans, local-model spike, consumed experiment, or external writes were used. This is not a complete exclusion of the remaining a=0,b=3 curve-base branch or of Q4.
