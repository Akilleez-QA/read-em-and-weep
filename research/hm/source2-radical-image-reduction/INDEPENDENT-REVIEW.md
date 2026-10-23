# Independent review: conditional source2 radical-image reduction

## Frozen artifacts checked

Reviewed on 2026-10-23 UTC, separately from the author's self-check.

- PROOF.md SHA-256: `d86b7ebf11aa7684a522f408a641b2a0d74c239d521ef9bf829815ae58551fb4`
- verify.py SHA-256: `e4ba300e51eb8315b941a818911913d4e85b724c3c46621193ffc04a1d027bed`
- INPUTS.json SHA-256: `e4e4a12cfb8f0f6b11e5e935246ddb8891e1d979b2acf7192bd11476fe02502a`

Verdict: PASS for the stated conditional deduction. No source2 exclusion,
existence claim for a compatible radical line, or complete repair follows.

## Independent mathematical checks

1. Read the full new proof and exact PR794 proof. Its exhaustive projective
   rank locus really has only pure V (5,6,4), one mixed exceptional direction
   (9,12,9), and all others (9,18,9). The exceptional direction is not an
   axis. The endpoint arguments use independent D images and independent P
   functionals, so the middle-rank drop cannot cause an unlisted endpoint
   drop. The new proof retains every stratum and both residual coupling
   classes, within the imported balanced-endpoint hypotheses.

2. Checked the actual rank33 theorem and the published PR949 proof copied
   as inputs. PR949 supplies only the bound of one on compatible radical
   dimension. It does not guarantee a line or identify its channel. The new
   proof makes precisely this distinction; its conditional cancellation is
   logically independent of the PR949 dimension bound.

3. For non-V j, injectivity of Q on the P constituent follows from the
   absence of P in kerQ. Independently, j4 induces a surjection from
   cokerQ=P onto I4/j4(imQ). Hence the latter has no D. Semisimplicity and
   multiplicity one in I4=P+D force the entire D into j4(imQ)=Q(I2).
   Therefore the actual restriction Q:I2->I4 is invertible, not merely a
   map between equal characters. The quotient rank is24, with natural
   kernel A+D and cokernel P.

4. Checked both chain-map equations and both homotopy equations in Section3.
   For M=[B C;0 D], s0=(-B^-1 C,1), s1=(0,1), and
   h(v,z)=(B^-1 v,0), direct multiplication gives Ms0=s1D,
   hM=1-s0p0, and Mh=1-s1p1. Invertibility of B(0) makes B^-1 an
   honest power-series matrix, with no negative powers. Thus maps and
   homotopy preserve every t-adic filtration level and survive reduction
   modulo every power of t. This proves filtered homotopy equivalence,
   stronger than a bare quasi-isomorphism. The associated-graded complexes
   are homotopy equivalent; their cohomology pages and all subsequent
   Bockstein differentials are identified. This does not assert equality
   of the raw associated-graded vector spaces, nor an equivalence of the
   entire three-vertex quiver or the full HM module.

5. The pure V long exact sequence was independently recomputed. Schur's
   lemma gives Q(I2)=0, so I2 is precisely the D in kerQ. Compatibility and
   dimensions give imQ=kerj4. Square-zero then gives I4 subset imQ. The
   connecting segment is consequently
   0 -> D -> A+D -> ker(barQ) -> P -> P -> coker(barQ) -> 0,
   with the map between the two displayed P spaces zero. Thus
   0 -> A -> ker(barQ) -> P -> 0 and coker(barQ)=P.
   Its semisimple character is A+P, dimension7; the quotient rank is29.
   The natural original kernel map kills D and has image A, so it cannot
   give the non-V Bockstein equivalence even on initial cohomology.

6. Recomputed all quotient dimensions: (36,48,33) for pure V,
   (32,42,28) for the exceptional mixed direction, and (32,36,28)
   otherwise. No claim concerning an actual selected direction is needed.

## Executed verification

Ran both `python verify.py` and `python -O verify.py` independently.
Both exit successfully, report981 checks, and give byte-identical JSON.
All seven copied input SHA-256 and Git blob digests pass. The checksum
manifest identifies immutable public commits and paths, including exact
PR794 and published PR949. Inspection of the checker confirms that its
matrix tests are explicitly synthetic formal-series regressions and a
pure V Schur-block negative control, not actual-source evaluations.

The bounded tests support the displayed formal identities and character
bookkeeping. They are not independent proofs of all imported geometry,
formal proof-assistant verification, or evidence that a compatible line
exists. This independent review itself is supporting verification, not an
additional mathematical reduction beyond the new theorem under review.
