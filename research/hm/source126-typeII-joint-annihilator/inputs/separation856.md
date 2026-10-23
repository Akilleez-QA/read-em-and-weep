# The remaining O(26) branch forces a constant degree-twenty-eight block

## Result and scope

For the actual maximal profile-(1,1) label

    G3.11.8ae96830fd21,
    A_q=O(26)+2 O(-8), B_q=O(-28)+2 O(6),

its remaining source E10 forces a genuine equivariant constant decomposition

    (H O,E) = (C O,F) direct-sum (Hbar O,R),             (1)
    C=Hbar=A+V+P+D,
    F=(P+2D) O(-2),  C O/F=O(28),
    R=O(-8)+W O(-9).

Equality (1) is obtained by an actual constant ambient shear, not by declaring an abstract bundle splitting horizontal. It preserves the original constant connection. The residual R is its actual projected inclusion, is saturated, spans Hbar, and has actual saturated Gauss quotient 2 O(-8).

The new assertion is separation of the constant fifteen-space. The previously established existence of that constant space did not by itself separate E. The possible gluing space has dimension two; two different constant representation channels detect both directions.

Consequently the fixed actual negative multiplication pencils have a simultaneous direct summand with characters

    (Sym26 W, Sym27 W, P+2D)
      = (A+2V+2P+2D, Wp+2S+3T, P+2D),                 (2)

and dimensions (27,28,14). This is the pencil system reconstructed from the actual degree-twenty-eight quotient C O -> O(28), not merely three representations of these dimensions.

Neither this label nor source2 is excluded. No residual contradiction is asserted. Existence of the required summand in the fixed actual tensors is not tested.

## 1. Immutable public inputs and conventions

All paths are in Akilleez-QA/read-em-and-weep.

- Original actual presentations, full constant span, and representation conventions: commit db51525015bb7c5e825833d550d08dedf6f6ea96, research/hm/order-four-quadratic-load/ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md, together with POSITIVE-DOUBLE-HYPERPLANE-GAUSS-GATE.md and UNIFORM-TWIST-FOUR-FIVE-HYPERPLANE-COHOMOLOGY.md at that pin.
- PR813, commit 3f99ecf539a3a3da61743df0dff409e54270c865, research/hm/profile11-o26-divisor-reduction/PROOF.md: this label has a basepoint-free top degree-twenty-eight system.
- PR817, commit a0b7cbd7a53c1603f284cf0e1a29fff106d02cb3, research/hm/profile11-o26-basepoint-free-top/PROOF.md, especially Sections 5–7: E10 forces the genuine constant C, the saturated positive quotient, and the actual saturated residual projection below; E0 for this label is excluded.
- PR822, commit b6bcb1fc5ba0ce245bd14ce104afb0a0a4222bbc, research/hm/profile11-o26-e18-polar-exclusion/PROOF.md: the original source list is exactly E0,E10,E18 and E18 is excluded. This input is needed only to identify the result with the remaining full-label branch.
- For the fixed-pencil consequence only, PR790, commit af0e03d26da5e47d18ae732291aca46f4d448dc5, research/hm/source2-first-constant-block/PROOF.md, Section 6: the natural reconstruction from an actual constant inclusion recovers the original two multiplication tensors simultaneously. This general reconstruction identity is used, not that proof's source2-specific splitting conclusion.

Each file is available at https://github.com/Akilleez-QA/read-em-and-weep/blob/COMMIT/PATH with the displayed immutable commit and path.

Work over C. The group G is binary icosahedral, W is its defining symplectic two-space, Wp its other symplectic two-space, A=Sym2 W, S=Sym3 W, D=Sym4 W, T=Sym5 W; V and P have dimensions three and four. We use P=W tensor Wp. All irreducibles are self-dual, and G has no nontrivial one-dimensional characters. On the parameter line P(W), O(-1) is the tautological line. Invariant nonempty effective divisors have orbit degrees 12,20,30,60.

The pinned actual presentations give

    M2=A+2V+3P+4D, M3=3Wp+3S+6T, M4=2V+4P+3D,
    H=M3 W-M2-M4=2A+2V+2P+2D.

The established exact geometric inputs are

    E=F+O(-8)+W O(-9), F=(P+2D) O(-2),
    F^+=C O, C=A+V+P+D,
    0 -> F -> C O --q--> O(28) -> 0,
    E intersect C O=F.                                (3)

The image of C O/F is precisely the saturated O(28) summand of E^+/E. Therefore E+C O is saturated in H O and projection gives a saturated R=E/F in Hbar O, where Hbar=H/C=A+V+P+D. The original E spans H, so R spans Hbar. Projection of the original derivative gives the actual onto Gauss map

    p_R:R -> 2 O(-8),
    R^+/R=2 O(-6).                                    (4)

