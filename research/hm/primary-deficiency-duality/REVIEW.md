# Independent review: actual primary deficiency duality

Verdict: PASS for the structural mathematical deduction from the immutable inputs below. No mathematical correction is required. Reviewed 2026-10-21 UTC. This is independent mathematical review, not formal verification or a fresh proof of every upstream geometric theorem. No selected actual HM/source instance, coefficients, evaluation matrix, numerical rank test, large computation, or public write was used.

## 1. Evidence and dependency boundary

I read the entire final PROOF.md, including its homogeneous-ring deficiency Ext corollary. I independently retrieved these immutable repository proofs with the read-only GitHub connector and checked the statements used here:

- PR590, eb236dac3af8adcbc7f2f660b55e9d07904858c6, research/hm/degree-five-invariants/PROOF.md: the actual ambient-pullback N-linearization, the normalization sequence and conductor multiplication, the reduced one-dimensional node quotients, and the six five-point Heisenberg eigenline orbits.
- PR591, 64a12e00718ec4cb09f17473237e879b08b28e16, research/hm/normalizer-residue-signs/PROOF.md: r5=29 and the full N-triviality of the one-dimensional degree-five cokernel, not merely triviality under the Heisenberg quotient.
- PR589, a1c77f791158cc0976df80220c958a50c2217ee3, research/hm/eigenline-postulation/PROOF.md: node-ring Hilbert function (1,5,15,25,30,30,...) and actual restriction surjectivity in every degree at least four.
- PR592, 1a2822304e0e76d985f8a083fb36548127b881a1, research/hm/normalization-resolution/PROOF.md, Sections 6–7: the actual graded normalization resolution, H1(X,nH)=0 for every integer n, and the consequent H0(X,nH)=0 for n<0.
- Commit 80f302ddd7e0dd19f1c54b725f56e5f81bb47c69, research/hm/lower-conductor-ranks/PROOF.md and REVIEW.md: the complete exact ranks (0,0,5,15,25,29,30,30,...), together with the independent review of their representation-theoretic derivation. I retrieved and checked both files at this exact commit.

## 2. Residue functional and fiber pairing

The quotient T5/M5 is a one-dimensional trivial N-representation. Any nonzero identification with C is therefore equivariant, and its composite lambda:T5->C annihilates M5 and is unique up to one common scalar among functionals descending through this quotient.

Full N-transitivity on nodes follows from the Heisenberg transitivity inside each five-point orbit and the SL2(F5) transitivity on the six directions. Since N sends the summand supported at z isomorphically to that supported at gz, lambda-invariance makes its zero-restriction locus N-stable. Nonzero lambda and transitivity force every fiber restriction lambda_z to be nonzero. This argument needs no independent branch orientation or arbitrary simultaneous trivialization.

The reduced-support hypothesis is used essentially and correctly. T is a rank-one module over O_Z, so T(n) tensor O_Z(5-n) -> T(5) is an isomorphism on every node fiber. Composing with the nonzero lambda_z gives a perfect one-dimensional pairing at every node. Its direct sum is perfect for every integer n, including negative twists. The proof does not mistake T for an algebra or multiply two conductor residues; it only uses its O_S-module action.

## 3. Descent, degree zero, negative tail, and high degrees

For every integer n the actual normalization long exact sequence contains

H0(X,nH) -> H0(T(n)) -> H1(S,O_S(n)) -> H1(X,nH)=0.

Thus E_n=T_n/M_n, naturally as an N-representation and compatibly with ambient multiplication. In degree zero the preceding H0(O_S) and H0(O_X) terms do not create an extra extension: the cokernel formula is still exact. The separate r0=0 input then gives E0=T0 of dimension thirty.

For d=5-n>=0, a polynomial in I_Z acts trivially on T, so lambda(p t) depends only on p|Z. The perfect pairing with all of H0(Z,O_Z(d)) restricts to a surjection T_n->R_d^*. Every functional on the subspace R_d extends over that finite-dimensional ambient space. For t in M_n, actual O_S-linearity sends p t to M5. Consequently M_n lies in this surjection's kernel; no unproved identification of an abstract graded module with cohomology is being assumed.

The dimension comparison for n=0,1,2,3,4,5 is respectively

30,30,25,15,5,1 = dim R5,dim R4,dim R3,dim R2,dim R1,dim R0.

Together with the already established surjection and kernel inclusion, this proves the required kernel equality in every one of these degrees. In particular n=0 pairs against R5, not R0.

For n<0, the normalization module has no sections, hence M_n=0. Now d=5-n>=6, and R_d is the full thirty-dimensional fiber space by actual interpolation. The perfect pairing itself is therefore an isomorphism. For n>=6, the full conductor-rank input gives E_n=0 and the nonnegative grading gives R_(5-n)=0. All integer degrees are covered, and the thirty-dimensional tail for every n<=1 is genuine.

## 4. Grading, multiplication, and the complete normalizer action

