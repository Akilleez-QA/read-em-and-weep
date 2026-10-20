# Polynomial extension of the actual pure obstruction across branch boundaries

19 October 2026. Formal mathematical record; no obstruction coordinates were evaluated.

## Result and precise dependencies

The proposed codimension-one extension route works. The full PR16 differential algebroid, not merely its bivector, has a regular universal two-jet. The first-order cancellation extends from the original smooth fiber because its class is constant in a canonically fixed pair-character target. At each generic branch-boundary divisor, the actual root-twisted bundle and a first-order lift extend. Consequently the complete pure obstruction extends as a section of the fixed invariant target. Normality and the explicit scaling law make that section a homogeneous polynomial of degree two in A,B,C.

This result uses the already accepted actual first-order cancellation at F0=(1,0,−1), the accepted vanishing of the two pair-character Ext¹ groups at F0, and the specified actual carrier E=f*H⊗N. It does not derive first-order cancellation from Chern numbers alone. It does not assert that the resulting quadratic polynomial, or its value at F0, is zero.

Write R0=C[A,B,C], D=B²−4AC, S=Spec R0[1/(ACD)], and F(x)=Ax³+Bx²+Cx, corresponding to XY(AX²+BXY+CY²). Let B0=(P¹)^4, ρ:B0→P⁴ multiply the four linear factors, M=ρ*End(H), and W=H²(B0,M). The notation B0 avoids confusion with the coefficient B. We construct the separate pure classes Q_P,Q_Q with values in W; their sum has all previously proved permutation/compact-target restrictions. The construction of polynomiality itself does not require a singular-fiber HKR theorem or the smooth invariant characteristic-map vanishing theorem.

## 1. Constant coefficient cohomology, including singular fibers

The universal curve is the finite flat double cover p:C→P¹ with algebra O⊕O(−2) and multiplication prescribed by the branch quartic. In finite and infinite charts it is

    y²=Ax³+Bx²+Cx,
    z²=At+Bt²+Ct³,       t=1/x, z=y/x².

Take the fourfold fiber product X=C⁴ over the parameter base. For every parameter ring R under consideration,

    p_*O_X = ⊕_{J⊂{1,2,3,4}} O_B0(−2 on the factors in J) ⊗ R

as a deck-linearized module. Its algebra multiplication depends on F; this module decomposition does not. Wherever N is an actual line bundle with N²=p*O_B0(1,1,1,1),

    End(E)=p*M,
    H^k(X,End E)_J = H^k(B0,M⊗O_B0(−2 on J)) ⊗ R.

These statements use finite pushforward, the projection formula, and ordinary flat scalar extension from C. They remain true for nodal fibers. They identify all required cohomology modules, not just their dimensions. In particular they are R-free, and the accepted pair-character Ext¹ vanishings persist over every such R.

## 2. The entire PR16 ambient two-jet extends explicitly

The derivation

    V=y∂x+(3Ax²+2Bx+C)∂y/2

preserves the curve relation. At infinity it is

    V(t)=−z,
    V(z)=−(A+2Bt+3Ct²)/2.

It is therefore a global relative derivation even on the singular covers. The four factor derivations commute. Their exponential bidifferential product truncated modulo h³ is associative on every fiber: the proof is the commuting-derivation identity, not smoothness or HKR.

On the overlap of the inverse images of the standard base charts put q=y/x. The exact generalization of PR16 §2 is

    V(q)=(Ax−C/x)/2,
    a0=−Ax/2,       a∞=−C/(2x),
    δa=V(q).

The B coefficient cancels. Both a-components are regular on their respective charts, and q is regular on the overlap. All are polynomial in the branch coefficients in the finite-flat algebra. Set λ=15/4 and use exactly the PR16 conventions:

    b=λ(q1∪q2+q3∪q4),
    sk=Σrs βrs(δkr ar∪qs−δks qr∪as),
    T=Σkl πkl sk Vl.

Then δsk=Vk b and δT={b,−}. Thus

    Fij=id+h²Tij,
    Aijk=1+h bijk+h² bijk²/2

satisfy the full noncentral algebroid descent equations modulo h³, by the same direct identities as PR16 §3. No inverse of A,C,D occurs. Separate pair parameters s,t give the corresponding pure T_P,T_Q and the complete two-parameter two-jet.

This proves regularity of the unary overlap correction and triple unit, not merely of μ1 or μ2. In particular the later source still contains both T_p(g)g and −μ_p(b_p,g).

## 3. Why the actual first-order obstruction is constant in F

