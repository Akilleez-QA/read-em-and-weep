# Exact ten-source coverage for G3.11.ea6bced3bddf

## 1. Claim and immutable scope

The original stable label G3.11.ea6bced3bddf, source index 125, is impossible in the actual rank-three one-one endpoint setup. This is a coverage deduction from nine previously proved source exclusions and the direct ff obstruction below. It is not a new proof of those nine source exclusions.

The fixed endpoints are

    A_q=O(-10)+O(4)+O(16),
    B_q=O(-18)+O(-6)+O(8),
    original determinant defect=0.

All references to “original” mean the catalog snapshot at commit db51525015bb7c5e825833d550d08dedf6f6ea96 of Akilleez-QA/read-em-and-weep. Under research/hm/order-four-quadratic-load/, the two identity inputs are

- one-one-endpoint-necessary-pairs.json, Git blob fe0afa410d89340d3082dc814277f89fbb582c19;
- rank-three-quotient-frontier-144.json, Git blob 8b5971092f9ef762584912609fd5e9301c4e271d.

The first file's zero-based entry125 has exactly the ordered ten source tuples in Section 3. The second file identifies that entry with the displayed stable label, endpoints and original defect. Its historical status field is not rewritten or treated as a present-day status statement.

These catalogs are necessary overlists, not realizability assertions. The actual-source classification and endpoint-necessity statements are the files ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md and ONE-ONE-ENDPOINT-DEGREE-WINDOWS-AND-159-NECESSARY-PAIRS.md at the same commit, with Git blobs b93e0b3589ef71cf2c029fd07a6bdb1da8ba92b3 and dcacf0bcdef8377c1ed7654e5b82659ea409456e. Their necessary-overlist direction is all that is used: an actual source for this label must be one of these ten tuples. No sufficiency or realization inference is made.

The source-exclusion dependency files were read at the exact publication commits in Section 4, including the bb/bc proof at d679aa09811f821505254572a51e65b2904d03c9. The latter is no longer an unpublished conditional branch. A publication pin does not imply that its pull request has merged.

## 2. Exact source decoding and the direct ff obstruction

Use the conventions of the fixed actual-source classification: G is binary icosahedral over C, W is its defining two-space, Wp its other two-space, A=Sym2 W, S=Sym3 W, D=Sym4 W, T=Sym5 W, and V,P the other even irreducibles of dimensions 3,4. Write R(-j) for R tensor O(-j), and O(-j) for the trivial coefficient representation. All representations used here are self-dual.

For the ordered tuple (a,b,c,d,e,f,g,h), the exact actual-bundle decoding is

    E=((c+g+h-1)V+(d+e+g+h)P+(f+g)D)(-2)
      +(a Wp+b T)(-3)+(c V+d P)(-4)
      +e Wp(-5)+f O(-8)+g W(-9)+h O(-10).

Every row in Section 3 has rank 17 and degree -54. These checks concern just the ten listed tuples; no new source search is performed.

For ff=(0,0,0,0,0,2,0,1), the top coefficient is P+2D. The actual source is saturated in the ambient constant bundle and has H0(E(1))=0. The strict-top lemma, NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md at the original commit, Git blob d7506dae49b4be43230450c4132bd5db91f137ef, gives H0(E^-(2))=0. The actual derivative therefore induces an injective G-map

    H0(E(2))=P+2D -> H0(A_q(2)).

The negative O(-8) term of A_q(2) has no sections, while the two positive terms give

    H0(A_q(2))=Sym6 W+Sym18 W
              =(V+P)+(A+V+2P+D)
              =A+2V+3P+D.

Semisimplicity in characteristic zero makes such an injection impossible: the source has D multiplicity 2 and the target only 1. This excludes the entire ff source. It is an obstruction on global-section representations, not a claim that the source derivative is fiberwise injective. No connection-compatible splitting is assumed.

## 3. The complete ten-row slice, in original catalog order

The rows below equal the catalog's complete compatible_E_types list, with no reordering, omission, duplicate or additional row. Each displayed bundle is obtained by the decoding formula in Section 2.

| Row | Exact tuple (a,b,c,d,e,f,g,h) | Actual bundle E | Exclusion dependency |
|---|---|---|---|
| ff | (0,0,0,0,0,2,0,1) | (P+2D)(-2)+2O(-8)+O(-10) | Section 2 of this note |
| ef | (0,0,0,0,1,1,0,1) | (2P+D)(-2)+Wp(-5)+O(-8)+O(-10) | EF, whole-source conclusion |
| ee | (0,0,0,0,2,0,0,1) | 3P(-2)+2Wp(-5)+O(-10) | EE, Result and scope, Section 6 |
| cf | (0,0,1,0,0,1,0,1) | (V+P+D)(-2)+V(-4)+O(-8)+O(-10) | CF, whole-source conclusion |
| ce | (0,0,1,0,1,0,0,1) | (V+2P)(-2)+V(-4)+Wp(-5)+O(-10) | CE, whole-source conclusion |
| cc | (0,0,2,0,0,0,0,1) | (2V+P)(-2)+2V(-4)+O(-10) | CC, whole-source conclusion |
| bf | (0,1,0,0,0,1,0,1) | (P+D)(-2)+T(-3)+O(-8)+O(-10) | BF, whole-source conclusion |
| be | (0,1,0,0,1,0,0,1) | 2P(-2)+T(-3)+Wp(-5)+O(-10) | BE, whole-source conclusion |
| bc | (0,1,1,0,0,0,0,1) | (V+P)(-2)+T(-3)+V(-4)+O(-10) | BB/BC, Sections5-7 and Boundary |
| bb | (0,2,0,0,0,0,0,1) | P(-2)+2T(-3)+O(-10) | BB/BC, Sections4 and6 and Boundary |

