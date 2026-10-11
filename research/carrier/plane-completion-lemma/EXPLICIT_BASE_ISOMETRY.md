# Explicit base-overlap isometry for the constructed plane completion

Date: 2026-10-11. This is a continuation of the bounded plane-completion lemma. It preserves that earlier artifact and any immutable publication of it. All formulas concern **our constructed completion of the displayed G**, not an identified ancestor or carrier.

## Source and notation

Pinned fixed-model input:
https://github.com/Akilleez-QA/read-em-and-weep/blob/6b69eefd57098d9a0c1d9f43ed993d36e1e54bcb/research/carrier/formal-five-parameter-chart/formal-chart.md

Put

    S=X²+Y², F=XY, a=X³+Y³, w=W⁶,
    g=S−zW², C=S²+zSW²+z²W⁴, T=−3S+2F.

The exact identities used are

    gC+z³w=S³,
    a²=S³+TF²=gC+z³w+TF².

Work on Y=P1×P2 with A=O(3,−6), P=O(3,−3), L=O(4,−2), D=LP⁻¹=O(1,1), B=P⊕E, G=B/A. The finite and infinity relations in ordered B coordinates (P,E0,E1,E2) are

    r0=(-a,w,−g,F),
    r∞=(-a,S³,−g/z,F).

The pinned infinity-to-finite transition is

    TB = [[z³,0,0,0],
          [0,1,zC,0],
          [0,0,z⁴,0],
          [0,0,0,z³]].

It satisfies TB r∞=z³r0 and TBᵀ ΩB,0 TB=z⁴ ΩB,∞. The latter's only nontrivial polynomial identity is gC+z³w=S³. These equations establish the global presymplectic G directly from the displayed data.

## 1. Local quotient frames and the plane transitions

Number the E coordinates as e1=E0,e2=E1,e3=E2. On each base chart, let (r1,r2,r3) be the three E entries of its relation. Let Vi be the local completion on D(ri), constructed from B⊕D with extra local D generator qi, form entries Ω(P,qi)=1 and Ω(ej,qi)=δij a/ri, and radical (-a,r1,r2,r3,0).

Use the rank-four quotient frame

    i=1: (P,E1,E2,q1),
    i=2: (P,E0,E2,q2),
    i=3: (P,E0,E1,q3).

For compact explicit formulas, Ji is the 5×4 inclusion omitting Ei−1 from the ordered five coordinates (P,E0,E1,E2,q). Put rhat=(-a,r1,r2,r3,0)ᵀ and let ei* select that omitted E coordinate. The quotient projection is

    Ri = Jiᵀ (I5 − rhat ei*/ri).

Thus Ri Ji=I4, Ri rhat=0, and the omitted coordinate is eliminated using

    ei = (a/ri)P − Σ(j≠i)(rj/ri)ej.

In each quotient frame the alternating form is

    Oi = [[0,0,0,1],
          [0,0,si ri,0],
          [0,−si ri,0,0],
          [−1,0,0,0]],       (s1,s2,s3)=(1,−1,1).

Its determinant is ri², a unit on that open.

For the cyclic pairs (1,2),(2,3),(3,1), the plane transition j→i fixes G and sends qj to qi+bij+cij P, with

    b12 = a/(r1r2) e3,
    b23 = a/(r2r3) e1,
    b31 = a/(r3r1) e2.

Use negatives for reversed pairs. The finite-chart central terms are

    c0,12=TF/(wg), c0,23=z³/(gF), c0,31=C/(wF),

and the infinity-chart terms are

    c∞,12=−TF/(r1r2), c∞,23=−1/(r2r3), c∞,31=0.

Set Mij=I5+(bij+cijP)e_q*. The **explicit rank-four plane matrix** is

    gij = Ri Mij Jj.

This formula specifies every matrix entry without a linear system or an unspecified gauge. It respects the exact line-bundle twists. On standard projective-coordinate refinements all entries become regular functions in the stated localized coordinate rings.

## 2. Common cover on the base overlap

Over z≠0 use

    U1=D(WS), U2=D(g), U3=D(F).

