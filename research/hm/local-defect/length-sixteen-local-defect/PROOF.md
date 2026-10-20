Publication context: this retained proof or audit may describe an intermediate bound or then-open branch. Read the unit overview for the current scope and later implications. Historical mathematical review is not a new formal verification.

# Length sixteen: a single exact homogeneous residual family

## Status and statement

This is a structural reduction, **not an exclusion of length sixteen**. Under the canonical hypotheses of the independently audited length-fifteen proof, every length-sixteen finite-dual defect P, if one exists, has Hilbert function

    (h0,h1,h2,h3) = (4,6,4,2).

Its B-weight layers are necessarily

    T = O0,
    gr1 P = O2 + {(0,2),(0,-2)},
    gr2 P = O1,
    gr3 P = {(0,1),(0,-1)}.

Moreover P has an exact homogeneous linear presentation: its ten minimal relations are its linear initial relations. Thus there are no higher filtered corrections in this residual case. A concrete description of those relations appears in Section 5.

The unrestricted lower bound remains sixteen, and the conditional thirty-point contribution remains 480. The cyclic lower bound remains 31. No existence or isolated reflexive realization of the residual family is asserted.

## Inputs and notation

We use precisely the hypotheses, notation, representation tables, and audited estimates of ../length-fifteen-local-defect/PROOF.md and AUDIT.md, together with ../length-fourteen-local-defect/PROOF.md, ../representation-defect-bound/PROOF.md, and ../cyclic-defect-further-bound/PROOF.md. In particular W=O3, O_c={(i,c i^2):i in F5*}, and negation sends O_c to O_{-c}. All other constituents are clock-trivial: characters of B-weight zero, or two-dimensional pairs {(0,b),(0,-b)}.

For T=P/mP, s=dim T, K1 the linear initial relation space, k=4s-h1, and q the dimension of the homogeneous quadratic quotient by K1, the estimates are

    beta1 + a_B(Tor1(P,k)) <= 2s+2,
    beta1 >= k + max(0,q-h2),
    q >= 4h1-6s.

If beta1=k, then K1 is the minimal relation representation and q=h2. When also k=2s+2, the imbalance budget is zero, so K1 is B-self-dual. The homogeneous quotient by K1 surjects onto gr P. Completion and equivariant coordinates/top lifts are allowed.

The cyclic bound excludes s=1, and the square-zero bound excludes m²P=0. Therefore h2>=1. From h1>=2s-2 and s+h1+h2<=16 we obtain 2<=s<=5.

## 1. Top dimension two

The first layer is divisible by four. If h1>=8, the estimates give

    beta1 >= (8-h1)+(4h1-12)-(14-h1) = 4h1-18 >=14>6.

Thus h1=4, k=4. The audited imbalance argument forces T to have weights (0,±2), K1=O0, and gr1 P=O1. The homogeneous linear quotient N is two planes: the top of weight (0,-2) uses x1,x4, and the top of weight (0,2) uses x2,x3. Its quadratic piece is O1+(0,±1), and its cubic piece is O2+O3, with no clock-trivial weights.

There are at most three orbit constituents, since the top already has dimension two. As in the audited preceding proofs, one orbit gives length at most eight. Two orbits cannot be separated by a clock-trivial quadratic layer: such separation requires at least four clock-trivial dimensions, while N2 has only two. With the second orbit in degree two and no third orbit, degree three vanishes, so length is at most twelve.

With three orbits, the second is in degree two and the third in degree three. The quadratic layer is either O1 or O1+(0,±1). These give exactly the following length-sixteen possibilities:

    (2,4,6,4),
    (2,4,4,4,2).

For the second shape, the quartic layer consists of two zero weights. Indeed every quartic in either twisted plane has second coordinate zero; its nonzero-clock constituents have dimension four, too large to fit. There cannot instead be two consecutive one-dimensional clock-trivial layers, since multiplication of a clock-trivial layer by W has no clock-trivial quotient.

In both shapes, no O0 weight occurs in any layer of P. Thus the four linear O0 relations are exact, and we may pass to the actual two-plane module N.

For (2,4,6,4), the kernel J of N→P has no initial terms below degree three, while its cubic initial space has dimension 8-4=4. Consequently dim J/mJ>=4. These supply at least four additional minimal relations beyond the four exact linear relations, contradicting beta1<=6. The additivity here follows also directly from orders: the eliminated relations have independent degree-one initials, and m times the remaining kernel starts in degree four.

For (2,4,4,4,2), the opposite quadratic monomials have weights (0,±1), absent from both the cubic and quartic layers. They are exact relations and supply two independent additional minimal classes. These exhaust beta1<=6. Their quotient is two twisted copies of C[[x,y]]/(xy), of infinite length. Contradiction.

## 2. Top dimension three

Here h1 is divisible by four. If h1>=8, the estimates give

    beta1 >= (12-h1)+(4h1-18)-(13-h1) =4h1-19>=13>8.

Hence h1=4 and k=8=beta1. The audited length-independent top-three calculation forces T to have weights 0,(0,±1), K1=O3+O2, first layer O4, and q=h2=6. Its homogeneous linear quotient is a residue-field summand plus two planes whose cubic piece has no clock-trivial weights. The prefix has length thirteen, leaving only three dimensions. A nonzero cubic layer would have to be clock-trivial, impossible. Thus s=3 is excluded.

## 3. Top dimension five

Here h1>=8. For h1>=9, the estimates give

    beta1 >= (20-h1)+(4h1-30)-(11-h1) =4h1-21>=15>12.

