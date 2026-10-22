# Complete equivariant source-weighted middle families and vertex restriction

Work over C with the marked binary icosahedral symmetry group Gamma. Write W for its negative two-dimensional representation, U=Wprime for the other two-dimensional representation, A=Sym^2 W, V=Sym^2 U, and D=Sym^4 W. Thus H=V direct-sum W and E=U tensor Omega^2(2) on P(H*). Retain the fixed determinant-valued skew pairing; no monad-channel scalar is normalized here.

## 1. Which source weights are relevant

The actual divided primitive equation is d C_h=a h Z_a-q V_h, not the later multiplied J4 equation. The published canonical lift identifies Z_a=k e_a, where e_a is the natural Hamiltonian deformation cochain, linear in a in A. The positive quadratic source h has representation D (the trace-free part of Sym^2 V). Consequently the bilinear-in-a, linear-in-h source module for C is

    P2=Sym^2 A tensor D=1+A+V+2P+3D, dimension30.

Here P is the even four-dimensional irreducible, distinct from the odd four-dimensional S. Polarization identifies polynomial dependence of degree (2,1) with linear maps out of P2. The trivial summand in P2 is retained: trace-free middle skewness does not impose trace-freeness on the quadratic parameter tensor. This identifies the complete ambient middle ansatz with Hom_Gamma(P2,H0(sp(E)(4))). It does not identify every element of that ansatz with a primitive. If V_h and primitive choices are to be made homogeneously, one chooses a linear splitting on the finite-dimensional image of the relevant global cochain map and averages. More explicitly, the polarized right-hand sides lie in the image whenever all pure a-squares do, because pure squares span Sym^2 A; a linear right inverse on that image and Reynolds averaging then give the same degree (2,1). This preserves any already-established exact primitive identity but does not prove a missing identity or a prescribed source membership.

The center of Gamma acts by + on V and - on W, and by - on U. Its action on End(E) is independent of this scalar on U. The determinant factors det U and det H are trivial Gamma characters; det(+I_V,-I_W)=+1. Thus a Gamma-equivariant map from the center-even P2 is automatically center-even, and the opposite sector admits no such family. The signs below may equivalently be computed using the natural coordinate involution iota=diag(+I_V,-I_W) with scalar + on U, since that scalar cancels in every middle-endomorphism term.

The relation to the physical marking is deliberately narrower: the pinned lower-cohomology Serre-involution note defines phi by negative-block scaling mu with mu^2=-1 and proves that phi squared agrees with physical inversion on induced adjoint classes on the cone, up to scalar conjugation. It does not thereby identify every chosen monad-gauge lift with every other lift. Our complete-family theorem is formulated for Gamma-equivariant middle operators in the natural marked Koszul model. No additional Serre-phi eigenspace constraint or equality of arbitrary gauge actions is imposed.

## 2. A canonical presentation, not a parameter count alone

Set G_i=U tensor Lambda^(3+i)H. The universal Koszul-square resolution of PR676, retaining its contraction and graded-Leibniz differentials, has global terms

    C0=Sym^2 G0 tensor Sym^3 H,
    C1=G1 tensor G0 tensor Sym^2 H,
    C2=(Lambda^2 G1 direct-sum G2 tensor G0) tensor H,
    C3=G2 tensor G1.

Tensor all terms with the fixed inverse determinant det(U)^(-1)det(H)^(-1), omitted from notation only because its character is trivial. The exact sequence is 0 -> C3 -> C2 -> C1 -> C0 -> R -> 0, with R=H0(sp(E)(4)). Its final map sends cubic-weighted symmetric generators to the determinant-skew transvections. This is a canonical polynomial prescription for every map and every relation, not an unevaluated rank hypothesis.

Apply the exact functor Phi(M)=Hom_Gamma(P2,M_+), where M_+ denotes its center-even summand. The projection of an arbitrary parameter-linearized tensor T is the Reynolds operator

    Re(T)(p)=1/|Gamma| sum_g g T(g^(-1)p).

If the natural iota-even summand has not already been retained, compose with (1+iota)/2. Exactness follows by averaging any preimage; polynomial parameter degree is unchanged. Therefore the COMPLETE family presentation is

    0 -> C^6 -> C^103 -> C^744 -> C^1850 -> F -> 0,
    dim F=1203.

The 1850 generating coefficients have precisely a 647-dimensional relation image, with the complete higher relations supplied by the preceding maps. None of these maps is the differential of the actual monad-source equation; they describe the middle bundle globally before those equations are imposed.

For reproduction, the positive character multiplicities in the order (1,A,V,P,D) are

    C0: (59,188,181,249,308), dimension3702;
    C1: (27,72,79,97,124), dimension1488;
    C2: (7,7,18,10,17), dimension207;
    C3: (1,0,2,0,1), dimension12;
    R+: (38,123,118,162,200), dimension2409.

The full R dimension is4755; its negative dimension is2346. Every negative irreducible is center-odd and hence has zero Hom from P2. This explains the absence of an extra independent parity cut.

## 3. Exact vertex preservation with no hidden cokernel

