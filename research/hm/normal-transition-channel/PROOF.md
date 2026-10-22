# The first surviving ambient transition channel after nilpotent normalization

## Statement

Work over C with the actual cone Q, negative line L=P(W), positive binary representation U=W', and V=Sym²U. Use cubic-first physical eigenframes, so E|L=O(5)_-⊕O(-2)_+. Let q be the invariant ambient quadric, a section of O(2), assigned cover weight four. The matrix weight convention is: weight d has diagonal, upper and lower cover degrees d,d−2,d+2.

Assume the regular chartwise normalization of the actual nilpotent N has been made so its cone expansion is n8+terms of weight at least16. Then the trace-free weight-four ambient transition defect, relative to the homogeneous weight-zero transitions, is q times a weight-zero coefficient. These coefficients define a canonical class

    κ ∈ H¹(L,J)^Γ,
    0 → V⊗O_L(-10) → J → O_L(-2) → 0.              (1)

Here canonical means independent of the local normalized physical frames and their ambient lifts, with the intrinsic weighted leading bundle identified. The exact sequence need not split. Projection to the diagonal quotient induces an isomorphism

    H¹(L,J)^Γ → H¹(L,O_L(-2))^Γ ≅ C.               (2)

Thus this specific first ambient transition layer has exactly one invariant cohomological channel. This does not evaluate κ, identify it with any previously normalized first-normal parameter, or evaluate a higher obstruction.

## Dependencies and prior results

