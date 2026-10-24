# Source provenance and assertion boundaries

## Fresh authentication

The complete five direct originals in INPUTS.json were obtained on
2026-10-24 from Akilleez-QA/read-em-and-weep. For each original, the author
made a fresh read-only GitHub fetch_file call at the exact immutable commit
and repository path, with base64 encoding and no line-range limits. The
author then made a distinct fetch_blob call at the blob identifier returned
by that file call. The full source bytes were decoded as UTF8 without any
newline or Unicode normalization. The returned complete blob text encoded
as UTF8 equals those path-read bytes exactly.

Each saved inputs/*.md is exactly those complete bytes. Its SHA256, byte
length, and computed SHA1 of the Git object header plus content agree with
the expected source pin and returned Git blob. INPUTS.json contains the
exact tools, arguments, start/end UTC timestamps, verified immutable file
URLs, and blob endpoints. All five complete originals were read in full.
The raw complete responses are retained in LOCAL-SOURCE-FETCHES.json for
local audit only, not included in the publication core or isolated replays.

The Git blob digest is computed as

    SHA1("blob " + decimal UTF8 byte length + NUL + complete UTF8 bytes).

The five expected SHA256 pins were supplied before these fresh reads;
none was inferred from a source summary or checker output. The PR1241 blob
was independently obtained from its fresh exact-commit path read.
No claim is made that all transitive ancestor files were fetched afresh.
Their complete actual-geometric hypotheses remain retained assumptions.

## Exact direct use

1. PR1235, first-kernel-span, supplies the actual embedded R11 type,
   span S, C/S=V_alt, the restriction kernel representation A+V_alt,
   p(S)=V18*, and the fixed W' tensor H3 identity. The new proof uses the
   actual map directions, not only dimensions.
2. PR1236, first-kernel-forward-closure, supplies E0, actual onto pi,
   its kernel R13, actual quotient R13/R11=W(3), R13^+=R15, and the
   invariant degree-twelve orbit facts.
3. PR1240, orthogonal-top-incidence, supplies the actual constant splitting
   S=Z direct-sum C7, C7=A+P, the complete x_j flag, x2 annihilating R13,
   y annihilating R15, y_Z in x2, and the nonzero top symbol a_Z followed
   by sigma2. Its additional self-duality and maximal-isotropy conclusions
   are not premises for the new Euler-extension exclusion.
4. PR1207, shared-d-gluing, supplies the actual restriction E0->F18 and
   its kernel T=V_alt(-4), together with the fact that this is restriction
   of the fixed constant map p. Its separate final corollary is not used
   or extended in the new argument.
5. PR1241, f18-row-resolution, supplies the resolved actual F18 type under
   exactly the retained branch and the fixed low-degree representation
   facts. Its conditional assumptions remain intact.

The seven-dimensional notation V in the PR1240 original is local to that
source. The new proof consistently uses V=V_alt and writes the seven-space
as C7*; it does not identify these different representations.

## Newly proved bridges

- Section 2 constructs the intrinsic D0 and N algebraically in E0, without
  a horizontal splitting.
- Sections 3-4 prove the actual D0 row of pi is nonzero and everywhere
  onto, with kernel W'(-5), by actual quotient incidence and universal
  character, saturation, and degree arguments.
- Section 5 lists the two possible equivariant extension types; it does
  not select one merely from those types.
- Section 6 excludes the zero extension: it would put the canonical N in
  the pure constant Z block and then in ann_Z(x3)=H6(-4), where ordinary
  degree makes its nonzero inclusion impossible. The bridge uses the
  actual nonzero symbol of y_Z and the actual forward pairing.
- Section 7 constructs the canonical Euler block E4=P(-4) and the exact
  type of R13. This E4 is not an auxiliary bundle from an earlier argument.
- Section 8 proves that the actual T row to V_alt O has nonzero invariant
  determinant of degree twelve. Universal local Smith theory then gives
  reduced simple cyclic cokernels, and the actual quotient diagram gives
  the sheaf injection R13->F18.

These bridges use actual maps already specified by the retained geometry.
They are not claims about arbitrary morphisms of the displayed types.
The length-one local cokernel statement identifies no equivariant
torsion-line character. No additional prospective map or span lead is a
dependency or conclusion.

## Preparation and verification status

The starting complete draft had SHA256
ab6fe8afbfe5fc004bf213bfd263c1f611962b90e3ad665623913de41ab75ef3.
The new packet replaces its local audit-status and source introduction
with the exact fresh provenance above. The newly defined Euler block is
named E4 throughout the new proof to distinguish it from earlier auxiliary
notation. The mathematical derivation is preserved; unrelated tentative
leads are not included.

FROZEN.json freezes the proof, checker, documentation, and five complete
direct originals. Author replay evidence records two fresh selected-only
directories, each run in normal and optimized Python. The checker is
explicitly not proof; it authenticates bytes and verifies only small
universal character and degree arithmetic. Author self-review and replay
do not substitute for a new independent review of the entire frozen proof
and all five complete originals. That review and the final publication
manifest are to be supplied separately by the parent.

No external state was changed during source authentication or preparation.
There was no selected actual source-instance evaluation, broad scan,
large computation, historical enumerator, local Codex task, GitHub write,
merge, or upstream submission.
