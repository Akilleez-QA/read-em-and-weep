# The first mixed-root obstruction on the six forced square survivors

## Result

Let R be the positive fixed plane, let W be the negative coordinate two-space, and write B=End_0(F). Fix a nondegenerate negative quadratic q_- and its reduced root divisor Z in P(W*). For a positive quadratic q_+ whose conic is smooth, retain the actual finite odd scaling family

    M_epsilon=(I/I^9) tensor g_epsilon*B tensor O_Q(4),
    Q=(q_++q_-=0),   g_epsilon(x,u,v)=(x,epsilon u,epsilon v).

Take the odd eigensheaf and put t=epsilon^2. The established first and second differentials have ranks 12 and b, respectively, where

    delta_q:30 -> 12,
    Delta_q:H0(Z,K(1)) -> H1(B_R(-1)) tensor H0(O_Z(5)),
    b=rank(beta_lambda1)+rank(beta_lambda2)<=12.

The actual square bundle Y=O(-3) tensor W gives a canonical six-dimensional subspace

    S_q=H0(Z,Sym^2 Y(1))
       =A tensor H0(Z,O_Z(-5))
       subset E3^0=ker(Delta_q).                       (1)

There is a canonical THIRD scaling obstruction on this subspace,

    Theta_(q_+,q_-):S_q
       -> coker[Delta_q:H0(Z,K(1))
                         ->H1(B_R(-1)) tensor H0(O_Z(5))].  (2)

The target has dimension 30-b, and dimension 30-2r when both roots have beta-rank r. For fixed q_-, the operator (2) is linear in the coefficients of q_+. It is the entire obstruction to extending the forced leading section through order t^3, equivalently epsilon^6, after the two preceding obstructions have vanished. It is not merely a necessary projection of that third obstruction.

No rank, nonzero value, or vanishing of (2) is asserted. In particular the six forced root survivors do not imply six, or any, odd sections on a smooth quadric.

## 1. Geometric meaning of the six-space

Let H_i=P(V_+ directsum lambda_i), for the two roots lambda_i of q_-, and let D=H_1 union H_2 be the reducible quadric (q_-=0). Its scheme-theoretic intersection is R. Mayer--Vietoris for the locally free B(4) gives

    0 -> B_D(4) -> B_H1(4) directsum B_H2(4)
      -> B_R(4) -> 0.

The involution acts trivially on B_R(4), hence

    H0(B_D(4))_- = H0(B_H1(4))_- directsum H0(B_H2(4))_-.

On H_lambda, the ideal of R is O_H(-1) tensor lambda*. Taking odd parts of the restriction sequence gives the exact, coordinate-free identification

    H0(B_Hlambda(4))_-
       =H0(B_Hlambda(3))_+ tensor lambda*.            (3)

Every square of the two actual sections of F_Hlambda(2) is an even B_Hlambda(3) section. Thus (1) consists geometrically of two independent triples of such squares, each multiplied by the normal linear form to R in its own hyperplane. Their restrictions to R are zero, so they glue on D without any equality between the two triples. The factor lambda*=O(1)|lambda is essential: the resulting bundle on the direction line is Sym^2 Y(1)=A tensor O(-5), not a trivial rank-three bundle.

There is also an independent plane-restriction check before multiplication by the normal forms. For distinct roots, the annihilator linear forms ell_1 and ell_2 are coprime. A quartic in both Y_lambda1=ell_1^3 W and Y_lambda2=ell_2^3 W would be divisible by ell_1^3 ell_2^3 of degree six, and is therefore zero. Consequently their symmetric-square subspaces have zero intersection in Sym^2 D=H0(B_R(3)): extend bases of the two disjoint two-spaces to see this directly. Thus the six unweighted square restrictions are independent already on the plane. This does not trivialize the evaluation-line factors in (1), nor imply smoothing injectivity.

This describes actual global sections on the reducible quadric. It imposes no smoothing compatibility yet.

## 2. Intrinsic third differential and its ambiguity

Use the cohomological spectral sequence of the t-adic filtration of the actual family. It can equivalently be obtained from successive parameter-truncation exact sequences. There are only section and first-cohomology terms for this proper curve-supported family. At the special fiber,

    h0(M_0)=30,   h1(M_0)=90.

The first image has dimension 12. The second image is canonically the image of Delta_q in the degree-five harmonic target modulo that first image. Consequently

    E3^0=ker(Delta_q) subset ker(delta_q),
    E3^1=(H1(M_0)/im(delta_q))/im(Delta_q),
    dim E3^1=78-b.                                   (4)

