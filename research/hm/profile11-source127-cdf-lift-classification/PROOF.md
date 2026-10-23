# All c-d-f off-diagonal lifts are removable by constant shears

## Result and precise equivalence

Assume the canonical constant-tower theorem for the original source127 c-d-f inclusion, with source tuple (0,0,1,1,0,1,0,0). Then every such saturated full-span inclusion is equivalent, over the fixed base P1 and by a G-equivariant constant ambient isomorphism, to exactly one member of the balanced one-parameter abstract family Omega of PR876.

This strengthens the necessary tower normal form to an exhaustion theorem for the displayed abstract constant-bundle inclusions. It does not identify which parameter, if any, occurs in actual HM data, select or evaluate a parameter, or assert that the ambient isomorphism extends to the rest of the actual HM module. The actual-HM realization question remains open. No source or stable label is excluded.

The new step is a universal jet argument: the five-dimensional D coefficient space maps generically onto the third-jet quotient of degree-ten binary forms. This proves the two-dimensional quartic shear map is an isomorphism. The scalar shear is the complete degree-eight coefficient identification.

## 1. Exact dependency interface

The canonical-tower theorem is PR920, commit 1528ff8ea56b21e03f7501a962bdaa6728a75904, at research/hm/profile11-source127-cdf-normal-form/PROOF.md, Git blob 718b5245560a84568492874bab8d8c34730e8319:

https://github.com/Akilleez-QA/read-em-and-weep/blob/1528ff8ea56b21e03f7501a962bdaa6728a75904/research/hm/profile11-source127-cdf-normal-form/PROOF.md

The six-input manifest authenticates it, PR876 and the four original actual/source inputs. Its exact mathematical interface is:

    E=F direct-sum B direct-sum L_- subset H O,
    F=(P+D) O(-2), B=(V+P) O(-4), L_-=O(-8),
    H=2A+2V+2P+2D,
    A_q=O(-8)+O(2)+O(16), original defect zero.

It produces a canonical constant tower A subset C10 subset H, an exact sequence

    0 -> F -> C10 O --q--> O(18) ->0,
    C10=A+V+P,

and an actual constant quotient decomposition

    H/C10 = C11 direct-sum C9,
    C11=Sym10 W=A+V+D,
    C9=Sym8 W=P+D,
    E/F = U_6^10 direct-sum U_0^8.

Here U_k^n=Sym^k W O(k-n) is the universal k-th osculating subbundle of the degree-n Veronese line. The theorem proves the entire kernel/polar flag, all required saturation, and both full coefficient spans. In particular this interface is stronger than a mere rank or splitting-character statement.

The top quotient q is the balanced quotient q_p for some p in the nonempty open set Omega from PR876, commit 7c7f25911ae1df3590c2b4ffe541c21bae9b1574:

https://github.com/Akilleez-QA/read-em-and-weep/blob/7c7f25911ae1df3590c2b4ffe541c21bae9b1574/research/hm/profile11-source127-cdf-open-family/PROOF.md

That proof establishes the converse existence for every p in Omega, including both maximal plateaux of length one. No new claim about existence of actual HM realizations is used or made here.

Choose an equivariant constant splitting of H over H/C10. The source inclusions then take the actual form

    f -> (f,0,0),
    b -> (u(b),i(b),0),
    l -> (v(l),0,j(l)),                         (1)

where i:B=U_6^10->C11 O and j:L_-=U_0^8->C9 O are standard, while u and v are arbitrary regular equivariant bundle maps into C10 O. This proof removes both u and v without evaluating them.

## 2. The scalar lift is a constant shear

Because j is the complete degree-eight Veronese coefficient inclusion, restriction induces an isomorphism

    Hom_G(C9,C10)
       -> Hom_G(O(-8),C10 O),  w -> w j.       (2)

Indeed the second space is the space of equivariant degree-eight C10-valued coefficients, which is exactly Hom_G(Sym8 W,C10) after the fixed self-duality. The coefficient map of j is an isomorphism, not merely a generically spanning map.

Let w9 be the unique constant map with w9 j=v. The constant triangular shear

    (c,x,y) -> (c-w9(y),x,y)

is equivariant, invertible, the identity on C10 and C11, and removes v from (1) without changing u, F or q. This is an existential identification of a vector space map, not a choice or evaluation of an actual parameter.

## 3. The quartic lift class and its constant shear map

Only the composite t=q u matters modulo a source map into F. Define

    T=Hom_G(B,O(18)).

Since B=(V+P)(-4) and Sym22 W=2A+V+P+2D, this space has dimension two, one V and one P channel. Constant shears on C11 provide the linear map

    R:Hom_G(C11,C10) -> T,
    R(w)=q w i.                               (3)

The source has dimension two, corresponding to the common A and V constituents of C11=A+V+D and C10=A+V+P. To prove that (3) is an isomorphism, dimensions alone are not enough. We prove its kernel is zero using the actual universal quotient

    0 -> B=U_6^10 -> C11 O --pi--> S O(7) ->0. (4)

The key assertion is that the restriction pi_D:D O->S O(7) is generically onto.

## 4. A self-contained jet proof of the D-channel assertion

Use the invariant alternating form of W to identify W with its dual. At the formal line ell, the subspace U_6^10 is ell^4 Sym6 W inside Sym10 W. Interpreting ell as the linear equation of the corresponding point of P1, this is precisely the subspace of degree-ten forms vanishing to order at least four there. Thus (4) is the universal quotient of degree-ten forms by their order-at-least-four vanishing subspace: equivalently, evaluation of jets of orders zero through three. Its rank-four target is the standard equivariant principal-parts bundle S O(7). This identification fixes the kernel and the quotient, so no transpose of an unrelated map is being used.

