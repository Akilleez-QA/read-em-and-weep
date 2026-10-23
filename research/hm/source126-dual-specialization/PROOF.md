# The three degree-twenty-eight residual templates have only two quotient types

## Statement and boundary

For the remaining source E10 of G3.11.8ae96830fd21 (original source126), the four historical dual quotient candidates with indices 129,157,231,249 reduce to exactly two possible splitting types:

- Residual Types I and II: Q*=O(-28)+O(-6)+Wp O(-1)+(P+D) O(-2), index129.
- Residual Type III: Q*=O(-28)+O(-6)+(Wp+T) O(-1)+V O(-4), index157.

Thus pairs (10,231) and (10,249) cannot occur under the actual template hypotheses. This removes two formal pairings, not a stable label. PR869 supplies nonempty abstract residual-template families; this theorem does not rule those templates out or assert realization by the fixed HM tensors. All statements are over C.

## Immutable inputs

All paths are in Akilleez-QA/read-em-and-weep. INPUTS.json records the four proof pins and hashes, with verbatim copies in inputs/.

- PR856, cee45480686c39a321feaa77d4b669682cc71efe, research/hm/profile11-degree28-constant-separation/PROOF.md: genuine constant separation H=C+Hbar, E=F+R, C/F=O(28), Hbar=A+V+P+D, R=O(-8)+W O(-9).
- PR858, d3b3134e23d0aa4c4b58fd1457f040856d2d0655, research/hm/profile11-degree28-residual-templates/PROOF.md: the three exhaustive saturated templates below, including their universal existence.
- PR862, e103e25456897a1123f9636eb20080e8641ce66a, research/hm/profile11-degree28-pencil-algebra/PROOF.md: canonical intrinsic residual line/tail and fixed-variable reconstruction boundary.
- PR869, e7ac74f7e92c3c59d4a3c13fa0388fcff8722f47, research/hm/profile11-degree28-open-family/PROOF.md: a nonempty family for each template, with required formal source, Gauss profile and reconstructed negative-pencil characters. No fixed HM realization is proved there.
- Original quotient catalogue: db51525015bb7c5e825833d550d08dedf6f6ea96, research/hm/order-four-quadratic-load/unrestricted-dual-splittings-and-pairs.json, Git blob e411417c9a61677df55e07f0aff15fbea4c9ec69. The four starting candidates are the currently retained source126 list; this proof filters that list, not a new completeness proof of the original catalogue.

Write X=O(-8), Y=W O(-9), R=X direct-sum Y and Q_R=Hbar O/R. The actual constant separation implies Q=O(28) direct-sum Q_R, not merely equality of characters.

Let U_j^d=Sym^j W O(j-d) inside Sym^d W O be the complete osculating bundle. PR858 supplies:

I: X=projection_P(U_0^8); Y=U_1^10 in (A+V+D)O.
II: X=U_0^8 in (P+D)O; Y=U_1^10 in (A+V+D)O, with the same D shared.
III: X=U_0^8 in (P+D)O; Y=projection_(A+V)(U_1^10).

In each case R and all projected bundles used here are saturated. We use P=W tensor Wp, Sym7 W=Wp+T, Sym8 W=P+D, Sym10 W=A+V+D. All named irreducibles are self-dual.

## 1. The quotient of the projected degree-eight line

The nonzero P-valued degree-eight covariant r8 has the universal factorization r8(w)=w tensor a7(w), proved by the Euler contraction in PR856 Section5. Here a7 is a nowhere-zero Wp-valued degree-seven covariant: its common divisor would be invariant of degree at most7, whereas the minimum nonempty invariant orbit has degree12. No value of w is selected.

Consequently X_P=projection_P(X) is a saturated subline of Wp O(-1) inside P O. The tensor-Wp Euler sequence and determinant give

0 -> Wp O(-1) -> P O -> Wp O(1) -> 0,
0 -> X_P=O(-8) -> Wp O(-1) -> O(6) -> 0.

The last quotient has trivial character because G has no nontrivial one-dimensional characters. Taking the quotient of the first sequence by X_P gives

