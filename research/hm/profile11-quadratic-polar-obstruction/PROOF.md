# A quadratic polar obstruction excludes a zero-defect profile-(1,1) label

## Result and scope

The formal rank-three Gauss label

    G3.11.003c6b04f1cc,
    A_q=2 O(-8)+O(14),
    B_q=O(-16)+2 O(6),
    original determinant defect=0,

is impossible. The complete necessary source list has three entries, E0,E10,E18. A profile-free quadratic Gauss-gap lemma excludes E0 and E10. For E18, the same lemma excludes the zero internal-derivative channel. The remaining channel forces a canonical constant three-space V inside the first osculation of the top quadratic block; its quotient then contains a linear subbundle whose derivative forces a further constant space inside a section-free bundle. This is the contradiction.

This argument does not assume H0(E^+)=0. In profile (1,1), E^+ is an endpoint and may contain constant sections. The constant V that appears below is retained rather than discarded.

The result removes one of the 19 retained profile-(1,1) labels. It does not exclude the other 18 labels or the distinct source2 profile-(2,1) label. It does not establish the original global rank goal. No selected actual HM/source coefficients, parameters, points, derivative values, matrices, source-instance ranks, model experiments, or large computation are used.

## 1. Exact immutable dependencies

The original source, quotient, and label data are at commit

    db51525015bb7c5e825833d550d08dedf6f6ea96

of Akilleez-QA/read-em-and-weep, under

https://github.com/Akilleez-QA/read-em-and-weep/blob/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load/

The exact files used are:

1. ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md: the actual saturated E in the constant thirty-space H O, its source catalog, H0(E(1))=0, and rank/degree data.
2. NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md: H0(E^-(2))=0.
3. ONE-ONE-ENDPOINT-DEGREE-WINDOWS-AND-159-NECESSARY-PAIRS.md and one-one-endpoint-necessary-pairs.json: actual quotients A_q=E/E^- and B_q=Q*/(Q*)^-, the injection A_q into B_q^*(-2), and the complete necessary source overlist for each one-one pair.
4. rank-three-quotient-frontier-144.json: stable label G3.11.003c6b04f1cc has source_index49 and the A_q,B_q,defect displayed above.

The source_index49 entry of the pinned one-one JSON has exactly the three source tuples

    (0,0,0,0,0,2,0,1),
    (0,0,0,0,0,1,1,0),
    (1,0,1,0,0,2,0,0).

In the established E-catalog these are, respectively,

    E0  = (P+2D) O(-2)+2 O(-8)+O(-10),
    E10 = (P+2D) O(-2)+O(-8)+W O(-9),
    E18 = 2D O(-2)+Wp O(-3)+V O(-4)+2 O(-8).           (1)

Two already-published structural lemmas are used from PR796, commit

    d2b43060c83328dd5118aee6b9288fcfa0c873ac,

at

https://github.com/Akilleez-QA/read-em-and-weep/blob/d2b43060c83328dd5118aee6b9288fcfa0c873ac/research/hm/profile12-quadratic-block-exclusion/PROOF.md

They are Section3's saturated derivative-image lemma and Section8's profile-free quadratic Gauss-gap lemma. Section5's exact E18 top-block kernel is also reused; its derivation is summarized below. None of these three statements assumes that E^+ is an interior stage. The profile-(1,2) positive-Euler contradictions from that publication are not imported.

For frontier context only, PR798 at commit 2bbf244bafc380cf5b0ce1114f86fcd8053e4e55 proves the separate exclusion of the remaining profile-(1,2) labels:

https://github.com/Akilleez-QA/read-em-and-weep/blob/2bbf244bafc380cf5b0ce1114f86fcd8053e4e55/research/hm/profile12-backward-plateau-exclusion/PROOF.md

The new profile-(1,1) exclusion does not depend on that result.

Work over C. Let G be the binary icosahedral group, W its defining two-space, Wp the other two-space, A=Sym2 W, S=Sym3 W, D=Sym4 W, T=Sym5 W, and V,P the remaining even three- and four-dimensional irreducibles. All irreducibles are self-dual.

## 2. The top quotient is onto and the relevant derivative images are saturated

