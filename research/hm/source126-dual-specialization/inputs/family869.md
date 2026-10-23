# A nonempty universal family of balanced unramified degree-twenty-eight blocks

## Result and boundary

Let G be the binary icosahedral group, W its defining two-space, and C=A+V+P+D. There is a nonempty Zariski-open set

    Omega subset P1 times P2, dim Omega=3,              (1)

parametrizing, up to equivariant constant gauge over the identity of P(W), precisely the quotient systems

    0 -> (P+2D) O(-2) -> C O -> O(28) -> 0.           (2)

The open conditions are the nonvanishing of three universal forms of bidegrees (1,0), (0,1), and (1,1). Every system (2) is unramified as a quotient curve: the actual derivative of its kernel is onto O(26).

The proof establishes nonemptiness by linear maps of universal covariant spaces and avoidance of proper hyperplanes. It selects no point of Omega, no actual coefficient, and no actual HM instance.

Combining each member with each of the three public residual templates gives three three-dimensional families of abstract constant inclusions with the formal source and maximal Gauss profile of G3.11.8ae96830fd21. Their reconstructed fixed-variable negative pencils have the required representation characters and uniform injectivity/surjectivity. This does not assert that any member is the fixed actual HM pencil or extends to the full actual module. The actual realization problem remains open, and no frontier label is excluded.

## 1. Immutable inputs and conventions

All cited paths are in Akilleez-QA/read-em-and-weep.

- PR856, commit cee45480686c39a321feaa77d4b669682cc71efe, research/hm/profile11-degree28-constant-separation/PROOF.md: every actual inclusion in the remaining label has the constant degree-twenty-eight block (2), separated by a genuine constant shear; it supplies the relevant actual coefficient and pencil conventions.
- PR858, commit d3b3134e23d0aa4c4b58fd1457f040856d2d0655, research/hm/profile11-degree28-residual-templates/PROOF.md: exactly three residual constant-gauge classes R=O(-8)+W O(-9) in Hbar=A+V+P+D, all with saturated Gauss quotient 2 O(-8), intrinsic first-polar tail, and full constant span.
- PR862, commit e103e25456897a1123f9636eb20080e8641ce66a, research/hm/profile11-degree28-pencil-algebra/PROOF.md, Section 5: reconstruction is fully faithful when H0(E)=0 and Q(-1) is globally generated, including degree-one quotient summands.
- Original actual representations and maximal-plateau convention: commit db51525015bb7c5e825833d550d08dedf6f6ea96, research/hm/order-four-quadratic-load/ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md and POSITIVE-DOUBLE-HYPERPLANE-GAUSS-GATE.md. These identify the formal target data, not a member of the constructed family.

Work over C and keep the parameter line P(W) and all variables fixed. Write A=Sym2 W, S=Sym3 W, D=Sym4 W, T=Sym5 W, and V,P,Wp for the remaining irreducibles of dimensions 3,4,2. We use invariant alternating forms on W,Wp, the self-dual identifications of all representations, and

    P=W tensor Wp, T=A tensor Wp=V tensor W.

For an irreducible R put M_R(n)=Hom_G(R,Sym^n W). Equivalently, after self-duality, this is the space of R-valued homogeneous degree-n covariants on W. The symbol w below is the formal homogeneous vector, not a selected parameter. Multiplication and contraction with w are universal bundle maps.

The fixed character identities needed are

    Sym24 W=1+A+V+2P+2D,
    Sym26 W=A+2V+2P+2D,
    Sym27 W=Wp+2S+3T,
    Sym28 W=A+V+2P+3D,
    Sym29 W=W+Wp+2S+3T,
    Sym16 W=V+P+2D.                                  (3)

In particular dim M_A(28)=dim M_V(28)=1, dim M_P(28)=2, dim M_D(28)=3; the target multiplicities of W,Wp,S,T in degree29 are 1,1,2,3. The spaces of scalar invariants in degrees24 and26 have dimensions one and zero. Each displayed identity is checked by the short verifier from the nine fixed McKay rules.

