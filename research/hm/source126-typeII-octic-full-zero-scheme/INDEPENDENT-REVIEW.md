# Independent review: full canonical octic zero scheme

The complete proof, checker, and cited source statements were independently reviewed. No mathematical blocker found. This review concerns the canonical nonzero universal generator, not selection of its actual scalar.

## Final bytes and replay

- PROOF.md SHA256: 4e39ef95d7127490044c79f6a69f4e91a21080dd46d29848b92642b08dfcdb49
- verify.py SHA256: 9eff523c37d0c3ba0e629d3e3ed26a1bac450b551c6c70b9083885f7431244d4
- INPUTS.json SHA256: bd65265b6941814f7ae15296c1f9f7ada16a9d26370032ce2ed40e3e460f69f4
- RESULT.json SHA256: 0266df1bb425c04d39f48c3bb01cff3245e67e0a73bc22ab2ba59900bc056b74

Both normal and optimized Python runs pass 53 checks with identical stdout and RESULT.json. All five input files authenticate against their manifest SHA256 and Git blob IDs. PR1000 matches the previously independently reviewed target-factor proof. The old six-axis input explicitly proves rank two at each axis and exhaustion of the rank-drop support in its Section 2.

## Mathematical verification

1. The derivative of a nonzero cubic P-valued covariant is nonzero in characteristic zero. Both it and the original quadratic symbol occupy the unique Hom_G(Sym²A tensor A, P) channel. They therefore agree up to a nonzero constant as whole polynomial families after fixed identifications, not merely in rank. The unique Hom follows from Sym²A = 1 + D and the single P in D tensor A.
2. Euler's identity sends every cubic basepoint into the old rank-drop locus. At each C5 axis the parameter vector is fixed while P has no fixed vector, forcing a cubic zero. Rank two of its derivative and its one-dimensional radial kernel then give rank two on the projective tangent plane. The component ideal has full cotangent image and equals the maximal ideal by Nakayama. Thus the cubic has six reduced basepoints, not the old derivative's length-24 scheme.
3. Wherever the quotient multiplication is onto, its dual has a local left inverse. Consequently the quartic row and cubic covariant generate exactly the same component ideal. This applies at the six C5 axes and off the ten quotient rank-drop points.
4. At a C3 axis the parameter line and O(-1) fiber have S3 sign character chi. The correct source is D tensor chi = chi + 2 standard, while P = 1 + chi + standard. Rank three therefore forces image chi + standard. The nonzero cubic value lies in the unique chi line of P, where the invariant perfect pairing is nondegenerate. Hence its row is nonzero there. Omitting the parameter twist would invalidate this argument; the proof and tests retain it explicitly.
5. In local frames the entries of the full generator are all pairwise products of target-section and source-row components. Its ideal is their product. At a C5 point this is (u²,v²)(u,v) = (u,v)³, of length six. At each C3 point the row is a unit ideal and the target factor has maximal ideal, giving a reduced point. All other points, including the entire conic, have both factors nonzero. The total zero length is therefore 6 times 6 plus 10 = 46.

## Boundaries

The zero scheme is exactly six triple fat points and ten simple points. For a nonzero actual octic scalar the actual symbol has this scheme; for zero scalar it is identically zero. Neither alternative is selected. There is no actual HM instance evaluation, new source-pair exclusion, higher-symbol conclusion, or complete-proof claim. The old rank theorem and the quotient-family theorem are retained dependencies rather than newly recomputed results. The bounded checker supports the argument but is not proof-assistant verification.
