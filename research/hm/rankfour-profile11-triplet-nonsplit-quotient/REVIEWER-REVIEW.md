# Independent entire-proof review

## Verdict and exact object reviewed

PASS. I find the theorem and every section of this proof mathematically valid, conditional on precisely the retained actual-geometric hypotheses and the complete immutable direct inputs. In that residual simultaneous rank-seven, original delta=12, k=2 case, the actual extension M=F6/U4 is necessarily nonzero and has equivariant middle-bundle type W(-9). This is a whole-proof verdict, not a verdict inferred from a passing checker.

The verdict binds the complete 13,619-byte PROOF.md with SHA256

    d4ff280dc943c2a112ea68ff4d9c4750fe5f93b3892d8a104fa9c08aa5960568

Its Git blob SHA1 is 1974a5c3b20546dcb414539096511388f495cdab. I read the entire proof, both complete direct inputs, INPUTS.json, REPRODUCE.md, and all of verify.py and characters.py. No frozen file was edited. No mathematical flaw requiring correction was found.

## Fresh independent source authentication

I made new read-only GitHub fetches myself, independently of the author's source-fetch record. For each direct input I fetched its complete immutable repository path in base64 and its Git blob independently, decoded the complete responses, and compared their bytes with the complete local input. All three byte strings agree for each input.

1. PR1219, commit 95137a91303d46fd945f5a2d0fed330f0e32df8c, path research/hm/rankfour-profile11-triplet-ranksix-common-kernel/PROOF.md: 9,703 bytes; SHA256 06e1795f1390e8451dbf4e98e10a8011b3e97ce733ec6b1cbbd5af90b4694111; Git blob 5661a972f1eccce29a49ea4b1af305c693a380b2.
2. PR1221, commit 84b418e22f03b5718409bdeb23ae353ecc4eb681, path research/hm/rankfour-profile11-triplet-mixed-jet-pairing/PROOF.md: 14,593 bytes; SHA256 3e1ce0d1589d694d578796a90398cbdaf8fdf6fb340158b5098ad3f79cdfa95b; Git blob 91e0c23867113c0a7d5b032098c8e365b356859d.

The path responses report the same Git blob SHAs, and the independently recomputed Git object hashes agree. REVIEWER-AUTHENTICATION.json records the exact fresh tool arguments, immutable source URLs, complete-byte results, and selected-file hashes. The fresh raw response record is local evidence only and must be excluded from publication and replay. No author fetch record was used. Transitive actual-geometric assumptions explicitly inherited by the two originals remain assumptions; this review does not claim a new audit or authentication of unspecified transitive files.

## Review of the complete direct inputs

I read all sections and conclusions of both originals, rather than just extracting their headline statements.

PR1219 retains the actual saturated flags, identifies G6 as the kernel of the actual upper derivative projection with its coherent O(-8) target, and gives G6=U4 direct-sum L10 relative to the specified U4. Its Ext vanishing and degree-based uniqueness justify the actual canonical L10. Its later splitting of B6/G6 retains F6/G6 as the internal O(-8) line. Its two derivative projections, coherent-image calculation, exact kernel U3, forward span B6, and full span of the entire G6 are mutually consistent. In particular its lower image is O(2)(-D12)=O(-10), not the saturated O(2). Its full-span statement for G6 is not a full-span statement for U4 or its scalar source.

PR1221 constructs the actual h, rather than inserting a chosen self-duality. Its mixed-jet rectangle and diagonal derivative recurrence give diagonal multiplicity twelve. The two residual invariant biforms are symmetric. The coefficient-operator factorization, unique Clebsch-Gordan summand, order-six transvectant symbol, rational Wronskian bound, and representation gap give exactly the original four-dimensional kernel, then the nondegenerate symmetric h and the auxiliary full span. The nonzero f12 component follows from the existing kernel and the nonzero biform. Its transfer of actual original jets through order nine is justified only after h is constructed. Its final at-most-two embedded-kernel statement does not select an actual eigenline or establish realization. These complete arguments support the specific imports used in the new proof and do not silently enlarge its scope.

## Section-by-section mathematical audit

### Statement, scope, and Section 1

