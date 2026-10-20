# Independent review: coherent reversal descent

## Verdict and exact scope

**PASS**, relative to the hypotheses and pinned mathematical inputs expressly retained in the proof.

Reviewed artifact:

- File: `PROOF.md` in the same directory as this review.
- Title: “Coherent reversal descent and strict parity data”.
- SHA-256: `2153ca56b24eb11ab9391d47c742942feda48b6c436af23d6eae9f6acf4e752b`.
- Review date: 2026-10-20 UTC.

The review independently checked the coherence conventions, the scalar involution and correction signs, compatible formal automorphism trivialization, strictification of coherent objects, equivariant arrows, and the local-equivalence argument. No mathematical correction is required for the claimed biequivalence under the stated hypotheses.

This is a scoped mathematical review, not formal machine verification. It does not discharge the retained literal lifting premise or independently reprove every earlier theorem on which the three pinned papers depend. It does not evaluate any selected HM source, quotient, multiplication matrix, obstruction, detector, rank, generator, or checker. No external repository write or publication was made.

## Sources actually read

The following full proofs were fetched read-only through the GitHub connector at their exact supplied commits, rather than inferred from PR titles or coordination comments.

1. PR444, commit `49ea1a16791fabbbfd6f8642854405446e98b2bd`, `research/hm/reversal-fixed-normal-form/PROOF.md`.
   - Returned Git blob SHA: `295ccf83f99f4593e0ea4415cc5cb632ee65796e`.
   - https://github.com/Akilleez-QA/read-em-and-weep/blob/49ea1a16791fabbbfd6f8642854405446e98b2bd/research/hm/reversal-fixed-normal-form/PROOF.md
   - Section 2 supplies the actual covariant involution, literal inverse and composition behavior, its chart-unit action, and strict fixed-data identification. Sections 5–6 supply finite and formal fixed-class normal form. Its explicit exclusion of coherent actions confirms that the present enhancement is not merely its stated theorem repeated.
2. PR438, commit `971c16a67b1e7d12fce0a8e2d2165ca4839911de`, `research/hm/formal-forgetful-comparison/PROOF.md`.
   - Returned Git blob SHA: `a583f09897ea9511df09c3080f57728add217332`.
   - https://github.com/Akilleez-QA/read-em-and-weep/blob/971c16a67b1e7d12fce0a8e2d2165ca4839911de/research/hm/formal-forgetful-comparison/PROOF.md
   - Lemma 2.1 establishes full finite unrestricted relative automorphism 2-triviality, not only graded vanishing. Theorems 3.2 and 4.2 establish exactly the finite and formal object-class injectivity used to find a parity gauge.
3. PR436, commit `502c978a17cd7037d740d4d08d373c1cb8bd5829`, `research/hm/formal-parity-tower/PROOF.md`.
   - Returned Git blob SHA: `33797db390d2c3863f3ec5c74a8f63c7d595fc2e`.
   - https://github.com/Akilleez-QA/read-em-and-weep/blob/502c978a17cd7037d740d4d08d373c1cb8bd5829/research/hm/formal-parity-tower/PROOF.md
   - Sections 2–3 and 6 supply unitary lifting, finite and compatible formal parity automorphism triviality, and the scalar description of pi_2. The distinction between ordinary and unitary 2-units is explicit in this source.

The source inputs have the same invariant, marked, regular differential scope as the reviewed proof. In particular, PR438's unrestricted automorphism lemma allows arbitrary lower unrestricted products; no parity hypothesis is silently inserted into its use here.

## 1. Coherent-data equations and orientation

The definitions are correctly typed with composition from right to left and a covariant strict involution I.

For an object, `u:x -> Ix` and `a:(Iu)u => id_x`. Both sides of equation (1),

    I(a) * u = u * a,

start at `u(Iu)u` and finish at `u`. This is the appropriate nontrivial normalized C2 associativity condition.

For an arrow, `eta:vf => (If)u`. The right side of equation (2) is the following well-typed pasting:

    (Iv)v f
      -- Iv * eta --> (Iv)(If)u
      -- I(eta) * u --> f(Iu)u
      -- f * a --> f.

Its endpoints coincide with those of `b * f`. No direction reversal or omitted inverse is needed.

