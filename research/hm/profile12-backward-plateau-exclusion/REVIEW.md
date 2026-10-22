# Independent review: backward-plateau exclusion

## Verdict and exact version

PASS, conditional on the explicitly cited actual-bundle and source-catalog inputs. No correction or additional saturation hypothesis is needed for the argument reviewed here.

Reviewed artifact: `PROOF.md` in this directory.

Reviewed SHA256:

    4ddb4c7993039cf0e4504c2cd7403b45925a508a6489cc366ac9892ba39f53e0

This verdict applies only to these exact proof bytes and the dependency versions below. It is an independent written mathematical audit, not proof-assistant certification or a source-instance computation.

## Dependency checks

The quadratic-block source reduction was read, and the public file at PR796 commit `d2b43060c83328dd5118aee6b9288fcfa0c873ac` was fetched independently. Its SHA256 is:

    622763aac375db7e17bc7cab472f1afda0477b0f769371a3b3ef845cd5c9e3b1

Its surviving source lists are entry 6 for `G3.12.37914c53373c`, and entries 6 and 13 for `G3.12.eed6acb13f3e`.

The tensor-quartic companion proof was read in full. Its public file at PR797 commit `cdee9396133fb96d4a91babba87b1a7a35903635` was fetched independently and has SHA256:

    863bb17be118558b5c6199d0b3b73a7257cdd1f6871cdd903be2a19128574c98

The needed conclusions are supplied by actual maps inside the original constant ambient bundle: the complete evaluation sequence with quotient `V O(4)`, its onto quotient `O(18)`, the sheaf intersections `Zplus` and `N`, the equality `N=Zplus^-`, and the residual bundle type `E/N=Wp O(-1)+L`. The companion's derivation of these conclusions does not supply a flat complement or assume saturation of the entire residual projection. The exclusion proof does not need either assertion.

The public `ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md` was fetched at `db51525015bb7c5e825833d550d08dedf6f6ea96`. Section 4 defines `F_k=E` and identifies the derivative kernel of each interior stage with the preceding stage. Section 5 states that the maximal rank-three plateau endpoints have Gauss rank one or two. Thus for `k=1`, `E=F_1` and `E^-=F_0` is such an endpoint. The strict inequality used in the exclusion has the correct indexing; it is not an extra plateau assumption.

## Mathematical checks

### 1. The mismatched source is impossible

For entry 6 with negative quotient `W O(-9)`, every source summand except `O(-10)` has degree too high to map nontrivially to that quotient. A line cannot surject onto its rank-two target. This removes precisely the mismatched source and does not discard either matching source without proof.

### 2. The projected backward kernel is an exact sheaf image

The map `N -> A_q` is onto `O(14)` because its restriction to `F` is already onto that line, while the displayed splitting degrees of `N` exclude every map to the negative quotient.

After quotienting by `N`, the surjection to `L` kills `Wp O(-1)` by degrees. Its restriction from the other rank-two summand `L` is a surjective endomorphism, hence an isomorphism. The kernel diagram therefore gives the genuine exact sequence

    0 -> K intersect N -> K -> Wp O(-1) -> 0.

The surjectivity of the last map uses the surjectivity `N -> O(14)`: a local lift can be adjusted by a section of `N` to kill its remaining positive-quotient component. This is a sheaf argument, not a claim about full fiberwise intersections. It proves that the actual image of `K` in the constant quotient is exactly the indicated copy of `Wp O(-1)`, even if the larger image of `E/N` has a torsion defect in its saturation.

Every equivariant map from this bundle to the constant quotient corresponds to an intertwiner from the irreducible representation `Wp tensor W=P`. The nonzero intertwiner is injective, so the resulting bundle map factors through the tautological inclusion into a constant copy of `P`. It is fiberwise injective and has Gauss rank two. This conclusion does not require any horizontal splitting of `E` or `K`.

### 3. Jet orders and degree shifts agree

The complete quartic evaluation sequence and the morphism `V O(4) -> O(18)` make the defining degree-eighteen system the product of a basepoint-free degree-fourteen system with the complete quartic system. At any point one degree-fourteen factor is a unit in the local ring. Multiplication by this unit preserves jet generation, and complete quartics generate jets through order four. This proves the required jet generation without evaluating a chosen point or coefficient.

With order zero included in principal parts, the indexing is

    J_0=Zplus,  J_1=N,  J_2=N^-.

Locally, write the row of generating sections as `f`. A local section `s` of `J_i` satisfies `f^(j) s=0` for `0<=j<=i`. Differentiation gives `f^(j) s'=-f^(j+1) s`. Hence `s'` lies in `J_(i-1)`, and it lies in `J_i` precisely when the next jet also vanishes. This verifies `J_i^-=J_(i+1)` and the stated quotient derivative map. Its surjectivity follows from generation of the next jet.

The successive principal-parts quotients are `O(18)`, `O(16)`, `O(14)`, and `O(12)`. Consequently `N/J_2=O(14)`, and the internal derivative of `J_2` maps onto

    (N/J_2)(-2)=O(12).

The proof's ranks 13 and 12 and degrees -34 and -48 are consistent with these quotients. There is no missing cotangent twist.

### 4. Kernel naturality and rank independence hold

For a local section of `N`, its derivative lies in the constant subsystem. Vanishing modulo `E` is therefore equivalent to vanishing modulo `E intersect C0=N`. It follows as an equality of sheaves that

    K intersect C0=N^-=J_2.

In particular the internal rank-one derivative of `J_2` remains nonzero modulo `K`.

At the generic point, constant projection makes the derivative diagram commute. The composite of `beta_K` with the quotient by the projected bundle is the tautological rank-two second fundamental form composed with the surjection from `K`. The nonzero derivative image of `J_2` belongs to the kernel of that projection. Therefore the image of `beta_K` has dimension at least two plus one. These are independent image contributions, not a sum of ranks in unrelated quotients.

This is sufficient for the contradiction. In fact `beta_K` takes values in `(E/K)(-2)`, which has rank three, because `K=E^-`. Thus the derived lower bound forces rank exactly three and would extend the plateau backward, contradicting its maximal backward index one.

## Scope and restrictions

The argument exhausts the two surviving profile-(1,2) labels using the pinned source lists. Its arithmetic change from 22 labels to 20, with profile counts 19/0/1, is conditional on the cumulative baseline reported in PR796. It makes no new source2, profile-(1,1), higher-lifting, algebraicity, `SF>=4`, or square-rank conclusion.

The audit used only written structural arguments, bounded universal representation identities, public text reads, and file hashes. No actual HM/source-instance coefficients, selected points, derivative evaluations, matrices, measured ranks, selected models, or large computation were used. No external writes were made.
