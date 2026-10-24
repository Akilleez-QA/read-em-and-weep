# Mixed jets force a nondegenerate constant symmetric identification of the auxiliary curve

## Statement and retained boundary

Retain the complete actual-geometric hypotheses and conclusions of PR1218, and assume its residual simultaneous rank-seven defect with the forced k=2 lower-column flag. Let V=V18 be the actual fifteen-dimensional ambient of the original degree-eighteen scalar curve v. Let u be the auxiliary degree-eighteen scalar curve in V* whose actual fourth jets U4=D(-14) lie in F6, as proved there.

Then the two actual coefficient maps determine a constant G-equivariant nondegenerate symmetric linear map

    h:V -> V*,
    u=h v.                                           (1)

Consequently the auxiliary curve has full coefficient span fifteen. Its actual jets through order nine are the constant images of the already proved original jets:

    U_r=h(T_r)=Sym^r W(r-18), 0<=r<=9.              (2)

Neither the auxiliary full span nor its higher jets are assumed in obtaining (1).

There is also a structural restriction on the actual embedded four-dimensional coefficient kernel. Under the fixed determinant-one apolar identification of E=H0(O(18))* with the physical Sym18 representation, that kernel must be one of at most two fixed embedded P-subspaces selected by the universal sixth transvectant with the degree-twelve invariant. This statement selects no eigenvalue, coefficient kernel, actual parameter, or normalization and asserts no realization.

The symmetric map in (1) is constructed from the actual original and auxiliary maps, not supplied by an arbitrary identification V=V*. The intermediate apolarly identified operator on E is self-adjoint for the fixed apolar form; it need not be represented by a symmetric matrix in arbitrary coordinates.

The result applies only to the residual simultaneous-defect k=2 case. It does not exclude or realize that case, the alternate rank-seven cyclic image, either original local defect, the separate e9 endpoint, or either retained F18 type. No original higher jets beyond order nine, algebraicity, or whole-branch/profile exclusion is claimed. No actual coefficient, parameter, point, jet, tensor, matrix, instance rank, or relative normalization is selected or evaluated. All transvectant and differential identities below are universal symbolic identities.

## 1. Complete immutable inputs and actual mixed-jet containment

INPUTS.json records three complete freshly fetched immutable inputs, with exact commits, paths, Git blobs, UTF8 lengths and SHA256 hashes:

* PR1218 at f5895c822322b4ddab07e51a97874d4528fb5b88, research/hm/rankfour-profile11-triplet-rankseven-equality/PROOF.md.
* PR1216 at 66a6bfe8dd424da58f3d775be1818d1f4f71eff1, research/hm/rankfour-profile11-triplet-nine-jets/PROOF.md.
* PR1212 at ca235151d5d93bbead2beffa7640fbd0741aec43, research/hm/rankfour-profile11-triplet-defect-capacity/PROOF.md.

All transitive actual-geometric hypotheses remain assumptions. Work over C with the physical G=SL2(F5), det W=1 and the retained representations A,V,D,P. To avoid confusion, V without a representation label denotes the actual ambient V18; the other three-dimensional irreducible in the displayed character identities is denoted V_alt.

The original coefficient system is an actual injection V*->H0(O(18)), with quotient the four-dimensional irreducible P. Dually, put

    E=H0(O(18))*,
    q:E ->> V,
    K=ker q, K is an actual embedded copy of P.        (3)

The auxiliary line gives a nonzero actual coefficient map r:E->V*. At this point no surjectivity or full span is assumed for r. Using the universal degree-eighteen Veronese coefficient line nu, the actual scalar maps are

    v=q nu, u=r nu.                                  (4)

All representation-theoretic dualities use the fixed determinant convention, not an arbitrary self-duality of the multiplicity-two P-isotypic part of E.

PR1218 proves that beta_(F6)(U4) is entirely the lower coherent O(-10) of I6=O(-8)+O(-10). The upper normal projection is beta_(B6)|F6, whose exact kernel is B7. Therefore

    U4 subset B7=ann(T7).                            (5)

The original T7 consists of actual globally separated jets through order seven, and U4 of actual globally separated auxiliary jets through order four. Thus their pairing vanishes as an identity of sections along the whole base line. No jet value is selected.

The small fixed character identities used below are

    Sym2 W=A, Sym4 W=D, Sym6 W=V_alt+P,
    Sym8 W=P+D, Sym10 W=A+V_alt+D,
    Sym12 W=1+A+D+P,
    E=Sym18 W=A+V_alt+D+2P.                          (6)

