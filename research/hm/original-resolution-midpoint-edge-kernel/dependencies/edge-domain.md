Editorial scope: This is a mathematical source edition. Historical review and check statements describe the original artifact, not a fresh run. Supporting snapshots are dependencies, not additional new results. Later PR145 mixed-class vanishing supersedes historical unknown mixed-class status; it does not resolve the six pure diagonal conditions.

Supporting dependency only: this complete source text is not a fresh result of this packet.

# Tensorial common-split overlaps and the two endpoint insertion domains

## Result and boundary

The first-face overlap of the common original-resolution split connection has an all-standard-chart, occurrencewise bound that is not asserted for the individual connection coefficients. On an internal-degree-r block F:K^u -> K^v, r=v-u, its exact action in direction d is

    A_(ij,d)^r(F)
      =(B_(j,d)^v-B_(i,d)^v)F-F(B_(j,d)^u-B_(i,d)^u)
         -r q_(ij,d) F.                                      (1)

It is a tensorial degree-zero operator, flips precisely deck bit d, and adds at most carrier/legal **5/1 at each of the two actual endpoint occurrences**. There is no additional standard-coordinate divisor. In the scalar q term only the actual bit-one endpoint pays the finite pole and only the actual bit-zero endpoint pays the infinity pole. This attribution is essential.

For the endpoint input Z_d of the supplied endpoint theorem, both unselected insertions

    H C_d J1(Z_d),              H delta H C_d j(Z_d),
    J1=H delta j,               C_d=[delta,G_d],              (2)

are genuine degree-minus-two, full-character ambient cochains. Their branch-safe coefficient sections are in multiplicity copies of O_Y(-4,-4,-4,-4). A safe uniform certificate for each is **31/9**, derived below from the literal endpoint formula. Alternatively, retaining the older supplied endpoint certificate 19/7 gives **36/9** without using that refinement. Both are dominated by the unchanged weights 54/29. The sharper full five-occurrence certificates are

| Insertion | Carrier vector | Legal vector |
| --- | --- | --- |
| H C_d J1(Z_d) | (9,22,14,14,5) | (1,6,7,7,3) |
| H delta H C_d j(Z_d) | (13,18,18,14,5) | (1,6,7,7,3) |

These are sufficient upper bounds, not exact attained orders. They apply on all standard charts and retain every selected owner and its original target tag. They also give a regular full ordinary partition comparison. A selected scalar conclusion additionally uses the admitted regular scalar selector; no new attribution or bound for that selector is proved here.

This settles the expanded overlap-domain gap for these two summands. It does not bound the isolated selector-connection term L G_d J2, prove cancellation with the baseline or either Fk branch, identify a total divergence, or prove a vanishing pairing. No actual source/model/owner evaluation, matrix or polynomial computation, source import is performed.

## 1. Pinned inputs, geometric convention, and owner indices

The new common-split identity is read at the immutable repository head

