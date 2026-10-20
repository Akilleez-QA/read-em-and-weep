# Independent mathematical review

Reviewed artifact: PROOF.md, SHA256

    698c6e50bcf72227c42eb33b016878ab449eef1aaceca0cd8636656169bde0fc

Verdict: the new conclusions follow from the explicitly pinned mathematical dependencies. No correction to the frozen proof is required. This is a mathematical text review, not formal proof-assistant verification.

## Representation and generation checks

I checked the character identity HM Lemma 3.3(vi) and the quotient/cohomology formulas (4.2), (4.4), and (4.6) against the primary paper's extracted text, and checked the normalized identifications in PR449 and PR452. Dualizing the degree-three polynomial representation gives S_3=A tensor (J direct sum W'), whereas M_0=A* and M_3=W'. Thus Hom(M_0,M_3)=A tensor W' has the correct dual and central character. The prime on W' is retained. The H-isotypic criterion makes the two source summands irreducible and nonisomorphic under N, so their different multiplicity characters suffice for Schur's lemma; mere H-equivariance would not suffice.

The cohomology quotient presentation is compatible with multiplication and gives generation in degree zero. Hence cubic multiplication is nonzero. Its unique permissible irreducible component is therefore a nonzero scalar isomorphism, proving surjectivity and the exact twenty-five-dimensional kernel. No selected polynomial was inserted into the universal map.

## Incidence geometry checks

Using PR449's classification, a nonzero bad quadratic has a unique image line l and is a tensor a tensor n_l. Its multiplication map cannot have rank zero. Adding the cubic fails to cover W' exactly when the cubic map has image in l. The preimage of A tensor l under the cubic projection has dimension 25+5=30, giving the projective linear fiber P^29.

Over P(A*) times P(W'), the image line is the tautological O(0,-1), not O(0,1). The kernel in equation (5) is a vector subbundle because the map onto A tensor (W'/l) is fiberwise surjective. The N-isotypic splitting gives the asserted direct sum O^25 direct sum O(0,-1)^5. The quadratic embedding uses the square of the tautological line and is O(1,2); that square does not enter the cubic image containment condition.

The projective bundle is a closed immersion into B times P(S_3), and B is closed in P(S_2). Its image is smooth and therefore reduced; equality of its closed points with the failure set over C identifies it with the reduced closed failure locus. Dimension 5+29=34 and codimension 48-34=14 are correct. The proof deliberately does not identify a potentially nonreduced determinantal scheme with this reduced image.

For the opposite projection, the rank-at-most-one tensor cone has dimension six, its cubic preimage has dimension thirty-one, and its projectivization has dimension thirty. The rank-zero locus P^24 is properly contained, so the rank-one stratum has dimension thirty. The fibers over rank-two, rank-one, and rank-zero cubics are respectively empty, P^4, and B, as claimed. Thus the dimension calculations agree from both projections.

## Full obstruction check

I checked PR456's proof that the natural cup map V tensor M_3 -> H^1(End_0(F)(5)) is injective, rather than merely an abstract embedding. The cup maps in the lower two degrees commute with multiplication by u and v. Their resulting image inside L_0 intersect U contains the image of V tensor (uM_1+vM_0), of dimension exactly 4r. The full quotient exact sequence then gives the upper bound 8-4r for its primary contribution. It does not give equality because other source classes may also meet L_0.

Since r is one or two for every nonzero quadratic, the uniform bound is four. Combining only with PR458's stated coprime-pair residual estimate gives dim Q_5<=10+k, and <=6+k under primary coverage. The hypotheses on coprimality and common contained lines are retained. Neither vanishing of the original Q_5 nor necessity of primary coverage is asserted.

## Scope

The review verifies the new deductions using the pinned results; it does not constitute an independent reproof of every geometric dependency. No selected HM/source-instance evaluation, numerical multiplication matrix or rank, parameter search, generator/checker, or large computation was performed. Actual-source membership, higher-order lifting and algebraicity remain outside these conclusions.
