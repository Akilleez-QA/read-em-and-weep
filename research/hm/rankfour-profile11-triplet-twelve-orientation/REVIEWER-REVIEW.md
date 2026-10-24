# Independent entire-proof review

## Verdict and exact binding

PASS for the entire frozen PROOF.md, conditional on its explicitly retained actual-geometric hypotheses and the conclusions imported from the authenticated direct sources. No mathematical correction or unresolved proof issue was found.

The reviewed proof has exactly 12,396 UTF-8 bytes and SHA256:

    a9b56b6f84c9a11dedb94639bf16ab5c1065e21a91d067c52f75435d4b014da2

This verdict covers the statement, retained boundary, every section 1 through 6, and all displayed conclusions. It is not a verdict based merely on arithmetic checks or excerpts. I read the three COMPLETE direct source proofs and all verifier source before execution. Their transitive actual-geometric hypotheses remain assumptions; this review does not certify an unconditional realization of those hypotheses or reopen every transitive source.

## Independent source authentication

I independently fetched each pinned immutable GitHub path and, separately, each named Git blob through the GitHub connector. All six fresh responses matched the corresponding complete vendored bytes, lengths, SHA256 values, and independently recomputed Git blob SHA1 values. The direct sources were:

- Twenty-exclusion at commit 4c70887589bbb6f9ffe818575005268d82d14cf0; 16,366 bytes; SHA256 fc42728dd57303770e15c9ff2ffa7d490f4f6aa11dae26cf4cabdcb8792b0fa7.
- Defect-capacity at commit ca235151d5d93bbead2beffa7640fbd0741aec43; 16,069 bytes; SHA256 135c74cc09d4f1da1fcae16c330e0c9d5a9d05d615e59a2461dd532cbb91a62f.
- Projected-ranktwo at commit b2d020a32a3ac5aaf5f264e33e2f930c16195c34; 15,271 bytes; SHA256 7f1567617b78898bcd218107de5bac5a71342a4cb34411862f7342d13699c4bd.

REVIEWER-AUTHENTICATION.json records the exact requests and fresh comparisons. Author LOCAL records and INDEPENDENT-ORIENTATION-PROOF.md were not used as evidence.

## Whole-proof mathematical review

1. Assumptions and actual flag. The authenticated projected-ranktwo proof supplies the saturated common-ambient flag, ranks, degrees, actual adjacent quotient lines, and the normal bundle splitting. Its complete-versus-partial third-jet comparison, also stated in defect-capacity, gives B=J^- contained in Sym14 W(-4). Thus every nonzero subbundle of B has negative top degree. The twenty-exclusion source supplies the retained necessary set delta in {0,12}. The proof does not silently identify the incomplete actual coefficient system with the complete degree-eighteen system. The actual O(2) subline and O(10) quotient are respected: the upper cross-component from O(2) vanishes by invariant degree eight, and the reverse component vanishes by negative degree. The splitting is only equivariant bundle splitting. Restriction identity (6) is naturality of the ambient derivative followed by the actual quotient map, not differentiation of a quotient.

2. Coherent fullness of beta_B. Nonzero negative-degree B cannot be horizontal, and its derivative factors through a line, so its coherent image is O(10)(-D). Every backward kernel remains saturated in the original ambient: its quotient is the locally free coherent image on the smooth curve, and saturation is transitive through the ambient bundle. A nonzero stage cannot be horizontal because it lies in negative-top B. The induced coherent quotient maps Ri -> R_(i-1)(-2) have their stated exact kernels. Starting from rank one, their positive ranks are all one; rank eleven therefore gives exactly eleven quotients. Their degree sum is 11(10-e)-2(0+...+10)=-11e. Hence -60<=-11e, so 0<=e<=60/11<12. Invariance of D forces D=0. No saturation of an intermediate image was substituted into this inequality, and no theorem for a rank-seventeen bundle was transferred. The kernel H has rank ten and degree -70.

