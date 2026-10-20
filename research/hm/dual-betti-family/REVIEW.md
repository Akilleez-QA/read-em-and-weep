# Independent mathematical review

Reviewed proof SHA256: `d304619b07ad080fdb61b6ed5b066ec2dfb2cd6031cc9a40ec8815e000339d0d`.

Verdict: accepted conditional on the pinned actual cohomology, multiplication, and presentation inputs. The proof determines the full minimal Betti family with r in {0,15} and s in {0,1}; it neither chooses these parameters nor asserts that every combination is realized.

## Independent checks

1. PR482 determines the first two free modules, and the actual Serre-compatible pairing gives complementary Tor degrees summing to ten and homological indices summing to five. Thus F_4 and F_5 follow. With no linear relations, F_2 begins in degree three and F_3 in degree four. Duality therefore restricts F_2 to degrees three through six. This uses exact minimal resolutions, not just the symmetric Hilbert function.

2. In the coordinate Koszul sequence for B(1), the q=1 and q=2 rows have internal degrees two and six. At (-5,3), Serre duality gives T and the next horizontal group vanishes. Its higher possible targets vanish by Tor_2(K)_2=0 and H^0(B)=0. The middle position (-3,2) has only the displayed incoming and outgoing d_2 maps, since the further outgoing H^0(B(1)) is zero. The final position (-1,1) has no outgoing map; its higher incoming sources vanish by H^3(B(-3))=0 and H^4(B(-4))=0. Zero abutment therefore proves the exact sequence with outer terms T and T tensor U', giving the actual twenty-dimensional representation and its dual.

3. In B(0), the left q=3 differential is dual to the actual degree-one cover of K. Its injectivity leaves exactly the Euler dual C at (-4,3), rather than killing that term. The position (-3,2)=Tor_3(H)_5 must inject by d_2 into the Euler relation C, so its dimension s is at most one. Duality gives the same dimension for Tor_2(H)_5. The d_2 from (-4,3) onto this latter space is justified by the vanishing of Tor_0(K)_1 and H^4(B(-5)), as well as the complex's range.

4. Crucially, the proof does not assume s=1. If s=0, the two outer scalar terms remain available for a nonzero third differential, which must be an isomorphism. If s=1, the two d_2 maps are isomorphisms and remove them earlier. This is the correct exhaustive scalar alternative; the mere presence of an Euler relation does not resolve it.

5. The Hilbert polynomial 2(1+t)^5 yields numerator 2(1-t^2)^5 over five variables. Its degree-four coefficient is twenty. Since the independently established second Tor dimension is already twenty, the third Tor degree-four entry must vanish. Duality removes the remaining possible second Tor degree-six entry. The earlier support bounds now exclude every additional entry, so the displayed Betti family is complete rather than a partial list.

## Limits

This review compares the new deductions with the pinned proof statements, not a fresh certification of every antecedent HM result. Equal-degree adjacent summands are not canceled in a minimal resolution. No self-adjointness or parity shortcut is used to choose s. No selected HM/source-instance evaluation, numerical multiplication matrix, rank calculation, coefficient search, generator/checker, or large computation was performed. The work is mathematically reviewed, not formally proof-assistant checked. The parameters, differentials, original fixed-pair values, source membership, higher-order lifting and algebraicity remain unresolved.
