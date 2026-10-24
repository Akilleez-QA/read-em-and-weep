# Independent whole-proof review

## Exact object and verdict

**PASS, conditional on the complete retained actual-geometric hypotheses.** I independently read the entire frozen `PROOF.md` (9,703 UTF-8 bytes), SHA256 `06e1795f1390e8451dbf4e98e10a8011b3e97ce733ec6b1cbbd5af90b4694111`, and both complete direct input proofs. No mathematical revision or additional hypothesis is required for the claims actually made in that exact proof.

The reviewed conclusion is the actual rank-six common kernel, its unique equivariant scalar complement, its exact coherent derivative image and backward kernel, its saturated forward span, and its own fifteen-dimensional constant span. It is not a conclusion about intrinsic auxiliary ramification, full auxiliary coefficient span, realization, exclusion of the residual branch, or any later original jet.

## Independent source authentication

I freshly fetched each entire pinned input through both the immutable commit/path API and its independently requested Git blob API. I compared all bytes of each response with the corresponding local file, and independently recomputed the UTF-8 length, SHA256, and Git blob SHA1. All four fresh source representations match their complete local inputs exactly.

- PR1218: commit `f5895c822322b4ddab07e51a97874d4528fb5b88`; path `research/hm/rankfour-profile11-triplet-rankseven-equality/PROOF.md`; 15,139 bytes; SHA256 `a6e56f535af652d3ff437cc5041527636f601751ae24285ba1ec91670f4db7ae`; blob `6a4ef8941ee4cee131992bdf9cd7657635b058c5`.
- PR1216: commit `66a6bfe8dd424da58f3d775be1818d1f4f71eff1`; path `research/hm/rankfour-profile11-triplet-nine-jets/PROOF.md`; 12,744 bytes; SHA256 `44ee429fa26b65b68b2668ce69dff219e4a4daf0a6bdaa9fac0e94aa8a631b3a`; blob `916cc6a3bc1cf8ad07e019f00a1f5ebf867311d6`.

Detailed byte comparisons are in `REVIEWER-AUTHENTICATION.json`. This is independent fresh authentication, not reliance on the author's saved fetch output. The transitive sources remain hypotheses as expressly stated; this review does not claim to have freshly authenticated the entire transitive dependency graph.

## Mathematical audit

### 1. The actual quotient columns are correctly identified

PR1218 Section 7 supplies actual U3 inside Q1, actual U4 inside F6, U4 intersect Q1 equal to U3, and the actual lower-line image of U4 in R0. U3/Q2 is the lower O(-12) in R1, so Q1/U3 is its upper O(-10) quotient. This is an assertion about the retained embedded flag, not merely the unordered splitting type of R1.

The map R1 to R0(-2) is an everywhere isomorphism. Its upper-to-lower component has negative degree, and its lower-to-upper component would be an invariant degree-two section. Both vanish, so its two diagonal scalar maps are invertible. In particular the Q1/U3 quotient maps isomorphically to the upper O(-10) in R0(-2). There is no column interchange or forgotten twist.

PR1216 supplies B7=B6^- and the full O(4) derivative target of B6, with ranks and degrees 8,-84 and 7,-88. The restricted upper map on F6 has coherent image O(-8), not O(4).

### 2. Transversality and the scalar complement are valid

The actual upper kernel sequence has quotient O(-8), hence G6 has rank six and degree -80 and is saturated. Q1 and U4 both lie in this kernel. The surjection of U4 onto the lower coherent line identifies U4/U3 with G6/Q1. Therefore Q1+U4=G6 as sheaves, not only generically, and their intersection is exactly U3. This proves the actual direct-sum quotient G6/U3=(Q1/U3) direct-sum (U4/U3)=2O(-10), and G6/U4=O(-10).

In characteristic zero the finite-group invariant functor is exact. Thus the relevant equivariant extension group is H1(D(-4))^G, whose Serre-dual invariant space is Hom_G(D,Sym2 W). It vanishes. Ordinary Hom(O(-10),D(-14)) vanishes by degree, proving uniqueness of the splitting section, not merely existence of an abstract splitting type. Its image is the highest-degree line because the other summand is pure degree -14. All of these statements retain the given embedded U4.

### 3. The normal splitting retains the required actual subline