Let F=R O(-2) be the canonical top block of one of (1). Here R=P+2D or R=2D. The actual quotient E->A_q restricts to a map

    p:F -> O(14),

since all maps to O(-8) vanish by degrees. The strict-top vanishing H0(E^-(2))=0 shows that its degree-sixteen section system is injective on R. Its dimension is therefore fourteen or ten.

A common zero divisor would be G-invariant and nonempty, hence have degree at least twelve. It would leave at most h0(O(4))=5 independent sections, impossible. Thus p is onto everywhere. Write K0=ker p. Then

    0 -> K0(2) -> R O -> O(16) -> 0.                    (2)

The original determinant defect is zero. Since B_q is a genuine locally free quotient of Q*, the identification A_q=B_q^*(-2) makes A_q, and hence O(14), saturated in Q(-2), where Q=(H O)/E.

Differentiation of K0 gives the O-linear internal map

    kappa:K0 -> (E/F)(-2).

Let J be its image. If J is saturated, the actual full derivative image I of F in (H O/F)(-2) is saturated and satisfies

    0 -> J -> I -> O(14) -> 0,
    0 -> F -> F^+ -> I(2) -> 0.                         (3)

Indeed the quotient by I is an extension of the locally free quotient of (E/F)(-2) by J and the locally free quotient of Q(-2) by O(14). This is exactly the original constant connection and its established subquotients.

## 3. The profile-free quadratic gap removes all zero-channel cases

For a saturated quadratic bundle F=O(-2)^r in a constant bundle, suppose its derivative has generic rank one and F^+/F=O(b). Then

    b=2r, or b<=r-1.                                    (4)

To recall the proof, the values and first two derivatives of the quadratic columns span their full constant coefficient space, so F^{++} is that constant span. The derivative of F^+ kills F and factors through its line quotient. The constant span consequently has dimension r+1 or r+2. In the first case degree zero gives b=2r. In the second, its quotient by F^+ is O(2r-b), and the nonzero derivative O(b)->O(2r-b-2) gives b<=r-1. This proof is independent of any maximal plateau profile.

For E0 and E10, K0(2) has rank13, degree-16 and only strictly negative degrees, by (2). Every degree of K0 is therefore between -6 and -3. The target (E/F)(-2) has degrees at most -10. Thus kappa=0, and (3) gives F^+/F=O(16), with rank F=14. The forbidden inequality 13<16<28 contradicts (4).

For E18, the exact kernel in (2) is

    K0=S O(-3)+V O(-4)+Wp O(-5).                        (5)

For completeness, H1(K0(2))=V+P and chi(K0(3))=S-Wp. The complete dimension/parity-supported blocks contributing to that H1 budget are V O(-4), P O(-4), Wp O(-5), O(-10), with contributions V,P,P,V+P. The first and last ways to assemble the budget would give the impossible H0 characters S-Wp or S+T-Wp at twist3. The remaining assembly gives exactly (5), including its S O(-3) block.

The target is

    (E/F)(-2)=Wp O(-5)+V O(-6)+2 O(-10).

Only the constant Wp O(-5)->Wp O(-5) component can be nonzero. Schur's lemma makes J either zero or the full saturated Wp O(-5). If J=0, (3) gives r=10,b=16, contradicting (4), since 9<16<20.

We are left with exactly

    F=2D O(-2),    J=Wp O(-5),
    0 -> Wp O(-3) -> X -> O(16) -> 0,
    X=F^+/F,
    rank F^+=13,    deg F^+=-10.                        (6)

The remaining argument excludes this nonzero channel without using H0(E^+)=0.

## 4. First polars force the exact splitting of F^+

We use the following universal fact about an actual quadratic inclusion F=R O(-2) into a constant space. Its coefficient map is

    a:R tensor Sym2 W -> H.

At an arbitrary line l in W, the fiber of F is a(R tensor l^2), and its value-plus-first-derivative span is a(R tensor l W). This is the fiber of the image of the global first-polar map

    R tensor W tensor O(-1) -> H O.                     (7)

