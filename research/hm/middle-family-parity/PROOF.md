# Relative middle obstruction and forced parity at the exceptional orbit

## Inputs and conventions

Work over C. Let S=Sym(T), dim(T)=5, W=W' be the two-dimensional generator representation of H, and P=P(W). Identify P with the column parameter line P(W*) using the invariant determinant form. A parameter line Cw has annihilator column lambda. Write O(d) for parameter twists, not S-grading shifts.

The exact inputs are:

- [PR518, commit b17c7cac111568f9b45876a2ad8fae4e46578841](https://github.com/Akilleez-QA/read-em-and-weep/blob/b17c7cac111568f9b45876a2ad8fae4e46578841/research/hm/middle-obstruction-symmetry/PROOF.md): the middle obstruction is symmetric under the pairing-induced identification; its nontrivial Heisenberg characters occur in twelve inverse pairs, each of dimension one, and its trivial-character space has dimension two.
- [PR519, commit cf328c6b0d05551a52911a3a4ba420c68f6fcc6f](https://github.com/Akilleez-QA/read-em-and-weep/blob/cf328c6b0d05551a52911a3a4ba420c68f6fcc6f/research/hm/gorenstein-flat-family/PROOF.md): the actual cyclic image M in H tensor O and its orthogonal B=M^perp are bundles in every graded degree, with B contained in M; their quotient is the Gorenstein algebra family twisted by O(-1).
- [PR512, commit 26811b53c198879d0c55a2fb9ba75187bee38d9c](https://github.com/Akilleez-QA/read-em-and-weep/blob/26811b53c198879d0c55a2fb9ba75187bee38d9c/research/hm/column-family-intersections/PROOF.md): the column algebra family A has graded pieces O, T tensor O, E tensor O(2), and zero in higher degrees.
- [PR513, commit df947c1ce092c0c59dcef187639147da8a7b2873](https://github.com/Akilleez-QA/read-em-and-weep/blob/df947c1ce092c0c59dcef187639147da8a7b2873/research/hm/column-level-resolution/PROOF.md): Tor4(A_lambda)_5=0 for every lambda, and the degree-five preceding Koszul kernel is precisely its scalar boundary.
- [PR516, commit 89b66cbede7513c4f196fdbda0ee3bb77c53d2e0](https://github.com/Akilleez-QA/read-em-and-weep/blob/89b66cbede7513c4f196fdbda0ee3bb77c53d2e0/research/hm/gorenstein-resolution/PROOF.md): the middle Betti number b is the common kernel/cokernel dimension of the actual 26-dimensional obstruction map.
- [PR499, commit 1112189481554b0353c64178e3adc0dede2c3fbe](https://github.com/Akilleez-QA/read-em-and-weep/blob/1112189481554b0353c64178e3adc0dede2c3fbe/research/hm/middle-euler-ghost-exclusion/PROOF.md): K(H)_5 is acyclic.
- [PR520, commit c56173aab6e9e5d7be2f2f638d6f953c9d7f93b1](https://github.com/Akilleez-QA/read-em-and-weep/blob/c56173aab6e9e5d7be2f2f638d6f953c9d7f93b1/research/hm/quartic-jump-divisors/PROOF.md): every nonempty invariant divisor on P has degree at least twelve; the unique invariant divisor of degree twelve is the reduced orbit Omega.

Use the actual finite normalizer action, with Heisenberg subgroup Gamma, and quotient G=SL2(F5). The representation source is [Horrocks--Mumford (1973), Section 3.3 and appendix](https://www.dam.brown.edu/people/mumford/alg_geom/papers/1973a--Rk2BdleP%5E4-NC.pdf). In particular Lambda3(T)=A_rep tensor W0, E=A_rep*, and Sym3(W') is the irreducible four-dimensional Qspin, so it contains no W0. The group G is perfect and has no nontrivial characters. The trace/Serre pairing used in PR518 has its original compatible normalizer linearization; det(T) is trivial.

## 1. Relative middle Tor bundle of the column family

The internal-degree-five Koszul segment for the column algebra is

Lambda5(T) tensor O -> T tensor Lambda4(T) tensor O -> E tensor Lambda3(T) tensor O(2) -> 0.

The first map identifies the scalar line inside End(T). The second has kernel exactly this line in every fiber, by PR513. Quotienting that line therefore gives an everywhere injective bundle map and a locally free cokernel F of rank26:

0 -> End_0(T) tensor O -> E tensor Lambda3(T) tensor O(2) -> F -> 0.

Formation of F commutes with fibers, and F_lambda=Tor3(A_lambda)_5. Decompose by Gamma/Z characters; this is exact because Gamma is finite in characteristic zero and acts trivially on the parameter line.

For every nontrivial character chi, the corresponding sequence is

0 -> O -> 2O(2) -> F_chi -> 0.

Its fiberwise injectivity implies F_chi is a line bundle. Determinants give F_chi=O(4) as an ordinary line bundle. For the trivial character, End_0(T) has no invariant part, whereas

(E tensor Lambda3(T))^Gamma = (E tensor A_rep)^Gamma tensor W0 = W0.

Consequently the trivial part is canonically F_1=W0 tensor O(2). Thus the ordinary splitting of F is 24O(4) plus 2O(2), with the indicated canonical trivial-character representation.

## 2. The actual obstruction twists

The actual quotient C=(H tensor O)/M is A tensor O(1), not A itself. Its degree-zero quotient is W tensor O -> O(1), the tautological column evaluation, and the induced multiplication gives the claimed identification in all degrees. The pairing identifies B=M^perp with the relative reversed graded dual D5(C).

Hence Tor3(C)_5=F tensor O(1). Relative Koszul duality gives

V := Tor2(B)_5 = (F tensor O(1))*.

In particular V_chi is an ordinary O(-5) for every nontrivial character chi, and

V_1=W0* tensor O(-3)=W0 tensor O(-3).

The acyclic constant complex K(H)_5 supplies the connecting isomorphism Tor3(C)_5 -> Tor2(M)_5. Composing its inverse with the inclusion B -> M constructs the relative morphism Q:V -> V*. It commutes with restriction to fibers. All relevant relative Tor bundles here have constant ranks, as shown above and by duality. The chain-level proof of PR518 works over the parameter structure sheaf, so Q is symmetric.

The actual coisotropic quotient M/B is the Gorenstein family twisted by O(-1). This parameter twist changes neither numerical fiber ranks nor the middle Betti number b(w). Thus b(w)=corank(Q_w).

The nontrivial inverse-character blocks are symmetric off-diagonal blocks, with a scalar entry that is a section of an ordinary O(10). There are twelve such entries. The trivial-character block is a symmetric equivariant morphism

Q_1: W0 tensor O(-3) -> W0* tensor O(3).

Its determinant is an invariant section of O(12). Coefficient determinants introduce no character twist because G is perfect.

## 3. The trivial block has only two possible rank patterns

Either Q_1 is zero, or its determinant is nonzero. We prove that a nonzero block cannot have generic rank one.

Suppose Q_1 is nonzero of generic rank one. Its entries are sections of O(6). Their common vanishing divisor is invariant and has degree at most six, so is empty. Thus Q_1 has rank one at every point. Let I be its image and K its kernel; these are line bundles and the image is saturated. Write I=O(d). Since V_1 has degree -6, K has degree -6-d.

Symmetry identifies the image with the annihilator of the kernel inside V_1*. Indeed inclusion into that annihilator follows from symmetry, and both are saturated rank-one subbundles with identical fibers. The annihilator has degree -d, because it is dual to V_1/K=I. Therefore d=-d and d=0.

The equivariant inclusion I=O into W0* tensor O(3) would require a nonzero invariant in W0* tensor Sym3(W'). Any equivariant linearization of O differs from its standard one by a character; there is no such nontrivial character of G. Since Sym3(W')=Qspin is irreducible of dimension four, it contains no W0. This is a contradiction.

It follows that a nonzero Q_1 has generic rank two. Its determinant is a nonzero invariant of degree twelve, hence has exactly the reduced divisor Omega. At each point of Omega the determinant has order one, so Smith form gives corank exactly one. Everywhere else Q_1 is invertible.

Thus precisely one of these two alternatives holds:

1. Q_1 is zero, and its radical has dimension two at every point.
2. Q_1 is generically invertible, with radical dimension one exactly on Omega and zero elsewhere.

No claim is made that either alternative is the actual one.

## 4. Consequences for the middle Betti number

The nontrivial-character radical has even dimension, by the inverse-pair symmetry from PR518. The preceding dichotomy therefore proves:

- b(w) is even at every point outside Omega.
- b(w)>=1 at every point of Omega, in either alternative.
- If Q_1 is nonzero, b(w) is odd at every point of Omega.
- If Q_1 is zero, b(w) is even everywhere and b(w)>=2 everywhere.

In particular the middle ghost cannot vanish on the entire parameter line. At the twelve parameters where [PR524, commit bde039960aafbf3ac8be7921eb48ca4800fbb1fd](https://github.com/Akilleez-QA/read-em-and-weep/blob/bde039960aafbf3ac8be7921eb48ca4800fbb1fd/research/hm/quartic-klein-reduction/PROOF.md) proves that five quartic generators occur, at least one middle ghost must occur as well. This implication does not require proving Q_1 nonzero or evaluating any parameter.

The normalizer quotient acts transitively on the twenty-four nontrivial characters of Gamma/Z and therefore on their twelve inverse pairs. It transports the corresponding scalar sections. Consequently either all twelve scalar sections vanish identically, or none does. In the latter case each has only finitely many zeros, so all are nonzero simultaneously on a nonempty open subset. The generic radical dimension contributed by nontrivial characters is therefore either zero or twenty-four, not an arbitrary even number. Combining with the trivial-block dichotomy gives the further restriction

b_generic is in {0,2,24,26}.

This is a restriction on the generic value; it does not eliminate any of these four alternatives or bound every exceptional value by two. The argument uses transitivity of the actual character action, not an assumption that the twelve sections are identical.

There is also a precise degree statement for the full determinant. The degree of V is 24(-5)+2(-3)=-126, so det(Q) is a section of O(252). If it is nonzero, its vanishing divisor has degree252, with factorization into the degree-twelve trivial determinant and the squares of twelve degree-ten pair sections. This is a conditional discriminant degree, not a claim that the full determinant is nonzero or that its zeros are reduced.

## Scope

This is authored structural mathematics requiring independent review, conditional on the pinned inputs. It uses no selected HM/source evaluation, numerical rank computation, coefficient search or large computation. It does not determine the actual generic middle rank, all paired scalar zeros, the original fixed-pair residual, higher-order lifting or algebraicity. It is not formally checked by a proof assistant.
