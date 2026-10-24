# Independent entire-proof review: actual R13 Euler extension and cyclic modification

## Verdict and exact review object

**ACCEPT, unchanged, as a necessary conditional theorem. No mathematical correction is required.**

This is a new independent review by
/root/advance_triplet_local_defect/review_r13_extension_incidence.
I read the entire frozen PROOF.md, the entire verify.py, README.md, INPUTS.md,
INPUTS.json, PROVENANCE.md, FROZEN.json, and all five complete retained direct
originals. I independently issued new complete exact-commit GitHub fetch_file
calls and separate fetch_blob calls at each returned blob identifier. I also
checked the author's full source-response payloads and retrieval metadata
against the independently retrieved bytes, and inspected the author replay
record. Neither preparatory acceptance nor the author's replay supplies the
mathematical verdict or the fresh replay evidence below.

The reviewed packet is
/workspace/shared/rankfour-profile11-triplet-r13-extension-incidence.

- PROOF.md SHA256:
  4819cebda47b3ef7a48ecbcb1fe01295a3a3a7ea7986df540421e1433d547b21.
- verify.py SHA256:
  96836077699dbffbedafc94062e7cb3ed41bc2cc585e131ed9ca2594d3a39696.
- FROZEN.json SHA256:
  1bbc25cbe3101666f71700fcd73a0f9cfcc99a75ab61024650779c1874d38ccb.
- Eleven-file core digest:
  b201b8318f4c8af47b3ceace4d552bd5b6018d1ab75520df5d8d41e0297df470.

The review concerns all eleven frozen core files and the additional
FROZEN.json used in the exact twelve-file isolated replay. I did not modify
the packet. All review outputs are in this separate review directory.

The accepted conclusion retains the full-positive triplet branch, original
t=0 and local delta=12, residual simultaneous rank-seven k=2 geometry, remaining
original K1, and every transitive actual-geometric hypothesis. It is precisely

    R13 = T6(-3) + (V_alt+P)(-4),

with the actual nonzero Euler extension block E4 and the actual reduced cyclic
modification R13 -> F18. This does not exclude or realize K1, prove horizontal
splitting, determine a torsion-line character, or establish any rank/image
claim for the separate map F18 -> Q.

## 1. Independent source authentication and source sufficiency

All five complete immutable originals were independently read and authenticated:

1. PR1235, first-kernel-span, commit
   7152e94cedbab18036b5e032d4e97934c4c061b7:
   11,977 bytes; SHA256
   66f8040b87f3d193fbd7e6eecb42a1457a59aa6f2cf3f10f29e7ac7b1aa1b6c9;
   recomputed Git blob b846834f8451e7202721d9669b43df294f7a96d3.
2. PR1236, first-kernel-forward-closure, commit
   092fc5f31dfaa5553ee5ea687f175ecba1878a2a:
   18,052 bytes; SHA256
   90081703a5e2a988a29e4d5bb918a93df4d4a954221a9bcba4cd858b0fa28137;
   recomputed Git blob f77cfb52743be86e46e0c40570ec036e69aebaf3.
3. PR1240, orthogonal-top-incidence, commit
   3fbaa182b1aceb6915be88088ef158d6d15e34fb:
   28,094 bytes; SHA256
   407d35049bb17ab4b8f4e270627adb416fc5601eab1445a21685f2cc27bcb637;
   recomputed Git blob f00b059695615d9b8ab6d315798940e3ab0a58d4.
4. PR1207, shared-d-gluing, commit
   af136934955f1bcc700ee768e2debb983e75451d:
   20,361 bytes; SHA256
   7043302b3fb672f02777d44aac67e4579ac3421bc9cad66af3655a503d2b6bb7;
   recomputed Git blob 3d051410e80a33f1c4d78d3403bb186595bb72c3.
5. PR1241, f18-row-resolution, commit
   fc43b0a6da1fc5e281284fc3b09e46acb97bec95:
   15,616 bytes; SHA256
   cd28b6dba69d23ef905f4816dcd1a7a3165bd8b337169ab0a6acb10a15ac06dc;
   recomputed Git blob 429c462fe6ba5f2b99770b9cabb35440130c807b.

