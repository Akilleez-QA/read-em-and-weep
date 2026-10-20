# Ramified invariants: the module obstruction survives endomorphism descent

## Result

Normalized canonical trace and equality of characteristic/HKR classes do not imply descent of a locally free equivariant module through a ramified quotient. There is a local obstruction already in multiplication of character eigensheaves. It occurs before any mixed obstruction class is evaluated.

In the universal sign-ramification model below, invariants of an equivariant free module are free over the invariant square-zero algebra if and only if its representation on the closed-point fiber is trivial. For two independent ramification factors, the same criterion holds for the full local stabilizer. Scalar nontrivial characters satisfy endomorphism descent but fail this module criterion. A root line therefore cannot be cancelled from a module descent argument merely because it cancels from End.

These statements concern a universal local model, not a computation of the physical deformation, its jets, or its obstruction values.

## 1. A free equivariant line whose invariants are not free

Work over a characteristic-zero field k. Put B=k[[u]], R=k[[x]] with x=u², and

    D=B[s]/(s²).

Let G=Z/2 act by u↦−u and s↦−s. Then

    A=D^G=R⊕Rε,     ε=us,     ε²=0.

Thus A is the split square-zero algebra with a locally free rank-one coefficient ideal I=Rε. The cover is ramified at x=0. Let M=D e be free of rank one, with g(e)=−e. Its invariants are

    P=M^G=Rm⊕Rn,     m=ue,     n=se,
    εm=xn,           εn=0.                              (1)

These formulas follow by separating even and odd powers of u. They imply

    IP=xRn,
    P/IP=Rm⊕(R/(x))n.                                 (2)

If P were free of rank one over A, its quotient by I would be free of rank one over R, contradicting (2). More generally it cannot be any locally free A-module at the closed point: its generic A-rank is one, whereas its minimal number of local generators is two. Away from x=0, m is an A-basis, since n=x^−1 εm.

There is also a direct flatness test. For A itself, kernel(ε:A→A)=image(ε:A→A)=Rε. For P,

    kernel(ε:P→P)=Rn,
    image(ε:P→P)=xRn.

Thus P is not flat over A at the branch point.

Exactness of invariants does not fix this. It gives

    0 → (sM)^G=Rn → P → (M/sM)^G=Rm → 0,

but the invariant algebra ideal acts with image IP=xRn, strictly smaller than (sM)^G. In particular invariant formation and the desired module reduction are different operations here:

    P/IP ≠ (M/sM)^G.

The ordinary invariant sheaf (M/sM)^G is an R-free line. That fact does not mean that it pulls back to the original equivariant line: the adjunction map B⊗R Rm→Be sends m to ue and fails to be an isomorphism at u=0.

## 2. Endomorphism descent is genuinely weaker

Upstairs, End_D(M)=D and conjugation removes the sign of e. Consequently

    (End_D M)^G=A.

At order zero, End_B(Be)=B and its invariant algebra is R. Both endomorphism statements hold despite failure of module descent.

In fact the natural map from invariant upstairs endomorphisms to endomorphisms of the invariant module need not be an isomorphism. Every R-linear endomorphism of P commuting with (1) has matrix

    [[a,0],[c,a]],     a,c∈R,

in the basis (m,n). Indeed commutation with [[0,0],[x,0]] and the fact that x is a non-zero-divisor force precisely this form. Hence

    End_A(P)=R[δ]/(δ²),     δ(m)=n, δ(n)=0,

while the natural map A→End_A(P) sends ε to xδ. It is not surjective at x=0.

Thus neither End_D(M)^G=A nor an ordinary endomorphism-sheaf identification establishes an equivalence of locally free module categories or a Morita equivalence through invariants.

## 3. Necessary and sufficient character criterion in the universal local model

Let M be any finite free D-module with semilinear G-action. Its closed-point fiber W=M/(u,s)M is a representation W=W_+⊕W_−. There is a G-equivariant D-module isomorphism

    M ≅ D⊗k W.                                         (3)

Proof: choose a k-linear section of M→W, average it over the finite group to make it equivariant, and extend D-linearly. The resulting map reduces to an isomorphism modulo the maximal ideal and is an isomorphism by Nakayama (or invertibility of its determinant). This is an existence argument; no canonical frame is asserted.

Writing a=dim W_+ and b=dim W_− gives

    M^G ≅ A^a⊕P^b.

Its generic A-rank is a+b, while its fiber dimension over A/(x,ε)=k is a+2b. Therefore

    M^G is A-free at x=0  ⇔  b=0.                       (4)

This is a proved necessary and sufficient local criterion, not merely an example. In the ordinary reduced ramified cover the usual equivariant descent criterion is also triviality of stabilizer action on fibers. Endomorphisms only see the conjugation representation: End(W) has trivial stabilizer action if and only if the stabilizer acts on W by scalar matrices. In particular a scalar sign on every vector is invisible to End and violates (4).

## 4. Two independent factors and the surviving mixed product

Now put

    B=k[[u,v]],   R=k[[x,y]],   x=u², y=v²,
    D=B[s,t]/(s²,t²),

with G=(Z/2)². Its first generator negates u,s and fixes v,t; its second negates v,t and fixes u,s. The invariant algebra is

    A=R[ε,η]/(ε²,η²),     ε=us, η=vt,
    εη=uvst.

The mixed term is retained: st is not set to zero. Let M=De carry the character (−,−). Then P=M^G has R-basis

    m00=uv e,  m10=v s e,  m01=u t e,  m11=st e.

