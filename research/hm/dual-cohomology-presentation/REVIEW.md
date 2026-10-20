# Independent mathematical review

Reviewed PROOF.md SHA256: `16c97b425ef751e376db5a7247307e74f2b3ed86df1a5d0a7aee96abaa6ce60b`.

Verdict: the all-degree generation, level socle, and complete quadratic–cubic presentation follow from the pinned actual-module inputs. The new deductions are accepted. This is mathematical review conditional on those inputs, not a fresh certification of all antecedent HM proofs or formal proof-assistant verification.

## Checks

1. The multiplication-pairing indices are correct. The transpose of the action from H_j to H_(j+1) is the action from H_(4-j) to H_(5-j). Thus the established nonzero actions in degrees zero and one force nonzero actions in degrees four and three. Their targets W' and V tensor W' are irreducible. Nonzero equivariance therefore proves surjectivity, completing generation in every degree.

2. The actual perfect S-compatible Serre pairing identifies the graded dual of the generator quotient with the socle in complementary degree. Once generation is proved, the socle is exactly the two-dimensional H_5. Symmetry of the Hilbert function alone would not suffice, but the proof does not use that shortcut.

3. Complementary Koszul exterior degrees sum to five, while paired H degrees sum to five. Consequently complementary internal Tor degrees sum to ten. The determinant factor is trivial for the stated normalizer. The cubic H relation and second-syzygy spaces are dual to the respective cubic K ghosts identified in PR479, so their representation is A tensor U', not A* tensor U'.

4. In the sheaf Koszul sequence for B(t), the q=1 row has internal degree t+1 for K and the q=2 row has internal degree t+5 for H. For t=1,0, the source at (-4,2) is therefore precisely the dual of the quartic or quintic H relation space. No incoming differential of order at least two lies inside the complex. The only outgoing targets have positions (-2,1) and (-1,0).

5. The first target is zero in internal degrees two and one. PR476's injective Euler relation and independent minimal quadratic lifts imply that the degree-two relation presentation is injective; this really proves Tor_2(K,C)_2=0, not merely a dimension coincidence. The other target is a subquotient of T tensor H^0(B(t-1)), zero by simplicity or negative-twist stability. The source thus survives to a zero abutment and must vanish.

6. No linear H relation means the first free relation module starts in degree two. In a minimal exact resolution over S, the fourth free module consequently starts in degree at least five. Together with the complementary-degree-ten Tor pairing this excludes every H relation degree at least six. Graded Nakayama then gives the stated complete presentation, including the choice of cubic lifts and without claiming their images form a direct sum.

## Boundary

The proof uses the actual cohomology, pairing, representation and multiplication inputs of PR479 and the low K relations of PR476. It does not need the later quartic-vanishing theorem for K. It leaves the zero-or-fifteen cubic alternative open and makes no claim of a pure or fully determined minimal resolution. No selected HM/source-instance evaluation, numerical rank computation, source membership test, higher-order lifting, or algebraicity claim was used or established.
