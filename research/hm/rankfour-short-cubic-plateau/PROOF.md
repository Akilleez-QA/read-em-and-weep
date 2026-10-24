# The rank-four short cubic plateau is impossible

## 1. The theorem and scope

Retain the actual geometric hypotheses, original physical parameter line, and fixed representation marking in the four complete original sources pinned in `INPUTS.json`. The actual second fundamental form cannot have generic rank four and maximal consecutive rank-four plateau lengths

    (k,l)=(1,3).

This excludes one ordered rank-four stratum. It does not by itself exclude any other rank-four profile, establish rank at least five, prove square-map surjectivity or full-adjoint invertibility, or repair the original theorem. No actual HM coefficients, parameters, jets, matrices or instance ranks are computed. No historical 28-, 37-, or 159-record enumeration is imported or rerun.

The argument first forces precisely two endpoint degree alternatives, with every determinant defect zero. It then uses exact cohomology of the actual source, a new bounded abstract rank-four quotient classification, and the full upper exact sequence. The final contradiction is an equivariant Euler character, not an ordinary dimension count.

## 2. Actual inputs and the hypothetical plateau

Let G=SL2(F5), T=P(W*), with the standard determinant-one linearization of O(1). The named irreducibles and their fixed physical marking are

    1, W, A=Sym2 W, S4=Sym3 W, D=Sym4 W, T6=Sym5 W,
    P, W', V,
    dimensions 1,2,3,4,5,6,4,2,3.

Here V is the other three-space, not A. The center-odd irreducibles are W, S4, T6, W'; all are self-dual. The group is perfect, so every one-dimensional representation is trivial.

The actual geometric objects are

    0 -> E -> H tensor O -> Q -> 0,
    rank E=17, degree E=-54, dim H=30,
    H=2A+2V+2P+2D.

Both E and Q*=E^perp have no nonzero constant subbundle and span their respective constant ambients. The original actual presentations are

    0 -> E  -> M3  O(-1) -> M4  O -> 0,
    0 -> Q* -> M3* O(-1) -> M2* O -> 0,

where

    M2=A+2V+3P+4D,
    M3=3W'+3S4+6T6,
    M4=2V+4P+3D.

In particular the actual cohomology identity is

    H1(E(1))=W'+3T6.                                    (1)

The ambient character above is obtained from the actual Koszul middle cohomology H=W M3-M2-M4. This uses the 30-dimensional plane-section space, not the 54-dimensional coefficient space M3.

Suppose the hypothetical maximal rank-four (1,3) plateau exists. Its actual saturated chain is

    F0 < F1 < F2 < F3 < F4,    F1=E,
    ranks 13,17,21,25,29.                               (2)

Set Li=Fi/F(i-1), for 1<=i<=4. At interior stages i=1,2,3, the derivative kernel is F(i-1) and the saturated forward transform is F(i+1). Thus the actual derivative induces regular, generically invertible maps

    Li -> L(i+1)(-2),    i=1,2,3.                       (3)

Saturation and sheaf-kernel identities extend this construction across exceptional parameters; (3) is not merely an assertion about generic subspaces. The endpoint derivative ranks are less than four and are not assumed equal to each other. None of the rank-two or rank-three endpoint exclusions is imported.

## 3. Persistence, including the endpoints

Every Fi with i<4 has no nonzero constant subbundle. Below E this follows by inclusion; above E a constant subbundle propagates backwards through the interior derivative kernels to E. Dually every Fi with i>0 has full constant span H. Consequently the reversed annihilator stages

    Di=F(4-i)^perp,    0<=i<=4,

have the same interior derivative properties and every Di with i<4 has no nonzero constant subbundle.

For i+d<4, with d>=0, the universal section-persistence argument gives

    H0(Fi(d))=H0(Di(d))=0.                             (4)

To include the endpoint i=0 explicitly, a section saturates to a line O(-s) in F0 with 1<=s<=d. The line is also saturated in the constant ambient: both intervening quotients are locally free. A degree-s polynomial vector reaches its constant coefficient span in at most s derivatives because the derivative-to-coefficient change of generators is triangular with nonzero factorial diagonal. These transforms lie successively in F1,...,Fs. The first containment follows from dF0 contained in F1 tensor Omega, which is a consequence of F0 being the derivative kernel at F1. At s<4 the nonzero constant span would lie in an interior stage, contradiction. The same proof applies to D0. No actual polynomial vector or jet is selected or evaluated.

Taking i=0,d=3 gives

    maxdeg F0<=-4,    D0=F4^perp=O(b), b<=-4.

Write a=degree F0 and b=degree F4=degree D0. Therefore

    a<=-52,    b<=-4.                                  (5)

The i=1,d=2 case gives maxdeg E<=-3. Its degree deficit from seventeen O(-3)'s is three. Center parity forbids a degree-minus-five block: its center-odd coefficient has dimension at least two, costing at least four deficit units. The only possibilities are

    E=R14 O(-3)+R3 O(-4),
    E=R16 O(-3)+O(-6).

