> Current actual-bundle specialization: the degree-one-kernel exclusion rules out a=1. The a=1 formulas below are historical conditional algebraic derivations, not current actual alternatives.

# When the entire 2C section space is an exact detector

## Statement and notation

Use the assumptions and notation of `PROOF.md`, in its nonzero-detector branch: E is locally free of rank two on W=P², K=O(a) is the unique nonnegative saturated line with a=0 or1, its quotient is I_Z⊗det(E)⊗K⁻¹, N=K²⊗det(E)⁻¹, and C is a smooth conic with equation q. Write B_W=End₀(E), D=2C, and d=length(Z∩C).

Then the restriction map

    H⁰(W,B_W(−1))→H⁰(D,B_W(−1)|D)

is an isomorphism if and only if Z∩C is empty. For arbitrary Z, the map is injective and its image is exactly the sections of the actual restricted nilpotent line j_D(N(−1)|D), as proved in `PROOF.md`.

If d>0, put ℓ=length O_W/(I_Z²,q²), so ℓ≥2d. The full restricted section space has at least ℓ−1 additional dimensions for a=0, and at least ℓ additional dimensions for a=1. These are lower bounds, not assertions of the exact number of extra sections.

## Proof

Assume the nonzero-detector branch, and set M=B_W/jN. Comparing the line jN with the rank-two kernel in the preceding exact sequence gives

    0→I_Z→M→I_Z²⊗N⁻¹→0.                         (A)

The quotient on the right is torsion-free, so (A) remains left-exact on any Cartier thickening of C.

### If Z is disjoint from C

Restriction of (A) to D=2C and twisting by −1 gives

    0→O_D(−1)→M(−1)|D→O_D(−2a−3)→0.

Both outer sheaves have no H⁰. Indeed a negative plane line bundle has no sections on 2C, by its divisor sequence and H¹(O_P²(t))=0. Thus H⁰(M(−1)|D)=0. The exact sequence

    0→N(−1)|D→B_W(−1)|D→M(−1)|D→0

proves that every section of B_W(−1)|2C belongs to the actual nilpotent line. Combined with coefficient extension, it yields

    H⁰(B_W(−1)) ≅ H⁰(B_W(−1)|2C).

### If Z meets C

There are necessarily additional, nonextendable sections on 2C. To see this without assuming reduced or transverse intersection, dualize the line and ideal-square sequences. They identify

    M** ≅ E⊗K⁻¹,
    T₀=M**/M ≅ Ext¹_W(I_Z²⊗N⁻¹,O_W).

Locally, up to a line twist, T₀ is the canonical module of the Artin ring A=O_W/I_Z². It has length 3 length(Z). Tensoring 0→M→M**→T₀→0 with O_D shows that the zero-dimensional torsion subsheaf of M|D is

    Tor₁(T₀,O_D).

Its length at a point is length A/(q²): the kernel of multiplication by q² on a finite-length module has the same length as its cokernel, and Artin duality preserves the rank of this multiplication map.

Put d=length(Z∩C)>0. Since C is smooth, the quotient O_C/I_Z² O_C has length 2d. The quotient by (I_Z²,q²) surjects onto the quotient by (I_Z²,q), so

    length Tor₁(T₀,O_2C) = length O_W/(I_Z²,q²) ≥ 2d.

These finite-support sections are global sections of M(−1)|2C. In the sequence with kernel N(−1)|2C, their failure to lift can have dimension at most

    h¹(O_2C(2a+1)) = 1 if a=0, and 0 if a=1.

Therefore the full H⁰(B_W(−1)|2C) is strictly larger than the globally extendable subspace: it has at least ℓ−1≥2d−1 extra dimensions if a=0 and at least ℓ≥2d if a=1. This uses only the finite-support subspace of H⁰(M(−1)|D); further sections are not excluded. These lower bounds are sufficient for strictness, since d≥1. Thus

    H⁰(B_W(−1))→H⁰(B_W(−1)|2C) is an isomorphism
        if and only if Z∩C is empty.              (B)

The given 2C line-membership criterion remains valid in both cases and is the correct unconditional formulation. Criterion (B) does not assert that Z∩C is empty for the actual HM pullback.


## Reduced-conic consistency check

Identify C≅P¹, so O_W(1)|C=O_P¹(2). Saturation of K|C has degree 2a+d. Its quotient in E|C has degree −4−2a−d, and the extension splits because H¹(O_P¹(4a+4+2d))=0. Thus

    E|C ≅ O_P¹(2a+d) ⊕ O_P¹(−4−2a−d),
    h⁰(C,B_W(−1)|C)=4a+3+2d.

The actual restricted nilpotent line has 4a+3 sections, and its saturation accounts for the additional 2d. The global restriction image is exactly this 4a+3-dimensional line-section space: dimension 3 for a=0 and dimension 7 for a=1. For a=1, the remaining three global detector parameters vanish on C and are detected by 2C.

## Scope

This criterion does not evaluate the actual intersection Z∩C, the extension, or the ambient detector rank. Even when all 2C sections extend, the ambient Gysin map remains necessary to test an ambient class.
