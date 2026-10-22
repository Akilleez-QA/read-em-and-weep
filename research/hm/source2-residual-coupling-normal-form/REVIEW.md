# Independent review: residual connection coupling normal form

## Reviewed statement and verdict

This review applies to **“A normal form for the source2 residual connection
coupling”**, `PROOF.md`, with SHA-256

`7eb626caae70e62613e8a3e318ac4c6a858502c4fdecfb44a6693e3ed85635c3`.

**Verdict: the stated residual classification passes written mathematical
review. No blocking mathematical gap was found.** Its conclusions are
relative to the cited representation and endpoint results, with precisely
the ambient and equivalence relation stated in the proof. In particular,
the endpoint is fixed in the genuine constant quotient by
\(V_1=\operatorname{Sym}^8W\), not as a horizontal lift in a frozen
complement.

The new conclusions are valid: the graph space is two-dimensional; the
constant shear map is nonzero at every endpoint parameter and forms an
\(\mathcal O(-1)\) subline; its quotient is \(\mathcal O(1)\), up to a
constant determinant factor; and the full specified constant stabilizer
has exactly two orbits, distinguished by zero versus nonzero quotient
coupling. For a balanced endpoint, both orbits retain the residual
splittings and residual Gauss conclusions explicitly cited in the proof.

This is an independent written review, not proof-assistant certification.
It does not certify an actual HM realization, identify its parameter or
coupling, or classify embeddings in the full thirty-dimensional constant
space.

## 1. Graphs, saturation, and apolar conventions

Write \(U=U_2^8\), \(K=(V_1\otimes\mathcal O_X)/U\). For a residual
meeting the stated intersection and projection conditions, its quotient
by \(U\) maps isomorphically onto the fixed line
\(C\subset F_t\otimes\mathcal O_X\). Its other component is therefore a
unique map \(\alpha:C\to K\). Taking the inverse image of its graph is
both necessary and sufficient. This argument classifies actual subbundles,
not merely extension classes.

The saturation assertion is correct. Since the endpoint is a subbundle,
its graph is locally a direct summand of
\(K\oplus(F_t\otimes\mathcal O_X)\); the ambient quotient by its inverse
image is consequently locally free. All-parameter basepoint-freeness in
PR786 supplies this hypothesis, including at the nonbalanced parameters.

The apolar formula has the correct exponent and point convention. Under
the invariant alternating identification \(W\simeq W^*\), the form
associated with a vector \(\ell\) vanishes at \([\ell]\). The apolar
annihilator of \(\ell^6\operatorname{Sym}^2W\) is
\(\ell^3\operatorname{Sym}^5W\). Thus

\[
\operatorname{ann}(U)=T\otimes\mathcal O_X(-3),\qquad
K=T^*\otimes\mathcal O_X(3)\simeq T\otimes\mathcal O_X(3).
\]

Consequently
\(\operatorname{Hom}_G(C,K)\) is the multiplicity space of \(T\) in
\(\operatorname{Sym}^{21}W\). The displayed Clebsch recurrence gives

\[
\operatorname{Sym}^{20}W=1+A+V+P+2D,\qquad
\operatorname{Sym}^{21}W=W+2S+2T,
\]

so its dimension is indeed two. The separate vanishing
\(\operatorname{Ext}^1(C,U)=A\otimes H^1(\mathcal O_X(12))=0\)
does not trivialize the graph datum by constant ambient transformations.
The proof consistently respects this distinction.

## 2. Wronskian nonvanishing and the shear map

The Wronskian lemma used here is valid for every fixed four-dimensional
subspace of \(H^0(\mathcal O_X(8))\) in characteristic zero. An adapted
local basis has distinct initial orders. The determinant of their
falling-factorial coefficients is the Vandermonde in these orders and is
nonzero. The resulting order-three jet determinant is therefore not the
zero section; its line bundle has degree \(32-12=20\).

On the complement of its zero divisor, no nonzero member of that
four-dimensional subspace can vanish to order at least four. In
particular, for the distinguished summand \(P_8\), there is no nonzero
intersection with \(\ell^6\operatorname{Sym}^2W\) there. This is a
generic statement on the whole curve, not a chosen-point calculation.

It follows that a bundle morphism \(C\to P_8\otimes\mathcal O_X\)
whose composition into \(K\) is zero vanishes on a dense open subset and
hence everywhere. Both equivariant Hom spaces have dimension two, so

\[
\rho:\operatorname{Hom}_G(C,P_8\otimes\mathcal O_X)
\xrightarrow{\sim}\operatorname{Hom}_G(C,K)
\]

is an isomorphism. Special points where the fiber intersection might be
nonzero do not invalidate this argument about global morphisms.