The second contributes S4 to H1(E(1)), contradicting (1). In the first, R3 is A, V, or three copies of 1. The equation R14+R3 W=W'+3T6 excludes A and 3*1 because they introduce W or S4. As V W=T6, it forces

    E=U O(-3)+V O(-4),    U=W'+2T6.                    (6)

This small degree-deficit proof does not rely on the historical splitting enumeration. In particular E(4) is globally generated and

    H0(E(3))=U, H1(E(3))=H1(E(4))=0,
    H0(E(4))=UW+V=2D+3P+3V.                           (7)

## 4. Exact endpoint alternatives and zero defects

Put ci=degree Li. The determinants in (3) give

    c(i+1)=ci+8+delta_i,    delta_i>=0.                 (8)

All these effective zero divisors are G-invariant. On the projective parameter line the action factors through A5. A finite point stabilizer is cyclic, and the possible cyclic stabilizer orders in A5 are 1,2,3,5. Thus point orbit sizes are 60,30,20,12. Every nonzero invariant effective divisor has degree at least 12. This is the general invariant-divisor fact from the retained ramification source; its rank-two conclusions are not used.

The center acts trivially on all stages and quotients. Their determinant degrees a,b,ci are even: any linearization of a line bundle differs from the standard one by a character, and G has no nontrivial characters.

Since a+c1=-54 and b=a+c1+c2+c3+c4, direct substitution in (8) gives

    3a+b=-168+3delta1+2delta2+delta3.                   (9)

Write a=-52-2u and b=-4-2v, with u,v>=0. Equation (9) becomes

    6u+2v+3delta1+2delta2+delta3=8.                    (10)

A nonzero delta is at least 12 and already exceeds the entire right side. Hence every delta_i=0, and 3u+v=4. The only alternatives are

    I:   a=-52, b=-12, (c1,c2,c3,c4)=(-2,6,14,22),
    II:  a=-54, b=-6,  (c1,c2,c3,c4)=(0,8,16,24).      (11)

Every map (3) is now an equivariant isomorphism. Setting

    B=L1=E/F0

therefore yields Li=B(2i-2). This identifies graded bundles, not a splitting of the filtered bundle or of the ambient connection.

## 5. Bottom exact cohomology and a forced finite window

In case I the slope bound in (5) and total degree force

    F0=R13 O(-4).

In case II the deficit from thirteen O(-4)'s is two. Ordinary splitting and center parity give precisely

    F0=R11 O(-4)+X O(-5), X=W or W',
    or F0=R12 O(-4)+O(-6),                             (12)

where each R is a genuine even representation of the indicated dimension. Thus H0(F0(3))=0, and

    I:   H1(F0(3))=0,     H1(F0(4))=0;
    II:  H1(F0(3))=W or W', H1(F0(4))=0 or 1.           (13)

The second line deliberately allows both quartic corrections without imposing their finer correlation with the cubic character. This is a necessary overlist, and cannot remove an actual possibility.

The exact sequence 0->F0(3)->E(3)->B(3)->0 and (7) imply

    I:   H0(B(3))=U,
    II:  H0(B(3))=U+W or U+W'.                         (14)

Every representation statement here follows from the actual long exact sequence and semisimplicity, not from a presupposed surjectivity on sections.

As B(4) is a quotient of the globally generated E(4), it too is globally generated. Thus each ordinary degree e of B is at least -4. Its rank is four and its total degree is d=-2 in case I or d=0 in case II. Hence

    -4<=e<=d+12.                                      (15)

The upper bound is forced: the three other ordinary line degrees are at least -4. Equivariant Birkhoff splitting is used only for these cohomology and slope computations. It is never assumed horizontal.

For each irreducible block R O(e) of B, dim R<=4, parity R=e mod2, and the genuine character R Sym^(e+3) W must be a subrepresentation of its target in (14), with zero contribution when e=-4. The complete admissible individual blocks, before rank and degree are imposed, are:

| Degree e | Coefficient R | Cubic contribution |
|---:|---|---|
| -4 | 1,A,P,V | 0 |
| -3 | W' | W' |
| -2 | P | W'+T6 |
| -2 | V | T6 |
| -1 | W' | T6 |
| 2 | 1 | T6 |
| 3 | W | W'+2T6 |
| 4 | 1 | W'+T6 |

For the target U+W only, also allow W O(-3) and O(-2), each contributing W. There are no further blocks in the derived interval (15). This follows from the exact McKay recurrence on the physical graph

    1--W--A--S4--D--T6--P--W', with an extra edge T6--V.

The recurrence is R Sym^(n+1)W=W(R Sym^n W)-R Sym^(n-1)W. The verifier checks every block in (15) against exact conjugacy-class characters over Q(sqrt5), separately from that recurrence. Rank, degree and (14) then leave exactly the following thirteen new possibilities.

## 6. Complete cubic list and quartic elimination

