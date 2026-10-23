# V and Z sources cannot occur in maximal Gauss profile (1,1)

## 1. The source-conditioned conclusion

Over C, retain the actual saturated inclusion E in H tensor O on the original negative parameter line P(W*), with dim H=30, rank E=17, degree E=-54. Put S=Q*, rank S=13 and degree S=-54. Assume the second fundamental form has rank three and its **maximal** rank-three plateau has profile (k,l)=(1,1). Let

    K=E^-, A=E/K, L=S^-, B=S/L.

Then A and B have rank three, K has rank fourteen, and L has rank ten. Both endpoint derivatives have rank at most two. We prove that neither of the following two actual source splittings is possible:

    V: V O(-2)+(W'+T)O(-3)+2V O(-4),
    Z: (W'+2T)O(-3)+V O(-4).

Here W is the physical standard doublet, T=Sym^5 W, V the nonstandard irreducible three-space, P the irreducible four-space, and D=Sym^4 W. In character files the key `A` means Sym^2 W, not the quotient bundle A. All irreducibles are self-dual.

The conclusion uses the original profile-(1,1) necessity theorem and its frozen 159-record output, not a new geometric exhaustiveness claim. It excludes these two sources throughout that specified profile, including positive determinant defect. It does not exclude source D or P, other profiles, every rank-three configuration, or repair the original theorem. Separate source closures are not imported here.

## 2. Complete pinned inputs and actual-source transfer

INPUTS.json retains eight complete immutable public originals, with repository paths, commits, Git blob hashes, SHA256 hashes and byte lengths. They are:

1. The original profile-(1,1) necessity proof and frozen JSON, at db51525015bb7c5e825833d550d08dedf6f6ea96. Section 5 of that proof says every actual profile-(1,1) pair is on this overlist and records compatible original source tuples.
2. PR1123 at 504b7eb800407dfc7e6340c98c72cdd553939f54: the four actual source types and tuple interpretation.
3. PR1140 at 7a2488bcd36d95f79b5198001111b1a31fe5c3ba: actual cubic visibility and cubic-kernel alternatives, without a source-ledger assumption.
4. ACTUAL, strict-top, and positive double-hyperplane Gauss originals at db51525015bb7c5e825833d550d08dedf6f6ea96: the actual thirty-dimensional constant ambient inclusion, saturated Gauss kernels, negativity, and endpoint interpretation.
5. The exact public characters.py at 4b97c71dace666dd5bf39e0128abbe7b01a2f056, used only for universal representation arithmetic.

The original eight-coordinate source tuple is (a,b,c,d,e,f,g,h), not the quotient degrees a,b used elsewhere. PR1123 Section 5 gives V=(1,1,2,0,0,0,0,0) and Z=(1,2,1,0,0,0,0,0). For each source and each of the 159 frozen records, the verifier independently recomputes every coefficientwise inequality

    H1(A(u)) <= H1(E(u)),
    H0(B(u)) <= H1(E(-u)),             -10 <= u <= 10.

The first follows from the actual quotient E->A. The second follows from B->E*(-2) and Serre duality. All representations are self-dual. Compatibility means these finite necessary tests pass; it does not assert their sufficiency or realization. Recomputed truth values agree with tuple membership in every stored compatible_E_types field, including all 125 incompatible records per source. RESULT.json gives a specific failed inequality for each incompatible record.

Both sources have exactly the same 34 compatible zero-based original indices:

    42,43,53,62,63,64,65,66,67,73,74,76,
    86,87,88,89,96,102,103,110,111,116,
    130,132,134,141,142,143,144,145,148,149,150,151.

This step reads the frozen list and checks source compatibility. It does not rerun the historical candidate-generation algorithm.

## 3. Two actual character obstructions remove 23 records

PR1140 proves, for either source,

    H0(K(3))=0,
    W'+2T embeds in H0(A(3)).

Thus H0(A(3))-(W'+2T) must be genuine. This eliminates exactly these 16 of the 34 compatible records:

    42,43,53,62,63,64,65,66,67,73,74,76,102,103,110,111.

These are exclusions by an actual necessary injection, not a generic fiber-rank inference from section dimensions.

The first vanishing says every degree of K is at most -4. K remains saturated in the same constant ambient space. Strict-top applied to K gives H0(K^-(4))=0. Its actual derivative lands in A(-2), so

    H0(K(4)) embeds in H0(A(2)).

Exact Euler additivity for 0->K->E->A->0 therefore makes

    C(A)=H0(A(2))+chi_G(A(4))-chi_G(E(4))

 a genuine representation: it equals the character of the cokernel of this section injection plus H1(K(4)). Direct calculation for either source gives

    chi_G(E(4))=3V+3P+2D.

Crucially this is an Euler characteristic, not H0(E(4)); no H1 term is silently dropped. This tightened quartic envelope excludes seven further records:

    86,87,88,89,96,116,134.

For each, the V coefficient of C(A) is -1. In V and Z sources the cubic vanishing is unconditional, so no forced-endpoint lemma or P-source alternative is needed. The verifier records full signed cubic and quartic characters for all 34 compatible records. Its counter subtraction retains negative multiplicities.

## 4. A complete dual-endpoint capacity bound

The remaining eleven records are eliminated geometrically at the dual endpoint. Write the ordinary degrees of B as lambda1>=lambda2>=lambda3, with repeated dimensions included.

Set F0=S, F1=L, and F_(j+1)=F_j^- for j>=1. All F_j are saturated in the same constant dual ambient bundle: each derivative kernel is saturated in its predecessor, and saturation composes. Since S has all degrees at most -1, every nonzero F_j is negative. A nonzero F_j cannot be horizontal. Otherwise its classifying map would have zero differential, be constant in characteristic zero, and saturation would make F_j constant of degree zero. Consequently every nonzero backward step strictly reduces rank, and the backward flag terminates at zero.

Put G0=B and G_j=F_j/F_(j+1) for j>=1. By the actual Gauss-kernel definition, differentiation of F_j lands in F_(j-1) modulo F_j and induces a sheaf injection

    G_j -> G_(j-1)(-2).

Its kernel is exactly F_(j+1) before passing to the quotient. This statement uses coherent locally free quotients, not saturation of the derivative image. Iteration gives G_j->B(-2j). If q_j=rank G_j, then

    2 >= q1 >= q2 >= ... >= 1,
    sum q_j=rank L=10.

The first bound is the maximal-profile endpoint condition. The injections give the remaining monotonicity. The terminating exact filtration gives deg L=sum deg G_j.

Taking determinants of G_j->B(-2j), the largest degree in wedge^(q_j) B(-2j) is the sum of its q_j largest ordinary degrees. The determinant injection is nonzero even if its image is unsaturated. Hence

    deg G_j <= sum_(i=1)^(q_j) lambda_i -2j q_j.

Let h1 count the q_j>=1 and h2 count the q_j>=2. Nonincreasing ranks mean h1>=h2>=0 and h1+h2=10. Summing yields

    deg L <= h1 lambda1 -h1(h1+1)
             +h2 lambda2 -h2(h2+1).                 (*)

There are precisely six possible pairs (h1,h2)=(5,5),(6,4),...,(10,0). The code verifies completeness independently by generating all nonincreasing positive rank sequences of sum ten and first term at most two, not by assuming a particular endpoint rank or flag length.

In particular, if lambda1<=-1 then (*) is at most -70: sum j q_j>=30 and sum q_j=10. This remains true for a rank-one endpoint. No profile-(2,1) stronger top-slope hypothesis is used, and determinant defect is not assumed zero in the proof.

## 5. The eleven remaining contradictions

All remaining B have top degree at most -1. Their exact data and capacities (the maximum of (*) over its six choices) are:

| Original index | Ordinary B degrees | deg L=-54-deg B | Exact capacity |
|---:|---|---:|---:|
|130|(-4,-6,-6)|-38|-110|
|132|(-5,-5,-6)|-38|-110|
|141|(-4,-6,-8)|-36|-110|
|142|(-5,-5,-8)|-36|-110|
|143|(-4,-7,-7)|-36|-114|
|144|(-1,-1,-16)|-36|-70|
|145|(-6,-6,-6)|-36|-120|
|148|(-6,-6,-8)|-34|-120|
|149|(-6,-7,-7)|-34|-125|
|150|(-1,-1,-18)|-34|-70|
|151|(-6,-7,-7)|-34|-125|

Each required degree is strictly greater than even the uniform upper bound -70; the smallest exact contradiction gap is 34. All six height capacities and ordered equivariant A/B blocks are retained for every row in RESULT.json. Ordinary degrees here come from the actual stored B in the necessity overlist, not an unsupported recovery of B from A.

Thus for EACH source there is a disjoint sequential covering

    34 compatible records = 16 cubic + 7 quartic + 11 capacity,

with no surviving record. The first failed filter determines each row's assignment; overlaps are not double-counted. Every actual pair would have to be compatible and pass all three necessary conditions. This contradiction proves the source-conditioned theorem in Section 1.

## 6. Reproduction and limitations

Run `python3 verify.py > /tmp/vz-result.json` and compare with RESULT.json. Run again using `python3 -O verify.py`; output is identical because checks use explicit exceptions rather than assert. The checked artifact has 1,135 explicit controls plus 81 character-module controls. Inputs are byte/hash checked on each run. Exact representation arithmetic, Euler characteristics, all 21 twists, stored compatibility, disjoint index partitions, rank/height completeness and capacities are reproducible with the Python standard library.

The geometry in Sections 2-4 is a proof using the pinned mathematical inputs, not proof-assistant verification. The finite program is not a substitute for the original necessity theorem or actual geometric transfer. No selected HM/source coefficient, parameter, point, jet, tensor, actual matrix, instance rank, experiment or model spike is evaluated. The old 159 enumeration is neither regenerated nor modified. No global completion claim follows.
