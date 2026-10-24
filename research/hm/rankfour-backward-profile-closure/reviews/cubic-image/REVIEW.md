# Independent review: backward dual-cubic image bound

## Verdict and scope

**PASS, conditional on the retained actual geometric inputs.** In the actual ordered maximal generic-rank-four plateau `(k,l)=(3,1)`, the derivative restricted to **every chosen equivariant copy of T6 in H0(Q*(3))** has nonzero image of rank at most three. If this image has rank one, it must be O(9), and the necessary actual source label is D.

The final theorem is stronger and more careful than a formulation referring to a canonical cubic subbundle: it assumes neither uniqueness of the T6 copy nor injectivity or saturation of its evaluation into Q*(3). The positive T6 coefficient of the actual Euler character supplies at least one copy. Each chosen copy is treated separately.

This is **not an exclusion of the (3,1) profile**. It does not decrease a coarse profile count, prove actual SF rank at least five, establish square-map surjectivity or full-adjoint invertibility, or repair the original theorem. Rank-17 E, rank-13 Q*, and dimension-30 H are never exchanged. In particular k=3 does not imply source Z. No actual coefficients, parameters, jets, matrices, instance ranks, local models, historical candidate enumeration, or external writes enter this review.

## 1. Sources read and actual premises retained

I read the five complete original source documents and the full author proof and verifier. The first four sources are pinned at `db51525015bb7c5e825833d550d08dedf6f6ea96`:

1. ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md: actual E and Q* presentations, physical marking, equivariant Birkhoff splitting, and rank-independent persistence. Its historical 28-type enumeration is not rerun.
2. POSITIVE-DOUBLE-HYPERPLANE-GAUSS-GATE.md: the actual saturated inclusion into the constant thirty-space and geometric second fundamental form, not a maximal-rank conclusion.
3. RANK-TWO-GAUSS-PLATEAU-NECESSARY-BOUND.md: actual ambient character, rank-independent regular derivative and saturation facts, and determinant parity. Its rank-two conclusion is not imported.
4. GAUSS-DETERMINANT-ORBIT-RAMIFICATION.md: only the invariant effective-divisor semigroup and derivative-isomorphism consequence of zero defect. Its special rank-one endpoint arguments are not imported.

The fifth source, four-sources.md, is the primary terminal slope theorem at `504b7eb800407dfc7e6340c98c72cdd553939f54`. Its actual primary inclusion W'+T6 into the canonical degree-minus-three coefficient module and its necessary four-source consequence are retained, with its explicit transitive primary-module hypotheses. Its proof uses both coefficient arrows of the same actual terminal pencil, functoriality for the canonical slope quotient, and a fixed determinant rotation. It does not assume a horizontal Birkhoff projection. The present argument imports its four-source theorem rather than rebuilding its historical source classification.

The independent verifier authenticates the complete original bytes by SHA-256 and Git blob SHA-1. This checks identity, not the truth of the underlying HM geometry or all transitive prerequisites.

The actual presentations are

    [E]=[M3 O(-1)]-[M4 O],  [Q*]=[M3 O(-1)]-[M2 O],
    M2=A+2V+3P+4D,
    M3=3W'+3S4+6T6,
    M4=2V+4P+3D,
    H=W M3-M2-M4=2A+2V+2P+2D.

The physical labels are A=Sym2 W, S4=Sym3 W, D=Sym4 W, T6=Sym5 W. V is the inequivalent even three-space. All irreducibles are self-dual; W,S4,T6,W' are center-odd. In particular

    chi E(3)=W'+2T6,
    chi Q*(3)=T6-2W-S4.

These are equivariant Euler characters, not assumptions that H1 vanishes.

## 2. Ordered geometry and nonzero restricted derivative

The actual saturated chain is

    F0 < F1 < F2 < F3=E < F4,
    ranks 5,9,13,17,21.

For interior indices, the derivative kernel is the preceding stage and the saturated forward transform is the next. The regular quotient maps are Li -> L(i+1)(-2), where Li=Fi/F(i-1) has rank four. Endpoint derivative ranks are not assumed one or equal.

The reversed annihilator chain is Di=F(4-i)^perp, so its central actual object is D1=Q*, not E. The usual nonconstant/full-span propagation applies. Persistence gives H0(Fi(d))=H0(Di(d))=0 for i+d<4, including endpoint i=0: the first derivative containment follows from the kernel construction at F1. The universal polynomial derivative identity reaches a section's constant coefficient span in at most its degree; saturation extends containments across exceptional parameters.

In particular H0(D0(3))=0. The derivative kernel of Q*=D1 is D0. For any inclusion T6 -> H0(Q*(3)), the composite

    T6 O -> Q*(3) -> E*(1)

is therefore injective on that T6 space of global sections. It is nonzero, even if the first evaluation map is not an injective bundle map. Its image rank is at most the full derivative rank four.

## 3. Positive defects are retained globally

