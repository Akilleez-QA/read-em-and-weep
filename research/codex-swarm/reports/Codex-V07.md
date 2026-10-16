> Worker proposal/review record. Acceptance and supersession are tracked in `../STATUS.md`.

# Codex-V07: exact obstruction and scalar-dual acceptance theorem

Independent cohomological reviewer; reviewer handoff: V08/I02. Scope: symbolic proof and tiny exact countercontrol only. No physical source arithmetic or dense oracle. Source pin 08b73637d4136f91606aad332c46cafd064417f8; paths below relative to research/hm/. Public discussion IDs refer to PR1. This report derives acceptance criteria; it does not certify missing evaluations.

## 1. Complete detector theorem (any field k)

Let C1 --B--> C2 --A--> C3 be finite-dimensional, AB=0, N=dim C2, b=rank B. Let L:C2->k^t satisfy LB=0. For a CLOSED v (Av=0), Lv!=0 implies [v]!=0. Conversely, all Lv=0 imply [v]=0 for EVERY closed v iff

rank([A;L])=N-b.                                           (C)

Proof: im B is contained in ker A intersect ker L. The latter has dimension N-rank([A;L]); equality of dimensions is equivalent to equality with im B. No conclusion uses merely a lower bound for rank. A verified upper bound N-b follows from LB=AB=0, so an authenticated nonzero minor of size N-b suffices for the remaining lower bound. Rank over a different field is not a substitute.

An alternative zero certificate is an explicit w with Bw=v, entrywise. This avoids dual completeness, but not the source-comparison obligation. For the pinned full-sign Q model, N=6560,b=2560,rank A=3648,dim H2=352, so (C) requires rank([A;L])=4000. Source: current-scalar-proof/checks/verify_finite_model.js:99-120. Its rank332 constant-scalar family plus ell has rank333, leaving19 dimensions; only evaluations actually supplied restrict the obstruction. Comments6104478488,6104582655.

Sector version: supply closed columns Z1,...,Zd spanning the relevant classes modulo im B, with rank([B Z])=b+d. If the actual [v] lies in this span, LB=0 and rank(LZ)=d suffice. For the characteristic-zero D8 epsilon sector d=32, use geometric naturality and full-sign choice independence (6130352358/6130391535), or explicit certificates; the finite-model action is corrected P rho(g) I. Naive harmonic permutation is invalid. Rank333 on352 does not determine rank on32. One ell has rank at most1 on32. The F3 perfect-complex dimension32 does not identify the HM bundle, authenticate obstruction specialization, or prove characteristic3 choice independence.

## 2. Source bridge and exact scope

Let r be the COMPLETE corrected closed geometric Rsharp, J its total End lift, C an authenticated regular cover comparison and P_A the finite chain projection. A candidate v must satisfy v-P_A C J(r)=B u (or an equivalent authenticated pulled-back dual identity for each row used). Domain, field, frames, full owners, partition powers, total signs and top J3 homotopy must match. D r=0 alone does not bind an arbitrary finite v to r.

For nonzero, one fully authenticated pairing suffices; for zero use a boundary witness or theorem(C)/sector version plus ALL evaluations. The78 staircase seeds are summands of ONE ell(n,z)=z[7]-z[25], not independent rows (6205341120). A nonzero summand need not survive assembly. The class represented in6205127744 is the full-sign component: vanishing there alone is not vanishing of every unprojected obstruction component. Baseline M0 must retain its gerbe terms; central pieces may be discarded only by the stated closed trace splitting, not individually.

## 3. Direct scalar dual: precise certificate

Use V0 --d0--> V1 --d1--> V2 from6206738230, with FULL homogeneous numerator spaces and all distinct common vertices; d1 d0=0, ker d1=im d0. For e in (V1)* satisfying e d0=0, finite-dimensional duality gives eta in(V2)* with eta d1=e. If s lies in V1 and d1 s=F, then e(s)=eta(F), independent of the primitive. Practical acceptance requires an exact identity eta d1=e on every V1 basis element (or a proved factored identity spanning the full space), and authenticated F,s admission. A solve on sampled demands is insufficient.

