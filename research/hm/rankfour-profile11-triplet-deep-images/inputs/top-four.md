# Three source-D shapes on the actual rank-four top-degree-four boundary

## Result and input boundary

On the original physical line P(W*) with G=SL2(F5), suppose the ACTUAL Gauss quotient A_q has rank four, top ordinary degree exactly four, and at least one negative ordinary degree. Retain the actual four-source theorem, center-even parity, and the source lower bound min degree(A_q)>=-8. Assume the three actual coefficient gates

    H0(A_q) <= M2=A_std+2V+3P+4D,
    H0(A_q(1)) <= M3=3W'+3S4+6T6,
    W'+2T6 <= H0(A_q(3)).

Here <= denotes an equivariant representation injection, not a fiberwise bundle injection. The first two come from the coherent-image injection A_q -> Q(-2) and the actual dual presentation; they are valid without zero determinant defect. The third is the actual two-cubic-channel theorem.

These constraints and actual source-Hom give fourteen necessary shapes. For maximal profile (1,1), the rank-thirteen primal endpoint capacity excludes three. A new actual-source quartic visibility lemma excludes four more. Two dual sign cuts and two small actual-kernel arguments then leave exactly the three source-D shapes in Section 9. None is asserted realized; this is neither closure of the top-four boundary nor a coarse-bin reduction.

Retain the actual saturated inclusion E in H O, dim H=30, and S=Q* in its dual constant ambient, over C with the constant connection and the fixed physical determinant convention. The actual bundles have ranks 17 and 13 and degree -54. Their derivative kernels are K and L. Generic derivative rank four and maximal ordered plateau (1,1) imply rank K=13, rank L=9 and endpoint derivative ranks at most three. These are assumptions on the actual Gauss objects, not on arbitrary bundles with the same splittings.

The four complete immutable sources in INPUTS.json are:

- ACTUAL at db51525015bb7c5e825833d550d08dedf6f6ea96, research/hm/order-four-quadratic-load/ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md: actual presentations, physical representations and equivariant splitting conventions.
- PR1123 at 504b7eb800407dfc7e6340c98c72cdd553939f54, research/hm/primary-terminal-slope-obstruction/PROOF.md: the necessary four actual sources.
- PR1140 at 7a2488bcd36d95f79b5198001111b1a31fe5c3ba, research/hm/primary-gauss-double-channel/PROOF.md: two independent cubic channels and the negative-horizontal-subspace mechanism.
- PR1185 at 236e0a3723c3d73ea7fb9e549376540a8e70508b, research/hm/rankfour-profile11-low-top/PROOF.md: the actual three-column endpoint capacity and the sign restriction min degree(A_q)<0. Its Section 2 proves these consequences for all defects, before assuming a low top degree.