Schur's lemma gives
\(\dim\operatorname{Hom}_G(F_t,V_1)=1\). A nonzero such shear cannot
kill \(C\): the fibers of \(C\) span \(F_t\), because the ten defining
sections are independent. Its composition with \(\rho\) is therefore
nonzero. This proves the required nonvanishing for every parameter and
also justifies the unique \(P_8\)-valued lift of every coupling.

## 3. Parameter twists and the quotient line

With the projective space convention that \(\Sigma=\mathbf P(M)\)
parametrizes lines in \(M\), the universal subsystem is

\[
\mathcal H=(A\oplus V)\otimes\mathcal O_\Sigma
\oplus P\otimes\mathcal O_\Sigma(-1).
\]

Its dual has relative \(P^*\)-multiplicity \(\mathcal O_\Sigma(1)\).
Dualizing universal evaluation gives a source pulled back from
\(\mathcal O_X(-18)\), with no parameter twist. Hence the graph space is
the constant bundle \(A_{\rm coup}\otimes\mathcal O_\Sigma\), whereas
the constant shear space is \(\mathcal O_\Sigma(-1)\), up to the harmless
constant identification of the irreducible coefficient spaces.

Under \(\rho\), restriction of a shear is exactly the tautological
multiplicity line. Its inclusion is fiberwise nonzero and has no torsion
degeneracy. Taking determinants yields

\[
0\longrightarrow\mathcal O_\Sigma(-1)
\longrightarrow A_{\rm coup}\otimes\mathcal O_\Sigma
\longrightarrow Q_{\rm coup}\longrightarrow0,
\qquad
Q_{\rm coup}\simeq(\det A_{\rm coup})\otimes\mathcal O_\Sigma(1).
\]

Thus the sign of the parameter degree is correct. This is not a second
endpoint parameter, and the proof does not assert a global nowhere-zero
representative of the positive-degree line bundle.

## 4. Completeness of the constant gauge group

The proof checks the full stipulated stabilizer, rather than only a
subgroup capable of producing two candidate classes.

First, the fibers of \(U_2^8\) span all of \(V_1\), since they contain
the complete Veronese line. A constant ambient automorphism preserving
\(U_2^8\) must therefore preserve \(V_1\); no lower off-diagonal block
is possible. Its restriction to \(V_1\) preserves the backward kernels
\(U_1^8\) and \(U_0^8\), since constant maps commute with the original
connection. The complete osculating identities used for this step are
proved in PR758.

A constant endomorphism preserving every line of an irreducible
full-span projective curve is scalar: the curve lies in the union of its
finitely many projective eigenspaces, hence in one eigenspace, which must
be the entire space. This applies both to the vertical Veronese curve
and to the single fixed endpoint curve as its point of \(X\) varies.
It does not require preservation of other endpoint parameters.

Every stabilizer element therefore has exactly the form

\[
(v,f)\longmapsto(a_0v+b(f),d_0f),\qquad
a_0,d_0\in\mathbf C^*,\quad b\in\operatorname{Hom}_G(F_t,V_1).
\]

Conversely, all these transformations preserve the required data. Their
action is
\(\alpha\mapsto(a_0/d_0)\alpha+d_0^{-1}\rho(bc_t)\).
After quotienting by the shear line, this is arbitrary nonzero scalar
multiplication on a one-dimensional space. There are exactly two orbits.

The zero orbit is precisely the orbit admitting a constant complement
in which the residual is \(U\oplus C\). Fixing that complement, or
fixing the horizontal lift \((0,C)\), would forbid shears and change the
classification. The proof expressly excludes this different equivalence
relation.

## 5. Survival of the stated residual constraints

For a balanced endpoint, the annihilator sequence follows from the
actual intersection and sheaf-surjective endpoint projection:

\[
0\longrightarrow(P+D)\otimes\mathcal O_X(-2)
\longrightarrow E'
\longrightarrow T\otimes\mathcal O_X(-3)
\longrightarrow0.
\]

Its extension group has \(H^1(\mathcal O_X(1))\) as its cohomological
factor and vanishes. Together with the earlier
\(H^1(\mathcal O_X(12))\) vanishing, this gives both asserted splittings.
Averaging a splitting over the finite group makes it equivariant.
Negativity and the full constant spans also follow as stated; the
annihilator of each saturated bundle is the other bundle.

The use of the Gauss results was checked against their actual proofs:

1. PR758's constant-projection kernel lemma requires the exact
   intersection, the saturated projected endpoint, and its zero backward
   kernel. Every graph residual has these properties, so its backward
   flag is \(U_1^8,U_0^8,0\).
2. PR785, Section 5, takes arbitrary regular local lifts of endpoint
   sections. Four-jet spanning makes the projected derivative columns
   independent, so the vertical intersection, sheaf surjectivity and
   saturation through step four hold without a horizontal splitting.
