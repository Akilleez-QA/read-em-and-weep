# A sharp boundary-image obstruction for free actual compensation

## Result and scope

For an already valid presentation K=Qdot T−ΠQ over a field, with unrestricted linear auxiliary maps and freely chosen compensation F=dV, actual removal of K on every input boundary is equivalent to the single inclusion

    K(im Δ) ⊂ im Π + im δ_C.                                (A)

This is stronger than merely restating the restriction-lift linear system: it eliminates its unknowns U,V completely. It uses the special factorization of K and splitting of vector spaces. It does not hold as an assertion of geometric realizability, owned regularity, fixed E, prescribed F, or module-linear splitting without additional hypotheses. In particular it does not establish any retained value or any cancellation among the four surviving families.

All reasoning below is universal formal algebra. The illustrative complex is newly invented. No actual source/model/owner/jet evaluation, physical polynomial matrix product, production import, geometric experiments was used. Nothing was posted externally.

## 1. Setup and quotient obstruction

Use the supplied cochain complexes (A,Δ),(B,δ_B),(C,δ_C) over a field, chain maps T:A→B of degree 2 and Π:B→C of degree 0, and

    Π′=d Qdot,  T′=E−dQ,  K=Qdot T−ΠQ,
    M′=dK+ΠE,

where Qdot has degree −1 and Q,K have degree 1. Actual changes have

    dU=0,  J=UT−ΠV,  F=dV,
    K_new=K+J,  E_new=E+F.

Define degreewise vector-space quotients, without asserting they are cohomology groups,

    D^k=C^k/(Π(B^k)+δ_C(C^(k−1))),
    q_k:C^k→D^k.

For W^r=im(Δ:A^(r−1)→A^r), define

    Ω_r:W^r→D^(r+1),   Ω_r(w)=q_(r+1)(K_r w).             (1)

The theorem is that Ω=0 is necessary and sufficient for actual free-compensation removal K_new|W=0 in this unrestricted vector-space category.

## 2. The extension lemma that makes the criterion sufficient

Write Bnd_B^m=im δ_B^(m−1) and Bnd_C^m=im δ_C^(m−1).

Lemma. Any degree −1 graded linear map

    u:Bnd_B→Bnd_C

extends to a degree −1 Hom-closed map U:B→C. The same holds for a map specified only on an arbitrary graded subspace S⊂Bnd_B, after first extending it linearly into Bnd_C.

Proof. Choose graded splittings

    B^m=Bnd_B^m ⊕ H_B^m ⊕ L_B^m,
    ker δ_B^m=Bnd_B^m ⊕ H_B^m.

The differential identifies L_B^m with Bnd_B^(m+1). Choose a linear right inverse s_C^m:Bnd_C^(m+1)→C^m to δ_C. Set U=u on Bnd_B, U=0 on H_B, and, for l∈L_B^m, set

    U(l)=−s_C^(m−1)(u(δ_B l)).

Here u(δ_B l)∈Bnd_C^m, and the chosen section sends it to C^(m−1). Thus δ_C U(l)=−u(δ_B l).

On Bnd_B and H_B the identity δ_C U+Uδ_B=0 holds because their U-images are closed. On L_B it holds by the displayed defining requirement. Thus dU=0 in all degrees. No boundedness or finite dimensionality is needed if these linear splittings are available. ∎

## 3. Proof of the criterion

Necessity. If K_new w=0, then

    Kw=−UTw+ΠVw.

Because w is a boundary and T is a chain map, Tw is a boundary in B. Closedness of U implies Uδ_B=−δ_C U, so UTw is a boundary in C. Thus qKw=0.

Sufficiency. Let

    S^m=T(W^(m−2))⊂Bnd_B^m.

For w∈W^r,

    Kw=Qdot(Tw)−ΠQw.

Therefore Ω=0 says exactly that Qdot(S^m) is contained in

    Π(B^(m−1))+Bnd_C^(m−1).

Let qΠ:C^(m−1)→C^(m−1)/Π(B^(m−1)). The last condition says qΠ Qdot|S lies in the image of Bnd_C^(m−1) under qΠ. Choose a linear section of the surjection from Bnd_C^(m−1) onto that image. It gives a map u:S^m→Bnd_C^(m−1) such that

    qΠ u(b)=−qΠ Qdot(b) for b∈S^m.

By the lemma, extend u to a Hom-closed U:B→C. It follows that (K+UT)(W^r)⊂Π(B^(r+1)). Choose a linear lift

    V_W:W^r→B^(r+1),  ΠV_W=(K+UT)|W^r,

and extend V_W linearly to V:A→B of degree 1. Then K+UT−ΠV vanishes on W. Taking F=dV gives an actual change of both auxiliary homotopies and the required compensated presentation. ∎