Let Z=P(W*) be the whole negative vertex line. Put B=U tensor Lambda^2 V and C=U tensor V tensor det W. Both have representation U tensor V, dimension6. PR676 proves restriction R -> R_Z is onto, by restricting the globally generating Koszul sections and multiplying binary forms. Its three blocks are

    Sym^2 B tensor H0 O_Z(5),
    B tensor C tensor H0 O_Z(4),
    Sym^2 C tensor H0 O_Z(3).

The first and third blocks are center-odd. The middle is center-even, with representation

    (R_Z)+ = (U tensor V)^2 tensor D
             =3·1+9A+9V+12P+15D, dimension180.

Since taking Gamma-equivariant parameter families is exact, vertex restriction has no additional source-weight or symmetry cokernel:

    0 -> F_Z -> F -> Hom_Gamma(P2,(R_Z)+) -> 0,
    dimensions 1113 -> 1203 -> 90.

In particular every prescribed equivariant center-even polynomial vertex middle value of degree (2,1) lifts globally, and the lifts form a torsor for the1113-dimensional kernel. This conclusion concerns a prescribed middle value, not a prescribed entire cochain defect.

The kernel has positive representation35·1+114A+109V+150P+185D. An exact generator-and-relation presentation for it is obtained without a new basis: let Q be the composite C0 -> R -> R_Z and C0^Z=ker Q. Then

    0 -> Phi(C3) -> Phi(C2) -> Phi(C1)
      -> Phi(C0^Z) -> F_Z -> 0,

with dimensions6,103,744,1760,1113. Here Q is explicitly restriction of cubics and contractions followed by the binary multiplication maps above. Thus the zero-vertex constraint is a canonical kernel of a specified universal map, not an actual HM coefficient test. Cokernel zero follows from the proved restriction surjectivity, not dimension subtraction alone.

## 4. Structural consequence and remaining gate

Only the center-even global sector can occur in the actual degree(2,1) family. The entire2346-dimensional opposite sector cannot contribute to the required mixed functional through such a family. Within the surviving1203 parameters, imposing any admissible vertex value leaves1113 exact middle-operator degrees of freedom, with no equivariance obstruction at the vertex.

This does NOT prove that these1113 directions span the simultaneous ramification-value target, nor that any satisfies the source-arrow equations. Even the vertex-cubic generators in PR676 must be Reynolds-projected before they can be used here; their unrestricted pointwise spanning does not survive averaging automatically. The remaining actual problem is the image of this explicit1203-dimensional quotient (or the1113-dimensional affine-direction space after fixing the vertex) under the mixed functional AND the coupled monad-source equations. There is no fourth-Bockstein evaluation, higher-order lifting theorem, algebraicity assertion, or selected actual-instance calculation here.

## Public dependencies and verification

- PR676 complete global presentation: https://github.com/Akilleez-QA/read-em-and-weep/blob/b7fd2c946b39301bdb226af362674e1b2e755097/research/hm/global-skew-middle-presentation/PROOF.md
- Fixed H=V+W, U=Wprime and intrinsic determinant line: https://github.com/Akilleez-QA/read-em-and-weep/blob/8d8b5be4ce62c3055bb53be9e16d29cc63072f04/research/hm/order-four-quadratic-load/UNIVERSAL-MONAD-CLIFFORD-HOMOTOPY-AND-HAMILTONIAN-DEFECT.md
- Actual U=Wprime, linear Z_a=k e_a, fixed duality and physical positivity: https://github.com/Akilleez-QA/read-em-and-weep/blob/3333cce744b3bd8e4472969f599588fec3e20d52/research/hm/order-four-quadratic-load/ACTUAL-MULTIPLIED-NILPOTENT-HAS-A-CANONICAL-SQUARE-ZERO-LIFT.md
- Actual primitive equation and global-cochain existence: https://github.com/Akilleez-QA/read-em-and-weep/blob/2e20281e6eb850904093af3a6c737f3ee0ed28f2/research/hm/order-four-quadratic-load/ACTUAL-FOURTH-BOCKSTEIN-AS-A-FIFTH-NEIGHBORHOOD-ADJOINT-BOUNDARY.md
- Physical coordinate inversion versus the additional Serre involution: https://github.com/Akilleez-QA/read-em-and-weep/blob/8d8b5be4ce62c3055bb53be9e16d29cc63072f04/research/hm/order-four-quadratic-load/ACTUAL-LOWER-COHOMOLOGY-SERRE-INVOLUTION-SPLITTING.md
- Fixed tensor and determinant conventions: https://github.com/Akilleez-QA/read-em-and-weep/blob/8d8b5be4ce62c3055bb53be9e16d29cc63072f04/research/hm/order-four-quadratic-load/UNIVERSAL-CARTAN-KOSZUL-MULTIPLIER-HOMOTOPY.md

Run python verify.py. This uses the nine abstract conjugacy classes and exact Q(sqrt5) arithmetic, Newton identities and character inner products. It verifies every displayed character multiplicity and family dimension. It does not evaluate actual coefficients, points, maps, ranks or monad equations. Geometric exactness is proved above using the pinned resolution and restriction theorem, not by the script. Not proof-assistant formalized.
