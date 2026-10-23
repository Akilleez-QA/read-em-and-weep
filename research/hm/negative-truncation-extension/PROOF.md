# Exact obstructions to extending the negative HM truncation

Status: deductive interface theorem and failed-route certificate. This document
does not exclude source2. It proves that its nontrivial pencil endomorphisms
cannot extend to degree-zero endomorphisms of the full adjoint module, and gives
an exact, different criterion for extending its subpencil filtration as graded
submodules. No actual tensor, coefficient, point, parameter or rank is evaluated.

## 1. Immutable inputs and notation

All paths below are in Akilleez-QA/read-em-and-weep.

| Input | Commit | Path and use |
|---|---|---|
| PR476 | `3aa461bc3581fb72fbf923fbe869ddee023b435a` | `research/hm/five-generator-module/PROOF.md`, §§3–4: actual cohomological module generated in degree zero; unique Euler relation in degree one. |
| PR481 | `6b20de2e4a06e7553bf2d59480cd6c02536f70a3` | `research/hm/quartic-scalar-exclusion/PROOF.md`, §4: complete relation module generated in degrees one, two and possibly three. |
| PR758 | `063216038f3aefd65617651c2426721efafc7f9b` | `research/hm/order-four-quadratic-load/POSITIVE-DOUBLE-HYPERPLANE-GAUSS-GATE.md`, §§1–2: the actual fixed negative multiplication arrows on the indicated inversion eigenspaces. |
| PR790 | `af0e03d26da5e47d18ae732291aca46f4d448dc5` | `research/hm/source2-first-constant-block/PROOF.md`, §§6–7: simultaneous actual-source transfer and the proper degree-ten projector. |
| PR791 | `2cd033a4a5ba549d07330427cd779364cb83c0fb` | `research/hm/source2-pencil-endomorphism-algebra/PROOF.md`, §§5–7: complete pencil algebra, its two-dimensional square-zero radical, full faithfulness and actual-source boundary. |
| PR795 | `3f811311d76914a555c7e7d0c5b887b41805aa6c` | `research/hm/source2-radical-filtration/PROOF.md`, §§4–9: actual-source conditional joint image and common-kernel subpencils. |
| Campaign PR805 | `d79b4ed8263076476296066def7f0c5be7752707` | `research/proof-repair-campaign/source-specific.md`, S03/S04/S06: exact extension task and prohibition on a simplicity-to-truncation inference. |

Work over C. Write F for normalized HM, B=End_0(F),

    T=H^0(O(1)),  S=Sym(T),  K_d=H^1(B(d−1)).

The dimension-five space V_gen=K_0 is dual to T. This notation avoids
confusing the five-dimensional generator representation with the binary
icosahedral irreducible denoted V in PR790–795. Let G be the fixed binary
icosahedral group and let its central inversion split the coordinate space as

    T=T_+ ⊕ W,  dim T_+=3,  dim W=2,

with W the same negative two-space as in PR758. A variable of sign τ sends
K_d^σ into K_(d+1)^(τσ). All multiplication maps below are the actual
cohomological S-action, with variables fixed.

The selected truncation is

    N_2=K_3^+,  N_3=K_4^−,  N_4=K_5^+,
    A_w=m_w|N_2,  B_w=m_w|N_3,  w∈W.

Its dimensions are (41,54,37). Define the full fixed-variable commutant

    C_N={ (e_2,e_3,e_4)∈⊕_(i=2)^4 End_G(N_i) :
          e_3 A_w=A_w e_2, e_4 B_w=B_w e_3 for every w∈W }.

“Full module endomorphism” means a degree-zero S-linear map on K. A
five-variable endomorphism of only the window K_3→K_4→K_5 is a weaker
notion and will not be conflated with it.

## 2. The Euler relation gives full-module rigidity directly

**Theorem 1.** The actual module has

    End_S^0(K)=C·id_K.

This is a theorem about all degree-zero S-linear endomorphisms, without an
equivariance hypothesis. It uses neither stability/simplicity of F nor a
coefficient description of its higher relations.

**Proof.** PR476 provides the actual graded surjection

    q:S⊗V_gen → K,

and identifies the degree-one kernel with Cε, where, for dual bases,

    ε=Σ_(i=1)^5 x_i⊗v_i ∈ T⊗V_gen.

