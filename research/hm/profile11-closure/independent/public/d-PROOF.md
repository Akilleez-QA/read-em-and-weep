# A three-pair necessary frontier for the D-source in maximal profile (1,1)

## 1. Statement and geometric hypotheses

Work over C on the original fixed physical binary-icosahedral parameter line, with G=SL2(F5), its defining doublet W, and the original determinant convention. All bundles, maps and Gauss kernels below are the actual ones in the original saturated inclusion

    0 -> E -> H O -> Q -> 0, dim H=30,
    S=Q*, K=E^-, L=S^-, A=E/K, B=S/L.

Assume generic Gauss rank three, maximal rank-three profile (1,1), and the D-source

    E=D O(-2)+(W'+T)O(-3)+V O(-4)+O(-8),
    D=Sym4 W, T=Sym5 W.

Thus ranks E,S,K,L,A,B are 17,13,14,10,3,3, respectively; deg E=deg S=-54; S is negative, with top degree at most -1; and the derivative of the endpoint L has rank at most two. The distinct irreducibles W',V,P have dimensions 2,3,4. No profile-(2,1) bound top S<=-2 is assumed.

Under the imported original geometric necessity theorem for the 159 pairs, the actual ordered pair (A,B), including its determinant defect t=-6-deg A-deg B, must be one of the following:

| Original zero-based index | A | B | t |
|---|---|---|---:|
|32|O(-8)+O(2)+O(4)|O(-18)+O(-4)+O(6)|12|
|50|O(-8)+O(2)+O(4)|O(-6)+O(-4)+O(6)|0|
|52|W O(3)+O(-8)|W O(-5)+O(6)|0|

This is a necessary two-A-shape, three-ordered-pair frontier for this source and profile only. It does not assert that any pair occurs, that these pairs are free of every other obstruction, or that the other source types are excluded. It does not prove full profile closure, global rank-three exclusion, smoothing, full-adjoint invertibility, or the original theorem repair.

## 2. Pinned necessity inputs, rather than ledger inference

INPUTS.json pins nine complete public files by immutable commit, byte count, SHA256 and Git blob SHA1. All were read at their immutable revisions. Their full bytes are retained in this packet. The principal geometric dependency is the complete original ONE-ONE-ENDPOINT-DEGREE-WINDOWS-AND-159-NECESSARY-PAIRS.md at db51525015bb7c5e825833d550d08dedf6f6ea96, retained as inputs/profile11-proof.md, together with its original JSON. Its Section 5 proves necessity of the finite quotient overlist using the actual presentations, negative transpose, strict-top, equivariant determinant constraints and source cohomology. We import that written theorem, including its stated prerequisites; a JSON count does not establish geometric exhaustiveness.

PR1123 at 504b7eb800407dfc7e6340c98c72cdd553939f54 supplies the four actual source alternatives and the D-source tuple (1,1,1,0,0,1,0,0). Conditioning on D does not claim that D is the sole actual alternative. PR1140 at 7a2488bcd36d95f79b5198001111b1a31fe5c3ba proves the actual cubic coefficient injection used below. PR1138 at c69f97aaf00e116e3a8abebf19a8e02868c4f7c4 contains the general endpoint-capacity argument; Section 4 below re-proves exactly the part needed here, without its profile21-specific stronger slope or closure conclusion.

The remaining three geometric exclusions are PR1135 at 24e713fe352f4ff8f70cd2e86940afa70df99c5c, PR1142 at df2fd3d35dac577d7f1e1c4d51fe68b1fcc824ad, and PR1145 at 2e2da6c1226b7671c79e55b3c9f8bb14a0f8719b. Their precise scopes are matched in Section 5. No unpublished P/V/Z closure, later ledger coverage, or live-count assertion is imported.

## 3. Exact D-source compatibility and cubic visibility

For an equivariant split bundle F=sum R O(e), compute

    H0(F(u))=sum R tensor Sym^(e+u) W,
    H1(F(u))=sum R tensor Sym^(-e-u-2) W,

with negative symmetric degrees contributing zero. All irreducibles are self-dual in this marking, so these expressions already incorporate Serre duality. Exactness of E->A and the injection B->E*(-2) imply respectively

    H1(A(u)) <= H1(E(u)),
    H0(B(u)) <= H1(E(-u)).

These are representation multiplicity inequalities. For every one of the 159 frozen records, the verifier recomputes both inequalities for each integer u=-10,...,10. It does not use the stored compatible_E_types field to decide compatibility. After computing it, it checks agreement with that field as an integrity control. Exactly 102 records pass and 57 fail. Every failure has explicit twist and negative irreducible multiplicity evidence in RESULT.json. The finite twist range is necessary only, not a characterization of all possible cohomology constraints.

PR1140 proves that W'+2T injects into H0(A(3)) for every actual source in PR1123. These are coefficient/global sections, not a rank14 fiber subbundle of rank3 A. The exact character H0(A(3))-(W'+2T) must therefore be genuine. Applied after D compatibility, this excludes 32 records, leaving 70. Every negative witness is retained, without replacing virtual character subtraction by a positive-only Counter operation.

