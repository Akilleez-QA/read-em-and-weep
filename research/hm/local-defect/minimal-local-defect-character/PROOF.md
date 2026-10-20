Publication context: this retained proof or audit may describe an intermediate bound or then-open branch. Read the unit overview for the current scope and later implications. Historical mathematical review is not a new formal verification.

# A universal character obstruction to a length-one isolated defect

## Result

Let R be the local ring of a smooth complex fourfold at a fixed point of a finite group H. Let M be an H-equivariant reflexive R-module of rank two, free away from the closed point, with equivariantly trivial determinant. Put W=m/m² and δ=det W. If

    Ext²_R(M,R) = kχ

has length one, then necessarily

    δ³ = χ⁻⁴                                      (1)

as characters of H. Consequently, if H contains an element g of order four with δ(g)=-1, such a length-one defect is impossible.

For the canonical 30-point orbit of the projective Heisenberg normalizer on P4, every point has such an element in its stabilizer in the order-15000 SL5 normalizer. Therefore an equivariant rank-two reflexive sheaf B with equivariantly trivial determinant and isolated singularities cannot have Ext²(B,O) of total length 30. Combined with the previously proved orbit gap, the possibilities strictly below 125 reduce to 60, 90, and 120. Equivalently, if length Ext²(B,O)=5q, then 0<q<25 forces q in {12,18,24}. This is a necessary restriction, not an existence assertion or an exclusion of the remaining rank-eight branch.

The proof does not assume a classification of length-one singularities. It proves the required minimal-resolution and alternating-form conclusions directly.

## 1. Duality and minimal Betti numbers

Write A=Ext¹_R(M,R) and D=Ext²_R(M,R). Reflexivity and the regular dimension-four hypothesis give pd M≤2. Isolated singularities make A and D finite-length. The rank-two determinant pairing gives an H-equivariant isomorphism M≅M*, since det M has the trivial linearization. The natural double-dual spectral sequence, or the free-resolution argument in the isolated-singularity proof cited below, therefore gives

    A ≅ Ext⁴_R(D,R).

The equivariant Koszul resolution gives Ext⁴_R(k,R)=k⊗(det W)*. Hence if D=kχ, then

    A=kψ,             ψ=χ⁻¹δ⁻¹.                  (2)

Choose a minimal free resolution

    0 → F2 → F1 → F0 → M → 0.

Minimality identifies D/mD with F2*/mF2*, so rank F2=1. After choosing a generator of F2*, the dual last differential is a row F1*→R with cokernel k; its entries generate m. Four of these entries can be chosen as regular parameters x1,…,x4. Elementary changes of basis subtract combinations of these from the remaining entries. Thus, nonequivariantly, the row is

    (x1,x2,x3,x4,0,…,0),

with u zero entries. Let K0=ker(R⁴ --x--> R). Its kernel K is K0⊕R^u. Rank counting in the resolution gives

    rank F1=4+u,       rank F0=5+u.

Let C=im(F0*→F1*). The dual complex gives an exact sequence

    0 → C → K → A → 0.                            (3)

Minimality gives C⊂mF1*. Also K0⊂mR⁴, because a syzygy among a regular minimal set of parameters has no nonzero constant coefficients. Therefore the map K→F1*/mF1* has rank u and factors through K/C=k. Thus u≤1.

Suppose u=1. The induced nonzero linear map A→F1*/mF1* is injective. Since K0 maps to zero in F1*/mF1*, the quotient K→A must vanish on K0 and be a nonzero scalar multiple of R→k on the remaining free summand. Thus

    C=K0⊕m.

The Koszul resolution gives μ(K0)=6 and μ(m)=4, hence μ(C)=10. But F0* has rank 6 and surjects onto C, a contradiction. Consequently u=0 and

    (rank F0,rank F1,rank F2)=(5,4,1).             (4)

This argument uses only the dimensions of A and D, not any assumed normal form for M.

## 2. Equivariant Koszul quotient and its nondegeneracy

We may complete R faithfully flatly. This preserves minimal resolutions, finite-length Ext modules, and all representation identities. Finite complex groups are linearly reductive, so minimal free resolutions and choices of generators may be made equivariant by averaging. An equivariant section W→m exists after completion, and its image is a system of formal parameters.

Since F2*/mF2*=D=kχ, we can identify F2*=R⊗χ. By (4), the differential F1*→F2* has four minimal generators for its image m⊗χ. Its linear term identifies the fibre of F1* with W⊗χ, and equivariant choices identify the differential with the parameter row

    R⊗W⊗χ → R⊗χ.

Its kernel K has the truncated Koszul resolution. In particular

    K/mK = Λ²W⊗χ,
    Tor¹_R(K,k) = Λ³W⊗χ.

The quotient K→A=kψ is therefore specified by a surjective H-equivariant functional

    f: Λ²W⊗χ → ψ.                                (5)

Apply Tor(-,k) to (3). Its relevant exact portion is

    Tor¹(K,k) → Tor¹(A,k) → C/mC → K/mK → A → 0.

Since Tor¹(A,k)=W⊗ψ and dim(K/mK)=6, if r is the rank of the first arrow, then

    μ(C)=(4-r)+(6-1)=9-r.

But rank F0=5 and F0* surjects onto C, so μ(C)≤5. Since r≤4, necessarily r=4 and μ(C)=5.

For completeness, the first arrow is the Koszul contraction determined by f. Removing the common χ twist, write η=ψχ⁻¹ and view f as an alternating form W×W→η. On exterior generators its contraction is

    a∧b∧c ↦ a⊗f(b,c) - b⊗f(a,c) + c⊗f(a,b).

