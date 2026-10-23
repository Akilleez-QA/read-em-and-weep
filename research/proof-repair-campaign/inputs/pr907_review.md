# Independent review of the source127 a-c-c-f common-image exclusion

## Verdict and reviewed version

**PASS.** The proof excludes the complete source edge

    label G3.11.cce6e3ba4eeb, source_index 127,
    tuple (1,0,2,0,0,1,0,0), original defect zero,
    E=(V+D) O(-2)+Wp O(-3)+2V O(-4)+O(-8),
    A_q=O(-8)+O(2)+O(16), B_q=O(-18)+O(-4)+O(6).

This verdict applies to the following exact frozen bytes, reviewed on 2026-10-23:

- PROOF.md SHA256: `4ad0f3798fbde99d995b5cc0ec3f82a5ecf70a00c2a793874c11541a8b1b3542`.
- verify.py SHA256: `cd5c654c3a4a73233d7b02f2b1f6994d2dc6ac728fd383b60bd86b67123001e2`.
- REPRODUCE.md SHA256: `341f09afb00636ef83a2a484f37233a14fd9558469effac714dac7d8f8e66b46`.

The proof and verifier were not modified. The review read the entire new proof, the entire PR901 cubic-reduction proof, both original actual-sheaf notes, the source127 catalog entry, and the matching frontier record. This was a mathematical review of the arguments, not an inference from the verifier's success.

The result is a whole-source exclusion, not a whole-label exclusion. It does not exclude the distinct a-b-c-f edge, the c-d-f abstract family, all other source127 tuples, or the remaining rank-three frontier. No global rank bound or realization claim is added.

## 1. Authentication and original actual interface

All five audit inputs were authenticated independently using the Git object formula

    SHA1("blob " + decimal byte length + NUL + exact file bytes).

Each computed hash equals the manifest value:

- ACTUAL.md: 9,672 bytes; `b93e0b3589ef71cf2c029fd07a6bdb1da8ba92b3`.
- STRICT-TOP.md: 4,983 bytes; `d7506dae49b4be43230450c4132bd5db91f137ef`.
- pairs.json: 58,635 bytes; `fe0afa410d89340d3082dc814277f89fbb582c19`.
- frontier.json: 378,361 bytes; `8b5971092f9ef762584912609fd5e9301c4e271d`.
- WP-REDUCTION.md: 17,124 bytes; `8734e450297032410ac5625efeddd3cea34fd654`.

The first four are pinned at commit `db51525015bb7c5e825833d550d08dedf6f6ea96`; the fifth is the PR901 proof pinned at commit `12d7fbb02ffbfd920bd5133c197ca9166cbabc5a`. Exact immutable URLs and repository paths are in audit-inputs/manifest.json and REPRODUCE.md. Authentication here is of the supplied exact Git-blob contents; it is not a new claim about remote branch state.

The original presentation note supplies a saturated E in the constant ambient bundle, rank 17, degree -54, and H0(E(1))=0. Its equivariant splitting is legitimate: distinct slope extensions split, and averaging yields equivariant splittings. Its tuple formula gives R_2=V+D and exactly the displayed remaining summands for (1,0,2,0,0,1,0,0). Thus every ordinary splitting degree is at most -2 and H0(E(2))=V+D.

The strict-top note proves H0(E^-(2))=0 for the actual derivative kernel. Its proof uses a top-degree line direct summand, saturation in the constant ambient bundle, vanishing of its internal derivative by degree, and the impossibility of a negative horizontal saturated subbundle. It does not confuse injectivity on top global sections with fiberwise injectivity of the derivative.

Catalog index 127 has original defect zero and A_q and B_q exactly as displayed above, and contains the stated source tuple among its necessary compatible E types. The frontier record with the stated label independently matches index 127, profile 11 and original defect zero. The original zero-defect Gauss convention identifies the actual derivative image with A_q, so E^+/E=A_q(2)=O(-6)+O(4)+O(18). The highest line L=O(18) is saturated in Q=H O/E. None of this turns a catalog-compatible type into a realization: the proof assumes a realization of this exact edge and contradicts it.

