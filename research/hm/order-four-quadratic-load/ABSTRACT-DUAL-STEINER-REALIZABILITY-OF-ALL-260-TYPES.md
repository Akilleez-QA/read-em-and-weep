# Abstract equivariant Steiner realizability of all 260 dual types

## Result and essential boundary

Every one of the 260 negative equivariant splitting types classified in
`UNRESTRICTED-DUAL-SPLITTINGS-AND-SAME-SOURCE-PAIR-CONSTRAINTS.md` occurs as the
kernel of **some abstract equivariant bundle surjection**

    M3 tensor O(-1) -> M2 tensor O,

where M3=3W'+3S4+6T6 and M2=A+2V+3P4+4D5. This is an abstract Steiner
presentation existence theorem, not realization by the fixed HM multiplication
map. It does not realize any A/B quotient, simultaneous primal witness,
Gauss flag, source-compatible connection, or differential-rank condition.
In particular it neither removes nor realizes any of the surviving A/B pairs.
The actual rank-three question, positive-square rank28, and smoothing remain open.

## Linearization and duality conventions

Work over C with G the binary icosahedral group, W its standard two-dimensional
SL2 representation, and P1=P(W) parametrizing lines. Give O(-1) its tautological
linearization. Then

    H0(O(n)) = Sym^n(W*) for n>=0,
    omega_P1 = O(-2) tensor det(W*).

Since det W is trivial, choosing an invariant volume form identifies omega
with O(-2) equivariantly. The choice is unique only up to nonzero scalar.
There is no suppressed nontrivial determinant character. Equivariant Serre
duality therefore gives, for any equivariant bundle F,

    H1(F(-1))* = H0(F* tensor O(1) tensor omega)
               = H0(F*(-1)).

The first equality is canonical; the second uses the stated volume
identification. All nine irreducible G-representations are self-dual, so the
published characters M2 and M3 equal their dual characters. No canonical
self-duality of those multiplicity spaces or identification with fixed HM
coefficient spaces is being asserted.

## General lemma and proof

Let F be a G-equivariant vector bundle on this P1 whose ordinary splitting
summands all have degree <=-1. Suppose, as representations,

    H1(F)=U,    H1(F(-1))=V.

Then there exists an equivariant exact sequence of bundles

    0 -> F -> V tensor O(-1) -> U tensor O -> 0.

Indeed put E=F*(-1). Every ordinary splitting degree of E is nonnegative,
so E is globally generated and H1(E)=0. Its canonical equivariant evaluation
sequence is

    0 -> K -> H0(E) tensor O -> E -> 0.                 (1)

The middle map is a bundle surjection; hence K is locally free. On global
sections the evaluation map is the identity of H0(E). As H1(O)=0, its long
exact sequence gives H0(K)=H1(K)=0. By ordinary Birkhoff-Grothendieck splitting,
each summand O(d) of K must satisfy both vanishings: H0=0 implies d<=-1,
and H1=0 implies d>=-1. Thus K is a sum of O(-1)'s.

Set R=H0(K(1)). The evaluation map R tensor O -> K(1) is a canonical
equivariant isomorphism: the underlying bundle K(1) is trivial, so this is
an isomorphism without selecting any equivariant splitting. Consequently
K=R tensor O(-1) equivariantly.

Dualize (1), which remains exact because its terms and quotient are locally
free, and tensor with O(-1). The result is

    0 -> F -> H0(E)* tensor O(-1) -> R* tensor O -> 0. (2)

Serre duality identifies H0(E)* with H1(F(-1))=V under the volume convention.
Taking cohomology in (2), using H0(O(-1))=H1(O(-1))=0, gives the connecting
isomorphism R* = H1(F)=U. Transporting (2) by the prescribed representation
isomorphisms proves the assertion. These transports need not recover any
previously specified source map.

Conversely, any such bundle-exact presentation has all degrees of F<=-1
because F embeds in V tensor O(-1), and its adjacent H1 characters are U
and V. At twist -1 the latter uses H1(O(-2))=1 equivariantly, which is exactly
where det W=1 matters. Thus negativity and the two adjacent character
identities are necessary and sufficient for this abstract presentation.

## Application and independent coefficient checks

For a listed type F=sum R_j tensor O(-j), j>=1, put

    E=sum R_j* tensor O(j-1).

The known adjacent characters give rank F=13, degree F=-54,
H0(E)=M3* of dimension54, and rank E=13, degree E=41. Consequently K has
rank41 and degree-41. Its coefficient representation can also be checked
without any map calculation:

    R = H0(K(1))
      = H0(E) tensor W* - H0(E(1))
      = sum_(j>=2) R_j* tensor Sym^(j-2)(W*)
      = M2*.

The middle equality is an equality of representation characters obtained
by twisting (1) and using H1(K(1))=0. The next equality is the SL2 identity
Sym^(j-1)W tensor W - Sym^j W = Sym^(j-2)W for j>=2;
for j=1 the difference is zero. No selected coefficient is involved.

The central signs agree throughout: F and M2 are center-even; E, H0(E),
and K are center-odd; K(1) and R are center-even. Hence the middle term in
(2) is center-even as required. G is perfect, so every representation has
trivial determinant character. Thus the equivariant determinant lines are
O(-54) for F, O(41) for E, and O(-41) for K, with their standard
linearizations, consistently in (1) and (2). There is no residual scalar
character that can obstruct the construction.

## Bounded reproduction and scope

Run `python verify_abstract_dual_steiner_realizability.py`.
The new verifier reads, but does not rewrite or regenerate, the published
260 profiles in `unrestricted-dual-splittings-and-pairs.json`. It reproduces
exact Q(sqrt(5)) character arithmetic independently and checks every profile:
negative degrees, central parity, rank/degree, adjacent cohomology,
nonnegative degrees and cohomology of E, kernel rank/degree, coefficient
character R=M2*, and the coefficient identity block by block. It also
recovers all ten published H0(F(1)) character counts, including the
37 section-free and 223 non-section-free types.

There are 261 precomputed irreducible/symmetric-power products (nine
irreducibles, powers0 through28), and 260 profiles, each with at most13
blocks. This is a bounded exact character verification, not a re-enumeration
of actual source maps. The existence and acyclicity arguments above are
mathematical proofs, not claims inferred from finite cohomology samples.

The run log is `abstract-dual-steiner-realizability-verification.log`.
The input SHA-256 is
`9aac29c629b7eb7d2e507eb663571221626a435b995809f05ecad627db126fab`.
Only these three new files were created. No actual HM coefficients,
selected points, matrices, rank tests/scans, local-model spikes, or consumed
experiments were used. Earlier published necessary-only files remain unchanged;
the upgraded statement concerns abstract presentations only.
