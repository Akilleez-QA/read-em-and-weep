# Order-two review and conditional character selection

## Scope and source

Read-only review of Akilleez-QA/read-em-and-weep PR 4, whose fetched current head is fa9be3c2d90ffce8d864bf927ecf3d7cd8dd5de5. The fetched diff adds only the 67-line note research/hm-order-two-reduction.md. Source: https://github.com/Akilleez-QA/read-em-and-weep/blob/fa9be3c2d90ffce8d864bf927ecf3d7cd8dd5de5/research/hm-order-two-reduction.md .

This review checks the character argument conditional on the source's Ext¹ vanishings and equivariant obstruction formalism. It does not rerun the finite-RHom rank certificate, compute any actual obstruction value, evaluate a source model or jet, or prove the source theorem to all orders. The examples below are invented algebraic examples, not models of the actual bundle.

## 1. Second-order proof and precise wording

Write P={1,2}, Q={3,4}, F=P△Q={1,2,3,4}, and 0=∅. A character is a subset, and character multiplication is symmetric difference.

The source asserts Ext¹(E,E) has only characters of cardinality 0 or 1. Accepting this input, any first-order lift variation u lies in these components. A character-compatible baseline lift a₀ can be chosen in P and Q: project a solution of the equivariant linear lift equation onto P and Q. Projection is valid for this linear equation; it is not an argument that an arbitrary nonlinear higher-order solution can be projected or averaged.

For this baseline, a genuinely quadratic expression in the first-order P/Q data has character among P△P=0, Q△Q=0, P△Q=F. This statement concerns the intrinsic quadratic contribution. If one includes arbitrary second-order ambient data in the phrase “quadratic obstruction,” the claim that the entire class has only 0 and F needs a qualification: arbitrary ambient acceleration η can contribute ev_E(η) in weight 2 as well as weight 0. Thus a safe formulation is:

“The intrinsic quadratic contribution for a character-compatible baseline is supported in trivial and full-sign characters. Adding arbitrary second-order ambient acceleration can introduce weight-2 components, but cannot change the full-sign component.”

The source's independence proof then holds. The difference for another first-order lift is L_ξ(u)+u∪u. Products of two weight-0/1 characters have weights 0,1,2; multiplying a P/Q character by a weight-0/1 character gives weight 2, or 1/3. Neither contains F. Hence projection to F annihilates both variation terms. This does not assert that L_ξ itself vanishes.

For completeness, on C⁴, inversion acts with character {i} both on the translation vector field in factor i and on H¹(O_C) from that factor. Consequently:

- H⁰(Λ²T_X) has pair characters {i,j}, i≠j.
- H¹(T_X) has characters {i}△{j}, giving 0 for i=j and weight 2 otherwise.
- H²(O_X) has pair characters {i,j}, i≠j.

Thus HH² has only weight 0 and 2. Equivariant evaluation cannot create F from these characters. Therefore pr_F O₂ is independent of first-order lift and arbitrary second-order ambient acceleration, conditional on the source's equivariant framework and stated vanishing input. Its value remains uncomputed.

## 2. Conditional formal two-parameter selection theorem

Work over a field of characteristic zero (in particular, over C). Give s character P and t character Q. Let M carry a G-action, and suppose a formal M-valued construction A(s,t)=Σ A_ab s^a t^b is equivariant in the precise sense

g A(s,t) = A(χ_P(g)s, χ_Q(g)t).

Equivalently, its series is invariant for the diagonal action on coefficients and base; the characters here have order two, so taking their inverse makes no difference. Comparing coefficients gives

g A_ab = χ_P(g)^a χ_Q(g)^b A_ab.

Hence A_ab belongs to the character P^(a mod 2) Q^(b mod 2). The same statement applies to obstruction cochains and their cohomology classes if the differential, products/brackets, ambient family, lift choices, homotopies, and any projections used in constructing them are compatible with this equivariance.

The complete parity table is:

| a parity | b parity | coefficient character |
|---|---|---|
| even | even | 0 |
| odd | even | P |
| even | odd | Q |
| odd | odd | F |

