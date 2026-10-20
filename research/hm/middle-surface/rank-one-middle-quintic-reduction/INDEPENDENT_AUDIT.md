# Independent audit: rank-one surface defect and quintic reduction

## Verdict

The local multiplicity bound is correct. The global reduced-degree bound, degree-five conclusion, irreducibility argument, and equality normal form in PROOF.md are correct under the explicit hypotheses below. No operation or source evaluation is used.

## Exact hypotheses and dependencies

1. The ambient variety is P^4 over a characteristic-zero field (the given complex setting suffices).
2. There is an exact sequence 0 -> G -> O^20 -> R -> 0 with G locally free of rank 14 and R torsion-free of rank 6.
3. At a codimension-two point where the normal quadratic map Q has residue-field rank r, the presentation matrix G -> O^20 has residue-field rank 4+r. This is the rank-four repeated-input cancellation hypothesis. Equivalently, after canceling units its minimal presentation has sizes (10-r) -> (16-r).
4. The effective codimension-two cycle of S=Ext^1(R,O) has degree delta <=70. This audit uses that established global bound as an input; it does not independently reprove the positivity and zero-c2 splitting results imported in rank-ten-fitting-strata/ADDENDUM.md.
5. For degree divisibility, the reduced union in question is invariant under H5 acting on P^4 through its standard five-dimensional representation; the central order-five element acts on O(1) by a primitive fifth root. Characteristic zero ensures the representation dimension property used below.
6. Irreducibility additionally requires invariance under the full stipulated normalizer N, whose conjugation action on H5/Z is the standard SL2(F5) action.
7. To call the resulting surface generically rank exactly one rather than rank at most one, import the independent exclusion of residual rank zero, or explicitly assume generic residual rank one.

## Local proof, with all modules accounted for

Let A=O_(P4,eta) at a generic surface point, with maximal ideal m=(x,y) and residue field k. This is a regular local ring of dimension two. A torsion-free finite A-module R has depth at least one and projective dimension at most one. Its double dual is reflexive, hence free over this regular local surface ring, of rank six. The quotient T=R**/R has finite length because R is free at every height-one point.

The injection A^14 -> A^20 cancels exactly 4+r units, since its residue-field rank is 4+r. The remaining presentation

    0 -> A^j -> A^(j+6) -> R -> 0,  j=10-r,

is minimal. Dualizing gives S=coker(A^(j+6) -> A^j). The remaining matrix entries lie in m, so mu(S)=j. This conclusion does not require the entire dual free resolution to be minimal.

Applying Hom(-,A) to 0 -> R -> A^6 -> T -> 0 gives

    Ext^1(R,A) = Ext^2(T,A).

The right side is the finite-length duality functor over a regular local ring of dimension two. Consequently length(S)=length(T), and dim_k Soc(S)=mu(T)<=6. Over a noncomplete ring these numerical assertions can be checked after faithfully flat completion; no algebraically closed residue field is required.

The A-linear map S -> (mS)^2, s |-> (xs,ys), has kernel Soc(S). If L=length(S), then length(mS)=L-j, and therefore

    dim_k Soc(S) >= L-2(L-j)=2j-L.

Thus L>=2j-6, and also L>=j. At r=1, j=9 and L>=12. At r=0, j=10 and L>=14. This proof avoids any coefficient-field choice.

## Global cycle and degree

At every generic surface point, the coefficient of that surface in [S]_2 is its localized module length L. Since every other coefficient is nonnegative, the reduced union Y of all surface components of rank(Q)<=1 satisfies

    12 degree(Y) <= degree([S]_2)=delta <=70.

This proves degree(Y)<=5 when Y is nonempty. It does not bound the degree of the nonreduced scheme defined by minors, and does not identify its scheme multiplicities with the lengths L. The cycle [S]_2 itself is the weighted cycle to which the argument applies.

For a reduced invariant surface Y, the central character on H^0(Y,O_Y(n)) is nontrivial whenever 5 does not divide n. Every representation of H5 with that nontrivial central character has dimension divisible by five. For sufficiently large consecutive n,n+1,n+2 with n=1 modulo 5, all three Hilbert polynomial values are divisible by five. Their second finite difference is degree(Y), proving 5 divides degree(Y). Hence nonempty Y has degree exactly five and contributes at least 60 to delta.

For each H5 orbit of components the same argument applies to its reduced union. Each such union has positive degree divisible by five, so there is one orbit. Its size divides 25 because the center acts trivially on P4. Degree five allows only one integral quintic component or five degree-one planes. In the latter case H5/Z acts transitively on five planes. The kernel is a line in F5^2. N-invariance of the five-plane set forces this kernel line to be SL2(F5)-invariant, which is impossible. Under full N-equivariance Y is therefore integral. Its coefficient m in [S]_2 satisfies 12<=m<=14, yielding contribution 60,65, or70.

## Equality and sharpness

At generic residual rank one, L=12 forces mu(T)=6 and Soc(T) dimension nine. The rank argument yields dim(xT)=dim(yT)=3, xT intersect yT=0, and ker(x)=ker(y)=Soc(T). Commutativity then forces m^2 T=0. Over the completed equicharacteristic ring, choosing a coefficient field and bases gives

    T = (A/m^2)^3 direct sum k^3.

This is a valid noncanonical abstract module classification in the equality case, not an equivariant splitting. Conversely this T has length 12, mu(T)=6 and socle dimension 9. Its kernel in A^6 is (m^2)^3 direct sum m^3, with minimal generators 15 and minimal relations 9, so the local lower bound is genuinely sharp for abstract rank-six torsion-free modules. This example does not construct the stipulated global geometric object.

## Hilbert constraints

The same representation argument, using the three nonzero residues 1,2,3 and the invertibility of 2 modulo 5, forces every integer-binomial coefficient of the quadratic Hilbert polynomial to be divisible by five. For

    P_Y(t)=5 binom(t,2)+(6-g)t+chi(O_Y),

this gives g=1 modulo5 and chi(O_Y)=0 modulo5. It does not assert normality, smoothness, or any identification of chi with that of the normalization.

## Scope

The theorem is conditional on the established generic-rank-ten setup and imported global defect budget. It gives a necessary geometric and multiplicity constraint, not existence or exclusion of the remaining integral quintic. The no-quintic-divisor result is not being applied to a codimension-two surface.
