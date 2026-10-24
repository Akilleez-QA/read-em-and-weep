# Independent whole-proof review

## Verdict and identity

PASS, with no correction required to the reviewed proof.

- Proof: PROOF.md.
- SHA256: e5d2c74f516bb5b2ede85287fceb3a774c6870b68b7b2418398e30fd5093d9b2.
- INPUTS.json SHA256: fedb86c38f2f59cdaf9f7d61a6f69d94987f64033ad105bb318ad9d7f3d319e7.
- Independent review completed on 2026-10-24, UTC.

The new conclusion is a genuine conditional exclusion of the scalar-positive primal quotient O(2)+2O(4)+O(-8) in the original actual rank-four maximal-(1,1) setting. Among the four imported small-dual forms, only A_std(-8)+W'(-11) survives. This is not a realization theorem for the W-positive branch, a triplet-branch exclusion, or closure of the full profile. The original determinant defect remains twelve.

## Source authentication and scope

I read the complete new proof and all four complete retained sources: the original actual presentation, the actual top-four pair image, the actual second-jet residual theorem, and the universal principal-parts source. Each of the four inputs was independently fetched anew through GitHub fetch_file at its exact immutable commit. Complete UTF-8 byte equality, length, SHA256, canonical URL, and both returned and recomputed Git blob SHA1 were verified. REVIEW-AUTHENTICITY.json records those comparisons, binding them to this proof and manifest.

I also read the accepted pair-defect and intrinsic-first-jet endpoint source texts as transitive context. In particular, the endpoint statement L^-=O(-10)+T6(-3) repeated near the end of this proof agrees with that accepted theorem. The new proof does not use any triplet-specific flag from the principal-parts input: only its universal construction is imported. The original actual-geometric premises remain assumptions, rather than being reconstructed from numerical characters.

## Review of the ambient and constant-span obstruction

The character of H is obtained from the actual presentations, not guessed from its dimension. The first presentation gives chi(E)=-M4, the dual second presentation gives chi(S*)=M3 tensor W-M2, and the actual sequence 0->E->H O->S*->0 gives H=M3 tensor W-M2-M4. The computed result is 2A_std+2V+2P+2D.

The actual map E->(H/C)O factors through E/E0=O(-8). Since E spans H, its coefficient map onto H/C is surjective. Both its source Sym8 W and target have dimension nine; hence H/C=P+D. This justifies C=2A_std+2V+P+D without presupposing a horizontal source decomposition.

The fact that S0 spans C* is also justified: any constant vector annihilating S0 lies in the actual annihilator E0 and gives a constant global section there. Negativity of E0 excludes that section.

Crucially, the coefficient bound for M is not the arbitrary coefficient space of the abstract bundle A_std(-8). The imported theorem identifies the very embedded M with the exact second osculation of U=O(-10). A constant subspace containing U contains its derivatives, and U is contained in M. Therefore span(M)=span(U), a quotient of Sym10 W. The latter contains precisely one A_std. In form II the equivariantly split extension supplies actual complements to this specific M. Their degree-six and degree-sixteen coefficient spaces contain no A_std. Their sum cannot span a constant representation with two A_std copies. This exclusion is valid and does not require any complement to be horizontal.

## Review of the genuine seven-space

The initial equality G_D intersect K=S4(-3) follows from the actual quotient row and its saturated injection into F. Its upgrade to G_D^-=S4(-3) uses the genuine constant connection: the derivative modulo G_D factors through (E0/G_D)(-2), whose top degree is -5; no map from pure degree -3 can land there. Conversely, projecting the derivative of G_D to the ambient quotient by E0 gives the opposite kernel inclusion.

For every successive kernel, the derivative factors through the preceding rank-one quotient twisted by -2. All bundles in question are saturated in the genuine constant ambient. Vanishing would make a negative subbundle horizontal, impossible in characteristic zero. The relevant equivariant Hom spaces are one-dimensional; their nonzero generators are the canonical binary evaluation rows, all everywhere onto. This proves the actual full flag down to O(-6), rather than merely matching characters of potential kernels.

