# Ten regular algebraic observations cannot isolate source membership

## Scope and immutable input

This is a conditional structural strengthening of the linear-detector bound in PR894, not a physical detector construction or an actual-source evaluation. Work over C under all hypotheses of:

https://github.com/Akilleez-QA/read-em-and-weep/blob/c963b48d8bd28eaac1dc2db1116fc1c430ba18b4/research/hm/physical-source-membership/PROOF.md

That theorem identifies the canonical-correction defect space

    M=Hom_G(Sym^3 A tensor D5,I), dim M=27,

and an affine surjection Omega from the 34-dimensional cohomology space of supplied closed W-families to M, with seven-dimensional fibers. Source membership is equivalent to Omega(W)=0. Closedness, complete coherent polynomial-family authentication, preceding canonical division, canonical correction and the actual global-complex comparison remain prerequisites. The error is defined in cohomology before membership, not by applying a trace outside its certified domain.

PR894 proves that a LINEAR detector M->C^10 has kernel dimension at least17. Here regular algebraic nonlinear maps are allowed, and the corresponding zero-fiber obstruction persists.

## 1. Local regular-detector theorem

Let U be any Zariski-open neighborhood of 0 in M. Suppose

    Phi:U -> C^m

is a regular algebraic map, with Phi(0)=0. There is no linearity assumption. Then the local dimension at 0 of the scheme-theoretic zero fiber is at least 27-m. In particular, if m=10, it is at least17 and 0 is not an isolated zero. Thus Phi(x)=0 cannot be equivalent to x=0 on any Zariski-open neighborhood of 0.

### Proof

The local ring R=O_(U,0) is Noetherian of dimension27. Write f_1,...,f_m in its maximal ideal for the component germs of Phi, and J=(f_1,...,f_m). Put d=dim(R/J). Choose a system of parameters of R/J with d elements and lift them to R. Together with the m generators of J, their lifts generate an ideal whose radical is the maximal ideal of R. The minimum number of generators of such an ideal is at least dim R. Therefore 27<=m+d, proving the claim.

The commutative-algebra input is the system-of-parameters characterization in the Stacks Project, Proposition10.60.9:
https://stacks.math.columbia.edu/tag/00KD

Equivalently this is the local dimension consequence of Krull's height theorem, Lemma10.60.12:
https://stacks.math.columbia.edu/tag/0BBZ

Dimension is unchanged by passage to the reduced zero fiber. Since the fiber is of finite type over C, positive local dimension implies that every Zariski-open neighborhood of 0 contains nonzero closed points of that fiber. Hence the obstruction concerns actual abstract complex defects, not only infinitesimal or nilpotent directions.

## 2. Consequence for supplied W-families

Assume such a detector is independently defined on the defect neighborhood U and accepts a packet exactly when Phi(Omega(W))=0. With m=10, it necessarily accepts incompatible defects in every neighborhood of the compatible defect0, unless further admissibility restrictions remove them. This conclusion does not assume that a physical trace detector factors through Omega; that factorization and regularity would require their own proof.

The accepted cohomology-W locus has local dimension at least24 near every compatible W. Indeed any affine surjection with seven-dimensional kernel is, after an abstract affine linear change of coordinates, the projection M times C^7 -> M. The inverse image of the zero fiber is therefore locally its product with C^7. Its dimension is at least17+7=24, while the genuinely compatible W-fiber has dimension7. This is an existence/structure statement, not a choice of any actual cochain, coefficient, source, parameter or splitting for a physical packet.

Thus replacing a ten-channel linear test with ten nonlinear REGULAR ALGEBRAIC zero conditions cannot cure the membership blind space on the unrestricted sector of PR894. This conclusion is stronger than a tangent-space or Jacobian argument: no derivative rank is evaluated, and singular or identically zero observation components are allowed.

## 3. Sharpness and limits

The numerical bound is sharp for abstract regular maps: a coordinate projection from a27-dimensional affine space to a10-dimensional affine space has a17-dimensional zero fiber. This example describes an abstract linear map, not selected HM data or a claimed physical observation.

The regular-complex-algebraic restriction is essential. A nonholomorphic real-valued test involving complex conjugation, such as the sum of squared absolute values of all27 coordinates, vanishes only at0; it is not a regular map to C. Discontinuous or set-theoretic encodings, inequalities, algorithmic branching, and additional independently authenticated restrictions on the defect locus are likewise outside this theorem. No assertion about all conceivable nonlinear tests is made.

A detector with fewer than27 scalar regular coordinates cannot isolate0 on this full27-dimensional sector. Having27 or more is merely necessary for such isolation, not sufficient to authenticate a physical detector or its references. Complete cohomology-family observations as in PR900 are not compressed into ten scalar coordinates, so this theorem does not contradict their separating interface.

The result does not construct a primitive, prove physical globality/equivariance, calibrate a norm, exclude any geometric source, establish a higher-order lifting result or solve the underlying algebraicity problem. It only rules out a precisely specified class of low-dimensional regular algebraic membership zero-tests under PR894's full-family hypotheses. No actual-instance computation or new numerical test is needed.
