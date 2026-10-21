# Forced square survivors on every hyperplane of the negative pencil

## Theorem and correction

Let F be normalized Horrocks–Mumford on P4, R=P(V_+) its positive fixed plane, W=V_-*, and H_lambda=P(V_+ directsum lambda) for lambda in P(W*). Put E_lambda=F|H_lambda and B=End_0(F).

The actual pencil satisfies

    h0(E_lambda(2))=2 for EVERY lambda,

and these sections are all inversion-even in the normalization in which F_R is inversion-even. Their three quadratic products give independent even adjoint sections:

    Sym^2 H0(E_lambda(2)) injects into H0(B|H_lambda(3))_+.

They restrict injectively to the plane section space H0(B_R(3)) and survive every normal-neighborhood obstruction. In particular the actual secondary root map beta_lambda:9->15 has

    dim ker beta_lambda >= 3,
    rank beta_lambda <= 6 for EVERY lambda.             (1)

The two-root secondary odd operator Delta_q:18->30 therefore has kernel dimension at least six for every nondegenerate q_-. The previously mentioned conditional route through rank(beta)=9 is impossible and is withdrawn as a candidate. None of this proves a nonzero odd adjoint section on the distinct quadric Q: later fixed-quadric lifting compatibility can still eliminate these finite scaling survivors.

The surviving bundles are explicit:

    Y=pi_*E_lambda(2)=ker[D tensor O -> A tensor O(2)]
      = W tensor O(-3),
    Sym^2 Y=A tensor O(-6) subset ker beta subset K.

Here K has rank nine and degree minus twelve. Thus beta factors through the rank-six, degree-six quotient K/Sym^2 Y. Its rank on that quotient is not determined.

## 1. Independent primary-literature obstruction

Bănică–Manolache prove that every stable rank-two bundle E on P3 with Chern classes (-1,4) has H0(E(2)) nonzero: INCREST Preprint 104/1981, §1.1, Lemma 1, printed p.3 (PDF p.7).

https://imar.ro/~increst/1981/104_1981.pdf#page=7

Ellia–Gruson restate this general result as Lemma 6.3, p.77 (PDF p.13), giving h0(E(2))=h1(E(2))>0. There is no additional instanton or Buchsbaum hypothesis in the recalled lemma.

https://rendiconti.dmi.units.it/volumi/47/006.pdf#page=13

Boralevi records stability of every HM hyperplane restriction, so the result applies to the actual bundle. It already rules out complete cubic trace-free-endomorphism vanishing on any HM hyperplane. The stronger exact dimension two in this fixed pencil is proved independently below from actual cohomology and the normal extension.

## 2. Restriction to the fixed plane is injective

The actual stable Steiner resolution is

    0 -> A tensor O_R(-3) -> D tensor O_R(-2) -> F_R -> 0,
    dim A=3, dim D=5.

It gives H0(F_R(k))=0 for k<=1 and H0(F_R(2))=D. For E=E_lambda, the hyperplane sequences inside H_lambda give

    0 -> E(k-1) -> E(k) -> F_R(k) -> 0.

For k<=1, H0(E(k-1))->H0(E(k)) is therefore an isomorphism. Descending to sufficiently negative k, where any vector bundle has no sections, proves H0(E(1))=0. Consequently

    H0(E(2)) -> H0(F_R(2))=D                           (2)

is injective. Inversion acts as the positive scalar on F_R(2), so every section in (2) is positive. This step does not require a generic hyperplane or an unproved restriction theorem.

## 3. Actual parity gives a lower bound two

The established actual HM primary cohomology is

    H0(F(1))=H0(F(2))=0,
    H1(F(1)) parity=(4+,6-),
    H1(F(2)) parity=(4+,6-).

These signs use the normalization F_R positive. Equivalently both ten-dimensional H1 groups have trace -2; changing the scalar lift changes the corresponding labels consistently and does not change the dimension argument or any square-section parity.

Let ell be the odd linear equation of H_lambda. The actual restriction sequence

    0 -> F(1) tensor <ell> -> F(2) -> E(2) -> 0

identifies its positive global sections with the kernel

    H1(F(1))_- tensor <ell> -> H1(F(2))_+,
    dimensions 6 -> 4.

Hence h0(E(2))>=2. No surjectivity of this multiplication map has been assumed, and no irreducibility is assigned to either of these parity spaces.

## 4. The actual first normal vector-bundle boundary gives the upper bound

The projective second-normal class is the proved nonzero actual zeta. On the direction lambda, its coefficient lies in

    H1(B_R(-2)) subset H1(End(F_R)(-2))

and acts on D=H0(F_R(2)) by the actual boundary

    y_lambda:D -> H1(F_R)=A tensor (lambda*)^2.         (3)

This is not an assumed lift of a projective class. The scalar part has H1(O_R(-2))=0, so the vector-bundle extension class lifting zeta(lambda) is unique in cohomology. The preceding first-normal comparison also has no scalar ambiguity, since H1(O_R(-1))=0. Taking inversion invariants in the actual third normal neighborhood of R in H_lambda yields an extension

    0 -> F_R tensor (lambda*)^2 -> J_lambda -> F_R(2) -> 0

whose boundary is exactly (3). The dual Steiner sequence identifies H1(End(F_R)(-2))=Hom(D,A), so the action on sections is that same coefficient map.

The earlier actual cup proof identifies D with Sym^2_0 A, and the unique actual A-channel with

    y_a(S)=S a,  a!=0.

The coefficient is nonzero for every direction because zeta identifies (Sym^2 W)* with its irreducible A-summand. The universal linear-algebra proof shows y_a is surjective for every nonzero a, including isotropic a. Therefore ker(y_lambda) has dimension two.

