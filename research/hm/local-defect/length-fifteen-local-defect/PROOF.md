Publication context: this retained proof or audit may describe an intermediate bound or then-open branch. Read the unit overview for the current scope and later implications. Historical mathematical review is not a new formal verification.

# Canonical local length fifteen exclusion

## Statement and imported hypotheses

Under exactly the canonical hypotheses and notation of ../length-fourteen-local-defect/PROOF.md, length fifteen is impossible. In particular, conditional on the previously established support/orbit hypotheses, the unrestricted canonical local minimum is at least sixteen and the thirty-point contribution at least 480. This does not assert existence at sixteen. The cyclic minimum remains at least 31.

We import the independently audited representation budget and filtered initial-relation estimates from the preceding proofs. Put P=Ext^4_R(Q,R), T=P/mP, s=dim T, h_j=dim gr_j P, K1=ker(W tensor T -> gr_1 P), k=4s-h1, and q=dim((Sym^2 W tensor T)/(W K1)). Then

    beta1 + a_B(Tor1(P,k)) <= 2s+2,
    beta1 >= k + max(0,q-h2),
    q >= 4h1-6s.

If beta1=k, K1 is the full minimal relation representation, and q=h2. A quotient by the homogeneous linear initial relations surjects onto gr P, even when there are higher corrections. All such uses below concern this associated-graded surjection unless exactness is explicitly proved.

Write O_c={(i,c i^2):i in F5*, all arithmetic mod 5}, with W=O_3. Other irreducibles are clock-trivial, of dimension one (B-weight zero) or two (weights (0,+b),(0,-b)). Negation sends O_c to O_{-c}. An H-character restricts trivially to B. We may complete and choose equivariant formal parameters and top lifts.

Cyclic P is excluded by its bound 31. Square-zero P is excluded by its bound ten. Consequently s>=2 and h2>=1. The inequalities h1>=2s-2 and h1<=14-s imply s<=5.

## 1. Top dimension two

The first layer has dimension divisible by four. If h1=8 or more, the relation estimate excludes it: h1=8 gives q>=20 and h2<=5, hence beta1>=15>6; larger h1 only increases the contradiction. Therefore h1=4 and k=4.

The audited imbalance argument forces K1=O_0, top weights (0,+2),(0,-2), and first layer O_1. Indeed any nonzero slope in K1 would already force dimension plus imbalance at least eight, beyond the budget six. The homogeneous quotient by K1 is two polynomial planes: the top of weight (0,-2) uses x1,x4, and the top of weight (0,2) uses x2,x3. Its quadratic piece is O_1 plus (0,+1),(0,-1), and its cubic piece has no clock-trivial weights.

There are at most three orbit constituents in P. With only one, the module ends after a clock-trivial quadratic layer of dimension at most two. With two, the second orbit must occur in degree two: a clock-trivial layer separating two single orbit layers must have dimension at least four, by the commutativity lemma in the length-thirteen proof, while the quadratic quotient has only two such dimensions. Then the cubic layer, being clock-trivial but a quotient of the cubic plane piece, vanishes. Its length is at most twelve.

With three orbits, the second again occurs in degree two. The quadratic layer cannot have dimension six, since the prefix would have length twelve and the third orbit would not fit. Thus it is O_1 of dimension four. The third orbit must then occur in degree three, since that degree has no clock-trivial weights. The prefix has shape (2,4,4,4), of length fourteen. Length fifteen therefore requires shape (2,4,4,4,1), with the fourth layer of B-weight zero. The cubic plane piece consists of O_2+O_3: in the x1,x4 plane its second coordinate is -2+3*3=2, and in the other plane it is 2+3*2=3; the first coordinates give the two stated slopes. Thus the cubic layer is O_2 or O_3.

We now control the filtered corrections explicitly. The O_0 weights of the four linear initial relations are absent from all layers of P: the first and second orbit layers are O_1, the cubic layer is O_2 or O_3, and the top and terminal layers are clock-trivial. Hence these four linear relations are exact. Their quotient N is the direct sum of two formal power-series planes with the top twists just specified. The opposite quadratic products x1*x4 on the first top and x2*x3 on the second have weights (0,-1),(0,1), respectively. Their quadratic images vanish since h2=O_1, and their weights occur in neither the cubic orbit nor the terminal zero-weight line. They too are exact relations.