The public exactness proof uses a locally contractible augmented wedge-Koszul sheaf complex, acyclic nonempty numerator bundles, and H1(O(0,0,-2,-2))=0. H2 is one-dimensional, so d1 is not surjective onto arbitrary V2; F must be the actual exact source or carry its compatibility certificate. The FULL dual cocycle proves e d0=0; restricting it to lambda2/3/4 is justified on J of exact residuals, not on arbitrary intermediate cochains. Clipped Laurent boxes inherit neither exactness nor this proof. Actual eta rows/factored inverse and cost remain missing.

## 4. Executed independent countercontrol

Tiny exact Q elimination using Python Fraction, no datasets retained: B=(1,0,0,0)^t, A=(0,0,0,1), l=(0,1,0,0), m=(0,0,1,0), k=(0,0,1,0)^t. Checked AB=lB=Ak=lk=0; rank([B k])=2 proves k nonboundary. rank([A;l])=2<4-1 while rank([A;l;m])=3. The78 rows j*l (1<=j<=78) have rank1. Thus78 zero readings can miss a nonzero class. Also A rejects the noncycle e4 although l(e4)=0; e1* is an invalid detector since it does not kill B. These last two checks are direct displayed dot products, not claimed separate program tests.

Available-report audit: I01 correctly distinguishes one detector from completeness; V01 correctly calls its156 cells ownership, not rank; V03 retains full-source/gerbe/frame requirements. D01/D02/T01/T02/V08 absent at inspection: no producer acceptance claimed. Next: apply(C) or sector criterion to D reports and the exact eta identity/domain test to T reports. Original contribution: explicit iff rank certificate and executable tiny countercontrol; dimensions and finite-domain lemma are existing published inputs.


## 5. NEW: all constant scalar maps ARE complete on epsilon

Pinned current-scalar-proof/structural-relations.md:121-153 proves: S has2430 output rows, supported on negative n alone; pure-positive ker C/(T ker A) has dimension30-10=20, injects into H2, EVERY constant scalar map kills it, and this equals their entire common kernel K. This uses explicit vanishing, not dimension alone.

Pure-positive inputs have internal degree2, Cech degree0, constant O(0,0,0,0) coefficients. In genuine inclusion I_A=(1+H Delta)^(-1)i, H Delta i=0 because H lowers Cech degree below0. Thus I_A(0,p)=i(0,p), a GLOBAL constant section. Factor permutations fix coefficient matrices (6130306841) and diagonal constant chart cochains; no H1/Koszul sign occurs in degree0. Hence rho(g)i(0,p)=i(0,p), and corrected P_A rho(g) I_A fixes (0,p). Therefore the ENTIRE K is the trivial D8 representation.

For W=H2[epsilon], a=(12) acts by-1. Any x in K intersect W satisfies ax=x=-x, hence x=0 overQ. Thus S|W is injective, rank32 under the published dimension premise. All2430 scalar outputs zero for the authenticated actual epsilon class DO prove boundary. Only two maps being evaluated is insufficient. This provides theoretical completeness, not the missing source values or a smaller extraction schedule. No F3 transfer: rational kernel identity and geometric membership are premises. D02's13..32 bound is correct but weaker; D01's invariant witness extends to all K by this argument.

## 6. Code and arriving-report review

Read research/codex-swarm/check_contracts.py; ran ONLY normal and -O self-tests with -B, both pass. Boundary-column transpose rank, AB=LB rejection, completeness rank criterion, Laurent shifts/cancellation and reconstructed156 ownership cells are correct. No blocking defect found. Inputs to the Laurent identity must be integer exponent tuples. The4096-entry toy cap is not a hostile-input resource guard: conversion precedes it, bit sizes/empty-matrix column counts are uncapped. This does not affect these tests.

D01/D02 dual contracts and V08 boundary criterion are correct. T01 homotopy defect signs and extension/admission caveat are correct; T02 gauge and compressed-kernel identities check algebraically. These accept contracts, not an instantiated eta or source evaluation. The new theorem supersedes their restricted-completeness uncertainty only.
