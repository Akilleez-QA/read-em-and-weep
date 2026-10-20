# The HM middle ghost term is at most one trivial representation

## New theorem

Let F be the normalized Horrocks–Mumford bundle on complex projective four-space, put B=End₀(F), S=Sym X with X=H⁰O(1)=V*, and L_d=H²B(d−5). In the previously audited self-dual minimal-resolution notation, put

    e=dim Tor₂^S(L,C)₅=dim Tor₃^S(L,C)₅.

Then

    e∈{0,1}.

If e=1, both Tor spaces are the trivial representation of the classical normalizer N⊂SL(V). This is independent of the unresolved cubic, quartic and linear-third-syzygy parameters a,b,d. The previously unrestricted middle ghost multiplicity is therefore reduced to a single scalar alternative.

The proof actually needs only the existing twist-one vanishing and the resulting audited low-H¹ multiplication theorem. It does not need the newer twist-two vanishing or h¹B(2)=85. Their availability motivated re-examining the Koszul spectral sequences, but claiming them as necessary inputs would overstate the dependency.

## 1. Established geometric inputs

The following are imported, not recomputed:

1. B is self-dual by its symmetric trace pairing and N⊂SL₅, so equivariant Serre duality gives H³B(t)=H¹B(−5−t)* and H⁴B(t)=H⁰B(−5−t)*.
2. H⁰B(t)=0 for t≤0 and H¹B(t)=0 for t≤−2.
3. With T_t=H¹B(t), one has T₋₁=V, T₀=sl(V). The actual multiplication map

       X⊗T₋₁ → T₀

   is, up to equivariant identifications and nonzero scale, the traceless projection V*⊗V→(V*⊗V)/C·id. It is surjective with a one-dimensional trivial kernel.
4. L is generated in degree zero and has the self-dual Betti shape from the prior relation proofs. In internal degree five the only possible nonzero Tor groups are Tor₁,₅ and Tor₄,₅ of common dimension c, and Tor₂,₅ and Tor₃,₅ of common dimension e. Endpoint Tor groups occur only in degrees zero and ten. We will recover c=0 independently, without using the prior quintic-relation exclusion.

Input 3, including nonvanishing rather than just a representation-compatible possibility, is proved in ../quintic-scalar-propagation/PROOF.md §8. Inputs 1–2 are also recorded there. Input 4 is ../middle-module-relations/PROOF.md §5. The independent earlier proof of c=0 in ../middle-relation-dependency/PROOF.md §§4–5 is compatible with, but not necessary for, the present argument.

The underlying primary representation source is Horrocks–Mumford, A rank 2 vector bundle on P4 with 15,000 symmetries, Topology 12 (1973), 63–81, §§1–2 and appendix:
https://www.dam.brown.edu/people/mumford/alg_geom/papers/1973a--Rk2BdleP%5E4-NC.pdf

## 2. Exact coordinate Koszul complex

Consider the sheaf complex in columns −5,…,0

    K^(−i)=Λ^iX⊗B(−i),   0≤i≤5.

The homogeneous coordinates have no common zero on P⁴. Locally at least one coordinate is a unit in a trivialization, so wedging by the corresponding basis vector divided by that coordinate gives a contracting homotopy for the usual contraction differential of the local Koszul complex. Hence K is exact. Its hypercohomology is therefore zero.

The bounded hypercohomology spectral sequence has

    E₁^(−i,q)=Λ^iX⊗H^qB(−i),
    d_r:(p,q)→(p+r,q−r+1),

and converges to zero. Its d₁ maps are the usual Koszul maps induced by coordinate multiplication. For the construction and convergence used here, see Stacks Project, Lemma 13.21.3 (015J), and Section 12.25 (012X):
https://stacks.math.columbia.edu/tag/015J
https://stacks.math.columbia.edu/tag/012X

These sources justify the general machinery, not any HM-specific ranks.

## 3. All nonzero entries on the E₂ page

### Rows q=0 and q=4

The q=0 row is zero because −i≤0. The q=4 row is zero because Serre duality identifies its factors with H⁰B(i−5)*, and i−5≤0. Thus neither extreme row can supply a hidden differential.

### Row q=1

Only columns −1 and 0 can be nonzero:

    X⊗T₋₁ → T₀.

Input 3 makes this surjective with kernel C·id. Consequently the sole nonzero q=1 entry is

    E₂^(−1,1)=C,

with the trivial N-action.

### Row q=3

