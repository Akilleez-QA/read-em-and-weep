# Conditional τ=2 central gluing and full-Artin rank gates

This is a conditional statement about the normalized block specified below. Normalization is an explicit hypothesis; no reduction of arbitrary families to this block is asserted. Both support partitions of the length-two divisor are retained. The result concerns central gluing, isotropy, and rank gates only, with the actual weighted symplectic bundle W. It contains no splitting classification, branch exclusion, global construction, stability conclusion, or mixed-Atiyah conclusion.

## 1. Hypotheses and the intrinsic bad divisor

Work on X=P¹×P³ over an algebraically closed field of characteristic zero. Let p be the first projection and set

    E=O(-5,1)⊕O(-3,1), T=O(-2,2)⊕O(-1,1),
    W=O(c,0)⊕O(-c,0), c≥0,
    L=[[ell,h],[0,a]], J=[[0,1],[-1,0]].

The symplectic rank-two W is written in local base frames with the displayed J. The central quotient below is independent of c; actual first-stage data still depend on c.

The bidegrees of ell,h,a are (3,1),(1,1),(2,0). Assume a is nonzero and the coefficient row of ell has no common zero on P¹ (primitivity), so Y={ell=0} is a P²-bundle. No splitting type of its rank-three quotient U=p_*O_Y(0,1) is fixed or classified here.

Let A=V(a)⊂P¹, a length-two Cartier divisor, either two reduced points or one double point. We require ell and h to be independent linear forms at every reduced point of A. Independence on the reduced fibers implies the needed regular sequences over the full Artin divisor, including a double point; no extra jet-independence assumption is made.

Thus

    Lambda=V(a,ell,h)⊂X

is a P¹-bundle over A, and (a,ell,h) is a regular sequence. On Y the pair (a,h²) is also regular. All ideals in this note are scheme-theoretic. Replacing a double a by its reduced equation, or replacing h² by h, changes the answer.

If ell,h fail independence at a reduced bad fiber, the following Koszul presentation need not apply: that locus is outside the hypotheses.

## 2. The primary condition and local sufficiency

Write a local central matrix as R=[[r,u],[v,w]]. Its entry bundles are

    r:O(-7,3), u:O(-5,3), v:O(-6,2), w:O(-4,2).

Let

    d(R)=a u-ell v-h w ∈ det T=O(-3,3),
    M=ker(d:T⊗E→det T).

For an actual first-stage lift Q_i, put f_i=(Q_i J Q_iᵗ)₁₂. Local isotropy is d(R_i)=f_i. The image sheaf of d is precisely I_Lambda det T. Therefore the necessary primary condition is

    f_i|Lambda=0 scheme-theoretically.                         (P)

It is also sufficient to find R_i over each entire affine-base chart. Indeed the homogeneous syzygies are

    u=ell b+h c, v=a b+h d₀, w=a c-ell d₀,

with ambiguity (b,c,d₀)↦(b+h k,c-ell k,d₀-a k). Their bundles give the exact Koszul resolution

    0→O(-9,1)
      →O(-7,3)⊕O(-8,2)⊕O(-6,2)⊕O(-7,1)→M→0,
    k↦(0,h k,-ell k,-a k).

All relative degrees are nonnegative. Consequently M has no positive cohomology on an affine-base chart times P³, or on an overlap. The exact sequence with I_Lambda det T gives chartwise solvability of d(R_i)=f_i.

Since L|Lambda=0, the primary restriction is unchanged by replacing Q_i by Q_i+L A_i. It glues to a section of det T|Lambda. Its space has dimension

    h⁰(Lambda,det T|Lambda)=length(A)·h⁰(P¹,O(3))=2·4=8.

For a double point these are value-and-jet conditions on the whole nonreduced Lambda. Merely imposing four reduced-fiber coordinates loses four conditions. The statement is a dimension of the target, not an assertion that the eight quadratic equations are independent.

## 3. Complete elimination of the central linear system

