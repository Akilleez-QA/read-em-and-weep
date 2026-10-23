# The P source cannot occur in the maximal rank-three profile (1,1)

## Theorem, hypotheses and scope

Work over C on the physical binary-icosahedral parameter line with the actual saturated primary bundle E in the constant thirty-dimensional ambient bundle, its actual quotient Q, and the maximal rank-three Gauss-plateau convention of the pinned actual-splitting theorem. Assume all hypotheses of the original profile(1,1) necessity theorem, including its actual-source and transpose inputs. Then the actual source

    E=P O(-2)+(W'+T)O(-3)+V O(-4)+W'O(-5)

cannot have maximal rank-three profile (k,l)=(1,1).

This is a source-conditioned profile exclusion. It does not exclude the other primary source types, assert global profile(1,1) closure, exclude this source in every other profile, or complete the original proof repair. The proof imports the pinned original159-record necessity theorem as a mathematical prerequisite. The checker does not re-prove its global transfer dependencies or regenerate its classification.

The new deduction combines a complete fixed P-conditioned partition with a dual endpoint-capacity contradiction for its last eleven records. Historical labels identify fixed necessary records only: no claim that these eleven records were all still live, or newly removed against every later theorem, is made.

## 1. Immutable sources and exact P compatibility

INPUTS.json authenticates complete public originals by commit, path, Git blob identity, byte count and SHA256. The inputs are:

- Original actual-splitting theorem, actual Gauss embedding, strict-top supporting lemma and159-record necessity theorem/list at db51525015bb7c5e825833d550d08dedf6f6ea96.
- Four-source theorem PR1123 at504b7eb800407dfc7e6340c98c72cdd553939f54.
- Cubic visibility PR1140 at7a2488bcd36d95f79b5198001111b1a31fe5c3ba.
- P-conditioned frozen-list certificate PR1155 at076d2fb4e6abec42bd365bb32318b89d8ece400f.
- All-source doublet endpoint exclusions PR1156 at69d4f410bcacab23ab4704ac20ec80e34fcc179b.
- All-source rank-one-flag exclusions PR1159 atb6c3581c1a6df25ea72a776f9d6cf2082bd73461.

The P source has rank17, degree−54 and original source tuple (1,1,1,0,1,0,0,0). Put K=E^-, A=E/K, S=Q*, L=S^-, B=S/L. The original necessity theorem says that the ordered pair (A,B) of any actual profile(1,1) is among the fixed159 records. Both quotients have rank3. The actual quotient E→A and transpose injection B→E*(-2) give, for each integer u from−10 through10,

    H1(A(u)) <= H1(E(u)),
    H0(B(u)) <= H1(E(-u)).

The first follows from the long exact cohomology sequence and H2=0. The second follows by twisting the injection, taking H0, and equivariant Serre duality; all irreducibles are self-dual. Inequalities mean coefficientwise nonnegative multiplicities. Only necessity is asserted. A finite twist range is not sufficient for actual realization.

The verifier recomputes these inequalities on each fixed record and checks exact agreement with membership of the P tuple in every original compatible_E_types field. This gives exactly35 records:

    42,43,53,62,63,64,65,66,67,73,74,76,86,87,88,89,96,102,
    103,109,110,111,116,130,132,134,141,142,143,144,145,148,149,150,151.

The other124 records cannot represent this actual source. Their explicit failed inequalities and twists are retained in RESULT.json. No candidates or source instances are generated.

## 2. Disjoint coverage by earlier actual exclusions

PR1140 requires W'+2T to inject into H0(A(3)) for every actual source. It excludes precisely the following16 P-compatible records, by a negative multiplicity in H0(A(3))−(W'+2T):

    42,43,53,62,63,64,65,66,67,73,74,76,102,103,110,111.

This is a coefficient-space injection, not a fiberwise rank14 statement. The exact negative multiplicities are retained. We do not count overlapping quartic criteria as further removals.

Among the remaining19 records, PR1156 excludes A=W'O(-1)+O4 at86,87,88,89,96 and A=W'O(-1)+O10 at116. Its all-source theorem applies to profile(1,1), independently of B and determinant defect.

PR1159 excludes A=W'O(-5)+O16 at109 and A=W'O(-3)+O16 at134. Its theorem holds whenever the lower plateau length is k=1, hence here; its complete rank-one-flag Euler contradiction is an explicit imported proof, not merely a claimed test result.

Thus16+6+2=24 of the35 are covered by these three nonoverlapping groups. The remaining11 fixed records are

    130,132,141,142,143,144,145,148,149,150,151.

The verifier checks each target shape, every index, disjointness, and equality of the union with the complete35-member P-compatible subset after the capacity group below is included.

## 3. Dual endpoint capacity, with actual saturation and termination