By Serre duality, only columns −5 and −4 can be nonzero:

    Λ⁵X⊗T₀* → Λ⁴X⊗T₋₁*.

The natural exterior pairings and det X=1 identify this map, up to a harmless Koszul sign, with the dual of the preceding q=1 map. It is injective with one-dimensional trivial cokernel. Thus the sole nonzero q=3 entry is

    E₂^(−4,3)=C.

### Row q=2

At column −i its E₁ term is Λ^iX⊗L_(5−i). This is exactly the internal-degree-five part of the usual Koszul complex computing Tor^S(L,C). Therefore

    E₂^(−i,2)=Tor_i^S(L,C)₅.

Initially Input 4 allows four entries, in columns −4,−3,−2,−1, of dimensions c,e,e,c. The slot (−1,2) has no outgoing higher differential, since its target column would be positive, and its possible incoming sources (−3,3), (−4,4) are zero. Thus Tor₁,₅ survives to E∞ and is zero. Likewise (−4,2) has no incoming higher differential within the column range; its possible outgoing targets (−2,1), (−1,0) are zero. Thus Tor₄,₅=0 independently. This recovers c=0 by a different structural proof.

Exactly two possible middle-row entries remain:

    E₂^(−3,2)=C^e,    E₂^(−2,2)=C^e.

Here C^e denotes only dimension until the representation is identified below. We have accounted for every row and column.

## 4. The only possible differential pattern

The entire potentially nonzero E₂ page now has four entries:

    A=E₂^(−4,3)=C,
    P=E₂^(−3,2)=Tor₃,₅,
    Q=E₂^(−2,2)=Tor₂,₅,
    D=E₂^(−1,1)=C.

The only possible d₂ maps are

    α:A→Q,       β:P→D.

At Q there is no outgoing d₂: its target is (0,1), which is zero. There is no later incoming differential because q=4 is zero, and no later outgoing differential because its target column is positive. Hence

    E₃^(−2,2)=coker α=E∞^(−2,2)=0.

Thus α is surjective. Similarly P has no incoming d₂ because (−5,3) is zero, no later incoming differential because the source would be outside the columns, and no later outgoing differential because q=0 is zero (for r=3) or the target row/column is outside the range. Consequently

    E₃^(−3,2)=ker β=E∞^(−3,2)=0.

Thus β is injective. A quotient of the trivial line A, and a subrepresentation of the trivial line D, have dimension at most one and are trivial if nonzero. This proves the theorem.

## 5. Exact remaining scalar alternative

After d₂, the only entries left are

    E₃^(−4,3)=ker α,     E₃^(−1,1)=coker β,

both of dimension 1−e. The only remaining possible differential is

    d₃:ker α → coker β.

It must be an isomorphism, since no higher differential can reach either slot and the abutment is zero. Accordingly there are precisely two necessary page patterns:

- e=0: α=β=0 and the residual d₃ between the two trivial lines is nonzero, hence an isomorphism.
- e=1: α and β are isomorphisms, so no residual d₃ source or target remains.

This is not a proof that both patterns occur for HM, nor a definition of one globally fixed scalar d₃ before E₃ has been formed. It identifies the residual spectral-sequence alternative without confusing its page-dependent domain with a canonical map between the original two lines.

## 6. Updated resolution constraints and boundary

The previous necessary shape remains

    F₀=S²;
    F₁=S(−2)¹⁰ ⊕ S(−3)^a ⊕ S(−4)^b;
    F₂=S(−3)^a ⊕ S(−4)^(20+b+d) ⊕ S(−5)^e ⊕ S(−6)^d;
    F₃=S(−4)^d ⊕ S(−5)^e ⊕ S(−6)^(20+b+d) ⊕ S(−7)^a;
    F₄=S(−6)^b ⊕ S(−7)^a ⊕ S(−8)¹⁰;
    F₅=S(−10)².

Now a∈{0,15}, b∈{0,5,10,15,20}, e∈{0,1}; a=0 forces d=0, and a=15 permits only d∈{0,5,10,15,20,25,30}. If present, the two S(−5) ghost coefficient spaces carry the trivial N-representation.

No claim is made that these necessary choices are all realizable. The theorem does not determine a,b,d, or choose e=0 versus e=1. In particular a pure even-degree resolution has not been proved. Symmetric self-duality alone is not used to assert an alternating residual scalar, and no parity exclusion is claimed.

The argument evaluates no selected HM/source/cofactor matrix, polynomial instance, catalecticant, or physical obstruction. It uses an actual multiplication theorem already proved structurally, not a newly evaluated map.