Work first over the smooth locus S, where the ordinary Atiyah/HKR first-order formula is legitimate. Put L0=O_B0(1,1,1,1). The actual root satisfies N²=p*L0, so in characteristic zero

    At(N)=½p*At(L0).

By functoriality and the tensor rule,

    At(E)=p*α,
    α=At(ρ*H)+½ id_H⊗At(L0),

with the differential map p*Ω_B0→Ω_X understood. The End-valued base class α is fixed, independently of F; no reduction to its trace is being made.

Contraction of its square with V_i∧V_j inserts the factors y_i y_j because V_i acts on a pulled-back base function as y_i∂xi. Under the canonical pair-character pushforward of §1, the remaining coefficient class is therefore independent of F. Likewise b_p=λq_i∪q_j is y_i y_j times a fixed base coefficient. Hence the full compensated first-order obstruction

    [C1,p]=ev_E(π_p)−[b_p] id

is the same element of the fixed pair-character cohomology space for every F∈S. Its known vanishing at F0 proves vanishing throughout S, including its function-field point.

A cochain explanation confirms that this does not hide a root-line ambiguity. On a fixed base cover trivializing ρ*H and L0, refine étale-locally so chosen N frames square to the chosen pulled-back L0 frames. If g=τh, where h is a base H transition and τ²=l is the base L0 transition, then

    V_i(g)=y_i τ(∂i h+(∂i log l)h/2).

In the normalized first-order residual the scalar transition factors cancel by their ordinary cocycle identity. The result is y_i y_j times a base End-valued expression independent of F. Extra refinement indices within a base chart have h=l=1 and τ=±1, whose derivatives vanish; thus the normalized expression descends. This is only a first-order comparison and does not assume the desired quadratic conclusion.

No assertion that a first-order cancellation at one arbitrary parameter automatically extends has been used. The fixed End-valued Atiyah class, or the displayed root-frame identity, is the missing structural reason it extends here.

## 4. Actual Cartier roots at each generic boundary

Localize R0 at one of its three height-one primes (A), (C), or (D). These are DVRs. The other required coefficients are units at the generic point.

- At (A), C is a unit. The section P0=(x,y)=(0,0) is in the relative smooth locus, so it is an effective relative Cartier divisor. Use N0=O(P0) on each curve factor.
- At (C), A is a unit. The infinity section P∞=(t,z)=(0,0) is relatively smooth and Cartier. Use N∞=O(P∞).
- At (D), A and C are units. Either section is relatively smooth and Cartier; use N∞.

Indeed the derivatives of the respective equations along these sections are C and A up to sign. Pullback of the base divisor 0 or ∞ is twice the corresponding section. Hence these are actual roots of p*O_P¹(1), not formal half-divisors. Their external products give actual N, and E=p*ρ*H⊗N is locally free on the possibly singular fourfold.

On the locus where both roots are available,

    div(x)=2P0−2P∞,
    O(P0−P∞)²≅O.

The comparison is an exact flat two-torsion twist, not a cancellation merely inside End. The associated μ2-torsor is finite étale in characteristic zero, even on a nodal curve. In its frames all transition constants are ±1. Every differential product and overlap derivation used here kills their derivatives. Thus tensoring by this torsion line preserves the entire noncentral module equation, and normalized End-obstructions are unchanged after faithful étale descent. Only the generic smooth comparison is needed at (A) and (C); at (D) it also works on the nodal fiber.

## 5. Extend the first boundary, then the complete obstruction

Over each DVR R just described, choose a finite affine cover of X_R trivializing E and refining the original product cover. Since X_R is separated, the affine intersections are acyclic for the required quasicoherent sheaves. The explicit ambient of §2 restricts to this cover.

The first-order source C1,p is a regular End-valued Čech two-cocycle. Its class belongs to the R-free pair-character cohomology module of §1. By §3 its generic restriction is zero. Torsionfreeness therefore forces the class itself to vanish over R. It follows on the acyclic cover that there is a regular first-order cochain u_p solving the module equation. Deck averaging chooses the prescribed pair character; a deck-stable affine refinement can be used if needed.

Form the complete PR16 pure obstruction symbolically:

    Rpp=u_p,jk u_p,ij
       +μ_p(u_p,jk,gij)+μ_p(gjk,u_p,ij)
       +μ_pp(gjk,gij)+T_p,ij(gjk)gij
       −b_p,ijk u_p,ik−(b_p,ijk²/2)gik
       −μ_p(b_p,ijk,gik),
    Cpp=gik⁻¹Rpp.