## 2. The projective parameter space and multiplication blocks

An injective equivariant coefficient map C->Sym28 W must contain the unique A and V constituents and choose one P copy and one D copy. Up to independent equivariant constant scalings of the four irreducibles of C, it is consequently specified by

    p in P(M_P(28)), d in P(M_D(28)),                 (4)

namely P1 times P2. No value of p or d is chosen. Nonzero representatives of the one-dimensional A and V spaces are only normalizations; rescaling them does not change any open condition below.

Let q_(p,d):C O->O(28) be the coefficient system, not yet assumed onto. Multiplication of sections gives

    mu_(p,d):C tensor W -> Sym29 W.                   (5)

The McKay decompositions

    A W=W+S, V W=T, P W=Wp+T, D W=S+T

split (5) into the following multiplicity-space blocks:

    W:  a_W;
    Wp: p_Wp(p);
    S:  [a_S, d_S(d)] in a two-dimensional space;
    T:  [v_T, p_T(p), d_T(d)] in a three-dimensional space.  (6)

The maps in (6) are the indicated Clebsch projections applied to a covariant tensored with the formal w. Invariant self-duality identifies the resulting coefficient map with the corresponding restriction of multiplication in (5), up to a nonzero normalization on each multiplicity-one Clebsch channel. Such normalizations do not affect invertibility or any vanishing condition. We now prove the needed properties of all these universal maps, rather than infer them from multiplicity counts.

## 3. Universal Euler contractions and injective multiplication channels

### The A channels

Contraction in Sym2 W by the alternating covector associated with w gives an everywhere onto map A O(28)->W O(29), with kernel generated by w^2. Thus

    0 -> O(26) -> A O(28) -> W O(29) -> 0.           (7)

All H1 groups of the left term vanish, and taking G invariants is exact. Since scalar invariants of degree26 vanish, the induced map M_A(28)->M_W(29) is an isomorphism. In particular a_W is nonzero.

The other channel A->S multiplies a quadratic by w. This is injective at every nonzero w, so it sends a nonzero covariant to a nonzero covariant. Hence a_S!=0.

### The D channels

The analogous first contraction Sym4 W->Sym3 W has kernel generated by w^4 and gives

    0 -> O(24) -> D O(28) -> S O(29) -> 0.           (8)

The left term has H1=0. Taking invariants proves that d_S:M_D(28)->M_S(29) is onto, with one-dimensional kernel. This is an exact rank-three to rank-two statement about covariant spaces, not a source-instance rank.

The D->T channel is multiplication by w from Sym4 W to Sym5 W. It is fiberwise injective away from the origin of the homogeneous cone, so d_T is injective on covariants. Its domain and target multiplicity spaces both have dimension three; therefore d_T is an isomorphism.

### The P channels

Using P=W tensor Wp, contraction of its W factor with w is the Wp channel. The tensor-Wp Euler sequence gives

    0 -> Wp O(27) -> P O(28) -> Wp O(29) -> 0.       (9)

Its invariant global-section sequence is exact. Both Wp multiplicities in degrees27 and29 are one, so p_Wp:M_P(28)->M_Wp(29) is onto with one-dimensional kernel.

The P->T channel instead multiplies the W factor by w into Sym2 W and tensors with Wp. Since multiplication W->Sym2 W is fiberwise injective, p_T:M_P(28)->M_T(29) is injective. Its image is therefore a two-dimensional plane.

### The V channel

The equivariant identification V tensor W=T sends a nonzero V-valued covariant tensored with w to a nonzero T-valued covariant. Thus v_T!=0. No scalar value of this covariant is needed.

## 4. The balanced locus is a nonempty open set

Choose volume forms only to express determinants on the fixed multiplicity spaces. By (6), mu_(p,d) is an isomorphism exactly when

    p_Wp(p) != 0,
    det(a_S,d_S(d)) != 0,
    det(v_T,p_T(p),d_T(d)) != 0.                    (10)

These are well-defined projective nonvanishing conditions, independent of all harmless Clebsch and volume normalizations. They have bidegrees (1,0),(0,1),(1,1) on P1 times P2.