These are contained in both finite and infinity rank-i patches, respectively. They cover Gm×P2: if F=g=0 then S=zW²; projectivity forces W≠0, and z≠0 forces S≠0.

Refine further by D(X),D(Y),D(W) if literal trivializations of all line bundles are desired. Denominators below use only geometric units on the stated opens, not parameter inversions.

## 3. Explicit infinity-to-finite maps

Retain TB on B. On the extra coordinate use

    q∞,1 ↦ z q0,1 + zC/(wS³)(TF·P−a·E2),
    q∞,2 ↦ z q0,2,
    q∞,3 ↦ z q0,3.

The factor z is the transition of D=O(1,1); the alternating-form value line has transition z⁴. Write the corresponding local 5×5 map as Hi and its quotient map as τi=R0,i Hi J∞,i.

In the rank-four frames of §1, the matrices are explicitly

    τ1 = [[z³, zCa/w, 0, zCTF/(wS³)],
          [0, zS³/w, 0, 0],
          [0, −zCF/w, z³, −zCa/(wS³)],
          [0, 0, 0, z]],

    τ2 = diag(z³,1,z³,z),

    τ3 = [[z³,0,0,0],
          [0,1,zC,0],
          [0,0,z⁴,0],
          [0,0,0,z]].

Their determinants are z⁸S³/w, z⁷ and z⁸, respectively. They are units on U1,U2,U3, so these are algebraic frame isomorphisms on the exact stated rings.

The form equation is

    τiᵀ O0,i τi = z⁴ O∞,i.

The mixed plane/base compatibility equation is

    τi g∞,ij = g0,ij τj.

At the five-coordinate presentation level, the mixed residuals for cyclic pairs 12 and 23 vanish already in B. The pair31 residual is exactly

    [zCa/(F wS³)] r0.

It is therefore zero after quotienting A. This is intentional: one must not require the locally chosen rank-five presentations to form a global rank-five B-hyperplane extension. The rank-four maps satisfy exact cocycles, with no normal-order truncation.

## 4. Homogeneity and the distinguished plane data

The five-coordinate frame weights, including the new D coordinate, are

    finite:   (3,0,2,2,1),
    infinity: (3,6,0,2,5),

with wt(z,X,Y,W)=(2,1,1,0). After deleting the omitted E coordinate from both weight lists, every nonzero entry of τi obeys

    wt((τi)mn) = dfinite,m − dinfinity,n + 6.

This is the same base-character offset as TB. It was checked as an exact rational-function identity under the torus scaling (z,X,Y,W)↦(t²z,tX,tY,W), not by counting a few monomials.

The isotropic line inclusion P→V is the first quotient coordinate on every patch and is transported by z³. It has perpendicular G by construction. Thus the distinguished isotropic **line and its fixed P normalization** are explicitly matched in our completion. If the source's symbol alpha denotes that P-inclusion, this supplies it; it does not identify a different unspecified alpha or an ancestor frame.

The section v=E0 descends exactly. On patch1 its coordinates are

    v0,1=(a/w, g/w, −F/w, 0),
    v∞,1=(a/S³, g/(zS³), −F/S³, 0).

On patches2 and3 it is (0,1,0,0). The identities τi v∞,i=v0,i and the plane-overlap equivalents are exact. The pairing map β=Ω(P,−):V→D is the last coordinate in each frame. Thus β(v)=0 on the plane, with the normalization β(qi)=+1.

## 5. First-normal pairing: local construction versus global matching

Let I=O(0,−1) be the original conormal. Since DI=O(1,0), the prescribed t0 (finite representative z, infinity representative 1) is a section of DI. On each local normal trivialization the section

    v_tilde,i = v + qi(t0 h)

is correctly typed and satisfies β(v_tilde,i)=+t0 h. This proves the local positive-pairing lift directly.

Its plane-overlap mismatch is t0h(bij+cijP); the base-overlap mismatch on U1 is h·zC/(wS³)(TF P−aE2), and vanishes on U2,U3. These are explicit first-order section defects for the **unchanged pullback middle bundle**. They must not be identified with the frozen deformation cochains in data/first_jet.json, whose middle transitions vary.

