# Canonical global kernel and unique normal form for lower third-operator classes

## Result and inputs

Work in characteristic zero with the actual finite icosahedral action, retaining the physical Serre marking in the identification of the lower source. Put A=H0(O_L(2)), dim A=3, P=P4, dim P=4, and D=D5. Let X=P(A) parameterize lines of negative quadratics. The following are pinned inputs in Akilleez-QA/read-em-and-weep, PR543 at 6c724c3b74e2ae4d6992d8c7b99b41c0715d69c0, directory research/hm/order-four-quadratic-load/:

- [ACTUAL-NEGATIVE-INVOLUTION-SECTOR-AS-SQUARE-QUOTIENT.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/6c724c3b74e2ae4d6992d8c7b99b41c0715d69c0/research/hm/order-four-quadratic-load/ACTUAL-NEGATIVE-INVOLUTION-SECTOR-AS-SQUARE-QUOTIENT.md): the actual negative 21-space is epsilon H0(Q4(4)); after quotienting its canonical polynomial 9-space, actual multiplication by a is evaluation on a from P tensor A* to P. The original degree-eight source is 24-dimensional and first loses its actual scalar 3-space. We do not replace this 24-to-21 map by an arbitrary polynomial tangent lift.
- [POSITIVE-SECOND-BOCKSTEIN-UNIVERSAL-SYMBOLS.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/6c724c3b74e2ae4d6992d8c7b99b41c0715d69c0/research/hm/order-four-quadratic-load/POSITIVE-SECOND-BOCKSTEIN-UNIVERSAL-SYMBOLS.md) and [ACTUAL-SECOND-BOCKSTEIN-NONZERO-BY-ATIYAH-QUINTIC.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/6c724c3b74e2ae4d6992d8c7b99b41c0715d69c0/research/hm/order-four-quadratic-load/ACTUAL-SECOND-BOCKSTEIN-NONZERO-BY-ATIYAH-QUINTIC.md): the ACTUAL nonzero second symbol has a sheaf presentation

  0 -> A O_X(-2) --beta--> P O_X -> I_Z(6) -> 0,       (1)