In particular degrees 2,4,6,8,10 have no invariant, degree twelve has a unique invariant up to scalar, and the irreducible dimensions appearing in E are 3,3,5,4,4. Write f12 for a fixed nonzero universal degree-twelve invariant. It represents this fixed one-dimensional invariant space and is not a coefficient chosen from an actual HM instance.

## 2. The rectangle of mixed jets forces diagonal multiplicity twelve

Form the actual invariant biform

    b(x,y)=<v(x),u(y)>,
    b has bidegree (18,18).                          (7)

It is nonzero. Indeed q is onto and r is nonzero, so the bilinear form induced by their pairing cannot be identically zero.

In a formal local coordinate, let p_(a,b) denote restriction to the diagonal of the indicated mixed derivative of a local expression for (7). Equation (5) gives the rectangular identities

    p_(a,b)=0, 0<=a<=7, 0<=b<=4.                   (8)

Differentiation along the diagonal gives

    D p_(a,b)=p_(a+1,b)+p_(a,b+1).                  (9)

We prove that every mixed restriction of total order at most eleven vanishes. Induct on the total order n. The assertion starts with p_(0,0)=0. If all restrictions of order n-1 vanish, (9) gives the adjacent-sum relations among the n+1 restrictions of order n. For every n<=11 there is at least one pair a+b=n with a<=7 and b<=4. Its restriction vanishes by (8); the adjacent-sum relations then force every order-n restriction to vanish.

This is an identity along the entire formal diagonal, not evaluation at an actual point. Changing the local trivialization adds only lower-order derivative terms, already zero. Equivalently the biform lies in the twelfth power of the diagonal ideal. If Omega(x,y) is the fixed determinant form, the global conclusion is

    b=Omega^12 c,  c in H0(O(6,6)).                  (10)

## 3. Exactly two invariant residual biforms, both symmetric

The determinant form is invariant, so c is G-invariant. Clebsch-Gordan gives

    Sym6 W tensor Sym6 W
      =Sym12 W+Sym10 W+Sym8 W+Sym6 W
         +Sym4 W+Sym2 W+Sym0 W.

Using (6), its invariant subspace has dimension two, with the two nonzero universal representatives

    Polar_(6,6)(f12), Omega^6.

The first is the Cartan polarization of the universal invariant. Hence, for scalars a,b0 not both zero,

    b(x,y)=Omega^12
       [a Polar_(6,6)(f12)+b0 Omega^6].             (11)

No values or relative normalization of these scalars are chosen or computed. The Cartan polarization is unchanged by exchange of its two six-fold blocks, and the powers six and twelve of Omega are even. Both terms in (11) are therefore exchange-symmetric. Thus the actual biform (7) is symmetric.

## 4. The precise coefficient operator and its sixth-transvectant form

The bilinear form (7) gives a map H:E->E* with

    H(a)(b)=r(b)(q(a)),
    H=r* q.                                         (12)

Since (7) is symmetric, also

    H=q* r.                                         (13)

In particular H is symmetric and nonzero, and K=ker q is contained in ker H. Let j:E->E* be the fixed symmetric apolar isomorphism in degree eighteen, obtained from det W=1. Define the endomorphism

    B=j^(-1)H.                                      (14)

It is self-adjoint for j. Symmetry is a statement about H; no symmetric-matrix assertion for B in arbitrary coordinates is required.

Under this fixed duality, Omega^18 gives a nonzero scalar multiple of the identity endomorphism. The other term Omega^12 Polar_(6,6)(f12) gives a nonzero scalar multiple of the universal sixth transvectant

    T_f(g)=(f12,g)_6, Sym18 W -> Sym18 W.            (15)

To verify the order, the construction F->Omega^12 Polar_(6,6)(F) is a nonzero SL2-equivariant map from Sym12 W to Sym18 W tensor Sym18 W. Clebsch-Gordan gives exactly one Sym12 summand in that tensor product. After adjunction by the fixed apolar form, the nonzero sixth transvectant is another realization of the same unique map, since 12+18-2*6=18. Thus the two are proportional by a universal nonzero scalar. This argument does not substitute a chosen actual form or matrix.

Consequently there are scalars alpha,beta such that

    B=alpha T_f+beta Id.                             (16)

Here alpha is nonzero. Otherwise the nonzero B would be a scalar identity, contrary to K subset ker B and dim K=4. This conclusion uses no eigenvalue or parameter evaluation.

## 5. A universal order-six differential symbol bounds the kernel

Use the unnormalized homogeneous convention

    (F,G)_6=sum_(k=0)^6 (-1)^k binom(6,k)
      (partial_X^(6-k) partial_Y^k F)
      (partial_X^k partial_Y^(6-k) G).               (17)

