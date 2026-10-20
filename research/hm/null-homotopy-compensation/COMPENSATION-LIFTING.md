# The compensation-lifting obstruction

## Result and scope

A proposed degree-one change J admits projected compensation precisely when its image in the relative cochain complex Hom(A,C)/ΠHom(A,B) is closed. It comes from actual changes of the two auxiliary homotopies precisely when that closed cochain itself is induced by a closed degree-minus-one map U:B→C composed with T. Equality of relative cohomology classes is insufficient. If the compensation F is prescribed, its exactness and a further closed-map quotient obstruction must both vanish.

These statements give necessary and sufficient algebraic tests, including for killing K on im Δ. Geometric realization and the regular-domain requirements remain additional premises. All examples and executable matrices below are invented finite complexes over Q. No physical source or retained-test value is evaluated. No value of an unknown target is claimed.

## 1. Setup

Use the cochain complexes (A,Δ),(B,δ_B),(C,δ_C), degree-zero chain map Π:B→C, degree-two chain map T:A→B, and convention

    d f = δ_target f − (−1)^|f| f δ_source.

Set X=Hom(A,B), Y=Hom(A,C), H=Hom(B,C). Define P:X→Y by Pv=Πv, and R:H→Y of degree two by Ru=uT. Since Π,T are chain maps and |T|=2, dP=Pd and dR=Rd. Let

    Qrel = Y/im P,
    q:Y→Qrel.

Here im P is its degreewise image, a subcomplex; Π need not be injective or surjective. This is an ordinary quotient of cochain complexes, not a derived quotient. Write Z^k for closed cochains and B^k for boundaries of the named complex.

For the fixed original presentations

    Π′=d Qdot,       T′=E−d Q,       K=Qdot T−ΠQ,

an actual auxiliary change has

    dU=0,   J=RU−PV,   F=dV,
    U∈H^−1, V∈X^1, J∈Y^1, F∈X^2.                    (1)

It automatically obeys dJ+PF=0. Conversely these choices produce a valid new algebraic presentation with the same Π′,T′. Any restrictions on the literal geometric construction are not supplied by (1).

## 2. Projected existence versus actual existence when F is free

### Theorem 1

For a specified J∈Y^1:

(a) Some F∈X^2 satisfies dJ+PF=0 if and only if

    o_proj(J)=[dJ]∈coker(P:X^2→Y^2)

vanishes, equivalently qJ∈Z^1(Qrel).

(b) Some U,V satisfy (1), with F allowed to be dV, if and only if

    qJ∈qR(Z^−1(H)).                                      (2)

Thus, after (a), the complete additional obstruction is

    o_actual(J)=[qJ]∈Z^1(Qrel)/qR(Z^−1(H)).               (3)

Proof. Part (a) is the definition of image/cokernel, including the minus sign in choosing F. If (1) holds, qJ=qRU. Conversely (2) gives J−RU∈im P^1, so choose V with PV=RU−J. Setting F=dV gives dJ=−PdV. This proves necessity and sufficiency, with no assumption on P's kernel. ∎

Equivalently, actual J form the subspace RZ^−1(H)+PX^1 of Y^1, whereas projectable J form ker(Y^1→coker P^2), J↦[dJ]. Formula (3) is the quotient of these two spaces, under the evident quotient identification.

The obstruction is deliberately at the cochain level. Put S=qRZ^−1(H)⊂Z^1(Qrel), and let Sbar be its image in H^1(Qrel). There is an exact sequence

    0 → B^1(Qrel)/(B^1(Qrel)∩S)
      → Z^1(Qrel)/S
      → H^1(Qrel)/Sbar → 0.                              (4)

This follows by taking the natural cohomology projection and its kernel. Thus a cohomology calculation discards precisely the possible residual boundary obstruction on the left. It cannot in general certify (2). Example 2 exhibits this failure even when J is already a boundary in Y.

## 3. Prescribed compensation has two further tests

### Theorem 2

Suppose a pair (J,F) satisfies dJ+PF=0. It is realized by (1) if and only if:

