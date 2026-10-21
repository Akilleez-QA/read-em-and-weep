# Independent review of the determinantal Betti family

The structural derivation in PROOF.md passes this independent mathematical review, conditional on its pinned inputs. The refinement to k in {15,25,35,45} additionally uses the proof of b=0 in PR502, commit f8c9b1fb8b03a5721e4eca97cac4137f7ba955d0; PR501 alone does not suffice. Exact added dependency: https://github.com/Akilleez-QA/read-em-and-weep/blob/f8c9b1fb8b03a5721e4eca97cac4137f7ba955d0/research/hm/excess-contraction-invertibility/PROOF.md . This review does not independently reprove every earlier dependency and is not formal proof-assistant verification.

## Exterior contraction

The degree-four diagonal Koszul term of C is the kernel of exterior^4(T) tensor A -> exterior^3(T) tensor C_1: there is no incoming term because C has no negative degrees. Tensoring by W_0 and evaluating the W_0 factors gives the claimed square universal map. Under a volume identification and a possible common sign, its output-flipped form is h Alt-id. Since Alt h=3id, multiplication by (h Alt)/2-id gives the identity. Thus the composite is injective and the original Koszul map is injective. This proves beta_(4,4)(C)=0 without a multiplicity-one nonvanishing assumption.

## Long exact Tor sequence

For Z=C(-3) tensor W', the supports are obtained by shifting every internal C degree by three and doubling dimensions. With the general C parameters b,d, the degree-six segment is

0 -> Tor_3(Z)_6 -> Tor_3(Q)_6 -> Tor_3(R)_6 -> Tor_2(Z)_6 -> Tor_2(Q)_6 -> 0.

Its dimensions at the fixed end terms are 2d,45,100+2d. Thus the two Q entries are 2d+45-rho and 100+2d-rho, respectively. This confirms both the homological index and the sign of rho. Degree five gives 2b+(52-2b)=52 because Tor_1(Q)_5=0. In degree seven, Tor_4(Z)_7=0 by the contraction argument, while Tor_3(Z)_7 has dimension150 and Tor_3(R)_7 has dimension10. In degree eight the respective Tor_4 terms have dimensions90 and20. The only Tor_5 contributions are Tor_5(Z)_9 of dimension20 and Tor_5(R)_10 of dimension3. The displayed support lists exclude every other entry.

Consequently the claimed free modules of Q are correct. Their alternating Hilbert numerator is

1-35t^4+52t^5+55t^6-160t^7+110t^8-20t^9-3t^10,

independently of k, agreeing with the Hilbert function (1,5,15,35,35,3).

## Pure-C refinement and representation exclusion

When b=0, minimality eliminates all later diagonal C terms, in particular d=0. The degree-three Koszul presentation therefore gives Tor_2(C)_3 as the difference of exterior^2(T) tensor V tensor W_0 and exterior^3(T) tensor A. Expanding with the stated identities gives precisely T tensor(U' plus W_0 plus J_5), of dimension50.

The duality in PR492 sends Tor_2(N)_4 to the dual of Tor_3(R)_6: homological indices add to5 and internal degrees add to10. The determinant character is trivial under the pinned conventions. Since the quotient representations U,W',Qspin are self-dual and V*=T, PR500's v=0 gives Tor_3(R)_6=T tensor(U plus W' plus Qspin). No self-duality of R or of Q is being assumed.

The quotient tensor identity J_5 tensor W'=Qspin plus R_6 can also be checked directly from the public Horrocks--Mumford Appendix character rows: both sides have character (10,-10,0,1,-1,0,0,0,0) in the Appendix class order. Together with U' tensor W'=W' plus Qspin and W_0 tensor W'=T_4, this gives

Tor_2(Z)_6=T tensor(W' plus 2Qspin plus T_4 plus R_6).

Thus the target lacks T tensor U. The proof's shorter parity argument establishes the same exclusion without requiring the full J_5 product. Equivariance kills the15-dimensional U source constituent. Each other source constituent is irreducible and occurs once, so its kernel is either zero or the whole constituent, of dimension10 or20. This proves k in {15,25,35,45}, not a claim that all four cases are realized. Determining the two remaining nonvanishing questions is still open.

No selected actual HM/source-instance evaluation, numerical matrix or rank calculation, coefficient search, checker, or large computation was performed for this review. The conclusion concerns minimal graded free-module ranks and shifts; it makes no higher-order lifting or algebraicity claim.