With the stated conventions, (R^vee(-5))_n=(R^vee)_(n-5)=Hom(R_(5-n),C). The shift is -5, not +5. This independently fixes the potentially ambiguous grading sign.

For x in P1, the contraction action on R^vee(-5) is (x f)(p)=f(xp), where p has degree 4-n if f has degree n. Associativity gives

lambda(p x t)=lambda((x p)t).

This is exactly the commutative multiplication square required for n<=4. At n=5 both degree-six targets are zero, and higher source and target pieces vanish. Thus the maps assemble into an actual graded P-module isomorphism, not merely a match of Hilbert functions.

For every g in the full N, invariance of lambda and equivariance of multiplication give

Phi_n(g t)(p)=Phi_n(t)(g^(-1)p).

This is precisely the contragredient representation. The quotient's full N-triviality is indispensable here and is actually supplied by PR591. No determinant character or residual one-dimensional representation has been suppressed. As an independent central-weight check, the center acts on R_(5-n)^* by epsilon^(-(5-n))=epsilon^n, matching its action on E_n. The arbitrary choice of nonzero lambda only rescales the entire isomorphism by one scalar.

## 5. Annihilator, socle, dual cyclicity, and linear-form kernels

The stated annihilator proof is correct. I_Z kills T and hence E. Conversely, for a nonzero homogeneous class p in R_k choose f in R_k^* with f(p) nonzero. Its corresponding class in E_(5-k) is taken by p to a nonzero class in E5, because evaluation on 1 gives f(p). Since the annihilator of a graded module is homogeneous, this proves Ann_P(E)=I_Z for arbitrary polynomials too. It recovers the complete reduced projective node scheme, not just the number thirty.

For n<5, put d=5-n>0. If all linear forms kill f in R_d^*, then f vanishes on P1 R_(d-1)=R_d by standard gradedness, so f=0. Degree five is one-dimensional and killed by P_+; higher pieces vanish. Therefore the full P_+-socle is exactly E5, in degree five, with trivial N-action.

Each graded piece is finite-dimensional, so degreewise biduality is legitimate even though the module has an infinite negative tail. It gives E^vee=R(5), cyclic with generator degree -5 and relation ideal I_Z. Conversely, E cannot be finitely generated over the nonnegatively graded ring P because any finite set of homogeneous generators would impose a lower degree bound. It also cannot have finite length. The proof does not incorrectly assert cyclicity of E itself.

If ell avoids every node, it is a nonzerodivisor on the reduced coordinate ring R. Dualizing its injective degreewise multiplication maps yields surjectivity ell:E_n->E_(n+1) in every integer degree. Explicitly the kernel in degree n is dual to

(R/ell R)_(5-n).

The Artinian-reduction h-vector is (1,4,10,10,5), so the kernel dimensions in n=1,2,3,4,5 are exactly (5,10,10,4,1), with no kernel in other degrees. In particular multiplication is an isomorphism for every n<=0. An arbitrary avoiding ell need not be N-invariant; the proof makes no such assertion.

## 6. Added homogeneous-ring deficiency Ext corollary

I independently checked Section 6 of PROOF.md. For the finitely generated graded coordinate ring A=P/I_S, the all-degree Cech/sheaf comparison gives H^(i+1)_m(A)_n=H^i(Proj A,O_(Proj A)(n)) for i>=1. Taking i=1 gives H2_m(A)=E with the same multiplication action in every degree. Projective normality concerns a different, lower-degree part of this comparison and is not an assumption here.

Graded local duality over P, which has five variables and canonical module P(-5), gives the natural graded isomorphism

Ext3_P(A,P(-5))=(H2_m(A))^vee.

The index 3=5-2 and the canonical shift -5 are correct. This uses the degreewise graded dual, not the ungraded total vector-space dual; in this category it is an actual module isomorphism and no completion is missing. Combining with the verified duality above gives R(5), with generator degree -5 and annihilator I_Z, as claimed.

The primary P-linear statement is unconditional on equivariant canonical-module conventions. For the optional N-equivariant version, the canonical module carries the ambient determinant line. Here N has determinant one on the ambient five-dimensional vector space and therefore also on its dual P1, so that determinant representation is trivial; using its compatible trivialization makes graded local duality equivariant. The proof explicitly states this convention instead of silently discarding a determinant character. The added corollary therefore also passes independent review.

## 7. Contribution and exclusions

The proof genuinely identifies every multiplication map in the actual primary H1 module using the degree-five residue functional and the separately verified ranks. Its annihilator, socle, and homogeneous-ring deficiency Ext consequences are justified, and the negative-tail warning is necessary and correct. It neither determines I_S nor proves ambient restriction isomorphisms or arithmetically Cohen–Macaulayness. It does not resolve the separate full-adjoint K4 connecting map, prescribed-source membership, higher lifting, or algebraicity. The argument is complete from the stated immutable inputs.