### 5.1 A checked obstruction for the unchanged pullback middle

There is a precise reason not to claim these local section lifts glue while leaving V and β unchanged. From

    0 → GI → VI → DI → 0

let δ:H⁰(DI)→H¹(GI) be the connecting map. The local section defects above represent δ(t0). Lift them to BI using t0(bij+cijP). Their cyclic sum is

    [t0 a/(r1r2r3)] · (-a,r1,r2,r3).

Moreover H¹(BI)=0, because its filtration lines O(3,−4), O(0,−1), O(4,−5), O(3,−5) all have H¹=0. Hence the map H¹(GI)→H²(AI), where AI=O(3,−7), is injective. It sends δ(t0), with our cyclic convention, to the generalized-fraction class

    [z a/(W⁶(−g)F)]

on the finite base chart.

This class is nonzero. Restrict to z=1, so t0=1 and g=S−W². In R=Q[X,Y,W], the three homogeneous polynomials W⁶,g,F have no common projective zero. Their ideal is a homogeneous parameter ideal, and they form a regular sequence because R is Cohen–Macaulay. For a regular sequence (f1,f2,f3), the maps

    R/(f1^n,f2^n,f3^n) → R/(f1^(n+1),f2^(n+1),f3^(n+1)),
    x ↦ (f1f2f3)x

are injective: the colon ideal of the target power ideal by f1f2f3 is the source power ideal. Their direct limit is H³_(X,Y,W)(R). Thus numerator nonmembership here really does imply the generalized fraction is nonzero; this argument would not be valid for an arbitrary denominator tuple without the regular-sequence check. In degree −7 this local cohomology identifies with H²(P2,O(−7)).

Finally a=X³+Y³ is not in (W⁶,S−W²,XY). Degree three excludes the W⁶ generator. If a=ℓ1(S−W²)+ℓ2 XY with linear forms ℓ1,ℓ2, the XW²,YW²,W³ coefficients force ℓ1=0, while a is not divisible by XY. As an additional exact linear check, the 10×6 degree-three coefficient matrix for Xg,Yg,Wg,XF,YF,WF has rank6, and adjoining a gives rank7.

Therefore δ(t0)≠0. The unchanged pullback middle π*V with the fixed pairing β does **not** admit a global section reducing to E0 and satisfying β(v_tilde)=+t0h even modulo h². This is not a first-order obstruction to the chart's coupled deformation problem: its middle transitions are allowed to deform, and their action on E0 changes the section equation. It is not a claim about arbitrary deformations of α or β on an unchanged bundle.

The next comparison, if requested, is a finite Čech problem: refine the displayed cover with the original D(X),D(Y),D(W) cover; express the frozen middle first cochains in these quotient frames; apply their action to E0; then compare the resulting section defects, including the +t0 pairing and the fixed signs, modulo a supplied regular 0-cochain/gauge. The available data determine our plane transition matrices and local pairing completely. They do not supply an independently pinned ancestor restriction or establish equality to a producer's unprovided frame map. No such equality is claimed here.

## 6. Exact verification

`verify_explicit_base_isometry.py` uses the displayed formulas only, over symbolic rational functions with rational coefficients. The receipt `EXPLICIT_BASE_ISOMETRY_CHECKS.json` records 163 successful checks, comprising 1,972 scalar matrix entries/identities:

- local projections, relation annihilation and radicals;
- both numerator identities and local nondegeneracy determinants;
- every ordered plane-overlap form/inverse identity and all 27 triples on each base chart;
- cross-base relation, form and explicit-matrix identities;
- all nine mixed cocycles;
- cross-base P and E0 transport;
- every nonzero cross-base entry's character.

Regularity is verified separately from symbolic equality by the named denominator/unit conditions above. A rational-function identity alone would not certify regularity on a larger open.

Independent review separately confirmed the cross-base formula, the common-cover argument, the exact relation-valued mixed residual and the fixed-middle first-normal section obstruction, including its regular-sequence nonvanishing test. No ancestor-source comparison, carrier computation, full normal-jet comparison or defect computation has been run.