These two quadratic relations give independent minimal classes beyond the four linear relations. Indeed, in N their lowest terms are the nonzero opposite quadratic monomials in distinct plane summands; no element of the kernel has order below two in N, so these cannot be in the maximal ideal times that kernel. Since beta1<=6, the four linear and two quadratic relations exhaust the minimal generators of the full kernel. Their quotient is the sum of two twisted modules C[[x,y]]/(xy), which has infinite length. This contradiction excludes the remaining top-two case, with arbitrary filtered corrections allowed.

## 2. Top dimension three

Again h1 is divisible by four. If h1>=8, then at h1=8 one has k=4, q>=14, h2<=4, hence beta1>=14>8; larger h1 is worse. Thus h1=4, k=8=beta1, and q=h2.

The length-independent top-three calculation in the audited length-thirteen proof gives top weights 0,(0,+1),(0,-1), K1=O_3+O_2, first layer O_4, and q=h2=6. The homogeneous linear quotient is a residue-field summand plus two polynomial planes, and its cubic piece has no clock-trivial weights. The prefix (3,4,6) has length thirteen. To reach fifteen a nonzero cubic layer would have dimension at most two, hence be clock-trivial, a contradiction. No claim that the linear relations are exact is needed here.

## 3. Top dimension four

Here 6<=h1<=10. For h1>=8, q>=4h1-24 and h2<=11-h1 give beta1>=(16-h1)+(4h1-24)-(11-h1)=4h1-19, at least13>10. Thus h1=6 or7. A clock-trivial top would force h1 divisible by four, so T=O_c.

If h1=7, the first layer is one orbit plus three clock-trivial dimensions. The clock-trivial part of W tensor O_c consists of two copies of each weight (0,+ (3+c)) and (0,-(3+c)); an odd-dimensional quotient requires c=2. Now k=9 and beta1<=10. Any remaining minimal relation representation has dimension at most one and cannot cancel a nonzero-clock imbalance of K1. Hence its two orbit constituents are self-dual, giving K1 orbit part O_4+O_1, and first layer O_0 plus three zero weights. The source and target of the degree-two Koszul map, at first coordinate one and second coordinates 0,1,2,3,4, are

    O_2 tensor Lambda^2 W:       (0,1,1,3,0),
    (O_0+3*0) tensor W:          (0,0,2,4,0).

The cokernel contains O_2 and O_3, so q>=8. Since h2<=4, beta1>=9+8-4=13, impossible.

Thus h1=6, k=10=beta1, K1 is self-dual, and q=h2<=5. The five candidate (top slope, retained first-layer orbit slope) pairs and source/target vectors are those in the audited length-fourteen proof:

    (0,2): (3,1,0,0,1) versus (2,2,0,0,1)
    (1,1): (1,1,1,0,2) versus (0,1,2,1,1)
    (2,0): (0,1,1,3,0) versus (0,0,2,3,0)
    (3,4): (0,0,3,1,1) versus (0,1,1,1,2)
    (4,3): (1,2,0,1,1) versus (3,1,0,0,1).

The last three excluded rows, namely (1,1),(3,4),(4,3), force at least eight nonzero-clock cokernel dimensions, impossible. In the surviving cases the cokernel contains respectively O_1 or O_2. With q<=5, its nonzero-clock part is exactly that orbit. Any additional dimension must have B-weight zero.

Case A has top O_0, first O_2 plus (0,+2),(0,-2), and quadratic layer O_1 with possibly one zero-weight dimension. Case B has top O_2, first O_0 plus two zero weights, and quadratic layer O_2 with possibly one zero-weight dimension. In B the Koszul target has no weight (0,0): its clock-trivial weights come from W tensor O_0 and are (0,+3),(0,-3). Thus B has q=h2=4.

If h2=4, length fifteen would require h3=1, of B-weight zero. This is impossible in both cases. For A, every cubic in the full free module on O_0 has nonzero second coordinate, since sums of three numbers +2 or -2 are nonzero mod 5. For B, the linear relations include every x_i t_j with j not equal to +i or -i, as shown in the previous proof. Its homogeneous linear quotient is therefore generated by monomials in the opposite pair x_j,x_-j on t_j. A cubic of this kind has second coordinate 2j^2+9j^2=j^2, nonzero. Consequently neither cubic quotient has weight zero.

Only A with shape (4,6,5) remains. Here K1=O_2+O_3 plus (0,+2),(0,-2). These weights are disjoint from the entire last layer O_1+0. Hence the linear initial relations are exact, by equivariant top lifts; their ten independent minimal classes exhaust beta1, so they generate the full kernel. The two-variable argument in the audited length-fourteen proof applies unchanged: after setting x2=x3=0, at most five linear relations remain among four generators over C[[x1,x4]]. Its degree-three piece has dimension at least 4*4-5*3=1. This contradicts m^3 P=0. All top-four cases are excluded.

