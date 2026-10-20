# Inversion eigenspaces in the full-deck obstruction target

## Theorem and precise scope

Over C (and by base change over Q(i)), use the stipulated HM carrier, its audited exact presentation, the audited inversion projective lift, the independent classical-cohomology proof of the invariant Ext row, and the injective full coefficient-family Kodaira–Spencer theorem. Let a be simultaneous elliptic inversion (x,y) ↦ (1/x, i y/x²). Its canonical action on End E commutes with geometric S4 factor permutations and preserves full deck character. On

V = Ext²_X(E,E)_{full-deck}

it is an involution. The following are abstract representation-theoretic conclusions:

* dim V = 352 and its a eigenspaces have dimensions (176,176).
* The S4 type [22] has multiplicity space M of dimension 30; a on M has eigenspace dimensions (12,18).
* For D8 stabilizing {{1,2},{3,4}} and epsilon((12))=epsilon((34))=−1, epsilon((13)(24))=+1, the retained space ker(e_sgn:V_epsilon→V_sgn) is one epsilon line in [22] tensored with M. Its a eigenspaces therefore have dimensions (12,18), not (24,36).
* The 2-dimensional S4-sign block is wholly a-negative. The whole 32-dimensional epsilon space has eigenspaces (12,20).

No assertion of invariance or vanishing of the actual obstruction class is used or proved here. Such invariance, if separately established with its actual-source premises, restricts the retained class to the 12-dimensional positive eigenspace. It does not prove that class is zero.

## 1. Global action and linearization choices

The audited [projective lift](../foundation-p02/INVERSION-LIFT.md) constructs a coherent order-four action on P(E); conjugation gives a coherent action on End E. Its square is simultaneous deck inversion d_all. Thus on the full deck character its square is (−1)^4=1; on the invariant deck character its square is also 1. The scalar line twist a*E≅E⊗Q causes no additional End character.

On Y=(P¹)^4, write j for simultaneous coordinate interchange and J=[[0,1],[1,0]] for its standard lift on each O(1) section space. Let L=O(1,1,1,1) with its ordinary external-tensor and permutation linearizations. Under the symmetric quotient σ:Y→P⁴, j induces reversal R of the five coordinates. The binary-quartic coefficient convention identifies σ*O(1)=L equivariantly for these particular lifts, with no extra scalar. R²=J²=1.

Pull the four-term HM presentation to Y. Its terms in degrees −1,0,1,2 are C_t⊗L^t, of dimensions (5,15,10,2). The [monomial full-chain theorem](../foundation-p02/MONOMIAL.md), §§3–4, supplies their involution matrices

P_pi, M_pi, −I₂⊗P_pi, −I₂,     pi(i)=4−i in F5.

These matrices square to one. Their traces are (1,3,−2,−2): pi has one fixed index, M_pi consists of three copies of its permutation, and the last two traces follow from their displayed tensor products. S4 acts trivially on these coefficient spaces. Choosing the inverse chain-map convention changes none of these involutions or characters. Scalar changes to a chain lift cancel on End.

## 2. Equivariant Euler character on Y

Put U^r=⊕_t Hom(C_t,C_{t+r}), so the internal degree-r Hom term is U^r⊗L^r. Since the coefficient actions are involutions, traces multiply in Hom. Direct finite sums of the four symbolic block traces give

tr(a|U^0)=1²+3²+(−2)²+(−2)²=18,
tr(a|U^1)=1·3+3·(−2)+(−2)·(−2)=1,
tr(a|U^2)=1·(−2)+3·(−2)=−8,
tr(a|U^3)=1·(−2)=−2.

The negative degrees have the same traces. These are abstract character identities, not ranks or evaluated source matrices.

For a permutation s with cycle lengths l, define

w(s)=∏_l tr(J^l),
v₂(s)=∏_l tr((Sym²J)^l),
w₃(s)=∏_l tr((Sym³J)^l).

The tensor-permutation trace identity identifies these with traces of js on H⁰(L), H⁰(L²), H⁰(L³). For L^{-1} all cohomology vanishes. For L^{-2} and L^{-3}, only H⁴ is nonzero. Each P¹ H¹ contributes an odd cohomological degree, so permutations contribute the Koszul sign sgn(s). On each factor the equivariant canonical line is O(−2) tensored by det(J), and det(J)=−1. Four such determinant factors multiply to +1. Consequently the traces on H⁴(L^{-2}) and H⁴(L^{-3}) are respectively sgn(s) and sgn(s)w(s). This includes both the determinant linearization and the Künneth permutation sign.

Euler additivity for the bounded equivariant Hom complex therefore gives

χ(js, σ*End H)
 = 18 − w(s) − 8v₂(s) + 2w₃(s) − 8sgn(s) + 2sgn(s)w(s).       (1)

