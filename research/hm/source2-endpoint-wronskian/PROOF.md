# The quartic endpoint Wronskian map and its four twelve-orbit jet types

## Result and scope

Work over the complex numbers. Let G be the binary icosahedral group, W its defining two-dimensional representation, and A = Sym^2 W, V the other center-even three-dimensional irreducible, and P the center-even four-dimensional irreducible. The degree-eighteen decomposition is

    Sym^18 W = A + V + 2P + D,

where D has dimension five. Thus the G-stable ten-dimensional subsystems

    H_t = A + V + P_t  inside H^0(P(W), O(18))

are parameterized by the projective line T of P-multiplicity lines. Every member of this entire parameter line is basepoint-free, including the two nonbalanced parameters of PR754.

Let D12, D20, D30 denote the unique reduced projective A5 orbits of the indicated sizes. For every t, the Wronskian divisor of H_t is exactly one of

    D30 + 5 D12,
    D30 + 3 D20,
    3 D30,
    D30 + D60,

where D60 is a reduced free orbit, which may depend on t.

For nonzero invariant orbit forms F12, H20, T30, there is a morphism

    Phi: T -> P(span(F12^5, H20^3))

of degree exactly four, given by the residual Wronskian after division by T30. Its three special target values are [F12^5], [H20^3], and [T30^2]. Hence there are at most twelve abstract parameters with a special residual orbit divisor. Outside those parameters, H_t spans jets through order eight at every point.

The fiber of Phi over [F12^5] consists of four distinct parameters t_0, t_1, t_2, t_3. Their respective vanishing sets at each point of D12 are

    {0,...,9} minus {5+r}, together with {10+r},   r = 0,1,2,3.

Consequently:

- Every member spans jets through order four everywhere.
- Exactly one abstract parameter, t_0, fails to span jets through order five somewhere; failure occurs precisely on D12.
- Exactly two abstract parameters, t_0 and t_1, fail to span jets through order six somewhere; failure occurs precisely on D12.
- For every member and every point, the order-thirteen jet map is injective. This uniform bound is sharp: at t_3 the maximal vanishing order on D12 is thirteen.

These are statements about the entire abstract degree-eighteen family. They do not locate any parameter in coordinates, identify the parameter of a hypothetical actual source, determine its membership in the exceptional fibers, exclude a source label, or prove realization.

## 1. Inputs and all-parameter basepoint-freeness

