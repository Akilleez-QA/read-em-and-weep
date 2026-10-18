# RS01: the same fresh five-term source is closed

## Result, representative and premises

Fix the declared ambient algebroid over k[h]/(h³), characteristic zero, on the four elliptic factors. Use the actual determinant-one physical row transitions, physical invariant vector derivatives and compensated gerbe of the pinned model. On the fresh source-first ordered common cover, take exactly the first lift

    s_r=T_N14,r F_r,   k_r=-mu_r(g^-1,g)/2,
    u_r=g(s_r I+k_r),   r=p=(0,1), q=(2,3).

FD's accepted source/domain theorem proves delta s_r=F_r for this same freshly evaluated source. Every N14 prism and standard branch is retained in T; no historical nonlinear scalar is substituted. The first-order rank-two identity delta k_r=-C_r^0 then gives the **actual full first-order module equation** delta(s_r I+k_r)=b_r I-C_r.

Let M be the normalized full-sign order-two module residual for this fresh lift, with second-order transition coefficient set to zero. Let M0 be the SAME `globalCross` with u_r^0=g k_r, retaining seven kinetic terms and all three negative gerbe terms. Define W=s_q k_p+s_p k_q. The concrete conclusion is

    Rsharp=M0^0+F_q k_p,ik+F_p k_q,ik+E_p(s_q)+E_q(s_p)
          =M^0+delta W.                                      (A)

Thus delta Rsharp=0. It represents the same full-sign H²(End E) class as M, by the scalar-character argument in §5. This is neither pointwise Rsharp=M nor the assertion that the five individual summands are closed.

All source identities are used in the same physical row convention before any transpose. Matrix order, inverse and all endpoint/moving-frame derivatives remain. The accepted ambient model/contraction premises, source first-lift and character conventions are explicit below; they are not proved by a compiler hash. No historical-order cochain equality, actual coefficient value, complete outer-domain witness, resource budget or obstruction verdict is supplied.

## 1. The actual ambient two-jet and both coherence identities

The source is `ambient-second-jet.md` at08b73637d4136f91606aad332c46cafd064417f8, not an unspecified associator oracle. Its commuting derivations are

    V_i=y_i partial_xi+(3x_i²-1)/2 partial_yi,
    pi=V0 wedge V1+V2 wedge V3,
    f star g=fg+h mu1(f,g)+h² mu2(f,g),
    mu1=pi/2,   mu2=pi*pi/8.

The exponential construction for commuting derivations proves associativity to this order, also on ordered matrices. On the two line charts, q=y/x, a0=-x/2, a1=1/(2x), so Vq=delta a. On any refinement, including the fresh legal-mask/common order, pull back these SAME local sections. Put lambda=15/4,

    b=lambda(q0 cup q1+q2 cup q3),
    T=lambda[(a0 cup q1)V1+(q0 cup a1)V0
             +(a2 cup q3)V3+(q2 cup a3)V2],
    Fij=1+h² Tij,    Aijk=1+h bijk+h² bijk²/2.

Here a0/a1 in the formula for T carry coordinate indices; their vertex values are the displayed finite/infinity chart choices. The ordinary AW differential gives delta b=0 and delta T={b,-}: delta(a cup q)=delta a cup q and delta(q cup a)=-q cup delta a. The commutator of A under star is h²{b,-} modulo h³, hence

    Fij Fjk=Ad_star(Aijk) Fik.                            (B1)

The second coherence identity is

    Aijk star Aikl=Fij(Ajkl) star Aijl.                    (B2)

Indeed corrections between the order-h scalar factors start at h³, as does Fij acting nontrivially on h b. The remaining order-two scalar equality is the exponential of delta b=0. Each T is an ordinary derivation, so Fij is a star-algebra map to this order. Both identities are proved by the displayed formulas; no physical coefficient test is needed or performed. These are precisely the ambient assumptions in the pinned closure proof, now attached to the actual fresh source application.

## 2. Exact universal module-defect identity

For any transitions G in this SAME ambient algebra define

    Eijk=Fij(Gjk) star Gij-Aijk star Gik.

Associativity, the algebra-map property and (B1) expand the single triple product in two ways. With (B2), subtraction gives the exact identity

    Aijk star Eikl + FijFjk(Gkl) star Eijk
       -Fij(Ajkl) star Eijl -Fij(Ejkl) star Gij=0.       (C)

