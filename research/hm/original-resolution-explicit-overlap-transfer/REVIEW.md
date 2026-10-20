# Independent audit: explicit first-face stage-two derivative

## Verdict

**Accepted within the stated source-bound formal scope.** The exact rewrite uses the accepted generator for the same original-reference derivative, retains both negative first-face insertions, preserves the row connection and selector derivative, and agrees with the complete public differentiated-transfer identity at commit `4c0e965b4de72e43c39ba863f9aa8eea15571851`. It does not identify the public differential-variation term with the overlap correction alone.

Reviewed producer proof SHA-256:

    4dc5843a5e7eecaedc0dc1548e2434a6fd56e50d6b3e420adcc6b6f979d7f117

The reviewed proof is copied to `inputs/reviewed-PROOF.md`; `reviewed-producer-pins.json` binds the reviewed producer artifacts. Independent checks pass in normal and optimized Python with identical output. The producer's separate checks were also replayed in both modes. No source module, source/model value, matrix value, source polynomial, detector, or numerical remainder was evaluated. 

## 1. Derivative, normalization, and row action

The inherited accepted homotopy proof has hash `641e7224e2ab1d9e530119817659439bf09d688d179d7572ff01ae63f2a753e1`. Its explicit correction S is applied to every leading owner using the SAME original-reference directional derivative. The resulting identities are

    d'=[ℒ,d],    H'=[ℒ,H],    P'=[ℒ,P],    ℒ=ad_S.

Here d is the internal End differential, P=jπ is supported in internal degree zero, and the directional derivative and ℒ are even. The commutator has no additional Čech or internal Koszul sign. This does not set the original derivative to zero; the corrected connection differs by the displayed ℒ.

The inclusion formula is derived rather than assumed. If v=j'−ℒj, differentiating dj=Hj=0 gives dv=Hv=0. Applying dH+Hd=1−jπ gives v=jπv. Hence

    j'=ℒj+j a_S,    a_S=π(j'−ℒj),
    π'=−a_Sπ−πℒ.

The second identity follows by differentiating P=jπ and using πj=1. These arguments retain the degree-zero projection; deleting it would incorrectly force a_S=0.

The physical single-transpose convention is correct. With j(R)=A R^t B, c_S=B(A'−SA), and B'+BS=−c_S B,

    a_S(R)=R c_S^t−c_S^t R.

The order reversal is essential. Let a=πj' denote the public transfer connection and b=πℒj. Then a=a_S+b, with b(R)=R(BSA)^t−(BSA)^t R. No horizontal row basis is silently selected.

The simultaneous corrected connections are V−ℒ on ambient End coefficients and V+a_S on row coefficients. They make j and π parallel, with the same input and output convention as the public general-gauge formula. A collection of owner-specific old derivatives cannot be substituted for the common initial reference derivative without first retaining their connection differences.

## 2. Raw first face and row transport

For an ambient Čech n-cochain, ℒ_n acts by the leading owner's commutator. Put

    C_n=δ_nℒ_n−ℒ_(n+1)δ_n.

In each deleted face k>0 the leading owner remains t0. Those two terms cancel with the same alternating sign. Face k=0 has sign +1 and changes the leading owner to t1. Thus, after restriction of every factor to the full overlap,

    (C_n F)_(t0...t_(n+1))
      =[S_(t1)−S_(t0),F_(t1...t_(n+1))].

There is no hidden alternating sign and no missing higher-face term. If ambient transport is retained explicitly, this means

    ρ_01 ℒ_(t1)F−ℒ_(t0)ρ_01 F
      =[ρ_01(S_(t1))−S_(t0),ρ_01 F].

The restriction must be the admitted algebra-preserving ambient transport. One cannot subtract coefficient arrays in different frames without it. The producer supplies this qualification explicitly.

Raw ambient δ is not the row differential. The latter is Δ=πδj, whose first face is g_ij^−1(−)g_ij by the accepted quotient-transition theorem. No extra row conjugation is inserted into raw δ. Differentiating Δ gives

    Δ_n'=Δ_n a_(S,n)−a_(S,n+1)Δ_n+π_(n+1)C_nj_n.

The index n+1 on the left row connection is required. Ambient δ'=0 does not imply Δ'=0. The independent formal checks also reconcile this equation with public transfer §8:

    Δ'=Δa−aΔ−πd'J1−πδHd'j.

This uses a=a_S+b and the same normalized contraction. In particular πδHd=πδ(1−jπ), since πδdH=πdδH=0. The projection term supplies the necessary b contribution.

If the INITIAL coefficient derivative has δ'≠0, the additional literal terms are −Hδ'Hδj−HδHδ'j. The corrected restriction variation is then δ'+C. The accepted fixed common-reference specialization uses δ'=0, rather than discarding such a variation after changing derivatives.

## 3. Stage-two signs, indices, and selector

The literal kernel is J2=−HδHδj, with the row input fixed. Substitution of H'=ℒH−Hℒ and j'=ℒj+j a_S into its product rule yields the free-word identity

    J2'=ℒJ2+J2a_S−HC Hδj−HδHCj.

Both overlap insertions have a minus sign. This check requires no contraction identities: all six differentiated words match exactly in a free associative algebra. No H is moved through δ.

For input Čech degree n the complete typing is

    J2_n=−H_(n+2,−1)δ_(n+1)H_(n+1,0)δ_nj_n,

    J2_n'=ℒ_(n+2)J2_n+J2_n a_(S,n)
      −H_(n+2,−1)C_(n+1)H_(n+1,0)δ_nj_n
      −H_(n+2,−1)δ_(n+1)H_(n+1,0)C_nj_n.

The second H index denotes its INTERNAL INPUT degree. C has bidegree (+1,0). Every term has bidegree (+2,−2). The HPL stage-one sign changes with n, but the product of the first two HPL signs is always −1. Therefore the unsigned intermediate J1=Hδj and the same minus word for J2 are consistent for both degree-two and degree-three inputs, and for the formal general-input extension.

The selected derivative is exactly

    (ΛJ2)'=(Λ'+Λℒ)J2+(ΛJ2)a_S
                −ΛHC Hδj−ΛHδHCj.

