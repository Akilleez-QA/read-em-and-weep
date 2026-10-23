# Independent conic ambient-scheme review

Result: PASS. No mathematical blocker found.

Reviewed the complete final proof, checker, manifest, fixed model and
immutable inputs. Independently replayed the final normal and optimized
runs: all 30 checks pass, outputs are byte-identical, and both agree with
RESULT.json.

## Core scheme argument

The pinned pairing makes cP^T GP cP an invariant sextic. Its whole binary
restriction under (p,q,t)=(u^2,2uv,v^2) is nonzero of degree twelve; the
reported leading coefficient is 3sqrt(5)/16. This is a polynomial identity,
not an evaluation at a selected square. The unique invariant binary line
and its reduced divisor identify its restriction with the twelve-point
orbit. Since the conic is smooth, (delta,f6) gives the reduced ambient
complete intersection of that conic and divisor.

The complete affine Groebner basis has colength twelve. On p=0, delta
forces q=0, and the remaining t=1 boundary chart has unit ideal. Thus the
affine chart contains every orbit point. The squarefree elimination and
nonzero constant-term checks separately confirm reducedness of this
presentation. No boundary point or nonreduced boundary structure is lost.

The immutable model and the previously justified determinant cokernel
map give the genuine universal nonic row F1=NLR1, up to a common nonzero
target normalization. The code reconstructs it in that same basis and
checks every component, not only a representative coefficient.

The inclusion F1 in I and exact equality (F1)+I^2=I are verified for the
whole affine ideal. Localizing gives A+m^2=m, and Nakayama on m/A gives
A=m. Consequently the nonic component ideal is the AMBIENT maximal ideal
at each of the twelve points. This is stronger than the older reduced
conic intersection and does not confuse the two assertions.

## Complete length-46 consequence

PR1036 puts R1 off both prescribed-axis jet lines, so its local scheme at
the sixteen old axes is exactly Z of length 34. PR1040 restricts the
fifteen-axis occurrence to the distinct line R1-R2. PR1042 excludes all
thirty-point base orbits in the full pencil. PR1035 exhausts the remaining
off-conic alternatives, and PR1033 identifies the conic support. Together
with the new ambient maximal ideals, these yield precisely Z disjoint
union the twelve reduced conic points, with total length 46. Neither
additional support nor unaccounted thickness remains on this line.

This does not determine whether the actual gate is nonzero or lies on
R1. Old occurrence lines, old support exclusions, and the length-34 scheme
are properly retained as inputs, not relabeled as new deductions.

## Provenance

Fresh direct GitHub reads in this review session authenticated all declared
blobs. The new PR1040 and PR1042 pins were read during this task; the other
four were read during the immediately preceding associated reviews.

- PR1036 proof: 718f987511b5bf6144a85fc14e8ef343612a4491.
- PR1036 model: a7ca4755e50c85fe7fc20a757125127a05de4056.
- PR1033 proof: 5625cb9e0a6ee2a53470616b82b3c93d76f0042b.
- PR1040 proof: f42554d807c0b66a0eea5bc8453e3a2682b94919.
- PR1035 proof: eb0b5dc78615331526b679eea952e4a46f7d01ea.
- PR1042 proof: c85eecff0c7bdc8caa7a74423b2bee318b35d700.

INPUTS.json retains exact commit IDs, repository paths, URLs, and SHA256
values. PR1042 is fixed at 848e947ae1575434e93a82a4ec8ba235606e3224.

## Frozen artifact hashes

SHA256:

- PROOF.md: f4e837a2365306caae9d8872f8fb00e5fe5304819a48e0dbe13bf548d6e1e443
- verify.py: e29e0bca5e27c34d60cc52cbd6abd7974d61a3fcd192c238191321c0c8e83d02
- INPUTS.json: 4f9496d3bf7632400fbab152b03d7346c3e7f90d38d583d21c2de2b303b5d25b
- RESULT.json: 45dc452be0389e53dd6aaae983e30a8c7a9b27b1d23627803c1164ad7354cd8d

No actual HM coefficients, selected orbit roots, source instances, or
actual ranks were evaluated. No public files were changed.