Every operation is defined over R. The full descent identities and the first-order equation imply δCpp=0 by expansion of the associative module equation. This proof is valid on the singular fiber and needs no HKR statement there. Hence [Cpp] is a regular element of W⊗R.

On the fraction field, the torsion-line comparison identifies the root choice with the original infinity-root problem. Pair-character Ext¹ vanishing identifies the chosen first-order lift with the stipulated one up to reduction-preserving gauge. The complete induced second-order gauge terms are retained; obstruction classes agree. The ambient is already the explicit same PR16 ambient, so no unsupported singular ambient-independence theorem is needed.

The argument also constructs the regular class over S. The class does not depend on the locally chosen first-order primitive because its admissible differences are pair-character coboundaries. Thus the DVR classes restrict to the same smooth-family class, not unrelated extensions.

## 6. Normality and exact quadratic scaling

We have shown that Q_p on S has no pole at the generic points of A=0,C=0,D=0. It has no other possible divisorial poles, since it is regular on S. The normal-domain intersection identity

    R0=⋂_{height(prime)=1} (R0)_prime

inside its fraction field now applies to each coordinate in the finite-dimensional space W. Therefore Q_p extends uniquely to W⊗R0. No bundle or root construction is required at codimension-two intersections or at the zero quartic.

For c≠0, the isomorphism C_F→C_(c²F), (x,y)↦(x,cy), preserves the chosen root sections. Under pullback, q and V have scale c, a has scale c², μ1 and b have scale c², and μ2,T,b² have scale c⁴. The transformed first-order lift can be taken to be c²u. Every term of the complete pure numerator then has scale c⁴. Any other admissible lift is gauge equivalent by pair-character Ext¹ vanishing. Thus

    Q_p(c²A,c²B,c²C)=c⁴ Q_p(A,B,C).

Over C every nonzero λ is c², so the polynomial has total degree exactly two in the homogeneous sense (the zero polynomial is allowed). This proves universal polynomiality, not merely smooth-locus homogeneity.

## 7. What has and has not been obtained

Established: a homogeneous quadratic polynomial Q_P,Q_Q: C³→W representing the complete actual pure classes, with actual roots, first boundary, noncentral ambient corrections, and generic-boundary comparisons included. The sum specializes to the known diagonal pure obstruction at F0.

Not established here: vanishing of either polynomial, evaluation of any obstruction coordinate, a primitive for the pure second-order source, or a full second-order module lift. A further D5-equivariance deduction must still use the audited HM action and the actual family/root/first-order comparisons, rather than declaring the fixed branch quartic torus-invariant. With those already audited covariance identifications, polynomiality supplies precisely the missing input for the conditional quadratic weight restriction in [branch-covariance-next.md](branch-covariance-next.md). Target dimensions or final nonvanishing/vanishing are not inferred solely from this extension theorem.

## Inspected sources

- [branch-covariance-next.md](branch-covariance-next.md), [pure-target-next.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/b8903f211ef47802a9f701d9e74d3f67377022f2/research/hm/null-pure-square-reduction/pure-target-next.md), [reciprocal-symmetry-audit.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/b8903f211ef47802a9f701d9e74d3f67377022f2/research/hm/null-pure-square-reduction/reciprocal-symmetry-audit.md), [pure-square-next.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/b8903f211ef47802a9f701d9e74d3f67377022f2/research/hm/null-pure-square-reduction/pure-square-next.md); also [pure-ambient-audit.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/b8903f211ef47802a9f701d9e74d3f67377022f2/research/hm/null-pure-square-reduction/pure-ambient-audit.md) and [second-order-implication-audit.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/b8903f211ef47802a9f701d9e74d3f67377022f2/research/hm/null-pure-square-reduction/second-order-implication-audit.md).
- Directly fetched PR16 full source, commit c8aec970fd65a105f39f4e8aeb8a17f0f0053f89, blob a58834ab61e18a5dedd8a7bf20bec7121bfa9165, especially §§2–6 and 8:
  https://github.com/Akilleez-QA/read-em-and-weep/blob/c8aec970fd65a105f39f4e8aeb8a17f0f0053f89/research/hm/second-order-algebroid.md

The general-branch derivative primitive, fixed first-order class argument, DVR extension, and normality/scaling conclusion above are formal deductions, not claims that PR16 itself stated the universal theorem.

## 8. Actual D5 covariance, not just formal polynomial weights

