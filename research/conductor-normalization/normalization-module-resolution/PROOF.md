# Publication scope

This is a preserved theorem manuscript, with the exact hypotheses and held identifications listed in unit 03 INPUTS.md. Abstract geometry and formal conditional implications are distinct from identification with the actual HM module or retained source. Historical words such as “new,” “remaining,” or “previously verified” describe the source manuscript, not a claim about the current research frontier.

# A minimal normalization resolution and a sixteen-dimensional boundary target

## Result

Over C let Y=P4, S=P1×P1, f(l,m)=l³m, and B=End₀(HM). The finite normalization pushforward has minimal locally free resolution

    0 → 5O(-3) → 9O(-2) → O ⊕ 3O(-1) → f_*O_S → 0.       (1)

The unit O→f_*O_S is represented by the literal inclusion of the O summand. Consequently normalized restriction has a strict finite line-complex model on Y, without a choice of Čech contractions. More efficiently, dualizing (1) gives

    0 → E=B(-1)⊕3B → L=9B(1) → P=5B(2) → f_*H → 0,      (2)
    H=f*B⊗O_S(10,2).

The dual normalized restriction δS:H0(S,H)→H2(Y,B(-1)) is the composite of the two connecting maps from (2), followed by projection onto the B(-1) summand. Its intermediate H2(E) has dimension sixteen, split into the ambient ten and six auxiliary dimensions. This is a map identity. It does not assert that δS is zero or surjective.

## 1. Cohen–Macaulayness and regularity determine every Betti degree

Let R=Sym H0(Y,O(1)) and M=⊕_{t∈Z}H0(S,O(3t,t)); negative pieces are zero. Since f is finite, this is the full section module of f_*O_S. It is finitely generated. The standard section-module local-cohomology sequence gives H⁰_m(M)=H¹_m(M)=0 and

    H²_m(M)_t = H¹(S,O(3t,t)),
    H³_m(M)_t = H²(S,O(3t,t)).

Künneth makes H¹ vanish for every integer t: for t≥0 both factor H¹ groups vanish; for t<0 both H⁰ groups vanish. The support dimension of M is three, so M is Cohen–Macaulay of depth three over the five-variable polynomial ring. Auslander–Buchsbaum gives projective dimension two. The top local cohomology is nonzero exactly at t≤−2, hence reg M=−2+3=1.

For t≥0, dim M_t=(3t+1)(t+1), and thus

    Hilb(M,z)=(1+5z)/(1-z)³
             =(1+3z−9z²+5z³)/(1-z)⁵.

The degree-zero generator is 1. The five ambient linear forms inject into M1: the equivariant pullback is the nonzero Sym4 summand in Sym3⊗Sym1=Sym4⊕Sym2. Equivalently the triple-root locus is not contained in a hyperplane. As dim M1=8, precisely three additional minimal degree-one generators are required. Regularity one excludes higher generators, so F0=R⊕3R(-1).

There are no degree-one relations: degree-one F0 maps isomorphically to M1. Therefore minimality forces the shifts of F1 to be at least two and those of F2 to be at least three. The regularity bound forces them to be at most two and three, respectively. Thus the numerator determines F1=9R(-2), F2=5R(-3), with no hidden same-degree cancellation. Sheafification gives (1).

No claim that R→M is injective is made: its kernel is I_N, the (2,3) complete-intersection ideal. The inclusion is only into the free resolution's degree-zero term.

## 2. Universal equivariant construction, with no selected instance

Write V_d=Sym^d(C²)* as an SL2 representation. The three generator spaces are

    F0 = R ⊕ V2 R(-1),
    F1 = (V4⊕V2⊕V0) R(-2),
    F2 = V4 R(-3).                                    (3)

Indeed the extra generator V2 is the canonical complementary irreducible in M1=V4⊕V2. Define F0→M using 1 and this inclusion. The space of quadratic relations is intrinsically

    K2=ker[(Sym²V4)⊕(V2⊗V4) → M2=V6⊗V2].

The map is the universal multiplication of sections after f*. Since Sym²V4=V8⊕V4⊕V0 and V2⊗V4=V6⊕V4⊕V2, subtraction of M2=V8⊕V6⊕V4 gives K2=V4⊕V2⊕V0. Semisimplicity of SL2 makes this representation subtraction valid; surjectivity follows from the generation already proved.

The map F1→F0 is the inclusion of these universal quadratic relations and their R multiples. Its degree-three kernel defines F2. In that degree the exact character identity is

    [F2_3]=[V4⊗K2]−[Sym³V4⊕V2⊗Sym²V4]+[V9⊗V3]=[V4].

Here Sym³V4=V12⊕V8⊕V6⊕V4⊕V0. This proves (3) without choosing values of l,m or HM coefficients. It also supplies a precise intrinsic recipe for every resolution arrow by kernels of universal multiplication. Bases and scalar normalizations may be chosen, but the unit is fixed.

The SL2 equivariance is that of the normalization geometry only. No SL2 linearization of the HM bundle is assumed.

## 3. Strict restriction, and a finite model with ordinary H4 maps

Let R• denote (1) without its final sheaf, in degrees −2,−1,0. The unit is the chain map O[0]→R• with image in its O summand. Tensoring by B(-4) gives the restriction morphism

    B(-4) → [5B(-7) → 9B(-6) → B(-4)⊕3B(-5)]

in the derived category, with the right complex representing f_*(f*B⊗O(-12,-4)).

To make both cohomology models finite without Čech contractions, use the already proved strict tracefree line complex E0 for B(-4):

    E0^k=m_k O(k-4),  k=−3,…,3,
    m=(10,80,245,353,245,80,10).

