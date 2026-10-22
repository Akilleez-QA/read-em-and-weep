# Exact twelve-orbit cokernel characters

This complements TWO-TWO-SYMMETRIC-QUOTIENT-DEFECT-IS-ZERO-OR-TWELVE.md without changing its 35-pair list or asserting realization. For each of its seven defect-twelve pairs, the actual cokernel of A -> B*(-2), if the pair occurs, is uniquely isomorphic as an equivariant sheaf to O_D(2) or O_D(6), where D is the reduced twelve-point orbit. The exponent is understood modulo 10 on D.

The stabilizer of a point of D is cyclic of order 10. Equivariant line bundles on that transitive reduced orbit correspond to its ten characters. Since A and B*(-2) are center-even, only the five even characters occur. The standard O(1) stabilizer character is primitive, so their sheaves are exactly O_D(s) for s=0,2,4,6,8. This is a classification of sheaves on the reduced orbit, not a splitting assertion for an extension over P1.

The invariant degree 12 equation of D gives

    chi_G(O_D(s+t)) = chi_G(O(s+t)) - chi_G(O(s+t-12)).

The exact sequence 0 -> A -> B*(-2) -> C -> 0 therefore forces this expression to equal chi_G(B*(-2+t))-chi_G(A(t)). Testing t=0,...,9 determines precisely one of the five characters for every surviving pair. All 259 compatible source/target records pass, so this refinement excludes no additional pair. It identifies the previously unspecified exact equivariant cokernel.

Run python3 verify_two_two_twelve_orbit_torsion_characters.py. Only formal character arithmetic is used. The finite twist window suffices here because the five candidate sheaves are exhaustively classified first, and each pair is distinguished by these checks.

Each line below lists A; B; the unique residue s.

- [[-10, 'one'], [-8, 'one'], [16, 'one']]; [[-18, 'one'], [-4, 'one'], [6, 'one']]; 2.
- [[-8, 'one'], [2, 'one'], [4, 'one']]; [[-18, 'one'], [-4, 'one'], [6, 'one']]; 6.
- [[-8, 'one'], [3, 'W']]; [[-11, 'Wp'], [6, 'one']]; 6.
- [[-8, 'one'], [3, 'Wp']]; [[-11, 'Wp'], [6, 'one']]; 2.
- [[-8, 'one'], [4, 'one'], [6, 'one']]; [[-18, 'one'], [-8, 'one'], [6, 'one']]; 6.
- [[-8, 'one'], [5, 'W']]; [[-18, 'one'], [-8, 'one'], [6, 'one']]; 6.
- [[-9, 'W'], [16, 'one']]; [[-18, 'one'], [-4, 'one'], [6, 'one']]; 2.
