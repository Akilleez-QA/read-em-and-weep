Publication context: this retained proof or audit may describe an intermediate bound or then-open branch. Read the unit overview for the current scope and later implications. Historical mathematical review is not a new formal verification.

# Length ten: an explicit boundary of the universal Betti obstruction

## Result and scope

The assertion that every equivariant finite module of length ten satisfies

    beta3(Q) - 2 beta4(Q) >= 3

is false. There is a universal square-zero module of length ten for which this expression is exactly two. Its construction is equivariant for the entire linear group of the four-dimensional cotangent space, and hence also for the order-twenty subgroup and the full linearized stabilizer. Thus imposing the larger stabilizer does not remove this counterexample.

This is an abstract local-algebra counterexample to a proposed blanket Betti strategy. It is not a construction of a rank-two reflexive module M with Q=Ext²(M,R), and it establishes no actual defect, source-model realization, rank instance, or operation evaluation. In particular, the audited global lower bound 300 remains unchanged; total 300 is neither excluded nor realized here.

## 1. Universal module

Let W be a four-dimensional complex vector space and R=C[[W]] the completed symmetric algebra, with maximal ideal m. Define the underlying vector space

    P = W direct-sum Lambda²W.

For x in W, define multiplication by x on P by

    x.v = x wedge v        for v in W,
    x.s = 0               for s in Lambda²W.

All composites of two parameters are zero, so the operators commute. This defines an R-module with m²P=0. Since decomposable two-vectors span Lambda²W,

    mP=Lambda²W,  P/mP=W,  length(P)=4+6=10.

The construction is natural under every linear automorphism of W. In particular it is equivariant under any finite group acting linearly on W. The common parameter kernel on its top W is zero: for every nonzero v there is x not proportional to v and x wedge v is nonzero. Thus the socle of P is exactly Lambda²W.

For the subgroup G=C5 semidirect C4 with W=V, the exterior square has representation type V plus two one-dimensional characters. Indeed the opposite-index wedges span a two-dimensional clock-trivial subspace, and the other four wedges have the four distinct nonzero clock weights and form V. Therefore P has representation type 2V plus two characters, exactly an allowed length-ten type.

For an initially nonlinear finite stabilizer action on a regular local ring, passage to completion and averaging an equivariant section of m/m² give equivariant linear parameters. Consequently the construction applies to that formal local setting as well. Completion is all that is needed for this counterexample to a universal local Betti assertion.

## 2. The degree-two Koszul map is an isomorphism

The Koszul complex of P with respect to W has terms P tensor Lambda^i W. Multiplication kills the bottom Lambda²W, so each nonzero differential is the map

    d_i: W tensor Lambda^i W -> Lambda²W tensor Lambda^(i-1)W.

Clearly rank(d_1)=6. We prove rank(d_2)=24, its full dimension, without a numerical computation.

On elementary tensors,

    d_2(v tensor (a wedge b))
       = (a wedge v) tensor b - (b wedge v) tensor a.

Flip the two output tensor factors, identifying the target with W tensor Lambda²W. Let

    A: W tensor Lambda²W -> Lambda³W,
    A(v tensor (a wedge b)) = v wedge a wedge b,

and let the alternating inclusion J be

    J(u wedge v wedge w)
       = u tensor (v wedge w) - v tensor (u wedge w)
         + w tensor (u wedge v).

Then AJ=3 times the identity, and the flipped d_2 is exactly

    I - JA.

The direct sum W tensor Lambda²W = ker(A) direct-sum im(J) has dimensions twenty and four. The operator I-JA acts as +1 on ker(A) and -2 on im(J), hence is invertible over C. This proves rank(d_2)=24.

## 3. Betti numbers needed for the obstruction

Minimal Betti numbers over R equal dimensions of Koszul homology. The degree-one Koszul term has dimension 10 times 4=40. Therefore

    beta0(P) = 4,
    beta1(P) = 40 - rank(d_1) - rank(d_2)
             = 40 - 6 - 24 = 10.

Take the finite local dual

    Q = D(P) = Ext⁴_R(P,R).

Finite-length duality preserves length and reverses the minimal Betti sequence. It is equivariant with the usual one-dimensional duality twist; this twist does not alter dimensions or the claimed representation type. Thus

    length(Q)=10,
    beta4(Q)=beta0(P)=4,
    beta3(Q)=beta1(P)=10,
    beta3(Q)-2 beta4(Q)=2.

Equivalently, the underlying vector-space dual of P (up to the duality character) has top of dimension six and bottom/socle of dimension four, with square-zero radical. Its top representation is V plus two characters and its bottom is V. This pinpoints the new length-ten square-zero shape (6,4) that defeats the lower-length bounds.

The previously audited necessary defect inequality beta3(Q)-2 beta4(Q)<=2 holds with equality for this Q. Neither that numerical inequality alone nor merely requiring the finite module to admit the full stabilizer action can exclude this module. Additional representation-theoretic constraints arising from Ext² realizability are not covered by this statement.

## 4. Additional rigorous family exclusions

These observations remain useful for any more refined length-ten analysis, but they do not imply a blanket exclusion.

### 4.1 Non-square-zero modules with socle dimension at least four

Let Q have length ten, m²Q nonzero, and socle dimension s>=4. Put P=D(Q), and let h1=dim(mP/m²P). Duality preserves the nonzero m² action, so

    h1 <= 10-s-1 = 9-s.

The minimal presentation of P has at least 4s-h1 independent linear relations: the map from mR^s/m²R^s to mP/m²P is surjective and its kernel has that dimension. These independent linear initial forms give independent minimal relations. Hence

    beta3(Q)-2 beta4(Q)
       = beta1(P)-2s >= 2s-h1 >= 3s-9 >= 3.

This family is excluded by the necessary defect inequality. The counterexample in Sections 1–3 avoids the argument because it is square-zero.

### 4.2 Four nonzero radical layers in type 2V plus two characters

There are only four irreducible constituents counted with multiplicity, so four nonzero radical layers each contain one constituent. Two consecutive character-only layers are impossible. A consecutive pattern (V, character, V) is also impossible: W tensor V -> character is a perfect equivariant pairing, while W tensor character -> V is an isomorphism. For a weight vector paired nontrivially with x_j, multiplication by a distinct x_i before x_j gives zero, while multiplication by x_j before x_i is nonzero. This contradicts commutativity in the associated graded module.

Consequently the only possible four-layer shape is

    (1,4,4,1).

It is cyclic. At each nonfinal layer, the common multiplication kernel is an invariant proper subspace of an irreducible representation, hence zero. Therefore its actual socle is the last character. The cyclic module is Artin Gorenstein, so its finite dual is cyclic and isomorphic to it as an underlying R-module. Its embedding dimension is four, and its degree-two radical layer has dimension four; its defining ideal consequently has at least 10-4=6 independent minimal quadratic initial relations. Thus beta3=beta1>=6 and beta4=1, giving beta3-2 beta4>=4. This argument does not assume that the filtered algebra is graded.

## Dependencies and stopping boundary

The necessary Ext²-defect inequality and Betti reversal are the audited inputs recalled in length-nine-local-defect/PROOF.md and length-eight-local-defect/PROOF.md. The current global boundary is rank-eight-defect-300/COROLLARY.md. The exterior-algebra construction and the invertibility argument above are new and self-contained.

No source application or upstream file was changed, no software was installed, and no large computation was performed. The counterexample settles the proposed blanket length-ten Betti claim negatively. Any actual exclusion of local length ten must use additional realizability information beyond the listed numerical inequality and abstract stabilizer equivariance, or otherwise exclude the explicit module above as an Ext² defect.
