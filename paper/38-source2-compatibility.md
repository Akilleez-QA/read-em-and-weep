# Source2 invariant product compatibility

**Craig Ward · 23 October 2026 · After PR949 and PR950**

[PR949's pinned theorem](https://github.com/Akilleez-QA/read-em-and-weep/blob/e8d9943ed8402be90a6f249a1ad3dd51dcc3c628/research/hm/source2-invariant-compatibility/PROOF.md) narrows the algebra compatible with the actual invariant positive quadratic product for source2. It applies to every balanced endpoint and both residual quotient-coupling classes. **No catalogue pair or stable label is removed:** source2 retains (E13,Q21), and the full necessary frontier remains **four pairs across three labels**.

## Exact conclusion

Let C_N be the complete fixed-variable, degree-preserving G-equivariant endomorphism algebra of the actual negative pencil. Let Q:N2 → N4 be the canonical invariant positive quadratic product, and let D_Q consist of its compatible negative-pencil endomorphisms. Then

    D_Q = C·1 ⊕ J_Q,
    J_Q = D_Q ∩ J,       J_Q² = 0,       0 ≤ dim J_Q ≤ 1.

Here J is the two-dimensional radical of C_N. Thus D_Q is local and commutative, with only zero and one as idempotents. It is either scalar or abstractly dual numbers if its radical is nonzero. Neither alternative is asserted actually realized. In particular **absence of a nontrivial idempotent is not scalarity**.

This is compatibility with the specified negative pencil and Q, not an extension theorem for endomorphisms of the entire HM module.

## The idempotent argument retains the actual source2 geometry

The proof uses the source2 algebra in the correct pencil orientation: radical arrows go from the genuine first block N0 into NC, contained in the residual block NR. This is opposite to the ambient dual-bundle algebra orientation. The extra N8 factor is isolated only when residual quotient coupling is zero; no horizontal splitting is inferred when that coupling is nonzero.

Every idempotent, including all radical shears, is conjugate by a negative-pencil unit to a vertex-subset projector. The conjugating unit need not commute with Q: only its preservation of endpoint characters is used. The eight proper subsets are exhausted.

Most partitions allow an invariant-product image of dimension at most 30, contradicting the actual image character 2V+3P+3D of dimension 33. The remaining N8 partition would saturate its character bound and force Q:N8_2 → N8_4 to be onto with kernel the unique actual A in ker Q. All negative quadratics preserve this genuine block.

A right inverse then constructs a first correction whose second error lies in im Q. The global first-Bockstein vanishing theorem identifies its class with the canonical actual second Bockstein, independently of the correction chosen. This would make the same actual A-to-P quadratic family identically zero, contradicting the pinned geometric nonvanishing theorem. It is not a comparison to a higher gate or unrelated lifting obstruction.

Polynomial interpolation modulo squared distinct diagonal factors turns any compatible nonscalar diagonal into a nontrivial idempotent. Excluding those idempotents therefore gives the scalar-diagonal decomposition C·1 ⊕ J_Q, but by itself does not eliminate J_Q.

## The full radical is excluded without a complement

The additional argument uses the **actual intrinsic annihilator subpencil** from PR795, not merely matching dimensions:

    U = Ann_J N2 = A + 2V + 2P + 3D,     dim U = 32,
    Z = Ann_J N4 = 2V + 2P + 2D,         dim Z = 24.

Suppose every element of J were Q-compatible. Each would preserve ker Q=A+D. Its equivariant square-zero action on this multiplicity-free kernel must vanish, so ker Q is contained in U. Compatibility sends Q(U) into Z. The restricted kernel is exactly the eight-dimensional ker Q, giving rank 32−8=24. Therefore Q:U → Z is onto.

Because this is a genuine annihilator subpencil, every negative quadratic sends U into Z. Its kernel contains the unique actual A. The same right-inverse and correction-independence argument again forces the actual second Bockstein to vanish there. This contradiction rules out J_Q=J, hence **dim J_Q ≤ 1**.

The argument does not require an idempotent, direct-sum complement or horizontal splitting. It strengthens the idempotent exclusion rather than assuming every nilpotent produces a decomposition.

## Conditional radical-image quotients

[PR950](https://github.com/Akilleez-QA/read-em-and-weep/blob/54c7e78bd5351b3ecbdcc4b3b558a0012eb79566/research/hm/source2-radical-image-reduction/PROOF.md) considers a **nonzero compatible radical element j, if one exists**. PR949 bounds such elements to at most one line but does not prove that line exists. Put I_i=im j_i in the actual fixed pencil. The image is preserved by Q and every negative quadratic T_a, so it is an actual subcomplex of Q+tT_a, not an arbitrary abstract quotient construction.

### Non-V directions preserve the specified formal obstruction problem

For every direction except pure V, both I2 and I4 have character P+D and dimension nine. Q is injective on the P constituent because ker Q=A+D has no P. The surjection from coker Q=P onto I4/j4(im Q) forces the full D constituent of I4 into j4(im Q)=Q(I2). Thus **Q:I2 → I4 is invertible**, not merely between spaces of equal dimension.

This removes a nine-dimensional acyclic block from each endpoint. The resulting two-term quotient is **32 → 28**, with invariant rank 24, kernel A+D and cokernel P. Its image block Q|I2+tT_a|I2 is invertible over C[[t]]. An explicit filtration-preserving block cancellation gives a filtered homotopy equivalence. Therefore the natural quotient preserves formal cohomology and the successive t-adic Bockstein cohomology pages and differentials for this exact Q+tT_a family, with their natural identifications. This does not assert equality of the raw associated-graded vector spaces or equivalence of the entire three-vertex pencil.

The exceptional mixed direction is included: its full three-space quotient has dimensions **(32,42,28)**, whereas the other non-V directions have **(32,36,28)**. The larger middle space does not change the two-term cancellation. No radical slope or actual parameter is selected.

### The pure-V direction is not an equivalent cancellation

For pure V, the image endpoints are D and P. Equivariance forces Q:D → P to be zero. Compatibility then identifies I2 with the actual D in ker Q and im Q with ker j4. The genuine quotient has dimensions **(36,48,33)**, invariant rank 29, kernel A+P and cokernel P.

Its natural kernel map kills D and has image A. It is therefore not an isomorphism even on initial cohomology, so the acyclic cancellation and preserved-Bockstein conclusion must **not** be transferred to this branch. This is a different conditional quotient, not an exclusion of pure V.

### Verification and limits of the quotient reduction

The pinned quotient proof SHA256 is

    d86b7ebf11aa7684a522f408a641b2a0d74c239d521ef9bf829815ae58551fb4

Its 981 supporting checks pass in ordinary and optimized Python modes. They cover immutable inputs, all three rank strata, constituentwise forced invertibility, formal-series cancellation and homotopy identities in universal synthetic models, and a pure-V negative control. The independent mathematical review checks the actual induced images and the filtered cancellation; neither verification route evaluates a selected actual HM instance or formalizes the entire geometric ancestry.

If J_Q=0, this theorem supplies no radical-image quotient. If J_Q is a line, the theorem describes alternatives without identifying which occurs. The preserved obstruction problem is specifically the displayed two-term negative deformation Q+tT_a; no equivalence with a different geometric higher gate or general smooth-quadric obstruction is asserted. No full-module or horizontal splitting is obtained. **Four catalogue pairs and three labels remain.**

## Evidence and boundaries

The pinned proof SHA256 is

    5cf4b0e0a14d5c072252ec55b5e308693bd5446b630baa96c7ed8fe56c077102

The recorded independent review authenticated all seven immutable source files, checked the actual-map reconstruction and radical orientation, the unique-A and annihilator saturations, and the precise first-correction comparison. Independent ordinary and optimized Python runs each passed **468 explicit supporting checks** with identical outputs. These finite rational, character and formal-identity diagnostics support the universal written argument; they do not prove the imported geometric nonvanishing theorem or constitute proof-assistant verification.

The possible compatible radical line is not identified or excluded. No actual HM coefficient, parameter, point, tensor, matrix or instance rank is selected or evaluated. Scalarity, source realization, remaining mixed multiplication constraints and complete proof repair remain unresolved.

The [four-pair certificate in PR942](https://github.com/Akilleez-QA/read-em-and-weep/blob/3cd8a620e7268cf86fb8cc019d35f04d3cb6b448/research/proof-repair-campaign/four-pair-composition/README.md) and all dated progress figures remain unchanged. The separate opposite-pencil result is recorded in [chapter37](37-compatibility-and-torsion.md).
