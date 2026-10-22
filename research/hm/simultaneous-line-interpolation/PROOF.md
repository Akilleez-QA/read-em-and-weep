# Sharp scalar localization cost and stabilized simultaneous realization

## Scope and dependencies

Work over C in the marked setup of [PR678](https://github.com/Akilleez-QA/read-em-and-weep/blob/f47c81086e5bd17be4ba714e43fa7f6226d41beb/research/hm/ramification-family-target/PROOF.md). Its reduced ramification scheme R is one Gamma orbit of twelve points in B=P(U) times P(W), a complete intersection of two sections of O(2,3). Its joining lines in P(V* direct-sum W*) are pairwise disjoint; the positive endpoint is the Veronese image v=r^2. Let Z=P(W*) be the negative vertex. We use [PR679](https://github.com/Akilleez-QA/read-em-and-weep/blob/17dce2263c2ad5ddc26d42c6aaeb21dfdfb7dacb/research/hm/linewise-operator-image/PROOF.md), which realizes arbitrary three-coefficient center-compatible values on each single entire joining line by global determinant-skew twist-four operators vanishing on all of Z.

This note proves an obstruction to scalar localization at twist four and a positive stabilized simultaneous realization. It does not determine the original twist-four simultaneous image, impose the coupled monad-source equations, or establish a Bockstein, higher-order, or algebraicity conclusion. No selected actual coefficients, points, or matrices are evaluated.

## 1. No cubic scalar isolates one joining line

For an ambient homogeneous polynomial P of degree d, split by positive-coordinate degree j. On the joining line above (r,w), write x=t r^2+s w. Then

    P(t r^2,s w)=sum over j of t^j s^(d-j) P_j(r,w),

where P_j is a section of O_B(2j,d-j). Conversely every such section lifts to an ambient polynomial of that bidegree: multiplication Sym^j(Sym^2 U*) -> Sym^(2j) U* is onto (every binary monomial of even total degree is a product of j quadratic monomials), and the negative factor is unchanged.

Suppose P vanishes on eleven whole joining lines but not the twelfth. At least one coefficient P_j has nonzero restriction supported on precisely that twelfth point of R. For any Gamma-linearized line bundle L on B, the restriction image in H0(R,L|R) is Gamma-stable. If it contains one nonzero section supported at one point, transitivity gives a nonzero section supported at each of the twelve points. These twelve sections are linearly independent. Therefore such an image must have dimension twelve.

For d<=3 this is impossible: the domain of the j-th restriction has dimension

    (2j+1)(d-j+1).

The lists for d=0,1,2,3 are respectively (1), (2,3), (3,6,5), and (4,9,10,7), all entries strictly below twelve. Consequently no polynomial of degree at most three vanishes on eleven joining lines without vanishing on all twelve. This is a whole-line statement, independent of choices of endpoint scales and of stabilizer characters of the fibers.

In particular one cannot turn degree-one global transvections into twist-four isolated-line operators merely by multiplying by scalar cutoffs: the available scalar degree is three, and no such cutoff exists. This does not rule out cancellation between different operator-valued generators.

## 2. Quartic scalar selectors exist, with a fixed endpoint divisor

The complete-intersection resolution twisted by O(4,2) is

    0 -> O(0,-4) -> O(2,-1)^2 -> I_R(4,2) -> 0.

All cohomology of O(2,-1) vanishes; H2(O(0,-4))=0. Thus H1(I_R(4,2))=0, and

    H0(B,O(4,2)) -> H0(R,O_R(4,2))

is onto. Also H0(I_R(4,2))=H1(O(0,-4)) has dimension three, consistent with 15-3=12.

Choose any nonzero value in the one-dimensional O_R(4,2) fiber at a selected point and zero values elsewhere. Lift it and then lift the section to an ambient polynomial P of positive degree two and negative degree two. Its total degree is four. It vanishes on all other eleven joining lines, while its restriction to the selected line, after choosing endpoint frames, is

    P(t v,s w)=a t^2 s^2, a nonzero.

Rescale to a=1. These are minimum-total-degree scalar selectors by section 1. They vanish at both endpoints of the selected line, each to order two; they are not nowhere-zero projectors on a projective line. They are center-even and vanish along the entire negative vertex to order at least two.

## 3. A simultaneous realization after an explicit four-degree stabilization

For each point i of R let T_i be a global twist-four determinant-skew, center-even operator vanishing on Z supplied by PR679. Prescribe its normalized line value q_i arbitrarily in

    span(t_i s_i^4, t_i^3 s_i^2, t_i^5).

Let P_i be the quartic selector above, normalized on that line. Set

    T = sum over i of P_i T_i.

This is a global determinant-skew twist-eight operator. Scalar multiplication preserves the skew identity; the center-even properties multiply; vertex vanishing is preserved. On the j-th whole line every term except j vanishes identically and hence

    lambda_(s_j w_j)(T Y)=t_j^2 s_j^2 lambda_(s_j w_j)(T_j Y).

In the normalized notation of PR679, q_T on the j-th line is exactly t_j^2 s_j^2 q_j. Therefore the image of the simultaneous map at twist eight contains the following 36-dimensional subspace of its full receiving space, consisting independently on all twelve lines of

    span(t^3 s^6, t^5 s^4, t^7 s^2).

This target is intrinsic: if the original three coefficient bundles are O_R(3,7), O_R(7,5), O_R(11,3), their stabilized coefficient bundles are obtained by tensoring O_R(4,2), namely

    O_R(7,9) direct-sum O_R(11,7) direct-sum O_R(15,5).

The extra factor t^2 s^2 and its coefficient transformation together make the construction independent of the temporary endpoint frames. The image space is Gamma-stable, since Gamma permutes the lines, preserves their two endpoints, and preserves the three relative-degree channels. Over C, averaging a lift of an equivariant linear map from any finite-dimensional Gamma representation gives an equivariant lift. Restrict the operator domain to the preimage of this Gamma-stable subspace. The resulting surjection also gives surjectivity on Gamma-equivariant parameter-family Hom spaces into this stabilized target. For a C10 stabilizer with the weights of PR678, the three shifted bundle exponents 3p+q are 30,40,50, so each fiber character is trivial. Each induced module is therefore 1+A+V+D; for P2=1+A+V+2P+3D the corresponding family target has dimension 3(1+1+1+3)=18. This numerical equality does not identify the target with the original eighteen-condition target. The multiplier bundle O_R(4,2) has exponent 14 and nontrivial stabilizer character, so it has no Gamma-invariant nowhere-zero section. In particular there is no canonical Gamma-equivariant unit identifying the old forcing with a shifted forcing.

## 4. Exact consequence and remaining dependency

The obstruction to naive scalar-cutoff gluing is sharp: total scalar degree three cannot isolate any whole joining line, whereas degree four can. The explicit selector method simultaneously realizes all original single-line three-coefficient data after multiplication by the common endpoint divisor of degree four. This supplies a structural finite stabilization, not a solution at the required original twist four.

Removing the added endpoint factor or avoiding its twist cost requires genuinely operator-valued compatibility or another structural argument. Dividing by the selectors is not allowed: it would introduce poles at the endpoints and destroy the claimed global regularity. The degree-eight construction makes no assertion that the degree-four cokernel vanishes.

## 5. The constant/moving splitting has a genuine global extension obstruction

There is an additional structural reason not to glue the single-line matrix construction by declaring its frames global. Let

    X=P_B(O(-2,0) direct-sum O(0,-1)),

using the convention of lines, with tautological O_X(-1), projection p, and the natural joining-scroll morphism X -> P(H*). Put K=ker(V O_B -> O(2,0)) direct-sum ker(W O_B -> O(0,1)). The two evaluation kernels split as

    K = O(-1,0)^2 direct-sum O(0,-1).

For the positive kernel, the two linear syzygies of the quadratic Veronese coordinates give this splitting; the negative kernel is the binary Euler sequence. Pullback of F=ker(H O -> O(1)) gives an exact sequence

    0 -> p*K -> F_X -> M -> 0,
    M = p*O(2,1) tensor O_X(-1).

Indeed H/K=O(2,0) direct-sum O(0,1), and the kernel of its tautological evaluation onto O_X(1) is its determinant tensored by O_X(-1). Exterior squaring and tensoring U gives

    0 -> N -> E_X -> U tensor p*K tensor M -> 0,
    N=U tensor Lambda^2(p*K).

Here N is Lagrangian and, as an ordinary bundle on B pulled back to X,

    N = O(-2,0)^2 direct-sum O(-1,-1)^4.

Neither displayed extension is globally split. To prove this, restrict to the negative-endpoint section B -> X and then to a positive P1 fiber with the negative coordinate fixed. There O_X(-1) restricts to a constant line, F_X is the trivial rank-four bundle, K restricts to O(-1)^2 direct-sum O, and M restricts to O(2). A splitting of the first sequence would give a nonzero morphism O(2)->O^4, impossible because H0(O(-2))=0. Similarly E_X is trivial of rank twelve on this curve, whereas its displayed quotient is

    U tensor (O(1)^2 direct-sum O(2)).

There is no nonzero morphism from this quotient to O^12, so the second extension cannot split either. This is a universal bundle obstruction, not an evaluation of the ramification instance.

Thus the constant and moving Lagrangians of the single joining line do not come from a global direct-sum decomposition over the full joining scroll. This does not prove that a splitting is impossible over the finite union of ramification lines, nor does it obstruct global sections from solving the original interpolation map. It does rule out the specific shortcut of using one global constant/moving frame decomposition on X. A fixed-twist-four proof must handle this extension rather than silently discard it.