For transparency set X=FijFjk(Gkl), Y=Fij(Gjk), Z=Gij, A=Aijk, V=Fik(Gkl), W=Gik, B=Aikl, H=Gil, C=Fij(Ajkl), D=Aijl, T=Fij(Gjl). Then XA=AV is (B1), AB=CD is (B2), and the left side of (C) expands in the free associative algebra to

    (AV-XA)W+(CD-AB)H.

`formal_identities.defect_syzygy` verifies this expansion without matrix commutation or a source value; the tests also reverse each defect sign independently. Both ambient relations are essential.

The classical transitions satisfy E^(0)=0 by g_jk g_ij=g_ik. The first lift above satisfies E^(1)=0 by FD and the actual rank-two identity. Taking the coefficient h² in (C) therefore gives

    Rikl+gkl Rijk-Rijl-Rjkl gij=0.                       (D)

There are no lower-defect cross terms left. Normalize on the **left**, M_ijk=gik^-1 Rijk. Multiplying the ordinary row-End delta M on the left by gil gives the negative of (D); thus delta M=0. In particular one must not try to prove closure from the mixed residual alone while omitting ambient T or mu1(b,g) from the complete unprojected problem.

## 3. Why its full-sign component is the actual seven-plus-three source

The source's deck linearization and physical frame transport are those of `closure-and-characters.md` and the accepted PH theorem. In common physical End frames, each actual pair lift has character chi_p or chi_q, including its scalar T solution: fixed cover maps and partitions are deck invariant. The scalar q_i and physical V_i have character chi_i; central line-frame signs cancel in normalized End. This character statement is not inferred from arbitrary unnormalized transition entries.

In the full defect, T has trivial character. The full-sign parts of mu1(b,g) vanish: same-pair contraction has trivial character, and cross-pair derivatives of b vanish because its coordinate sets are disjoint. The surviving mixed component, with A=gij, B=gjk, G=gik and u_p,u_q as above, is exactly

    u_p,jk u_q,ij+u_q,jk u_p,ij
    +mu_p(u_q,jk,A)+mu_q(u_p,jk,A)
    +mu_p(B,u_q,ij)+mu_q(B,u_p,ij)
    +mu2,mixed(B,A)
    -b_p u_q,ik-b_q u_p,ik-b_p b_q G.                  (E)

This is the pinned `crossResidual` plus all three `globalCross` subtractions. After left normalization it is M's full-sign component. The two disjoint orders in the Moyal square give

    mu2,mixed(B,A)=1/4[
       (V0V2 B)(V1V3 A)-(V0V3 B)(V1V2 A)
       -(V1V2 B)(V0V3 A)+(V1V3 B)(V0V2 A)].

The coefficient is1/4, not1/8. The mixed part of -b²G/2 is -b_p b_q G. The source's distinct-axis jets carry no repeated-coordinate factorial or omitted y derivative: form the physical derivatives with coherent moving frames, then remove the common y0y1y2y3. The existing SC4270 graph implements these same derivatives and terms. Character projection commutes with delta, so this actual normalized mixed M is closed.

## 4. Trace-free scalar elimination and the explicit positive boundary

Let C_r=G^-1 mu_r(B,A), c_r=tr(C_r)/2 and F_r=b_r-c_r. In the actual determinant-one rank-two model,

    delta k_r=-C_r^0,   tr(k_r)=0.

The identities are inherited from the authenticated first-order source and contraction premises; no determinant/physical-polynomial scan is rerun. The trace-free baseline is formed **after** all gerbe subtractions in M0. In particular M0 already includes -b_p k_q,ik-b_q k_p,ik-b_p b_q I. A baseline from `crossResidual` before those terms would require different Fk corrections and is not used.

For the s_q terms involving k_p, put kbar=A^-1 k_p,jk A and use C_p^0=-(kbar-k_p,ik+k_p,ij). The undifferentiated trace-free difference is

    s_q,jk k_p,ij+s_q,ij kbar+(s_q,jk+s_q,ij)C_p^0
       =-delta(s_q k_p)+(delta s_q)k_p,ik
       =-delta(s_q k_p)+F_q k_p,ik.