For a 2-arrow `c:f => f'`, both sides of equation (3) go from `vf` to `(If')u`. Solving that equation for the transported comparison gives

    eta' = (I(c) * u) o eta o (v * c)^(-1).

This also explicitly justifies transporting comparisons across an ordinary 2-isomorphism later in the proof.

PR444 Section 2.3 verifies the relevant exact 2-functoriality: `C -> tau(C^(-1))` preserves unit-product order in the reversed-opposite algebra, preserves the endpoints of 2-cells, and respects vertical and horizontal composition. Thus using I covariantly in these equations is justified by the cited actual-data formulas, rather than assumed from a cohomological involution.

## 2. Unrestricted pi_1 and pi_2

### Formal pi_1

The compatible ordinary-unit construction is valid. Given a unit C_n trivializing a formal automorphism modulo h^n:

1. Lift C_n as invariant ordinary chart-unit data in the given upper source product. Constant term 1 ensures invertibility; there is no norm condition in U.
2. Apply it to the upper automorphism. The result is literally identity modulo h^n, with both endpoints unchanged.
3. Apply the top part of PR438 Lemma 2.1. Its chart component is an invariant global vector field and vanishes. Its edge component is an invariant Cech 1-cocycle in O_X and is a boundary. A unit identity modulo h^n removes it.
4. Compose the correction with the lifted C_n. The resulting C_(n+1) restricts exactly to C_n.

The coefficientwise limit therefore exists and trivializes the original formal automorphism. Each coefficient requires only finitely many regular differential operations. This establishes formal pi_1=0 directly; no inference from finite pi_1 alone and no inverse-limit/quotient interchange is made.

### Scalar pi_2 and its involution

For an identity 2-automorphism the gluing equation is `C_i=F_ij(C_j)`. Assuming the lower coefficients are common scalars, the next coefficient glues as an ordinary global regular function: positive-order normalized coefficients of F annihilate constants. Connected properness then makes that coefficient scalar. Induction gives exactly `1+h^M C[[h]]`, or its finite truncation. Such units are indeed central and satisfy the equations conversely.

Every gauge acts trivially on these scalars, because its chart map is linear over the base ring and unital. The action of I is not this gauge transport: it is `C -> tau(C^(-1))`. After logarithm it is exactly

    j(c(h)) = -c(-h).

Consequently the j-fixed subspace consists of odd powers, not even powers. The proof's sign, fixed subspace, and identification with unitary scalar units are correct.

## 3. Strictification of coherent objects

The fixed underlying class of `(x,u,a)` has a parity representative p by PR444. For a gauge `g:x -> p`, put

    v = (Ig)u g^(-1),
    b = g * a * g^(-1),

where the square-cell source is identified using the literal gauge cancellations. Indeed

    (Iv)v = g(Iu)u g^(-1).

The comparison for the underlying gauge g is the cancellation identity `vg=(Ig)u`; its arrow-coherence equation is exactly the whiskered original square equation. Thus this is actual transport of the supplied coherent structure.

Unrestricted pi_1=0 gives a 2-cell `t:v => id_p`. One can make the subsequent normalization completely explicit: use the identity underlying gauge from `(p,v,b)` to `(p,id_p,a_0)` and comparison `eta=t^(-1):id_p => v`. Equation (2) defines

    a_0 = b o (I(eta) * v) o eta.

This is an identity 2-automorphism. Coherent transport along the invertible t preserves equation (1), which now reads `j(a_0)=a_0` after logarithm.

For the identity underlying gauge between two normalized structures, equation (2) gives exactly

    a_1 = a_0 + d + j(d).

The choice `d=-a_0/2` therefore gives `a_1=0`. Unique division by two is available both formally and at each finite order, and preserves the marking. The essential-surjectivity proof is correct.

Conversely, if g identifies x with a strict parity p, the stated formula

    u = (Ig)^(-1)g

has `(Iu)u=id_x` literally. Taking the identity square cell gives coherent data and its required triple coherence. No additional square-coherence obstruction is hidden in the converse.

## 4. Equivariant automorphisms and specified gauges

For a strict object, an equivariant automorphism has comparison `eta:f => If`. Trivializing f by an ordinary 2-isomorphism and transporting eta gives a scalar comparison d. The square equation becomes

    d+j(d)=0.

