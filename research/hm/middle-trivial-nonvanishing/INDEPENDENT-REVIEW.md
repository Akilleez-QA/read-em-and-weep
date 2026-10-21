# Independent review: trivial-character middle nonvanishing

## Verdict and exact scope

The proof passes independent mathematical review, conditional on its pinned actual-module, pairing, representation and relative-family inputs. This review checks the actual source maps and tensor contractions, not only character dimensions. It is not a proof-assistant verification. No selected HM parameter, numerical matrix, coefficient search, rank search or large computation was used.

The reviewed file is `PROOF.md`, SHA256 `a327776d0776bd6eaa8034589749016cc91723fb056a5997f8613abd2becf9af`. The final correction removed a stray comma inside the PR512 link target and did not change mathematics.

## 1. Actual central map and obstruction

For K_i(H)_5=H_(5-i) tensor Lambda^i(T), taking Gamma invariants is exact. The two outer maps are isomorphisms on the stated two-dimensional spaces, by the actual degree-zero multiplication and its pairing dual. The adjacent maps are therefore zero, and acyclicity forces the central eight-dimensional differential to be invertible. The Koszul wedge/trace pairing identifies its target with the dual of its source. The sign identity for two degree-three inputs makes this central form symmetric, not alternating.

The cubic embedding is also an actual map. The presentation H2=E tensor Sym3(W) comes from the multiplication quotient Sym2(W) tensor W -> Sym3(W), whose kernel is the lower binary summand. A column lambda evaluates the last W factor and the residual degree-two factor evaluates by lambda squared. Their composite on H2 is lambda cubed. Thus dualizing H2 -> C2=E O(3) gives the stated cubic Veronese inclusion of B3. Taking exterior pairing and Gamma invariants does not change that Q-factor map.

Because B2=0 there are no degree-five boundaries into K2(B). The outgoing invariant map vanishes as the restriction of the zero adjacent map in K(H). Thus the embedded W0* O(-3) is exactly Tor2(B)_5^Gamma, not merely an auxiliary two-plane family. The chain lift formula then identifies the actual obstruction with the restriction of the inverse central form.

## 2. Separate symmetry survives the actual contraction

Write H2=E tensor Q and Lambda3(T)=A_rep tensor W0, with E=A_rep*. The invariant source embedding Q tensor W0 -> H2 tensor Lambda3(T) is coevaluation on E tensor A_rep. In a dual pair of bases e_r,a_r, it sends q tensor u to the sum of e_r tensor q tensor (a_r tensor u). This embedding is independent of q and does not mix the Q factor with the exterior factor.

Balance and symmetry of b_H imply that m(t,h,k)=b_H(th,k) is symmetric in h,k. The possible alternating-in-Q component lies in the summand Lambda2(E) tensor Lambda2(Q). The actual identities Lambda2(E)=T* tensor W' and Lambda2(Q)=1+J5 rule it out: after taking Gamma invariants in T tensor T*, only the scalar identity remains, and neither 1 nor J5 supplies W'. This is a statement about the invariant trilinear map, not an inference from its dimension alone.

In the central Koszul form, the remaining operations are contraction of a T index and wedge pairing of exterior factors. Expanding the two coevaluation sums shows that they do not touch either Q argument. Swapping only the two Q arguments therefore leaves the form unchanged. Since the total central form is symmetric, its W0 arguments are separately symmetric as well. No exterior sign can create an alternating-in-Q component that is absent from m.

## 3. Restriction kernel and contradiction

The invariant symmetric forms on Q* tensor W0* have dimension two: one invariant in Sym2(Q) tensor Sym2(W0), and one in Lambda2(Q) tensor Lambda2(W0). The latter is the nondegenerate alternating-product form and vanishes on every cubic-Veronese two-plane.

For the former, restriction is multiplication Sym2(Sym3 W) -> Sym6 W. Its kernel is Sym2 W=U', whereas its invariant contraction with Sym2(W0)=U uses the distinct U summand. The restriction is nonzero. Thus the kernel on the invariant two-dimensional space is precisely the alternating-product line.

If the actual trivial obstruction vanished identically, the inverse central form would be a nonzero alternating-product form. Its inverse is again a product of alternating forms. This contradicts the separately symmetric Q-component established from actual multiplication. Invertibility excludes the zero form throughout. The nonvanishing conclusion follows.

## 4. Eigenvalue ratio

The alternating-product form J is symmetric, invariant and invertible. Hence A=J^(-1)d is equivariant on the multiplicity-free representation U direct_sum J5. Its eigenvalues a,c are nonzero. The trace contraction vanishes because the Q indices of d are symmetric and the corresponding indices of J^(-1) are alternating. Therefore 3a+5c=0, giving a:c=5:-3. This conclusion is unaffected by the global normalization of J or d and evaluates no actual scalar.

## 5. Consequences and remaining open part

The pinned relative-family theorem now applies in its nonzero alternative: the trivial block has corank one exactly on the reduced twelve-point orbit and is invertible elsewhere. Nontrivial inverse-character pairs contribute even corank, so the full middle Betti number is odd on that orbit and even away from it. Its generic value is restricted to 0 or 24.

This does not show nonvanishing of the twelve paired scalar sections, determine all exceptional total ranks, or prove that the middle Betti number is one on the twelve-point orbit. It does not resolve the original fixed-pair residual, higher-order lifting or algebraicity.