The five-dimensional D is a genuine constant subspace of Sym10 W. Dehomogenizing on an affine chart identifies it with five linearly independent polynomials of degree at most ten. We claim that its jets through order three have generic rank four.

Here is the characteristic-zero polynomial argument. Choose any four-dimensional subspace and then a degree-adapted basis f0,f1,f2,f3 with distinct increasing degrees n0,n1,n2,n3; ordinary elimination with respect to the degree filtration gives such a basis. Let a_i be their nonzero leading coefficients. The formal Wronskian det(d^j f_i/dz^j), with j=0,1,2,3, has leading coefficient

    (product a_i) det((n_i)_j),

where (n)_j is the falling factorial. The polynomials (n)_j are monic of degree j, so this determinant is the Vandermonde product of the distinct n_i, up to its fixed sign. It is nonzero in characteristic zero. Hence this Wronskian is not the zero polynomial and the four jets are independent over the function field. This is a universal existence argument, with no chosen source coefficients, point, derivative values, matrix or instance-rank evaluation.

It follows that pi_D is generically onto. Consequently, for any bundle map gamma:S O(7)->O(18),

    gamma pi_D=0 implies gamma=0.              (5)

Indeed a morphism of bundles vanishing over the function field is zero. No claim that pi_D is everywhere onto or saturated is needed for (5).

## 5. The quartic shear is an isomorphism, and the lift is removed

Suppose R(w)=0. Exactness of (4) says that q w factors uniquely through a regular bundle map gamma:S O(7)->O(18). Because w is a constant equivariant map C11->C10 and C10 contains no D, w kills the D summand. Therefore gamma pi_D=0. By (5), gamma=0, so q w=0.

The coefficient map C10->H0(O(18)) of q is injective, because H0(F)=0. Since w is constant, q w=0 therefore forces w=0. Thus R has zero kernel. Both sides of (3) have dimension two, so R is an isomorphism.

For the actual lift t=q u there is a unique constant w11 with R(w11)=t. Apply the constant shear

    (c,x,y) -> (c-w11(x),x,y),

which fixes C10 and C9. The new quartic lift u'=u-w11 i satisfies q u'=0 and hence factors as a regular bundle map B->F, by exactness of the top quotient sequence. Its graph changes no generated subbundle: subtracting that map into F is a triangular automorphism of the source F direct-sum B direct-sum L_-. Thus u' may be removed without changing E as an embedded bundle. Together with Section2 this puts E into the actual constant direct-sum form

    E = F_p direct-sum U_6^10 direct-sum U_0^8
    inside C10 direct-sum Sym10 W direct-sum Sym8 W. (6)

Every step is a regular bundle or constant-space isomorphism. No lift was discarded merely because it vanished generically, and no connection-rank additivity across an unremoved extension was assumed.

## 6. The two exceptional parameter lines are distinct

Let f12 denote any nonzero generator of the one-dimensional invariant degree-twelve space. Only its line is used, not a normalized polynomial or coefficient value. The unique V covariant of degree eighteen spans f12 times the unique V covariant of degree six. Likewise multiplication by f12 embeds the unique P covariant line of degree six in the two-dimensional P covariant space of degree eighteen.

PR876 identifies the T-channel map from P18 with an isomorphism onto its two-dimensional T19 space. Its determinant condition compares this image with the fixed nonzero V18-to-T19 line. At degree six, both the V-to-T and P-to-T channels are nonzero into the unique T covariant line of degree seven. The former follows from V W=T; the latter is the fiberwise injective multiplication channel P=W Wp to T=Sym2 W Wp. After multiplication by f12 their images are the same T19 line. Therefore the determinant-condition kernel is exactly the one-dimensional covariant line represented by f12 times the P6 covariant line.

This line does not lie in the other exceptional kernel. The universal Euler sequence

    0 -> Wp O(5) -> P O(6) -> Wp O(7) ->0

has zero left invariant sections, one-dimensional middle and right invariant sections, and zero left H1. Thus the degree-six P-to-Wp channel is an isomorphism on invariant sections. Multiplication by f12 commutes with this universal channel and preserves a nonzero covariant. Consequently its degree-eighteen counterpart is nonzero on the determinant-exceptional line. The two excluded lines are distinct.

Hence Omega is the projective parameter line with exactly two distinct points deleted, rather than only an open complement of at most two points. This identifies canonical exceptional covariant lines structurally; no actual-source parameter or point is selected or evaluated.

## 7. Exhaustion, uniqueness and the remaining realization question

The canonical-tower theorem places p in Omega. Equation (6) proves every inclusion under consideration is equivalent to the PR876 member E_p. Conversely every p in Omega gives such an abstract inclusion by that immutable construction. Hence this is an exhaustion, not only a list of compatible examples.

For uniqueness, any G-equivariant constant ambient isomorphism over the fixed base carrying one inclusion to another carries the canonical A and C10 tower to the corresponding tower and induces an isomorphism of the high line quotient. On C10=A+V+P its restriction acts by an independent nonzero scalar on each irreducible constituent. The high line isomorphism is also a scalar. These changes preserve the projective P covariant line in Hom_G(P,Sym18 W). Thus the two parameters p are equal. This statement is over the fixed G-action on P1; no additional quotient by base reparametrizations is asserted.

The original one-parameter abstract family therefore completely describes these equivariant constant-bundle inclusions up to the stated equivalence. It does not describe an extension of that equivalence to the other actual HM maps, and does not prove that any p is attained by the fixed actual HM source. That is the exact remaining compatibility question. No moduli-scheme isomorphism or algebraic family-level trivialization is asserted. The theorem changes no source count and excludes no stable label.
