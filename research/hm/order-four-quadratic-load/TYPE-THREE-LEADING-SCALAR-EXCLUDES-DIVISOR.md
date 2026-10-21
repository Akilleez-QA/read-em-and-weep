# Type III: nonzero leading scalar excludes divisorial torsion

This is an extension of THREE-TARGET-TYPES-WITHOUT-OFF-DIAGONAL-TORSION.md, not a change to its unconditional three-type result. Work over characteristic zero with the actual equivariant pure map j:S7* -> K8 and its three-coupling section T2 in H0(F4 external-tensor O(6)). The actual leading diagonal scalar lambda is not evaluated here.

## New conditional exclusion

Suppose F4 = V tensor O(4) direct-sum O(12) (type III). Write T2=(L,H) in these two summands. Universal character arithmetic gives coupling-space dimensions 2 and 1, respectively, and diagonal invariant dimensions

- dim H0(V tensor O(10))^G = 1;
- dim H0(O(18))^G = 0.

Consequently lambda nonzero implies L nonzero: the high component has identically zero diagonal restriction.

The preceding divisor theorem shows that any nonempty common-zero divisor away from the diagonal must have bidegree (9,3) in this type. Divisibility by its defining section would put L in H0(V tensor O(4-9) external-tensor O(6-3)), which is zero. Thus such a divisor forces L=0, contradicting lambda nonzero.

Therefore type III and lambda nonzero imply no off-diagonal divisorial common zeros, and hence no off-discriminant divisorial torsion in Q6=coker(j). The actual Hermite computation in the preceding proof, also checked by verify_pure_hermite_boundary.py, shows lambda nonzero implies generic fiber injectivity of j on the discriminant. Thus Q6 has no divisorial torsion anywhere. The rank-two alternative would require a nonzero divisorial quotient of S5*, of degree d-4 at least 2, supported in Q6. It is impossible. The actual residual map therefore has generic rank four under these two hypotheses.

Combined with the preceding proof, lambda nonzero gives generic rank four in types I, II, III, and V. Neither the actual type nor lambda is determined. No conclusion is asserted for types IV, VI, or VII.

## Defining-biform existence does not further prune the list

For every remaining necessary divisor bidegree (p,q), p+q is 12, 20, or 24. The diagonal restriction

H0(O(p,q)) -> H0(O(p+q))

is the multiplication map Sym^p W tensor Sym^q W -> Sym^(p+q) W and is surjective. In characteristic zero, taking finite-group invariants preserves surjectivity. The target invariant space has dimension one at each of these three degrees. Hence each remaining candidate admits an invariant defining biform with nonzero diagonal restriction, meaning it is not divisible by the diagonal equation.

This is an exact limitation of that proposed pruning test: the existence of an invariant defining biform alone excludes none of the remaining bidegrees. It does not say that such a biform divides the actual T2. The missing datum is compatibility between an invariant defining biform and the actual three-coupling section, not existence of the biform. No actual coefficient or rank has been computed.

Reproduction: python verify_type_three_scalar_divisor.py. Its character arithmetic is exact over Q(sqrt(5)); it prints both defining and residual invariant dimensions for each candidate. It imports the stable universal character verifier only. The Hermite verifier is supporting verification, not counted as the new deduction here.
