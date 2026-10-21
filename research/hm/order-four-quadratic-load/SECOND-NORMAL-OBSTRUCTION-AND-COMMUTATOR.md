# The intrinsic second-normal obstruction and its commutator action

## Results and exact scope

Let Q be a smooth inversion-even quadric with balanced fixed conic C in the positive fixed plane R_+=P(V_+). Thus F_C=O_P1(-1)^2. Put B=End_0(F_Q), I=I_(C/Q), W=V_-*, N*=I/I^2=W tensor O_C(-1), and

    S=Sym^2 N*=Sym^2 W tensor O_P1(-4).

Here O_C(1)=O_P1(2). Let 3C mean the subscheme defined by I^3, not a product neighborhood.

There are two distinct intrinsic second-order classes:

1. The invariant structure algebra R=(O_Q/I^3)^+ is a square-zero extension of O_C by S. Its geometric class

       kappa in H1(T_C tensor S)

   is nonzero for every smooth even Q. Consequently this invariant second neighborhood does not retract to C.

2. The invariant algebra (End(F_Q)|3C)^+ is Azumaya over R. Comparison with the canonical constant matrix algebra over this actual, possibly nonsplit R gives

       xi in H1(B_C tensor S),             dimension 27.

   No splitting of R, lift of O_P1(-1), or coordinate expansion of F is chosen.

The second-order lifting obstruction of an untwisted constant adjoint s is [xi,s]. Its liftable space has dimension only 0,1, or3. At twist one the actual local obstruction is a 9-to-9 commutator map. At twist four the corresponding zeroth-order obstruction target vanishes, so xi alone does not settle the global positive restriction gates.

The class nevertheless gives precise necessary higher-order compatibility factors: the actual third-leading odd gate has a 36-to-18 commutator factor, and the actual fourth-leading even gate has a 15-to-63 commutator factor. The latter is injective exactly when an intrinsic quadratic commutator tensor of xi is nonzero. Its possible kernel dimensions are exactly among {0,3,4,5,15}; no claim selects the actual case.

## 1. The geometric neighborhood is genuinely nonsplit

Inversion fixes C pointwise, acts negatively on N*, and positively on S. Exact eigenspaces in

    0 -> I^2/I^3 -> O_Q/I^3 -> O_Q/I^2 -> 0

give an exact square-zero algebra extension

    0 -> S -> R -> O_C -> 0.

The doubled first neighborhood O_Q/I^2 splits canonically by invariants, but this does not split R. Since C is smooth, square-zero commutative algebra extensions with the specified ideal are classified by Ext^1(Ω_C,S)=H1(T_C tensor S).

Write the actual even equation as q_+(x)+q_-(u,v)=0. Projection to the positive coordinates is defined on an open neighborhood of C. Modulo I^3 it sends the conic equation q_+ to -q_-, a quadratic normal class in S. It therefore induces a homomorphism from the structure algebra of the doubled conic in R_+ to the invariant algebra R. On conormal ideals this is

    O_C(-2) -> Sym^2 W tensor O_C(-2),
    a -> -q_- tensor a.

The resulting square-zero extension is the pushout of the actual plane-conic extension by this conormal map: the map of extensions is the identity on O_C and the displayed map on kernels. Thus, with the extension convention fixed by this pullback equation,

    kappa_Q = -q_- tensor kappa_(C in R_+).

Changing a Čech boundary convention changes both signs and has no geometric effect.

The plane-conic class is nonzero intrinsically. Twist the tangent-normal sequence by O_C(-2)=O_P1(-4):

    0 -> O_P1(-2) -> T_(P2)|C(-4) -> O_C -> 0.

The restricted Euler sequence is

    0 -> O_P1(-4) -> O_P1(-2)^3 -> T_(P2)|C(-4) -> 0.

Its map on H1 is dual to the complete coordinate basis of H0(O_P1(2)), hence is an isomorphism between two three-dimensional spaces. Therefore the middle tangent bundle has H0=H1=0, and the tangent-normal boundary H0(O_C)->H1(O_P1(-2)) is an isomorphism. Its value at1 is the nonzero plane-conic extension class.