Therefore the full-sign part has the form st B(s²,t²), with coefficients in M_F. No full-sign coefficient can occur at odd total degree. Degree two permits st. The next allowed degree is four, permitting s³t and st³; s²t² has trivial character. Degree six permits s⁵t, s³t³, st⁵. “Permits” means not excluded by characters; it does not mean nonzero.

Setting s=t=h after constructing this equivariant series preserves the conclusion that only even h-degrees can occur in its full-sign projection, although the diagonal one-parameter slice is not itself generally G-stable. An arbitrary one-parameter extension with the same initial tangent need not arise this way and has no such parity guarantee.

This is a conditional selection theorem for an equivariant formal construction, not an existence theorem for the actual star-algebroid/module family. At each solvable linear correction stage one may average an appropriate correction under a finite group, provided the already-fixed data and right-hand side are equivariant. This does not establish solvability of that stage, remove obstructions, or justify averaging a nonlinear Maurer–Cartan solution. PR4 only supplies an order-two reduction and explicitly lists missing chain-level work. It neither proves that an all-order equivariant ambient family exists in the needed category nor computes its module obstructions.

## 3. Why independence does not propagate to order four

Two related but distinct mechanisms matter. Unrestricted second-order ambient accelerations may have weight 2, and two such components can combine into F at order four. Under strict two-parameter equivariance, total-degree-two coefficients instead have character 0 or F, so that particular weight-2 second-order choice is excluded. Even then, degree-three coefficients can have P or Q and combine with a first-order complementary character to produce degree-four full-sign terms. The parity theorem does not prove choice independence.

### A. Actual second-order acceleration can change order four (unrestricted one-parameter example)

Invent a graded DGLA L with degree-one basis x,z of character P and y,v of character Q, degree-two central basis w of character F, and d=0. Its sole nonzero brackets are [z,v]=[v,z]=w. Graded skew-symmetry requires symmetry on degree-one inputs; centrality makes every Jacobi expression zero. The bracket respects characters because P△Q=F.

Let A be the abelian DGLA on x,y,z,v in degree one, and project L→A by killing w. This is a DGLA morphism. Its kernel K has K¹=0 and K²=<w>, so in particular it has no forbidden high-character first-order module freedom; H¹(K)=0. Every formal ambient series solves MC in A. The obstruction to lifting it is the curvature in K², where d=0 makes a nonzero w coefficient a nonzero cohomology class.

For the fixed initial tangent x+y, choose the ambient extension

a(h)=h(x+y)+h²(αz+βv).

Its unique degree-one lift to L has curvature d a + ½[a,a] = αβ h⁴ w. The factor ½ cancels the two equal cross terms. Orders two and three vanish for every α,β. Order four varies with the second-order ambient acceleration. Choosing α=β=0 gives a lift to every order in this toy example, whereas α=β=1 obstructs at order four. There is no contradiction with order-two acceleration independence: it simply does not control the later quadratic interaction of accelerations. This h-family is not claimed to satisfy the strict s,t-equivariant restriction.

### B. Strict equivariance still does not imply higher ambient-choice independence

Invent L' with degree-one basis x,z of character P and y of character Q; degree-two central w of character F; d=0; and sole bracket [z,y]=[y,z]=w. Project onto the abelian ambient degree-one algebra as before. Again K¹=0, K²=<w>, and all Jacobi and equivariance requirements hold.

The family a(s,t)=sx+ty+αs³z is strictly equivariant: both s and s³ have character P, and t has character Q. Its curvature is αs³t w. All lower-degree obstructions vanish, but the allowed full-sign degree-four coefficient changes with the third-order ambient choice α. The zero and nonzero choices have the same first-order direction and the same second-order ambient jet. This example directly disproves the inference from order-two independence plus parity selection to independence from arbitrary higher ambient choices.

Neither example alleges any such nonzero coefficient for the actual Horrocks–Mumford problem. They demonstrate only the logical insufficiency of the stated character hypotheses for an all-order independence assertion.

## 4. Bounded check

The companion check.py performs only finite XOR-character and sparse-polynomial checks: the second-order support exclusions, the parity selection table through total degree 12, and the two invented central DGLA curvature calculations. It does not use actual source matrices, models, owners, jets, or production computations. Passing the check verifies these bounded identities, not the source vanishings, actual obstruction values, or all-order ambient existence.
