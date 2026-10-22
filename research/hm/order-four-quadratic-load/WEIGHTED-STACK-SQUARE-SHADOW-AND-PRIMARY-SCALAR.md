# The weighted-stack square shadow and a forced primary scalar

## New conclusions

Let X=P_stack(1,1,2,2), with coarse map pi:X->Q0, and let L and C0 be the negative vertex and invariant positive conic. Write O(1)=O_wt(2) for the ordinary hyperplane twist, S_hat=O_wt(1), E_hat=pi*F_Q0(2), and G=E_hat tensor S_hat^(-1).

The actual coarse saturated spinor map lifts uniquely to a regular section sigma of G. Its zero scheme Z is a codimension-two local complete intersection on the smooth stack, supported over C0 union L. There is an exact sequence

    0 -> G(2) -> pi*B_Q0(4) -> I_Z^2(6) -> 0.      (1)

The square is the ordinary square on the stack. Its coarse pushforward must not be replaced by the square of the coarse Ext-annihilator ideal.

Set Qsq=pi_*(I_Z^2(6)) and P=pi_*G(2)=F_Q0 tensor S(3). The only possible positive cohomological obstruction to lifting a square-shadow section is one P4:

    H0(P)_+ = A+D5, H1(P)=0,
    or
    H0(P)_+ = A+P4+D5, H1(P)=P4.                  (2)

Using the independently proved invariant-cone rank33, only the first alternative occurs. Hence the previously undecided P4 scalar in the primary spinor-resolution map is nonzero. Moreover

    H0(Qsq)_+=0, H1(Qsq)_+=P4, H^i(Qsq)_+=0 (i>=2).

Equivalently ordinary positive sextics inject into the square-thickening sections, with exact four-dimensional P4 cokernel:

    0 -> H0(O_Q0(6))_+ -> H0(pi_*O_(2Z)(6))_+
      -> P4 -> 0,                                (3)

of dimensions 72,76,4. These are consequences of the now-proved rank33, not an independent proof of that rank and not a proof that the later smoothing scalar gamma is nonzero.

## 1. Lifting the coarse spinor without an invalid pullback

The naive pullback pi*S need not be the invertible S_hat at the vertex. We do not use that assertion. Instead

    pi_*S_hat=S, pi_*S_hat^(-1)=S*=S(-1).

The identities follow directly from the even and odd weighted modules; on a negative affine chart they are the even and odd modules for the cover C[a,b] over C[a^2,ab,b^2]. Since E is locally free,

    Hom_Q0(S,E)=H0(E tensor S*)
              =H0(X,E_hat tensor S_hat^(-1)).

Thus the actual inclusion gives a unique sigma. On a vertex chart, the residual stabilizer mu2 acts by (a,b)->(-a,-b). E_hat has trivial stabilizer character and S_hat has the sign character, so sigma is locally a pair of odd functions. This local mu2 parity is distinct from the physical inversion parity on global sections, which will always be denoted by a subscript + or -.

Away from L the coarse map is an isomorphism and the established defect support is C0 union L. Consequently sigma has no zero outside this union; it vanishes over L because its stabilizer character is odd, and has the reduced conic zero scheme near C0. Its zero set has pure codimension two. In a smooth three-dimensional stack chart, its two local components therefore have height two and are a regular sequence. This proves regularity everywhere, not merely at the generic vertex.

The determinant is det G=O(2), since det E_hat=O(3) and S_hat^2=O(1). Its section sequence is

    0 -> O_X -> G -> I_Z(2) -> 0.

Tensoring by S_hat and pushing to the coarse space recovers

    J=pi_*(I_Z S_hat(2)),
    T=pi_*(O_Z S_hat(2)).                          (4)

The pushforward is exact: locally it takes invariants under the finite group mu2 in characteristic zero. This is a stack ideal description, not an ordinary ideal-times-spinor description on the singular coarse space.

## 2. The ordinary square is the exact lower-component shadow

For a regular section of a rank-two bundle, its symmetric-square sequence is

    0 -> G --multiply by sigma--> Sym^2G
      -> I_Z^2 tensor (det G)^2 -> 0.

Locally this is the usual two-syzygy resolution of the square of the regular ideal (f,g). Twisting by O(2) gives (1), because

    Sym^2G(2)=Sym^2E_hat(1)=End_0(E_hat)(4).

For a tracefree endomorphism, the quotient is its lower component relative to the section line. In a local trivialization it is, up to an invertible factor,

    beta f^2-2 alpha f g-gamma g^2.

This proves that global square shadows exactly measure nonpreserving adjoints. In particular the kernel on global sections is precisely the filtration-preserving adjoint space, not just its nilpotent subspace.

At a vertex the even invariant part of (f,g) is (f,g)B_odd, namely the coarse Ext-annihilator I_e. Therefore

    pi_*O_Z=O_Q0/I_e.                              (5)

However pi_*(I_Z^2) is generally larger than I_e^2: its even elements include f^2, whereas f times an odd generator is needed even to enter I_e. Keeping these two ideals distinct is essential.

## 3. The primary kernel cohomology has only one undecided channel

Projection formula gives P=E tensor S(1)=F_Q0 tensor S(3). Tensor the ambient spinor resolution by F(3):

    0 -> W' tensor F(2) -> W' tensor F(3)
      -> i_*P -> 0.                               (6)

The actual primary cohomology is

    H0(F(2))=0, H0(F(3))=P4,
    H1(F(2))=1+A+T6, H1(F(3))=W,