For each, the exact repository path in INPUTS.json was requested with base64
encoding and no line bounds. The distinct blob request used the returned
Git SHA, not merely a hash assumed from the author. Transport base64 wrapping
was decoded; no decoded newline or Unicode normalization was performed.
Complete path bytes, blob UTF8 bytes, and frozen local bytes agree, including
byte count, SHA256, and SHA1("blob "+decimal length+NUL+bytes). Returned immutable
display URLs agree with the recorded exact-commit source URLs. Fresh calls
were made after the freeze, with exact calls and timestamps retained in
REVIEW-AUTHENTICATION.json and full replies in raw/FRESH-SOURCE-FETCHES.json.

The source-to-assertion mapping is adequate:

- PR1235 Sections 2, 3, and 5 provide the actual R11 decomposition and fifth-jet
  complement, the correctly directed restriction p and ker p representation,
  p(S)=V18*, and the missing alternate triple C/S. Its proof derives the actual
  span, rather than transferring an unrelated capacity result. The coefficient
  direction M* -> H0(Q*) and the W' tensor H3 identity are explicit.
- PR1236 Sections 3 and 4 provide the actual saturated forward R13 and R15,
  R13/R11=W(3), the onto actual constant projection on E0, and ker pi=R13.
  Sections 1 and 7-9 supply the invariant divisor facts and the actual
  annihilator/forward relationships. Its rank-two internal row, saturation,
  and reduced defect are distinguished; the new proof does not silently
  replace a coherent image by its saturation.
- PR1240 Section 1 explicitly retains the actual complete degree-ten flag,
  constant S=Z+ C7 with C7=A+P, y_Z in x2, nonzero a_Z, and y annihilating
  R15. Section 7 derives x2 annihilating R13 in the required direction by
  differentiating actual constant pairings. Section 8 proves the complete
  flag symbol sigma_j is an everywhere isomorphism. The later self-duality,
  maximal-isotropy, and P(-6) conclusions are not needed for the new exclusion.
  I read those arguments as well; no part is silently substituted for the
  actual pairing and symbol used here.
- PR1207 Sections 3-7 establish the exact gluing and actual restriction
  E0 -> F18, including the common actual saturated kernel T=V_alt(-4).
  This is the restriction of the same fixed p, not a freely chosen quotient
  with the displayed splitting type. Its separate Section 10 map F18 -> Q
  is not used to assign a rank or saturation in this packet.
- PR1241 Sections 2-6 give the syzygy, second-jet obstruction, directed
  orthogonality, and complete-jet contraction proving the nonzero alternate
  row. Section 7 applies it to this same retained actual F18. Its universal
  representation facts are sufficient for the new low-degree Hom arguments.
  The new Euler exclusion does not use the F18 resolution conclusion;
  only the Section 8 modification needs that resolved type.

An explicit source-sufficiency point: the invariant-divisor minimum alone
would show that a degree-twelve divisor is one simple orbit, but would not
identify it with a previously named orbit without uniqueness. That additional
premise is supplied, not missing. PR1241 Section 1 explicitly states orbit
lengths 12,20,30,60 and the unique length-twelve orbit. PR1236 Section 1 also
gives H12=1+A+D+P, the one-dimensional invariant equation line, and div(f12)=D12.
Consequently the determinant in Section 8 is proportional to that f12 and
has the same D12. No frozen correction is needed.

The complete originals, including their arguments and limited historical
status wording, have been read. No fresh authentication of every transitive
ancestor is claimed. The packet clearly retains their actual-geometric
hypotheses, and I find no additional undeclared direct dependency.

## 2. Sections 2-4: actual canonical blocks and the D0 row

The maximal ordinary degree -2 makes D0 canonical. The equivariant map
space from W'(-3) to E0 has exactly the W' identity component: the D component
vanishes by D tensor W=S4+T6, the T6 component by irreducibility, and the
V(-4) component by ordinary degree. This proves the uniqueness of the actual
image N, not merely an abstract type. An equivariant splitting then shows
D0+N is a subbundle with the stated locally free quotient. No splitting has
been declared constant or horizontal.

If pi killed D0, the composite D0 -> R13/R11=W(3) could not vanish because
Hom(D0,R11)=0. Its equivariant Hom space is one-dimensional. The complete
quartic evaluation followed by the physical Euler inclusion is a nonzero
generator, with kernel S4(-3). This would inject S4(-3) into R11, contradicted
by the ordinary degree bounds. In particular the proof correctly uses an
actual quotient map, not only rank and degree.