Let f be a degree-zero S-linear endomorphism. It is determined by its
restriction f_0:V_gen→V_gen because K is generated in degree zero.
The map 1⊗f_0 on the free cover must preserve the kernel of q. In degree
one this requires

    (1⊗f_0)ε=cε                                      (1)

for some c∈C. Comparing the coefficients of the independent x_i gives
f_0(v_i)=cv_i for every i. Thus f_0=c id, and generation gives f=c id_K.
Conversely scalar multiplication is an S-linear endomorphism. ∎

There is an explicit linear Euler obstruction, not just a dimension argument:

    δ_E:End(V_gen) → (T⊗V_gen)/Cε,
    δ_E(a)=[(1⊗a)ε].                                 (2)

The coevaluation tensor identifies End(V_gen) with T⊗V_gen, so (2)
is onto and has kernel C·id. Its target has dimension24. This number
is a universal vector-space dimension; it is not an HM rank computation.

For completeness, PR481 makes the full presentation test finite. If
E_2⊂S_2⊗V_gen and E_3⊂S_3⊗V_gen are homogeneous lifts of the actual
minimal quadratic and cubic relations, then

    R=Sε+SE_2+SE_3,
    dim E_2=15,  dim E_3∈{0,15}.

For a proposed generator map a the complete descent equations are

    δ_d(a)=q_d∘(1⊗a)|E_d=0,
    δ_d(a)∈Hom(E_d,K_d),  d=1,2,3,                   (3)

where E_1=Cε. They are necessary and sufficient because the E_d generate R.
Equation (1) shows the first equation alone forces scalar a; scalars
satisfy the other equations. Consequently neither the unresolved cubic
alternative nor unknown embeddings E_2,E_3 leave a gap in Theorem1.

## 3. The exact full-module lifting obstruction

Consider restriction from equivariant degree-zero full-module maps:

    res:End_(S,G)^0(K) → C_N.

Such maps preserve inversion eigenspaces and commute with every fixed
variable, so restriction is well-defined. Theorem1 gives

    im(res)=C·1_N,  ker(res)=0.                       (4)

The kernel assertion uses N≠0. Define the vector-space obstruction

    Ob_full(N)=C_N/(C·1_N),
    ob_full(e)=[e].                                  (5)

Then

    0 → C → C_N → Ob_full(N) → 0                     (6)

is exact, and e lifts to a degree-zero S-linear endomorphism of K if and
only if ob_full(e)=0. A lift, if it exists, is unique and scalar.
The quotient in (5) is a vector space, not an algebra quotient: the scalar
line need not be an ideal in C_N. Conjugation by a fixed-variable pencil
isomorphism preserves the scalar line and hence transports (5) canonically.

This obstruction can also be expressed as a fully typed finite system.
Let σ_3=+, σ_4=−, σ_5=+, and let ι_i:N_i→K_(i+1) be the actual
eigenspace inclusions. Unknowns F_d∈End_G(K_d), 0≤d≤5, must satisfy

    F_(d+1)m_d=m_d(1_T⊗F_d)  in Hom_G(T⊗K_d,K_(d+1)),
       0≤d≤4;
    F_(i+1)ι_i=ι_i e_i  in Hom_G(N_i,K_(i+1)),
       i=2,3,4.                                     (7)

The first square and the Euler relation force F_0 scalar. Surjectivity
of each multiplication T⊗K_d→K_(d+1), a consequence of PR476's
degree-zero generation, forces F_1,…,F_5 to be the same scalar. Thus
(7) is solvable exactly when (5) vanishes, and then extends to all degrees.
Only asking for the two squares d=3,4 in (7) omits the Euler argument;
Theorem1 does not assert that this smaller window commutant is scalar.

Under the published source2 hypotheses and their actual-source bridge,
PR791 gives C_N≅T(J) or C×T(J), with dim J=2 and J²=0. Hence

    dim Ob_full(N)=3 or 4, respectively.              (8)

The proper PR790 projector p has image dimensions (9,18,16) and is
neither zero nor identity, so [p]≠0. Every nonzero j∈J also has [j]≠0:
a scalar square-zero element over C is zero. The entire J injects into
Ob_full(N), since J∩C1_N=0. Both residual coupling classes are covered.

If a hypothetical lift of an idempotent existed, its uniqueness would force
the lift itself to be idempotent: its square minus itself restricts to zero
and restriction is injective. Here the stronger conclusion is that no
nontrivial such lift exists. Likewise, no nonzero radical element lifts.

