# Independent audit of the branch-boundary extension route

19 October 2026. Formal mathematical record; no obstruction coordinates were evaluated.

## Verdict

The proposed height-one extension argument passes, provided the already imported first-order cancellation at the original smooth carrier and pair-character Ext¹ vanishing are retained. Its previously vulnerable step, passage from cancellation at one branch quartic to cancellation on the generic smooth family, has an actual transition-level proof. Neither singular HKR nor polynomiality of the complete pure source is assumed.

The result is polynomiality of the canonical pure obstruction class, not vanishing. A degree-two scaling law and the audited family symmetries then give the conditional weight restriction previously recorded in [branch-covariance-next.md](branch-covariance-next.md). The restriction can now use this extension proof rather than assuming polynomiality. The target dimensions/representation and numerical reduction are imported from the separate target audit, not recomputed here.

## 1. Proper flat family and roots at the three generic boundary points

Put R0=C[A,B,C], F=XY(AX²+BXY+CY²), and let p:C_F→P¹_R0 be the double cover defined by the O(-2) summand whose square is F. Its algebra is O⊕O(-2). Consequently p is finite locally free of degree two and C_F is proper and flat over R0, including nodal or reducible fibers. The fourfold product has the corresponding finite locally free algebra over B=(P¹)^4. Smoothness is not needed for these assertions.

On x=X/Y, write y²=Ax³+Bx²+Cx. At the height-one local ring (A), C is a unit. The origin section P0 is Cartier: near it,

x(C+Bx+Ax²)=y²,

and the parenthesis is a unit, so (x,y)=(y). Its doubled divisor is p*{0}. Thus N0=O(P0), and its four-factor external product, are genuine root lines with square pulled back from O(1) on each P¹. At (C), the analogous infinity root N∞ is Cartier. At the generic discriminant divisor (B²−4AC), both A and C are units, so both root sections are Cartier. The collision there occurs at another branch point, not at either selected section.

Only the selected root needs to be Cartier in each local model. N0 versus N∞ is compared over the common smooth fraction field; no extension of the missing Cartier root to the other special fiber is claimed or needed.

## 2. Global derivations, including infinity

The relative derivation

Vx=y, Vy=(3Ax²+2Bx+C)/2

preserves the equation. At infinity, z=1/x and w=y/x² give

w²=Az+Bz²+Cz³,
Vz=−w,
Vw=−A/2−Bz−3Cz²/2.

Thus V is globally regular on the entire projective double cover, including its singular fibers. It need not be nowhere zero there. The derivations on distinct factors commute, so the truncated exponential/Moyal product built from them is associative algebraically without smooth HKR.

## 3. The scalar and unary algebroid data really extend

The author's direct inspection of pinned PR16 supplies b=λ(q1 cup q2+q3 cup q4), λ=15/4, with q=y/x. The identities

V(q)=(Ax−C/x)/2,
a0=−Ax/2,
a∞=−C/(2x),
δa=V(q)

hold on the inverse images of the standard two affine charts. a0 and a∞ are regular on their respective charts, with coefficients polynomial in A,B,C; q is regular on their overlap. There is no division by a branch discriminant or by A or C.

The PR16 cup-product primitive s_k and T=Σπ^{kl}s_k V_l therefore extend with δT={b,−}. This is the complete overlap correction, not a claim that it may be omitted. With F_ab=id+h²T_ab and A_abc=exp(hb_abc), the algebroid coherence identities through order two use only the commuting derivations, δb=0, and this displayed δT identity. They remain valid on singular fibers. The terms involving T(g)g, b²g/2, and μ1(b,g) are present in the resulting module residual.

This audit checks the extension logic and the displayed identities; the identification of these conventions with pinned PR16 is imported from the author's direct source inspection, not independently reread here.

## 4. The essential first-order source comparison

It would be invalid simply to say that a unique first lift at F0 must extend, or that an obstruction vanishing at F0 vanishes generically. Here is the actual bridge supplied by the author and independently checked.

