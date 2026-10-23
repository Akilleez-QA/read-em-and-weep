# The fixed negative-pencil quotient by a regular source2 radical image

## Result

Retain all source2 normal-form and actual-source hypotheses of the immutable
PR790, PR794 and PR795 inputs listed below. Let j be any nonzero element of
the two-dimensional pencil radical which is neither the pure V direction
nor the unique exceptional mixed direction of PR794. Put I=im(j), with
images taken at each of the three pencil vertices. Then there is a
G-equivariant isomorphism using exactly the original fixed pencil variables

    N/I is isomorphic to N0 direct-sum N8 direct-sum (V+D)[2].       (1)

Here N0 is the complete separated degree-ten first block, N8 is the complete
degree-eight core of PR795, and (V+D)[2] means V+D at vertex two and zero
at vertices three and four. Its arrows are zero. This is a theorem for all
regular projective radical directions, including the pure A direction,
all balanced endpoints, and both residual coupling classes. The isomorphism
type is independent of the endpoint and coupling; no canonical section or
scalar normalization is asserted.

Q-compatibility is NOT needed for (1). If j additionally commutes with the
actual invariant quadratic Q, (1) identifies the negative-arrow system
underlying the 32-to-28 obstruction quotient. It does NOT say that the
induced Q preserves the displayed summands. Nor does it assert the
existence of such a compatible j, scalarity, a catalogue cut, or a completed
proof repair. No selected actual coefficient, slope, point or matrix is used.

## 1. Exact geometric inputs

All paths are in Akilleez-QA/read-em-and-weep. INPUTS.json freezes their
public URLs, exact bytes, Git blobs and SHA-256 hashes.

- PR790, commit af0e03d26da5e47d18ae732291aca46f4d448dc5,
  research/hm/source2-first-constant-block/PROOF.md: the genuine fixed-pencil
  splitting N=N0 direct-sum NR, with N0 independent of the residual endpoint.
  Its Section 6 identifies these maps with the original actual tensors.
- PR794, commit 7fd254100b83bb03f41b776ea3119690aa51f671,
  research/hm/source2-radical-rank-locus/PROOF.md: every radical image lies
  in the genuinely embedded endpoint pencil NC. For the directions retained
  here, its image characters are (P+D,W'+S+2T,P+D), dimensions(9,18,9).
  The unique exceptional mixed direction instead has middle rank12, and
  pure V has ranks(5,6,4). All statements are uniform for balanced endpoints.
- PR795, commit 3f811311d76914a555c7e7d0c5b887b41805aa6c,
  research/hm/source2-radical-filtration/PROOF.md: Sections2–3 give the
  genuine short exact sequence of fixed pencils

      0 -> NC -> NR -> N8 -> 0,                              (2)

  with NC characters(V+P+2D,W'+S+2T,P+D), dimensions(17,18,9).
  Section7 supplies the elementary splitting mechanism used below; we apply
  it to an individual radical-image quotient, not to the full ideal image.

The complete N8 has dimensions(15,18,12) and characters
(A+V+P+D,W'+S+2T,V+P+D). The complete N0 has dimensions(9,18,16) and
characters(P+D,W'+S+2T,V+2P+D). These are actual fixed pencil models, not
just abstract character triples. N8 comes from the complete osculating
inclusion A O(-6)=U_2^8 inside Sym^8(W) O. N0 comes from the complete
first block U_8^10 inside Sym^10(W) O.

## 2. Quotient of the endpoint pencil

Since j intertwines both fixed arrows, its vertexwise image I is a
subpencil. PR794 identifies its images inside the embedded NC, not just
in isomorphic spaces. Because I3 and NC3 both have dimension18, and I4
and NC4 both have dimension9, their containments are equalities:

    I3=NC3,       I4=NC4.

At vertex two, NC2/I2 has character

    (V+P+2D)-(P+D)=V+D.

The next space of this quotient is zero. Consequently, as a fixed-pencil
system and not only vertexwise as a representation,

    NC/I is isomorphic to (V+D)[2].                          (3)

Quotienting (2) by I gives the genuine exact sequence

    0 -> (V+D)[2] -> K=NR/I --p--> N8 -> 0.                 (4)

In particular p3 and p4 are isomorphisms. This argument neither splits (2)
nor treats an abstract bundle complement as a horizontal one.

## 3. Explicit section commuting with every pencil arrow

Representations of the finite group G over C are semisimple. Choose any
G-equivariant vector-space section s2 of p2, and put

    s3=p3^(-1),       s4=p4^(-1).

For every linear form l in the same fixed two-dimensional pencil space,
naturality of p in (4) gives

    p3 A_l^K s2 = A_l^8 p2 s2 = A_l^8,
    p4 B_l^K s3 = B_l^8 p3 s3 = B_l^8.

Invertibility of p3 and p4 proves A_l^K s2=s3 A_l^8 and
B_l^K s3=s4 B_l^8. Thus s=(s2,s3,s4) is a section in the category of
fixed-variable pencils, proving

    NR/I is isomorphic to N8 direct-sum (V+D)[2].             (5)

Any two s2 differ by a map into the kernel(V+D)[2], which all first arrows
kill. This explains the existence of many valid sections and the absence
of a claimed canonical splitting. Since I is contained in NR and the first
splitting N=N0 direct-sum NR is genuine, taking its quotient and using (5)
proves (1).

The resulting quotient characters are

    (A+2V+2P+3D, 2W'+2S+4T, 2V+3P+2D),

with dimensions(32,36,28), agreeing with subtraction of the regular image.
This establishes the whole arrow-level isomorphism type, not just those
character identities.

## 4. Boundaries and exceptional case

At the exceptional mixed direction, NC3/I3 has character T and dimension6.
Thus p3 in the analogous sequence is not an isomorphism, and the Section3
argument does not apply. No decomposition like(1) is asserted there. At pure
V the image dimensions are(5,6,4), and this theorem likewise does not apply.
Neither exceptional case is excluded as an actual compatible line.

The isolated vertex-two summand does not belong to the negative evaluation
bundle category of PR791's full-faithfulness theorem. Splitting(4) therefore
does not split the original residual bundle, trivialize its coupling, or
extend a pencil endomorphism to the whole HM module. In particular, even
when Q descends, its possible off-diagonal blocks between the summands in(1)
are retained. The original proof repair and four-pair frontier remain open.

verify.py checks exact input digests, character/dimension identities and
bounded exact synthetic sections with nontrivial coordinate shears at the
middle/last vertices. The proof above is universal; its tests instantiate
only the elementary linear-algebra section lemma, never actual source data.