The flag G6 inside F6 inside B6 gives the exact normal extension of O(4) by the actual F6/G6=O(-8). Its equivariant extension group is H1(O(-12))^G=(Sym10 W)^G=0, and the splitting section is unique because Hom(O(4),O(-8))=0. After twisting by Omega=O(-2), the first O(-10) is consequently the actual internal normal subline, while the O(2) summand maps isomorphically to the external quotient. Nothing in this argument assigns a connection or horizontal structure to either summand.

G6 inside B7=B6^- ensures that its derivatives lie in B6. Hence this rank-two normal bundle is sufficient; no other ambient normal direction has been suppressed.

### 4. The two projections prove the full coherent image

Derivatives of Q1 lie in F6. The preceding actual quotient-column isomorphism makes the internal component of beta_G6 on Q1 coherently onto O(-10), with zero external component. Thus the image contains the full actual internal summand.

Naturality identifies the external projection with the lower projection of beta_F6 on its upper kernel. That coherent image is exactly O(2)(-D12), and U4 already surjects onto it. A subsheaf containing the internal summand and surjecting onto this external subsheaf equals its full inverse image: locally, subtract a lift of the external coordinate, and the difference is internal. Therefore the asserted image equality is a sheaf equality, not only an equality of generic ranks or splitting degrees.

The normal quotient is precisely O(2)|D12. Because D12 is reduced, the internal direction is full and the external inclusion has a simple zero at each point of D12. Tensoring the surjection from G6 to its locally free coherent image is still surjective. Consequently the derivative has fiber rank one on D12 and two elsewhere. This correctly distinguishes the rank-two coherent image from its rank-deficient fiber embedding.

### 5. The exact kernel and forward span follow without auxiliary overreach

U3 has derivatives in its actual next jet bundle U4 inside G6. Hence U3 is in the exact intrinsic kernel. The induced surjection G6/U3 to the coherent image is between locally free sheaves of equal rank two, and is therefore an isomorphism; the degree -20 agreement is consistent. The exact kernel is U3=S4(-15), with degree -60, not merely a subbundle of that rank or an equality away from D12.

The coherent image saturates to the entire actual normal bundle (B6/G6)(-2). By the definition of saturated forward transform, G6^+=B6. The full-span argument is also actual: a constant functional annihilating G6 annihilates its derivatives, hence B6, while the converse is immediate. Since ann(B6)=T6=Sym6 W(-12) has no global sections, B6 and G6 span all fifteen constant dimensions.

The last conclusion belongs to G6 as a whole. The extra actual scalar complement prevents any inference that U4 or its degree-eighteen scalar source must have the same span. The proof correctly leaves that question open.

### 6. Boundary and unresolved component

The proof does not infer intrinsic auxiliary ramification from a projected defect. The derivative of U4 may have a component in (F6/U4)(-2) which is invisible in the external projected defect. No assertion that this component vanishes is used in any argument above. It is therefore correct not to import the earlier ramified forward-climb exclusion.

Both rank-seven image alternatives, both quotient M alternatives in the direct input, original delta=12, the separate e9 endpoint, algebraicity, occurrence, and whole-branch/profile exclusion remain undecided. The proof makes no new original higher-jet claim beyond the retained order-nine result, no rank-seventeen transfer, and no quotient-connection argument.

## Complete checker inspection and isolated replay

I read all of `REPRODUCE.md`, `verify.py`, and `characters.py`. The executable checks are explicit raises, not Python assertions, and remain active with optimization. They authenticate the frozen proof and complete inputs, check fixed small universal character identities, and check displayed exact-sequence degree arithmetic. The imported character module checks 81 fixed exact-rational McKay identities. The selected mathematical calls do not use a chosen actual source instance or perform a candidate scan.

I copied exactly the seven files listed in the reproducer to a newly empty directory. No saved fetches, other drafts, outputs, or caches were included. I removed inherited PYTHONPATH and disabled bytecode writes, then ran the verifier normally and with -O. Both returned exit code zero and identical PASS output with 35 explicit verifier checks. Every selected file's bytes and SHA256 remained unchanged, and exactly seven files remained present after both runs. `REVIEWER-REPLAY.json` records the commands, outputs, all seven hashes, and the isolation details.

The replay is a bounded consistency check, not a substitute for the geometric audit above. No GitHub writes were performed. No selected actual coefficient, parameter, point, jet, tensor, matrix, instance rank, or normalization was evaluated, and no unapproved large computation was performed.