The inclusion (1) is the actual inclusion of leading sections; it is independent of a first or second lift. The third differential is defined on E3^0, not on a chosen space of lifted representatives.

More explicitly, after eliminating the special-fiber differential in a two-term cohomology model, write its differential as

    t D1+t^2 D2+t^3 D3+... .

For v0 in E3^0 choose v1 with D1 v1=-D2 v0. The third class is represented by D3 v0+D2 v1 modulo im D1 and the image of the second differential. Replacing v1 by an element of ker D1 adds precisely that second image. This is the relevant indeterminacy, not permission to set a correction equal to zero. The parameter-truncation definition makes the construction independent of this auxiliary model.

## 3. The actual sixth normal term remains

In local projective frames write the actual transition comparison, to the needed order, as

    exp(t ad z_ij+t^2 ad r_ij+t^3 ad h_ij) modulo t^4.

The cochains z, r, h have normal degrees two, four, six. The quadratic cochain represents the nonzero actual zeta. The higher terms satisfy their nonlinear Baker--Campbell--Hausdorff gluing equations. Neither r nor h is discarded on the grounds that a free invariant comparison group vanishes.

For corrections s1,s2 to a leading section s0, the third gluing defect has the following expression in consistent transported frames:

    [h,s0]
    + (1/2)([z,[r,s0]]+[r,[z,s0]])
    + (1/6)[z,[z,[z,s0]]]
    + [r,s1] + (1/2)[z,[z,s1]] + [z,s2].             (5)

Formula (5) displays the actual third differential; its intrinsic definition is Section 2. In particular both earlier corrections and the sixth-order comparison term occur.

## 4. Whole-plane corrections and the degree-seven component

Choose temporarily a harmonic complement for the nondegenerate binary form q_-. Reducing by q_-=-q_+ preserves the odd harmonic degrees. The previous first- and second-obstruction constructions choose corrections on a cover of the whole plane R, with

    s0: degrees 1;
    s1: degrees 1,3;
    s2: degrees 1,3,5.

Their coefficient bundles at degree d are B_R(4-d). The first correction includes the degree-one compensation for the q_- trace; the second includes the compensations needed after the secondary obstruction vanishes. These terms are not optional.

For a section in S_q, the high degree-five secondary component is zero because the root sections are actual global hyperplane squares. The lower degree-three secondary class is canceled by the surjective first differential. Degree-one H1 vanishes. Hence these corrections exist on the whole plane, rather than only on the finite conic neighborhoods.

All terms of (5) therefore have degrees at most seven. Its degree-seven component evaluates at the two roots to the actual normal-degree-six boundary gamma_lambda of the hyperplane B_Hlambda(3) section. The preceding high-degree corrections agree with the unique root lifts: the intervening H0 groups B_R(1), B_R(-1), and B_R(-3) vanish. Since every square extends globally on its hyperplane, both gamma values are zero.

This is zero as a whole-plane cohomology class, not merely zero after an unidentified restriction. Indeed, the degree-seven coefficient is B_R(-3), and its finite target is B_C(-3). The exact sequence

    0 -> B_R(-5) --q_+--> B_R(-3) -> B_C(-3) -> 0

has H1(B_R(-5))=0. Thus H1(B_R(-3)) injects into that finite target. Evaluation of harmonic septics identifies their two-dimensional quotient with H0(O_Z(7)). The high class is exactly the two root gamma classes in this injected space. It vanishes on S_q, and a whole-plane primitive removes it.

## 5. Exact target reduction, including the lower residues

After the degree-seven class is removed, the third class is represented on the whole plane in degrees one, three, and five.

- Degree one has coefficient B_R(3), whose H1 is zero.
- Degree three has coefficient B_R(1). Its entire harmonic cohomology is the twelve-dimensional first image, because delta_q is surjective.
- Degree five has coefficient B_R(-1). Its harmonic cohomology is the thirty-dimensional target of Delta_q.

The latter injects into H1(M_0)/im(delta_q), by the already established restriction injection H1(B_R(-1))->H1(B_R(-1)|2C), using H1(B_R(-5))=0. Changing a quintic representative by q_- times a cubic changes it, on Q, by a degree-three term, hence by the first image. Therefore this injection is canonical even though a harmonic complement was used in its construction.

Modulo the second image, the degree-five target becomes exactly the cokernel in (2). This embeds in E3^1. The third class on S_q lies in that embedded subspace, proving the claimed target reduction.