Every global E(2) section restricts to a section extending over that normal neighborhood. Its image in (2) lies in ker(y_lambda), giving h0(E(2))<=2. Combined with Section 3 this proves

    H0(E_lambda(2)) = ker(y_lambda),  dimension two.    (4)

In particular all first-normal kernel sections in this case do extend globally; that conclusion follows from the two independent bounds, not from formal lifting alone.

## 5. Exact linearization and three independent squares

For a rank-two bundle, the determinant pairing gives

    End_0(E)(3)=Sym^2(E) tensor (det E)^(-1)(3).

The isomorphism det E=O_H(-1) has no extra inversion sign. On the fixed plane the involution is scalar on E, so its determinant acts positively; the standard O_R(-1) also acts positively. This checks the possible character discrepancy directly. Equivalently, the full binary normalizer is perfect, so its linearizations differ by no nontrivial character. Therefore the identification

    B|H(3)=Sym^2(E(2))                                 (5)

is equivariant. All products of the two positive sections of (4) are even.

They are independent. Indeed, their plane restrictions are the symmetric square of a two-dimensional subspace Y_lambda of D, and the actual Steiner calculation identifies

    Sym^2 D = H0(B_R(3)).

Thus Sym^2 Y_lambda injects with dimension three. Their global restrictions cannot have a relation which is absent on R. Alternatively, a constant quadratic relation between two independent sections factors over C into linear factors; evaluation at the generic point of the integral H would force one constant linear combination to vanish, a contradiction.

These are actual global hyperplane sections. Hence they lift through the fifth normal neighborhood defining beta and through the seventh normal neighborhood defining the later gamma boundary. This proves (1) and

    dim ker(gamma_lambda) >= 3.

The actual ambient odd-linear 44->46 multiplication pencil therefore has kernel dimension at least three on every member.

## 6. The surviving section and square bundles

On P(W*), the actual family has constant h0(E_lambda(2))=2. Cohomology and base change, together with (4), identify its rank-two section bundle with

    0 -> Y -> D tensor O -> A tensor O(2) -> 0.         (6)

The coefficient map is pointwise surjective, so Y is locally free and deg Y=-6.

There is a universal binary-form description. The invariant identifications are A=Sym^2 W and D=Sym^4 W. Up a single nonzero scalar, y_lambda is contraction of a binary quartic twice by the direction lambda, equivalently the second transvectant with its squared direction after identifying W with its dual using the determinant form. This follows from the SO(A)-equivariant map Sym^2_0 A tensor A -> A, and does not select HM coefficients.

Let L_lambda be the line in W annihilating lambda. In characteristic zero, a homogeneous quartic has zero second directional contraction precisely when it is divisible by L_lambda cubed. Thus

    ker(y_lambda)=L_lambda^3 tensor W.

The annihilator lines form O(-1) tensor det W; det W is equivariantly trivial for the binary normalizer. Hence

    Y=O(-3) tensor W,
    Sym^2 Y=O(-6) tensor Sym^2 W=O(-6) tensor A.        (7)

Multiplication of the global family sections gives a fiberwise injective bundle map Sym^2 Y -> K, and its image lies in ker beta by Section 5. Since it has constant rank three, the quotient

    Q_6=K/Sym^2 Y

is a vector bundle of rank six and degree (-12)-(-18)=6. The secondary boundary factors as

    K -> Q_6 --beta_bar--> H1(B_R(-1)) tensor O(4).    (8)

No maximal-rank assertion for beta_bar is made.

One may identify the quotient without choosing a splitting of D. The first-cup proof gives the universal maps sigma_y and psi_y, with im(sigma_y)=ker(psi_y), and the injective actual Steiner map phi. It gives

    Q_6 = ker[ (wedge^2 A tensor V) tensor O(2)
                --psi_y phi--> wedge^2 A tensor O(4)]. (9)

The last arrow is onto by the same actual Steiner fiber-injectivity argument used for first-cup surjectivity. Formula (9) retains its parameter twists and reproduces rank six and degree six.

## 7. Correction to the secondary route and remaining distinction

The exact operator Delta_q and its two-root description remain valid. What changes is the possible rank: the rank-nine-injectivity route is ruled out. If r denotes the generic rank of beta, then

    0<=r<=6,
    dim ker Delta_q=18-2r>=6

for general negative blocks, with at least six survivors for every nondegenerate block. The previously proved generic upper bound for global odd quadric sections remains 18-2r; an upper bound of six when r=6 is NOT a lower bound of six on those global sections.

The forced survivors are global sections on two DIFFERENT hyperplanes. They need not satisfy the higher parameter-lifting and mixed normal compatibility required on the actual quadric. No odd-quadric nonvanishing, smooth determinant cubic, three-conic section, or classification of all cubic adjoints is inferred. In particular h0(E(2))=2 does not imply that all of H0(B|H(3)) consists of the three squares.

The primary-literature obstruction and the exact HM-pencil argument therefore prune an impossible secondary-injectivity route while leaving the actual quadric question open.

## Source interfaces

The primary literature is cited in Section 1. The actual primary parity inputs are proved in LOWER-TWIST-EVEN-QUADRIC-PARITY.md and the inversion notes. The genuine A and V distinction, plane Steiner cohomology, and coefficient identifications are proved in the fixed-plane notes. ACTUAL-AMBIENT-SECOND-NORMAL-NONVANISHING.md is published at b3fc992ebba27fc28967f934bf9966148eb86961. ODD-FIRST-SCALING-OBSTRUCTION.md proves y_a surjectivity and the actual Leibniz cup formula. ODD-SECOND-SCALING-OBSTRUCTION.md defines beta, K, gamma, and the two-root secondary operation.

No selected HM coefficients or source-instance rank evaluations are used. The binary contraction statement is a universal polynomial identity, not a source-instance computation.