Tensor E0 by R• and totalize with differential d_E⊗1+(-1)^k1⊗d_R. Every line-bundle summand has negative twist, hence its only possible cohomology is H4 on P4. Define

    Z^n=⊕_{k+r=n} H4(Y,E0^k⊗R^r),
    C^n=H4(Y,E0^n).

Then H2(Y,B(-4))=H^-2(C), the normalized target is H^-2(Z), and rS is induced by the literal inclusion C→Z into the unit summand. All differentials are ordinary H4 maps induced by universal polynomial arrows; there is no cross-row map or transferred comparison. Naturality of the one-row hypercohomology spectral sequence proves the identification.

For completeness the nonzero dimensions of Z, in degrees −5,…,0, are

    6300, 34300, 69275, 63550, 25930, 3664.

These are larger vector spaces than the earlier surface-row model, but the comparison has become a coordinate inclusion, with no auxiliary infinite-dimensional contraction. Their alternating Euler sum is 9, agreeing with χ(S,f*B⊗O(-12,-4)). The source has dimensions150,400,245 in degrees−3,−2,−1. Thus rS([x])=0 exactly when the coordinate inclusion of x is a boundary in Z. No matrix is instantiated or ranked here.

The strict quotient complex of B(-4)⊗R• by B(-4) is

    Q=[5B(-7)→9B(-6)→3B(-5)].

It represents Cone(restriction), not merely the normalization quotient sheaf. Its sheaf cohomology is H^-1(Q)=B(-4)I_N and H0(Q)=B|C⊗O_C(-18). This warning prevents losing the ideal contribution by incorrectly treating O→f_*O_S as injective.

## 4. Duality makes the small target and its projection intrinsic

The CM module has codimension two, so its sheaf Ext into ωY is concentrated in degree two. Proper duality, or finite duality followed by the codimension-two embedding, identifies

    Ext²_Y(f_*O_S,ωY)=f_*ωS.

Dualizing (1) into ωY=O(-5) gives the exact sequence

    0→O(-5)⊕3O(-4)→9O(-3)→5O(-2)→f_*ωS→0.

Tensor by B(4), use the trace pairing B≅B∨, and use ωS=O(-2,-2), to obtain (2). Its last sheaf is exactly f_*H with H=f*B⊗O(10,2).

Let K=im(L→P). Split (2) into 0→E→L→K→0 and 0→K→P→f_*H→0. With a common derived connecting-sign convention write

    Δ:H0(S,H)→H1(K)→H2(E).

Duality transposes the strict unit inclusion in §3 to the projection E=B(-1)⊕3B→B(-1) at the left end of the dual resolution. Therefore

    δS=pr₁∘Δ.                                        (4)

This follows either from functoriality of derived duality or by pairing against the strict inclusion: for c∈H2(B(-4)), s∈H0(S,H),

    <c,pr₁Δ(s)>_Y=<rS(c),s>_S.

Thus it is precisely the previously defined Gysin map, not a replacement chosen solely by matching dimensions. Simultaneous changes in resolution/connecting conventions preserve this identity with compatible duality choices.

The verified HM cohomology gives h2(B(-1))=10 and h1(B)=24. Stability gives h0(B)=0, duality and negative-H1 vanishing give h3(B)=h4(B)=0. The Riemann–Roch polynomial gives χ(B)=3−25=−22, hence h2(B)=2. Consequently h2(E)=10+3·2=16.

## 5. Exact sixteen-dimensional criterion, retaining positive cohomology

Set

    V=ker[H2(E)→H2(L)],
    J=coker[H1(L)→H1(P)].

For v∈V choose a lift y∈H1(K) under the first connecting map, and define σ(v) to be the image of y in H1(P), modulo im H1(L). This is well defined because different lifts differ by an image from H1(L). Exactness gives

    im Δ=ker σ ⊂ V ⊂ H2(E),
    im δS=pr₁(ker σ) ⊂ H2(B(-1)).                     (5)

For the first identity, a section maps to a lift killed in H1(P). Conversely if σ(v)=0, adjust y by an H1(L) image so its image in H1(P) vanishes; it then comes from H0(S,H). The second identity is (4).

Therefore

    rank rS = dim kerσ − dim(kerσ∩[0⊕3H2(B)]),
    rS injective ⇔ pr₁(kerσ)=H2(B(-1)),
    rS=0 ⇔ kerσ⊂0⊕3H2(B).

A sufficient, not asserted, injectivity criterion is H2(B(1))=0 and surjectivity of H1(9B(1))→H1(5B(2)); then V=H2(E), J=0, and (5) projects onto the full ten-space. More generally one only needs pr₁(V)=H2(B(-1)) and σ(V)=σ(V∩ker pr₁), which allows every auxiliary σ error to be removed without altering the ten-component.

The improvement is that all possible surviving detector directions now occur inside a fixed sixteen-dimensional group, and only six auxiliary directions can be lost under the unit projection. The positive-twist H1/H2 groups and σ are retained, not declared zero. No nonzero rank, actual vanishing, or physical obstruction value follows without further input.

The cusp-supported map β from the preceding normalization proof remains independent after rS is tested. Injectivity of rS would suffice for zero fourth-power image; it is not established here.

## Scope

Only universal module structure, representation identities, cohomology, and functorial duality are used. No actual HM/source coefficients, selected rank instance, physical source, or any of the thirty obstruction values are evaluated.  The only arithmetic is the displayed Hilbert/cohomology dimension identities.