This is a **failed extension route**, not an exclusion. Source2 gives
endomorphisms of a smaller category, and their non-extension is consistent
with that category having many more endomorphisms. In particular the
proposed universal lifting premise “every source2 projector extends” is
false whenever the source2 hypotheses hold. One cannot combine Theorem1
with that unproved premise and declare a contradiction.

## 4. The first omitted five-variable equation

There is a useful necessary test before demanding a full-module lift.
The actual positive quadratic action is the map

    q_+:Sym²(T_+)⊗N_2 → N_4,
    q_+(pq⊗x)=m_p m_q x.                            (9)

Its typing uses two positive variables, so inversion sign remains positive.
The source factor Sym²(T_+) has dimension6. Commutativity of the S-action
is what makes (9) factor through the symmetric square.

For e∈C_N define

    Θ_+(e)=e_4 q_+−q_+(1⊗e_2)
       ∈Hom_G(Sym²(T_+)⊗N_2,N_4).                  (10)

If e extends to an equivariant five-variable endomorphism of the full
window K_3→K_4→K_5, then Θ_+(e)=0: apply its two positive-variable
intertwining squares successively. The analogous equation for Sym²(W)
already follows from e's A and B equations. Mixed positive-negative
products land in K_5^− and do not give an equation solely on N_2,N_4.

The kernel of Θ_+ is a unital subalgebra. Indeed

    Θ_+(ef)=e_4 Θ_+(f)+Θ_+(e)(1⊗f_2).              (11)

This is a necessary test, not an asserted sufficient condition for a
five-variable window lift. Such a lift still has unknown actions on
K_3^−, K_4^+, K_5^− and must satisfy all positive and negative squares.
No values of (9) or (10) are evaluated here.

## 5. A sharp submodule-extension theorem for S03/S06

Submodules and endomorphisms have different extension problems. Let

    U=(U_2⊂N_2, U_3⊂N_3, U_4⊂N_4)

be any G-equivariant negative subpencil, meaning WU_2⊂U_3 and
WU_3⊂U_4. No complement or retraction is assumed.

**Theorem2.** There exists a G-stable graded S-submodule L⊂K with

    L_3∩K_3^+=U_2,  L_4∩K_4^−=U_3,
    L_5∩K_5^+=U_4                                  (12)

if and only if

    q_+(Sym²(T_+)⊗U_2)⊂U_4.                        (13)

When (13) holds, the minimal S-submodule generated by the three U_i
provides such L. Thus (13) is both necessary and sufficient for this
specific submodule-extension problem, not merely another necessary rank
condition.

**Proof.** Necessity follows because any L in (12) contains U_2 and is
closed under positive quadratic multiplication. For sufficiency put

    L=S·(U_2⊕U_3⊕U_4),

where the generators have actual K-degrees3,4,5. Then

    L_3=U_2,
    L_4=T U_2+U_3,
    L_5=S_2 U_2+T U_3+U_4.                          (14)

These are sums of actual images in K, not direct sums in a free model.
The generators and all sign summands are G-stable, so L is G-stable.
Taking inversion eigenspaces in (14) gives

    L_4^−=W U_2+U_3=U_3,
    L_5^+=Sym²(T_+)U_2+Sym²(W)U_2+W U_3+U_4.

The two terms involving W already lie in U_4 by subpencil stability.
Equation (13) therefore gives L_5^+=U_4, proving (12). ∎

No unknown lower-degree part of L can remove a failure of (13): every
candidate contains the minimal S-span in (14). Conversely, arbitrary
higher-degree consequences do not obstruct (12), which only marks
degrees3,4,5. The theorem does not demand a direct summand, a generated-
in-degree-zero submodule, or a prescribed Hilbert function in other degrees.

For a nested pair of subpencils U⊂V, a full nested pair L_U⊂L_V
with exactly the marked intersections exists if and only if (13) holds
for U and V separately. Necessity follows from Theorem2; sufficiency
uses their nested minimal S-spans.

Apply this to the intrinsic PR795 pair

    U=JN,  V=Ann_J N,
    dim U=(14,18,9),  dim V=(32,36,24).

The exact remaining filtration-extension conditions are the two zero maps

    χ_U:Sym²(T_+)⊗(JN)_2 → N_4/(JN)_4,
    χ_V:Sym²(T_+)⊗(Ann_J N)_2 → N_4/(Ann_J N)_4,    (15)

