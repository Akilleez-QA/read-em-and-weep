# Independent review: exact exceptional-jet local ideals and lengths

## Verdict and boundary

PASS. The two exact ideal identities in the packet imply the full local component ideals, not merely their orders or associated-graded dimensions. Together with the authenticated support and placement theorems, they prove exact total base-scheme lengths 46 on ell5 and 54 on ell3.

The statements concern nonzero members of two universal coefficient lines. They do not identify an actual source with either line, evaluate an actual obstruction, or establish occurrence of either branch.

Reviewed PROOF.md SHA256:

    bd474f4a0d1248a07854f22627aef4acc9faaac1fbfc4e14ffd2e25f3542e688

Reviewed verify.py SHA256:

    a7f0b2fd75c7e861cc86a9c2d7ab8566be69214e192044f563dbaa9f15ab0784

## 1. Fresh authentication and dependency scope

The reviewer independently fetched all four inputs through the GitHub connector at their exact commit and path. The returned UTF-8 bytes matched the retained files exactly, and the independently recomputed SHA256 and Git-blob SHA1 values matched INPUTS.json. The matching Git blobs are:

- PR1030, commit 418a7d9ebedaae9b5d00db9f69e449b5d8767108: aec4e3f550d3dc4bedb2911019de65e61852c436.
- PR1031 model, commit 7150cf97eeebe473bcd7c61c1f968c73625d92ef: a7ca4755e50c85fe7fc20a757125127a05de4056.
- PR1035 support theorem, commit 6effcd9b61b1942447a2c3f136a6776dda213c15: eb0b5dc78615331526b679eea952e4a46f7d01ea.
- PR1036 placement theorem, commit bb22e239e9423b54487236dba8c4f70f9e6b738f: 718f987511b5bf6144a85fc14e8ef343612a4491.

This authenticates the direct dependencies. It does not claim a fresh replay of every theorem in their transitive dependency graph. The reviewer also read the support theorem's relevant argument: on either jet line the prescribed multiplicities contribute at least eight to each involution-fixed line, and an additional off-conic orbit would add at least two, forcing a common line divisor of the nonics. The no-divisor theorem excludes that. This supplies exactly the off-conic support exclusion used here and does not depend on the new exact local lengths.

## 2. Normalization and coverage

The component rows F_i=N L R_i are the same determinant representatives already reviewed in PR1036. The alternating cofactor row N annihilates the quadratic second-symbol matrix B. The torsion-free rank-one target embeds via this determinant map, so its component ideal is the one under study, up to a common nonzero scalar. There is no new target normalization or change of coefficient basis.

The reduced ideals I5 and I3 on p=1 describe all six C5 axes and all ten C3 axes. Their displayed leading ideals give affine lengths six and ten, which equal their known global reduced lengths. Thus no axis is omitted at p=0. This coverage and the exact placement ell5=[1:2], ell3=[1:−2] were independently checked in the preceding placement review; the retained model and proof are unchanged.

After extending the coefficient field to its algebraic closure, localization of I5 or I3 at an indicated point is the point's maximal ideal. Ordinary ideal powers commute with localization. Hence the global affine ideal identities below yield the claimed local power identities at every geometric point, not only at rational points over Q(sqrt(5)).

## 3. Independent exact-ideal verification

The reviewer reconstructed B and N using iterative exterior multiplication of columns, independently of the production permutation determinant routine, and formed the full polynomial rows F1 and F2. The review then used graded reverse lexicographic order, rather than the production lexicographic order, over Q(sqrt(5)).

For each orbit, all products of a Groebner generating set were used to construct the required ordinary ideal powers. The reviewer adjoined the full unreduced nonic components to the higher power, rather than using the production reductions modulo that power. The reduced Groebner bases of the resulting ideal and the lower power agreed exactly. Both directions of ideal containment were also checked by normal-form reduction.

The independent results are:

    (F1+2F2)+I5^4 = I5^3,
    (F1−2F2)+I3^3 = I3^2.

Every component of the respective row belongs to the lower power. The independently computed quotient dimensions were 60 and 36 for I5^4 and I5^3, and 60 and 30 for I3^3 and I3^2. These dimensions are cross-checks only: the certification is equality of ideals, not equality of dimensions.

All calculations retain q and t as algebraically independent variables on an entire chart. The coefficient combinations are the already identified universal line generators, not selected coefficients of an actual source. No point or source instance is evaluated.

## 4. Why the finite identities determine all higher local terms

Fix one geometric axis and let R be its local surface ring, m its maximal ideal, and J the localized component ideal. The lower-power membership and the corresponding ideal equality give

    J ⊆ m^r,       J+m^(r+1)=m^r,

with r=3 on ell5 at a C5 axis, or r=2 on ell3 at a C3 axis. The module M=m^r/J is finitely generated because R is Noetherian. Multiplication by m gives

    mM=(m^(r+1)+J)/J=M.

Nakayama's lemma therefore gives M=0 and J=m^r. The argument applies in the ordinary local ring itself, hence also after completion. It does not require convergence, an infinite jet calculation, or an unjustified deduction from the initial homogeneous ideal. No undetected higher-order thickening remains possible.

Since R is a regular local ring of dimension two, the lengths are r(r+1)/2: six for m³ and three for m². These are scheme colengths, not the larger intersection multiplicities of a general pair of generators. Confusing those quantities would give incorrect totals; the packet correctly uses colengths.

At the other orbit, the distinctness of the two jet lines and PR1030's Nakayama conclusion already give the prescribed local ideal: m at the ten C3 axes on ell5, and the fixed length-four ideal of Z, with completed normal form (u²,v²), at the six C5 axes on ell3. No new coordinate choice at an actual axis is needed.

## 5. Exact support and totals

The newly proved local equalities alone would not justify global total lengths. The packet correctly adds both required support inputs:

1. PR1035 excludes every additional off-conic basepoint on either jet line.
2. PR1036 identifies the conic-base line as [1:0], distinct from both [1:2] and [1:−2], so neither jet line has any conic basepoint.

The fixed scheme Z already lies in every component base scheme, so all sixteen prescribed axes remain present. There is therefore no additional support, and the local lengths sum exactly to

    ell5: 6·6+10·1=46,
    ell3: 6·4+10·3=54.

This is a genuine upgrade of the previous lower bounds. It makes no claim that either line occurs as an actual source's gate or that the original fourth obstruction vanishes.

## Reproducibility

The bundled primary commands are `python verify.py` and `python -O verify.py`. The reviewer replayed both: all 26 checks passed with byte-identical output. The independent exterior-minor and grevlex calculations described above all passed; they are documented as executed cross-checks, not additional bundled executables. The written Nakayama and support arguments supply the geometric implications of the exact polynomial certificates.
