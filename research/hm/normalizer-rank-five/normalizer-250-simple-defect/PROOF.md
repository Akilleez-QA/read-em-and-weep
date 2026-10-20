# No length-one isolated defect on a 250-point orbit

## Result and scope

Let G=A⋊K, A=F5² and K=SL2(F5), be the standard projective Schrödinger normalizer on P(V), dim V=5. Let N=H5⋊K⊂SL(V) be its stipulated determinant-one lift. For an N-equivariant rank-two reflexive sheaf B with equivariantly trivial determinant and isolated singularities, put T=Ext²(B,O).

If a point p in Supp(T) belongs to a G-orbit of size 250, then length(T_p)≥2. Consequently such an orbit contributes at least 500 to length(T), and total length 250 is impossible.

More generally, using the established 250-point gap, every nonzero T of total length strictly below 300 has support equal to the canonical 30-point orbit. Thus its length is 30m with 1≤m≤9; the already-established canonical length-one obstruction removes m=1. The noncanonical 250-point orbit exists and is unique, so the previously proved 250-point orbit gap is sharp. Every orbit other than this orbit and the canonical 30-point orbit has at least 300 points. No assertion about canonical stalk lengths 2 through 9 or an improved universal defect lower bound is made here.

Only universal finite-group representations and the previously proved local character obstruction are used. There is no evaluation of a geometric source, model matrix, operation, selected input, rank instance, jet, or residue.

## 1. Reduction of a 250-point stabilizer

The established orbit theorem says that every noncanonical point has trivial A-stabilizer. If |G·p|=250, then S=G_p has order 12 and projects isomorphically to L≤K of order 12. It is the graph of an A-valued cocycle f on L.

The unique involution of K is c=−I: a matrix of order two in characteristic five is diagonalizable with eigenvalues ±1, and determinant one leaves only I and −I. Cauchy's theorem therefore puts c in L. Since c acts by −1 on A, the cocycle identity and centrality of c give

    2f(g)=f(c)−g f(c).

Hence f(g)=a−ga for a=f(c)/2, and S is A-conjugate to L. A lift of this conjugating element to H5 also conjugates the corresponding linear action in N. We may therefore assume that L itself fixes p.

## 2. Every order-12 subgroup is binary dihedral

The quotient L/⟨c⟩ has order six in K/⟨c⟩≅A5. A group of order six is C6 or S3: its Sylow-three subgroup is normal, and a Sylow-two complement acts either trivially or by inversion. The cyclic case would contain an element of order six, whereas the cycle types in A5 have orders only 1,2,3,5. Thus L/⟨c⟩≅S3.

Choose an order-three element a∈L, which projects onto the subgroup of order three of S3, and choose a lift u∈L of a transposition. Since u²∈⟨c⟩ and u cannot be an involution other than c, u has order four and u²=c. The conjugate uau⁻¹ projects to a⁻¹. The two possible lifts are a⁻¹ and ca⁻¹; the second has order six, while the conjugate has order three. Thus

    a³=1,   u⁴=1,   u²=c,   uau⁻¹=a⁻¹.

The elements a,u generate L because they generate its quotient and already contain c. These relations identify L with C3⋊C4, with the C4 acting by inversion, equivalently the binary dihedral group Dic3 of order twelve.

## 3. Restricted representation and its unique stable line

Use the standard determinant-one linear complement K⊂N. The following universal character facts were established in Section 2 of ../normalizer-refined-point-gap/PROOF.md:

- For g∈K with no nonzero fixed vector on A, |tr(g|V)|²=1, by the Weyl-operator basis of End(V).
- The c-eigenspace decomposition is V=V+⊕V− with dimensions 3 and 2.
- Every order-four u∈K has spectrum {1,−1,−1,i,−i}; in particular tr(u|V+)=−1.

Here is the additional order-three calculation, without invoking a character table. The element a has no nonzero fixed vector on A. Indeed its minimal polynomial divides t³−1, which has distinct roots in characteristic five. If it had eigenvalue one, determinant one would make both eigenvalues one, forcing a=I.

Let ω be a primitive complex cube root of unity. Conjugation by u takes a to a⁻¹, so the multiplicities of ω and ω² on V agree. Writing their common multiplicity as t, the trace is 5−3t with t∈{0,1,2}. The trace identity |tr(a|V)|²=1 forces t=2. Thus the spectrum of a is

    {1,ω,ω,ω²,ω²}.

Because c is central, u preserves V+ and V−, and the same conjugation argument gives equal ω and ω² multiplicities separately on each piece. Each piece has room for at most one such pair. Since the total is two pairs, each has exactly one. Therefore

    Spec(a|V+)={1,ω,ω²},     Spec(a|V−)={ω,ω²}.