3. PR787, Sections 2–4, isolates the potentially problematic fifth step.
   At a point of the twelve-point orbit the possible vertical repair is
   a map from the fiber of \(\mathcal O(-8)\) to the fiber of
   \(\mathcal O(8)\). Their stabilizer characters are
   \(\lambda^8\) and \(\lambda^{-8}\), which are distinct for a primitive
   tenth root \(\lambda\). Equivariance forces that repair to vanish,
   irrespective of the residual coupling. The normalization and exact
   fifth-step saturation argument therefore transfer unchanged. At step
   six the full constant \(V_1\) is present, so inverse-image exactness
   transfers the endpoint branch and its defect. The full-fifth-jet
   alternatives in Section 6 use the same hypotheses.

Thus the residual statements claimed here apply to both coupling orbits
at the same balanced endpoint. This does not import the separate primal
or full-HM conclusions of PR785 or PR787 without their additional
full-space hypotheses. Nor does it assert feasibility of every additional
condition considered elsewhere. PR788's displayed residual is explicitly
\(U_2^8\oplus C_t\), so it belongs to the zero orbit; its existence does
not force the coupling of a hypothetical actual source to vanish.

## 6. Immutable public sources checked

The following are the public file contents checked for the dependencies
used above. Each SHA-256 is for the UTF-8 contents returned at the linked
immutable commit. These are source hashes, distinct from the reviewed
proof hash at the beginning.

- [PR751, residual full span](https://github.com/Akilleez-QA/read-em-and-weep/blob/e21d50b6bd7d124dc419beeb8c27fa3b9ef3e169/research/hm/order-four-quadratic-load/TWO-ONE-INDEX-TWO-RESIDUAL-FULL-SPAN.md)
  — SHA-256 `f7621cc508b76f8c12e52a0c5eddf067e18688a174265d930403fc8a69641026`.
- [PR751, residual osculations](https://github.com/Akilleez-QA/read-em-and-weep/blob/e21d50b6bd7d124dc419beeb8c27fa3b9ef3e169/research/hm/order-four-quadratic-load/TWO-ONE-INDEX-TWO-RESIDUAL-OSCULATIONS.md)
  — SHA-256 `e89dd5169fc0c80360884de045e8d067564be582366e7f9608394d738b200e3f`.
- [PR754, balanced systems](https://github.com/Akilleez-QA/read-em-and-weep/blob/044add76ebb14043a0edf73171517c90b9ef0c13/research/hm/order-four-quadratic-load/ABSTRACT-DEGREE-EIGHTEEN-BALANCED-SYSTEMS.md)
  — SHA-256 `26afce66386de77a6ef3b511d9de1b3053b2a885c290bda84dccf4889562d5bc`.
- [PR758, exact residual flag](https://github.com/Akilleez-QA/read-em-and-weep/blob/063216038f3aefd65617651c2426721efafc7f9b/research/hm/order-four-quadratic-load/TWO-ONE-INDEX-TWO-EXACT-RESIDUAL-GAUSS-FLAG.md)
  — SHA-256 `65d1e4132f1be1d2b4323b2160d8562c28c5aa3350153b979a8e740ef40a1722`.
- [PR785, four-jet rigidity](https://github.com/Akilleez-QA/read-em-and-weep/blob/7ec3b8140abe6ee60f9d0dfee657e7b0be022fc3/research/hm/source2-four-jet-rigidity/PROOF.md)
  — SHA-256 `0378cf255b1666f3e8d03f588335a52352ba305d9765cdaea9c4965db8c2792a`.
- [PR786, endpoint Wronskian](https://github.com/Akilleez-QA/read-em-and-weep/blob/575c0720268af5bb4b305e29284f65614ba9f9ca/research/hm/source2-endpoint-wronskian/PROOF.md)
  — SHA-256 `858a750d6a7c320affc28fcea614164e5c9c40fcf96be687faa1cc9d38af99c0`.
- [PR787, fifth and sixth transforms](https://github.com/Akilleez-QA/read-em-and-weep/blob/19ec11c934cbba7be18dd1f465ba0d0cc547dcf8/research/hm/source2-fifth-sixth-conditional/PROOF.md)
  — SHA-256 `504913562f56d67efa590ef6877880eaae83394026c8f6da095ac5a099138c7c`.
- [PR788, universal constant flag](https://github.com/Akilleez-QA/read-em-and-weep/blob/941b7b3b77dc8ae8a19b1e000dddeb0438d05db7/research/hm/source2-universal-constant-flag/PROOF.md)
  — SHA-256 `81bb2d40705fa1e35f5719ef59323cd60af675ebe74015651dda9590a2488f29`.

The mathematical checks above use universal representation, bundle,
Wronskian, and stabilizer arguments. They require no selected actual
parameter, invariant-form coefficients, source point, source derivative,
source matrix or source-instance evaluation, and no parameter scan or
large computation.