1. F∈B^2(X), so there exists V0∈X^1 with dV0=F;
2. for one, hence every, such V0, the following class vanishes:

    [J+PV0] ∈ Z^1(Y)/(RZ^−1(H)+PZ^1(X)).                 (5)

Proof. The numerator is closed because dJ+PF=0. Every primitive of F is V0+W with W∈Z^1(X). The equation J=RU−P(V0+W) is equivalent to J+PV0=RU−PW. This is exactly (5). Changing V0 adds an element of PZ^1(X), so the obstruction is independent of the primitive. ∎

Exactness of F includes dF=0. The projected equation alone only forces P(dF)=0; it does not imply closure or exactness of F. In particular, even if a specified J has some actual compensation, an arbitrarily chosen projected compensation need not be the actual one. Theorem 1 is existential in F; Theorem 2 is for its prescribed value.

A cone warning makes the same distinction explicit. On W^k=Y^k⊕X^(k+1), set D(y,x)=(dy+Px,−dx). A projected pair is a W-cocycle only if dF=0 also holds. Actual pairs have the form

    (RU,0)+D(0,−V).

Replacing this restricted boundary by an arbitrary cone boundary D(y0,x1) additionally allows (dy0,0). That allowance is not justified by the auxiliary homotopy changes. Cone cohomology membership alone can therefore be too weak, exactly as Example 2 shows.

## 4. Killing the defect requires a restriction-lift test

Let r:Y^1→Y^2 be the linear map

    r(g)=gΔ,     r(g)_n=g_(n+1)Δ_n.

It records g on all input boundaries; r(g)=0 is exactly g|im Δ=0. Define the actual-change map

    L:Z^−1(H)⊕X^1→Y^1,      L(U,V)=RU−PV.

### Corollary

There is an actual presentation change with (K+J)|im Δ=0 if and only if

    [rK]=0 in coker(rL),                                  (6)

or equivalently the linear system rL(U,V)=−rK is soluble. It then has F=dV automatically. If the literal E must stay fixed, replace X^1 by Z^1(X) throughout (6). If F is prescribed, also impose dV=F; equivalently first use Theorem 2 and then the restriction equation.

This follows directly from (1), so it tests exact operator removal on every boundary, not removal on just selected samples. For a bounded specified family ΔZ_i only, replace r by evaluation on that family; the resulting weaker test certifies only those inputs.

Necessary conditions such as boundary-exactness of individual defect outputs, or vanishing of a relative cohomology class, do not replace (6). Nor does a solution prove the paired correction vanishes. Writing P_pair(Z)=KΔZ+ΠEZ, a valid change gives

    P_pair,new(Z)−P_pair,old(Z)=−δ_C(JZ).

If K_newΔ=0, this becomes

    Π(E+F)Z=KΔZ+ΠEZ−δ_C(JZ).                              (7)

Thus the surviving contribution may simply move into the connection term. To remove it in a regular trace/cohomology calculation one still needs the regularity of JZ and all admitted comparison maps, closure when claiming cohomology, a functional annihilating genuine boundaries, and an independent vanishing/cancellation of the full remaining paired expression. The other families of the complete remainder are unaffected by this algebraic permission.

## 5. Small finite counterexamples

All omitted groups and maps are zero; all scalars are rational. Every Π and T below is nonzero and is a chain map of its specified degree.

### Example 1: projected compensation exists, but F is not exact

    A^0=Q a;
    B^2=Q b;
    C^1=Q e, C^2=Q c, δ_C e=c;
    Πb=c, Ta=b, Ja=e, Fa=−b.

Then dJ(a)=c and ΠF(a)=−c. Thus projected compensation exists. But X^1=0, so no nonzero F is dV. Also any U:B^2→C^1 has U(b)=u e, and dU(b)=u c; closed U must be zero. Hence no actual J is nonzero. This obstructs actual realization even though F is closed and the projected equation holds exactly.

