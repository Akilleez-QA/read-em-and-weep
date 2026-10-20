# The canonical cubic represents a filtered rank-eight extension functor

## Result

Put Q_i=H(-i), 0<=i<=3, for the stable rank-two bundle H on P4. A graded-framed filtered bundle means a rank-eight algebraic vector bundle E with a filtration whose successive graded factors, starting at the bottom, are Q_3,Q_2,Q_1,Q_0, together with specified identifications of those factors. Isomorphisms must preserve the filtration and induce the identity on these identifications.

Label the three adjacent extension classes from bottom to top by u,v,w in V=Ext1(H,H(-1)). Then:

1. The two consecutive rank-six partial extensions always exist. Each is unique up to a unique graded-framed filtered isomorphism, and their common rank-four subquotient has a unique compatible identification.
2. A rank-eight completion exists if and only if the canonical ordered cubic f(u,v,w)=m111(u,v,w) in J3=Ext2(H,H(-3)) vanishes.
3. If a completion exists, it is unique up to a unique graded-framed filtered isomorphism.
4. Over arbitrary affine complex bases, this filtered-bundle functor is represented by the closed subscheme of V x V x V cut out by the components of the universal cubic f. There is an actual algebraic universal filtered bundle on this subscheme, constructed below by transition functions.

All assertions are conditional on the previously established pair-product vanishing and Ext1 gap vanishings. The scalar multiplying the symmetry-eligible cubic is neither computed nor shown nonzero.

## 1. Inputs and conventions

Use the ordered standard affine cover of P4, with its alternating Cech differential delta and Alexander-Whitney composition product. Every finite intersection is affine. For r>0, let C_r be the Cech complex of End(H)(-r). Import the established hypotheses

    H1(C_2)=H1(C_3)=0,
    V=H1(C_1),
    V tensor V -> H2(C_2) is zero.

Stability gives H0(C_r)=Hom(H,H(-r))=0 for every r>0: H and H(-r) are stable and the source has strictly larger slope. This last vanishing controls automorphisms, rather than existence.

The canonical ordered cubic convention is

    f(u,v,w)=[a h_bc+h_ab c],
    delta h_ab=ab, delta h_bc=bc,

where a,b,c represent u,v,w. All products in this proof are formal Cech products. This is an ordinary algebraic Cech defining system, not an interpretation of a Thom-Whitney expression under a nonmultiplicative integration map. The established multiplicative comparisons identify its canonical cohomology class with the previously audited f.

## 2. Actual algebraic gluing

On each affine chart U_p an extension of locally free sheaves by locally free sheaves splits, because the quotient is projective as a module. Inductively every filtered bundle with these fixed graded pieces is locally isomorphic, compatibly with its graded framing, to Q=direct_sum_i Q_i. This assertion does not require Q_i to be trivial bundles on U_p.

A change between such splittings is a lower-unitriangular automorphism T_pq=1+t_pq of Q on U_p intersect U_q. Its block t_ij lies in Hom(Q_j,Q_i)=End(H)(-(i-j)) for i>j. The cocycle equation T_pq T_qr=T_pr is, block by block,

    delta t_ij = - sum_(i>k>j) t_ik cup t_kj.             (1)

This is a universal identity for gluing variables, not an evaluated source/model matrix product. Transition functions on oppositely ordered overlaps are defined by inverses; they remain algebraic because the strict triangular part is nilpotent.

Fix closed cochains a,b,c and set

    t32=a, t21=b, t10=c.

Their consecutive Yoneda products vanish, so choose regular Cech one-cochains h_ab,h_bc with delta h_ab=ab and delta h_bc=bc. Set

    t31=-h_ab, t20=-h_bc.

All cocycle equations except the bottom-left block now hold. That final block is precisely

    delta t30 = a h_bc+h_ab c = M.                     (2)

The right side is closed: delta(a h_bc)=-abc while delta(h_ab c)=abc. Thus (2) has an algebraic solution exactly when f(u,v,w)=0. A solution makes the displayed transition corrections a genuine algebraic cocycle and therefore constructs the required rank-eight vector bundle and filtration. Conversely every such filtered bundle gives these block equations after local splitting, so completion implies the vanishing of the same canonical f.

The bottom three grades Q3,Q2,Q1 glue using t32,t21,t31. The top three grades Q2,Q1,Q0 glue using t21,t10,t20. They share the rank-four extension of Q1 by Q2. Equivalently, all the displayed data before t30 form a cocycle in the quotient of the triangular automorphism group by its central last-block subgroup Hom(Q0,Q3). This quotient cocycle is the precise partial four-grade object to be completed.

## 3. Gauge ambiguities and exact uniqueness statement

A change of local splitting is a zero-cochain g_p in the same lower-unitriangular group. Its effect is

    T'_pq=g_p^(-1) T_pq g_q.

On the first nonzero block diagonal, changing g by a block s changes that diagonal of t by delta s. Hence two sets of adjacent representatives of the same classes can first be matched by first-diagonal gauge transformations.

