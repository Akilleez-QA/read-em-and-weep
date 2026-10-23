# The exact negative-pencil algebra forced by the degree-twenty-eight branch

## Result and boundary

Conditionally on the actual G3.11.8ae96830fd21 branch, the entire equivariant fixed-variable negative-pencil endomorphism algebra has one of three types, corresponding to the three residual constant-gauge templates:

    Type I:   C times T(J),
    Type II:  T(J),
    Type III: S(J_X,J_Y),                             (1)

where dim J=2 and dim J_X=dim J_Y=1. The algebra T(J) consists of triples (a,d,b) with multiplication

    (a,d,b)(a',d',b')=(aa',dd',a b'+d' b).

The algebra S(J_X,J_Y) consists of (a,x,y,b_X,b_Y), with multiplication

    (a,x,y,b_X,b_Y)(a',x',y',b'_X,b'_Y)
      =(aa',xx',yy',a b'_X+x' b_X,a b'_Y+y' b_Y).      (2)

Thus Type III has two distinct residual vertices, each with one arrow into the degree-twenty-eight block. It is not the disconnected Type I algebra: their centers have dimensions one and two respectively.

In every case the Jacobson radical has dimension two and square zero. The full algebra dimensions are 5,4,5 and the semisimple quotients are C^3,C^2,C^3, respectively. These assertions classify the whole algebra and its multiplication, not only a dimension lower bound or a subgroup of units.

This is a necessary exact algebra condition for the fixed negative pencils. No actual tensor, coefficient, parameter, point, derivative, matrix or source-instance rank is evaluated. No label is excluded, and no nontrivial endomorphism is asserted to extend to the full HM module.

## 1. Immutable inputs and actual normal form

All paths refer to Akilleez-QA/read-em-and-weep.

1. PR856, commit cee45480686c39a321feaa77d4b669682cc71efe, research/hm/profile11-degree28-constant-separation/PROOF.md: the genuine constant decomposition, the two-dimensional coupling space, surjectivity of constant restriction, and its nonzero P-top and V-tail channels.
2. PR858, commit d3b3134e23d0aa4c4b58fd1457f040856d2d0655, research/hm/profile11-degree28-residual-templates/PROOF.md: the three exhaustive actual residual constant-gauge templates and their complete constant endomorphism algebras.
3. Original actual bundle presentations and common negative pencils: commit db51525015bb7c5e825833d550d08dedf6f6ea96, research/hm/order-four-quadratic-load/ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md, POSITIVE-DOUBLE-HYPERPLANE-GAUSS-GATE.md, and UNIFORM-TWIST-FOUR-FIVE-HYPERPLANE-COHOMOLOGY.md.
4. PR790, commit af0e03d26da5e47d18ae732291aca46f4d448dc5, research/hm/source2-first-constant-block/PROOF.md, Section 6: natural reconstruction recovers both fixed actual pencils simultaneously. The source2-specific normal form is not used.
5. PR791, commit 2cd033a4a5ba549d07330427cd779364cb83c0fb, research/hm/source2-pencil-endomorphism-algebra/PROOF.md, Section 6, gives a full-faithfulness argument under stronger degree hypotheses. Section 5 below proves explicitly the version needed here: Q(-1) globally generated, not Q* of top degree at most -2. This distinction is essential in profile (1,1).

The exact actual normal form from the first input is

    H=C direct-sum Hbar, E=F direct-sum R,
    C=Hbar=A+V+P+D,
    0 -> F -> C O --q--> Z=O(28) -> 0,
    F=(P+2D) O(-2), R=O(-8)+W O(-9).                (3)

Both F and R span their respective constant spaces. The decomposition is obtained by a genuine constant shear and respects the original connection.

The residual has intrinsic X=O(-8), L=R^-=O(-10), and Y=L^+=W O(-9), with R=X direct-sum Y. The actual constant spans are

    Type I:   span X=P,   span Y=A+V+D;
    Type II:  span X=P+D, span Y=A+V+D;
    Type III: span X=P+D, span Y=A+V.                (4)

Hbar has multiplicity one on each irreducible. Its constant endomorphisms preserving R form B=C^2,C,C^2 respectively. In the two split rows the scalar factors act on X's and Y's disjoint constant spans. In Type II the common D connects the scalars, so B=C.

Throughout, maps cover the identity of P(W) and the same negative variable space W is fixed. In particular a base automorphism is not a pencil endomorphism.

## 2. The complete ambient endomorphism shape

Let h be an arbitrary equivariant constant endomorphism of H preserving E, including possibly singular h. Write its four blocks relative to (3):

    h(c,r)=(a(c)+b(r),c_0(c)+d(r)).

The lower block restricted to F is a bundle map F->R. All such maps vanish by ordinary degrees: every degree of F is -2 and every degree of R is at most -8. Thus c_0 kills F. Since F spans C, c_0=0 as a constant map.

It follows that a preserves F, d preserves R, and b(R) is contained in F. The induced map of C O/F=O(28) is multiplication by a scalar a_0. Hence q a=a_0 q. The coefficient map C->H0(O(28)) is injective, since H0(F)=0. Therefore a=a_0 id_C. Conversely every such triple preserves E precisely when

    d belongs to B=End_G(Hbar;R),
    b belongs to J=ker Theta,
    Theta:Hom_G(Hbar,C)->Hom_G(R,Z),
    Theta(b)=q b|_R.                                 (5)

This exhausts all equivariant constant endomorphisms, not only those preserving an arbitrarily chosen complement. The vanishing of the omitted lower block was proved for every h.

By PR856, the source of Theta has dimension four, its target has dimension two, and Theta is onto. Thus dim J=2. Extending b by zero on C gives h_b(c,r)=(b(r),0), so

    h_b h_b'=0 for every b,b' in J.                  (6)

For arbitrary d in B, b d belongs to J because d preserves R. Composition is consequently

    (a_0,d,b)(a'_0,d',b')
       =(a_0 a'_0,d d',a_0 b'+b d').                 (7)

The precise right B-action on J, not its dimension alone, now decides the three algebra types.

## 3. Determine every radical arrow and its action

The restriction Theta splits over the actual direct sum R=X+Y. Both Hom_G(X,Z) and Hom_G(Y,Z) are one-dimensional. Its P channel is nonzero on X, and its V channel is nonzero on Y. The P channel is zero on Y because Y is the actual first polar of a degree-ten line and Sym10 W has no P. The V channel is zero on X because Sym8 W has no V. These are actual restriction statements from PR856, not generic rank guesses.

### Type I

Here Hbar=P direct-sum (A+V+D). The top X lies in P and the tail Y lies in A+V+D. Thus the P scalar channel is the only one which can restrict to X, and its restriction is nonzero. Every b in J must have zero P component.

The remaining three channels A,V,D restrict to the one-dimensional tail Hom space, and that restriction is onto by its nonzero V channel. Hence their kernel is exactly two-dimensional. It follows that J vanishes on the P constant summand and is supported entirely on A+V+D.

If d has scalars x on P and y on A+V+D, then b d=y b. Equation (7) therefore becomes

    (a_0,x,y,b)(a'_0,x',y',b')
       =(a_0 a'_0,xx',yy',a_0 b'+y' b).              (8)

The x factor is isolated. This is C times T(J), with both radical arrows from the Y vertex to the F vertex. No arrow from X to F survives.

### Type II

The residual algebra B is scalar, because both span X and span Y contain D and together span Hbar. Therefore b d=d b for scalar d, and (7) is exactly the displayed multiplication of T(J). There are two parallel radical arrows from the single residual vertex to F.

### Type III

Now Hbar=(P+D) direct-sum (A+V). The first summand supports X and the second supports Y. The two channels P,D restrict only to the top Hom space, and their restriction is onto by the P channel. Their kernel J_X has dimension one. Independently, A,V restrict only to the tail Hom space, and their restriction is onto by the V channel. Their kernel J_Y has dimension one. Thus

    J=J_X direct-sum J_Y.

If d acts by x on P+D and y on A+V, then b_X d=x b_X and b_Y d=y b_Y. Substituting in (7) gives exactly (2). Both one-dimensional radical spaces consist of actual nonzero constant maps when their element is nonzero. Since R spans Hbar, such a map cannot vanish on all of R. Thus neither arrow has been introduced only as a formal character possibility.

These calculations are valid for arbitrary scalars, including zero. They classify all noninvertible endomorphisms as well as the automorphism groups.

## 4. Radical, center, and orientation

In each case J is a two-sided square-zero ideal, and the quotient by J is the displayed product of copies of C. A nilpotent ideal in a finite-dimensional algebra lies in the Jacobson radical; the semisimple quotient gives the reverse inclusion. Thus J is exactly the Jacobson radical.

The center of T(J) is C: commuting with the two vertex idempotents forces the radical component of a central element to vanish, and commuting with nonzero J then equates its two diagonal scalars. Type I consequently has center C^2.

For Type III, commuting with the three vertex idempotents again kills any radical component of a central element. Commutation with J_X forces a_0=x and with J_Y forces a_0=y. Its center is therefore C. Type I and Type III are not isomorphic despite both having dimension five and semisimple quotient C^3.

The arrows in (2) go from X and Y into F: this follows directly from the actual constant maps b:Hbar->C and from rightmost-first composition in (7). This proof works with E subset H O, not with its annihilator inclusion. The fixed-pencil identification below is covariant, so there is no opposite-algebra reversal. In particular no claim that the connected three-vertex algebra is isomorphic to its opposite is needed or made.

## 5. Full faithfulness allowing degree-one quotient summands

We prove the precise general reconstruction statement needed here. Let

    0 -> E -> H O -> Q -> 0                           (9)

be an equivariant exact sequence on P1 satisfying H0(E)=0 and such that Q(-1) is globally generated. The latter implies that every degree of Q is at least one, so H1(Q(-2))=0. Define

    N2=H0(Q(-2)), N3=H0(Q(-1)), N4=H1(E),
    A_t(s)=t s, B_t(u)=boundary(t u).                 (10)

Then the functor from constant maps preserving (9) to fixed-variable pencil morphisms is fully faithful.

Indeed the natural evaluation sequence is

    0 -> N2 O(-1) -> N3 O -> Q(-1) -> 0.             (11)

For a summand O(d) of Q with d>=1, this is the complete degree-(d-1) evaluation sequence; d=1 simply contributes a zero kernel. The canonical first map is multiplication by the linear form vanishing at the parameter, with the determinant convention fixed. Thus (11) is natural and remains valid in the degree-one case.

Choose arbitrary independent basis symbols u,v of the fixed two-space. The Koszul sequence of Q and H1(Q(-2))=0 give

    H0(Q)=coker[(A_v,-A_u):N2->N3+N3].

The boundary H0(Q)->H1(E) is onto and has kernel H, by H0(E)=0 and H1(H O)=0. Therefore, with compatible fixed signs,

    H=ker(B_u,B_v)/im(A_v,-A_u).                     (12)

Given a triple (e2,e3,e4) intertwining both pencils, it induces a constant map h:H->H' on (12). Its first intertwining relation gives a morphism of (11), hence a quotient map q_0:Q->Q' with H0(q_0(-1))=e3. A cycle (x,y) in (12) represents the Q-section u x+v y. Both maps of that section are u e3(x)+v e3(y), so

    q_0 composed with H O->Q
      = H' O->Q' composed with h.

Hence h(E) is contained in E' everywhere, not merely generically. The induced N2 map equals e2 because multiplication by any nonzero formal linear form on global sections is injective. The induced N4 map equals e4 by surjectivity of the boundary and the second pencil relation. Conversely the construction on natural cohomology from a constant h gives this same triple. Uniqueness follows either from (12) or from global generation in (11). Addition and composition are preserved. This proves full faithfulness under the stated weaker hypotheses.

In the actual setting, H0(E)=0 is established and Q=D_lin(1), where D_lin is a quotient of M3 O by the actual first multiplication presentation. Thus Q(-1)=D_lin is globally generated. All hypotheses hold without assuming H0(Q*(1))=0. Such a vanishing is not available in profile (1,1); indeed the Type III residual has a complete degree-eight line quotient whose dual contains degree-minus-one summands.

Finally PR790 Section 6, as used already in PR856, identifies (10) simultaneously with the fixed original actual tensors. Thus full faithfulness identifies the algebra computed in Sections 2–4 covariantly with their entire fixed-variable equivariant pencil commutant. This proves (1).

## Contribution and limits

The degree-twenty-eight separation forces not only a proper projector but a two-dimensional square-zero radical. The three residual templates determine its exact right action and separate two distinct five-dimensional possibilities. The weakened full-faithfulness lemma resolves the degree-one quotient dependency instead of importing a source2-only slope hypothesis.

No full-module lifting premise follows. PR818, commit f4a73af666900ad2cb34a756d24b88e19dd6feaa, already distinguishes that different extension problem; no scalar-rigidity argument for the full module is used to exclude these pencil algebras. The statement remains a conditional necessary algebra constraint, not a computation of the fixed actual commutant, a label exclusion, or a proof of the global rank goal.