## 4. Rank-ten dual endpoint capacity, valid in profile11

Set F_0=S, F_1=L and F_(j+1)=F_j^- in the original constant ambient. Let G_0=B and G_j=F_j/F_(j+1), q_j=rank G_j for j>=1. Actual differentiation stays in F_(j-1) and has kernel F_(j+1) after projection modulo F_j. It induces sheaf injections

    G_j -> G_(j-1)(-2) -> B(-2j).

No saturation of these image injections is asserted. Their ranks are nonincreasing, and q_1<=2 by the maximal-profile endpoint hypothesis. Every F_j is saturated and negative. A nonzero horizontal saturated subbundle of a trivial bundle on P1 in characteristic zero is constant of degree zero, so no nonzero F_j is horizontal. Its derivative has positive rank, and the chain terminates in zero. Hence sum q_j=10 and deg L=sum deg G_j.

Write lambda_1>=lambda_2>=lambda_3 for the ordinary splitting degrees of B with multiplicities. Taking the determinant of G_j->B(-2j) gives

    deg G_j <= sum_(i=1)^q_j lambda_i-2j q_j.

For h_i=#{j:q_j>=i}, nonincreasing ranks imply h_1>=h_2>=0, h_1+h_2=10, and

    -54-deg B = deg L
       <= h_1 lambda_1-h_1(h_1+1)
          +h_2 lambda_2-h_2(h_2+1).

The six possibilities are h_1=5,...,10 and h_2=10-h_1. Thus deg L cannot exceed the maximum of these six explicit integers. This uses only negativity of S, not top S<=-2, no endpoint rank-three assumption, and no horizontal Birkhoff projection.

The verifier expands B blocks into ordinary degrees, computes all six capacities and all maximizers, and compares with -54-deg B. Of the 70 records remaining after cubic visibility, 62 violate the bound strictly. The eight which do not are original 32,50,52,94,95,100,106,127. This is exact filtering of the frozen list, not re-enumeration of candidate bundles or evaluation of actual instances.

## 5. Match the remaining proved shape exclusions

PR1135 excludes A=O(-8)+O(4)+O(6) and A=O(-8)+W O(5) for the actual D-source without any derivative-rank or defect assumption. It therefore removes the surviving records 94 and95. Its proof retains the V(-4) rows and uses actual saturated graph cancellation, not a horizontal splitting. No stronger scope than its statement is needed here.

PR1142 excludes A=O(-8)+O(4)+O(8) and A=O(-8)+O(4)+O(10) for the actual D-source, again without a condition on the next derivative rank or determinant defect. It removes surviving records 100 and106. The proof's vanishing of Hom_G(O(2),A) forces cubic-kernel vanishing and a genuine fourth-twist envelope; it is not applied to the O(2) residual shapes.

PR1145 excludes A=O(-8)+O(2)+O(16) specifically in maximal profile(1,1). Its original 119 positive-defect record already fails capacity; its original 127 zero-defect record is removed here by that full theorem. Both its height7 and height8 alternatives are covered by its actual constant-splitting/apolar proof, and it uses only top S<=-1. We do not infer this exclusion solely from an equality capacity calculation.

Accordingly the D-compatible set has the following disjoint sequential partition:

    102 =32 cubic +62 capacity +2 PR1135 +2 PR1142 +1 PR1145 +3 remaining.

The57 D-incompatible records account for the rest of the original159. These category counts are not additive counts of newly live exclusions; earlier tests overlap and the order fixes a disjoint certificate. RESULT.json gives every record's full A/B/defect, signed failures, capacities, shape identification and assigned partition. It leaves exactly32,50,52, proving Section 1 conditional on the imported original necessity theorem.

For transparency, the residual capacities at h_1=5,...,10 are:

    32: (-50,-42,-38,-38,-42,-50), deg L=-38;
    50: (-50,-42,-38,-38,-42,-50), deg L=-50;
    52: (-55,-46,-41,-40,-43,-50), deg L=-50.

Record 32 is an equality case, not excluded by capacity: its possible height pairs are (7,3),(8,2). No additional geometry of any of these residual records is asserted here.

## 6. Verification boundary

Run the standard-library verifier as described in REPRODUCE.md. It checks all input bytes/hashes/blobs; source rank, degree and Euler character; universal character dimensions; every frozen row's ranks/degrees/defect; all 42 source cohomology inequalities per row; the cubic multiplicities; all six rank-ten capacities; the disjoint partition; and the exact three residual identities. Normal and optimized Python outputs agree byte-for-byte. Assertions are not used for required checks.

The new artifact is the source-conditioned exhaustive reduction to three necessary ordered pairs, with a mathematical transfer argument and a reproducible witness for each discarded record. It is not a new proof of the imported geometry and not proof-assistant verification. No actual coefficient, source instance, parameter, point, matrix, tensor, jet, rank experiment, historical enumeration, stopped model spike or one-shot computation is run.
