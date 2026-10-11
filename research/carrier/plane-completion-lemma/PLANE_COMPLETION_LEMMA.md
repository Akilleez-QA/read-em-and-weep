# A bounded plane-completion lemma and a presentation obstruction

Date: 2026-10-11. Characteristic zero. This note derives new statements from the displayed fixed-plane data. It does not identify an omitted ancestor, supply a carrier, establish algebraization of the five-parameter chart, or compute any defect.

## 1. Pinned input and interpretation boundary

Fixed model: https://github.com/Akilleez-QA/read-em-and-weep/blob/6b69eefd57098d9a0c1d9f43ed993d36e1e54bcb/research/carrier/formal-five-parameter-chart/formal-chart.md

Boundary: https://github.com/Akilleez-QA/read-em-and-weep/blob/6b69eefd57098d9a0c1d9f43ed993d36e1e54bcb/research/carrier/formal-five-parameter-chart/README.md

Inventory: https://github.com/Akilleez-QA/read-em-and-weep/blob/cdccc9e94afedac76def6d21084c1cd49c41a97a/research/hsd-ancestor-61/SOURCE_INVENTORY.md

Coordination: https://github.com/Akilleez-QA/read-em-and-weep/pull/61#issuecomment-6107077804 and https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6109904663

The README calls the omitted input a “full rank-five symplectic presentation”, without defining its terms. A rank-five bundle cannot carry a nondegenerate alternating form in characteristic zero. That fact does not identify what the author intended by a rank-five presentation. Below, the rank-five ansatz is explicitly specified and its failure applies only to that ansatz.

Let Y=P1×P2, A=O(3,-6), P=O(3,-3), L=O(4,-2), B=P⊕E, and D=L P^(-1)=O(1,1). E has subline E0=O and quotient E1⊕E2=O(4,-4)⊕O(3,-4), with the actual triangular base gluing retained. Set S=X²+Y², F=XY, a=X³+Y³, g=S-zW², C=S²+zSW²+z²W⁴.

The relation A→B is r=(-a,r_E), with finite r_E=(W⁶,-g,F) and infinity r_E=(S³,-uS+W²,F), u=z^(-1). The alternating form on E is

    Ω_E = [[0,r3,-r2],[-r3,0,r1],[r2,-r1,0]],

and Ω_B is zero on P and Ω_E on E. The transition identity T_B r_infinity=z³r_finite is part of the pinned input; it also follows from g C=S³-z³W⁶.

## 2. Everywhere rank and line-quotient checks

Finite base: if r_E vanishes, W=0, F=0 and S=0. Over any field extension, XY=0 and X²+Y²=0 imply X=Y=0, impossible in P2.

Infinity base: vanishing implies S=0, W²=uS=0 and F=0, again impossible. This checks the point u=0 as well as all other points; no base point is omitted. Thus A→E is a line subbundle, Ω_E has constant rank two and radical precisely its image. Consequently r:A→B is a line subbundle, G=B/A is locally free of rank three, and P embeds as a line subbundle of G. The descended form on G has radical exactly P. H=G/P=E/r_E(A) is symplectic of rank two with values in L.

In particular, G is not the missing rank-four symplectic object. The desired completion has the form 0→G→V→D→0, with V symplectic of rank four, G=P-perpendicular, and the induced P⊗D→L pairing the canonical one.

## 3. Explicit local rank-five alternating completion

