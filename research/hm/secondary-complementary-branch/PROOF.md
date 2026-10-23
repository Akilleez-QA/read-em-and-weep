# A rank-two residual obstruction in the complementary secondary branch

Work over C with the actual normalized HM adjoint and G=SL2(F5). On T=P(W*) retain A=Sym2 W, D=Sym4 W, S=Sym3 W, T6=Sym5 W, V=Sym2 W', and P=W tensor W'. All line-bundle linearizations are retained.

## 1. Immutable inputs and conditional statement

The exact originals in Akilleez-QA/read-em-and-weep are pinned by bytes and hashes in INPUTS.json:

- FIBER: PR1004, 0b9a8505e71951cf54950f54458c96cae0520146, research/hm/secondary-fiber-completion/PROOF.md. We use its unconditional constructions of the P-to-V and P-to-P channels and its six-channel actual presentation, NOT its conclusion conditional on two nonzero D channels.
- DROW: PR991, 1ac03caea0564db40acabf8d8d5a0a39984216a2, research/hm/secondary-d-row/PROOF.md. We retain its invariant twelve-form, Euler/Veronese channel, and the globally established actual balanced K=T6 O(-1) plus A O(-2), NOT its separate coefficient hypothesis.
- FORCEDW: PR971, f96962f2219e096821c3dec50712cc0108abea8f, research/hm/forced-secondary-w-extension/PROOF.md. The actual preimage of W O(-1) in K is D O(-4).

The actual reduced secondary boundary retains all quartic corrections and has source Q=P O(2) plus W O(-1), target (V+P+D) O(4), and row coefficients (a_J,b_J), J=V,P,D, in the unique nonzero P-source and W-source channels. The A target is identically zero. Here assume the COMPLEMENTARY branch

    a_D=0,       a_V a_P nonzero.                       (1)

None of these actual coefficient conditions is selected by this proof.

We construct an actual quotient diagram reducing the remaining obstruction to

    h: W O(-1) -> O(10) plus W' O(5) plus D O(4).       (2)

Its three one-dimensional channels have actual residual coefficients x,y,z. The pair (x,y) is an invertible linear recombination of (b_V,b_P) for the retained nonzero a_V,a_P; z=b_D after consistent normalization. No values of x,y,z are chosen. The canonical residual channel geometry gives the complete table:

    y!=0, (x,z)!=(0,0): residual rank2 everywhere;
    y!=0, x=z=0:       residual rank2 off Omega, rank1 on Omega;
    y=0, xz!=0:        residual rank2 off Omega, rank1 on Omega;
    y=z=0, x!=0:       residual rank1 everywhere, kernel O(-12);
    x=y=0, z!=0:       residual rank1 everywhere, kernel O(-2);
    x=y=z=0:           residual rank0, kernel W O(-1).

Here Omega is the reduced twelve-point orbit. In the two jumping cases the generic-rank determinantal ideal is exactly the reduced ideal of Omega, and cokernel torsion has length12, one simple length at each point. In all other cases the cokernel is torsion-free. The full reduced and original secondary maps have fiber rank FOUR MORE than the residual rank; their cokernels have the same torsion. The table concerns actual maps under (1), not arbitrary assigned matrices.

## 2. Injecting and eliminating the actual P source

FIBER constructs the unique channels

    0 -> O(-4) -> P O(2) --i_V--> V O(4) -> 0,
    ker i_P=W' O(1),        im i_P=W' O(3).

The restriction of i_P to ker i_V is nonzero. Otherwise the inclusion O(-4)->P O(2) would factor through W' O(1); but its equivariant Hom space is Hom_G(W',Sym5 W)=0. A nonzero O(-4)->P O(4) has no zeros: its coefficient forms have degree8, while a nonempty G-invariant common-zero divisor must have degree at least12. Thus the joint P-source map

    P O(2) --(a_V i_V,a_P i_P)--> (V+P) O(4)           (3)

is everywhere injective. Its quotient Y is canonically the cokernel of the restriction ker i_V -> P O(4), via the actual quotient diagram using the surjection a_V i_V. No choice of a splitting of i_V is made.

The space Hom_G(O(-4),P O(4)) has dimension1, since Sym8 W=P+D. Thus the restriction is the nonzero channel dual to evaluation of the P-isotypic subspace P8 of Sym8 W. It remains to identify that evaluation kernel exactly, rather than infer Y from its rank and degree.

