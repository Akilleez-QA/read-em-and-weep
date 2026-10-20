> Historical mathematical record, 16 October 2026. Statements of PASS and check counts below refer to the original recorded verification, not a new execution. See PUBLICATION-SCOPE.md at the common series root for current scope, imported premises, and source/public hash bindings.

# Four detector plus projections are already independent in the first summand

## Result

The four actual detector functionals h,j,p,r have linearly independent restrictions to the inversion-positive part of the first,20-dimensional summand of the global epsilon bridge. Their plus-projected dual cycles have a4-by4 minor equal to16. Consequently no nonzero linear combination of these four functionals is anti-invariant on the full32-dimensional epsilon space. Inversion covariance alone therefore supplies no linear vanishing relation involving only their four original values.

This is a statement about the space of functionals, not nonvanishing of any actual obstruction or detector value. The actual obstruction may satisfy further source-specific conditions, and its separate inversion-invariance premise is not proved here. No remaining twist-1 or twist0 reduction is needed for this rank-four conclusion.

This note also provides an explicit8-dimensional positive quotient basis, its reduction/projection maps and dual linear basis. They are in `positive-eight-maps.json`. These specify eight coordinates of the inversion-positive target through Serre duality, without acquiring any source coefficient.

## 1. Exact free coordinates on the30-dimensional kernel

Use the genuine complex degrees -1,0,1,2 and the source/target convention from ../hm-epsilon-projective-generator-bridge-20261016/THEOREM.md. At internal degree+2 the two constant blocks are E02:K0->K2 and E13:K1->K3. The twist-2 global-section differential is

    E |-> ev E02 - E13 gamma.

Write gamma[b,a,k] for the coefficient of vk in its entry[b,a]. Since ev is two copies of(v0,...,v4), the cycle equations are exactly

    E02[5c+k,a] = sum_(b=0..14) E13[c,b] gamma[b,a,k],
    c=0,1; k,a=0,...,4.                            (1)

Thus all30 E13 entries are freely chosen; (1) uniquely determines all50 E02 entries. This is an explicit integral graph isomorphism K30=ker(80->50), not a new rank calculation. The free coordinate e_r has r=15c+b for E13[c,b]. It is literally the archived PR76 free-variable ordering50,...,79 after subtracting50. The homogeneous model literals independently verify (1) for every graph generator and all current detector cycles.

## 2. Exact d5 quotient and involution

The published PR76 complete-Cech certificate gives the incoming d5 image, in precisely this K basis, with columns

    b_(2a) = e_a + e_(25+a),
    b_(2a+1) = e_(10+a) + e_(20+a),  a=0,...,4.     (2)

Every displayed coefficient is+1. Its20 support positions are distinct. The complete hypercohomology spectral-sequence reduction identifies H2(B(-2)) with K30/image(d5); there is no other incoming differential. We use that authenticated complete-domain result, not a clipped-Cech inference. A global sign change of all d5 columns would leave the image unchanged, but the saved coefficients match the published convention.

Retain quotient basis e0,...,e19 and eliminate

    e_(25+a)=-e_a, e_(20+a)=-e_(10+a).              (3)

For k=(k0,...,k29), the exact quotient map Q is

    q_a=k_a-k_(25+a),
    q_(5+a)=k_(5+a),
    q_(10+a)=k_(10+a)-k_(20+a),
    q_(15+a)=k_(15+a),      a=0,...,4.             (4)

Its kernel is exactly (2), and inclusion of the first20 coordinates is a section. In particular rows5,...,9 and15,...,19 are completely untouched by any d5 boundary.

From the authenticated chain reversal, E13 transforms as -E13 diag(J5,J5,J5). Hence

    I(e_(5b+a))=-e_(5b+4-a).                       (5)

This is true on K30 for b=0,...,5. It preserves (2), commutes with Q, and induces four -J5 blocks on the quotient basis(3). No extra Serre or canonical-line sign occurs: reversal on five projective coordinates is even and the global epsilon generator a is fixed. Thus the quotient has positive dimension8 and negative dimension12, consistently with the independent trace audit.

## 3. Actual detector coordinates, including the factor4

The global generator bridge identifies the first detector component with4E_d in H2(B(-2)), where genuine-degree supertrace gives

    Str(FE)=-tr(F20E02)+tr(F31E13).