There is no fixed-point formula, localization, or evaluation on geometric points in this argument.

## 3. Recovering the invariant Ext² character

Write T^j=H^j(Y,σ*End H), the deck-invariant Ext groups. The [independent cohomology proof](../foundation-p01/INVARIANT-COHOMOLOGY.md) gives dimensions (1,79,352,0,0). Simplicity implies T⁰ is the scalar identity with trivial action.

The [full coefficient family](../foundation-p01/COEFFICIENT-FAMILY.md) has injective KS map from the 79-dimensional tangent of U⊂P(W⁵), W=H⁰(Y,L), into T¹. It lands in T¹ because the family is pulled back from Y; equality of dimensions makes it an isomorphism. Equivariance follows by functoriality of KS: on tuples, the action fixing the original tuple is s↦R(j* s), and factor permutations act by pullback only. The base tuple v is fixed as a vector, because j*v=Rv and R²=1. Thus the projective tangent is the representation W⊗k⁵ modulo the fixed line kv, with inversion acting by J^{⊗4}⊗R. Since tr(R)=1 and S4 acts trivially on k⁵,

tr(as|T¹)=w(s)−1.

One can make the same argument for the family on Y before pulling to X, avoiding any choice of the twisting line N. The pullback invariant identification is canonical and preserves KS.

Combining this with (1), T³=T⁴=0, and tr(T⁰)=1 yields

tr(as|T²)=16 − 8v₂(s) + 2w₃(s) − 8sgn(s) + 2sgn(s)w(s).       (2)

For classes (1⁴, 21², 2², 31, 4), the elementary symmetric-power trace rule gives

w   = (0,0,4,0,2),
v₂  = (1,3,9,1,3),
w₃  = (0,0,16,0,4).

Indeed J has eigenvalues +1,−1; Sym²J has trace 1 at odd powers and dimension 3 at even powers, while Sym³J has trace 0 at odd powers and dimension 4 at even powers. These abstract class-character values in (2) give

tr(as|T²)=(0,0,−24,0,4).                               (3)

## 4. Equivariant Serre duality and the full-deck sign

The trace pairing makes End E self-dual. The holomorphic form dx/y on C pulls back under a to i dx/y: this follows formally from d(1/x)/(i y/x²)=i dx/y. Its fourth external wedge therefore has a-eigenvalue i⁴=1, geometric permutation eigenvalue sgn(s), and deck character full-deck. Equivariant Serre duality on X consequently pairs T² perfectly with V, with value character trivial on a and equal to sgn on S4. Thus V≅(T²)^*⊗sgn as an a×S4 representation. Inverting a does not alter its action on these two sectors since a²=1 there; inverse permutations have the same cycle types. Hence

tr(as|V)=(0,0,−24,0,−4).                               (4)

This is also why one must not insert a permutation sign into the ordinary full-deck function eigensheaf itself. That eigensheaf is L^{-2} with ordinary permutation linearization; the sign in (4) comes from canonical volume and Serre duality.

At s=1, (4) is zero. Since dim V=352 by duality, its plus and minus dimensions are both 176.

## 5. Multiplicity extraction and the retained 30-dimensional target

Let M=Hom_S4([22],V). The [retained-sector decomposition](RETAINED-SECTOR.md), with the independent classical cohomology dimensions above and Serre duality on P⁴, gives dim M=20+10=30. The S4-sign multiplicity is 2. These dimensions use no historical rank certificate.

For the five classes in the established order, sizes are (1,6,3,8,6) and the [22] character is (2,0,2,−1,0). Since a commutes with S4, character orthogonality extracts its trace on M:

tr(a|M) = (1/24)∑_classes |class| χ_\[22\](s) tr(as|V)
         = (1/24)(3·2·(−24)) = −6.

Thus dim M_+=(30−6)/2=12 and dim M_-=(30+6)/2=18. The entire [22]-isotypic component has dimensions (24,36), since [22] itself is two-dimensional; it must not be confused with its multiplicity space.

For the sign multiplicity the same extraction gives

tr(a|V_sgn)=(−72+24)/24=−2.

As dim V_sgn=2, this block is wholly negative.

The stabilizer D8 and character epsilon=sgn|D8 satisfy Ind_D8^S4 epsilon=sgn⊕[22], by the three-pairing permutation representation. Frobenius reciprocity says [22] contains exactly one epsilon line and no other S4 types except sign have an epsilon line. Therefore

V_epsilon = V_sgn ⊕ ([22]_epsilon⊗M),
ker(e_sgn|V_epsilon) = [22]_epsilon⊗M.

Both splittings here are canonical isotypic statements, and a acts trivially on the [22] factor after identifying the isotypic representation as [22]⊗M; all its information lies in M. Thus the retained kernel inherits exactly the (12,18) eigenspace dimensions. The whole epsilon space has (12,20).