The theorem is expressly conditional on the residual simultaneous image and k=2 flag. It excludes one formerly retained quotient, not the simultaneous image or a whole branch. The use of U5=Sym5 W(-13) is supplied by the subsequent mixed-jet theorem; it is not inferred from the earlier span statement about G6. The given U4, L10, G6, F6, and B6 are actual embedded objects. Their ranks, degrees, and coherent quotient columns agree with the inputs. The notation for the fixed six-dimensional representation and the actual sixth jet is distinguishable by context; no representation identification is inferred from the notation alone.

### Section 2: the orthogonal quotient and its norm

The order-twelve diagonal vanishing gives all pairings of jet orders totaling at most eleven equal to zero. It therefore makes T5 isotropic and puts T6 inside its perpendicular. Saturation of T5 and nondegeneracy of h give an everywhere surjection from the constant bundle to T5*, so its kernel and the induced quotient H are vector bundles. The induced form on H is nondegenerate, with rank three and degree zero.

The line N=T6/T5 is saturated in H: the quotient of T5-perpendicular by T6 is torsion-free, as it embeds in the quotient of the constant bundle by the saturated T6. The mixed derivative of orders (6,6) has exactly the claimed surviving term. All twelve derivatives must fall on Omega^12, giving a nonzero universal factor; Omega^18 cannot contribute. Lower-jet changes have zero contribution. Thus the restricted norm is a nonzero section proportional to f12, while still vanishing on D12.

The Euler-character signs are correct. An independent simplification of the fixed identity is

    Sym5 W tensor Sym13 W - Sym5 W tensor Sym11 W
      = Sym18 W - Sym6 W.

Using the complete input decompositions of Sym18 W and Sym6 W then gives chi_G(H)=V_alt directly. This cross-check does not depend on treating the checker as a proof.

### Section 3: the Harder-Narasimhan exclusion

Ordinary self-duality of a rank-three degree-zero bundle forces degrees (d,0,-d), including d=0. If d>0, the distinct-degree Harder-Narasimhan graded lines are canonical and equivariant. Their linearizations differ from the standard ones only by characters, which are trivial for G. The inherited even central action therefore forces d even.

For d>6, the projection of N to the lowest graded quotient vanishes by degree. Its remaining projection to the middle scalar line vanishes because Sym6 W has no invariant. Hence N lies in the positive line, whose norm is zero by degree, contradicting the already proved nonzero norm. This reasoning uses the canonical filtration, not a horizontal or arbitrarily selected orthogonal complement.

For d=2,4,6, equivariant Euler additivity gives exactly the three displayed virtual characters, none equal to V_alt. Therefore H is ordinary trivial. Only at that point is the canonical global-section evaluation isomorphism used to identify its constant representation with V_alt. The proof does not call an arbitrary Birkhoff complement canonical.

### Section 4: the actual perpendicular kernel

The map H to N* is everywhere surjective because the form on H is nondegenerate and N is a subbundle. It does not rely on the restricted quadratic norm being nonzero at a point. In particular, its surjectivity remains valid on D12. The actual h-identification and T5-perpendicular/T6-perpendicular relation identify its kernel with B6/U5, not merely with an abstract bundle of the same rank.

The kernel has rank two, degree -6, and top degree at most zero. An unequal splitting would give a canonical top scalar line with degree -2, -1, or 0; each is excluded by the displayed invariant Hom vanishing. The remaining ordinary type is 2O(-3). The character calculation then identifies its multiplicity representation as W'. Independently, the McKay relations give V_alt tensor Sym3 W=S4+T6+W', while Sym9 W=S4+T6, confirming the difference W'.

### Section 5: the unique actual splitting and L10

The sequence with A8=U5/U4 and quotient R is an actual exact bundle sequence. Its equivariant Ext group vanishes, and its ordinary Hom group vanishes, so the equivariant splitting section is unique relative to this specified A8. The character vanishing can also be read as the absence of W' from Sym3 W. This does not assert that the full ordinary Ext group vanishes.

The actual L10=G6/U4 has zero component in A8, by the absence of degree-two invariants. Since it is saturated in E, it is saturated in the R summand as well. Its quotient is the scalar line O(4), with no character ambiguity. The resulting extension of O(4) by O(-10) is nonzero because its actual middle ordinary type is 2O(-3), not O(-10)+O(4). Equivariant Serre duality gives its one-dimensional invariant Ext space correctly.