Endpoint persistence gives a=deg F0<=-20 and b=deg F4=deg D0<=-36. Determinant degrees are even. With ci=deg Li, regular derivative determinants give

    c(i+1)=ci+8+delta_i,
    delta_i in <12,20,30>.

Direct elimination with deg F3=-54 yields

    a+3b=-168+delta1+2delta2+3delta3.

Writing a=-20-2u and b=-36-2v gives slack **40**:

    2u+6v+delta1+2delta2+3delta3=40,
    c1=(-78-a-2delta1-delta2)/3 in 2Z.

My independent endpoint-and-defect enumeration gives exactly the author's 31 numerical rows, including 24 rows with positive defects and twelve defect triples. For example

    a=-24, b=-36, (delta1,delta2,delta3)=(0,0,12),
    (c1,c2,c3,c4)=(-18,-10,-2,18)

satisfies the necessary degree ledger. Consequently a blanket zero-defect argument is invalid here. The proof never makes one. The ledger is only a necessary numerical overlist, not a realization theorem.

The author's second enumeration has proved finite bounds: a in [-60,-20], b in [-48,-36], c1 in [-46,-6], and c2 in [-38,2]. The upper bounds follow from c4=b+54<=18 and nonnegative differences; c1's lower bound follows from the central prefix and the slack bound, and c2>=c1+8. My enumeration independently scans endpoint bounds and the invariant semigroup, imposing the central-prefix divisibility.

## 4. Complete image domain and maps versus sections

Let J be the image sheaf of the restricted derivative. On a smooth curve J is locally free and a quotient of T6 O, so J is globally generated. It is not initially assumed saturated in E*(1). It is center-odd.

The four necessary source types D,P,V,Z imply maxdeg E*(1)<=9. Thus every irreducible block R O(e) of an image of rank at most four has

    0<=e<=9, dim R<=4, parity R=e+1 modulo 2.

Two distinct necessary tests are imposed:

- Source generation: T6 occurs in R Sym^e W.
- Target inclusion: for some actual source shape and target block S O(f), the multiplicity of R in S Sym^(f-e) W is positive, with this Hom space zero when f<e.

The second is a bundle-map condition, not merely the existence of sections of a target. The tests deliberately form an overlist; simultaneous realizability of every tested component is not asserted.

Exact independent class characters over Q(sqrt5) give the complete fourteen-block list:

    P O(1), V O(1), S4 O(2), W' O(2),
    P O(3), V O(3), W' O(4), P O(5), V O(5),
    S4 O(6), W' O(6), A O(7), W O(8), O(9).

There are exactly 24 unordered rank-four multisets. No empirical degree cutoff or historical list is used. The only rank-one block is O(9), whose nonzero target Hom is available only in source D. This proves the stated necessary rank-one corollary without claiming realization.

## 5. Saturation bound and the four full-rank shapes

Assume rank J=4. The negative-transpose derivative identity identifies the saturation

    Jbar=(E/F2)*(1).

This follows from the generic annihilator of the actual saturated kernel F2 and then equality of saturated sheaves. Set B=E/F2 and dbar=deg Jbar. Thus deg B=4-dbar and deg F2=dbar-58. Dualizing J -> Jbar gives a regular inclusion B -> J*(1); it does not presume J=Jbar.

The regular backward derivative maps give

    F2(3) -> B(1), kernel F1(3),
    F1(3) -> L2(1), kernel F0(3),
    L2(1) -> B(-1).

The last map is an injective sheaf map: it is regular and generically invertible between vector bundles of equal rank. Since H0(F0(3))=0, left exactness and the inclusion of B into J*(1) imply

    h0(F2(3)) <= h0(J*(2))+h0(J*).

Riemann--Roch for rank-thirteen F2 gives h0(F2(3))>=dbar-6. Therefore

    deg J <= dbar <= 6+h0(J*(2))+h0(J*).

The 24-shape domain reduces exactly to:

    J=P O(1):             deg J=4,  dbar<=14;
    J=S4 O(2):            deg J=8,  dbar<=10;
    J=V O(1)+O(9):        deg J=12, dbar<=12;
    J=2W' O(2):           deg J=8,  dbar<=10.

The torsion lengths dbar-deg J are at most 10,2,0,2, all below 12. Their effective determinant divisors are invariant, so each length is zero. **Only now is J=Jbar concluded.** This is cubic-image saturation, not a statement that the three plateau defects vanish.

For every candidate B=J*(1) has H0(B(-1))=0, and consequently H0(F1(3))=0 and H0(F2(3)) embeds in H0(B(1)).

## 6. Each full-rank candidate is impossible

### S4 O(2)

Here B=S4 O(-1), and exact Euler additivity gives

    chi F2(3)=W'+T6-W-S4,
    H0(B(1))=S4.

Positive Euler coefficients force W' and T6 into H0(F2(3)), contrary to its injection into S4. H1 is genuine and cannot cancel these positive coefficients.

### 2W' O(2)

