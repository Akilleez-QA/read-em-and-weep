# Independent whole-proof geometric review

Verdict: PASS, relative to the explicitly imported actual-bundle, primary four-type, and original profile-(1,1) necessity theorems. I found no blocking mathematical defect and request no proof change.

This is a review of the entire proof, not only its apolar or constant-splitting step. It certifies the stated narrow exclusion of

    A = O(-8) + O(2) + O(16)

for the actual maximal profile-(1,1) situation. It does not certify a global rank-three exclusion, realization of a formal splitting type, or repair of the original theorem.

## Exact reviewed version

- PROOF.md SHA256: `47ce243076419081917682b9ab78990e7cf8066598d8eae1f4a175e80ab91b98`
- verify.py SHA256: `14534e059dd5052c3052be3a6102aa2e378d25612727ae45ae15762f883eaa2a`
- characters.py SHA256: `5b3b1d415f26ca467670afeb73357cbb0e9c125a6b1acd25155b6d85eef4e4f1`
- RESULT.json SHA256: `ece3083613037b66e0a92250e67f9dea17bef255c82ea102695c155635e0b43f`
- INPUTS.json SHA256: `a51a0e735d60a345325dc6eecd489475d2df25d5d7d7a74995597c7083822db6`

The proof binding above is to the final version supplied for review, including its spacing cleanup and explicit no-character-twist sentence after (4). I inspected that last clarification and reran the final verifier after its stdout newline polish. No modification of PROOF.md was made in this review.

## Inputs, physical marking, and scope

I read all six retained written/code sources and the relevant records of the complete retained JSON. I independently recomputed all seven retained files' byte counts, SHA256 values, and Git blob SHA1 values and matched them to INPUTS.json. I also checked that AUTHENTICATION.json agrees with that manifest. This review's own authentication check is a local-byte identity check; the fresh remote byte comparison is recorded in the supplied authentication artifact, not represented here as a second remote fetch by this reviewer.

The original actual-inclusion source identifies the saturated rank-17, degree-minus-54 bundle in the constant thirty-space and identifies its quotient and actual Gauss derivative. The actual-splitting and profile11 sources supply rank S=13, degree S=-54, and H0(S)=0. The maximal profile-(1,1) endpoint hypothesis gives rank L=10 and derivative rank at most two. No dual-interior or stronger profile-(2,1) top-degree bound is imported.

The original profile11 written theorem, rather than the bare JSON, supplies geometric necessity of its 159-record overlist. Direct extraction gives exactly the zero-based original indices 119 and 127 for the specified A. Their respective B degrees and defects are (6,-16,-18),12 and (6,-4,-18),0. The new proof does not require a later live-frontier count or an unproved transfer/coverage statement.

PR1123 supplies the necessary four-type reduction for the same actual E and fixed determinant convention. Its three non-D types have no ordinary summand of degree at most -8, so the surjection E to the O(-8) summand of A forces precisely the displayed D type. This uses an ordinary Hom-degree obstruction, not a choice of actual source coefficients.

The W, W', V, P, D, and T conventions match the retained physical character reference. In particular V is the nonstandard three-space, not Sym2 W. The fixed determinant identification of W with its dual is used consistently for the parameter line, the coefficient systems, and the apolar identifications. A linearized rank-one O(d) contributes no extra character, since this group is perfect, as recorded by the actual-splitting input.

## Section 2: capacity and its equality case

The derivative construction is valid at the level of actual sheaves. Since F_j is the Gauss kernel of F_(j-1), its derivative takes values in F_(j-1) tensored with Omega. Projecting modulo F_j is O-linear and its kernel is exactly F_(j+1). This yields the claimed injections of the locally free quotients G_j, with Omega=O(-2). No initial image-saturation assertion is needed.

All the kernel subbundles are saturated in the original constant bundle. Every nonzero one has strictly negative splitting degrees because it lies in S. A zero second fundamental form would make its Grassmannian map constant in characteristic zero, contradicting negativity. Thus the sequence terminates and the q_j are positive until termination, weakly decreasing, and bounded by two. Consequently the two-height description with h_1+h_2=10 is exhaustive, including h_2=0.

Taking determinants of G_j into B(-2j) gives the stated upper bound. Independent arithmetic reproduces both six-entry capacity lists. The positive-defect row has degree L=-26, strictly greater than the maximum capacity -50. The zero-defect row has degree L=-38, and only heights (7,3) and (8,2) can attain it. Because the total equals the sum of upper bounds, every individual bound is an equality.

The equality-to-exact-image step is sound. The top wedge summand of B is unique for q=1 or 2. An equal-degree determinant has a nonzero constant top component and zero lower components. Its generic Plucker point is therefore the top q-dimensional subspace. The map factors through the corresponding top subbundle globally, and its determinant is nowhere zero. Thus it is an isomorphism onto that subbundle, not merely an isomorphism away from a torsion divisor.

The nonzero highest-line symbol at each intermediate derivative then propagates a nonzero leading component through successive quotients. Lower-order differentiation of a local scalar contributes only previously obtained filtration terms. Accordingly the first k derivatives of the last line supply k+1 generically independent directions in the asserted stage. This validates the coefficient-image dimension bounds without assigning a connection to a Birkhoff complement.

## Section 3: height eight

Nine independent directions force the degree-ten coefficient quotient to have dimension at least nine. The semisimple multiplicity-free representation Sym10 W=A_std+V+D has no proper quotient of dimension greater than eight. Hence the coefficient map is injective and its image is a genuine constant eleven-space.

