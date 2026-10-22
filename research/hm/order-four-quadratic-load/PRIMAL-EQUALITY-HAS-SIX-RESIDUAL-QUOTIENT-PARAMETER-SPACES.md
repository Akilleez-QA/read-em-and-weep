# Primal equality has six residual quotient parameter spaces

## Result and scope

For the three primal equality labels retained in PR733 (commit3349988b5c3fc82dbca0741fc1b5fe70af1c7d0d), the forced osculating bundle

    C=(P+D) tensor O(-2) subset E

is an equivariant direct summand as a bundle. There are exactly six remaining formal splitting types for Z=E/C, each of rank8 and degree-36. The actual quotient E -> A induces a surjection

    Z -> R=O(2)+O(-8).

For each of the six types, all equivariant morphisms to R form an explicit three- or four-dimensional vector space, and surjectivity has the exact scalar conditions below. All six loci are nonempty. This is a sharp residual bundle-and-quotient reduction, not a label exclusion, a realization statement, or a construction of a connection on Z.

The three labels are G3.11.942927348917, G3.12.8e9af2d08af9, and G3.21.45ca6278cbfc. Their primal A is O(6)+O(2)+O(-8).

## 1. Direct summand and the six residual types

The actual input H0(E(1))=0 gives top E<=-2. Every morphism O(-2) -> O(-j) with j>2 is zero. Therefore C maps entirely into the degree-2 top block R2 tensor O(-2) of E. Its coefficient embedding P+D -> R2 splits by finite-group semisimplicity. Consequently E=C direct sum Z equivariantly as bundles; no connection splitting is asserted.

The strict-top-slope theorem gives H0(K(2))=0 for K=E^-. Thus E -> A induces an injection

    H0(E(2)) -> H0(A(2))=Sym^8 W + Sym^4 W=P+2D.

Together with the inclusion P+D -> H0(E(2)), this forces H0(E(2)) to be P+D or P+2D.

Apply the already proved 28-type parametrization from ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md. In its variables (a,b,c,d,e,f,g,h), the conditions are

    a+d+g+h=1,
    b+c+d+e+f+2g+h=3,
    c+g+h-1=0,
    d+e+g+h=1,
    f+g in {1,2}.

They have exactly six nonnegative solutions. Subtracting the forced C gives:

1. Z1=D O(-2) + 2 O(-8) + O(-10).
2. Z2=T O(-3) + O(-8) + O(-10).
3. Z3=D O(-2) + O(-8) + W O(-9).
4. Z4=T O(-3) + W O(-9).
5. Z5=(V+P) O(-4) + O(-8).
6. Z6=Wp O(-3) + V O(-4) + Wp O(-5) + O(-8).

These six types are exhaustive under the specified necessary inputs, but none is asserted to occur for the actual source map.

## 2. The induced quotient is an ordinary quotient, not a descended connection

For the complete degree10 rational-normal system forced by PR733, C is its eighth osculating bundle. Its seventh osculating bundle is

    C7=(Wp+T) O(-3).

The equality-chain leading symbol identifies C/C7=O(6) with the top line of A. Indeed C7 lies in K, and the next graded derivative is a nowhere-zero map to that O(6). A map from O(6) to either lower summand of A is zero, so the image is exactly its top line, not a graph into the lower summands. Thus

    C intersect K=C7,
    0 -> K/C7 -> Z -> O(2)+O(-8) -> 0.

Here K/C7 has rank6 and degree-30. Also top K<=-3, so C7 lies in K's top HN block and is an equivariant bundle direct summand of K. This last statement still does not endow either quotient with a connection. Only the original ambient derivative was used to identify C7 and the image of C.

## 3. A low-degree covariant has no common zero

For the A5 action on P1, a point stabilizer is cyclic (its action on the tangent line is faithful). Cyclic subgroups have order at most5; consequently every orbit has at least12 points.

A nonzero equivariant covariant U O(-j) -> O(t), represented by binary forms of degree m=t+j<12, has an invariant common-zero divisor of degree at most m. Such a nonempty divisor cannot exist. The map is therefore a surjection. This applies to all irreducible covariants of degrees1,4,5,6,7,11 appearing below. A map O(-10) -> O(2), in contrast, is a degree12 scalar section and necessarily vanishes somewhere.

The needed multiplicities follow from

    Sym1=W; Sym4=D; Sym5=T; Sym6=V+P;
    Sym7=Wp+T; Sym10=A+V+D;
    Sym11=W+S+T; Sym12=1+A+P+D.

Every displayed constituent has multiplicity one. Hence each named component below has a single scalar coefficient after choosing any nonzero generator of its one-dimensional Hom space.

## 4. Exact morphism spaces and surjectivity conditions

Write the two rows as maps to O(2), then to O(-8). Components not listed are zero. Distinct copies of O(-8) in Z1 have separately chosen coordinates.

- Z1: upper row alpha on D O(-2), beta on O(-10); lower row a,b on 2 O(-8). Dimension4. Surjective exactly when alpha!=0 and (a,b)!=(0,0).
- Z2: upper row alpha on T O(-3), beta on O(-10); lower row a on O(-8). Dimension3. Surjective exactly when alpha*a!=0.
- Z3: upper row alpha on D O(-2), beta on W O(-9); lower row a on O(-8), b on W O(-9). Dimension4. Surjective exactly when (a,b)!=(0,0) and either alpha!=0 or a*beta!=0.
- Z4: upper row alpha on T O(-3), beta on W O(-9); lower row b on W O(-9). Dimension3. Surjective exactly when alpha*b!=0.
- Z5: upper row alpha on V O(-4), beta on P O(-4); lower row a on O(-8). Dimension3. Surjective exactly when a!=0 and (alpha,beta)!=(0,0).
- Z6: upper row alpha on V O(-4), beta on Wp O(-5); lower row a on O(-8). Dimension3. Surjective exactly when a!=0 and (alpha,beta)!=(0,0). The Wp O(-3) summand is annihilated by every such quotient.

For sufficiency, the nonzero upper covariant specified by these conditions is surjective by Section3 and is supported independently of a surjective lower component; elementary row elimination proves fiberwise rank2. For Z3 when alpha=0 and a*beta!=0, the O(-8) component provides the independent lower direction and the W covariant provides the upper direction.

For necessity, a zero lower row always fails. In Z1 or Z2 with alpha=0, the only possible upper component is a scalar section of degree12 and has a zero. In Z3 with alpha=a=0, or Z4 with alpha=0, the entire rank2 quotient factors through W O(-9). The determinant of a map from that rank2 bundle to O(2)+O(-8) has degree12, and cannot be nowhere zero, even if it is nonzero generically. The remaining failures are identically zero upper rows. These arguments cover all scalars, not sampled coefficients.

Each admissible set is a nonempty Zariski-open subset of its Hom space (before quotienting by automorphisms). The table parameterizes ordinary equivariant quotient maps exactly. It does not solve their compatibility with the full Gauss flag, the fixed source presentation, or the actual constant connection.

## Reproduction

Run verify_primal_equality_six_residual_quotients.py. It pins PR733's local note/certificate and the source and strict-slope notes; independently enumerates the 28 types and the six retained types; verifies all ranks/degrees, the symmetric-power character table, every Hom component and dimension, and nonemptiness of each stated support condition. The invariant-divisor and determinant arguments above prove the uniform surjectivity criteria. There are no actual-instance evaluations, numerical rank tests, or external writes.