The E13 entry in each E_d has coefficient+1. Therefore the exact K coordinates are

    4Eh=4e15, 4Ej=4e16, 4Ep=4e5, 4Er=4e6.        (6)

The E02 components are not discarded: they are the uniquely determined graph entries(1), and the checker compares them with every sparse ambient cycle in the bridge. Chain transport, followed by the same graph identification, gives

    I(4Eh)=-4e19, I(4Ej)=-4e18,
    I(4Ep)=-4e9,  I(4Er)=-4e8.

Applying the plus projector(1+I)/2 and then Q therefore yields

    h: 2(e15-e19), j: 2(e16-e18),
    p: 2(e5-e9),   r: 2(e6-e8).                  (7)

The rows15,16,5,6 of these four columns form2I4, with determinant16. None of those rows occurs in a d5 column. Thus the four classes in(7) are independent in the **actual cohomology quotient**. Neither ordinary closure alone nor disjoint raw pivots alone would prove this; the absence of all d5 boundary coordinates is the essential extra certificate.

The global epsilon splitting and inversion preserve its three summands. Any relation making a combination of the original four detectors anti-invariant would have zero plus component in every summand, hence in this one. By (7) its coefficients must all vanish. Equivalently, the four functionals restricted to the invariant32-sector are independent already on its first positive8-dimensional subspace. This does not say the actual obstruction occupies arbitrary directions of that subspace.

## 4. Explicit positive8 basis, reduction and dual basis

For b=0,...,3 and s=0,1, in order(b,s), put

    p_(b,s)=e_(5b+s)-e_(5b+4-s).                   (8)

These eight invariant quotient classes form a basis. Their ambient80-cycle lifts are obtained by the graph formula(1). They are supplied sparsely in `positive-eight-maps.json`.

For a K30 vector k, compute q=Qk by(4), and define

    alpha_(b,s)(k)=(q_(5b+s)-q_(5b+4-s))/2.       (9)

These functionals annihilate image(d5) and the minus eigenspace, and satisfy alpha_(b,s)(p_(c,t))=delta_(b,c)delta_(s,t). The section J sends coordinate vectorz to sum z_(b,s)p_(b,s). The exact identities are

    alpha J=I8,
    J alpha = Q (1+I)/2,
    alpha I=alpha,
    alpha d5=0.                                 (10)

The right side in the second identity is read in the retained20-coordinate section. The checker verifies all these identities on every K basis vector. Thus the table supplies both a complete projection/reduction and its dual basis. Through the canonical perfect/Serre pairing, the alpha classes are the basis of the positive part of H2(B(-3)) dual to the eight cycles(8). This determines their cohomology classes exactly as linear functionals; it does not claim separate explicit complete-Cech representatives for those primal classes.

If x_(b,s) denotes the primal coordinate pairing with p_(b,s), the first-summand part of the actual four detectors is

    h=2x_(3,0), j=2x_(3,1), p=2x_(1,0), r=2x_(1,1).  (11)

Contributions from the second and third summands remain in the full detector formula; equation(11) is not an evaluation of the complete detector on an arbitrary class. The positive4-dimensional quotient is supplied by the companion quotient certificate. The negative twist-5 component, if the separate eigenspace theorem is adopted, has no contribution on an invariant class; this note does not rely on that theorem.

## 5. Verification and source scope

The checker runs exact sparse integer/rational arithmetic on at most30 coordinate slots, plus the already specified homogeneous gamma coefficients. It performs no rank search and no physical source, primitive, residue or obstruction evaluation. It verifies all30 kernel graph cycles, the ten d5-image reductions, involution compatibility, a complete quotient-splitting certificate, all eight sparse detector cycles, the nonzero minor, and the positive/dual maps(10).

Inputs are pinned by SHA256 in receipt.json:

- ../hm-epsilon-projective-generator-bridge-20261016/detector-dual-cycles.json, with its proved detector normalization, supertrace signs and finite trace comparison;
- ../hm-factored-coefficient-action-20261014/pinned-model-input.json, original homogeneous gamma/ev source literals;
- ../hm-seed-gauge-scope-independent-20261016/PR76-NOTE.md, the complete twist-2 hypercohomology and d5 certificate.

Related independent reviews are historical imported premise hm-twist-minus3-inversion-independent-20261016/AUDIT.md (see PUBLICATION-SCOPE.md) and the bundled detector-bridge/first-component audit. The completed independent audit reconstructs d5 by a separate sparse Cech contraction rather than merely reusing the support table.
