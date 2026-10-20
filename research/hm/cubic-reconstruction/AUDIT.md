# Audit of canonical cubic splitting and reconstruction

This preserves the two October 19 audits in source order. It certifies the stated algebraic identities and conditional reconstruction, not the vanishing of the actual obstruction. See [PROOF.md](PROOF.md) for public provenance and chronology. The historical thirty-unknown statement is not a claim about later symmetry reductions.

## Part I: Splitting audit

### Verdict

The proposed correction is valid over the characteristic-zero base of the existing argument. The prior report [filtration-only statement](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6276362114) correctly says that the abstract sheaf isomorphism type alone supplies no preferred splitting. Its stronger conclusion that the actual algebra-equipped problem has no unconditional canonical twenty-dimensional projection must be withdrawn. The multiplication and normalized algebra trace on the even algebra supply one.

This audit independently checks the argument from the stated splitting type and universal binary-quadratic algebra. It does not establish vanishing of either detector. At this October 19 stage, all thirty actual retained conditions remained unknown.

### 1. Intrinsic maps and constant lines

Let A=(m_*O_X)^+, let tr_6 denote the rank-six algebra trace restricted to A, and put G=ker(tr_6|_A). Since tr_6(1)=6, the unit gives the canonical splitting A=O_Y⊕G. The admitted splitting type is A≅O⊕O(−1)⊕O(−2).

Set W=H^0(G(1)), a one-dimensional vector space, and L=W⊗O(−1) with its canonical evaluation inclusion into G. Define a map

    j_2: W^{⊗2}⊗O(−2) → G,
    j_2(u v) = ev(u) ev(v) − (1/6) tr_6(ev(u) ev(v))·1.

Here the expression is interpreted as a twisted sheaf map: ev(W) consists of sections of G(1), their products lie in A(2), and the trace is a section of O(2). Thus the centered product lies in G(2), with precisely the required twist. No trivialization of O(1), W, or a determinant line is implicit.

For a chosen nonzero σ∈W, its image is

    τ = σ² − m^*(tr_6(σ²)/6) ∈ H^0(X,O_X(2,2)),

viewed equivalently in H^0(G(2)). The pullback in this formula is understood when working on X. Rescaling σ by c rescales τ by c². Therefore j_2 and its image line are independent of the chosen generator. The restriction of tr_6 to A equals twice the rank-three algebra trace, as can be checked on the dense étale locus and extended as an equality of sheaf maps. Centering by tr_6/6 is consequently the same as centering by tr_A/3.

### 2. The determinant proof is global and noncircular

Form

    Φ: O ⊕ (W⊗O(−1)) ⊕ (W^{⊗2}⊗O(−2)) → A,
    (r,s,t) ↦ r·1 + ev(s) + j_2(t).

Its source determinant is W^{⊗3}⊗O(−3); its target determinant has isomorphism type O(−3). Hence det Φ is a section of a degree-zero line bundle. Equivalently, if D=H^0(det A(3)), this determinant is an element of the constant line D⊗W^{−3}. A nonzero such section is nowhere zero on P^4. Establishing generic nonvanishing therefore proves that Φ is an isomorphism everywhere. This does not assume a preexisting canonical identification D≅W³; the nonzero determinant supplies that identification.

To verify generic nonvanishing, work on the monic separable-quartic chart with roots a,b,c,d. The values of σ on the three unordered quadratic partitions are

    s_12|34=(a+b)(c+d)−2(ab+cd),
    s_13|24=(a+c)(b+d)−2(ac+bd),
    s_14|23=(a+d)(b+c)−2(ad+bc).

Direct subtraction gives

    s_12|34−s_13|24=3(a−d)(c−b),
    s_12|34−s_14|23=3(a−c)(d−b),
    s_13|24−s_14|23=3(a−b)(d−c).

These are nonzero for distinct roots in characteristic zero. In the étale fiber A_y≅k³, the columns 1,σ,τ have the same determinant as 1,σ,σ²: subtracting a scalar multiple of the first column leaves the determinant unchanged. This is the nonzero Vandermonde determinant in the s-values. Thus det Φ is nonzero generically and consequently nowhere zero.

