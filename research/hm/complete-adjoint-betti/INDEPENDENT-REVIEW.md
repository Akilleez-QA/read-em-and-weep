# Independent mathematical review

Reviewed the complete adjoint cohomology Betti-family proof against its pinned module inputs, in particular the local copies of PR479, PR481, PR482, PR484, PR485, PR486 and the exceptional cohomology input PR466. The final reviewed proof has SHA256 042f07bdd34533b5467bd56d515ad58e683fa5b5e8a8775bf1a27a04d8ea1a27.

## Verdict

Accepted as a structural mathematical proof, conditional on the cited inputs. No mathematical defect was found in the new degree-four argument or in the completion of the table. The minor terminology correction has been incorporated: the finite generating polynomial for the graded dimensions of K is correctly called its Hilbert series, not its Hilbert polynomial.

## Checks

1. The coordinate Koszul complex tensored with B(3) has terms Lambda^i T tensor B(3-i), so its q=1 and q=2 rows are exactly internal degrees four of K and eight of H. Its column interval is [-5,0].

2. All section-row terms vanish because the twists lie in [-2,3], and the proof correctly establishes positive-twist vanishing through Riemann–Roch and higher-cohomology bounds, not stability alone. All q=3 terms vanish, including the exceptional twist -2 supplied by PR466. The q=4 row is dual to section twists [-8,-3], hence also vanishes. The only two nonzero possible rows after E1 are q=1 and q=2.

3. With differential bidegree (a,1-a), only d2 can connect those remaining rows. Thus the source (-4,2) and target (-2,1) have no alternate incoming or outgoing differential capable of killing their kernel or cokernel. Zero abutment forces the d2 isomorphism. The compatible duality shift is 5+5=10, so Tor_4(H)_8 is dual to Tor_1(H)_2, giving dimension ten and representation A tensor W' with the stated determinant convention.

4. Tor_3(K)_4 can receive only Tor_5(H)_8. This is dual to Tor_0(H)_2, which is zero because H is generated in degree zero. Its outgoing q=0 target is zero; higher incoming positions lie outside the complex. Hence Tor_3(K)_4 is zero, rather than merely unconstrained by the Hilbert numerator.

5. Independence of the quadratic relation classes modulo T epsilon and injectivity of the Euler column genuinely rule out degree-two second syzygies. Minimality and exactness then force F2 to start at degree at least three and subsequent free modules at degrees at least four, five, and six. The zero-column exclusion in the proof justifies this step without an unstated purity assumption. These bounds cover the higher homological indices in every internal degree at most four.

6. PR484 gives every degree-five entry and every degree-six entry, not just an alternating sum. PR485's comparison applies to every n>=7 in indices 2 through 5, and the exact PR486 section resolution supplies all of those entries. The generator/relation bounds handle indices zero and one; Hilbert's syzygy theorem handles indices above five. Thus no internal or homological degree is omitted.

7. The two cubic terms have opposite homological signs and cancel in the alternating numerator. The resulting numerator agrees with the established graded dimension series. This is a consistency check only and does not decide r or exclude further ghosts by itself. The proof expressly avoids asserting existence of both r alternatives.

## Scope

The review establishes correctness of the deduction from pinned results, not an independent reconstruction of all upstream HM theory or a formal proof-assistant verification. No selected actual HM/source evaluation, numerical matrix or rank computation, coefficient search, generator/checker, or large computation was performed. The actual cubic alternative remains open, as do the original fixed-pair, source-membership, higher-order and algebraicity questions.