The same calculation with p and q exchanged gives the second term. `formal_identities.reduction_identity` expands the exact identity; the wrong sign of delta W fails.

The scalar derivative terms in the two product-rule expansions are precisely

    E_r(t)=1/2[(Va t_jk)Lb-(Vb t_jk)La
                 +(Vb t_ij)Ua-(Va t_ij)Ub],
    Ld=A^-1 Vd A,   Ud=A^-1 B^-1(Vd B)A.

The undifferentiated terms above and these derivative terms together exhaust the linear scalar dependence. Both endpoint derivatives and product order are mandatory. Determinant one makes Ld and Ud traceless, so E is traceless. Quadratic s_p s_q terms and scalar gerbe corrections are central and disappear under the trace-free projection, without being assumed individually zero. This proves

    M^0=M0^0-delta W+F_q k_p,ik+F_p k_q,ik
                        +E_p(s_q)+E_q(s_p).

Rearranging proves (A), including its **positive** boundary. This is the identity between the actual fresh residual and the actual source emitted by the existing compiler. Since trace projection commutes with row-End delta and delta²=0, it proves delta Rsharp=0. No closure of M0 or E alone is asserted.

## 5. Class identification without evaluating a central homotopy

The full-sign decomposition End E=O I direct-sum End0 E is a cochain splitting: conjugation fixes I and preserves trace in characteristic zero. M's central part is separately closed. Under the stated deck linearization, its scalar eigensheaf on (P1)^4 is O(-2,-2,-2,-2). Each O(-2) has tensor Cech harmonic space only in degree1. The fourfold tensor product therefore has scalar cohomology only in degree4, and H² in this character is zero. Thus M-M^0 is exact in the full-sign sheaf cohomology. Together with (A), Rsharp has the SAME full-sign obstruction class as the actual M of the chosen fresh first lift.

The trace is not asserted pointwise zero. Its quadratic scalar terms need not fit the smaller regularization ledger of Rsharp; this proof does not allocate them a5251 domain, compute their homotopy, or infer a finite cutoff comparison. The abstract scalar H² statement suffices for this class identification.

The chosen first lift is exactly the fresh FD homotopy lift. Scalar first-lift differences of pure pair character would be boundaries because scalar H¹ of that pair character is zero; any first-order gauge comparison must still retain its induced order-two transition term. RS01 needs no such comparison: it defines M for the chosen lift directly. It makes no equality claim about a historical nonlinear cochain re-evaluated in another order.

## 6. Concrete source-bound constructor and limits

`r_binding.ActualFullSourceApplication(repo=None)` authenticates the exact immutable PR87 SC/FD/P/Q definitions and the original ambient/model/source formulas, then composes the fixed `ActualDomainApplication`. It accepts no source callback, arbitrary catalog, forged proof flag or replacement ambient identity. `describe(ordered_owners)` requires a strict increasing same-seed triple with distinct full owner occurrences. It binds source slots0,1,2 to those supplied owners and includes both canonical FD pair descriptions.

The SC4270 graph is read, not rebuilt. Its20 existing universal source-triple records are checked for all five branches, seven kinetic and three gerbe nodes, left normalization, and the exact five-child residual sum. Physical jets are checked for differentiated moving frames and at most two distinct axes. The actual g leaf denotes `D_b (P_a I_b)^t D_a^-1` with the pinned carrier primitives, physical line frames and constants; q leaves denote the same mask differences and y/x sections as the ambient gerbe. This semantic dictionary, the source equations (E)/(A), and the published compiler reduction bind the grammar to the actual source. Byte identity alone would not establish them.

The result is source identity/closure and class identification, not a physical coefficient executor. Coefficient, stream and actual fiber methods always refuse. Full96 fibers remain descriptors. The new package does not reimplement scalar solving, generic two-jet algebra, cover algorithms, coefficient convolution or scans. All tests are free-word/rational artificial controls or source metadata. No physical coefficient, jet, residual, fiber list or matrix payload is evaluated.

Still separate: independent RS review; whole-lift J0..J3 source inclusion/domain compatibility; complete outer54/29/5251 standard/prism/restriction regularity; actual coefficient programs/fibers and aggregate resource schedule; authenticated detector values and global obstruction decision. Closure and source identification do not discharge those domains or give an obstruction value.
