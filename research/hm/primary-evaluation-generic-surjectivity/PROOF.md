# Full support excludes the last deficient primary evaluation rank

Work over C. This proof concerns the actual primary evaluation map, not the full adjoint quadratic map. Use the notation A0=M0=V3, dim A0=dim V=5, and dim W=2, where W is the primed binary representation in PR543. The actual quadratic multiplication is, up to a nonzero scalar,

(a tensor D)x = (id_V tensor D)(a wedge x),

under Lambda^2 A0 = V tensor W and S2=A0 tensor sl(W). The preceding structural exclusions leave generic evaluation rank seven or ten. We prove that it is ten.

## 1. A universal annihilator lemma

Let V have dimension n, let W have dimension two, and let L be an l-dimensional subspace of V tensor W over a characteristic-zero field. Put

K = {k in V* tensor W* : k((id_V tensor D)z)=0 for every D in sl(W), z in L}.

Assume that the V*-support of K is all of V*, meaning that the image of contraction K tensor W -> V* spans V*. Then

dim K <= 2n-2l.

Here the support and the annihilator are literal subspaces, not numerical ranks assigned to a selected matrix.

Choose a basis of W and write each z in L as (a,b) in V direct_sum V. Let A and B be the respective projection images of L. Write a dual vector as (c,d) in V* direct_sum V*. The three standard generators E12, E21 and diag(1,-1) of sl(W) show that membership in K is equivalent to

c restricted to B = 0,
d restricted to A = 0,
c(a)-d(b)=0 for every (a,b) in L.

Thus the two projection images of K lie in B-perp and A-perp, respectively. If v belongs to A intersect B, both projection images annihilate v. Full V*-support then forces v=0. Therefore A intersect B=0.

There is consequently a surjective linear map

B-perp direct_sum A-perp -> L*,
(c,d) |-> [(a,b) |-> c(a)-d(b)].

To justify surjectivity, A intersect B=0 makes the restriction maps B-perp -> A* and A-perp -> B* onto, separately. Their direct sum maps onto (A direct_sum B)*; restriction from there to the subspace L is onto. Its kernel is exactly K by the displayed membership conditions. Hence

dim K = 2n-dim A-dim B-l <= 2n-2l,

because L is a subspace of A direct_sum B. This proves the lemma. It is valid over the function field of a parameter space as well as over C.

## 2. Apply the lemma to the actual generic kernel

At the generic point of X=P(A0), the line represented by x determines

L=x wedge A0 subset Lambda^2 A0=V tensor W.

Its dimension is four: the kernel of a |-> a wedge x is the one-dimensional line spanned by x. The exterior multiplication formula identifies the image of evaluation e_x:S2 -> M2 with sl(W)L. The generic kernel of the dual evaluation beta is therefore precisely the annihilator K in Section 1. The dual binary factor is W*; identifying W with W* by its invariant alternating form does not change the V*-support condition.

Suppose the generic rank were seven. Then dim K=10-7=3. PR543's full-support theorem at 622aebd082db42057cd5b8502e941229ff499e58 proves that this actual hypothetical kernel has full V*-support. It uses stability of the actual kernel and determinant-character exclusions, not an assumption that arbitrary covariants define stable sheaves.

The universal lemma now applies with n=5 and l=4, giving

dim K <= 10-8=2.

This contradicts dim K=3. The rank-seven alternative is impossible. Since all other deficient generic ranks were already excluded, the actual primary evaluation has generic rank ten.

Equivalently, there is a nonempty Zariski-open subset of P(A0) on which e_x:S2 -> M2 is surjective, and the dual bundle map beta is generically injective. No point of this open is selected or evaluated by the proof.

## 3. Consequences and retained boundaries

The exact two-channel criterion at PR543, 3fec79146becd5ffee965614dcc50e13de9eb532, now implies that D_beta has rank two. Its two actual determinant-channel images are linearly independent. This conclusion is structural, obtained without evaluating either image.

The earlier Chern obstruction still proves that evaluation is not surjective at every point. Combining the results gives a proper, nonempty evaluation-degeneracy locus. Its maximal-minor codimension is at most three. The degree-105 cycle calculation remains conditional on expected codimension three; generic surjectivity alone does not establish that premise.

This evaluation varies x while allowing all quadratics. It is not the assertion that a fixed quadratic gives full adjoint invertibility. The quadratic residual map, its plane-trace obstruction, and the actual twenty-dimensional primary lift boundary remain separate. No original fixed quadratic/cubic membership, Q4 vanishing, first-order source value, higher lifting, or algebraicity is inferred.

The separate determinantal-comparison parameter k and the derived-intersection parameters x,y are unrelated to the rank-seven alternative eliminated here. In Section 2 the letter x denotes a generic primary-module vector, not the derived parameter.

## Exact dependencies

- Actual exterior multiplication and the evaluation interpretation: PR543 at 7bf725bcd857a2deb975f9ecb80fca32e7833ae0, research/hm/order-four-quadratic-load/PRIMARY-INJECTION-AND-FAILURE.md:
https://github.com/Akilleez-QA/read-em-and-weep/blob/7bf725bcd857a2deb975f9ecb80fca32e7833ae0/research/hm/order-four-quadratic-load/PRIMARY-INJECTION-AND-FAILURE.md
- Remaining ranks seven or ten: PR543 at d6ddff0f1a663df9b102a9fd8d8f915f2d9142d6, RANK-SIX-EXCLUSION.md, with its preceding exclusions:
https://github.com/Akilleez-QA/read-em-and-weep/blob/d6ddff0f1a663df9b102a9fd8d8f915f2d9142d6/research/hm/order-four-quadratic-load/RANK-SIX-EXCLUSION.md
- Full support of the actual hypothetical rank-seven kernel: PR543 at 622aebd082db42057cd5b8502e941229ff499e58, FULL-SUPPORT-AND-PURE-CHANNEL.md, section Stability forces full support. Only this support result is used, not its additional Chern-cycle conclusion:
https://github.com/Akilleez-QA/read-em-and-weep/blob/622aebd082db42057cd5b8502e941229ff499e58/research/hm/order-four-quadratic-load/FULL-SUPPORT-AND-PURE-CHANNEL.md
- Actual two-channel criterion: PR543 at 3fec79146becd5ffee965614dcc50e13de9eb532:
https://github.com/Akilleez-QA/read-em-and-weep/blob/3fec79146becd5ffee965614dcc50e13de9eb532/research/hm/order-four-quadratic-load/TWO-CHANNEL-CRITERION.md
- Nonempty evaluation degeneracy and conditional cycle: PR543 at cef412c142ad8d154cdb18a9967ab6459217cd11:
https://github.com/Akilleez-QA/read-em-and-weep/blob/cef412c142ad8d154cdb18a9967ab6459217cd11/research/hm/order-four-quadratic-load/EVALUATION-DEGENERACY.md

The new contribution is the universal annihilator-support bound and its exclusion of the last deficient actual generic rank. The preceding rank restrictions and full-support theorem are credited inputs. This is an authored structural proof, pending independent review, not formal verification. No selected HM/source-instance evaluation, coefficient search, numerical multiplication matrix, or large computation occurs.
