# Direct endpoint capacity closes the original maximal profile (1,1)

## 1. The exact conditional theorem and its scope

Work over C on the original physical binary-icosahedral parameter line T=P(W*) with the fixed determinant identification and G=SL2(F5) marking. Use the ACTUAL saturated plane-section inclusion

    0 -> E -> H O -> Q -> 0,  dim H=30,
    S=Q* subset H* O,  K=E^-, L=S^-, A=E/K, B=S/L.

The minus operation is the kernel of the actual second fundamental form for the constant connection. Suppose its generic rank is three and its maximal rank-three plateau has profile (1,1). Then rank E=17, rank S=13, deg E=deg S=-54, rank K=14 and rank L=10. The two endpoint derivatives, those of K and L, each have rank at most two. All E degrees are at most -2; all S degrees are at most -1. No stronger bound on S is used.

Under the immutable actual-input and original profile-specific necessity theorems listed below, this configuration is impossible. This closes the maximal profile (1,1) branch directly from its original necessary overlist, without importing a later source-pair ledger, a source-transfer assertion, or global profile exhaustiveness. The geometric content is a simultaneous two-endpoint capacity obstruction and the consequent exact reduction to six already controlled shapes. The original 159 records are historical necessary possibilities, not realized sources or a current frontier.

This does NOT prove that every hypothetical generic-rank-three inclusion has one of profiles (1,1), (1,2), (2,1). The remaining profile-exhaustiveness dependency is separate. In particular this note alone is not COV, a global rank-three exclusion, a rank-four theorem, maximal rank, full-adjoint invertibility, smoothing, algebraicity, or repair of the original theorem.

Fourteen complete immutable public inputs are retained under inputs/ and authenticated by full commit URL, byte count, SHA256 and Git blob ID in INPUTS.json. They were freshly read, not inferred from a local ledger:

- ACTUAL, ambient-Gauss and strict-top originals at db51525015bb7c5e825833d550d08dedf6f6ea96 establish the precise inclusion, profiles, ranks, degrees, saturation and negative bounds above.
- The original profile11 theorem at that commit, ONE-ONE-ENDPOINT-DEGREE-WINDOWS-AND-159-NECESSARY-PAIRS.md, and its exact ordered JSON supply the necessary overlist. Its written theorem is an imported geometric necessity result, not a conclusion of the JSON or this checker. The original verifier is retained for a read-only audit of its construction and is NOT executed here. Its explicitly imported primal bound a>=-4 is retained at PR674, 2516a879b4b1469da1a29eaefafcfddf4e171a0d.
- PR1123 at 504b7eb800407dfc7e6340c98c72cdd553939f54 supplies the four actual necessary E types, independent of rank-three source ledgers.
- PR1140 at 7a2488bcd36d95f79b5198001111b1a31fe5c3ba supplies actual cubic visibility W'+2T6 in H0(A(3)).
- PR1135 at 24e713fe352f4ff8f70cd2e86940afa70df99c5c excludes A=O(-8)+O(4)+O(6) and A=O(-8)+W O(5), in every profile.
- PR1142 at df2fd3d35dac577d7f1e1c4d51fe68b1fcc824ad excludes A=O(-8)+O(4)+O(8) and A=O(-8)+O(4)+O(10), in every profile.
- PR1145 at 2e2da6c1226b7671c79e55b3c9f8bb14a0f8719b excludes A=O(-8)+O(2)+O(16) in profile (1,1), retaining both original defects.
- PR1134 at 7cb2e260b2bcbac15df89612b6a2096263a9c89c supplies the iterated-section argument. Section 5 below rederives the only use, so no profile21 hypothesis is transferred.
- The physical character reference at db515250 fixes all nine irreducibles. Here A_std=Sym2 W, S4=Sym3 W, D=Sym4 W, T6=Sym5 W; V is the other three-space, P the positive four-space and W' the other negative doublet. The symbol A always denotes the Gauss quotient, never A_std.

## 2. A capacity inequality at both genuine rank-drop endpoints

We give the argument independently, retaining both orientations. Let F0 be either E or S, let F1=F0^- be its actual endpoint K or L, and let F_(j+1)=F_j^- thereafter. Each is saturated in the same original constant ambient bundle: a derivative kernel has torsion-free quotient in its source, hence locally free quotient on the smooth curve; successive locally free quotients preserve saturation in the ambient. Put C=F0/F1 and G_j=F_j/F_(j+1), q_j=rank G_j for j>=1. Differentiation gives actual sheaf injections

    G_j -> G_(j-1)(-2) -> ... -> C(-2j).