On an open where the line bundles are trivialized and r_i is a unit, choose ψ_i:E→P with ψ_i(e)=a e_i/r_i. Thus ψ_i(r_E)=a. Let Q_i=B⊕D locally and define

    Ω_i((p,e,d),(p',e',d'))
       = Ω_E(e,e') + p d' - d p' + ψ_i(e)d' - d ψ_i(e').

All products land in L: ψ_i maps E to P and P⊗D=L. The relation (-a,r_E,0) is radical, since its pairing with the D coordinate is -a+ψ_i(r_E)=0. Conversely, pairing a radical vector against P forces d=0; then pairing against E forces e=t r_E; pairing against D forces p=-ta. Hence the radical is exactly A, and V_i=Q_i/A is nondegenerate of rank four. This is a local construction, not a claim that the Q_i descend as rank-five bundles.

The principal opens D(r1),D(r2),D(r3) cover each base chart and may be refined by standard projective coordinate opens to trivialize all lines. Local unit inversions use these geometric coordinates only. Over a locally trivial normal-line neighborhood these formulas pull back to a local algebraic normal thickening. Leaving v=E0 unchanged gives zero normal pairing. Locally choose the displayed splitting q:D→V_i and put v_tilde=v+q(t0 h). Since t0 h is a section of D=O(1,1), this is correctly typed and Ω(P,v_tilde)=+t0 h. Thus a local structured normal lift exists with the required sign. These local sections do not automatically glue, nor do they identify the prescribed global first-jet class.

The finite form grading is consistent if d_D=1: ψ0 has weight 3, ψ1 and ψ2 weight 1, so wt(ψ_i)+d_Ei+d_D=4; the P,D entry also has 3+1=4. On the infinity chart d_D=5 gives the corresponding sum 8, using d_E=(6,0,2). This verifies local form weights, not an independent identification with every prescribed completion-frame convention.

## 4. Exact central descent residual on the finite base

Use the cover U_i=D(r_i) over A1_z×P2, refining as above. On U_i∩U_j define a map V_j→V_i that is identity on G and sends the local D generator q_j to q_i+b_ij. Choose the E components

    b12 = a/(r1 r2) e3,
    b23 = a/(r2 r3) e1,
    b31 = a/(r3 r1) e2,
    bji = -bij.

Then Ω_E(-,b_ij)=ψ_j-ψ_i, so these are exact isometries, not first-order approximations. The P component of b_ij may be chosen freely. On the triple overlap, the sum of the displayed E components is a r_E/(r1 r2 r3). Since r_E=aP in G, their composition sends q to q+a²/(r1 r2 r3) P. Thus the residual is the central section

    R123 = a²/(r1 r2 r3) ∈ P² L^(-1).

There are no omitted nonlinear terms: each transition fixes G pointwise and adds an element of G to q. This formula also proves why local completion is insufficient without descent.

Write T=-3S+2F. The polynomial identity

    a² = g C + z³ W⁶ + T F²

is exact. Since r1 r2 r3=-W⁶ g F, it gives

    R123 = -C/(W⁶ F) - z³/(g F) - T F/(W⁶ g).

With cyclic Čech convention b12+b23+b31, choose additional P components

    c12 = T F/(W⁶ g),
    c23 = z³/(g F),
    c31 = C/(W⁶ F),
    cji = -cij.

Each is regular on its named double overlap with the correct line twist, and c12+c23+c31=-R123. The corrected transitions therefore descend the rank-four V_i exactly over A1_z×P2. This is an actual local-in-base algebraic plane completion, not a finite-jet test.

## 5. Global plane completion: two complementary descent arguments

For clarity, this section establishes existence without exporting a matrix for the finite-to-infinity isometry on the original six-open cover.

On the infinity base chart set r1=S³, r2=−uS+W², r3=F. The same local completion and b_ij formulas apply, with residual a²/(r1r2r3). The identity a²=S³+TF² now gives the correction

    c12 = −TF/(r1r2),
    c23 = −1/(r2r3),
    c31 = 0,
    cji = −cij.

Again their sum is the negative central residual, so an algebraic completion exists over the infinity base chart as well. These infinity identities were also checked exactly with symbolic rational arithmetic.

Given two local completions of the same presymplectic G, the sheaf of isometries fixing G is locally nonempty: the difference of two D-pairing functionals annihilates the radical and can be represented by Ω_G(-,b) locally. An automorphism fixing G is precisely q↦q+c with c in P. Thus that automorphism sheaf is M=Hom(D,P)=P²L^(-1)=O(2,-4), and the isometry sheaf is an M-torsor. On the base overlap Gm×P2, H¹(M)=0, by projective-space cohomology over the affine base. Therefore the two completions admit an isometry fixing G on that whole overlap, so they glue algebraically. H⁰(M)=0 makes that isometry unique; there is no additional base-triple condition for this two-open gluing other than the inverse identity.

This proves that the displayed G admits a global algebraic rank-four L-symplectic plane completion V, with P⊂G=P-perpendicular and V/G=D. In fact H¹(Y,M)=H⁰(Y,M)=0, so any two completions fixing this same G and canonical P–D pairing are uniquely isometric.

For a second check, local completions and pairwise isometries have a central Čech degree-two obstruction in H²(Y,M). It restricts to zero by §4. Künneth gives

    H²(Y,O(2,-4)) = H⁰(P1,O(2)) ⊗ H²(P2,O(-4)),

of dimension 3×3=9. Restriction to A1_z×P2 is injective, because H⁰(P1,O(2)) injects into its restriction over A1. Hence the global obstruction vanishes. This is ordinary Zariski descent, not deformation-theoretic algebraization.

Equivariance has a conditional refinement. Given fixed compatible algebraic torus linearizations on G, P, L and their pairings, the completion inherits a unique compatible linearization. Over T×Y, the two completions obtained by action and pullback have an isometry torsor under the pullback of M; its H¹ and H⁰ vanish because T is affine and the corresponding groups on Y vanish. The unique isometry therefore exists algebraically, and uniqueness over T²×Y enforces the action cocycle. This proves a compatible linearization exists for the stated input linearizations; it does not identify an unprovided ancestor framing.

The construction can identify any supplied object satisfying exactly this fixed-G completion contract, but the source's intended alpha/completion frame and its first-normal jet have not been independently identified here.

## 6. A rigorous no-go for one natural rank-five presentation type

Assume a locally free rank-five Q contains the given B as a subbundle with Q/B=D, carries an L-valued alternating form restricting to Ω_B, has radical exactly the given relation A⊂B, and pairs P⊂B canonically with Q/B=D. This is a specific ansatz, not an interpretation imposed on the README.

First, Ext¹(D,B)=H¹(B P L^(-1))=0. Its filtration lines are

    O(2,-4), O(-1,-1), O(3,-5), O(2,-5).

Each has H¹=0 by projective-space cohomology/Künneth, and the actual successive extensions preserve this vanishing. Thus every such vector-bundle extension Q splits as B⊕D.

Under any splitting, the form's E,D entries define a global ψ:E→P. The radical condition forces ψ(r_E)=a. But every global ψ vanishes on E0 because H⁰(P)=H⁰(O(3,-3))=0. It factors through E/E0=O(4,-4)⊕O(3,-4). The first summand has Hom-to-P global space H⁰(O(-1,1))=0; the second gives H⁰(O(0,1)). Therefore

    Hom(E,P) = {ψ=(0,0,ℓ(X,Y,W)): ℓ linear},
    ψ(r_E)=ℓ XY.

No such expression equals X³+Y³ (for example, restrict to X=0). Thus no Q of this precisely specified type exists.

This does not contradict §5: local rank-five presentations can descend only after quotienting A, and a rank-four V need not admit a rank-five presentation retaining this B and this A globally. It also does not rule out another rank-five complex/presentation, another ambient restriction or a carrier construction.

## 7. First remaining construction deliverable

The bounded next constructive deliverable is to turn §5 into explicit global homogeneous rank-four plane transitions, identify the intended alpha/completion frame and prove the declared supplied coefficient maps come from it. After that, a claimed ancestor needs independently specified ambient scheme and embedded Y (normal/conormal identification), its bundles/relations/form, exact transitions on stated overlap rings, and a quotient/restriction isomorphism to that plane object. A specified first-normal jet must match the nonzero prescribed pairing and frozen Čech class up to an explicit compatible gauge/chain map.

A pullback along Tot(O(0,1))→Y always extends a constructed plane bundle, but does not supply the chart's prescribed nonzero first-normal pairing. The all-order formal theorem remains conditional on its framed inputs. Neither plane completion nor formal continuation establishes a geometric carrier, relative reflexive-hull base change, or a zero-defect member. HSD's ancestor-comparison lane is unchanged; no comparison can run until actual ancestor data are pinned.

## Verification and background references

The polynomial identity, each of the three equations Ω_E b_ij=ψ_j−ψ_i, the E-valued triple sum and its exact central cancellation were independently evaluated as symbolic rational-function identities with SymPy on 2026-10-11; every residual was identically zero. These calculations verify §4, not the abstract global descent argument by themselves.

For the standard cohomology formula used above, see [Stacks, Lemma 30.8.1](https://stacks.math.columbia.edu/tag/01XT). For the general role of an abelian automorphism sheaf in degree-two descent, see [Stacks, Second cohomology and gerbes](https://stacks.math.columbia.edu/tag/0CJZ); the particular automorphism sheaf and its Čech residual are derived explicitly here.

Independent review on 2026-10-11 confirmed the local signs, central residual, two-base-chart gluing, uniqueness, conditional equivariance refinement and the precise retained-B rank-five no-go. This review does not certify any ancestor identification or frozen first-jet comparison.
