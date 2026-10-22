# Independent mathematical review

Verdict: PASS for the ramification and exact five-torsion conclusions, conditional on the pinned smooth invariant (4,4) Gram-curve input from PR656 at 561f4cf5e4ad23a9f384936816d7a6ef0bd07dd6. This is an independent mathematical check, not formal proof-assistant verification. No selected source-instance coefficient, point, matrix, or rank was evaluated.

## 1. Independent representation check

Let phi=(1+sqrt(5))/2 and G be the binary icosahedral group. Its defining two-dimensional representation W has trace classes 2,-2,0,1,-1,phi,-phi,phi^-1,-phi^-1, of sizes 1,1,30,20,20,12,12,12,12. For P_n(t)=character(Sym^n W), use P_0=1, P_1=t, and P_n=t P_{n-1}-P_{n-2}. Odd symmetric powers have odd character, so it suffices to display the classes 2,0,1,phi,phi^-1:

- P_3: 4,0,-1,1,-1.
- P_5: 6,0,0,-1,1.
- P_7-P_5: 2,0,1,-phi^-1,-phi.

The last row is the character of the other two-dimensional representation Wprime. The norm of P_5 is (72+24+24)/120=1. The norm of P_3 is (32+40+24+24)/120=1, and their inner product is (48-24-24)/120=0. Thus Sym^5 W and Sym^3 W are nonisomorphic irreducibles of dimensions six and four. Swapping W with Wprime sends phi to -phi^-1 and phi^-1 to -phi, leaving the P_5 character unchanged. Consequently Sym^5 Wprime is the same six-dimensional irreducible, and Sym^7 W = Wprime direct-sum Sym^5 W. These checks establish the representation inputs without relying merely on dimension names.

## 2. Exact five-torsion

Write X=P(Wprime) times P(W), C an invariant smooth divisor of type (4,4), and T=O_C(1,-1). The equation line is a trivial G-character because G is perfect. Therefore its divisor sequences are equivariant without a hidden character twist. The determinant characters of W and Wprime are trivial, so Serre duality introduces no determinant twist. All representations in use are self-dual.

For T the divisor sequence has left term O_X(-3,-5) and middle term O_X(1,-1). Both H^0 of the middle term and H^1 of the left term vanish by the cohomology of P1 and Kunneth. Hence H^0(C,T)=0, so T is nontrivial.

For T^5 the left term is O_X(1,-9), and the middle term is O_X(5,-5). Both ambient H^0 groups vanish. Thus H^0(C,T^5) is the kernel of the map between their H^1 groups. Their invariant dimensions are respectively

    dim (Wprime tensor Sym^7 W)^G = 1,
    dim (Sym^5 Wprime tensor Sym^3 W)^G = 0.

Taking invariants is exact in characteristic zero. Hence this kernel has a nonzero invariant section. As deg(T^5)=0 on the smooth connected curve C, that section has no zeros and trivializes T^5. Nontriviality of T then proves exact order five. No rank or value of the multiplication map is needed.

## 3. Ramification audit

At a C5-fixed pair use an order-ten lift with tautological weights u in {3,-3}, v in {1,-1}. The equation fiber has weight -4(u+v), never zero modulo ten, so all four pairs lie on C. The two surface tangent weights are -2u and -2v. For each pair exactly one equals the equation-fiber weight; smoothness forces its allowed derivative to be nonzero. Thus C is tangent to the other coordinate direction.

For example u=3,v=1 permits the derivative in the first direction, so C has tangent weight -2 and the first target has weight -6. The ramification index e of the first projection therefore obeys -2e=-6 modulo ten, or e=3 modulo five. Since its global degree is four, e=3. The second projection is unramified. For u=3,v=-1 the roles reverse. Negating both weights gives the other two cases. This verifies the sign and index claims.

There are six C5 subgroups; each contributes four pairs, and smooth-curve stabilizers are cyclic, so the resulting 24 points are distinct. Each projection has twelve index-three points. Riemann--Hurwitz gives total ramification degree 2g-2+8=24, so these exhaust ramification. The two reduced supports R1 and R2 are disjoint, each a single A5 orbit of length twelve. The pullbacks of the two exceptional base orbits are 3R1+R2 and R1+3R2 respectively.

Faithfulness follows from either equivariant surjective projection. Cyclic stabilizers in A5 can only have orders two, three or five. If a and b count the remaining stabilizer-two and stabilizer-three orbits, Riemann--Hurwitz is

    16=60(2q-2)+96+30a+40b.

It forces q=0,a=0,b=1. Thus the quotient signature is (3,5,5).

Finally, for Li=p_i^*O(1), the two Hurwitz formulas give 2(R1-R2)=2(L1-L2), while the exceptional-orbit pullbacks give 2(R1-R2)=12(L1-L2). Hence 10(L1-L2)=0, consistently sharpened to exact order five above.

## Scope

The five-torsion belongs to the genus-nine Gram curve C. It is not the spectral genus-ten two-torsion, and does not transfer automatically to the original genus-four support curve. The actual R-class, final contraction, third Bockstein and algebraicity remain unresolved by this argument.

## 4. Further cyclic-five-cover consequence

The proposed next construction also passes. The natural G-linearization on T=O_C(1,-1) has trivial central action and therefore descends to A5. Since T^5 is trivial, its space of sections is one-dimensional; A5 is perfect, so its nonzero trivialization is invariant. The algebra direct-sum of T^{-j} for j=0,...,4, with multiplication supplied by that trivialization, defines an etale cyclic-five cover Z->C with an honest A5 action commuting with its deck C5. Exact order five makes this cover connected: for j=1,...,4, the nontrivial degree-zero line T^{-j} has no section, so H^0(Z,O_Z)=C. Its genus is 1+5(9-1)=41. The two actions intersect trivially, since an A5 element agreeing with a deck transformation would act trivially downstairs on C. Thus the action is by A5 times C5.

At any C5-fixed pair, the T-fiber weight is -u+v, one of 2,-2,4,-4 modulo ten, so the relevant nonidentity order-five A5 element acts on the five points of the cover fiber without fixed points. At a C3-fixed point, the fiber character has both cube and fifth power equal to one, and is therefore trivial. Every one of the five points above it is fixed. There are twenty such points on C, yielding one hundred points on Z of stabilizer three under the A5 factor, and no other nontrivial stabilizers. Riemann--Hurwitz gives

    80=60(2q-2)+100(3-1),

so q=0. The quotient by this A5 factor has exactly five branch orbits, all of order three. This construction is a new genus-forty-one cover, not an identification with any of the previous spectral covers.