As with the reviewed proof, this audit takes the frozen actual HM bundle construction and original Gauss conventions as inputs. It does not reconstruct that upstream construction from selected coefficients.

## 2. Audit of the complete PR901 dependency

The necessary imported conclusion is stronger than an abstract splitting statement. It says that the actual original R=Wp O(-3) has saturated raw first span M_R=P O(-2), constant coefficient span C_R=V+D, and actual image in Q equal to O(6) embedded in L by f12. I checked the arguments establishing all three parts.

### 2.1 The cubic derivative and its exact image

The negative external row of R vanishes by degree and the O(2) row vanishes because Wp is absent from Sym5 W. If the high row vanished too, the full derivative would be internal into degrees at most -4; it would then vanish on R(-3), making R horizontal. Thus the high row is nonzero.

Wp occurs with multiplicity one in Sym7 W and Sym19 W. Multiplication by the nonzero invariant f12 identifies these two covariant spaces. The degree-seven row cannot have a nonempty invariant common divisor of degree at most seven. It is consequently onto O(4), with kernel O(-10), before its image is included in O(16) by f12. This proves the precise divisor twelve and preserves the nonsaturated image lattice.

For the a-c-c-f source, the kernel O(-10) has only the internal top V(-4) and scalar O(-10) channels. The D(-4) and 2V(-6) channels vanish by the stated characters. A nonzero top V channel is basepoint-free because its degree is six; a nonzero scalar channel is an isomorphism. Therefore the complete internal image is either zero or a saturated O(-10), even when both allowed components occur.

The raw exact image sequences then give either a rank-three degree-zero first span, hence constant V O, or a rank-four degree-minus-eight first span. In the latter case the cubic polar map is a surjection P O(-2) onto that raw first span of the same rank and degree, so it is an isomorphism. Any saturation defect has invariant degree at most eight and must vanish. The possible constant coefficient spans are D or V+D, not arbitrary four-dimensional spaces.

### 2.2 The zero internal image is actually excluded

PR901 Section 4 uses coherent projection, not saturation of the high image. In the zero-channel case C=V O has C/R equal to precisely the f12 image O(6). For the canonical top B=V(-2), the high derivative is divisible by the same f12, including if it were zero. Consequently the derivative of B lies in (E+C)(-2), the exact preimage of that coherent image.

Projection by C gives the actual coherent lattice E/R, and the projected B is still isomorphic to B, since E intersect C=R and B intersect R=0. Its derivative modulo projected B lands in (E/(R+B))(-2), all of whose degrees are at most -4, and vanishes. A preserved coherent lattice in a trivial bundle cannot have negative degree: the generic horizontal space is constant, and a positive determinant zero produces a logarithmic pole incompatible with preservation. This yields the stated contradiction without replacing the projected lattice by its saturation.

### 2.3 The scalar channel and full coefficient span are forced

I checked both universal injections used in PR901 Section 5. The nonzero V(-2) to P O and V(-2) to D O channels each have rank three everywhere. The P case follows from the basepoint-free P-valued degree-six row and its kernel's rank-three, degree-minus-six, H0=0, H1=V budget. The D case follows from the saturated Wp(-3) injection into D O, dualization, and the identical budget. In the budget, an O(-1) contribution alone gives no H1; the only negative atom capable of supplying the single V in H1 within rank three is V(-2), which already uses the full rank. Thus no omitted O(-1) summand remains.

If the scalar channel were zero, the remaining internal top V line would be killed by projection outside C_R. Since every nonzero P or D component of the projected B is one of these saturated injections, the projection must be zero. This gives B inside C_R. The C_R=D option would contain the saturated rank-five negative B+R in a constant five-space and is impossible. Thus C_R=V+D, B lies in its D part, and B^+=D O. The proof of this last equality checks generic rank two of B's derivative in the quotient Wp O(1) and then bounds the raw polar defect by five, rather than assuming saturation.