where Z has length 24. This is the actual symbol, not a freely normalized substitute. The proof below works with its actual scalar.
- [THIRD-BOCKSTEIN-POLARIZATION-AND-SQUARE-DIRECTION-GATE.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/6c724c3b74e2ae4d6992d8c7b99b41c0715d69c0/research/hm/order-four-quadratic-load/THIRD-BOCKSTEIN-POLARIZATION-AND-SQUARE-DIRECTION-GATE.md): the two effective third channels are already known; their dimension is not claimed as a new result.
- [PR650 corrected extractor](https://github.com/Akilleez-QA/read-em-and-weep/blob/389d5488257348d7bd57ceb1b81cdb8f1b916ce8/research/hm/last-jet-double-cubic/PROOF.md): the positive boundary is the corrected quintic remainder, after subtraction of an actual reduced kernel lift. This compatibility is retained; no raw first-normal coefficient is substituted here.

The new result is the canonical equivariant splitting of the GLOBAL kernel after taking the second-symbol quotient, and the resulting unique polynomial normal form for all equivariant lower operator families with zero third class. Neither the actual lower family nor either surviving coefficient is evaluated.

## 1. The global rank-eleven kernel

Set E=P tensor A* tensor O_X. Universal evaluation is the surjection

 e:E -> P O_X(1),     e_a(T)=T(a).

Compose it with the twist of (1), and define F as its kernel:

 0 -> F -> E -> I_Z(7) -> 0.                         (2)

Pullback of (1)(1) along e gives

 0 -> P tensor Omega_X^1(1) -> F -> A O_X(-1) -> 0.   (3)

This is an exact sequence of vector bundles. In particular F is locally free of rank eleven, although its injection into E is NOT a subbundle along Z. This distinction matters: the quotient is the ideal sheaf I_Z(7), not a line bundle there. The construction retains the full nonreduced degeneration scheme.

There is an equivariant splitting of (3), and it is unique. Indeed

 Ext1_X(A O(-1),P tensor Omega^1(1))
 = Hom(A,P) tensor H1(Omega^1(2)) = 0.

The last equality follows from the Euler sequence, because multiplication A* tensor A* -> Sym2 A* is onto. Averaging a splitting gives an equivariant one. Differences of equivariant splittings form

 Hom_G(A,P tensor H0(Omega^1(2)))
 = Hom_G(A,P tensor Lambda2 A*) = 0,                 (4)

since Lambda2 A*=A and P tensor A=V+P+D, with V the other three-dimensional irreducible, not A. Thus

 F = (P tensor Omega_X^1(1)) direct-sum A O_X(-1)    (5)

canonically as an equivariant bundle over X equipped with the actual beta. Its Chern classes are c1(F)=-7H and c2(F)=25H2. This also checks (2): c2(I_Z(7))=24H2, so c2(F)=49-24=25.

## 2. The unique splitting has an explicit derivative formula

Regard beta(a,b) as quadratic in a and linear in its source b in A. Define

 L(a,b)(v) = (1/2) (d/du)|_(u=0) beta(a+uv,b).       (6)

The derivative holds b fixed; only afterwards may b=B(a,h) be substituted. It is not the total derivative of beta(a,B(a,h)). It is linear in a and b, and linear in the evaluation argument v. It therefore defines A O_X(-1)->E. Euler's identity gives L(a,b)(a)=beta(a,b). Hence (6) supplies a splitting in (3). It is equivariant because differentiating a polynomial map is natural, so (4) proves this is the unique equivariant splitting.

In the usual universal symbol convention beta(a,b)=c projection(a^2 b), this is simply L(a,b)(v)=c projection(avb), with the SAME actual nonzero scalar c. No scalar is selected or computed.

This makes the second-symbol-exact part of the lower twelve-dimensional class canonical, rather than choosing an arbitrary lift of the three-dimensional second-symbol image. It is valid across Z at the sheaf level. At a point where beta has rank r, the image F_x->E_x has dimension 8+r, not necessarily eleven; its failure of fiber injectivity is the Tor contribution from I_Z. Thus (5) must not be used to claim a rank-eleven pointwise kernel at the degeneracy scheme.

## 3. Unique normal form for every ineffective lower family

Consider any equivariant polynomial lower family R(a,h) in Hom(A,P), homogeneous of degree two in a and linear in h in D. It defines D O_X(-2)->E. Its third class is the composite into I_Z(7), equivalently an equivariant map D->H0(I_Z(9)).

This third class is identically zero if and only if there exist UNIQUE equivariant polynomials B and S such that

 R(a,h)(v) = L(a,B(a,h))(v) + S(a,h)(a,v),           (7)

where B(a,h) in A is linear in a and h, and S(a,h) in P tensor Lambda2 A* is also linear in a and h.

Proof: if the composite vanishes, R factors uniquely through F. The canonical splitting (5) gives a unique B and a unique contraction-invisible remainder R-LB. The latter is a section of P tensor Omega^1(3) for each h. The Koszul sequence on X gives

 0 -> Lambda3 A* tensor O_X
   -> Lambda2 A* tensor O_X(1)
   -> Omega_X^1(3) -> 0.                            (8)

Its global-section sequence is exact because H1(O_X)=0. Thus the remainder is S(a,h)(a,v), with S defined modulo a constant map D->P tensor Lambda3 A*. This ambiguity has no equivariant part: det A is trivial and Hom_G(D,P)=0. Exactness of finite-group invariants therefore gives existence and uniqueness of equivariant S. Conversely, evaluating (7) on v=a kills the skew term and gives beta(a,B(a,h)), which vanishes in the second-symbol quotient.

The formula asserts uniqueness only for an equivariant whole polynomial family. For an isolated a or an arbitrary nonequivariant family, skew gauges and degeneracy issues remain. It does not assert a preferred complement of F in E.

## 4. Exact scalar accounting, as a consequence rather than the theorem

For an explicit binary-form version of its one-dimensional B channel, identify A=Sym2 W and D=Sym4 W. Then B(a,h) is a scalar multiple of the second transvectant (a,h)_2 in Sym2 W. This is nonzero universally and spans the unique A constituent of A tensor D. Thus the second-symbol-exact lower family is precisely a scalar multiple of L(a,(a,h)_2). Its scalar remains free; this observation does not evaluate an actual operator.

The normal form decomposes the ineffective coefficient space intrinsically. The actual lower-family space has six equivariant channels:

 dim Hom_G(D,P tensor A* tensor Sym2 A*) = 6.

The contraction-invisible summand has dimension three, since H0(Omega^1(3))=A+D, and D occurs once in P tensor A and twice in P tensor D. The second-symbol-exact summand has dimension one, since Hom_G(D,A tensor A*) has dimension one. Hence precisely four of the six lower coefficients are ineffective, with the two remaining coefficients mapping to the previously known two third gates.

There is no missing cokernel in this count: (5) gives H1(F(2))=0, using H1(Omega^1(3))=H1(O(1))=0. Therefore (2)(2) is surjective on global sections and then on equivariant Hom from D. This proves an exact sequence of actual polynomial coefficient spaces, not only an equality of characters.

## Contribution and boundary

The new construction supplies a canonical, explicit second-symbol lift (6), proves the global kernel bundle splits uniquely equivariantly, and gives the unique no-obstruction normal form (7), including the three Koszul-invisible channels and the one actual second-symbol channel. It reduces a future corrected lower-class computation to testing membership in this precise four-dimensional subspace. It does not compute that class, prove that it belongs or does not belong, or eliminate either of the two effective third channels. Null's corrected harmonic-operator/frame calculation remains untouched. No selected actual HM coefficients, source instances, pointwise matrices/ranks, scans, or large computations enter this derivation.

## Verification status

This is a mathematical derivation from the pinned source interfaces, independently reviewed at that level, not a proof-assistant certificate or an independent reconstruction of the complete HM foundation.