Any L-stable line carries a one-dimensional character. The inversion relation forces its a-eigenvalue to equal its inverse, and that eigenvalue also has cube one. It is consequently one. Thus every L-stable line lies in the one-dimensional a-fixed space ℓ⊂V+.

This ℓ is itself u-stable, since u normalizes ⟨a⟩, and therefore is L-stable. On the other two a-eigenspaces in V+, u exchanges the ω and ω² spaces and has trace zero. Since tr(u|V+)=−1, the eigenvalue of u on ℓ is exactly −1.

We have proved the needed precise statement: L has exactly one stable line in V, it lies in V+, and its order-four generator u acts on it by −1. This also establishes the existence and uniqueness of a 250-point orbit, as shown next.

### 3.1. Sharpness and uniqueness of the 250-point orbit

Order-12 subgroups exist: the normalizer of a Sylow-three subgroup in A5 has order six, since there are twenty 3-cycles and thus ten such subgroups; its inverse image in K has order twelve. For any such L, its unique stable line defines a point p. It cannot lie in E: a point of E has projective stabilizer of order 3000/30=100, which cannot contain a subgroup of order twelve. The established noncanonical gap therefore gives |G·p|≥250. Conversely its stabilizer contains L, so |G·p|≤3000/12=250. Equality follows.

Every subgroup of order six in A5 is the normalizer of its normal subgroup of order three, since that normalizer has order six. Sylow conjugacy shows that all such subgroups are conjugate. Every order-12 subgroup of K is the full inverse image of its order-six quotient, so all order-12 subgroups of K are conjugate as well. For any 250-point orbit, Section 1 conjugates its stabilizer by A to such an L. Section 3 then forces the point to be its unique stable line. The conjugacy just proved shows that all these points lie in the same G-orbit. Thus there is exactly one orbit of size 250.

## 4. Cotangent determinant and the local obstruction

At p=[ℓ], the tangent representation is Hom(ℓ,V/ℓ). If g∈SL(V) preserves ℓ with eigenvalue λ, then

    det(T_p P(V))(g)=λ⁻⁴ det(V/ℓ)(g)=λ⁻⁵,
    det(T_p* P(V))(g)=λ⁵.

For the actual order-four element u of the linear subgroup K⊂N, Section 3 gives λ=−1. Hence the cotangent determinant character δ satisfies δ(u)=−1.

The universal local theorem in ../../local-defect/minimal-local-defect-character/PROOF.md applies to the local N-stabilizer representation: if M=B_p has rank two, is reflexive, is free away from the closed point, and has equivariantly trivial determinant, then a length-one defect Ext²(M,R)=kχ must satisfy

    δ³=χ⁻⁴.

But u has order four in N itself, so χ(u)⁴=1 even if χ does not descend to the projective stabilizer. Evaluating gives −1=1. Thus a nonzero local defect at p cannot have length one. Conjugating back by a Heisenberg lift preserves the order-four element and its cotangent determinant, so this conclusion applies to the original p.

The isolated-singularity condition supplies the local freeness on the punctured spectrum required by that theorem. Mere finite support of Ext² without this condition is not asserted to suffice.

## 5. Total lengths strictly below 300

Equivariance makes the local lengths constant on every point orbit. A supported 250-point orbit therefore contributes at least 250·2=500.

Any noncanonical orbit is free under A, hence has size 25k, where k=[K:L] divides 120. The previously established gap gives k≥10. The only integer k with 250≤25k<300 other than k=10 is k=11, which does not divide 120. Consequently every orbit other than E and the unique 250-point orbit has at least 300 points. Section 4 excludes occurrence of the 250-point orbit in the support of T when length(T)<300.

It follows that nonzero T of length below 300 is supported precisely on the unique canonical orbit E, with constant local length m and total length 30m. Thus m≤9. The earlier canonical order-four obstruction excludes m=1; this proof does not analyze the other canonical local lengths.

In particular 250 is not a multiple of 30 and is impossible. Among total lengths 250 through 299, the sole arithmetic candidate left by this argument is 270. If length(T)=5q, the corresponding necessary condition is

    0<q<60  ⇒  q∈{12,18,24,30,36,42,48,54}.

These are necessary conditions only, and should be combined with separately verified stronger canonical-stalk restrictions when available.

## Inputs and evidence boundary

Inputs are ../normalizer-refined-point-gap/PROOF.md (the 250-point gap, cocycle reduction, and universal character facts), ../normalizer-minimal-point-orbit/PROOF.md (the unique canonical orbit and free-A reduction), and ../../local-defect/minimal-local-defect-character/PROOF.md (the isolated rank-two length-one obstruction and the stipulated SL5 lift). No subgroup search, character-table database, large computation, source-app write, installation, or upstream change was used. The only write is this local proof artifact.