Indeed differentiation of F_j stays in F_(j-1), and the kernel of its projection modulo F_j is precisely F_(j+1). These are coherent-image injections, not assertions of saturated image in C(-2j). Thus q_(j+1)<=q_j, and q1<=2 because F1 is an endpoint of the maximal rank-three plateau.

Every nonzero F_j is negative, as a subbundle of E or S. If its derivative vanished it would be a saturated horizontal subbundle of a constant bundle, hence constant in characteristic zero and degree zero, impossible. Thus each nonzero stage has q_j>0 and rank strictly decreases; the chain ends at zero. If n=rank F1, this proves

    sum_(j>=1) q_j=n,   deg F1=sum_(j>=1) deg G_j.

Write lambda1>=lambda2>=lambda3 for the ORDINARY degrees of C, with representation dimensions expanded into repeated ordinary entries. Taking the top nonzero exterior power of G_j->C(-2j) gives

    deg G_j <= lambda1+...+lambda_(q_j)-2j q_j.

Set h_i=#{j>=1:q_j>=i}. Since q_j is positive, nonincreasing and at most two, h1>=h2>=0 and h1+h2=n. Summing the determinant inequalities gives

    deg F1 <= h1 lambda1-h1(h1+1)
              +h2 lambda2-h2(h2+1).

Define the universal integer capacity

    Cap_n(C)=max_{ceil(n/2)<=h<=n}
      [h lambda1-h(h+1)+(n-h)lambda2-(n-h)(n-h+1)].

Consequently the SAME actual pair A,B satisfies BOTH

    -54-a <= Cap_14(A),      -54-b <= Cap_10(B),       (1)

where a=deg A and b=deg B. Only eight primal heights and six dual heights occur. Rank-one endpoints are included by h=n. Ties of degrees and of optimizing heights do not affect this inequality; no equality-image theorem or strict-top equality filter is used. In particular there is no use of the stronger top(S)<=-2 that belongs to other profiles.

## 3. The other direct necessary conditions