Crucially, the O(-8) in this new splitting comes from U5/U4. It is not identified with the O(-8)=F6/G6 retained in PR1219's earlier splitting. Both splittings preserve their own actual specified sublines; there is no conflict and no horizontal-splitting assertion.

### Section 6: both graph components are nonzero

Saturation of F6/G6 in E/L10 forces a nonzero projection to A8. If that projection vanished, its only possible nonzero component would be a degree-twelve scalar section in the other line and would vanish somewhere, violating the subbundle condition. The resulting scalar projection to A8 is an isomorphism, so the graph description is legitimate globally.

The remaining component is lambda f12 by the one-dimensional fixed invariant space. If it were zero, the actual preimage would be U5+L10 and hence U5 would lie in F6. Restriction of the actual derivative to this U5, followed by projection to the coherent lower target O(-10), is a regular equivariant bundle map. The relevant Hom group is zero because the six-dimensional Sym5 W is not Sym3 W. Its restriction to U4 would therefore be zero, contradicting the exact nonzero coherent lower image imported from PR1219. The target is correctly O(-10), not O(2). Thus lambda is nonzero without being evaluated or normalized.

### Section 7: pullback, duality direction, and the middle bundle

M is the full inverse image of the actual graph, so its specified extension is exactly the pullback of the nonzero R-extension. Multiplication by phi has direction

    H1(O(-14))^G -> H1(O(-2))^G.

The Serre-dual map has the opposite cohomological direction, from H0(O)^G to H0(O(12))^G, and sends 1 to lambda f12. It is nonzero between one-dimensional spaces. Averaging preserves the perfect invariant pairing, so the pullback cannot annihilate the nonzero invariant extension class. This argument neither assumes an apolar self-norm nor evaluates any actual pairing or coefficient.

Twisting the final extension by nine gives the standard nonzero equivariant Euler extension of O(1) by O(-1). Its middle representation is W, and the extension space is one-dimensional with trivial character. Consequently every nonzero class has the claimed equivariant middle-bundle type W(-9), with no selected endpoint normalization required.

### Section 8 and retained boundaries

The contribution accurately identifies the new actual-incidence obstruction and retains all cases not excluded by it. Nothing in the proof identifies a quotient splitting with a connection, treats a projected divisor as intrinsic ramification, establishes an original tenth jet, or asserts algebraicity or realization. First-order actual derivative statements and the already justified higher-jet statements remain separate. No actual HM/source instance or graph scalar is selected.

## Checker inspection and fresh selected-only replay

I inspected the entire verifier and character module before executing them. The verifier uses explicit RuntimeError conditions rather than assert statements, so its checks survive optimization. Its computation consists only of complete input hashing, fixed finite character recursion, integer degree arithmetic, and formal mixed-norm/Serre-duality bookkeeping. The imported character module performs exactly 9 times 9 explicit exact-rational McKay checks. It performs no instance search, coefficient evaluation, normalization, package installation, network request, or remote write. Unused helper functions do not execute any additional search.

I created a newly empty isolated directory, copied exactly the seven files specified in REPRODUCE.md, preserving paths and bytes, and ran exactly:

    PYTHONDONTWRITEBYTECODE=1 PYTHONPATH= python verify.py
    PYTHONDONTWRITEBYTECODE=1 PYTHONPATH= python -O verify.py

Both executions exited successfully with PASS and 53 explicit verifier checks; both imported and completed the fixed 81 character checks. The stdout bytes and parsed result objects were identical. The full file inventory remained precisely those seven files, with no cache or output file added. Every copied file's bytes, SHA256, and Git blob hash remained unchanged, and the corresponding seven source files remained unchanged as well. The imported count is established by the reviewed fixed 9-by-9 loop and successful completion of each import, not by an extra unrequested computation.

REVIEWER-REPLAY.json contains the before/after manifests, exact commands, complete outputs, interpreter details, and comparison results. These replay checks corroborate the selected fixed facts; they do not replace any geometric step reviewed above.

## Final disposition

The exact frozen proof passes independent entire-proof review and fresh selected-only normal/-O replay. No correction or enlargement of its claim is requested. The only newly excluded alternative is the split actual M inside the stated residual simultaneous k=2 case. Publication of the reviewer reports does not constitute authorization to merge, submit upstream, or otherwise write to GitHub.