It follows that K=im j_2 is a line subbundle, canonically isomorphic to W²⊗O(−2), and

    G=L⊕K,
    K → Q=G/L is a canonical isomorphism.

### 3. Branch fibers do not invalidate the splitting

The Vandermonde computation is used only to prove generic nonvanishing of the global determinant section. Its expression in the basis of point-evaluations is not a regular frame comparison through a branch point: that evaluation basis ceases to be a basis there. At branch fibers, the cubic algebra can be nonreduced, and nilpotents retain the rank lost by evaluation on reduced points.

Likewise, the algebra trace pairing may degenerate without a chosen algebra basis degenerating. With the author's conventions I=12ae−3bd+c² and J=72ace+9bcd−27ad²−27b²e−2c³, the supplied cubic relation σ³−3Iσ−J=0 gives tr_6(σ²)=12I and τ=σ²−2I. In the global basis (1,σ,τ), the trace Gram matrix is

    [[6,0,0],[0,12I,6J],[0,6J,12I²]],

whose determinant is 216(4I³−J²). This determinant belongs to the determinant line appropriate to a bilinear form, of positive degree, and can vanish on the discriminant. It is not det Φ. No inversion of this Gram matrix, discriminant, or Jacobian is justified globally or needed anywhere in the argument.

### 4. Duality gives two unconditional detectors

The canonical splitting yields

    H²(B₀⊗G^∨⊗ω_Y)
      ≅ W^∨⊗H²(B₀(−4))
         ⊕ (W^{⊗2})^∨⊗H²(B₀(−3)).

The dimensions of the two factors are the imported 10 and 20. Intrinsically the components are restriction to L and restriction to K. Their descriptions do not require choosing σ; choosing σ evaluates their W-dual factors and presents them as ordinary cohomology classes.

Under finite duality m_*ω_X≅Hom(m_*O_X,ω_Y), the duality trace is evaluation at the unit. For any local coefficient a and dualizing section λ,

    Tr_m^ω(aλ)=(aλ)(1)=λ(a).

Consequently, for the actual retained class represented on X by C_X, its two coordinates are

    Tr_m^ω(σ C_X) ∈ H²(Y,B₀(−4)),
    Tr_m^ω(τ C_X) ∈ H²(Y,B₀(−3)).

There is no factor 1/6 in these duality-trace formulas. The factor 1/6 belongs only to the algebra-trace centering defining τ. These coefficient maps are regular across the branch divisor because finite duality does not require an étale trace-pairing inverse.

The two classes vanish jointly if and only if the entire retained obstruction vanishes. At cochain level this is equivalently the existence of regular one-cochains p,q satisfying

    δp=Tr_m^ω(σ c_X),
    δq=Tr_m^ω(τ c_X).

Both tests are unconditional. If the first vanishes, the second agrees with the old staged twenty-dimensional class after the canonical identification K≅Q. If the first does not vanish, the second is still a well-defined canonical component, which the prior filtration-only treatment did not furnish.

### 5. Limits and exact correction

The result repairs the coefficient-sheaf decomposition and furnishes an explicit canonical twenty-dimensional detector. It does not give primitives for either weighted source, evaluate the physical mixed class, or reduce the number of unknown conditions. The previous filtration, first detector, and conditional second-stage criterion remain valid; only the claimed absence of an unconditional algebraic complement and projection is superseded.

 The only matrix discussed is the universal scalar trace pairing of a rank-three algebra, checked algebraically from its cubic relation.


## Part II: Reconstruction audit

### Verdict

The proposed coefficient-extraction dual basis and reconstruction formula are correct. They give a regular, globally well-defined primitive **provided the three coefficient primitives are actually supplied** in their proper twists. The rank-six extension is valid only for the block-even dual summand. Any discrepancy between that retained cochain and the actual mixed cocycle must be repaired by explicit comparison boundaries. The mixed correction is the negative of the reconstructed primitive.

This audits the proposed universal step independently from the author’s draft. Its dependencies are Part I of PROOF.md and [complete mixed source and correction equation](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6271101716). No actual obstruction vanishing or value is established; all thirty retained values remained unknown at this October 19 stage.