For smooth even Q with smooth C, both diagonal blocks q_+ and q_- are nondegenerate. In particular q_- is nonzero, so kappa_Q is nonzero. This proves that the quotient algebra R->O_C has no algebra section O_C->R, equivalently that the corresponding infinitesimal scheme has no retraction to C, without any selected coefficient evaluation.

## 2. The actual invariant algebra is Azumaya

Write A=(End(F_Q)|3C)^+. On C, inversion acts on F_C by a scalar epsilon=+1 or-1; its value is irrelevant for End(F_C).

Here is a local proof rather than an assumed equivariant trivialization. On a sufficiently small invariant open neighborhood in 3C, choose lifts of a basis of F_C. Apply the projector (1+epsilon*iota)/2 to those lifts. They still reduce to the chosen basis and now have character epsilon. Nakayama's lemma makes them a basis of F|3C. In this basis inversion acts only on coefficients, together with the common scalar epsilon. Consequently

    A locally equals Mat_2(R).

Likewise the invariant or epsilon-eigenspace of a lifted line or vector bundle is locally free over R. This proves the required Azumaya and module assertions intrinsically; no global equivariant basis is assumed.

Balance makes the evaluation map

    A_0 tensor O_C -> End(F_C),
    A_0=H0(C,End(F_C)),

an isomorphism of algebras. A_0 is a matrix algebra of dimension4. Its trace-zero part B_0=H0(B_C) has dimension3, and B_C=B_0 tensor O_C. These are canonical evaluation identifications, even though identifying A_0 with a particular matrix algebra requires a basis.

The reference algebra on the actual nonsplit R is A_0 tensor_C R. This construction does not require an O_C-algebra structure on R or a lift of the line O_P1(-1).

## 3. Definition of the projective bundle class xi

Consider the sheaf of R-algebra isomorphisms from A_0 tensor R to A which reduce to the canonical evaluation isomorphism on C. It is locally nonempty by Section2 and lifting invertible matrices across a square-zero ideal.

Its automorphism kernel consists of inner automorphisms

    1+ad(x),                  x in B_C tensor S.

Indeed derivations of a matrix algebra are inner; a unique trace-zero representative removes the central ambiguity in characteristic zero. Since S^2=0, this kernel has the additive group law. Thus the isomorphism sheaf is a torsor under B_C tensor S, with intrinsic class

    xi in H1(B_C tensor S)
       = B_0 tensor Sym^2 W tensor H1(O_P1(-4)).

The dimension is 3*3*3=27. Fix the convention that local comparison maps phi_i from the reference algebra to A satisfy

    phi_i^(-1) phi_j=1+ad(xi_ij).

Then the Čech difference of local lifts of a constant adjoint s is [xi_ij,s]. Changes of local comparison maps add a coboundary to xi. The resulting class is independent of those choices and is not a chosen coordinate coefficient of F.

In particular xi=0 exactly when A is globally isomorphic to the reference matrix algebra by an isomorphism with the specified reduction. Such an isomorphism, if it exists, is unique because H0(B_C tensor S)=0. This algebra splitting does not imply a splitting of R: its geometric class kappa is still nonzero.

## 4. Untwisted constants and the weighted scalar boundary

First consider B itself. Its invariant restriction has the exact sequence

    0 -> B_C tensor S -> (B|3C)^+ -> B_C -> 0.

The actual connecting map is

    B_0 -> H1(B_C tensor S),
    s -> [xi,s].

Since the leftmost sheaf has no sections, H0((B|3C)^+) is exactly the common centralizer of the coefficient span of xi in B_0. A nonzero element of sl_2 has a one-dimensional centralizer in sl_2: its full two-by-two matrix centralizer consists of the scalar matrix and that element. Two independent elements therefore have zero common trace-zero centralizer. Hence the possible dimensions are 3 if xi=0, 1 if its coefficient span is a nonzero line, and0 if that span has dimension at least two. No assertion is made about the actual span.