The original actual-splitting theorem gives rank S=13, deg S=−54, and no constant subbundle in S=Q*. As a subbundle of a constant bundle, every ordinary degree of S is therefore at most−1. The dual reversed plateau has S as its central bundle. When l=1, L=S^- is its lower endpoint; the maximal-plateau convention gives rank beta_L at most2. Also rank L=10 and deg L=−54−deg B. No rank-three interior-quotient assertion is imposed on this endpoint.

Define F0=S, F1=L and F(j+1)=ker beta_(Fj). Each kernel is saturated in its source: its quotient is the torsion-free coherent derivative image on the smooth curve, hence locally free. Since its source is saturated in the constant ambient, the kernel is saturated in that ambient too. All F(j) for j>=1 have only negative ordinary degrees, because they are subbundles of S.

A nonzero negative saturated subbundle of a constant bundle cannot have zero second fundamental form. Indeed zero derivative makes the associated Grassmannian map constant over C; saturation then identifies the subbundle with a constant subspace tensored with O, contradicting negativity. Consequently each nonzero F(j) loses positive rank at the next kernel step, and the sequence terminates at zero after finitely many steps. No positive-rank horizontal remainder is omitted.

Write G(j)=F(j)/F(j+1), with G(0)=B. For j>=1 the actual derivative of F(j) lands in (F(j−1)/F(j))(-2): its projection outside F(j−1) vanishes because F(j) is the kernel of that preceding derivative. It induces a sheaf injection

    G(j) -> G(j−1)(-2) -> ... -> B(-2j).

These are injections of locally free sheaves, not presumed saturated images. If q_j=rank G(j), then 2>=q_1>=q_2>=...>=1 until termination, and sum q_j=rank L=10. Let h1 be the number of nonzero q_j and h2 the number equal to2. Then h1>=h2>=0, h1+h2=10, so h1 ranges from5 through10.

Let the ordinary degrees of B be lambda1>=lambda2>=lambda3. Taking exterior powers of G(j)→B(-2j) gives a nonzero morphism from det G(j) to a direct sum of line bundles. Therefore

    deg G(j) <= sum_(i=1)^q_j lambda_i − 2j q_j.

This determinant bound does not require image saturation, equivariant splitting compatible with differentiation, or knowledge of the actual map. Additivity in the finite saturated flag yields

    deg L <= h1 lambda1 − h1(h1+1)
             + h2 lambda2 − h2(h2+1).

In particular, if lambda1<=−1, then

    deg L <= max_(h1+h2=10, h1>=h2>=0)
               [−h1−h1(h1+1)−h2−h2(h2+1)] = −70.

The maximum occurs at h1=h2=5. This simple uniform bound already suffices below. The exact stronger per-record maxima are included as reproducible evidence.

## 4. The last eleven records contradict dual capacity

All eleven B bundles have negative top ordinary degree. The entries below are read from the immutable list; degrees repeat with the dimension of each coefficient representation. Capacity is the exact maximum from Section3 over all six allowed height pairs.

| Original index | Ordinary B degrees, descending | deg L | Capacity | Positive gap deg L−capacity |
|---:|---|---:|---:|---:|
|130|−4,−6,−6|−38|−110|72|
|132|−5,−5,−6|−38|−110|72|
|141|−4,−6,−8|−36|−110|74|
|142|−5,−5,−8|−36|−110|74|
|143|−4,−7,−7|−36|−114|78|
|144|−1,−1,−16|−36|−70|34|
|145|−6,−6,−6|−36|−120|84|
|148|−6,−6,−8|−34|−120|86|
|149|−6,−7,−7|−34|−125|91|
|150|−1,−1,−18|−34|−70|36|
|151|−6,−7,−7|−34|−125|91|

In particular the negative doublet W'O(-1) in records144 and150 is not an exception: its two ordinary degrees are both−1, and capacity is still−70. All deg L values exceed even that uniform upper bound. Every one of the last eleven records is therefore impossible.

The four disjoint groups have sizes16,6,2,11 and union all35 P-compatible records. Since the original necessity theorem covers every actual profile(1,1) and actual P compatibility is necessary, no actual P-source profile(1,1) remains. This concludes the stated source-conditioned theorem only.

## Reproducibility and limits

Run python3 verify.py and compare stdout with RESULT.json. Running python3 -O verify.py must give byte-identical output. The checker authenticates eleven immutable inputs, checks exact source rank/degree and representation dimensions, recomputes all159 source-compatibility decisions, records failed-twist witnesses, verifies the full partition, and evaluates all six capacities for each final record both by the height formula and by summing the corresponding quotient-rank bounds. Checks use explicit exceptions, not optimization-removable assertions.

The saturation, maximal-endpoint, original necessity and cited exclusion arguments are written mathematical inputs, not consequences of arithmetic alone. This is not proof-assistant verification. No actual source coefficient, parameter, point, jet, tensor, instance matrix, actual rank experiment, historical-list regeneration, stopped local-model spike or consumed experiment is run. No live-frontier percentage or global completion claim follows.