3. Exhaustion of degree-zero coherent image types. At delta=12, I is locally free of rank two and degree zero. The equal-degree possibility I=R O is genuinely treated: center-evenness makes the two-dimensional multiplicity representation factor through A5, whose irreducible dimensions force R=1+1. Both invariant Hom spaces to E vanish, excluding this case. For unequal degrees a>-a, the highest-degree line is canonical and equivariant. Absence of scalar characters identifies its linearization with physical O(a). A nonzero component into O(2) or O(10) then has nonnegative degree below twelve, so invariant-divisor minimality forces a=2 or a=10. The relevant extensions split equivariantly since H1(O(2a))=0 and the finite group is linearly reductive. The top line maps isomorphically onto the corresponding full actual normal summand. A coherent subsheaf containing the full kernel summand equals the preimage of its image in the quotient; this justifies the embedded equalities (14), not merely their abstract splitting types. Their remaining determinant divisor has degree twelve and is the unique reduced orbit D12.

4. Torsion restriction obstruction. In the rejected orientation, naturality gives phi(F)=O(10)(-D12). Reduction of the proven surjection phi modulo D12 is still a surjection B -> O(10)|D12, and it kills F, so it factors equivariantly through B/F=O(4). The resulting Hom space is H0(O(6)|D12)^G. The invariant divisor has physical degree-twelve linearization because any difference is a scalar character, of which there are none. Its exact sequence has left term O(-6). Exactness of finite-group invariants places the desired invariant space between H0(O(6))^G and H1(O(-6))^G. Equivariant Serre duality uses K=O(-2) in the determinant-one convention and identifies the latter with the dual of H0(O(4))^G. Both groups vanish by the fixed physical identities. Therefore the factor map is zero, contradicting torsion surjectivity. The opposite orientation survives, with precisely cyclic length-one torsion at the twelve orbit points. This is a sheaf obstruction using coherent fullness, not just a generic-rank argument.

5. Common-kernel incidence and saturation. In the surviving case, phi|F is onto O(10). With H=ker phi and G9=F intersect H, this gives F+H=B and the two exact quotient sequences in (19). Both degree calculations give -74 for G9: -64-10 and -70-4. Its rank is nine. Saturation is valid: G9 is the kernel of the surjection from saturated F to the locally free line O(10), and hence is saturated in the original constant ambient. Equivalently, it is the intersection of the two saturated common-ambient subbundles. Pulling back the exact kernel O(2)(-D12)=O(-10) of I -> O(10) along the surjection F -> I gives (20), with F^- rank eight and degree -64, consistent with -76+delta. No intrinsic jet identification of G9 or H is needed.

6. Contribution and boundary. The unconditional conclusion is coherent fullness of the actual beta_(J^-). The conditional conclusion is the unique lower-normal defect orientation at delta=12, with the stated actual common-kernel incidence. Neither delta=0 nor delta=12 is asserted realized or excluded. The original defect t=0 remains distinct. The retained F18 types, dual-extension alternatives, other image branches, original higher-jet separation, whole-profile exclusion, and algebraicity remain outside this result. All numerical conclusions in the statement agree with the proof and the imported data.

## Isolated selected-only replay

After reading REPRODUCE.md, verify.py, and characters.py completely, I copied exactly the eight prescribed files into a newly empty temporary directory. No LOCAL file, exploratory note, reviewer record, prior output, or cache was copied. Both commands were executed with bytecode writes disabled:

    python verify.py
    python -O verify.py

Both exited zero, reported PASS and 45 explicit main checks, and reported the exact frozen proof hash above. The imported character module also executes its 81 fixed exact-rational McKay identity checks. Explicit require calls remain active under optimization. The replay contained exactly the same eight files afterward; every selected byte was unchanged both in the original source directory and the isolated replay. REVIEWER-REPLAY.json records the selected-file hashes, commands, outputs, and comparisons.

The checker performs only fixed universal character and degree arithmetic plus exact-byte authentication. It does not prove the actual-geometric arguments; the separate entire-proof review above supplies that audit. No selected actual HM coefficient, parameter, point, jet, tensor, matrix, instance rank, or normalization was evaluated. No broad scan, large computation, quotient connection, horizontal splitting, rank-seventeen transfer, or GitHub write was performed.

## Final decision

PASS. The entire frozen proof and both requested replay modes are independently reviewed and bound to the exact proof hash. No correction is required for the stated result.
