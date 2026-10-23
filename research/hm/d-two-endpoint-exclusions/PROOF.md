# Two D-source endpoint exclusions in maximal profile (1,1)

## 1. Statement, actual hypotheses and scope

Over C, on the fixed physical G=SL2(F5) parameter line P(W), retain the original actual saturated inclusion E -> H O with dim H=30, rank E=17, deg E=-54, and S=(H O/E)* of rank13, degree -54, with H0(S)=0. Suppose the actual rank-three Gauss plateau has maximal profile (1,1). Put K=E^-, L=S^-, A=E/K, B=S/L. Then rank L=10 and rank beta_L<=2. All kernels and derivatives below are for the actual constant connection, never for a chosen Birkhoff complement.

Assume the actual D source

    E=D O(-2)+(W'+T)O(-3)+V O(-4)+O(-8).             (1)

We exclude the following two exact pairs:

    32: A=O(-8)+O2+O4, B=O6+O(-4)+O(-18), defect12;
    52: A=O(-8)+W O3, B=O6+W O(-5), defect0.          (2)

The labels are the original zero-based identifiers in the immutable 159-pair necessary list, not new enumeration results. This proof does not exclude pair50, exhaust other profiles, establish occurrence of any formal type, or repair the original theorem. It does not infer a full-adjoint, smoothing, or algebraicity conclusion. Its inputs are written mathematical theorems, not proof-assistant certification.

Here D=Sym4 W, T=Sym5 W, dim W'=2, dim V=3; V is the nonstandard three-dimensional representation. The required physical identities are

    Sym6 W=V+P, Sym8 W=P+D, dim P=4,
    Sym10 W=A_std+V+D.

All are self-dual. G is perfect, so every equivariant line of degree e has the standard O(e) linearization, without a character twist. In particular this applies to determinant lines of arbitrary equivariant graded bundles, not only split flags.

The complete original actual, four-source and profile11 necessities, PR1145's full apolar argument, the fixed original list, and exact character implementation are retained and pinned in INPUTS.json. This proof re-establishes the specific jet consequence and residual apolar argument it needs; it does not extend PR1145's stated A-shape theorem by citation alone.

## 2. Kernel chain, capacity and the finite-jet bound

Let F_0=S, F_1=L, F_(j+1)=F_j^-, and G_j=F_j/F_(j+1), q_j=rank G_j for j>=1; G_0=B. Kernels are saturated in the constant ambient: the quotient by a kernel is the torsion-free image of its second fundamental form, hence locally free on the smooth curve, and saturation composes. Differentiating F_j lands in F_(j-1), and induces injections

    G_j -> G_(j-1)(-2) -> ... -> B(-2j).             (3)

The first injection's kernel is exactly F_(j+1) by definition. Thus 2>=q_1>=q_2>=... . Negative saturated nonzero bundles cannot be horizontal: the corresponding Grassmannian map would have zero differential, hence be constant in characteristic zero, giving degree zero. Thus the chain terminates, q_j is positive until then, and sum q_j=10.

Write h=h_1=#{j:q_j>=1}, h_2=#{j:q_j>=2}=10-h. Then h=5,...,10. If lambda_1>=lambda_2 are the top two ordinary degrees of B, determinants in (3) give

    deg L <= h lambda_1-h(h+1)
             +(10-h)lambda_2-(10-h)(11-h).          (4)

This allows nonsaturated composite images and all torsion deficits.

For (1), F_8=0. Here is a direct proof, including partial coefficient systems. Choose a bundle splitting of E, and write each actual embedded affine frame as a vector polynomial p_i(t) of degree a_i<=8. This does not make the splitting horizontal. Their coefficient vectors span H because H0(S)=0. Inductively a local section s of F_j annihilates all p_i^(a) for 0<=a<=j. Indeed membership in F_j means s,Ds belong to F_(j-1), and differentiating <s,p_i^(a)>=0 gives <s,p_i^(a+1)>=-<Ds,p_i^(a)>. The exact Taylor identities

    v_k=sum_(a=k)^d binom(a,k)(-t)^(a-k) p^(a)(t)/a!

for p(t)=sum v_k t^k show that derivatives through8 span all coefficient vectors over the affine ring. Hence F_8=0 on that chart, and globally by torsion-freeness. Thus h<=7.

We will also use the converse-direction elementary observation: if an actual line C=O(-d) lies in F_d, then its first d derivatives lie in S. The same Taylor identities imply that S contains its entire nonzero constant coefficient image. Saturation extends the containment over the missing point, contradicting H0(S)=0. Completeness or independence of the coefficient vectors is not needed.

## 3. Pair32 forces a complete degree-eight constant summand

For pair32, deg B=-16, so deg L=-38. Its capacities (4), for h=5,...,10, are

    -50,-42,-38,-38,-42,-50.

The jet bound removes h>=8. Therefore h=7, h_2=3, and every determinant bound is equality.

For q=1 or2 the top-degree summand of wedge^q B is unique, because the three scalar degrees are6,-4,-18. Equality makes the determinant component into that top line a nonzero constant; components into lower lines vanish. Consequently the composite in (3) has generic image equal to the top q summands, factors through that subbundle everywhere, and has invertible determinant. Thus it identifies G_j with those top q summands of B(-2j). This proves an exact image statement, not an assumption that arbitrary Plucker images are top flags.

In particular F_7=O(-8). Its successive derivatives have new nonzero leading components in G_6,G_5,...,G_0: on the highest line, maps to lower summands vanish by degree, and the composite identifications force the highest-line channel to be nonzero. Thus derivatives through7 have eight independent generic directions. Its coefficient map Sym8 W -> H* has image dimension at least8. Since Sym8 W=P+D, a proper quotient has dimension at most5. Hence its constant image U has dimension9 and the coefficient map is an isomorphism onto U.

For the complete degree-eight line, the seventh osculating bundle is Sym7 W O(-1), with fiber l Sym7 W, inside U O. Its generic inclusion into S extends everywhere by saturation. Under invariant apolarity its annihilator in U* O is the complete line J_0=O(-8), fiber l^8. Thus the constant projection E -> U* O factors through J_0. Only the O(-8) summand of (1) can map to J_0. Its scalar is nonzero, since otherwise U O would be a constant subbundle of S.

Let N=ker(H -> U*), dim N=21. Choose a bundle splitting E=F+J with J=O(-8) and

    F=D O(-2)+(W'+T)O(-3)+V O(-4).                 (5)

The embedded F lies in N O. The actual coefficient map of J has image C in H, and its composition with H -> U* is an isomorphism of degree-eight coefficient spaces. Hence C is a constant nine-dimensional complement to N. We have the genuine constant decomposition

    H=N direct-sum C, E=F direct-sum J.

This is not a horizontally chosen Birkhoff complement: the coefficient-space argument constructs the constant complement from the complete polynomial system. The quotient splits, so both embedded summands are saturated and their actual derivatives are block diagonal. Rank F=16 and deg F=-46.

## 4. Pair32 residual apolar contradiction, independent of A_F

Write S_F=(N O/F)*, S_J=(C O/J)*. The complete degree-eight summand has

    S_J=Sym7 W O(-1), L_J=Sym6 W O(-2), B_J=O6.

These follow by differentiation of fibers l Sym7 W and l^2 Sym6 W. L_J has derivative rank one. Constant block differentiation therefore gives S=S_F+S_J and L=L_F+L_J with

    rank S_F=5, deg S_F=-46, rank L_F=3,
    B_F=S_F/L_F=O(-4)+O(-18), deg L_F=-24.

Cancellation here is cancellation of actual direct sums, with uniqueness of equivariant splitting. The bound rank beta_L<=2 implies rank beta_(L_F)<=1. Negativity makes it positive. Its subsequent kernel chain has ranks3,2,1,0; all increments are positive and at most1 by (3). The three line quotients inject into B_F(-2j), j=1,2,3, so their degrees are bounded by -6,-8,-10. Their sum is -24, forcing equality. The last line M_3 is O(-10), and its first three derivatives lie in S_F.

Let q:Sym10 W -> R subset N* be its actual coefficient quotient, which may be partial. Duality embeds R* into (Sym10 W)*. The projection of F into R*, followed by that injection, annihilates l^7 Sym3 W because its image under q is the third osculating system inside S_F. The universal apolar annihilator is l^4 Sym6 W. Consequently the composite factors through

    Sym6 W O(-4)=(V+P)O(-4).                       (6)

This deduction uses the dual injection of a possibly partial coefficient quotient, not an assumed full rational-normal curve in R. By degrees in (5), only V O(-4) can map to (6), and Schur's lemma leaves a scalar channel to V. It is nonzero: otherwise R would be a nonzero constant subspace of S_F subset S.

The sextic net V subset Sym6 W is basepoint-free. A common-zero divisor would be G-invariant of degree at most6, whereas every projective A5 orbit has size at least12: a finite point stabilizer is cyclic by the faithful tangent character, and A5 has no cyclic subgroup larger than5. The evaluation kernel T_V in V O -> O6 has rank2, degree-6, H0(T_V)=0, so T_V=O(-a)+O(-b) with a,b>=1 and a+b=6. Hence a,b<=5 and H1(T_V(4))=0. Thus V tensor Sym4 W -> Sym10 W is onto. Pure fourth powers span Sym4 W, so the subspaces l^4 V span all Sym10 W.

The nonzero channel into (6) forces R* to contain every l^4 V. Therefore dim R=11. The higher-degree rank13 subbundle D O(-2)+(W'+T)O(-3) of F maps to zero in R*, and so injects into the constant kernel of N -> R*, whose dimension is21-11=10. This is impossible.

This proof never uses A_F. In the present case A_F=O2+O4, unlike PR1145's O2+O16. The only residual inputs are the actual source (5), constant ambient21, B_F as displayed, and derivative rank bound. Hence pair32 is excluded without importing the different A-shape theorem.

## 5. Pair52: equivariant determinant gaps

For pair52, deg B=-4 and deg L=-50. Its six capacities are

    -55,-46,-41,-40,-43,-50.

The h=5 bound is too small; h>=8 is excluded by Section2. Only h=6 or7 remain. For an arbitrary rank-two G_j, put

    delta_j=(1-4j)-deg G_j.

The determinant injection lands in

    wedge^2 B(-2j)=W O(1-4j)+O(-10-4j).

The determinant line is standard, since G is perfect. A nonzero component into the W term requires W in Sym^(delta_j) W; a component into the scalar term requires an invariant in Sym^(delta_j-11) W. Ordinary slope gives delta_j>=0. The universal character identities imply W first occurs at degree1 and next at degree11, with no occurrence at any degree2 through10. Therefore

    delta_j=1 or delta_j>=11.                       (7)

This bound applies to every possible determinant image, even one with both components, without selecting a Plucker plane or assuming saturation of the composite image.

For a rank-one G_j=O(e), put epsilon_j=(6-2j)-e. Its injection into B(-2j) has scalar component of invariant degree epsilon_j, or W component of degree epsilon_j-11. There is no positive invariant below degree12, and W first occurs at degree1. Hence

    epsilon_j=0 or epsilon_j>=12.                   (8)

For completeness the invariant gap also follows from the orbit bound above: a nonconstant invariant binary form has a nonempty invariant zero divisor, of degree at least12. Parity and the W occurrences through11 are checked exactly by the pinned character implementation; the underlying identities are Sym1=W, Sym3=S4, Sym5=T, Sym7=W'+T, Sym9=S4+T, Sym11=W+S4+T. Even degrees cannot contain center-odd W.

If h=6, there are four rank-two and two rank-one quotients. The total deficit relative to ordinary capacity is -46-(-50)=4. Equations (7)-(8) force all four delta_j=1 and both epsilon_j=0. In particular the terminal line F_6=G_6 is O(6-12)=O(-6). Its six derivatives belong to S, so Section2's Taylor argument forces a nonzero constant subspace of S. Contradiction. This step does not assume its coefficient system is complete or seven derivatives generically independent.

If h=7, there are three rank-two and four rank-one quotients. Total deficit is -41-(-50)=9. The three mandatory deficits in (7) contribute3, leaving6. Any additional contribution is at least10 from a rank-two quotient or at least12 from a rank-one quotient. A sum equal to6 is impossible. This excludes h=7 and hence pair52.

## 6. Evidence and boundaries

The verifier authenticates all six retained immutable sources, identifies only the two fixed original records, checks source ranks/degrees, both capacity vectors, exact low-degree character gaps, all degree patterns within the relevant deficit budgets, coefficient-space dimension bounds, residual degree sums, all sextic-net splitting possibilities, and universal Taylor inversion in bounded degrees. It does not regenerate the historical enumeration or run any actual source/parameter/jet experiment. The all-degree and geometric proofs are given above; tests are regression evidence, not replacements for them.

This is a two-pair D-source exclusion under maximal profile(1,1). Pair50 and any separate coverage obligation are deliberately not resolved here. A complete checked proof repair is not claimed.