The generic-rank argument for d=pi|D0 is sound. For a rank-one image,
global generation of I(2) gives deg I>=-2, while its saturated line in V O
requires V in H(-a) and a<=-6. For a rank-two image, the saturated rank-two
bundle has quotient O(b) with b>=6, hence degree at most -6, whereas
deg I>=-4. Both inequalities have the correct direction. The globally
generated object is the coherent image twisted by two, not an unjustified
positive-degree claim about a subbundle.

Once generic rank three is known, the common divisor of maximal minors has
degree at most six, is invariant, and must be empty. This proves everywhere
surjectivity. The kernel J has rank two and degree -10. An unequal split
would give a canonical top line of degree at least -4; a nonzero inclusion
into D(-2) would require a D constituent in a symmetric power of degree at
most two (or an impossible negative degree). Thus J has ordinary type
O(-5)^2. At twist two the long exact cohomology sequence gives
H1(J(2))=P: D maps injectively to the single D in V tensor H2=P+D.
Writing J=U(-5), this is U tensor W=P, selecting U=W' rather than W
or a sum of characters. The parity and no-character observations are
consistent with this identification. The resulting sequence (4.1) is actual.

## 3. Sections 5-7: only the Euler block can extend, and its class is nonzero

Surjectivity of d makes R13 -> E0/D0 onto and gives kernel J. The three
equivariant extension blocks have precisely the stated cohomology:

- W'(-3) by W'(-5): End_G(W') tensor H1(O(-2))=C.
- T6(-3) by W'(-5): zero by Hom_G(T6,W')=0.
- V(-4) by W'(-5): zero by H1(O(-1))=0.

Thus only the W' block can be nontrivial. Its nonzero class is the physical
Euler sequence tensored by W', whose middle type is P(-4). The two abstract
possibilities are legitimate, but classification alone does not select one.

