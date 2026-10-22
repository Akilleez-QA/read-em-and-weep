# A constrained elementary-transform presentation of the rank-25 kernel

## Scope and current source

The latest coordination at PR1, issuecomment-6316852300, pins everywhere-surjective twist-four value descent at 03a0182dfe2dd7fa28b9d80cca002638d1589599, and the actual graph trace algebra at 83cfae3ee74dd32cdb476be617489131c115f7f3. The independent review at issuecomment-6317063542 retains H0(K4)=0 as the unresolved sufficient gate. This note derives new structure of that actual kernel, without replacing the trace bundle by End0(V)(-2F).

Use f:S(5)->P1, pi:W->S(5), and b:Wtilde->W. Let J0 be the graph curve on W and J its strict transform. Put L4=pi*(10I+12F)-h, M=L4-J0=L3-pi*H, and N4=b*L4-2 sum F_i. The fifty modified parameters are distinct, and all the previously established common-open conditions hold.

## 1. The unmodified rank-fifteen bundle has only two possible splittings

Write E=f_*O(3I). Its actual Heisenberg multiplicity decomposition and the torsion-section argument already prove that E splits in blocks of five, with three degrees either (-5,-3,-3) or (-4,-4,-3).

Set Fbundle=pi_*M=E3(-H), where E3=pi_*L3 is the exact rank-two bundle of the double-cover sequence. Dualizing via det(E3)=5I+9F gives the exact sequence

    0 -> Fbundle* -> Sym²(V*) tensor O(H) -> O(3I+2F) -> 0.

Since det V=I+3F and H=I+2F, the middle term is End0(V)(-F). Its entire relative derived pushforward vanishes by CUSP-RULING-BUNDLE-SIMPLICITY.md, including at every cusp. Thus

    R1 f_*Fbundle* = E(2).

The bundle R0=f_*Fbundle has rank fifteen, and R1 f_*Fbundle=0 by the established value-map cohomology argument. Relative duality, with omega_{S(5)/P1}=O(5F), gives

    R1 f_*Fbundle* = R0* (-5).

Consequently there is an actual bundle isomorphism

    R0 = E* (-7).

Its only possible splittings are therefore

    O(-2)^5 directsum O(-4)^10,
    or O(-3)^10 directsum O(-4)^5.

In particular rank R0=15, deg R0=-50, H0(R0)=0, and h1(R0)=35. This conclusion uses an exact dual sequence and relative acyclicity, not generic-bundle heuristics.

## 2. Exactly fifty normal-direction elementary conditions

Since N4-J=b*M-sum F_i, blowup pushdown gives

    b_*(N4-J)=M tensor I_{P_1,...,P_50},    R1 b_*(N4-J)=0.

The symbolic degeneration already proves surjectivity at each P_i, simultaneously for general Q. Thus, with R=(f pi b)_*(N4-J),

    0 -> R -> R0 -> directsum_i k_{beta_i} -> 0.

Each quotient is exactly one reduced-point condition. Hence rank R=15, deg R=-100, H0(R)=0, and h1(R)=85.

The full normalization-section space loses one hundred additional conditions in the graph direction: N4|J=b*(L4|J0)(-2 sum P_i). The remaining fifty of the original one hundred fifty doublepoint conditions are precisely the normal-direction conditions in the displayed elementary transform. This separates the two kinds of correction rather than treating all one hundred fifty as independent generic evaluations.

## 3. Exact extension presenting K4

Let r:Y->P1 be the degree-ten reduced conductor map, and let A4=O_Y(12F-H). The graph restriction is everywhere surjective, because R1(f pi b)_*(N4-J)=0. The common-value subbundle of the graph-value bundle is P=r_*A4. Taking its inverse image gives

    0 -> R -> K4 -> P -> 0.

Here rank P=10 and deg P=35. This recovers rank K4=25 and deg K4=-65, but also identifies its negative subbundle explicitly as a fifty-point elementary transform of one of the two split bundles in Section1.

On global sections,

    H0(K4) = ker[ H0(Y,A4) -> H1(P1,R) ],