## 3. The P8 evaluation kernel and the canonical quotient

The P8 linear system has no basepoints, since its degree8 is smaller than every projective G orbit. Write

    0 -> M -> P O -> O(8) -> 0.                        (4)

The kernel H0(M(1)) of multiplication P8 tensor W -> Sym9 W contains W', because P tensor W=W'+T6 while Sym9 W=S+T6. It cannot also contain T6: a binary relation x f+y g=0 is determined by f in the four-dimensional P8, so the entire kernel has dimension at most4. Consequently H0(M(1))=W'.

Its evaluation map W' O(-1)->P O is the nonzero unique equivariant channel. Under P=W tensor W' it is W' tensored with the Euler inclusion O(-1)->W O; hence it is a fiberwise injection, with quotient W' O(1). Its composite with evaluation belongs to Hom_G(W',Sym9 W)=0, so its image indeed lies in M. Therefore (4) descends to an onto map W' O(1)->O(8). This is the nonzero degree-seven W' evaluation channel, whose kernel is O(-6). Therefore

    0 -> W' O(-1) -> M -> O(-6) -> 0.

The ordinary Ext group H1(W' O(5)) is zero, so the extension splits equivariantly after averaging. Its equivariant splitting is unique because Hom_G(O(-6),W' O(-1))=Hom_G(W',Sym5 W)=0. Dualizing (4) and twisting by4 proves the equivariant quotient identity

    Y = O(10) plus W' O(5).                            (5)

This is the actual quotient of (3). The two equivariant summands are intrinsic: Hom_G(O(10),W' O(5))=0 and Hom_G(W' O(5),O(10))=Hom_G(W',Sym5 W)=0. Named representation identifications remain subject to scalar normalization.

Since a_D=0, eliminating the everywhere-injective P block in the FULL actual target gives (2). The resulting diagram identifies ker b with ker h and coker b with coker h. The first identification is via unique graph lifts into Q, not a claim that ker b lies literally in its W summand.

## 4. No residual channel is silently discarded

Apply equivariant Hom(W O(-1),-) to (3) and (5). The preceding Hom and following Ext groups for P O(2) vanish:

    Hom_G(W O(-1),P O(2))=Hom_G(W,P tensor Sym3 W)=0,
    Ext1_G(W O(-1),P O(2))=H1(W tensor P O(3))^G=0.

Hence quotienting induces an isomorphism from the two-dimensional space of W-source maps into (V+P) O(4) onto the two-dimensional space of W-source maps into Y. The latter channels each have multiplicity1: W occurs once in Sym11 W, and P=W tensor W' occurs once in Sym6 W=V+P. This proves the invertible recombination assertion for (x,y). The D target is untouched, so its residual coefficient z is the original b_D. The actual quartic correction remains in these unselected residual coefficients.

## 5. Geometry of the three residual channels

Let f12 be the nonzero invariant binary twelve-form whose divisor Omega is reduced, as proved in DROW. Every projective orbit has size at least12, and G is perfect.

The O(10) channel g:W O(-1)->O(10) is the Hamiltonian gradient of f12. The fixed character multiplicity Hom_G(W,Sym11 W)=1 identifies it with the unique nonzero channel. It is everywhere onto: the two first partials of a reduced homogeneous binary form have no common projective zero in characteristic zero. Its kernel line is O(-12), by degrees. This is a universal derivative of the abstract invariant form, not a selected HM/source derivative or jet.

The W' O(5) channel m:W O(-1)->W' O(5) has generic rank2. For otherwise its saturated image is an equivariant line O(d). Nonzero source and target maps give -1<=d<=5; central parity forces d even, so d=0,2,4. W occurs in Sym^(d+1) W only for d=0. That case would require W' in Sym5 W=T6 for the target factor, impossible. Thus det m is a nonzero invariant section of O(12); it is a nonzero multiple of f12. The determinant has twelve simple zeros, so m has rank1 on Omega and rank2 elsewhere, with cokernel length one at each orbit point.

The D channel is j=v epsilon, where epsilon:W O(-1)->O is Euler evaluation and v:O->D O(4) the nowhere-zero quartic Veronese section. It has rank1 everywhere and kernel O(-2).

Finally the combined scalar map (g,epsilon):W O(-1)->O(10) plus O has determinant a nonzero multiple of f12. In an arbitrary abstract binary basis X,Y, take epsilon=(X,Y) and g=(partial_Y f12,-partial_X f12). Their determinant, up to the sign of row order, is 12 f12 by Euler's homogeneous identity. This identity is basis-independent up to a nonzero scalar. It proves nonvanishing and the exact simple divisor, rather than inferring them merely from invariant multiplicity.

## 6. Complete residual fiber table and minor ideals

For the behavior at Omega, use the abstract C10 stabilizer, with O(1) fiber character lambda and zeta=lambda^2. The source W O(-1) has characters0,4 in zeta exponents. The W' O(5) target has characters1,4. Since m has rank1 there, its kernel is exactly character0. Both the scalar O(10) target and the Euler quotient O have character0, so their onto maps g and epsilon have kernel character4. These computations hold equivariantly over the whole orbit and select no actual point.

If y is nonzero, m makes h injective off Omega. If either x or z is also nonzero, that extra channel is nonzero on the character0 kernel of m on Omega, making h rank2 everywhere. If x=z=0, h is just m with zero other rows, giving the stated simple twelve-point rank drop and torsion.

If y=0 and xz is nonzero, the rank of h equals the rank of (g,epsilon), since v is a subbundle inclusion. Its determinant is a nonzero multiple of f12. In local frames a component of v is a unit; therefore the two-by-two minors of h generate exactly the same ideal (f12) as the determinant of (g,epsilon). This proves rank2 off Omega, rank1 on it and simple torsion lengths. The single-channel and zero cases follow directly from Section5, and all have constant rank.

Locally split off the four-column identity block (3) in the original quotient diagram. The matrix of b becomes that identity block plus h after invertible row and column operations. Thus rank(b)=4+rank(h) on every fiber, and coker b=coker h. In the jumping cases its generic-rank six-by-six minor ideal equals the residual two-by-two minor ideal (f12). The original map beta:K->(A+V+P+D) O(4) has three additional locally zero columns after the quotient K->Q and a zero A row; the same rank and minor ideals persist. Local Smith form proves that the torsion lengths stated in Section1 are exact.

## 7. Original kernel sheaves, with graph lifts retained

The always-surviving square bundle is L=A O(-6). The actual quotient diagram gives

    0 -> L -> ker beta -> ker h -> 0.                  (6)

The right map uses the graph-lift identification ker b=ker h; no arbitrary zero P-component is assigned.

In every generic-rank-two residual case, ker h=0 as a sheaf, even when exceptional fiber kernels occur. Thus ker beta=L.

If only x is nonzero, ker h=O(-12). The equivariant extension in (6) splits because the ordinary group H1(A O(6)) is zero. Its equivariant splitting is unique because Hom_G(O(-12),A O(-6))=Hom_G(A,Sym6 W)=0. Consequently

    ker beta = A O(-6) plus O(-12).

If only z is nonzero, ker h=O(-2). The equivariant Ext group in (6) has dimension1. It is not the zero class: a splitting would give an equivariant O(-2)->K, whereas the actual balanced K gives H0(K(2))^G=(T6 tensor W+A)^G=0. The standard cubic evaluation sequence realizes the nonzero class with middle bundle S O(-5). Hence ker beta=S O(-5).

If x=y=z=0, the invertible recombination in Section4 gives b_V=b_P=0, and z=b_D=0. Thus the W source itself maps to zero before elimination; its lift is not a nontrivial graph. The original kernel is its actual preimage in K, namely D O(-4) by FORCEDW.

All these are kernel SHEAVES. At a simple rank-drop point the fiber kernel has one extra dimension contributed by the torsion term, so sheaf injectivity must not be read as fiber injectivity.

## 8. Contribution and limitations

This result constructs a smaller actual obstruction in the previously untreated branch (1), with a canonical rank-eight quotient target and only a rank-two source. It identifies all three universal channels, proves the residual coefficient transformation is invertible, determines every conditional rank/torsion alternative and the original kernel sheaves, and retains the actual graph lifts. It does not assert that branch (1) occurs or select any actual residual scalar.

No top sigma, vertex delta, remaining C type, source/catalogue pair or global odd-quadric conclusion is selected. No actual HM/source coefficient, point, parameter, jet, matrix or instance rank has been evaluated. Universal binary forms, abstract stabilizer characters, and ordinary exact bundle arguments are the only computations used.
