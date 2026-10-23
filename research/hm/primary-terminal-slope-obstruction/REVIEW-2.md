# Independent whole-proof review 2

## Verdict

PASS for the canonical primary-terminal inclusion and the four-type necessary reduction, relative to the six frozen actual-HM inputs. I found no source2, nonzero pure-V compatible-radical, residual-large, R=0, positive-projector, or Gauss-horizontal hypothesis imported into the new lemma.

This verdict does not certify the geometric completeness of a rank-three source ledger, actual realization of any surviving bundle type, a global rank-three exclusion, or HM nonexistence. The proof explicitly preserves these boundaries.

Reviewed proof SHA256:

    d5feb4b4478b5ec8178a049124179d25473b2e2526b20823a40f6dc60095e28e

No change to the reviewed proof or its six originals was made.

## 1. Independent authentication and executable controls

I independently fetched all six complete files through read-only GitHub file requests with the exact immutable commit refs. The returned URLs and Git blob SHAs agree with the frozen manifest. I saved the independently fetched contents separately and checked, for every file:

- Exact byte equality with its complete frozen original.
- Byte length.
- SHA256.
- Git blob SHA1 computed from the canonical blob header and the complete bytes.

All six passed. Public source metadata is recorded in REVIEW-2-AUTHENTICATION.json. The independently fetched originals byte-match the complete originals in inputs/.

I ran verify.py both normally and with Python -O. Both exited successfully with PASS and 150 controls; their complete JSON outputs are byte-identical to one another and to RESULT.json.

Verifier SHA256:

    d82507bdbab9f54b3c177727367010b2186c24572e8a1bda657d9474248bf06e

Manifest SHA256:

    f855db17d0fe579f791cf56b4fabe994c6c4d541effef8fa61e075ff64c798eb

The verifier uses only standard-library code and explicit require checks, not removable Python assert statements. Its representation calculations concern fixed abstract conjugacy classes and its bundle calculations concern universal formal splitting data. It does not evaluate selected HM/source coefficients, maps, tensors, matrices, points, parameters, derivatives, jets, or actual-instance ranks. Its printed canonical conclusion is a description of the written theorem, not an independently machine-proved embedded-subspace theorem.

## 2. The primary pencil is genuinely source-independent

PR477 constructs an actual polynomial-module map before proving its injectivity. Consequently the inclusions in K5 and K6 are not unrelated degreewise character embeddings. In the grading used by the new proof, they give the actual coefficient inclusions

    U tensor H1(F(2)) -> H1(B(4)),
    U tensor H1(F(3)) -> H1(B(5)),

and the same negative variables intertwine these inclusions.

PR1120 supplies U=P, H1(F(2))=1+A+T6, and H1(F(3))=W in the physical parity convention. Thus Y=1+A is the actual positive primary piece, while Z=W is entirely negative. Positive-coordinate multiplication V tensor Y -> Z is zero by this parity, not by a pure-V source hypothesis.

If y is in the kernel of the actual curry Y -> Hom(W,Z), every negative coordinate kills it. Every positive coordinate already kills it. For a fixed nonzero u in U, the actual PR477 image of u tensor y is therefore in the degree-five socle of K. PR486 excludes this socle, and PR477 injectivity then gives y=0. This is valid for every y in the kernel; no irreducibility of Y or selected multiplication value is needed. The equal dimensions, both four, now make the actual curry an isomorphism.

Evaluation on the tautological line is surjective because all of Hom(W,Z) is available. Its kernel is

    Z tensor (W/O(-1))* tensor O(-1) = Z O(-2),

with the fixed determinant convention. Tensoring with U gives the stated exact primary pencil. This is a proof of surjectivity over the whole parameter line, not a generic-point assertion.

PR1122's later source2 hypotheses furnish its separated first-block projector and its final contradiction. They are not needed for the argument just checked. The new proof rederives the independent primary-pencil part instead of treating the conditional conclusion of PR1122 as an unconditional input.

## 3. The reconstructed terminal pencil is the actual original pencil

For clarity, the natural sequence in Section 3 follows directly on T x T from

    0 -> p1*F tensor p2*O(-1)
      -> p1*(F(1)) -> delta_*(F(1)) -> 0.

The displayed sequence uses the standard diagonal equation and the fixed determinant trivialization. Pushing to the second factor, H0(F)=H0(F(1))=0 gives

    0 -> F(1) -> H1(F) O(-1) -> H1(F(1)) O -> 0.

This construction is natural for every bundle morphism F -> F'. It does not require a bundle splitting or a projector compatible with positive-coordinate multiplication.