where the target has dimension85. The source has dimension45 on a nonempty common open by TWIST-FOUR-COMMON-VALUE-DIMENSION.md. That note proves A4 is not canonical by a symbolic degeneration to a quadric containing one HM line. The connecting map is the actual extension map; its injectivity remains unproved.

## 4. An exact presentation of the rank-ten quotient and an upper splitting bound

The same Heisenberg argument in rank five gives f_*O(I)=O(-2)^5. Use the divisor sequence for Y in |2H|, tensored by O(12F-H). Both surface line bundles have negative fiber degree. Relative duality therefore gives

    0 -> P -> E* (1) -> O(7)^5 -> 0.

The last map is induced by the actual defining quadric of Y. Thus the middle term is either

    O(6)^5 directsum O(4)^10,
    or O(5)^10 directsum O(4)^5.

It follows that H0(P(-7))=0 in both cases. Section1 gives H0(R(-7))=0 as well, so the extension in Section3 proves

    H0(K4(-7))=0.

Equivalently every splitting summand of K4 has degree at most six. In the second Heisenberg splitting case the stronger bound is degree at most five. This is a concrete restriction on the actual kernel, not a balanced-splitting claim.

## 5. A pre-modification bundle with at least ten sections

The graph blowup is an isomorphism on the smooth marked graph points, so identify J with J0 as curves for this comparison. The inclusion p*A4=L4|J0(-2 sum P_i) gives an inclusion of the common-value bundle P into the unmodified graph-value bundle. Define Kplus as its inverse image under the surjective unmodified graph evaluation. Then

    0 -> R0 -> Kplus -> P -> 0,
    0 -> K4 -> Kplus -> directsum_i k_{beta_i} -> 0.

The second quotient map is surjective because it already is on R0. Thus Kplus has rank25 and degree-15. Its Euler characteristic is ten, so h0(Kplus)>=10; its injection on sections into H0(P) gives h0(Kplus)<=45. The actual remaining question can equivalently be stated as whether these fifty reduced normal-direction conditions annihilate all sections of Kplus. Their number alone does not establish independence.

No selected coefficients, numerical ranks, one-shot experiments, or external writes occur in this deduction. The original proof repair and the global-section vanishing remain open.

## 6. The actual connecting map has an intrinsic thirty-five plus fifty filtration

Taking cohomology of Section2, using H0(R0)=0 and the vanishing of higher cohomology of the skyscraper quotient, gives

    0 -> C^50 -> H1(R) -> H1(R0) -> 0,    dim H1(R0)=35.

This is an exact filtration, not a canonical direct-sum decomposition. The connecting map beta:H0(A4)->H1(R) has a forty-five-dimensional source. Its projection to the thirty-five-dimensional quotient is exactly the connecting map beta0 of 0->R0->Kplus->P->0. Therefore

    ker(beta0) = H0(Kplus),    10 <= dim ker(beta0) <= 45.

Every element of ker(beta0) has a unique lift to H0(Kplus), because H0(R0)=0. On these unique lifts the remaining component of beta is precisely the fifty reduced normal-direction evaluations from Section5. The actual sufficient vanishing gate is their injectivity on H0(Kplus). Surjectivity of beta0, and independence of these fifty evaluations, are not established by this presentation. In particular no arbitrary generic-matrix assumption is made.

## 7. An intrinsic kernel and pairing, without choosing matrices

The middle bundle E*(1) in Section4 has h0=85 and h1=0 in either allowed splitting. Since h1(A4)=0 by the geometric degeneration, the actual quadric-induced map on global sections is surjective and gives

    0 -> H0(A4) -> H0(E*(1)) -> H0(O(7)^5) -> 0,
                     45             85                 40.

Serre duality on P1 identifies H1(R0)*=H0(E(5)), whose dimension is35 in either splitting. Thus beta0 is canonically an actual bilinear pairing between the displayed forty-five-dimensional kernel and H0(E(5)). This describes its source and target intrinsically. Neither the presentation nor relative acyclicity of End0(V) proves that the pairing has rank35: that would require control of the actual lifting extension Kplus. No such maximal-rank assertion is used.