Thus h1=8, k=12=beta1, K1 is B-self-dual, and q=h2<=3. The complete top-five enumeration in Section 4 of the audited length-fifteen proof is length-independent once these facts hold. Its hypotheses are exactly: top dimension five, first dimension eight, and self-dual K1 of dimension twelve. Every possible clock-trivial top or top O_c plus a character has a positive target-minus-source multiplicity at a nonzero-clock weight in the quadratic Koszul map. Hence each forces q>=4. This contradicts q<=3 and excludes s=5. The old proof used q=2; here only its stronger orbit obstruction is imported.

## 4. Top dimension four

For h1>=8, the estimates give

    beta1 >= (16-h1)+(4h1-24)-(12-h1) =4h1-20>=12>10.

Thus h1 is six or seven. A clock-trivial top would force h1 divisible by four, so T=O_c.

For h1=7, exactly the audited argument applies: the three retained clock-trivial dimensions force c=2; k=9 leaves at most one further minimal relation, which cannot repair an orbit imbalance. Thus K1 has orbit part O4+O1 and gr1 P=O0+3·0. The quadratic Koszul source and target at first coordinate one have vectors (0,1,1,3,0) and (0,0,2,4,0). They force q>=8. Since h2<=5, beta1>=9+8-5=12>10.

Consequently h1=6 and k=10=beta1, with K1 B-self-dual and q=h2<=6. The five candidate pairs in the audited length-fourteen table apply. Three force q>=8 and are excluded. The remaining possibilities are

    A: T=O0, gr1 P=O2+(0,±2), K1=O2+O3+(0,±2);
    B: T=O2, gr1 P=O0+2·0, K1=O1+O4+2·0.

In each case q contains its forced orbit (O1 in A, O2 in B), and no second orbit fits. In A all clock-trivial weights of W⊗gr1 P are zero. In B they are (0,±3), so any retained clock-trivial contribution has even dimension. Thus

    A: h2=4,5,or6, with gr2 P=O1 plus zero weights;
    B: h2=4 or6, with gr2 P=O2, possibly plus (0,±2).

### Case A with h2=5 or6

If h2=5, the remaining dimension is one, necessarily gr3 P of weight zero. But every cubic in the full free module on O0 has nonzero second coordinate: sums of three numbers ±2 are never zero modulo five. This excludes h2=5.

If h2=6, the shape is (4,6,6), and gr2 P=O1+2·0. Its weights are disjoint from K1, so all ten linear initial relations are exact. They exhaust the minimal relation budget and generate the entire kernel. Set x2=x3=0 in this homogeneous presentation. As in Section 6 of the audited length-fourteen proof, at most five linear relations remain among four generators over C[[x1,x4]]. Its degree-three piece has dimension at least 4·4-5·3=1, contradicting m³P=0.

### Case B

For h2=6 the shape is (4,6,6). The quadratic weights O2+(0,±2) are disjoint from K1, so again all ten relations are exact and generate the kernel. The polynomial-line quotient of Section 5 of the audited length-fourteen proof applies: set x2=x3=x4=0 and t2=t3=t4=0. Every linear relation vanishes, leaving a free C[[x1]] generator t1. Infinite length is impossible.

For h2=4, exactly two dimensions remain after the prefix. A third layer must therefore be clock-trivial and a quotient of W⊗O2; its clock-trivial weights are zero. On the other hand, the homogeneous linear quotient in case B is generated by monomials in x_j,x_{-j} on each top t_j. Every such cubic has second coordinate 2j²+9j²=j², which is nonzero. Hence its cubic piece has no zero weight, and neither can gr3 P. This contradiction excludes B entirely.

### Case A with h2=4

Exactly two dimensions remain. Since W⊗O1 has clock-trivial weights (0,±1) only, its nonzero clock-trivial quotient of dimension at most two is the complete pair. Thus necessarily gr3 P=(0,±1), h3=2, and no higher layer occurs.

Now all higher-layer weights O1 and (0,±1) are disjoint from K1=O2+O3+(0,±2). Equivariant top lifts therefore make every linear initial relation exact. Their ten independent classes exhaust beta1=10, so these exact homogeneous linear relations generate the full kernel. This proves the stated reduction, including the filtered assertion.

## 5. Explicit residual presentation and open point

Let x_i have weight (i,3i²) and t_j have weight (j,0), for i,j in F5*. The only remaining presentation has four top generators t_j and the following ten homogeneous linear relations:

- four monomial relations x_i t_{3i}=0;
- for each i, one nonzero linear relation in the two-dimensional weight space spanned by x_i t_i and x_{-i}t_{3i};
- one nonzero linear relation in span{x1t4,x4t1}, and one in span{x2t3,x3t2}.

The entire relation space must be H-stable; the coefficients are not assumed arbitrary independently of that requirement. The displayed two-term relations allow a zero coefficient. This is precisely the audited A family, now forced to be exact and to have Hilbert function (4,6,4,2).

The remaining question is whether this homogeneous H-equivariant family is itself impossible under the full canonical defect hypotheses, or whether some members pass these necessary local tests and need an additional realization obstruction. The present proof does not settle that question. In particular, the older two-variable cubic count gives a nonzero cubic layer and is compatible with the residual Hilbert function; it cannot be reused to claim an exclusion.

## Scope

This proof uses only universal abstract local algebra and finite-group weight arithmetic. No physical source/model, actual matrix instance, operation, chosen input, rank instance, jet, residue, or detector was evaluated.  The only writes are local proof artifacts. Independently audited: PASS; see AUDIT.md. The separate CANDIDATE.md gives a symbolic abstract-module construction, with its own audit status; it does not establish isolated-defect realizability.