Two facts are essential. First, K modulo im Π factors through T; a general candidate degree-one operator need not have this compatibility when T has a kernel. Second, V is free, so its restriction to W can be lifted and extended without imposing dV=0 or a prescribed derivative. These are why a necessary output condition becomes sufficient here, despite the general extension warnings in the earlier packets.

## 4. An outer-derivative formulation and complete separating witnesses

For every z∈A^n, the presentation identity gives

    q_(n+2)(M′z)=q_(n+2)(KΔz),                            (2)

because δ_C Kz and ΠEz vanish in D. Also M′=Π′T+ΠT′, so

    q_(n+2)(M′z)=q_(n+2)(Π′Tz).                           (3)

Consequently Ω vanishes if and only if qΠ′T vanishes on every A^n. The free actual defect-removal obstruction can thus be tested using the outer derivative Π′T alone. This is an equality in a quotient of cochains, not a license to drop ΠE in a Serre trace.

For every nonzero Ω_r(w), there is a linear functional λ:C^(r+1)→k with

    λΠ=0,  λδ_C=0,  λ(Kw)≠0.                             (4)

Conversely any witness (4) proves Ω≠0 and prohibits free actual removal. This is just dual separation in D; finite dimensionality makes it an ordinary finite linear algebra witness. It does not require Kw to be closed. For w=Δz the same functional satisfies

    λ(KΔz)=λ(M′z)=λ(Π′Tz).

Thus (4) is a complete formal detector of failure, not merely a necessary obstruction. Such a λ is not automatically the retained Serre/residue detector, continuous, geometric, or defined on the admitted regular domain.

One useful sufficient special case is C^k=Π(B^k)+Bnd_C^k in the relevant output degrees: then free algebraic removal is always possible. Surjectivity of Π is a still stronger sufficient case. Neither statement makes the compensated paired correction vanish.

## 5. Exact synthetic example with a nonclosed detected output

Over Q let

    A^0=Q a, A^1=Q w, Δa=w;
    B^2=Q b, B^3=Q c, δ_B b=c;
    C^2=Q e⊕Q p, C^3=Q f, δ_C e=f, δ_C p=0.

All unspecified groups/maps are zero. Define

    Ta=b, Tw=c;
    Π(t)b=p+t e, Π(t)c=t f;
    Qdot b=0, Qdot c=e;
    Q=0, E=0, T′=0.

Π(t) and T are chain maps. At t=0, Πb=p, Πc=0, and dQdot sends b to e and c to f, exactly Π′. Hence the presentation is valid and

    Ka=0, Kw=e.

But D^2=C^2/Q p, so Ω_1(w)=[e]≠0. The functional λ(e)=1, λ(p)=0 annihilates Π(B^2) and δ_C(C^1)=0. Thus no free actual correction can kill K on im Δ. Directly, every closed U has Uc=−δ_C Ub=0 because C^1=0, while ΠVw is a multiple of p and cannot cancel e.

Notice δ_C e=f≠0. The obstruction remains valid even though the detected output does not define a class in H^2(C). This prevents an accidental substitution of ordinary cohomology for D.

## 6. Relation to the complete remainder and precise remaining gap

The original four-family retained target remains unresolved. The theorem concerns exact elimination of the KΔ operator by unrestricted actual auxiliary changes with free F. Even when Ω=0 and that elimination succeeds, the paired term obeys the established identity

    Π(E+F)Z=KΔZ+ΠEZ−δ_C(JZ).

Its trace need not vanish; the contribution may move into ΠF. In the actual sheaf problem, the splitting construction supplies no homogeneous transition, character, owned denominator, full comparison-weight, or regularity guarantee for U,V,JZ. A module-linear or geometrically admissible extension can be obstructed even when this vector-space Ω vanishes. Fixed-E and prescribed-F problems retain their additional constraints.

Therefore the bounded advance is a sharp unrestricted algebraic obstruction, its constructive sufficiency proof, and a complete dual failure certificate. The remaining steps are to establish whether the required quotients or witnesses are meaningful in the admitted geometric domain, to realize any desired correction there, and independently to determine the full four-family retained trace. None of those steps is certified or evaluated here.

## Formal inputs

- https://github.com/Akilleez-QA/read-em-and-weep/blob/4659e4425c6b5ab6b1899e6af93656ac03ff0862/research/hm/null-complete-remainder-normal-form/RESULT.md
- [COMPENSATION-LIFTING.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/0c7f3f16ddea65616b2c6d4629c8b44f6fdae625/research/hm/null-homotopy-compensation/COMPENSATION-LIFTING.md)
- [HOMOTOPY-CHOICE.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/0c7f3f16ddea65616b2c6d4629c8b44f6fdae625/research/hm/null-homotopy-compensation/HOMOTOPY-CHOICE.md)