Both Λ'J2 and ΛℒJ2 remain. The scalar selector has no assumed trace representation that would annihilate the latter. If the input varies, add (ΛJ2)(Z'); outer weights, tests, and any subsequent operators have their own derivative terms. There is no separate free Δ' term in the derivative of the literal word, which contains δ rather than Δ. No input-closure assumption is used.

## 4. Exact comparison with the public transfer, including every endpoint

Write σ=HH' to distinguish the public auxiliary symbol from the accepted generator S. The public definitions are

    t=Hj',    U=σδj−Hδt,
    W=−σδJ1+HδU,
    E_var=−Hd'J2+HδHd'J1+HδHδHd'j.

Normalized H²=Hj=0 gives, with no extra assumption,

    U=HℒHδj−HδHℒj.

This U generally remains an original-derivative boundary primitive. It has Čech increment +1 and internal degree −2; W has increments (+2,−3). For an input of degree n, the public nonclosed-input term is specifically U_(n+1)Δ_n. It cannot be replaced by U_nΔ_n or discarded because the original problem has degree-two inputs.

Define O=−HC Hδj−HδHCj. The exact comparison is

    dW−δU−UΔ+E_var=ℒJ2−J2b+O,

or, equivalently,

    E_var=ℒJ2+O−J2b−dW+δU+UΔ.

The audit independently checks this stronger equation by expanding d'=[ℒ,d] in the public E_var and reducing finite typed operator words using dH+Hd=1−P, the support of P, dδ=δd, dj=πd=0, H²=Hj=πH=0, πj=1, and δ²=0. This is not merely a comparison of two printed conclusions. The ENTIRE public transfer

    dW−δU−UΔ+J2a+E_var

reduces to the newly differentiated word with all of its terms retained.

When Λd=0 and Λ commutes with the admitted restrictions, this becomes

    ΛE_var=ΛℒJ2+ΛO−(ΛJ2)b+δ(ΛU)+(ΛU)Δ.

Thus E_var alone is not being equated with O. The internal boundary dW, the Čech boundary, the nonclosed-input term, and the induced projection correction participate in the exact change of decomposition. Neither an equality of total expressions nor a formal normal form implies source-specific nonvanishing of any individual summand.

