# Publication scope

This is a preserved theorem manuscript, with the exact hypotheses and held identifications listed in unit 07 INPUTS.md. Abstract geometry and formal conditional implications are distinct from identification with the actual HM module or retained source. Historical words such as “new,” “remaining,” or “previously verified” describe the source manuscript, not a claim about the current research frontier.

# Double-conic conductor intersection and mandatory component relations

Work over C on Y=P4. Let B=End_0(F), G=B(-1), Z=N∪W the reduced conductor, N the triple-root (2,3) complete intersection, W≅P2 the surface q↦q², and C≅P1 the quadruple-root curve. Write G_X=G|X and B_C=B|C. Degrees on C in this document mean O_P1(1). In particular O_Y(1)|C=O_P1(4). The symbol E here means N∩W downstairs, not the upstairs conductor divisor 2R+S.

## 1. The exact scheme intersection

For a quartic ax⁴+bx³y+cx²y²+dxy³+ey⁴ use
I=c²−3bd+12ae and J=72ace+9bcd−27ad²−27b²e−2c³.
The proved ideal of N is (I,J). For q=ux²+vxy+wy² write D=v²−4uw. Substitution of the universal square coefficients (u²,2uv,v²+2uw,2vw,w²) gives I(q²)=D² and J(q²)=−2D³. These are polynomial identities, not evaluations at a selected quartic. Consequently

    I_N O_W=(D²,D³)=(D²),   E=N×_Y W=2C⊂W=P2.

The discriminant conic C=(D) is smooth, so E is its Cartier double structure, without extra embedded points. Its degree in Y is 8 (a plane quartic with hyperplane bundle O_P2(2)). Its reduction C has degree 4. Reducedness of Z does not imply reducedness of the intersection of its components.

## 2. Ribbon sequence and the nonsplitting safeguard

The canonical sequence for the square-zero ideal of C in E is

    0→O_C(-4)→O_E→O_C→0.

Tensor by the locally free ambient G to get

    0→L:=B_C(-8)→G_E→M:=B_C(-4)→0.                 (1)

These are sheaves on E (or Y); one must not assume an O_C-module structure on the middle term via a retraction. There is in fact NO global retraction E→C. Such a retraction would split the conormal sequence

    0→O_C(-4)→Ω_P2|C→Ω_C=O_C(-2)→0.                (2)

Indeed Ω_E|C≅Ω_P2|C, since d(D²) vanishes on C, and differentiating a retraction supplies a right inverse of Ω_E|C→Ω_C. But restriction of the Euler sequence, followed by twisting by O_P1(2), gives

    0→Ω_P2|C(2)→O_C³→O_C(2)→0.

The map on global sections is the complete conic linear system, hence an isomorphism; thus H0(Ω_P2|C(2))=0. A split (2) would give Ω_P2|C(2)=O(-2)⊕O, contradicting this. Equivalently its extension is the nonzero class in H1(O(-2))≅C. Local normal-coordinate descriptions exist but their first-order gluing cannot be dropped.

Retain the actual connecting map

    ε:H0(M)→H1(L).

The complete relevant exact sequence is

    0→H0(L)→H0(G_E)→H0(M) --ε→ H1(L)
      →H1(G_E)→H1(M)→0.                            (3)

Nonsplitting of the ribbon does not by itself determine ε for B or prove that ε is nonzero.

The previously proved splitting bound is B_C≅O⊕O(d)⊕O(-d), d∈{0,2,...,20}. Set A=max(d−7,0), T=max(d−3,0), and ρ=rank ε. Formula (3) gives exactly

    h0(G_E)=A+T−ρ,  h1(G_E)=30+A+T−ρ,
    0≤ρ≤min(T,21+A).

In particular h0(G_E)≤30 and 30≤h1(G_E)≤60. Moreover

    dim ker[H1(G_E)→H1(M)]=21+A−ρ≥21+A−T≥17.

For d≤3 the last lower bound is 21, for 3≤d≤7 it is 24−d, and for d≥7 it is 17. Thus replacing the double conic by its reduction necessarily kills at least seventeen H1 directions, irrespective of the unknown ribbon connecting map. This does not say these directions survive the subsequent component-image quotient D1 or contain any actual ambient/source class. No actual splitting type or connecting rank is selected. Since rk B=3 and deg B_C=0, χ(L)=−21, χ(M)=−9 and χ(G_E)=−30 independently of all these choices.

## 3. Exact Mayer–Vietoris and both ambiguities

The ideal identity for a union supplies the sheaf-exact sequence

    0→G_Z→G_N⊕G_W --v→G_E→0,   v(s_N,s_W)=s_N|E−s_W|E.  (4)

Tensoring is exact because G is locally free. Put

    D0=coker[H0(G_N)⊕H0(G_W)→H0(G_E)],
    K1=ker[H1(G_N)⊕H1(G_W)→H1(G_E)],
    D1=coker[H1(G_N)⊕H1(G_W)→H1(G_E)].

