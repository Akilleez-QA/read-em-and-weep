# The alternating transfer has the same small-branch scalar

**Craig Ward · 23 October 2026 · PR1071**

[Immutable full proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/ad1653dd81f23d604bbd99820897c6145e1993c8/research/hm/source2-pure-v-alternating-normalization/PROOF.md).

## Later refinement through PR1075

PR1075 now proves γ≠0 in endpoint nine, so the diagonal, full mixed transfer and alternating transfer below are all nonzero there. The normalization theorem and its zero equivalences remain valid; its own nonvanishing boundary was historical. [Full theorem](105-nonzero-small-transfer.md).

In the pinned complex-bilinear adjoint and Hamiltonian conventions, for formal negative quadratics a,b and bracket [a,b]=a_x b_y−a_y b_x,

    ρ_D(a)L_b*−ρ_D(b)L_a*=−2L_[a,b]*.

This is an exact normalization, not an unspecified nonzero scalar. It follows on the entire sextic space from the unnormalized transvectant identity

    (a,(b,f)₂)₁−(b,(a,f)₂)₁=−2((a,b)₁,f)₂.

The full multiplication adjoint is (b,f)₂/60. To pass to P, f must be the pinned included sextic E(p), not quotient coordinates treated as monomial coefficients. Both sides receive the same adjoint factor, leaving −2 unchanged. No Hermitian conjugation is used.

In endpoint nine, the already proved factorization B(a,b)=γρ_D(a)L_b* therefore gives

    B(a,b)−B(b,a)=−2γL_[a,b]*,
    Alt(B)(a,b)=−γL_[a,b]*,
    B(a,b)=[R(a+b)−R(a)−R(b)]/2−γL_[a,b]*.

Alt includes the factor one-half. The alternating coefficient is fixed by the same γ as the diagonal, not an independent parameter. Since R₁ and the bracket-adjoint family are nonzero,

    R≡0 ⇔ γ=0 ⇔ B≡0 ⇔ Alt(B)≡0.

These are whole-family identities; a zero at one direction does not imply them. The ambient two symmetric plus one alternating channels remain, but only the small-branch factorization imposes this linkage. No such diagonal determination is asserted in endpoint sixteen, no full-pencil commutation follows, and this theorem alone neither evaluates γ nor proves it nonzero. Exact formal polynomial checks support the written normalization.
