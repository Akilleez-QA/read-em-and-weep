# Independent mathematical review

Reviewed proof SHA-256: a5e29660b6f0cb23c8d0597a730dbe2c2fad78a905f0abb0c0bb6693c74ca5ef.

Verdict: PASS relative to the pinned PR458, PR449 and PR451 inputs. This is mathematical review, not formal machine verification or a selected-instance calculation.

## Checked deductions

1. Polynomial multiplication defines a morphism between the stated projective spaces because a product of nonzero polynomials is nonzero. The factor incidence is closed and projective. Unique factorization gives finitely many projective degree-two/degree-three factorizations of a fixed nonzero quintic, so its dimension and the dimension of its quadratic projection are at most five. Projectivity makes the projection closed. Restriction of W is injective exactly when no nonzero member is divisible by u.

2. The four conditions on u define nonempty open subsets of the same irreducible projective space. The bad factor projection and primary failure cone are proper. For a line, restriction S2 to its three-dimensional quadratic section space is onto, so line containment has codimension three. A finite union of these proper closed loci cannot fill P14. Smooth quadrics in P4 are integral; this is used later for products and global coprimality.

3. On the smooth quadric, the divisor of a nonzero section has finitely many prime components with finite multiplicities. A factor's divisor is a sub-divisor, giving finitely many possibilities. Sections of the same line bundle with equal divisors have ratio a global unit: smoothness implies normality, so a rational function without codimension-one poles extends regularly, and the same applies to its inverse. On an integral projective variety over C that unit is constant. Thus projective factorization fibers are finite. No factoriality of the homogeneous coordinate ring is required.

4. Hypersurface restriction gives dimensions 14 and 30 for A2 and A3, and surjectivity in the needed degrees. Hence the cubic factor projection in P29 has dimension at most five. Restricting and lifting factorizations identifies this factor condition with a nonzero intersection W∩(u,v)5, away from the cubic projection center. A nonzero restricted h cannot disappear because W restricts injectively.

5. The linear restriction S3 to A3 has a five-dimensional kernel. The inverse image of an affine cone of dimension at most six therefore has dimension at most eleven; projectivization has dimension at most ten in P34. The center is correctly included, and the empty-incidence case is harmless. Outside this cone u does not divide v; irreducibility of u then gives gcd(u,v)=1.

6. The exact kernel statement in PR458 gives injection of the simultaneous interpolation space into the quintic intersection because u contains no component line, so k=0 for every v. Consequently zero quintic intersection kills the residual quotient without requiring avoidance of all intersection points on C. PR449's uM1=M3 supplies primary coverage, so the full quotient vanishes. The proof correctly claims containment, not equality, of the full exceptional locus in the factor cone.

7. Surjectivity of the finite-dimensional multiplication family is a Zariski-open condition on parameter charts and is unaffected by rescaling u or v. The constructed nonempty set therefore proves a dense open vanishing locus in the full independent coefficient product. The optional avoidance condition is also a nonempty open: the noncontained line restrictions cut a finite length-fifty scheme, and finitely many pointwise nonvanishing conditions exclude proper hyperplanes. This is compatible with the complement of the exceptional cone.

## Scope

The proof does not establish that the original fixed pair, or any restricted actual-source family, meets the open locus. The PR451 geometric consequence is explicitly conditional on its realization hypotheses. No order-four vanishing or optimality, actual-source membership, six pure conditions, higher-order module lifting, or algebraicity follows. The review inspected the use of the pinned prior results and the new incidence argument; it does not re-prove every prerequisite.
