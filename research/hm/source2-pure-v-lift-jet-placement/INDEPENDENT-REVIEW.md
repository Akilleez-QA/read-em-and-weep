# Independent review: four distinct lines in the pure-V lift pencil

## Verdict and precise scope

PASS for the final statement and proof: in the fixed PR1031 basis, the two axis-jet lines are ell5=[1:2] and ell3=[1:−2], the conic line is ellDelta=[1:0], and the exceptional generic-rank-three line remains [1:−1]. These are four distinct points of the projective coefficient pencil, or equivalently four distinct one-dimensional subspaces of the two-dimensional gate.

The review preserves all conditional source2 pure-V hypotheses. It evaluates no actual gate coefficients and makes no source-occurrence, exclusion, or original-fourth-value claim. It retains the exceptional length bounds as lower bounds and the conic statement as an intersection statement, not a claim about transverse surface thickness.

Reviewed PROOF.md SHA256:

    f2a8368fc6abd45eb5120078b608af566539e5df70d66381acf939ac62ce81dd

## 1. Fresh immutable-input authentication

All five files in INPUTS.json were independently fetched through the GitHub connector at their stated commit and repository path. The returned UTF-8 bytes matched the retained local files exactly. Both SHA256 and Git-blob SHA1 were independently recomputed and matched the manifest. The matching blobs are:

- PR1030 proof, commit 418a7d9ebedaae9b5d00db9f69e449b5d8767108: aec4e3f550d3dc4bedb2911019de65e61852c436.
- PR1031 proof, commit 7150cf97eeebe473bcd7c61c1f968c73625d92ef: 0694e96e2d17a53b68d625ec6065f8bf513cd083.
- PR1025 proof, commit 09f1377f83b027ca27eea0b3a9f40a1b92c6c466: d036adcf5bc2bfc53e07cd752ff180c5993251f7.
- PR1031 model, commit 7150cf97eeebe473bcd7c61c1f968c73625d92ef: a7ca4755e50c85fe7fc20a757125127a05de4056.
- PR1033 proof, commit 7065160df56ffa7de1bea7e02c01dd98a6219781: 5625cb9e0a6ee2a53470616b82b3c93d76f0042b.

This is fresh authentication of the five direct dependencies, not a claim to have freshly replayed all their transitive geometry. The rank-pencil theorem and its model had also been independently reviewed before this packet.

## 2. The nonic target normalization is the correct one

Write B_a(h)=Pi(a²h), and let N be its alternating maximal-minor row. Independently constructing these minors by exterior multiplication of columns gives N B=0 identically. The row entries have degree six, and N L R_i has degree nine.

The exact source premise identifies the original second map with a nonzero scalar multiple of B. Changing that scalar multiplies all entries of N by one common nonzero scalar, so cannot change any coefficient line under discussion. The determinant map from coker B to O(6) is generically injective. Its kernel is torsion, hence zero because the imported cokernel is torsion-free. Its rank-one image is therefore the same embedded ideal-sheaf model used to represent the gate, up to a common scalar target normalization. Equivalently, two identifications of the double dual with O(6) differ by a scalar, not by a new direction-dependent factor.

Consequently F_i=N L R_i are the genuine component rows of the universal gates obtained through PR1025's unique lift isomorphism. There is no independent rebasing of F1 and F2 and no additional relative scalar that could alter the slopes [1:2] and [1:−2]. This also explains why the original second-symbol sign does not affect the answer.

## 3. Whole-orbit coverage and ordinary powers

The independently computed Groebner bases of the reduced C5 and C3 ideals on p=1 agree with those displayed in PROOF.md. Their leading ideals are respectively

    (q²,q t²,t⁴),          (q²,q t⁴,t⁶).

The standard monomials count to six and ten: respectively four plus two, and six plus four. Since the imported global schemes are reduced of those exact lengths, this affine chart covers all points. As a separate direct check, the reviewer set p=0 while retaining the remaining projective variable symbolically on each of q=1 and t=1. For both homogeneous ideals, both boundary-chart Groebner bases are [1]. Thus no point is hidden on p=0, independently of the length argument. These are entire symbolic charts, not evaluations at selected directions.

After passing to the algebraic closure, each reduced affine ideal is an intersection of pairwise comaximal maximal ideals. Therefore its ordinary kth power is the intersection of the kth powers of those maximal ideals. Flat extension preserves the membership tests over Q(sqrt(5)). It follows that membership in I5³ imposes precisely order-three vanishing at all six C5 points, and membership in I3² precisely order-two vanishing at all ten C3 points. There is no inappropriate replacement of an ordinary power by a projective symbolic power.