[PR754](https://github.com/Akilleez-QA/read-em-and-weep/blob/044add76ebb14043a0edf73171517c90b9ef0c13/research/hm/order-four-quadratic-load/ABSTRACT-DEGREE-EIGHTEEN-BALANCED-SYSTEMS.md) supplies the representation decomposition above, the unique A and V subspaces, and the two-dimensional P-multiplicity space M. Write the P-isotypic summand as P tensor M. The subsystem at a line ell in M is

    H_ell = A + V + (P tensor ell).

It has dimension ten at every parameter. In particular, the two parameters failing PR754's no-linear-syzygy condition remain independent ten-section systems; that condition is not required here.

The common base divisor B of any H_ell is G-invariant. If nonempty, it has degree at least twelve, the smallest orbit size of the projective A5 action. Factoring out B embeds H_ell into H^0(O(18 - deg B)), of dimension at most seven. This contradicts dim H_ell = 10. Thus B is empty for every ell.

The projective stabilizers are cyclic of orders one, two, three, or five, giving orbit sizes sixty, thirty, twenty, or twelve. There is a unique orbit of each exceptional size: the fifteen order-two subgroups, ten order-three subgroups, and six order-five subgroups each have two fixed points, and distinct such stabilizers cannot fix the same point. The binary group G is perfect, so all of its one-dimensional characters are trivial.

[PR785](https://github.com/Akilleez-QA/read-em-and-weep/blob/7ec3b8140abe6ee60f9d0dfee657e7b0be022fc3/research/hm/source2-four-jet-rigidity/PROOF.md) proves universal four-jet spanning and its actual-source Gauss consequences. The argument below strengthens the endpoint-family information rather than repeating those Gauss consequences. [PR784](https://github.com/Akilleez-QA/read-em-and-weep/blob/66aa488fb10158abcc2d35ce58b05b901d44b81a/research/hm/source2-second-defect-zero/PROOF.md) provides the preceding actual-source endpoint theorem. No actual-source existence follows from these conditional applications.

## 2. Wronskian degree and the forced thirty-orbit divisor

For a ten-dimensional system in O(18), the determinant of its order-nine jet map is a section of

    det(H)^* tensor O(18)^10 tensor (Omega^1)^(0+...+9)
      = O(90),

because 10*18 - 2*45 = 90. At a point with vanishing sequence

    0 <= a_0 < ... < a_9 <= 18,

the local Wronskian order is

    w = sum_i (a_i - i).                                      (1)

Indeed, an adapted basis has leading terms of these orders, and the leading Wronskian coefficient is the product of their nonzero leading coefficients times the Vandermonde in the a_i. Characteristic zero makes this nonzero. Thus the Wronskian is nonzero for every parameter. Its determinant character is trivial by perfectness, so it is an invariant degree-ninety form.

At an arbitrary point of D30, choose an order-four binary lift whose eigenvalues on W are i and -i, with i on the tautological line. The O(18) fiber character is i^(-18) = -1, and the cotangent character is i^2 = -1. Hence the order-j graded jet line has character

    (-1)^(j+1).                                               (2)

Both three-dimensional irreducibles restrict to eigenvalue multiplicities (+1:1, -1:2). The four-dimensional P, the five-letter permutation representation minus its invariant line, has multiplicities (+1:2, -1:2) at a double transposition. Therefore H has multiplicities (+1:4, -1:6).

The stabilizer preserves the vanishing filtration, so (2) requires six even vanishing orders and four odd vanishing orders. Their unique coordinatewise minimum is

    0,1,2,3,4,5,6,7,8,10,

with sum 46 and weight one. Thus D30 is a fixed effective summand of the Wronskian divisor. The sign of the O(18) fiber in (2) is essential.

The residual divisor is effective, invariant, and has degree sixty. If its exceptional-orbit multiplicities are a,b,c and its number of free-orbit contributions, counted with multiplicity, is d, then

    12a + 20b + 30c + 60d = 60.

The only nonnegative solutions are (a,b,c,d) = (5,0,0,0), (0,3,0,0), (0,0,2,0), and (0,0,0,1). For example, after d=0, the possibility c=1 is impossible modulo four, and c=0 reduces to 3a+5b=15. This proves the four-divisor classification. A degree-sixty free orbit has multiplicity one.

## 3. The degree-sixty invariant pencil

Let F12, H20, T30 be nonzero forms with divisors D12, D20, D30. Their lines are G-stable, and perfectness makes each form invariant. Their zero sets are pairwise disjoint.

The ratio

    q = F12^5 / H20^3

is A5-invariant. It defines a degree-sixty map P(W) -> P1 because the numerator and denominator both have degree sixty and no common zero. Therefore

    [C(P(W)) : C(q)] = 60.

The faithful A5 action has order sixty, so its invariant field has the same index sixty. Consequently

    C(P(W))^A5 = C(q).                                        (3)

If R is any invariant degree-sixty form, R/H20^3 belongs to the field (3). Its poles can occur only on D20, and there with order at most three. The map q has pole order exactly three at every point of D20. Accordingly the descended rational function on the q-line has only a possible simple pole at infinity. It is affine linear in q. Thus

    H^0(O(60))^G = span(F12^5, H20^3).                         (4)

In particular T30^2 belongs to this span. Both of its coordinates in the displayed basis are nonzero, since its divisor is disjoint from D12 and D20. Hence [F12^5], [H20^3], and [T30^2] are three distinct target values.

This proof needs neither an explicit Klein relation nor coefficients of the orbit forms.

## 4. The parameter Wronskian map has degree exactly four

Choose two G-equivariant embeddings i_0, i_1 of P that identify its multiplicity space M with C^2. If (s,t) is a nonzero multiplicity vector, choose bases a_1,...,a_3 of A, v_1,...,v_3 of V, and p_1,...,p_4 of P. A basis of H_[s:t] is

    a_1,...,a_3, v_1,...,v_3,
    s i_0(p_1)+t i_1(p_1), ..., s i_0(p_4)+t i_1(p_4).

The universal Wronskian is alternating and linear in each of its ten entries. The resulting invariant degree-ninety form is therefore homogeneous of degree four in (s,t). Section 2 shows that it is divisible by the fixed form T30. By (4), it has the form

    W(s,t) = T30 [A4(s,t) F12^5 + B4(s,t) H20^3],              (5)

where A4 and B4 are homogeneous degree-four forms in the parameter coordinates. No coefficient of these forms is needed.

They have no common projective zero: such a zero would make W(s,t) identically zero as a section on P(W), contradicting independence of the ten sections and (1). Thus

    Phi([s:t]) = [A4(s,t):B4(s,t)]                             (6)

is a morphism with pullback O(1) = O(4). In particular it is nonconstant and has degree exactly four, not merely degree at most four. Equivalently, a constant ratio would force the two homogeneous quartics to have a common zero.

Each target fiber has length four, counted with parameter multiplicity. The union of the three special fibers therefore has at most twelve distinct parameters. Outside it, Section 2 forces a reduced free residual orbit. Every ramification point then has weight one, whose only possible vanishing sequence is (0,1,...,8,10). Every other point has sequence (0,1,...,9). Thus the order-eight jet map is surjective at every point for all those parameters. Surjectivity of Phi also shows that every one of the four divisor regimes occurs somewhere in the abstract family; no actual-source realization is asserted.

## 5. Local possibilities at the special orbits

The vanishing filtration is invariant under the point stabilizer. Each nonzero one-dimensional associated graded piece has the character of the corresponding graded jet line. Thus character multiplicities determine the numbers of vanishing orders in each congruence class.

At D12, choose an order-ten lift with tautological eigenvalue lambda and put zeta = lambda^2. The O(18) fiber has character lambda^(-18) = zeta and the cotangent character is zeta. The order-j line has character zeta^(j+1). The restrictions are

    A = 1 + zeta + zeta^(-1),
    V = 1 + zeta^2 + zeta^(-2),
    P = zeta + zeta^2 + zeta^3 + zeta^4.

Hence exactly two orders occur in each residue class modulo five. Their minimum is 0,...,9. If the weight is five, exactly one terminal entry of a residue class rises by five, giving provisionally

    {0,...,9} minus {5+r}, together with {10+r},  0 <= r <= 4.  (7)

Section 6 excludes r=4 for the family under consideration and proves that each of the other four cases occurs at its own parameter.

At D20, the two three-dimensional irreducibles each restrict as 1+omega+omega^2, and P restricts as 2+omega+omega^2. The O(18) fiber character is trivial. Thus the order residues modulo three have counts (4,3,3), whose minimum is 0,...,9. Weight three permits only

    {0,...,9} minus {7}, together with {10};
    {0,...,9} minus {8}, together with {11};
    {0,...,9} minus {9}, together with {12}.                   (8)

At D30, Section 2 gives the minimum of weight one. Weight three raises exactly one terminal residue-class entry by two, so its only possibilities are

    (0,1,2,3,4,5,6,7,8,12),
    (0,1,2,3,4,5,6,8,9,10).                                  (9)

For (7)--(9), raising a nonterminal entry alone would collide with the next entry in the same residue class; any larger total change exceeds the available local weight. This proves completeness of these lists. The divisor classification gives local weight zero at every point not listed in its support. We do not claim here that every candidate in (8) or (9) occurs.

## 6. Four distinct twelve-orbit parameters

Consider an arbitrary point of D12 and the order-nine jet map as a family over T. This is a statement about its stabilizer-character decomposition; no values of a particular source system are required.

Each of the five character spaces of the order-nine jet target has dimension two. The fixed part A+V of H has multiplicity two in the trivial character and multiplicity one in each nontrivial character. The variable P part has multiplicity one in each nontrivial character and no trivial character.

Consequently the determinant of the order-nine jet map factors, up to a fixed nonzero scalar, into

    c L_0 L_1 L_2 L_3,                                       (10)

where c is the determinant of the fixed trivial-character block, and L_r is homogeneous linear on M for the block of character zeta^(r+1), r=0,1,2,3. These determinant sections are intrinsic; chosen bases only multiply their factors by nonzero constants.

None of the factors is identically zero. Otherwise the Wronskian would vanish on D12 for every parameter. The divisor classification would then force every residual divisor to be 5D12, making Phi constant, contrary to Section 4. Thus c is nonzero and each L_r has one simple projective zero t_r.

These four zeros are pairwise distinct. If L_r and L_s vanished at the same parameter for r != s, the two corresponding residue classes would each have vanishing-order sum at least five above its minimum. The total local weight on D12 would be at least ten. This is impossible: Section 2 allows weight only zero or five there. At the zero of L_r there is consequently precisely the r-th change in (7).

The trivial-character block corresponds to the order residue r=4, because the fiber twist is zeta. It is fixed and nonsingular, so that residue cannot change. This eliminates the provisional case r=4. Equation (10) also shows that the special target fiber is reduced: the coefficient cutting out the value [F12^5] in (5) is a nonzero scalar multiple of the product of the four distinct linear factors. Hence Phi is unramified over that value.

This proves both the exact four-point fiber and its stated vanishing sequences without selecting parameter coordinates or assigning any actual coefficient.

## 7. Exact low-order jet exceptions and the sharp upper vanishing bound

The first missing vanishing order at t_r on D12 is 5+r. At all other D12 parameters the ordinary sequence 0,...,9 occurs. At D20 the possibilities (8) first omit an order at least seven; at D30 the possibilities in Section 2 and (9) first omit an order at least seven. Free ramification points first omit nine. Thus no point outside D12 can fail order-five or order-six jet spanning.

It follows that t_0 is the unique abstract member failing order-five spanning anywhere, and t_0,t_1 are exactly the members failing order-six spanning anywhere. Their failure sets are D12. All possible sequences begin with 0,1,2,3,4, recovering universal four-jet spanning.

The largest possible final order in the refined D12 list is thirteen; in (8) and (9) it is at most twelve, and at a free ramification point it is ten. Therefore every nonzero section in every H_t has vanishing order at most thirteen at every point. Equivalently, every order-thirteen jet map is injective. At t_3 the sequence is

    (0,1,2,3,4,5,6,7,9,13),

so a nonzero section has order thirteen. The order-twelve jet map is then not injective, proving sharpness of the uniform bound.

## 8. Novelty and the remaining source interface

PR754 proves the parameter line and identifies its balanced open locus, but does not classify its ramification divisors or construct its Wronskian map. PR784 establishes the hypothetical actual endpoint's second jets; PR785 proves universal four-jet spanning and transfers that to the next actual Gauss flag. The new statements here are all-parameter basepoint-freeness, the forced D30 and four possible residual divisor types, the degree-four parameter Wronskian morphism, and the four distinct D12 parameters with their exact jet behavior.

The actual source parameter, if one exists, must still satisfy all same-source compatibility conditions, including the balanced presentation. This theorem does not identify it with any parameter above, decide whether it avoids the exceptional loci, or establish any further actual Gauss growth beyond what follows under an explicitly stated jet-spanning hypothesis. It does not change the source-label frontier.

The proof is structural and uses character restrictions, invariant divisors, function fields, and universal jet determinants. It assigns no invariant-form coefficients and computes no actual-source point, derivative, matrix, or rank. No source-instance experiment or parameter scan is part of the argument. The local lists (8) and (9) are necessary possibilities, not claims of their individual realization.