For a twist d, let

    L_d=O_C(d),
    T_d=(O_Q(d)|3C)^+.

T_d is an invertible R-module, with exact scalar sequence

    0 -> L_d tensor S -> T_d -> L_d -> 0.

Denote its actual boundary on global sections by

    b_d:H0(L_d)->H1(L_d tensor S).

This boundary packages the geometric derivation and line-twist effects without choosing a splitting of R. Tensoring the local algebra comparisons with T_d gives, for an adjoint-valued section s, the exact formula

    ob_d(s)=(id_(B_0) tensor b_d)(s)+[xi,s].

The second term is cup product, multiplication of line-bundle coefficients, and the adjoint commutator. The formula follows directly from the difference of local lifts: the scalar differences contribute b_d, and the comparison automorphisms contribute ad(xi). Products of two ideal-valued differences vanish because S^2=0.

For every d>=0 the scalar boundary b_d is zero on global sections. Every section of O_C(d) lifts to a degree-d polynomial on R_+=P2: the ideal sequence of the plane conic and H1(P2,O(d-2))=0 prove surjectivity. The same positive-coordinate polynomial is an even global section of O_Q(d), hence gives a section of T_d. This is a proof of scalar lifting, not a product-neighborhood assumption.

It follows that ob_d(s)=[xi,s] for global sections and nonnegative d. Nonzero kappa is fully compatible with this scalar lifting fact.

## 5. The exact local d=0,1,4 interfaces

For d=0 the preceding map is the centralizer map already described. The odd summand is B_C tensor N*, which has no sections; hence all local untwisted adjoints on3C are these constants that pass the commutator test.

For d=1, the actual local obstruction is

    B_0 tensor H0(O_P1(2))
      -> B_0 tensor Sym^2 W tensor H1(O_P1(-2)),
    dimensions 9 -> 9.

Via Serre duality H1(O_P1(-4))=H0(O_P1(2))* up the intrinsic dualizing trace line, xi is a map from H0(O_P1(2)) to B_0 tensor Sym^2 W tensor H1(O_P1(-2)). The obstruction sends s tensor f to [xi(f),s]. It has kernel H0((B(1)|3C)^+) and cokernel H1((B(1)|3C)^+), because H0(B_C(1) tensor S)=H1(B_C(1))=0. The odd summand has six sections and no H1.

These are sections of a finite neighborhood, not global sections on Q. In particular the known lower-good global H0(B_Q(1))=0 does not imply injectivity of this local nine-by-nine map.

For d=4, the obstruction target is

    H1(B_C(4) tensor S)=B_0 tensor Sym^2 W tensor H1(O_P1(4))=0.

Every reduced-conic adjoint section therefore extends through this second-normal order. The invariant sections on3C have dimension72 and the odd sections dimension42, with H1 zero. This does not split the neighborhood or canonically split its filtered section space. Most importantly it does not identify the global d_0 or d_2 gates with this zero obstruction.

## 6. Natural multiplication and the first nonzero higher-jet factors

Put G=B(4). For m>=0, normal multiplication gives a diagram of extensions from

    Sym^m W tensor (B(4-m)|3C)^+

into the parity-(-1)^m part of I^mG/I^(m+3)G. Its right map identifies the leading graded pieces, and its left map is the natural symmetric product

    Sym^m W tensor Sym^2 W -> Sym^(m+2) W.

The target exact sequence is

    0 -> gr^(m+2)G -> (I^mG/I^(m+3)G)_((-1)^m)
      -> gr^m G -> 0.

Exactness follows because the intervening (m+1)-st graded piece has the opposite character. Naturality of connecting maps therefore proves that its boundary

    ell_m:E_m -> H1(gr^(m+2)G)

is the symmetric normal product of the weighted coefficient obstruction in Section4. For 0<=m<=4 the coefficient twist4-m is nonnegative, so its scalar boundary is zero. Thus ell_m is precisely symmetric normal multiplication of [xi, coefficient]. No splitting of I^m/I^(m+3) is used.