Indeed, lift the degree-zero quotient (5) to the constant-coefficient map on the free Koszul generators Λ²W; composing with their Koszul relation gives the displayed expression, now landing in the degree-one Koszul generators of kψ. This constructs the chain map computing the Tor arrow.

A nonzero alternating form on a four-dimensional space has rank two or four. In a basis in which a rank-two form is e1*∧e2* (with a chosen basis of η), the displayed contraction has image span(e3,e4)⊗η, of dimension two. A rank-four form is e1*∧e2*+e3*∧e4*, and its contraction takes the four basis elements of Λ³W to nonzero multiples of the four distinct basis vectors of W⊗η, hence is invertible. Since the Tor arrow has rank four, f is nondegenerate.

Wedge-square of this nondegenerate η-valued alternating form gives a nonzero equivariant map Λ⁴W→η². Hence

    δ=η²=(ψχ⁻¹)².

Substituting (2) yields δ=χ⁻⁴δ⁻², which is exactly (1).

Only this necessary alternating-form conclusion is needed. We make no stronger analytic or equivariant classification claim about M.

## 3. The canonical point stabilizer and its determinant character

Use the universal Schrödinger model with basis e_i indexed by F5. Let ζ be a primitive fifth root and consider the canonical point p=[e_0]. The universal projective normalizer contains

    Z e_i = ζ^i e_i,
    D e_i = ζ^(i²/2)e_i,
    T e_i = e_(2i).

These are representation operators of the abstract Heisenberg normalizer, not evaluations of any geometric operation or rank instance. All three fix p. The commuting projective operators Z,D generate a group of order 25: a relation Z^a D^b scalar would force the polynomial ai+bi²/2 to be constant for every i in F5, hence a=b=0. The permutation T has order four and normalizes this group. Explicitly T Z T⁻¹=Z³ and T D T⁻¹=D⁴. Its nonidentity powers are not diagonal, so the generated projective subgroup has order 100. The already established orbit size 30 in a group of order 3000 shows it is the whole projective stabilizer P.

Both conjugation multipliers 3 and 4 differ from 1 in F5. Commutators with T therefore generate both order-five factors, so P_ab=C4. This verifies the anticipated stabilizer description, although the obstruction below does not require its abelianization.

The four affine coordinates transverse to [e_0] are indexed by F5×. On them T acts by a four-cycle. Its tangent determinant is -1, and its cotangent determinant is also -1. The determinants of Z and D on these four tangent directions are respectively ζ^(1+2+3+4)=1 and ζ^((1²+2²+3²+4²)/2)=1. Thus δ on P is the nontrivial order-two character of its C4 abelianization.

The projective action lifts to the stipulated order-15000 group N⊂SL5. Since det T=-1, its determinant-one lift

    g=-T

belongs to N: N is the full inverse image of its projective order-3000 image under SL5→PGL5, because it has order 15000 and contains the kernel μ5. The operator -T still has order four. Its projective action agrees with T, so it fixes p and satisfies δ(g)=-1.

Every character χ of the N-stabilizer satisfies χ(g)^4=1. Evaluating (1) at g would give

    -1 = δ(g)³ = χ(g)⁻⁴ = 1,

a contradiction. This also handles central characters correctly: no descent of χ to the projective stabilizer is assumed.

All canonical orbit points are conjugate, so the same argument applies at each one.

## 4. Global consequence and scope

The determinant linearization hypothesis is automatic in the stipulated global setting. Indeed N=H5⋊SL2(F5) is perfect. To see this explicitly, SL2(F5) is generated by upper and lower unipotents, and conjugation by diag(2,3) acts on the upper-unipotent parameter by multiplication by 4. Thus its commutators contain every upper unipotent, and by conjugation every lower unipotent; SL2(F5) is perfect. Also [H5,H5]=Z(H5). On H5/Z(H5)=F5², the central element -I of SL2(F5) acts as -1, so its commutators induce the invertible map -2 on F5². Consequently [N,N] contains Z(H5) and surjects onto H5/Z(H5), hence contains all of H5. It also contains the SL2(F5) factor, proving [N,N]=N.

An N-linearization on the underlying line bundle det B≅O differs from the standard trivial linearization by a character N→C×: every automorphism of O on P4 is multiplication by a constant. A perfect group has no nontrivial such character. Hence det B is equivariantly trivial, as required by the local theorem. This supplies the linearization conclusion from the underlying determinant statement, without assuming a particular choice of trivialization.

If T_B=Ext²(B,O) has total length 30, the unique-minimal-orbit theorem forces support equal to the canonical orbit, with length one at every point. In the isolated-singularity branch, each stalk B_p satisfies the local hypotheses above. The contradiction in Section 3 excludes total length 30.

More generally, if 0<length(T_B)<125, its support is the same 30-point orbit, with constant stalk length m. The original orbit argument allowed m=1,2,3,4. This proof excludes m=1 and leaves m=2,3,4 unexamined. It makes no assertion for nonisolated singularities, where Ext¹ may fail to have finite length and Section 1 does not apply.

Inputs used from existing proofs:

- `../rank-eight-isolated-singularity/PROOF.md`, Section 1: natural local duality for isolated reflexive modules (the equivariant version follows from exactly the same natural resolution maps).
- `../normalizer-minimal-point-orbit/PROOF.md`: the canonical orbit, its uniqueness, and the 125-point gap for other orbits.
- `../full-hm-image-symmetry/PROOF.md`, Section 1 and its SL5-lift discussion: the stipulated order-15000 normalizer, central kernel μ5, and projective order 3000.

All new steps above are proved directly by local algebra, Koszul complexes, and the universal finite-group representation. No actual source, operation matrix, selected input, rank instance, jet, residue, or large computation was used. The only write was this proof artifact.
