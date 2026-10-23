# Independent verification of the Type I joint-annihilator gate

## Frozen artifacts and outcome

Reviewed on 2026-10-23. The reviewed proof and checker are:

- PROOF.md SHA256: `0957ba7fb53f03b99c98fe8d16fd00bdc000d264055d70018bfdac54345b96b9`
- verify.py SHA256: `e09d26412f7dddb87789670147184ee5bc141fa213f4c7328748cb8157f51a01`

Outcome: the new conditional deductions are valid relative to the nine pinned interfaces. No blocking mathematical issue was found. This review checks the new argument and the imported statements at the cited interfaces; it does not claim an independent reconstruction of the entire preceding geometric proof chain or proof-assistant verification.

## Checks of the new deductions

1. **Nonzero joint D channel.** The Type I constant radical consists of A,V,D scalar channels satisfying one linear equation with nonzero V coefficient. Thus the projection to the A coordinate is surjective. Since the actual Y spans A+V+D, a radical with nonzero A coefficient has an image whose constant span contains A. Naturality of the H1/Serre-duality identification, including its compatibility with the target summands, means zero D cohomology components imply zero bundle components into 2D O(-2). Factoring through P O(-2) would force the constant span to be a quotient of P tensor Sym2 W=V+P+D, which cannot contain A. This proves nonvanishing of the joint D action. Because the source has only one D copy, its common D kernel is zero. No assertion that every individual radical has nonzero D action is needed.

2. **Common kernels, not individual ranks.** The P contribution is precisely the kernel of the aggregate two-row map on a two-dimensional P multiplicity space. It has multiplicity 2-r. Adding the killed F and X summands gives Z=2V+(4-r)P+2D. The source kernel contains F2+X2; the only remaining multiplicity-free summands are P and D in Y2, yielding the stated epsilon/delta form. The direct decomposition is justified because radicals kill F2+X2, so their common kernel is this whole subspace plus the kernel of their restriction to Y2.

3. **Invariant-product consequences.** Under full-J compatibility, each radical preserves the actual kernel A+D and is square-zero. Equivariance and multiplicity-freeness force its restriction there to vanish. Hence the restricted Q has exactly that kernel, not merely a kernel of the same dimension. Constituentwise comparison forces delta=0. When r=0 the P target action vanishes globally, so Q-injectivity on the P source forces epsilon=1. These are actual compatibility consequences, not genericity claims.

4. **Surjective-row contradiction.** Stability of the common-annihilator subpencil under every negative quadratic follows from the actual pencil commutation identities. If restricted Q is onto, a right inverse produces a first correction staying in U and a second obstruction lying in im Q. Comparing this correction with the original canonical correction is legitimate because their difference lies in the original kernel and the imported entire first Bockstein is zero. Consequently the actual nonzero A-to-P second-symbol family rules out r=2 and r=1,epsilon=1. It need not be nonzero for each individual negative quadratic: the surjective-row argument would kill the whole family, which is enough for the contradiction.

5. **Surviving footprints.** The only remaining alternatives are (r,epsilon,delta)=(1,0,0) and (0,1,0). They give dimensions (32,28) and (36,32), with restricted kernel A+D and cokernel P. All dimensions and characters were independently recomputed from the displayed endpoint characters.

6. **Actual quotient invertibility.** On P, Qx in Z implies Q(j2x)=0 for every radical. P-injectivity gives j2x=0 and hence x in U; this proves injectivity of the induced quotient map. On D, surjectivity of the original Q onto its whole D-isotypical target gives quotient surjectivity. Equality of the corresponding quotient multiplicities now gives invertibility. Equality of characters alone would not have sufficed, and is not being used as that proof.

7. **Filtered cancellation orientation.** For M=[[A,C],[0,B]], the displayed p0, p1 and h satisfy p1 M=A p0, pi=1, hM=1-i0p0 and Mh=1-i1p1 by direct block multiplication, with no commutativity assumption on the blocks. B has invertible constant term, so B inverse is a formal power series and every map preserves all t-adic filtration powers. Thus the retained annihilator subcomplex is filtered chain-homotopy equivalent to the original complex; it is the quotient that is acyclic and cancelled. This identifies the original successive Bocksteins under the induced maps. In particular, the restricted cokernel P maps isomorphically to the original cokernel, and the same actual second symbol remains nonzero.

## Reproducible checks

Executed from this directory:

    python verify.py
    python -O verify.py

Both returned:

    PASS: 11872 exact checks; 9 immutable inputs; two conditional footprints.

The checker authenticates all nine input SHA256 and Git-blob hashes. Its finite matrices are synthetic controls for universal linear-algebra implications, not evaluations of HM instances. The scalar block tests support the contraction formulas; the general block argument above is the proof, including noncommuting blocks.

## Scope retained

The result is conditional on all of J being Q-compatible and applies only to Type I. It does not determine r, show det R is nonzero on the balanced locus, prove either surviving footprint occurs, exclude full-J compatibility, evaluate any actual HM coefficient or rank, extend an endomorphism to the full module, remove a source-dual pair, or complete the original proof repair. The two remaining conditional footprints and their common restricted cokernel are a new reduction, not a solution claim.