For nonemptiness, the first condition removes one point from P(M_P(28)). Since p_T is injective with two-dimensional image and v_T is a fixed nonzero vector, the condition that p_T(p) be proportional to v_T removes at most one additional projective point. Thus there is a nonempty open set of p for which p_Wp(p)!=0 and v_T,p_T(p) are independent.

For every such p, surjectivity of d_S and a_S!=0 make d_S^(-1)(C a_S) a proper hyperplane in the three-dimensional D multiplicity space. The isomorphism d_T makes d_T^(-1)(span(v_T,p_T(p))) a proper hyperplane as well. Their union cannot exhaust a vector space over C. Its projective complement is nonempty, and precisely supplies d satisfying the remaining conditions.

This proves that the locus Omega cut out by (10) is a nonempty Zariski-open subset of P1 times P2. It is irreducible and has dimension three. The proof does not exhibit, select, or evaluate a point of Omega; it is a universal open-set existence argument.

## 5. Balanced splitting and complete constant-gauge classification

For (p,d) in Omega, the coefficient system q_(p,d) has no base point. If all its coefficient sections vanished at any point, all sections in the image of (5) would vanish there as well. But (5) is onto the complete degree-twenty-nine system, which is basepoint-free. Thus q is onto as a bundle map and has locally free kernel F of rank14 and degree-28.

Twisting its kernel sequence by one, (5) being an isomorphism gives

    H0(F(1))=H1(F(1))=0.

A line bundle on P1 is acyclic exactly in degree -1; splitting therefore forces every degree of F(1) to equal -1. Hence F=U O(-2) for a representation U. The equivariant Euler character of the original sequence gives

    U=Sym28 W-C=P+2D,

proving (2). Conversely every quotient (2) has acyclic F(1), so its multiplication map (5) is an isomorphism and its parameter lies in Omega.

Every such coefficient map is injective on global constants because H0(F)=0. Thus it has nonzero A,V,P,D components and is covered by (4). Two systems define equivalent constant inclusions over the identity of P(W) exactly when their coefficient subspaces in H0(O(28)) agree: the induced isomorphism of O(28) is a scalar, while an ambient constant gauge changes only the basis in C. Those subspaces agree exactly when their projective P and D choices agree. Therefore Omega is the full constant-gauge parameter space, not only a family mapping onto part of it.

## 6. Every balanced member has unramified derivative

The new balancing conclusion does not alone permit one to ignore derivative torsion. We check it explicitly.

Regard F in (2) as the hyperplane kernel of the quotient curve C O->O(28). This curve is nonconstant because it has fifteen independent coefficient sections. Thus its second fundamental form has generic rank one and F^+=C O after saturation. Let B be the raw sheaf generated by F and its first derivatives. Write the actual derivative image as O(26-Delta), where Delta is its invariant effective zero divisor and delta=deg Delta. Then

    0 -> F -> B -> O(28-Delta) -> 0,
    rank B=15, deg B=-delta.                          (11)

Since F=(P+2D)O(-2), its universal quadratic first polar is an onto map onto B from (P+2D) tensor W tensor O(-1). Hence B(1) is globally generated. It is also a subsheaf of a constant bundle, so every splitting degree of B is 0 or -1. Equation (11) consequently gives 0<=delta<=15. The only possible nonempty invariant divisor in that range is the reduced twelve-point orbit D12. Thus delta=0 or12.

The V component of q is nonzero and unique in degree28. Since V occurs once in degree16, it is

    q_V=f12 v16,

where f12 is the invariant equation of D12 and v16 is a nonzero V-valued degree-sixteen covariant. Its common divisor is empty: the only possible positive invariant divisor of degree at most16 has degree12, and division by it would give a V constituent in Sym4 W=D, impossible.

At every arbitrary point of D12, q_V vanishes and its first derivative has nonzero V component, because f12 has a simple zero and v16 is nowhere zero. The full value q is nonzero by basepoint-freeness and has zero V component at that point. Its derivative therefore cannot be a scalar multiple of its value. The projective quotient curve is unramified there.

