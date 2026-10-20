> Publication scope: preserved mathematical proof/audit. Historical statements that rank eight remains open are superseded only after the final assembly and all its prerequisites. No source-instance evaluation or formal verification is claimed here.

# Exclusion of the rank-eight branch and generic rank-one thickness five

## Statement and standing scope

Work over C in the canonical cubic-operation setup of the previously audited packet: dim V=5, dim J=20, the established N=H5 semidirect SL2(F5) equivariance, canonical square relation, repeated-input injection, and the associated quadratic normal-obstruction bundle map Q. Let r be the generic rank of Q on P(V). All conclusions below concern that setup and its established source/representation identifications.

Then r=10. The generic transverse local algebra of the rank-one component D of the cubic zero scheme has residue field K=C(D) and is isomorphic to

    K[e1,e2,e3,e4]/(e1,e2,e3,e4)^2.

Its Hilbert function is (1,4), its length is five, and its maximal ideal is nonzero with square zero. Thus the generic scheme multiplicity along this component is exactly five.

This is a structural deduction from the audited exclusions and a global sheaf bound, not an evaluation of the operation at a selected input. It does not assert constant rank ten at every point, determine the entire zero scheme, or establish higher extension/module quantization or any retained source value.

## 1. What the rank-eight alternative would produce

The audited two-length reduction in ../degree-fifteen-quintic-obstruction/TWO_LENGTH_COROLLARY.md and its audit leaves precisely r=8 or r=10. It incorporates the earlier exclusions of ranks four, five, six, seven and nine; these are inputs here, not new computations.

Assume r=8. The audited global kernel construction ../rank-eight-kernel-chern/PROOF.md gives the actual sheaf exact sequence

    0 -> O(-2) -> Ktilde -> K -> 0,
    B=K(2), rank B=2.

Its saturation and Chern calculations, followed by ../rank-eight-flat-kernel-exclusion/PROOF.md, exclude the flat endpoint and give a reflexive sheaf B on P4 with c1(B)=0 and c2(B)=5. The same argument proves slope-semistability; STABILITY.md strengthens it to slope-stability. Semistability alone suffices below.

The audited ../rank-eight-third-chern-bound/PROOF.md and invariant curve exclusions ../../rank-four/normalizer-small-curve-exclusion/PROOF.md and ADDENDUM_DEGREE_30.md (with AUDIT.md and DEGREE_30_AUDIT.md) force c3(B)=0 and a finite singular locus, using the support and effective-cycle identities of ../rank-eight-singularity-chern/PROOF.md and its audit. Here one uses the previously proved effectivity of the sheaf-Ext singular-curve cycle, so no positive-dimensional singular component is discarded merely on the basis of a numerical congruence. The Riemann–Roch obstruction rules out local freeness. In particular

    T=Ext²(B,O_P4)

is a nonzero finite sheaf. All Ext in this display and below denote sheaf Ext. These facts and the identification with the saturation defect are recorded in ../rank-eight-finite-image-defect/PROOF.md with its audit, after its explicitly conditional finite-singularity hypothesis is discharged by the curve exclusions.

The N-linearization and determinant trivialization are also established inputs. They are the hypotheses used by the local-defect and orbit arguments; they are not extra assumptions made solely for the contradiction.

## 2. A lower bound requiring only the earlier local exclusions

The independently audited ../rank-eight-defect-420/COROLLARY.md gives

    length T >= 420

in exactly this rank-eight branch. For this assembly it suffices to use the exclusions of canonical local lengths one through thirteen: a supported canonical orbit has thirty points and contributes at least 30 times 14. The established noncanonical orbit/defect bounds give no smaller contribution. Later exclusions raising this bound to 480 are compatible but unnecessary for the contradiction.

The local modules in this lower-bound argument are the stalks of the same finite sheaf T=Ext²(B,O). Thus there is no change of Ext convention, defect sheaf, twist-dependent length or support hypothesis between the lower bound and the next section.

## 3. The global upper bound applies to this same sheaf

The new independently audited theorem ../global-isolated-defect-bound/PROOF.md states:

    If B is slope-semistable reflexive of rank two on complex P4,
    c1(B)=0, c2(B)=5, and Sing(B) is finite, then
    length Ext²(B,O) <= 390.

Every hypothesis has been discharged in Section 1. The theorem allows singular B and properly semistable hyperplane restrictions. Its proof uses an actual bundle restriction to a hyperplane avoiding the finite singular locus, bounds the total first cohomology of that restriction, and telescopes the original sheaf's second cohomology. In particular, no stability of a restriction or unproved local-freeness of B is being inserted into the assembly.

The same nonzero T would therefore satisfy

    420 <= length T <= 390,

which is impossible. Hence r=8 is excluded.

## 4. Rank ten and the precise transverse conclusion

The prior exhaustive alternative r in {8,10} now forces r=10. The audited even-normal-form theorem ../rank-one-even-normal-form/PROOF.md identifies the generic local algebra along D with its quadratic graded normal algebra on four generators. The quadratic space has dimension binomial(5,2)=10. When the rank of the quadratic relation span is ten, that span is the entire space of degree-two forms. Its ideal is therefore the square of the homogeneous maximal ideal, and every degree at least two vanishes.

This gives exactly the algebra, Hilbert function and length stated above. The four-dimensional maximal ideal remains nonzero, so this component is generically nonreduced; its nilpotence order is exactly two. The isomorphism is an abstract K-algebra identification in normal coordinates, not a chosen global trivialization or a classification of special points.

## 5. Evidence boundary and independent review

The deduction uses the established canonical-operation identities and group representation identifications, the audited exhaustive rank alternatives, and the audited global restriction/regularity theorem. It selects the generic structural rank by contradiction, without executing or evaluating physical source operations, matrices, products, selected inputs, actual jets, residues or detectors.

It does not identify any actual higher obstruction value, prove a full formal module lift, settle mixed-direction compatibility, or provide a new algebraicity theorem. The connection and global quantization questions remain logically separate.

This file is an assembly proof written by the reviewer of the earlier packet. Its separate assembly audit is included in AUDIT.md; the upper-bound audit does not by itself certify the historical lower-bound chain.
