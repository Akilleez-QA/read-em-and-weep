# Independent review: paired middle stabilizers

Reviewed proof SHA-256: a5a10ff88ed4ac8aeb5e833c0c580da1c8cf96c4a8cbed1f018f32d75b102071.

Verdict: the five sections are correct conditional on the exact structural inputs pinned in PROOF.md. This is an independent mathematical review, not a proof-assistant check or an evaluation of an actual selected HM parameter.

## Equivariant determinant audit

The character summands must first be regarded as modules for the inverse image C_tilde in the finite normalizer. Individual coefficient lines need not descend to C. The reviewed version explicitly makes this distinction and uses no splitting of the extension.

The determinant of the rank-two target is L_chi^2 tensor det(W0) tensor O(4), and det(W0)=1. Dividing by the rank-one source yields the stated actual linearization of F_chi. Nondegeneracy and invariance of the trace pairing on each endomorphism representation identify inverse character lines dually. For a nontrivial character, passing from End(T) to End_0(T) removes only the trivial summand, so this pairing remains perfect on the relevant pair. Tensoring the two determinant identities therefore cancels all coefficient lines. The product descends through Gamma to the standard C-linearization of O(8). Duality with its two tautological twists gives the standard O(10) for the paired scalar. Dualization interchanges character labels but does not change this paired product.

## Stabilizer and root audit

An order-five element on W' has distinct reciprocal primitive fifth-root eigenvalues. The degree-ten invariant monomials have indices k=0,5,10. The displayed decimic therefore has fixed-point vanishing orders only 0,5,10. Factoring its quadratic in x^5,y^5 gives exactly the two degree-five divisors asserted; a nonfixed root has multiplicity at most two. These statements allow the scalar to vanish identically and never infer its nonvanishing.

Finite projective point stabilizers are cyclic: the derivative character at a fixed point is faithful for a finite subgroup in characteristic zero. An order-five subgroup consequently fixes points in the unique size-twelve orbit Omega.

## Multiplicity and Betti audit

A nonidentity element of C5 acts unipotently on the two-dimensional character space over F5. Its fixed line has four nonzero vectors and hence two inverse pairs. No additional pair can be fixed by swapping its two representatives, since an odd-order group cannot act nontrivially on a two-element set. The other ten inverse pairs split into two free orbits of size five.

In the paired-nonzero branch, each of the twelve scalar divisors has degree ten. Their sum is invariant under transport by G, whether or not individual sections are globally invariant. Transitivity on Omega gives a common multiplicity n with 12n<=120. A vanishing fixed pair costs at least five and a vanishing free orbit costs at least five. Thus s+t<=2, and the possible numbers of vanished pairs are exactly the necessary candidate list {0,1,2,5,6,10}. Adding twice this count to the trivial-block corank one gives the asserted list. This is a necessary restriction, not an existence claim for every listed value.

In the identically-zero branch, all twelve paired two-dimensional blocks are zero. The pinned trivial-block result then gives exactly 24 off Omega and 25 on Omega.

## Orbit-degree refinement

The remaining projective orbit sizes are 20,30,60. Consequently 120-12n is divisible by ten, so n is a multiple of five. Together with 0<=n<=10 this gives {0,5,10}. The values b=5,13,21 force s+t=2 and therefore n=10. No degree remains for zeros outside Omega, so all paired blocks and the trivial block are invertible there. The claimed global conclusion in these cases follows.

The proof resolves a genuine stabilizer-linearization issue and gives new necessary exceptional-rank restrictions. It does not decide the actual generic branch, assert any selected source-instance result, or imply higher-order lifting or algebraicity. No source coefficients, selected parameter, numerical ranks, or large computation were used in this review.