The power-quotient lengths 36 and 30 match six local quotients by m³ of length six and ten local quotients by m² of length three. These finite affine conditions are exactly PR1030's jet-kernel definitions: the lower jets already vanish because the gate targets I_Z(6).

## 4. Independent coefficient-kernel calculation

The reviewer separately formed all determinant rows by iterative exterior multiplication, rather than the production permutation routine, and independently formed the entire four-component rows F1 and F2. For each ideal power, the reviewer checked componentwise membership of the proposed exceptional combination and then assembled the full coefficient matrix of the two remainder rows over Q(sqrt(5)).

For I5³, the full remainder coefficient matrix has rank one and kernel spanned by (1/2,1). Thus it has exactly the projective kernel [1:2], not merely a single vanishing witness. Equivalently,

    rem(F2)=−(1/2) rem(F1),     rem(F1)≠0.

For I3², the full remainder coefficient matrix has rank one and kernel spanned by (−1/2,1), namely [1:−2]. Equivalently,

    rem(F2)=(1/2) rem(F1),      rem(F1)≠0.

The production nonzero coefficient witnesses are consistent with these full-row checks. Hence the two exact line equations are 2alpha−beta=0 and 2alpha+beta=0. All direction variables and all linear-combination coefficients remain formal; no actual gate element is selected.

## 5. Wronskian, dual convention, and full homogeneous conic check

The Wronskian of the invariant three-dimensional kernel of Pi gives a nonzero binary form of degree twelve. The group-stable Wronskian line is invariant because the binary icosahedral group has no nontrivial characters. Thus it spans the unique degree-twelve invariant line used by PR1033. The exact polynomial derived independently agrees with the displayed f12.

The conversion between a square factor u x+v y and its zero point is the symplectic coordinate substitution (u,v)↦(v,−u), up to overall sign. It is not valid to assert that an arbitrary coordinate change preserves this fixed invariant. The corrected proof instead uses the explicit pinned equality

    f12(v,−u)=f12(u,v)=f12(−v,u).

Every exponent in the displayed form is even, and its coefficients are symmetric under interchange of u and v, so this equality follows directly. The independent checker verifies it by simultaneous substitution. This resolves the factor-variable versus zero-point-variable normalization without a representation convention shortcut.

The reviewer then substituted the full formal square family (p,q,t)=(u²,2uv,v²) into the homogeneous nonic rows and performed exact two-variable polynomial division by f12. All four components of F1 have zero remainder, while at least one component of F2 has nonzero remainder. Thus the kernel of the full homogeneous remainder map is exactly [1:0]. This test does not depend on a single affine chart or on sampling the twelve points.

The production affine calculation gives the same conclusion. Its divisor f12(1,v) has degree twelve with nonzero leading coefficient, and each restricted component has degree at most eighteen. Exact divisibility therefore gives quotient degree at most six, which homogenizes to a genuine degree-six quotient. There can be no missed factor or exceptional point at u=0; directly, f12(0,1)=−2. The independent homogeneous division supplies a separate check of this step.

As further checks, the reviewer verified that f12(1,v) is square-free by its gcd with its derivative, and that the four sextic quotients of F1 generate the unit ideal on both charts of P1. Therefore their restricted component ideal is exactly (f12), with no extra zero and no extra multiplicity on the conic. The general dichotomy for other nonzero gate elements is the imported PR1033 result.

## 6. Consequences and non-consequences

At [alpha:beta]=[1:−1], the two jet functionals take nonzero values proportional to 3 and 1. The rank-three line therefore lies off both jet kernels. PR1030's full-stabilizer and Nakayama argument then identifies its local nonic base ideal with I_Z at all sixteen prescribed axes. The conclusion is local on that support and does not rule out additional points elsewhere.

At [1:2] and [1:−2], alpha+beta is nonzero, so PR1031 gives generic lift rank four. Each also has beta≠0, hence lies off the conic line. The rank-three line likewise lies off the conic line. The four coefficient points are pairwise distinct.

The length bounds 46 and 54 remain inherited lower bounds; the calculation does not show exact total lengths. Reduced intersection with the conic does not imply reduced ambient surface points. Nothing here computes an actual source's coefficient pair, decides whether its gate is zero, or identifies lift rank with rank of the original fourth row.

## Reproducibility

The bundled primary commands are `python verify.py` and `python -O verify.py`, run from this packet's directory. The reviewer replayed both: all 40 production checks passed, with byte-identical normal and optimized output. The reviewer also executed separate exterior-minor, full remainder-coefficient-kernel, homogeneous conic-division, projective-boundary, and residual-sextic calculations described above; all passed. Those methods are recorded here as independently executed checks, not as additional bundled scripts. The source-theorem geometry and target identifications remain justified by the written arguments and authenticated dependencies rather than by numerical experiments.
