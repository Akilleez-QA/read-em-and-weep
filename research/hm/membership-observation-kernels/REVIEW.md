# Independent final-byte review: membership observations

Reviewed 2026-10-23. Verdict: **PASS with the stated conditional scope.**
No required mathematical correction was found.

This verdict binds only to `MEMBERSHIP-OBSERVATION-COROLLARY.md`, 7,267
bytes, SHA-256
`72b06e5d3afb605c587bc84998d42eef3fce2c9d73095e0209aefd99b81b8af0`.
The proof was not modified. This is a fresh review of the written
argument, not Lean certification and not an actual physical-source test.
The optional nonlinear-polynomial detector extension is not part of the
reviewed artifact and is neither audited nor certified by this verdict.

## Provenance and current coordination

Read current PR1 coordination through
https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6357157412,
including the PR889/891 interfaces, the PR894 membership handoff at
https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6357098313,
and the later PR896 limited multiplier formalization. None supplies the
remaining actual source-membership or physical calibration observations.

Independently fetched the two direct proofs at their immutable commits
and compared all bytes with the local copies:

- PR894 `c963b48d8bd28eaac1dc2db1116fc1c430ba18b4`,
  `research/hm/physical-source-membership/PROOF.md`:
  SHA-256 `74d801f850d281658955f7583a838c90ff49fa2f9122dea8a2391e01a71dcc0b`.
- PR891 `eb83daa45fe4686a9f55da604fb2cc8c28d47fb0`,
  `research/hm/generic-parameter-calibration/PROOF.md`:
  SHA-256 `98fa36fff78c35f5dc071bbc52aa5e44e045c5f3a8252672a63e1015d027eed9`.

Their current PR heads still matched those commits during this review.
Also independently fetched all seven original source files at the
commit/path pairs in `SOURCE-MANIFEST.json`. Each matched its local copy,
manifest byte count, SHA-256, and Git blob SHA-1. The relevant statements
in those sources were checked directly. This authenticates and audits
the inputs used here; it does not re-prove every transitive geometric
dependency of the imported theorems.

## 1. The defect is legitimately defined before membership

Section 1 expressly requires closed global cochains, coherent polynomial
equivariance on the entire homogeneous parameter/source module, the fixed
canonical Z, the preceding full-family division, and canonical or
independently compared b. These are prerequisites, not consequences of
the proposed observation test.

Their bidegrees make T_W cubic in a and linear in h. Closedness places
its coefficient map in Hom_G(R,Z^1_4). The positive-twist full-complex
comparison identifies its cohomology with the actual H^1(B(4)); the
central-even convention places the image in M4. Canonical raw-cubic
factorization removes the quotient-P4 component, so the independently
defined class really lies in Hom_G(R,I). An arbitrary closed V or an
uncompared correction would not justify this last reduction.

The input used from the global-complex source is termwise acyclicity,
not its later existence assertion for E. The input used from canonical
division is the quotient factorization, not a desired equation dE=T_W.
There is therefore no circular appeal to the membership being tested.
Exactness of equivariant Hom over C then proves

    [T_W]=0 if and only if T_W=dE

for one global equivariant polynomial family E. This does not glue
unrelated pointwise primitives. The uniqueness statement remains only
modulo degree-minus-one boundaries, using H^0(B(4))=0.

## 2. Exact arithmetic and target-independent cyclic support

The three tensor decompositions were independently checked against the
five A5 character classes. A tensor D and V tensor D both have character
(15,-1,0,0,0), equal to A+V+P4+D5. P4 tensor D has character
(20,0,-1,0,0), equal to A+V+P4+2D5. Pairing multiplicities with
I=2V+3P4+3D5 therefore gives exactly

    M_A: 2+3+3 = 8,
    M_V: 2+3+3 = 8,
    M_P: 2+3+6 = 11.

These total 27 scalar equivariant-Hom parameters. They are not dimensions
of a particular output vector or ranks measured on an actual instance.