Its action is

    εm00=xm10,    εm01=xm11,    εm10=εm11=0,
    ηm00=ym01,    ηm10=ym11,    ηm01=ηm11=0,
    εηm00=xy m11.                                      (5)

In particular the mixed ideal acts through xyRm11, whereas the invariant upstairs mixed module ideal is (stM)^G=Rm11. The discrepancy is supported on the branch divisors. For J=(ε,η),

    P/JP ≅ Rm00 ⊕ (R/(x))m10 ⊕ (R/(y))m01
                    ⊕ (R/(x,y))m11.                    (6)

At x=y=0, four generators are required for a generically rank-one A-module. Away from both branch divisors it becomes free.

The same equivariant frame argument proves the full criterion. Decompose the closed-point fiber of a free equivariant D-module into characters W_ab, where a,b∈{0,1} denote signs. The invariant summand for W_ab has generic A-rank dim W_ab and requires 2^(a+b) dim W_ab generators at the closed point. Therefore

    M^G is A-free at the double branch point
       ⇔ W_10=W_01=W_11=0.                             (7)

At a point on only one branch divisor the criterion is triviality for the one generator in that local stabilizer. Spectator smooth coordinates can be added without changing any argument.

## 5. The coefficient-multiplication obstruction is intrinsic

For the one-factor model write B=B_+⊕B_− with B_+=R and B_−=Ru. The ramification defect is exactly the multiplication map

    B_−⊗R B_− → B_+,     u⊗u ↦ x.                      (8)

Each character summand is a line; (8) nonetheless fails to be an isomorphism at the branch point. For a sign root line, the invariant square-zero coefficient times the invariant reduced module is governed by this map. This is why knowing only the coefficient line (even with its exact normalized trace) loses essential information.

This obstruction also persists for a general first-order associative deformation with the same underlying equivariant B⊕sB, s²=0, ordinary reduced multiplication, and an equivariant locally free module reducing to the sign line. Multiplication of an order-one algebra element with an order-zero module element is fixed by the reduced module structure: additional first-order product terms would be multiplied by s² and vanish. Thus the map

    I⊗R (M/sM)^G → (sM)^G

still has image xRn. A free invariant A-module would have its I-action surject onto its reduction kernel. Consequently this coefficient defect cannot be repaired just by changing the first-order Hochschild cocycle. This assertion presumes the stated flat underlying deformation and usual square-zero ideal identification; it does not assert those data for an unspecified physical presentation.

For independent factors, (8) tensors to multiplication by xy in the mixed character. The split model (5) proves failure explicitly with all mixed terms present. No claim that an arbitrary interacting mixed deformation has exactly the presentation (5) is needed.

## 6. Application boundaries for the supplied root line

The supplied geometry has F=N⊗p*E and N²=p*O(1). There is a canonical ordinary equality

    End(F)=p*End(E).

It does not say N descends. In fact N cannot be the ordinary pullback of a line on P²: if N=p*O(k), then p*O(2k−1) would be trivial. This is impossible for finite surjective p, since a nonzero integral power of the pulled-back ample hyperplane class is not trivial. Hence no integral k exists. Assuming a genuine equivariant structure on N, the ordinary finite-quotient descent criterion forces nontrivial stabilizer action somewhere. An equivariantly compatible square identity says that these scalar stabilizer characters have order dividing two; it does not make them trivial. An underlying nonequivariant square identity alone does not specify the linearization. If equivariance is only projective, the appropriate gerbe/stack must additionally be specified.

The universal counterexample uses exactly a nontrivial scalar order-two character at simple ramification. It shows why cancelling N in End, matching normalized trace and the corrected HKR characteristic class, and proving compact pure-lift uniqueness do not supply ordinary module descent through the quotient. It does not assert that the specific physical truncated deformation is the split local algebra above or that every possible corrected/gerbe transport is impossible.

A proposed comparison must instead provide the actual equivariant local algebra/module transport and check coefficient multiplication and reduction compatibility at inertia strata, or use a genuinely specified stack/gerbe/Morita construction that retains the root character. Untwisting by N at order zero is legitimate; extending that operation to deformed modules requires additional structure and proof. A rational cohomological expression H/2 is not such a construction.

## 7. Why the HKR match is insufficient, even in the weakest case

In the split synthetic model every ambient first-order Hochschild deformation class is zero, so its HKR class and any normalized-trace image agree identically. Nevertheless the free equivariant line has nonfree invariants. Thus an implication based on HKR matching alone is false. The stronger coefficient argument in §5 explains why nonzero first-order bidifferentials do not automatically resolve the branch character issue.

The supplied normalized canonical trace controls a linear identification of coefficient eigensheaves and characteristic evaluations. It does not invert the branch factor in (8), identify invariant reduction with quotient by the invariant ideal, or prove a chain-level module transport. The remaining mixed physical comparison therefore cannot be discharged by these cohomological identities alone.

## Inputs and scope

Read: ../../null-root-characteristic/root-characteristic-0527/RESULT.md; ../../null-pair-quotient-bracket/canonical-bracket-0517/RESULT.md; ../../null-pure-lift-uniqueness/pure-lift-uniqueness/RESULT.md. All additional work is formal local algebra, finite-group averaging, and the elementary Picard group of P². No physical source or jet values are evaluated in this argument.

The accompanying check_synthetic.py is an elementary numerical illustration of (1). It checks the invented two-dimensional dual-number action at four synthetic scalar values. The exact proof above is independent of that check; no physical conclusion is inferred from it.
