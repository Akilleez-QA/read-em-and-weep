> Publication scope: preserved mathematical proof/audit. Historical statements that rank eight remains open are superseded only after the final assembly and all its prerequisites. No source-instance evaluation or formal verification is claimed here.

# Independent audit: pass

Audited the exterior-quotient resolution, its cohomology indexing, and the elementary Koszul-homology argument. No actual operation, source matrix, input, rank instance, jet, residue, or polynomial instance was evaluated.

## Checks

1. **Bundle identification and twists.** For L=O(-2)⊂S⊗O and E=(S⊗O)/L, the kernel of wedge with the universal square on Λ^mS⊗O(e) is L⊗Λ^(m−1)E⊗O(e). Thus it is Λ^pE(e−2), p=m−1. The requested lift is precisely the surjectivity map stated in the proof.
2. **Resolution.** Locally splitting L⊂S verifies exactness of the complex with C_j=Λ^(p−j)S⊗O(t−2j). Globally its differentials are wedge with the same universal square, so it glues with the stated twists.
3. **Cohomology obstruction.** P⁴ line-bundle cohomology is concentrated in degrees zero and four. In the resolution spectral sequence with C_j at horizontal degree −j, the only possible extra contribution to total degree zero is the H⁴-row homology at j=4. No later differential leaves or enters that term. Consequently it is the cokernel obstruction to lifting global sections. Terms at j=5 may affect the kernel of the global lifting map through a higher differential, but do not create another cokernel obstruction. For p≤3 there is no obstruction.
4. **p=4.** Equivariant Serre duality gives the displayed dual cokernel S*⊗Sym^(3−e)V*→Sym^(5−e)V*. For e≤3 this is ordinary polynomial multiplication by all quadrics, and is surjective. Negative polynomial degrees are interpreted as zero as stated.
5. **p=5.** The dual row is exactly the degree-(7−e) first Koszul homology of the fifteen quadratic generators of the square of the homogeneous maximal ideal. The shifts and exterior-power positions in all three terms agree.
6. **Koszul vanishing.** Pairwise monomial syzygies generate the first syzygy module. If two quadrics are coprime, introducing a mixed quadratic reduces their degree-four relation to multiples of degree-three relations; all other nontrivial pairwise relations already have degree three. Thus first Koszul homology is generated in degree three. Wedge multiplication by a generator basis vector provides a chain homotopy annihilating multiplication by its quadratic generator, so the maximal-ideal square annihilates homology. Since every coefficient of degree at least two belongs to that ideal, all homology degrees at least five vanish. This proves the stated e≤2 range.
7. **Equivariance and limits.** Finite-group averaging gives a lift of the required equivariance type. Neither this argument nor the exterior resolution proves decomposability of a constant lift, and the proof correctly declines that inference. The result is a lifting theorem, not a rank-six exclusion.

The ranges are understood for positive exterior degrees m, as in the kernel-Plücker applications. No substantive correction is required.