Here we use the accepted binary/HM D5 lifts and target decomposition from [pure-target-next.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/b8903f211ef47802a9f701d9e74d3f67377022f2/research/hm/null-pure-square-reduction/pure-target-next.md). The binary generators have determinant one. Their natural maps between the double-cover families preserve the relative differential dx/y (with the usual y transformation of weight two), hence transport each V_i and each pair bivector to its counterpart. They also preserve the base polarization L0. The torus preserves the infinity root. Reversal exchanges N∞ and N0, requiring exactly the flat two-torsion equivalence of §4.

Accordingly θ=At(N) is preserved after the specified root transport, and the compensated scalar-gerbe class b=−15 ι_π(θ²)/2 is transported correctly. The explicit b representative need not be literally invariant on the same ordered Čech cover. On a common refinement its discrepancy is a scalar coboundary; transport by its actual first-order algebroid equivalence, with the induced second-order corrections retained. Pair-character Ext¹ vanishing then identifies the transported first-order module boundary with the stipulated one up to reduction-preserving gauge.

The remaining difference between the two valid ambient second jets, after those identifications, evaluates by the ordinary characteristic map. Its invariant evaluation is zero on every smooth member of S, not only F0. Indeed on each smooth genus-one fourfold, invariant HH² consists of the four individual curve-complex-structure directions V_i⊗H¹(O_Ci). Varying one branch cross-ratio at a time extends the actual degree-two map, root section, and bundle p*ρ*H⊗N; its nonzero Kodaira–Spencer class spans that direction. Thus each evaluation is zero. This is exactly the geometric proof of [pure-square-next.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/b8903f211ef47802a9f701d9e74d3f67377022f2/research/hm/null-pure-square-reduction/pure-square-next.md) applied at an arbitrary smooth member, using marked branch deformation rather than the possibly ramified coarse j-coordinate. No assertion about singular HH² is made.

Functoriality of the full module obstruction now proves D5 equivariance of Q_P,Q_Q and their sum on S. The transformations do not mix factor pairs. The unique polynomial extension is consequently D5 equivariant everywhere: equality of polynomial maps follows from equality on dense S. The scaling argument in §6 likewise used actual root-preserving curve isomorphisms, exact scaling of the complete ambient, and boundary identification, not the raw vector-field weight alone.

## 9. Six remaining conditions and a boundary coefficient

Let Q=Q_P+Q_Q with its established block-even compact target

    M = H²(P⁴,End₀H⊗(O⊕W O(−1)⊕W² O(−2)))
      =8ε⊕6ρ1⊕6ρ2.

Here ε is the reflection-sign representation; the coefficient lines W,W² are trivial under D5. In the audited convention the branch coefficient representation is

    U=1(B)⊕ρ1(A,C),
    Sym²U=2·1⊕ρ1⊕ρ2.

The two trivial summands are generated by B² and AC. There is no trivial target summand, so equivariance annihilates both. There is also no ε summand in the domain. The only possible pieces are the AB,BC pair in ρ1 and the A²,C² pair in ρ2. Therefore at F0=(1,0,−1), where B=0, only the reflection-even line of each of the six target ρ2 copies survives. The obstruction has at most six independent remaining coordinates:

- two in the canonical W H²(End₀H(−1)) projection;
- four in the canonical W² H²(End₀H(−2)) projection.

This is an exact restriction of the actual class, reducing the preceding twelve-condition target to six. It is not evaluation or vanishing of those six coordinates.

More intrinsically, put v=Q(1,0,0). The A² coefficient lies in one rotation-eigenspace of the six ρ2 copies. Reflection gives Q(0,0,1)=R v, while the AC coefficient is zero. Since (−1)²=1,

    Q(1,0,−1)=v+R v.

The map v↦v+Rv is injective from that rotation eigenspace to the reflection-even sector, because the two nontrivial rotation eigenspaces are distinct. Thus the six coordinates of v determine, and vanish exactly when, the remaining diagonal obstruction does.

The point (A,B,C)=(1,0,0) corresponds to y²=x³, a cuspidal double cover. Its infinity section is still smooth Cartier because A is a unit, so the explicit PR16 ambient and actual N∞ bundle make sense there. In fact the construction with N∞ works over the whole open A≠0: first-order cancellation follows from the same fixed/torsionfree cohomology argument, and pair-character Ext¹ remains zero. Therefore the value v is also the complete obstruction class of this cuspidal boundary problem, not merely an abstract polynomial extrapolation. This identifies a precise further formal or computational target but performs no computation, source evaluation, or vanishing test at that boundary.