The projection of R to the V part is a saturated injection, so D+M_R has full generic span C_R. Saturation of E^+ then gives C_R inside E^+. The quotient of C_R by B+R has ends Wp O(3) and O(6), neither of which maps to the lower O(4) or O(-6) rows. The D restriction of its high row is nonzero. Five independent degree-eighteen coefficient sections give a common-divisor bound of fourteen; the only possible invariant degree in this range is twelve, and a degree-twelve factor would require D in Sym6 W, which is absent. Thus this high row is onto L, not merely generically nonzero.

It follows that X=E intersect C_R has rank seven and degree -18. Its quotient by the actual saturated B+R is a rank-two, degree-minus-six subbundle of D(-2)+2V(-4)+O(-8). No rank-two equivariant bundle can have an admissible degree -2 or -3 atom mapping to this target: D has dimension five, and D W=S+T contains neither possible two-dimensional odd coefficient. All splitting degrees would therefore be at most -4, contradicting degree -6. This excludes the V-only channel while retaining an unrestricted additional V component when the scalar channel is nonzero.

Finally, if C_R=D in the remaining scalar-nonzero case, C_R/M_R=O(8). The derivative of M_R kills R. On N_R=E intersect M_R it therefore factors through N_R/R=O(-8) to O(6), an invariant degree-fourteen scalar map, which is zero. Differentiation of N_R would stay in M_R and could supply no negative external row. But its nonzero component to the original scalar O(-8) source summand supplies a nonzero negative derivative row; no other source summand can contribute to that row by degree. This is a contradiction. Therefore C_R=V+D really is forced.

The following cubic Euler flag in PR901 is compatible with the full coefficient map Wp Sym3 W=V+D. It is not needed for the new exclusion; in particular no assertion about E^+ intersect C_R or a final flag endpoint has been imported. The optional V internal component has not been discarded.

## 3. Independent derivation for the top V block

Let B=V O(-2). Its negative external row vanishes by degree, and its O(2) row vanishes because Sym4 W=D contains no V. Strict-top injectivity on H0(E(2)) prevents the high row from vanishing on B. V occurs once in Sym6 W and once in Sym18 W, and multiplication by f12 is a nonzero injection between these spaces. Thus the row is exactly

    V O(-2) -> O(4) -> O(16),

where the second arrow is multiplication by f12. The first arrow is onto: a common-zero divisor of a nonzero degree-six covariant would be invariant of positive degree at most six, impossible. The row has actual image O(4), not O(16).

Its kernel is Wp O(-5). An independent intrinsic construction is the unique nonzero Wp(-3) to V O map. Generic rank one would give an equivariant coherent line image O(e), e<=0, requiring Wp in Sym^(e+3) W, absent for every possible degree from zero to three; for negative degree there is no Hom at all. Therefore the rank is two. Its determinant defect has invariant degree at most six, since the saturated rank-two image in a constant bundle has nonpositive degree. That defect is empty. The quotient is the uniquely linearized O(6). Dualizing and twisting by -2 gives

    0 -> Wp O(-5) -> V O(-2) -> O(4) -> 0.

Uniqueness of the degree-six V row identifies this kernel with the actual high-row kernel; no source map was selected.

The entire internal derivative target of K_B=Wp(-5) is

    (E/B)(-2)=D(-4)+Wp(-5)+2V(-6)+O(-10).

The first channel vanishes because D W=S+T contains no Wp, the lower channels vanish by degree, and the equal-degree Wp channel is scalar. Hence the complete internal image J_B is exactly zero or the entire original Wp(-5). There are no intermediate coherent images or other internal channels.

## 4. Both raw first-span alternatives

Write I_B for the full raw derivative image and M_B for the raw first span. The exact sequences are

    0 -> J_B -> I_B -> O(4) -> 0,
    0 -> B -> M_B -> I_B(2) -> 0.

The quotient on the first line is the actual external image. It has not been saturated.

If J_B=0, then M_B has rank four and degree zero. All splitting degrees of a subsheaf of H O are nonpositive, so M_B is constant and its inclusion is automatically saturated. Its coefficient character is

    chi(B)+chi(O(6))=-V+(V+P)=P.

Thus M_B=P O, with actual image O(6) in Q included into L by f12.