Write R=chi_G(E(4))-chi_G(B(4)). By exactness,

    H0(F0(4))=R+H1(F0(4)).                             (16)

In the tables, 1 means the trivial representation, and coefficients on O denote direct-sum multiplicity.

Case I, degree B=-2 and target U:

| B | R |
|---|---|
| 2O(-4)+O(2)+O(4) | -2*1+D+P+2V |
| 2O(-4)+W O(3) | -2*1+D+P+2V |
| O(-4)+W' O(-1)+O(4) | -1+2P+2V |
| W' O(-3)+2O(2) | 2D+V |
| V O(-2)+O(4) | P+3V |

Here H1(F0(4))=0. The first three rows are impossible because R has a negative trivial multiplicity. The last two rows remain.

Case II, degree B=0:

| B | Cubic excess over U | R |
|---|---|---|
| 2O(-4)+2O(4) | W' | -2*1+P+3V |
| O(-4)+O(-2)+O(2)+O(4) | W | -1-A+D+P+2V |
| O(-4)+O(-2)+W O(3) | W | -1-A+D+P+2V |
| W O(-3)+O(2)+O(4) | W | -1-A+D+P+2V |
| W O(-3)+W O(3) | W | -1-A+D+P+2V |
| W' O(-3)+O(2)+O(4) | W' | D+2V |
| W' O(-3)+W O(3) | W' | D+2V |
| O(-2)+W' O(-1)+O(4) | W | -A+2P+2V |

Adding either allowed correction 0 or 1 to R cannot fix the first row's coefficient -2 at 1, or any coefficient -1 at A. Only the sixth and seventh rows remain. In fact these surviving rows have cubic excess W', so their tail in (12) is W' O(-5) and their quartic correction is zero. This refinement is consistent but unnecessary for the contradiction.

The complete finite list is derived in the proof's forced window, not taken from an earlier source. `verify.py` obtains it twice, once by recursively choosing blocks and once by independent bounded multiplicity products over the individual-block table. It performs no actual map calculation.

## 7. The full upper exact sequence eliminates all four survivors

The rank-one quotient of the upper endpoint is fixed equivariantly:

    0 -> F4 -> H tensor O -> O(-b) -> 0.                (17)

There is no unspecified coefficient character on O(-b), since G is perfect. The three associated graded quotients above E are B(2), B(4), B(6). Additivity in equivariant K-theory, and then in equivariant Euler characteristic, gives

    chi_G(E)+chi_G(B(2))+chi_G(B(4))+chi_G(B(6))
        +Sym^(-b)W-H = 0.                             (18)

No filtered extension is split to obtain this identity. Also, (18) is used at twist zero: it concerns Euler characteristics, not a claimed exact sequence of global sections or a claimed vanishing of H1.

For the four survivors, its left side is:

| Case | B | Left side of (18) |
|---|---|---|
| I, b=-12 | W' O(-3)+2O(2) | 1-A+D-V |
| I, b=-12 | V O(-2)+O(4) | 1+A-P |
| II, b=-6 | W' O(-3)+O(2)+O(4) | V-A |
| II, b=-6 | W' O(-3)+W O(3) | V-A |

Every displayed character is nonzero, since distinct irreducibles form a free basis of the representation ring. Each has ordinary dimension zero, so ordinary rank and degree data alone would have missed the contradiction. This eliminates all four survivors and proves the theorem.

## 8. Reproduction, dependencies, and limitations

Run

    python3 verify.py
    python3 -O verify.py

from any working directory. Their outputs must match `RESULT.json` byte for byte. The program uses only the Python standard library. It authenticates the four complete immutable originals, checks the actual source and ambient characters, derives the endpoint identity symbolically, verifies all thirteen quotient candidates and their exact character contradictions, and runs fail-closed mutation controls. No correctness check uses a Python assertion that optimization can disable.

The four direct sources serve distinct purposes:

1. ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md: actual presentations, cohomology, equivariant splitting, and arbitrary-rank section persistence.
2. RANK-TWO-GAUSS-PLATEAU-NECESSARY-BOUND.md: actual ambient character, generic-rank-independent transform and saturation facts, and determinant parity. Its rank-two conclusion is not used.
3. GAUSS-DETERMINANT-ORBIT-RAMIFICATION.md: projective orbit sizes and the invariant-divisor gap. Its endpoint/rank-two exclusions are not used.
4. POSITIVE-DOUBLE-HYPERPLANE-GAUSS-GATE.md: the actual square/SF identification and original ambient inclusion. No surjectivity conclusion is imported.

The related (3,3) proof informed the endpoint/cohomology technique but is not a logical dependency. No (2,3) conclusion is assumed. Source hashes authenticate retained bytes, not the truth of the transitive actual-geometric hypotheses. The geometric arguments establishing persistence, exactness, saturation and the original presentations are the written mathematical inputs; the arithmetic verifier is not proof-assistant verification of those inputs or of the original theorem.