### 1. Exact local algebra

Over a characteristic-zero base ring, take

    A = R[z]/(z³ − 3Iz − J),   tau = z² − 2I.

The ordered basis is (1,z,tau), and epsilon extracts the tau coefficient, equivalently the z² coefficient. The supplied multiplication table gives

    epsilon(1)=epsilon(z)=0, epsilon(tau)=1,
    epsilon(z²)=1, epsilon(z tau)=0, epsilon(tau²)=−I.

Thus the coefficient-extraction pairing has Gram matrix

    H = [[0,0,1],[0,1,0],[1,0,−I]],
    H^−1 = [[I,0,1],[0,1,0],[1,0,0]],
    det H = −1.

Direct multiplication of these two displayed matrices gives the identity over the universal polynomial ring. The dual elements to (1,z,tau) are consequently (tau+I,z,1). For any R-module F and lambda in Hom_R(A,F), using the module action (a lambda)(b)=lambda(ab),

    lambda = epsilon · [(tau+I)lambda(1) + z lambda(z) + lambda(tau)].

Here epsilon with F-valued coefficients means the natural F-linear extension. Evaluation on each of the three basis elements verifies the formula. No inverse of I, J, a quartic coefficient, or a discriminant occurs.

### 2. Global line factors and twists

Keep the canonical line L = W tensor O_Y(−1) and K=L² = W² tensor O_Y(−2). The algebra splitting is A=O_Y direct-sum L direct-sum K. Let pi_K:A→K be its canonical projection. The intrinsic perfect pairing is

    A tensor A → K,     (a,b) ↦ pi_K(ab).

Accordingly the correct global isomorphism is

    A tensor K∨ → A∨,
    a tensor eta ↦ [b ↦ eta(pi_K(ab))].

In particular, coefficient extraction is not an untwisted global scalar functional without a choice of frame. It is the local expression of the K-valued projection; its scalar versions are local generators of the K∨ factor inside A∨.

To check gluing explicitly, replace a local frame z of L by z'=u z, with u an invertible base function. Then

    tau'=u² tau, I'=u² I, J'=u³ J, epsilon'=u^−2 epsilon.

The coefficient I is locally the value of a section of L^−2 on z², and similarly J comes from L^−3. This transformation includes both projective-chart and constant-W frame changes.

For a coefficient sheaf F, the evaluation components of lambda in F tensor A∨ belong intrinsically to

    lambda(1): F,
    lambda|_L: F tensor L∨,
    lambda|_K: F tensor K∨.

Their local values on z and tau transform by u and u². Consequently every term inside the reconstruction brackets transforms by u² and cancels epsilon’s u^−2 transformation. This proves global well-definedness.

For the finite-duality coefficient F=B_0 tensor omega_Y used by the retained detector, the three primitive complexes have coefficient sheaves

    F,
    B_0 tensor W∨ tensor O_Y(−4),
    B_0 tensor (W²)∨ tensor O_Y(−3),

respectively, since omega_P4=O(−5). In particular the second weighted component has twist −3, not −2.

### 3. Ramification and trace normalization

The determinant −1 proves perfection on every fiber of the monic cubic algebra, including nonreduced and ramified fibers. This pairing is not the algebra-trace pairing. The latter degenerates on the discriminant, which has no bearing on this calculation.

There is a useful exact consistency check:

    epsilon((tau+I)a) = Tr_3(a)/3 = Tr_6(a)/6,    a in A.

Both sides take values (1,0,0) on (1,z,tau). Thus the constant-component summand of the reconstruction is already correctly normalized. It must not be multiplied by an additional 1/6. This identity does not identify epsilon itself with normalized trace: epsilon(1)=0 whereas normalized trace(1)=1.

The finite-duality trace is evaluation at 1, not normalized algebra trace. For a finite-duality functional lambda and a in the algebra, it is lambda(a) after multiplication by a. Hence no 1/6 belongs in the weighted evaluation or primitive formula.

### 4. Rank-six extension and its exact scope

Let s be block swap on B, and e+=(1+s)/2:B→A=B+. Since a in A is invariant, e+(ab)=a e+(b). Thus e+ is A-linear and sends 1 to 1. It is not generally an algebra homomorphism, which is unnecessary here.

