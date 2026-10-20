# Ownerwise literal residual and block-sensitive lift bounds

## Result and scope

The exact frozen raw residual admits the carrier vector **(11,16,11)** on its three original owner occurrences `(i,j,k)`. With the established conservative transition legal allowance two, its legal vector is **(11,16,11)** as well, so the literal residual has uniform carrier/legal bound **16/16**. This improvement uses owned primitive carrier bound two, raw block bound 5/1, and ordinary exact derivative semantics. It does not need the proposed sharper transition legal theorem.

Using the independently accepted all-chart transition legal-one theorem, the same calculation gives the sharper legal vector **(7,10,7)**, and hence **R <= 16/10**. All seven kinetic terms, three gerbe terms, two Fk terms and eight E summands remain present. No transition cocycle, inverse cancellation, curvature cancellation, or residual closure is used.

Using also the independently accepted source-bound inclusion increment 4/1 and legal-free homotopy theorem with whole-projector carrier bound two, the literal lift is more sharply bounded than uniform padding suggests. Its actual block supports give

    J0 <= 16/10, J1 <= 19/10, J2 <= 22/10, J3 <= 24/10.

The full J3 vectors on its six ordered original occurrences are

    carrier: (24,22,19,16,16,11),
    legal:   ( 8,10,10,10,10, 7).

These are sufficient certificates, not assertions of exact attained pole orders. The transition/inclusion and homotopy improvements use the independently accepted pinned dependencies below; the residual carrier result stands separately. The retained raw-block, complementary-stripping, exact-derivation and assigned-sheaf assumptions remain explicit. The supplied metadata checker is not their proof.

The clearing exponents remain **54/29**, and the standard allowance remains **5251**. This is a new mathematical bound, not a changed partition, program, source evaluation, detector run, or Ward/residue calculation.

## 1. Frozen source and retained hypotheses

The inert source snapshots are unchanged from the authenticated sources:

