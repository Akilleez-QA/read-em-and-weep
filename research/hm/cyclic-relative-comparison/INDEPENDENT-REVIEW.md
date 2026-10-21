# Independent review: relative cyclic comparison

Reviewed proof: `PROOF.md`, SHA256 `c03f39633de27628feab81520b7a11dc02a2afe1b122f89080ba610a0de07863`.

Verdict: the three sections are mathematically valid conditional on their pinned inputs. This is an independent structural review, not formal proof-assistant verification. No selected HM/source-instance evaluation, coefficient search, or numerical multiplication-rank computation was performed.

## Checks

1. **Actual dual map and family twists.** In degrees 3 and 4, scalar evaluation R_d O -> H_d O(1) is onto because the cyclic submodule equals H in these degrees. The trace identity identifies its dual with multiplication by the tautological binary generator. The resulting binary quotient line bundles have degrees 4 and 2. Dualization therefore gives K3/I3=A_rep O(-4) and K4/I4=V O(-2), with no substitution of the coisotropic ideal for the cyclic annihilator. The restriction to d=3,4 is important: the displayed injective dual map is not asserted in arbitrary degree.

2. **Reduced multiplication and generic rank.** Equivariant splittings exist by the stated H1 vanishing and averaging. The reduced map has source (U'+W0) O(-4) and target U O+O(-2), after the common V factor is removed. Central parity kills W0. Generation of K_w/I in degree 3 makes the lower row onto at every parameter. Off Omega, the relative Tor2(C)_4 target is V O(9), whose multiplicity parity is opposite to 1+U'. Thus rho=0 there. The pinned fiber exact sequence gives a five-dimensional cyclic quartic-generator space, so the reduced map has generic rank three.

3. **Uniform rank without nonflat semicontinuity.** At a rank-three point with a nonzero lower row, some three-row minor containing that row is nonzero. Its degree is 4+4+2=10. The intrinsic common divisor of all maximal minors is invariant and divides this minor's divisor. It is therefore empty by the minimum orbit size 12. On the smooth parameter curve, every rank-drop point would contribute to this common divisor, so rank three holds everywhere. This uses an intrinsic determinantal divisor, not an unsupported invariance assertion for coordinates of an arbitrary splitting.

4. **Cyclic Tor and exact ranks.** The cokernel line has degree 10. Hence Tor1(S/K)_4=V O(10), and passage to the actual image module M introduces O(-1), giving V O(9). The cubic linear-syzygy bundle is an extension of V W0 O(-4) by the fixed ten-dimensional kernel; H1(O4)=0 splits that extension. Its rank is 20. The fiber identities then give rho=u and sigma=5-u, consistent with dim Tor2(L)_4=u+20-rho=20. No semicontinuity of the nonflat column Tor2 target is used.

5. **Actual sigma source.** The pairing gives B=D5(C), with B3=A_rep O(-3), B4=V O(-1), and B2=0. Consequently Tor1(B)_4 is directly the kernel of T B3 -> B4, not a guessed dual Betti bundle. The quadratic evaluation row has kernel W O(-4), and the parity-forbidden row gives W0 O(-3). The resulting source is a bundle and its formation commutes with fibers.

6. **Elementary modification.** The sigma target is the locally free cyclic Tor bundle established above, so its map specializes to the fiber comparison used to define sigma. Parity kills W0 O(-3); the remaining nonzero degree-13 row vanishes exactly on Omega. Its invariant common divisor has degree at most 13 and contains Omega. The orbit bound therefore forces precisely the reduced degree-12 divisor, with no extra point or multiplicity. Dividing leaves a basepoint-free linear row W O(-4) -> O(-3), whose kernel is O(-5). Restoring V gives the claimed kernel and image, and torsion length 5 times 12 equals 60. The proof appropriately does not identify the residue line's equivariant linearization with a trivial one.

## Limits

The review assumes the published actual-module pairing, binary multiplication identifications, representation extensions, and the proved common 0/5 patterns of a and u. It does not independently reprove all those dependencies. The middle obstruction b, the original fixed scalar pair, higher-order lifting, and algebraicity remain outside the conclusion.