Choose a fixed affine base cover refining a trivializing cover for ρ*H and O_B(1,1,1,1). Let h_ab be the fixed matrix transitions and l_ab the fixed transitions of that line. On the selected family root N with N² identified with the pulled-back line, pass étale locally to frames whose squares equal these prescribed base frames. Such frames exist: the ratio between the square of any frame and the prescribed base frame is an invertible function, and adjoining its square root is finite étale in characteristic zero.

Write the actual module transition as g_ab=τ_ab h_ab, with τ_ab²=l_ab. For every relative derivation,

V_i(τ_ab)=τ_ab V_i(l_ab)/(2l_ab).

Hence, in a finite coordinate chart,

V_i(g_ab)=y_i τ_ab(∂_i h_ab + h_ab ∂_i log(l_ab)/2).

All terms inside the parentheses are fixed base data. In the normalized first-order product residual, τ_bc τ_ab cancels against τ_ac. The scalar gerbe contribution b has the same fixed pair-character form because q_i q_j=y_i y_j/(x_i x_j). Consequently the complete normalized first-order obstruction cocycle is the image of a fixed base cocycle in

M⊗O_i(-2)⊗O_j(-2),  M=ρ*End(H),

under the canonical pair-character inclusion. It is independent of A,B,C in that fixed cohomology group. The notation y_i y_j expresses this inclusion in local coordinates; it is not an assertion that these are global functions.

Additional étale indices over a single base chart have h=l=1 and root-frame transitions ±1. Their derivatives vanish, so the normalized expression descends to the fixed base cover. This is the missing effective source comparison, not merely cancellation of N in End or equality of Chern classes.

The imported actual first-order vanishing at F0 therefore kills this same fixed base class for every smooth F. Equivalently a fixed base Čech primitive can be chosen and transported. The argument uses no singular HKR. The smooth Atiyah identity At(N)=p*At(O_B(1,...,1))/2 gives a useful independent class-level explanation, but is not needed in place of the transition proof.

## 5. Why generic vanishing legitimately gives an integral first lift

For any of the height-one local rings R, E_R=ρ_R*H⊗N_R is locally free, and End(E_R)=p_R*M canonically. Finite pushforward gives in every deck character χ_S

H^k(X_R,End E_R)_{χ_S}=H^k(B,M⊗⊗_{i∈S}O_i(-2))⊗R.

These are fixed finite-dimensional complex spaces tensored with R. In particular all are free and hence torsion-free, not merely constant in dimension on closed fibers. This follows directly from the fixed split finite algebra and a base Čech complex, so no singular cohomology-and-base-change theorem is silently assumed.

The full first-order residual is a cocycle over R. Its image over the fraction field is zero by §4, hence its class in this free H² is zero over R. On an acyclic affine refinement trivializing E_R, an integral first-order primitive therefore exists. Finite-group averaging selects its prescribed pair character. The imported pair-character H¹ vanishing identifies any two such first lifts modulo reduction-preserving gauge.

There is no division by the uniformizer in this conclusion. Vanishing over the fraction field alone would not suffice without the explicit free cohomology calculation.

## 6. The complete second-order residual and root comparison

Substitute the integral first lift, the genuine root-twisted transitions, and the extended b,T and Moyal operations into the full module descent equation. Its second-order normalized residual is an integral End-valued Čech cocycle by algebroid coherence. Invariant cohomology is W⊗R. Thus its class has no pole at this height-one point, regardless of denominators that might occur in an unrelated smooth-family gauge.

To identify this integral class with the stipulated smooth class, first compare first-order ambient data and module boundaries. The same b,T model is used. Any first-boundary difference is removed by the imported pair-character Ext¹ vanishing with its induced second-order gauge term retained. If different valid second ambients are used, only on the smooth fraction field invoke the already proved invariant characteristic-map vanishing, after identifying first-order data. No singular version is required.

For N0 versus N∞ over the smooth fraction field, their quotient has square O because div(x)=2P0−2P∞. The associated μ2 torsor is finite étale. In horizontal root frames the transition constants are ±1; relative derivations kill them, so every product, overlap map and triple unit, including the noncentral terms, is intertwined exactly. Faithfully flat étale descent therefore gives the required module equivalence and the identity on End-obstructions. Neither a bare End identification nor unproved quantization of an arbitrary line bundle is being used.

