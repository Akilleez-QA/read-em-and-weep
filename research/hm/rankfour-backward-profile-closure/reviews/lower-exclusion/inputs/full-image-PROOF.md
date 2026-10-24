# A strict dual-cubic image bound in the ordered rank-four (3,1) plateau

## 1. New result and exact scope

Retain the actual geometric hypotheses, original physical negative parameter line and fixed G=SL2(F5) marking of the five complete sources in INPUTS.json. Suppose the actual second fundamental form has generic rank four and maximal ordered plateau (k,l)=(3,1). Then the restriction of the dual derivative to any copy of T6 in H0(Q*(3)) has image of generic rank at most three.

More precisely, choose any equivariant inclusion T6 -> H0(Q*(3)) and compose its evaluation with the actual derivative to obtain

    psi: T6 O -> Q*(3) -> E*(1).

Its image is nonzero, hence has rank one, two or three, but never four. If its rank is one, its image is O(9), and the necessary source label is D. Such a copy exists because the actual Euler character of Q*(3) has coefficient +1 at T6. No five-type dual classification, canonical splitting of Q*, or injectivity of the evaluation bundle is needed.

We also give a complete 31-row necessary endpoint/defect ledger derived solely from the ordered ranks, endpoint persistence, determinant parity and invariant orbit semigroup. Twenty-four of these rows have positive defects. The ledger is a necessary overlist, not a realization claim; the image theorem does not eliminate the whole (3,1) plateau. It establishes neither generic SF rank at least five, square surjectivity, full-adjoint invertibility nor original proof repair.

No actual coefficients, parameters, jets, matrices, instance ranks, or historical 28/37/159-record enumeration are evaluated. The two finite shape lists below are newly derived within forced rank/degree windows. The rank-three theorem is not imported: every rank and cohomological inequality here is rederived for rank four and the unequal actual bundles.

## 2. Actual inputs and ordered stages

Work on T=P(W*) with its original determinant-one linearization. The physical irreducibles are

    1,W,A=Sym2 W,S4=Sym3 W,D=Sym4 W,T6=Sym5 W,P,W',V,
    dimensions 1,2,3,4,5,6,4,2,3.

V is the other even three-space, not A. The center-odd irreducibles are W,S4,T6,W'. All are self-dual, and G is perfect. The actual sequences are

    0 -> E -> H O -> Q -> 0,
    0 -> E  -> M3 O(-1) -> M4 O -> 0,
    0 -> Q* -> M3* O(-1) -> M2* O -> 0,

with rank E=17, rank Q*=13, both of degree -54, and

    M2=A+2V+3P+4D,
    M3=3W'+3S4+6T6,
    M4=2V+4P+3D,
    H=W M3-M2-M4=2A+2V+2P+2D,  dim H=30.

In particular

    chi(E(3))=W'+2T6,
    chi(Q*(3))=T6-2W-S4.                              (1)