## 4. The new top-five case

Here h1>=8 and h1<=9. If h1=9, k=11, q>=6, h2<=1, giving beta1>=16>12. Thus h1=8, and h2<=2. The estimates q>=2 and k=12 force

    (h0,h1,h2)=(5,8,2), beta1=12, q=h2=2,

and K1 is self-dual as a B-representation. In particular the quadratic Koszul cokernel has only clock-trivial weights. We exclude every possible top and first layer using explicit weight multiplicities. This uses no assumptions about higher corrections.

Recall Lambda^2 W=O_0 plus (0,+1),(0,-1). The three nonzero-clock slopes of W tensor O_c are

    c=0: 2,2,3; c=1: 1,3,2; c=2: 0,4,1;
    c=3: 4,0,0; c=4: 3,1,4.

For any source and target representations, a target weight multiplicity greater than the source multiplicity forces that weight in the cokernel. Thus even one positive difference at first coordinate one forces a full four-dimensional orbit in this equivariant cokernel, contradicting q=2.

### 4a. Clock-trivial top

Write its weight multiplicities as a copies of zero, b copies each of (0,+1),(0,-1), and c copies each of (0,+2),(0,-2), with a+2b+2c=5. The slopes of W tensor T are 3 repeated a times, 4 and 2 each repeated b times, and 0 and 1 each repeated c times.

The first layer consists of two orbits, so K1 consists of three orbits and must be self-dual. Such a multiset must contain an odd number of O_0. Three O_0 would require c>=3, impossible. With one O_0, the other two must be O_1+O_4 or O_2+O_3. Either requires a=b=c=1. Consequently the top has all five weights (0,b), b in F5, and the first layer is either O_2+O_3 or O_1+O_4.

The source T tensor Lambda^2 W has vector (1,1,1,1,1) at first coordinate one. The corresponding targets (gr_1 P) tensor W have vectors

    first O_2+O_3: (3,1,0,0,2),
    first O_1+O_4: (0,2,1,2,1).

Both have a positive difference. Thus q>=4, contradiction.

### 4b. Top is one orbit plus a character

The only remaining dimension-five top is O_c plus a character, whose B-weight is zero. The nonzero-clock slopes in W tensor T are the preceding triple plus one additional 3. Its clock-trivial part has dimension four. Hence the dimension-eight first layer contains either two orbits and no clock-trivial part, or one orbit and all four clock-trivial dimensions.

In the two-orbit case, self-duality of the two removed orbits leaves exactly the following possibilities. The displayed vectors are source (O_c+0) tensor Lambda^2 W and target (gr_1 P) tensor W at first coordinate one:

    c=0, first O_2+O_3: (4,1,0,0,1) versus (3,1,0,0,2)
    c=1, first O_1+O_3: (2,1,1,0,2) versus (2,1,1,1,1)
    c=2, first O_0+O_3: (1,1,1,3,0) versus (2,0,2,1,1)
    c=3, first O_4+O_3: (1,0,3,1,1) versus (2,1,0,1,2)
    c=4, first O_3+O_3: (2,2,0,1,1) versus (4,0,0,0,2).

Every row has a positive target-minus-source difference, contradicting q=2.

In the one-orbit case all twelve relations are orbit constituents. A self-dual triple can only be removed from the four available slopes when c=2: remove O_0+O_4+O_1 and retain O_3. The first layer is then O_3 plus four zero weights. Its source and target vectors are

    (1,1,1,3,0) versus (2,0,0,4,1).

Again a positive difference forces an orbit in the quadratic cokernel. This completes the top-five exclusion.

## Conclusion and scope

Every top dimension is excluded, including the new top-five configurations and all extra terminal-layer possibilities. Therefore local length fifteen is impossible. Together with the audited exclusions through fourteen, the unrestricted local bound is sixteen, giving 480 on the canonical thirty-point orbit, conditional on the established support hypotheses.

All reasoning concerns universal abstract local algebra and finite-group representations. The small displayed weight tables are direct finite sums of the stated weight multisets and can be checked entry by entry; no search over module coefficients is used. No physical source/model, actual matrix instance, operation, chosen input, rank instance, jet, residue, or detector was evaluated. No external write, installation, or large computation occurred.

Audit status: independently reviewed and passed after correcting the top-two terminal case; see AUDIT.md.