These assertions follow directly by differentiating l^2: the two contributions l^2 and 2lm span l W. No point or coefficient is selected. In the present situation the derivative image is already saturated by (3), so (7) surjects onto the actual F^+. Hence F^+(1) is globally generated. Since F^+ is also a subbundle of a constant bundle, all its ordinary degrees lie in {-1,0}.

From (6), using Sym16 W=V+P+2D, Sym17 W=Wp+S+2T, Wp W=P and VW=T,

    chi_G(F^+)   = -2D-P+Sym16 W = V,
    chi_G(F^+(1))= -Wp+Sym17 W = S+2T.                  (8)

A bundle whose degrees lie in {-1,0} has H1=0. Thus its degree-zero multiplicity space is canonically H0(F^+)=V. Write C=H0(F^+), regarded as the corresponding genuine constant three-dimensional subspace of H. Equation (8) then gives

    C O=V O subset F^+,
    F^+/(C O)=(S+T) O(-1).                             (9)

Both are actual embedded objects. The constant evaluation embeds C O in H O; it is the degree-zero part of F^+. Its quotient is locally free. Since F^+ is saturated in H O, the quotient (9) is saturated in the constant quotient (H/C) O. In particular

    H0(F^+/(C O))=0.                                   (10)

No horizontal splitting of F^+ or E is asserted or needed.

## 5. The forced linear image gives the contradiction

Let M be the two-dimensional multiplicity space in F=D tensor M O(-2). Project its actual inclusion to the quotient (9). Since

    S tensor W=A+D,
    T tensor W=V+P+D,

each of the two equivariant Hom spaces

    Hom_G(D O(-2),S O(-1)),
    Hom_G(D O(-2),T O(-1))

is one-dimensional. Fix any nonzero generators phi_S and phi_T. The projection F->(S+T) O(-1) is therefore determined by two linear forms lambda,mu in M*:

    phi_S tensor lambda,   phi_T tensor mu.             (11)

This is a universal description of the entire Hom space, not a selected instance matrix.

The two linear forms must be independent. If they were dependent, the projection would factor through a single copy of D O(-2), and its generic rank would be at most five. Its kernel would have rank at least five. But the kernel of this projection, inside the actual inclusion F subset F^+, lies in C O of rank three, a contradiction.

After a constant change of basis in M, the two channels in (11) separate. The map phi_S is the standard nonzero SL2-equivariant contraction

    Sym4 W O(-2) -> Sym3 W O(-1).

It is onto at every point: contraction by the nonzero covector annihilating l maps Sym4 W onto Sym3 W in characteristic zero. Because this SL2-equivariant map is nonzero and the G-equivariant Hom space is one-dimensional, it generates the whole channel. Therefore the actual projected image of F contains the full subbundle

    S O(-1) subset (S+T) O(-1).                         (12)

Projection by the constant C commutes with the original connection. Every local section of (12) has a local lift in F, so its derivative lies in the projected F^+, namely (S+T) O(-1). Saturation preserves this containment because (9) is saturated in (H/C) O.

But a nonzero pure linear subbundle S O(-1) of a constant bundle reaches its nonzero constant coefficient span after one forward transform: values and first derivatives of its vector-valued linear columns span those constant coefficients. Thus (12) forces a nonzero constant subbundle inside (S+T) O(-1). This contradicts (10).

The nonzero-channel E18 case is impossible. Together with Section3, all three entries in the complete source overlist are excluded. Hence the full label G3.11.003c6b04f1cc is excluded.

## Verification boundary and contribution

The new structural ingredient is first-polar generation, which fixes the actual constant part of F^+, followed by a dimension-forced separation of its two universal degree-one channels. Quotienting by that genuine constant part leaves an embedded section-free bundle in a genuine constant quotient, and the original connection forces a forbidden constant span there.

The argument is compatible with an endpoint E^+ containing constants. It does not import the profile-(1,2) no-section condition. Every quotient connection used is induced by a constant ambient subspace, not assigned to an abstract bundle complement. There is no rerun or repackaging of the exhausted all-twist section envelope and no use of the withdrawn recursive symbolic-division method.

This is a written structural exclusion of one full profile-(1,1) label. It leaves the other profile-(1,1) labels and source2 untouched.