## 4. Immutable whole-source dependencies

All paths below are repository-relative. COVERAGE.json records their commit, exact path, Git blob, canonical URL and explicit theorem-scope excerpts. Each immutable proof was read to verify the source tuple, bundle, original label, endpoints, defect and whole-source conclusion, rather than inferred from a PR title or a branch-local lemma.

- EE: PR846, commit 1644b5221fe6f8c23f30401fd6f2dc64230c0f5f, research/hm/profile11-o16-six-source-exclusions/PROOF.md, blob c62eb6cc2e5368f9a5364121fd9df4e67198f8d0. The result explicitly lists source125 tuple (0,0,0,0,2,0,0,1); Section 6 proves that ee source. This is not a nonexistent source125-ee path, and no other edge in that six-source theorem is counted here.
- EF: PR860, commit cdf1d9ae5e477ef5f541d92888059ceedb4fd9b4, research/hm/profile11-source125-ef-exclusion/PROOF.md, blob 75e46cbd8c56a9a969691663d34587825cb8eb71.
- BF: PR875, commit 01f835fda6e771351555f0af1fa11647c27eb01e, research/hm/profile11-source125-bf-exclusion/PROOF.md, blob 5c0ec54ce5d234780f16c20d41134c18a32e6417.
- CF: PR882, commit ef8ed8d457494608472a2c07de776e9162b2c20f, research/hm/profile11-source125-cf-exclusion/PROOF.md, blob b4ccaf9d3e5a77f0069664e86ae303a962e39442.
- BE: PR887, commit 3ab2f311ed2e87828d42c7c0ce0124bcd6e35771, research/hm/profile11-source125-be-exclusion/PROOF.md, blob 139ed6f19e5ab2ead6c9029e95e751ea132a0a49.
- CE: PR893, commit 7645e2458c3b85c5d814c22255dae8cabc7226bc, research/hm/profile11-source125-ce-exclusion/PROOF.md, blob fba1eb60737405f3ced37ab2d5542ca17eef20cb.
- CC: PR895, commit f720acbe80547fd1bccd5ff54e6b62a4daa41834, research/hm/profile11-source125-cc-exclusion/PROOF.md, blob d997b3822a32f33ab63ad8e3db27fcf043528bf7.
- BB/BC: PR906, commit d679aa09811f821505254572a51e65b2904d03c9, research/hm/profile11-source125-bb-bc-exclusion/PROOF.md, blob 2d6256b9b3350c0cecfadd022cdd302c216b37cb, SHA256 9d0ac1a9bfbd0bb1f30b42721d456f0ee7776b215c07b52648e62f416f90758c. Its scope and boundary explicitly exclude both full original tuples, including both quartic-component cases for bc. REVIEW.md at the same commit, blob 31fc9e225dc0c2201ba88520ff7b01d794a76b6b and SHA256 4cdb87817e8722602ce01ebf5db793b8db3e90b1fd9644941ed35e86626fe0d1, binds the independent whole-proof review to these exact proof bytes.

The proofs carry their own foundational dependencies and geometric arguments. Their whole-source conclusions, not just character tests or citations to another source's exclusion, are the inputs to this coverage deduction. The bb and bc rows share one proof file but remain two distinct original source tuples.

## 5. Exhaustion and boundary

Suppose the displayed original stable label were realized by an actual source. The fixed necessary catalog forces its splitting tuple to occur in the exact ten-row list. The ff row is impossible by Section 2. Every other row is impossible by its matching immutable whole-source theorem. This exhausts the necessary list and is a contradiction. Thus this original stable label is excluded.

This deduction removes no other label. It neither computes nor certifies a current frontier count, does not assert a global rank-four conclusion, and does not rewrite any original catalog. It does not strengthen any dependency's individual theorem beyond the exact source claimed there.

The bounded verifier checks immutable file identities, this one catalog entry and stable label, exact ordered ten-row coverage, decoding, ranks/degrees, dependency scope markers, the bb/bc review's byte binding, and the two fixed characters used in ff. It does not certify the truth of a proof by hashing it, repeat the published exclusion proofs, or replace their saturation, actual-connection, exact-sequence and branch-exhaustion arguments. Independent review of this assembly must additionally check the written application and exhaustion logic.

No selected actual HM/source coefficients, parameters, points, derivative evaluations, matrices, instance rank tests, experiments, scans or large computation are used. This is written mathematics with a bounded audit aid, not formal proof certification.
