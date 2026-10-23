# The remaining four actual profile-(2,1) shapes are impossible

## 1. Statement, exact source and imported reductions

Work over C on the same physical binary-icosahedral parameter line and in the original actual constant ambient bundle. Suppose the actual second fundamental form of E has generic rank three and its maximal rank-three plateau has profile (k,l)=(2,1). Write

    0 -> E -> H O -> Q -> 0,
    S=Q* inside H* O, L=S^-, B=S/L.

The actual identities give rank S=13, deg S=-54 and top S<=-2; the last bound follows from k=2 by the section-persistence theorem. Since l=1, L is the dual endpoint: rank L=10 and its own generic derivative rank is at most two. It is not a rank-three interior stage.

The original thirteen-pair theorem is a geometrical necessary overlist, not a realization assertion. The direct primary profile reduction excludes its original indices 0,1,8,11,12 and forces the exact same actual source on every other row:

    E=D O(-2)+(W'+T)O(-3)+V O(-4)+O(-8).        (1)

The separately proved cubic rigidity theorem excludes indices 3,4,6,7, including both original determinant defects. Thus only these four original indices require a new argument here:

    2: A=O(-8)+O(2)+O(16), B=O(6)+O(-4)+O(-18);
    5: A=O(-8)+O(4)+O(16), B=O(6)+O(-6)+O(-18);
    9: A=O(-8)+O(6)+O(16), B=O(6)+O(-8)+O(-18);
   10: A=O(-8)+W' O(9),   B=O(6)+W' O(-11).

All four have original transpose defect zero. We prove that none is possible. Consequently the actual maximal profile (2,1) is excluded, conditional only on the explicitly pinned actual hypotheses and preceding direct reductions, not on the later 182-to-23 or same-source ledger.

The complete public prerequisites are pinned in INPUTS.json: the direct reduction is PR1134 at 7cb2e260b2bcbac15df89612b6a2096263a9c89c, and cubic rigidity is PR1135 at 24e713fe352f4ff8f70cd2e86940afa70df99c5c. Their downloaded proof bytes are identical to the independently reviewed packets. Ten immutable inputs also include the actual ambient/source and strict-top originals, the original thirteen-pair theorem and row identities, and the earlier equality/intersection proofs at 3349988b5c3fc82dbca0741fc1b5fe70af1c7d0d and 2348d4b6fb2afd67d66b15aad6037ab92c94f076.

The new proof uses no second primal determinant defect, no selected source coefficients and no horizontal Birkhoff splitting. Its capacity and equality arguments re-establish the relevant narrow steps of the earlier degree-envelope and rational-normal-subbundle methods, rather than assuming their retained-label coverage.

## 2. A finite endpoint degree-capacity bound

Set F_0=S, F_1=L and F_(j+1)=F_j^- for j>=1, with saturation in the original constant ambient. Put G_j=F_j/F_(j+1), q_j=rank G_j for j>=1, and G_0=B.

Differentiation of F_j stays in F_(j-1). Its induced map therefore gives an injection of locally free sheaves

    G_j -> G_(j-1)(-2) -> ... -> B(-2j).       (2)

This remains an injection across ramification: it is the quotient by the actual sheaf kernel, not an asserted saturated image. It implies q_(j+1)<=q_j. Since L is the endpoint, q_1<=2.

All F_j are saturated negative subbundles of the constant ambient. A nonzero F_j cannot be horizontal: a horizontal saturated subbundle of a trivial bundle with its constant connection on P1 over C is a constant subspace bundle, of degree zero. Thus whenever F_j is nonzero its derivative rank is positive, so rank F_(j+1)<rank F_j. The chain terminates in zero in at most ten steps. Degree and rank additivity consequently give

    sum_(j>=1) q_j=10,
    deg L=sum_(j>=1) deg G_j.                 (3)

Let lambda_1>=lambda_2>=lambda_3 be the ordinary splitting degrees of B, retaining multiplicity. Taking exterior powers in (2) bounds

    deg G_j <= sum_(i=1)^q_j lambda_i -2j q_j.

Indeed a nonzero determinant map to the wedge of a split bundle cannot have source degree greater than its highest summand degree. No horizontality or saturation of the injected image is used.

Define h_i=#{j:q_j>=i}. Then h_1>=h_2>=0, h_3=0 and h_1+h_2=10. Summing the bounds yields

    deg L <= sum_(i=1)^2 [h_i lambda_i-h_i(h_i+1)].       (4)

There are exactly six integer possibilities, h_1=5,6,7,8,9,10 and h_2=10-h_1. These are universal rank partitions, not selected actual derivative ranks.

For indices 5,9,10 respectively, the right side of (4) has maximum

    -42, -46, -49,

whereas the actual degrees deg L=-54-deg B are

    -36, -34, -38.

Each is strictly greater than its permitted maximum, so those three cases are impossible.

## 3. The remaining equality case fixes the graded images

For index 2, lambda=(6,-4,-18) and deg L=-38. The maximum of (4) is exactly -38 and occurs only for

    (h_1,h_2)=(7,3) or (8,2).                  (5)

Hence the actual rank partition is one of (5), and every determinant bound used in (4) is equality. The ordinary degrees 6,-4,-18 are distinct. For rank q=1 or2, the top-degree line in wedge^q B is unique. Equality makes the determinant of the composite map G_j -> B(-2j) a nonzero constant into that top line, with zero components in every lower-degree wedge summand. Therefore its generic image is exactly the top q_j-summand subbundle B_(q_j)(-2j). The map factors through that subbundle everywhere and has a nowhere-zero determinant. Thus

    G_j is isomorphic to B_(q_j)(-2j).         (6)

This is an exact equality of the actual composite derivative image, not merely an Euler-character or degree match. The intermediate derivative maps in (2), under the composite identifications (6), are the inclusions of the corresponding top flags after twisting. Their highest-line channels are nonzero isomorphisms.

Let h=h_1. Since h>h_2, the final nonzero F_h=G_h is the saturated equivariant line

    C=O(6-2h).                                (7)

Strict top decrease from top F_0<=-2 gives top F_h<=-2-h. If h=7, (7) instead has degree -8, greater than the permitted -9. Hence h=7 is impossible and h=8.

Repeated differentiation of its local sections has a nonzero component in a new graded step at each of the next h steps, by the highest-line channels just proved. Lower derivatives lie in the preceding filtration term, so the leading symbol cannot cancel with them. It follows successively that the k-th forward span of C has generic rank k+1 for 0<=k<=h, and lies in F_(h-k), the last of which is S.

## 4. Equality forces the complete polynomial system

Now h=8 and e=2h-6=10, so C=O(-10). Its actual inclusion into H* O is given by an equivariant linear coefficient map

    Sym^e W -> H*.

The preceding independent derivative directions imply that its constant polynomial image has dimension at least h+1. No coefficient of this map is chosen or evaluated.

The exact decomposition Sym10 W=A_std+V+D has constituent dimensions 3+3+5. Every proper equivariant quotient has dimension at most8, less than9=h+1. By finite-group semisimplicity the coefficient map is injective.

Thus C is the full degree-e rational-normal system in a genuine constant subspace V_0 isomorphic to Sym^e W. Its k-th osculating bundle has fiber

    l^(e-k) Sym^k W inside Sym^e W

at a parameter line l, hence is Sym^k W O(k-e). This follows universally by differentiating a local power l^e, not by choosing an actual parameter or jet. Multiplication gives a fiberwise-injective equivariant bundle map into V_0 O with these fibers. Its generic containment in F_(h-k), and saturation of F_(h-k) in the ambient, make the containment hold everywhere. In particular its h-th osculating bundle lies in S.

Taking h=8 and e=10 proves that

    U=Sym8 W O(-2)=(P+D)O(-2)

lies in S inside the genuine constant V_0=Sym10 W subspace of H*.

## 5. The actual D-type annihilator gives the final contradiction

Under the invariant apolar pairing on Sym10 W, the annihilator of the fiber l^2 Sym8 W is l^9 W. Thus the annihilator bundle of U in V_0* O is

    U^perp=W O(-9).                            (8)

The actual E is the annihilator of S=Q* in H O. Its restriction/projection into V_0* O must therefore factor through (8). But every degree of the exact D-type (1) is at least -8, so

    Hom(E,W O(-9))=0

even non-equivariantly. The entire restriction is zero. Consequently every constant vector of V_0 annihilates E, so V_0 O lies in Q*=S. This contradicts H0(S)=0, which follows from top S<=-2.

This excludes index 2. Unlike the earlier general source2 intersection argument, the final step needs neither an enumeration of possible E blocks nor a residual source classification: the new exact D-type supplies the immediate ordinary-degree Hom vanishing.

## 6. Contribution and boundary

The new result excludes precisely the four remaining original profile21 shapes after the two pinned direct reductions. Together they exclude all thirteen necessary profile21 quotient rows, hence the actual maximal profile (2,1). The geometric necessity comes from the original written thirteen-pair theorem; the JSON records only exact row identities.

With the separately proved profile(1,2) exclusion, neither of these two profiles remains. Reducing a hypothetical generic-rank-three object to profile(1,1) additionally retains the original theorem excluding the other six profiles. We do not re-audit that full theorem here and do not infer it from row counts.

No profile(1,1) exclusion, COV theorem, global rank-three exclusion, maximal rank, obstruction value, full-adjoint invertibility, smoothing, algebraicity or original theorem repair is claimed. No actual coefficient, point, parameter, jet, matrix, tensor, instance rank, scan or historical enumeration is evaluated. The bounded check comprises six universal height partitions and exact character identities for the complete degree-ten polynomial system.
