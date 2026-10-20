# Independent audit: universal boundary-image removal criterion

## Verdict

**Correct**, for split graded vector-space cochain complexes over a field, unrestricted algebraic linear maps, compensation free to be `F=dV`, and the stated special form

`K = Qdot T − Π Q`.

Let `D^n=im(Δ:A^(n−1)→A^n)`. Then there exist a closed degree-minus-one `U:B→C` and an unrestricted degree-one `V:A→B` such that

`(K+UT−ΠV)|D=0`

if and only if, in every degree n,

`K(D^n) ⊂ im(Π:B^(n+1)→C^(n+1)) + im(δ_C:C^n→C^(n+1))`.

The equivalence concerns existence of some change that removes the restriction to boundaries. It does not characterize realization of a prescribed full cochain J, and does not replace the stronger fixed-E or prescribed-F tests in the input result.

## 1. Necessity

Write `x=Δa∈D^n`. Since T is a degree-two chain map,

`Tx = TΔa = δ_B Ta`.

Closure of the odd map U means `δ_C U + Uδ_B=0`; hence

`UTx = −δ_C UTa`.

The removal equation gives

`Kx = ΠVx − UTx = ΠVx + δ_C UTa`,

which lies in the stated sum. This direction does not need the special representation of K.

## 2. Boundary-extension lemma, with signs

Let `S⊂im δ_B` be a graded subspace, and prescribe any degree-minus-one linear map `g:S→im δ_C`. Then g extends to a closed degree-minus-one map `U:B→C`.

Choose splittings

`B^m = D_B^m ⊕ H_B^m ⊕ L_B^m`,

where `D_B^m=im δ_B^(m−1)`, `D_B^m⊕H_B^m=ker δ_B^m`, and `δ_B:L_B^m→D_B^(m+1)` is an isomorphism. Extend g degreewise to maps

`g_m:D_B^m→D_C^(m−1)`.

Choose right inverses `s_C^r:D_C^r→C^(r−1)` of δ_C. Define

- `U_m|D_B^m = g_m`;
- `U_m|H_B^m = 0`;
- `U_m(l) = −s_C^(m−1) g_(m+1)(δ_B l)` for `l∈L_B^m`.

On boundaries, `δ_C U=0` and `Uδ_B=0`. The same holds on H. On L, `δ_C U(l)=−g_(m+1)(δ_B l)=−Uδ_B(l)`. Thus `dU=0` exactly, with the required restriction. No finite-dimensional or boundedness hypothesis is needed when these algebraic splittings are available.

## 3. Sufficiency and the kernel-T issue

Set `S^(n+2)=T(D^n)⊂D_B^(n+2)`. The assumed condition and the identity `Kx=Qdot Tx−ΠQx` imply

`Qdot(S^(n+2)) ⊂ im Π^(n+1)+D_C^(n+1)`.

Let `q:C→C/im Π` denote the degreewise quotient. The restriction of q maps `D_C^(n+1)` onto `q(D_C^(n+1))`. By linear splitting choose a linear lift

`g:S^(n+2)→D_C^(n+1)`

of `−q Qdot|S`. Then `Qdot(s)+g(s)∈im Π` for all s in S. By the extension lemma, extend g to a closed degree-minus-one U on B. For x in D,

`Kx+UTx = (Qdot+U)Tx−ΠQx ∈ im Π`.

Choose a linear right inverse of Π onto its image. It lifts `(K+UT)|D` to a degree-one map `V_D:D→B`. Extend `V_D` linearly to all A. Then `(K+UT−ΠV)|D=0`. Define `J=UT−ΠV` and `F=dV`; automatically `dJ+ΠF=0`.

There is no hidden inconsistency when T is noninjective: if `x∈D∩ker T`, then `Kx=−ΠQx`. Equivalently, `qK|D=qQdot T|D` already factors through `T|D`. The construction chooses g on S itself, rather than choosing independent potentially inconsistent values for each preimage x.

## 4. Why the representation of K matters

For arbitrary degree-one K, the displayed image inclusion is not sufficient. For example, take `A^0=ka`, `A^1=kb`, `Δa=b`; `C^1=ke`, `C^2=kc`, `δ_Ce=c`; and `B=0`, so `T=Π=0`. Define `Kb=c`, `Ka=0`. Then K sends input boundaries to output boundaries, but all actual changes `UT−ΠV` vanish. Removal is impossible. This K cannot have the required special representation.

More generally, for arbitrary K one must also ensure the relevant restriction modulo im Π factors through T. The asserted theorem avoids this extra obstruction precisely because of its assumed representation of K.

## 5. Scope limits

- **Fixed E:** This requires `F=dV=0`. Arbitrary extension and lifting of V need not preserve closure. Example 3 of the supplied RESULT.md has image inclusion satisfied (Π is the identity) but fixed-E removal impossible. Thus the universal simplification cannot be stated for that setting.
- **Prescribed F:** The construction freely defines F after choosing V. A prescribed F imposes exactness and the additional affine/closed-map conditions recorded in Theorem 2 of the supplied result.
- **Prescribed J:** An image criterion for removing K only on D does not imply a specified full J is actual. The original cochain obstruction remains valid for that different question.
- **Restricted domains/maps:** Algebraic splittings and extensions can violate continuity, locality, regularity, geometric origin, support, analytic-domain, or other admissibility requirements. If any such restrictions apply, this is only an unrestricted algebraic theorem, not a realization proof in the restricted category.
- **Remaining correction:** Removing `KΔ` does not establish vanishing of the paired correction or complete remainder; compensation can move the contribution into E. No unknown target value follows.

## Provenance

Reviewed [COMPENSATION-LIFTING.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/0c7f3f16ddea65616b2c6d4629c8b44f6fdae625/research/hm/null-homotopy-compensation/COMPENSATION-LIFTING.md) and independently proved the new criterion and its boundary-extension lemma. Only formal algebra and the invented counterexample above were used. No physical sources, model data, geometric jets, production matrices/products, repository imports, geometric experiments were used.
