# Independent audit: C5-equivariant local length-25 model

## Verdict

PASS as a countermodel to an inference from the explicitly retained local data. The actual stabilizer representations, rank-nine residue, exact forced square-kernel line, vanishing normalized derivative on that line, isolated reduced rank-nine degeneracy scheme, and auxiliary complete intersection of orders (1,1,5,5) are compatible with auxiliary length exactly 25.

This does not supply a counterexample under all the original operation hypotheses. Fixed-frame linearity, realization by one cyclic outer-symmetric trilinear operation, repeated-input injectivity, and full-normalizer realization have not been established. Those omissions are essential to how the conclusion may be used. In particular, this model does not determine the actual rank or multiplicity at any point of M600.

## 1. The actual restricted characters

The order-five classification identifies a nonzero-cocycle stabilizer generator as a monomial five-cycle on the five-dimensional Schrödinger representation. Such a matrix has characteristic polynomial t^5-c with c nonzero. After order-five normalization its eigenvalues are all five fifth roots, each once. Further shifting the normalization so the chosen point eigenline has eigenvalue one leaves this regular representation unchanged.

With that convention the point has affine tangent eigenvalues zeta, zeta^2, zeta^3, zeta^4. The source bundle fiber is the point line tensored with Sym²V. Its point-line factor is trivial after normalization. The unordered pairs of five character labels have each sum modulo five exactly three times, so Sym²V=3Reg. Equivalently its character is fifteen at identity and zero at each nonidentity power.

The target argument is valid without a choice of actual operation coefficients. The established representation identities are Lambda²V=A tensor W_h and J=A* tensor Sym³W_h. For a nonidentity power g^r, both g^r and g^(2r) have trace zero on V, so

    trace(Lambda²V)(g^r) = (trace(V)(g^r)^2 - trace(V)(g^(2r)))/2 = 0.

The two eigenvalues of W_h at that power are fifth roots; their sum cannot be zero, since their quotient cannot be -1. Consequently trace(A)(g^r)=0 for all four nonidentity elements. Dimension five then gives A=Reg. Tensoring a regular representation with any four-dimensional representation gives four regular representations. Therefore J=4Reg. Scalar normalization changes labels but not these uniform multiplicities.

These calculations use only the imported representation identities and the universal stabilizer action, not the source matrix at the chosen point.

## 2. Equivariance convention and fiber splitting

In the proof, x_i -> zeta^i x_i describes the action on affine points. With fiber bases e_j of weight j, S_i(e_j)=e_(j+i) satisfies

    g S_i g^-1 = zeta^i S_i.

Thus the displayed matrix obeys the bundle-map covariance equation D(gx)=g_C D(x)g_K^-1. This is correct. If one instead uses the usual left action on the coordinate ring by inverse pullback, x_i has weight -i; these two descriptions must not be mixed.

The image module A9 has character multiplicities (1,2,2,2,2). The proposed source has multiplicities

    A9 + Reg + 1 = (3,3,3,3,3),

and the target has multiplicities

    A9 + 2Reg + 1 = (4,4,4,4,4).

Hence they are equivariantly isomorphic to the actual source and target fibers. The distinguished trivial source summand can be identified with u² because u² is a nonzero vector in the three-dimensional trivial-character source space. The source O(-1) factor is trivial on this normalized invariant chart; intrinsically the forced line is O(-1) tensor O(-2)=O(-3), and its fiber character is likewise trivial here.

The residue map is identity on A9 and zero on its six-dimensional complement, so its rank is exactly nine and its kernel/cokernel are precisely those claimed.

## 3. Determinantal calculation

For the block map diag(I9,D,0), elimination identifies I10(B) with I1(D). Each individual x_i occurs as an entry: the cyclic-shift supports in either five-row block are disjoint. Thus I10(B)=m exactly, not merely after taking radicals. The completed or ordinary local rank-at-most-nine scheme is the reduced origin and has length one.

Either five-row block is invertible on a nonempty open set, so D has generic column rank five, and B has generic rank fourteen. The permanent zero column excludes rank fifteen.

Adding the full identity block to a chosen entry of D makes that entry a ten-minor, up to sign. Adding it to either whole five-row block gives the stated fourteen-minor. Therefore f=x2 and g=x4 are permissible ten-minors, while h and k are permissible fourteen-minors.

After quotienting by x2,x4, the latter minors are respectively det(S1)x1^5 and det(S3)x3^5. Both permutations are five-cycles, so their determinant is +1. The quotient is exactly

    C[x1,x3]_(x1,x3)/(x1^5,x3^5).

Its basis consists of x1^a x3^b for 0<=a,b<=4, proving length 25. Its four defining elements form a parameter system in a regular local ring of dimension four and hence a regular sequence. Each determinant is homogeneous of degree five with a nonzero pure-power coefficient, so its order is exactly five; the other two orders are one.

The determinants are invariant under the covariance equation because conjugation has determinant ratio one; x2 and x4 are semi-invariants. The parameter ideal is therefore C5-stable. There is no hidden character-divisibility obstruction to this length.

## 4. Moving square and normalized derivative

The universal cyclic and outer-symmetric identities give f(u,u,u)=0 and f(u,v,u)=-2f(u,u,v). Hence the derivative of the actual middle map on u² lands in its original image. This is precisely the assertion that its induced derivative K -> C kills that line, with no statement about the other five kernel directions.

For the model, set P(x)u=u+x and P(x)|T=Id. It is invertible and P(gx)=gP(x)g^-1. After identifying the distinguished source line with u², replace B(x) by

    B(x) composed with Sym²P(x)^-1.

The resulting equivariant map annihilates (u+x)² identically. The extra O(-1) chart factor is understood as above. Right multiplication by an invertible matrix preserves all determinantal ideals. At the origin P=Id; the extra first derivative term factors through B(0), so it vanishes in the cokernel. Thus the normalized derivative is unchanged under its natural identification.

This frame change generally introduces higher-degree entries. No fixed-frame globally linear cyclic realization follows from it.

## 5. Exact logical scope

The model proves that the listed local representation, moving-kernel and reduced-support conditions alone cannot universally force an auxiliary contribution greater than 25 at M600. It also proves that auxiliary complete-intersection length and determinantal-scheme length are distinct quantities: here they are 25 and 1.

It does not rule out stronger bounds from the simultaneous fixed-frame linearity and cyclic identities, restrictions on the image of the first derivative, higher-order compatibility, global interpolation, or full-normalizer structure. Nor does it assert that the particular local minor choices are restrictions of the already chosen global complete intersection. Those additional issues are outside the proposed countermodel and cannot be silently imported into it.

The independent check involved only static proof reads and symbolic abstract algebra. No actual source operation, selected rank instance, source jet, external write or large computation was used.