After the adjacent cochains match, differences of second-diagonal blocks are Cech one-cocycles. The vanishing H1(C_2)=0 makes these differences boundaries, so second-diagonal gauges match them, without changing the adjacent cochains. This proves uniqueness of the partial object and of each rank-six extension. For full completions, once these lower diagonals agree, the difference of their last blocks is a one-cocycle in C_3. Since H1(C_3)=0, a central last-block gauge matches them. Thus there is exactly one isomorphism class of completions, when nonempty.

For an automorphism inducing the identity on all graded pieces, its first potentially nonzero block diagonal is a global section of the relevant Hom(Q_j,Q_i). Such sections vanish by stability. Induction on the three diagonals forces the automorphism to be the identity. Consequently all the isomorphisms above, including the identification of the common rank-four subquotient, are unique. Without these H0 vanishings the statements about unique isomorphisms must be weakened to uniqueness of gauge classes; without the H1 gap vanishings additional torsors and Massey indeterminacy occur.

This gauge argument handles changes of input representatives as well as changes of primitives. For fixed representatives, changing a pair primitive by a closed cochain changes it by an exact cochain, which is exactly the second-diagonal gauge just described. The apparent choice in the final solution is exactly the last-diagonal gauge. Nothing is quotiented by automorphisms of the graded factors themselves: the graded framing is essential to this exact moduli statement.

## 4. Universal family and obstruction ideal, including nonreduced bases

Let P=V x V x V and S=Sym((V direct_sum V direct_sum V)^*). Choose a linear section V -> Z1(C_1). It supplies universal closed cochains a,b,c with coefficients in S, linear in their respective slots. Because every product V tensor V -> H2(C_2) vanishes, its cochain-level image lies in B2(C_2). Choose a complex-linear right inverse to delta:C_2^1 -> B2(C_2). Applying it formally to the universal products gives h_ab and h_bc, bilinear in their two slots. Only finitely many chosen cochains occur, since V is finite-dimensional.

Then M=a h_bc+h_ab c is a universal closed cochain, trilinear of multidegree (1,1,1). Its cohomology class is the universal element

    F in J3 tensor S,

corresponding to f. Choose a linear representative section i:J3 -> Z2(C_3) and a linear right inverse s:B2(C_3) -> C_3^1. Define

    k=s(M-i(F)), so delta k=M-i(F).

This is well-defined, since the argument is a boundary. Define the ideal and affine scheme

    I_f=(ell(F) : ell in J3^*),       Z_f=Spec(S/I_f).

On Z_f the element F vanishes identically, including all nilpotent structure. Hence t30=k together with the preceding blocks supplies transition functions for an actual universal algebraic filtered bundle on P4 x Z_f.

For any complex algebra R, the same affine cover after base change computes the relative extension groups by C_r tensor_C R. Tensoring vector spaces over C is exact; therefore its cohomology is Hq(C_r) tensor_C R. Every R-valued adjacent triple has a completion precisely when its cubic F_R is zero, and the gauge existence/uniqueness proof applies word for word over R. Thus pullback of the displayed universal bundle gives a natural bijection between morphisms Spec R -> Z_f and graded-framed filtered-bundle isomorphism classes with pulledback graded pieces. Automorphisms are trivial over R by the same H0 tensor-base-change argument. In particular, this describes the full affine-base functor, not merely its complex closed points or its reduced vanishing set.

No canonical cochain splitting or equivariant local presentation is asserted. Different choices produce universally uniquely isomorphic graded-framed bundles. The scheme and functor are intrinsic because f is canonical.

## 5. The one-parameter alternative and its limits

Import the audited fact that the N-equivariant cubic satisfying the required permutation relations belongs to a one-dimensional eligible vector space. Choose any nonzero generator Phi of that space. Then f=lambda Phi for one unknown complex scalar lambda. Formally,

    lambda=0  => I_f=0 and Z_f=P;
    lambda!=0 => I_f=I_Phi and Z_f=Z_Phi.

These are conditional alternatives, not a determination of lambda. The ideal is N-stable for the diagonal action and is generated in total degree three, multidegree (1,1,1). No reducedness, radicalness, codimension, smoothness, number of minimal generators, or complete-intersection claim follows here. A nonzero Phi has some nonzero coordinate polynomial: its ordered trilinear polynomial on three independently labeled copies of V determines the trilinear map. Thus the nonzero branch is a proper closed subscheme, without selecting or evaluating a triple.

Combined with the separately audited multiplication argument, the nonzero branch would also imply the full twelve-dimensional retained detector span. This gluing proof does not decide which branch occurs.

## 6. Exactly what commuting diagonal data fail to detect

The established cyclic-zero relation implies 3 f(x,x,x)=0, hence f(x,x,x)=0 in characteristic zero. Polarizing this identity says that the total symmetric part of f vanishes. Consequently a cubic calculation that replaces the three ordered slots by one commuting formal V-valued variable sees zero from this operation, regardless of the unknown scalar.

This does not say that all deformations over commutative rings are blind, or that the full ordinary deformation problem is unobstructed. Our universal base S is itself commutative. The distinction is that a single repeated input symmetrizes the three slots, whereas the filtered rank-eight problem retains three independently labeled adjacent arrows and their composable order. The extension gluing equations retain f(u,v,w) without symmetrizing those slots. Other operations in an ordinary deformation problem are outside the present conclusion.