The four actual E types from PR1123 are

    E_D=D O(-2)+(W'+T6)O(-3)+V O(-4)+O(-8),
    E_P=P O(-2)+(W'+T6)O(-3)+V O(-4)+W' O(-5),
    E_V=V O(-2)+(W'+T6)O(-3)+2V O(-4),
    E_Z=(W'+2T6)O(-3)+V O(-4).

No type has an ordinary degree below -8. Hence E(8) is globally generated, and its actual quotient A(8) is globally generated. Every ordinary degree of A is therefore at least -8. Moreover an O(-8) quotient can only be supplied by the single O(-8) of E_D. No actual source can surject onto 2O(-8); a proposed map from its only possible rank-one lower block has rank at most one. This is an actual simultaneous quotient-rank obstruction, not an independent nonzero-Hom test for each target copy. In particular every candidate containing one O(-8) forces E=E_D.

PR1140 proves, for each of those same actual source types and independently of derivative rank,

    W'+2T6 embeds in H0(A(3)).                         (2)

Its proof uses the actual top-row kernel dimension, followed by saturated graph cancellation to force independence of the two T6 channels. It is an injection of coefficient spaces, not of rank14 bundles into A. Here (2) is used exactly in that form. The fixed calculation is

    H0(A(3))=sum_(e,R in A) R tensor Sym^(e+3) W,

with negative symmetric indices contributing zero and all multiplicities retained.

For the finite reduction we use ONLY the source degree/multiplicity obstruction, (2), and (1). We do not choose independent E witnesses for primal and dual tests, do not use compatible_E_types from the historical JSON, and do not use any later ledger. All four sources obey the two uniform source obstructions and (2); the endpoint inequalities concern the one actual pair.

## 4. Exhaust the original ordered necessary records

The imported original theorem states -4<=a<=24, -30<=b<=-2 and t=-6-a-b in {0,12,20,24}, and gives exactly 159 necessary ordered records. Its construction uses the actual rank-three quotient classification, endpoint cohomology, negative-transpose injection A->B*(-2), and actual-source necessary cohomology. These are necessary conditions, not occurrence claims. The original written derivation and read-only verifier audit are retained; the original enumeration is not rerun.

Apply the following disjoint decision order to those exact records:

1. Remove 56 records having an ordinary A degree below -8 or at least two ordinary A degrees equal to -8.
2. Among those left, remove 32 failing (2).
3. Among those left, remove 62 violating the dual inequality in (1).
4. Among those left, remove the three original records 32,50,52 violating the primal inequality in (1).

The full original A/B splittings, a,b,t, cubic character, both lists of height values, all capacity optimizers, and first exclusion reason for every one of the 159 records appear in RESULT.json. The sum 56+32+62+3 is an accounting check, not the coverage proof. The exact remaining ORIGINAL indices and splittings are:

    94: A=O(-8)+O(4)+O(6);  B=O(6)+O(-6)+O(-8).
    95: A=O(-8)+W O(5);     B=O(6)+W O(-7).
    100: A=O(-8)+O(4)+O(8); B=O(6)+O(-6)+O(-10).
    106: A=O(-8)+O(4)+O(10);B=O(6)+O(-6)+O(-12).
    109: A=W' O(-5)+O(16);  B=W' O(3)+O(-18).
    127: A=O(-8)+O(2)+O(16);B=O(6)+O(-4)+O(-18).

All six have their ORIGINAL determinant defect t=0. Their (a,b) values are respectively (2,-8),(2,-8),(4,-10),(6,-12),(6,-12),(10,-16). Their primal capacities are -42,-42,-26,-10,20,38; their dual capacities are -42,-44,-42,-42,-30,-38. No determinant torsion of a different Gauss map has been set to zero.

The first, second, third, fourth and sixth shapes force the SAME E_D by their O(-8) quotient. They are exactly the actual shape theorems in PR1135 (94,95), PR1142 (100,106), and PR1145 (127). Those complete immutable proofs are retained. Their saturation, negative-tail cohomology and endpoint hypotheses match the present actual inclusion; none depends on the later same-source ledger. In particular PR1145's profile11 height7 argument supplies the genuine constant splitting and partial-coefficient apolar obstruction, rather than importing the profile21 bound top(S)<=-2.

It remains to justify index109 without borrowing any other profile hypothesis.

## 5. The remaining W'(-5)+O(16) shape has an invariant deficit

If A=W' O(-5)+O(16), the quotient projection onto W' O(-5) forces E=E_P. E_V and E_Z have all degrees greater than -5 and hence have zero Hom to that summand. In E_D only O(-8) could contribute by degree, but

    Hom_G(O(-8),W' O(-5))=(W' tensor Sym3 W)^G=0,

because Sym3 W=S4 is inequivalent to W'. Therefore E_P is the actual source, not merely a compatible formal witness.

Set F0=E and F_(i+1)=F_i^- for its actual successive kernels, without assuming later rank3. Strict-top gives every degree of F_i at most -2-i. Put J_i=F_i/F_(i+1), so J0=A. The actual kernel argument of Section2 gives J_i->A(-2i). Since H0(F9(10))=0, telescoping the nine exact quotient sequences yields the representation inequality

    H0(E(10)) <= sum_(i=0)^8 H0(A(10-2i)).           (3)

Every group representation is semisimple over C; hence coefficientwise inequalities on H0 may be added. If a kernel reaches zero earlier, the extra terms on the right only weaken the necessary bound.

For E=E_P, the trivial multiplicity in H0(E(10)) is FOUR: exactly one comes from each of P tensor Sym8 W, W' tensor Sym7 W, T6 tensor Sym7 W, and V tensor Sym6 W. The remaining W' tensor Sym5 W contributes none. This uses the physical irreducible identities Sym6 W=V+P, Sym7 W=W'+T6, Sym8 W=P+D, and Sym5 W=T6.

For the W'(-5) part on the right of (3), the only nonnegative symmetric indices are 5,3,1. None contains W', so it contributes no invariant. For the O(16) part they are 26,24,22,20,18,16,14,12,10. The trivial multiplicities in that order are 0,1,0,1,0,0,0,1,0, respectively. Thus the right side has exactly THREE invariants, contradicting (3). This excludes109 in any profile where this actual quotient arose. It uses no actual coefficients, chosen parameters, jets, tensors, matrices or source-instance ranks.

## 6. Conclusion and verification boundary

Every original necessary profile11 record now has a direct obstruction. Thus, relative to the pinned actual-input and original necessity theorems, maximal rank-three profile (1,1) is impossible. The advance is resolution of this missing profile-specific coverage dependency by the two simultaneous actual endpoint capacities and six exact shape arguments, not a new later ledger count or claim that a necessary formal type occurs.

The bounded verifier checks all immutable bytes and all 159 original ordered records, but does not rerun their historical enumeration. It uses only fixed representation arithmetic through degree31 and the fourteen universal endpoint height values per record. Its explicit checks remain active under python -O. A second independent calculation must reconstruct the full row certificates from class characters without importing the production character recurrence or trusting RESULT.json; two independent whole-proof reviews are required before any broad profile11 closure is reported as reviewed.

The original other-profile exhaustion remains open here, even after separately known profile12 and profile21 exclusions. No global conclusion is obtained by treating their three labels as exhaustive. All public writes, merges and upstream changes are outside this packet.