The sheaf map Sym²E→M, S↦LS, is injective: L is invertible over the function field. Define

    N=M/(L Sym²E).

Subtracting L[[0,b],[b,c]] from a syzygy matrix leaves

    R(r',d₀)=[[r',0],[h d₀,-ell d₀]], r'=r-h b.

Its exact relations are

    (r',d₀)=(ell s+h² k,a k).

The regular-sequence syzygy calculation proves surjectivity onto N. Conversely, if R(r',d₀)=L[[s,b],[b,c]], then a b=h d₀. Since h is a nonzerodivisor modulo a, d₀=a k and b=h k; the other entries force c=-ell k and r'=ell s+h² k. Hence there are no omitted relations. We obtain

    0→O(-10,2)⊕O(-9,1)
      --[[ell,h²],[0,a]]-->
      O(-7,3)⊕O(-7,1)→N→0.                         (N1)

The first map is injective since its determinant is a ell. This is a sheaf-local elimination and does not assert a globally split middle symplectic bundle.

Let D⊂Y be defined by the exact ideal (a,h²). The map

    (r',d₀)↦a r'-h²d₀ mod ell

has image I_{D/Y}O_Y(-5,3). Its kernel is represented by (0,ell z); its annihilator is exactly (a), by regularity of (a,ell). Since z has bidegree (-10,0), there is an exact sequence

    0→j_*j*O(-10,0)→N→I_{D/Y}O_Y(-5,3)→0,        (N2)

where j:A×P³→X. The left term is the entire base-torsion subsheaf. In particular, for double a it is the full length-two torsion module, not two reduced copies or a length-one replacement. Its cohomology is h⁰=2, hⁱ=0 for i>0.

For comparison, the first-stage quotient K=coker L has the analogous exact sequence

    0→j_*j*O(-4,0)→K→I_{Lambda/Y}O_Y(0,2)→0.

Thus its vertical torsion has dimension two for each section of K; the actual first-stage datum in Hom(W,K) retains four torsion scalars, two in each weighted column. They change local Q_D by ell times a section over A, so they do not affect (P), but they must be retained when evaluating the central obstruction. No uniform claim about the total dimension h⁰(K) is needed here.

## 4. The half-corrected obstruction is necessary and sufficient

Use the symplectic form and transition

    Omega=[[0,0,I],[0,J,0],[-I,0,0]],
    g(V,S)=[[I,VᵗJ,S+(1/2)VᵗJV],[0,I,V],[0,0,I]], S=Sᵗ.

Then gᵗOmega g=Omega and beta=(L,Q,R) is isotropic exactly when

    R Lᵗ-L Rᵗ-Q J Qᵗ=0.

Assume (P) and choose any chartwise solutions R_i⁰. With the actual first-stage transition Q_j=Q_i+L VᵗJ, define

    C_ij=R_j⁰-R_i⁰-Q_iV-(1/2)L VᵗJV.              (C)

The full identity gives C_ij∈M. Its image defines

    omega(Q,V)=[C_ij]∈H¹(X,N).                      (O)

The half correction is essential. Omitting it leaves a quadratic skew error and does not define this central obstruction.

All expressions on an overlap are written after transporting E, T, and W to the same local frames using their actual diagonal bundle transitions. The displayed g(V,S) is the unipotent factor after those diagonal transitions, not a global trivialization. In particular the W transition diag(t^c,t^(-c)) preserves J, and the identities are equivariant under it. Explicitly, the two Q columns have row bidegrees ((-2-c,2),(-1-c,1)) and ((-2+c,2),(-1+c,1)). The V rows have bidegrees ((c-5,1),(c-3,1)) and ((-c-5,1),(-c-3,1)), since V is in Hom(E*,W). The local Q and V coordinate spaces depend on c; replacing them by their c=0 spaces is not justified. None of the construction of M, N, or their cohomology depends on that replacement.

Changing R_i⁰ adds an M-coboundary. Arbitrary changes of the first-stage lifts also preserve the N-class, provided their central local matrices are transformed by the corresponding symplectic gauge. Explicitly put B(V)=(1/2)VᵗJV and

    H(V,W)=(1/2)(VᵗJW-WᵗJV), which is symmetric.

For Q_i'=Q_i+L U_iᵗJ, use R_i'=R_i+Q_iU_i+LB(U_i) and V'=V+U_j-U_i. Direct multiplication gives

    C_ij'-C_ij=L[-H(U_i,V)+H(V,U_j)-H(U_i,U_j)],

so the classes agree in N.

The two affine-base charts and their overlap are acyclic for M, Sym²E, and N, using the displayed positive-relative-degree resolutions. If omega=0, lift an N-coboundary to local sections of M; this is possible because H¹(Sym²E) vanishes on each chart. Adjust R_i⁰ by those sections. The new C_ij is uniquely LS_ij with S_ij symmetric, giving the desired central transition. Conversely any completed central gluing makes the N-cocycle zero. Inverses supply reverse transitions, and this two-open cover has no three-distinct-open cocycle condition.

Therefore (P) and omega=0 are jointly necessary and sufficient for central gluing and isotropy, conditional on the fixed first-stage data and normalized block. They are not sufficient for rank two, and no vanishing of omega is asserted here.

## 5. Completion parameters and the two rank gates

Fix the actual first-stage data Q_i,V, including all first-stage vertical torsion. Once (P) and omega=0 hold, framed central completions modulo local symmetric changes of splitting form a torsor under H⁰(N). This follows by taking differences of completed R_i and using chartwise surjectivity M→N. It is not a count of all monad isomorphism classes modulo further automorphisms.

There are always exactly two base-torsion directions inside this space. With z a local lift of a section over A, their representative is

    Delta R=[[0,0],[h ell z,-ell²z]].

For a invertible this equals L times the symmetric matrix

    [[-h²z/a,h ell z/a],[h ell z/a,-ell²z/a]].

It is therefore rank-ineffective on ordinary fibers modulo a splitting change. It also vanishes identically on Y over every reduced exceptional point, so cannot repair rank there. For double a, a torsion coefficient divisible by the local base parameter has zero reduction and cannot change the rank anywhere on that reduced exceptional fiber. The torsion is nevertheless a genuine length-two deformation parameter and must be retained in gluing.

Any remaining completion directions are non-torsion. They must not be discarded and, unlike the two torsion directions, may change the ordinary rank test. The sharper exceptional argument below shows that no central parameter, including these non-torsion directions, changes the exceptional rank outcome once isotropy holds.

### Ordinary locus a≠0

Define q=a Q_C-h Q_D and rho=a R_C1-h R_D1. Elementary pivot elimination and isotropy give the exact localized ideal identity

    I₂([L,Q,R])=(ell,q_+,q_-,rho) after inverting a.

Here q_± has bidegree (∓c,2), with the column signs matching W=O(c,0)⊕O(-c,0), and rho has bidegree (-5,3). Thus on every ordinary fiber Y_t=P² the exact condition is that q_+,q_- be a regular pair and rho be nonzero at every point of their length-four complete-intersection scheme. Equivalently, after trivialization rho is a unit in every corresponding local Artin ring. Testing geometric support detects this condition; the complete-intersection scheme itself may be nonreduced.

Regularity of the pair is necessary: if their common zero set has a positive-dimensional projective component, a cubic has a zero on that component, forcing rank drop. Away from Y_t, L is invertible already. For a family-wide check one must exclude rank drop over the entire open a≠0, not merely at finitely many sampled fibers.

### Exceptional locus: a sharp first-stage gate

Fix a reduced point of A and trivialize all base lines. Let C=(C₁,C₂)=Q_C and D=(D₁,D₂)=Q_D there. The following are equivalent, for an isotropic completion:

1. [L,Q,R] has rank two everywhere on that P³.
2. D₁,D₂ are an invertible constant linear recombination of ell,h, and C₁,C₂ have no common zero on the line Lambda={ell=h=0}.

In particular, the exceptional rank outcome is determined entirely by first-stage data and is independent of every central completion parameter.

For necessity, row D of the full matrix is (0,0,D₁,D₂,v,w) and must be nowhere zero. If its two linear forms are dependent, their common zero locus contains a P², on which two quadrics v,w have a common zero. Thus D₁,D₂ are independent and cut out a line K. The quadrics v,w have no common zero on K, and isotropy restricts there to

    ell|K·v|K+h|K·w|K=0.

Two coprime binary quadratics admit no nonzero degree-one syzygy, so ell|K=h|K=0. Hence K=Lambda and D is an invertible linear recombination of ell,h. Write

    D₁=b₁₁ ell+b₁₂ h, D₂=b₂₁ ell+b₂₂ h, det B≠0.

The isotropy equation then gives, for a linear form z,

    v=-b₂₁ C₁+b₁₁ C₂+h z,
    w=-b₂₂ C₁+b₁₂ C₂-ell z.

On Lambda, the pair (v,w) is the displayed invertible transformation of (C₁,C₂). Rank two there is therefore equivalent to C having no common zero there. Conversely, outside Lambda the positive row (ell,h) and the nonzero row D in the W columns force rank two. On Lambda, the nonzero C lies in the W block while the nonzero transformed pair (v,w) lies in the R block, again forcing independence. This proves sufficiency as well.

One may equivalently verify the full minors: on each exceptional reduced P³, saturation of I₂([L,Q,R]) by the entire irrelevant ideal must be the unit ideal. The sharper first-stage criterion proves this without searching central parameters. Checking only a chosen coordinate chart is insufficient.

For double a, the reduced-fiber rank test is also sufficient for surjectivity over the thickened base by Nakayama; there is no independent derivative-rank condition. The nonreduced structure remains essential to the primary equations and central gluing even though rank is detected on residue fields.

There is also a useful full-Artin strengthening. Once the reduced exceptional C₁,C₂ have no common zero on Lambda, the map on relative binary forms

    (D₁,D₂)↦C₁D₂-C₂D₁: O_Lambda(1)²→O_Lambda(3)

is an isomorphism on the four-dimensional spaces of sections at every reduced bad point: its matrix is the invertible binary Sylvester matrix. After choosing base-line trivializations over A, its determinant remains a unit over A. The full primary equation therefore forces D₁,D₂ to vanish on Lambda over A, not merely over its reduced support. Equivalently Q_D lies in the O_A-span of ell,h, and its coefficient matrix is invertible over A because its reduction is invertible. This jet constraint is already part of (P); it is not a missing extra rank gate.

## 6. Reproducible checks and evidence boundary

Run `python run_checks.py` in this directory after installing `requirements.txt`. The two standalone scripts import no earlier verifier or stored tensor:

- `verify_central.py` checks symplectic isotropy, the half correction and lift-gauge identities, the quotient/torsion relations, the ordinary determinantal ideal after inverting a, and the exceptional transform.
- `verify_artin_weighted.py` checks the W-transition covariance with a symbolic invertible diagonal weight, the actual Q/V column degrees, and the full binary Sylvester operator over both Q[e]/(e²-e) and Q[e]/(e²). It includes negative controls that lose a component or a first jet if only one reduced fiber is checked.

The proof above establishes the conditional equivalences. The exact tests certify the stated polynomial identities and Artin models; they do not solve the primary or central zero locus, provide a globally surjective family, classify splittings, or exclude branches. No automated CI result is implied by the recorded local output.

Public context: [carrier dependencies, issue #52](https://github.com/Akilleez-QA/read-em-and-weep/issues/52), [τ=1 focused contribution, PR #53](https://github.com/Akilleez-QA/read-em-and-weep/pull/53). This τ=2 note is self-contained and does not modify or depend on the τ=1 contribution.