The exact identity W' Sym2 W=T6 makes Hom_G(T6 O,W' O(2)) one-dimensional. A map into two identical target copies consequently has components (alpha f,beta f) for the same f, and factors through one diagonal W' O(2), of rank two. Such a map cannot surject onto its proposed rank-four image. The multiplicity-one argument is essential; separate nonzero Hom tests do not establish joint generation.

### V O(1)+O(9)

Here B=V O+O(-8). Exact Euler additivity and the section injection give

    chi F2(3)=T6=H0(B(1)),
    H0(F2(3))=T6, H1(F2(3))=0.

Hence all ordinary summands of F2 have degree at least -4. Its actual derivative into B(-2)=V O(-2)+O(-10) has zero component to O(-10), since every relevant line-bundle Hom vanishes. Its image is thus contained in the rank-three first summand, contradicting the required generic rank four.

### P O(1)

Here B=P O and c3=0. The determinant recurrence and endpoint bounds imply

    a=-30+delta1+2delta2<=-20,
    b=-46+delta3<=-36.

The first positive invariant defect costs at least twelve, whereas both available gaps are ten. Thus and **only in this branch** all three delta_i vanish. Therefore

    a=-30, b=-46,
    (L1,L2,L3,L4)=(P O(-4),P O(-2),P O,P O(2)).

These are derivative-induced associated-graded isomorphisms, not a splitting of the filtered bundle or connection.

## 7. Complete endpoint domain and zero derivative

F0 has rank five, degree -30, all ordinary degrees at most -4, and center-even parity. Each ordinary degree is at least -14 because the other four sum to at most -16. I enumerated the complete domain independently by partitioning the total ten degree deficits from five copies of O(-4), then decomposing each repeated-degree multiplicity into irreducibles of the required central parity. There are exactly 46 shapes.

Associated-graded exactness gives

    chi F0(3)=-S4-T6,
    chi F0(4)=V-A-D.

Exactly the same two shapes as the author survive both character identities:

    F0=V O(-4)+O(-8)+O(-10),
    F0=V O(-4)+W O(-9).

The cubic condition alone leaves seventeen shapes, so omitting the quartic condition would not be justified. The two-twist tests are used only as necessary filters; they are not asserted to classify equivariant K-theory or construct a bundle.

The endpoint derivative is a regular equivariant map F0 -> L1(-2)=P O(-6). Its V O(-4) component vanishes by ordinary degree. The other Hom multiplicities are

    [1 : P Sym2 W]=0,
    [1 : P Sym4 W]=0,
    [W : P Sym3 W]=0.

Therefore the entire endpoint derivative Hom space vanishes in both cases. A subbundle of a constant bundle with zero second fundamental form has constant Grassmannian classifying map in characteristic zero, hence degree zero. This contradicts deg F0=-30 and excludes the final rank-four image shape.

## 8. Independence, controls, and frozen-byte reconciliation

The independent verifier does not import any author code, McKay graph, or historical enumeration. Its character calculations use exact conjugacy-class traces and inner products in Q(sqrt5), check all nine irreducibles' dimensions, central signs and orthogonality, and derive the relevant products and Euler values. It performs 603 checks. Complete equality, not just equality of counts, was checked for the 31-row ledger, 46 endpoint shapes, two endpoint survivors, and four full-rank image shapes.

Run from any working directory:

    python3 verify.py
    python3 -O verify.py
    python3 test_controls.py
    python3 check_package.py

Normal and optimized independent outputs agree byte for byte with RESULT.json. The thirteen executable negative controls reject source-hash corruption, exchanging physical A/V, omitting H1, exchanging actual E/Q* presentations, globally suppressing defects, changing Hom degree differences into section-like degree sums, changing image parity, permitting an unjustified saturation cap, changing the intertwiner multiplicity, changing the endpoint derivative twist, retaining only source Z, dropping the quartic endpoint test, and replacing character equalities by dimensions.

The retained author checker has 12,643 checks. Its normal and optimized runs reproduce the frozen author RESULT.json exactly. The final author proof, checker, result, and complete mathematical inputs were authenticated. The reviewed final author hashes are:

- PROOF.md: `0e291e31481530df3163ed6abc3d433a4e402c98e9258d3a329b05b51a2ea507`
- verify.py: `6d4f66ca5ac1be539a09ef791775e782bc4cafba56dbf18131b0bb7586a21242`
- RESULT.json: `6ba21af4feb947a9bd90190478c8a5ff5ddfb43754b101e009eb10fd34a94a05`

During publication preflight, a reporting-only loop-variable shadow was corrected: the final JSON now records intertwiner_multiplicity=1, matching the already checked one-dimensional Hom space, instead of an overwritten endpoint-partition count of five. The mathematical tests, complete domains, and author files are unchanged. Package preflight now explicitly checks that reported value. Normal and optimized replays and all thirteen mutation controls were rerun successfully.

These computations verify universal necessary character and degree consequences. They are not proof-assistant verification of differentiation, saturation, the actual inclusion, the primary-module theorem, or the original geometric theorem. Subject to those written premises, the restricted image bound and its rank-one corollary pass independent review; the ordered (3,1) profile remains open.