Its long exact sequence gives canonical short exact sequences

    0→D0 --∂MV→H1(G_Z)→K1→0,                      (5)
    0→D1 --∂MV→H2(G_Z)→H2(G_N)⊕H2(G_W)→0.         (6)

There is no asserted splitting or omitted H0 ambiguity. The component condition in K1 uses the whole ribbon H1(G_E), including ε, not simply equality on C.

## 4. Exact filtration of the mandatory cofactor-lift relations

Retain the established Hilbert–Burch and ideal sequences

    0→4B(-6)→5B(-5)→G I_Z→0,
    0→G I_Z→G→G_Z→0.

Write a:H1(G_Z)→H2(G I_Z), h:H2(G I_Z)→4H3(B(-6)), and

    W_Z=ker[4H3(B(-6))→5H3(B(-5))],
    λ=h a,  R=im λ,  R0=im[λ∂MV:D0→W_Z].

The last composition is fully specified by the displayed sequences and positive connecting conventions. Because (5) is exact, choosing any lift of k∈K1 to H1(G_Z) and applying λ gives a well-defined canonical map

    λbar:K1→W_Z/R0.

Its image is exactly R/R0; therefore

    0→R0→im(h a)→im λbar→0,                        (7)
    V_Z=W_Z/im(h a)≅(W_Z/R0)/im λbar.              (8)

This is an explicit two-stage reduction of the compulsory relations: first global ribbon-section mismatch, then compatible component H1 classes modulo that first ambiguity. Neither is discarded. A lift change in (5) changes λ by precisely R0; no arbitrary splitting is needed.

The established lower bound dim R≥90+4h0(B(1))+4h2(B(1)), combined with dim R0≤dim D0≤h0(G_E)≤30, yields the new unconditional bound

    dim im λbar ≥60+4h0(B(1))+4h2(B(1))≥60.         (9)

The sharper unevaluated bound replaces 30 by A+T−ρ or by dim D0. Thus ribbon global sections alone cannot account for all mandatory lift relations: at least sixty independent relations survive into the compatible-component quotient. This is a bound, not an actual rank computation.

## 5. Component restriction can miss a ribbon gluing obstruction

Let r:H2(Y,G)→H2(Z,G_Z) and r_N,r_W its component restrictions. By (6), vanishing of r_N(η),r_W(η) puts r(η) in D1; it does not establish r(η)=0. The residual class is canonical in D1.

For an explicit positive-sign check, represent η by a G two-cocycle x on an affine acyclic cover. If dp_N=x|N and dp_W=x|W, then t=p_N|E−p_W|E is a closed one-cochain on E. Its class modulo the component H1 image is independent of the chosen primitives. The connecting convention for (4) lifts t to (p_N,p_W), whose differential is (x|N,x|W); hence

    ∂MV[t]=r(η),

with a plus sign. This residual class vanishes exactly when the primitives can be adjusted and glued to a primitive on Z. Here 0≤dim D1≤h1(G_E)≤60; since H2(Y,G) has dimension ten, the actual ambient image in D1 is at most ten-dimensional. Neither bound makes it zero.

Together with (8), the established criterion remains

    im α*={η∈ker r : t_HB(η)=0 in V_Z},

where t_HB is the Hilbert–Burch lift class. Equations (6)–(9) refine its two stages without claiming invertibility or source vanishing.

## 6. Euler checks and the concrete cost of using only C

Using χ(B(t))=3 binom(t+4,4)−15t²/2−75t/2−25 and the (2,3) resolution gives

    χ(G_N)=χ(B(-1))−χ(B(-3))−χ(B(-4))+χ(B(-6))
          =5−20−5−55=−75.

The conductor ideal resolution gives χ(G_Z)=−105, so (4) and χ(G_E)=−30 imply χ(G_W)=−60. Independently, on W=P2 with plane class h, ch(B|W)=3−60h² and G_W=B|W⊗O(-2), hence ch(G_W)=3−6h−54h². Multiplying by td(P2)=1+3h/2+h² gives χ(G_W)=3−9−54=−60. Consequently

    h1(G_N)+h1(G_W)=135+h0(G_N)+h0(G_W)+h2(G_N)+h2(G_W),
    dim K1≥75+h0(G_N)+h0(G_W)+h2(G_N)+h2(G_W).

Replacing E by C changes the last Euler term from −30 to −9 and predicts −126 in place of −105. Precisely the missing layer B_C(-8) has Euler characteristic −21. At the sheaf level the kernel of the reduced-difference map G_N⊕G_W→G_C is larger than G_Z, with quotient B_C(-8): take the preimage of ker(G_E→G_C) in (4). Thus the replacement changes the object, not merely a convenient presentation. It loses actual first-order compatibility and the associated H0/H1 maps.

## Scope and dependencies

All results are universal polynomial identities, exact sheaf/cohomology arguments, and bounds. No actual HM matrix, selected rank, retained source, polynomial instance, obstruction pairing, large computation, or local Codex task was used. The tiny arithmetic check only evaluates the universal Riemann–Roch polynomial at fixed twists.