- [Compiler](https://github.com/Akilleez-QA/read-em-and-weep/blob/491306fd2f7f8a04c29784afa48a6cb8a467f154/research/hm/null-raw-regular-extension/inputs/compiler.py.txt), SHA256 `28e95b87adefaba0d4ec886a7ab272f252f376bbb1fc26e0a387bc05f896a386`.
- [Raw engine](https://github.com/Akilleez-QA/read-em-and-weep/blob/491306fd2f7f8a04c29784afa48a6cb8a467f154/research/hm/null-raw-regular-extension/inputs/raw_engine.py.txt), SHA256 `c9804022b362277d63217c7674c4d6d3dff5941ae4210c30f51f3b5cf3868da9`. These bytes are also the original [e93cf712 source](https://github.com/Akilleez-QA/read-em-and-weep/blob/e93cf712f9da4926a8450cc870ed45a7bfc379ab/research/codex-swarm/detector-realization/raw_engine.py).
- [Complete-residual source authentication](https://github.com/Akilleez-QA/read-em-and-weep/blob/560645be183e1fbb1029983319295e4a77f08984/research/hm/null-complete-residual-lowering/PROOF.md) and the archived [raw-domain proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/491306fd2f7f8a04c29784afa48a6cb8a467f154/research/hm/null-raw-regular-extension/PROOF.md).

The local dependency snapshots preserve the homogeneous primitive theorem, raw block proof, cancellation-free residual proof, and accepted transition/inclusion and homotopy improvements. The accepted transition proof has SHA256 `b4c3041e8f945df65518f37dd59f92e16d6cd8cc29fd9803d8576daf7c9b99c8`; the accepted homotopy proof has SHA256 `d3b1471814a153f931eedc2309e162195fe3fdbe649dacd6d74ebf85cddd01c3`. Their independent review snapshots and exact dependency hashes are included. They are never imported or executed. Their substantive assumptions are retained explicitly:

1. Each unweighted I or P entry is cleared on all standard charts by the square of its OWN homogeneous carrier. Its actual homogeneous weight and physical frame interpretation are the established ones. Eta is cleared by its own carrier to the first power. H0 and H1 are cleared by its square.
2. The raw B block at owner a has simultaneous bound 5/1 at a alone, including the physical moving-frame and old-connection terms on every chart. The same normalized q on an edge has carrier zero and legal allowance one at an actual endpoint present. Padding the other endpoint with one is permitted below. No absent endpoint supplies a factor.
3. The actual invariant derivatives and the complementary stripped scalar derivatives have the retained exact, all-chart quotient-rule semantics. A derivative raises each participating positive allowance by at most one; a missing owner remains missing. The scalar derivative directions in E are complementary to the scalar pair. The mixed derivatives in the source are distinct-coordinate derivatives.
4. Rational coefficients denote sections of the assigned sheaves in the correct transported frames. This geometric attribution, raw closure, HPL class identities and any obstruction interpretation remain distinct obligations. Local adjugate pole arithmetic does not alone establish sheaf gluing.

No new public-source read is claimed by this packet; it authenticates the previously fetched inert snapshots. No physical model is imported, constructed or evaluated.

The exact raw route matters: `source_and_lift` instantiates `RawSource(model.M)` and `SC.Lift(model.M,source.residual,...)`. Here `model.M` is the raw engine's `Mat`; `Mat.inverse` is the entrywise rank-two adjugate and `Mat.D` applies the exact field derivation V entrywise. Therefore D(g#) is bounded by differentiating the adjugate entries themselves. This packet does not silently use the same literal-word estimate for `compiler.Circuit.D`'s different formal inverse branch, which expands an inverse derivative as `-g# (Dg) g#`. Identifying or simplifying that distinct formal representation would need its own semantics. The source signatures and wiring to the raw Mat route are statically bound by the checker.

## 2. Occurrence algebra, without owner merging

For an ordered occurrence list T, use two vectors C and L. The certificate means clearance by

    product_(v in T) H_v^(C_v) product_r ell_(v,r)^(L_v).

The legal coordinate L_v is a conservative common allowance for the four legal sections at v. Finer direction-specific legal bookkeeping is unnecessary here. Each occurrence, rather than its carrier label or polynomial divisor, is the index of a vector entry.

For addition, align occurrence lists and take the coordinatewise maximum. For an ordered product, align the lists and add coordinatewise. Trace, transpose, constant multiplication and entry selection do not increase the certificate. An absent occurrence has zero allowance. A rank-two adjugate merely permutes and negates entries and preserves the certificate. Derivatives retain the existing owner support and increase its allowance by at most one.

When the same selected occurrence occurs twice in a word, add both charges at that occurrence. When two distinct occurrences happen to have the same carrier, legal mask, or divisor, keep two vector entries and multiply both clearing factors. At a prime divisor their multiplicity-weighted charges add; a maximum across distinct occurrences is not allowed. Repeated labels therefore do not invalidate the argument, and do not improve its bound by themselves.

This is the specific improvement over the former scalar-pair ledger: P_i I_j needs H_i^2 H_j^2, not H_i^4 H_j^4. No cancellation is involved in keeping those two owners separate.

## 3. Transition, raw scalar, and derived edge inputs

Write lambda for the transition's legal allowance at EACH endpoint: lambda=2 is the established conservative case; lambda=1 uses the independently accepted physical root-frame theorem. The exact source is

    g_ij = D_j (P_i I_j)^t D_i^-1.

The diagonal physical factors introduce no carrier. Thus the edge certificate for g and its implemented adjugate is `(2,lambda)` at i and `(2,lambda)` at j. The new transition theorem directly proves the stronger carrier factor H_i^2 H_j^2 before padding to its advertised uniform carrier four. The same owned factor also follows directly from the unweighted I/P theorem and carrier-free physical factors when retaining lambda=2.

The source's edge-derived objects, at EACH of their two actual endpoints, have:

| Object | Carrier | Legal |
|---|---:|---:|
| g, adj(g) | 2 | lambda |
| Dg, D adj(g) | 3 | lambda+1 |
| distinct D2g | 4 | lambda+2 |
| k | 6 | 2lambda+2 |
| u=gk | 8 | 3lambda+2 |
| Du | 9 | 3lambda+3 |

For k, each summand is a product of two first derivatives. For Du the two complete Leibniz types are (Dg)k and g(Dk), and both have the displayed bound. The complementary Dk differentiates exactly one of the first-derivative factors, so its carrier/legal bound is 7/(2lambda+3) at each endpoint. No derivative factor is dropped.

The raw scalar source, not the N14 solver, is used. In each of its four resolution-block terms it contains

    tr(B_i,a B_j,b)-tr(B_i,b B_j,a),
    q_a [tr(B_i,b)+tr(B_j,b)],
    q_b [tr(B_i,a)+tr(B_j,a)],

and finally a scalar multiple of q_a q_b. The integer weights and signs change no denominator. Consequently the source-owner vectors on edge (i,j) are

| Raw scalar family | Carrier | Legal |
|---|---|---|
| B_i B_j | (5,5) | (1,1) |
| q B_i | (5,0) | (2,1) |
| q B_j | (0,5) | (1,2) |
| q q | (0,0) | (2,2) |
| whole s_ij | (5,5) | (2,2) |
| complementary D s_ij | (6,6) | (3,3) |

Every endpoint and every raw block remains present. Charging carrier ten separately to both endpoints is unnecessary: no literal scalar monomial contains two B factors at one endpoint. The legal bounds intentionally allow q at both endpoints, although its actual pole is allocated more precisely in the raw-domain proof. The derivative estimate is the retained all-chart complementary derivative statement, applied to this sharper SAME-owner carrier clearance; it does not invent an extra infinity factor.

## 4. Full literal triple ledger

Put A=g_ij, B=g_jk, G=g_ik, and write # for the implemented adjugate. No relation G=BA or G#G=Id is imposed. All vectors below are aligned to `(i,j,k)`.

The literal scalar b is a constant multiple of q_(a,ij)q_(b,jk), so its legal vector is bounded by (1,2,1) and its carrier vector is zero. This may overcount different coordinate legal factors, but is valid for the common-per-coordinate allowance used here.

The curvature scalar and E currents are exactly

    F=b-tr(G# mu(B,A))/2,
    L_d=A# D_d A,
    U_d=A# B# (D_d B) A.

The following table gives every literal normalized residual family. A row saying 'two' or 'four' counts the source slots before expanding their fixed alternating bidifferentials; each such expansion has the displayed bound.

| Literal source family | Count | Carrier vector | Legal vector |
|---|---:|---|---|
| G# u_jk u_ij | 2 | (10,16,10) | (4lambda+2,6lambda+4,4lambda+2) |
| G# mu(u_jk,A) | 2 | (5,12,11) | (2lambda+1,4lambda+4,4lambda+3) |
| G# mu(B,u_ij) | 2 | (11,12,5) | (4lambda+3,4lambda+4,2lambda+1) |
| G# mu2(B,A) | 1 | (6,8,6) | (2lambda+2,2lambda+4,2lambda+2) |
| G# b u_ik | 2 | (10,0,10) | (4lambda+3,2,4lambda+3) |
| G# b_p b_q G | 1 | (4,0,4) | (2lambda+2,4,2lambda+2) |
| F | auxiliary | (5,6,5) | (2lambda+1,2lambda+2,2lambda+1) |
| F k_ik | 2 | (11,6,11) | (4lambda+3,2lambda+2,4lambda+3) |
| L_d | auxiliary | (5,5,0) | (2lambda+1,2lambda+1,0) |
| U_d | auxiliary | (4,9,5) | (2lambda,4lambda+1,2lambda+1) |
| (D s_jk) L_d | 4 | (5,11,6) | (2lambda+1,2lambda+4,3) |
| (D s_ij) U_d | 4 | (10,15,5) | (2lambda+3,4lambda+4,2lambda+1) |

For clarity, in the first row the two u factors share j. Their carrier charges there add to 8+8=16, while the outer G# contributes only at i and k. This is exactly why (10,16,10) is valid and a maximum across all factors would be invalid.

Similarly U has two A occurrences, one B# and one DB. Its j carrier charge is 2+2+3+2=9, its i charge is 2+2=4, and its k charge is 2+3=5. Ds_ij adds (6,6,0), giving (10,15,5) without a cocycle-current simplification.

F is bounded directly from its literal b and normalized mu summands. For lambda in {1,2}, its normalized-mu legal vector dominates b's (1,2,1). Thus no historical F14/1 certificate is used.

Taking coordinatewise maxima across the complete residual yields

    C_R = (11,16,11),
    L_R = (4lambda+3,6lambda+4,4lambda+3), lambda=1 or 2.

Therefore lambda=2 gives (11,16,11) legal, and lambda=1 gives (7,10,7). Trace-free projection can only add diagonal trace terms already having these entrywise bounds. No trace cancellation is invoked. Individual residual branches are not claimed to be closed.

## 5. Exact leading-owner lift

This section is conditional on lambda=1, inclusion increment 4/1 at its selected owner, and the legal-free homotopy theorem giving E=IP carrier/legal 2/0 as a WHOLE morphism. The identity E=Id-gamma H0-H1 delta is its separate established basis; we never evaluate or expand IP.

The source begins with the sole block

    J0(t)_(1,1)=I_(t0) R(t)^t P_(t0).

Consequently its exact certified vector is

    C_J0=(15,16,11), L_J0=(8,10,7).

The inclusion adds only at the first occurrence. The uniform bound is already 16/10, since the middle residual allowance exceeds that first-owner addition. Padding this operation at every occurrence would lose this information.

For a vector x of length n, let Delta(x) be the coordinatewise maximum of its n+1 embeddings into an ordered length-(n+1) tuple with one position deleted. This is a bound for the alternating Cech difference. Delete a displayed vertex only for that face; retain every owner previously selected by any factor in that face's expression. No selected owner is dropped from its expression's certificate. The operation introduces no new divisor.

If an operator adds a at the selected first owner, it transforms Delta(x) into Delta(x)+a e0. This remains valid for repeated physical labels, because these operations address tuple occurrences, not carrier names.

The exact homotopy source has only two block branches:

    (u,v)->(u,v-1): h_v F, if v>0;
    (u,v)->(u+1,v): (-1)^r E F h_(u+1), if v=1 and u<3.

It follows by inspection of these predicates that

    J0 support: (1,1)
    J1 support: (1,0), (2,1)
    J2 support: (2,0), (3,1)
    J3 support: (3,0).

Every v=0 block is killed by the next homotopy. Thus the only path that contributes to J3 is

    (1,1) --E(-)H1--> (2,1) --E(-)eta--> (3,1) --H0(-)--> (3,0).

Its successive added carrier charges are 4,3,2, each at that stage's actual leading owner, with legal charge zero. The middle charge is 2+1 because eta has its own-carrier bound one. No H0I, PH1 or other side-condition cancellation is used.

Applying the face-embedding rule gives the complete block ledger:

| Stage/block | Carrier vector | Legal vector |
|---|---|---|
| J0 (1,1) | (15,16,11) | (8,10,7) |
| J1 (1,0) | (17,16,16,11) | (8,10,10,7) |
| J1 (2,1) | (19,16,16,11) | (8,10,10,7) |
| J2 (2,0) | (21,19,16,16,11) | (8,10,10,10,7) |
| J2 (3,1) | (22,19,16,16,11) | (8,10,10,10,7) |
| J3 (3,0) | (24,22,19,16,16,11) | (8,10,10,10,10,7) |

The recurrence permits different deleted faces at each stage. Delta takes the maximum across ALL those choices, so this is not a calculation on only one face chain. Scalar signs do not affect upper bounds. Literal source `Lift.at` requires distinct tuple objects; the divisor argument also covers different objects carrying equal physical labels and divisors. 

Two conservative corollaries are useful for comparison. Ignoring block support but retaining selected-owner positions and the uniform homotopy increment4/0 gives J3 carrier vector (27,23,19,16,16,11), legal (8,10,10,10,10,7), hence27/10. Padding every operation uniformly gives32/11. Both are valid weaker consequences. The sharper24/10 uses the source's exact block predicates and eta bound, not a smaller unproved homotopy bound for arbitrary inputs.

## 6. Extension and unchanged weights

The new vector certificate is a product of homogeneous clearing sections at the original occurrences. The same retained assigned-sheaf and all-chart assumptions imply regularity after that product; normality supplies the extension exactly as in the cancellation-free raw-domain proof. The proof does not replace a homogeneous bundle degree by an affine numerator degree.

For J3 a convenient uniform mathematical certificate is

    C'_v=H_v^24 product_r ell_(v,r)^10,
    D'_v=C'_v product_r Z_(r(v),r)^5251.

The assigned full-sign coefficient twist remains -5 in each coordinate. Its cleared degree in coordinate r is therefore

    sum_v(24 deg_r H_v+10 deg_r ell_(v,r)+5251)-5.

One can instead use the displayed position-specific vectors, retaining their ordered occurrence positions. The uniform24/10 certificate is simpler for a position-independent statement. This optional certificate does not alter any program's actual denominator weights or arithmetic representation.

The unchanged partition has C_v=H_v^54 product_r ell_(v,r)^29 and rho_v=C_v Q_v on its own standard chart. Since C_v/C'_v is a regular product, these same weights also factor rho_v=C'_v Q'_v with Q'_v regular. The original cleared-suffix proof applies, using the FULL original input tuple's standard target and the original target-tag correspondence. Inserted weights clear inserted owners only; the original suffix owners must still be cleared. Absent standard tags cannot be borrowed. J3 has six occurrences and its Cech boundary has seven, with retained face owners. No six-owner boundary bound is claimed.

For the independent lambda=2 residual result, the same existing 54/29 clearing exponents remain unchanged; this packet does not need a smaller lift consequence from that fallback to prove domination by the previously established domain.

## 7. Verification boundary

`check_owner_ledger.py` authenticates the inert compiler/raw bytes, checks source AST contracts, and evaluates only finite integer owner vectors and block-support metadata. It never imports either source, executes a model constructor, multiplies actual matrices, expands primitive polynomials, evaluates a source or jet, computes a coefficient.

The checker includes active controls rejecting a missing normalization, max-instead-of-add at a shared owner, a dropped U factor, an omitted E endpoint, merged equal-divisor occurrences, a dropped leading-owner charge, false eta order zero, changed homotopy block predicates, a raw scalar with a same-endpoint B square, and changed clearing exponents. Normal and optimized runs agree. These checks bind the proof to the frozen wiring; they do not establish the imported all-chart inputs or general program semantics.

The new mathematical content is the source-owner vector derivation, the explicit scalar endpoint decomposition, and the block/face-sensitive lift proof. Residual attribution and closure, Ward or residue identities, arithmetic realization, coefficient detectors, final cohomology or obstruction values, remain outside this packet.