Define epsilon_B=epsilon_A composed with e+. Restriction and extension give mutually inverse identifications

    Hom(B,F)+ ↔ Hom(A,F),
    lambda_A ↦ lambda_A composed with e+.

For an invariant functional lambda_B the same reconstruction is therefore valid with epsilon_B and its evaluations on 1,z,tau. Indeed it reconstructs its restriction to A, and both sides annihilate B−. For a general functional the formula reconstructs only lambda_B composed with e+, its even projection. It says nothing about the odd part and does not make epsilon_B a Frobenius generator for the whole rank-six algebra.

The only factor 1/2 in this extension comes from block averaging. It is unrelated to either Tr_3/3 or Tr_6/6.

### 5. Primitive reconstruction and sign

Work on a common acyclic cover with the actual sheaf differentials and line transitions included. Suppose lambda is a closed degree-two cochain in the even finite-duality summand, and genuine degree-one cochains p_0,p_1,p_2 in the three complexes of section 2 satisfy

    delta p_0=lambda(1),
    delta p_1=lambda(z),
    delta p_2=lambda(tau).

Then

    q=epsilon_B · [(tau+I)p_0 + z p_1 + p_2]

is a regular degree-one cochain and delta q=lambda. This follows because reconstruction is a morphism of coefficient sheaves, so commutes with the Cech differential. The formula requires no evaluation at geometric roots and no etale restriction.

If lambda(1)=0 literally at cochain level, one may choose p_0=0. If only its cohomology class vanishes, p_0 must still be found and included. An assertion of class vanishing supplies existence on an acyclic cover, not a displayed primitive or a computable correction.

The normalized mixed defect from [complete mixed source](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6271101716) is C and the correction equation is delta x=−C. Therefore, after transporting q back through the specified finite-duality/cochain identification, the mixed correction is x=−q, not q. If comparison boundaries h are needed, it is x=−(h+q).

### 6. Boundaries that cannot be silently discarded

There are three distinct normalizations, which must not be conflated:

1. Matrix tracefree normalization on End(E).
2. Block-even projection on the rank-six finite algebra dual.
3. Removal of the unit-evaluation component to retain the two weighted components.

Class-level membership in these summands does not imply literal cochain-level membership. A general audit-safe statement is: if lambda_full−lambda_ret=delta h with an explicitly specified degree-one h, and q_ret is the reconstructed primitive of lambda_ret, then q_full=h+q_ret is a primitive of lambda_full. One needs all comparison boundaries accumulated through the chosen reductions, with their signs and transport maps.

For example, [complete mixed source](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6271101716) gives, for rank-two E,

    delta k=tr(C),
    C_0=C−delta[(k/2)Id_E].

Thus a primitive q_0 of C_0 yields the primitive (k/2)Id_E+q_0 of C and the correction −(k/2)Id_E−q_0. Knowing H²(X,omega_X)=0 alone does not display k.

Similarly, if only the odd class vanishes, an odd primitive must be supplied before claiming reconstruction of the full cocycle. If only the constant class vanishes, its primitive p_0 must be supplied. Matrix tracefreeness alone does not force lambda(1)=0.

A related weight substitution also requires care:

    lambda(tau)=lambda(z²)−2I lambda(1).

If delta p_0=lambda(1) and delta p_square=lambda(z²), then the correct primitive for the tau component is p_2=p_square−2I p_0, with the indicated twists. Merely replacing tau by z² because the constant class is known to vanish loses a cochain boundary.

If pushforward, duality, projection, or change of cover is represented only up to cochain homotopy, its comparison homotopy must also be included. A sheaf-level or consistently chosen strict cochain identification avoids an additional discrepancy; a cohomology isomorphism by itself does not provide an explicit lifted cochain.

### Scope and stopping point

This establishes an unconditional regular reconstruction operator and a conditional primitive formula. It does not supply p_1 or p_2 for the actual obstruction, does not establish that their classes vanish, and does not evaluate any of the thirty retained conditions. Only symbolic scalar algebra and sheaf/line-bundle reasoning were used.
