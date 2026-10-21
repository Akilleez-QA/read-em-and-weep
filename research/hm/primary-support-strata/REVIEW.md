# Independent mathematical review

Reviewed proof: `PROOF.md`, SHA256 `97a1a3cbbe8ffd204ba99bf33c4170c87ee3c74f9864e49ec6f38cdf977a7352`.

Conclusion: the stated deductions are correct relative to the pinned actual exterior model, no-full-fiber theorem, generic-rank theorem, and representation-theoretic invariant input. No mathematical correction is required.

## Checks

1. **Universal dimension formula and classification.** The off-diagonal traceless operators span `B direct-sum A`; adding the diagonal operator contributes `4-d`. Thus `dim Y=a+b+4-d`. For the quotient image of L, both projections are surjective, so `t>=max(p,q)`. If the deficit is at least two, then p,q are at least two. With support dimension at most five this forces c at most one. For c=0, d=0 and the deficit is at most one; for c=1, p=q=2 and d=2, giving precisely the prohibited full fiber. Hence the deficit is at most one. The lower bound six from PR550 gives the exact listed alternatives, including the equivalence of support dimension three with evaluation rank six.

2. **Intrinsic bundle and fibers.** On the projective space of lines in A0, the star bundle is `O(-1) tensor Q`, not Q alone. W-contraction gives `E=Q(-1) tensor W* -> V tensor O`. The presentation `0 -> 2O(-2) -> 10O(-1) -> E -> 0` is exact. Its quotient is locally free, so the 5-by-10 linear presentation and the rank-eight source map have the same fiber ranks. The proof correctly uses the image of each fiber map rather than the fiber of its image sheaf.

3. **Chern obstruction.** The degree-four coefficient of `(1-h)^10/(1-2h)^2` is `210-480+540-320+80=30`. Everywhere-surjectivity would give a rank-three vector-bundle kernel with this nonzero fourth Chern class, a contradiction. No generic smoothness or expected-codimension hypothesis enters this existence argument.

4. **Strata and schemes.** The classification proves equality of the underlying closed sets for rank-at-most-eight evaluation and support rank at most four, and likewise for rank six and support rank at most three. Equality of radical ideal sheaves follows over C. The proof does not incorrectly identify the original determinantal scheme structures.

5. **Divisorial exclusion.** The linear presentation is equivariant, so its nonzero maximal minors span an invariant space of quintics. Their gcd spans a character, trivial by the pinned perfectness input. The absence of positive-degree invariants through degree five therefore rules out a nonconstant gcd and every divisorial common-zero component. The cited Section 2 at commit `8d24a12c4af9c922db2052a360c96a053dcba5b8` was fetched and checked: central weight restricts possible degrees to five, and the degree-five invariant space for the Heisenberg subgroup is `U direct-sum U'`, without a normalizer-fixed vector. This proves dimension at most two, not finiteness.

6. **Conditional length.** For the dual map `5O -> E*`, failure of injectivity has expected codimension `(5-4)(8-4)=4`. Under this hypothesis the maximal-minor Porteous class is `c4(E*)=30h^4`. Thus length thirty is correct only in the explicitly conditional expected-codimension case. Neither reducedness nor an orbit description follows.

The exterior and no-full-fiber dependency at `7bf725bcd857a2deb975f9ecb80fca32e7833ae0` and the universal four-plane lemma at `edd49e0e6b15ae1bb41e51e5cd9f46f418e05f6f` were also fetched and checked. Their use matches the stated representations and hypotheses.

This is an independent structural mathematical review, not proof-assistant verification. No selected HM coefficient, matrix, source instance, numerical rank, or large computation was used. The full adjoint multiplication, original fixed pair, Q4, higher lifting, and algebraicity remain outside these conclusions.