No saturation is inferred merely from local freeness of an image sheaf; it is supplied here by the saturated quotient in (3).

## 2. Put the residual tail in its actual first-polar position

Write initially R=X direct-sum Y, X=O(-8), Y=W O(-9). The maps from X to 2 O(-8) are a constant column, while the maps from Y factor through the unique equivariant Euler quotient

    e:W O(-9) -> O(-8).

Thus (4) has the form (a,b e), where a,b are constant two-component columns. Surjectivity implies that a,b are independent. Its exact kernel is consequently

    L=R^-=O(-10),                                     (5)

the standard tautological kernel of e inside Y. In particular R/L=2 O(-8).

The internal derivative of L lands in (R/L)(-2)=2 O(-10). It cannot vanish, since a negative nonzero line in a constant bundle cannot be horizontal in characteristic zero. It is therefore a nonzero constant column and saturated. As R is saturated in Hbar O, the full derivative image of L is saturated there. Its actual first transform L^+ has rank two and degree -18.

Euler's identity identifies the raw value-and-first-derivative sheaf of a degree-ten line with the image of its universal first-polar map W O(-9) -> Hbar O. Saturation just established makes this image L^+, so the map, between rank-two bundles of the same degree, is an isomorphism onto L^+.

The projection of this L^+ to the original Y is a scalar endomorphism of W O(-9). It is nonzero: otherwise its rank-two inclusion in R would factor through the rank-one X. Hence L^+ is the graph of a map Y->X. Replacing the abstract complementary tail by this graph leaves X unchanged and gives

    R=X direct-sum Y,  Y=L^+=W O(-9),                 (6)

where Y now denotes the actual degree-ten first-polar bundle. This change of source splitting is not asserted to be horizontal; all subsequent maps use the actual ambient inclusion.

The degree-ten line in Hbar is represented by an equivariant coefficient map Sym10 W->Hbar. Since

    Sym8 W=P+D, Sym10 W=A+V+D,                        (7)

the actual first-polar Y has no P component. Because R spans Hbar, the top X has a nonzero P component and Y has a nonzero V component. The latter is the projected first polar of the unique nonzero V-valued degree-ten covariant.

## 3. The two-dimensional coupling space

Choose any equivariant constant splitting H=C direct-sum Hbar, possible by finite-group semisimplicity. Modulo F, the actual E is the graph of a unique equivariant map

    beta:R -> Z,  Z=C O/F=O(28).                      (8)

The universal identities give

    dim Hom_G(X,Z)=dim (Sym36 W)^G=1,
    dim Hom_G(Y,Z)=dim Hom_G(W,Sym37 W)=1.             (9)

Thus Hom_G(R,Z) has dimension two. Every constant map t:Hbar->C supplies a coupling restriction

    Theta(t)=q t|_R.

The constant space Hom_G(Hbar,C) has dimension four, with one scalar channel for each of A,V,P,D. We prove that its V and P channels already map onto (9).

## 4. The V channel is nonzero on the tail

The nonzero V-valued degree-ten covariant has three independent coefficient sections. Its common base divisor is empty, since its degree is ten and every nonempty invariant divisor has degree at least twelve. Its first polar is generically rank two: a generically constant projective curve would have only a one-dimensional coefficient span, whereas these three sections are independent. This is also the characteristic-zero first-jet criterion.

Let J be the image sheaf of Y in the constant V space, and Js its saturation. Then J is isomorphic as a sheaf to W O(-9), and

    deg J=-18, deg Js=-18+r,

where r>=0 is the length of an invariant torsion quotient. Hence r=0 or r>=12.

On the quotient side q:C O->O(28), the V component is nonzero because C->H0(O(28)) is injective. The V multiplicities in Sym16 W and Sym28 W are each one. Multiplication by the nonzero invariant f12 identifies the unique V-valued degree-twenty-eight covariant as

    q_V=f12 v16.

The covariant v16 is basepoint-free. A common invariant divisor of positive degree can only have degree twelve, but dividing by it would put V into Sym4 W=D, impossible. Thus v16 defines a saturated line O(-16) in the dual constant V space.

If the V-channel composite Y->V O->O(28) vanished, v16 would annihilate Js. Both the v16 line and ann(Js) are saturated lines in V* O, so containment would be equality. The exact dual quotient sequence gives

    deg ann(Js)=deg Js=-18+r.

Equality with O(-16) forces r=2, impossible for an invariant torsion divisor. Therefore the V-channel composite is nonzero on Y. It is zero on X, by the absence of V from Sym8 W.

## 5. The P channel is nonzero on the top