Equation (3), for a scalar 2-cell c, changes it by

    d' = d+j(c)-c.

For `c=d/2`, anti-invariance gives `d'=0`. The signs in the proof are correct, and every relative equivariant 1-automorphism is consequently 2-isomorphic to the equivariant identity.

The automorphisms of that identity instead satisfy `j(c)=c`. They survive as

    exp(product_(r >= M, r odd) C h^r).

Thus the proof does not confuse connectedness of a hom-groupoid with contractibility, or existence of a 2-isomorphism with uniqueness of that 2-isomorphism.

For a specified underlying gauge f between coherent objects, endpoint strictification reduces the existence question to two parity objects p and q that are U-equivalent. PR438's injectivity yields an actual parity gauge `k:p -> q`. Transporting k back produces one equivariant arrow with the original endpoints. Its underlying gauge and f differ by an unrestricted relative automorphism, so unrestricted pi_1=0 provides a 2-isomorphism between them. The explicit transport formula from Section 1 above equips f itself with a comparison. This is stronger than merely finding some equivariant gauge, and the proof supplies the extra step.

For two comparisons on the same f, their ratio is a scalar after transport; their common square condition says the logarithmic difference is anti-fixed. The operator `j-1` is surjective on this anti-fixed part, by division by two. Hence they are related by an equivariant 2-isomorphism. That 2-isomorphism still has the nontrivial j-fixed scalar ambiguity. The stated uniqueness only up to 2-isomorphism is therefore the right strength.

## 5. Local equivalence and biequivalence

For parity p,q, nonemptiness of the coherent hom-groupoid supplies a U-gauge; PR438 then supplies an R-gauge. The converse is immediate. The emptiness comparison is therefore valid.

When nonempty:

- The R hom-groupoid is connected by full relative parity pi_1=0 from PR436.
- The coherent hom-groupoid is connected by the just-proved coherent relative pi_1 calculation, after composing with a chosen parity gauge.
- Both automorphism groups at a gauge are the same j-fixed scalar group.
- The natural functor is literally the identity on those scalar units.

These facts prove an equivalence of groupoids, not merely agreement of abstract homotopy groups: choose any source isomorphism between two source objects, and both isomorphism sets become torsors under their automorphism groups. The induced map of torsors is a bijection because the map on those groups is a bijection. Connectedness of the target supplies essential surjectivity.

Together with the coherent-object strictification, this establishes the claimed biequivalence. At finite order the same argument uses the truncated scalar group. At formal order the proof works with compatible ordinary or unitary units as appropriate and with actual formal scalar corrections; it does not require homotopy fixed points to commute with an inverse limit.

## 6. Assumptions, contribution, and final-edition verification

The argument depends essentially on:

- The exact marked invariant category and its covariant involution.
- The retained literal parity-lifting premise behind PR444.
- Full unrestricted and parity relative pi_1 triviality, including compatible formal trivializations.
- Connected properness and base-linear unital maps, which identify pi_2 and trivialize gauge transport on it.
- Characteristic zero, in particular division by two.

The proof resolves the coherent enhancement left outside PR444: strict parity data model normalized coherent reversal data up to biequivalence, with no extra coherent object-class or pi_1 ambiguity and with the odd-scalar pi_2 retained. It proves neither arbitrary unrestricted parity normalizability nor any source-specific HM, module, prescribed-product, convergence, or algebraicity assertion.

The initial review examined SHA-256 `ac707427284a5b96e32b4bde8204e8c01372a1c9727f041e719a7e8aad182192` and suggested an optional wording clarification distinguishing formal noncontractibility from very small finite truncations. The final edition incorporates it: each nonempty **formal** connected component is not discrete or contractible, while a smallest finite truncation may have zero pi_2. This wording is correct. At n=M the scalar group is zero, and at some other very low truncations it can also be zero.

The final file was reread at the changed passage and its SHA-256 verified. Replacing precisely that one sentence with the earlier sentence recovers the exact initial SHA-256, so the unchanged body is the body independently reviewed above. The verdict therefore applies to the final SHA-256 shown at the beginning of this review, with no outstanding correction or wording request.

**Final result: PASS for the exact SHA-256 above, under the stated pinned premises.**