The actual primary-slope source theorem supplies the four necessary E types

    D: D O(-2)+(W'+T6) O(-3)+V O(-4)+O(-8),
    P: P O(-2)+(W'+T6) O(-3)+V O(-4)+W' O(-5),
    V: V O(-2)+(W'+T6) O(-3)+2V O(-4),
    Z: (W'+2T6) O(-3)+V O(-4).                         (2)

This is an imported actual necessary theorem with its transitive assumptions retained, not a claim that every type occurs. The forward length l=1 does NOT force Z. All four types are retained in every image-block test. Their original proof is included in full; its historical classification is not rerun.

The ordered saturated plateau is

    F0 < F1 < F2 < F3=E < F4,
    ranks 5,9,13,17,21.                               (3)

Write Li=Fi/F(i-1), rank Li=4. At each interior stage the derivative kernel is the preceding stage, and its saturated forward transform is the next. The actual derivative gives regular generically invertible maps

    Li -> L(i+1)(-2),  i=1,2,3.                       (4)

These are sheaf maps across ramified parameters, by the original kernel and saturation construction. Endpoint derivative ranks are less than four, not assumed one or equal.

Every Fi with i<4 has no nonzero constant subbundle, and every Fi with i>0 spans H. The dual reversed plateau Di=F(4-i)^perp has the same properties. Universal section persistence, including the endpoint step dF0 contained in F1 tensor Omega, gives

    H0(Fi(d))=H0(Di(d))=0 whenever i+d<4.              (5)

Indeed a section saturates to O(-e), 1<=e<=d, inside the constant ambient. Its degree-e polynomial vector reaches its constant coefficient span after at most e derivatives, by the triangular derivative identity in characteristic zero. Differentiation and saturation preserve inclusion in the actual stages, so that span would lie in an interior stage. This is a proof for arbitrary sections, not an actual jet evaluation or a horizontal splitting.

In particular F0 and D0 have all ordinary degrees at most -4, and H0(D0(3))=0. The derivative kernel of Q*=D1 is exactly D0. Thus the composite psi in Section 1 is injective on its T6 space of global sections, so it is nonzero.

## 3. General endpoint and defect ledger, with positive defects retained

Put a=deg F0, b=deg F4=deg D0, and ci=deg Li. Equation (5) gives

    a<=-20,  b<=-36.                                  (6)

The determinant maps in (4) have invariant effective zero divisors with degrees delta_i, and

    c(i+1)=ci+8+delta_i,   delta_i in S=<12,20,30>.     (7)

The semigroup follows from projective A5 orbit sizes 12,20,30,60. Central evenness and perfectness make a,b,ci even. Eliminating c1 from the prefix degree -54 and the total degree gives

    a+3b=-168+delta1+2delta2+3delta3.                  (8)

Writing a=-20-2u, b=-36-2v yields the finite exact equation

    2u+6v+delta1+2delta2+3delta3=40,  u,v>=0,           (9)
    c1=(-78-a-2delta1-delta2)/3 in 2Z.

The complete derived ledger has 31 rows, seven unramified and 24 with positive defects. The twelve possible defect triples are

    (0,0,0), (0,0,12), (0,12,0), (0,20,0),
    (12,0,0), (12,12,0), (20,0,0), (24,0,0),
    (30,0,0), (32,0,0), (36,0,0), (40,0,0).

LEDGER.json records a,b,all ci and all defects for every row. Its scope is exactly (6)-(9), not all actual equivariant geometry. For the independent scan, (9) bounds a in [-60,-20] and b in [-48,-36]. Equation (7), c4=b+54<=18, and (9) bound c1 in [-46,-6] and c2 in [-38,2]; c3 is then fixed by the actual central prefix. Thus both finite scans have proved bounds. The certificate independently derives the ledger by this even-degree scan and by solving (9). In particular, nothing in the remainder assumes that these general defects vanish.

## 4. The full-rank cubic image has only four possible shapes

Let J=im psi, an actual locally free image on the smooth curve. It is globally generated as a quotient of T6 O, center-odd, and embeds as a sheaf in E*(1). By (2), E*(1) has maximum ordinary degree nine. Every equivariant irreducible block R O(e) of J therefore satisfies

    0<=e<=9, dim R<=4, parity R=e+1 mod 2;
    T6 occurs in R Sym^e W;
    Hom_G(R O(e), E*(1)) is nonzero for at least one type in (2). (10)

The second condition follows by projecting the surjection T6 O->J onto each summand; the third follows because its inclusion in E*(1) is nonzero on that summand. These are necessary conditions only. Testing them in the forced interval yields exactly

    P O(1), V O(1), S4 O(2), W' O(2),
    P O(3), V O(3), W' O(4), P O(5), V O(5),
    S4 O(6), W' O(6), A O(7), W O(8), O(9).          (11)

The only rank-one block in (11) is O(9), and its target Hom is nonzero only for the necessary source D. This proves the rank-one corollary. Each rank-four multiset of these blocks is considered. No actual map is chosen by this test.

Suppose now rank J=4. Let Jbar be its saturation in E*(1) and put dbar=deg Jbar. The negative-transpose identity, obtained by differentiating E perpendicular to Q*, identifies the generic full derivative image with (E/F2)*(1). Saturation in E*(1) therefore gives

    Jbar=(E/F2)*(1),  B:=E/F2=Jbar*(1),
    deg B=4-dbar,  deg F2=dbar-58.                     (12)

Dualizing J subset Jbar gives B subset J*(1). The two backward derivative maps are

    F2(3) -> B(1),      kernel F1(3),
    F1(3) -> L2(1),     kernel F0(3),

and (4) embeds L2 into B(-2). Since H0(F0(3))=0, left exactness gives

    h0(F2(3)) <= h0(B(1))+h0(B(-1))
              <= h0(J*(2))+h0(J*).                  (13)

Riemann--Roch on the rank-thirteen F2 gives h0(F2(3))>=dbar-6. Hence

    deg J-6 <= dbar-6 <= h0(J*(2))+h0(J*).             (14)

Among all rank-four multisets in (11), (14) leaves only

| J | deg J | upper bound for dbar |
|---|---:|---:|
| P O(1) | 4 | 14 |
| S4 O(2) | 8 | 10 |
| V O(1)+O(9) | 12 | 12 |
| 2W' O(2) | 8 | 10 |

In all four cases 0<=dbar-deg J<12. The saturation defect is an invariant effective divisor, so its degree belongs to S and is zero. Thus J=Jbar in every full-rank candidate. This conclusion concerns the cubic image saturation only; it does not yet kill any plateau defect.

Every candidate has H0(B(-1))=0. The second map above therefore also gives H0(F1(3))=0, and

    H0(F2(3)) embeds in H0(B(1)).                    (15)

## 5. Three candidates are impossible without endpoint enumeration

### 5.1. J=S4 O(2)

Here B=S4 O(-1). Exact Euler additivity and (1) give

    chi(F2(3))=W'+T6-W-S4,
    H0(B(1))=S4.

The positive W' and T6 Euler coefficients force those irreducibles into H0(F2(3)), contrary to (15). Nonnegative H1 can only increase those coefficients.

### 5.2. J=2W' O(2)

The space Hom_G(T6 O,W' O(2)) has dimension one, since W' Sym2 W=T6. Therefore every map to 2W' O(2) has the form (alpha f,beta f) for one fixed intertwiner f. Its image factors through one diagonal W' O(2), of rank two. Such a map cannot be the surjection T6 O->J onto a rank-four image. No matrix or generic-rank experiment is used.

### 5.3. J=V O(1)+O(9)

Now B=V O+O(-8). Exact Euler additivity gives

    chi(F2(3))=T6,   H0(B(1))=T6.

Equation (15) and positivity of H1 force H0(F2(3))=T6 and H1(F2(3))=0. Ordinary splitting then makes every summand of F2 have degree at least -4. But its derivative must have generic rank four in

    F2 -> B(-2)=V O(-2)+O(-10).

Every map from F2 to O(-10) is zero by degree. The derivative consequently factors through the rank-three first summand, contradicting its rank four. This is a universal Hom vanishing, not an actual derivative-rank computation.

## 6. The P O(1) case alone forces unramified plateau maps

The remaining full-rank candidate has B=P O, so c3=0. From (7),

    c2=-8-delta2,
    c1=-16-delta1-delta2,
    a=-30+delta1+2delta2.

The bound a<=-20 implies delta1+2delta2<=10. Since every nonzero defect is at least 12, delta1=delta2=0. Then c4=8+delta3 and b=-46+delta3; b<=-36 similarly gives delta3=0. Thus, only under this candidate assumption,

    a=-30, b=-46, (c1,c2,c3,c4)=(-16,-8,0,8),
    L1=P O(-4), L2=P O(-2), L3=P O, L4=P O(2).      (16)

These isomorphisms are induced by the graded derivative maps. They do not split the filtered inclusion or its connection.

## 7. Two forced endpoints have no derivative

By (5), every ordinary degree of F0 is at most -4. Its rank is five and degree is -30. Thus every degree also is at least -14, because the other four ordinary line summands have degree at most -4. Equivariant splitting therefore lies in the complete finite window

    -14<=e<=-4, parity R=e mod2,
    sum dim R=5, sum e dim R=-30.                    (17)

The window has 46 abstract unordered block multisets. Additivity of the actual filtration (16) gives

    chi(F0(t))=chi(E(t))-chi(P O(t-4))
                          -chi(P O(t-2))-chi(P O(t)).

At twists three and four this is

    chi(F0(3))=-S4-T6,
    chi(F0(4))=V-A-D.                               (18)

Exactly two of the 46 shapes satisfy both character identities:

    F0=V O(-4)+O(-8)+O(-10),
    F0=V O(-4)+W O(-9).                             (19)

The verifier derives (17) both by irreducible-block recursion and independently by ordinary degree partitions and parity-compatible coefficient representations. It checks (18) both through McKay recurrence and exact conjugacy-class characters, and records every candidate rather than importing a prior list.

The endpoint derivative must take values in

    F0 -> L1(-2)=P O(-6).                            (20)

The V O(-4) component vanishes by degree. In the first line of (19), the remaining components vanish because

    Hom_G(1,P Sym2 W)=0,
    Hom_G(1,P Sym4 W)=0.

In the second line they vanish because

    Hom_G(W,P Sym3 W)=0.

Thus beta_F0=0. In characteristic zero a subbundle of a constant bundle with zero second fundamental form is constant: its Grassmannian classifying map has zero differential, hence is constant. This contradicts deg F0=-30 (or its inclusion in E with no constant subbundle). Therefore the last full-rank image candidate is impossible, proving rank psi<=3.

## 8. Reproduction and boundaries

Run python3 verify.py and python3 -O verify.py from any working directory. Both produce RESULT.json exactly. The standard-library verifier authenticates all five complete original inputs; tests actual Euler and ambient characters; derives the positive-defect ledger twice; derives the image-block and rank-four candidate lists; checks every contradiction and both complete endpoint enumerations; and runs negative regression controls. No correctness check uses an assert removed by optimization.

INPUTS.json distinguishes the four original Gauss/cohomology sources at db51525015bb7c5e825833d550d08dedf6f6ea96 from the primary-slope theorem at 504b7eb800407dfc7e6340c98c72cdd553939f54. The latter's transitive primary-module assumptions remain explicit in its retained full text. The equivariant Birkhoff splitting is used for cohomology and ordinary Hom bounds only, never as a horizontal splitting.

The arithmetic certificate does not mechanically prove the original actual geometric premises, saturation theorems or their transitive hypotheses. The theorem is conditional on those retained premises. Neither all 31 numerical rows nor any remaining lower-rank cubic image is asserted realizable, and no complete (3,1) exclusion follows here.