The independent gauge check agrees as well. Set Γ_E=−ℒ, Γ_R=a_S, Γ_scalar=0 in public boundary §5. Then dot d=dot H=dot j=dot π=0 and a_cov=0, but dot δ=C and dot Λ=Λ'+Λℒ. The public primitive-change formula gives

    U_cov−U=−HℒHδj+HδHℒj=−U.

Hence U_cov=0 in that changed connection, while the restriction insertion O survives. Because dot(ΛJ2)=(ΛJ2)'−(ΛJ2)a_S, the public selected identity reproduces the exact selected derivative above. This does not say that the original U is zero or erase its original boundary family.

## 5. Functional equality, ownership, and limits

The producer incorporated the requested explicit distinction. Under the accepted legal-free carrier identification and the SAME initial derivative, identical carrier contractions give the same rational h,E,D and therefore the same rational S. On such a first face S_j−S_i=0, so that C insertion vanishes as a rational operator.

This functional cancellation does not identify the two owner OCCURRENCES, their partition weights, legal clearing factors, standard tags, or any earlier prefix owners. Equal masks or coincident divisors alone do not authorize merging ledger entries. Even where C vanishes, the row connection and selector terms still require their displayed treatment.

The producer only inherits the already accepted factor-level reference allowance for S, including its named infinity factor. It does not replace it by the bound for a different old connection, spend an existing standard bound without proof, or infer a domain for the newly separated products. This audit proves no new pole/regularity estimate, deck-character statement, ownerwise bound, partition extension, zero Serre pairing, or full divergence.

The existing public boundary-domain theorem concerns its original properly compared boundary under its stated premises. The algebraic equality here does not transfer that result to each separated overlap or selector summand. Source-specific residual cancellation, total remainder, and obstruction values remain unresolved by this packet.

## 6. Evidence and reproducibility

The audit independently read both principal public proofs through the read-only GitHub connector at the exact commit:

- [Differentiated contraction transfer](https://github.com/Akilleez-QA/read-em-and-weep/blob/4c0e965b4de72e43c39ba863f9aa8eea15571851/research/hm/null-differentiated-contraction-transfer/PROOF.md), Git blob `ba09bf1005bca11537784260d4273cc59431be56`, SHA-256 `c0bbb976e98cc7c4e137079a0ddd9ad191607fc8f7608e97088539b185ff17e2`.
- [Boundary domain and general-gauge formula](https://github.com/Akilleez-QA/read-em-and-weep/blob/4c0e965b4de72e43c39ba863f9aa8eea15571851/research/hm/null-inner-boundary-domain/PROOF.md), Git blob `1941cb00c420185d976de2c43e51b33498019a25`, SHA-256 `3ff8e0634cff39143f2ab57b00741540f545e947a6ae978ca9741bb6f0f5de1d`.

Both independently retrieved texts match the producer's vendored bytes exactly. Records are in `independent-remote-reads.json` and `remote-byte-comparisons.json`. The remaining source conventions were reviewed in the producer's pinned HPL and endpoint snapshots and the accepted homotopy proof/review; hashes authenticate bytes rather than reprove those geometric premises.

`check_formal_identities.py` has 17 passing independent checks. They include the free-word derivative, normalized inclusion/projection compatibility, full old/new transfer, explicit E_var comparison, public/new row compatibility, selector derivative, primitive change, all relevant degree/arity checks for n=0 through 5, and literal first-face cancellation. Negative controls detect omission/sign reversal of the overlap terms and the unsupported E_var-only reduction in the declared formal algebra. A nonzero control residual is not an evaluation or nonvanishing theorem for the actual source.

The producer's `check_formal.py` was inspected before replay and passes its separate checks, seven snapshot pins, and twelve active negative controls. Both checkers use finite dictionaries of symbolic words or integer/string metadata. No assertions are required for optimized-mode correctness, no source modules are imported, and there is no actual matrix or polynomial evaluation.

Reproduce the independent checks with:

    python check_formal_identities.py
    python -O check_formal_identities.py

The saved normal and optimized reports are byte-identical. `SHA256SUMS` binds the audit artifacts; the reviewed producer is frozen separately. All acceptance statements above are scoped to that exact reviewed proof and its declared premises.