For the complete polynomial line, the saturated kth osculating bundle is Sym^k W tensored with O(k-e), with fiber l^(e-k) Sym^k W. Generic containment extends through the saturated actual flag. The apolar annihilator of l^2 Sym8 W is l^9 W, giving W O(-9). All source degrees are at least -8, so the projection from E is zero even non-equivariantly. The resulting nonzero constant subspace inside S contradicts H0(S)=0. No unproved stronger top-S bound is used.

## Section 4: height seven and the constant splitting

The analogous degree-eight map has image dimension at least eight, whereas a proper quotient of P+D has dimension at most five. It is therefore complete. Its seventh osculating bundle has annihilator the complete line J_0=O(-8).

The actual projection of E to U_9* factors through J_0. Degree alone kills its restriction to F, and its restriction to J=O(-8) is a nonzero scalar: zero would again put a constant U_9 in S. The crucial passage from a bundle splitting to a constant ambient splitting is justified. The coefficient map of the actual embedded J projects isomorphically to the coefficient space of J_0. Its constant nine-dimensional image C_9 therefore projects isomorphically to U_9* and is a complement of N. Hence F lies in N and J lies in C_9 as actual embedded bundles.

This is not an arbitrary horizontalization of a Birkhoff splitting. It is a consequence of the full degree-eight coefficient system. The quotient decomposition makes N O/F locally free, so the residual inclusion is saturated. The constant decomposition makes both actual second fundamental forms block diagonal; the line J is nonconstant and has zero Gauss kernel. Cancellation therefore gives the actual residual Gauss quotient O(2)+O(16).

## Section 5: the residual dual endpoint

The residual dimensions and signs are correct: dim N=21, rank F=16, degree F=-46, rank S_F=5, and degree S_F=-46. For the complete degree-eight line, S_J=Sym7 W O(-1) and L_J=Sym6 W O(-2), of respective ranks eight and seven and degrees -8 and -14. Their quotient is O(6). The derivative rank of L_J is one, not just bounded by one: negativity excludes zero.

The actual block decomposition gives rank L_F=3 and B_F=O(-4)+O(-18), so degree L_F=-24. Since the total endpoint derivative rank is at most two and the J part contributes one, the F part has rank at most one. Negativity makes it positive at every nonzero subsequent stage. The ranks 5,3,2,1,0 and three line-quotient bounds -6,-8,-10 follow. Their sum is exactly -24, so the residual terminal line is saturated O(-10), with its first three actual derivatives in S_F.

Only four independent directions have been established here. The proof correctly does not infer completeness from them.

## Sections 6-7: partial quotient, apolar factor, and span

The use of a potentially incomplete degree-ten system is correct. If q:Sym10 W onto R is its coefficient map, the dual injection q*:R* into (Sym10 W)* is available regardless of the dimension of R. The actual projection of F, followed by q*, annihilates the universal four-dimensional fibers l^7 Sym3 W because their q-images are the actual osculating directions in S_F. This argument does not need q to preserve their rank everywhere.

Their full apolar annihilator is l^4 Sym6 W, a saturated rank-seven bundle (V+P)O(-4). The displayed factorization is therefore valid in the full dual space even when the original polynomial system is partial. The degree -2 and -3 source blocks have zero Hom into it. The V(-4) block has exactly one equivariant scalar channel, since V occurs once in Sym6 W and is distinct from P. If that scalar vanished, the whole nonzero constant R would annihilate F and lie in S_F, contrary to H0(S)=0. Thus R* contains every l^4 V.

The sextic-net span lemma is valid and requires no special coefficient calculation. Its common base divisor is invariant and has degree at most six, while every projective A5 orbit has at least twelve points: the stabilizer is cyclic of order at most five. The net is therefore basepoint-free. Its evaluation kernel has rank two, degree -6, and no sections, so its line degrees are -a,-b with a,b positive and a+b=6. After twisting by four both degrees are at least -1 and H1 vanishes. Consequently V tensor Sym4 W maps onto Sym10 W. This includes the extreme pair (a,b)=(1,5); no balanced-syzygy assumption is required.

Pure fourth powers span Sym4 W, so the span of all l^4 V is the whole eleven-space. Only at this point is R proved complete. The rank-thirteen source subbundle D(-2)+(W'+T)(-3) is killed by the constant projection N to R*, whose kernel has dimension 21-11=10. Its actual injection into that rank-ten constant kernel is impossible. The last contradiction uses bundle rank, not an evaluated instance matrix.

## Verifier and reproduction

I inspected verify.py and characters.py and ran both:

    python3 verify.py
    python3 -O verify.py

Both executions succeeded, and each stdout compared byte-identically to the retained RESULT.json with 194 bounded controls. The normal and optimized modes keep the require-based checks active. The character adjacency checks agree with the retained physical traces, and the degree convention used in Hom is target degree minus source degree.

The bounded program checks source-file identities, the two exact historical records, the two capacity lists and equality heights, universal representation dimensions, residual degree/rank identities, Hom vanishings, apolar dimension/twist formulas, and all five positive ordered pairs a+b=6. It does not establish geometric saturation, the original list's necessity, actual-map compatibility, or the span lemma by computation; those points were separately checked above as arguments.

No selected actual HM/source point, coefficient, parameter, jet, tensor, matrix, or rank evaluation, historical enumeration rerun, large computation, or public write was performed for this review.

## Final conclusion

The proof closes the stated A-shape case, including both original B records. In particular its delicate height-seven branch does not rely on a nonconstant bundle projector, an unjustified complete residual polynomial system, or an accidental strengthening of the endpoint hypothesis. The precise contribution and the remaining scope boundaries in Sections 1 and 8 are appropriate.
