# Historical scope-limited review receipt

This review concerns the original source, possibly a larger scope than the excerpt in this unit. It is not a review of normalized publication bytes.

# Independent formal audit

## Verdict

PASS, conditional on the explicitly imported canonical invariant Massey operation, ordered vanishing K·K=0, stipulated equivariant HM presentation, classical cohomology row, and Kodaira–Spencer identification. The proof establishes a canonical four-dimensional filtered detector subspace inside the twelve-dimensional retained positive target and an eight-dimensional quotient. It establishes the stated restriction for triples containing two K₀ arguments. It does not establish any nonzero value or spanning assertion.

The entire PROOF.md was read, together with the relevant existing canonical-Massey, inversion-eigenspace, invariant-Ext structural, and retained-sector structural proofs. The checks below are formal checks of those statements and their compatibility.

## 1. Intrinsic filtration and cohomological injections

The graded-generation filtration is intrinsic relative to the polarization. In any degree-compatible free splitting, its terms consist exactly of summands with generator degree at most p. Consequently its terms and quotients are locally free, and each inclusion splits as an ordinary vector bundle. No canonical or multiplicative splitting is required.

The finite-group averaging argument applies to generator lifts even with inversion acting nontrivially on the graded polynomial ring: a linear equivariant section of the generator quotient extends to an equivariant R-linear isomorphism by the semilinear compatibility. Thus the claimed equivariant splitting exists. Multiplicativity follows from the displayed vanishing of maps to twists of larger generator degree.

The level-one cohomology isomorphism and level-one and level-two H² injections follow from the quoted vanishing groups. At level zero that particular H¹-vanishing argument is unavailable, as the proof correctly notes. The Reynolds retraction onto B^S4=O supplies the needed injection; it agrees with the normalized trace on this quotient algebra. Alternatively, the bundle splitting suffices at every level.

## 2. Filtered defining systems and independence

The proof correctly chooses a level-zero primitive for an adjacent pair of K₀ representatives. Choosing only level-one primitives would leave a gap when the third input has level one. For mixed pairs the level-one injection suffices, and for a pair of level-one inputs the level-two injection suffices. These choices prove the desired bounds in each ordering.

A Čech model may be taken on an affine cover of P⁴ with affine intersections, so that its filtered coherent subcomplexes compute the claimed cohomology. Its ordered cup product is associative and obeys the Leibniz rule. The filtration terms need not individually be subalgebras. The stipulated multiplicative comparison identifies its operation with the invariant derived-endomorphism operation.

The full invariant Massey class is independent of defining-system choices because the possible degree-one changes have cohomology in K and K·K=0. Existence of one filtered defining system then proves intrinsic membership. Injection into full H² also gives uniqueness of its filtered preimage. This does not require arbitrary primitives to be filtered, nor does it authorize primitives from the unrestricted, noninvariant algebra.

An additional immediate consequence is that M(K₀,K₀,K₀) lies in H²(F), so its [22] detector projection is zero.

## 3. Finite-duality inversion sign

The sign in B^∨≅B(3)⊗sgn is correct. Under S4, the top differential form on Y contributes the permutation sign, whereas the ordinary external tensor linearization of L^(−2) does not. The base has trivial S4 action.

Under simultaneous coordinate interchange, the four canonical-line determinant factors on Y multiply to det(J)^4=+1. Coordinate reversal on the five-dimensional base section space has determinant +1, since it consists of two transpositions and one fixed coordinate. Thus the relative canonical linearization contributes no additional inversion sign. The choice between a determinant and its inverse in the projective canonical-bundle convention makes no difference here, since both determinants have value +1.

Duality pairs the degree-one and degree-two generator representations, with the S4 sign twist and no inversion twist. The [22] degree-one factor is det²(C²), with inversion +1. Its degree-two partner consequently also has inversion +1. This justifies using the positive eigenspaces of H²(F(−1)) and H²(F(−2)) directly, rather than interchanging their positive and negative eigenspaces.

## 4. Euler signs and the negative endpoint

The twist −1 Euler expression has precisely the stated surviving internal degrees 1, 2, 3. The relevant line-bundle section traces are 1, 1, 3, and the internal-degree signs alternate. The expression −3 and the inferred H² trace −2 follow from the supplied Hom-coefficient traces and H¹ trace 1. Hence its positive dimension is 4.

At twist −2, the internal degree −3 term has line-bundle twist −5. It contributes H⁴, hence total degree −3+4=1, with a negative Euler sign. The standard H⁴(O(−5)) inversion character is +1 because det(R)=+1. Since the coefficient trace is −2, this endpoint contributes +2. Together with the internal degree 2 and 3 contributions, this is exactly the expression −8+2+2=−4 in the proof. The classical row has only H², giving positive dimension 8. This endpoint must not be discarded.

No further [22] contribution arises in degrees zero or three. Exact character projection and the existence of an equivariant splitting therefore identify the canonical retained associated graded dimensions as 4 and 8. They do not choose a canonical complement to the first piece.

## 5. Dual interpretation and limits

The Serre pairing is sign-valued for S4 and positive under inversion. Accordingly the physical D8-epsilon line pairs with the detector D8-trivial line. Projecting the detector to epsilon instead would be incorrect.

Writing L for the four-dimensional detector subspace, its annihilator L-perp in the twelve-dimensional physical sector has dimension eight. The detector quotient Tret/L pairs perfectly with L-perp, while L pairs perfectly with the physical quotient by L-perp. Any equivariant dual identification retains the Serre value-character line. There is no canonical eight-dimensional complementary detector subspace, and the proof gives no assertion that the actual physical obstruction belongs to L-perp.

The quotient operation annihilates the span of tensors with two K₀ slots. This is a necessary restriction only. Inputs with two nontrivial coefficient components face no additional restriction from this particular filtration, but that statement supplies neither a nonzero value nor accessibility of every quotient direction. Further geometric identities could still force additional vanishing.

