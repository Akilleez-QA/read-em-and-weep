# An exact cohomology obstruction removes one (2,2) quotient pair

The 35-pair necessary overlist in TWO-TWO-SYMMETRIC-QUOTIENT-DEFECT-IS-ZERO-OR-TWELVE.md has one pair that cannot occur:

    A = W O(-7) + O(16),
    B = O(-18) + W O(5).

Here A is the full quotient E/E^- and B is the full dual quotient. This is the defect-zero pair A=B*(-2); there is no saturation assumption for any other pair.

Indeed every actual E splitting in the proved 28-type list satisfies

    H1(E(2)) = (c+g+h)V + (d+e+g+h)P4 + (f+g)D5.

In particular its coefficient of A3=Sym²W is zero. On the other hand

    H1(A(2)) = W tensor Sym³W = A3 + D5.

Since E -> A is a quotient of bundles on P1, the long cohomology sequence forces H1(E(2)) -> H1(A(2)) to be surjective: the following H2(E^-(2)) is zero. This is impossible as a map of semisimple G-representations. Thus A itself is impossible, without any choice of E type, quotient map, or dual type.

Consequently at most 34 of the 35 ordered quotient pairs in the earlier necessary list remain. The earlier list was explicitly an overlist, so this does not invalidate its defect-zero-or-twelve conclusion. It does not exclude (2,2), any other remaining full Gauss profile, or establish a stronger square-rank bound.

Run python3 verify_two_two_seven_w_quotient_exclusion.py. This checks the tensor identity and the absent A3 in all 28 types using exact abstract characters. The mathematical use of the exact cohomology sequence is supplied above; no actual map evaluations occur.