If J_B=Wp(-5), then M_B has rank six and degree -6. Its quadratic first-polar presentation is a surjection V W O(-1)=T O(-1) onto M_B. Equal rank and degree force an isomorphism. The saturation defect in H O has invariant degree at most six, hence is zero. This justifies M_B=T O(-1) as an actual saturated first span, not a splitting assigned to a generic image.

There is an important sheaf identification here. Modulo B, the intersection E intersect M_B is the exact internal image J_B(2), which is the original R in E/B. Thus E intersect M_B is its full preimage B+R, not a potentially unrelated isomorphic bundle or graph. In particular the original R is contained in M_B.

Differentiation does not enlarge the constant coefficient span, and M_B contains B. Their constant spans therefore agree and are a quotient of V Sym2 W=P+D. A rank-six M_B cannot lie in either of the smaller quotient representations P or D, so its span is exactly P+D. Containment of the original R would then force its full span V+D to be a subrepresentation of P+D. The V constituent makes this impossible. This rules out the entire nonzero-channel alternative, independently of the optional internal V row in the cubic reduction.

## 5. Exact common image and the final obstruction

The only remaining alternative is M_B=P O. Its coefficient representation has no constituent in common with C_R=V+D. Their intersection in H is therefore zero, regardless of the choices of isomorphic copies in H. Consequently

    S0=M_B direct-sum M_R=P O direct-sum P O(-2)

is their actual sheaf sum, of rank eight and degree -8.

Both summands lie in E^+. Each maps onto a coherent O(6) image in L, followed by a nonzero invariant degree-twelve inclusion. Because the invariant degree-twelve space is one-dimensional, these inclusions differ only by a nonzero constant scalar after identification of their source line bundles. They have exactly the same image subsheaf f12 O(6) of L. This remains true at every point of the divisor of f12. Equality of their generic line alone would not suffice and is not what the proof uses.

The map S0 to Q is therefore onto this common coherent image, giving

    0 -> N=E intersect S0 -> S0 -> O(6) -> 0.

In particular N has rank seven and degree -14. This argument does not require S0 itself to be saturated in H O. The kernel is locally free on P1, and the displayed quotient is the actual locally free image as a sheaf, although its inclusion in Q is nonsaturated.

Every ordinary splitting degree of N is at most -2 because N injects into E. Seven such degrees summing to -14 must all equal -2. Equivariant splitting therefore gives N=U O(-2) for a genuine seven-dimensional representation U. Taking sections after twisting yields an injection

    U -> H0(E(2))=V+D.

Over C, this multiplicity-free semisimple representation has subrepresentation dimensions only 0, 3, 5 and 8. Dimension seven is impossible. This contradicts the remaining zero-channel case and completes the whole-source exclusion.

## 6. Reproduction, independent checks, and limitations

The frozen command `python3 verify.py` completed successfully. It authenticated all five inputs and passed the stated fixed character, exact source identity, rank, degree and constituent checks.

Separately, without importing the verifier, I recomputed the needed symmetric powers from the affine-E8 McKay multiplication-by-W graph and the recurrence Sym^(n+1) W=W Sym^n W-Sym^(n-1) W, through n=19 only. This independently gives

    Sym6 W=V+P,
    Sym7 W=Wp+T,
    Sym12 W=1+A+P+D,
    Sym14 W=A+V+P+D,
    Sym18 W=A+V+2P+D,
    Sym19 W=W+Wp+S+2T,
    V W=T, D W=S+T, Wp W=P,
    V Sym2 W=P+D, Wp Sym3 W=V+D.

These checks also verify the low-degree absences and the one-dimensional invariant degree-twelve space used above. The invariant effective-divisor minimum twelve is the standard projective icosahedral orbit bound retained by the actual setup.

All computational work was small fixed abstract character arithmetic, file hashing, and reading the exact catalog identities. No selected actual HM/source coefficients, parameters, points, derivatives, matrices, instance ranks, models, scans or large computation were evaluated. No local Codex task, external publication, branch update or source modification was performed.

The character verifier does not certify the sheaf reasoning by itself. The exact image, raw first-span saturation, universal kernel identification, original R containment, full cubic dependency, and common-image intersection arguments have been checked separately above. No correction to the frozen proof is required for this verdict.
