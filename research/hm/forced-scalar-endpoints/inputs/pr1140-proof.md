# Two independent cubic T channels survive the actual Gauss quotient

## 1. Statement and exact dependencies

Work over C on the original negative parameter line P(W*) with the physical binary-icosahedral marking G=SL2(F5) and fixed determinant convention. Let

    0 -> E -> H O -> Q -> 0,   dim H=30,
    beta_E:E -> Q(-2),   K=ker(beta_E),   A_q=E/K

be the ACTUAL saturated plane-section inclusion, its second fundamental form for the constant connection, and its actual kernel and locally free image quotient. The sheaf injection A_q -> Q(-2) need not have saturated image. The 54-dimensional coefficient presentation of E is not this constant Gauss ambient inclusion.

The primary-terminal theorem PR1123 forces one of four equivariant bundle types:

    D: D O(-2)+(W'+T)O(-3)+V O(-4)+O(-8),
    P: P O(-2)+(W'+T)O(-3)+V O(-4)+W' O(-5),
    V: V O(-2)+(W'+T)O(-3)+2V O(-4),
    Z: (W'+2T)O(-3)+V O(-4).                     (1)

Here T=Sym5 W has dimension6, D=Sym4 W has dimension5, S=Sym3 W has dimension4, and dim(W',V,P)=(2,3,4). No type is asserted realized. For every actual type in (1), independently of the rank of beta_E, we prove

    W'+2T embeds equivariantly in H0(A_q(3)).      (2)

More precisely, the possible cubic kernel representations are

    D-type: H0(K(3)) is 0 or S;
    P-type: H0(K(3)) is 0 or W';
    V-type or Z-type: H0(K(3))=0.                (3)

These are coefficient/global-section conclusions. In particular (2) does NOT give a fiberwise-injective rank14 subbundle of A_q or imply rank(beta_E)>=14.

Eight complete immutable inputs are retained and authenticated in INPUTS.json. PR1123 at 504b7eb800407dfc7e6340c98c72cdd553939f54 supplies (1), not a rank-three source-ledger assertion. PR1129 at d1238732f42df5c70ba4430e230428d2cf699bbe supplies the general near-top coefficient visibility lemma. The ACTUAL, ambient-Gauss and strict-top originals at db51525015bb7c5e825833d550d08dedf6f6ea96 fix the actual inclusion and derivative. The character source fixes the physical representation convention. The original182 coverage note and its JSON are used only for the fixed historical consequence in Section5; their prior geometric coverage theorem is not re-proved here or inferred from a row count. Exact repository paths and full immutable URLs appear in the manifest.

## 2. Saturated negative graphs cannot be horizontal

We recall the small geometric ingredient rather than assume that ordinary Birkhoff summands are horizontal. Suppose F is saturated in a constant bundle, L=U O(-3) is a saturated subbundle of F, and every degree of F/L is at most-2. If beta_F kills L, the actual second fundamental form of L lands in (F/L)(-2). But

    Hom(L,(F/L)(-2))=U* tensor H0((F/L)(1))=0.

Thus L is horizontal in the constant ambient bundle. Its Grassmannian classifying map has zero differential and is constant over C; saturation then makes L a constant subbundle. Its negative degree contradicts this. The same argument applied to any coefficient line in U gives the coefficientwise near-top lemma in PR1129.

For every displayed cubic summand in (1), the complement has degrees at most-2. Hence its cubic coefficient map into H0(A_q(3)) is injective. Any graph of a bundle map from a cubic summand to the degree-minus-two top block is again a saturated direct summand with isomorphic complementary quotient, so the same obstruction applies to such graphs. This is a triangular change of bundle presentation, not a change of the actual embedding or connection.

## 3. The top block contributes a nonzero T channel

First assume type D, P or V, and let F=R O(-2) be its top block, with R=D,P,V respectively. Write p:E -> A_q for the actual quotient, I=im(p|F) for the coherent image, and K_R=ker(F -> I). Since I is torsion-free on the smooth parameter line, it is locally free, and

    0 -> K_R -> F -> I -> 0

is an exact sequence of bundles. We do not replace I by its saturation in A_q.

Strict-top for E implies H0(K(2))=0. Thus H0(K_R(2))=0 and every degree of K_R is at most-3. Moreover R=H0(F(2)) maps injectively into H0(A_q(2)), so p|F is nonzero and r=rank I>=1. It follows that

    h0(K_R(3)) <= rank K_R = dim R-r <= dim R-1.  (4)

The last bound is 4,3,2 for D,P,V. The fixed tensor identities are

    D tensor W=S+T,   P tensor W=W'+T,
    V tensor W=T.                                (5)

The six-dimensional T constituent in H0(F(3)) cannot be killed by its map into H0(A_q(3)), since that would violate (4). Its map is therefore injective, and determines one T multiplicity line in the target. Notice that this argument bounds the kernel of the ACTUAL top row; it never evaluates a scalar of that row or its actual generic rank.

## 4. Graph cancellation forces an independent second T

Let C_T=T O(-3) be the displayed cubic summand in the first three types. By Section2 its coefficient map is nonzero. By (5),

    Hom_G(C_T,F)=Hom_G(T,R tensor W)

is one-dimensional. Composing it with p|F yields exactly the nonzero top T channel from Section3.

Suppose the cubic T image were contained in that same T multiplicity line. Then the bundle row p|C_T would factor as (p|F)g for a map g:C_T -> F: equality on the corresponding coefficient Hom space is equality of bundle morphisms. The graph c -> c-g(c) inside F+C_T is a saturated direct T O(-3) summand of E, and its full p-row is zero. Since beta_E factors through p, this graph is killed by beta_E. Its quotient in E still has maximal degree at most-2, contradicting Section2. Thus the two T channels are independent.

The displayed W' O(-3) has injective cubic coefficient map by Section2. Its irreducible type is distinct from T, so it is disjoint from those two T copies. This proves (2) for the first three types. In Z-type, strict-top directly gives H0(K(3))=0 because every E degree is at most-3, proving (2) there too.

Finally (5) gives the complete source cubic characters

    H0(E(3)) = W'+S+2T,  2W'+2T,  W'+2T,  W'+2T

for D,P,V,Z respectively. In D-type all constituents except S already inject by the preceding argument, and S has multiplicity one. In P-type both T copies and at least one W' copy inject, leaving at most one irreducible W' in the kernel. Finite-group semisimplicity gives precisely (3). In the other two cases equality of the source character with (2) leaves no kernel. Since K has top degree at most-3, the vanishing alternatives are equivalently maxdeg K<=-4. No actual source coefficients or points are selected in any step.

## 5. A fixed historical consequence, not a live frontier count

For each of the original182 ordered rank-three quotient records, compute only

    H0(A_q(3)) = sum_(e,R in A_q) R tensor Sym^(e+3) W,

with negative symmetric indices contributing zero and all multiplicities retained. Condition (2) requires at least one W' and at least two T constituents.

Relative to the weaker PR1129 condition W'+T, this excludes exactly15 additional ORIGINAL records, of which14 have profile(1,1) and one has profile(1,2). Their profile-specific original indices are

    (1,1): 19,20,23,42,43,44,45,53,54,62,67,73,76,102;
    (1,2): 14.

They have only the following five A_q shapes, with their cubic characters:

    O(-8)+W' O(3): W+W'+S+T;
    W' O(-3)+O(4): 2W'+T;
    W' O(-3)+O(6): W'+S+T;
    V O(0): W'+S+T;
    W' O(-3)+O(10): W+2W'+S+T.

Each has exactly one T and so fails the new independent-channel requirement. These five quotient shapes are impossible for any of the actual four sources regardless of profile; the fixed list supplies their historical occurrences, not the proof of impossibility.

In total the strengthened condition rejects45 of the fixed182 records:39/2/4 in profiles11/12/21. Exactly137 records pass this condition alone. These are not newly live exclusions, not a new complete frontier, and not numbers to add to subsequent campaign totals. In particular the entire profile(1,2) and profile(2,1) branches were separately resolved by PR1134 and PR1138; no new profile closure is claimed here. All stable labels, ordered A/B blocks, original defects and cubic characters are recorded in RESULT.json.

The bounded checker verifies the eight input identities, four source characters, three top-channel dimension bounds, relevant Hom multiplicities, five exact quotient identities and the single new condition on the fixed182 records. It uses only the nine-dimensional universal representation ring, through symmetric degree31. It does not rerun the historical quotient enumeration, evaluate an actual instance, or assert that a passing record is realized.

## 6. Contribution and open boundary

The new content beyond the canonical eight-dimensional coefficient visibility of PR1129 is the forced independence of a second six-dimensional T channel from the top block, uniformly across all four primary-compatible sources. The full cubic-kernel alternatives (3) retain additional actual map information for the profile(1,1) investigation.

Profile(1,1) is not excluded here, and the separate original other-profile exhaustiveness is not audited. No COV theorem, global rank-three exclusion, rank-four lower bound, maximal rank, obstruction value, full-adjoint invertibility, smoothing, algebraicity or original-theorem repair follows. No selected actual HM/source coefficient, parameter, point, derivative, jet, tensor, matrix, instance rank or scan is evaluated. The proof concerns the original30-dimensional Gauss ambient space throughout, never the unrelated coefficient-presentation inclusion.