[4ae1ba6081db6563389d5ff78597cf2e98ecc04f](https://github.com/Akilleez-QA/read-em-and-weep/blob/4ae1ba6081db6563389d5ff78597cf2e98ecc04f/research/hm/null-common-split-connection/PROOF.md).

Its Git blob is eeb936278d11020bfcddc7ed440aa0eaf592d1d9. The local complete snapshot matches that blob and has SHA256 1a60ae58e110ca02393599cfd391aab9470eb5a90bb9569c8d00ab4c50651a93. All dependencies, accepted reviews, source snapshots, and byte hashes are retained in source-pins.json. The source files are treated only as inert text/AST.

We use these specific mathematical inputs:

1. The accepted raw-block all-chart theorem: B_(o,d)^k=z_d b_(o,d)^k with H_o^5 L_(o,d) b regular on each standard chart, in its actual transported frame. The four resolution weights are k=(-1,1,3,5).
2. The accepted complementary-scalar theorem: s_(q;ij) is an actual scalar of character q for a pair of distinct directions; its coefficient has carrier (5,5), legal (2,2), and the actual q_(ij,d) has the endpoint allocation used below. This proof needs its undifferentiated scalar theorem, not a new scalar derivative.
3. The accepted transition theorem: g_ij and its adjugate are cleared by H_i^2 H_j^2 with legal one at each endpoint, before its advertised conservative carrier-four padding. Its exact invariant derivative has carrier three/legal two at each endpoint. The accepted determinant/common-frame identification supplies the intended inverse interpretation where that is used.
4. The accepted inclusion theorem: j adds 4/1 at its selected owner in the fixed physical row frame. The accepted legal-free homotopy theorem, including its whole-projector identity E=1-gamma H0-H1 delta_K, supplies H with 4/0 at its selected owner.
5. The common-split theorem supplies the SAME original-resolution contraction, fixed common ambient restrictions, equation (1), and the two terms in (2). The supplied endpoint theorem defines Z_d exactly. We retain its physical row/ambient interpretation, without assuming Delta Z_d=0.

Write X=C^4, C:y^2=x^3-x, and Y=(P^1)^4. On a standard chart A let z_d=y_d on a finite factor and z_d=u_d on an infinity factor, where t=1/x, u=y/x^2 and u^2=t(1-t^2). The square-line frame ell_A has transition ell_B=lambda^-1 ell_A. Thus degree-r ambient Hom coefficients obey F_B=lambda^r F_A, with lambda the product of the switched t coordinates. No formal square root of lambda is used.

An owner means an occurrence, including its carrier, legal mask and standard target tag. Two different tuple positions are different occurrences even if every label or divisor coincides. Multiplication adds powers at the same occurrence; addition takes maxima only after occurrence lists are aligned. Equality of divisor equations does not merge occurrences. The legal allowance is a uniform allowance on each of the owner's four legal sections; direction-specific allowances may be padded to it.

## 2. Difference of connections, before any pole estimate

The common-split theorem proves, in one common original-resolution reference,

    Gamma_(i,k)=B_(i,k)+k beta_i,
    beta_i=-m_(i,d)y_d/(2x_d),
    Gamma_(j,k)-Gamma_(i,k)
       =B_(j,k)-B_(i,k)-(k/2)q_(ij,d),
    q_(ij,d)=(m_(j,d)-m_(i,d))y_d/x_d.                    (3)

The old connection is included in this identity. Dropping it would change the operator. The scalar weight difference on F is k_v-k_u=2(v-u)=2r, so the induced difference is precisely (1). G is degree zero and these are ordinary operator commutators. There is no additional sign from r being negative. In particular, the q coefficient is +1 for r=-1 and zero for r=0.

Each Gamma_i is a connection on the same ambient bundle. If a common change of coefficient frame is F_k -> T_k F_k, then

    Gamma_(i,k) -> T_k Gamma_(i,k) T_k^-1-(V_d T_k)T_k^-1.

The second term is independent of the owner. Subtracting the two connections cancels it identically. Hence their difference is an actual End-valued tensor, and its induced action on a Hom block has the usual tensor transformation. This argument holds in genuine bundle frames and does not require square roots on Y. In the strict even Hom frame it reads

    A_B(lambda^r F_A)=lambda^r A_A(F_A).                 (4)

The overlap therefore has no representation-frame derivative anomaly. It is not correct to infer the same statement about an isolated Gamma_i. For example at infinity beta_i/z_d=-m_(i,d)/(2t_d). At a bit-one endpoint the owner's legal section is 1-t_d^2, a unit at t_d=0; it cannot clear that t_d pole. Equation (3) first replaces the difference of these problematic terms by q. When q is nonzero the actual opposite-bit endpoint exists and owns the needed legal equation. This is a cancellation within the exact difference of connections, not a borrowed standard-factor exponent for either isolated connection.

For a common ambient n-cochain F, its first-face overlap is exactly

    (C_d F)_(t0,...,t_(n+1))
       =A_(t0,t1;d)^r(F_(t1,...,t_(n+1))).               (5)

All factors are restricted to the full overlap first. Later faces retain leading owner t0 and cancel in delta G-G delta; the first face has sign +1. In nonidentity ambient transport, (5) is read with that transport on both the input and the second owner's tensor. It is not a subtraction of unrelated framed matrices. This theorem uses the specified fixed common ambient restrictions. It does not drop separate delta-prime terms in a formulation where those restrictions genuinely vary.

## 3. Exact all-chart denominator allocation

For one factor the owner's legal equations are

| Chart | bit 0 | bit 1 |
| --- | --- | --- |
| finite | 1 | x(x^2-1) |
| infinity | t | 1-t^2 |

Set delta_m=m_j-m_i. After coefficient extraction, q=z_d kappa, where

    kappa_finite=delta_m/x,    kappa_infinity=delta_m/t.   (6)

If delta_m=0, q vanishes and needs no denominator. Otherwise one actual endpoint has bit one and the other bit zero. Multiplying kappa by the finite bit-one legal equation gives delta_m(x^2-1); multiplying it by the infinity bit-zero equation gives delta_m. Both are polynomial. Equivalently, padding both endpoint legal factors gives

    L_i L_j kappa=delta_m(x^2-1)       on finite charts,
    L_i L_j kappa=delta_m(1-t^2)       on infinity charts.

The local infinity equation t is charged here to the bit-zero endpoint's global legal section. It is not introduced as an independent standard-tag equation. At ramification its actual multiplicity is retained: t has valuation two on C at infinity.

Let the input have an all-chart coefficientwise certificate (c_o,l_o) on its occurrence list. The exact five summands of (1) have these additional allowances:

| Summand | Additional carrier | Additional legal |
| --- | --- | --- |
| B_j^v F or -F B_j^u | +5 at j only | +1 at j in direction d |
| -B_i^v F or +F B_i^u | +5 at i only | +1 at i in direction d |
| -r q F | zero | +1 at the endpoint specified by (6), if nonzero |

This is a sum-specific allocation. No individual summand needs carrier five simultaneously at both endpoints. A single certificate for their sum is obtained by padding to

    c_i -> c_i+5, c_j -> c_j+5,
    l_i -> l_i+1, l_j -> l_j+1.                           (7)

Existing factors at either occurrence remain and add to these powers. All other input occurrences retain their existing factors. The two endpoints are the actual first two positions of the output tuple, even if their labels coincide; no absent third endpoint pays any pole. The same proof works for equal masks: q is zero but the two raw B terms retain their respective owners.

The accepted B theorem gives coefficientwise polynomial clearance of b=B/z_d on each of all 16 charts. Equations (6) and (7) therefore give an explicit base-coefficient formula for the cleared operator. Regularity is proved on the entire standard chart, not just the legal open where the chosen equations are units. Every clearing equation is the local representative of its existing global homogeneous carrier or legal section. No extra standard equation is left over.

## 4. Character flip and branch-safe operator line

For a chart base ring R_A, the regular cover algebra is free:

    S_A=direct sum_(S subset {0,1,2,3}) R_A z_S,
    z_d^2=f_(A,d),
    f_finite=x_d^3-x_d,    f_infinity=t_d-t_d^3.           (8)

Freeness follows by reduction by monic quadratics and holds at the branch divisors. Localization by invariant base clearing sections preserves the direct sum. Thus coefficient extraction in any character is R_A-linear after clearing. It is never regular division by z_S.

Both B_d and q_d are z_d times base coefficients. If a degree-r input has character S, write its local coefficient as z_S f. Formula (1) gives

    A_d(z_S f)=z_(S xor {d}) D_(S,d) a_d(f),
    D_(S,d)=1 if d notin S;  D_(S,d)=f_(A,d) if d in S,  (9)

where a_d is (1) with B replaced by b and q by kappa. The extra factor f_(A,d), when present, is a polynomial. It creates no denominator. Therefore the character is exactly S xor {d}, allowing zero, and the certificate (7) applies to its extracted coefficient in either case.

The degree-r character-S coefficient line on Y is

    O_Y(r*1-2*1_S).                                      (10)

Tensoriality (4) and the basis identity u=t^2 y prove that (9) has the claimed output line with S replaced by S xor {d}. For an explicit check, b_infinity=t^-2 b_finite and kappa_infinity=t^-2 kappa_finite after substituting x=1/t. If d is absent from S this supplies the new -2 shift. If d belongs to S, f_infinity=t^4 f_finite, so f_infinity b_infinity=t^2 f_finite b_finite, the required +2 shift. The other coordinates retain their existing degree/character transitions. These are transition multipliers on overlaps, not new poles in the already transported infinity coefficient. Equations (6)-(9) give its regular clearance directly there.

This establishes the operator domain on arbitrary admitted pure-character inputs, including the distinction between adding and removing an odd bit. No derivative of the input is being taken in C_d. In particular no quotient-rule increment is charged to the input merely because C_d arose from differentiating a connection comparison.

## 5. Endpoint input: exact typing and a direct owned bound

Let (a,b) and q be complementary pairs among the four directions. The supplied endpoint theorem defines

    Z_a=(theta_b cup s_q-s_q cup theta_b)/2,
    Z_b=-(theta_a cup s_q-s_q cup theta_a)/2.

On an increasing triple (i,j,k), with v the other member of the pair containing d, this is, up to the displayed fixed sign,

    Z_d=(L_v s_(q;jk)-s_(q;ij) U_v)/2,
    L_v=g_ij^-1 V_v(g_ij),
    U_v=g_ij^-1 g_jk^-1 V_v(g_jk) g_ij.                  (11)

The trailing g_ij is retained. These are the same current factors in the frozen Source.E slots and the same raw scalar supplied by RawSource.T. Formula (11) does not simplify U by a cocycle-current identity or cancel inverse factors. The proof applies to the supplied endpoint definition even if Z is nonclosed.

The physical g_ij is a scalar transition matrix in the fixed actual endpoint frames; changing a standard representation chart does not reset these frames. It has character m_i xor m_j, as does its adjugate. The global V_v flips bit v, so the two literal currents in (11) have character {v}. They are meromorphic row endomorphisms in the i frame, with the stated transport on the second term. The accepted raw scalar is a genuine scalar of character q. Thus Z_d has the pure missing-d character S_d={0,1,2,3} minus {d}, as an actual row endomorphism. This is more than a parity label on an unidentified affine matrix.

Using own-carrier two/legal one for each g endpoint and three/two for its derivative, the literal triple ledger is

| Factor | Carrier on (i,j,k) | Legal on (i,j,k) |
| --- | --- | --- |
| L_v | (5,5,0) | (3,3,0) |
| U_v | (4,9,5) | (2,5,3) |
| L_v s_(q;jk) | (5,10,5) | (3,5,2) |
| s_(q;ij) U_v | (9,14,5) | (4,7,3) |
| Z_d | (9,14,5) | (4,7,3) |

All charges on j in U add: 2+2+3+2=9 carrier and 1+1+2+1=5 legal. The scalar contributes at its own two endpoints, not an inferred adjacent pair. Thus Z_d has safe uniform bound 14/7. This direct bound also proves the older 19/7 certificate sufficient; we do not need to recover that older bound through a current simplification.

Inclusion into the strict complex uses the actual integral frame formula

    j_A(Z)=I_i(v_A) diag(1,c_iA^-1) Z^t
                           diag(1,c_iA) P_i(v_A),
    c_iA=e_i^2/ell_A.

Its two homogeneous changes cancel the c changes, so j_B(Z)=j_A(Z) in degree zero. All displayed multipliers are deck invariant; the one transpose is retained. The inclusion therefore preserves the missing-d character and adds 4/1 at i alone, giving

    jZ: carrier (13,14,5), legal (5,7,3).                 (12)

The legal-free H is an actual degree-minus-one bundle map, invariant under the deck group, satisfying H_B(lambda^r F)=lambda^(r-1)H_A(F). It adds 4/0 at the selected owner. Ambient restrictions preserve these identities because lambda is independent of the selected owner. This gives all the typing and clearance inputs needed for (2); no selector connection enters.

## 6. Two insertion domains and full occurrence ledger

The unsigned J1=H delta j has bidegree (+1,-1). C_d has bidegree (+1,0). Hence both terms (2) have bidegree (+2,-2). Starting from Z_d of Čech degree two, both outputs have Čech degree four and therefore five ordered occurrence positions. Every occurrence selected before later face deletion remains attached to its factor.

Both paths contain exactly one C_d, two H factors and one j. The H and j preserve deck character; C_d flips missing bit d. Both outputs are consequently pure full-character degree-minus-two ambient maps. Formula (10) gives O_Y(-4,-4,-4,-4) in every block multiplicity. This is a rational sheaf-membership assertion before the pole bound, and its coefficient extraction is the branch-safe projection (8).

For a vector x of length n let D(x) be the coordinatewise maximum of its n+1 embeddings in a tuple of length n+1 with one slot omitted. This is a bound for delta. It adds no denominator. Define

    Q(x)=(0,x_0,...,x_(n-1))+5(e_0+e_1)  for carriers,
    Q(l)=(0,l_0,...,l_(n-1))+1(e_0+e_1)  for legals.

These are the first-face operation (5), not an all-face maximum: the input is the suffix and both actual overlap endpoints are retained. A homotopy adds 4e_0 to carrier and nothing to legal at its current selected first occurrence. From (12), the complete ledger is

| Word | Carrier | Legal |
| --- | --- | --- |
| jZ | (13,14,5) | (5,7,3) |
| delta jZ | (13,14,14,5) | (5,7,7,3) |
| J1Z | (17,14,14,5) | (5,7,7,3) |
| C_d J1Z | (5,22,14,14,5) | (1,6,7,7,3) |
| H C_d J1Z | (9,22,14,14,5) | (1,6,7,7,3) |
| C_d jZ | (5,18,14,5) | (1,6,7,3) |
| H C_d jZ | (9,18,14,5) | (1,6,7,3) |
| delta H C_d jZ | (9,18,18,14,5) | (1,6,7,7,3) |
| H delta H C_d jZ | (13,18,18,14,5) | (1,6,7,7,3) |

The q term of C_d j is actually zero because its input internal degree is zero. We do not exploit that cancellation in the padded table. The table also does not exploit the sharper rank-specific B estimates or block-sensitive H branches. Thus it remains a conservative consequence of the supplied uniform operator bounds. The union of the two summands is cleared by carrier (13,22,18,14,5), legal (1,6,7,7,3), or uniformly 22/7.

For a simpler certificate independent of the placement refinement, pad every operator to every occurrence. With the directly proved 14/7 endpoint bound this gives

    14/7 + 4/1 + 4/0 + 5/1 + 4/0 = 31/9.                (13)

The two distinct overlap endpoints do not cause +10 at a single occurrence: (7) is +5 at each, and tuple positions are not merged. With the older sufficient endpoint allowance 19/7, the same reasoning gives 36/9. No formula uses a maximum instead of addition for two factors belonging to the same occurrence.

The signs in the common-split identity are unchanged:

    J2'=-G_d J2+H C_d J1+H delta H C_d j.

Both insertions have plus signs here, unlike the alternative S=-Gamma convention. Sign changes would not change the pole inequalities but would change the derivative identity. We have not re-proved or used any cancellation against -G_d J2.

## 7. Full weighted extension, with original tags retained

Let b be any coefficient of either insertion in its full-character O(-4)^4 line. Choose the simple uniform certificate

    C'_o=H_o^31 product_r L_(o,r)^9.

The preceding all-chart proof says N=(product_o C'_o)b is regular on every standard chart in the corresponding cleared line. The sharper vectors or the weaker 36/9 certificate work equally well. The fixed weights remain

    C_o=H_o^54 product_r L_(o,r)^29,
    rho_o=C_o Q_o

on the owner's own standard chart, with the existing regular Q_o. Since C_o/C'_o is a regular product of the SAME owner's homogeneous sections, rho_o/C'_o is regular there. No partition is changed.

For the full ordinary comparison Pi_4, all five sampled source occurrences retain their individual weights and original source-to-target tag assignments. On its full target intersection,

    (product_o rho_o)b=N product_o(rho_o/C'_o)

is regular in the output line. If the inherited standard factor Z_(r(o),a)^5251 is included in the bookkeeping, put D'_o=C'_o product_a Z_(r(o),a)^5251 and instead write the identical expression

    ((product_o D'_o)b) product_o(rho_o/C'_o)
                    / product_(o,a) Z_(r(o),a)^5251.     (14)

Every denominator in (14) is a unit on this FULL target intersection because its original target tag is retained. No new such factor was required by the overlap calculation. Standard allowances here are inherited bookkeeping, not a substitute for proving (6).

For a partial inserted-prefix comparison with unweighted original suffix, retain the suffix clearing product explicitly. If B is the inserted occurrence list and A the original suffix, then

    (product_(a in A) C'_a)(product_(b in B)rho_b)b

has the same cleared-suffix interpretation on the full original target intersection. Omitting the suffix factors would be a different, unproved statement. Repeated target tags do not identify source occurrences or permit absent tags to be borrowed. The boundary of a degree-four output uses six occurrence positions, with face owners retained and zero padding where absent; it is not a five-owner boundary assertion.

An admitted regular, degree-compatible selector L takes these ambient coefficients to the corresponding scalar line without adding poles, and commutes with the stated chart interpretation. Under that existing selector premise, L applied separately to either term in (2) has the same regular compared domain. This statement does not derive regularity or covariance of L G_d J2, L'J2, or any output obtained by differentiating L. The two regular overlap summands need not themselves be boundaries or have zero Serre trace. Full comparison and regularity alone imply no remainder cancellation.

## 8. Static controls and remaining frontier

check_overlap_metadata.py authenticates complete inert input/dependency bytes, verifies complete selected AST contracts, and checks only finite integer weights, characters, legal-factor ownership, tuple deletion and occurrence vectors. It does not import the source or construct source field, polynomial, primitive, matrix, source or jet objects. Scalar identities, tensoriality and regularity are established by the mathematical arguments above, not by testing physical values.

The controls range over all 16 standard charts, all 256 legal-mask pairs, all four directions, all characters and all complex block degrees. They reject the wrong infinity owner for q, borrowing a legal equation when masks agree, omitting the common frame anomaly before subtraction, using k_v-k_u=r, replacing the character XOR by unconditional union, branch-factor division, losing the first-face prefix owner, merging equal-label occurrences, dropping the trailing transition in U, wrong placement of the two H charges, undercharging a same-occurrence product, and changing either insertion sign. Normal and optimized Python reports are required to agree.

The resulting theorem is an all-chart domain for an explicit connection-difference operator and its two actual endpoint insertion words. It uses accepted primitive and frame facts, the exact mathematical denotation of V, and the supplied endpoint/HPL definitions. It does not newly verify arbitrary implementation semantics, prove selector attribution, bound separate Gamma or selector-Gamma pieces, eliminate nonclosed-input defects, prove full remainder cancellation, certify, or obtain an obstruction or detector value.