The incidence argument selects the nonzero class correctly. Under the zero
class, the actual inclusion of the W'(-3) summand into E0 has image N by
the proved uniqueness. Then N lies in R13 and S O. Its coefficient map
has types in H0(N*)=(W')* tensor H3=D+V_alt. Therefore its constant projection
to C7 O vanishes, since C7=A+P has no common constituent. This justifies the
actual pure-Z containment; it is not a chosen constant decomposition of E0.

The annihilation rectangle has the required directions:
x2 annihilates R13; y annihilates R15=R13^+; hence differentiation of
y(e)=0 for an arbitrary local R13 section gives dy(e)=0, because de lies
in R15 tensor Omega. Since N is in the pure Z block, the pairings with y
and dy reduce exactly to y_Z and its first derivatives against N.
The derivative of y_Z modulo x2 is sigma2 composed with a_Z, with the
Omega twist as displayed. Coefficient derivatives stay in x2. This is
the intrinsic symbol of actual differentiation, not a quotient connection.
Both factors are nonzero and sigma2 is an isomorphism. Thus x2 and these
first derivatives span x3 generically, forcing N to annihilate x3.
Vanishing extends everywhere as a bundle-pairing identity; no saturation
under an arbitrary projection is assumed.

Completeness of the degree-ten curve is essential and is supplied. The
order-three annihilator is exactly H6(-4): universally it consists of
degree-ten forms divisible by the fourth power of the varying vanishing
linear form. Its rank is seven and its degree is -28. The direction is the
primal annihilator in Z, not the jet bundle x3 in Z*. The nonzero inclusion
W'(-3) -> H6(-4) is impossible because its ordinary entries have degree -1.
This excludes the zero extension. The same rectangle directly proves
pi|N != 0.

For E4=ker(pi|(D0+N)), d onto ensures a saturated rank-four actual subbundle
and the exact sequence J -> E4 -> N. Were this extension zero, an equivariant
lift of N would have zero D0 component by Hom_G(N,D0)=0, contradicting
pi|N != 0. Therefore E4=P(-4) is the nonzero Euler block.
The quotient R13/E4 has type T6(-3)+V(-4), and its extension by E4 splits
equivariantly because the relevant ordinary differences are -1 and 0.
This proves the claimed full R13 type while retaining the actual E4
incidence. The notation E4 avoids any earlier auxiliary U4 collision.

## 4. Section 8: transverse T, determinant, and actual elementary modification

The actual T is the kernel of p|E0, not an arbitrary V(-4). It is saturated
in C O: E0/T and C O/E0 are locally free, so C O/T is locally free.
The onto constant map ker p -> C/S has source A+V and target V, giving
S intersect ker p=A by semisimplicity and the distinct irreducible types.

If b=pi|T vanished, T would lie in this constant A O. Since both have rank
three, A O/T would be nonzero torsion of length twelve, yet it injects into
the locally free C O/T. That is impossible. This proves b is nonzero
using its actual ambient incidence.

The generic-rank exclusions are valid and complementary:

- Rank one: the saturated image line has degree <=-6, but the image twisted
  by four is globally generated and hence has degree >=-4.
- Rank two: its kernel line O(-k) in V(-4) requires k>=10, giving
  deg I=k-12>=-2. The saturated rank-two image in V O has quotient O(c)
  with c>=6, and therefore degree <=-6. Again deg I<=deg F contradicts
  the bounds.

Thus b has generic rank three and zero sheaf kernel. Its determinant is
a nonzero invariant section of O(12). By the supplied unique orbit/invariant
line statement discussed above it is a nonzero multiple of f12, without
choosing that multiple or an invariant-polynomial representative.
The divisor is reduced D12. Over each arbitrary local DVR, the sum of
the three nonnegative Smith exponents equals the determinant valuation
one, so the exponents are 0,0,1. Hence the cokernel has precisely length
one at every orbit point, not merely total length twelve.

Finally, T intersect R13 is zero as a sheaf since it is ker b.
Consequently E0 -> E0/T=F18 restricts to an injective sheaf map R13 -> F18.
Its quotient is

    E0/(T+R13) = (V O)/b(T) = H.

This is an exact quotient-diagram argument. It does not replace a sheaf
intersection by a fiberwise intersection over D12. Indeed the map is not
a subbundle inclusion there. A length-one local cokernel gives the single
simple elementary factor, and outside D12 the map is an isomorphism.
The degrees -46 for R13 and -34 for F18 yield the required difference twelve.
No equivariant torsion-line character has been selected or inferred.

## 5. Checker and independent replay audit

The checker was read in full. It authenticates the eleven frozen files and
the five prescribed source pins using explicit runtime checks. Its mathematical
calculations are fixed formal character recurrences through degree twelve,
the small displayed products, and fixed degree/cohomology arithmetic.
There is no source-instance input, numerical geometric evaluation, network,
subprocess, optional search mode, or historical enumerator in the checker.
Its require function remains active under -O; it does not rely on assert.
It is evidence for byte identity and fixed arithmetic only, not a proof.

I created two new empty directories, copied exactly the twelve selected
files, and ran both normal and optimized isolated Python in each:

- /tmp/r13-independent-review-a-8ezbpfdo
- /tmp/r13-independent-review-b-440tdnng

Commands use python -I -B and python -I -B -O with that directory's verify.py.
All four runs exit zero with empty stderr and identical PASS output,
220 runtime checks, five complete direct originals, and the expected core
digest. Before/after inventories contain exactly the selected twelve files;
the only subdirectory is inputs. All bytes are unchanged. No raw source
response, author evidence, review file, cache, or unselected extra was copied
into either replay directory. The packet freeze and all selected source bytes
were checked unchanged after replay.

REVIEW-REPLAY.json retains exact commands, interpreter version, timestamps,
outputs, both complete pre/post inventories with byte counts/SHA256/Git hashes,
and the source pre/post inventory. Raw stdout and stderr are stored separately.
The external inventory check, not a claim that verify.py rejects arbitrary
extra directory contents, establishes selected-only replay.

## 6. Final boundaries

This review accepts the entire frozen proof, not just a character checker or
a local lemma. It confirms the actual-map construction and source sufficiency
under the retained assumptions. The accepted new progress is the nonzero
Euler extension class, the actual E4 incidence, the exact R13 splitting type,
and the reduced cyclic actual modification into the resolved F18.

There is no K1 exclusion or realization, broader profile conclusion,
higher-order matching claim, or algebraicity claim. Higher/first jet maps
here serve the stated intrinsic actual incidence argument, not a claim
that separate formal branches match. There is no horizontal splitting,
quotient connection, inverse-map differentiation, rank-seventeen transfer,
or extension of PR1207's separate F18 -> Q corollary.

No selected actual coefficient, parameter, point, jet, tensor, matrix,
eigenline, scalar normalization, invariant-polynomial representative, or
instance rank was evaluated in this review. No broad scan, large computation,
GitHub write, local Codex task, merge, publication, or upstream submission
was performed. All review and replay evidence is separate; the frozen
packet remains unchanged.

