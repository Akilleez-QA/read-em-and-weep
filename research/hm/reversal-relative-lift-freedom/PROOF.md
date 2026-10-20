# One-step relative freedom in the reversal-compatible ambient category

## 0. Result and scope

Fix a strictly invariant reversal-compatible differential algebroid presentation modulo h^N, N >= 3, on the individually invariant affine acyclic cover stipulated in PR409 and PR416. Keep every coefficient of degree less than N literally fixed. At order N allow all three new coefficient types to vary: local binary products, overlap maps, and triple units. Quotient by invariant chart gauges which commute with formal reversal and invariant reversal-unitary edge units, all literally the identity modulo h^N.

Provided at least one such lift exists, its one-step equivalence classes form a torsor under

- H^1(X,T_X)^G, if N is even;
- H^0(X,Lambda^2 T_X)^G direct_sum H^2(X,O_X)^G, if N is odd.

For a complex abelian variety of dimension g with geometric inversion iota, PR416 supplies nonemptiness under its explicit invariant literal lifting input. These vector spaces have dimensions g^2 and 2 binom(g,2), respectively. For g=4 the new split is 16 at even steps and 12 at odd steps. The previously established unrestricted one-step torsor has dimension 28 at every step; it is not being reproved or renamed here.

The result classifies only the stated one-step relative equivalence relation. It does not identify arbitrary all-orders continuations with reversal-compatible ones, classify unmarked or non-equivariant equivalences, or prove a module lift, period identification, algebraization, fixed-Moyal theorem, or six-pure-condition vanishing. No selected source, HM function, module, matrix, or retained detector is evaluated.

One categorical distinction must be explicit. Requiring even chart 1-gauges and reversal-unitary edge units does not, by itself, stipulate whether chart units implementing 2-morphisms must be reversal-unitary. The object torsor above is the same under either convention. Section 6 computes both choices rather than silently conflating them.

## 1. Dependencies and exact setting

The immediate inputs are:

1. [PR409, full parity-separated proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/59fc9cdc40cf9a21fbb38549767829ff7471294f/research/hm/parity-separated-ambient-lifting/PROOF.md) and [odd-bivector repair](https://github.com/Akilleez-QA/read-em-and-weep/blob/59fc9cdc40cf9a21fbb38549767829ff7471294f/research/hm/parity-separated-ambient-lifting/ODD-BIVECTOR-REPAIR.md), exact head 59fc9cdc40cf9a21fbb38549767829ff7471294f: parity-separated lifting and the reversal-unitarity lemmas.
2. [PR416, full reversal-compatible continuation proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/c71356722bc7bd1a426d26ea0ca6d050f4c3ed81/research/hm/parity-separated-ambient-lifting/REVERSAL-COMPATIBLE-CONTINUATION.md), exact head c71356722bc7bd1a426d26ea0ca6d050f4c3ed81: existence of a reversal-compatible continuation, conditional on the prior invariant literal small-extension theorem. Only nonemptiness and, separately, continuation of a chosen reversal-compatible representative use this input.
3. The [public invariant literal small-extension proof](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6259748725) supplies the unrestricted regular differential three-slot framework. The prior unrestricted 28-dimensional relative-moduli result is retained as a comparison, not an existence proof for the restricted category. The complete difference and gauge calculations needed for that comparison are repeated here in Sections 2, 3, and 5, so the present proof does not depend on an unavailable private artifact.
4. Ordinary normalized differential Hochschild cohomology on smooth affine intersections, affine Cech acyclicity, and exactness of finite-group invariants in characteristic zero.

The [coordination question](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6286774961) asks for deformation freedom inside this category and explicitly distinguishes this from classification of arbitrary continuations. This proof respects that boundary.

Let X be smooth and separated over a characteristic-zero field k. Let G be finite and preserve each indexed open of a chosen affine cover with affine finite intersections. All cochains below are regular differential cochains, positive-arity cochains are normalized, and all data are strictly G-invariant. Assume the cover computes the indicated coherent cohomology. Put

  R = k[h]/(h^(N+1)),   I = (h^N) subset R,   epsilon = h^N.

Thus I^2=0 and hI=0. The ordinary multiplication is denoted m. Formal reversal tau fixes ordinary functions and sends h to -h; it is distinct from the geometric G-action, which fixes h.

An object consists of associative products mu_i, unital differential algebra maps F_ij, and units A_ijk with classical reductions m, id, and 1, and descent equations

  F_ij F_jk = Ad_i(A_ijk) F_ik,
  A_ijk *_i A_ikl = F_ij(A_jkl) *_i A_ijl.

Reversal compatibility means

  mu_(r,i)(g,f) = (-1)^r mu_(r,i)(f,g),
  tau F_ij = F_ij tau,
  tau(A_ijk) = A_ijk^(-1).

Equivalently every odd coefficient of F vanishes. Inversion of an element and multiplication of units use the relevant local product. For positive arity, normalization in particular gives t(1)=0 for a chart 1-cochain and u(1,f)=u(f,1)=0 for a binary cochain.

## 2. Linear equations for differences of two lifts

Choose one genuine reversal-compatible lift as origin only for the calculation. Write a second lift with the same literal reduction as

  mu'_i = mu_i + epsilon u_i,
  F'_ij = F_ij + epsilon v_ij,
  A'_ijk = A_ijk + epsilon a_ijk.

Every product involving epsilon and a positive power of h vanishes. Thus all difference equations use only ordinary multiplication and the identity classical maps. Let b be the ordinary Hochschild differential, with

  (bt)(f,g) = f t(g) - t(fg) + t(f)g,
  (bu)(f,g,l) = f u(g,l) - u(fg,l) + u(f,gl) - u(f,g)l.

Let delta be the alternating Cech differential, so (delta t)_ij=t_j-t_i and (delta v)_ijk=v_jk-v_ik+v_ij. Direct subtraction of the four defining identities gives precisely

  bu = 0,                       (associativity)
  delta u - bv = 0,             (multiplicativity)
  delta v = 0,                  (inner descent)
  delta a = 0.                  (scalar pentagon)                 (2.1)

For example, the multiplicativity difference is u_j-u_i+v(fg)-v(f)g-fv(g), giving the second equation with its stated sign. The top change of A has no inner effect: Ad(1+epsilon a)=id because the classical algebra is commutative and the quantum commutator costs at least one further h. The top change u of a normalized product has no effect on an inner conjugation or a unit product at this precision, since the units reduce to 1. The top v acts trivially on A=1+O(h), since v(1)=0. The scalar difference is a_ijk+a_ikl-a_jkl-a_ijl=-delta a.

Conversely, (2.1) is sufficient: adding any such triple to a genuine lift preserves all identities, since there is no surviving nonlinear remainder. This is a direct one-step argument, not a formality assumption.

Reversal imposes further exact restrictions:

  u(g,f)=(-1)^N u(f,g),
  v=0 if N is odd,
  a=0 if N is even.                                          (2.2)

The last assertion deserves verification even when the products vary. Expanding tau(A')*'A' relative to tau(A)*A changes its top coefficient by ((-1)^N+1)a. The contribution of u is u(1,1)=0; all its nonconstant arguments cost further h. Hence the norm condition forces 2a=0 at even N and imposes no condition at odd N.

## 3. The actual allowed gauge action

Choose unital differential chart changes E_i and edge units B_ij. Use the transport convention

  mu_i^E(x,y) = E_i^(-1)(mu_i(E_i x,E_i y)),
  F_ij^E = E_i^(-1) Ad_i(B_ij) F_ij E_j,
  A_ijk^E = E_i^(-1)(B_ij *_i F_ij(B_jk) *_i A_ijk *_i B_ik^(-1)).  (3.1)

Require E_i to commute with tau and B_ij to be reversal-unitary. These conditions preserve the category exactly, not just linearly. Indeed even E transports the anti-automorphism tau; Ad(B) commutes with tau for reversal-unitary B; and products, inverses, and images under an even algebra map preserve reversal-unitarity. Therefore every expression in (3.1) has the required parity or unit condition and satisfies descent by the ordinary transport calculation.

At the relative one-step level write

  E_i = id+epsilon t_i,   B_ij=1+epsilon c_ij.

Evenness of E and reversal-unitarity of B are exactly

  t=0 if N is odd,       c=0 if N is even.                  (3.2)

For the unit constraint, tau(B)*B=1+epsilon(((-1)^N+1)c); for the chart constraint, tau E tau=id+(-1)^N epsilon t. All allowed t and c subject to these conditions define actual invertible gauges over R. There is no further integrability condition.

Expanding (3.1) gives

  Delta mu = epsilon bt,
  Delta F = epsilon delta t,
  Delta A = epsilon delta c.                               (3.3)

To see the last formula, the top effect of E_i^(-1) on A is zero because t_i(1)=0; the unit contribution is c_ij+c_jk-c_ik. The top inner action of B is zero by classical commutativity. In a noncommutative classical model it would contribute -bc to Delta F, but here bc(f)=fc-cf=0. Dropping that contribution here is a calculation, not omission of arity zero: c remains essential in Delta A and in the 2-morphisms below.

Consequently the allowed actions on the differences (u,v,a) are exactly

  N even: (u,v,0) -> (u+bt, v+delta t, 0),
  N odd:  (u,0,a) -> (u, 0, a+delta c).                    (3.4)

All formulas preserve the given coefficients below degree N literally.

## 4. Classification of the relative object classes

### 4.1 Even N

Here u is a symmetric normalized differential Hochschild 2-cocycle on each affine chart. Differential HKR says that its class is its bivector antisymmetrization. This class is zero, so choose normalized differential t_i with bt_i=-u_i. Since u is invariant, finite-group averaging makes t invariant without altering the equation. Using this even chart gauge sets u to zero.

The remaining equations are bv=0 and delta v=0. A normalized Hochschild 1-cocycle of a commutative algebra is exactly a derivation, so v is a Cech 1-cocycle in T_X. A remaining chart gauge which keeps u=0 satisfies bt=0, and hence is a derivation-valued Cech 0-cochain. It changes v by delta t. Thus the quotient is exactly

  H^1(X,T_X)^G.                                            (4.1)

The choice of local primitive is immaterial: two primitives differ by a derivation-valued Cech 0-cochain and hence change v only by a Cech coboundary. Conversely each invariant derivation-valued 1-cocycle gives a lift difference (0,v,0); every class is therefore realized. No scalar gerbe direction survives at this parity because the norm condition forces a=0, and no local-product class survives because symmetric binary cocycles are exact.

### 4.2 Odd N

Here v=0 and u is antisymmetric. An antisymmetric Hochschild 2-cocycle on a commutative characteristic-zero algebra is an actual biderivation. This can be proved without choosing HKR representatives. The cocycle equations on (f,g,l), (f,l,g), and (g,f,l), using antisymmetry and commutativity, give

  u(fg,l)=f u(g,l)+u(f,gl)-l u(f,g),
  u(f,gl)=f u(g,l)-u(g,fl)+g u(f,l),
  u(g,fl)=u(fg,l)-g u(f,l)-l u(f,g).

Substitution yields 2u(fg,l)=2f u(g,l)+2g u(f,l). Characteristic zero gives the first Leibniz rule, and antisymmetry gives the other. Therefore u_i is a section of Lambda^2 T_X.

Equation delta u=0 glues these sections into a global invariant bivector. The remaining independent equation is delta a=0. By (3.4) the allowed gauge does not change u and changes a by an arbitrary invariant Cech boundary. Thus the quotient is exactly

  H^0(X,Lambda^2 T_X)^G direct_sum H^2(X,O_X)^G.            (4.2)

Both directions are realized independently: add epsilon times a global bivector to all local products, or add epsilon times an invariant scalar Cech 2-cocycle to the triple units. Their associativity and descent equations hold by (2.1), and their reversal constraints hold by (2.2). In particular these are genuine lift directions, not just candidate obstruction groups.

### 4.3 Torsor, not preferred vector space

The preceding calculations used one lift as a temporary origin. Differences between any two lifts satisfy the same equations, and their gauge action is the same translation action, independently of the origin. Consequently the nonempty set of relative classes is a torsor under (4.1) or (4.2). No canonical origin or canonical representative has been selected.

If the new local products are instead fixed in advance, the odd-order bivector summand is absent and the conditional lift set, when nonempty, is an H^2(O_X)^G torsor. The even-order calculation still gives H^1(T_X)^G, with chart gauges restricted to derivations at the top. None of these statements removes PR409's fixed-product odd obstruction.

## 5. Comparison with the unrestricted 28-dimensional result

For the same fixed literal lower presentation, unrestricted invariant relative lifts have torsor group

  HH^2(X)^G = H^0(Lambda^2 T_X)^G direct_sum H^1(T_X)^G direct_sum H^2(O_X)^G.

The inclusion of reversal-compatible objects and gauges induces an injective map on the one-step relative classes. This injectivity does not need an unproved equivariant-normal-form theorem. It follows immediately from the explicit top action.

If two even-step reversal lifts are related by an unrestricted relative gauge (t,c), their product and map changes depend only on t, while their scalar difference is zero. Replacing c by zero still gives the same endpoint, and this is a permitted reversal-compatible gauge at even N.

If two odd-step reversal lifts are related by an unrestricted relative gauge (t,c), their bivector difference equals bt. The left side is antisymmetric and bt is symmetric, so both vanish. Their map difference is zero as well. Replacing t by zero therefore retains the same product and map endpoints, and retaining c gives the same scalar endpoint. This is a permitted reversal-compatible gauge at odd N.

With any reversal lift as shared origin, the images are precisely the H^1(T_X)^G summand at even N and the other two summands at odd N. This is the new parity restriction on the existing unrestricted freedom. It is not a claim that an arbitrary unrestricted lift can be brought to reversal form: a nonzero complementary unrestricted class already obstructs doing so by a gauge literally identity below this step.

## 6. Literal automorphisms and 2-morphisms

These groups must not be confused with the object parameters.

### 6.1 Actual 2-morphism formula

For chart units C_i in the unprimed local algebras, put

  E_i^new = Ad_i(C_i) E_i,
  B_ij^new = C_i *_i B_ij *_i F_ij(C_j^(-1)).              (6.1)

This changes the gauge but not either endpoint in (3.1). For the overlap identity, the factors Ad(F_ij(C_j^(-1))) and F_ij Ad(C_j) cancel. For the triple unit, use F_ij F_jk=Ad(A_ijk)F_ik to move the C_k term across A_ijk; the remaining conjugation by C_i is removed by (E_i^new)^(-1). Thus (6.1) is an actual inner 2-morphism convention, with no appeal to a total-complex slogan.

At the relative top level C_i=1+epsilon s_i, Ad(C_i)=id and (6.1) becomes

  t^new=t,   c^new=c-delta s.                              (6.2)

If C is required to be reversal-unitary, then s=0 at even N and s is unrestricted at odd N. Such unitary C automatically preserve the allowed E and B at all truncated orders.

### 6.2 Automorphisms with unitary 2-morphisms

At even N, an automorphism of a fixed lift has c=0 and satisfies bt=0 and delta t=0. Thus its literal one-step automorphism group is H^0(T_X)^G tensor I. There are no nontrivial relative unitary 2-morphisms at even N and no relative 2-automorphisms of the identity.

At odd N, an automorphism has t=0 and delta c=0. Literal automorphisms are invariant scalar Cech 1-cocycles, not necessarily zero. Quotienting by (6.2) gives the 1-automorphism classes H^1(O_X)^G tensor I. The 2-automorphisms of the identity are delta s=0, namely H^0(O_X)^G tensor I.

Consequently, under the unitary-2-morphism convention,

  N even: pi_1 = H^0(T_X)^G tensor I,  pi_2 = 0;
  N odd:  pi_1 = H^1(O_X)^G tensor I,  pi_2 = H^0(O_X)^G tensor I.  (6.3)

These are relative top groups at a fixed object. They are not an assertion that gauges or 2-morphisms at different orders act independently.

### 6.3 If all ordinary inner 2-morphisms are retained

Suppose the 1-morphisms remain even/unitary as before, but no unitary constraint is imposed on C. At odd N nothing changes, since every C=1+epsilon s is automatically unitary. At even N, both edge coefficients must remain zero, so (6.2) requires delta s=0. Hence arbitrary global scalar top units remain 2-automorphisms, even though they are not reversal-unitary at this order. The even pi_2 in (6.3) is then replaced by H^0(O_X)^G tensor I. The object torsors and pi_1 calculations do not change.

Thus an unqualified assertion that there are no even scalar 2-automorphisms would be false unless unitary chart 2-morphisms are part of the category definition. Conversely importing unrestricted scalar 2-automorphisms into the strictly unitary category would also be false.

## 7. Abelian inversion specialization and continuation boundary

Let X be a connected complex abelian variety of dimension g, G=<iota> with iota=[-1], V=H^0(T_X), and W=H^1(O_X). Both V and W have dimension g and inversion acts by -1 on both. The standard coherent cohomology descriptions give

  H^1(T_X)^iota = V tensor W,
  H^0(Lambda^2 T_X)^iota = Lambda^2 V,
  H^2(O_X)^iota = Lambda^2 W.

All three spaces are inversion-even. Therefore their dimensions are g^2, binom(g,2), and binom(g,2). For g=4 they are 16,6,6, and the two reversal steps have 16 and 12 object parameters. Their sum is 28, the dimension of the unrestricted one-step torsor, but they occur at different parity steps rather than all at each step.

Furthermore H^0(T_X)^iota=0, H^1(O_X)^iota=0, and H^0(O_X)^iota=C. In the unitary-2-morphism convention, invariant 1-automorphism classes vanish at every step, while scalar relative 2-automorphisms occur exactly at odd steps. At even steps the literal invariant relative 1-gauge automorphism is already the identity; at odd steps nontrivial literal Cech-boundary edge automorphisms can remain, but they are 2-isomorphic to the identity.

PR416 supplies at least one lift of every admissible literal lower presentation on this cover, conditional on its retained invariant literal lifting theorem. This establishes nonemptiness for each of the torsors just computed. Moreover any representative of any of these classes is itself a reversal-compatible presentation, so PR416 can be applied starting from that representative. It follows that every one-step class has some coefficientwise reversal-compatible continuation, preserving that representative literally.

This last existence consequence must not be promoted to a classification of all formal continuations, a canonical affine product of the successive torsors, or a statement that every unrestricted continuation is equivalent to reversal form. Nothing here changes the fixed-product odd equation, the ambient-versus-module distinction, or any remaining source-dependent obstruction.