with no higher cohomology in these twists. The character identities are

    W' tensor T6=A+P4+D5,
    W' tensor P4=W+T6,
    W' tensor A=T6, W' tensor W=P4.

Thus the positive H1 map in (6) is a single scalar lambda on P4; every other positive constituent maps to zero. It follows that

    H0(P)_+=A+D5+ker(lambda:P4->P4),
    H1(P)=coker(lambda:P4->P4),
    H0(P)_-=W+W'+2T6,
    H^i(P)=0 for i>=2.                            (7)

This proves (2), with both possible outcomes retained until additional geometry is applied. The long exact sequence of (1), after coarse pushforward and taking physical inversion-even parts, identifies the actual nonpreserving quotient with

    ker[H0(Qsq)_+ -> H1(P)_+].                     (8)

The target in (8) is either zero or one P4. In particular every non-P4 isotypic square-shadow section automatically lifts, before knowing lambda.

## 4. Consequences of the independently established rank33

The two independently proved cone results, NO-PRESERVING-POSITIVE-CONE-EXCESS.md and POSITIVE-CONE-MOVING-LINE-OBSTRUCTION-VANISHES.md, give

    H0(B_Q0(4))_+=A+D5,
    H1(B_Q0(4))_+=P4,
    H^i(B_Q0(4))=0 for i>=2.

The last two assertions also follow from the ambient multiplication block after its rank is33, with source and target dimensions41 and37 and the established ambient cohomology concentration.

Since H0(P)_+ injects into this eight-dimensional adjoint space and already contains A+D5, (7) forces lambda nonzero. Therefore H1(P)=0. Exactness of (1) now proves the stated cohomology of Qsq. Combining this with

    0 -> Qsq -> O_Q0(6) -> pi_*O_(2Z)(6) -> 0

gives (3). The positive sextic dimension is

    13 + 9*3 + 5*5 + 7 =72,

coming respectively from negative-coordinate degrees 0,2,4,6 in the weighted polynomial model. Also H1(pi_*O_(2Z)(6))_+=0.

The forced primary scalar and the exact square-shadow obstruction P4 are new consequences of the cone closure. They do not identify gamma: gamma concerns deformation away from the cone, whereas (1)-(8) describe the exact cone fiber.

## 5. The first thickening retains both parity quotients

Regularity gives I_Z/I_Z^2=G*|Z. Twisting the first-thickening sequence by O(6) and using (4)-(5) gives the exact coarse sequence

    0 -> E tensor T(1) -> pi_*O_(2Z)(6)
      -> (O_Q0/I_e)(6) -> 0.                      (9)

Indeed G*=E_hat* S_hat=E_hat S_hat(-3), so its twist by six is E_hat S_hat(3), whose restriction to Z pushes to E tensor T(1).

At the generic vertex, the odd complete intersection has a regular initial pair of degrees3 and5. Its square has Hilbert series

    [1-z^6-z^8-z^10+z^11+z^13]/(1-z)^2.

The total length is45, with even length22 and odd length23. In particular the generic even square-thickening length22 is the sum of the Ext quotient length8 and twice the odd defect length7, exactly as (9) predicts. The square target cannot be replaced by the length8 quotient or the length7 spinor defect.

The Hilbert series uses only the regular initial pair; powers retain the initial complete-intersection filtration because the regular-sequence Rees filtration is flat. Alternatively the lengths and parity difference follow directly from the square resolution of two odd generators.

## 6. A global conormal cohomology calculation

The unique actual vertex module has pushforward

    D=A O_L(2) plus B1 plus B2,
    B1=B2=W' O_L(2),
    B2 -> A O_L(2) -> B1 -> 0.

Its generic collective action maps onto A and B1. These maps are onto everywhere: their possible degeneracy divisors are G-invariant, while a nonzero maximal minor has degree at most3, respectively2. A nonempty invariant divisor on L has degree at least12. Consequently the actual global Loewy graded pieces are

    gr T_L = W'O_L(2), A O_L(2), W'O_L(2).         (10)

Tensoring this filtration by the locally free E(1), and using the actual equivariant splitting E|L=O_L(5)+O_L(-2), gives positive graded pieces

    2 W' O_L(1) plus A O_L(8).

All line degrees in both parities are1 or8, so H1(E tensor T_L(1))=0. Its positive H0 is

    2P4 plus A tensor Sym^8W
      = A+2V+4P4+2D5, dimension35.                (11)

The conic contribution to E tensor T(1) is W O_P1(10), entirely inversion-odd. It has no H1. Thus (11) is also the complete positive conormal contribution in (9), and H1(E tensor T(1))=0 globally.

Using (3), (9), and (11), one obtains

    h0((O_Q0/I_e)(6))_+=76-35=41,
    H1((O_Q0/I_e)(6))_+=0.

The conic summand contributes13 positive sections. Hence the vertex Ext quotient has exactly28 positive sections at twist six and no positive H1. These are cohomological consequences, not an assumption about a reduced vertex scheme or a global pair of generators.

## Scope and evidence

Inputs: the actual cone spinor filtration; reduced-conic first-jet theorem; vertex support; unique three-step module; generic odd (3,5) complete intersection; and the independently proved rank33 closure. No actual coefficient, selected matrix, or experiment is used. The companion verifier checks universal characters, ordinary-square Hilbert coefficients, parity lengths, and the dimension deductions. All stack stabilizer invariants and physical inversion signs are kept separate.
