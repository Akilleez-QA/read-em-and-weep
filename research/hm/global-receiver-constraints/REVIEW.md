# Final independent review

Status: PASS after independent whole-proof review and normal/optimized checker replay.

Frozen PROOF.md SHA256:

    bf15c52dd38736960f30c1746a2c3342725caaaae21f7a54c003e538a85ce356

The author derived the receiving-subbundle and joint-kernel constraints. A separate mathematical reviewer read the complete frozen proof, both exact input interfaces, the manifest and the checker. A further root-level reading checked the full argument. No substantive defect or required correction was found.

The independent review verified the following substantive points:

- The receivers are actual images of all equivariant channels, not merely character upper bounds. The quadratic and Euler exact sequences prove the common-image factorizations and supply channels generating the entire stated receivers.
- The joint kernels are exactly W O(3) plus O(4) in five rows and the quadratic-tautological O(2) in the other two. The latter lies inside the former when applicable; it is not counted as an additional independent summand.
- All seven Hom_G(C,O(6)) vanishings hold. The unconditional O(2) inclusion is selected by the actual finite geometry, and its containment in the global Jg follows from the actual bridge.
- The row18 receiver is independent of nonunique complements: all permissible shears into W O(7) factor through its O(6) subbundle. No unique receiver complement is asserted.
- Every named global inclusion is a subbundle, with a locally free quotient. The proof distinguishes the kernel sheaf from possible extra pointwise kernels at a rank drop.
- In a line-receiver row a nonzero actual map is onto on every fiber, giving kernel rank4 degree16; the zero alternative gives all S5 of rank5 degree22. Neither alternative is selected.

The reviewer independently ran `python verify.py` and `python -O verify.py`; both passed. Both exact local input files matched their recorded byte counts, SHA256 hashes and Git blob identities, and matched the input originals read for review. The author additionally freshly fetched the raw immutable public files and matched their bytes exactly. The reviewer did not claim a separate remote fetch. INPUTS.json and REPRODUCE.md give public immutable references and raw-byte reconstruction instructions.

The checker uses bounded exact character arithmetic, verifies channel counts and vanishings for the seven fixed abstract types, checks ranks/degrees and authenticates inputs. It is not a formal proof checker. Universal evaluation geometry, receiver canonicity and actual subbundle consequences were reviewed mathematically. No actual HM/source coefficient, point, parameter, derivative, jet, matrix or instance rank was evaluated. No actual row or scalar is selected, and no external publication was performed during review.