For a nonzero abstract a, equivariance gives

    F((g a)^3 tensor h)=g F(a^3 tensor g^-1 h).

Thus zero evaluation on ALL of D implies zero on Gspan(a^3) tensor D.
The converse is immediate. Since S=A+V+P4 is multiplicity-free and
semisimple, its cyclic submodule is exactly the sum of summands whose
projections of a^3 are nonzero. One may apply the central isotypic
projectors in C[G] to see both inclusions. Consequently the kernel is
exactly the direct sum of missing-support Hom spaces, proving (C3),
including its equality rather than merely a dimension bound. This
argument is independent of the old trace target and applies to I.

The proof correctly uses the primal Sym^3 A and does not silently
identify polynomial functions with that primal space. It also does not
assert that all formal support patterns occur.

## 3. Generic open, special observations, and line fibers

Each projected cubic a -> pi_X(a^3) is nonzero as a polynomial map:
otherwise the projector would vanish on all pure cubes, which span
Sym^3 A in characteristic zero. Each zero locus is proper closed.
Irreducibility of P(A) makes the intersection of their three open
complements nonempty. Thus the cited generic-open argument proves
injectivity for I just as it does for the earlier target.

The special supports imported from PR891 agree with the geometric
arguments in PR889: axis cubic vanishing is P4, whereas square cubic
vanishing is the discriminant multiple of A. Hence

    ker Ev_p = M_P,  dimension 11; image dimension 16;
    ker Ev_s = M_A,  dimension 8;  image dimension 19.

Their intersection is zero, so the combined image has dimension 27.
No association between the chosen abstract axis and square is needed.
Neither observation alone is injective on unrestricted M.

For completeness, let E_p and E_s denote the respective observation
images. Evaluation induces isomorphisms

    E_p = M/M_P = M_A directsum M_V,
    E_s = M/M_A = M_V directsum M_P,

where the equal signs denote these quotient identifications, not literal
raw-coordinate equalities. Projecting those identifications onto M_V
gives the two maps needed to define a fiber product. A compatible pair
has one common M_V component and unique M_A,M_P components, so it comes
from a unique F in M. This proves the claimed fiber-product description
and the exact count 16+19-8=27.

The retained O(3) fiber is essential and correctly handled: replacing a
representative by lambda a multiplies evaluation by lambda^3. Vanishing
and injectivity are invariant, but numerical output coordinates at
different parameter lines cannot be directly identified. The shared
eight-dimensional channel is a quotient channel of the two images,
not an intersection of raw target coordinates or eight unqualified
equalities between them.

## 4. Membership and trace calibration remain separate

Because F_W is already defined, an injective complete cohomology-family
observation can establish F_W=0 and hence membership. This uses the
whole h-linear family of actual cohomology classes. It is neither one
source value nor one scalar functional. The special-orbit alternative
has the same full-family requirement.

Nothing here defines eta on a source outside its certified domain.
Nothing compresses M through the ten-dimensional trace-family space.
The lower bound 27-10=17 for the kernel of an independently defined
linear detector into that space is therefore unchanged. Source
membership must still precede the separately authenticated physical
contraction, trace, multiplier, and reference-calibration interfaces.

## Scope and remaining certificate

PASS is conditional on the imported actual-cohomology theorems and all
explicit full-family hypotheses. The new result is a sharp observation
interface, not the required observations themselves. It selects no
actual parameter, source, point, coefficient, derivative, matrix, or
instance rank; constructs no primitive or physical trace row; and
authenticates no concrete packet. There was no actual-instance scan,
finite-model run, or large computation in this review. Only written
mathematics, immutable-source retrieval, and byte/hash checks were used.

The unresolved action remains to authenticate the supplied complete
closed coherent physical family and establish its required cohomology
zero observations, or otherwise prove its defect zero. No source
exclusion, global theorem repair, or nonlinear detector result follows
from this review. Existing proof and review files were preserved, and
no external write or publication was performed.