We give the contraction argument with its linearizations explicit. Equip W and Wp with invariant alternating forms and identify P=W tensor Wp with its dual by their tensor product pairing. A P-valued homogeneous polynomial of degree d denotes a G-equivariant morphism O(-d)->P O. Its contraction in the W factor with the tautological homogeneous vector w is a Wp-valued polynomial of degree d+1. This is the ordinary equivariant Euler contraction; w is a formal homogeneous variable, not a selected point.

Let r8 be the nonzero P component of X from Section 2. Contracting r8 with w gives a Wp-valued polynomial of degree nine. It vanishes because Wp does not occur in Sym9 W=S+T. The Euler kernel sequence, tensored with Wp and twisted by eight, therefore gives uniquely

    r8(w)=w tensor a7(w),                             (10)

where a7 is a nonzero Wp-valued degree-seven covariant. Its common zero divisor is empty, because it is invariant of degree at most seven. Thus a7 is a saturated O(-7) line in Wp O.

Let q_P be the P-valued degree-twenty-eight covariant obtained from the P component of q using the fixed invariant self-duality. Contract its W factor with w and write c29 for the resulting Wp-valued degree-twenty-nine covariant.

This contraction is nonzero. Indeed twisting (3) by one gives

    C tensor W --multiplication--> H0(O(29))=Sym29 W

as an isomorphism, because F(1)=(P+2D)O(-1) has both cohomology groups zero. In the decomposition

    A W=W+S, V W=T, P W=Wp+T, D W=S+T,

the unique Wp in C W comes only from P W. The restriction to this summand is therefore nonzero. Using the alternating identification W=W*, evaluation of that restriction is exactly the contraction c29, up to a nonzero scalar. This proves c29!=0 without choosing q's coefficients.

By the tensor product pairing and (10), the scalar P-channel restriction on X is, up to a nonzero sign,

    <r8,q_P> = <a7,c29>_Wp.                          (11)

Suppose it were zero. Since a7 is nowhere zero and Wp has dimension two, c29 would lie everywhere in the line defined by a7. The resulting global factorization is

    c29=a7 h22,

where h22 is a homogeneous scalar polynomial of degree 22. Equivariance of both maps and injectivity of the a7 line force h22 to be invariant. There is no nonzero invariant of degree 22: an invariant divisor of that degree cannot be a sum of orbits of sizes 12,20,30,60. Thus h22=0, contrary to c29!=0. The P-channel composite on X is nonzero.

## 6. Constant separation

The V restriction has zero X component and nonzero Y component. The P restriction has nonzero X component. They are therefore independent in the two-dimensional space (9), proving that Theta is onto.

For the actual beta in (8), choose t in Hom_G(Hbar,C) with Theta(t)=beta. Only existence is used; no value or actual coefficient is selected or computed. The equivariant constant automorphism

    g(c,h)=(c-t(h),h)

fixes C and induces the identity on Hbar. Modulo F it sends the graph of beta to the zero graph. Taking preimages gives

    g(E)=F direct-sum R in C O direct-sum Hbar O.

Because g is constant, it preserves the original connection and all Gauss constructions. This proves (1). In particular the genuine constant separation is stronger than the initial abstract splitting E=F+O(-8)+W O(-9).

## 7. Consequence for the fixed multiplication tensors

For an actual inclusion 0->E->H O->Q->0, define naturally

    N2=H0(Q(-2)), N3=H0(Q(-1)), N4=H1(E),
    A_t(s)=t s, B_t(u)=boundary(t u).

The original actual quotient presentation and its connecting maps identify these simultaneously with the fixed spaces M2,M3,M4 and their original two multiplication pencils. PR790 Section 6 proves this by universal homogeneous-variable identities for those presentations. This is functorial in constant direct sums, so it applies to (1), without transferring any source2-specific geometric conclusion.

For the first summand, Q0=O(28) and E0=F, so its spaces are exactly (2). Under these identifications its first pencil is multiplication Sym26 W->Sym27 W and its second is multiplication into Sym28 W followed by the quotient

    Sym28 W -> Sym28 W/C = H1(F)=P+2D.

Thus the statement includes the actual degree-twenty-eight subsystem C in the second pencil; it does not replace it with an arbitrary quotient of the same character. Equivalently there are simultaneous equivariant idempotents on the original M_i whose image dimensions are (27,28,14) and which intertwine every member of both original pencils.

The complementary characters are

    P+2D, 2Wp+S+3T, 2V+3P+D,

of dimensions (14,26,23). No existence or nonexistence test for these idempotents is made.

## Verification boundary

The accompanying short verifier checks only the displayed universal symmetric-power decompositions, the two Hom dimensions, the Euler multiplication character identity, the ambient character, and the two triples of summand characters. Its input is the nine fixed McKay rules and integer arithmetic. It performs no source enumeration, all-twist envelope, selected-instance calculation, matrix construction, coefficient evaluation, or rank experiment. The saturation, contraction, and constant-connection arguments are proved above and are not delegated to the program.
