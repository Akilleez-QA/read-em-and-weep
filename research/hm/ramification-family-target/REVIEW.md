# Independent review of the ramification-family target

Status: the candidate's weights, ramification matching, homogeneous exponents, line bundles, and target dimension check out. The polynomial-extension argument is valid assuming the established transvection presentation of all global twist-four skew middle operators. This review does not establish surjectivity of their restriction map.

## 1. Matching, reducedness, and a stronger local lemma

Let a C10 generator have eigenweights ±3 on U and ±1 on the negative binary space, with primitive tenth root ζ. At (r+,ell+), the invariant bicubic has weight 12. Its positive tangent coefficient has weight 6 and vanishes; its negative tangent coefficient has weight 10 and is allowed. The equivariant symplectic identification between the negative dual and negative space preserves eigenweights; it does not reverse this matching.

More precisely put x=r−/r+ and y=ell−/ell+. A monomial x^i y^j in the local bicubic is allowed precisely when 12−6i−2j=0 mod 10. For 0≤i,j≤3 this gives exactly

    F(x,y)=A y+B x²+C x y³+D x³ y².

Smoothness at (r+,ell+) forces A≠0. At the other positive eigenline with the SAME negative eigenline, put X=r+/r−. Dividing the homogeneous equation by r−³ell+³ gives

    A X³y+B X+C X²y³+D y².

At (X,y)=(0,0), its sole linear term is B X, so smoothness forces B≠0. Therefore the negative projection has simple ramification at (r+,ell+), with y=−(B/A)x²+O(x³). The analogous matched point for the opposite eigenlines is also simple. The six order-five subgroups supply twelve distinct matched points. A smooth (3,3) curve has genus four, and its degree-three negative projection has ramification degree twelve. These points consequently exhaust its ramification divisor. This derives the reduced twelve-point description without a separate reducedness assumption.

For g², the eigenweights on v=r² and w are respectively 12 and 2, equal modulo ten. Hence C5 acts by a common scalar on their joining line. The central involution fixes v and reverses w.

## 2. Polynomial extension and independence

Write q=i_x Ω_q with Ω_q a constant U-valued three-form, and η∈E_x=U⊗ker(i_x:Λ²→Λ¹). Fix a nonzero ambient volume Ω. Contraction obeys

    i_x ε(Ω_q∧η)=ε((i_x Ω_q)∧η)−ε(Ω_q∧i_xη)=ε(q∧η).

Since ε(Ω_q∧η) is a top form, it equals L_q(η)Ω for a constant ambient linear functional L_q. Thus ε(q∧η)=L_q(η)i_xΩ, so the intrinsic symplectic pairing β(q,η) equals L_q(η). There is no denominator and no x-dependent coefficient in L_q.

Consequently pβ(q,−)+qβ(p,−) extends to an ambient operator linear in x. Cubic multiples extend with homogeneous degree four. Given the established spanning presentation by these cubic transvections, every global operator has such an extension. Averaging over the central involution preserves its intrinsic restriction and makes the extension center-even. The mixed-to-VV block is then odd in negative variables, hence has only negative degrees j=1,3.

Two extensions agreeing on E give the same value on Y∈E. Consequently the projected scalar restriction is independent of the extension. This uses the actual-middle-vector property of Y, not a statement about arbitrary ambient inputs.

## 3. Exponents and frames

Here b_m/a_m is fixed, unlike the quadratic source polynomial a(w). Along v=t v0, w=s w0, choose u=r and z=(t/s)z0. The zero-VV and zero-WW input is

    Y=(t²/s) Cmix0−(b_m/a_m)s Bmix0.

A degree-four mixed-to-VV block with negative degree j contributes t^(4−j)s^j, and λ_sw=s³λ_w. Its C term therefore has exponent t^(6−j)s^(j+2); its B term has exponent t^(4−j)s^(j+4). For j=1,3 these are precisely t⁵s³,t³s⁵,ts⁷. There are no other exponents.

Under r→αr,w→βw, z0→α³β^(−1)z0. Thus Cmix0 scales α⁵β^(−1), Bmix0 scales αβ, and λ scales β³. The three coefficient weights are respectively (11,3),(7,5),(3,7), as claimed.

Crucial clarification: z lies in Sym²W, so z(w) is QUADRATIC evaluation. Thus [(t/s)z0](sw0)=ts z0(w0), and the forcing 2k a(w)²h(v)z(w) has precisely t³s⁵ scaling, with frame weight (7,5). Treating z(w) as linear evaluation would give a spurious missing-factor objection.

## 4. Target representation

The stabilizer in 2A5 of a ramification pair is C10. For the three line bundles O_R(p,q), the stabilizer exponents 3p+q are 16,26,36, all congruent six modulo ten. Their central character is even, and all three induced twelve-dimensional representations are isomorphic, up to the harmless reciprocal convention for section characters.