The transitive actual geometric hypotheses of these inputs remain imported. No rank-three ledger, historical bundle enumeration, later top-three kernel/image deduction, or actual-instance computation is used. The four sources, in the physical notation, are

    E_D=D(-2)+(W'+T6)(-3)+V(-4)+O(-8),
    E_P=P(-2)+(W'+T6)(-3)+V(-4)+W'(-5),
    E_V=V(-2)+(W'+T6)(-3)+2V(-4),
    E_Z=(W'+2T6)(-3)+V(-4).

The established gates are applied before source-row or kernel analysis. Indeed the actual coherent-image injection A_q -> Q(-2), without saturating its image, induces both section injections above. Dualizing the actual S presentation gives

    0 -> M2 O(-2) -> M3 O(-1) -> Q(-2) -> 0.

Its cohomology gives H0(Q(-2))=M2, since O(-1) is acyclic and H1(O(-2))=1. After one twist it gives H0(Q(-1))=M3, since O(-1) is acyclic. These familiar gates are rederived, not claimed new. Positive determinant defect cannot invalidate left exactness of H0. Also every degree of A_q is at least -8 because E(8), and hence its actual quotient A_q(8), is globally generated.

## 1. Gates before source tests

Use R(e) as shorthand for R tensor O(e), and O(e) for a trivial coefficient line. Finite-group equivariant Birkhoff splitting and the center-even ambient force coefficient parity to equal degree parity. The only irreducibles of dimension at most four are 1, W, W', A_std, V, S4, P; W,W',S4 are odd, and 1,A_std,V,P are even.

A top-four block is therefore scalar, A_std(4), V(4), or P(4). A dimension-four top block fills the quotient and contradicts the negative minimum. A top triplet leaves exactly one scalar, necessarily negative. The identities

    A_std tensor Sym4 W = A_std+V+P+D,
    A_std tensor Sym5 W = W'+S4+2T6,
    V tensor Sym4 W = A_std+V+P+D,
    V tensor Sym5 W = W+S4+2T6

show that V(4) fails the twist-one gate: M3 contains no W. A_std(4) passes these two gates.

For scalar-top shapes, H0 excludes every O(0), and permits at most one O(2), since M2 has no trivial constituent and has A_std multiplicity one. Nonnegative scalar degrees are therefore 2 or 4, with at most one degree two.

For a doublet block R(e), the only positive odd degrees under consideration are 1 and 3. W(1) fails H0 because W tensor W=1+A_std. W(-1) fails twist one because it contributes W. The remaining locally relevant identities are

    W' tensor W=P,
    W' tensor Sym2 W=T6,
    W tensor Sym3 W=A_std+D,
    W' tensor Sym3 W=V+D,
    W tensor Sym4 W=W' tensor Sym4 W=S4+T6,
    W tensor Sym6 W=W'+2T6,
    W' tensor Sym6 W=W+W'+S4+T6,
    Sym7 W=W'+T6.

These are fixed universal character identities through symmetric degree seven. In particular O(4) supplies exactly W'+T6 at cubic twist.

## 2. Source-Hom and the negative scalar/doublet blocks

For an actual source row R(d), the Hom into a target U(e) is

    Hom_G(R(d),U(e))=Hom_G(R,U tensor Sym^(e-d) W),

with negative symmetric powers zero. Apply this only to the four fixed source presentations.

A negative scalar target has even degree in {-8,-6,-4,-2}. Hom into O(-6), O(-4), O(-2) vanishes for every source. Hom into O(-8) comes solely from the unique O(-8) of E_D. Hence every negative scalar is O(-8), its presence forces the actual source E_D, and two copies cannot occur: the only possible contributing source rank is one.

For negative doublets, the twist-one gate already excluded W(-1). The remaining source calculation is:

- W(-3), W(-5), W'(-7): all source Hom spaces vanish.
- W(-7): only the O(-8) row of E_D contributes, of rank one, and therefore cannot surject onto the rank-two quotient projection.
- W'(-5): only the W'(-5) row of E_P contributes; its presence forces E_P.
- W'(-3): only the displayed W'(-3) row contributes, in every source.
- W'(-1): there are nonzero source Hom spaces for every source.

The last three are the only possible negative doublet blocks after these necessary source tests. No claim is made that the mere existence of a nonzero Hom guarantees simultaneous quotient surjectivity.

## 3. Exhaustion by the remaining rank partition

### Triplet at the top

The preceding steps leave only

    A_std(4)+O(-8),   source D.                         (T)

Its cubic character contains W'+3T6+S4, so the cubic gate adds no exclusion.

### Scalar at the top, triplet complement

Write A_q=O(4)+R(e), with R=A_std or V. The negative-minimum hypothesis forces e<=-2 even. For e<=-4 the triplet contributes no cubic sections, leaving only one T6 from O(4), which is insufficient. At e=-2, A_std tensor W=W+S4 has no T6 whereas V tensor W=T6. The only shape is therefore

    O(4)+V(-2).                                        (C1)

### Scalar at the top, three scalar complements

At least one scalar is negative. It must be the unique O(-8), forcing D. The other three scalars have degrees 2 or 4, with at most one degree two. Consequently the only shapes are

    O(-8)+O(2)+2O(4),   O(-8)+3O(4).                    (C2,C3)

### Scalar at the top, a doublet and a scalar

Write A_q=O(4)+R(e)+O(f).

If f<0, then f=-8 and the source is D. Since O(-8) contributes no cubic sections, R(e) must supply at least one T6. The rank, parity, and gates in Section 1 leave exactly

    (R,e)=(W',-1), (W',1), (W,3), (W',3).              (C4-C7)

Indeed e<=-3 supplies no T6; at e=-1 only W' supplies T6; W(1) was already removed by H0; and both doublets at degree three supply T6. All four displayed shapes pass the three coefficient gates.

If f>=0, then f=2 or 4. Negative minimum now forces e<0. Section 2 leaves e=-1,-3,-5 with R=W'. Thus precisely

    O(4)+O(f)+W'(e),  f in {2,4}, e in {-1,-3,-5}.     (C8-C13)

Both scalar blocks together supply the required W'+2T6 at cubic twist. The e=-5 shapes force source P; the others have no source restriction from these particular Hom tests.

These partitions are exhaustive without an enumeration of bundle candidates: a scalar top consumes rank one, and its rank-three complement has only the irreducible dimension partitions 3, 2+1, or 1+1+1. Repeated top scalar blocks are already included in the last two partitions.

## 4. Three-column primal capacity, with an exact square completion

In maximal ordered profile (1,1), the actual endpoint K has rank thirteen and degree -54-a, where a=deg A_q. Its derivative rank is at most three. The coherent-image capacity lemma gives

    -54-a <= max sum_(i=1)^3 [h_i lambda_i-h_i(h_i+1)],

where lambda_1>=lambda_2>=lambda_3 are the top three ordinary degrees of A_q, h_1>=h_2>=h_3>=0 are integers, and their sum is thirteen. This uses actual saturated derivative kernels, not a split connection or saturated image in A_q(-2j).

There is a uniform symbolic upper bound. Put L=lambda_1+lambda_2+lambda_3 and

    c_i=lambda_i/2+(26-L)/6,
    C=-208/3+13L/3+(3 sum lambda_i^2-L^2)/12.

On the plane sum h_i=13, exact completion of squares gives

    sum [h_i lambda_i-h_i(h_i+1)] = C-sum (h_i-c_i)^2.

Therefore the integer capacity is at most floor(C). For every one of the thirteen symbolically derived scalar-top shapes, the displayed single height triple below attains floor(C), certifying the exact capacity without scanning any candidates or heights.

| Shape | a | deg K | top three | attaining heights | capacity | decision |
| --- | ---: | ---: | --- | --- | ---: | --- |
| O4+V(-2) | -2 | -52 | (4,-2,-2) | (6,4,3) | -64 | excluded |
| O(-8)+O2+2O4 | 2 | -56 | (4,4,2) | (5,4,4) | -26 | retained, D |
| O(-8)+3O4 | 4 | -58 | (4,4,4) | (5,4,4) | -18 | retained, D |
| O(-8)+O4+W'(-1) | -6 | -48 | (4,-1,-1) | (6,4,3) | -57 | excluded |
| O(-8)+O4+W'(1) | -2 | -52 | (4,1,1) | (5,4,4) | -42 | retained, D |
| O(-8)+O4+W(3) | 2 | -56 | (4,3,3) | (5,4,4) | -26 | retained, D |
| O(-8)+O4+W'(3) | 2 | -56 | (4,3,3) | (5,4,4) | -26 | retained, D |
| O4+O2+W'(-1) | 4 | -58 | (4,2,-1) | (5,5,3) | -45 | retained |
| 2O4+W'(-1) | 6 | -60 | (4,4,-1) | (5,5,3) | -35 | retained |
| O4+O2+W'(-3) | 0 | -54 | (4,2,-3) | (6,5,2) | -50 | retained |
| 2O4+W'(-3) | 2 | -56 | (4,4,-3) | (6,5,2) | -40 | retained |
| O4+O2+W'(-5) | -4 | -50 | (4,2,-5) | (6,5,2) | -54 | excluded |
| 2O4+W'(-5) | -2 | -52 | (4,4,-5) | (6,6,1) | -43 | retained, P |

Here O4 denotes O(4) and O2 denotes O(2). For the three exclusions alone, the continuous bounds are respectively -190/3, -113/2, and -323/6; their floors already contradict deg K. Equality or attainment is not required to exclude them.

The triplet-top shape (T) has a=4, deg K=-58, and top triple (4,4,4), whose capacity is -18; this capacity test does not exclude it.

## 5. A uniform actual quartic V-visibility lemma

For every actual source, independently of the generic derivative rank or plateau profile,

    V embeds in H0(A_q(4)).                              (V4)

Here is a proof using the actual ambient connection. Let C be the full direct sum of the displayed V(-4) rows in an equivariant source splitting. Thus C=V(-4) for sources D, P, Z and C=2V(-4) for source V. Since C is a direct summand of E, and E is saturated in the original constant ambient H O, C is saturated there as well.

Suppose the V multiplicity in H0(A_q(4)) were zero. Then the actual quotient p:E->A_q vanishes on C, since

    Hom_G(C,A_q)=Hom_G(H0(C(4)),H0(A_q(4)))=0.

The actual derivative beta_E therefore kills C. The second fundamental form of C in the constant ambient factors as

    delta_C:C -> (E/C)(-2) -> (H O/C)(-2).

All target summands in (E/C)(-2) have degree below -4 except the degree-minus-two source top row after twisting by minus two. This sole possible coefficient target is D, P, V, or zero in sources D, P, V, Z respectively. All of these statements concern ordinary bundle Hom; no source splitting is declared horizontal.

For D, P, Z, the coefficient target contains no V, so delta_C=0. A saturated horizontal subbundle of a constant bundle on P1 over C is constant: its Grassmannian classifying map has zero differential, hence is constant in characteristic zero. This contradicts the negative degree of C.

For source V, delta_C is determined by an equivariant constant coefficient map 2V->V. Its kernel contains a nonzero coefficient subrepresentation U. The subbundle U(-4) is saturated in C and hence in the original constant ambient. Its derivative modulo C is zero, by the choice of U. Its own second fundamental form therefore lands in

    (C/U(-4))(-2),

whose ordinary degrees are all -6. Hom from U(-4) to this target is zero by degree. Thus U(-4) is again horizontal and negative, a contradiction. This also treats delta_C=0. Therefore the V multiplicity cannot vanish, proving (V4).

This proof proves only a coefficient-space visibility statement. It never asserts a fiberwise-injective V(-4) image in A_q and never uses a saturated image of the actual derivative.

Among the ten scalar-top capacity survivors, exactly four have no V in their quartic sections:

    H0((O(-8)+3O4)(4)) = 3P+3D,
    H0((O(-8)+O4+W'(1))(4)) = A_std+2P+2D,
    H0((2O4+W'(-3))(4)) = 3P+2D,
    H0((2O4+W'(-5))(4)) = 2P+2D.

These use only Sym8 W=P+D, W' tensor Sym5 W=A_std+P+D, and W' tensor W=P. Thus (V4) excludes all four, uniformly over their permitted actual sources. The first two already force D by their scalar tail; the last forces P by its doublet tail. No source choice can repair the missing V.

## 6. Seven shapes before the dual and kernel tests

After the preceding gates, source-Hom tests, primal capacity, and the actual quartic lemma, the only necessary shapes are:

1. A_std(4)+O(-8), source D.
2. O(-8)+O(2)+2O(4), source D.
3. O(-8)+O(4)+W(3), source D.
4. O(-8)+O(4)+W'(3), source D.
5. O(4)+O(2)+W'(-1), no further source restriction asserted here.
6. 2O(4)+W'(-1), no further source restriction asserted here.
7. O(4)+O(2)+W'(-3), no further source restriction asserted here.

For clarity, all seven pass the new quartic V test. Their H0(A_q(4)) characters in the same order are

    A_std+2V+2P+2D,
    V+3P+2D,
    V+3P+2D,
    1+A_std+V+2P+2D,
    2V+2P+2D,
    V+2P+3D,
    V+3P+D.

The first line uses A_std tensor Sym8 W. This list is a necessary reduction only. It contains no assertion that any quotient is actually realized, any source listed as unrestricted really supplies it, or any remaining determinant defect is zero.

## 7. Two immediate dual endpoint sign exclusions

Keep the original determinant defect t>=0, so deg A_q+deg B=-8-t. Write a=deg A_q and v=min degree(A_q). The dual endpoint estimate from PR1185 Section 2, before its low-top contradiction, is

    a+9v <= -8-t.                                      (D)

For clarity this is obtained without assuming a saturated transpose image: B injects as a coherent sheaf into A_q*(-2), hence top B<=-2-v. Three-column capacity for L of rank nine gives -54-b<=9(-2-v)-36, or b>=9v; combining with a+b=-8-t yields (D).

For O(4)+O(2)+W'(-1), a=4 and v=-1, so a+9v=-5. For 2O(4)+W'(-1), a=6 and v=-1, so a+9v=-3. Both contradict (D) for every t>=0. Thus these two intermediate shapes are impossible without any further kernel analysis.

## 8. Two small actual-kernel exclusions

We first record the precise derivative coefficient facts used below. Strict top for the original actual E implies top K<=-3. The actual derivative of K factors through A_q(-2), since beta_E kills K. Choose an ordinary equivariant Birkhoff splitting

    K=R3(-3)+R4(-4)+N,       top N<=-5.

Then

    R3 -> H0(A_q(1)),    R4 -> H0(A_q(2))              (K)

are coefficient-space injections. To prove each, a killed coefficient vector gives a saturated direct line O(-3) or O(-4) in K. Its own actual derivative lands in (K/line)(-2), whose top degree is at most -5. No nonzero morphism from either line to that target exists. The line would be horizontal in the original constant ambient and negative, a contradiction. Only the R4 coefficient block injects in the second statement, not all H0(K(4)). No splitting is assumed horizontal.

The complete actual cubic alternatives from PR1140 are R3=0 or S4 for D, 0 or W' for P, and 0 for V and Z. The four sources also have common Euler characters

    chi_G(E(3))=W'+2T6,
    chi_G(E(4))=3V+3P+2D.

For any candidate quotient, exactness of 0->K->E->A_q->0 and the above splitting give

    H1(N(3))=R3-chi_G(K(3)),
    R4=chi_G(K(4))-R3 tensor W+H1(N(4)).              (E)

All H1 summands on the left are genuine representations. For a negative block R(-j), j>=5, its contributions are R tensor Sym^(j-5) W at twist three, and R tensor Sym^(j-6) W at twist four, the latter zero for j=5.

### 8.1 Exclude O(4)+O(2)+W'(-3)

Directly from the displayed quotient and the fixed physical representation products,

    chi_G(K(3))=-W',      chi_G(K(4))=2V+D,
    H0(A_q(1))=S4+T6,    H0(A_q(2))=V+P+D.           (A)

The possible P-source cubic W' is excluded by the first injection in (K). Thus R3 is 0 or S4.

If R3=0, (E) gives H1(N(3))=W'. A genuine contribution to this two-dimensional irreducible budget can only be W'(-5). Hence N=W'(-5), H1(N(4))=0 and R4=2V+D. Its two V copies cannot inject into the single V in the last target of (A).

If R3=S4, then H1(N(3))=S4+W'. The only irreducible negative blocks contributing inside this six-dimensional budget are

    W'(-5) -> W',    S4(-5) -> S4,    O(-8) -> S4.

This list follows from (j-4)dim R<=6, central parity, and the fixed symmetric powers through degree five; any other block contributes W or T6, or exceeds the dimension. Consequently N is S4(-5)+W'(-5), or O(-8)+W'(-5). Their quartic H1 characters are respectively 0 and A_std. Since S4 tensor W=A_std+D, formula (E) gives respectively

    R4=2V-A_std,       R4=2V.

The former is not genuine, and the latter again violates the single V target in (A). This excludes the quotient for every actual source and defect. The argument uses the actual maps in (K), not only a coincidental match of cohomology characters with an earlier quotient.

### 8.2 Exclude O(4)+W'(3)+O(-8)

The scalar tail already forces source D. Its cubic alternative is 0 or S4. Suppose R3=S4. The actual inclusion of its evaluated top subbundle S4(-3) into E_D can have a nonzero component only in D(-2), by degree and irreducible inequivalence. That Hom space is one-dimensional, because D tensor W=S4+T6. The canonical binary evaluation sequence is

    0 -> S4(-3) -> D(-2) -> O(2) -> 0.

Thus the actual D-row of p:E->A_q factors through O(2). But

    Hom_G(O(2),O(4))=0,
    Hom_G(O(2),W'(3))=0,
    Hom_G(O(2),O(-8))=0:

the first has coefficient invariants in Sym2 W=A_std, the second in W' tensor W=P, and the third is negative by degree. The D-row would vanish entirely, putting D(-2) in K and contradicting H0(K(2))=0. Therefore R3=0.

The exact Euler and target characters are

    chi_G(K(3))=-W-W',   chi_G(K(4))=2V+P-1,
    H0(A_q(2))=A_std+D+V+2P.                         (B)

Now H1(N(3))=W+W'. Its dimension is four. The only negative irreducible blocks contributing inside it are

    W(-5) -> W,     O(-6) -> W,     W'(-5) -> W'.

Indeed (j-4)dim R<=4 and parity leave only these: S4(-5) or O(-8) contribute forbidden S4, and all further blocks are too large. Hence N=W(-5)+W'(-5), or O(-6)+W'(-5). Their quartic H1 is 0 or 1. Formula (E) then gives R4=2V+P-1, which is not genuine, or R4=2V+P. The genuine case has two V copies while (B)'s target has one, contradicting the second injection in (K).

This is a four-dimensional genuine-cohomology argument and one canonical source-row factorization, not a global kernel search or an evaluation of the actual D-row coefficient.

## 9. Final three necessary source-D forms

Only the following forms remain after all proved constraints:

    A_q=A_std(4)+O(-8),
    A_q=2O(4)+O(2)+O(-8),
    A_q=O(4)+W(3)+O(-8).

In every case the actual source must be E_D. Their quotient degrees are respectively 4,2,2, and their actual kernels have rank thirteen and degrees -58,-56,-56. No form is asserted realized or excluded. All original defects remain within the scope: the proof has not assumed t=0 or used a defect classification. The top-degree-four locus and the full maximal profile (1,1) remain open. No coarse-bin count changes.

## 10. Contribution and verification boundary

The structural contributions are the complete symbolic top-degree-four reduction and the rank-independent quartic V-visibility consequence (V4). The method applies the original coherent-image section gates first, then irreducible rank partitions and source maps, and finally actual derivative geometry. It uses no broad quotient search, historical enumeration, selected coefficients, parameters, points, jets, tensors, matrices or instance ranks.

The universal character products, fixed negative-source Hom checks and exact square-completion certificates are the only arithmetic checks. Independently reviewing those computations does not certify the transitive actual geometric premises by a proof assistant. Higher top degrees and the three final actual configurations remain open beyond this theorem.

The negative-horizontal-subbundle method itself is established, including the general near-top coefficient argument in PR1129 at d1238732f42df5c70ba4430e230428d2cf699bbe. The source-specific quartic consequence here reaches beyond that immediate degree bound: a quartic source can reach the degree-minus-two top row, so its V-isotypic internal target must be examined. The two-copy source-V argument is retained explicitly. No claim that the underlying connection method is new is intended.
