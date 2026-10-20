# Residual rank one is globally impossible

## Assumptions and result

Work over C with the established source/equivariance and bundle hypotheses of /research/hm/middle-surface/independent-dimension-six/PROOF.md. In particular retain its independently proved finiteness of Z2={rank Q<=2}, the standard projective Heisenberg normalizer N=A semidirect SL2(F5), A=F5^2, and the fixed outer-symmetric cyclic-zero operation with repeated-input injectivity.

Then Z1={rank Q<=1} is EMPTY. Thus the residual rank is at least two at every middle point. This is a global structural exclusion, not a selected rank evaluation. It does not assert full residual rank ten everywhere.

## 1. A finite support bound

The global linear matrix b:O(-1)^15 -> O^20 has rank b=4+rank Q. Its degree-seven minors have finite base support Z2. Four suitable linear combinations form a zero-dimensional complete intersection of degree7^4=2401. At every point of Z1 the matrix has rank at most five, so all seven-minors lie in the square of the local maximal ideal. A parameter ideal of four such equations in a regular local ring of dimension four has colength at least2^4=16.

Consequently |Z1,red|<=floor(2401/16)=150. These constructions and multiplicity details are in /research/hm/normalizer-rank-five/small-normalizer-point-orbits/PROOF.md, Section6. The bound concerns distinct support points; no equation identifies the length of Z1 itself with this complete-intersection length.

## 2. The only possible orbit is excluded

The abstract orbit theorem in /research/hm/normalizer-rank-five/small-normalizer-point-orbits/PROOF.md proves that the only N-point orbit of size at most150 is the canonical orbit E of thirty Heisenberg eigenpoints. Therefore the invariant finite support Z1,red is either empty or E.

The independently audited /research/hm/normalizer-rank-five/heisenberg-eigenpoint-rank-parity/PROOF.md proves that every point of E has residual rank in {4,6,8,10}. Its diagonal-subgroup characters split the ten quadratic monomials into orbits of sizes4,4,2; the correction has no matching linear characters, and repeated-input injectivity forces the four-dimensional square module to survive. Thus none of E belongs to Z1. This proves Z1 empty. The combined independent audit is AUDIT.md here.

## 3. Uniform independent-zero fiber bound

The previous pointwise bounds now give separately projectivized independent-zero fiber dimension at most two at EVERY middle point. For residual ranks2,3,4,5 use the universal K8, K7, K6 and K5 proofs cited in /research/hm/middle-surface/independent-dimension-six/PROOF.md. Rank6 has pointwise bound two by /research/hm/middle-surface/rank-six-surface-reduction/COROLLARY.md, Section1. For ranks>=7 the kernel-parameter bound9-r in ../rank-nine-independent-incidence/PROOF.md is at most two; rankten has no independent zeros. The rankone fiber-three possibility is now absent globally.

The previously proved global affine independent-zero bound six remains valid. Its unique seven-dimensional all-three-nonzero diagonal component is unchanged. The new result removes rankone as a possible source of an independent dimension-six component; it does not exclude dimension-six components at other residual ranks.

## 4. Next restriction: any rank-two points are numerous and outside the canonical orbit

Z2 remains finite, and E is disjoint from Z3 by the stronger eigenpoint rank bound. Thus every point of Z2 has trivial A-stabilizer, since E is exactly the set of points with nontrivial A-stabilizer.

The same degree-seven complete intersection contains Z2, so |Z2,red|<=2401. Free A-orbits have25 points, hence |Z2,red| is a multiple of25, giving |Z2,red|<=2400.

If Z2 is nonempty, each of its N-orbits has size25m, with m the index of a subgroup S of SL2(F5). The small-orbit theorem excludes m<=6. Index7 and index9 do not divide120. Index8 would give |S|=15. Such an odd-order S injects into A5, but an order15 subgroup there cannot exist: its Sylow-five subgroup would be normal (its number divides3 and is1 modulo5), forcing the subgroup into the order10 normalizer of that Sylow-five subgroup. Thus m>=10 and every such orbit has at least250 points.

We obtain the necessary alternative

    Z2 is empty, or 250 <= |Z2,red| <= 2400,
    with |Z2,red| divisible by25.

This is only a support-cardinality restriction. It does not prove existence, reducedness, or emptiness of Z2, and does not claim that every integer in the interval can occur. The lower-bound argument uses subgroup indices, not an assumption that orbit size250 is attained.

## Scope

The abstract parity argument and point-orbit theorem contain no source-map evaluations. Finiteness of Z2, and therefore the global rankone exclusion, retains the full hypotheses of the preceding geometric chain. These results concern algebraic rank strata and reduced supports; they establish no new first-order integrability, higher-order lifting, or actual obstruction values.
