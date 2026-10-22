# Fourth-square containment on the smooth locus

## Scope and pinned dependencies

This is a structural local proof, not an evaluation of a selected HM instance. It proves the conic part of the local square-ideal gate left open in [PR687](https://github.com/Akilleez-QA/read-em-and-weep/pull/687), at commit `2874402c884a6b426cfd521a674c962a738f84a6`. It also proves a global source factor by extension across the vertex. It does not prove the vertex square-ideal condition, global vanishing, algebraicity, or a value of the fourth obstruction.

We use the actual first-normal coherence/tangency calculation in [the corrected third-neighborhood square-zero theorem](https://github.com/Akilleez-QA/read-em-and-weep/blob/8d8b5be4ce62c3055bb53be9e16d29cc63072f04/research/hm/order-four-quadratic-load/ACTUAL-CORRECTED-THIRD-NEIGHBORHOOD-LIFT-IS-SQUARE-ZERO.md), especially its conic formula. All these are mathematical dependencies, not claims newly formally checked here.

Write Q=(q=0), and let I be the actual Serre zero ideal, with its full scheme structure. Let a be a nonzero actual negative-coordinate quadratic source and h a nonzero positive quadratic source on Q. Let U_a be its fixed trace-free first-normal lift, let J_3 be an actual corrected square-zero lift on 3Q, and let J_4 be any classified fourth lift satisfying J_4|_{3Q}=aJ_3. The pinned results give

    J_3|_{2Q}=(a h_amb-q b_amb)U_a,
    J_3^2=0 on 3Q,
    J_4^2=q^3 S_4 Id on 4Q.

The scalar S_4 is the choice-independent section of O_Q(14) from PR687. The local square-zero extension criterion is S_4 in a^3 h I^2(6).

## Proposition

At every closed point p of the smooth conic component of the Serre locus, including points where a or h vanishes, one has

    S_4 in a^3 h I_p^2.

Twists are suppressed in this local expression. The assertion holds for every actual primitive choice covered by the pinned hypotheses.

## Coordinates and frames

Fix a positive affine chart at p and use its fixed trivializations of all twists. The physical negative coordinates s,t generate I near p. The physical q depends only on the positive coordinates. Smoothness of Q at p allows a remaining positive coordinate z so that q,s,t,z are regular parameters on the ambient smooth fourfold. Formal implicit coordinates therefore identify the completed local ring with R[[q]], where R is a regular complete local domain with parameters s,t,z. In this splitting the actual a, a homogeneous quadratic in s,t, is q-independent. We do not replace q by a rescaled equation.

Use a Serre frame on Q in which

    N=u rho rho^T J,    rho=(s,t)^T,

where u is a unit and J is a fixed alternating matrix. Extend the frame to the ambient completion and lift u and rho through the coefficient ring R. Thus N is q-independent and N^2=0 identically. Retaining u avoids imposing an unauthorized determinant normalization on the actual frame.

Write U_a=aN+qT modulo q^2. The pinned conic first-normal theorem, in these coordinates, supplies

    tr(NT)=0,
    T=tau((kappa u/2)D_a rho+a v),
    tau(w)=rho w^T J+w rho^T J,
    D_a=(-partial_t a,partial_s a),

with v regular. Consequently all entries of N and T belong to I^2: D_a rho is linear in s,t, while a v belongs to I^2. In particular, if T^2=c Id, then c belongs to I^4. No evaluation of v, u, or kappa, and no stronger formula for c, is needed below.

## The h derivative and the second-order equation

Expand h_amb=h+q h_1+O(q^2) and b_amb=b+O(q), and put beta=b-a h_1. In the chosen completed frame write

    J_3=L_0+qL_1+q^2L_2,
    L_0=a^2 h N,
    L_1=a(hT-beta N).

Each L_i is trace-free. The h_1 term is essential; no q-independence of the actual positive source has been assumed. Let L denote the lift of this expression to 4Q with zero q^3 coefficient. It is a chosen local lift, not an identification with the actual J_4.

For trace-free two-by-two matrices A,B over characteristic zero,

    AB+BA=tr(AB) Id.

Hence L_1^2=a^2 h^2 c Id, using N^2=0 and tr(NT)=0. The q^2 coefficient of J_3^2=0 is

    a^2 h [h c+tr(NL_2)]=0.

Because R is a domain and a,h are nonzero elements, cancellation gives

    tr(NL_2)=-h c.

This is integral cancellation of an identity, not division in a local ring. It remains valid at every zero of a or h. Their nonzero restrictions on the integral Q remain nonzero in these local domains and their completions.

## The cubic coefficient and containment

The q^3 scalar coefficient of L^2 is

    chi=tr(L_1L_2)
       =a h [tr(TL_2)+beta c].

Since a is q-independent and J_4|_{3Q}=aJ_3, there is a regular trace-free K over R such that

    J_4=aL+q^3 K.

The plus sign is a definition of K and requires no convention about the sign of a primitive. Squaring yields

    S_4=a^2 chi+a tr(L_0K)
       =a^3 h [tr(TL_2)+beta c+tr(NK)].

The bracket lies in I^2: T and N have entries in I^2, L_2 and K are regular, and c is in I^4. This proves the asserted membership in the completed local ring. Completion is faithfully flat, so the membership descends to the original local ring.

Closed points suffice for the stated sheaf-local containment along the conic. In particular this argument does not discard source-zero points by passing to a source-unit open set.

## Extension to the other smooth patches

The same source factor holds at every smooth point outside the conic. The pinned actual Serre-locus description gives I=O there. Every smooth point of the rank-three quadric lies in a positive affine chart, and q only involves positive coordinates. As before choose a formal coefficient-ring splitting retaining the physical negative coordinates, so a is q-independent. Extend any local bundle frame from Q, and lift the entries of N|Q through the coefficient ring. This preserves its polynomial identity N^2=0 exactly. Thus U_a=aN+qT modulo q^2 with T regular; no Jordan normalization or additional coherence calculation is needed on these patches.

The pinned first-normal square-zero statement U_a^2=0 modulo q^2 implies a tr(NT)=0, hence tr(NT)=0 in the coefficient domain. Nothing else about T is required: the coefficient calculation above gives

    S_4=a^3 h [tr(TL_2)+beta c+tr(NK)].

The bracket is regular, and membership in I^2=O is automatic. In particular source-zero points off the conic are included. Faithfully flat descent again gives the result in the original local ring.

Consequently S_4/(a^3 h) is a regular section rho_4 of O_Q(6) on the entire smooth locus, and belongs to I^2 there. These local quotients glue because they are all the same quotient in the function field with its line-bundle twists.

## Hartogs extension and the remaining vertex gate

The integral rank-three quadric Q is normal: it is a hypersurface, hence Cohen--Macaulay and S2, and its singular locus is the vertex line of codimension two, so it is regular in codimension one. For an invertible sheaf on a normal variety, sections extend uniquely across a closed set of codimension at least two. Therefore rho_4 extends uniquely to

    rho_4 in H^0(Q,O_Q(6)),     S_4=a^3 h rho_4.

The global equality follows from equality on the dense smooth locus. Since the physical sources and S_4 are center-even, the unique quotient is center-even too. This strengthens the previously established factor a^2 without evaluating the remaining scalar.

The conic part of PR687's exact local criterion is proved, and the only unproved local square-ideal membership is now at the vertex. The remaining question is precisely whether the extended rho_4 belongs to I^2(6) there. Hartogs extension for the line bundle O_Q(6) does not imply extension as a section of the square ideal I^2(6), for which no such extension statement has been proved here. This distinction prevents an unsupported global square-zero conclusion.

If the vertex membership is subsequently proved, rho_4 is a global section of I^2(6) in the even character; PR687's pinned vanishing of that space then forces rho_4=0 and hence S_4=0. No vertex order estimate, such membership, or fourth-obstruction value is asserted here.

## Verification status

Authored proof: the local derivation above. Independent mathematical review is recorded in REVIEW.md. The accompanying finite universal polynomial check verifies the rank-two identities, source-order estimates and coefficient signs. It is not a proof-assistant formalization and does not evaluate an actual HM/source instance.
