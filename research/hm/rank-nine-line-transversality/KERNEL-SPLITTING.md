# Independent audit: kernel on the 25 rank-nine lines

Verdict: the proposed kernel splitting and the rank-at-most-two intrinsic normal derivative are valid, with the representation identification supplied below. The splitting into two O(-4)'s is an ordinary bundle splitting, not a claim that their multiplicity representation is trivial. Exact derivative rank two is a separate additional assertion, not proved by this audit.

## Inputs and scope

Work over C. Use PR562 at 86b643fe2adecbd321d1c8f98be84fe2082bcd10: each of the 25 lines L=P(R) has evaluation rank nine everywhere, constant annihilator line Ck, and one may choose its stabilizing complement I=SL2(F5). Its beta net is Lambda²B*, where A=B direct-sum R, with central eigenvalues +1 on B (dimension 3) and -1 on R (dimension 2). The invariant k has tensor rank two. All representations used here are self-dual. The central signs follow from the reflection multiplicities and det(A)=1, forced by perfectness of I: the negative of the reflection would have determinant -1.

Use the full-normalizer identities in PRIMARY-INJECTION-AND-FAILURE.md at 7bf725bcd857a2deb975f9ecb80fca32e7833ae0, freshly fetched for this audit:

S2=A tensor U', M2=V tensor W', Lambda²A=V tensor W', Sym²A=V tensor U,

where U'=Sym²W', and U is the other even irreducible of dimension three. These derive from HM1973 Lemma 3.3 and equations (4.4),(4.11). The standard binary icosahedral character identities used below are recorded in its appendix. No selected actual coefficient, matrix, rank sample, or source evaluation is used.

## 1. Resolve the representation types without guessing

The beta net is I-isomorphic to sl(W')=U'. Since I is perfect, det B is trivial, so Lambda²B* is isomorphic to B. Thus B=U'.

The even part of Lambda²A has dimension four. Since W' is odd, Lambda²A=V tensor W' implies dim V_odd=2. The invariant rank-two tensor k in V* tensor W'^* induces an equivariant injection W' -> V*, so V_odd=W'. Now take odd parts in Sym²A=V tensor U:

B tensor R = W' tensor U = R6.

This is the irreducible six-dimensional odd representation. In contrast U' tensor W'=W' direct-sum Q4. Consequently R is the other odd two-dimensional representation, denoted W0, and Sym²R=U. In particular U and B are inequivalent. This deduction fixes the potentially dangerous Galois convention.

## 2. Restrict the evaluation bundle with its linearization

Let Q be the tautological quotient on P(A), so evaluation is

e: E=U' tensor Q(-1) -> M2 tensor O.

On L=P(R), the equivariant decomposition A=B direct-sum R gives

Q|L = B tensor O direct-sum (R tensor O/O(-1)).

The second summand is det(R) tensor O(1)=O(1), because I is perfect. Therefore

E|L = U' tensor O direct-sum (B tensor U') tensor O(-1).

The central involution acts +1 on the first summand and -1 on the second. It acts on M2=Lambda²A with even part Lambda²B direct-sum Lambda²R=U' direct-sum 1, and odd part B tensor R=R6. The cokernel of e|L is the constant trivial line O: its dual is Ck tensor O, and an I-stable one-dimensional representation is trivial by perfectness.

Since rank e is nine at every point, its even block is an isomorphism U' O -> U' O, and its odd block is a surjection

(B tensor U') O(-1) -> R6 O.

As B tensor U'=U' tensor U'=1 direct-sum U' direct-sum J5, the trivial-coefficient summand O(-1) maps to zero: a degree-one equivariant map would require Hom_I(R,R6), which vanishes. Hence

K=ker(e|L)=O(-1) direct-sum K2,

where K2 is the kernel in the exact sequence

0 -> K2 -> (U' direct-sum J5) O(-1) -> R6 O -> 0.

In particular rank K2=2 and deg K2=-8.

## 3. Force the balanced splitting

Both source representation channels U' and J5 are nonzero in the surjection: otherwise its rank is at most five or three, respectively. After twisting by O(1), the map on global sections is an equivariant map

U' direct-sum J5 -> R6 tensor R*.

Its restriction to each irreducible source summand is nonzero, hence injective; the two images cannot intersect because the summands are inequivalent. Thus H0(K2(1))=0.

Write K2=O(-a) direct-sum O(-b), a<=b, a+b=8. The vanishing gives a>=2. If unbalanced, a<b, so a is 2 or 3. Its unique maximal-degree line subbundle O(-a) is I-invariant. Its linearization differs from the standard one only by a character, and I has no nontrivial characters.

The central involution acts as -1 on all of (U' direct-sum J5)O(-1), hence on K2. On standard O(-a), it acts as (-1)^a. Thus a must be odd, ruling out a=2. For a=3, an equivariant inclusion O(-3) -> (U' direct-sum J5)O(-1) is an invariant section of (U' direct-sum J5)O(2). But H0(O(2))=Sym²R*=U, and Hom_I(U,U' direct-sum J5)=0. This rules out a=3.

Therefore, as ordinary bundles,

K = O(-1) direct-sum O(-4) direct-sum O(-4).

The proof neither assumes nor asserts a trivial coefficient representation on the balanced pair.

## 4. Intrinsic normal derivative

Because e has constant rank along L, its intrinsic derivative descends to

N_{L/P(A)} -> Hom(K,coker e)=K*.

Equivalently, dualizing gives an I-equivariant morphism

K -> N*_{L/P(A)}=B* tensor O(-1).

The restriction from the distinguished trivial-coefficient O(-1) is zero, since such a morphism is an element of B* fixed by I. There are no such elements. Consequently the intrinsic normal derivative has rank at most two at every point of every one of the 25 lines.

This upper bound alone does not prove exact rank two, reducedness, smoothness, normality, algebraicity, or any lifting claim.

## Conditional consequence if exact rank two is independently established

If the normal derivative has rank two everywhere, its restriction K2 -> B*O(-1) is a subbundle injection and its quotient is O(5), by degrees. Its dual exact sequence is

0 -> O(-5) -> B O(1) -> K2* -> 0.

Thus the kernel of the normal derivative is O(-5). This is conditional on exact rank, not a substitute for proving it.