Write formally F(X,Y)=X^12 f(t), G(X,Y)=X^18 g(t), t=Y/X. This is an identity over C(t), not specialization at a point. In partial_X^k partial_Y^(6-k)G, the coefficient of the sixth derivative of g after dehomogenization is (-t)^k. Therefore the coefficient of D_t^6 in (17) is

    sum_(k=0)^6 binom(6,k) t^k
       (partial_X^(6-k) partial_Y^k F)(1,t)
       =(12*11*10*9*8*7) f(t).                      (18)

The last identity is the sixth radial derivative of a homogeneous degree-twelve form, with the direction held formally fixed. Because f12 is a nonzero universal form and alpha is nonzero, (16) is a genuine differential operator of order six over C(t). The added scalar identity cannot cancel its highest-order term.

Its solution space in C(t), hence also its polynomial solution space, has dimension at most six over C. Here is an algebraic proof requiring no point choice or initial-data evaluation. In characteristic zero a rational-function Wronskian vanishes exactly when its functions are linearly dependent over the constant field. This criterion follows by induction: after dividing all functions by a nonzero first one, the Wronskian is its corresponding power times the Wronskian of 1 and the ratios; expansion along the first column reduces to the Wronskian of the derivatives of the remaining ratios. A constant dependence among those derivatives integrates to a constant dependence among the original ratios and 1. The converse is immediate.

If seven rational functions solved an order-six equation with nonzero leading coefficient, their sixth derivatives would be linear combinations over C(t) of their lower derivatives. Their seven-by-seven Wronskian would be zero, so they would be linearly dependent over C. Thus

    dim ker B<=6.                                   (19)

This is a universal differential-order argument. It computes no actual coefficient rank or selected matrix.

## 6. The representation gap identifies the exact actual kernel

The kernel of B is G-equivariant and contains the actual K=P from (3). By semisimplicity, a strict enlargement of K inside E would add a nonzero representation in E/K. By (6), its smallest possible irreducible dimension is three. Such an enlargement would have dimension at least seven, contradicting (19). Therefore

    ker B=ker H=K,
    rank H=15.                                      (20)

Now use the actual factorization H=q* r from (13). Since q is onto, q* is injective. Hence ker r=ker H=K. The map r therefore factors uniquely through q:

    r=h q, h:V -> V*.                               (21)

It has rank fifteen by (20), so h is a constant equivariant isomorphism. Moreover H=q* h q. The surjectivity of q and symmetry of H imply symmetry of h. Equations (4) and (21) give u=h v, proving (1).

The auxiliary full span is now a conclusion: r is onto V*. No full-span assertion for a proper auxiliary tail was used at any earlier step. The construction also does not identify V and V* by an independently chosen physical self-duality; h is forced by the actual two coefficient maps.

## 7. Actual auxiliary higher jets and a finite embedded-kernel constraint

A constant linear isomorphism commutes with the intrinsic differential-evaluation maps and preserves saturation. Equation (1) therefore identifies every actual auxiliary saturated jet span with h(T_r). The original jets are proved globally separated through order nine in the complete PR1216 input, so (2) follows. This is a new justified auxiliary conclusion, not an inference from the earlier incomplete source or a new original tenth-jet claim.

There is also a finite structural restriction on K. For every scalar lambda, the universal operator T_f-lambda Id remains of order six, so its eigenspace has dimension at most six by the same proof as (19). On the P-isotypic component E_P=P tensor C^2, equivariance writes T_f as

    Id_P tensor M,

for a fixed endomorphism M of the two-dimensional multiplicity space. It cannot be scalar: that would yield an eight-dimensional eigenspace. A nonscalar complex two-dimensional endomorphism has at most two eigenlines. Since (16) kills the actual embedded K, that subspace is P tensor one of those eigenlines.

Thus K lies in a fixed set of at most two embedded P-subspaces. The set is independent of scaling f12, and no eigenvalue, eigenvector or actual kernel is selected or computed. This necessary finiteness statement does not identify those subspaces with the two retained F18 splitting alternatives and does not prove either is realized.

## 8. Contribution and exact stopping point

The new proof turns a rectangular actual jet containment into a symmetric biform with only two universal invariant components. The order-six differential symbol then bounds its kernel, and the physical representation gap forces exact equality with the actual four-dimensional coefficient kernel. Only after that step does the actual factorization produce the constant nondegenerate symmetric h and full auxiliary span.

The result resolves the previously missing auxiliary-span dependency in this residual case and legitimately transfers original jet separation through order nine to the auxiliary curve. It leaves the remaining internal derivative/incidence problem, both main rank-seven images, the original delta alternatives, e9, realization and algebraicity open.