## 7. Hartogs and qualifications

The smooth parameter locus excludes exactly A=0, C=0, and B²−4AC=0. The three local constructions remove the poles at all generic points of those irreducible divisors. A rational W-valued class regular on that smooth locus and at those height-one points lies in W⊗C[A,B,C], since affine three-space is normal. No extension through each individual higher-codimension bad fiber is needed.

The degree-two scaling and D5 covariance must still be applied to the actual identified first-order family, including the root-torsion transport. Once this is done, a homogeneous degree-two regular class is an honest quadratic polynomial. Homogeneity alone on the smooth locus was insufficient, as the earlier counterexamples demonstrated; this proof supplies precisely the previously absent pole-removal statement.

This audit does not establish that the resulting quadratic map or its value at F0 is zero. It does not remove the remaining target coordinates, evaluate them, construct a second-order module primitive.

## Material reviewed

Direct review: [branch-covariance-next.md](branch-covariance-next.md); [pure-target-next.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/b8903f211ef47802a9f701d9e74d3f67377022f2/research/hm/null-pure-square-reduction/pure-target-next.md); [reciprocal-symmetry-audit.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/b8903f211ef47802a9f701d9e74d3f67377022f2/research/hm/null-pure-square-reduction/reciprocal-symmetry-audit.md); [pure-ambient-audit.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/b8903f211ef47802a9f701d9e74d3f67377022f2/research/hm/null-pure-square-reduction/pure-ambient-audit.md); [pure-square-next.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/b8903f211ef47802a9f701d9e74d3f67377022f2/research/hm/null-pure-square-reduction/pure-square-next.md). Additional explicit b,T and square-frame formulas were reviewed alongside the extension proof. All first-order vanishing, pair-character Ext¹ vanishing, HM actions, and fixed target character calculations remain the accepted source premises stated in those reports.

## 8. Additional independent audit: actual homogeneity and D5 covariance

The following closes the qualification in §7, under the same imported smooth-fiber source premises and HM action. It concerns the canonical diagonal pure class o0; the construction and comparisons also apply separately to the pair coefficients.

### Scaling and its square-root ambiguity

For λ≠0 choose c with c²=λ and identify C_F with C_{λF} by (x,y)↦(x,cy). Pullback of the target derivation is cV_F. Therefore the pair bivector and the actual first-order gerbe b pull back to λ times their original values. This identifies the full first-order ambient with the parameter replacement h↦λh, not just its Poisson symbol. The root sections are preserved, so the actual root line and module reduction are identified as well. Pair-character Ext¹ vanishing identifies the transported first boundary up to gauge; any valid second-ambient difference has zero invariant characteristic image after this identification.

Consequently Q(λF)=λ²Q(F) on the smooth locus. The other square root replaces c by −c and differs by simultaneous deck involution. This acts trivially on the canonical invariant target and supplies no monodromy or sign in Q. The scaling identity extends to the polynomial class by dense equality, proving that it has homogeneous degree two.

### SL2 family action, with the reflection normalization checked

For g=[[a,b],[c,d]] in SL2, the natural family map is

x′=(ax+b)/(cx+d),
y′=y/(cx+d)²,
F′=F composed with g inverse.

The binary-form equation transforms correctly, and dx′/y′=dx/y. Hence the relative vector field and pair bivector transport without an additional determinant or character. If coefficient actions are instead written contravariantly, the rotation weights are inverted; this exchanges the two members of each ± weight pair and does not change the conclusion.

In particular the accepted binary reflection [[0,i],[i,0]] gives x′=1/x and y′=−y/x². Its action on binary quartics is ordinary positive reversal, so it exchanges A and C and fixes B. It sends F0 to −F0. It should not be confused with the fixed-curve reciprocal (x,y)↦(1/x,iy/x²): the latter additionally identifies −F0 with F0 by branch scaling, up to a deck sign. The scaling parameter is then −1 at first order and its square is +1 at pure second order. There is no extra reflection sign on the quadratic target.