- PR774, commit eec909bef4a7e6998737773d5eadd0ad562e79d9, research/hm/matrix-jet-filtration/PROOF.md: physical eigenlines, regular local frames, matrix filtration, and weight-zero lower triangular transitions.
- PR776, commit c885531e345cc67d1848b0cd8baa0f02ca786f47, research/hm/subleading-nilpotent-normal-form/PROOF.md: for every regular cubic/quintic pair, ad_n is injective on trace-free weight-four matrices.
- [PR777 global first-subleading residue theorem](https://github.com/Akilleez-QA/read-em-and-weep/blob/490337fee9e8f06fa8bf3e893ab646a37f996bf2/research/hm/global-subleading-residue/PROOF.md), commit 490337fee9e8f06fa8bf3e893ab646a37f996bf2, proof SHA256 43200eeebb2ec4b4809433d1568e4f244219be899f9a20a3e3d4afbe016f54ea: regular chartwise elimination of the actual N12 over every point of L. This is an explicit dependency, not a claim of a global gauge.

The original sources below are pinned at 8d8b5be4ce62c3055bb53be9e16d29cc63072f04, in research/hm/order-four-quadratic-load/:

- [NEGATIVE-VERTEX-EVALUATION-SCALAR.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/8d8b5be4ce62c3055bb53be9e16d29cc63072f04/research/hm/order-four-quadratic-load/NEGATIVE-VERTEX-EVALUATION-SCALAR.md) supplies the actual ordered physical eigenlines.
- [VERTEX-QUINTIC-RELATION-EXTENSION-AND-SQUARE-P4.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/8d8b5be4ce62c3055bb53be9e16d29cc63072f04/research/hm/order-four-quadratic-load/VERTEX-QUINTIC-RELATION-EXTENSION-AND-SQUARE-P4.md) supplies uniform regularity and the nonsplit quintic-generator extension.
- [MIDPOINT-HESSIAN-SYMBOL-MATCHING-BY-FULL-FRAME-COVARIANCE.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/8d8b5be4ce62c3055bb53be9e16d29cc63072f04/research/hm/order-four-quadratic-load/MIDPOINT-HESSIAN-SYMBOL-MATCHING-BY-FULL-FRAME-COVARIANCE.md), §§2–3, already retains the homogeneous lower-triangular transitions and the quintic-transition coefficient V⊗O(-8).
- [MIDPOINT-NORMAL-EXTENSION-HAS-UNIQUE-SQUARE-ZERO-ADJOINT.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/8d8b5be4ce62c3055bb53be9e16d29cc63072f04/research/hm/order-four-quadratic-load/MIDPOINT-NORMAL-EXTENSION-HAS-UNIQUE-SQUARE-ZERO-ADJOINT.md) already proves a one-dimensional invariant first-normal extension space on Q and a nonzero bracket between invariant lines. We do not claim that general one-dimensionality as new, nor identify its global class with the particular weighted vertex class κ without a comparison map.

- [FULL-HOMOGENEOUS-NORMAL-MATRIX-STILL-LOSES-THE-POLYNOMIAL-NINE-SPACE.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/8d8b5be4ce62c3055bb53be9e16d29cc63072f04/research/hm/order-four-quadratic-load/FULL-HOMOGENEOUS-NORMAL-MATRIX-STILL-LOSES-THE-POLYNOMIAL-NINE-SPACE.md), §3, already identifies the regular weight-zero coefficient at physical twist two as J_-=P4⊗O(-4), with exact sequence 0→V⊗O(-6)→J_-→O(2)→0 and triangular law r_j=r_i+2p k_i. Its marked frame convention is exactly the present one, so J0=J_-(-2)=P4⊗O(-6). Thus the abstract coefficient bundle and its twists are existing results, not new claims here.

The contribution here is the passage from N12-normalization to an ambient q-divisible transition cocycle, identification of its weighted coefficient sheaf, and its diagonal detection isomorphism (2). The tangent-modulo-commutator sheaf called M in the Hessian source is a different sheaf; J is not that quotient.

## 1. Cone transition collapse

Write a normalized overlap, with homogeneous coordinate substitution understood, as

    T=T0(1+Y4+terms of weight at least8),
    T0=[[a,0],[c2,d]],

where a,d are base units and c2 is binary quadratic. On the standard negative-coordinate atlas the twisting line of N has base-only transition h. The transformations of its first two pieces are

    n'=h T0 n T0^-1,
    D'=h T0(D+[Y4,n])T0^-1.

Both D and D' vanish by normalization. Hence [Y4,n]=0. Subtract half the trace of Y4; the scalar part commutes. PR776's injection implies that the remaining trace-free matrix is zero. This holds over every base open, either by its relative version or by injectivity generically and torsion-freeness of the regular coefficient bundles.

Therefore the cone weight-four overlap is scalar. We retain scalars until passing to the adjoint/projective transition; it is not necessary to choose square roots of determinants or a global scalar normalization.

## 2. An exact ambient reference, not a nonmultiplicative harmonic guess

The weight-zero transitions satisfy their exact cocycle identity because products add matrix weights. They lift canonically to ambient homogeneous matrices: the lower entry has cover degree two, hence ordinary transverse degree one, and there is no quadric relation in that degree. The diagonal entries are base functions. In multiplying two such matrices the lower entry is a sum of a base function times a lower entry; no product of two lower entries occurs. Consequently this lift preserves products and inverses exactly. Homogeneous coordinate changes on negative charts also commute with the lift.

Thus the ambient matrices T0 themselves form an exact reference cocycle. This step is essential: a general harmonic lift is not multiplicative and would introduce a spurious inhomogeneous cocycle defect.

For the actual ambient overlap write its weight-four correction as Y4^amb and take its trace-free part A4. Section 1 gives A4|Q=0. Since the ambient cone equation is the principal homogeneous quadric q, uniquely

    A4=q Z0,
    Z0=[[t,0],[ell2,-t]],                          (3)

with t a base function and ell2 an ordinary-linear transverse polynomial, equivalently a binary quadratic. The upper entry of A4 would have cover degree two and cannot be divisible by q unless zero. The diagonal and lower entries have cover degrees four and six, giving the two remaining degrees in (3). These statements are regular homogeneous divisibility, not generic division by any selected source.

## 3. Coefficient sheaf and the negative normal twist

Let J0 be the sheaf of trace-free weight-zero coefficients glued by conjugation with T0. For a local coefficient [[t,0],[ell,-t]], direct conjugation gives

    t ↦ t,
    ell ↦ (d/a)ell+(2c2/a)t.

Thus the diagonal quotient is O_L and the lower kernel carries the actual lower-Hom and transverse-coordinate factors. In cubic-first order lower-Hom is

    Hom(O(5),O(-2))=O(-7).

A binary quadratic is a linear ordinary positive transverse function. Its coefficient bundle on L is V⊗O(-1), not V⊗O(-2). Hence

    0 → V⊗O(-8) → J0 → O → 0.                     (4)

The triangular c2 term need not split and has not been discarded.

The ideal generated by q is O(-2). More explicitly, if q_j=u_ij q_i in local equation generators, then equality of q_i Z_i and its transported q_j Z_j says Z_i=u_ij Ad(T0_ij)Z_j. These are precisely the transitions of J0 tensored with the normal ideal O(-2). Therefore J=J0(-2), proving (1). Dividing the local expression by q removes four cover degrees but retains the negative ideal-line twist; it does not give J0(+2).

All linearizations are the actual coordinate linearizations: V=Sym²U, W defines L, q is invariant, and conjugation on the diagonal quotient is trivial. The two physical eigenlines are intrinsic. No exchange of V with Sym²W is made; both are nontrivial, inequivalent three-dimensional representations. The central action is positive on the even twists in (1).

## 4. The actual additive cocycle and independence

Work modulo terms of matrix weight at least8 and modulo scalar transition corrections. Products of two weight-four corrections vanish at this precision. Since the lifted T0 cocycle is exact, the actual transition identity becomes the additive Čech cocycle equation for the trace-free corrections A4, with the T0 adjoint transport. Trace-free projection commutes with conjugation, so scalar corrections have no cross-effect in this equation. Dividing by q, with its equation-line transition included, gives the Čech equation in J.

Changing an ambient normalized frame by a weight-four correction changes this cocycle by a coboundary. Indeed its cone trace-free part must commute with n, hence vanish by the same injection; its ambient trace-free part is q times a local section of J. Scalar parts again have no effect. A weight-zero change only identifies the leading coefficient bundle by its exact lifted homogeneous change of frame. Higher-weight changes have no effect. Refinement gives the same cohomology class κ.

The construction is natural for Γ: the actual N, physical splitting, q, homogeneous coordinate atlas, trace-free projection and the canonical weight-zero lift are equivariant. Comparing any translated normalized atlas with the original one by the preceding independence proves Γ-invariance of κ without presuming equivariant local frames.

## 5. Invariant cohomology and a precise next test

Both O(-2) and V⊗O(-10) have zero H0. Equivariant Serre duality on P(W), with det W trivial, gives

    H¹(O(-2))=C,
    H¹(V⊗O(-10))=V⊗(Sym⁸W)*.

For either binary icosahedral two-dimensional representation, Sym⁸ has the A5 character (9,1,0,-1,-1) on the classes (1,2,3,5a,5b). This follows directly from sin(9θ)/sin(θ) for eigenvalues exp(±iθ); the central sign disappears in degree eight. The character is P4+D5, whose respective characters are (4,0,1,-1,-1) and (5,1,-1,0,0). Hence Sym⁸W=P4⊕D5 and contains no three-dimensional constituent. Since V is irreducible and self-dual,

    H¹(V⊗O(-10))^Γ=0.

There is no H2 on L. Taking invariants is exact in characteristic zero, so the long exact sequence of (1) proves (2), independently of its extension class. Also H0(J)=0.

In particular κ vanishes if and only if its diagonal Čech class in H¹(O(-2)) vanishes. If it vanishes, a regular local qZ0 gauge removes the entire trace-free weight-four ambient defect, not only its diagonal; its cochain primitive is unique relative to the fixed reference cocycle because H0(J)=0. Equivariance of that primitive follows from uniqueness. This is a conditional elimination criterion, not an assertion that its hypothesis holds for the actual ambient bundle.

The next missing dependency is a comparison from the existing global first-normal extension class on Q to this weighted vertex class, including its chosen reference origin. Alternatively one could determine the diagonal class directly by a separately authorized structural computation. Dimension one alone establishes neither a nonzero actual value nor identification with the midpoint, the scalar parameter λ, rho4, beta4, or an algebraicity obstruction. No inference about the remaining normal coefficients B1,B2,B3 is made. Even κ=0 does not construct a global four-q-truncated lift of K16: conjugation by T0 need not preserve harmonic splitting and can generate q⁴ coefficient defects. The transition layer treated here is therefore not asserted to be the sole fifth-section obstruction.

## 6. Distinguish the fifth-layer coefficient space: a consistency proof

The exact earlier identification just cited gives J0(4)=P4⊗O(-2), hence H0(J0(4))=0 and H1(J0(4))=P4. These are cohomology groups of the weight-zero trace-free coefficient at physical twist four. Identifying a particular fifth-section gluing discrepancy with a class there still requires its actual transport law; it is not a consequence of a dimension count. In particular this four-dimensional space is distinct from the invariant line H1(J0(-2))^Γ governing κ.

Here is an independent structural derivation of that cohomology, retaining the extension instead of inferring it from dimensions. Let e∈H1(V⊗O(-8)) be the class of (4). It is nonzero. Otherwise a global lift of the constant diagonal quotient section would locally have the form [[1,0],[ell2,-1]]. A weight-zero lower-unipotent change of frame, using ell2/2, diagonalizes that section; all transformed T0 then commute with diag(1,-1), hence are diagonal. This would split the weighted leading transitions.

In those frames the actual global n8, of physical twist two, would have diagonal coefficient bundle Sym8U⊗O(-2) and lower coefficient bundle Sym10U⊗O(-10): subtract cover half-degrees four and five, respectively, and include the lower-Hom factor O(-7). Both have zero H0. Thus both entries vanish globally. But the lower entry is locally u(g5')², where g5'=g5+p2 f3 after the lower-unipotent change. Regularity of (f3,g5) implies g5' is not zero in any fiber, since otherwise g5 would be a multiple of f3. The base unit u is nonzero. This contradiction proves e≠0. This argument uses the actual n8 only through its already-proved regular leading pair, not through any evaluation.

Twisting (4) by four gives

    0 → V⊗O(-4) → J0(4) → O(4) → 0.

Its boundary δ:H0(O(4))→H1(V⊗O(-4)) is cup product with e. It is nonzero: if δ vanished on every h∈H0(O(4)), Serre duality would make e annihilate every tensor v*⊗hs with s∈H0(O(2)). Multiplication H0(O(4))⊗H0(O(2))→H0(O(6)) is surjective on P1, so e would pair trivially with all of V*⊗H0(O(6)), forcing e=0.

Now H0(O(4))=D5 and H1(V⊗O(-4))=V⊗A=P4⊕D5, where A=Sym2W and A≠V. The invariant extension makes δ equivariant. Since it is nonzero, Schur's lemma identifies it with the unique D5 summand, and the long exact sequence gives H0(J0(4))=0 and H1(J0(4))=P4. This independently recovers the known twisted coefficient result without asserting any value of an actual obstruction.

## 7. Exact whole-cone comparison dependency

For precision, the prior midpoint theorem concerns B_Q=End0(F_Q), not J or J0. Its “New deduction” and “Proof” establish that the actual bracket

    H1(Q,B_Q(-2))^Γ ⊗ C N → H1(Q,B_Q)^Γ

is nonzero between two invariant lines. At the midpoint in the affine line of first-normal extensions, the invariant N∈H0(Q,B_Q(2)) has a unique invariant trace-free lift to the midpoint adjoint on 2Q, and this lift squares to zero. The same theorem explicitly says that the midpoint bundle does not extend to 3Q: its obstruction is −c²/(4d)≠0. It does not assert a flat lifted spinor kernel or an ambient realization.

The missing comparison is therefore from that whole-cone normal-extension torsor, with its specified origin, to the weighted vertex class constructed here. Restriction and taking an associated graded layer require a verified map and compatibility with the local normalization/reference; the two one-dimensional invariant spaces alone do not establish an isomorphism, nonzero map, or matching actual value.

## Verification and scope

All identities used here are universal 2×2 triangular-matrix identities, homogeneous divisibility, and line-bundle cohomology. The character calculation is an abstract representation calculation, not selected actual HM/source-instance evaluation. No actual coefficients, points, derivatives, matrix ranks, source scans, or large computations were used. The proof is authored mathematics, not a proof-assistant certificate. The prior-source comparison above is targeted, not an exhaustive claim that every repository file has been searched.