0 -> O(6) -> Q_P=P O/X_P -> Wp O(1) -> 0.

Ext^1(Wp O(1),O(6))=Wp* tensor H1(O(5))=0. Thus Q_P=O(6)+Wp O(1), equivariantly. Averaging a splitting over finite G makes it equivariant. This is a bundle splitting; no constant or horizontal splitting of P O is inferred.

## 2. Types I and II have the same quotient

The standard complete osculating quotient is

Sym^d W O/U_j^d = Sym^(d-j-1) W O(j+1).

It follows either by the universal apolar annihilator, or by dualizing its fiberwise identification with Sym^(d-j-1) W O(-j-1). Hence (A+V+D)O/Y=(P+D)O(2)=:B.

Type I has disjoint constant summands, so Q_R=Q_P+B directly.

For Type II, first divide Hbar O=P O+(A+V+D)O by Y. This gives P O+B. The projection of X to P O is the saturated X_P and is an isomorphism X→X_P. Quotienting its graph therefore gives the actual exact bundle sequence

0 -> B -> Q_R -> Q_P -> 0.

This step retains the shared-D graph and does not assume it removable by a constant shear. Its equivariant extension group vanishes:

Ext^1_G(Wp O(1), B)=0 by H1(O(1))=0;
Ext^1_G(O(6), B)=((P+D) tensor H1(O(-4)))^G
                         =Hom_G(A,P+D)=0.

Serre duality identifies H1(O(-4)) with Sym2 W=A; its self-duality removes convention ambiguity. Finite-group invariants are exact in characteristic zero, so invariant Ext computes equivariant extensions here. Thus the actual graph extension splits as an equivariant bundle and Q_R=B+Q_P also in Type II. This yields index129 in both cases.

## 3. A first-polar system has no linear annihilator

Lemma. Let f:O(-d)→V O be a homogeneous vector polynomial of degree d>0 whose coefficients span V. If the first-polar image Y_f is a subbundle, then H0((V O/Y_f)*(1))=0.

Proof. A section is a homogeneous linear covector ell(w) with ell(w)∂_u f(w)=ell(w)∂_v f(w)=0 as polynomial identities. Euler's identity yields d ell(w)f(w)=0. Differentiate this last equality in u and v and subtract the previous identities. Then (∂_u ell)f=(∂_v ell)f=0. The two covectors ∂_u ell,∂_v ell are constant; full coefficient span forces both zero. Homogeneity of ell then forces ell=0. The proof is basis-independent despite using formal coordinate symbols, and evaluates no point or derivative value.

## 4. Type III selects index157

Here the two constant summands (P+D) and (A+V) are disjoint. The complete degree-eight line quotient is Sym7 W O(1)=(Wp+T)O(1). Set Z=(A+V)O/Y. The projected degree-ten line spans A+V, and its first polar is exactly Y by PR858; the lemma gives H0(Z*(1))=0. Hence

H0(Q*(1))=Wp+T.

The O(-28) block contributes nothing. Among the four starting candidates, the degree-minus-one characters are respectively

129: Wp; 157: Wp+T; 231: 2Wp; 249: 2Wp+T.

Only157 has the required character. This proves the stated full Type III splitting conditional on the exhaustive retained candidate list. In particular it does not infer the V O(-4)+O(-6) splitting merely from rank and degree.

Combining Sections2 and4 leaves exactly129 and157 as formal splitting possibilities. PR869 constructs all three residual templates with a balanced degree28 block. The present theorem does not contradict their abstract nonemptiness. Its Type III full-profile conclusion is conditional on the retained actual quotient catalogue; no transfer of that catalogue completeness to every abstract family member is asserted here. Neither remaining actual pairing is excluded, and no actual-HM realization is proved.

## Verification scope

The verifier checks immutable input bytes, catalogue profiles, rank/degree consistency, the two exact filters and their disjoint removed indices. It checks the formal differentiated Euler implication coefficientwise for universal polynomials in a bounded degree range. It does not establish the geometric inputs by computation and performs no actual-HM coefficient, parameter, point, matrix, derivative-value or rank evaluation.
