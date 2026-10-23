# Independent fifteen-axis scheme review

Result: PASS after the homogeneous-ideal clarification described below.

Read the complete proof, checker, manifest, immutable model, PR1036 input,
and prior support and axis-geometry inputs. Independently replayed both
normal and optimized verification: 30 checks pass, outputs are identical,
and agree byte-for-byte with RESULT.json.

## Geometry and normalization

The quadratic invariant supplies an invertible bilinear identification of
covectors and vectors. The degree-five gradient of f6 therefore gives a
section of A tensor O(5); modulo the radial O(4) it is a section of
T_P2(4) by the twisted Euler sequence. The minors with d(delta) give exactly
its zero scheme, including scheme structure. Thus the twist and top Chern
number 31 are correct, not a degree-only guess.

The p=1 critical chart has length 30. The two charts on p=0 exclude every
positive-dimensional boundary component. This establishes finiteness, not
by itself reducedness. Regularity of a finite rank-two section zero locus
on the smooth surface gives total length 31. The stabilizer cotangent
argument puts all 31 distinct axes in this locus, so it is reduced and has
no other support. At non-isotropic axes, differentiating f6/delta^3 and
Euler's identity justify the same critical equations.

The sextic cut is invariant. As a closed subscheme of the reduced critical
scheme it is a reduced union of complete orbits. PR1036 puts all six and
ten axes in p=1, leaving one omitted axis from the fifteen-point orbit.
The affine cut length 14 can therefore come only from the full fifteen
orbit. This accounts for the projective boundary rigorously.

An initial draft called the raw homogeneous ideal J15 the reduced ideal.
That wording was corrected at review: its associated projective ideal
sheaf, or saturation, is the reduced ideal sheaf. The raw degree-six
presentation cannot itself be the saturated ideal of fifteen points,
which necessarily has degree-five sections. The final proof explicitly
avoids that false graded-ideal equality. No computation or conclusion
requires it.

The immutable model preserves the prior apolar forms, projection, and
lift basis. N is the signed maximal-minor row of B; the prior torsion-free
cokernel identification makes N L Ri the actual universal nonic rows up
to common target normalization. This is not replacement by an unrelated
covariant of the same character. Complete remainder equality and the
nonzero coefficient witness prove exactly the coefficient line
alpha+beta=0. Equivariance then gives all fifteen axes or none, not just a
claim about the fourteen chart points.

The ordinary affine-square certificate A+I15^2=I15 localizes to
A+m^2=m. Nakayama gives A=m at every chart point. Equivariance transports
this to the omitted orbit point. This proves reduced AMBIENT basepoints,
not merely simple intersection with a line or conic. The prior placement
puts this line off both jet lines and the conic line. Prior support bounds
exclude a concurrent thirty-point orbit and all other extra support, so
the full length is exactly 49. No actual gate element is selected.

## Immutable source authentication

Fresh direct GitHub reads matched:

- PR1036 proof, commit bb22e239e9423b54487236dba8c4f70f9e6b738f,
  blob 718f987511b5bf6144a85fc14e8ef343612a4491.
- PR1036 model.py, same commit,
  blob a7ca4755e50c85fe7fc20a757125127a05de4056.
- PR1035 proof, commit 6effcd9b61b1942447a2c3f136a6776dda213c15,
  blob eb0b5dc78615331526b679eea952e4a46f7d01ea.
- PR1000 proof, commit 260cd6a777b23dc7ccd5ed956fcf65e17ff56145,
  blob 0ca1301de04a630cb184c4429f5b59e09698c6c9, authenticated earlier
  in this same review session during the finite-support review.

The manifest records exact paths and URLs. Old ranks, old line placements,
and the fixed target scheme remain inputs rather than new claims.

## Frozen hashes

SHA256:

- PROOF.md: df30c1a876f661e5cc439245a0e779ca2644c65aa6a61ea2beef4346a74ad2a7
- verify.py: 0d513c8c8d887366c7739f7fcc4c0496f072f1e24b6637b7affffd2cfbe6d107
- INPUTS.json: a440cea5a2be29405d8b693c7cf5588d5282968c8871b9254e4ee277e52a9b25
- RESULT.json: 7446fc21eab4fde8b803ea196aee8802d77e645c184157e344fe1f4483c57fbc

All computations retained universal polynomial variables. No actual HM
coefficient, source instance, orbit root, or actual parameter was evaluated.
No public files were changed.