The reverse derivative steps everywhere recover G_D as the fourth osculation of this actual O(-6). Thus their constant spans agree. Its coefficient span is a quotient of Sym6 W=V+P, and must have dimension at least rank(G_D)=5. Semisimplicity leaves only dimension seven, forcing the actual coefficient isomorphism Sym6 W->J_D.

Under that specific isomorphism the whole osculating inclusion is the standard complete sextic inclusion. Its annihilator inside J_D* O is W(-5). The physical Euler line O(-6) in that W(-5) consists of sixth powers, so its composition into J_D* O is the full dual Veronese line. Its annihilator is consequently the canonical T6(-1) evaluation kernel. This is the indispensable embedding-sensitive step; it is proved, not inferred from an abstract W(-5) splitting. Transport by the actual coefficient isomorphism and its dual preserves all these annihilator identities.

## Review of apolarity and the O(-18) exclusions

The map q:C->H0(O(10)) is a constant linear map obtained from the actual line U. The jet evaluation map is the O-linear extension of jets of those constant sections. Its dual image is exactly the actual M. Since E0 annihilates M, q(E0) lies in the universal second-jet kernel Sym7 W O(-3). This does not apply a differential operator to variable coefficients of a section of E0, and does not assume that q is complete.

The actual G_D has pure degree -2, so its map to that pure degree -3 kernel vanishes. Constancy of q then kills the entire actual span J_D. Both U and its derivatives, and hence M, annihilate J_D as a constant space.

Restricting S0 to J_D therefore gives an actual map pi:S0->W(-5) that kills M. The zero-map case is properly handled: it would put J_D O in E0 and contradict H0(E0)=0. In either remaining O(-18) form the residual quotient is O(-4)+O(-18), irrespective of whether the original extension is split. The O(-4) restriction row vanishes by ordinary degree. The other Hom is one-dimensional, and multiplication by the nonzero invariant f12 followed by the same physical Euler inclusion is a nonzero generator.

The coherent image is allowed to have zeros along the divisor of f12. The proof does not identify that image with its saturation. It uses instead that multiplication by f12 is injective on a line bundle over the integral smooth curve. Therefore a local pairing annihilating f12 times the Euler line annihilates the Euler line itself. The two images have exactly the same annihilator sheaf.

It follows that the genuine T6(-1) inside J_D O annihilates S0, and therefore lies in E0=(S0)^perp. This is a nonzero sheaf inclusion, which ordinary degree forbids because top(E0)=-2. Both forms III and IV are excluded. The argument includes both zero pi and nonzero torsion-image possibilities.

## Independent executable checks

review_verify.py is independently written and does not import characters.py or verify.py. It uses exact conjugacy-class characters over Q(sqrt(5)), closed physical SU(2) traces and class sizes, orthogonality, and reconstruction. Its scope is bounded to the fixed identities required by this proof, through symmetric degree sixteen. It checks:

- The exact H and C characters and dimensions.
- Sym6 W, Sym10 W and Sym16 W and the decisive A_std multiplicities.
- The unique initial cubic-to-D inclusion and the four successive canonical evaluation Hom dimensions.
- The actual-flag rank/degree arithmetic and the four semisimple quotient dimensions of V+P.
- The two residual restriction Hom dimensions, the invariant degree-twelve multiplicity, and the Euler composition degrees.
- Principal-parts, annihilator, and surviving/excluded bundle rank/degree identities.
- The exact frozen proof hash, required manifest, all four immutable source identities and hashes, and the fresh-authentication record.

The normal and optimized executions both pass and produce byte-identical JSON, with 382 checks. Standard output contains JSON only. All checks use explicit RuntimeError and remain active under python -O. In separate temporary copies, eight negative controls were tested: removal of the manifest, alteration of the proof, alteration of an input, and alteration of the authentication binding, each in normal and optimized mode. Every test failed closed with a nonzero exit, RuntimeError, and no successful JSON on stdout. The accepted packet files were not modified during those tests.

Run:

    python review_verify.py
    python -O review_verify.py

These bounded calculations support the conceptual review; they are not a proof-assistant certification of sheaf theory or imported actual geometry. No actual coefficients, parameters, points, jets, tensors, matrices, instance ranks, broad candidate scan, public write, merge, or upstream submission was used in the review.