Since P2 restricts to C5 as six copies of its regular representation and has even central character, Frobenius reciprocity gives multiplicity six for each target coefficient line. Therefore the space of equivariant source-linear coefficient triples has dimension eighteen. This is an ambient target dimension only, not the rank or image of operator restriction. A useful refinement is that the target is three copies of the induced twelve-dimensional module V⊕P⊕D in the fixed labels. Indeed V=Sym²U has C10 weights 6,0,4, whereas A=Sym²W has weights 2,0,8; therefore either reciprocal section-character convention (weight 6 or 4) selects V, not A. The four-dimensional P contains each nontrivial C5 character once, and D contains every C5 character once, so Frobenius reciprocity gives exactly V⊕P⊕D.

## Scope and sources

No actual HM/source instance, selected ramification value, matrix, rank, or large computation was evaluated. No GitHub write was performed.

Source identities checked against commit 8d8b5be4ce62c3055bb53be9e16d29cc63072f04 in Akilleez-QA/read-em-and-weep, files under research/hm/order-four-quadratic-load:
- ACTUAL-RAMIFICATION-DETECTS-A-NONZERO-MIXED-FORM-MIDDLE-VALUE.md
- ACTUAL-RAMIFICATION-FORCES-A-NONTRIVIAL-PRINCIPAL-U-SOURCE-CORRECTION.md

Remaining inherited assumptions are the actual monad sector formulas and their markings, the global cubic-transvection spanning presentation, and the stated restriction of the source representation. Under those assumptions the whole target construction is consistent. Realizing the forced target in the actual global operator image remains an independent dependency.

## 5. Additional verified step: the prescribed middle coefficient is surjective

Assume k≠0. This statement concerns the required coefficient as an ordinary Γ-module map from P2 to a twelve-dimensional section space; it does not assert that global middle operators realize the coefficient triple.

The two positive homogeneous partial derivatives of F have bidegree (2,3). Euler's identity implies their common zero locus lies on F=0, where it is exactly the negative-projection ramification locus. This locus is finite because the projection is a nonconstant morphism of smooth curves in characteristic zero. The preceding simple-ramification calculation identifies twelve reduced zeros, which exhaust the complete-intersection length (2,3)·(2,3)=12. Thus R is their scheme-theoretic complete intersection.

Twisting its Koszul resolution by O(4,4) gives

    0 → O(0,−2) → O(2,1)⊕O(2,1) → I_R(4,4) → 0.

Künneth yields H¹(O(2,1))=0 and H²(O(0,−2))=0. Therefore H¹(I_R(4,4))=0, and the restriction map H0(O(4,4))→H0(R,O_R(4,4)) is onto. Its dimensions are 25→12, with kernel dimension13. The negative H¹ of O(0,−2) does not spoil surjectivity: it instead accounts for the thirteenth ideal section beyond the twelve obtained by directly multiplying the two defining equations.

Binary-quadratic multiplication Sym²A→Sym⁴W* is onto, with its one-dimensional invariant kernel. The positive trace-free quadratic representation D restricts isomorphically to H0(P¹_positive,O(4)). Their product therefore gives P2→H0(O(4,4)) onto, with dimensions30→25 and kernel dimension5.

The marked input z0 transforms by α³β^(−1), and its quadratic evaluation z0(w) transforms by α³β. Hence z0(w) is a section of O_R(3,1). It is nowhere zero by the published ramification source lemma, so multiplication by it is an equivariant isomorphism

    H0(R,O_R(4,4)) → H0(R,O_R(7,5)).

Multiplication by 2k preserves this isomorphism when k≠0. The desired map

    (a⊙a)⊗h ↦ 2k a(w)² h(r²) z0(w)

therefore extends linearly to a surjective Γ-module map P2→H0(R,O_R(7,5)), with ordinary rank12 and kernel dimension18. Pure squares span Sym²A in characteristic zero, so specifying it on a⊙a determines the linear map. In particular its image cannot omit any irreducible constituent of the twelve-dimensional target.

Two different appearances of the number eighteen must remain distinguished: this ordinary source-map kernel has dimension18, whereas the equivariant space of all three coefficient maps also has dimension18. Neither fact proves realizability by global middle operators.

## 6. Kernel lower bounds

For the linear global coefficient restriction from a 1203-dimensional family to the eighteen-dimensional equivariant coefficient target, rank-nullity gives kernel dimension at least 1185. Restricting that map to the stated 1113-dimensional vertex kernel gives kernel dimension at least 1095. These are lower bounds only, independent of any surjectivity claim or actual rank evaluation.