The first-order scalar gerbe class transports correctly too. The odd H¹(O_C) identifies with H¹(P¹,O(-2)); with its natural SL2 linearization this line is trivial, equivalently by Serre duality with H⁰(O). Thus the q Čech representatives may change by a coboundary, but their cohomology classes and the pair b class have the required family identification. On a common refinement choose the corresponding scalar coboundary equivalence. It is essential to retain its induced second-order terms rather than declaring raw b or T cochains strictly invariant.

The torus preserves the infinity root. Reflection changes it to the origin root. The finite étale two-torsion tensor equivalence of §6 identifies the actual module problems, not merely their End targets. Under the imported HM lift, the resulting action on End-cohomology is precisely the specified D5 target action; scalar HM-lift ambiguities cancel under conjugation. The central element −I in SL2 acts trivially on quartics, on this degree-two y coordinate, and on the End target. There is no residual projective-action ambiguity here.

After these first-order ambient and root identifications, pair-character Ext¹ vanishing fixes the module boundary. Remaining second-order ambient differences evaluate to zero in the invariant target. The latter theorem holds at every smooth F by the same independent branch-variation argument used at F0: deform one elliptic factor through double covers retaining its Cartier root section, extend the genuine bundle by pullback and tensor, and obtain its nonzero one-dimensional complex-structure tangent. Extra finite automorphisms do not kill this tangent. This uses smooth HKR only on smooth fibers and nowhere asserts a singular-HKR extension.

Therefore Q(gF)=gQ(F) on the smooth locus for the binary D5 subgroup. Since Q is polynomial, equality extends everywhere by density.

## 9. Strongest verified target reduction: six conditions

Use the supplied representation data, not a new character computation:

U=span(A,B,C)=1⊕ρ1,
Sym²U=2·1⊕ρ1⊕ρ2,
M=8ε⊕6ρ1⊕6ρ2.

An equivariant homogeneous quadratic Q is a D5 map Sym²U→M. The B² and AC directions are trivial representations and have zero images because M contains no trivial representation. The AB and BC contributions vanish at F0=(1,0,−1). Only A² and C² remain. With the positive quartic reflection normalization above,

Q(F0)=Q(1,0,0)+R Q(1,0,0).

Evaluation at the boundary point (1,0,0) here is evaluation of the extended polynomial, not an assertion that its singular fiber carries the original smooth module problem. The vector Q(1,0,0) has rotation weight twice that of A; its reflection has the opposite weight. Thus Q(F0) lies in the reflection-even part of the ρ2-isotypic sector. The possible weight-zero part is absent, consistently with its being entirely reflection-odd in M.

There are six copies of ρ2, each with a one-dimensional reflection-even line. The remaining allowed space therefore has dimension six, with two dimensions in the twist −1 summand and four in the twist −2 summand. This is the exact reduction from twelve to six. It is not a proof that any of those six actual coordinates vanish. No obstruction coordinate, source product, numerical model, or second-order primitive has been evaluated or constructed in this audit.

### Companion-report check and the optional cusp interpretation

After reading [branch-boundary-extension.md](branch-boundary-extension.md) §§8–9, I accept its exact covariance and six-condition conclusions. Its further interpretation of v at the cusp is also justified, with its explicitly stated extra extension argument: over the entire affine parameter open A≠0, the infinity root remains Cartier, all character cohomology is fixed/free, and the same vanishing first-order class admits a regular primitive. The complete residual therefore defines a regular class there and agrees with the polynomial on the dense smooth locus. Specialization at (1,0,0) consequently does identify v with the complete obstruction of that cuspidal algebroid-module problem. This is an extension/identification result, not an evaluation of v.

The map v↦v+Rv is injective from its single nontrivial rotation eigenspace because the reflected eigenspace is distinct. Thus v=0 is equivalent to vanishing of the original diagonal class after the proved reductions. No claim that v is zero has been made.
