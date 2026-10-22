# Independent written audit: fifth and sixth actual source2 transforms

## Verdict and exact proof identification

The reviewed proof is **Conditional fifth and sixth actual source2 forward
transforms**, with SHA-256

`504913562f56d67efa590ef6877880eaae83394026c8f6da095ac5a099138c7c`.

**Verdict: the stated conclusions follow from the pinned inputs, with their
stated branch conditions and scope. No mathematical defect was found.**
This verdict includes Section 7's balanced-locus corollary. It is a written
mathematical audit, not proof-assistant certification, and applies only to
the identified proof bytes.

The essential point is not a formal transfer of endpoint saturation through
an arbitrary quotient. At step five the vertical kernel is not yet full.
The proof supplies the missing argument: an intrinsic obstruction map,
incompatible stabilizer characters at its possible vertical fibers, and
regular division in the actual ambient quotient. At step six the full
constant vertical kernel is genuinely present, so inverse-image transfer
then becomes valid without an additional character argument.

## Public inputs checked

The following source statements were checked against their pinned texts.
The SHA-256 values identify the complete UTF-8 source contents.

1. [PR754: abstract balanced degree-eighteen systems](https://github.com/Akilleez-QA/read-em-and-weep/blob/044add76ebb14043a0edf73171517c90b9ef0c13/research/hm/order-four-quadratic-load/ABSTRACT-DEGREE-EIGHTEEN-BALANCED-SYSTEMS.md),
   commit `044add76ebb14043a0edf73171517c90b9ef0c13`, SHA-256
   `26afce66386de77a6ef3b511d9de1b3053b2a885c290bda84dccf4889562d5bc`.
   It supplies the parameter line, exactly two distinct nonbalanced
   parameters, and the identification of the unique b-zero with
   \(P_t=f_{12}P_6\).
2. [PR784: zero second primal Gauss defect](https://github.com/Akilleez-QA/read-em-and-weep/blob/66aa488fb10158abcc2d35ce58b05b901d44b81a/research/hm/source2-second-defect-zero/PROOF.md),
   commit `66aa488fb10158abcc2d35ce58b05b901d44b81a`, SHA-256
   `b0695ab0fbbfa9a4a4985f29c2818b15a8f6ec1977a5c2eae944d7c3b1bfe766`.
   It supplies the actual constant projections and the saturated equality
   \((Q^*)^{++}=p^{-1}(R_2)\), not merely a generic identification.
3. [PR785: universal four-jet spanning and the actual flag](https://github.com/Akilleez-QA/read-em-and-weep/blob/7ec3b8140abe6ee60f9d0dfee657e7b0be022fc3/research/hm/source2-four-jet-rigidity/PROOF.md),
   commit `7ec3b8140abe6ee60f9d0dfee657e7b0be022fc3`, SHA-256
   `0378cf255b1666f3e8d03f588335a52352ba305d9765cdaea9c4965db8c2792a`.
   It supplies the exact, already derivative-generated sequences
   \(0\to U_{k+2}^8\to R_k\to U_k^{18}\to0\) for \(0\leq k\leq4\),
   the actual \(J_4=\mathcal O(-4)\oplus\mathcal O(10)\), and the
   constant full-inverse-image propagation theorem.
4. [PR786: endpoint Wronskian and its four twelve-orbit types](https://github.com/Akilleez-QA/read-em-and-weep/blob/575c0720268af5bb4b305e29284f65614ba9f9ca/research/hm/source2-endpoint-wronskian/PROOF.md),
   commit `575c0720268af5bb4b305e29284f65614ba9f9ca`, SHA-256
   `858a750d6a7c320affc28fcea614164e5c9c40fcf96be687faa1cc9d38af99c0`.
   It supplies all-parameter basepoint-freeness, the distinct parameters
   \(t_0,t_1,t_2,t_3\), their stated vanishing sequences on \(D_{12}\),
   and exhaustion of all fifth- and sixth-jet exceptions by \(t_0,t_1\).

The audit checks the continuation against these inputs; it does not replace
the source-realization question by an abstract-family existence assertion.

## 1. Local indices and endpoint successive growth

The local index formula

\[
\operatorname{length}_p(C_k/\mathcal A_k)
 =\sum_{i=0}^k(a_i-i)
\]

is correct. In a vanishing-adapted section basis, any maximal minor of the
matrix of derivatives through order \(k\) has valuation at least this
number. The minor for the first \(k+1\) adapted sections attains it:
the leading coefficient is a product of nonzero initial coefficients
times the determinant of the falling-factorial polynomials at the distinct
integers \(a_0,\ldots,a_k\). That determinant is a nonzero Vandermonde.
The minimum maximal-minor valuation over a discrete valuation ring is the
length of the image lattice in its saturation. This also establishes the
claimed local lengths, not just total degrees.

At \(t_0\), the first six orders sum to \(16\), versus the ordinary sum
\(15\); the first seven sum to \(23\), versus \(21\). Thus the original
fifth and sixth endpoint images have lengths one and two at each point
of \(D_{12}\), respectively. There is no contribution elsewhere at these
orders. Consequently

\[
\deg C_4=-70,\qquad \deg C_5=-78+12=-66,\qquad
\deg C_6=-84+24=-60.
\]

Each \(C_k\) is saturated in the same constant ambient bundle. Therefore
\(C_k/C_{k-1}\) is a bundle, not a quotient with hidden torsion. At the
generic point, differentiation of the span through order \(k-1\) gives
the span through order \(k\). This justifies successive saturated growth
without using a horizontal splitting.

In particular \(C_5/C_4=\mathcal O(4)\) and
\(C_6/C_5=\mathcal O(6)\). The sixth fundamental map induced by the
constant connection is nonzero generically, and is a map
\(\mathcal O(4)\to\mathcal O(4)\) after the cotangent twist.
It is an isomorphism. Thus differentiation of the *saturated* \(C_5\)
already produces \(C_6\), with no new sixth-step torsion. This does not
assert that the original sixth derivative image was saturated.

## 2. Intrinsic construction of the fifth obstruction

For \(S=R_4+U_7^8\), the actual projections give

\[
0\to U_7^8\to S\to C_4\to0.
\]

A local frame of \(U_7^8\), together with lifts of a frame of the endpoint
subbundle \(C_4\), is independent in the ambient fibers. Hence \(S\) is
a saturated subbundle. Its quotient \(B\) is locally free and has the
exact sequence

\[
0\to K=V_1\mathcal O/U_7^8\to B\to
H_{\rm fin}\mathcal O/C_4\to0,
\qquad K=\mathcal O(8).
\]

The derivative of a section of \(R_4\), reduced modulo \(S\), is
\(\mathcal O\)-linear in that section: the extra Leibniz term lies in
\(R_4\subset S\). The resulting map kills \(R_3\) and \(U_6^8\)
because their derivatives lie in \(R_4\) and \(U_7^8\), respectively.
Moreover \(R_3+U_6^8\) is exactly the inverse image of \(C_3\) inside
\(R_4\), by the sheaf-surjectivity in the pinned sequences. Thus the
factorization is genuinely a map from the line bundle

\[
L=(C_4/C_3)\otimes T_X=\mathcal O(-10)\otimes\mathcal O(2)
 =\mathcal O(-8).
\]

The raw fifth derivative sheaf contains \(S\), since the complete
vertical step \(U_6^8\to U_7^8\) has nonzero coefficient \(2\).
Its image in \(B\) is precisely the image of \(\phi:L\to B\).
The projection \(\psi\) of this map is the endpoint fifth fundamental
map. The local index calculation shows that \(\psi\) vanishes simply
at each point of \(D_{12}\) and nowhere else in the \(t_0\) branch.

All these constructions use actual nested subbundles and the original
constant connection. They are independent of coordinate, frame, and lift
choices. A bundle splitting is not being differentiated.

## 3. Character obstruction and exact regular saturation

At an arbitrary point of \(D_{12}\), let \(\lambda\) be the tautological
character of a generator of the binary stabilizer, of order ten, and put
\(\zeta=\lambda^2\). The fiber of \(\mathcal O(d)\) has character
\(\lambda^{-d}\). Since the binary group is perfect, the line-bundle
identifications cannot carry an additional one-dimensional character.

Because \(\psi_p=0\), the map \(\phi_p\) can only land in \(K_p\).
But

\[
L_p:\lambda^8=\zeta^4,\qquad
K_p:\lambda^{-8}=\zeta,
\]

and these characters are distinct. Equivariance therefore forces
\(\phi_p=0\). This is exactly the extra fact needed to exclude a
vertical component repairing the missing endpoint derivative.

For \(D=D_{12}\), vanishing of the whole fiber map is equivalent to
divisibility of every local component of \(\phi\) by a local equation
of \(D\). Division therefore gives a regular map

\[
\widetilde\phi:L(D)=\mathcal O(4)\longrightarrow B.
\]

Its projection is nowhere zero: the original projected zeros were simple.
Thus \(\widetilde\phi\) is a line subbundle inclusion. The inverse image
of this line in the ambient bundle is saturated and has the same generic
span as the raw fifth derivative sheaf. It is exactly \(R_5\).

Regular ambient lifts introduce no ambiguity. Two lifts differ by a
section of \(S\). Two choices of a section of \(S\) subtracted before
division differ by a section vanishing at the divisor; after division
their difference is still a regular section of \(S\). Changing the local
equation by a unit changes only the intrinsic transition of \(L(D)\).

It follows, as actual sheaf statements, that

\[
R_5/S=\mathcal O(4),\qquad
R_5/\mathcal G_5=L(D)/L,
\]
\[
0\to U_7^8\to R_5\to C_5\to0,
\qquad R_5\cap V_1\mathcal O=U_7^8.
\]

There is exactly one unit of saturation length at each point of \(D\)
and none elsewhere. The projected normalized line is fiberwise injective,
so it creates no new vertical kernel. Finally

\[
\deg S=-8-70=-78,\quad
\deg\mathcal G_5=-78-8=-86,\quad
\deg R_5=-86+12=-74,
\quad \operatorname{rk}R_5=14.
\]

## 4. Sixth-step full inverse image and cumulative defect

Differentiating the contained \(U_7^8\) produces all of the constant
\(V_1=U_8^8\) as a sheaf. The last vertical coefficient is \(1\), so
there is no saturation caveat. Since \(R_5\to C_5\) is sheaf-surjective,
regular local lifts and constant projection give

\[
q(\mathcal G_6)=C_5+T_X\nabla C_5=C_6.
\]

A subsheaf containing the entire kernel of a quotient and mapping onto
\(C_6\) is the full inverse image of \(C_6\). Therefore

\[
\mathcal G_6=R_6=q^{-1}(C_6),\qquad
\operatorname{rk}R_6=9+7=16,\qquad \deg R_6=-60.
\]

The quotient of the ambient bundle by this inverse image is the vector
bundle \(H_{\rm fin}\mathcal O/C_6\); saturation is established as a
sheaf equality, not just at the generic point.

The sheaf obtained instead from derivatives of the original \(R\)
through order six contains \(V_1\) and projects to \(\mathcal A_6\).
It is \(q^{-1}(\mathcal A_6)\) and has cumulative saturation length
\(24\). This is a different sheaf from the derivative of the already
saturated fifth transform. The new sixth-step defect is \(0\), not
\(24\) or \(12\).

## 5. Primal duality, consecutive quotients, and torsion sheaves

The first quotient \(p\), unlike the fifth-step use of \(q\), already
has its full constant kernel in \((Q^*)^{++}\). Forward differentiation
and saturation commute with that full inverse image. Induction from the
pinned equality gives \((Q^*)^{(k)+}=p^{-1}(R_k)\) for all subsequent
steps under consideration.

The constant pairing identifies
\(E_k=\operatorname{ann}(p^{-1}(R_k))\). The exact dual quotient
sequence gives

\[
\operatorname{rk}E_k=30-11-\operatorname{rk}R_k,
\qquad \deg E_k=\deg R_k,
\qquad J_k=(R_k/R_{k-1})^*.
\]

The degree sign is positive in the middle equality: the quotient of the
constant primal bundle is \((p^{-1}(R_k))^*\).

At \(t_0\), the actual nested sequences yield

\[
0\to\mathcal O(6)\to R_5/R_4\to\mathcal O(4)\to0,
\]
\[
0\to\mathcal O(8)\to R_6/R_5\to\mathcal O(6)\to0.
\]

Both extensions split since \(H^1(\mathcal O(2))=0\); averaging gives
equivariant splittings. They are used only for bundle isomorphism types.
Thus

\[
(\operatorname{rk}E_5,\deg E_5)=(5,-74),\quad
(\operatorname{rk}E_6,\deg E_6)=(3,-60),
\]
\[
J_5=\mathcal O(-6)\oplus\mathcal O(-4),\quad
J_6=\mathcal O(-8)\oplus\mathcal O(-6).
\]

For the fifth Gauss injection, the canonical dual filtration has endpoint
subline map \(\mathcal O(-4)\to\mathcal O(8)\), with simple divisor
\(D_{12}\), and vertical quotient map
\(\mathcal O(-6)\to\mathcal O(-6)\), an isomorphism. The snake lemma
therefore gives precisely \(\mathcal O(8)|_{D_{12}}\) as its cokernel.
This is stronger than merely computing its length. It also avoids
assuming that a selected splitting diagonalizes the Gauss map.

The next Gauss injection has equal-rank source and target of degree
\(-14\). Its determinant is nonzero generically and is a section of
\(\mathcal O\), so it is an isomorphism everywhere.

## 6. The other two branches

If fifth endpoint jets span everywhere, the projection of \(\phi\)
is already nowhere zero. Hence no fifth saturation occurs and
\(0\to U_7^8\to R_5\to U_5^{18}\to0\), of degree \(-86\).
Its consecutive quotient is an extension of \(\mathcal O(-8)\) by
\(\mathcal O(6)\), split by \(H^1(\mathcal O(14))=0\).
This gives \(J_5=\mathcal O(-6)\oplus\mathcal O(8)\) and an
isomorphic fifth Gauss injection.

At \(t_1\), the sixth endpoint index is one at each point of
\(D_{12}\), so \(\deg C_6=-84+12=-72\). The full constant vertical
kernel is present at the raw sixth step, giving
\(\mathcal G_6=q^{-1}(\mathcal A_6)\) and
\(R_6=q^{-1}(C_6)\). The new defect is reduced of length twelve.
The consecutive endpoint quotient is \(\mathcal O(6)\), and the
vertical quotient is \(\mathcal O(8)\). Their extension splits, giving
\(J_6=\mathcal O(-8)\oplus\mathcal O(-6)\).
The sixth Gauss map has endpoint subline
\(\mathcal O(-6)\to\mathcal O(6)\), with divisor \(D_{12}\), and
isomorphic vertical quotient. Its exact cokernel is
\(\mathcal O(6)|_{D_{12}}\).

Outside \(t_0,t_1\), sixth jets span everywhere. Then \(\deg C_6=-84\),
\(C_6/C_5=\mathcal O(-6)\), and the extension by the vertical
\(\mathcal O(8)\) splits by \(H^1(\mathcal O(14))=0\). Thus
\(J_6=\mathcal O(-8)\oplus\mathcal O(6)\), and the sixth Gauss map
is an isomorphism. The final numerical check is

| Endpoint branch | \(\deg E_5\) | \(\deg E_6\) | New fifth defect | New sixth defect |
| --- | ---: | ---: | ---: | ---: |
| \(t_0\) | \(-74\) | \(-60\) | \(12\) | \(0\) |
| \(t_1\) | \(-86\) | \(-72\) | \(0\) | \(12\) |
| \(t\notin\{t_0,t_1\}\) | \(-86\) | \(-84\) | \(0\) | \(0\) |

The primal ranks are \(5\) and \(3\) throughout. Exhaustion of these
branches is exactly the stated PR786 input.

## 7. Balanced-locus corollary and remaining boundary

At PR754's unique b-zero,

\[
\mathcal H_b=A_{18}\oplus f_{12}H^0(\mathcal O(6)).
\]

The invariant divisor of the nonzero degree-twelve form \(f_{12}\) is
the reduced \(D_{12}\), because no smaller projective orbit exists.
At any point of that divisor, the complete degree-six subsystem has
orders \(0,\ldots,6\); multiplication by the simple zero gives seven
sections of distinct orders \(1,\ldots,7\). PR786's all-parameter
basepoint-freeness supplies a section of order zero. The eight initial
orders \(0,\ldots,7\) give independent order-seven jet images.

Consequently this b-zero cannot be \(t_0,t_1\), or \(t_2\). Since the
only other nonbalanced parameter is a single distinct a-zero, at most
one of the distinct points \(t_0,t_1\) is nonbalanced. At least one is
balanced, while both fail global sixth-jet spanning. Therefore balancedness
alone does not imply sixth-jet spanning and cannot rule out both exceptional
rows.

This argument does not establish that \(t_0\) itself is balanced, locate
the a-zero, choose an actual source parameter, or prove realization of an
exceptional branch. The complete audit uses only universal local identities,
exact sequences, and arbitrary-stabilizer arguments; no selected
actual-source coefficient, point, derivative, matrix, or rank is required.

The frozen proof correctly preserves these distinctions. Its conditional
actual flag conclusions and its abstract balanced-locus corollary are
mathematically supported by the cited inputs.