induced by q_+. Their vanishing is equivalent to extension of this marked
filtration as nested S-submodules. This uses the joint image and common
kernel from the entire radical, not just ranks of separate elements.

If Θ_+(j)=0 for every j∈J, then both maps in (15) vanish. For an image
vector j_2 x, equation (10) gives q_+(s⊗j_2x)=j_4q_+(s⊗x), which
lies in (JN)_4. For x killed by every j_2, the same identity says every
j_4 kills q_+(s⊗x), giving the common-kernel inclusion. The converse
is not asserted: preserving the two filtration spaces need not commute
with each radical operator.

For the proper projector p, Θ_+(p)=0 is equivalent to q_+ having both
cross terms zero between im p_2⊕ker p_2 and im p_4⊕ker p_4. Thus it
implies that both the image and complementary subpencils extend as
submodules by Theorem2. Their minimal extensions need not be complementary
in other parities or degrees. Theorem1 rules out a global splitting
projector, so these weaker submodule extensions cannot be promoted to one.

## 6. What data is actually missing and where this route stops

Full-module lifting has no remaining coefficient gap: (4)–(8) answer it
exactly from the authenticated Euler relation. Neither F's simplicity nor
a generic representation argument is substituted for that relation.

The distinct five-variable-window and filtration routes require the actual
map q_+ in (9), or a new deductive theorem about its action on the intrinsic
subspaces. PR476/481 give generation, an Euler relation and a degree bound,
but do not determine the relation embeddings needed to recover q_+.
One exact presentation of this missing map is the positive-sign restriction
of the ordinary product followed by quotient:

    Sym²(T_+)⊗[(S_3⊗V_gen)/R_3]^+
       → [(S_5⊗V_gen)/R_5]^+,
    (pq)⊗[f] ↦ [pqf],
    R_5=S_4ε+S_3E_2+S_2E_3.                         (16)

Thus dimensions and degrees of E_2,E_3 alone do not give (15). Formula
(16) specifies precisely the missing authenticated inclusion data. It is
not a request or authorization to evaluate them. A deductive structural
theorem about q_+ could replace their coefficient realization.

A nonzero χ_U or χ_V would disprove extension of that marked subpencil
filtration; by itself it would **not exclude source2**, because no source2
theorem in the pinned inputs requires that filtration to extend. Likewise,
a nonzero Θ_+(p) only disproves the proposed five-variable lift of p.
Turning either into an exclusion needs a separate actual-HM theorem that
forces the corresponding vanishing under source2. That is the precise
missing logical premise, not a numerical rank to be inferred from the
already-feasible negative-pencil axioms.

Any endomorphism of the full HM geometric structure covering the identity
on the base and inducing compatible maps B(j)→B(j) for every twist gives,
by multiplication naturality, an S-linear map on K. If it is asserted to
induce one of the nontrivial source2 triples, Theorem1 obstructs it. Maps
which move base coordinates, change the variables, or lack compatible
twist maps are outside this assertion.

Recommendation: STOP the projector/radical-to-full-module exclusion route.
Preserve (15) as a bounded interface for a genuinely new structural theorem;
do not pursue an actual tensor calculation under this campaign's scope.

## 7. Review and falsification checklist

1. Check PR476 proves the *actual* cohomological cover and identity-tensor
   Euler kernel, rather than an isomorphic-character model. If either fails,
   Theorem1 must be withdrawn.
2. Check the grading: N_2,N_3,N_4 are K_3^+,K_4^−,K_5^+, not K_2,K_3,K_4.
3. In (7), require the degree-zero square. Its omission is exactly why the
   five-variable window problem is not settled by Euler rigidity.
4. In (14), retain both positive quadratic and negative quadratic summands;
   mixed signs land in the unmarked parity. An omitted sign term falsifies
   the claimed sufficiency in Theorem2.
5. Test an alleged nonzero radical lift by its action on K_0 and ε before
   invoking any full-bundle theorem. Equation (1) forces its scalar value;
   its nonzero square-zero restriction then makes the claimed lift impossible.
6. Do not replace the joint spaces JN and Ann_JN in (15) by independent
   image/kernel dimensions. Do not infer commutation from filtration
   preservation, or a global splitting from two submodule extensions.
7. The final outcome is an exact non-lifting and interface result. Any
   frontier change or source2 exclusion attributed to this document fails
   its stated theorem boundary.

Written mathematical proof, pending independent review; not formal
proof-assistant certification. The frozen gauge-bridge proof is untouched.