For m=0,1,2 the target vanishes. For the last two relevant leading orders it gives

    ell_3:E_3 -> H1(gr^5G),           dimensions 36 -> 18,
    ell_4:E_4 -> H1(gr^6G),           dimensions 15 -> 63.

These factor the ACTUAL global staged boundaries of the finite-obstruction theorem. Namely

    ell_3: E_3 --d_3--> K_- -> H1(gr^5G),
    K_-=H1(I^5G)_-,

and

    ell_4: E_4 --d_4--> K_+ = H1(I^6G)_+ -> H1(gr^6G).

The equality in the second line is the canonical parity isomorphism H1(I^6G)_+ -> H1(I^5G)_+, since gr^5G is odd. The last arrows are actual quotient-induced cohomology maps and are not asserted onto.

Consequently every global odd section with leading order three must pass ell_3, and every global even section with leading order four must pass ell_4. Passing these tests is not sufficient for global lifting. Their targets are only parts of the82- and83-dimensional global obstruction spaces. In particular the necessarily large kernel of36-to18 supplies no global section by itself.

## 7. Exact universal classification of the top commutator factor

Set T=H1(O_P1(-4)), of dimension3. Intrinsically xi defines a map

    T* -> B_0 tensor Sym^2 W.

After choosing a basis of T only for notation, its images are three B_0-valued binary quadratics xi_i(w). The actual map ell_4 sends a B_0-valued binary quartic s(w) to

    ([xi_1(w),s(w)], [xi_2(w),s(w)], [xi_3(w),s(w)]).

This description is basis-independent through the natural tensor formulation. Define the intrinsic tensor

    c_xi:Lambda^2 T* -> B_0 tensor Sym^4 W,
    a wedge b -> [xi(a),xi(b)].

Then ell_4 is injective if and only if c_xi is nonzero. If a pair does not commute, it is independent over the fraction field of Sym W; the common centralizer of two independent sl_2 elements over that characteristic-zero field is zero. Thus a polynomial quartic in the kernel must vanish. Conversely, if all pairs commute and xi is nonzero, any nonzero quadratic xi_i multiplied by a scalar binary quadratic is a nonzero quartic in the kernel. If xi=0 the map is zero.

There is a precise kernel classification. If xi is nonzero and all its columns have function-field span one, write

    xi_i=p_i a,

where a is a primitive homogeneous sl_2-valued polynomial of degree e and the p_i are homogeneous scalar polynomials of degree2-e. Such a choice with 0<=e<=2 follows by taking a nonzero column and removing the greatest common divisor of its components; every other column is a rational multiple, and primitiveness forces that multiplier to be polynomial. The same argument shows every polynomial quartic in the common centralizer equals h a with h homogeneous of degree4-e. Therefore

    dim ker ell_4 = 5-e in {5,4,3}.

Together with the independent-column and zero cases, the only possibilities are

    dim ker ell_4 in {0,3,4,5,15},
    rank ell_4 in {15,12,11,10,0}.

This is a universal algebraic classification, not an evaluation of the actual HM class. If c_xi is proved nonzero by some future actual argument, then ell_4 and hence d_4 are injective, ruling out global even sections with leading order four. Neither actual nonvanishing nor any consequence for the remaining d_2/d_0 gates is asserted here.

## Boundary and dependencies

The balanced-conic theorem, canonical doubled-neighborhood splitting, and actual global staged boundaries are those of FIXED-PLANE-CONIC-BALANCE-AND-FOURTH-JETS.md, FIXED-CONIC-PARITY-JETS-AND-POSITIVE-GATE.md, and BALANCED-CONIC-FINITE-OBSTRUCTION-COMPLEX.md. The constructions above retain the nonsplit second-order geometry and use exact actual restriction and multiplication maps. No selected HM coefficients, chosen actual evaluations, rank scans, or external writes occur.
