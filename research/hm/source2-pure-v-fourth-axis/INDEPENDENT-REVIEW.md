# Independent original-fourth component-ideal review

Result: PASS. No mathematical blocker found.

Read the complete proof, checker, fixed model, manifest, and actual quotient
comparison in PR1025. Independently replayed both final verification modes:
30 checks pass, normal and optimized outputs are byte-identical, and both
match RESULT.json. The final artifact hashes match the declared freeze.

## Actual map and sheaf interpretation

PR1025 gives the original-fourth identity iota beta4|D=-sL in coker B with
its stated endpoint identifications. The determinant row N kills B and
embeds that torsion-free cokernel into its ideal-sheaf image in O(6).
Therefore F=NLR is the genuine determinant image of s, and H=FL is the
negative determinant image of this original fourth. Changing a representative
by an image of B changes neither determinant row. A common nonzero target
normalization and the sign leave its component ideal unchanged.

The twists D(-4) to P(-3) to J to O(6) give degree ten, whereas P(-3) to
O(6) gives the nonic degree nine. This does not confuse the degree-four
symbol with its determinant-embedded polynomial row. The conclusion is
about their component ideal SHEAVES in the ambient target line bundle,
not equality of unsaturated graded ideals or a fiberwise claim of tensor
injectivity at singular points of the ideal-sheaf target.

## Local proof and coefficient quantifiers

The inclusion (H) in (F) holds everywhere. Away from the ten C3 points,
the actual universal L is locally a split surjection, so a local right
inverse gives the reverse inclusion. Generic surjectivity alone would
not suffice, and the proof correctly isolates the exceptional orbit.

The whole reduced C3 chart ideal contains all ten points. Ordinary powers
localize to the appropriate maximal-ideal powers, and the independently
computed quotient dimensions are ten, thirty, and sixty. Every first-jet
component of H2 is half that of H1. The nonzero witness and the full ideal
identity (H1)+I^2=I then imply (H)=m for every coefficient pair with
2alpha+beta nonzero, not just a generic pair. On the remaining nonzero
line beta=-2alpha, the certificate (H1-2H2)+I^3=I^2, including membership
in I^2, implies (H)=m^2 by Nakayama on m^2/(H). All higher terms are
controlled by this argument.

The authenticated nonic input gives exactly the same local ideals for F.
Thus equality holds at every C3 point and hence everywhere as a projective
ideal-sheaf equality. It transfers exact component schemes, not only
supports. It does not infer the rank of the original fourth from the rank
of R, cover additional specialized A-kernel classes, or select any actual
gate coefficient. For the zero pair both ideals vanish identically; finite
base-scheme consequences are properly restricted to nonzero pairs.

## Provenance

Fresh direct GitHub reads in this review matched PR1025, PR1037 and PR1043.
The PR1036 proof and unchanged model were authenticated earlier in this
same review session. All declared blobs agree with the retained files:

- PR1025: d036adcf5bc2bfc53e07cd752ff180c5993251f7.
- PR1036 proof: 718f987511b5bf6144a85fc14e8ef343612a4491.
- PR1036 model: a7ca4755e50c85fe7fc20a757125127a05de4056.
- PR1037: 7fdcab9202a78e9f371c32903840969e0453c7b5.
- PR1043: 68bd6866c432983693cd1e66e313d06305187548.

Exact immutable commits, paths, URLs, and SHA256 values are in INPUTS.json.
The old nonic schemes are inputs; the new content is their exact bridge
to the original-fourth determinant row across the rank-drop orbit.

## Frozen hashes

SHA256:

- PROOF.md: 99ed3b4ca07d37837874cecdca59cca18d6b6ce3387fbb4183dc92b47dcf7b86
- verify.py: 541e9abf6c016a033c526aa69a4769bf3f9b63281f9f7d74cffa0357367ea5a9
- INPUTS.json: 2bf38b0275c2ed82a27a222a13870dea50e1ed46e5f5ab618be2c3d9728dd931
- RESULT.json: 19b37fff9e47f64709d9cf63de844cdf102dd665eb36df3b0ff7be86b6840b4f

No actual HM coefficients, selected axis roots, source instances, or actual
ranks were evaluated. No public files were changed.