Conversely, if (2) is zero, change the earlier correction by an appropriate first-kernel section to cancel its second-image component. This is allowed by the exact indeterminacy in Section 2. The remaining degree-three residue is canceled using the surjective first differential, by changing the next correction. Degree-one and degree-seven residual coboundaries have whole-plane primitives. Thus the section extends through t^3. No lower-degree residue is silently omitted, and no injectivity of a later differential is used.

## 6. Linearity in the positive quadratic

The roots, the source S_q, the first differential, the secondary operator Delta_q, and the target of (2) depend on q_- and the actual bundle, but not on q_+.

The q_+ dependence enters through the relation q_-=-q_+. Give a harmonic term of degree 2j+1 in the coefficient of t^k the weight k-j in q_+. Starting from the degree-one leading section, harmonic reduction and the actual normal-degree-two, four, and six transition terms preserve this grading. The defects and corrections can be solved with fixed linear choices of primitives and fixed right inverses for the already proved surjections, independently of q_+.

At third order the possible components therefore have the following q_+ degrees:

    normal degree 7: q_+ degree 0;
    normal degree 5: q_+ degree 1;
    normal degree 3: q_+ degree 2;
    normal degree 1: q_+ degree 3.

The first is the root gamma component, which vanishes on S_q. The last two disappear in the justified quotients of Section 5. Thus the surviving degree-five class is linear in q_+. Changing the solving choices changes this representative by the fixed Delta_q image; hence linearity holds for the canonical operator, not only for a chosen representative.

Equivalently, for fixed nondegenerate q_- there is a genuine linear map

    S_q tensor H0(O_R(2))
       -> coker(Delta_q),                             (6)

whose evaluation at q_+ is (2). This is an actual third-order obstruction pencil. Its rank is not determined here.

## 7. A separate global smoothing interface

The geometric interpretation in Section 1 also supplies an independent global obstruction, without identifying it prematurely with a weighted scaling stage. Consider the flat projective family

    D_s=(q_-+s q_+=0) in P4.

At s=0 its odd sections include S_q. The exact ambient restriction sequence identifies

    H0(B_D(4))_- = ker[q_-:H1(B(2))_- -> H1(B(4))_-],
    H1(B_D(4))_- = coker[q_-:H1(B(2))_- -> H1(B(4))_-].

Here H0(B(2))=H0(B(4))=0, and H2(B(2))=0 is an independently proved ambient input, not an inference from section vanishing. Precisely, [PR167, Section 2, immutable commit 063da90fc4543304e87e701cdefcc08225412f17](https://github.com/Akilleez-QA/read-em-and-weep/blob/063da90fc4543304e87e701cdefcc08225412f17/research/conductor-normalization/sharper-hm-regularity/SHARPEST-BOUND.md) proves H2(B(t))=0 for every t>=2 by tensoring Decker's actual primary section resolution with F dual and checking the controlling diagonal cohomology. At t=2 the relevant groups are 15H2(F(-1)) plus 4H2(F), 35H1(F(-2)) dual, and 20H0(F(-1)) dual, all zero. The trace splitting transfers the result from End(F) to B. Thus the stated cokernel really is H1(B_D(4))_-. The first global smoothing obstruction is therefore the canonical map on this kernel induced by q_+ multiplication, modulo q_- image. Restricting it to S_q is legitimate and again linear in q_+.

This global smoothing differential is not asserted to equal the finite weighted third differential (2). The two models carry different filtrations, and a proof of their exact comparison would have to retain all intervening normal orders. The present result establishes (2) directly and supplies the global interface without making that extra identification.

## Boundary of the conclusion

The new progress is a geometric realization of the six forced survivors and an exact, smaller, q_+-linear next obstruction on them. On a generic-rank root pair its target has dimension 30-2r, at least eighteen. This does not prove that the obstruction is nonzero, injective, or zero. If beta has additional kernel beyond its square subbundle, those extra survivors require their own third-stage analysis. Neither the square theorem nor the present construction proves odd-quadric nonvanishing.

The argument uses the actual transition comparison through sixth normal order, not a split formal neighborhood or a zero quartic/sixth term.

## Dependencies

HYPERPLANE-SQUARE-SURVIVORS.md supplies the actual global hyperplane square sections and the section bundle Y. ODD-FIRST-SCALING-OBSTRUCTION.md supplies the first surjection and finite family. ODD-SECOND-SCALING-OBSTRUCTION.md supplies the canonical secondary operator, its root description, and gamma. The actual plane Steiner vanishing H1(B_R(t))=0 for t>=2, its dual negative consequences, and stable H0 vanishing are the only cohomological elimination inputs.