### Example 2: compensation is exact and J is Hom-exact, still not realizable

    A^0=Q a, A^1=Q b, Δa=b;
    B^2=Q c;
    C^1=Q e, C^2=Q c_C⊕Q f, δ_C e=f;
    Πc=c_C, Ta=c, Tb=0;
    Ja=e, Jb=−f, F=0.

Then dJ(a)=f−f=0 and dJ(b)=0. Set H0∈Hom^0(A,C) by H0(a)=0,H0(b)=e. Directly dH0(a)=−e,dH0(b)=f, so J=−dH0. Consequently qJ is zero in relative cohomology, and F=0 is exact.

Nevertheless a degree-minus-one U has U(c)=u e and dU(c)=u f, so dU=0 forces U=0. A degree-one V has V(a)=0,V(b)=v c. Thus every actual J=−ΠV has J(a)=0 and J(b) in Q c_C, contradicting the proposed values. No choice of compensation can repair this J. In particular, qJ is a nonzero exact cochain in Qrel, outside S=0. This verifies the left-hand obstruction in (4) concretely.

### Example 3: removing KΔ transfers rather than erases the correction

    A^0=Q a, A^1=Q b, Δa=b;
    B^2=C^2=Q c, Π=id, Ta=c,Tb=0;
    Ka=0,Kb=c, E=0.

Take Qdot=0,Qb=−c,Qa=0; then K=Qdot T−ΠQ. The presentation derivatives can consistently be Π′=0,T′=−dQ, so this example fits the original setup. For an actual coefficient family take T(t)a=(1+t)c at t=0, and Δ fixed.

Choose U=0,Vb=c,Va=0. Then J=−K, F=dV sends a to c, and K_new=0. The paired correction on a remains c, now from ΠF(a). If E is required fixed, dV=0 forces V=0, so no removal is possible. There is no C^1, hence c is not a boundary. The executable rank test verifies both outcomes.

## 6. Explicit finite linear constraints

Choose bases in any finite-dimensional bounded instance. For every relevant degree n,m, unknown matrices U_m:B^m→C^(m−1), V_n:A^n→B^(n+1) must satisfy

    δ_C,m−1 U_m + U_(m+1) δ_B,m = 0;
    U_(n+2) T_n − Π_(n+1) V_n = J_n;
    δ_B,n+1 V_n + V_(n+1) Δ_n = F_n.                     (8)

The third row is omitted when F is free, in which case it defines F. If only defect removal is specified, replace the second row by

    (K_(n+1)+U_(n+3)T_(n+1)−Π_(n+2)V_(n+1)) Δ_n=0.       (9)

For E fixed, set every F_n=0. For prescribed J,F, projected feasibility alone is merely

    δ_C,n+1 J_n + J_(n+1)Δ_n + Π_(n+2)F_n=0.

These are linear equations: T,Π,Δ,δ and J,F,K when specified are data, not unknowns. Vectorization via vec(AWB)=(B^t⊗A)vec(W) yields a single matrix equation Mx=b. Feasibility is exactly rank M=rank[M|b] over the stated field. A basis for ker d_H on H^−1 may instead eliminate the first row in advance. This is an abstract linear test, not an evaluation of physical data.

## 7. Reproduction and provenance

Run `python test_synthetic.py` in this directory with Python and SymPy. It constructs only the invented complexes in §5, builds Hom differentials and composition matrices, and checks projected versus actual rank conditions, exactness, and fixed-E versus free-E defect removal using exact rational arithmetic. Recorded output is in TEST_OUTPUT.txt.

Formal inputs read:
- HOMOTOPY-CHOICE.md, especially §§1–3 and 5.
- https://github.com/Akilleez-QA/read-em-and-weep/blob/4659e4425c6b5ab6b1899e6af93656ac03ff0862/research/hm/null-complete-remainder-normal-form/RESULT.md, especially §§2 and 5.

The cohomology-trap witness in Example 2 was checked algebraically and by the synthetic program in the original preparation. The advance beyond those formal inputs is the complete cochain/cokernel obstruction, the prescribed-F refinement, and the exact restriction-lift criterion. None authenticates additional geometric domains or evaluates the remaining target.