The parameter check in the proof is essential and correct. PR1056 Section 2 identifies cohomological multiplication by u with m_y and multiplication by v with -m_x for the original pencil u m_x+v m_y. The diagonal equation produces

    v H1(mult_u) - u H1(mult_v)
      = v m_y + u m_x.

Thus the terminal arrow is the actual original negative pencil on the same parameter line. This is not an independently rotated isomorphic pencil. A common harmless global determinant sign would not alter naturality or kernels, but no such independent change is needed here.

PR1056 explicitly separates its unconditional Sections 2–4 from its conditional bundle-type computations in Section 5. The construction used in the new proof belongs to the unconditional part.

## 4. Canonical slope filtration, both coefficient maps, and exactness

On P1, H0(E(1))=0 forces all ordinary splitting degrees to be at most -2. The canonical Harder–Narasimhan truncation E_{>=-3} consists of the degree -2 and -3 pieces. The construction is independent of an arbitrary Birkhoff splitting and is G-invariant. Its quotient E_{<-3} is locally free and has all splitting degrees at most -4.

Both H0(E_{<-3}) and H0(E_{<-3}(1)) vanish, so the natural terminal reconstruction applies to this quotient. Naturality gives the coefficient maps from the actual E terminal pencil to its quotient pencil. Composing with the actual primary inclusions therefore preserves both coefficient arrows. No Gauss connection, positive-coordinate projector, or source decomposition is involved.

The induced kernel map has source (U tensor Z) O(-2) and target E_{<-3}(1). Every target summand has degree at most -3, hence this map is zero. This is a genuine global Hom vanishing.

It follows that the first coefficient arrow q1 vanishes on the entire primary kernel. Since the primary sequence is exact as a sequence of vector bundles, q1 factors through its quotient (U tensor Z) O. The new factor maps a trivial bundle to H1(E_{<-3}) O(-1), so it is zero. Therefore q1=0. Commutation of the two pencils and surjectivity of the primary terminal arrow then imply q2=0.

The proof correctly uses both coefficient arrows. A bare injection of the primary kernel bundle into E(1) would not provide this conclusion, because it can map nontrivially into the degree -1 summands of E(1).

For the canonical short exact bundle sequence twisted once, the H1 map from E_{>=-3}(1) is injective because H0(E_{<-3}(1))=0. It is the kernel of H1(E(1)) -> H1(E_{<-3}(1)), and the latter is onto because H2 vanishes on P1. Thus q2=0 locates the actual embedded primary terminal subspace in the stated canonical H1 subspace. This is stronger than, and logically prior to, a character containment.

Finally, E_{-2}(1)=R2 O(-1) is acyclic. The canonical degree -3 slope quotient is R3 O(-3), with R3 as defined by its twisted global sections. Consequently

    H1(E_{>=-3}(1))
      = R3 tensor H1(O(-2))
      = R3

canonically after the fixed determinant trivialization. Equivariance and injectivity are preserved throughout. The actual terminal representation is U tensor Z=P tensor W=W'+T6, so its injection into R3 is justified.

## 5. Four-type deduction and excluded conditional types

ACTUAL supplies the exact necessary equations and genuine coefficient representations quoted in Sections 1 and 5. The new proof does not alter their conventions.

Since R3=a W'+b T6, the actual injection forces a>=1 and b>=1. Nonnegativity together with a+d+g+h=1 forces

    a=1, d=g=h=0.

The remaining equations become

    b+c+e+f=3, b>=1, c>=1, e,f>=0.

Equivalently, (b-1)+(c-1)+e+f=1. A sum of four nonnegative integers equals one precisely when exactly one is one. This proves completeness of the four possibilities without any actual-instance scan. Substituting into the authenticated R2 and other block formulas gives exactly the four displayed bundle types.

Their formal ranks, degrees, terminal characters, and twist-two Euler characters agree with the verifier. This establishes necessity only. It does not show that all four occur, nor that any occurs for the fixed actual pencil.

The conditional PR1056 types E10 and E14 have no degree -3 coefficient representation, and E13 has only T6 there. None can contain the newly proved W'+T6. These exclusions are valid for those exact types. They do not establish that the ledger accounts for every geometric rank-three source or that every abstract source transfers to the actual E.

## 6. Scope and review limitations

The proof's mathematical dependency is the actual module and bundle structure in the authenticated originals. Authentication proves that these are the pinned original texts; it is not a recursive proof-assistant verification of all historical HM dependencies.

Within this stated scope, the new embedded-subspace theorem, its source-independent nature, and its four-type consequence are sound. I found no blocking gap or required mathematical correction.

I made no public writes. All work was read-only source retrieval, inspection of the complete originals and proof, local review/authentication files, and the bounded universal verifier runs.