This rules out Delta=D12. Therefore delta=0 and the actual derivative is onto

    F -> (C O/F)(-2)=O(26).                           (12)

No parameter or orbit representative was selected; this argument holds simultaneously for the whole family and every point of the invariant orbit.

## 7. Abstract formal Gauss branches and their pencil boundary

For any member of Omega, take the direct sum of its constant inclusion (2) with any of the three universal residual templates of PR858:

    E=F direct-sum R subset H O=(C direct-sum Hbar) O.

Both summands are saturated and span their constant spaces. The source splitting is

    E=(P+2D)O(-2)+O(-8)+W O(-9),
    H=2A+2V+2P+2D.

By (12) and the exact residual derivative, its actual saturated Gauss quotient is

    A_q=O(26)+2 O(-8).

The dual second fundamental form is the negative transpose. Since the quotient is saturated, its exact quotient is therefore

    B_q=A_q*(-2)=O(-28)+2 O(6),

with no determinant defect.

The backward endpoint has generic Gauss rank two. Indeed E^-=F^- direct-sum L, where the hyperplane kernel F^- has generic derivative rank one because the fifteen-section quotient has independent second jets generically in characteristic zero, while the nonconstant degree-ten line L has derivative rank one in the other constant summand.

The forward endpoint E^+=C O direct-sum R^+ likewise has generic derivative rank two. In the two disjoint residual rows, the next osculations of X and Y are independent in their constant summands. In the shared-D row, the P projection of the second osculation of the degree-eight line is generically injective: the four-dimensional P system has independent second jets generically. The third osculation of the complete degree-ten line has zero P component, so these next increments remain generically independent. Both individual increments are nonzero. Hence the rank-three plateau of E has maximal profile (1,1), not a longer profile inferred from bundle counts.

For completeness, reconstruction gives uniform commuting negative pencils with the prescribed formal representation characters. The quotient Q is globally generated and, because E spans H, has no degree-zero summand. Thus Q(-1) is globally generated. Its natural evaluation sequence gives the first pencil

    A_t:H0(Q(-2))->H0(Q(-1)),

which is injective for every nonzero formal linear form t. The second pencil B_t is multiplication by t followed by the boundary H0(Q)->H1(E). It is onto: modulo t H0(Q(-1)), sections of Q identify with the fiber at the zero of t, and the constant H surjects onto that fiber. Thus H0(Q)=H+t H0(Q(-1)), which proves surjectivity of B_t. Commutativity follows from multiplication of linear forms and the same boundary.

Their characters, obtained from these exact sequences, are

    N2=A+2V+3P+4D,
    N3=3Wp+3S+6T,
    N4=2V+4P+3D,

and dimensions (41,54,37). The short verifier checks these Euler identities. PR862's full-faithfulness applies, so constant-gauge inequivalence remains fixed-variable pencil inequivalence.

Conversely PR856 and PR858 put every actual inclusion in the remaining label into exactly one block parameter in Omega and one of the three residual types. Intrinsicness of the maximal-slope F and its constant span F^+=C prevents an ambient isomorphism from changing that block parameter; the intrinsic residual dimensions distinguish the three rows. Thus the abstract normal-form class consists of three copies of Omega.

This is an abstract compatibility and normal-form statement. In particular it supplies no proof that any one of these reconstructed pencils is the fixed actual HM tensor pair. The extra full-module relations or other actual-HM structure are not constructed, evaluated, or claimed to hold for a generic member. A contradiction to the actual branch needs an additional structural constraint beyond the constant inclusions, saturated Gauss maps, representation characters and negative-pencil identities proved here.

## Verification boundary

The verifier checks only the displayed universal symmetric powers, invariant and Clebsch multiplicities, and the reconstructed character identities using the nine McKay rules. The nonempty-open argument, Euler exact sequences, saturation, ramification and intrinsicness are written proofs. No selected actual or abstract parameter value, source coefficients, point, derivative value, matrix, rank experiment, scan, old all-twist envelope, or large computation is used.
