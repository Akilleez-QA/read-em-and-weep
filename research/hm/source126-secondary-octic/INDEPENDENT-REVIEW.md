# Independent review: secondary octic restriction

Reviewed the complete proof, checker and four pinned inputs. No mathematical blocker found in the stated universal identity or its conditional application.

## Frozen bytes and replay

- PROOF.md SHA256: 200a74c6c7aa6b2f7ee0a183f17d37f8016dda779ba043350e7a6ef0efc53c3d
- verify.py SHA256: 903600e9b6fb45ab07639b5512cd1e4b30d973b9eb1d0401b4b1eecc5f48adfc
- INPUTS.json SHA256: 4d2e521356206d93b4758006f2304519dc13626bb3469551af0e5fb6b686d1dc
- `python verify.py` and `python -O verify.py` independently replayed successfully: 51 checks each, identical stdout.
- The authenticated PR995 proof has the exact SHA256 8f75112f5dcc7bb57efb24d9abc0bf7b33fbbcc6b128569eea8576bcf90699cd previously independently reviewed. The manifest pins it at f9435fa37c78e86391fd1a773a039dd646a05e53 with Git blob 0e63a5cc5a209939c29de8aa2df272cc249814d6.

## Mathematical checks

1. The signed-minor quotient kernel has coefficient degree four. Its equivariant line carries no additional character because the group is perfect. Composition with the degree-one first transvectant and any equivariant quartic covector is therefore a scalar invariant of degree nine on the three-dimensional parameter representation A. It is not a binary degree-nine invariant calculation.
2. The plethysm into binary degrees 18, 14, 10, 6, 2 and the pinned McKay recurrence give zero invariant multiplicity in each constituent. As an independent check not using that recurrence, the A5 class-average calculation with class sizes 1,15,20,12,12 and traces 3,-1,0,(1+sqrt(5))/2,(1-sqrt(5))/2 gives invariant multiplicities in Sym^n A for n=0,...,9 equal to [1,0,1,0,1,0,2,0,2,0]. Here complete symmetric characters satisfy h_n=t h_(n-1)-t h_(n-2)+h_(n-3), since the rotation representation has determinant one and second elementary character t. In particular degree nine is zero.
3. Higher naturality uses only the quotient first-cycle line at a fixed direction a. Generic surjectivity of its first symbol permits recursive finite-order quotient lifts. Applying the same-direction secondary chain map gives the eighth obstruction on its induced initial class. No commutation with another direction or assertion on all of D is used.
4. Total degree is 4+1+8=13, giving O(-13) to E. Factoring the octic map through sigma leaves the degree-nine scalar 4+1+4. Its universal vanishing makes the resulting condition automatic, regardless of either scalar.
5. The independent coefficient certificate uses the authenticated universal P6 matrix and the Wronskian invariant. Both quartic rows have the claimed degree and equivariance. C is nonzero; B has a nonzero coefficient on the discriminant-zero abstract form, proving independence from C. The exact signed-minor identities on the formal monic chart prove the normalized primary relation, nonzero primary restriction, and zero secondary restrictions globally by homogeneity and density. The two free chart variables are not assigned actual-instance values.

## Scope

This is a new negative restriction theorem: the proposed secondary test cannot eliminate the canonical octic line, even conditional on a nonzero secondary scalar. It does not establish occurrence, nonzero actual octic scalar, vanishing of that scalar, or a repaired original proof. The tests are exact bounded universal computations and source authentication; they are not proof-assistant verification or actual HM evaluations.
